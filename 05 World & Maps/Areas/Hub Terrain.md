> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.
# Hub Terrain

Whole-map landscape, replacing the old round terrain domes (Cristian didn't like how they looked).

## How it looks
- Rolling hills, ridges and valleys made from layered noise. No round mounds.
- Every built area (city, drag strip, hub, west strip, tuner district, speedway, off-road lot, neighborhood, roads) stays flat. The ground eases up into hills about 20–200 studs away from it.
- The hills are bigger in the off-road park and on the open land east of the hub.
- Steep slopes turn to rock and dirt. Flatter ground is grass, with dirt patches and darker meadow.
- Snow-capped mountains rise past the edge of the playable area on all four sides, so the map has a frame instead of a hard edge.
- The dirt trail loop is built into the ground: an 18-stud dirt core that blends into the hills, with grades kept to 14% or less. The gravel link to the speedway is included.
- A natural rock arch sits over the trail near Titan Rock. Its opening is about 22 wide by 18 tall.

## Protected (not touched)
- MX track
- Titan Rock + tunnel

## Tech (for edits)
- Generator: `ServerStorage.WorldTerrain`. To change how it looks, edit the module and rerun it (takes about 25 s).
- The flat part ground tiles were swapped for terrain. Old tiles are in `ServerStorage.GroundBackup`.
- Old terrain backup: `ServerStorage.TerrainBackup_PreRealistic`.

Related: [[Off-Road Park]] · [[OverTake Speedway]] · [[Hub]]
