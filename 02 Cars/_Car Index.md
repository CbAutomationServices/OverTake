> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.

# Car Index

One note per car in `02 Cars/Roster/`, made from the **Car** template.
Car stats/prices are NOT stored here: each car's numbers live in [[Car Stats]] (Rules & Settings).

## Master Vehicle Registry
| Car | Slot | Category | Drivetrain | Archetype | Base → Max PR | Weight | Grip ↔ Drift lean | Status |
|---|---|---|---|---|---|---|---|---|
| [[Starter A - Hayate\|Hayate GT]] *(working name)* | #1 Starter A | JDM | RWD | Agile JDM Corner Carver | 70 (C) → 450 (Z) | Light 1,150 kg | Drifty (0.35) | 🟡 Prototype: config + sheet done, model not started |

### Every new car gets
1. A **Vehicle Design Sheet** in `Roster/` (copy [[Starter A - Hayate]]): identity & role, contrast with the cars above, handling DNA, studs blueprint, rig checklist, ortho prompt, test notes
2. A **CarConfig** module `ReplicatedStorage/Shared/Chassis/CarConfigs/<CarID>` (copy `Hayate.lua`; same keys, its own numbers)
3. A row in this table. Before adding it, check it **doesn't duplicate** an existing car's slot on the balance map below

### Balance map (keep every car in its own spot)
| | Light | Medium | Heavy |
|---|---|---|---|
| **Drifty** | Hayate | | |
| **Balanced** | | | |
| **Grippy** | | | |

## Categories
- JDM / tuner
- American muscle
- Euro / exotic
- Off-road / trucks
- Classics *(later update)*

**Launch goal:** 10–15 cars (changed 2026-11-19, was 30+). Proposed split by tier → [[Car Stats]]

How models are built: [[Car Model Spec]]

How stats work: [[Car Stats Explained]]
