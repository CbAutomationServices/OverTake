exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(22)
LS=pbr("Limestone","plaster",(1.0,0.95,0.86)); GR=pbr("Granite","conc",(0.62,0.6,0.58)); MB=pbr("Marble","tile",(1.0,0.98,0.95)); PV=pbr("Pavement","walk",(0.9,0.9,0.88))
GL=flat("Glass","1e2a33",0.05); BRZ=flat("Bronze","8a6a3a",0.35,0.9); GOLD=flat("GoldGlow","ffd27a",0.3,emit=3.5); BRASS=flat("Brass","c9a44e",0.3,0.95)
UP=flat("Uplight","fff1d0",0.3,emit=5.0); WARM=flat("InteriorWarm","ffdca8",0.3,emit=1.6); MT=flat("SteelGrey","9aa0a6",0.35,0.85); SCR=flat("ATMScreen","35c8ff",0.2,emit=3.0)
NAVY=flat("BankNavy","1b2f5c",0.4); FLAG=flat("FlagRed","b8322a",0.7); FLAGB=flat("FlagBlue","24407a",0.7); FLAGW=flat("FlagWhite","eeeeea",0.7)
W,D,H=26.0,18.0,12.0; FZ=-D/2; pz=2.0
box((0,0,1.0),(W+1,D+1,2.0),GR,bev=0.05,uv=1.5)
box((0,0,pz+H/2),(W,D,H),LS,uv=2.0)
for k in range(6): box((0,FZ-0.04,2.3+k*0.65),(W,0.12,0.06),GR)
xs=[-9,-5.4,-1.8,1.8,5.4,9]
box((0,FZ-3.2,pz+0.1),(21,6.2,0.2),MB,bev=0.03)
for x in xs:
    cyl((x,FZ-5.6,pz+0.3),0.78,0.4,GR,20); cyl((x,FZ-5.6,pz+0.5+4.6),0.56,9.2,MB,24)
    box((x,FZ-5.6,pz+9.9),(1.55,1.55,0.4),MB,bev=0.04); box((x,FZ-5.6,pz+10.15),(1.7,1.7,0.12),MB)
    box((x,FZ-6.45,pz+0.12),(0.5,0.12,0.12),UP)                 # column uplights
box((0,FZ-3.2,pz+10.6),(21.6,6.6,1.0),LS,bev=0.05)
for i in range(54): box((-10.6+i*0.4,FZ-6.52,pz+10.2),(0.18,0.12,0.18),MB)
prism((0,FZ-3.2,pz+11.1),22.2,3.2,6.8,LS); prism((0,FZ-6.62,pz+11.35),18.5,2.4,0.1,MB)
box((0,FZ-6.66,pz+10.45),(9,0.08,0.7),NAVY); box((0,FZ-6.7,pz+10.45),(8.4,0.04,0.45),GOLD)   # lit name plate
sphere((0,FZ-6.7,pz+12.0),0.5,GOLD,1)                                                       # medallion
for i in range(5): box((0,FZ-6.8-i*0.45,pz-0.2-i*0.4),(23,0.45,0.4*(i+1)+0.4),GR,bev=0.02)
for x in (-3,3):                                                                            # brass handrails
    for k in range(4): cyl((x,FZ-7.0-k*0.6,pz+0.2-k*0.45),0.04,1.0,BRASS,8)
    box((x,FZ-7.9,pz+0.6-0.7),(0.06,2.4,0.06),BRASS,rot=(math.atan2(1.8,2.4),0,0))
