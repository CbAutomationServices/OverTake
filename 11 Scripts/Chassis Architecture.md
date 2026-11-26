---
system: Vehicle Chassis
status: draft
owner: Cristian
last-updated: 2026-11-25
---
> **Status:** 🟡 Draft. Step 1 of 3 (architecture & math). Nothing here is final until marked 🟢 Locked.

# Chassis Architecture (Step 1)

Our own arcade chassis (decided 2026-11-19), built so every car feels different from data alone. Links: [[Architecture]] · [[Car Stats]] · [[Car Model Spec]] · [[Performance Rating]] · [[Tuning]] · [[Part Levels]]

## 1. The big picture

```
ReplicatedStorage/Shared/Chassis
├─ ChassisSim          pure math: step(state, input, config, dt) → forces. Same code on client + server
├─ ChassisController   owns one car: raycasts, applies forces, exposes telemetry
├─ CarConfigs/<CarID>  one module per car: its "DNA" (stock + elite values)
├─ StatResolver        config + part levels + tuning → the live numbers the sim uses
└─ PR                  (already planned) same function in garage UI + server
StarterPlayerScripts
├─ InputController     Input Action System: Throttle, Brake, Steer, Handbrake, Nitro, Shift
├─ CameraRig           FOV, look-ahead, shake (reads telemetry)
└─ CarFX               body roll/pitch, wheels, smoke, skids, backfire, blow-off (reads telemetry)
ServerScriptService
├─ VehicleService      spawn, seat, network owner / authority, respawn after part swaps
└─ VehicleGuard        speed / teleport / checkpoint sanity checks
```

**Rule:** the physics never reads a hard-coded number. Everything comes from `StatResolver`, which reads the car's config, its installed parts and its tuning.

## 2. Physics model: raycast "hover" chassis (recommended)

**One rigid body.** The car is a single invisible box (`Root`) with real mass. Body and wheels are welded, Massless, CanCollide off, purely visual. No wheel constraints, no hinges.

**Why not constraint wheels (HingeConstraint / CylindricalConstraint cars)?**
- Wheel-to-ground contact at 150+ mph jitters, bounces on part seams, and explodes on curbs. We have thousands of road segments, so seams are everywhere.
- Grip comes from Roblox friction, which we can't shape into a drift curve.
- Several assemblies per car means more to replicate and more to break.

**Per wheel, every simulation step (4 wheels):**
1. **Suspension:** a spherecast (radius = wheel radius × 0.6) from the wheel's top mount, straight down along the car's −Up, length = rest length + travel. A sphere instead of a thin ray, so it doesn't fall into seams between road parts.
2. **Spring-damper:** `compression = restLen − hitDist`; `Fs = k·compression − c·(compression velocity)`, clamped ≥ 0, pushing along the car's Up at that wheel.
3. **Tire forces:** from the contact point's velocity split into forward (`vLong`) and sideways (`vLat`) along the wheel's heading (front wheels rotated by the steer angle):
   - **Lateral:** `Flat = −sign(vLat) · μlat(slip) · load` (curve in §4)
   - **Longitudinal:** drive force (from the engine, §5) on driven wheels, brake force on all, rolling resistance
   - Combined with a **friction circle**: if `|Flong, Flat| > μ·load`, scale both down. This is what makes "too much throttle in a corner = rear steps out" work for RWD.
4. **Load:** each wheel's spring force is its tire load, so weight transfer happens on its own. Braking loads the front (more front grip = sharper turn-in); throttle loads the rear.

**Applying the forces:** sum the 4 wheels into one net force + torque about the center of mass, plus aero (downforce ∝ v², drag ∝ v²), then apply with `Root:ApplyImpulse` / `ApplyAngularImpulse` each fixed step. No VectorForce instances to manage, and it works under both network models below.

**Arcade helpers (all per-car config, so they also give each car its personality):**
- **Anti-roll / stability torque** so cars never flip from a curb (the "arcade glue")
- **Air control:** small pitch/roll correction in the air so you always land wheels-down
- **Downforce at speed** keeps 150+ mph stable on the freeway viaduct
- **Yaw damping** when the steering is centered, so the car settles after a slide

**Weight & inertia per car:** mass, center-of-mass height/offset (`CenterOfMass` is shifted with a hidden weighted part), plus a **yaw inertia multiplier** (heavy muscle = lazy rotation, light JDM = snappy). Spring rates and anti-roll scale with mass, so a heavy car squats and leans visibly more.

