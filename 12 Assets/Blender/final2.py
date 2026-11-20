exec(open("/home/claude/blender/lib.py").read())
import sys
BLD={}
def reg(name,cam,tgt,lens=26,res=(1100,780)):
    def deco(f): BLD[name]=(f,cam,tgt,lens,res); return f
    return deco
def face_grid(face,W,D,z0,z1,cols,rows,frame_col,lit=0.35,inset=0.0):
    """windows on one face of a box centered at origin: face in 'front','back','left','right'"""
    span=W if face in("front","back") else D; w=(span-2*inset)/cols; h=(z1-z0)/rows
    for c in range(cols):
        for r in range(rows):
            u=-span/2+inset+w*(c+0.5); cz=z0+h*(r+0.5); m=warm() if random.random()<lit else glass()
            if face=="front": box((u,-D/2-0.02,cz),(w*0.74,0.04,h*0.68),m)
            elif face=="back": box((u,D/2+0.02,cz),(w*0.74,0.04,h*0.68),m)
            elif face=="left": box((-W/2-0.02,u,cz),(0.04,w*0.74,h*0.68),m)
            else: box((W/2+0.02,u,cz),(0.04,w*0.74,h*0.68),m)
    for c in range(cols+1):
        u=-span/2+inset+w*c
        p={"front":(u,-D/2-0.06),"back":(u,D/2+0.06),"left":(-W/2-0.06,u),"right":(W/2+0.06,u)}[face]
        sz=(0.12,0.1) if face in("front","back") else (0.1,0.12)
        box((p[0],p[1],(z0+z1)/2),(sz[0],sz[1],z1-z0),frame_col)
    for r in range(rows+1):
        z=z0+h*r; p={"front":(0,-D/2-0.06),"back":(0,D/2+0.06),"left":(-W/2-0.06,0),"right":(W/2+0.06,0)}[face]
        sz=(span-2*inset,0.1) if face in("front","back") else (0.1,span-2*inset)
        box((p[0],p[1],z),(sz[0],sz[1],0.12),frame_col)
def tower(W,D,z0,H,mat,cols,colsd,floors,frame_col,lit=0.35,faces=("front","left","right")):
    box((0,0,z0+H/2),(W,D,H),mat,uv=3.0)
    for f in faces: face_grid(f,W,D,z0+0.4,z0+H-0.4,cols if f in("front","back") else colsd,floors,frame_col,lit)
@reg("OT_Brownstone_A",(-18,-22,4),(0,-3,5),26)
def brownstone():
    BS=T_("Brownstone","plaster",(0.62,0.42,0.32)); ST=T_("Stone","trim",(0.8,0.7,0.6)); IRON=C("Iron","1c1c1c",0.5,0.6)
    for i in range(3):     # row of 3 attached brownstones
        x=-8+i*8; W,D,H=7.8,12,12; FZ=-D/2
        box((x,0,H/2),(W,D,H),BS,uv=1.6); box((x,FZ-0.05,0.9),(W,0.2,1.8),ST,bev=0.03)
        box((x-1.6,FZ-1.2,H/2+0.3),(3,2.4,H-2.2),BS,uv=1.6)                 # bay
        for f in range(3):
            z=2.6+f*3.2
            for dx in (-2.6,-1.6,-0.6): box((x+dx,FZ-2.42 if dx==-1.6 else FZ-1.5,z+0.9),(0.8,0.06,1.7),warm() if random.random()<0.35 else glass())
            box((x+2.2,FZ-0.03,z+0.9),(1.1,0.06,1.8),warm() if random.random()<0.3 else glass()); box((x+2.2,FZ-0.08,z+1.95),(1.5,0.2,0.3),ST)
        box((x+2.2,FZ-0.05,2.9),(1.2,0.1,2.4),C("Door","3a2416",0.4))
        for k in range(7): box((x+2.2,FZ-0.6-k*0.42,1.75-k*0.25),(1.8,0.42,0.25*(k+1)),ST)
        for s in (-1,1): box((x+2.2+s*1.0,FZ-2.0,1.4),(0.05,3.0,0.05),IRON,rot=(math.atan2(1.6,3.0),0,0))
        box((x,0,H+0.3),(W,D,0.6),ST); 
        for k in range(10): box((x-W/2+0.4+k*0.78,FZ-0.25,H-0.1),(0.2,0.4,0.4),ST)
    lot(0,-12,30,6)
@reg("OT_Office_A",(-34,-42,8),(0,-4,14),24,(900,1100))
def office():
    LS=T_("Limestone","plaster",(0.95,0.92,0.86)); GR=T_("Granite","granite",(0.7,0.7,0.72)); FR=C("Bronze","4a3a28",0.4,0.8)
    W,D=22,16
    box((0,0,2.5),(W+1,D+1,5),GR,uv=2.0); storefront(0,-D/2-0.5,16,3.6,0.4,8,True)
    tower(W,D,5,30,LS,10,7,9,FR,0.4)
    for x in range(-10,11,2): box((x,-D/2-0.3,20),(0.35,0.5,30),LS)
    box((0,0,35.4),(W+0.6,D+0.6,0.8),GR,bev=0.05); roofunits([(-4,2,4,3,2),(5,0,3,3,1.5)],35.8)
    box((0,-D/2-1.6,4.6),(8,3,0.3),FR); lot(0,-D/2-6,W+10,9); tree(-12,-D/2-4); tree(12,-D/2-4)
