exec(open("/home/claude/blender/lib.py").read())
import sys
BLD={}
def reg(name,cam,tgt,lens=26,res=(1100,780)):
    def deco(f): BLD[name]=(f,cam,tgt,lens,res); return f
    return deco
def laps(x0,x1,fz,z0,z1,col,step=0.32):
    n=int((z1-z0)/step)
    for i in range(n): box(((x0+x1)/2,fz-0.03,z0+i*step),(x1-x0,0.04,0.035),col)
def laps_side(xp,y0,y1,z0,z1,col,step=0.32,dirx=1):
    n=int((z1-z0)/step)
    for i in range(n): box((xp+dirx*0.03,(y0+y1)/2,z0+i*step),(0.04,y1-y0,0.035),col)
GOLD=lambda: C("GoldGlow","ffd27a",0.3,emit=3.5)
@reg("OT_Jewelry_A",(-20,-26,4),(0,-3,4),26)
def jewelry():
    MB=T_("BlackMarble","marble",(0.22,0.22,0.24)); GR=T_("Granite","granite",(0.9,0.9,0.9)); BRS=C("Brass","c9a44e",0.3,0.95); BLK=C("Awning","141416",0.6)
    W,D,H=16,12,9; FZ=-D/2
    box((0,0,H/2),(W,D,H),MB,uv=2.0); box((0,FZ-0.1,0.4),(W+0.4,0.4,0.8),GR,bev=0.03)
    for x in (-5,5):                          # arched display windows w/ spotlit displays
        box((x,FZ-0.02,2.8),(4.2,0.06,3.6),warm()); box((x,FZ-0.05,2.8),(4.2,0.04,3.6),glass())
        halfcyl((x,FZ-0.04,4.6),2.1,0.08,glass(),24)
        for k in range(3): box((x-1.3+k*1.3,FZ+0.2,1.5),(0.8,0.5,0.9),C("DisplayCase","f2efe6",0.3)); sphere((x-1.3+k*1.3,FZ+0.2,2.1),0.15,GOLD(),1)
        box((x,FZ-0.1,1.0),(4.6,0.18,0.15),BRS); box((x,FZ-0.12,6.8),(4.6,0.2,0.2),BRS)
        for k in range(9): cyl((x-2.0+k*0.5,FZ-0.25,2.6),0.03,3.2,BRS,6)   # security bars
    box((0,FZ-0.05,2.2),(2.4,0.1,4.4),glass()); box((0,FZ-0.1,2.2),(0.08,0.12,4.4),BRS)
    box((0,FZ-0.1,4.5),(2.8,0.14,0.15),BRS)
    box((0,FZ-1.0,4.9),(3.6,2.0,0.12),BLK,rot=(math.radians(-12),0,0))
    signband(0,FZ,W-1,7.6,BLK,GOLD(),1.2,"1a1a1c")
    box((0,FZ-0.4,7.6),(10,0.04,0.5),GOLD())
    box((0,0,H+0.2),(W+0.5,D+0.5,0.4),GR,bev=0.04)
    for x in (-7.6,7.6): box((x,FZ-0.2,H/2),(0.8,0.4,H),GR,bev=0.03)
    for x in (-7.2,7.2): planter(x,FZ-1.6,1.2,1.2,GR,1)
    cyl((-6,FZ-3.5,2.2),0.12,4.4,BRS,10); cyl((-6,FZ-3.5,4.6),0.55,0.2,BRS,20,rot=(math.radians(90),0,0)); cyl((-6,FZ-3.62,4.6),0.45,0.04,C("ClockFace","f6f1e4",0.4,emit=1.0),20,rot=(math.radians(90),0,0))
    for x in (-3,3): bollard(x,FZ-3.6,BRS,0.9)
    lot(0,FZ-5,W+8,8)
