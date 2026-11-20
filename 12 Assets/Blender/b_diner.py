exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(51)
SS=flat("Steel","d4d8de",0.22,1.0); PV=pbr("Pavement","walk",(0.85,0.85,0.83)); TL=pbr("Tile","tile",(1,1,1)); BR=pbr("Brick","brick",(0.9,0.75,0.65))
GL=flat("Glass","2a3a46",0.05); FR=flat("Frame","c9ccd1",0.25,0.9); RED=flat("DinerRed","c3201e",0.35); CRM=flat("Cream","f2ead7",0.45)
NEONR=flat("NeonRed","ff2d3c",0.3,emit=6.0); NEONB=flat("NeonTeal","2fe0d8",0.3,emit=5.0); LAMP=flat("Interior","ffe2b0",0.3,emit=2.0)
BOOTH=flat("BoothRed","8f1818",0.5); BLK=flat("Black","121212",0.6); WHT=flat("PaintWhite","f0f0ee",0.6); YEL=flat("Yellow","e8b81e",0.5)
L,Dd,H=22.0,7.0,4.0; FZ=-Dd/2
# body: steel box with rounded ends
box((0,0,H/2+0.6),(L,Dd,H),SS,uv=1.0)
for s in (-1,1):
    bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=Dd/2,depth=H,location=(s*L/2,0,H/2+0.6)); o=bpy.context.object; o.data.materials.append(SS); uvbox(o,1.0)
box((0,0,0.3),(L+Dd,Dd-0.2,0.6),TL,uv=1.0)                       # tile skirt
box((0,FZ-0.03,1.0),(L,0.08,0.18),RED); box((0,-FZ+0.03,1.0),(L,0.08,0.18),RED)
# window band + interior glow + booths
box((0,FZ-0.04,2.9),(L-1,0.06,1.7),GL)
for k in range(12): box((-L/2+0.5+k*(L-1)/11,FZ-0.08,2.9),(0.08,0.1,1.8),FR)
box((0,FZ+0.6,2.6),(L-1.5,0.1,2.0),LAMP)
for k in range(8): box((-L/2+2+k*2.6,FZ+0.9,1.4),(1.6,0.6,0.9),BOOTH)
box((0,FZ-0.06,4.0),(L,0.1,0.3),RED); box((0,FZ-0.12,4.15),(L,0.04,0.06),NEONR)
box((0,FZ-0.06,1.9),(L,0.1,0.12),FR)
# barrel roof
bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=Dd/2+0.3,depth=L,location=(0,0,H+0.6),rotation=(0,math.radians(90),0)); o=bpy.context.object; o.scale=(1,1,0.28); o.data.materials.append(CRM); uvbox(o,1.0)
# entrance vestibule (center front)
box((0,FZ-1.4,2.3),(3.6,2.8,3.4),SS,uv=1.0); box((0,FZ-2.82,1.6),(1.8,0.06,2.6),GL); box((0,FZ-2.86,3.15),(3.6,0.1,0.3),RED)
box((0,FZ-1.4,4.1),(4.2,3.2,0.25),CRM)
for i in range(3): box((0,FZ-3.2-i*0.35,0.45-i*0.15),(3.0,0.35,0.3),TL)
# rooftop neon sign
box((0,0,H+2.8),(10,0.5,2.2),CRM,bev=0.06); box((0,-0.27,H+2.8),(9.4,0.04,1.6),RED)
for z in (H+1.75,H+3.85): box((0,-0.3,z),(10,0.05,0.1),NEONB)
for x in (-5,5): box((x,-0.3,H+2.8),(0.1,0.05,2.2),NEONB)
for x in (-3,3): box((x,0.1,H+1.5),(0.2,0.2,1.2),SS)
# kitchen annex (brick) behind
box((4,Dd/2+3,2.2),(10,6,4.4),BR,uv=1.6); box((7,Dd/2+3,4.9),(1.2,1.2,1.0),SS)
# lot: stripes, pylon sign with arrow
box((0,FZ-8,0.05),(L+18,16,0.1),PV,uv=2.5)
for i in range(8): box((-12+i*3.4,FZ-12,0.07),(0.15,5,0.02),WHT)
px=16
cyl((px,FZ-9,4),0.25,8,SS,12)
box((px,FZ-9,8.6),(5,0.6,2.2),RED,bev=0.06); box((px,FZ-9.32,8.6),(4.6,0.04,1.6),CRM)
for z in (7.45,9.75): box((px,FZ-9.34,z),(5,0.04,0.08),NEONR)
box((px+0.5,FZ-9,6.4),(3.4,0.5,0.9),YEL,bev=0.05); prism((px+2.6,FZ-9,6.4-0.45),0.9,0.9,0.5,YEL,rot_z=0)
for x in (-9,9): cyl((x,FZ-1.2,0.5),0.18,1.0,YEL,12)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_diner.png",(-20,-30,5),(1,FZ-1,2.6),26,(1100,800),36)
else:
    export("OT_Diner_A",drop_y=-99)
