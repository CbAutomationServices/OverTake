exec(open("/home/claude/blender/kit2.py").read())
import sys
def car(x,y,rz=0.0,col="c4261d",z0=0.0):
    B=C(f"Car{col}",col,0.25,0.6); G=C("CarGlass","10161c",0.05,0.3); T=C("Tire","151515",0.85); R=C("Rim","c9ccd1",0.3,0.9)
    ca,sa=math.cos(rz),math.sin(rz)
    def L(dx,dy,dz): return (x+dx*ca-dy*sa, y+dx*sa+dy*ca, z0+dz)
    box(L(0,0,0.65),(4.4,1.85,0.7),B,bev=0.12,rot=(0,0,rz)); box(L(-0.3,0,1.22),(2.2,1.58,0.5),G,bev=0.12,rot=(0,0,rz))
    box(L(-0.4,0,1.5),(1.7,1.66,0.1),B,bev=0.04,rot=(0,0,rz))
    for s_ in (-1,1): box(L(-0.3,s_*0.8,1.22),(0.12,0.06,0.5),B,rot=(0,0,rz))
    for dx in (-1.4,1.4):
        for dy in (-0.88,0.88):
            cyl(L(dx,dy,0.36),0.36,0.26,T,14,rot=(math.radians(90),0,rz)); cyl(L(dx,dy*1.02,0.36),0.24,0.27,R,10,rot=(math.radians(90),0,rz))
    box(L(2.2,0,0.7),(0.04,1.5,0.14),C("HeadLight","fff6e0",0.3,emit=3.0),rot=(0,0,rz)); box(L(-2.2,0,0.75),(0.04,1.5,0.1),C("TailLight","ff2020",0.3,emit=3.0),rot=(0,0,rz))
def jersey(x0,x1,y,z=0.0,m=None):
    m=m or T_("Concrete","plaster",(0.82,0.82,0.8))
    L=x1-x0; box(((x0+x1)/2,y,z+0.25),(L,0.6,0.5),m); box(((x0+x1)/2,y,z+0.65),(L,0.3,0.5),m)
def guardrail(x0,x1,y,z=0.0,step=2.0):
    S=C("Galv","b9bec4",0.35,0.85); P=C("GalvPost","8e959c",0.4,0.8)
    L=x1-x0; box(((x0+x1)/2,y,z+0.62),(L,0.08,0.32),S); box(((x0+x1)/2,y+0.05,z+0.52),(L,0.04,0.08),S)
    n=int(L/step)
    for i in range(n+1): box((x0+i*L/n,y+0.12,z+0.4),(0.12,0.12,0.8),P)