@reg("OT_Apartments_A",(-34,-40,6),(0,-4,10),24,(1100,850))
def apartments():
    PL=T_("Stucco","plaster",(0.95,0.93,0.9)); WD=T_("Wood","wood",(0.85,0.62,0.42)); GR=C("Railing","2a2c30",0.4,0.6)
    W,D,H=30,14,18; FZ=-D/2
    box((0,0,H/2),(W,D,H),PL,uv=2.0)
    for i in range(5):
        x=-12+i*6
        box((x,FZ-0.12,H/2),(2.2,0.25,H),WD,uv=1.0) if i%2==0 else None
        for f in range(5):
            z=1.6+f*3.4
            box((x+(1.4 if i%2==0 else 0),FZ-0.02,z+0.9),(2.4 if i%2 else 1.4,0.06,2.0),warm() if random.random()<0.35 else glass())
            if f>0: box((x,FZ-0.8,z-0.2),(3.6,1.6,0.15),PL); box((x,FZ-1.6,z+0.35),(3.6,0.04,0.9),glass()); box((x,FZ-1.6,z+0.8),(3.6,0.06,0.06),GR)
    storefront(-6,FZ,10,3,0.4,5,True); box((-6,FZ-1.2,3.7),(11,2.4,0.2),GR)
    box((0,0,H+0.2),(W+0.4,D+0.4,0.4),C("SteelGrey","9aa0a6",0.35,0.85)); roofunits([(-8,2,3,2,1.4),(6,2,3,2,1.4)],H+0.4)
    for x in (-13,13): tree(x,FZ-3)
    for x in (2,7,12): planter(x,FZ-1.5,3,1.2,None,3)
    lot(0,FZ-7,W+10,10,8,-10,FZ-9)
@reg("OT_Skyscraper_Glass",(-50,-60,10),(0,0,40),24,(800,1150))
def sky_glass():
    GL2=C("CurtainGlass","2b4d66",0.06,0.4); FR=C("Mullion","c9ccd1",0.25,0.9); GR=T_("Granite","granite",(0.6,0.6,0.62))
    W,D=24,24
    box((0,0,4),(W+4,D+4,8),GR,uv=2.0); storefront(0,-D/2-2,18,5,0.6,9,True)
    box((0,0,8+36),(W,D,72),GL2)
    for f in ("front","left","right"):
        span=W
        for c in range(13):
            u=-span/2+c*span/12
            p={"front":(u,-D/2-0.08),"left":(-W/2-0.08,u),"right":(W/2+0.08,u)}[f]; sz=(0.18,0.12) if f=="front" else (0.12,0.18)
            box((p[0],p[1],44),(sz[0],sz[1],72),FR)
        for r in range(0,73,4):
            p={"front":(0,-D/2-0.08),"left":(-W/2-0.08,0),"right":(W/2+0.08,0)}[f]; sz=(W,0.12) if f=="front" else (0.12,D)
            box((p[0],p[1],8+r),(sz[0],sz[1],0.25),FR)
    box((0,0,80+4),(18,18,8),GL2); box((0,0,88.5),(19,19,1),FR)
    cyl((0,0,96),0.4,14,FR,10); sphere((0,0,103),0.5,C("GlowRed","ff2a2a",0.3,emit=6.0),1)
    for z in (80.2,88): box((0,-9.1,z),(18,0.06,0.2),C("LEDStrip","e8f2ff",0.3,emit=5.0))
    lot(0,-D/2-8,40,10)
@reg("OT_Skyscraper_Deco",(-50,-60,10),(0,0,36),24,(800,1150))
def sky_deco():
    LS=T_("Limestone","plaster",(0.95,0.9,0.8)); FR=C("DecoBronze","5a4426",0.4,0.8); GOLD=C("GoldGlow","ffd27a",0.3,emit=3.5)
    box((0,0,4),(30,26,8),T_("Granite","granite",(0.55,0.5,0.48)),uv=2.0); storefront(0,-14,20,5,0.6,8,True)
    levels=[(28,24,8,30),(22,18,38,18),(16,13,56,12),(10,8,68,8)]
    for (w,d,z0,h) in levels:
        box((0,0,z0+h/2),(w,d,h),LS,uv=2.5)
        cols=int(w/2.2)
        for c in range(cols): 
            u=-w/2+(c+0.5)*w/cols
            box((u,-d/2-0.03,z0+h/2),(w/cols*0.5,0.06,h-1),warm() if random.random()<0.25 else glass())
            box((u+w/cols/2,-d/2-0.15,z0+h/2),(0.35,0.3,h),LS)
        for c in range(int(d/2.2)):
            v=-d/2+(c+0.5)*d/int(d/2.2)
            for s in (-1,1): box((s*(w/2+0.03),v,z0+h/2),(0.06,d/int(d/2.2)*0.5,h-1),warm() if random.random()<0.25 else glass())
        box((0,0,z0+h+0.2),(w+0.5,d+0.5,0.4),LS)
    prism((0,0,76),8,5,6,FR); cyl((0,0,85),0.3,8,FR,10)
    for z in (38.3,56.3,68.3): box((0,-levels[[38,56,68].index(z-0.3)+1][1]/2-0.2,z),(levels[[38,56,68].index(z-0.3)+1][0],0.05,0.15),GOLD)
    lot(0,-20,44,10)
@reg("OT_OfficeTower_B",(-46,-56,10),(0,0,30),24,(850,1150))
def office_tower_b():
    CO=T_("Concrete","conc",(0.9,0.9,0.9)); FR=C("DarkFrame","25282c",0.4,0.5)
    box((0,0,3),(26,22,6),CO,uv=2.0); storefront(0,-11,20,4.4,0.5,10,True)
    tower(22,18,6,54,CO,9,7,15,FR,0.35)
    for i in range(3): box((-11.2,-9.2,6+18*i+9),(0.6,0.6,18),CO)
    box((6,0,62),(10,18,4),CO); box((-5,0,61.2),(12,18,2.4),C("CurtainGlass","2b4d66",0.06,0.4))
    box((0,-9.1,60.2),(22,0.06,0.25),C("LEDStrip","e8f2ff",0.3,emit=5.0)); lot(0,-16,40,10)
