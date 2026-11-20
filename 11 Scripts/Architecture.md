> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# Architecture

How the code is organized in Studio. Each vault section maps to its own module (Vault Rule 7).

## Places (one universe)
| Place | What runs there |
|---|---|
| **Hub** (current place) | Always day: free roam, Garage, Dealership, day races, FTUE |
| **Night: City v2** (MVP, proposed) | Night lighting, AI cops, Heat, safehouses, night races |
| Night: Tokyo / LA / Miami (later) | Same night code, different map |

You go to night through the **Garage → TeleportService**. Player data saves before the teleport, and ProfileStore's session lock stops it loading on two servers at once.

## Folder layout
```
ReplicatedStorage
└─ Shared
   ├─ Config         defaults + ConfigService live values (every number from 09 Rules & Settings)
   ├─ CarData        from [[Car Stats]]
   ├─ PartData       from [[Part Values]]
   ├─ PR             the PR formula; used by server AND garage preview → [[Performance Rating]]
   └─ Remotes        every RemoteEvent/Function in one place
ServerScriptService
└─ Services
   ├─ PlayerDataService   ProfileStore (save/load)
   ├─ EconomyService      the ONLY place cash/Rep change: Add(player, amount, reason) → analytics
   ├─ GarageService       buy / equip / downgrade parts (server checks price, Rep, ownership)
   ├─ DealershipService   buy cars
   ├─ VehicleService      spawn cars, give the driver network ownership, zone-based enter/exit
   ├─ VehicleGuard        anti-cheat: speed, teleport, checkpoint-order checks
   ├─ RaceService         lobby, countdown, checkpoints, results, payouts (Drag, Circuit, Sprint, Drift)
   ├─ DailyService        streak + featured race
   ├─ MonetizationService gamepasses, dev products, ProcessReceipt
   └─ Night only: HeatService, CopService, SafehouseService, GasStationService
ServerStorage
└─ World-gen modules (CityGen, CityKit, … already there: don't touch)
StarterPlayerScripts
└─ Controllers
   ├─ ChassisController   our custom raycast chassis (driver's device)
   ├─ CameraController    speed FOV, shake, nitro pull-back
   ├─ InputController     phone / PC / gamepad (Input Action System)
   ├─ HUDController, GarageUI, DealershipUI, FTUEController
```

## Key choices (from [[Phase 1 Research Dossier]])
| Choice | Why |
|---|---|
| **Custom raycast chassis** (decided) | Full control of grip and drift |
| Driver's device runs the car's physics; the server checks it | No input lag. Roblox staff recommend server-side checks of car motion |
| **ProfileStore** for saves | Successor to ProfileService, with session locking |
| **No Knit** | Archived by its author in July 2024 |
| **ConfigService** for every number | Change payouts and prices live, A/B test |
| StreamingEnabled ON | Big map, phones. Also needed if we try Server Authority later |
| Part swaps only in the Garage, car respawned after | Re-welding parts on a moving car can reset network ownership |
| Own enter-car check (distance + owner) | Stops the "teleport into the seat" exploit |

## Cops (CopService)
- Cop cars are **server-owned** and driven by AI inputs (steer/throttle/brake) through the same chassis module.
- They navigate a **road graph** built from the CityGen road data (no Pathfinding for cars).
- Line of sight = raycasts from each cop to the player. That drives the escape timer.
- **Performance cap:** ~10 cops per player and ~30 per server. Must test with the profiler + 4G network simulation.

## Player data (v0)
```
Cash, Premium, Rep, RepLevel,
Cars = { [carId] = { parts = {Engine=2, Turbo={type="Turbo",lvl=1}, ...}, owned = {...}, cosmetics = {...} } },
SelectedCar, Daily = {streak, lastClaim}, FTUE = {step}, Stats = {races, wins, busts, escapes, driftBest}
```
Unbanked night Rep/cash live **in the night server's memory only** until you bank at a safehouse.