@reg("OT_Dealership_A",(-34,-40,7),(0,-4,3),24,(1150,800))
def dealership():
    GL=C("ShowGlass","1d2a33",0.04,0.3); FR=C("Mullion","c9ccd1",0.25,0.9); RED=C("OTRed","d0181e",0.35); CY=C("NeonCyan","2fe0ff",0.3,emit=6.0)
    WH=T_("Panel","plaster",(0.95,0.95,0.96)); TL=T_("Tile","tile",(0.9,0.9,0.92))
    W,D,H=34,20,8; FZ=-D/2
    box((0,0,0.15),(W,D,0.3),TL,uv=2.0)
    box((0,0,H/2),(W-0.2,D-0.2,H),GL)                                       # glass box
    for x in range(-17,18,3): box((x,FZ-0.05,H/2),(0.16,0.12,H),FR)
    for y in range(-10,11,4):
        for s in (-1,1): box((s*(W/2+0.05),y,H/2),(0.12,0.16,H),FR)
    box((0,FZ-0.05,H*0.5),(W,0.12,0.14),FR)
    box((-2,0,H+0.5),(W+6,D+4,1.0),WH,bev=0.08,rot=(math.radians(-3),0,0))   # floating roof
    box((-2,FZ-2.05,H+0.3),(W+6,0.06,0.25),CY)
    box((W/2+6,4,4),(12,14,8),WH,uv=2.0)                                    # service building
    for i in range(3): box((W/2+2+i*4,4-7.03,2.4),(3.2,0.06,4.4),C("BayDoor","b8bcc2",0.5,0.4))
    box((W/2+6,4-7.1,6.6),(10,0.12,1.0),RED); box((W/2+6,4-7.18,6.6),(9,0.04,0.6),C("SignWhiteGlow","f4f8ff",0.3,emit=3.0))
    box((-6,FZ-0.15,H+1.6),(16,0.5,2.2),RED,bev=0.05); box((-6,FZ-0.42,H+1.6),(14.5,0.04,1.3),C("SignWhiteGlow","f4f8ff",0.3,emit=3.5))
    for i,(x,col) in enumerate(((-10,"d0181e"),(0,"1f6db0"),(10,"e8b81e"))):   # showroom cars on turntables
        cyl((x,1,0.35),3.0,0.1,C("Turntable","2a2c30",0.2,0.8),24); car(x,1,math.radians(25+i*20),col,0.4)
    for k in range(10): car(-16+k*3.6,FZ-11,math.radians(90),["d0181e","1a1a1a","f0f0ee","1f6db0","9aa0a6","e07a3a","2f8a4a","7a3a9e","e8b81e","c9ccd1"][k],0.1)
    box((0,FZ-11,0.06),(W+6,7,0.06),T_("Pavement","walk",(0.86,0.86,0.84)))
    for k in range(11): box((-18+k*3.6,FZ-11,0.1),(0.12,6,0.02),C("PaintWhite","f0f0ee",0.6))
    lot(0,FZ-20,W+16,10)
    cyl((-W/2-5,FZ-16,6),0.4,12,C("PoleDark","2a2c30",0.45,0.6),12)          # pylon sign
    box((-W/2-5,FZ-16,13),(2.2,1.0,6),RED,bev=0.08); box((-W/2-5,FZ-16.52,13.6),(1.8,0.04,3.6),C("SignWhiteGlow","f4f8ff",0.3,emit=3.5))
    box((-W/2-5,FZ-16.53,11),(1.8,0.04,0.6),CY)
    for k in range(6):
        x=-12+k*5; cyl((x,FZ-15,3),0.06,6,FR,6); box((x+0.6,FZ-15,5.4),(1.2,0.03,0.8),[RED,C("FlagBlue","1f6db0",0.5),C("FlagWhite","f0efe9",0.5)][k%3])
    for x in (-20,0,20): lightpole(x,FZ-24,9,1.8,1)
@reg("OT_Overpass_Freeway",(-30,-38,10),(0,0,4),24,(1150,780))
def overpass():
    CO=T_("Concrete","plaster",(0.8,0.8,0.78)); AS=C("Asphalt","35373b",0.85); W_=C("PaintWhite","f0f0ee",0.6); YL=C("Yellow","e8b81e",0.5)
    L,Wd,Hc=40,24,6.5
    box((0,0,Hc+0.3),(L,Wd,0.6),AS); box((0,0,Hc-0.5),(L,Wd+0.6,1.0),CO)                 # deck
    for y in (-8,-3,3,8): box((0,y,Hc-1.6),(L,1.0,1.4),CO)                                 # girders
    for x in (-12,12):                                                                      # pier bents
        box((x,0,Hc-2.6),(1.6,Wd-2,1.2),CO,bev=0.1)
        for y in (-8,0,8): cyl((x,y,(Hc-3.2)/2),0.8,Hc-3.2,CO,16)
    for s in (-1,1): jersey(-L/2,L/2,s*(Wd/2-0.4),Hc+0.6,CO)
    for y in (-3.6,3.6,-7.2,7.2): 
        for k in range(10): box((-18+k*4,y,Hc+0.61),(2.0,0.15,0.02),W_)
    for y in (-0.4,0.4): box((0,y,Hc+0.61),(L,0.15,0.02),YL)
    for x in (-18,0,18): lightpole(x,Wd/2-0.7,9,2.2,-1) if False else None
    for x in (-16,4): 
        cyl((x,Wd/2-0.6,Hc+5),0.15,9,C("PoleDark","2a2c30",0.45,0.6),10); box((x,Wd/2-1.8,Hc+9.4),(0.35,2.6,0.2),C("PoleDark","2a2c30",0.45,0.6)); box((x,Wd/2-2.6,Hc+9.27),(0.3,1.2,0.05),led())
    box((0,0,0.05),(L+20,Wd+16,0.1),T_("Pavement","walk",(0.86,0.86,0.84)))
