exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(31)
BR=pbr("Brick","brick2",(0.95,0.88,0.82)); CO=pbr("Concrete","conc",(0.95,0.95,0.93)); PV=pbr("Pavement","walk",(0.9,0.9,0.88)); MT=pbr("Metal","metal",(0.6,0.6,0.62),0.8)
CR=pbr("Corrugated","corr",(0.55,0.57,0.6),0.6,True)
GL=flat("Glass","1c2833",0.05); FR=flat("Frame","1a1b1e",0.4); NAVY=flat("PoliceNavy","1b2f5c",0.4); BLUE=flat("GlowBlue","2f6dff",0.3,emit=5.0)
WHT=flat("PaintWhite","f0f0ee",0.6); YEL=flat("Yellow","e8b81e",0.5); RED=flat("GlowRed","ff2a2a",0.3,emit=4.0); FENCE=flat("Fence","8a8f96",0.5,0.7)
DOOR=flat("BayDoor","3a3f46",0.5,0.4); FLAG=flat("FlagRed","b8322a",0.7); GRN=flat("Hedge","3d5e2e",0.9); LAMP=flat("LampGlow","fff0cc",0.3,emit=4.0)
W,D,H=30.0,18.0,9.0; FZ=-D/2
box((0,0,H/2),(W,D,H),BR,uv=1.6)
box((0,0,0.6),(W+0.2,D+0.2,1.2),CO,bev=0.03)
box((0,FZ-0.06,H-0.9),(W+0.1,0.15,0.9),NAVY)                      # navy band
box((0,FZ-0.1,H-1.4),(W+0.1,0.06,0.1),BLUE)                         # glow line
box((0,0,H+0.2),(W+0.4,D+0.4,0.4),CO,bev=0.04)
# entrance block (taller, concrete) with canopy
ex=-4
box((ex,FZ-0.5,(H+2)/2),(9,1.2,H+2),CO,bev=0.04,uv=2.0)
box((ex,FZ-1.12,3.2),(6.4,0.06,5.6),GL)
for k in range(5): box((ex-3.2+k*1.6,FZ-1.16,3.2),(0.12,0.12,5.6),FR)
box((ex,FZ-1.16,1.6),(6.6,0.12,0.1),FR)
box((ex,FZ-3.6,6.4),(10,5.0,0.5),CO,bev=0.05)                         # canopy
for x in (ex-4.4,ex+4.4): box((x,FZ-5.8,3.2),(0.45,0.45,6.4),MT)
box((ex,FZ-6.12,6.4),(10,0.06,0.25),NAVY); box((ex,FZ-6.15,6.15),(10,0.04,0.06),BLUE)
for x in (ex-3,ex,ex+3): box((x,FZ-3.6,6.13),(1.4,1.0,0.04),LAMP)
box((ex,FZ-1.2,H+0.9),(7,0.2,1.4),NAVY); box((ex,FZ-1.32,H+0.9),(6.4,0.04,0.9),WHT)   # sign (text later)
for s in (-1,1): box((ex+s*3.6,FZ-1.25,4.2),(0.35,0.35,0.6),BLUE)   # blue lamps by door
# windows along the left and right
for x in (-13,-10.5,4.5,7):
    for z in (2.6,6.0):
        window(x,FZ,z,1.6,1.8,GL,FR,CO,flat("Reveal","262626",0.9))
# sally port garage (right)
for x in (10.5,13.6):
    box((x,FZ-0.02,2.2),(2.6,0.1,4.0),DOOR,uv=1.0)
    for k in range(10): box((x,FZ-0.08,0.4+k*0.38),(2.6,0.04,0.05),FR)
    box((x,FZ-0.15,4.5),(2.9,0.2,0.3),NAVY)
box((12,FZ-0.25,5.2),(7,0.3,0.4),RED)                                  # red warning bar
# rooftop: antenna tower + units
box((8,3,H+1.3),(3,2,1.8),MT,bev=0.04); box((-10,3,H+1.0),(2,2,1.2),MT,bev=0.04)
for k in range(4):
    cyl((11+0.8*(k%2),5+0.8*(k//2),H+5),0.05,10,FENCE,6)
box((11.4,5.4,H+10.2),(0.3,0.3,0.6),RED)
for z in (H+2,H+4,H+6,H+8): box((11.4,5.4,z),(0.9,0.9,0.05),FENCE)
# fenced impound yard on the left side
yx=-W/2-6
box((yx,0,0.06),(12,D,0.12),PV,uv=2.5)
for i in range(13):
    cyl((yx-6+i,FZ,1.2),0.04,2.4,FENCE,6); cyl((yx-6+i,-FZ,1.2),0.04,2.4,FENCE,6)
box((yx,FZ,2.3),(12,0.04,0.04),FENCE); box((yx,-FZ,2.3),(12,0.04,0.04),FENCE)
box((yx,FZ,1.2),(12,0.02,2.2),flat("ChainLink","9aa0a6",0.5,0.6))
# parking + flag + planters
for i in range(6): box((-6+i*3.4,FZ-10,0.07),(0.15,5,0.02),WHT)
box((0,FZ-9,0.05),(W+10,12,0.1),PV,uv=2.5)
cyl((-13,FZ-6,7),0.08,14,MT,10); box((-12,FZ-6,13.2),(2,0.05,1.2),FLAG)
for x in (-12,4): box((x,FZ-1.6,0.55),(3,1.2,1.1),CO,bev=0.04); box((x,FZ-1.6,1.15),(2.8,1.0,0.3),GRN)
for x in (-1.5,-6.5): cyl((x,FZ-6.5,0.6),0.18,1.2,YEL,12)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_police.png",(-30,-42,7),(-2,FZ,4),26,(1100,800),36)
else:
    export("OT_Police_A",drop_y=-99)
