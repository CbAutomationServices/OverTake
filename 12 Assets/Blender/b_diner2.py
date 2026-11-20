exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(52)
SS=flat("Steel","d4d8de",0.2,1.0); CHK=pbr("Checker","checker",(1,1,1)); PV=pbr("Pavement","walk",(0.85,0.85,0.83)); BR=pbr("Brick","brick",(0.9,0.75,0.65))
GL=flat("Glass","2a3a46",0.05); FR=flat("ChromeFrame","e6e9ee",0.15,1.0); RED=flat("DinerRed","c3201e",0.35); CRM=flat("Cream","f2ead7",0.45); TEAL=flat("Teal","1fa6a0",0.4)
NEONR=flat("NeonRed","ff2d3c",0.3,emit=6.0); NEONT=flat("NeonTeal","2fe0d8",0.3,emit=5.5); NEONY=flat("NeonYellow","ffd23a",0.3,emit=5.5); WARM=flat("InteriorWarm","ffdca8",0.3,emit=1.8)
BOOTH=flat("BoothRed","9e1a1a",0.45); COUNTER=flat("Counter","e9e4d8",0.3); BLK=flat("Black","121212",0.6); UMB=flat("Umbrella","c3201e",0.6); UMB2=flat("UmbrellaW","f0ece2",0.6)
JUKE=flat("Jukebox","ff8a2a",0.3,emit=3.0); GB=flat("GlassBlock","b9d6e0",0.15,0.0)
L,Dd,H=22.0,7.0,4.2; FZ=-Dd/2; bz=0.6
box((0,0,bz/2),(L+Dd,Dd+0.2,bz),CHK,uv=1.0)
box((0,0,bz+H/2),(L,Dd,H),SS,uv=1.0)
for s in (-1,1):
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=Dd/2,depth=H,location=(s*L/2,0,bz+H/2)); o=bpy.context.object; o.data.materials.append(SS); uvbox(o,1.0)
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=Dd/2+0.02,depth=0.18,location=(s*L/2,0,bz+0.55)); o=bpy.context.object; o.data.materials.append(RED)
    bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=Dd/2+0.03,depth=0.08,location=(s*L/2,0,bz+H-0.2)); o=bpy.context.object; o.data.materials.append(NEONT)
for z,(m,th) in ((bz+0.55,(RED,0.18)),(bz+H-0.2,(NEONT,0.08))):
    box((0,FZ-0.03,z),(L,0.06,th),m); box((0,-FZ+0.03,z),(L,0.06,th),m)
for k in range(30): box((0,FZ-0.05,bz+0.75+k*0.012*0),(L,0.0,0.0),SS) if False else None
# fluted steel band below windows
for k in range(5): box((0,FZ-0.04,bz+0.8+k*0.12),(L,0.04,0.04),FR)
# windows with interior: booths, counter, stools, lamps
box((0,FZ-0.03,bz+2.55),(L-0.6,0.05,1.7),GL)
for k in range(13): box((-L/2+0.3+k*(L-0.6)/12,FZ-0.07,bz+2.55),(0.09,0.1,1.8),FR)
box((0,FZ+0.03,bz+3.5),(L-0.6,0.06,0.12),FR)
box((0,FZ+2.4,bz+2.2),(L-1,0.1,3.0),WARM)
for k in range(9): 
    x=-L/2+1.6+k*2.35; box((x,FZ+0.9,bz+0.75),(1.5,0.55,1.1),BOOTH); box((x,FZ+1.5,bz+1.05),(0.9,0.6,0.08),COUNTER)
    sphere((x,FZ+1.2,bz+3.6),0.18,NEONY,1)
box((0,FZ+3.0,bz+1.2),(L-3,0.8,1.1),COUNTER)
# barrel roof + red trim
bpy.ops.mesh.primitive_cylinder_add(vertices=32,radius=Dd/2+0.35,depth=L+0.4,location=(0,0,bz+H),rotation=(0,math.radians(90),0)); o=bpy.context.object; o.scale=(0.3,1,1); o.data.materials.append(CRM); uvbox(o,1.0)
box((0,FZ-0.36,bz+H+0.05),(L+0.4,0.08,0.22),RED)
# entrance: glass-block vestibule, chrome canopy, neon OPEN
box((0,FZ-1.5,bz+1.8),(4.0,3.0,3.6),SS)
for gx in range(-3,4):
    for gz in range(0,6):
        if abs(gx)<=1 and gz<5: continue
        box((gx*0.5,FZ-3.02,bz+0.3+gz*0.55),(0.46,0.06,0.5),GB)
