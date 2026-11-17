> **Status:** 🟡 v1 (built 2026-11-14). Replaces the old hub oval (backed up in ServerStorage).
# OverTake Speedway

Main inspiration: NFS Heat's old Palm City speedway (weathered concrete, giant cantilever stands, press box, light towers), original name/branding.
Studio: `OverTake_Hub > OverTake Speedway`. Center ~ (720, 1650), next to the off-road park (east of it).

## Track
- Oval, long axis east-west: 680-stud straights, 250-radius turns, **70-stud wide**
- **15° banked turns** with smooth transitions in/out; inner edge at ground, outer edge ~18 studs up
- Outer concrete walls + catch fence, inner apron, yellow/white lines, checkered start/finish on the front stretch
- Pit road + pit wall + pit boxes inside the front stretch
- **Track Access gate** in the back-straight wall (only way in for cars right now)

## Stands
- **Main grandstand** on the front stretch: 2 sections, 26 rows, aisles with yellow rails, ENTRANCE vomitories, ad panels, huge concrete cantilever roofs with struts, back facade with windows
- **Press box** in the middle: red frame, glass booth, OVERTAKE SPEEDWAY sign, winged logo, antennas
- **Curved turn grandstand** around the west turn with partial roof + big sign facing the off-road park
- 9 **light towers** (lights ready for night)

## Infield: Stunt Park
- Big concrete **half-pipe** (west), drive-through **concrete tube**
- **Mega jump** ("SEND IT" gantry) over stacked containers
- **Wall ride** (east): banked 30° into a 72° wall
- 2 **quarter pipes**, a **spine ramp**, 4 kickers
- 2 **drift circles** with tire-stack centers, cone gymkhana, jersey barriers, tire walls
- **Scoreboard** facing the grandstand (STUNT SCORE / OVERTAKE STUNT PARK)
- Weathered pad: cracks, stains, weeds
- `StuntZone` part for stunt scoring

## Around it
- Back straight: old team garages/warehouse with red band + windows, mural, RACE THE NIGHT billboard, chain-link fence, tire piles, drums, big concrete pipe, OVERTAKE flag
- Parking lot (north) with islands, trees, light poles, cars; entrance plaza with ticket booths + OVERTAKE SPEEDWAY arch + flags
- Roads: from the N-S avenue end, from Tuner Row, a service loop around the stadium, a road to the track gate
- **Gravel link to the off-road trail loop** (west side)
- Backdrop hills south + east (past the map edge) with ~260 evergreens

## Numbers
- ~6,300 parts in the speedway; ~34,500 in the whole hub. **Phones:** turn on StreamingEnabled before testing on mobile.

## Open questions
- [ ] Second entrance from the parking lot side (tunnel under the stands?)
- [ ] Track for races: which tier classes use it, laps, AI?
- [ ] What goes in the empty land where the old oval was (east of the hub)?

## Detail pass (2026-11-16): Daytona-style frontstretch
Built by `ServerStorage.SpeedwayKit`. The old main grandstand is kept in `ServerStorage.OldSpeedwayParts`.
- **Main grandstand** (x 392..1048), about 800 parts with one invisible collider:
  - Sponsor podium and glass fence
  - Lower deck (blue, 20 rows, 5 sections) with stair aisles, handrails and section tunnels
  - Glass suite level with a warm light strip
  - Upper deck (red, 15 rows)
  - Steel back facade with a banner, and 5 gate towers with glass escalators facing the entrance plaza
  - Cantilever truss roof with lights underneath
  - Big video board on the roof, Race Control box in the centre
  - End walls
- **SAFER barrier** (steel and blue) on the track side of every outer wall.
- **Sponsor boards** along both straightaway walls (fake brands: NITRO-X, Rain City Tires, Cascade Oil, Heat Energy, Turbo Cola, and others).
- **Start/finish:** checkered line at x 720 with a flag stand hanging over the track (green flag).
- **Scoring pylon** in the turn-3 infield: 12 position rows, lap counter, OT crown, beacon.
- **Track surface** recoloured to dark race asphalt, with a lighter apron and pit lane.

