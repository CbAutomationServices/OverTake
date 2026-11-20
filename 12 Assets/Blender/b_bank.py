exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(21)
LS=pbr("Limestone","plaster",(1.0,0.95,0.86)); ST=pbr("Stone","conc",(0.95,0.93,0.9)); CO=pbr("Concrete","walk",(0.9,0.9,0.88)); MT=pbr("Metal","metal",(0.55,0.55,0.57),0.8)
GL=flat("Glass","1e2a33",0.05); BRZ=flat("Bronze","8a6a3a",0.35,0.9); GOLD=flat("Gold","d8b25a",0.3,0.9); GRN=flat("Hedge","3d5e2e",0.9)
LAMP=flat("LampGlow","fff0cc",0.3,emit=4.0); IRON=flat("Iron","1a1a1a",0.5,0.6); FLAG=flat("FlagRed","b8322a",0.7); FLAGB=flat("FlagBlue","24407a",0.7); SCR=flat("ATMScreen","35c8ff",0.2,emit=2.5)
W,D,H=26.0,18.0,12.0; FZ=-D/2
box((0,0,1.0),(W+1,D+1,2.0),LS,bev=0.05,uv=1.5)                # plinth
box((0,0,2+H/2),(W,D,H),LS,uv=2.0)
# rusticated courses on lower wall
for k in range(6): box((0,FZ-0.04,2.3+k*0.65),(W,0.12,0.06),ST)
# portico: 6 columns + entablature + pediment
pz=2.0; for_cols=[-9,-5.4,-1.8,1.8,5.4,9]
box((0,FZ-3.2,pz+0.1),(21,6.2,0.2),LS,bev=0.03)
for x in for_cols:
    cyl((x,FZ-5.6,pz+0.3),0.75,0.4,LS,20)                        # base
    cyl((x,FZ-5.6,pz+0.5+4.6),0.55,9.2,LS,20)                    # shaft
    box((x,FZ-5.6,pz+9.9),(1.5,1.5,0.4),LS,bev=0.04)             # capital
box((0,FZ-3.2,pz+10.6),(21.6,6.6,1.0),LS,bev=0.05)               # entablature
for i in range(54): box((-10.6+i*0.4,FZ-6.52,pz+10.2),(0.18,0.12,0.18),ST)  # dentils
prism((0,FZ-3.2,pz+11.1),22.2,3.2,6.8,LS)                         # pediment
prism((0,FZ-6.62,pz+11.35),18.5,2.4,0.1,ST)                        # tympanum inset
box((0,FZ-6.64,pz+10.4),(8,0.06,0.6),GOLD)                        # name plate (text later)
# steps
for i in range(5): box((0,FZ-6.8-i*0.45,pz-0.2-i*0.4),(23,0.45+i*0.0,0.4*(i+1)+0.4),LS,bev=0.02)
# bronze doors + transom
box((0,FZ-0.04,pz+2.4),(3.4,0.12,4.8),BRZ); box((0,FZ-0.08,pz+2.4),(0.06,0.14,4.8),GOLD)
box((0,FZ-0.04,pz+5.6),(3.4,0.08,1.2),GL); box((0,FZ-0.12,pz+6.3),(4.2,0.25,0.3),LS)
# tall windows with arched tops (side bays)
for x in (-11.2,-7.4,7.4,11.2):
    box((x,FZ-0.02,pz+4.8),(1.8,0.1,5.4),GL)
    halfcyl((x,FZ-0.02,pz+7.5),0.9,0.1,GL,16)
    for s in (-1,1): box((x+s*0.95,FZ-0.1,pz+4.8),(0.15,0.15,5.6),LS)
    box((x,FZ-0.1,pz+2.0),(2.3,0.3,0.25),LS); box((x,FZ-0.1,pz+5.0),(1.8,0.08,0.08),BRZ)
    box((x,FZ-0.14,pz+8.5),(0.45,0.25,0.55),LS)                  # keystone
box((0,0,2+H+0.3),(W+0.8,D+0.8,0.6),LS,bev=0.05); box((0,0,2+H+0.75),(W+0.4,D+0.4,0.3),LS)
for i in range(64): box((-W/2+0.2+i*0.405,FZ-0.42,2+H),(0.18,0.12,0.2),ST)
# ATM niche on the right side wall front corner
box((W/2+0.05,FZ+3,pz+1.4),(0.12,1.4,2.2),MT); box((W/2+0.12,FZ+3,pz+1.8),(0.02,0.6,0.4),SCR)
box((W/2+0.25,FZ+3,pz+2.7),(0.5,1.8,0.12),MT)
# flagpoles, lamps, planters
for i,x in enumerate((-14.5,14.5)):
    cyl((x,FZ-9.5,7.5),0.08,15,MT,10); box((x+1.0,FZ-9.5,14.2),(2.0,0.05,1.2),[FLAG,FLAGB][i]); cyl((x,FZ-9.5,15.05),0.15,0.2,GOLD,10)
for x in (-11.8,11.8):
    box((x,FZ-8.3,0.5),(2.4,1.4,1.0),LS,bev=0.04); box((x,FZ-8.3,1.1),(2.2,1.2,0.3),GRN)
    cyl((x,FZ-10.4,2.2),0.1,4.4,IRON,10); box((x,FZ-10.4,4.6),(0.6,0.6,0.7),LAMP)
box((0,FZ-12.6,0.06),(36,6,0.12),CO,uv=2.5)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_bank.png",(-26,-40,5),(0,FZ,6),28,(1100,850),36)
else:
    export("OT_Bank_A",drop_y=-99)
