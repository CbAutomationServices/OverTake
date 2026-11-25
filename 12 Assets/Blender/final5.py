exec(open("/home/claude/blender/kit2.py").read())
exec(open("/home/claude/blender/final4.py").read().split("@reg(")[0].split("import sys",1)[1])   # car/jersey/guardrail helpers
import sys
POLE=lambda: C("PoleDark","2a2c30",0.45,0.6)
def cone(loc,r1,r2,depth,m,verts=10,rot=None):
    bpy.ops.mesh.primitive_cone_add(vertices=verts,radius1=r1,radius2=r2,depth=depth,location=loc); o=bpy.context.object
    if rot: o.rotation_euler=rot
    o.data.materials.append(m); uvbox(o,1.0); return o
GND=lambda w=6,d=6: box((0,0,0.02),(w,d,0.04),C("Asphalt","35373b",0.85))
SMALL=(-5,-6,3); 
@reg("OT_TrafficLight",(-7,-9,4),(0,0,3.5),26,(800,900))
def traffic():
    P=POLE(); Y=C("SignalBody","e8b81e",0.5)
    cyl((0,0,3),0.15,6,P,10); box((2.6,0,5.8),(5.2,0.18,0.18),P); box((1.2,0,5.4),(2.4,0.06,0.06),P,rot=(0,math.radians(-18),0))
    for x in (2.2,4.6):
        box((x,0,5.2),(0.4,0.35,1.1),Y,bev=0.04)
        for i,(z,c,e) in enumerate(((5.55,"ff2a2a",3.5),(5.2,"ffb01f",0.4),(4.85,"2aff6a",0.4))):
            cyl((x,-0.19,z),0.12,0.04,C(f"Lamp{c}{e}",c,0.3,emit=e),12,rot=(math.radians(90),0,0))
    box((0.0,-0.12,2.6),(0.35,0.25,0.5),Y); box((0,0,0.15),(0.5,0.5,0.3),P)
    box((1.6,-0.1,6.25),(1.2,0.05,0.35),C("HwyGreen","0f5a35",0.5)); box((1.6,-0.13,6.25),(1.0,0.02,0.2),C("SignWhiteGlow","f4f8ff",0.4,emit=0.6))
@reg("OT_StreetLight",(-7,-9,4),(0,0,4),26,(800,900))
def streetlight():
    P=POLE(); cyl((0,0,4.5),0.13,9,P,10); cyl((0,0,0.3),0.3,0.6,P,12)
    for s in (-1,1): box((s*1.0,0,8.9),(2.0,0.15,0.12),P); box((s*1.9,0,8.8),(0.7,0.35,0.18),P,bev=0.03); box((s*1.9,0,8.7),(0.55,0.28,0.04),led())
    box((0,-0.14,3.2),(0.4,0.04,1.2),C("Banner","c4261d",0.6))
@reg("OT_StopSign",SMALL,(0,0,1.4),28,(700,800))
def stop():
    cyl((0,0,1.25),0.05,2.5,C("Galv","b9bec4",0.35,0.85),8)
    cyl((0,-0.06,2.4),0.38,0.04,C("StopRed","c4161d",0.4),8,rot=(math.radians(90),0,math.radians(22.5)))
    cyl((0,-0.085,2.4),0.31,0.02,C("StopBorder","f0f0ee",0.5),8,rot=(math.radians(90),0,math.radians(22.5)))
    cyl((0,-0.1,2.4),0.29,0.02,C("StopRed","c4161d",0.4),8,rot=(math.radians(90),0,math.radians(22.5)))
    box((0,-0.115,2.4),(0.4,0.01,0.1),C("StopText","f0f0ee",0.5))
@reg("OT_Crosswalk",(-8,-10,6),(0,0,0),26,(800,700))
def crosswalk():
    for k in range(8): box((-4.2+k*1.2,0,0.02),(0.6,4,0.03),C("PaintWhite","f0f0ee",0.6))
    box((0,-2.6,0.02),(10,0.3,0.03),C("PaintWhite","f0f0ee",0.6))