@reg("OT_Convenience_A",(-22,-28,5),(0,-3,2.5),26)
def convenience():
    ST=T_("Stucco","plaster",(1.0,0.96,0.9)); BR=T_("Brick","brick",(0.85,0.7,0.62)); RED=C("Red","c4261d",0.45); GRN=C("Green24","1f8a4c",0.45)
    W,D,H=20,12,5; FZ=-D/2
    box((0,0,H/2),(W,D,H),ST,uv=1.6); box((0,FZ-0.05,0.5),(W+0.2,0.25,1.0),BR,bev=0.03)
    storefront(-2,FZ,13,2.8,0.9,7,True)
    for k in range(5): box((-7.5+k*2.6,FZ-0.1,2.0),(1.0,0.03,1.4),C("Poster","f2c230",0.5) if k%2 else C("Poster2","e2483a",0.5))
    box((7,FZ-0.04,1.7),(2.2,0.06,2.6),glass()); box((7,FZ-0.08,3.1),(2.4,0.12,0.1),frame())
    box((0,FZ-0.5,H-0.3),(W+0.6,1.0,0.9),RED,bev=0.04); box((0,FZ-1.02,H-0.55),(W+0.6,0.04,0.25),GRN); box((0,FZ-1.04,H-0.72),(W+0.6,0.03,0.06),C("NeonRed","ff2d3c",0.3,emit=5.0))
    for x in (-6,0,6): box((x,FZ-0.5,H-0.78),(1.6,0.8,0.04),led())
    box((0,FZ-0.3,H+0.9),(8,0.4,1.4),RED,bev=0.04); box((0,FZ-0.52,H+0.9),(7.4,0.04,0.9),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    box((0,0,H+0.15),(W+0.3,D+0.3,0.3),C("SteelGrey","9aa0a6",0.35,0.85))
    box((-9,FZ-0.7,0.9),(1.6,0.8,1.6),C("IceBox","f0f0ee",0.4),bev=0.05); box((-9,FZ-1.11,1.2),(1.3,0.02,0.5),C("GlowBlue","2f8cff",0.3,emit=4.0))
    box((9.2,FZ-0.7,0.95),(1.4,0.8,1.7),C("Cage","8a8f96",0.5,0.7),bev=0.03)
    box((4.6,FZ-0.5,1.0),(0.8,0.6,1.8),C("ATM","3a3d42",0.4,0.5),bev=0.04); box((4.6,FZ-0.81,1.3),(0.5,0.02,0.35),C("Screen","35c8ff",0.2,emit=2.5))
    for k,x in enumerate((-6.8,-6.0)): box((x,FZ-0.6,0.6),(0.6,0.5,1.0),[C("NewsBlue","2a4f9e",0.5),C("NewsRed","b8322a",0.5)][k],bev=0.04)
    for x in (-4.4,1.8): cyl((x,FZ-0.6,0.5),0.3,0.9,C("Trash","2a2c30",0.5),12)
    roofunits([(-5,2,2,1.6,1.0),(4,2,1.6,1.4,0.8)],H+0.3)
    for x in (-8,-3,2,7): bollard(x,FZ-1.4)
    lot(0,FZ-7,W+10,12,7,-9,FZ-9)
    lightpole(-13,FZ-12,8,1.6,1); cyl((11,FZ-10,4),0.18,8,C("PoleDark","2a2c30",0.45,0.6),10); box((11,FZ-10,8.2),(2.8,0.5,1.8),RED,bev=0.05); box((11,FZ-10.27,8.2),(2.4,0.04,1.3),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
@reg("OT_Hotel_A",(-36,-46,8),(0,-4,17),24,(900,1100))
def hotel():
    LS=T_("Limestone","plaster",(1.0,0.95,0.86)); GR=T_("Granite","granite",(0.8,0.8,0.8)); NAVY=C("HotelNavy","1b2440",0.4); GOLDC=GOLD()
    W,D=26,18; podH=7; FZ=-D/2; floors=10; fh=3.3; top=podH+floors*fh
    box((0,0,podH/2),(W+6,D+4,podH),GR,uv=2.0)
    storefront(0,FZ-2,20,4.6,0.4,10,True)
    box((0,FZ-6.5,podH-1.6),(14,8,0.5),NAVY,bev=0.06); box((0,FZ-10.52,podH-1.6),(14,0.06,0.3),GOLDC)   # porte cochere
    for x in (-6,-2,2,6):
        for y in (FZ-5,FZ-8): box((x,y,podH-1.62),(1.6,1.2,0.04),led())
    for x in (-6.6,6.6): box((x,FZ-10,(podH-1.8)/2),(0.6,0.6,podH-1.8),GR)
    cyl((0,FZ-2.3,1.6),1.3,3.2,glass(),20); cyl((0,FZ-2.3,3.3),1.4,0.2,C("Brass","c9a44e",0.3,0.95),20)   # revolving door
    box((0,0,podH+floors*fh/2),(W,D,floors*fh),LS,uv=2.5)
    window_grid(-W/2+1,W/2-1,FZ,podH+0.3,top-0.3,8,floors,0.4,NAVY,LS)
    for side in (-1,1):
        xp=side*W/2; ny=6; wy=(D-2)/ny
        for r in range(floors):
            for c in range(ny):
                cy=-D/2+1+wy*(c+0.5); cz=podH+0.3+(r+0.5)*(floors*fh-0.6)/floors
                box((xp+side*0.02,cy,cz),(0.04,wy*0.72,fh*0.62),warm() if random.random()<0.35 else glass())
        for c in range(ny+1): box((xp+side*0.06,-D/2+1+wy*c,podH+floors*fh/2),(0.1,0.12,floors*fh-0.6),NAVY)
        for r in range(floors+1): box((xp+side*0.06,0,podH+0.3+r*(floors*fh-0.6)/floors),(0.1,D-2,0.12),NAVY)
    for f in range(1,floors,2):                                   # balconies
        for x in (-8.4,-2.8,2.8,8.4): box((x,FZ-0.6,podH+f*fh+0.1),(2.6,1.2,0.12),LS); box((x,FZ-1.2,podH+f*fh+0.6),(2.6,0.05,1.0),glass())
    box((0,0,top+0.4),(W+0.6,D+0.6,0.8),NAVY,bev=0.05); box((0,FZ-0.32,top+0.4),(W+0.6,0.04,0.2),GOLDC)
    box((0,0,top+2.2),(14,10,2.8),NAVY,bev=0.05); box((0,FZ+3.98,top+2.2),(13,0.04,1.6),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    box((W/2+0.4,FZ+1,podH+12),(0.6,2.4,16),NAVY,bev=0.04); box((W/2+0.72,FZ+1,podH+12),(0.04,1.8,15),GOLDC)   # vertical sign
    for i,x in enumerate((-12,-10.6,-9.2)): cyl((x,FZ-11,6),0.08,12,C("SteelGrey","9aa0a6",0.35,0.85),10); box((x+0.9,FZ-11,11.2),(1.8,0.05,1.1),[C("FlagRed","b8322a",0.7),C("FlagWhite","eeeeea",0.7),C("FlagBlue","24407a",0.7)][i])
    for x in (-15,15): tree(x,FZ-6,1.0); planter(x,FZ-6,2.6,2.6,GR,0)
    lot(0,FZ-12,W+16,10)
@reg("OT_Aquarium_A",(-44,-56,12),(0,-6,6),26,(1150,780))
def aquarium():
    CO=T_("Concrete","conc",(0.95,0.95,0.95)); WHT=C("PaintWhite","f0f0ee",0.5); TEAL=C("NeonTeal","2fe0d8",0.3,emit=5.0); BLUE=C("WaterGlow","1f8fff",0.2,emit=2.2)
    AG=C("AquaGlass","2e7fa8",0.05,0.2); PV=T_("Pavement","walk",(0.9,0.9,0.88))
    box((0,4,4),(40,20,8),CO,uv=2.5)
    for i in range(12):                                   # wave roof
        x=-19+i*3.45; z=8.4+math.sin(i*0.6)*1.6
        box((x,4,z),(3.5,21,0.35),WHT,rot=(0,math.radians(math.cos(i*0.6)*18),0))
    bpy.ops.mesh.primitive_uv_sphere_add(radius=11,location=(-6,-6,0),segments=32,ring_count=16); o=bpy.context.object; o.scale=(1,1,0.9); o.data.materials.append(AG); uvbox(o,2.0)  # glass dome
    for k in range(8):
        a=math.radians(k*22.5); bpy.ops.mesh.primitive_torus_add(major_radius=11.02,minor_radius=0.12,location=(-6,-6,0),rotation=(math.radians(90),0,a)); o=bpy.context.object; o.scale=(1,1,0.9); o.data.materials.append(WHT)
    box((-6,-6,4),(9,0.2,8),BLUE)
    box((10,-6.05,3.2),(14,0.06,4.4),glass()); box((10,-6.0,3.2),(14,0.04,4.4),BLUE)
    box((10,-6.2,6.8),(15,0.4,1.4),C("AquaNavy","123a5a",0.4)); box((10,-6.42,6.8),(14,0.04,0.9),TEAL)
    box((0,-20,0.08),(56,26,0.16),PV,uv=3.0)
    cyl((14,-16,0.5),4,1.0,CO,32); cyl((14,-16,0.95),3.6,0.1,BLUE,32); cyl((14,-16,1.8),0.6,1.8,CO,16); sphere((14,-16,3.0),0.7,BLUE,2)  # fountain
    for s,(dx,dz,r) in enumerate(((0,0,1.6),(1.8,0.3,1.2),(3.2,0.5,0.8),(-1.6,0.1,1.0))): sphere((-18+dx,-17,4+dz),r,C("WhaleBlue","2d5f8a",0.4),2)   # whale sculpture
    cyl((-18,-17,1.5),0.25,3,CO,10); prism((-14.4,-17,4.2),1.2,1.4,0.3,C("WhaleBlue","2d5f8a",0.4))
    for x in (0,4): box((x,-12,1.4),(2.4,2.0,2.8),WHT,bev=0.05); box((x,-13.02,1.7),(1.8,0.04,1.0),glass())
    for k in range(6): cyl((-4+k*4,-26,3),0.08,6,C("SteelGrey","9aa0a6",0.35,0.85),8); box((-4+k*4+0.5,-26,4.6),(0.9,0.04,2.4),[TEAL,C("BannerOrange","f26b1d",0.5)][k%2])
    for x in (-24,24): tree(x,-24,1.1)
    for x in (-10,22): bench(x,-24)
    for x in (-26,26): lightpole(x,-30,8,1.6,1)
@reg("OT_GunStore_A",(-22,-28,5),(0,-4,3),26)
def gunstore():
    BR=T_("Brick","brick2",(0.9,0.84,0.8)); CR=T_("Corrugated","corr",(0.45,0.5,0.42),0.6,True); OL=C("Olive","4a5236",0.5); BLK=C("Black","121212",0.5)
    RED=C("TargetRed","c4261d",0.45); WHT=C("PaintWhite","f0f0ee",0.5)
    W,D,H=22,14,6; FZ=-D/2
    box((-3,0,H/2),(16,D,H),BR,uv=1.6); box((9,2,H/2+0.5),(8,D+4,H+1),CR,uv=2.5)       # shop + range annex
    box((-3,FZ-0.06,H-0.5),(16.1,0.15,1.0),OL)
    for x in (-8,2):
        box((x,FZ-0.02,2.3),(3.2,0.06,2.4),warm()); box((x,FZ-0.05,2.3),(3.2,0.04,2.4),glass())
        for k in range(8): cyl((x-1.4+k*0.4,FZ-0.15,2.3),0.03,2.6,BLK,6)
        for z in (1.2,3.4): box((x,FZ-0.15,z),(3.3,0.05,0.06),BLK)
    box((-3,FZ-0.05,1.6),(1.8,0.12,3.2),C("SteelDoor","3a3d42",0.4,0.7)); box((-3,FZ-0.12,3.4),(2.2,0.14,0.2),BLK)
    box((-3,FZ-0.9,3.9),(3,1.8,0.12),OL,rot=(math.radians(-10),0,0))
    for r,c in ((1.6,RED),(1.15,WHT),(0.7,RED),(0.3,WHT)): cyl((-3,FZ-0.2-(1.6-r)*0.02,H+1.6),r,0.08,c,32,rot=(math.radians(90),0,0))   # target logo
    box((-3,FZ+0.2,H+0.6),(0.3,0.3,1.2),BLK)
    signband(-3,FZ,12,H-0.5,OL,C("NeonRed","ff3b2a",0.3,emit=5.0),0.9,"e8e2d0")
    for x in (-10.6,4.6): box((x,FZ-0.3,H-1.2),(0.3,0.6,0.25),WHT)
    box((-3,0,H+0.15),(16.3,D+0.3,0.3),C("SteelGrey","9aa0a6",0.35,0.85))
    box((9,FZ-2.06,3),(4,0.08,3.6),C("RangeDoor","2c3138",0.4,0.5)); box((9,FZ-2.1,5.2),(5,0.1,0.3),RED)
    for x in (-9,-6,0,3,6): bollard(x,FZ-1.2,C("Yellow","e8b81e",0.5))
    lot(0,FZ-6,W+12,11,8,-10,FZ-8); lightpole(-14,FZ-10,8,1.6,1)
@reg("OT_Barber_A",(-13,-18,3),(0,-3,3),28,(1000,800))
def barber():
    BR=T_("Brick","brick",(0.95,0.78,0.68)); RED=C("BarberRed","c4261d",0.4); WHT=C("PaintWhite","f0f0ee",0.4); BLU=C("BarberBlue","1f4e8c",0.4)
    W,D,H=9,10,7; FZ=-D/2
    box((0,0,H/2),(W,D,H),BR,uv=1.4)
    storefront(-0.8,FZ,6,2.8,0.6,3,True,T_("Stone","trim",(0.9,0.86,0.8)))
    for k in range(3): box((-2.8+k*2,FZ+0.6,1.2),(0.8,0.8,1.2),C("BarberChair","8f1818",0.4)); box((-2.8+k*2,FZ+1.2,2.6),(0.9,0.05,1.2),C("Mirror","c8d4dc",0.1,0.9))
    box((3.2,FZ-0.04,1.7),(1.4,0.06,2.6),glass())
    awning_striped(0,FZ,W-0.4,3.7,RED,WHT,1.4)
    signband(0,FZ,W-0.6,4.6,C("SignNavy","1b2440",0.4),C("NeonTeal","2fe0d8",0.3,emit=5.0),0.8,"f2efe6")
    for z in range(10): cyl((4.15,FZ-0.35,1.6+z*0.18),0.14,0.18,[RED,WHT,BLU][z%3],12)   # barber pole
    sphere((4.15,FZ-0.35,3.5),0.18,WHT,1); sphere((4.15,FZ-0.35,1.45),0.16,C("Chrome","e6e9ee",0.15,1.0),1); box((4.15,FZ-0.1,2.5),(0.08,0.4,0.1),C("Chrome","e6e9ee",0.15,1.0))
    window_grid(-3.5,3.5,FZ,5.2,6.6,3,1,0.4,frame(),T_("Stone","trim",(0.9,0.86,0.8)))
    box((0,0,H+0.15),(W+0.3,D+0.3,0.3),T_("Stone","trim",(0.9,0.86,0.8)))
    box((1.6,FZ-0.3,3.2),(1.0,0.04,0.35),C("NeonRed","ff3b2a",0.3,emit=5.0))
    bench(-1.5,FZ-1.4); planter(-3.9,FZ-1.2,0.9,0.9,None,1)
    lot(0,FZ-4,W+8,8)
@reg("OT_Prison_A",(-62,-72,22),(0,-4,4),26,(1200,800))
def prison():
    CO=T_("Concrete","conc",(0.85,0.85,0.83)); CB=T_("Block","conc",(0.75,0.75,0.72)); FENCE=C("Fence","8a8f96",0.5,0.7); WIRE=C("Razor","b9bec4",0.3,0.9)
    FL=C("Floodlight","fffaf0",0.3,emit=7.0); ORG=C("Orange","e46a1e",0.5); PV=T_("Pavement","walk",(0.8,0.8,0.78)); YARD=C("YardDirt","8a7a5e",0.9)
    box((0,0,0.06),(84,64,0.12),PV,uv=4.0)
    for (x,y,w,d,h) in ((-18,8,28,12,10),(18,8,28,12,10),(0,22,40,10,8)):
        box((x,y,h/2),(w,d,h),CB,uv=2.5)
        for k in range(int(w/1.6)):
            for f in range(int(h/3)): box((x-w/2+0.8+k*1.6,y-d/2-0.03,1.6+f*3),(0.25,0.06,1.4),C("Slit","1a1c20",0.6))
        box((x,y,h+0.2),(w+0.4,d+0.4,0.4),CO)
        box((x,y-d/2-0.06,h-0.6),(w,0.1,0.3),ORG)
    box((0,-14,4),(24,10,8),CO,uv=2.0); window_grid(-11,11,-19,1.5,7.2,8,2,0.3)   # admin building
    box((0,-19.4,6.6),(12,0.3,1.2),C("SignNavy","1b2440",0.4)); box((0,-19.6,6.6),(11.4,0.04,0.8),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    box((0,-4,0.13),(30,8,0.04),YARD)                                           # yard + court
    box((14,-4,0.15),(10,7,0.04),C("Court","3f6e8c",0.6)); box((14,-4,0.17),(0.1,7,0.02),C("PaintWhite","f0f0ee",0.6))
    for ring,(hw,hd) in enumerate(((40,30),(38,28))):                           # double fence + razor wire
        for side in (-1,1):
            for i in range(int(hw*2/3)+1):
                cyl((-hw+i*3,side*hd,2.5),0.08,5,FENCE,6)
            box((0,side*hd,2.5),(hw*2,0.03,4.8),C("ChainLink","9aa0a6",0.5,0.6)); box((0,side*hd,5),(hw*2,0.06,0.06),FENCE)
            bpy.ops.mesh.primitive_torus_add(major_radius=0.45,minor_radius=0.04,location=(0,side*hd,5.5),rotation=(0,math.radians(90),0)); o=bpy.context.object; o.scale=(1,1,hw*2/0.9*0.02); o.data.materials.append(WIRE)
            for i in range(int(hd*2/3)+1): cyl((side*hw,-hd+i*3,2.5),0.08,5,FENCE,6)
            box((side*hw,0,2.5),(0.03,hd*2,4.8),C("ChainLink","9aa0a6",0.5,0.6)); box((side*hw,0,5),(0.06,hd*2,0.06),FENCE)
    for (x,y) in ((-40,-30),(40,-30),(-40,30),(40,30)):                         # guard towers
        for dx in (-1,1):
            for dy in (-1,1): cyl((x+dx*1.4,y+dy*1.4,6),0.25,12,CO,8)
        box((x,y,12.5),(4.4,4.4,2.6),CO,bev=0.05); box((x,y,12.6),(4.5,4.5,1.2),glass()); prism((x,y,13.8),5.0,1.4,5.0,C("TowerRoof","3a3d42",0.5,0.4))
        box((x+(2.4 if x>0 else -2.4)*0,y-2.3 if y<0 else y+2.3,13.4),(1.0,0.4,0.6),FL)
    box((0,-30,3.4),(10,1.2,6.8),CO); box((0,-30.62,2.6),(6,0.06,5.2),C("GateSteel","4a4e54",0.4,0.8)); box((0,-30.7,6.0),(10,0.1,0.4),ORG)
    for (x,y) in ((-30,-20),(30,-20),(-30,20),(30,20),(0,0)): cyl((x,y,7),0.2,14,C("PoleDark","2a2c30",0.45,0.6),10); box((x,y,14.2),(2.6,0.8,0.6),FL)
    lot(0,-42,60,16,14,-21,-44)
@reg("OT_Bar_A",(-18,-24,4),(0,-3,3),26)
def bar():
    BR=T_("Brick","brick2",(0.8,0.7,0.65)); WD=T_("Wood","wood",(0.55,0.36,0.24)); BLK=C("BarBlack","141416",0.5); AMB=C("NeonAmber","ffb02a",0.3,emit=5.5)
    W,D,H=16,12,6; FZ=-D/2
    box((0,0,H/2),(W,D,H),BR,uv=1.5)
    box((0,FZ-0.12,1.8),(W,0.25,3.6),WD,uv=1.0)                                  # wood front
    for x in (-5,3.5):
        box((x,FZ-0.28,2.0),(3.0,0.06,1.6),warm()); box((x,FZ-0.31,2.0),(3.0,0.04,1.6),glass())
        for k in range(4): box((x-1.5+k*1.0,FZ-0.34,2.0),(0.08,0.06,1.7),BLK)
    box((-0.8,FZ-0.27,1.6),(1.6,0.06,3.0),C("BarDoor","3a2416",0.5)); box((-0.8,FZ-0.5,3.6),(0.6,0.5,0.5),C("WallLamp","fff0cc",0.3,emit=4.0))
    box((0,FZ-0.35,4.4),(W,0.4,1.2),BLK,bev=0.03); box((0,FZ-0.56,4.4),(9,0.04,0.7),AMB)
    for (x,z,c) in ((-5,2.9,C("NeonBlue","3aa0ff",0.3,emit=5.0)),(3.5,2.9,C("NeonRed","ff2d3c",0.3,emit=5.0))): box((x,FZ-0.36,z),(1.4,0.04,0.35),c)
    for x in (-6,6): box((x,FZ-0.5,3.8),(0.8,0.6,0.15),BLK); 
    box((0,0,H+0.15),(W+0.3,D+0.3,0.3),BLK)
    box((W/2+4,-1,0.15),(8,10,0.3),WD,uv=1.0)                                    # patio + string lights
    for (x,y) in ((W/2+1,FZ+0.5),(W/2+7,FZ+0.5),(W/2+1,4),(W/2+7,4)): cyl((x,y,1.6),0.08,3.2,BLK,8)
    for i in range(14): sphere((W/2+1+i*6/13,FZ+0.5,3.1-math.sin(i/13*math.pi)*0.4),0.08,AMB,1); sphere((W/2+1+i*6/13,4,3.1-math.sin(i/13*math.pi)*0.4),0.08,AMB,1)
    for (x,y) in ((W/2+2.5,FZ+2.5),(W/2+5.5,FZ+2.5),(W/2+4,2)): cyl((x,y,0.75),0.5,0.06,WD,16); cyl((x,y,0.45),0.06,0.6,BLK,8)
    for x in (-7,7.4): cyl((x,FZ-0.9,0.45),0.4,0.9,WD,14); sphere((x,FZ-0.9,1.0),0.35,C("Shrub","3e6b2f",0.9),2)
    lot(0,FZ-5,W+14,9,6,-6,FZ-6,2.0)
@reg("OT_TechStore_A",(-26,-30,4),(0,-4,4),26)
def techstore():
    WHT=C("WhitePanel","eef0f2",0.25,0.1); ST=T_("Granite","granite",(0.95,0.95,0.95)); TB=C("TableGlow","e8f2ff",0.3,emit=2.2); SKY=C("ScreenGlow","8fd0ff",0.2,emit=3.5)
    W,D,H=24,16,9; FZ=-D/2
    box((0,0,H/2),(W,D,H),WHT,uv=2.0)
    box((0,FZ-0.03,H/2-0.2),(W-2,0.05,H-1.2),glass())
    for k in range(7): box((-W/2+1+k*(W-2)/6,FZ-0.07,H/2-0.2),(0.08,0.08,H-1.2),C("Chrome","e6e9ee",0.15,1.0))
    box((0,FZ+1.5,H-1.0),(W-3,0.1,0.2),led())
    for k in range(4):
        for r in range(2): box((-7.5+k*5,FZ+2.5+r*4,1.0),(3.2,1.4,0.12),TB); box((-7.5+k*5,FZ+2.5+r*4,0.5),(3.0,1.2,0.9),WHT)
        for j in range(3): box((-8.5+k*5+j*1.0,FZ+2.5,1.12),(0.5,0.35,0.04),SKY)
    box((0,FZ+7.8,4),(18,0.1,3.4),SKY)                                                  # video wall
    box((0,FZ-0.05,H-0.4),(3.0,0.04,1.2),C("LogoGlow","ffffff",0.2,emit=4.0))
    box((0,0,H+0.1),(W+0.2,D+0.2,0.2),WHT)
    box((0,FZ-7,0.1),(W+16,14,0.2),ST,uv=1.5)
    for x in (-14,-7,7,14): planter(x,FZ-4,2.2,2.2,ST,0); tree(x,FZ-4,0.9)
    for x in (-3.5,3.5): bench(x,FZ-6)
    for x in (-18,18): lightpole(x,FZ-12,8,1.6,1)
@reg("OT_CardShop_A",(-14,-19,3),(0,-3,3),28,(1000,800))
def cardshop():
    BR=T_("Brick","brick",(0.85,0.72,0.66)); PUR=C("ShopPurple","5b2a8a",0.4); YEL=C("ShopYellow","f2c230",0.45); NEON=C("NeonPink","ff3fb4",0.3,emit=5.5)
    W,D,H=11,11,7; FZ=-D/2
    box((0,0,H/2),(W,D,H),BR,uv=1.4); box((0,FZ-0.06,1.8),(W,0.15,3.6),PUR)
    storefront(-1,FZ-0.1,7,2.6,0.7,3,True,YEL)
    cols=[C("CardA","e2483a",0.4),C("CardB","2f8cff",0.4),C("CardC","2fa45a",0.4),C("CardD","f2c230",0.4),C("CardE","ffffff",0.4)]
    for k in range(18): box((-4.2+(k%6)*1.25,FZ-0.12,1.3+(k//6)*0.7),(0.45,0.03,0.62),cols[k%5])        # card displays
    box((-1,FZ+1.6,1.0),(3,1.6,0.9),C("GameTable","2f6b45",0.6)); 
    box((3.8,FZ-0.14,1.6),(1.4,0.06,2.6),glass())
    awning_striped(0,FZ-0.1,W-0.4,3.75,PUR,YEL,1.3)
    signband(0,FZ-0.1,W-0.6,4.7,YEL,NEON,1.1,"5b2a8a")
    for i,(dx,c) in enumerate(((-3.4,cols[0]),(3.4,cols[1]))): box((dx,FZ-0.45,4.7),(0.9,0.06,1.2),c,rot=(0,math.radians(10*(1 if i else -1)),0))
    box((2.5,FZ-0.32,3.2),(1.2,0.04,0.35),C("NeonBlue","3aa0ff",0.3,emit=5.0))
    window_grid(-4,4,FZ,5.3,6.6,3,1,0.5,frame())
    box((0,0,H+0.15),(W+0.3,D+0.3,0.3),YEL)
    box((-4.6,FZ-1.2,1.0),(0.9,0.06,1.6),C("Aboard","1a1a1a",0.6),rot=(math.radians(12),0,0))
    planter(4.6,FZ-1.2,0.9,0.9,None,1); lot(0,FZ-4,W+8,8)
@reg("OT_HardwareStore_A",(-70,-80,18),(0,-12,6),24,(1200,780))
def hardware():
    CB=T_("Block","conc",(0.9,0.88,0.84)); CR=T_("Corrugated","corr",(0.6,0.62,0.66),0.6,True); ORG=C("HWOrange","f26b1d",0.45); FENCE=C("Fence","8a8f96",0.5,0.7)
    W,D,H=80,50,12; FZ=-D/2
    box((0,0,H/2),(W,D,H),CB,uv=3.0); box((0,FZ-0.1,H-1.4),(W+0.2,0.3,2.8),ORG)
    box((0,0,H+0.2),(W+0.4,D+0.4,0.4),C("SteelGrey","9aa0a6",0.35,0.85))
    for x in (-18,14):                                                                   # entrances
        box((x,FZ-3,5.5),(12,6,0.5),ORG,bev=0.05); box((x,FZ-6.02,5.5),(12,0.06,0.3),C("GlowOrange","ff7a1a",0.3,emit=5.0))
        for y in (FZ-2,FZ-5): 
            for dx in (-4,0,4): box((x+dx,y,5.23),(1.6,1.0,0.04),led())
        storefront(x,FZ,10,4.2,0.2,5,True)
        for s in (-1,1): box((x+s*5.8,FZ-5.6,2.75),(0.5,0.5,5.5),C("SteelGrey","9aa0a6",0.35,0.85))
    box((-2,FZ-0.3,H+2.6),(28,0.6,5.2),ORG,bev=0.08); box((-2,FZ-0.62,H+2.6),(26,0.04,3.8),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    gx=-W/2-12                                                                            # garden center
    box((gx,FZ+14,0.08),(24,28,0.16),T_("Pavement","walk",(0.86,0.86,0.84)),uv=3.0)
    for side in (-1,1):
        for i in range(10): cyl((gx-12+i*2.6,FZ+14+side*14,2),0.06,4,FENCE,6)
        box((gx,FZ+14+side*14,2),(24,0.03,3.8),C("ChainLink","9aa0a6",0.5,0.6))
    for i in range(10): cyl((gx-12,FZ+i*2.8,2),0.06,4,FENCE,6)
    box((gx-12,FZ+14,2),(0.03,28,3.8),C("ChainLink","9aa0a6",0.5,0.6))
    box((gx+3,FZ+20,3),(14,12,0.1),C("GreenhouseGlass","cfe6e0",0.1,0.0)); 
    for i in range(6): box((gx-4+i*2.8,FZ+20,1.5),(0.1,12,3),FENCE)
    for i in range(14):                                                                   # plant tables
        box((gx-8+(i%7)*2.6,FZ+4+(i//7)*4,0.8),(2.0,1.2,0.1),T_("Wood","wood",(0.8,0.6,0.42)))
        for j in range(3): sphere((gx-8.6+(i%7)*2.6+j*0.6,FZ+4+(i//7)*4,1.1),0.25,[C("Shrub","3e6b2f",0.9),C("FlowerRed","d23a4a",0.8),C("FlowerYel","f2c230",0.8)][j],1)
    lx=W/2+10                                                                             # lumber yard canopy
    box((lx,0,6.5),(18,36,0.4),CR,bev=0.04)
    for y in range(-16,17,8):
        for x in (lx-8.5,lx+8.5): box((x,y,3.2),(0.4,0.4,6.4),C("SteelGrey","9aa0a6",0.35,0.85))
    for i in range(6): box((lx-5+(i%3)*5,-12+(i//3)*12,0.8),(3.6,7,1.4),T_("Wood","wood",(1.0,0.82,0.6)))
    lot(0,FZ-22,W+40,40,24,-36,FZ-16); stripes(-36,FZ-30,24,3.0,5.0)
    for x in (-30,-10,10,30):
        lightpole(x,FZ-23,10,2.0,1); lightpole(x+1,FZ-23,10,2.0,-1)
        box((x+5,FZ-23,0.6),(4,1.4,1.2),C("CartCorral","9aa0a6",0.4,0.8))
@reg("OT_Trailer_A",(-14,-17,4),(0,-1,1.5),26,(1000,700))
def trailer():
    SID=T_("Siding","plaster",(0.98,0.95,0.86)); SK=T_("Corrugated","corr",(0.75,0.75,0.72),0.5,True); WHT=C("TrimWhite","ecebe6",0.5); BRN=C("Awning","8a6a3a",0.6)
    L,D,H=18,4.6,3.0
    box((0,0,0.45),(L,D,0.9),SK,uv=1.0); box((0,0,0.9+H/2),(L,D,H),SID,uv=1.5)
    laps(-L/2,L/2,-D/2,1.1,0.9+H,C('LapShadowT','c8c2b0',0.6),0.25)
    box((0,0,0.9+H+0.2),(L+0.3,D+0.4,0.3),C("RoofMetal","b9bec4",0.4,0.8))
    for x in (-6,-2,4.5,7.5): box((x,-D/2-0.02,2.6),(1.3,0.06,1.1),glass()); box((x,-D/2-0.06,2.6),(1.5,0.06,1.3),WHT)
    box((1.2,-D/2-0.03,1.9),(1.0,0.06,2.0),C("TrailerDoor","f0eee6",0.5))
    for i in range(4): box((1.2,-D/2-0.6-i*0.3,0.15+i*0.22),(1.6,0.3,0.15),T_("Wood","wood",(0.8,0.62,0.45)))
    box((1.2,-D/2-1.6,1.0),(2.4,1.6,0.12),T_("Wood","wood",(0.8,0.62,0.45)))
    box((1.2,-D/2-1.3,3.9),(4,2.2,0.08),BRN,rot=(math.radians(-6),0,0))
    for x in (-0.6,3.0): cyl((x,-D/2-2.3,2.2),0.05,3.4,WHT,8)
    box((-8,-D/2-0.5,1.3),(0.9,0.7,0.7),C("SteelGrey","9aa0a6",0.35,0.85),bev=0.04)
    cyl((L/2+1,0,0.9),0.4,1.4,C("Propane","f0f0ee",0.4),16,rot=(math.radians(90),0,0))
    box((5,-D/2-2.4,0.9),(0.6,0.6,0.9),C("Grill","1a1a1a",0.5,0.6)); cyl((-4,-D/2-2.6,0.5),0.5,0.06,C("PatioTable","eeeeea",0.5),12)
    for i in range(12): box((-9+i*1.6,-D/2-4.0,0.6),(0.08,0.08,1.2),WHT)
    box((0,-D/2-4.0,1.0),(19,0.06,0.08),WHT); box((0,-D/2-4.0,0.4),(19,0.06,0.08),WHT)
    box((0,-2.5,0.03),(24,12,0.06),C("Lawn","567d3a",0.9)); box((-3,-5,0.05),(3,6,0.06),C("Gravel","8f8a80",0.9))
@reg("OT_House_A",(-20,-24,6),(0,-1,4),26)
def house_a():   # two-story colonial with garage
    SID=T_("Siding","plaster",(0.97,0.97,1.0)); BR=T_("Brick","brick",(0.85,0.7,0.62)); SH=T_("Shingle","shingle",(0.8,0.8,0.8)); WHT=C("TrimWhite","f0efe9",0.5); SHT=C("Shutter","1f3a5c",0.5)
    W,D=13,9; H=6.4; FZ=-D/2
    box((0,0,0.3),(W+0.2,D+0.2,0.6),BR,bev=0.03); box((0,0,0.6+H/2),(W,D,H),SID,uv=1.5)
    LC=C('LapShadow','c9cbd0',0.6); laps(-W/2,W/2,FZ,0.8,0.6+H,LC); laps_side(-W/2,-D/2,D/2,0.8,0.6+H,LC,dirx=-1)
    for x in (-4.2,-1.4,1.4,4.2):
        for z in (2.2,5.2):
            if z<3 and abs(x)<2: continue
            box((x,FZ-0.03,z),(1.1,0.06,1.5),warm() if random.random()<0.3 else glass()); box((x,FZ-0.06,z),(1.3,0.06,1.7),WHT)
            for s in (-1,1): box((x+s*0.85,FZ-0.08,z),(0.4,0.06,1.6),SHT)
    box((0,FZ-0.05,1.8),(1.2,0.1,2.3),C("FrontDoor","7a1f1f",0.4)); box((0,FZ-1.0,3.2),(2.6,2.0,0.15),WHT)
    for x in (-1.1,1.1): cyl((x,FZ-1.9,1.9),0.12,2.6,WHT,10)
    prism((0,FZ-1.0,3.3),2.8,0.8,2.0,WHT)
    for i in range(3): box((0,FZ-0.5-i*0.35,0.45-i*0.15),(2.2,0.35,0.3),BR)
    gable(0,0,0.6+H,W,D,3.0,SH,"x",0.5)
    box((W/2+3.2,0.5,1.6),(6.4,8,3.2),SID,uv=1.5); box((W/2+3.2,FZ+0.48,1.4),(5.0,0.06,2.6),C("GarageDoor","f0efe9",0.5))
    for k in range(5): box((W/2+3.2,FZ+0.44,0.3+k*0.55),(5.0,0.04,0.04),C("GDLine","c9c8c2",0.5))
    gable(W/2+3.2,0.5,3.2,6.4,8,1.6,SH,"x",0.4)
    box((W/2+3.2,FZ-4,0.06),(5,7,0.1),T_("Concrete","walk",(0.9,0.9,0.88)),uv=2.0)            # driveway
    box((0,FZ-3.5,0.05),(1.2,5,0.08),T_("Concrete","walk",(0.9,0.9,0.88)))
    box((2,-2,0.02),(30,20,0.04),C("Lawn","567d3a",0.9))
    for x in (-5.5,-3.5,3.5,5.5): sphere((x,FZ-0.7,0.6),0.6,C("Shrub","3e6b2f",0.9),2)
    tree(-8,FZ-5,1.2); box((-1.6,FZ-6.6,0.7),(0.5,0.3,0.3),C("Mailbox","1a1a1a",0.5,0.4)); cyl((-1.6,FZ-6.6,0.4),0.04,0.8,C("Post","eeeeea",0.5),6)
    box((W/2-0.3,2,0.9),(0.9,0.7,0.8),C("SteelGrey","9aa0a6",0.35,0.85))
@reg("OT_House_B",(-18,-22,5),(0,-1,2.5),26)
def house_b():   # ranch with stone + hip-like roof
    ST=T_("Stone","granite",(0.85,0.8,0.74)); SID=T_("Siding","plaster",(0.95,0.86,0.68)); SH=T_("Shingle","shingle",(0.7,0.62,0.55)); WHT=C("TrimWhite","f0efe9",0.5)
    W,D,H=18,10,3.2; FZ=-D/2
    box((0,0,H/2+0.3),(W,D,H),SID,uv=1.5); box((-5,FZ-0.06,1.6),(8,0.15,2.6),ST,uv=1.2)
    LC=C('LapShadowB','bba98a',0.6); laps(-1,W/2,FZ,0.5,H+0.3,LC); laps_side(-W/2,-D/2,D/2,0.5,H+0.3,LC,dirx=-1)
    for x in (-6.5,-3.5,3,6):
        box((x,FZ-0.15 if x<0 else FZ-0.03,2.0),(1.8,0.06,1.4),warm() if x==3 else glass()); box((x,FZ-0.18 if x<0 else FZ-0.06,2.0),(2.0,0.06,1.6),WHT)
    box((0.2,FZ-0.05,1.5),(1.1,0.1,2.2),C("FrontDoor","2f5d3a",0.4))
    box((0.2,FZ-1.2,3.2),(5,2.4,0.15),SH); 
    for x in (-2,2.4): box((x,FZ-2.3,1.7),(0.25,0.25,2.8),WHT)
    gable(0,0,H+0.3,W,D,2.4,SH,"x",0.7)
    box((W/2-2,FZ-0.04,1.4),(4.4,0.06,2.4),C("GarageDoor","f0efe9",0.5))
    box((W/2-2,FZ-4,0.06),(4.6,7,0.1),T_("Concrete","walk",(0.9,0.9,0.88)),uv=2.0)
    box((0,-2,0.02),(32,22,0.04),C("Lawn","567d3a",0.9))
    for i in range(16): box((-15+i*2,FZ-7.5,0.5),(0.12,0.12,1.0),WHT)
    box((-1,FZ-7.5,0.85),(32,0.08,0.1),WHT); box((-1,FZ-7.5,0.5),(32,0.08,0.1),WHT)
    tree(-11,FZ-4,1.3); tree(9,4,1.1)
    for x in (-8,-6,-4,-2): sphere((x,FZ-0.8,0.5),0.5,C("Shrub","3e6b2f",0.9),2)
@reg("OT_House_C",(-16,-20,5),(0,-1,3.5),26)
def house_c():   # craftsman bungalow with big porch
    SID=T_("Siding","plaster",(0.62,0.78,0.74)); ST=T_("Stone","granite",(0.8,0.76,0.7)); SH=T_("Shingle","shingle",(0.55,0.5,0.48)); WHT=C("TrimCream","efe6cf",0.5)
    W,D,H=11,12,3.6; FZ=-D/2
    box((0,0,0.4),(W+0.2,D+0.2,0.8),ST,bev=0.03); box((0,0,0.8+H/2),(W,D,H),SID,uv=1.5)
    LC=C('LapShadowC','4f6a66',0.6); laps(-W/2,W/2,FZ,1.0,0.8+H,LC); laps_side(-W/2,-D/2,D/2,1.0,0.8+H,LC,dirx=-1)
    for x in (-3.2,3.2): box((x,FZ-0.03,2.6),(2.2,0.06,1.5),warm() if x>0 else glass()); box((x,FZ-0.06,2.6),(2.5,0.06,1.8),WHT)
    box((0,FZ-0.05,2.0),(1.1,0.1,2.3),C("FrontDoor","6a4424",0.4))
    box((0,FZ-1.6,0.8),(W,3.2,0.15),T_("Wood","wood",(0.75,0.58,0.42)))                # porch deck
    for x in (-4.8,-1.6,1.6,4.8): box((x,FZ-3.0,0.8+0.6),(0.7,0.7,1.2),ST); box((x,FZ-3.0,2.0+0.9),(0.4,0.4,1.8),WHT)
    for i in range(18): box((-4.6+i*0.55,FZ-3.05,1.2),(0.06,0.06,0.8),WHT) if abs(-4.6+i*0.55)>0.9 else None
    for i in range(3): box((0,FZ-3.4-i*0.3,0.6-i*0.2),(1.8,0.3,0.25),ST)
    gable(0,FZ-1.4,0.8+H,W+0.6,3.4,1.4,SH,"x",0.3)
    gable(0,0.8,0.8+H,W,D-1.6,3.2,SH,"y",0.5)
    box((0,FZ+0.8,0.8+H+1.2),(1.6,0.06,0.9),glass())
    cyl((-3,FZ-2.2,1.45),0.25,0.4,C("Planter","b85a3a",0.6),12); bench(2.6,FZ-1.2)
    box((0,-1,0.02),(26,22,0.04),C("Lawn","567d3a",0.9)); box((0,FZ-6,0.05),(1.2,5,0.08),T_("Concrete","walk",(0.9,0.9,0.88)))
    tree(-8,FZ-3,1.2); tree(8,3,1.0)
if __name__=="__main__" or True:
    name=sys.argv[-2]; mode=sys.argv[-1]
    f,cam,tgt,lens,res=BLD[name]; reset(); random.seed(hash(name)%1000); _cache.clear(); f()
    if mode=="render": world_and_render(f"/home/claude/blender/r_{name}.png",cam,tgt,lens,res,24)
    else: export(name,drop_y=-999)
