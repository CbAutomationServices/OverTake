> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.
# Building Prefabs

Reusable building models, the same idea as the car models: build once, drop in anywhere.
- **Where:** `ServerStorage.Prefabs.Buildings`
- **Builder script:** `ServerStorage.BuildingKit` (change a design there and rebuild the prefab)
- **Format:** every model has an invisible `Pivot` at ground centre, and its front faces -Z. To place one: `Clone()` then `PivotTo(CFrame.new(x, groundY, z) * rotation)`.
- **Recolouring:** parts named `Wall` take a per-copy colour (`BuildingKit.tint`), so copies of one model can have different brick or siding colours.

## Lot sizes
| Lot | Footprint (studs) | Fits |
|---|---|---|
| S | 36 x 54 | one third of a city block row |
| L | 76 x 54 | two thirds of a block row |
| XL | 96 x 96 | a whole tower block |
| House | 22 x 28 | one residential lot |

## Catalogue
| Model | Lot | Height | Notes |
|---|---|---|---|
| Brick_Midrise_A | S | 74 | 5 floors, storefronts + awnings, fire escape, water tower |
| Brick_Midrise_B | S | 62 | 4 floors, light brick, 2 storefronts |
| Brick_Midrise_C | S | 50 | 3 floors, dark brick |
| Office_Stone_S | S | 116 | limestone grid, lobby columns |
| Office_Stone_L | L | 152 | "ONE CASCADE PLAZA" |
| Tower_Glass_S | S | 170 | curtain wall, glowing crown |
| Tower_Glass_S2 | S | 120 | green glass |
| Tower_Glass_XL | XL | 310 + spire | retail podium |
| Tower_Setback_XL | XL | 360 + spire | 3 stepped tiers, warm crown |
| Apartments_L | L | 91 | balconies, wood cladding, rooftop solar |
| Loft_Warehouse_L | L | 45 | industrial windows, loading docks, painted wall sign |
| House_Craftsman | House | 1 story | porch |
| House_TwoStory | House | 2 stories | chimney |
| House_Modern | House | 2 stories | flat roofs, big glass |
| StripMall_Large / _Small | Special | | wrapped from the city |
| ParkingGarage_Downtown / _South | Special | | drivable ramps |
| Landmark_SkyNeedle | Special | | |

The city was rebuilt with these on 2026-11-16: 205 placements. The old generated buildings are kept in `ServerStorage.OldCityBuildings`.

Related: [[City]] · [[Nature Prefabs]] · [[Asset List]]
