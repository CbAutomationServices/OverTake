> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.

# City Kit: Building List

Made in Blender with real CC0 PBR textures (Poly Haven) → GLB → uploaded through Open Cloud → fixed in Studio by `ServerStorage.OT_ImportFixer`.
Build scripts: `12 Assets/Blender/` (`final1.py`, `final2.py`; earlier `b_*.py`). Run with `python3 final1.py <Name> render|export`.

✅ = imported into Studio (Workspace.OT_CityKit_Test) · 🟡 = rendered, not imported yet · ⬜ = planned

## Key buildings
| Building | Model | Asset ID | Status |
|---|---|---|---|
| Player Garage (exterior) | OT_PlayerGarage_A | 91807574648198 | ✅ interior still to do |
| Gas station | OT_GasStation_B | 77891465054729 | ✅ |
| Bank | OT_Bank_B | 137199664922091 | ✅ |
| Police station | OT_Police_B | 125289097712648 | ✅ |
| Repair / body shop | OT_RepairShop_B | 83182882700238 | ✅ |
| Diner | OT_Diner_B | 106681518001436 | ✅ |
| Jewelry store | OT_Jewelry_A | 115765505057991 | ✅ |
| Convenience store 24/7 | OT_Convenience_A | 86480239913257 | ✅ |
| Hotel (downtown) | OT_Hotel_A | 90113084241687 | ✅ |
| Aquarium | OT_Aquarium_A | 127559275906933 | ✅ |
| Gun store | OT_GunStore_A | 80422687789110 | ✅ |
| Barber shop | OT_Barber_A | 98776390843406 | ✅ |
| Prison | OT_Prison_A | 91617425637574 | ✅ |
| Bar | OT_Bar_A | 101221217796219 | ✅ |
| Tech store | OT_TechStore_A | 108627679196107 | ✅ |
| Trading card store | OT_CardShop_A | 136796620167858 | ✅ |
| Hardware / equipment store | OT_HardwareStore_A | 104445072702591 | ✅ |
| Tuner / performance shop | OT_TunerShop_A | — | 🟡 |
| Fast food (drive-thru) | OT_FastFood_A | — | 🟡 |
| Motel | OT_Motel_A | — | 🟡 |
| Fire station | OT_FireStation_A | — | 🟡 |
| Hospital (helipad) | OT_Hospital_A | — | 🟡 |
| Car wash | OT_CarWash_A | — | 🟡 |
| Truck stop | OT_TruckStop_A | — | 🟡 |
| Church | OT_Church_A | — | 🟡 |
| Port crane + containers | OT_PortCrane_A | — | 🟡 |
| City landmark tower | OT_Landmark_Tower | — | 🟡 |
| Car dealership (OverTake Motors) | — | — | ⬜ |

## Fillers (used many times)
| Building | Model | Asset ID | Status |
|---|---|---|---|
| Brick tenement | OT_Tenement_A | 139420612631871 | ✅ |
| Brick walk-up | OT_WalkUp_A | 91493802040452 | ✅ |
| Storefront row | OT_Storefront_A | 138157256650997 | ✅ |
| House: colonial | OT_House_A | 71659542651872 | ✅ |
| House: ranch | OT_House_B | 132801602760254 | ✅ |
| House: craftsman | OT_House_C | 109428348482175 | ✅ |
| Trailer home | OT_Trailer_A | 89378718232462 | ✅ |
| Brownstone row | OT_Brownstone_A | — | 🟡 |
| Mid-rise office | OT_Office_A | — | 🟡 |
| Apartment block (balconies) | OT_Apartments_A | — | 🟡 |
| Glass skyscraper | OT_Skyscraper_Glass | — | 🟡 |
| Art deco skyscraper | OT_Skyscraper_Deco | — | 🟡 |
| Concrete office tower | OT_OfficeTower_B | — | 🟡 |
| Parking garage | OT_ParkingGarage_A | — | 🟡 |
| Warehouse | OT_Warehouse_A | — | 🟡 |
| Townhouses | OT_Townhouses_A | — | 🟡 |
| Strip mall | OT_StripMall_A | — | 🟡 |
| Farm (house + barn + silo) | OT_Farm_A | — | 🟡 |

## Rules
- Original designs only: no real brands, logos or famous buildings.
- ≤ ~12k triangles per building, ≤ 10k per mesh (Roblox cap is 20k).
- Render preview → Cristian approves → import.

## Import notes (learned 2026-11-20)
- GLB arrives 1 m = 1 stud → scale ×3.57 (done by `F.fix`).
- Plain-color materials arrive grey → color is stored in the mesh name as `__RRGGBB` and re-applied by `F.materials`.
- Tints must be baked into the texture before export.
- Parts arrive unanchored → `F.materials` anchors them.
- Front direction: `F.orient` uses the lot stripes (`PaintWhite`) or the front door.
- Upload folder approved in Studio: `12 Assets/Blender`.
- The test lineup in `OT_CityKit_Test` is temporary. Real placement happens in the Map v3 (Horizon Valley) build.
