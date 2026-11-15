> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.
# Gas Stations

Like NFS Heat: drive through to **repair your car**.

## Confirmed
- **Hub:** at least one, mostly for looks/vibe (the hub has no damage)
- **Night maps:** **full repair** + **refills nitrous**
- **Limited uses per night:**
  - **C / B / A tier** → **1 repair**
  - **S / SS / Z tier** (PR 281+) → **2 repairs**
  - **+1 extra repair** from a Premium booster → [[Boosters]]
- Uses **reset each new night**
- **Works during cop chases**

## The model (prefab) — used for EVERY gas station
**Brand:** OVERTAKE FUEL (original, red/white/charcoal with neon red + amber stripes)
**Where:** `ServerStorage > Prefabs > GasStation`. To add a station: clone it and `PivotTo(CFrame.new(x, groundY, z) * rotation)`. Front (pumps) faces -Z; pivot is at ground level, lot center. Footprint 110 x 92 studs.
**Inside the prefab:**
- Canopy with layered neon stripes, red fascia, glowing OVERTAKE FUEL signs on 3 sides, underside lights (night-ready)
- 3 pump islands, 6 detailed pumps (screens, displays, nozzles, hoses), columns, yellow bollards, trash cans
- Mini mart: metal siding, red parapet with glow line, MINI MART sign + logo, windows with shelves/products visible inside, coolers, counter, slushie machine, glass doors, awning, ICE freezer, propane cage, bench, planters, roof units, restrooms, dumpster enclosure
- Price pylon (REG / PLUS / PREM / DSL), air machine, 2 EV chargers, parking stalls + arrows
- Landscaping beds, bushes, trees, lamps
- `RepairZone` part (invisible) for the repair + nitrous system
**Placed at:** hub (by the main avenue) and the city (west side). Old versions backed up in ServerStorage.
**Hub surroundings:** grassy terrain mounds, boulders, evergreens, flower beds, hedges, benches, WELCOME TO OVERTAKE sign.

## Open questions
- [ ] How many gas stations per night map?
- [ ] Does it also work in day races, or night only?

Numbers → [[Heat Settings]]
