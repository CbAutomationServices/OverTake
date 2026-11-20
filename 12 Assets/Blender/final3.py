exec(open("/home/claude/blender/kit2.py").read())
import sys
def curtain(W,D,z0,H,GL,FR,cols,floors,faces=("front","left","right","back")):
    box((0,0,z0+H/2),(W,D,H),GL)
    for f in faces:
        span=W if f in("front","back") else D
        for c in range(cols+1):
            u=-span/2+c*span/cols
            p={"front":(u,-D/2-0.08),"back":(u,D/2+0.08),"left":(-W/2-0.08,u),"right":(W/2+0.08,u)}[f]
            sz=(0.18,0.12) if f in("front","back") else (0.12,0.18); box((p[0],p[1],z0+H/2),(sz[0],sz[1],H),FR)
        for r in range(floors+1):
            p={"front":(0,-D/2-0.08),"back":(0,D/2+0.08),"left":(-W/2-0.08,0),"right":(W/2+0.08,0)}[f]
            sz=(span,0.12) if f in("front","back") else (0.12,span); box((p[0],p[1],z0+r*H/floors),(sz[0],sz[1],0.22),FR)
def base_plinth(W,D,H,M,sf_w):
    box((0,0,H/2),(W,D,H),M,uv=2.0); storefront(0,-D/2,sf_w,H*0.65,0.5,int(sf_w/2.2),True)
    box((0,-D/2-1.4,H*0.85),(sf_w+2,2.8,0.3),C("CanopyDark","2a2c30",0.4,0.6)); box((0,-D/2-2.8,H*0.85-0.05),(sf_w+2,0.06,0.14),led())
@reg("OT_Skyscraper_Twist",(-60,-70,10),(0,0,45),24,(800,1150))
def twist():
    GL=C("TealGlass","2a5a62",0.05,0.4); FR=C("Mullion","c9ccd1",0.25,0.9); GR=T_("Granite","granite",(0.62,0.62,0.64))
    base_plinth(30,30,8,GR,20)
    for i in range(22):
        z=8+i*4; a=math.radians(i*3.2)
        box((0,0,z+1.9),(20,20,3.6),GL,rot=(0,0,a)); box((0,0,z+3.8),(20.6,20.6,0.4),FR,rot=(0,0,a))
        if i%3==0:
            for s in (-1,1): box((s*5*math.cos(a),s*5*math.sin(a),z+1.9),(0.2,20.4,3.6),FR,rot=(0,0,a)) if False else None
    for k in range(4):
        a=math.radians(21*3.2)+k*math.pi/2
        box((math.cos(a)*10,math.sin(a)*10,98),(0.6,0.6,12),C("LEDStrip","e8f2ff",0.3,emit=5.0))
    cyl((0,0,100),2,8,FR,16); cyl((0,0,110),0.3,14,FR,8); sphere((0,0,117.2),0.5,C("GlowRed","ff2a2a",0.3,emit=6.0),1)
    lot(0,-24,46,12)
@reg("OT_Skyscraper_Setback",(-60,-72,10),(0,0,42),24,(800,1150))
def setback():
    GL=C("GreenGlass","2f5a48",0.05,0.4); FR=C("Mullion","d6d8dc",0.25,0.9); LEDc=C("LEDStrip","e8f2ff",0.3,emit=5.0)
    base_plinth(34,28,9,T_("Limestone","plaster",(0.9,0.88,0.84)),24)
    tiers=[(30,24,9,36),(24,20,45,24),(18,15,69,18),(12,10,87,10)]
    for (w,d,z0,h) in tiers:
        curtain(w,d,z0,h,GL,FR,int(w/3),int(h/4))
        box((0,0,z0+h+0.3),(w+0.6,d+0.6,0.6),FR); box((0,-d/2-0.32,z0+h+0.3),(w+0.6,0.04,0.2),LEDc)
    for s in (-1,1): box((s*4,0,101),(0.8,6,8),FR); box((s*4,-3.02,101),(0.1,0.06,8),LEDc)
    lot(0,-22,48,12)
