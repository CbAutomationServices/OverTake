exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(42)
CB=pbr("Block","conc",(0.92,0.9,0.86)); CR=pbr("Corrugated","corr",(0.72,0.74,0.78),0.6,True); PV=pbr("Pavement","walk",(0.85,0.85,0.83)); WD=pbr("Wood","wood",(0.8,0.62,0.45))
BR=pbr("Brick","brick",(0.85,0.7,0.62))
GL=flat("Glass","1e2a33",0.05); FR=flat("Frame","1a1b1e",0.4); DOOR=flat("RollDoor","c2c3bf",0.5,0.4); DARK=flat("BayInterior","24262b",0.8)
RED=flat("ShopRed","b5261e",0.45); YEL=flat("Yellow","e8b81e",0.5); TIRE=flat("Tire","151515",0.85); LIFT=flat("LiftBlue","2a5fb0",0.4,0.5)
SIGN=flat("SignPanel","f2efe6",0.5); NEONR=flat("NeonRed","ff3b2a",0.3,emit=6.0); NEONB=flat("NeonBlue","3aa0ff",0.3,emit=5.0); SHOPL=flat("ShopLight","f6fbff",0.3,emit=6.0)
TOOLB=flat("ToolBoard","5a5f66",0.5,0.4); WARM=flat("InteriorWarm","ffe8c4",0.3,emit=1.4); MT=flat("SteelGrey","9aa0a6",0.35,0.85); STRIPE=flat("StripeBlack","1a1a1a",0.6)
W,D,H=32.0,16.0,7.0; FZ=-D/2
box((0,0,1.6),(W,D,3.2),CB,uv=1.2); box((0,0,3.2+(H-3.2)/2),(W,D,H-3.2),CR,uv=2.5)
box((0,FZ-0.06,3.35),(W+0.1,0.15,0.3),RED); box((0,FZ-0.06,3.0),(W+0.1,0.12,0.12),STRIPE)
box((0,0,H+0.15),(W+0.3,D+0.3,0.3),MT)
# office: brick, big window, striped awning, neon OPEN
ox=-12.5
box((ox,FZ-0.15,H/2),(7,0.35,H),BR,uv=1.6)
box((ox,FZ-0.35,2.2),(5.6,0.06,2.6),WARM); box((ox,FZ-0.39,2.2),(5.6,0.04,2.6),GL)
for k in range(4): box((ox-2.8+k*1.87,FZ-0.42,2.2),(0.1,0.1,2.6),FR)
for i in range(8): box((ox-2.8+i*0.8,FZ-1.25,3.85),(0.8,1.9,0.07),RED if i%2==0 else SIGN,rot=(math.radians(-15),0,0))
box((ox+1.6,FZ-0.43,2.9),(1.6,0.04,0.5),NEONR); box((ox-1.6,FZ-0.43,2.9),(1.2,0.04,0.4),NEONB)
# 4 bays: 2 open with lit interiors (lift, tool wall, lights), 2 closed
for i,x in enumerate((-4.5,1.6,7.7,13.8)):
    w=5.2
    if i in (0,2):
        box((x,FZ-0.04,2.3),(w,0.06,4.6),DARK)
        box((x,FZ-0.07,3.0),(w-0.8,0.04,1.2),TOOLB)
        for k in range(6): box((x-1.8+k*0.7,FZ-0.09,3.0),(0.1,0.04,0.7),[RED,YEL,MT][k%3])
        box((x,FZ-0.09,4.4),(3.4,0.04,0.12),SHOPL)
        for s in (-1,1): box((x+s*1.7,FZ-0.5,1.1),(0.3,0.3,2.2),LIFT); box((x+s*1.7,FZ-0.5,0.08),(0.8,0.8,0.12),LIFT)
        box((x-2.0,FZ-0.6,0.6),(0.9,0.5,1.2),RED,bev=0.04)
    else:
        box((x,FZ-0.02,2.3),(w,0.1,4.6),DOOR,uv=1.0)
        for k in range(12): box((x,FZ-0.08,0.3+k*0.38),(w,0.04,0.05),FR)
    box((x,FZ-0.15,4.8),(w+0.4,0.25,0.3),MT); box((x,FZ-0.3,5.2),(1.2,0.4,0.3),flat("WallLamp","fff0cc",0.3,emit=4.0))
    for s in (-1,1): box((x+s*(w/2+0.25),FZ-0.15,2.4),(0.35,0.3,4.8),CB)
    box((x,FZ-0.17,5.6),(1.0,0.06,0.7),YEL)                       # bay numbers
