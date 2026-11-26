---
system: Car
car-id: Hayate
roster-slot: 1
status: draft
owner: Cristian
last-updated: 2026-11-25
---
> **Status:** 🟡 Draft. Prototype for **Starter A (JDM)**. Final starter names/models are still decided last (decision 2026-11-20); this is the car we build the chassis around.

# Hayate GT (working name) · Vehicle Design Sheet

Config: `ReplicatedStorage/Shared/Chassis/CarConfigs/Hayate` · Architecture: [[Chassis Architecture]] · Registry: [[_Car Index]]

## 1. Identity & role
| | |
|---|---|
| Roster slot | #1 · Starter A · free pick ([[Car Stats]]) |
| Category | JDM / tuner |
| Archetype | **Agile JDM Corner Carver** |
| Drivetrain | **RWD** |
| PR | Base **70 (C)** → Max **450 (Z)** |
| Tier path | Stock C · Street C · Sport B · Race A · Pro SS · Elite Z ([[Performance Rating]] example) |
| Garage bars (stock, estimate) | Speed 30 · Accel 35 · Handling 55 · Nitro 35 |
| One-line feel | Light, eager, rotates on a dime. The easiest car in the game to drift, but it runs out of steam on long straights. |

**Contrast with the registry** (first car, so contrast is with the planned starters):
| | Hayate (A, JDM) | Starter B, Muscle (planned) | Starter C, Euro (planned) |
|---|---|---|---|
| Weight | Light (1,150 kg) | Heavy | Medium |
| Drivetrain | RWD | RWD | AWD or FWD |
| Power | Peaky top end, weak low end | Huge low-end torque | Smooth, flat |
| Corners | Snappy turn-in, easy drift | Lazy turn-in, big power slides | Planted, grippy, safe |
| Straights | Weakest | Strongest | Middle |
| Who picks it | Players who want to drift and dance through the city | Drag + freeway players | New players who want stable |

## 2. Handling DNA (what the config does, in plain words)
- **Weight & inertia:** light, low center of mass, 52/48 front/rear. Yaw inertia 0.85, so it changes direction fast. The body visibly rolls and pitches (FX roll 1.1) because it's soft on stock suspension.
- **Grip vs drift:** decent grip peak (1.05 front / 1.0 rear on stock tires), with a gentle fall-off. Drifts start from 32 mph with brake-tap, handbrake, or just too much throttle mid-corner. While sliding the rear keeps 40–62% grip (by tuning slider), the angle holder is strong and counter-steer assist is 0.7, so it holds an angle without spinning.
- **Powerband:** inline-4, 205 Nm stock with the torque peak at 5,600 rpm and a 7,600 redline (8,800 on Elite). Weak below 3,000 rpm, so you keep it high in the revs. Six gears, short final drive.
- **Forced induction:** stock is naturally aspirated. The Turbo slot is where it comes alive: a single turbo spools in 1.2 s (0.6 s Elite) with a big top-end kick and blow-off pops. Twin turbo spools faster. A supercharger gives instant boost but less of it.
- **Nitrous:** Burst style, short and strong (2.5 s stock → 5.5 s Elite), with a 12° FOV kick.
- **Top speed:** soft limit 128 mph stock → 205 mph Elite.
- **Upgrade personality:** Tires and Suspension pay off the most on this car (it's a handling car). Engine and Turbo turn it from a slow toy into an A/S-tier contender.

## 3. Blueprint specs (studs) · model must match
1 stud ≈ 0.28 m. Front faces **−Z**, pivot at ground level, center of the car ([[Car Model Spec]]).

| Measurement | Studs | ≈ Real |
|---|---|---|
| Overall length | **15.6** | 4.37 m |
| Overall width (no mirrors) | **6.6** | 1.85 m |
| Overall height | **4.4** | 1.23 m |
| Wheelbase | **9.0** | 2.52 m |
| Front track (wheel center to center) | **5.5** | 1.54 m |
| Rear track | **5.6** | 1.57 m |
| Wheel radius (tire outer) | **1.15** | 0.32 m (≈17″ wheel) |
| Tire width | **0.75** | 0.21 m |
| Ride height (ground → bottom of skirt) | **0.55** | 15 cm |
| Fender gap (tire top → arch) | **0.25** | 7 cm |
| Front overhang (bumper → front axle) | **3.1** | |
| Rear overhang (rear axle → bumper) | **3.5** | |

Wheel centers (from the pivot, X right / Z forward = −Z):
- FL (−2.75, 1.15, −4.5) · FR (2.75, 1.15, −4.5)
- RL (−2.8, 1.15, 4.5) · RR (2.8, 1.15, 4.5)

## 4. Rig & hierarchy checklist
Existing [[Car Model Spec]] names, plus the chassis additions (marked **new**):
```
Hayate (Model)            PrimaryPart = Root
├─ Root                   invisible box 15.6 × 2.0 × 6.6, bottom at ride height
├─ Body/                  Paint · Glass · Trim · Interior (Massless, CanCollide off)
├─ Wheels/
│   ├─ FL · FR · RL · RR  Model: Tire + Rim, model center = wheel center
│   └─ each wheel: Knuckle attachment (steering pivot)            ← new
├─ Lights/                Headlight_L/R · Taillight_L/R · BrakeLight_L/R
├─ Sockets/               FrontBumper · RearBumper · Spoiler · Hood · Skirts · Exhaust   ← new (attachments)
└─ Attachments on Root    DriverSeat · Exhaust_L · Exhaust_R · Underglow · CameraTarget
```
Budgets: body ≤ 10k triangles · each wheel ≤ 1.5k · 1024² PBR · ~40 parts total.

## 5. Orthographic concept sheet prompt
Use as-is for a 4-view reference sheet:

> Orthographic vehicle reference sheet, four views in a 2×2 grid: front, left side, rear, top. Same scale in every view, aligned on a shared ground line, flat light-gray background, neutral studio lighting, no perspective, no shadows on the background, thin dimension lines.
> Subject: a compact 2-door rear-wheel-drive Japanese-style sports coupe from the late-1990s tuner era, fictional design, **no logos, no badges, no brand names, no license plate text**. Long hood, short rear deck, fastback roofline, low and wide stance. Slim swept-back headlights, a wide lower front intake with a thin splitter, flared front and rear fenders, side skirts, a small ducktail spoiler, round twin taillights each side, a single large exhaust tip on the right. Five-spoke 17-inch wheels with low-profile tires and a small fender gap.
> Proportions: length 4.37 m, width 1.85 m, height 1.23 m, wheelbase 2.52 m, wheels 0.64 m tall. Paint: solid white body, black window trim, gunmetal wheels. Clean line-art plus flat color, suitable as a 3D modeling blueprint.

## 6. Test drive notes
*(filled in during Step 3 testing: what felt right, what to tune)*
- [ ] Stock: can a new player drift it in the first race?
- [ ] Elite: does it still feel like a light JDM car, not a rocket?
- [ ] Phone (auto-gas on): steering not twitchy at 120+ mph?
