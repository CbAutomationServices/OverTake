> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# MVP Priority Matrix

Scored **1–5**. **Impact** = how much it makes players stay, have fun or pay. **Effort** = how much work for us (5 = huge). Ranked by impact, then lowest effort.

## MVP: must ship at launch
| # | Feature | Impact | Effort | Why MVP | Owner |
|---|---|---|---|---|---|
| 1 | Custom arcade chassis + **drift feel** | 5 | 4 | The whole game is driving | Cristian + Claude |
| 2 | Player data saving (ProfileStore) | 5 | 2 | Nothing sticks without it | Claude |
| 3 | PR system + 7 slots × 6 levels + Garage/Upgrade UI | 5 | 3 | The core upgrade high | Claude |
| 4 | Day races: Circuit, Sprint, Drag | 5 | 3 | The cash loop | Claude |
| 5 | **Night server + Heat 1–6 + AI cops + safehouse banking** | 5 | 5 | Required for progression (confirmed) | Claude |
| 6 | 10–15 car models | 5 | 4 | Content | **Partner** |
| 7 | First 10 Minutes (FTUE) + funnel analytics | 5 | 2 | D1 retention | Claude |
| 8 | HUD (speed, nitro, position, Heat, bust/escape rings) | 4 | 2 | Readable racing | Claude |
| 9 | Dealership (buy cars) | 4 | 2 | Progression goal | Claude |
| 10 | Anti-exploit `VehicleGuard` + server-owned economy | 4 | 2 | Protects leaderboards & economy | Claude |
| 11 | Daily reward + daily featured race | 4 | 1 | D1/D7 | Claude |
| 12 | Gas station repair/nitro refill (night) | 3 | 1 | Already designed | Claude |
| 13 | VIP gamepass + Premium currency + 1–2 boosters | 4 | 2 | Launch revenue | Claude |
| 14 | Basic cosmetics: paint colors + rims | 3 | 2 | Flex at the meet lot | Claude |
| 15 | Drift event (score attack) | 3 | 2 | Shows off the chassis | Claude |
| 16 | ConfigService for all numbers | 3 | 1 | Rebalance without restarts | Claude |
| 17 | Codes system | 3 | 1 | Ties into your TikTok/YouTube | Claude |

## ⭐ Blocker: the night map
Night happens on real-place maps (decided), and none are built. Pick one for the MVP:
- **A. Use City v2 as the first night map:** copy the city into a separate night place, add night lighting, cop spawns and safehouses. Effort 2. Ships fastest. City v2 is Seattle/PNW-inspired, so it still counts as a "real place".
- **B. Build Tokyo first.** Effort 5. Matches the plan exactly, but delays launch by weeks.
- **Recommendation: A**, with Tokyo as the first big post-launch update.

## Post-launch (v1.1+)
| Feature | Impact | Effort | Note |
|---|---|---|---|
| Tokyo night map | 5 | 5 | First content update |
| Crews + crew Rep leaderboard | 4 | 3 | Social / D30 |
| Weekly Blacklist rivals | 4 | 3 | D7 |
| Season pass (4–6 weeks, prize car) | 4 | 3 | Revenue + D30 |
| Grip ↔ drift tuning slider + suspension stiffness | 3 | 2 | Decided; needs the chassis to exist first |
| Wraps, underglow, body kits, exhaust flames | 4 | 3 | High-margin cosmetics |
| Loot boxes (cosmetics only, odds shown, age/region checks) | 3 | 3 | Roblox paid-random-item rules |
| Per-tier leaderboards | 3 | 2 | |
| LA, then Miami maps | 4 | 5 | |
| Passenger seats for friends | 2 | 2 | Decided; low urgency |
| Server Authority migration | 3 | 4 | If our test shows it works for cars |

## Build order (Phase 3)
1. **Week 1–2:** Chassis prototype on a placeholder car (drift test) · data saving · ConfigService. *Partner starts car #1 to the [[Car Model Spec]]*
2. **Week 3:** PR + parts + Garage UI · Dealership · Economy
3. **Week 4:** Day races (Drag first, since the FTUE uses it) · HUD · FTUE
4. **Week 5–6:** Night place + cops + Heat + safehouse + gas stations
5. **Week 7:** Monetization · daily systems · codes · cosmetics · analytics
6. **Week 8:** Playtest on phone + 4G simulation, then soft launch
