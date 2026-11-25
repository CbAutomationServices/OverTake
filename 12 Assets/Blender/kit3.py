exec(open("/home/claude/blender/kit2.py").read())
import bmesh
def frustum(loc,wb,lb,wt,lt,h,m,rz=0.0,shift=0.0,uv=1.5):
    """box tapering from (wb x lb) at bottom to (wt x lt) at top; shift moves the top along x"""
    me=bpy.data.meshes.new("fr"); bm=bmesh.new()
    pts=[(-lb/2,-wb/2,0),(lb/2,-wb/2,0),(lb/2,wb/2,0),(-lb/2,wb/2,0),(-lt/2+shift,-wt/2,h),(lt/2+shift,-wt/2,h),(lt/2+shift,wt/2,h),(-lt/2+shift,wt/2,h)]
    v=[bm.verts.new(p) for p in pts]
    for f in ((0,3,2,1),(4,5,6,7),(0,1,5,4),(1,2,6,5),(2,3,7,6),(3,0,4,7)): bm.faces.new([v[i] for i in f])
    bm.to_mesh(me); bm.free(); o=bpy.data.objects.new("fr",me); bpy.context.scene.collection.objects.link(o)
    o.location=loc; o.rotation_euler=(0,0,rz); o.data.materials.append(m); uvbox(o,uv); return o
def cone(loc,r1,r2,depth,m,verts=10,rot=None):
    bpy.ops.mesh.primitive_cone_add(vertices=verts,radius1=r1,radius2=r2,depth=depth,location=loc); o=bpy.context.object
    if rot: o.rotation_euler=rot
    o.data.materials.append(m); uvbox(o,1.0); return o
def ico(loc,scale,m,sub=1,rot=(0,0,0),uv=2.0):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=sub,radius=1,location=loc); o=bpy.context.object
    o.scale=scale; o.rotation_euler=rot; o.data.materials.append(m); uvbox(o,uv); return o
CONC=lambda: T_("Concrete","plaster",(0.8,0.8,0.78))
CONC2=lambda: T_("ConcLight","plaster",(0.86,0.86,0.84))
GALV=lambda: C("Galv","b4b9bf",0.35,0.6)
ASPH=lambda: T_("Asphalt","walk",(0.42,0.42,0.43),0.0,True)
POLE=lambda: C("PoleDark","2a2c30",0.45,0.6)
WHITE=lambda: C("PaintWhite","f0f0ee",0.6)
YELW=lambda: C("PaintYellow","e8b81e",0.6)
def car2(x,y,rz=0.0,col="c4261d",z0=0.0,kind="sedan"):
    B=C(f"Car{col}",col,0.22,0.65); G=C("CarGlass","141c24",0.04,0.3); T=C("Tire","151515",0.85); R=C("Rim","c9ccd1",0.25,0.9)
    BL=C("CarTrim","121212",0.5); ca,sa=math.cos(rz),math.sin(rz)
    def L(dx,dy,dz): return (x+dx*ca-dy*sa, y+dx*sa+dy*ca, z0+dz)
    Lg=4.5 if kind=="sedan" else 4.6; Wd=1.86
    frustum(L(0,0,0.32),Wd,Lg,Wd*0.97,Lg*0.98,0.5,B,rz)                                     # lower body
    frustum(L(0.15,0,0.82),Wd*0.97,Lg*0.96,Wd*0.94,Lg*0.9,0.12,B,rz)                         # shoulder
    hood=0.0 if kind=="sedan" else 0.35
    frustum(L(-0.25,0,0.94),Wd*0.86,2.6,Wd*0.74,1.5 if kind=="sedan" else 2.2,0.52+hood,G,rz,shift=-0.15)   # glasshouse
    frustum(L(-0.25+(-0.15),0,1.46+hood),Wd*0.74,1.5 if kind=="sedan" else 2.2,Wd*0.7,1.35 if kind=="sedan" else 2.05,0.05,B,rz) # roof skin
    for s in (-1,1):
        box(L(Lg/2-0.02,s*0.6,0.72),(0.06,0.42,0.14),C("HeadLight","fff6e0",0.3,emit=3.0),rot=(0,0,rz))
        box(L(-Lg/2+0.02,s*0.62,0.78),(0.06,0.4,0.12),C("TailLight","ff2020",0.3,emit=3.0),rot=(0,0,rz))
    box(L(Lg/2+0.01,0,0.5),(0.06,1.2,0.22),BL,rot=(0,0,rz)); box(L(-Lg/2-0.01,0,0.45),(0.06,1.5,0.2),BL,rot=(0,0,rz))
    box(L(Lg/2+0.03,0,0.5),(0.02,0.5,0.12),C("Grille","2a2a2a",0.5,0.6),rot=(0,0,rz))
    for dx in (-1.45,1.45):
        for dy in (-0.9,0.9):
            cyl(L(dx,dy,0.36),0.36,0.26,T,16,rot=(math.radians(90),0,rz)); cyl(L(dx,dy*1.02,0.36),0.24,0.27,R,10,rot=(math.radians(90),0,rz))
    for s in (-1,1): box(L(0.55,s*0.98,1.0),(0.18,0.1,0.08),BL,rot=(0,0,rz))       # mirrors
