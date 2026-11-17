> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.
# Road Surfaces

## Asphalt material
- **Material:** `MaterialService.OT_Asphalt`, a PBR asphalt (color, normal, roughness and metal maps; cracks and patching). Source: "Asphalt PBR" from the free Creator Store, by TheRobloxGamer15782.
- **Applies everywhere:** it's set as the **base material override for Asphalt**, so every Asphalt part *and* the terrain asphalt on the mountain pass use it automatically.
- **Tiling:** 14 studs per tile.
- **Tint:** the part's colour multiplies the texture.
  | Surface | Colour (RGB) |
  |---|---|
  | City streets | 146,146,150 |
  | Speedway racing surface (black) | 88,88,94 |
  | Speedway apron | 150,150,154 |
  | Pit lane | 118,118,122 |
  | Terrain asphalt | 140,140,144 |

## Markings (`CityKit.detailMarkings`)
- **Centre line:** wide streets (half-width 15 or more) get a solid double yellow; narrow streets get a dashed yellow.
- **Edge lines:** white, 1.6 studs in from each curb.
- **Junctions:** a zebra crosswalk at every road a street meets, plus a stop bar on the inbound lane.
- **Applied to:** Hubside and the East City. The old downtown keeps its old markings until it's rebuilt.

## Garage Circle island
- Landscaped roundabout centre: lawn, granite plinth, reflecting pool, chrome ring sculpture with an orange neon core, trees and shrubs.

Related: [[City Blueprint v2]] · [[City Settings]] · [[OverTake Speedway]]
