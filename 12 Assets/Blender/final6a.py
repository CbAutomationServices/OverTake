exec(open("/home/claude/blender/kit3.py").read())
import sys
@reg("OT_Dealership_A",(-36,-44,8),(2,-6,3),24,(1150,800))
def dealership():
    GL=C("ShowGlass","24353f",0.04,0.4); FR=C("Mullion","c9ccd1",0.25,0.9); RED=C("OTRed","d0181e",0.3,0.2); CY=C("NeonCyan","2fe0ff",0.3,emit=6.0)
    ACM=T_("ACMPanel","metal",(0.78,0.8,0.83),0.7,True); DK=C("DarkPanel","23262b",0.4,0.5); TL=T_("Tile","tile",(0.92,0.92,0.94)); WD=T_("Wood","wood",(0.85,0.62,0.42))
    W,D,H=34,20,8; FZ=-D/2
    box((0,0,0.2),(W+2,D+2,0.4),CONC(),uv=2.0)
    box((0,0,0.42),(W,D,0.04),TL,uv=1.2)                                                # showroom floor
    box((W/2-3,0,H/2),(6,D,H),ACM,uv=2.5); box((-W/2+1,2,H/2),(2,D-4,H),ACM,uv=2.5)     # solid ends
    box((-1,FZ+0.1,H/2),(W-8,0.06,H),GL); box((-W/2+0.2,0,H/2),(0.06,D,H),GL)            # glass faces
    for x in range(-15,15,3): box((x,FZ,H/2),(0.14,0.18,H),FR)
    for y in range(-8,10,3): box((-W/2+0.1,y,H/2),(0.18,0.14,H),FR)
    box((-1,FZ,4.6),(W-8,0.14,0.12),FR)
    # interior: lit back wall, reception desk, ceiling lights, rug
    box((-2,D/2-0.3,H/2),(W-10,0.3,H),C("BackWall","f2efe9",0.6)); box((-2,D/2-0.5,5.4),(14,0.06,1.2),C("WallLogo","d0181e",0.3,emit=1.5))
    box((8,5,0.95),(5,1.2,1.1),WD,bev=0.04); box((8,5,1.52),(5.2,1.4,0.06),C("Counter","f0efe9",0.3))
    for x in range(-12,10,4):
        for y in (-5,1,6): box((x,y,H-0.25),(1.6,1.6,0.06),C("CeilLight","fff6e6",0.3,emit=3.5))
    box((0,0,H-0.1),(W-1,D-1,0.16),C("Ceiling","e9e6df",0.7))
    for i,(x,col) in enumerate(((-10,"d0181e"),(-2,"1f6db0"),(6,"e8b81e"))):
        cyl((x,-3,0.5),3.0,0.12,C("Turntable","2a2c30",0.2,0.8),28); cyl((x,-3,0.57),2.6,0.02,CY,28); car2(x,-3,math.radians(25+i*25),col,0.58,"coupe" if i==1 else "sedan")
    # floating canopy + entrance portal
    box((-2,-1,H+0.6),(W+8,D+6,1.0),DK,bev=0.06); box((-2,FZ-4.05,H+0.6),(W+8,0.08,0.3),CY); box((-2,-1,H+0.08),(W+7,D+5,0.06),C("Soffit","d8d4cc",0.6))
    for x in range(-18,16,6): box((x,FZ-3.6,H+0.07),(1.2,0.3,0.04),led())
    frustum((-6,FZ-0.8,0),2.6,9,2.6,9,H+3.5,RED,0)                                       # red portal fin
    box((-6,FZ-0.8,H/2),(6,2.8,H-1.4),C("PortalHole","1a1e24",0.1)) 
    box((-6,FZ-2.15,H+2.4),(7.6,0.06,1.4),C("SignWhiteGlow","f4f8ff",0.3,emit=4.0))
    for s in (-1,1): box((-6+s*3.6,FZ-1.4,2.4),(0.4,0.4,4.8),FR)
    # service building
    box((W/2+7,3,4.5),(12,16,9),ACM,uv=2.5); box((W/2+7,3,9.2),(12.4,16.4,0.4),DK)
    for i in range(3):
        x=W/2+3+i*4; box((x,3-8.03,2.5),(3.4,0.06,4.6),C("BayLit","2a2e36",0.6)); box((x,3-8.06,4.95),(3.6,0.1,0.25),RED)
        box((x,3-7.0,0.6),(0.3,1.2,1.2),C("Lift","e8b81e",0.5)); box((x,3-8.07,3.6),(2.8,0.03,0.08),led())
    box((W/2+7,3-8.15,7.3),(10,0.2,1.2),RED); box((W/2+7,3-8.27,7.3),(8.6,0.04,0.7),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    # front lot with cars, flags, planters
    box((0,FZ-12,0.06),(W+16,14,0.08),ASPH(),uv=3.0)
    cols=["d0181e","1a1a1a","f0f0ee","1f6db0","9aa0a6","e07a3a","2f8a4a","7a3a9e","e8b81e","c9ccd1"]
    for k in range(10): box((-19+k*3.8,FZ-9,0.11),(0.12,5.6,0.02),WHITE())
    for x in (-21,21): planter(x,FZ-3,3,1.2,CONC2(),3)
    for k in range(8):
        x=-18+k*5.2; cyl((x,FZ-5.8,3.5),0.07,7,FR,6); box((x+0.75,FZ-5.8,6.4),(1.5,0.03,1.0),[RED,C("FlagW","f0efe9",0.5),C("FlagBlue","1f6db0",0.5)][k%3])
    lot(0,FZ-25,W+16,10,10,-15,FZ-25,3.3)
    PX=W/2+12; cyl((PX,FZ-18,6),0.5,12,DK,12)                                                  # pylon sign
    frustum((PX,FZ-18,11),1.2,3.2,1.0,2.8,6,RED,0); box((PX,FZ-18.62,14),(2.4,0.04,3.4),C("SignWhiteGlow","f4f8ff",0.3,emit=3.5))
    box((PX,FZ-18.63,12),(2.2,0.04,0.8),C("LEDScreen","1b1f3a",0.3,emit=0.9)); box((PX,FZ-18.64,12),(1.8,0.03,0.4),CY)
    for x in (-24,-8,8,24): lightpole(x,FZ-30,10,2.0,1); lightpole(x+0.3,FZ-30,10,2.0,-1)
    for x in (-24,24): tree(x,FZ-20,1.1)
@reg("OT_Overpass_Freeway",(-34,-42,12),(0,0,4),24,(1150,780))
def overpass():
    CO=CONC(); AS=ASPH(); L,Wd,Hc=40,24,6.5
    box((0,0,Hc+0.3),(L,Wd,0.6),AS,uv=3.0); box((0,0,Hc-0.4),(L,Wd+0.8,0.8),CO)
    for y in (-9,-4.5,0,4.5,9): frustum((-L/2,y,Hc-2.3),0.6,L,1.1,L,1.6,CO,0); box((0,y,Hc-0.75),(L,1.6,0.3),CO)   # I-girders
    for x in (-L/2+0.4,L/2-0.4): box((x,0,Hc-1.5),(0.8,Wd,1.6),CO)                        # end diaphragms
    for x in (-12,12):
        box((x,0,Hc-3.0),(2.0,Wd-1,1.3),CO,bev=0.12)
        for y in (-8,0,8):
            cyl((x,y,(Hc-3.6)/2),0.85,Hc-3.6,CO,20); box((x,y,Hc-2.25),(1.0,1.0,0.12),C("BearingPad","1a1a1a",0.8))
            box((x,y,0.3),(2.4,2.4,0.6),CO)
    for s in (-1,1):
        y=s*(Wd/2-0.4)
        box((0,y,Hc+0.85),(L,0.6,0.5),CO); box((0,y,Hc+1.3),(L,0.32,0.5),CO)               # barrier
        box((0,y,Hc+2.6),(L,0.05,2.0),C("ChainLink","9aa0a6",0.5,0.7))                     # fence
        for x in range(-20,21,3): box((x,y,Hc+2.6),(0.08,0.08,2.1),GALV())
        box((0,y,Hc+3.62),(L,0.08,0.08),GALV())
        for x in range(-18,19,6): box((x,s*(Wd/2+0.42),Hc-0.6),(0.3,0.15,0.15),C("Scupper","3a3d42",0.6,0.5))
    for x in (-L/2,L/2): box((x,0,Hc+0.61),(0.25,Wd,0.04),GALV())                          # expansion joints
    for y in (-3.6,3.6,-7.2,7.2):
        for k in range(10): box((-18+k*4,y,Hc+0.61),(2.4,0.15,0.02),WHITE())
    for y in (-0.5,0.5): box((0,y,Hc+0.61),(L,0.15,0.02),YELW())
    for s in (-1,1): box((0,s*(Wd/2-1.1),Hc+0.61),(L,0.15,0.02),WHITE())
    for x in (-14,6):
        cyl((x,Wd/2-0.5,Hc+5.5),0.16,9,POLE(),10); box((x,Wd/2-1.9,Hc+9.9),(0.35,2.8,0.22),POLE()); box((x,Wd/2-2.8,Hc+9.77),(0.3,1.2,0.05),led())
    box((0,0,0.05),(L+30,Wd+20,0.1),ASPH(),uv=4.0)
    for k in range(12): box((-24+k*4.5,0,0.11),(2.4,0.15,0.02),WHITE())
@reg("OT_Bridge_Steel",(-44,-56,16),(0,0,8),24,(1150,780))
def bridge():
    ST=C("BridgeSteel","2f5a7a",0.35,0.75); RV=C("BridgeSteelDark","24465f",0.4,0.75); CO=CONC(); STN=T_("Stone","granite",(0.92,0.9,0.86)); AS=ASPH()
    L,Wd,Hd,Ha=64,15,8,15
    box((0,0,Hd),(L,Wd,0.6),AS,uv=3.0); box((0,0,Hd-0.6),(L,Wd+0.6,0.7),CO)
    for x in range(-30,31,4): box((x,0,Hd-1.2),(0.5,Wd,0.6),RV)                             # floor beams
    for s in (-1,1): box((0,s*(Wd/2-0.2),Hd-1.0),(L,0.6,1.2),ST)                            # tie girders
    R=L/2-2
    for s in (-1,1):
        y=s*(Wd/2+0.1)
        n=28
        for i in range(n):
            a0=math.pi*i/n; a1=math.pi*(i+1)/n
            p0=(-math.cos(a0)*R, Hd+math.sin(a0)*Ha); p1=(-math.cos(a1)*R, Hd+math.sin(a1)*Ha)
            mx,mz=(p0[0]+p1[0])/2,(p0[1]+p1[1])/2; ln=math.hypot(p1[0]-p0[0],p1[1]-p0[1]); ang=-math.atan2(p1[1]-p0[1],p1[0]-p0[0])
            box((mx,y,mz),(ln+0.15,1.0,1.3),ST,rot=(0,ang,0)); box((mx,y,mz+0.66),(ln+0.15,1.1,0.12),RV,rot=(0,ang,0))
        for k in range(1,14):
            x=-R+k*2*R/14; hz=math.sqrt(max(0,1-(x/R)**2))*Ha
            if hz>1: cyl((x,y,Hd+hz/2),0.09,hz,RV,6)
        box((0,s*(Wd/2-0.6),Hd+0.9),(L,0.12,0.12),GALV()); box((0,s*(Wd/2-0.6),Hd+0.5),(L,0.08,0.08),GALV())
        for x in range(-30,31,2): box((x,s*(Wd/2-0.6),Hd+0.6),(0.06,0.06,0.7),GALV())
    for k in range(-5,6):                                                                     # top cross bracing
        x=k*4.4; hz=math.sqrt(max(0,1-(x/R)**2))*Ha
        if hz>6: box((x,0,Hd+hz-0.2),(0.5,Wd+0.4,0.5),ST)
        if hz>8 and k%2==0:
            for d in (-1,1): box((x+2.2,0,Hd+hz-0.4),(0.25,math.hypot(Wd,4.4),0.25),RV,rot=(0,0,d*math.atan2(4.4,Wd)+math.pi/2))
    for x in (-L/2,L/2):
        box((x,0,Hd/2-1.5),(3.4,Wd+2.4,Hd+1),STN,uv=1.5); box((x,0,Hd-0.9),(3.8,Wd+2.8,0.6),CO)
    for s in (-1,1):
        for x in (-L/2+2,0,L/2-2):
            cyl((x,s*(Wd/2-0.4),Hd+3),0.1,5,POLE(),8); sphere((x,s*(Wd/2-0.4),Hd+5.6),0.3,C("GlobeLamp","fff0cc",0.2,emit=4.0),1)
    sphere((0,0,Hd+Ha+0.6),0.35,C("GlowRed","ff2a2a",0.3,emit=6.0),1)
    for k in range(8): box((-28+k*8,0,Hd+0.31),(4,0.15,0.02),WHITE())
@reg("OT_TunnelPortal",(-28,-36,7),(0,0,5),24)
def tunnel():
    CO=CONC(); STN=T_("Stone","granite",(0.92,0.9,0.86)); AS=ASPH(); DK=C("TunnelDark","0b0c0e",0.95)
    Wd=12; zc=4.0; R=Wd/2; Hw=zc+R+3
    box((0,0.8,Hw/2),(Wd+14,1.6,Hw),STN,uv=1.4)                                             # stone portal face
    box((0,-0.02,zc/2),(Wd,0.1,zc),DK)
    for k in range(12):
        z0=k*R/12; z1=(k+1)*R/12; w=2*math.sqrt(max(R*R-z1*z1,0)); w0=2*math.sqrt(R*R-z0*z0)
        box((0,-0.02,zc+(z0+z1)/2),((w+w0)/2,0.1,z1-z0+0.02),DK)
    for k in range(15):                                                                      # concrete arch ring + keystone
        a=math.pi*k/14; box((math.cos(a)*(R+0.5),-0.15,zc+math.sin(a)*(R+0.5)),(1.0,0.4,0.8 if k==7 else 0.55),CO,rot=(0,-a,0))
    for s in (-1,1): box((s*(R+0.5),-0.15,zc/2),(1.0,0.4,zc),CO)
    box((0,0.3,Hw+0.4),(Wd+16,2.4,0.8),CO); box((0,-0.92,Hw+0.4),(Wd+16,0.05,0.12),C("Trim","8e959c",0.5))
    box((0,-0.2,Hw-1.4),(7,0.12,1.1),C("TunnelSign","1f5a3a",0.4)); box((0,-0.27,Hw-1.4),(6,0.03,0.5),C("SignWhiteGlow","f4f8ff",0.4,emit=1.0))
    for s in (-1,1):
        box((s*(Wd/2+10.5),-2.5,2.6),(9,1.0,5.2),STN,rot=(0,0,s*math.radians(28)),uv=1.4)
        box((s*(Wd/2+10.5),-2.5,5.3),(9.2,1.2,0.3),CO,rot=(0,0,s*math.radians(28)))
        box((s*(R+1.6),-0.4,zc+1),(0.5,0.3,0.5),C("WallLamp","ffe2a0",0.3,emit=4.0))
        box((s*(R-0.3),-6,0.5),(0.6,12,1.0),CO); box((s*(R-0.3),-6,1.1),(0.3,12,0.3),CO)
        for k in range(4): box((s*(R-0.62),-1-k*3,0.7),(0.02,0.5,0.15),C("Reflector","ffcc33",0.3,emit=1.5))
    box((0,11,zc+R/2),(Wd,20,R+zc),DK); box((0,11,Hw),(Wd+4,20,2),CO)
    for k in range(4):
        for s in (-1,1): box((s*(R-0.4),2+k*4,zc+1.5),(0.3,1.2,0.12),C("TunnelLamp","ffe2a0",0.3,emit=5.0))
    box((0,-8,0.05),(Wd+4,30,0.1),AS,uv=3.0)
    for k in range(6): box((0,-20+k*5,0.11),(0.15,2.5,0.02),WHITE())
    for s in (-1,1): box((s*(R-1.2),-8,0.11),(0.15,30,0.02),WHITE())
    for (x,y,sc) in ((-15,4,(5,4,6)),(15,4,(5,4,6)),(-9,6,(4,3,4)),(9,6,(4,3,4)),(0,7,(9,4,4))):
        ico((x,y,Hw+sc[2]*0.2-1),sc,T_("Rock","granite",(0.6,0.58,0.54)),1,(0.2,0.1,x*0.1))
@reg("OT_Guardrail_10m",(-6,-8,2.5),(0,0,0.5),30,(900,600))
def gr():
    S=GALV(); P=C("GalvPost","8e959c",0.4,0.8)
    for z in (0.62,):
        box((0,0,z+0.12),(10,0.06,0.08),S); box((0,0.03,z),(10,0.1,0.16),S); box((0,0,z-0.12),(10,0.06,0.08),S)
    for i in range(6):
        x=-5+i*2; box((x,0.18,0.42),(0.12,0.12,0.9),P); box((x,0.1,0.62),(0.1,0.18,0.25),P)
        box((x,-0.05,0.75),(0.08,0.02,0.08),C("Reflector","ffcc33",0.3,emit=1.5))
    box((-5.4,0.15,0.62),(0.6,0.4,0.36),S,rot=(0,0,math.radians(30)))
    box((0,-1.5,0.03),(12,3,0.06),ASPH()); box((0,0.8,0.03),(12,1.6,0.06),C("Grass","567d3a",0.9))
@reg("OT_JerseyBarrier_10m",(-6,-8,2.5),(0,0,0.5),30,(900,600))
def jb():
    CO=CONC()
    for k in range(3):
        x=-3.35+k*3.35
        frustum((x,0,0),0.62,3.2,0.24,3.2,0.85,CO,0); box((x,0,0.07),(3.2,0.66,0.14),CO)
        box((x,-0.24,0.5),(0.6,0.02,0.15),C("Reflector","ffcc33",0.3,emit=1.5))
    box((-5,0,0.43),(0.06,0.5,0.8),C("Stripe","e8b81e",0.5)); box((5,0,0.43),(0.06,0.5,0.8),C("Stripe","e8b81e",0.5))
    box((0,-1.5,0.03),(12,3,0.06),ASPH())
@reg("OT_SignGantry",(-24,-28,7),(0,0,5),24)
def gantry():
    ST=GALV(); GR=C("HwyGreen","0f5a35",0.45); WH=C("SignWhiteGlow","f4f8ff",0.4,emit=0.9); Sp=28; H=7
    for s in (-1,1):
        for dy in (-0.7,0.7):
            for dx in (-0.4,0.4): box((s*Sp/2+dx,dy,H/2),(0.2,0.2,H+1.6),ST)
        for z in range(1,8,2): box((s*Sp/2,0,z),(0.9,1.5,0.1),ST)
        box((s*Sp/2,0,0.4),(2.2,2.6,0.8),CONC())
    for z in (H-0.3,H+1.5):
        for dy in (-0.7,0.7): box((0,dy,z),(Sp,0.22,0.22),ST)
    for k in range(14):
        x=-Sp/2+1+k*2; box((x,-0.7,H+0.6),(0.1,0.1,2.0),ST,rot=(0,math.radians(35 if k%2 else -35),0)); box((x,0.7,H+0.6),(0.1,0.1,2.0),ST,rot=(0,math.radians(35 if k%2 else -35),0))
    box((0,1.4,H-0.4),(Sp-2,0.9,0.08),ST); box((0,1.85,H+0.1),(Sp-2,0.05,0.9),C("CatRail","8e959c",0.4,0.8))
    for i,(x,ln) in enumerate(((-8.8,3),(0,2),(8.8,2))):
        box((x,-1.0,H+0.6),(7.8,0.16,3.4),GR,bev=0.05); box((x,-1.09,H+0.6),(7.4,0.02,3.0),C("SignBorder","f0f0ee",0.5)); box((x,-1.1,H+0.6),(7.2,0.02,2.8),GR)
        box((x-2.6,-1.12,H+1.55),(1.0,0.02,0.7),C("Shield","1f4e8c",0.4)); box((x-2.6,-1.13,H+1.65),(0.8,0.02,0.25),C("ShieldRed","c4161d",0.4))
        for r in range(ln): box((x+0.4,-1.12,H+1.55-r*0.65),(4.4-r*0.8,0.02,0.4),WH)
        box((x+0,-1.12,H-0.35),(0.4,0.02,0.7),WH); box((x,-1.12,H-0.62),(0.9,0.02,0.18),WH)
        for k in range(3): box((x-2.4+k*2.4,-1.5,H-1.2),(0.6,0.5,0.15),C("SignLamp","fff4e0",0.3,emit=3.0))
    box((0,0,0.03),(Sp+8,12,0.06),ASPH(),uv=3.0)
    for x in (-10.5,-3.5,3.5,10.5):
        for k in range(3): box((x,-4+k*4,0.07),(0.15,2.0,0.02),WHITE())
@reg("OT_ExitSign",(-8,-10,4),(0,0,3),28,(900,700))
def exitsign():
    ST=GALV(); GR=C("HwyGreen","0f5a35",0.45); WH=C("SignWhiteGlow","f4f8ff",0.4,emit=0.9)
    for x in (-1.6,1.6): box((x,0,2.6),(0.2,0.2,5.2),ST); box((x,0,0.2),(0.6,0.6,0.4),CONC())
    box((0,0.05,4.4),(4.0,0.1,0.12),ST); box((0,0.05,3.6),(4.0,0.1,0.12),ST)
    box((0,-0.15,4.4),(4.6,0.12,2.2),GR,bev=0.04); box((0,-0.22,4.4),(4.3,0.02,1.9),C("SignBorder","f0f0ee",0.5)); box((0,-0.23,4.4),(4.1,0.02,1.7),GR)
    box((0.3,-0.24,4.85),(3.0,0.02,0.42),WH); box((-0.3,-0.24,4.2),(1.8,0.02,0.36),WH); box((1.5,-0.24,3.85),(0.7,0.02,0.4),WH)
    box((1.4,-0.15,5.75),(1.6,0.1,0.6),C("ExitYellow","e8b81e",0.5)); box((1.4,-0.21,5.75),(1.2,0.02,0.3),C("ExitText","1a1a1a",0.5))
    box((0,0,0.03),(8,4,0.06),C("Grass","567d3a",0.9))
name=sys.argv[-2]; mode=sys.argv[-1]
f,cam,tgt,lens,res=BLD[name]; reset(); random.seed(hash(name)%1000); _cache.clear(); f()
if mode=="render": world_and_render(f"/home/claude/blender/r_{name}.png",cam,tgt,lens,res,18)
else: export(name,drop_y=-999)
