exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(32)
BR=pbr("Brick","brick2",(1.0,0.92,0.86)); CO=pbr("Concrete","conc",(0.95,0.95,0.93)); PV=pbr("Pavement","walk",(0.9,0.9,0.88)); ST=pbr("Stone","trim",(0.85,0.82,0.76))
GL=flat("Glass","1c2833",0.05); BGL=flat("BlueGlass","24476e",0.05,0.3); FR=flat("Frame","1a1b1e",0.4); NAVY=flat("PoliceNavy","1b2f5c",0.4)
BLUE=flat("GlowBlue","2f6dff",0.3,emit=6.0); RED=flat("GlowRed","ff2a2a",0.3,emit=5.0); WHT=flat("PaintWhite","f0f0ee",0.6); WARM=flat("InteriorWarm","ffe8c4",0.3,emit=1.5)
SIGNW=flat("SignWhiteGlow","f4f8ff",0.3,emit=3.0); MT=flat("SteelGrey","9aa0a6",0.35,0.85); FENCE=flat("Fence","8a8f96",0.5,0.7); DOOR=flat("BayDoor","3a3f46",0.5,0.4)
FLAG=flat("FlagRed","b8322a",0.7); FLAGB=flat("FlagBlue","24407a",0.7); BLK=flat("Black","141414",0.5); YEL=flat("Yellow","e8b81e",0.5); PBLUE=flat("PaintBlue","2a4f9e",0.6)
W,D,H=34.0,18.0,9.5; FZ=-D/2
box((0,0,H/2),(W,D,H),BR,uv=1.6)
box((0,0,0.6),(W+0.2,D+0.2,1.2),ST,bev=0.03)
box((0,FZ-0.06,H-0.8),(W+0.1,0.15,0.8),NAVY); box((0,FZ-0.12,H-1.25),(W+0.1,0.06,0.08),BLUE)
box((0,0,H+0.2),(W+0.4,D+0.4,0.4),CO,bev=0.04)
# vertical concrete fins across facade with windows between
for i in range(9):
    x=-16+i*2.6
    if -7<x<1: continue
    box((x,FZ-0.35,H/2),(0.4,0.7,H-1.0),CO,bev=0.03)
for x in (-14.7,-12.1,-9.5,2.3,4.9,7.5):
    for z in (2.7,6.1):
        box((x,FZ-0.02,z),(2.0,0.06,2.4),WARM); box((x,FZ-0.06,z),(2.0,0.04,2.4),GL); box((x,FZ-0.1,z-1.25),(2.2,0.14,0.12),CO)
# tall blue-glass entrance tower with lit POLICE sign
ex=-3
box((ex,FZ-0.6,(H+3)/2),(8,1.4,H+3),CO,bev=0.05,uv=2.0)
box((ex,FZ-1.32,(H+2)/2+0.2),(5.6,0.06,H+1.4),BGL)
for k in range(5): box((ex-2.8+k*1.4,FZ-1.36,(H+2)/2+0.2),(0.1,0.1,H+1.4),FR)
for z in (3.6,7.2,10.0): box((ex,FZ-1.36,z),(5.8,0.1,0.1),FR)
box((ex,FZ-1.45,H+2.2),(6.6,0.3,1.3),NAVY); box((ex,FZ-1.62,H+2.2),(6.0,0.04,0.85),SIGNW)   # lit sign (text later)
box((ex,FZ-4.0,4.2),(11,5.4,0.45),CO,bev=0.05)                                             # entrance canopy
box((ex,FZ-6.72,4.2),(11,0.06,0.3),NAVY); box((ex,FZ-6.75,3.98),(11,0.04,0.06),BLUE)
for x in (ex-3.5,ex,ex+3.5): box((x,FZ-4.0,3.96),(1.6,1.0,0.04),flat("LEDPanel","fff4e0",0.3,emit=6.0))
for x in (ex-5,ex+5): box((x,FZ-6.3,2.1),(0.45,0.45,4.2),MT)
box((ex,FZ-6.72,4.6),(3.0,0.4,0.35),BLK); box((ex-1,FZ-6.93,4.6),(1.2,0.04,0.25),RED); box((ex+1,FZ-6.93,4.6),(1.2,0.04,0.25),BLUE)   # light bar
for s in (-1,1): box((ex+s*3.3,FZ-1.45,3.0),(0.4,0.4,0.7),BLUE)
box((ex,FZ-1.36,1.5),(2.6,0.06,2.8),GL)
# ramp with rails + steps
box((ex+6,FZ-2.4,0.35),(4,1.6,0.7),ST,bev=0.03,rot=(0,math.radians(-4),0))
for k in range(4): cyl((ex+4.2+k*1.2,FZ-3.2,1.0),0.04,0.9,MT,8)
box((ex+6,FZ-3.2,1.45),(4.2,0.06,0.06),MT)
# sally port + gate arm + guard booth
for x in (12,15.2):
    box((x,FZ-0.02,2.3),(2.8,0.1,4.2),DOOR,uv=1.0)
    for k in range(11): box((x,FZ-0.08,0.4+k*0.38),(2.8,0.04,0.05),FR)
    box((x,FZ-0.15,4.65),(3.1,0.2,0.3),NAVY)