@reg("OT_Bridge_Steel",(-40,-50,14),(0,0,6),24,(1150,780))
def bridge():
    ST=C("BridgeSteel","2f5a7a",0.4,0.7); CO=T_("Concrete","plaster",(0.8,0.8,0.78)); AS=C("Asphalt","35373b",0.85); W_=C("PaintWhite","f0f0ee",0.6)
    L,Wd,Hd=64,15,8
    box((0,0,Hd),(L,Wd,0.6),AS); box((0,0,Hd-0.6),(L,Wd+0.4,0.8),CO)
    for s in (-1,1):
        y=s*(Wd/2+0.3)
        n=24
        for i in range(n):                                  # arch made of segments
            a0=math.pi*i/n; a1=math.pi*(i+1)/n; R=L/2-2
            p0=(-math.cos(a0)*R, Hd+math.sin(a0)*14); p1=(-math.cos(a1)*R, Hd+math.sin(a1)*14)
            mx,mz=(p0[0]+p1[0])/2,(p0[1]+p1[1])/2; ln=math.hypot(p1[0]-p0[0],p1[1]-p0[1])
            box((mx,y,mz),(ln+0.1,0.8,1.0),ST,rot=(0,-math.atan2(p1[1]-p0[1],p1[0]-p0[0]),0))
        for k in range(1,12):
            x=-L/2+2+k*(L-4)/12; R=L/2-2; t=max(0,1-(x/R)**2); hz=math.sqrt(t)*14
            if hz>0.8: box((x,y,Hd+hz/2),(0.25,0.25,hz),ST)
        box((0,y,Hd+0.9),(L,0.3,1.0),ST)
    for k in range(8): box((-28+k*8,0,Hd+0.31),(4,0.15,0.02),W_)
    for x in (-L/2,L/2): box((x,0,Hd/2-1),(3,Wd+2,Hd),CO)
@reg("OT_TunnelPortal",(-26,-34,6),(0,0,4),24)
def tunnel():
    CO=T_("Concrete","plaster",(0.78,0.78,0.76)); AS=C("Asphalt","35373b",0.85); RK=T_("Rock","granite",(0.62,0.6,0.56)); W_=C("PaintWhite","f0f0ee",0.6)
    DK=C("TunnelDark","0d0e10",0.9); Wd,H=12,7
    zc=4.0; R=Wd/2; Hw=zc+R+2
    box((0,0.6,Hw/2),(Wd+12,1.2,Hw),CO,uv=2.0)                          # portal wall
    box((0,-0.02,zc/2),(Wd,0.1,zc),DK)                                   # opening rect
    for k in range(10):                                                  # opening arch (stacked strips)
        z0=k*R/10; z1=(k+1)*R/10; w=2*math.sqrt(max(R*R-z1*z1,0)); w0=2*math.sqrt(R*R-z0*z0)
        box((0,-0.02,zc+(z0+z1)/2),((w+w0)/2,0.1,z1-z0+0.02),DK)
    for k in range(13):
        a=math.pi*k/12; box((math.cos(a)*(R+0.4),-0.12,zc+math.sin(a)*(R+0.4)),(0.9,0.3,0.5),CO,rot=(0,-a,0))
    H=Hw-3
    box((0,0.4,H+3.4),(Wd+16,2.0,0.8),CO); box((0,-0.42,H+2.1),(7,0.05,1.0),C("TunnelSign","1f5a3a",0.4))
    for s in (-1,1): box((s*(Wd/2+10),-2,2.5),(8,0.8,5),CO,rot=(0,0,s*math.radians(25)))
    box((0,11,H/2),(Wd,20,H),DK)
    box((0,-6,0.05),(Wd,26,0.1),AS)
    for k in range(5): box((0,-14+k*5,0.11),(0.15,2.5,0.02),W_)
    for k in range(4): box((0,2+k*4,H-0.6),(1.2,0.3,0.12),C("TunnelLamp","ffe2a0",0.3,emit=5.0))
    box((0,11,H+1),(Wd+4,20,2),CO)   # tunnel roof (terrain covers it in game)