@reg("OT_BusStop",(-6,-8,3),(0,0,1.3),26,(900,700))
def busstop():
    F=C("Galv","b9bec4",0.35,0.85); G=C("ShelterGlass","8fb7c9",0.05,0.2)
    for x in (-1.9,1.9):
        for y in (-0.6,0.7): box((x,y,1.2),(0.08,0.08,2.4),F)
    box((0,0.05,2.45),(4.2,1.7,0.1),F); box((0,0.75,1.3),(3.8,0.04,2.0),G); box((-1.9,0.05,1.3),(0.04,1.2,2.0),G)
    box((1.9,0.1,1.4),(0.06,1.1,1.8),C("AdPanel","f4f8ff",0.3,emit=2.0))
    box((0,0.45,0.48),(3.0,0.4,0.06),F); box((2.6,-0.6,1.4),(0.06,0.06,2.8),F); box((2.6,-0.62,2.6),(0.5,0.03,0.5),C("BusSign","1f6db0",0.4))
    box((0,0,0.06),(5,2.4,0.12),T_("Concrete","walk",(0.9,0.9,0.88)))
@reg("OT_Hydrant",(-1.6,-2,0.9),(0,0,0.4),34,(600,600))
def hydrant():
    R=C("HydrantRed","c4161d",0.45,0.2); cyl((0,0,0.35),0.15,0.7,R,12); sphere((0,0,0.7),0.15,R,2); cyl((0,0,0.05),0.22,0.1,R,12)
    for a in (0,math.pi): cyl((math.cos(a)*0.17,math.sin(a)*0.17,0.45),0.06,0.12,R,8,rot=(0,math.radians(90),a))
    cyl((0,-0.17,0.38),0.08,0.12,R,8,rot=(math.radians(90),0,0)); cyl((0,0,0.86),0.04,0.06,C("Brass","c9a64a",0.3,0.9),8)
@reg("OT_TrashCan",(-1.6,-2,1.0),(0,0,0.5),34,(600,600))
def trashcan():
    G=C("CanGreen","1f4a32",0.5,0.3); cyl((0,0,0.5),0.32,1.0,G,14); cyl((0,0,1.02),0.35,0.08,G,14)
    for k in range(8): a=k*math.pi/4; box((math.cos(a)*0.33,math.sin(a)*0.33,0.5),(0.05,0.05,0.95),C("CanRib","15301f",0.5,0.3),rot=(0,0,a))
@reg("OT_Bench",(-2.5,-3,1.2),(0,0,0.4),34,(700,600))
def benchm(): bench(0,0)
@reg("OT_Dumpster",(-3.5,-4.5,2),(0,0,0.7),30,(700,600))
def dumpster():
    B=C("DumpBlue","1f4e8c",0.55,0.4); box((0,0,0.75),(2.0,1.3,1.3),B,bev=0.04); box((0,0.05,1.45),(2.05,1.4,0.1),C("Lid","2a2c30",0.6),rot=(math.radians(4),0,0))
    for x in (-0.8,0.8): cyl((x,0,0.08),0.08,0.06,C("Tire","151515",0.85),10,rot=(math.radians(90),0,0))
@reg("OT_Billboard",(-14,-18,6),(0,0,8),26,(900,800))
def billboard():
    P=C("Galv","b9bec4",0.35,0.85)
    cyl((0,0,5),0.4,10,P,12); box((0,0,13),(12,0.6,5),P); box((0,-0.32,13),(11.6,0.04,4.6),C("AdFace","f4f8ff",0.3,emit=1.5))
    box((0,-0.33,13.6),(6,0.02,1.2),C("AdRed","d0181e",0.4)); box((-3.5,-0.33,12.3),(3,0.02,1.4),C("AdDark","1a1a1a",0.5))
    box((0,-1.0,10.4),(12,1.2,0.1),P); 
    for x in (-4,0,4): box((x,-1.3,10.6),(0.1,0.8,0.1),P); box((x,-1.6,10.8),(0.5,0.3,0.15),led())
