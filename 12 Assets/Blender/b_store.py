exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(5)
BR=pbr("Brick","brick",(0.9,0.72,0.62)); ST=pbr("Stone","trim",(0.92,0.88,0.8)); CO=pbr("Concrete","conc",(0.9,0.9,0.88)); MT=pbr("Metal","metal",(0.5,0.5,0.5),0.8)
GL=flat("Glass","26323c",0.05); FR=flat("Frame","202224",0.4); REV=flat("Reveal","262626",0.9)
signs=[flat("SignA","b8322a",0.5,emit=0.0),flat("SignB","1f4e8c",0.5),flat("SignC","e0a21e",0.5)]
awn=[flat("AwnRed","9e2a24",0.8),flat("AwnBlue","2a4f7e",0.8),flat("AwnGreen","2f6b45",0.8)]
W,D=24.0,12.0; GF=4.6; F2=3.4; top=GF+F2; FZ=-D/2
box((0,0,top/2),(W,D,top),BR,uv=1.6)
for i in range(3):
    cx=-8+i*8
    # storefront glass with mullions + bulkhead
    box((cx,FZ-0.04,0.35),(6.6,0.2,0.7),ST,bev=0.03)
    box((cx,FZ-0.03,2.05),(6.6,0.06,2.7),GL)
    for k in range(4): box((cx-3.3+k*2.2,FZ-0.08,2.05),(0.1,0.12,2.7),FR)
    box((cx,FZ-0.08,3.42),(6.8,0.14,0.12),FR); box((cx,FZ-0.08,0.72),(6.8,0.14,0.08),FR)
    # recessed door
    box((cx+2.2,FZ-0.02,1.45),(1.2,0.1,2.5),GL)
    # sign band
    box((cx,FZ-0.12,3.95),(6.8,0.2,0.75),signs[i])
    box((cx,FZ-0.18,3.95),(7.0,0.06,0.85),FR)
    # awning (sloped)
    box((cx,FZ-0.75,3.3),(6.6,1.5,0.08),awn[i],rot=(math.radians(-20),0,0))
    box((cx,FZ-1.45,3.0),(6.6,0.05,0.35),awn[i])
    # upstairs windows
    for k in (-2.3,0,2.3):
        window(cx+k,FZ,GF+F2*0.5,1.2,1.7,GL,FR,ST,REV)
        box((cx+k,FZ-0.08,GF+F2*0.5+1.0),(1.6,0.18,0.25),ST)
# pilasters
for x in (-12,-4,4,12):
    box((x+(0.3 if x==-12 else -0.3 if x==12 else 0),FZ-0.1,top/2),(0.7,0.35,top),BR,uv=1.6)
    box((x+(0.3 if x==-12 else -0.3 if x==12 else 0),FZ-0.15,top+0.05),(0.9,0.45,0.25),ST)
# stepped parapet + cap
box((0,FZ+0.15,top+0.5),(W,0.3,1.0),BR,uv=1.6); box((0,FZ+0.15,top+1.05),(W+0.2,0.45,0.12),ST)
box((0,FZ+0.15,top+1.4),(8,0.3,0.8),BR,uv=1.6); box((0,FZ+0.15,top+1.85),(8.3,0.45,0.12),ST)
box((0,FZ-0.05,GF+0.05),(W,0.25,0.2),ST)
for x in (-6,6): box((x,2,top+0.6),(1.6,1.2,1.0),MT,bev=0.03)
if "render" in sys.argv[-1]:
    ground(40); world_and_render("/home/claude/blender/r_store.png",(-16,-20,2.5),(0,FZ,3.5),28,(1100,800))
else:
    export("OT_Storefront_A")
