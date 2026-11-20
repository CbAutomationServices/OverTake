> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# First 10 Minutes (FTUE script)

Goal: **driving in under 15 s, first part by minute 3, three parts by minute 8**, then a reason to come back tomorrow. Every beat logs a **funnel event** (in brackets) so we can see exactly where new players quit.

| Time | Beat | What the player sees / does | Teaches | Funnel event |
|---|---|---|---|---|
| 0:00 | Join | Short loading screen (car silhouette + "OVERTAKE"). The starter cars load in the background | — | `1_Joined` |
| 0:05 | **Pick your ride** | 3 big cards: JDM / Muscle / Euro starter, each with a 1-line vibe and its 4 stat bars. One tap. A default is pre-highlighted, so the impatient can just tap GO | Stat bars | `2_PickedStarter` |
| 0:12 | **Spawn in the car** | Spawned *seated* outside the Garage, engine running, camera behind. Pulsing gas button (phone) / "W" hint (PC) | Gas, steer | `3_InCar` |
| 0:20 | Go race | Glowing GPS line + a rival car revving: "**Ronin** thinks your car is junk. Prove him wrong." | Following the GPS | `4_HeadedToRace` |
| 0:40 | **First race: drag** | Drag Strip, 1v1 vs Ronin (AI). The Christmas tree counts down. "Hit NITRO!" prompt at the halfway mark. Tuned so a new player wins narrowly | Nitro | `5_Race1Started` |
| 1:10 | Win | Slow-mo finish, confetti, **$2,500 + $1,000 first-race bonus** counts up | Cash | `6_Race1Won` |
| 1:30 | To the Garage | GPS → Garage. Ronin: "Lucky. Bet you can't beat me with *that* engine." | — | `7_EnteredGarage` |
| 2:00 | **First upgrade** | Garage opens on the **Engine** slot: ghost bar grows, "**PR 70 → 84**". One big BUY button ($2,100). The engine sound changes on purchase | Parts raise PR | `8_FirstPart` |
| 2:30 | Second upgrade | "You've got $1,400 left" → Tires flash (+7 PR, $1,200). Buy | Slots | `9_SecondPart` |
| 3:00 | Feel it | Free-roam drive to the next race. A **near-miss / drift prompt** pops on the first big corner: combo meter + "nitro refilled!" | Drift → nitro, combo pays | `10_FirstCombo` |
| 4:00 | **Race 2: circuit** | Speedway or city loop, C tier, vs players + AI fill-ins, ~2 min | Racing lines | `11_Race2Done` |
| 6:30 | **Third upgrade: choose your boost** | Turbo vs Supercharger choice screen: each plays its sound (spool vs whine). Pick one (+11 PR) | Forced-induction feel | `12_ThirdPart` |
| 7:30 | Come-back hooks | **Daily reward** pops (Day 1 of 7) + today's **Featured Race** (2× payout) | Appointment | `13_SawDaily` |
| 8:30 | **The Night tease** | Back in the Garage, the **Night** door glows: "Sport parts need **Rep**. Rep only comes at **night**… and the cops are waiting." A short clip of a chase | Why night matters | `14_SawNight` |
| 9:30 | Next goal | A goal card: "Finish your Street set (4 parts left) → enter the Night." Progress bar 3/7 | Clear next step | `15_GoalShown` |

## Rules for the FTUE
- **No text walls.** Max 8 words per prompt. Prompts show only when the feature first appears.
- **No menus before the first race.** Just the starter pick.
- **The FTUE starts race 1 by itself.** It's an exception to "join races only from the Garage" (decided 2026-11-12).
- **Night unlocks** after 3 day races *or* the full Street set (proposed), so brand-new players don't get wrecked by cops in minute 2.
- **Returning players skip all of this** and spawn at the Garage.
- If the Drag Strip is more than ~30 s from spawn, the first trip there **teleports on accept**. *(Measure in Studio.)*

Numbers → [[Race Settings]], [[Economy Settings]] · Pacing → [[Progression Curve]]