@reg("OT_ParkedCar",(-5,-6,2.2),(0,0,0.7),30,(900,600))
def parked(): car(0,0,0,"9aa0a6")
@reg("OT_Tree_Pine",(-7,-9,4),(0,0,5),28,(700,900))
def pine():
    cyl((0,0,1.5),0.3,3,C("Bark","4a3424",0.9),8)
    for i,(z,r) in enumerate(((3,3.0),(5,2.4),(7,1.8),(8.8,1.2))): cone((0,0,z),r,0,2.8,C("PineNeedle","2d5a2e",0.9),9,rot=(0,0,i*0.4))
@reg("OT_Tree_Oak",(-8,-10,4),(0,0,4),28,(800,800))
def oak():
    cyl((0,0,1.6),0.35,3.2,C("Bark","4a3424",0.9),8); cyl((0.5,0,3.6),0.18,1.8,C("Bark","4a3424",0.9),6,rot=(0,math.radians(30),0))
    for (x,y,z,r,c) in ((0,0,5,2.6,"3f6e2c"),(1.6,0.4,4.4,1.8,"58893a"),(-1.5,-0.5,4.6,1.9,"4a7a33"),(0.4,-1.4,5.6,1.6,"58893a"),(-0.4,1.3,5.8,1.5,"3f6e2c")):
        sphere((x,y,z),r,C(f"Leaf{c}",c,0.9),1)
@reg("OT_Tree_Palm",(-8,-10,4),(0,0,5),28,(700,900))
def palm():
    BK=C("PalmBark","8a6a48",0.9); LF=C("PalmLeaf","4f8a3a",0.8)
    pts=[(0,0,0)]
    for i in range(1,9): pts.append((math.sin(i/8*1.2)*1.4,0,i*1.0))
    for a,b in zip(pts,pts[1:]):
        m=[(a[k]+b[k])/2 for k in range(3)]; ln=math.dist(a,b); ang=math.atan2(b[0]-a[0],b[2]-a[2])
        cyl(tuple(m),0.22,ln+0.05,BK,8,rot=(0,ang,0))
    top=pts[-1]
    for k in range(8):
        a=k*math.pi/4
        for j in range(3):
            d=0.9+j*0.9; z=top[2]+0.2-0.25*j*j
            box((top[0]+math.cos(a)*d,math.sin(a)*d,z),(1.0,0.5-j*0.1,0.05),LF,rot=(0,math.radians(15+j*18),a)) if False else box((top[0]+math.cos(a)*d,top[1]+math.sin(a)*d,z),(1.0,0.55-j*0.12,0.06),LF,rot=(0,math.radians(12+j*20),a))
    sphere(top,0.4,C("Coconut","5a4a2a",0.8),1)
@reg("OT_Bush",(-3,-4,1.6),(0,0,0.6),30,(700,600))
def bush():
    for (x,y,r,c) in ((0,0,0.9,"3e6b2f"),(0.7,0.3,0.7,"5a8a3a"),(-0.6,-0.2,0.75,"4a7a33"),(0.1,-0.6,0.6,"5a8a3a")): sphere((x,y,r*0.75),r,C(f"Shrub{c}",c,0.9),1)
