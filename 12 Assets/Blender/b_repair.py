exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(41)
CB=pbr("Block","conc",(0.92,0.9,0.86)); PL=pbr("Stucco","plaster",(0.95,0.9,0.78)); PV=pbr("Pavement","walk",(0.85,0.85,0.83)); MT=pbr("Metal","metal",(0.6,0.6,0.62),0.8)
CR=pbr("Corrugated","corr",(0.6,0.62,0.66),0.6,True); RUST=pbr("Rust","metal",(0.75,0.5,0.35),0.5)
GL=flat("Glass","1e2a33",0.05); FR=flat("Frame","1a1b1e",0.4); DOOR=flat("RollDoor","b8b8b4",0.5,0.4); DARK=flat("BayInterior","15161a",0.9)
RED=flat("ShopRed","b5261e",0.45); YEL=flat("Yellow","e8b81e",0.5); TIRE=flat("Tire","151515",0.85); LIFT=flat("LiftBlue","2a5fb0",0.4,0.5)
SIGN=flat("SignPanel","f2efe6",0.5); NEON=flat("NeonRed","ff3b2a",0.3,emit=5.0); LAMP=flat("LampGlow","fff0cc",0.3,emit=4.0)
CAR1=flat("CarBodyA","3d6e9e",0.35,0.3); CAR2=flat("CarBodyB","8e2b22",0.35,0.3); BLK=flat("Black","121212",0.6)
W,D,H=30.0,16.0,6.5; FZ=-D/2
box((0,0,H/2),(W,D,H),CB,uv=1.2)
box((0,FZ-0.05,H-0.6),(W+0.1,0.15,1.2),RED)                      # red fascia band
box((0,0,H+0.15),(W+0.3,D+0.3,0.3),MT)
# office (left, stucco) with windows
ox=-11.5
box((ox,FZ-0.1,H/2),(7,0.25,H),PL,uv=1.5)
box((ox,FZ-0.25,2.0),(5.6,0.06,2.4),GL); box((ox,FZ-0.3,3.25),(5.8,0.1,0.1),FR); box((ox,FZ-0.3,0.8),(5.8,0.1,0.1),FR)
for k in range(4): box((ox-2.8+k*1.87,FZ-0.3,2.0),(0.1,0.1,2.4),FR)
box((ox,FZ-1.2,3.6),(6.4,2.0,0.12),RED,rot=(math.radians(-10),0,0))
# 4 bays: two open (dark interior + lift), two closed
for i,x in enumerate((-4.5,1.5,7.5,13.0)):
    w=5.0
    if i in (0,2):
        box((x,FZ-0.04,2.2),(w,0.06,4.4),DARK); box((x,FZ-0.08,4.2),(1.4,0.04,0.08),LAMP)
        for s in (-1,1): box((x+s*1.6,FZ-0.1,1.0),(0.25,0.06,2.0),LIFT)
        box((x,FZ+2.5,0.1),(w-0.4,4,0.2),PV)
        for s in (-1,1): box((x+s*1.6,FZ+2.6,1.0),(0.25,0.25,2.0),LIFT)
        box((x,FZ+2.6,1.9),(3.6,0.4,0.15),LIFT)
        box((x,FZ+2.8,4.2),(1.4,0.3,0.06),LAMP)
    else:
        box((x,FZ-0.02,2.2),(w,0.1,4.4),DOOR,uv=1.0)
        for k in range(12): box((x,FZ-0.08,0.3+k*0.36),(w,0.04,0.05),FR)
    box((x,FZ-0.15,4.6),(w+0.4,0.25,0.3),MT)
    for s in (-1,1): box((x+s*(w/2+0.25),FZ-0.15,2.3),(0.35,0.3,4.6),CB)
# rooftop sign with neon outline
box((3,FZ+0.6,H+2.0),(14,0.4,2.8),SIGN,bev=0.04)
for z in (H+0.62,H+3.38): box((3,FZ+0.37,z),(14,0.06,0.1),NEON)
for x in (-4,10): box((x,FZ+0.37,H+2.0),(0.1,0.06,2.8),NEON)
for x in (-1,7): box((x,FZ+0.9,H+0.6),(0.25,0.25,1.2),MT)
# yard props: tire stacks, drums, project car, side fence
for (x,y,n) in ((-15.5,FZ-1.5,5),(-14.5,FZ-1.8,4),(17.5,FZ-1.2,6),(16.6,FZ-2.2,3)):
    for k in range(n): cyl((x,y,0.15+k*0.28),0.38,0.26,TIRE,14)
for (x,y) in ((18.5,FZ+1),(18.5,FZ+2.2),(19.6,FZ+1.6)): cyl((x,y,0.55),0.32,1.1,[RED,flat("DrumBlue","2a4f7e",0.5),YEL][int(y)%3],12)
# tool chests, air compressor, engine stand, oil drums by the open bays
for x in (-6.6,5.4): box((x,FZ+4.4,0.6),(1.2,0.6,1.2),RED,bev=0.04)
box((-2.3,FZ+4.6,0.8),(0.8,0.8,1.6),flat("Compressor","2a5fb0",0.4,0.4),bev=0.05)
box((9.6,FZ+4.0,0.9),(0.9,0.9,0.9),flat("Engine","3b3b3e",0.5,0.7),bev=0.08)
for k,x in enumerate((-17.8,-17.0)): cyl((x,FZ+2,0.55),0.32,1.1,[RED,YEL][k],12)
box((-7,FZ-3.5,0.6),(2.2,1.0,1.2),flat("Dumpster","2f5d3a",0.6,0.3),bev=0.05)
box((W/2+0.2,2,1.2),(0.08,D-2,2.4),CR)                                  # side fence
box((0,FZ-6,0.05),(W+8,13,0.1),PV,uv=2.5)
for x in (-8.5,-1.5): cyl((x,FZ-0.6,0.6),0.18,1.2,YEL,12)
cyl((-17,FZ-4,4),0.12,8,MT,10); box((-17,FZ-4,8.2),(2.4,0.3,1.4),SIGN); box((-17,FZ-4.16,8.2),(2.2,0.04,0.1),NEON)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_repair.png",(-26,-36,6),(0,FZ,3),26,(1100,800),36)
else:
    export("OT_RepairShop_A",drop_y=-99)