## 3. Networking: who runs the physics

Roblox now offers two models, and this design works with both because `ChassisSim` is pure math driven only by inputs:

| | **A. Driver owns the car** (start here) | **B. Server Authority** (test later) |
|---|---|---|
| How | Server gives the driver network ownership; the driver's device simulates; others see it smoothly interpolated | Roblox's new built-in mode (full release 2026): client predicts instantly, server is the truth, rollback + resimulation on mismatch |
| Feel | Zero input lag, buttery | Instant locally; may snap on bad 4G if a misprediction happens |
| Cheating | We must check (VehicleGuard: max speed per car/PR, teleport, checkpoint order, impossible acceleration) | Speed/teleport hacks impossible by design |
| Cost | Proven, simple | Needs Input Action System, `BindToSimulation`, fixed simulation, deferred signals. Roblox engineers say complex physics can still mispredict |

**Recommendation:** build A now (the fastest way to a car that feels great), but write the sim the Server-Authority way from day 1:
- Inputs come only from the **Input Action System** (already planned for phone / PC / gamepad)
- The step function runs at a fixed dt, uses no `tick()` or `os.clock()`, and keeps effects (sound, smoke, camera) out of the sim, in a separate RenderStepped layer

Then, once races exist, we flip a test server to B and drive it on the network simulator. If it feels good, competitive races get it for free anti-cheat.

**Cop cars:** server-owned, same `ChassisSim`, AI fills the input struct.

## 4. Grip, drift and the Grip ↔ Drift slider

**Slip angle** per axle: `β = atan2(|vLat|, max(|vLong|, 3))` (the 3 avoids nonsense at a standstill).

**Lateral grip curve** (per axle, per car):
```
μ(β) rises linearly to its peak at β_peak (≈ 6–10°),
then falls off to μ_slide (the "sliding grip") by β_slide (≈ 25°+)
```
- Grip car: high peak, gentle fall-off (forgiving)
- Drift car: lower rear peak, sharp fall-off, decent `μ_slide` (easy to hold an angle)