@reg("OT_Skyscraper_Round",(-55,-65,10),(0,0,40),24,(800,1150))
def roundt():
    GL=C("BlueGlass","2b4d66",0.06,0.4); FR=C("Mullion","c9ccd1",0.25,0.9)
    cyl((0,0,4),18,8,T_("Granite","granite",(0.62,0.62,0.64)),32); 
    box((0,-17,3.2),(14,4,5.4),glass()); box((0,-18,6.2),(16,4,0.4),FR)
    cyl((0,0,8+36),13,72,GL,32)
    for z in range(8,81,4): cyl((0,0,z),13.25,0.35,FR,32)
    for k in range(16):
        a=k*math.pi/8; box((math.cos(a)*13.2,math.sin(a)*13.2,44),(0.3,0.3,72),FR,rot=(0,0,a))
    cyl((0,0,82),11,4,FR,32); cyl((0,0,84.2),11.2,0.4,C("LEDStrip","e8f2ff",0.3,emit=5.0),32)
    bpy.ops.mesh.primitive_cone_add(vertices=24,radius1=10,depth=10,location=(0,0,89)); o=bpy.context.object; o.data.materials.append(GL)
    cyl((0,0,100),0.25,14,FR,8); sphere((0,0,107.2),0.45,C("GlowRed","ff2a2a",0.3,emit=6.0),1)
    lot(0,-26,46,12)
@reg("OT_Skyscraper_Residential",(-50,-60,10),(0,0,38),24,(800,1150))
def resid():
    WH=T_("Stucco","plaster",(0.97,0.96,0.94)); GL=glass(); RL=C("Railing","2a2c30",0.4,0.6); WD=T_("Wood","wood",(0.85,0.62,0.42))
    W,D,H=18,16,78
    base_plinth(W+4,D+4,7,T_("Granite","granite",(0.55,0.55,0.58)),14)
    box((0,0,7+H/2),(W,D,H),WH,uv=3.0)
    for f in range(24):
        z=7+1.2+f*3.2
        for sgn,face in ((-1,"front"),):
            for c in range(4):
                x=-W/2+2.25+c*4.5
                box((x,-D/2-0.02,z+0.6),(3.4,0.04,2.2),warm() if random.random()<0.3 else GL)
                box((x,-D/2-0.9,z-0.4),(3.9,1.8,0.16),WH); box((x,-D/2-1.78,z+0.1),(3.9,0.04,0.9),GL); box((x,-D/2-1.78,z+0.55),(3.9,0.06,0.06),RL)
        for s in (-1,1):
            for c in range(3): box((s*(W/2+0.02),-D/2+2.6+c*5.4,z+0.6),(0.04,3.6,2.2),warm() if random.random()<0.3 else GL)
    for s in (-1,1): box((s*(W/2-0.3),-D/2-0.3,7+H/2),(0.9,0.9,H),WD)
    box((0,0,7+H+1.5),(W-4,D-4,3),C("SteelGrey","9aa0a6",0.35,0.85)); box((0,0,7+H+0.2),(W+0.4,D+0.4,0.4),WH)
    lot(0,-D/2-8,34,10); tree(-12,-D/2-4); tree(12,-D/2-4)
@reg("OT_Skyscraper_Twin",(-90,-105,14),(0,0,44),24,(900,1150))
def twin():
    GL=C("SilverGlass","4a5a68",0.06,0.5); FR=C("Mullion","c9ccd1",0.25,0.9); LEDc=C("LEDStrip","e8f2ff",0.3,emit=5.0)
    box((0,0,4),(56,24,8),T_("Granite","granite",(0.6,0.6,0.62)),uv=2.0); storefront(0,-12,40,5,0.6,16,True)
    for sx,H in ((-15,76),(15,64)):
        box((sx,0,8+H/2),(18,18,H),GL)
        for c in range(7):
            u=-9+c*3
            box((sx+u,-9.08,8+H/2),(0.18,0.12,H),FR); box((sx-9.08,u,8+H/2),(0.12,0.18,H),FR); box((sx+9.08,u,8+H/2),(0.12,0.18,H),FR)
        for r in range(0,H+1,4):
            box((sx,-9.08,8+r),(18,0.12,0.22),FR); box((sx-9.08,0,8+r),(0.12,18,0.22),FR); box((sx+9.08,0,8+r),(0.12,18,0.22),FR)
        box((sx,0,8+H+1),(16,16,2),FR); box((sx,-8.02,8+H+1),(16,0.06,0.25),LEDc)
    box((0,0,52),(12,8,4),GL); box((0,-4.05,50.1),(12,0.1,0.25),FR); box((0,-4.06,53.9),(12,0.1,0.25),FR); box((0,-4.07,52),(12,0.04,0.12),LEDc)
    cyl((-15,0,92),0.3,12,FR,8); sphere((-15,0,98.2),0.45,C("GlowRed","ff2a2a",0.3,emit=6.0),1)
    lot(0,-20,62,12)
