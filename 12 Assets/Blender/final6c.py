exec(open("/home/claude/blender/kit3.py").read())
import sys
SEATS=["d0181e","f0efe9","1f4e8c"]
@reg("OT_Grandstand",(-52,-62,20),(0,4,8),24,(1150,780))
def grandstand():
    CO=CONC(); ST=GALV(); RED=C("OTRed","d0181e",0.35); L=70; rows=16
    for r in range(rows):
        z=0.9+r*0.55; y=r*0.9
        box((0,y,z/2),(L,0.9,z),CO,uv=2.5)
        for blk in range(7):
            x0=-L/2+1+blk*10
            col=SEATS[(blk+r//4)%3] if r%4 else "2a2c30"
            box((x0+4.4,y+0.15,z+0.22),(8.6,0.4,0.42),C(f"Seat{col}",col,0.45))
            box((x0+4.4,y+0.38,z+0.5),(8.6,0.06,0.5),C(f"Seat{col}",col,0.45))
        for blk in range(8): box((-L/2+0.5+blk*10,y,z+0.1),(0.9,0.9,0.2),C("Stair","b8b8b4",0.7))
    box((0,rows*0.9+0.4,6),(L,0.8,12),CO,uv=2.5)
    for x in range(-35,36,7):
        box((x,rows*0.9,9.5),(0.5,0.5,11),ST); box((x,rows*0.9-7,14.3),(0.4,15,0.4),ST,rot=(math.radians(-6),0,0))
    box((0,rows*0.9-7,15.1),(L+2,16,0.3),T_("RoofMetal","corr",(0.85,0.87,0.9),0.6,True),rot=(math.radians(-6),0,0))
    for x in range(-33,34,6): box((x,-0.4,14.3),(1.2,0.5,0.4),C("Floodlight","2a2c30",0.4,0.6)); box((x,-0.68,14.2),(1.0,0.04,0.3),led())
    box((0,-1.2,1.3),(L,0.12,1.4),C("Wall","f0efe9",0.6))
    for k in range(14): box((-32.5+k*5,-1.28,1.3),(4.4,0.04,1.0),[RED,C("AdBlue","1f4e8c",0.4),C("AdYellow","f6c22c",0.45),C("AdBlack","1a1a1a",0.5)][k%4])
    for x in range(-35,36,2): box((x,-1.2,2.6),(0.05,0.05,1.2),ST)
    box((0,-1.2,3.2),(L,0.08,0.08),ST)
    box((0,rows*0.9+4,8),(20,6,16),CO,uv=2.5); box((0,rows*0.9+0.95,12.6),(18,0.06,3.4),glass())
    box((0,rows*0.9+0.9,14.8),(18,0.1,0.6),RED); box((0,rows*0.9+0.84,14.8),(14,0.03,0.35),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    box((L/2+6,6,10),(8,1,6),C("Scoreboard","121212",0.5)); box((L/2+6,5.45,10.3),(7,0.05,4.6),C("ScoreGlow","f6c22c",0.3,emit=1.0))
    for z in (8.8,10.3,11.8): box((L/2+6,5.42,z),(6,0.04,0.6),C("ScoreRow","ff7a1a",0.3,emit=2.0))
    cyl((L/2+6,6,3.5),0.5,7,ST,10)
    box((0,-5,0.03),(L+20,8,0.06),ASPH(),uv=3.0); box((0,-8.8,0.07),(L+20,0.3,0.03),WHITE())
@reg("OT_PitBuilding",(-42,-50,11),(0,0,4),24,(1150,780))
def pits():
    WH=T_("Panel","plaster",(0.95,0.95,0.96)); DK=C("DarkPanel","23262b",0.4,0.5); RED=C("OTRed","d0181e",0.35); L=60
    box((0,4,3.2),(L,8,6.4),WH,uv=2.0)
    for i in range(10):
        x=-27+i*6
        box((x,0.0,2.3),(4.8,0.06,4.2),C("PitInside","34383f",0.7)); box((x,0.5,0.5),(1.6,0.8,1.0),C("ToolChest","c4261d",0.4),bev=0.04)
        box((x+1.6,0.6,0.9),(0.8,0.5,1.8),C("TireStack","151515",0.85)); box((x,-0.02,4.25),(4.8,0.04,0.08),led())
        box((x,-0.08,4.9),(5.4,0.12,0.7),RED if i%2 else DK); box((x-1.8,-0.15,4.9),(0.9,0.03,0.5),C("PitNum","f4f8ff",0.3,emit=1.8))
        box((x+0.8,-0.15,4.9),(2.6,0.03,0.35),C("Sponsor","f6c22c",0.4,emit=0.8))
    for x in range(-30,31,6): box((x,-0.05,3.2),(0.6,0.3,6.4),WH)
    box((0,4,7.8),(L,8,2.8),glass()); box((0,4,7.8),(L-0.2,7.8,2.6),warm())
    for x in range(-30,31,4): box((x,0,7.8),(0.15,0.15,2.8),C("Mullion","c9ccd1",0.25,0.9))
    box((0,4,9.4),(L+1,9,0.4),DK); box((0,-0.45,9.7),(L+1,0.1,0.8),C("RoofRail","9aa0a6",0.35,0.85))
    box((0,-3,6.4),(L,6,0.3),WH); for_=None
    for x in range(-30,31,2): box((x,-5.9,7.1),(0.05,0.05,1.1),GALV())
    box((0,-5.9,7.6),(L,0.08,0.08),GALV())
    for x in range(-30,31,10): box((x,-5.8,3.2),(0.35,0.35,6.4),GALV())
    box((0,-12,0.6),(L,0.6,1.2),CONC()); box((0,-12,1.5),(L,0.08,0.6),C("Fence","9aa0a6",0.5,0.7))
    for k in range(6): box((-25+k*10,-11.6,0.4),(2.4,0.6,0.8),C("PitStand","2a2c30",0.4,0.5)); box((-25+k*10,-11.6,0.85),(2.4,0.6,0.06),C("Screen","35c8ff",0.2,emit=1.5))
    box((0,-8,0.03),(L+6,14,0.06),ASPH(),uv=3.0); box((0,-6,0.07),(L+6,0.25,0.03),WHITE())
    for i in range(10): box((-27+i*6,-3.5,0.07),(4.6,0.1,0.03),YELW())
@reg("OT_DragStartTower",(-20,-24,8),(2,2,4),24,(950,800))
def dragtree():
    P=GALV(); BK=C("TreeBody","151515",0.5); RED=C("OTRed","d0181e",0.35); CO=CONC()
    box((0,-1,0.03),(24,12,0.06),ASPH(),uv=3.0)
    for s in (-1,1): box((s*4.5,-1,0.07),(0.25,12,0.03),WHITE())
    box((0,-1,0.07),(0.25,12,0.03),YELW()); box((0,2,0.07),(9,0.3,0.03),WHITE())
    box((0,-4,0.065),(8,4,0.03),C("BurnoutStain","1a1a1a",0.9))
    cyl((0,2,0.15),0.4,0.3,CO,12); frustum((0,2,0.3),0.3,0.3,0.2,0.2,4.6,P,0)
    box((0,2,5.8),(0.9,0.4,3.2),BK,bev=0.05); box((0,2,7.5),(1.1,0.5,0.2),RED)
    lamps=(("1f6dff",0.3),("1f6dff",0.3),("f6c22c",3),("f6c22c",3),("f6c22c",3),("2aff6a",0.3),("ff2a2a",0.3))
    for i,(c,e) in enumerate(lamps):
        for s in (-1,1): cyl((s*0.22,1.78,7.0-i*0.42),0.13,0.05,C(f"DL{c}{e}",c,0.3,emit=e),12,rot=(math.radians(90),0,0)); box((s*0.22,1.74,7.12-i*0.42),(0.3,0.12,0.04),BK,rot=(math.radians(-30),0,0))
    for s in (-1,1): box((s*6,0,0.5),(0.6,14,1.0),CO); box((s*6,0,1.05),(0.3,14,0.1),RED)
    TW=T_("Block","plaster",(0.86,0.86,0.86))
    box((11,7,5),(6,6,10),TW,uv=2.0); box((11,7,10.4),(6.8,6.8,0.8),RED); box((11,3.95,7.4),(5.6,0.06,2.2),glass()); box((11,3.97,7.4),(5.4,0.04,2.0),warm())
    for k in range(10): box((8.2,7-2.5+k*0.55,0.3+k*0.85),(1.2,0.5,0.12),P)
    box((7.6,7,4.5),(0.06,5.5,0.06),P,rot=(math.radians(-47),0,0))
    box((11,3.9,9.2),(5.6,0.08,1.0),C("TimeBoard","121212",0.5))
    for k in range(5): box((9.0+k*1.0,3.85,9.2),(0.7,0.03,0.6),C("Digit","ff3a2a",0.3,emit=3.0))
    for s in (-1,1):
        cyl((s*9,-6,3),0.15,6,P,8); box((s*9,-6,6.2),(1.4,0.6,1.0),C("TimeBoard","121212",0.5)); box((s*9,-6.32,6.2),(1.2,0.03,0.6),C("Digit2","2aff6a",0.3,emit=2.5))
@reg("OT_Bleachers",(-14,-18,6),(0,1.5,1.5),26,(900,700))
def bleachers():
    AL=C("Aluminum","c9ccd1",0.3,0.8); ST=C("GalvFrame","8e959c",0.4,0.8); L=16
    box((0,1.5,0.03),(L+3,7,0.06),CONC())
    for r in range(7):
        box((0,r*0.75,0.45+r*0.45),(L,0.4,0.07),AL); box((0,r*0.75+0.32,0.25+r*0.45),(L,0.04,0.38),AL)
        for x in range(-7,8,2): box((x,r*0.75,0.53+r*0.45),(0.04,0.4,0.02),C("SeatNum","1f4e8c",0.5))
    for x in range(-8,9,4):
        box((x,2.6,1.7),(0.1,5.3,0.1),ST,rot=(math.radians(-31),0,0)); box((x,4.6,1.9),(0.1,0.1,3.8),ST); box((x,0,0.25),(0.1,0.1,0.5),ST)
        box((x,2.3,0.8),(0.08,4.6,0.08),ST)
    for s in (-1,1):
        box((s*L/2,2.4,2.9),(0.06,5.2,0.06),AL,rot=(math.radians(-31),0,0))
        for k in range(6): box((s*L/2,0.3+k*0.8,1.0+k*0.48+0.5),(0.04,0.04,1.0),AL)
    box((0,4.7,3.9),(L,0.06,1.2),AL); box((0,4.7,4.5),(L,0.08,0.08),AL)
    for k in range(4): box((-6+k*4,4.74,3.9),(3.2,0.02,0.7),[C("BannerRed","c4261d",0.6),C("BannerBlue","1f4e8c",0.6)][k%2])
@reg("OT_FestivalHub",(-62,-74,24),(0,2,7),24,(1150,800))
def festival():
    WH=C("TentWhite","f2f2ee",0.6); MG=C("FestMagenta","e0287a",0.4); CY=C("NeonCyan","2fe0ff",0.3,emit=5.0); PK=C("NeonPink","ff3fb4",0.3,emit=5.0); YL=C("FestYellow","f6c22c",0.4)
    TR=C("Truss","9aa0a6",0.35,0.85)
    box((0,0,0.03),(96,66,0.06),T_("Pavement","walk",(0.86,0.86,0.84)),uv=3.0)
    box((0,0,0.05),(70,40,0.02),C("FestGrass","567d3a",0.9))
    # main stage with truss roof
    box((0,14,1.2),(28,12,2.4),C("Stage","1a1a1a",0.5)); box((0,8.05,1.2),(28,0.1,2.4),MG)
    for k in range(5): box((-11+k*5.5,8.0,0.6),(4,0.12,0.8),C("Speaker","121212",0.5))
    for x in (-14,14):
        for y in (8.5,19.5): box((x,y,9),(1,1,16),TR)
        for z in range(3,16,3): box((x,14,z),(0.2,11,0.2),TR)
    for y in (8.5,19.5): box((0,y,17),(29,1,1),TR)
    frustum((0,14,17.5),12,30,10,26,2.2,C("StageRoof","1a1a1a",0.5),0)
    box((0,19.8,9),(26,0.4,13),C("LEDScreen","1b1f3a",0.3,emit=0.8)); box((0,19.55,9.5),(22,0.05,9),C("ScreenGlow","ff3fb4",0.3,emit=2.2))
    box((0,19.5,9.5),(10,0.04,3),C("ScreenLogo","2fe0ff",0.3,emit=3.0))
    for k in range(10): box((-12.5+k*2.8,8.5,16.3),(0.5,0.5,0.5),[CY,PK,YL][k%3]); box((-12.5+k*2.8,8.5,16.0),(0.06,0.06,0.6),TR)
    for s in (-1,1): box((s*20,13,7),(6,1,9),C("SideScreen","1b1f3a",0.3,emit=0.8)); box((s*20,12.45,7.4),(5,0.04,6),C("SideGlow","2fe0ff",0.3,emit=1.5)); box((s*20,13,1.25),(0.6,0.6,2.5),TR)
    # tents
    for i,(x,y) in enumerate(((-34,-8),(-34,8),(34,-8),(34,8),(-18,-18),(18,-18))):
        box((x,y,1.7),(10,8,3.4),WH); cone((x,y,4.9),7.4,0.25,3.2,MG if i%2 else WH,4,rot=(0,0,math.radians(45)))
        box((x,y-4.05,2.9),(7,0.06,0.9),[MG,C("FestBlue","1f6db0",0.4),YL][i%3]); box((x,y-4.06,2.9),(5,0.03,0.4),C("SignWhiteGlow","f4f8ff",0.3,emit=1.5))
        cyl((x,y,6.6),0.06,1.6,TR,6); box((x+0.5,y,7.1),(1,0.03,0.6),[MG,CY,YL][i%3])
    # food trucks
    for k,(x,col) in enumerate(((-6,"f6c22c"),(2,"2fa45a"),(10,"e07a3a"))):
        box((x,-24,1.6),(6,2.6,2.6),C(f"Truck{col}",col,0.4),bev=0.08); box((x,-25.32,1.9),(3,0.05,1.2),warm()); box((x,-25.8,2.6),(3.4,1.2,0.08),C("Awning","f0efe9",0.6),rot=(math.radians(-15),0,0))
        for dx in (-2,2): cyl((x+dx,-24,0.4),0.4,2.7,C("Tire","151515",0.85),12,rot=(math.radians(90),0,0))
    # ferris wheel
    FW=C("Wheel","f0efe9",0.4,0.6); cx,cy,cz,R=-26,22,14,11
    for s in (-1,1): box((cx,cy+s*1.2,cz/2),(0.6,0.6,cz),FW,rot=(0,math.radians(18),0)); box((cx,cy+s*1.2,cz/2),(0.6,0.6,cz),FW,rot=(0,math.radians(-18),0))
    for k in range(24): a=k*math.pi/12; a2=(k+1)*math.pi/12
    for k in range(24):
        a=k*math.pi/12; p0=(cx+math.cos(a)*R,cz+math.sin(a)*R); p1=(cx+math.cos(a+math.pi/12)*R,cz+math.sin(a+math.pi/12)*R)
        mx,mz=(p0[0]+p1[0])/2,(p0[1]+p1[1])/2; ln=math.hypot(p1[0]-p0[0],p1[1]-p0[1]); ang=-math.atan2(p1[1]-p0[1],p1[0]-p0[0])
        for s in (-1,1): box((mx,cy+s*1.0,mz),(ln+0.1,0.25,0.25),FW,rot=(0,ang,0))
        if k%2==0:
            box((cx+math.cos(a)*R/2,cy,cz+math.sin(a)*R/2),(R,0.12,0.12),FW,rot=(0,-a,0))
            box((p0[0],cy,p0[1]-1.0),(1.2,1.6,1.4),[MG,C("FestBlue","1f6db0",0.4),YL][k%3],bev=0.08)
        box((p0[0],cy-1.15,p0[1]),(0.3,0.04,0.3),[CY,PK][k%2])
    cyl((cx,cy,cz),0.8,2.6,FW,12,rot=(math.radians(90),0,0))
    # entry arch with neon
    for s in (-1,1): frustum((s*8,-30,0),2.4,2.4,1.6,1.6,11,MG,0)
    box((0,-30,11.6),(18,2.6,2.4),MG,bev=0.1); box((0,-31.35,11.6),(14,0.06,1.4),C("SignWhiteGlow","f4f8ff",0.3,emit=3.5))
    for z in (10.3,12.9): box((0,-31.36,z),(18,0.06,0.15),CY)
    for s in (-1,1):
        for k in range(5): box((s*8,-31.25,1.5+k*2),(1.6,0.05,0.15),PK)
    # string lights + flags + light towers
    for k in range(16):
        a=k/16*math.pi*2; x,y=math.cos(a)*40,math.sin(a)*26+2; cyl((x,y,4.5),0.1,9,GALV(),6); box((x+0.8,y,8.3),(1.6,0.04,1.0),[MG,CY,YL][k%3])
    for k in range(20): box((-38+k*4,-2,6.0+0.5*math.sin(k)),(0.25,0.25,0.25),C("Bulb","fff0b0",0.3,emit=5.0))
    for x in (-24,24):
        cyl((x,-16,8),0.35,16,GALV(),8); box((x,-16,16.4),(3.6,0.8,1.4),GALV()); box((x,-16.42,16.4),(3.2,0.04,1.0),led())
    for x in range(-44,45,8): box((x,-29,0.08),(0.15,7,0.02),WHITE())
@reg("OT_Lighthouse",(-28,-34,11),(0,0,12),24,(800,1000))
def lighthouse():
    WH=C("LHWhite","f2f2ee",0.5); RD=C("LHRed","c4161d",0.45); RK=T_("Rock","granite",(0.62,0.6,0.56)); CO=CONC2(); IR=C("Iron","1c1c1c",0.45,0.6)
    for (x,y,s) in ((0,0,(7,6.5,3)),(-5,3,(4,3.5,2.4)),(5,4,(4.2,3.6,2.2)),(-4,-5,(3.5,3,1.8)),(6,-3,(3,3,1.6))): ico((x,y,0),s,RK,1,(0.3,0.1,x*0.2))
    cyl((0,0,2.6),4.0,1.2,CO,24)
    for i in range(7): cone((0,0,3.2+i*3.0+1.5),3.4-i*0.25,3.4-(i+1)*0.25,3.0,[WH,RD][i%2],22)
    for k in range(4): box((math.cos(k*1.57)*3.0,math.sin(k*1.57)*3.0,7+k*4),(0.4,0.12,1.0),C("Window","1c262e",0.1),rot=(0,0,k*1.57+1.57))
    cyl((0,0,24.6),2.4,0.4,IR,22)
    for k in range(20): a=k*math.pi/10; box((math.cos(a)*2.3,math.sin(a)*2.3,25.2),(0.06,0.06,1.0),IR)
    cyl((0,0,25.7),2.35,0.08,IR,22)
    cyl((0,0,26.3),1.4,2.6,C("LampGlass","fff4c0",0.1,emit=6.0),16)
    for k in range(8): a=k*math.pi/4; box((math.cos(a)*1.42,math.sin(a)*1.42,26.3),(0.08,0.08,2.6),IR)
    cone((0,0,28.4),1.8,0.15,1.8,RD,16); sphere((0,0,29.4),0.25,IR,1); cyl((0,0,29.9),0.04,0.8,IR,6)
    box((6.5,0,3.8),(5.5,4.5,3.2),WH); prism((6.5,0,5.4),5.8,1.8,4.8,RD)
    box((6.5,-2.28,3.4),(0.9,0.06,2),C("Door","3a2416",0.4)); box((8.0,-2.28,4.0),(0.9,0.06,0.9),warm())
    cyl((8,1.3,6.3),0.25,1.4,C("Chimney","8a4a3a",0.6),8)
    for k in range(24): a=k*math.pi/12; box((math.cos(a)*4.6,math.sin(a)*4.6,3.6),(0.06,0.06,0.9),WH)
@reg("OT_Pier",(-24,-6,10),(0,30,2),24,(1150,780))
def pier():
    WD=T_("Wood","wood",(0.8,0.62,0.45)); PL=T_("Piling","wood",(0.5,0.38,0.28)); RL=C("PierRail","f0efe9",0.5); L=60; Wd=8
    for k in range(int(L/0.6)): box((0,k*0.6,2.5),(Wd,0.55,0.25),WD,uv=1.2) if k%3==0 else None
    box((0,L/2,2.45),(Wd,L,0.2),WD,uv=1.2)
    for k in range(0,L,1): box((0,k,2.56),(Wd,0.04,0.02),C("PlankGap","3a2a1c",0.9))
    for y in range(0,L+1,6):
        for x in (-Wd/2+0.3,Wd/2-0.3): cyl((x,y,0.5),0.32,5,PL,10)
        box((0,y,2.1),(Wd,0.3,0.4),PL)
    for s in (-1,1):
        box((s*(Wd/2-0.1),L/2,3.7),(0.15,L,0.12),RL); box((s*(Wd/2-0.1),L/2,3.2),(0.08,L,0.08),RL)
        for y in range(0,L+1,2): box((s*(Wd/2-0.1),y,3.2),(0.1,0.1,1.2),RL)
    for y in range(6,L,10):
        for s in (-1,1):
            cyl((s*(Wd/2-0.6),y,4.8),0.09,4.6,C("PoleGreen","1f3a2e",0.4,0.6),8); sphere((s*(Wd/2-0.6),y,7.2),0.3,C("GlobeLamp","fff0cc",0.2,emit=4.0),1)
            box((s*(Wd/2-0.9),y+3,2.95),(0.5,1.8,0.06),T_("Wood","wood",(0.82,0.6,0.42))); box((s*(Wd/2-0.7),y+3,3.3),(0.06,1.8,0.4),T_("Wood","wood",(0.82,0.6,0.42)))
    S=T_("Siding","plaster",(0.92,0.86,0.76))
    box((0,L+5,4.2),(10,8,3.2),S); prism((0,L+5,5.8),10.6,2.4,8.6,C("RoofTeal","1fa6a0",0.5))
    awning_striped(0,L+1,9,4.6,C("AwnTeal","1fa6a0",0.6),C("AwnW","f0efe9",0.6),1.4)
    box((0,L+0.98,3.6),(6,0.06,1.6),warm()); box((0,L+0.95,5.3),(6,0.12,0.6),C("SignFace","f2efe6",0.5))
    for k in range(3): cyl((-3+k*3,L-3,3.1),0.4,0.06,C("Table","f0efe9",0.5),12); cyl((-3+k*3,L-3,2.8),0.05,0.6,RL,6); cyl((-3+k*3,L-3,4.6),0.04,2.4,RL,6); cone((-3+k*3,L-3,5.6),1.3,0.05,0.5,C("Umbrella","e05a3a" if k%2 else "1fa6a0",0.6),10)
    for k in range(5): box((Wd/2-0.4,8+k*10,3.9),(0.04,0.04,1.2),C("FishRod","2a2c30",0.5),rot=(0,math.radians(40),0))
    for x in (-3,3): cyl((x,L+9.5,3.2),0.3,1.4,C("Bollard","2a2c30",0.4,0.6),10)
name=sys.argv[-2]; mode=sys.argv[-1]
f,cam,tgt,lens,res=BLD[name]; reset(); random.seed(hash(name)%1000); _cache.clear(); f()
if mode=="render": world_and_render(f"/home/claude/blender/r_{name}.png",cam,tgt,lens,res,18)
else: export(name,drop_y=-999)
