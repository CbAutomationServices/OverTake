> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# Core Loop

```mermaid
flowchart LR
  GAR[Start in the Garage: pick car + upgrades] -->|Exit: Day| DAY[Day races]
  DAY -->|queue fills -> teleport to race map| RM[Race map]
  RM -->|Cash only| CASH[(Cash)]
  CASH --> PARTS[Buy parts / cars]
  PARTS --> PR[PR goes up -> higher tier]
  PR --> GAR
  GAR -->|Exit: Night| NIGHT[Night overworld + AI cops]
  NIGHT --> NR[Night races]
  NR -->|little Cash + Rep + Heat| UNB[Unbanked Rep & Cash]
  UNB -->|reach Safehouse| BANK[(Banked Rep)]
  UNB -->|Busted| LOSE[Lose unbanked Rep + fine]
  BANK --> REPLVL[Rep level]
  REPLVL -->|unlocks part levels| PARTS
  NR --> HEAT[Heat 1-5, Heat 6 after 30 min at 5]
  HEAT -->|bigger multiplier| UNB
  HEAT -->|faster, tougher, smarter cops| NR
```

## The two halves
| | Day | Night |
|---|---|---|
| Where | Race markers on the overworld → race runs on its own map once the queue fills | **The same overworld map**, at night, with AI cops roaming |
| Pays | **Cash only** | A little cash + **Rep** + Heat |
| Cops | None | AI cops, scale with Heat + your tier |
| Risk | None | Busted = lose unbanked Rep + fine |
| Why go | Fund parts and cars | **Rep is the only way to unlock better parts** |

Cash buys parts, but **Rep unlocks them**. So a player can't skip the cops. That's the "police required for progression" rule.

## Moment to moment (the micro-loop)
Drift / near-miss / draft / airtime → **refills nitro** + builds a **combo** → combo pays cash (day) or Rep (night) when it ends.

## Progression by stage
| Stage | Tier | What the player is doing | Gate |
|---|---|---|---|
| Early (session 1) | C | Starter car, Street parts, first day races | Street parts need no Rep |
| Early-mid (sessions 2–4) | C → B | First nights, Heat 1–2, Sport parts | **Rep 5** for Sport |
| Mid (week 1–2) | B → A → S | Second car, Race parts, Heat 3–4 | **Rep 12** for Race |
| Late (weeks 3–6) | S → SS | Pro parts, Heat 5 runs | **Rep 22** for Pro |
| End | Z | Elite parts, Heat 6 bragging rights, collection | **Rep 35** for Elite |

Numbers → [[Progression Curve]], [[Economy Settings]], [[Part Values]], [[Race Settings]], [[Heat Settings]]
