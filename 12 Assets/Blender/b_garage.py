exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(9)
BR=pbr("Brick","brick",(0.75,0.6,0.55)); CR=pbr("Corrugated","corr",(0.42,0.44,0.48),0.6,True); CO=pbr("Concrete","walk",(0.9,0.9,0.88)); MT=pbr("Metal","metal",(0.55,0.55,0.57),0.8)
GL=flat("Glass","1e2a34",0.05); FR=flat("Frame","16171a",0.4); DOOR=flat("RollDoor","3a3d42",0.5,0.4)
NEON=flat("Neon","ff6a14",0.3,emit=5.0); SIGN=flat("SignPanel","121214",0.4); YEL=flat("Yellow","e8b81e",0.5); LIGHT=flat("WallLight","fff1d6",0.3,emit=3.0)
W,D,H=32.0,20.0,10.0; FZ=-D/2
box((0,0,1.6),(W,D,3.2),BR,uv=1.6)
box((0,0,3.2+(H-3.2)/2),(W,D,H-3.2),CR,uv=2.5)
box((0,0,H+0.1),(W+0.4,D+0.4,0.25),MT)
# 3 roll-up doors
for i,x in enumerate((-11,-3,5)):
    box((x,FZ-0.02,2.6),(6.0,0.1,5.2),DOOR,uv=1.0)
    for k in range(14): box((x,FZ-0.08,0.3+k*0.36),(6.0,0.04,0.05),FR)
    box((x,FZ-0.12,5.4),(6.6,0.25,0.4),MT)
    box((x,FZ-0.26,5.75),(6.0,0.05,0.08),NEON)
    box((x,FZ-0.3,6.4),(1.2,0.5,0.3),LIGHT)
    for s in (-1,1): box((x+s*3.3,FZ-0.15,2.7),(0.3,0.3,5.4),MT)
    box((x,FZ-0.15,6.9),(1.4,0.06,0.9),YEL)  # bay number plate
# office: 2-story glass corner on the right
ox=12.5
box((ox,FZ+0.0,4.9),(6.4,0.12,9.0),GL)
for k in range(5): box((ox-3.2+k*1.6,FZ-0.08,4.9),(0.12,0.14,9.0),FR)
for z in (0.4,3.4,6.4,9.3): box((ox,FZ-0.08,z),(6.6,0.14,0.14),FR)
box((ox,FZ-0.1,1.6),(1.6,0.08,2.8),GL)
# big sign on top
box((-3,FZ+0.5,H+1.9),(20,0.5,3.4),SIGN,bev=0.05)
for z in (H+0.25,H+3.55): box((-3,FZ+0.2,z),(20,0.06,0.1),NEON)
for x in (-13,7): box((x,FZ+0.2,H+1.9),(0.1,0.06,3.4),NEON)
for x in (-8,2): box((x,FZ+0.7,H+0.8),(0.3,0.3,1.6),MT)
# vertical neon strips on corners
for x in (-W/2-0.05,W/2+0.05): box((x,FZ-0.05,H/2),(0.08,0.08,H),NEON)
# apron + bollards
box((-3,FZ-5,0.08),(26,10,0.16),CO,uv=3.0)
for x in (-14.4,-6.6,-6.0+0.6,1.4,2.0+0.6,8.6):
    pass
for x in (-14.3,-7.7,-6.3,0.3,1.7,8.3): cyl((x,FZ-0.6,0.6),0.18,1.2,YEL,12)
# roof units
for x in (-8,4): box((x,3,H+0.8),(3,2,1.4),MT,bev=0.04)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_garage.png",(-26,-34,4),(0,FZ,5),26,(1100,800))
else:
    export("OT_PlayerGarage_A",drop_y=-99)
