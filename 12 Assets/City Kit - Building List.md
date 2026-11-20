> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# City Kit: Building List

Made in Blender with real CC0 PBR textures (Poly Haven) → imported as meshes. Every type gets **2–4 variants** (color, floor count, signs), so ~30 types turns into 80+ different-looking buildings.

✅ = done (prototype) · ⏳ = next · ⬜ = planned

## Fillers (used many times)
| # | Building | Variants | Where |
|---|---|---|---|
| 1 | Brick tenement, 5–7 floors | ✅ v1 imported: asset **139420612631871** (OT_Tenement_A), ~11k tris, 14 meshes · colors, water tower on/off | Inner neighborhoods |
| 2 | Brick walk-up, 3–4 floors | ✅ imported: asset 91493802040452 (OT_WalkUp_A, ~3k tris) | Neighborhoods |
| 3 | Brownstone rowhouses | ⬜ | Neighborhoods |
| 4 | Storefront row, 2 floors (shops below) | ✅ imported: asset 138157256650997 (OT_Storefront_A) · swap shop signs | Main streets, towns |
| 5 | Mid-rise office (limestone), 8–12 floors | ⬜ | Downtown edge |
| 6 | Modern apartment block with balconies | ⬜ | Neighborhoods |
| 7 | Glass skyscraper | ⬜ 3 heights | Downtown |
| 8 | Art deco skyscraper (setbacks) | ⬜ | Downtown |
| 9 | Concrete/glass office tower | ⬜ | Downtown |
| 10 | Parking garage | ⬜ | Downtown |
| 11 | Warehouse / industrial shed | ⬜ | Port, industrial |
| 12 | Suburban houses (3 styles) | ⬜ | Suburbs |
| 13 | Townhouses | ⬜ | Suburbs |
| 14 | Strip mall | ⬜ | Suburbs, highway exits |
| 15 | Farmhouse + barn + silo | ⬜ | Farmland |

## Key buildings (one or a few each)
| # | Building | Notes |
|---|---|---|
| 16 | **Player Garage** (exterior + interior) | ✅ exterior imported: asset 91807574648198 (OT_PlayerGarage_A); interior next · game starts here; night safehouse |
| 17 | **Car dealership** (OverTake Motors) | Showroom glass, cars inside |
| 18 | **Gas station** (OVERTAKE FUEL) | 🟡 rendered + exported (OT_GasStation_A) · night repairs + nitrous |
| 19 | **Police station** | 🟡 rendered + exported (OT_Police_A) · cop spawn at night |
| 20 | **Bank** | 🟡 rendered + exported (OT_Bank_A) |
| 21 | **Jewelry store** | Fancy storefront |
| 22 | **Convenience store / 24-7** | |
| 23 | **Repair / body shop** | 🟡 rendered + exported (OT_RepairShop_A) |
| 24 | **Tuner / performance shop** | Neon, dyno bay |
| 25 | **Diner** | 🟡 rendered + exported (OT_Diner_A) |
| 26 | **Fast food restaurant** | Drive-thru lane |
| 27 | **Hotel** (downtown) | |
| 28 | **Motel** (highway/coast) | |
| 29 | **Fire station** | |
| 30 | **Hospital** | |
| 31 | **Car wash** | |
| 32 | **Truck stop / rest stop** | Highway |
| 33 | **Church / clock tower** | Landmark |
| 34 | **Port cranes + containers** | Harbor |
| 35 | **City landmark tower** | Skyline focal point |

## Rules
- Original designs only: no real brands, logos or famous buildings copied exactly.
- Each building ≤ ~12k triangles total, ≤ 10k per mesh; shared texture sets.
- Render a preview of each → Cristian approves → import.
- Build scripts live in `12 Assets/Blender/` so any building can be tweaked and rebuilt.

## Import notes (learned on the test import, 2026-11-20)
- GLB arrives 1 m = 1 stud → scale ×3.57 after insert
- Textured materials keep their maps; plain-color materials arrive grey → set colors after insert (or bake every material to a small texture)
- Blender color tints are lost → bake the tint into the texture before export
- Parts arrive unanchored → anchor all
- Upload folder approved in Studio: `12 Assets/Blender`