box((13.6,FZ-0.25,5.3),(7,0.3,0.35),RED)
box((18.6,FZ-6,1.4),(2.0,2.0,2.8),CO,bev=0.04); box((18.6,FZ-7.02,1.7),(1.6,0.04,1.2),WARM); box((18.6,FZ-6,2.95),(2.4,2.4,0.2),NAVY)
box((15,FZ-6.6,1.1),(6,0.15,0.15),WHT); box((12.3,FZ-6.6,0.6),(0.4,0.4,1.0),YEL)
# CCTV cams + wall lamps
for x in (-16.8,16.8): box((x,FZ-0.3,H-1.6),(0.3,0.6,0.25),WHT)
for x in (-12,6,10): box((x,FZ-0.25,4.4),(0.4,0.4,0.4),flat("WallLamp","fff0cc",0.3,emit=4.0))
# roof: mast w/ dish + units
box((8,3,H+1.3),(3,2,1.8),MT,bev=0.04); box((-12,3,H+1.0),(2,2,1.2),MT,bev=0.04)
cyl((13,5,H+6),0.25,12,FENCE,10)
for z in (H+3,H+6,H+9): box((13,5,z),(1.4,0.08,0.08),FENCE)
bpy.ops.mesh.primitive_uv_sphere_add(radius=0.9,location=(13.6,5,H+9.5),segments=16,ring_count=8); o=bpy.context.object; o.scale=(0.4,1,1); o.data.materials.append(WHT); uvbox(o,1.0)
box((13,5,H+12.2),(0.35,0.35,0.5),RED)
# impound yard: real chain-link look with posts + rails
yx=-W/2-6.5
box((yx,0,0.06),(12,D,0.12),PV,uv=2.5)
for side in (FZ,-FZ):
    for i in range(13): cyl((yx-6+i,side,1.3),0.05,2.6,FENCE,6)
    for z in (0.2,1.3,2.5): box((yx,side,z),(12,0.04,0.04),FENCE)
    for i in range(48): box((yx-6+i*0.25,side,1.3),(0.015,0.015,2.3),FENCE,rot=(0,math.radians(30 if i%2 else -30),0))
box((yx-6,0,1.3),(0.04,D,0.04),FENCE)
# police-only bays + flag trio + planters + bike rack + light poles
box((0,FZ-11,0.05),(W+16,16,0.1),PV,uv=2.5)
for i in range(4): box((-15+i*3.2,FZ-12,0.075),(3.0,5.4,0.02),PBLUE)
stripes(-16.6,FZ-12,5,3.2,5.4); stripes(0,FZ-12,6,3.0,5.0)
for i,(x,f) in enumerate(((-18,FLAG),(-16.8,flat("FlagWhite","eeeeea",0.7)),(-15.6,FLAGB))):
    cyl((x,FZ-7,7),0.08,14,MT,10); box((x+0.9,FZ-7,13.2),(1.8,0.05,1.1),f)
box((-17,FZ-7,0.5),(4.6,2.0,1.0),ST,bev=0.04)
for x in (-11.5,5.5): planter(x,FZ-2.2,3.6,1.3,None,3)
for k in range(5): box((9+k*0.6,FZ-3,0.5),(0.05,1.0,0.9),MT)
for x in (-20,6,20): lightpole(x,FZ-17,8.5,1.6,1)
for x in (-7.5,1.5): bollard(x,FZ-7.4,YEL)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_police2.png",(-34,-46,8),(-1,FZ-2,4),24,(1200,820),40)
else:
    export("OT_Police_B",drop_y=-99)
