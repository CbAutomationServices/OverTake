> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.
# OverTake Freeway

A fast freeway linking the **drag strip → the city → the speedway**. It's the quickest way across the map and full of moments: flying over Hubside on a viaduct, diving through the hill tunnel, and the long tunnel run under the hub area. Dimensions are in [[City Settings]].

## Route (north → south)
| Section | From → to (x, z) | Type | Notes |
|---|---|---|---|
| Drag strip on-ramp | (1100, -1313) → (1140, -1200) | at grade | starts at the drag strip turnoff |
| Hubside Viaduct | (1040, -1080) → (560, -860) | elevated, about 34 high | sweeps west over the Arts district edge and Hubside; city streets pass underneath |
| Hubside Hill Tunnel | (490, -780) → (415, -430) | tunnel through the park hill | stone portals with the name over the entrance |
| Hubside Cut | (415, -430) → (440, -260) | open trench, descending | retaining walls; park bridges can cross later |
| OverTake Tunnel | (480, -140) → (760, 520) | deep tunnel, about 16 below ground | passes under Main Ave, the takeover pad and the garage; lit tiled walls |
| Stadium Cut | (770, 660) → (725, 850) | trench rising to street level | |
| Stadium end | (725, 850) | at grade | joins the Stadium Way roundabout; the speedway parking is just south |

## Cross-section
- 2 lanes each way, with a median barrier and shoulders
- Jersey barriers on the edges
- Dashed lane lines, yellow inner edge lines, white outer edge lines
- Double-arm street lights in the median
- Concrete pillars with cap beams under the viaduct
- Tunnels: tiled walls, ceiling light strips, portal facades

## Built (2026-11-16)
- Built by `ServerStorage.FreewayBuilder` (`F.route` holds the control points; it works out from the terrain which parts are raised, at ground level, sunk in a cut, or in a tunnel) into `Workspace.OverTake_Hub["OverTake Freeway"]`, about 2,400 parts.
- **Hubside Hill:** a 48-stud park hill north of the takeover, added to `WorldTerrain.parkHills`.
- **Speedway end:** the speedway service road was shortened so the freeway exit joins it at z ~856.
- The leftover tuner shipping containers were moved to ServerStorage.
- **Known issue:** in the deep tunnel under the hub area, the terrain ceiling shows instead of the concrete ceiling (only 2 studs of cover). It looks like a rock-cut tunnel; it can be reworked later.

## Later
- On/off ramps into Hubside and the East Side
- Overhead sign gantries ("SPEEDWAY", "DRAG STRIP", "DOWNTOWN")
- Night races using the freeway (fits the night-heat system)

Related: [[City Blueprint v2]] · [[Drag Strip Complex]] · [[OverTake Speedway]]
