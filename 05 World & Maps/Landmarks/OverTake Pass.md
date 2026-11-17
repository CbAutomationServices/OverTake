> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.
# OverTake Pass

A touge-style paved mountain road climbing the mountain south of the off-road park. Inspired by the hairpin-pass screenshots Cristian sent.

- **Start:** the speedway's southwest back road, at about (-40, 2068). The entrance sign reads "OVERTAKE PASS".
- **Route:**
  - A long sweeping climb west along the mountain's flank
  - Then a stack of switchback legs with tight hairpins (radius 35)
  - Up to the summit lookout at elevation about 310
- **Length:** about 4,860 studs at a steady 6.5% grade.
- **Road:**
  - 30 wide asphalt with paved shoulders (terrain material, so it's seamless)
  - Double yellow centre line and white edge lines (parts laid on the terrain surface)
  - Wooden guardrails wherever the edge drops off
  - 36 street lamps that light up at night
- **Summit lookout:**
  - Asphalt pad with parking stalls
  - Red/white radio tower with a blinking beacon
  - Equipment shed
  - Overlook railing, benches, coin binoculars
  - Summit sign
- **Tech:**
  - Road path + heights: `WorldTerrain.passPolyline` / `buildRoad`
  - The mountain is shaped to follow the road: `buildMassif`
  - Props: `Workspace.OverTake_Hub["OverTake Pass"]`

## Open ideas
- Timed hill-climb / downhill drift event
- Night touge races (fits the night-heat system)

Related: [[Off-Road Park]] · [[Hub Terrain]] · [[OverTake Speedway]]
