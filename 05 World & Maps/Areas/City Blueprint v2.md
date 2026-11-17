> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.
# City Blueprint v2

The plan for rebuilding the hub's city: higher-quality buildings, a street layout with personality, a much bigger footprint (wrapping the garage and the speedway), and an elevated metro. Build in phases. Each phase gets screenshots and Cristian's OK before the next starts.

![[City Blueprint v2 Map.png]]

## Goals
1. **No straight shots.** You should never be able to floor it from one end of the city to the other on one street. Routes bend, jog, T-out, cross diagonals and go around roundabouts.
2. **Every district feels different:** its own street pattern, building style, props and lighting.
3. **Buildings match the reference style** in [[Building Style Guide]]: real window depth, trim, ornament, rooftops.
4. **Alive:** storefront signs, neon, lit windows at night, parked cars, street furniture, the metro running overhead. Pedestrians and traffic come later.
5. **Metro-ready.** Every street the metro follows keeps a median, and building rules respect the metro corridor (see [[OverTake Metro]]).

## Districts
| District | Rough area (x / z) | Street pattern | Buildings | Feel |
|---|---|---|---|---|
| Downtown West | -1500..-1000 / -1150..-590 | Needle Park loop | supertalls, Sky Needle | landmark skyline |
| Downtown Core | -1000..-20 / -1150..-590 | **Pike diagonal** cuts the grid; the grid north of Pike is rotated to match it, so streets T into Pike; flatiron buildings on the triangle lots | glass skyline, clock-spire tower, maze tower | big-city canyon |
| Central Park | -1000..-760 / -700..-500 | blocks the east–west streets | park, pond, kiosks | breather |
| Old Town | -1500..-950 / -590..30 | narrow, curved, one-way, cobblestone | tenements with water towers, classical brick, market | old brick, tight streets |
| Midtown | -950..-20 / -590..30 | grid that **jogs half a block** every crossing, so no through-runs | art deco offices, brownstones, walk-ups | classy |
| South End | -1500..-600 / 30..545 | curved residential streets + roundabout + cul-de-sacs | twin walk-ups, rowhouses | neighbourhood |
| Arts & Warehouse *(new)* | 780..1250 / -1120..-350 | grid rotated 15° | lofts, murals, breweries, metro yard | gritty, creative |
| East Side *(new)* | 780..1250 / -350..560 | **Garage Circle** roundabout with 6 radial streets | mid-rises, shops around the garage | busy hub of the east |
| Capitol Hill *(new)* | 1250..1850 / -1120..560 | winding hillside streets that follow the terrain | farmhouses, villas, small apartments | hills, views |
| Stadium District *(new)* | 780..1460 / 560..1075 | Stadium Way boulevard + roundabout | hotels, sports bars, merch stores | game-day energy |
| Stadium West *(new)* | -40..780 / 800..1075 | plaza + parking | plaza, food stalls | gateway to the speedway |

The east-side districts need the east mountains pushed out to about x 1900. That's one setting change in the terrain generator.

## Street network rules
Numbers are in [[City Settings]].
- **Hierarchy:** ring boulevard → avenues (metro medians) → streets → alleys.
- **Straight runs:** no street runs straight longer than the max in [[City Settings]]. After that it bends, jogs, Ts or hits a roundabout or plaza.
- **Ends of long views** finish on something to look at: a landmark, plaza, or tower.
- **Mix of junctions:** 4-way, T-junctions, roundabouts, offset jogs, diagonal triangles.
- **Width varies by district:** Old Town lanes are narrow, avenues are wide.
- **Alleys** behind blocks are drivable shortcuts. The tight corners are good for chases.
- **One-way streets** in Old Town only.

## "Alive" checklist (per block)
- [ ] Storefront signs + awnings, some neon at night
- [ ] Lit-window system at night (random warm windows)
- [ ] Parked cars along curbs (placeholder cars until the car models exist)
- [ ] Street furniture: lamps, benches, bins, hydrants, bus stops, news boxes, planters, trees (new tree meshes)
- [ ] Rooftop life: water towers, HVAC, antennas, rooftop bars on a few buildings
- [ ] Murals in the Arts district; billboards on boulevards
- [ ] Metro trains running overhead (visual loop, no gameplay yet)
- [ ] Later: ambient pedestrians and AI traffic

## Phases
- [ ] **A. Style:** v2 building prefabs that match [[Building Style Guide]]. Prototypes first, for approval.
- [ ] **B. Layout:** rebuild the existing city's streets per this plan (Pike diagonal, jogs, Old Town curves, Central Park).
- [ ] **C. Expansion:** push the east mountains out; build the Arts, East Side, Capitol Hill and Stadium districts.
- [ ] **D. Metro:** Line 1 viaduct + stations + train visuals ([[OverTake Metro]]).
- [ ] **E. Life:** alive checklist, night lighting, props.
- [ ] **F. Later:** pedestrians, traffic, Metro Line 2.

## Open questions
- Should the hub centre (dealer, shop, meet lot) stay traffic-free with the metro flying over it, or should the metro go around it?
- Canal or river through the East Side with bridges? (Not on the map yet.)
- Does the metro get used in gameplay (fast travel / ride it) or is it just scenery?

Related: [[City]] · [[Hub]] · [[OverTake Metro]] · [[Building Style Guide]] · [[Building Prefabs]] · [[City Settings]]