@reg("OT_Rock_A",(-6,-8,3),(0,0,1),28,(700,600))
def rock():
    RK=T_("Rock","granite",(0.62,0.6,0.56))
    for (x,y,z,s) in ((0,0,0.8,(2.2,1.6,1.3)),(1.6,0.6,0.4,(1.2,1.0,0.8)),(-1.4,-0.5,0.3,(1.0,0.9,0.6))):
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=1,location=(x,y,z)); o=bpy.context.object; o.scale=s; o.rotation_euler=(0.3,0.2,x); o.data.materials.append(RK); uvbox(o,2.0)
@reg("OT_Grandstand",(-50,-60,18),(0,0,8),24,(1150,780))
def grandstand():
    CO=T_("Concrete","plaster",(0.8,0.8,0.78)); ST=C("Galv","b9bec4",0.35,0.85); RED=C("OTRed","d0181e",0.35)
    L=70; rows=14
    for r in range(rows):
        box((0,r*0.9,0.6+r*0.55),(L,0.9,0.3+r*0.0),CO)
        box((0,r*0.9+0.2,0.95+r*0.55),(L,0.35,0.4),[RED,C("SeatW","f0efe9",0.5),C("SeatB","1f4e8c",0.5)][(r//3)%3])
    box((0,rows*0.9/2,(0.6+rows*0.55)/2),(L,rows*0.9,0.6+rows*0.55),CO) if False else None
    box((0,rows*0.9+0.5,5),(L,1.0,10),CO)                                      # back wall
    for x in range(-35,36,7): box((x,rows*0.9+0.2,9),(0.5,0.5,10),ST)
    box((0,6,14.4),(L+2,16,0.5),ST,rot=(math.radians(-6),0,0))                  # roof
    box((0,-1.95,14.9),(L+2,0.06,0.5),led())
    box((0,-0.8,1.4),(L,0.1,1.2),C("Fence","8e959c",0.4,0.8)); 
    for k in range(10): box((-31.5+k*7,-0.86,1.4),(5,0.04,0.8),[RED,C("AdW","f4f8ff",0.3,emit=1.0)][k%2])
    box((0,rows*0.9+4,8),(18,6,16),CO)                                           # press box tower
    box((0,rows*0.9+0.95,13),(16,0.06,3),glass())
    box((0,-4,0.03),(L+10,6,0.06),C("Asphalt","35373b",0.85))
@reg("OT_PitBuilding",(-40,-48,10),(0,0,4),24,(1150,780))
def pits():
    WH=T_("Panel","plaster",(0.95,0.95,0.96)); RED=C("OTRed","d0181e",0.35)
    L=60
    box((0,4,3),(L,8,6),WH,uv=2.0)
    for i in range(10): 
        x=-27+i*6; box((x,-0.03,2.2),(4.6,0.06,4.0),C("PitDark","1a1c20",0.8)); box((x,-0.06,4.6),(5.2,0.06,0.5),RED)
        box((x,-0.07,4.6),(1.2,0.03,0.35),C("PitNum","f4f8ff",0.3,emit=1.5))
    box((0,4,7.5),(L,8,3),glass()); box((0,4,9.2),(L+1,9,0.4),WH)
    box((0,-3,6.2),(L,6,0.25),WH)
    for x in range(-30,31,10): box((x,-5.8,3.1),(0.3,0.3,6.2),C("Galv","b9bec4",0.35,0.85))
    box((0,-7,0.03),(L+6,12,0.06),C("Asphalt","35373b",0.85)); box((0,-10,0.06),(L+6,0.25,0.03),C("PaintWhite","f0f0ee",0.6))
@reg("OT_DragStartTower",(-14,-16,6),(0,0,4),26,(900,800))
def dragtree():
    P=C("Galv","b9bec4",0.35,0.85); BK=C("TreeBody","1a1a1a",0.5)
    cyl((0,0,2.5),0.18,5,P,10); box((0,0,5.6),(0.7,0.3,2.6),BK)
    for i,(c,e) in enumerate((("f6c22c",3),("f6c22c",3),("f6c22c",0.5),("f6c22c",0.5),("f6c22c",0.5),("2aff6a",0.5),("ff2a2a",0.5))):
        for s in (-1,1): cyl((s*0.18,-0.16,6.7-i*0.33),0.11,0.04,C(f"DL{c}{e}",c,0.3,emit=e),10,rot=(math.radians(90),0,0))
    box((0,0,0.15),(1.2,1.2,0.3),T_("Concrete","plaster",(0.8,0.8,0.78)))
    box((9,6,4),(5,5,8),T_("Block","plaster",(0.82,0.82,0.82))); box((9,3.47,6),(4.4,0.06,2),glass()); box((9,6,8.3),(5.6,5.6,0.6),C("OTRed","d0181e",0.35))
    for k in range(5): box((9+0,3.4,8.3),(4.6,0.04,0.3),C("TowerSign","f4f8ff",0.3,emit=2.0)) if k==0 else None
    box((0,-1,0.03),(14,8,0.06),C("Asphalt","35373b",0.85)); box((0,-1,0.07),(14,0.25,0.03),C("PaintWhite","f0f0ee",0.6))
@reg("OT_Bleachers",(-14,-18,6),(0,0,1.5),26,(900,700))
def bleachers():
    AL=C("Aluminum","c9ccd1",0.3,0.8); ST=C("Galv","8e959c",0.4,0.8); L=16
    for r in range(6):
        box((0,r*0.75,0.45+r*0.45),(L,0.35,0.06),AL); box((0,r*0.75+0.3,0.25+r*0.45),(L,0.04,0.35),AL)
    for x in range(-8,9,4):
        box((x,2.25,1.6),(0.1,4.6,0.1),ST,rot=(math.radians(-31),0,0)); box((x,4.0,1.6),(0.1,0.1,3.2),ST); box((x,0,0.25),(0.1,0.1,0.5),ST)
    box((0,4.3,3.4),(L,0.06,1.0),AL)
@reg("OT_FestivalHub",(-60,-70,20),(0,0,8),24,(1150,800))
def festival():
    WH=C("TentWhite","f2f2ee",0.6); MG=C("FestMagenta","e0287a",0.4); CY=C("NeonCyan","2fe0ff",0.3,emit=5.0); PK=C("NeonPink","ff3fb4",0.3,emit=5.0)
    # main stage
    box((0,10,1),(26,12,2),C("Stage","1a1a1a",0.5))
    for x in (-13,13): box((x,10,8),(1,1,14),C("Truss","9aa0a6",0.35,0.85))
    box((0,10,15),(27,1,1),C("Truss","9aa0a6",0.35,0.85)); box((0,15.5,8),(26,0.4,12),C("LEDScreen","1b1f3a",0.3,emit=0.8))
    box((0,15.3,8),(20,0.05,8),C("ScreenGlow","ff3fb4",0.3,emit=2.0))
    for k in range(9): box((-12+k*3,10,15.6),(0.4,0.4,0.4),[CY,PK][k%2])
    # tents
    for i,(x,y) in enumerate(((-30,-6),(30,-6),(-30,16),(30,16))):
        box((x,y,1.6),(12,10,3.2),WH); cone((x,y,4.6),8.4,0.3,3,MG if i%2 else WH,4,rot=(0,0,math.radians(45)))
        box((x,y-5.05,2.8),(8,0.06,0.8),[MG,C("FestBlue","1f6db0",0.4)][i%2])
    # entry arch
    for s in (-1,1): box((s*7,-24,5),(2,2,10),MG)
    box((0,-24,10.5),(16,2.2,2),MG); box((0,-25.15,10.5),(13,0.06,1.2),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    for z in (9.3,11.7): box((0,-25.18,z),(16,0.06,0.15),CY)
    # flags + light towers
    for k in range(14):
        a=k/14*math.pi*2; x,y=math.cos(a)*38,math.sin(a)*24+4; cyl((x,y,4),0.1,8,C("Galv","b9bec4",0.35,0.85),6); box((x+0.7,y,7.4),(1.4,0.04,0.9),[MG,CY,C("FestYellow","f6c22c",0.4)][k%3])
    for x in (-20,20): cyl((x,-14,7),0.3,14,C("Galv","b9bec4",0.35,0.85),8); box((x,-14,14.4),(3,0.6,1.2),C("Galv","b9bec4",0.35,0.85)); box((x,-14.32,14.4),(2.6,0.04,0.9),led())
    box((0,0,0.03),(90,60,0.06),T_("Pavement","walk",(0.86,0.86,0.84)),uv=3.0)
    for x in range(-40,41,8): box((x,-18,0.08),(0.15,8,0.02),C("PaintWhite","f0f0ee",0.6))
@reg("OT_Lighthouse",(-26,-32,10),(0,0,12),24,(800,1000))
def lighthouse():
    WH=C("LHWhite","f2f2ee",0.5); RD=C("LHRed","c4161d",0.45); RK=T_("Rock","granite",(0.62,0.6,0.56))
    for i in range(6): cone((0,0,1+i*3.5),3.2-i*0.3,3.2-(i+1)*0.3,3.5,[WH,RD][i%2],20)
    cyl((0,0,22.5),2.0,0.5,C("Gallery","2a2c30",0.4,0.6),20); cyl((0,0,24),1.3,2.6,C("LampGlass","fff4c0",0.1,emit=6.0),16)
    cone((0,0,26),1.6,0.2,1.8,RD,16); cyl((0,0,23),2.1,1.0,C("Rail","1c1c1c",0.5,0.6),20) if False else None
    for k in range(16): a=k*math.pi/8; box((math.cos(a)*1.95,math.sin(a)*1.95,23.3),(0.06,0.06,1.0),C("Rail","1c1c1c",0.5,0.6))
    box((5,0,1.8),(5,4,3.6),WH); prism((5,0,3.6),5,1.6,4.2,RD); box((5,-2.03,1.3),(0.9,0.06,2),C("Door","3a2416",0.4))
    for (x,y,s) in ((0,0,6),(-4,3,3),(4,4,3.4),(-3,-4,3)):
        bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=1,location=(x,y,-s*0.4)); o=bpy.context.object; o.scale=(s,s*0.9,s*0.7); o.data.materials.append(RK); uvbox(o,2.0)
@reg("OT_Pier",(-30,-36,9),(0,8,1),24,(1150,780))
def pier():
    WD=T_("Wood","wood",(0.8,0.62,0.45)); PL=T_("Wood","wood",(0.55,0.42,0.3)); RL=C("PierRail","f0efe9",0.5)
    L=60; Wd=8
    box((0,L/2,2.5),(Wd,L,0.4),WD,uv=1.5)
    for y in range(0,L+1,6):
        for x in (-Wd/2+0.3,Wd/2-0.3): cyl((x,y,0.5),0.3,5,PL,8)
    for s in (-1,1):
        box((s*(Wd/2-0.1),L/2,3.7),(0.15,L,0.12),RL); box((s*(Wd/2-0.1),L/2,3.2),(0.08,L,0.08),RL)
        for y in range(0,L+1,3): box((s*(Wd/2-0.1),y,3.2),(0.1,0.1,1.2),RL)
    for y in range(6,L,12):
        for s in (-1,1): cyl((s*(Wd/2-0.6),y,4.8),0.08,4.6,C("PoleDark","2a2c30",0.45,0.6),8); sphere((s*(Wd/2-0.6),y,7.2),0.28,C("GlobeLamp","fff0cc",0.2,emit=4.0),1)
    box((0,L+4,4),(10,8,3),T_("Siding","plaster",(0.92,0.86,0.76))); prism((0,L+4,5.5),10.6,2.2,8.6,C("RoofTeal","1fa6a0",0.5))
    for k in range(4): bench(-2+k*1.0 if False else 0, 14+k*12) if False else None
    box((0,L/2,-0.5),(40,L+30,1),C("Water","2c5f78",0.1,0.2)) if False else None
name=sys.argv[-2]; mode=sys.argv[-1]
f,cam,tgt,lens,res=BLD[name]; reset(); random.seed(hash(name)%1000); _cache.clear(); f()
if mode=="render": world_and_render(f"/home/claude/blender/r_{name}.png",cam,tgt,lens,res,16)
else: export(name,drop_y=-999)
