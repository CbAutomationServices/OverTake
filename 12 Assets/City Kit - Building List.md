> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.

# City Kit: Building List

Made in Blender with real CC0 PBR textures (Poly Haven) → GLB → uploaded through Open Cloud → fixed in Studio by `ServerStorage.OT_ImportFixer`.
Build scripts: `12 Assets/Blender/` (`final1.py`, `final2.py`, `final3.py`; earlier `b_*.py`). Run `python3 final3.py <Name> render|export`.
Contact sheets: `12 Assets/Blender/renders/`.

**61 models imported.** Where they are in Studio: `Workspace.OT_CityKit_Test` (first batches) and `Workspace.OT_KitGallery` (temporary lineup at x≈7000). Real placement happens in the Map v3 (Horizon Valley) build.

## Key buildings
| Building | Model | Asset ID |
|---|---|---|
| Player Garage (exterior) | OT_PlayerGarage_A | 91807574648198 |
| Gas station | OT_GasStation_B | 77891465054729 |
| Bank | OT_Bank_B | 137199664922091 |
| Police station | OT_Police_B | 125289097712648 |
| Repair / body shop | OT_RepairShop_B | 83182882700238 |
| Diner | OT_Diner_B | 106681518001436 |
| Jewelry store | OT_Jewelry_A | 115765505057991 |
| Convenience store 24/7 | OT_Convenience_A | 86480239913257 |
| Hotel | OT_Hotel_A | 90113084241687 |
| Aquarium | OT_Aquarium_A | 127559275906933 |
| Gun store | OT_GunStore_A | 80422687789110 |
| Barber shop | OT_Barber_A | 98776390843406 |
| Prison | OT_Prison_A | 91617425637574 |
| Bar | OT_Bar_A | 101221217796219 |
| Tech store | OT_TechStore_A | 108627679196107 |
| Trading card store | OT_CardShop_A | 136796620167858 |
| Hardware / equipment store | OT_HardwareStore_A | 104445072702591 |
| Tuner / performance shop | OT_TunerShop_A | 95524234580868 |
| Fast food (drive-thru) | OT_FastFood_A | 109524231558212 |
| Motel | OT_Motel_A | 91320261585279 |
| Fire station | OT_FireStation_A | 108731505950076 |
| Hospital (helipad) | OT_Hospital_A | 100416417804953 |
| Car wash | OT_CarWash_A | 103151185912725 |
| Truck stop | OT_TruckStop_A | 132108254901864 |
| Church | OT_Church_A | 97712472881086 |
| Port crane + containers | OT_PortCrane_A | 127206374115501 |
| City landmark tower | OT_Landmark_Tower | 107019334052902 |
| Auto parts store | OT_AutoParts_A | 133723295269954 |
| Gym | OT_Gym_A | 128671834889410 |
| Laundromat | OT_Laundromat_A | 114749799004244 |
| Car dealership (OverTake Motors) | — | ⬜ planned |

## Skyscrapers (downtown skyline)
| Style | Model | Asset ID |
|---|---|---|
| Glass tower | OT_Skyscraper_Glass | 133159999431793 |
| Art deco setbacks | OT_Skyscraper_Deco | 95214259159225 |
| Concrete office tower | OT_OfficeTower_B | 105419301547042 |
| Twisting teal tower | OT_Skyscraper_Twist | 98785789668048 |
| Green glass setback tower | OT_Skyscraper_Setback | 140067268470761 |
| Round blue tower | OT_Skyscraper_Round | 127737263073211 |
| White residential tower | OT_Skyscraper_Residential | 120831469255664 |
| Twin towers + skybridge | OT_Skyscraper_Twin | 119374343595634 |
| 1920s brick high-rise | OT_Skyscraper_Brick | 79907022974824 |
| Black braced tower | OT_Skyscraper_Braced | 138386032592842 |

## Fillers (used many times)
| Building | Model | Asset ID |
|---|---|---|
| Brick tenement | OT_Tenement_A | 139420612631871 |
| Brick walk-up | OT_WalkUp_A | 91493802040452 |
| Storefront row | OT_Storefront_A | 138157256650997 |
| House: colonial | OT_House_A | 71659542651872 |
| House: ranch | OT_House_B | 132801602760254 |
| House: craftsman | OT_House_C | 109428348482175 |
| Trailer home | OT_Trailer_A | 89378718232462 |
| Brownstone row | OT_Brownstone_A | 130542413108226 |
| Mid-rise office | OT_Office_A | 108972314324541 |
| Apartment block | OT_Apartments_A | 135326904746725 |
| Parking garage | OT_ParkingGarage_A | 77598551671200 |
| Warehouse | OT_Warehouse_A | 114246743410777 |
| Townhouses | OT_Townhouses_A | 100399532532915 |
| Strip mall | OT_StripMall_A | 84972763908717 |
| Farm (house, barn, silo) | OT_Farm_A | 108904600886971 |
| Corner shop + apartments | OT_CornerShop_A | 110990806511048 |
| Mixed-use block | OT_MixedUse_A | 140730149763782 |
| Duplex | OT_Duplex_A | 97635175568796 |
| Factory | OT_Factory_A | 115352238615619 |
| Office park | OT_OfficePark_A | 126481219553519 |

## Rules
- Original designs only: no real brands, logos or famous buildings.
- ≤ ~12k triangles per building, ≤ 10k per mesh (Roblox cap is 20k).
- Render preview → Cristian approves → import.

## Import notes (learned 2026-11-20)
- GLB arrives 1 m = 1 stud → `ScaleTo(1/0.28)` (×3.57). Check `GetScale()` before scaling, or a re-run double-scales.
- Plain-color materials arrive grey → color is stored in the mesh name as `__RRGGBB` and re-applied by `F.materials`.
- Tints must be baked into the texture before export.
- Parts arrive unanchored → `F.materials` anchors them.
- Front direction: `F.orient` uses `PaintWhite` (lot stripes), the door, or `Pavement`.
- `F.place` can drop big models near the origin and can stall Studio → for bulk imports use the gallery grid instead.
- Colored glass (teal/green/blue/dark) is set to SmoothPlastic + reflectance 0.2 so its color shows. Roblox Glass washes it out.
- Load assets with `game:GetObjects` into a ServerStorage hold folder, then fix 5–8 at a time with `task.wait()`.
- Upload folder approved in Studio: `12 Assets/Blender`.