# bronze doors, lit transom
box((0,FZ-0.04,pz+2.4),(3.4,0.12,4.8),BRZ); box((0,FZ-0.08,pz+2.4),(0.06,0.14,4.8),BRASS)
for s in (-1,1): box((s*0.9,FZ-0.1,pz+2.2),(0.08,0.1,0.8),BRASS)
box((0,FZ-0.04,pz+5.6),(3.4,0.08,1.2),WARM); box((0,FZ-0.12,pz+6.3),(4.2,0.25,0.3),MB)
for s in (-1,1): box((s*2.4,FZ-0.25,pz+3.4),(0.5,0.4,0.9),BRASS); box((s*2.4,FZ-0.46,pz+3.4),(0.3,0.04,0.6),UP)   # wall lanterns
for x in (-11.2,-7.4,7.4,11.2):
    box((x,FZ-0.02,pz+4.8),(1.8,0.1,5.4),WARM); box((x,FZ-0.06,pz+4.8),(1.8,0.04,5.4),GL)
    halfcyl((x,FZ-0.04,pz+7.5),0.9,0.1,GL,20)
    for s in (-1,1): box((x+s*0.95,FZ-0.1,pz+4.8),(0.15,0.15,5.6),MB)
    for z in (pz+3.2,pz+5.0,pz+6.6): box((x,FZ-0.1,z),(1.8,0.06,0.06),BRZ)
    box((x,FZ-0.1,pz+2.0),(2.3,0.3,0.25),MB); box((x,FZ-0.14,pz+8.5),(0.45,0.25,0.55),MB)
box((0,0,pz+H+0.3),(W+0.8,D+0.8,0.6),LS,bev=0.05)
for i in range(64): box((-W/2+0.2+i*0.405,FZ-0.42,pz+H),(0.18,0.12,0.2),MB)
for i in range(40): cyl((-W/2+0.6+i*0.64,FZ+0.2,pz+H+1.05),0.12,0.8,MB,8)                 # roof balustrade
box((0,FZ+0.2,pz+H+0.62),(W,0.5,0.12),MB); box((0,FZ+0.2,pz+H+1.5),(W,0.5,0.15),MB)
# drive-thru annex (modern) on the right + ATM kiosk
ax=W/2+5
box((ax,2,2.4),(8,10,4.8),GR,uv=1.5); box((ax,FZ+1.95,2.4),(6.4,0.06,3.4),GL); box((ax,FZ+1.9,4.6),(8.2,0.2,0.4),NAVY)
box((ax+5.5,2,5.0),(5,11,0.3),NAVY,bev=0.04); box((ax+5.5,2,4.82),(4.2,10,0.04),UP)
for y in (-2.5,6.5): box((ax+7.7,y,2.5),(0.4,0.4,5.0),MT)
box((ax+4.2,2,1.0),(0.7,1.0,2.0),MT); box((ax+4.56,2,1.3),(0.02,0.6,0.4),SCR)
box((-W/2-3,FZ-6,1.2),(1.2,1.0,2.4),GR,bev=0.04); box((-W/2-3,FZ-6.51,1.5),(0.7,0.02,0.45),SCR)   # ATM kiosk
box((-W/2-3,FZ-6,2.6),(1.8,1.6,0.25),NAVY); box((-W/2-3,FZ-6.81,2.6),(1.8,0.04,0.1),UP)
# flags, landscaping, lot
for i,x in enumerate((-14.5,-13.3,14.5)):
    cyl((x,FZ-10,7.5),0.08,15,MT,10); box((x+1.0,FZ-10,14.2),(2.0,0.05,1.2),[FLAG,FLAGW,FLAGB][i]); sphere((x,FZ-10,15.1),0.16,BRASS,1)
for x in (-8.6,8.6): planter(x,FZ-8.6,5.0,1.4,GR,4)
for x in (-12.5,12.5): planter(x,FZ-7.6,1.8,4.0,GR,3)
for x in (-11,-5,5,11): sphere((x,FZ-11.8,0.5),0.5,GR,2)                                  # stone sphere bollards
for x in (-16,16): lightpole(x,FZ-12.5,8,1.6,1 if x<0 else -1)
box((0,FZ-16,0.06),(52,14,0.12),PV,uv=2.5); stripes(-15,FZ-19.5,11,3.0,5.0)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_bank2.png",(-30,-46,6),(2,FZ,6),26,(1200,850),40)
else:
    export("OT_Bank_B",drop_y=-99)
