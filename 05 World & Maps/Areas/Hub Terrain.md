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
- **Off-road park:** hills are bigger (boost 2.8). A creek runs from the hillside into a pond, then on to a small pool. The dirt trail splashes through it at a shallow ford.
- **Pass mountain:** a mountain south of the off-road park, shaped around the paved [[OverTake Pass]] road.
- **Mountain edge:** the edge mountains are taller and more varied, and the terrain now extends to z 3328, so you can't see the end of the world from the summit.
- **Trees and rocks:** realistic meshes, see [[Nature Prefabs]].
- **West bay (2026-11-16):** the land west of x -1900 is now a bay. Water surface at y -4, a seawall slope down from the waterfront, sand and mud on the bottom, and low forested hills on the far shore around x -3200. North of z -1700 it meets the mountains.
- **City land (2026-11-16):** every planned [[City Blueprint v2]] district is flat build land (waterfront, Northgate, the east districts to x 2700, Stadium District, Stadium Heights, Southpoint, Stadium West). The east mountains now start at x 2850.

## Protected (not touched)
- MX track
- Titan Rock + tunnel

## Tech (for edits)
- Smooth terrain draws its surface about 2 studs above the occupancy height, so the generator corrects for this (`W.OFF`). Built areas sit at -0.3, just under the roads.
- `W.prepare()` builds the pass road, mountain, creek and trail. `W.regen(T, x0, x1, z0, z1)` rebuilds one area.
- Generator: `ServerStorage.WorldTerrain`. To change how it looks, edit the module and rerun it (takes about 25 s).
- The flat part ground tiles were swapped for terrain. Old tiles are in `ServerStorage.GroundBackup`.
- Old terrain backup: `ServerStorage.TerrainBackup_PreRealistic`.

Related: [[Off-Road Park]] · [[OverTake Speedway]] · [[Hub]]