@reg("OT_Guardrail_10m",(-6,-8,3),(0,0,0.5),30,(900,600))
def gr():
    guardrail(-5,5,0); box((0,-1.5,0.03),(12,3,0.06),C("Asphalt","35373b",0.85))
@reg("OT_JerseyBarrier_10m",(-6,-8,3),(0,0,0.5),30,(900,600))
def jb():
    jersey(-5,5,0); box((0,-1.5,0.03),(12,3,0.06),C("Asphalt","35373b",0.85))
    for k in range(3): box((-3.3+k*3.3,-0.31,0.6),(0.6,0.02,0.15),C("Reflector","ffcc33",0.3,emit=1.5))
@reg("OT_SignGantry",(-22,-26,6),(0,0,5),24)
def gantry():
    ST=C("Galv","b9bec4",0.35,0.85); GR=C("HwyGreen","0f5a35",0.5); WH=C("SignWhiteGlow","f4f8ff",0.4,emit=0.8)
    Sp=28; H=7
    for s in (-1,1):
        for dy in (-0.6,0.6): box((s*Sp/2,dy,H/2),(0.35,0.35,H),ST)
        box((s*Sp/2,0,0.3),(1.6,2.2,0.6),T_("Concrete","plaster",(0.8,0.8,0.78)))
    for z in (H-0.3,H+1.3): 
        for dy in (-0.6,0.6): box((0,dy,z),(Sp,0.25,0.25),ST)
    for k in range(9): box((-Sp/2+1.5+k*3.2,-0.6,H+0.5),(0.12,0.12,1.6),ST,rot=(0,math.radians(30 if k%2 else -30),0))
    for i,x in enumerate((-8.5,0,8.5)):
        box((x,-0.9,H+0.5),(7.6,0.15,3.2),GR,bev=0.05); box((x,-0.99,H+0.5),(7.2,0.02,2.8),C("SignBorder","f0f0ee",0.5))
        box((x,-1.0,H+0.5),(7.0,0.02,2.6),GR); 
        for r in range(2): box((x-0.6,-1.02,H+0.9-r*0.9),(4.8-r*1.4,0.02,0.45),WH)
        box((x+2.6,-1.02,H-0.3),(1.0,0.02,0.6),C("ArrowW","f4f8ff",0.4,emit=0.8))
        box((x,-1.02,H-0.62),(7.6,0.06,0.12),C("SignLamp","fff4e0",0.3,emit=3.0))
    box((0,0,0.03),(Sp+6,10,0.06),C("Asphalt","35373b",0.85))
@reg("OT_ExitSign",(-8,-10,4),(0,0,3),28,(900,700))
def exitsign():
    ST=C("Galv","b9bec4",0.35,0.85); GR=C("HwyGreen","0f5a35",0.5)
    for x in (-1.6,1.6): box((x,0,2.6),(0.18,0.18,5.2),ST)
    box((0,-0.15,4.4),(4.6,0.12,2.2),GR,bev=0.04); box((0,-0.22,4.4),(4.3,0.02,1.9),C("SignBorder","f0f0ee",0.5)); box((0,-0.23,4.4),(4.1,0.02,1.7),GR)
    box((0,-0.24,4.75),(3.0,0.02,0.45),C("SignWhiteGlow","f4f8ff",0.4,emit=0.8)); box((-0.6,-0.24,4.05),(1.6,0.02,0.4),C("SignWhiteGlow","f4f8ff",0.4,emit=0.8))
    box((1.6,-0.15,5.75),(1.4,0.1,0.6),C("ExitYellow","e8b81e",0.5))
    box((0,0,0.03),(8,4,0.06),C("Grass","567d3a",0.9))
name=sys.argv[-2]; mode=sys.argv[-1]
f,cam,tgt,lens,res=BLD[name]; reset(); random.seed(hash(name)%1000); _cache.clear(); f()
if mode=="render": world_and_render(f"/home/claude/blender/r_{name}.png",cam,tgt,lens,res,20)
else: export(name,drop_y=-999)
