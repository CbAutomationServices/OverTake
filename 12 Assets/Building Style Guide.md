> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.
# Building Style Guide (v2)

How the v2 building prefabs should look. Built from parts, realistic and readable from a car at speed. All numbers are in [[City Settings]].

## References
| | |
|---|---|
| ![[Building Ref 1 - Farmhouse.png]] | Modern farmhouse: board-and-batten / limestone, dark metal roofs, gables + dormers, stone-pier porch with white rails, black grid windows, chimney |
| ![[Building Ref 2 - Art Deco Office.png]] | Art deco office: tan stucco, tall vertical pilasters, stepped parapet with fins, recessed centre bay, black marquee, sconces, planters |
| ![[Building Ref 3 - Classical Brick.png]] | Classical brick: stone frame + red brick panels, rusticated base with arched windows, stoops, iron fences, dentil cornice with blocks, lamp posts |
| ![[Building Ref 4 - Twin Walk-up.png]] | Twin walk-up: red brick, stone quoins + lintels, stone base, small awning entrances with lanterns |
| ![[Building Ref 5 - Supertalls.png]] | Supertalls: clock tower with spire, maze-pattern facade, stepped glass tower |
| ![[Building Ref 6 - Tenement Water Tower.png]] | Tenement: brick, arched window heads, storefront + striped awning, water tower |
| ![[Building Ref 7 - Glass Skyline.png]] | Glass skyline: tall towers with vertical ribs, crowns, mixed heights |

## What makes it look good (rules for every model)
1. **Real depth.** Walls are built as piers + bands around each window, with the glass set 0.8 studs back. That gives shadows and reveals, not flat glass pasted on a wall.
2. **Three layers of trim:** base (rusticated stone or a storefront), middle (repeating floors), top (cornice / parapet / crown). Every building has all three.
3. **Corners matter:** quoins, pilasters or chamfers at the corners.
4. **Windows have parts:** frame, mullions, sill, lintel or arch with keystone.
5. **Ground floor is the most detailed:** entrances with steps, lights, signs, awnings, planters, railings.
6. **Rooftops are busy:** water towers, HVAC, bulkheads, antennas.
7. **Materials:** Brick, Limestone, Sandstone, Concrete, Metal frames, Glass (with reflectance). SmoothPlastic only for crisp trim.
8. **Performance:** decorative parts don't collide. Each building gets one invisible collider. Stay within the part budgets in [[City Settings]].
9. **Recolourable:** main wall parts are named `Wall`, so copies of one model can vary colour.

## v2 catalogue (planned)
| Model | Ref | Lot |
|---|---|---|
| Walkup_Twin | 4 | S |
| Tenement_WaterTower | 6 | S |
| Classical_Brick | 3 | L |
| ArtDeco_Office | 2 | S/L |
| Brownstone_Row | 3 | S |
| Flatiron (triangle lot) | — | special |
| Tower_ClockSpire | 5 | XL |
| Tower_Maze | 5 | S |
| Tower_SteppedGlass | 5 | XL |
| Tower_Ribbed A / B | 7 | S / L |
| Loft_Arts (mural wall) | — | L |
| Hotel_Stadium | — | L |
| Farmhouse_Grand / Farmhouse_Small | 1 | Capitol Hill lots |
| Metro_Station | — | special |

The v1 models in [[Building Prefabs]] stay until v2 replaces them.

Related: [[City Blueprint v2]] · [[Building Prefabs]]
