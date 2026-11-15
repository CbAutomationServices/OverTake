> **Status:** 🟡 v1 (built 2026-11-14)
# OVERTAKE PERFORMANCE (Workshop / Upgrade Shop)

Reusable model, same idea as the gas station: `ServerStorage > Prefabs > Workshop`.
Clone + `PivotTo(CFrame.new(x, groundY, z) * rotation)`. Bays face -Z, pivot at ground center, footprint 240 x 230 studs.
Placed in the hub as `Hub Center > OverTake Performance` (old gray block backed up in ServerStorage).
Inspiration: modern metal auto shop with glass roll-up doors + classic open-bay service shop.

## Outside
- Dark blue metal-panel siding with ribs, stone base, low gable roof, gutters + downspouts
- 4 bays with glass-panel roll-up doors (2 open, 2 closed), red bollards, wall lights, BAY 1-4 labels
- Big OVERTAKE PERFORMANCE sign with red neon underline + "UPGRADES · TUNING · PAINT"
- Office with storefront glass, canopy with red glow, CUSTOMER ENTRANCE sign, ramp
- **Paint & Wrap booth** attached on the side (white booth, glass front, lights, exhaust stack, car inside)
- Lot: stalls incl. blue accessible stall, customer cars, pylon sign (TUNING / DYNO / PAINT / WHEELS), feather flags, tire display, dumpsters, back fence, landscaped beds with trees, lamps

## Inside
| Bay (from the street, left to right) | What's there |
|---|---|
| Bay 1 | Alignment rack with a car + alignment tower/screen |
| Bay 2 (open) | **Dyno**: rollers in the floor, red car, big fan, monitor cart |
| Bay 3 | Two-post lift, car lowered |
| Bay 4 (open) | Two-post lift, car raised, oil drain, wheel off |
Back wall: red tool chests, workbenches with vises + pegboards of tools, tire shelves, oil drums, compressor, tire changer + wheel balancer. Ceiling LED strips, hose reels, exhaust fans, posters.
Office: counter with register + red logo, waiting chairs, TV, coffee station, wheel display wall, posters, plant.

## Gameplay hook
- `UpgradeZone` (invisible) in front of the bays: driving in will open the Upgrade Shop / customization menu
