> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# Map Redesign v3

Replaces the current hub layout. Everything gets rebuilt with the new Blender mesh kit → [[City Kit - Building List]].

## Goals (Cristian, 2026-11-20)
- **Bigger:** ~12,000 × 12,000 studs (~3.4 km a side, about 3× today's map)
- **Open driving:** long highway runs, not just city blocks (reference: Forza Horizon-style map)
- **A city that feels alive:** dense, varied buildings, props, signs, things to look at
- **Runs on phones** (budget below)

## Regions (proposed layout: concept map in this folder)
| Region | What's there | Driving it gives you |
|---|---|---|
| **Downtown** (generic big US city) | Skyscrapers, offices, bank, hotel, police HQ, plaza, elevated train (scenery) | Tight street racing, night chases |
| **Inner neighborhoods** | Tenements, walk-ups, brownstones, storefront rows, diner, tuner shop | The "lived-in" streets |
| **The Garage hub** | Player Garage (start + safehouse), dealership, meet lot, takeover lot | Hangout, starting point |
| **Ring highway** | Loop around the city, interchanges, tunnels, a bridge over the bay | High-speed loop, cop chases |
| **Harbor / port** | Container yard, cranes, warehouses, docks, drag strip on the old runway | Industrial, wide open for drag + night |
| **Coast road** | Beach highway, cliffs, motel, rest stop, lighthouse | Long sweeping run |
| **Mountains** | Two touge passes (one paved, one gravel), lookout, tunnel | Technical driving, drifting |
| **Farmland + 2 small towns** | Fields, barns, a main-street town, gas station, motel | Long open straights, scenery |
| **Off-road park** | Trails, MX track, river ford | Off-road events |
| **Speedway** | Stadium oval + infield road course | Circuit races |

## Road types
- **Freeway:** 2–3 lanes each way, median, on-ramps; raised viaducts near the city
- **Highway:** 1–2 lanes each way through countryside and coast
- **City streets:** avenues + side streets + alleys
- **Mountain roads:** narrow, hairpins, guardrails
- **Dirt / gravel:** off-road park and farm roads

## Phone budget (non-negotiable)
| Item | Target |
|---|---|
| Total parts on the map | < 60,000 (today: 381,000) |
| Buildings | Meshes from the kit, 1–15 meshes each, ≤ 10k triangles per mesh |
| Far buildings | Simple low-detail versions (Model LevelOfDetail / streaming meshes) |
| Ground | Roblox Terrain for land; road meshes on top |
| Streaming | StreamingEnabled, tuned on a low-end phone |
| Texture reuse | One shared texture set per material (brick, concrete, glass…), not one per building |

## Build order
1. **Rough layout:** terrain shape + road network blockout (no detail yet). Drive it to test the flow.
2. City kit buildings (see list) → downtown + Garage hub first
3. Highways, bridges, tunnels
4. Venues: Speedway, Drag Strip, touge, off-road park
5. Countryside, towns, coast, port
6. Props + detail pass, then night lighting pass

## Open questions
- [ ] Sign off on the concept layout
- [ ] Bay/water on which side?
- [ ] Is the old map kept as a backup place? *(proposed: yes, copy it before we start)*
