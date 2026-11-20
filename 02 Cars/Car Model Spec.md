> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# Car Model Spec (for the partner)

How every car model must be built so the chassis, garage and paint system can use it without rework. **Build car #1 to this spec first**, then we test it in Studio before you make the rest.

## Size & orientation
- **Real-life scale:** about **15–17 studs long, 6.5–7.5 wide** for a normal sports car (1 stud ≈ 0.28 m).
- **Front of the car faces −Z** (Roblox "forward"). Pivot at **ground level, center of the car**.
- Wheels touching the ground at the pivot height.

## Model layout (names must match exactly)
```
CarName (Model)          ← PrimaryPart = Root
├─ Root                  invisible box, roughly the car's footprint (the chassis uses this)
├─ Body (folder)         all MeshParts, CanCollide OFF, Massless ON
│   ├─ Paint             the paintable body shell (ONE MeshPart, or several all named Paint)
│   ├─ Glass             windows (separate so tint can change)
│   ├─ Trim              black plastics, grille, etc.
│   └─ Interior          seats, dash (low detail is fine)
├─ Wheels (folder)
│   ├─ FL / FR / RL / RR each a Model: Tire + Rim (separate MeshParts, so rims can be swapped)
│   │                     center of the wheel = center of the model
├─ Lights (folder)       Headlight_L/R, Taillight_L/R, BrakeLight_L/R (Neon parts or SurfaceAppearance)
└─ Attachments on Root   DriverSeat, Exhaust_L, Exhaust_R (nitro flames), Underglow, CameraTarget
```

## Budgets (mobile-friendly)
| Item | Max |
|---|---|
| Body triangles | 10,000 |
| Each wheel (tire + rim) | 1,500 |
| Textures | 1024×1024, PBR (SurfaceAppearance) |
| Total parts in the model | ~40 |

## Rules
- **No real brands, badges or logos** (decided). Real-*looking* shapes are fine.
- No scripts inside the model.
- Export **FBX or GLB** from Blender. We import with the Studio import tool and check scale, orientation and textures together.
- Name the file with the car's slot from [[Car Stats]] (e.g. `03_StarterEuro.fbx`).

## Order to build
The 3 starters first (JDM, Muscle, Euro), then the rest of [[Car Stats]] from C upward.