box((0,FZ-3.04,bz+1.35),(1.6,0.06,2.6),GL); box((0,FZ-3.08,bz+2.75),(1.8,0.08,0.12),FR)
box((0,FZ-2.2,bz+3.75),(5.2,4.6,0.22),SS,bev=0.06); box((0,FZ-4.52,bz+3.75),(5.2,0.06,0.22),NEONR)
box((1.4,FZ-3.06,bz+3.0),(1.2,0.04,0.4),NEONR)
for i in range(3): box((0,FZ-3.3-i*0.4,bz-0.15-i*0.15),(3.4,0.4,0.3),CHK)
for s in (-1,1): cyl((s*1.9,FZ-3.6,0.6),0.05,1.2,FR,8)
# big rooftop sign: star + arrow
box((0,0.3,bz+H+2.9),(11,0.5,2.4),CRM,bev=0.08); box((0,0.03,bz+H+2.9),(10.2,0.04,1.7),RED)
for z in (bz+H+1.75,bz+H+4.05): box((0,0.0,z),(11,0.05,0.1),NEONT)
for x in (-5.5,5.5): box((x,0.0,bz+H+2.9),(0.1,0.05,2.4),NEONT)
for x in (-3.5,3.5): box((x,0.4,bz+H+1.4),(0.2,0.2,1.2),SS)
for a in range(5):                                                    # neon star
    ang=math.radians(90+a*72); box((6.6+math.cos(ang)*0.6,0.0,bz+H+4.4+math.sin(ang)*0.6),(0.15,0.05,1.2),NEONY,rot=(0,-ang+math.radians(90),0))
# kitchen annex
box((4,Dd/2+3,2.2),(10,6,4.4),BR,uv=1.6); box((7,Dd/2+3,4.9),(1.2,1.2,1.0),SS); box((1,Dd/2+3,4.7),(1.6,1.6,0.6),SS)
# patio: tables + umbrellas
box((-15.5,FZ-2.2,0.12),(7,6,0.24),CHK,uv=1.0)
for (x,y) in ((-17.5,FZ-0.8),(-13.8,FZ-0.8),(-17.5,FZ-3.8),(-13.8,FZ-3.8)):
    cyl((x,y,0.5),0.5,0.06,COUNTER,16); cyl((x,y,0.3),0.06,0.5,FR,8); cyl((x,y,1.4),0.04,2.6,FR,8)
    bpy.ops.mesh.primitive_cone_add(vertices=16,radius1=1.3,depth=0.45,location=(x,y,2.65)); o=bpy.context.object; o.data.materials.append(UMB if (x+y)%2<1 else UMB2)
box((-12.2,FZ-2.2,0.85),(0.6,0.5,1.5),JUKE,bev=0.05)
for x in (-19.4,-11.8): planter(x,FZ-5.6,1.4,1.4,None,1)
# lot: stripes, light poles, neon pylon w/ arrow, menu board
box((0,FZ-9,0.05),(L+22,17,0.1),PV,uv=2.5); stripes(-11,FZ-13,9,3.0,5.0)
for x in (-14,10): lightpole(x,FZ-16,8,1.6,1)
px=17
cyl((px,FZ-9,4.5),0.25,9,SS,12)
box((px,FZ-9,9.2),(5.4,0.6,2.4),RED,bev=0.08); box((px,FZ-9.32,9.2),(5.0,0.04,1.8),CRM)
for z in (7.95,10.45): box((px,FZ-9.34,z),(5.4,0.04,0.08),NEONR)
box((px+0.5,FZ-9,6.8),(3.6,0.5,0.9),NEONY,bev=0.05); prism((px+2.75,FZ-9,6.35),0.9,0.9,0.5,NEONY)
box((px,FZ-9,5.4),(2.4,0.4,0.8),TEAL,bev=0.05); box((px,FZ-9.22,5.4),(2.0,0.04,0.5),NEONT)
box((10,FZ-4,1.2),(2.2,0.3,1.6),BLK,bev=0.04); box((10,FZ-4.16,1.2),(2.0,0.02,1.4),WARM)   # menu board
for x in (-8,8): bollard(x,FZ-1.3,RED)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_diner2.png",(-24,-32,5),(-1,FZ-1,2.6),24,(1200,800),40)
else:
    export("OT_Diner_B",drop_y=-99)
