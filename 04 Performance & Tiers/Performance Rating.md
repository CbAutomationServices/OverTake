> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# Performance Rating (PR)

Every car has a number from 60 to 500 that shows how good it is. Upgrading parts raises it. The number sets the tier → [[Tiers]].

## Confirmed
- **Any car can be maxed out.** How high it goes depends on its parts.
- Tuning nudges PR slightly → [[Tuning]]

## How it's calculated (proposed 2026-11-19)
Every car has two numbers in [[Car Stats]]:
- **Base PR**: the PR with all stock parts
- **Max PR**: the PR with all Elite parts. Every car's max is in **Z tier (440–500)**, so every car can reach the top. Expensive cars just start higher and get there cheaper.

**PR = Base PR + (Max PR − Base PR) × (sum of each slot's weight × its level %)** + tuning nudge

- Each slot has a **weight** (how much it matters). Engine matters most, brakes least.
- Each part level has a **level %**: Stock 0% → Elite 100%.
- Weights and % → [[PR Settings]]

## Why this works
- **About one tier per part level for a starter car:** a full Street set keeps you in C, full Sport → B, Race → A, Pro → SS, Elite → Z. The upgrade high comes at a steady pace.
- **Downgrading works for free:** drop a part a level and the PR falls, so you can sit at the top of a lower tier (decided 2026-11-12).
- **The garage preview can't lie:** the same function runs on the server and in the garage UI.

## Example: a starter car (Base 70, Max 450)
| All parts at | PR | Tier |
|---|---|---|
| Stock | 70 | C |
| Street | 127 | C |
| Sport | 203 | B |
| Race | 279 | A |
| Pro | 366 | SS |
| Elite | 450 | Z |

The first 3 parts a new player buys: Street Engine **+14**, Street Turbo **+11**, Street Tires **+7**.
