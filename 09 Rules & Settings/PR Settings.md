> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# PR Settings

Formula → [[Performance Rating]]. These go into ConfigService so they can be tuned live.

## Slot weights (must add up to 1.00)
| Slot | Weight | Why |
|---|---|---|
| Engine | 0.25 | Biggest power gain |
| Turbo / Supercharger | 0.20 | Power curve |
| Tires | 0.13 | Grip = corners |
| Nitrous | 0.13 | Boost is half of NFS racing |
| Transmission | 0.12 | Accel + top speed |
| Suspension | 0.10 | Handling |
| Brakes | 0.07 | Least PR, still matters for corners |

## Level %
| Stock | Street | Sport | Race | Pro | Elite |
|---|---|---|---|---|---|
| 0% | 15% | 35% | 55% | 78% | 100% |

## Other
| Setting | Value | Notes |
|---|---|---|
| PR range | 60–500 | Confirmed |
| Every car's Max PR | 440–500 (all in Z) | Proposed |
| Tuning nudge | ±3 PR max | Proposed; **can't cross a tier line** (clamped) |
| Rounding | Nearest whole number | |
