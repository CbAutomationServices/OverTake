> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.
# Forced Induction (Boost Paths)

**One slot, pick one boost path.** Each path adds power the way it does in real life, so every path has a clear **pro and con**. There's no "best" path, only the best one for a car, a race type and a driving style.

Chassis math → [[Chassis Architecture]] §5 · Car configs set each path's numbers per car.

## Confirmed
- One slot, one path at a time (2026-11-12)
- **More than 2 options**, each must feel like the real thing, with real trade-offs (2026-11-25)

## The 6 boost paths
| Path | How it works in real life | How it feels in game | Pro | Con |
|---|---|---|---|---|
| **Single Turbo** (big turbo) | Exhaust gas spins a turbine. A big turbo needs lots of exhaust flow before it makes boost | Nothing… nothing… **then a huge hit** of power high in the revs. Whistle, flutter, blow-off | **Strongest top end and top speed** of any path | **Worst lag.** Dead below ~55% rpm, 1.2 s to spool. Loses boost every shift and every time you lift |
| **Twin Turbo** | Two smaller turbos, each spools faster | Boost arrives earlier and smoother, still with a short delay | Wide, usable powerband. **Best all-rounder** | A bit less peak power than the big single. Still some lag |
| **Roots Supercharger** (blower) | Belt-driven by the crank, pushes air at every rpm | **Instant shove** off every corner and the line. Loud whine | **Best launch and corner exit.** Zero lag | Steals engine power to spin itself: **falls flat at the top end**, lowest top speed. Heat-soaks on long full-throttle runs |
| **Twin-Screw Supercharger** | More efficient belt-driven compressor | Instant power, not quite as violent down low, pulls further up | Instant **and** holds better up top than a Roots | Less low-end punch than the Roots, still fades near redline |
| **Centrifugal Supercharger** (pro-charger style) | Belt-driven like a turbo compressor; boost rises with rpm | No lag, but feels almost stock down low, then **keeps building to redline** | **No lag + strong top end.** Great for drag and the freeway | **Weak low end.** Bad corner exits in the city if you drop the revs |
| **Twincharger** (supercharger + turbo) | Supercharger fills the low end while the turbo spools, turbo takes over up top | Instant low end **and** a big top end | **The widest powerband in the game** | **Late unlock and the most expensive.** Adds weight (slightly worse handling) and a little less peak than the big single |

## Where each path wins
| Path | Drag | Freeway sprint | City circuit | Drift | Cop escape |
|---|---|---|---|---|---|
| Single Turbo | ★★★ | ★★★ | ★ | ★ | ★★ |
| Twin Turbo | ★★ | ★★ | ★★ | ★★ | ★★ |
| Roots | ★★ (launch) | ★ | ★★★ | ★★★ | ★★ |
| Twin-Screw | ★★ | ★★ | ★★★ | ★★ | ★★ |
| Centrifugal | ★★★ | ★★★ | ★ | ★ | ★★ |
| Twincharger | ★★★ | ★★ | ★★ | ★★ | ★★★ |

**Drift note:** turbo lag makes drifts harder to hold. Lift off and the boost dies, then comes back late. Superchargers answer the throttle instantly, so they're the drift-friendly choice. Real-life behavior, and a real choice.

## How the chassis makes each one feel (per path)
| Setting | What it does | Single T | Twin T | Roots | Twin-Screw | Centrif. | Twinch. |
|---|---|---|---|---|---|---|---|
| Boost starts at | % of redline where boost can build | 55% | 40% | idle | idle | idle | idle |
| Spool time | seconds to reach full boost (turbo lag) | 1.2 | 0.7 | 0 | 0 | 0 | 0.6 (turbo half) |
| Boost shape | how boost follows rpm | ramps late, holds | ramps early, holds | flat | flat, small rise | rises to redline (²) | flat low → turbo top |
| Peak boost (Elite) | extra torque on top of the engine | **+60%** | +52% | +42% | +45% | +55% | +55% |
| Parasitic loss | power the belt drive eats at redline | 0 | 0 | **−14%** | −8% | −4% | −6% |
| Boost lost on shift | turbos dump pressure between gears | 35% | 20% | 0 | 0 | 0 | 10% |
| Lift-off bleed | boost lost per second off throttle | fast | fast | instant back | instant back | instant back | medium |
| Heat soak | power fade after ~8 s flat out | 0 | 0 | −6% | −4% | −2% | −3% |
| Weight | extra weight (handling) | 0 | +1% | +2% | +2% | +1% | **+4%** |
| Sound | | whistle + flutter + blow-off | twin whistle + blow-off | deep whine | whine | rising scream | whine + whistle |

The numbers are starting points for test drives (Step 3). Each car's config can push them (e.g. a muscle car gets a stronger Roots, a JDM car a stronger single turbo), so the right path also depends on the car.

## Rules (proposed)
- **Each path is its own part with 6 levels** (Stock → Elite). Levels make it stronger and quicker to spool; they don't change its character
- **Same level = same PR** on every path, so a race tier is fair. Paths change the *shape* of the power, not the total
- **Switching paths:** buy the new path's part. Old ones stay in your inventory (swap in the Garage, car respawns: [[Architecture]] rule)
- **Every car can run every path**, but each car has its own numbers per path (its "affinity")
- **Twincharger** unlocks late (Rep level TBD) and costs the most
- **HUD boost gauge:** yes. It's how players *see* the lag and the supercharger's instant response

## Ideas for later
- **Anti-lag** add-on for turbos: keeps boost on lift, with pops and bangs (costs reliability or nitro refill?)
- **Wastegate / boost tuning** in [[Tuning]]: more peak boost but more lag

## Open questions
- [ ] Twincharger: launch item or post-launch?
- [ ] Anti-lag: yes / no / later?

Numbers → [[Part Values]]