@reg("OT_Skyscraper_Brick",(-46,-56,10),(0,0,30),24,(800,1150))
def brickhigh():
    BR=T_("Brick","brick",(0.92,0.72,0.6)); ST=T_("Stone","trim",(0.9,0.85,0.76)); FR=frame()
    W,D=22,18
    box((0,0,3),(W+1,D+1,6),ST,uv=2.0); storefront(0,-D/2-0.5,16,4,0.5,8,True,ST)
    box((0,0,6+24),(W,D,48),BR,uv=1.6)
    for f in ("front","left","right"): face_grid(f,W,D,6.6,53.4,8 if f=="front" else 6,14,FR,0.35)
    for s in (-1,1): box((s*(W/2-0.4),-D/2-0.3,30),(1.2,0.8,48),ST)
    for z in (20,40): box((0,-D/2-0.2,z),(W+0.4,0.5,0.6),ST)
    box((0,0,54.4),(W+1,D+1,0.8),ST); box((0,0,57),(14,12,4.4),BR); box((0,-6.02,57),(12,0.06,1.2),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    wt=T_("Wood","wood",(0.65,0.48,0.34))                     # water tower
    for dx in (-1.4,1.4):
        for dy in (-1.4,1.4): box((5+dx,3+dy,60.5),(0.2,0.2,3),C("Iron","1c1c1c",0.5,0.6))
    cyl((5,3,64),2.2,4,wt,14); bpy.ops.mesh.primitive_cone_add(vertices=14,radius1=2.4,depth=1.4,location=(5,3,66.7)); o=bpy.context.object; o.data.materials.append(C("SteelGrey","9aa0a6",0.35,0.85))
    lot(0,-D/2-6,36,10)
@reg("OT_Skyscraper_Braced",(-60,-72,10),(0,0,45),24,(800,1150))
def braced():
    GL=C("DarkGlass","15191e",0.05,0.5); FR=C("BlackSteel","1e2024",0.35,0.8); LEDc=C("LEDStrip","e8f2ff",0.3,emit=5.0)
    base_plinth(32,28,8,T_("Granite","granite",(0.4,0.4,0.42)),22)
    levels=12
    for i in range(levels):
        z=8+i*7; w=26-i*0.9; d=22-i*0.75
        box((0,0,z+3.5),(w,d,7),GL)
        for fy,ww in ((-d/2-0.1,w),(d/2+0.1,w)):
            for s in (-1,1): box((0,fy,z+3.5),(math.hypot(ww,7),0.25,0.45),FR,rot=(0,s*math.atan2(7,ww),0))
        for fx in (-w/2-0.1,w/2+0.1):
            for s in (-1,1): box((fx,0,z+3.5),(0.25,math.hypot(d,7),0.45),FR,rot=(s*math.atan2(7,d),0,0))
        box((0,0,z+7),(w+0.4,d+0.4,0.35),FR)
        if i%2==0: box((0,-d/2-0.14,z+5.8),(w*0.8,0.04,0.1),C("InteriorWarm","ffdca8",0.3,emit=1.6))
    for s in (-1,1): cyl((s*3,0,100),0.3,16,FR,8); sphere((s*3,0,108.2),0.45,C("GlowRed","ff2a2a",0.3,emit=6.0),1)
    box((0,-8.5,92.2),(14,0.06,0.3),LEDc)
    lot(0,-22,46,12)
@reg("OT_CornerShop_A",(-24,-28,5),(0,-2,5),24)
def cornershop():
    BR=T_("Brick","brick",(0.95,0.78,0.66)); ST=T_("Stone","trim",(0.9,0.86,0.78)); IRON=C("Iron","1c1c1c",0.5,0.6)
    W,D,H=14,12,13; FZ=-D/2
    box((0,0,H/2),(W,D,H),BR,uv=1.6); box((0,0,2.1),(W+0.2,D+0.2,4.2),C("ShopGreen","1f5a3a",0.45))
    storefront(-1.5,FZ-0.1,9,2.8,0.6,4,True); box((W/2+0.1,-1,2.0),(0.04,8,2.8),glass())
    awning_striped(-1.5,FZ-0.1,9,4.0,C("AwnRed","b8322a",0.6),C("AwnW","f0efe9",0.6),1.4)
    signband(-1.5,FZ-0.1,9,4.6,C("ShopGreen","1f5a3a",0.45),C("NeonW","fff4e0",0.3,emit=4.0),0.7)
    window_grid(-6.5,6.5,FZ,5.4,12.2,4,3,0.4,frame(),ST)
    for f in range(3):                                  # fire escape
        z=5.6+f*2.4; box((W/2+0.9,0,z),(1.6,7,0.08),IRON); box((W/2+1.7,0,z+0.5),(0.06,7,0.06),IRON)
        for k in range(8): box((W/2+1.7,-3.5+k*1.0,z+0.25),(0.04,0.04,0.5),IRON)
        box((W/2+0.9,2,z-1.2),(0.8,0.06,2.6),IRON,rot=(0.0,0,0))
    box((0,0,H+0.3),(W+0.4,D+0.4,0.6),ST); roofunits([(3,2,2,2,1.2)],H+0.6)
    box((0,FZ-3,0.05),(24,6,0.1),T_("Pavement","walk",(0.86,0.86,0.84))); tree(6,FZ-3.5,0.8)
@reg("OT_MixedUse_A",(-34,-40,7),(0,-3,7),24,(1100,820))
def mixeduse():
    PL=T_("Stucco","plaster",(0.92,0.92,0.92)); cols=["e07a3a","3a8fd0","e8c23a","4aa86a"]; FR=C("DarkFrame","25282c",0.4,0.5)
    W,D,H=36,16,16; FZ=-D/2
    box((0,0,2.5),(W,D,5),C("Charcoal","2e3136",0.5)); 
    for i in range(4): storefront(-13.5+i*9,FZ,8,3.4,0.5,4,True); signband(-13.5+i*9,FZ,8,4.5,C(f"MU{i}",cols[i],0.45),None,0.6)
    box((0,0,5+(H-5)/2),(W,D,H-5),PL,uv=2.0)
    for i in range(6):
        x=-15+i*6
        box((x,FZ-0.15,5+(H-5)/2),(2.0,0.3,H-5),C(f"MUp{i%4}",cols[i%4],0.5))
        for f in range(3):
            z=6+f*3.5; box((x+2.6,FZ-0.02,z+1.2),(2.6,0.04,2.2),warm() if random.random()<0.35 else glass())
            box((x+2.6,FZ-0.7,z-0.1),(3.2,1.4,0.15),PL); box((x+2.6,FZ-1.38,z+0.4),(3.2,0.04,0.9),glass())
    box((0,0,H+0.15),(W+0.3,D+0.3,0.3),FR); roofunits([(-10,2,3,2,1.2),(8,2,3,2,1.2)],H+0.3)
    for k in range(5): box((-14+k*7,0,H+0.9),(5,4,0.1),C("Solar","1b2a4a",0.2,0.6),rot=(0.25,0,0))
    box((0,FZ-3.5,0.05),(W+6,7,0.1),T_("Pavement","walk",(0.86,0.86,0.84)))
    for x in (-12,0,12): tree(x,FZ-4.5,0.9)
@reg("OT_Duplex_A",(-22,-26,5),(0,-2,3),24)
def duplex():
    S=T_("Siding","plaster",(0.88,0.84,0.74)); SH=T_("Shingle","shingle",(0.6,0.6,0.6)); WHT=C("TrimWhite","f0efe9",0.5)
    W,D,H=18,10,6; FZ=-D/2
    box((0,0,H/2),(W,D,H),S,uv=1.5); gable(0,0,H,W,D,2.8,SH,"x",0.5)
    for k in range(10): box((0,FZ-0.03,0.4+k*0.6),(W,0.04,0.06),C("LapLine","bdb6a4",0.6))
    for s in (-1,1):
        x=s*4.5
        box((x-s*1.5,FZ-0.05,1.2),(1.0,0.1,2.2),C("DoorBlue" if s<0 else "DoorRed","1f3a5c" if s<0 else "7a1f1f",0.4))
        for wx in (x+s*1.0,x+s*2.6): box((wx,FZ-0.04,1.6),(1.1,0.06,1.4),warm() if random.random()<0.4 else glass()); box((wx,FZ-0.06,1.6),(1.3,0.04,1.6),WHT)
        for wx in (x-1.2,x+1.2): box((wx,FZ-0.04,4.4),(1.1,0.06,1.2),glass()); box((wx,FZ-0.06,4.4),(1.3,0.04,1.4),WHT)
        box((x-s*1.5,FZ-1.0,0.15),(2.2,2,0.3),T_("Concrete","walk",(0.9,0.9,0.88))); box((x-s*1.5,FZ-1.0,2.6),(2.6,2.2,0.15),WHT)
        box((x+s*1.6,FZ-4,0.06),(3,8,0.1),T_("Concrete","walk",(0.9,0.9,0.88)))
    box((0,0,0.02),(26,22,0.04),C("Lawn","567d3a",0.9)); box((0,FZ+0.2,0.25),(0.15,D-0.4,0.5),WHT)
    for x in (-11,11): tree(x,-4,1.0)
    for k in range(4): sphere((-1.5+k*1.0,FZ-0.7,0.45),0.45,C("Shrub","3e6b2f",0.9),2)
@reg("OT_Laundromat_A",(-22,-26,4),(0,-2,2.5),24)
def laundromat():
    PL=T_("Stucco","plaster",(0.85,0.92,0.98)); BL=C("LaunBlue","1f6db0",0.45); CY=C("NeonCyan","2fe0ff",0.3,emit=6.0)
    W,D,H=16,12,5; FZ=-D/2
    box((0,0,H/2),(W,D,H),PL,uv=1.6); storefront(0,FZ,13,3,0.5,6,True)
    for k in range(6): box((-5.5+k*2.2,FZ+1.2,0.6),(1.2,1,1.2),C("Washer","e9e9e6",0.35)); cyl((-5.5+k*2.2,FZ+0.68,0.7),0.35,0.04,C("Door","3a3d42",0.2,0.5),12,rot=(math.radians(90),0,0))
    signband(0,FZ,14,H-0.1,BL,CY,1.0)
    box((0,0,H+0.15),(W+0.3,D+0.3,0.3),BL); roofunits([(4,2,2,2,1)],H+0.3)
    cyl((W/2+2,FZ-2,2),0.12,4,C("PoleDark","2a2c30",0.45,0.6),8); box((W/2+2,FZ-2,4.4),(1.6,0.2,1.0),BL); box((W/2+2,FZ-2.12,4.4),(1.4,0.04,0.8),CY)
    lot(0,FZ-6,W+10,10,5,-6,FZ-7)
@reg("OT_AutoParts_A",(-30,-36,6),(0,-4,3),24,(1100,780))
def autoparts():
    BR=T_("Block","plaster",(0.82,0.82,0.82)); RED=C("APRed","c4161d",0.4); YEL=C("Yellow","e8b81e",0.5); W_=C("PaintWhite","f0f0ee",0.6)
    W,D,H=30,20,7; FZ=-D/2
    box((0,0,H/2),(W,D,H),BR,uv=2.0); box((0,FZ-0.1,H-1.2),(W+0.2,0.3,2.4),RED)
    for k in range(int(W/1.0)): box((-W/2+0.5+k,FZ-0.27,H-1.2),(0.08,0.04,2.4),C("RedLine","a01218",0.4))
    box((0,FZ-0.5,H+1.3),(16,0.5,2.6),RED,bev=0.05); box((0,FZ-0.77,H+1.3),(14.5,0.04,1.6),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    box((-6,FZ-0.78,H+1.3),(1.8,0.03,1.8),C("Checker","1a1a1a",0.5))
    storefront(-4,FZ,16,3.4,0.5,8,True); box((8,FZ-0.04,1.8),(5,0.06,3.4),glass())
    for k in range(3): box((10.5+k*1.6,FZ-1,0.6),(1.2,0.8,1.2),C("Pallet","c0a070",0.8)); cyl((10.5+k*1.6,FZ-1,1.5),0.38,0.26,C("Tire","151515",0.85),14)
    for x in (-W/2+0.3,W/2-0.3): box((x,FZ-0.3,H/2),(0.6,0.6,H),RED)
    lot(0,FZ-9,W+14,16,8,-11,FZ-10); 
    for x in (-14,14): lightpole(x,FZ-15,8,1.6,1)
    cyl((-W/2-4,FZ-6,5),0.3,10,C("PoleDark","2a2c30",0.45,0.6),10); box((-W/2-4,FZ-6,10.2),(4,0.6,2.4),RED,bev=0.06); box((-W/2-4,FZ-6.32,10.2),(3.4,0.04,1.6),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
@reg("OT_Gym_A",(-30,-36,6),(0,-4,4),24,(1100,780))
def gym():
    CR=C("GymGrey","3a3e44",0.45,0.4); OR=C("NeonOrange","ff7a1a",0.3,emit=6.0); FR=C("DarkFrame","25282c",0.4,0.5)
    W,D,H=28,22,9; FZ=-D/2
    box((0,0,H/2),(W,D,H),CR,uv=2.0)
    for k in range(int(W/1.2)): box((-W/2+0.6+k*1.2,FZ-0.04,H/2),(0.12,0.08,H),C("Rib","2a2e33",0.45,0.5))
    box((-3,FZ-0.12,4),(18,0.06,6.4),glass()); box((-3,FZ-0.1,4),(18,0.04,6.4),warm())
    for k in range(10): box((-11.6+k*1.9,FZ-0.18,4),(0.12,0.1,6.4),FR)
    box((-3,FZ-0.18,2.2),(18,0.1,0.12),FR)
    for k in range(5): box((-10+k*3.5,FZ+1.5,0.5),(2,0.6,0.25),C("Equip","1a1a1a",0.5,0.4)); box((-10+k*3.5,FZ+1.5,1.2),(0.1,0.1,1.4),C("SteelGrey","9aa0a6",0.35,0.85))
    box((9,FZ-0.04,1.6),(2.4,0.08,3.2),C("Door","3a3d42",0.4,0.5)); box((9,FZ-1.4,3.6),(4,2.8,0.25),FR)
    box((-3,FZ-0.3,H+0.4),(14,0.4,1.4),FR); box((-3,FZ-0.52,H+0.4),(12,0.04,0.7),OR)
    box((0,FZ-0.2,0.15),(W,0.1,0.06),OR); box((0,0,H+0.1),(W+0.3,D+0.3,0.2),FR)
    lot(0,FZ-9,W+14,16,8,-11,FZ-10)
    for x in (-14,14): lightpole(x,FZ-15,8,1.6,1)
@reg("OT_Factory_A",(-60,-68,16),(0,0,6),24,(1150,780))
def factory():
    BR=T_("Brick","brick",(0.85,0.66,0.56)); CR=C("FacMetal","8e98a3",0.45,0.5); STK=T_("Brick","brick",(0.8,0.6,0.5))
    W,D,H=50,30,12
    box((0,0,H/2),(W,D,H),BR,uv=1.8)
    for i in range(5):                                      # sawtooth roof
        x=-20+i*10; box((x,0,H+2),(10,D,0.3),CR,rot=(0,math.radians(22),0)); box((x+4.6,0,H+2),(0.2,D,4),glass())
    for k in range(10):
        x=-22.5+k*5; box((x,-D/2-0.03,6),(3,0.06,6),glass()); box((x,-D/2-0.06,6),(3.2,0.04,6.2),frame())
        box((x,-D/2-0.06,6),(0.1,0.06,6),frame())
    for s in (0,1):
        cyl((W/2+4+s*6,8,14),1.8,28,STK,16); cyl((W/2+4+s*6,8,27),2.1,1,STK,16)
        for z in (8,16,22): cyl((W/2+4+s*6,8,z),1.85,0.4,C("Band","e0e0e0",0.5),16)
    cyl((-W/2-8,-4,5),4,10,C("Tank","c9ccd1",0.35,0.8),20); sphere((-W/2-8,-4,10),4,C("Tank","c9ccd1",0.35,0.8),2)
    cyl((-W/2-8,8,5),4,10,C("Tank","c9ccd1",0.35,0.8),20); sphere((-W/2-8,8,10),4,C("Tank","c9ccd1",0.35,0.8),2)
    box((-W/2-4,2,9),(8,0.8,0.8),C("Pipe","6a7078",0.4,0.8)); box((W/2+2,8,10),(4,0.8,0.8),C("Pipe","6a7078",0.4,0.8))
    box((0,-D/2-0.3,H-1.2),(20,0.3,1.6),C("FacGreen","1f5a3a",0.45)); box((0,-D/2-0.47,H-1.2),(18,0.04,1.0),C("SignFace","f2efe6",0.5))
    lot(0,-D/2-10,W+30,20,8,-10,-D/2-14)
    for x in (-24,0,24): lightpole(x,-D/2-19,10,2.0,1)
    box((0,0,0.02),(W+40,D+50,0.04),C("Gravel","8f8a80",0.9))
@reg("OT_OfficePark_A",(-40,-46,8),(0,-4,4),24,(1150,780))
def officepark():
    PL=T_("Stucco","plaster",(0.93,0.9,0.84)); GL=C("BlueGlass","2b4d66",0.06,0.4); FR=C("Mullion","c9ccd1",0.25,0.9)
    W,D,H=40,18,8.4; FZ=-D/2
    box((0,0,H/2),(W,D,H),PL,uv=2.0)
    for z0 in (0.8,5.0): 
        box((0,FZ-0.04,z0+1.4),(W-4,0.06,2.6),GL)
        for k in range(19): box((-18+k*2,FZ-0.08,z0+1.4),(0.12,0.08,2.6),FR)
    for s in (-1,1): box((s*(W/2-1),FZ-0.3,H/2),(2,0.6,H),PL)
    box((0,FZ-2,H*0.5),(10,4,H),GL); box((0,FZ-2,H+0.2),(10.4,4.4,0.4),PL); box((0,FZ-4.03,2.2),(4,0.06,3.6),warm())
    box((0,FZ-4.5,1.0),(12,0.6,2),PL,bev=0.04); box((0,FZ-4.82,1.0),(8,0.04,0.6),C("SignFace","f2efe6",0.5))
    box((0,0,H+0.2),(W+0.4,D+0.4,0.4),FR); roofunits([(-12,2,4,3,1.5),(12,2,4,3,1.5)],H+0.4)
    lot(0,FZ-14,W+10,18,12,-16,FZ-16)
    for x in (-18,-6,6,18): tree(x,FZ-6,1.0)
    for x in (-20,0,20): lightpole(x,FZ-22,8,1.6,1)
name=sys.argv[-2]; mode=sys.argv[-1]
f,cam,tgt,lens,res=BLD[name]; reset(); random.seed(hash(name)%1000); _cache.clear(); f()
if mode=="render": world_and_render(f"/home/claude/blender/r_{name}.png",cam,tgt,lens,res,20)
else: export(name,drop_y=-999)