# tall vintage sign pole with neon + arrow
px=-18
cyl((px,FZ-5,5),0.2,10,MT,12)
box((px,FZ-5,9.4),(3.6,0.5,2.6),RED,bev=0.06); box((px,FZ-5.27,9.4),(3.2,0.04,2.0),SIGN)
for z in (8.15,10.65): box((px,FZ-5.28,z),(3.6,0.04,0.08),NEONR)
box((px+0.6,FZ-5,7.3),(2.6,0.4,0.8),YEL,bev=0.04); prism((px+2.25,FZ-5,6.9),0.8,0.8,0.4,YEL)
# roof sign
box((4,FZ+0.6,H+2.0),(15,0.4,2.8),SIGN,bev=0.04)
for z in (H+0.62,H+3.38): box((4,FZ+0.37,z),(15,0.06,0.1),NEONR)
for x in (-3.5,11.5): box((x,FZ+0.37,H+2.0),(0.1,0.06,2.8),NEONR)
for x in (0,8): box((x,FZ+0.9,H+0.6),(0.25,0.25,1.2),MT)
# tire display rack, tire stacks, pallets, drums, compressor, dumpster, fence w/ gate
box((-8.6,FZ-1.6,1.2),(2.8,0.8,0.08),MT); box((-8.6,FZ-1.6,0.3),(2.8,0.8,0.08),MT)
for k in range(5): cyl((-9.7+k*0.55,FZ-1.6,0.82),0.38,0.24,TIRE,14,rot=(0,math.radians(90),0)); cyl((-9.7+k*0.55,FZ-1.6,1.62),0.38,0.24,TIRE,14,rot=(0,math.radians(90),0))
for (x,y,n) in ((18,FZ-1.4,6),(18.9,FZ-2.3,4),(-15.8,FZ-1.4,5)):
    for k in range(n): cyl((x,y,0.15+k*0.28),0.38,0.26,TIRE,14)
for k in range(3): box((19.6,FZ+1.8,0.1+k*0.16),(1.2,1.0,0.12),WD)
for k,(x,y) in enumerate(((19.5,FZ+3.4),(19.5,FZ+4.4),(20.4,FZ+3.9))): cyl((x,y,0.55),0.32,1.1,[RED,flat("DrumBlue","2a4f7e",0.5),YEL][k],12)
box((-2.4,FZ-1.2,0.8),(0.8,0.8,1.6),flat("Compressor","2a5fb0",0.4,0.4),bev=0.05)
box((-20.5,2,0.75),(2.4,1.4,1.5),flat("Dumpster","2f5d3a",0.6,0.3),bev=0.05)
box((W/2+3,0,1.3),(0.1,D,2.6),CR); box((W/2+1.5,-FZ,1.3),(3,0.1,2.6),CR)
box((0,FZ-6.5,0.05),(W+12,13,0.1),PV,uv=2.5); stripes(-6,FZ-9,8,3.0,5.0)
for x in (-14,14): lightpole(x,FZ-12,8,1.6,1)
for x in (-7.2,-1.5,4.6,10.7): bollard(x,FZ-0.6,YEL)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_repair2.png",(-28,-36,6),(0,FZ,3),24,(1200,800),40)
else:
    export("OT_RepairShop_B",drop_y=-99)