**Drift state machine (arcade "assisted" drift, like Heat):**
```
GRIP ──(entry trigger at speed > driftMinSpeed)──► DRIFT ──(β < exitAngle for 0.25s, or speed too low)──► GRIP
```
- **Entry triggers (per car, from config):** handbrake tap · brake-tap then steer + throttle (Heat style) · or a plain power-over on RWD (the friction circle does it naturally)
- **While drifting:**
  - Rear grip × `driftRearGrip` (e.g. 0.45), front keeps grip
  - **Angle holder:** a yaw torque pushes the car toward a target angle set by steering: `target = steer × driftMaxAngle`. Throttle widens, lifting tightens
  - **Counter-steer assist:** if β passes `driftMaxAngle` it adds opposite yaw (no spin-outs unless the car's config allows it)
  - **Speed keeper:** keeps part of the speed through the slide, so drifting isn't slower than gripping in arcade terms (`driftSpeedRetain`)
- **Exit:** blends grip back over `recoverTime` so the car doesn't snap

**Drivetrain DNA** comes out of the same math:
- **RWD:** drive force on the rear → friction circle → power oversteer. Lower `driftMinSpeed`
- **AWD:** drive split 40/60 front/rear → best launch, powerslides that pull straight
- **FWD:** drive on the front → understeer on power; lift-off oversteer via weight transfer; drift entry only by handbrake

**Grip ↔ Drift slider (tuning, decided):** one value 0–1 that blends the car's grip-set and drift-set values (rear peak μ, fall-off, `driftRearGrip`, angle-holder strength, steering lock). The same car can be a corner-carver or a smoke machine.

## 5. Engine, gears, turbo vs supercharger, nitrous

- **RPM** = wheel speed × gear ratio × final drive (clamped to idle…redline). Auto-shift by default (upshift at the RPM where the next gear makes more force); manual optional.
- **Torque curve:** 5–7 points per car (RPM → torque), smoothly interpolated. Muscle = big low-end; JDM = peaky top-end.
- **Drive force** = torque × gear × final drive × efficiency ÷ wheel radius, split to the driven wheels.
- **Top speed** comes naturally from drag (∝ v²) vs drive force, plus a soft limiter at the car's `vMax` so tuning can't break it.
- **Forced induction (one slot: turbo OR supercharger, decided):**
  - **Turbo:** boost builds with lag: `boost += (target − boost)·(1 − e^(−dt/τ))`, where τ = spool time (single turbo slow, twin faster). Bigger top-end. Blow-off sound on lift
  - **Supercharger:** boost ≈ instantly proportional to RPM (centrifugal = rises with RPM; roots = flat from low RPM). Whine sound
- **Nitrous** (per car + Nitrous part):
  - **Burst:** big force for a short time, high FOV kick
  - **Sustained:** smaller force for longer
  - Capacity, strength and refill rate (drift / near-miss / draft refill, from the Core Loop note) are all config values

## 6. How parts change the physics (upgrade hooks)

Every tunable stat in a car's config has a **stock** and an **elite** value. A part at level L (Stock 0% → Elite 100%, from [[Part Levels]]) interpolates only the stats its slot owns:

`live = stock + (elite − stock) × levelPct(slot)`, then tuning nudges, then hard caps.

| Slot | Stats it moves |
|---|---|
| Engine | torque curve scale, redline |
| Turbo / Supercharger | boost amount, spool τ (turbo), boost curve shape |
| Transmission | gear ratios spacing, shift time, final drive |
| Suspension | spring k, damping c, anti-roll, ride height, roll/pitch stiffness |
| Brakes | brake force, front/rear bias, ABS strength |
| Tires | μ peak, μ slide, β_peak, fall-off |
| Nitrous | capacity, strength, refill rate |

Because each car has its own elite values, **every car tops out differently** (a maxed muscle car is still a muscle car), which matches the PR rule that every car can reach Z but gets there its own way. PR stays the formula already in [[Performance Rating]]. The 4 garage bars (Speed, Accel, Handling, Nitro) are computed from these live numbers, so the bars always tell the truth.

## 7. Making it feel alive (telemetry → FX)

The controller publishes a telemetry table every frame:
`speed, rpm, gear, throttle, brake, steer, slipFront, slipRear, isDrifting, driftAngle, wheel compression ×4, contact material ×4, grounded, boost, nitroActive, longG, latG`

- **CarFX (visual only, never touches physics):**
  - Body roll from `latG × rollFactor` and pitch from `longG × pitchFactor` through a little spring, so it overshoots and settles
  - Wheels: steering lock, spin from speed, suspension travel from compression, visual camber
- **CameraRig:**
  - FOV 70 → 90 with speed; nitro adds a kick + pull-back
  - Drift look-ahead (yaws the camera toward where you're going, by driftAngle)
  - Boost shake; tiny road rumble scaled by speed; landing thump
- **Triggers:**
  - Smoke + skidmarks when slip > threshold (rear on RWD drifts)
  - Exhaust pops on upshift and lift-off at high RPM
  - Turbo blow-off on throttle lift with boost > 50%
  - Nitro flames at the `Exhaust_L/R` attachments

## 8. Model rig standard (extends [[Car Model Spec]])

The physics measures wheels straight from the model, so the 3D model and the raycasts always match:
- `Root` (= the prompt's ChassisRoot): footprint box. The chassis reads wheel mount points from the **wheel model centers** in `Wheels/FL FR RL RR`
- **New for the chassis:** each wheel gets a `Knuckle` attachment (steering pivot). Optional swap sockets go in a `Sockets` folder of attachments: `FrontBumper, RearBumper, Spoiler, Hood, Skirts, Exhaust`
- Wheelbase, track width, wheel radius and ride height are therefore **measured, not typed**, and the registry records them for the orthographic sheets

## 9. Vehicle Design Registry (set up in Step 2)

One note per car in `02 Cars/Roster/`, plus a master table in `_Car Index`:
- Identity & role, tier range (C → Z), drivetrain, archetype, and how it contrasts with the cars already registered
- The handling DNA (the config values, in plain words)
- Studs blueprint: length, width, height, wheelbase, front/rear track, wheel radius, ride height / fender gap
- Rig checklist + a 4-view orthographic concept prompt (front, side, rear, top; flat background, neutral light; no real brands)

## Open questions (asked 2026-11-25)
- [ ] Default feel: grip-first with assisted drift (Heat) or drift-happy (Underground)?
- [ ] Drift entry: brake-tap, handbrake, or both?
- [ ] Which archetype is the hero starter car for Step 2?
- [ ] Phone controls: auto-accelerate option, or always manual?