@reg("OT_ParkingGarage_A",(-40,-46,10),(0,-2,6),24,(1150,780))
def garage():
    CO=T_("Concrete","conc",(0.88,0.88,0.86)); RED=C("Red","c4261d",0.45); YEL=C("Yellow","e8b81e",0.5)
    W,D=40,28; FZ=-D/2
    for lv in range(5):
        z=lv*3.2; box((0,0,z+0.15),(W,D,0.3),CO,uv=3.0)
        box((0,FZ+0.2,z+1.0),(W,0.4,1.0),CO); box((0,-FZ-0.2,z+1.0),(W,0.4,1.0),CO)
        for x in (-W/2+0.2,W/2-0.2): box((x,0,z+1.0),(0.4,D,1.0),CO)
        for i in range(12): box((-W/2+2+i*3.2,FZ+5,z+0.32),(0.12,5,0.02),C("PaintWhite","f0f0ee",0.6))
        for x in range(-18,19,6):
            for y in (FZ+0.6,-FZ-0.6,0): box((x,y,z+1.7),(0.6,0.6,3.2),CO)
        box((0,FZ+0.0,z+1.55),(W,0.06,0.08),YEL)
        for x in (-10,10): box((x,0,z+2.9),(1.2,0.6,0.08),led())
    box((W/2-4,FZ-0.5,9),(4,4,18),CO); box((W/2-4,FZ-2.52,9),(2,0.06,16),glass())     # stair tower
    box((W/2-4,FZ-2.6,16.5),(3.6,0.2,1.4),C("ParkBlue","1f4e8c",0.4)); box((W/2-4,FZ-2.72,16.5),(3,0.04,1),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    box((-12,FZ-1,1.2),(0.3,0.3,2.4),C("SteelGrey","9aa0a6",0.35,0.85)); box((-10,FZ-1,1.9),(4,0.15,0.15),RED)
    lot(0,FZ-6,W+10,10)
@reg("OT_Warehouse_A",(-44,-50,10),(0,-2,5),24,(1150,780))
def warehouse():
    CR=T_("Corrugated","corr",(0.7,0.72,0.76),0.6,True); CB=T_("Block","conc",(0.88,0.86,0.82)); BLU=C("WhBlue","1f4e8c",0.45); YEL=C("Yellow","e8b81e",0.5)
    W,D,H=50,30,11; FZ=-D/2
    box((0,0,1.5),(W,D,3),CB,uv=2.0); box((0,0,3+(H-3)/2),(W,D,H-3),CR,uv=3.0)
    gable(0,0,H,W,D,2.0,CR,"x",0.3)
    box((0,FZ-0.06,3.1),(W+0.1,0.15,0.3),BLU)
    for i in range(6):
        x=-20+i*7.5; box((x,FZ-0.02,2.2),(3.8,0.1,4.2),C("DockDoor","b8bcc2",0.5,0.4)); box((x,FZ-0.5,1.0),(4.2,1,0.2),C("Bumper","1a1a1a",0.7))
        box((x,FZ-0.25,4.6),(4.4,0.3,0.25),YEL); box((x,FZ-0.3,5.4),(0.6,0.4,0.3),C("WallLamp","fff0cc",0.3,emit=4.0))
    box((W/2-4,FZ-0.04,1.6),(1.2,0.08,2.4),C("Door","3a3d42",0.4,0.5)); box((-14,FZ-0.1,H-1.5),(16,0.2,2.0),BLU); box((-14,FZ-0.22,H-1.5),(15,0.04,1.4),C("SignWhiteGlow","f4f8ff",0.3,emit=2.5))
    for k in range(4): box((22,FZ-3-k*1.3,0.1+0.0),(1.2,1.0,0.12),T_("Wood","wood",(0.8,0.62,0.45)))
    box((-W/2-6,0,1.5),(4,12,3),C("Container","b8322a",0.5,0.4),bev=0.04); box((-W/2-6,0,4.5),(4,12,3),C("Container2","2a5fb0",0.5,0.4),bev=0.04)
    lot(0,FZ-10,W+16,18,10,-15,FZ-14)
    for x in (-20,0,20): lightpole(x,FZ-18,9,1.8,1)
@reg("OT_Townhouses_A",(-26,-30,5),(0,-2,4),24)
def townhouses():
    cols=[(0.92,0.86,0.76),(0.72,0.8,0.86),(0.86,0.74,0.7),(0.8,0.84,0.74)]; SH=T_("Shingle","shingle",(0.7,0.7,0.7)); WHT=C("TrimWhite","f0efe9",0.5)
    for i in range(4):
        x=-10.5+i*7; W,D,H=7,10,7; FZ=-D/2
        S=T_(f"Siding{i}","plaster",cols[i]); box((x,0,H/2),(W,D,H),S,uv=1.5)
        for z in (1.8,4.8):
            box((x-1.6,FZ-0.03,z),(1.4,0.06,1.6),warm() if random.random()<0.35 else glass()); box((x-1.6,FZ-0.06,z),(1.6,0.06,1.8),WHT)
        box((x+1.8,FZ-0.03,4.8),(1.2,0.06,1.6),glass()); box((x+1.8,FZ-0.05,1.2),(2.6,0.1,2.2),C("GarageDoor","f0efe9",0.5))
        box((x-1.6,FZ-0.05,1.2),(0.9,0.1,2.2),C(f"Door{i}",["7a1f1f","1f3a5c","2f5d3a","3a2416"][i],0.4))
        prism((x,0,H),W,2.4,D,SH,rot_z=0) if False else gable(x,0,H,W,D,2.2,SH,"y",0.2)
        box((x+1.8,FZ-3,0.06),(2.8,6,0.1),T_("Concrete","walk",(0.9,0.9,0.88)))
        sphere((x-2.8,FZ-0.7,0.5),0.5,C("Shrub","3e6b2f",0.9),2)
    box((0,-3,0.02),(34,16,0.04),C("Lawn","567d3a",0.9)); tree(-15,-8,1.0); tree(15,-8,1.0)
@reg("OT_StripMall_A",(-40,-46,8),(0,-6,3),24,(1150,760))
def stripmall():
    PL=T_("Stucco","plaster",(0.95,0.9,0.8)); BR=T_("Brick","brick",(0.85,0.7,0.62)); cols=["c4261d","1f4e8c","2fa45a","e8b81e","7a3a9e","f26b1d"]
    W,D,H=48,16,6; FZ=-D/2
    box((0,0,H/2),(W,D,H),PL,uv=2.0); box((0,FZ-2,H-0.3),(W,4,0.4),PL,bev=0.04)
    for i in range(6):
        x=-20+i*8; storefront(x,FZ,6.6,2.8,0.5,3,True,BR)
        signband(x,FZ-2,7,H+0.6,C(f"Sign{i}",cols[i],0.45),C("NeonW","fff4e0",0.3,emit=4.0),1.0,"f2efe6")
        box((x,FZ-2,H-0.52),(2,1.2,0.04),led())
    for x in range(-24,25,8): box((x,FZ-3.8,(H-0.5)/2),(0.5,0.5,H-0.5),BR)
    box((0,FZ+0.5,H+1.4),(14,0.4,2.8),PL); box((0,0,H+0.15),(W+0.3,D+0.3,0.3),C("SteelGrey","9aa0a6",0.35,0.85))
    lot(0,FZ-14,W+16,24,16,-22,FZ-12); stripes(-22,FZ-20,16,3.0,5.0)
    for x in (-20,0,20): lightpole(x,FZ-16,9,1.8,1); lightpole(x+0.3,FZ-16,9,1.8,-1)
    cyl((26,FZ-24,5),0.3,10,C("PoleDark","2a2c30",0.45,0.6),10)
    for k in range(4): box((26,FZ-24,7+k*1.1),(4,0.6,1.0),C(f"Sign{k}",cols[k],0.45),bev=0.04)
@reg("OT_Farm_A",(-40,-46,10),(0,0,4),24,(1150,780))
def farm():
    RED=T_("BarnRed","siding",(1.0,0.45,0.38),gray=True); SID=T_("Siding","plaster",(0.97,0.95,0.9)); SH=T_("Shingle","shingle",(0.6,0.6,0.6)); CR=T_("Corrugated","corr",(0.75,0.75,0.78),0.6,True)
    WHT=C("TrimWhite","f0efe9",0.5)
    box((-14,0,3),(12,9,6),SID,uv=1.5); gable(-14,0,6,12,9,3,SH,"x",0.5)                       # farmhouse
    for x in (-17,-11): box((x,-4.53,3),(1.2,0.06,1.6),glass()); box((x,-4.56,3),(1.4,0.06,1.8),WHT)
    box((-14,-5.5,2.4),(12,2,0.15),T_("Wood","wood",(0.8,0.62,0.45))); 
    for x in (-19,-14,-9): box((x,-6.3,1.2),(0.25,0.25,2.4),WHT)
    box((10,4,5),(16,22,10),RED,uv=1.5); gable(10,4,10,16,22,5,CR,"y",0.6)                     # barn
    box((10,-7.05,3.5),(6,0.1,7),C("BarnDoor","7a2420",0.6)); 
    for d in (-1,1): box((10,-7.12,3.5),(6*1.1,0.06,0.25),WHT,rot=(0,d*math.atan2(7,6),0))
    box((10,-7.1,8.6),(2,0.06,1.6),C("Loft","4a2a1e",0.6))
    cyl((22,10,8),3,16,C("Silo","b9bec4",0.35,0.8),24); sphere((22,10,16),3.05,C("Silo","b9bec4",0.35,0.8),2)
    for k in range(6): cyl((22,10,1+k*2.6),3.05,0.15,C("SiloRing","8a8f96",0.4,0.8),24)
    for i in range(10): box((-30+i*6,-14,0.6),(0.15,0.15,1.2),T_("Wood","wood",(0.75,0.6,0.45)))
    box((0,-14,1.0),(60,0.1,0.12),T_("Wood","wood",(0.75,0.6,0.45))); box((0,-14,0.55),(60,0.1,0.12),T_("Wood","wood",(0.75,0.6,0.45)))
    for k in range(5): cyl((0+k*2.2,-10,0.7),0.7,1.2,C("HayBale","d8b25a",0.9),16,rot=(0,math.radians(90),0))
    box((0,0,0.02),(70,40,0.04),C("Grass","5a7d38",0.9)); box((-4,-6,0.04),(4,20,0.05),C("Gravel","8f8a80",0.9))
    for (x,y) in ((-24,6),(-26,-2),(28,-6)): tree(x,y,1.4)
@reg("OT_TunerShop_A",(-30,-36,6),(0,-4,4),24)
def tuner():
    CR=T_("Corrugated","corr",(0.25,0.26,0.28),0.6,True); CO=T_("Concrete","conc",(0.75,0.75,0.76)); PUR=C("NeonPurple","b24bff",0.3,emit=6.0); CY=C("NeonCyan","2fe0ff",0.3,emit=6.0)
    W,D,H=28,18,8; FZ=-D/2
    box((0,0,H/2),(W,D,H),CR,uv=2.5); box((0,0,0.5),(W+0.2,D+0.2,1.0),CO)
    for i,x in enumerate((-8,0)):
        box((x,FZ-0.04,2.8),(6.4,0.06,5.0),C("BayDark","15161a",0.8)); box((x,FZ-0.07,5.0),(5,0.04,0.12),C("ShopLight","f6fbff",0.3,emit=6.0))
        box((x,FZ-0.09,0.1),(6.4,0.04,0.1),PUR)
        for s in (-1,1): box((x+s*3.4,FZ-0.15,2.8),(0.25,0.25,5.4),PUR if i==0 else CY)
    box((9,FZ-0.03,3),(7,0.06,5),glass()); box((9,FZ+1,0.4),(5,3,0.5),C("Dyno","2a2c30",0.4,0.6)); box((9,FZ+1,0.7),(5,3,0.06),CY)
    box((0,FZ-0.3,H-0.6),(W,0.4,1.0),C("Black","121212",0.5)); box((0,FZ-0.52,H-0.6),(W,0.04,0.12),PUR); box((0,FZ-0.52,H-1.0),(W,0.04,0.06),CY)
    box((-2,FZ-0.4,H+1.8),(16,0.5,2.6),C("Black","121212",0.5),bev=0.05)
    for z in (H+0.55,H+3.05): box((-2,FZ-0.67,z),(16,0.04,0.1),PUR)
    box((-2,FZ-0.68,H+1.8),(12,0.04,1.2),CY)
    for k in range(6): box((-13+k*0.5,FZ-0.1,5),(0.1,0.04,1.5),[PUR,CY][k%2])
    for k in range(4): cyl((12.6,FZ-1.5,0.2+k*0.3),0.38,0.26,C("Tire","151515",0.85),14)
    box((-12.5,FZ-1,1),(1.2,0.6,1.6),C("ToolChest","c4261d",0.4),bev=0.04)
    lot(0,FZ-9,W+12,16); 
    for i in range(6): box((-10+i*4,FZ-10,0.12),(0.12,5,0.02),PUR)
    for x in (-16,16): lightpole(x,FZ-15,8,1.6,1)
@reg("OT_FastFood_A",(-28,-32,5),(0,-3,2.5),24)
def fastfood():
    BR=T_("Brick","brick",(0.92,0.75,0.65)); RED=C("FFRed","d0281e",0.4); YEL=C("FFYellow","f6c22c",0.45)
    W,D,H=18,14,5; FZ=-D/2
    box((0,0,H/2),(W,D,H),BR,uv=1.6); storefront(-2,FZ,12,3.0,0.6,6,True)
    box((0,FZ-0.5,H+0.2),(W+1,1.2,1.2),RED,bev=0.05); box((0,FZ-1.12,H+0.2),(W+1,0.04,0.3),YEL)
    box((0,0,H+1.2),(10,8,1.6),RED,bev=0.06); prism((0,0,H+2.0),10,1.6,8.2,YEL)
    box((W/2+0.05,2,2.2),(0.1,2.4,1.4),glass()); box((W/2+1.2,2,3.6),(2.4,3,0.2),RED)                 # drive-thru window
    box((W/2+5,-2,1.3),(1.8,0.4,2.6),C("MenuBoard","1a1a1a",0.5)); box((W/2+5,-2.22,1.5),(1.6,0.04,2.0),warm())
    box((W/2+3,0,0.08),(6,30,0.04),C("LaneYellow","e8b81e",0.6))
    cyl((-11,FZ-8,5),0.3,10,C("PoleDark","2a2c30",0.45,0.6),10); box((-11,FZ-8,10.5),(4,0.8,3),RED,bev=0.08); box((-11,FZ-8.42,10.5),(3.4,0.04,2.4),YEL)
    for x in (-6,-2): cyl((x,FZ-2.6,0.75),0.6,0.06,YEL,16); cyl((x,FZ-2.6,0.4),0.06,0.7,RED,8); cyl((x,FZ-2.6,1.6),0.05,2.0,RED,8)
    for x in (-6,-2): bpy.ops.mesh.primitive_cone_add(vertices=12,radius1=1.2,depth=0.4,location=(x,FZ-2.6,2.7)); o=bpy.context.object; o.data.materials.append(RED)
    lot(0,FZ-9,W+18,14,8,-9,FZ-11); lightpole(10,FZ-14,8,1.6,-1)
@reg("OT_Motel_A",(-36,-42,8),(0,-4,3),24,(1150,780))
def motel():
    PL=T_("Stucco","plaster",(0.98,0.9,0.78)); TEAL=C("MotelTeal","1fa6a0",0.4); PINK=C("NeonPink","ff3fb4",0.3,emit=6.0)
    W,D,H=40,10,6.4; FZ=-D/2
    box((0,0,H/2),(W,D,H),PL,uv=2.0); box((0,FZ-1.2,3.2),(W,2.4,0.25),PL)
    box((0,FZ-2.4,3.9),(W,0.06,1.0),TEAL)
    for i in range(18): box((-20+i*2.35,FZ-2.4,3.85),(0.04,0.04,1.0),C("Rail","f0efe9",0.5))
    for f in (0,1):
        for i in range(10):
            x=-18+i*4; z=f*3.2
            box((x,FZ-0.03,z+1.3),(1.0,0.06,2.2),C(f"MDoor{i%3}",["1fa6a0","f26b1d","e8b81e"][i%3],0.4))
            box((x+1.4,FZ-0.03,z+1.8),(1.2,0.06,1.0),warm() if random.random()<0.4 else glass()); box((x+1.4,FZ-0.3,z+0.9),(0.9,0.5,0.6),C("SteelGrey","9aa0a6",0.35,0.85))
    for x in range(-20,21,8): box((x,FZ-2.3,1.6),(0.3,0.3,3.2),PL)
    box((0,0,H+0.15),(W+0.3,D+0.3,0.3),TEAL)
    box((W/2+3,-1,1.8),(5,7,3.6),PL); storefront(W/2+3,-4.5,4,2.4,0.5,2,True); box((W/2+3,-1,3.8),(5.4,7.4,0.3),TEAL)  # office
    cyl((-W/2-4,FZ-6,5),0.3,10,C("PoleDark","2a2c30",0.45,0.6),10); box((-W/2-4,FZ-6,9.4),(4.2,0.6,3.4),TEAL,bev=0.08)
    for z in (7.75,11.05): box((-W/2-4,FZ-6.32,z),(4.2,0.04,0.08),PINK)
    box((-W/2-4,FZ-6.33,9.4),(3.6,0.04,1.6),C("SignFace","f2efe6",0.5)); box((-W/2-4,FZ-6,7.0),(3,0.4,0.8),PINK)
    box((0,FZ-14,0.05),(W+16,18,0.1),T_("Pavement","walk",(0.86,0.86,0.84)),uv=2.5); stripes(-18,FZ-7,13,3.0,5.0)
    box((-10,FZ-15,0.3),(10,6,0.6),T_("Tile","tile",(0.95,0.95,0.95))); box((-10,FZ-15,0.62),(9,5,0.04),C("PoolWater","3fb8e0",0.1,emit=0.6))
    for x in (-20,20): lightpole(x,FZ-20,8,1.6,1)
@reg("OT_FireStation_A",(-28,-34,6),(0,-3,4),24)
def firestation():
    BR=T_("Brick","brick",(0.9,0.72,0.62)); ST=T_("Stone","trim",(0.92,0.88,0.8)); RED=C("FireRed","c4161d",0.4); WHT=C("TrimWhite","f0efe9",0.5)
    W,D,H=26,18,9; FZ=-D/2
    box((0,0,H/2),(W,D,H),BR,uv=1.6); box((0,FZ-0.06,0.5),(W+0.2,0.25,1.0),ST,bev=0.03)
    for i,x in enumerate((-8,-1,6)):
        box((x,FZ-0.03,2.6),(5,0.06,4.8),C("BayDoorFire","d23a2a",0.4,0.3) if i<2 else glass())
        for k in range(4):
            for j in range(3): box((x-1.7+j*1.7,FZ-0.07,1.0+k*1.2),(1.4,0.04,0.9),glass())
        box((x,FZ-0.12,5.4),(5.8,0.24,0.4),ST); box((x,FZ-0.22,6.0),(0.9,0.06,0.6),C("BayNum","f2c230",0.4))
    window_grid(-11,11,FZ,6.6,8.4,7,1,0.4,frame(),ST)
    box((0,FZ-0.3,H+0.8),(14,0.4,1.4),ST); box((0,FZ-0.52,H+0.8),(12,0.04,0.9),C("SignFace","f2efe6",0.5))
    box((0,0,H+0.25),(W+0.5,D+0.5,0.5),ST)
    box((W/2+3,4,8),(5,5,16),BR,uv=1.6); box((W/2+3,4,16.3),(5.5,5.5,0.6),ST); box((W/2+3,1.47,13),(1.4,0.06,3),glass())   # hose tower
    for x in (-8,-1): box((x,FZ-5,0.08),(5.6,10,0.04),C("Apron","7a7a78",0.9))
    box((-W/2+0.5,FZ-0.2,6.5),(0.6,0.5,0.6),C("GlowRed","ff2a2a",0.3,emit=5.0)); 
    for x in (-12,12): bollard(x,FZ-1,RED)
    cyl((-14,FZ-6,7),0.08,14,C("SteelGrey","9aa0a6",0.35,0.85),10); box((-13.1,FZ-6,13.2),(1.8,0.05,1.1),C("FlagRed","b8322a",0.7))
    lot(0,FZ-8,W+14,14)
@reg("OT_Hospital_A",(-50,-58,12),(0,-4,10),24,(1150,820))
def hospital():
    PL=T_("Stucco","plaster",(0.97,0.97,0.98)); BL=C("HospBlue","1f6db0",0.4); RED=C("GlowRed","ff2a2a",0.3,emit=5.0)
    box((0,0,4),(44,24,8),PL,uv=2.5); window_grid(-21,21,-12,1.2,7.4,14,2,0.45,BL)
    box((0,4,8+12),(30,16,24),PL,uv=2.5)
    for f in ("front","left","right"): pass
    window_grid(-14,14,-4,8.6,31.4,10,7,0.45,BL)
    box((-12,-12-4,7.4),(14,8,0.5),BL,bev=0.05); box((-12,-20.02,7.4),(14,0.06,0.3),led())          # ER canopy
    for x in (-18,-6): box((x,-19.5,3.6),(0.5,0.5,7.2),PL)
    box((-12,-12.05,9.2),(10,0.1,1.4),RED); 
    box((10,-12.04,2),(8,0.06,3.6),glass()); box((10,-14,4.2),(10,4,0.3),PL)
    box((0,4,32.4),(31,17,0.8),BL)
    cyl((8,6,33.2),5,0.3,C("Helipad","3a3d42",0.6),24); box((8,6,33.4),(0.6,4,0.04),C("PaintWhite","f0f0ee",0.6)); 
    for s in (-1,1): box((8+s*1.2,6,33.4),(0.6,4,0.04),C("PaintWhite","f0f0ee",0.6))
    box((8,6,33.4),(3,0.6,0.04),C("PaintWhite","f0f0ee",0.6))
    box((-14,-3.9,30),(2.4,0.06,2.4),RED); box((-14,-3.92,30),(0.8,0.04,2.0),C("CrossW","ffffff",0.3,emit=3.0)); box((-14,-3.92,30),(2.0,0.04,0.8),C("CrossW","ffffff",0.3,emit=3.0))
    lot(0,-26,56,20,14,-20,-28); 
    for x in (-24,0,24): lightpole(x,-34,9,1.8,1)
    for x in (16,22): tree(x,-17)
@reg("OT_CarWash_A",(-26,-30,5),(0,-3,2.5),24)
def carwash():
    CB=T_("Block","conc",(0.95,0.95,0.95)); BL=C("WashBlue","1f8fff",0.4); CY=C("NeonCyan","2fe0ff",0.3,emit=6.0); YEL=C("Yellow","e8b81e",0.5)
    W,D,H=24,10,5.5
    for i in range(4):
        x=-9+i*6
        box((x-3,0,H/2),(0.4,D,H),CB)
        box((x,FZ_:=-D/2,H-0.2),(6,0.3,0.4),BL)
        box((x,0,0.06),(5.4,D,0.04),C("WetFloor","4a4e54",0.2,0.3))
        box((x,-1,H-0.6),(1.6,0.3,0.2),C("WandRack","2a2c30",0.4,0.6)); box((x+2,-D/2+0.6,1.2),(0.8,0.5,1.4),C("Coin","3a3d42",0.4,0.6)); box((x+2,-D/2+0.34,1.4),(0.5,0.02,0.3),C("Screen","35c8ff",0.2,emit=2.5))
    box((15,0,H/2),(0.4,D,H),CB)
    box((0,0,H+0.15),(W+2,D+1,0.3),BL,bev=0.05); box((0,-D/2-0.52,H+0.1),(W+2,0.04,0.12),CY)
    box((0,-D/2-0.3,H+1.2),(12,0.4,1.6),BL); box((0,-D/2-0.52,H+1.2),(11,0.04,1.0),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    for i in range(4): box((-9+i*6,-D/2+0.0,H-0.6),(5.6,0.04,0.12),CY)
    for k in range(3): box((18+k*2.6,-3,1.2),(1.2,0.8,2.4),C("Vacuum","f6c22c",0.45),bev=0.05); cyl((18+k*2.6,-3,2.6),0.06,1.0,C("Hose","1a1a1a",0.6),6)
    box((0,-9,0.05),(W+16,12,0.1),T_("Pavement","walk",(0.86,0.86,0.84)),uv=2.5)
    for x in (-14,14): bollard(x,-6,YEL)
@reg("OT_TruckStop_A",(-60,-68,14),(0,-6,4),24,(1150,780))
def truckstop():
    CO=T_("Concrete","walk",(0.9,0.9,0.88)); GRN=C("TSGreen","1f6b45",0.4); YEL=C("Yellow","e8b81e",0.5); W_=C("PaintWhite","f0f0ee",0.6)
    box((0,-6,0.08),(80,44,0.16),CO,uv=4.0)
    box((-14,10,3.5),(28,14,7),T_("Brick","brick2",(0.9,0.82,0.76)),uv=1.6); storefront(-14,3,20,3.4,0.6,8,True)
    box((-14,1.8,6.4),(30,3,0.4),GRN,bev=0.05); box((-14,0.28,6.4),(30,0.04,0.2),C("GlowGreen","3aff8a",0.3,emit=4.0))
    box((-14,10,8.2),(14,0.5,2.4),GRN); box((-14,9.73,8.2),(13,0.04,1.6),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    box((18,-6,7.5),(30,16,0.8),C("CanopyW","eeeeec",0.4),bev=0.06); box((18,-14.02,7.5),(30,0.06,0.5),GRN)
    for x in (8,18,28):
        for y in (-11,-1): box((x,y,3.7),(0.7,0.7,7.4),C("SteelGrey","9aa0a6",0.35,0.85))
        box((x,-6,0.4),(2,14,0.5),CO); 
        for y in (-9,-3): box((x,y,1.5),(1.0,0.8,2.2),C("PumpBody","e9e9e6",0.35),bev=0.05); box((x,y,2.7),(1.1,0.9,0.3),GRN)
    for y in (-14,-10,-6,-2): 
        for x in (8,18,28): box((x+5,y,7.08),(2.4,1.4,0.04),led())
    for i in range(8): box((-36+i*4.2,-22,0.17),(0.15,14,0.02),W_)                         # truck parking
    box((30,12,2),(3,10,4),C("Scale","3a3d42",0.4,0.6)); box((30,12,0.2),(4,14,0.3),YEL)
    cyl((-34,-26,9),0.4,18,C("PoleDark","2a2c30",0.45,0.6),10); box((-34,-26,18.5),(6,1,4),GRN,bev=0.08); box((-34,-26.52,18.5),(5.4,0.04,3.4),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    for x in (-20,0,20,38): lightpole(x,-28,10,2.0,1)
@reg("OT_Church_A",(-30,-36,8),(0,-2,9),24,(1000,1000))
def church():
    ST=T_("Stone","granite",(0.85,0.82,0.76)); SH=T_("Slate","shingle",(0.5,0.5,0.55)); WHT=C("TrimWhite","f0efe9",0.5)
    W,D,H=14,26,9
    box((0,2,H/2),(W,D,H),ST,uv=1.6); gable(0,2,H,W,D,6,SH,"y",0.6)
    box((0,-D/2+1-3,9),(6,6,18),ST,uv=1.6); box((0,-D/2+1-3,18.4),(6.6,6.6,0.8),ST)                    # bell tower
    bpy.ops.mesh.primitive_cone_add(vertices=4,radius1=4.3,depth=10,location=(0,-D/2-2,23.8),rotation=(0,0,math.radians(45))); o=bpy.context.object; o.data.materials.append(SH)
    box((0,-D/2-2,29.5),(0.25,0.25,2),C("Gold","d8b25a",0.3,0.9)); box((0,-D/2-2,29.9),(1.0,0.25,0.25),C("Gold","d8b25a",0.3,0.9))
    for s in (-1,1): halfcyl((s*1.2,-D/2-5.02,15.5),0.6,0.1,C("Louver","2a2c30",0.5),12); box((s*1.2,-D/2-5.02,14.6),(1.2,0.1,1.8),C("Louver","2a2c30",0.5))
    halfcyl((0,-D/2-5.05,10.5),1.4,0.1,C("RoseWin","8a3a9e",0.2,emit=1.5),24)
    box((0,-D/2-5.04,2.4),(2.4,0.1,4.4),C("ChurchDoor","5a2e1c",0.5)); halfcyl((0,-D/2-5.04,4.6),1.2,0.1,C("ChurchDoor","5a2e1c",0.5),16)
    for i in range(5):
        for s in (-1,1):
            y=-6+i*4.6; box((s*(W/2+0.03),y,5),(0.06,1.4,4.4),C("Stained","3a6ea8",0.2,emit=1.2)); halfcyl((s*(W/2+0.03),y,7.2),0.7,0.06,C("Stained","3a6ea8",0.2,emit=1.2),12,axis="x")
            box((s*(W/2+0.4),y+2.3,4),(0.8,0.8,8),ST)
    for i in range(3): box((0,-D/2-5.6-i*0.4,0.15+i*0.15*0),(5,0.4,0.3+i*0.0),ST)
    box((0,-24,0.05),(30,14,0.1),T_("Pavement","walk",(0.86,0.86,0.84))); tree(-11,-16,1.3); tree(11,-16,1.3)
    for x in (-5,5): bench(x,-20)
@reg("OT_PortCrane_A",(-70,-80,24),(0,0,18),24,(1150,820))
def portcrane():
    STL=C("CraneRed","c4361d",0.45,0.4); STL2=C("CraneDark","2a2c30",0.45,0.6); CO=T_("Concrete","walk",(0.85,0.85,0.83))
    box((0,0,0.1),(80,40,0.2),CO,uv=4.0); box((0,22,-1),(80,4,2),C("DockEdge","3a3d42",0.7))
    for x in (-8,8):                                     # gantry crane legs
        for y in (-6,10): box((x,y,14),(1.2,1.2,28),STL)
        box((x,2,28),(1.4,18,1.4),STL)
    box((0,4,30),(18,4,2),STL); box((0,18,30),(4,40,1.6),STL); box((0,-10,30),(4,14,1.6),STL)  # boom
    box((0,-14,32),(6,4,4),STL2); box((0,2,27),(3,3,2),STL2); cyl((0,2,22),0.05,10,STL2,6); box((0,2,16.6),(3,6,0.6),STL2)
    for k in range(6): box((0,10+k*5,33),(0.2,0.2,4),STL)
    cols=["b8322a","2a5fb0","2fa45a","e8b81e","f26b1d","8a8f96"]
    for i in range(8):
        for j in range(3):
            for lv in range(1+((i+j)%3)):
                box((-30+i*7.5 if i<4 else 0+i*4.8,-14+j*3,1.5+lv*2.7),(6.1,2.5,2.6),C(f"Cont{(i+j+lv)%6}",cols[(i+j+lv)%6],0.5,0.4),bev=0.04)
    for x in (-30,30): lightpole(x,-18,14,2.4,1)
@reg("OT_Landmark_Tower",(-70,-80,20),(0,0,50),24,(800,1150))
def landmark():
    CO=T_("Concrete","conc",(0.92,0.92,0.92)); GL2=C("CurtainGlass","2b4d66",0.06,0.4); LED=C("LEDStrip","e8f2ff",0.3,emit=6.0); GOLD=C("GoldGlow","ffd27a",0.3,emit=3.5)
    cyl((0,0,2),14,4,T_("Granite","granite",(0.7,0.7,0.72)),32)
    for k in range(3):
        a=math.radians(k*120); box((math.cos(a)*6,math.sin(a)*6,24),(3,3,48),CO,rot=(0,0,a))
    cyl((0,0,40),3.2,80,CO,24)
    bpy.ops.mesh.primitive_uv_sphere_add(radius=9,location=(0,0,84),segments=32,ring_count=16); o=bpy.context.object; o.scale=(1,1,0.45); o.data.materials.append(GL2)
    cyl((0,0,84),9.4,0.6,LED,32); cyl((0,0,80),8.0,0.4,GOLD,32)
    cyl((0,0,92),1.2,8,CO,16); cyl((0,0,104),0.35,16,C("Antenna","c9ccd1",0.3,0.9),8); sphere((0,0,112.5),0.6,C("GlowRed","ff2a2a",0.3,emit=6.0),1)
    for z in range(10,80,10): cyl((0,0,z),3.35,0.3,LED,24)
    for x in (-10,10): tree(x,-16,1.2)
    box((0,-20,0.05),(40,14,0.1),T_("Pavement","walk",(0.86,0.86,0.84)))
name=sys.argv[-2]; mode=sys.argv[-1]
f,cam,tgt,lens,res=BLD[name]; reset(); random.seed(hash(name)%1000); _cache.clear(); f()
if mode=="render": world_and_render(f"/home/claude/blender/r_{name}.png",cam,tgt,lens,res,20)
else: export(name,drop_y=-999)
