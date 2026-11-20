exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(11)
CO=pbr("Concrete","walk",(0.92,0.92,0.9)); ST=pbr("Stone","trim",(0.9,0.86,0.78)); BR=pbr("Brick","brick",(0.85,0.7,0.62)); WD=pbr("WoodSlat","wood",(1.0,0.72,0.48))
CR=pbr("Corrugated","corr",(0.5,0.52,0.56),0.6,True); MT=pbr("Metal","metal",(0.6,0.6,0.62),0.8)
CHAR=flat("Charcoal","26282c",0.45); ORG=flat("Orange","f26b1d",0.4); GLOW=flat("GlowOrange","ff7a1a",0.3,emit=5.0); LED=flat("LEDPanel","fff4e0",0.3,emit=6.0)
GL=flat("Glass","22303a",0.05); FR=flat("Frame","18191c",0.4); PUMP=flat("PumpBody","e9e9e6",0.35); SCR=flat("Screen","35c8ff",0.2,emit=2.5)
BLK=flat("Black","121212",0.6); YEL=flat("Yellow","e8b81e",0.5); WHT=flat("PaintWhite","f0f0ee",0.6); GRASS=flat("Grass","4f7a3a",0.9)
BLUE=flat("GlowBlue","2f8cff",0.3,emit=4.0); RED=flat("Red","c4261d",0.45); DIG=flat("PriceDigits","ffb020",0.3,emit=4.0)
# pavement + islands + stripes
box((0,-3,0.08),(46,34,0.16),CO,uv=3.0)
for x in (-10,10):
    box((x,-18.5,0.25),(10,2,0.3),ST,bev=0.05); box((x,-18.5,0.42),(9.4,1.5,0.06),GRASS)
for i in range(7): box((-9+i*3,9.6,0.17),(0.15,5,0.02),WHT)
# canopy: wedge fascia
cy=-8; ch=6.0
box((0,cy,ch),(26,14,0.6),CHAR,bev=0.06)
box((0,cy-7.1,ch+0.35),(26.4,0.3,1.5),CHAR,bev=0.05)            # tall front fascia
box((0,cy-7.28,ch+0.55),(26.4,0.06,0.35),ORG)                    # orange band
box((0,cy-7.3,ch-0.32),(26.4,0.05,0.08),GLOW)                   # lower glow strip
for s in (-1,1): box((s*13.15,cy,ch+0.2),(0.3,14,1.0),CHAR); box((s*13.32,cy,ch+0.25),(0.05,14,0.25),ORG)
box((0,cy+7.1,ch+0.15),(26.4,0.3,1.0),CHAR)
for x in (-9,-3,3,9):
    for y in (cy-3.5,cy+3.5): box((x,y,ch-0.31),(2.4,1.6,0.04),LED)
# columns: stone base + charcoal upper
for x in (-6,6):
    for y in (cy-4,cy+4):
        box((x,y,1.2),(1.1,1.1,2.4),ST,bev=0.04,uv=1.0); box((x,y,2.45),(1.25,1.25,0.15),CHAR)
        box((x,y,4.2),(0.8,0.8,3.5),CHAR); box((x,y-0.41,4.2),(0.08,0.02,3.2),GLOW)
# pump islands (3) with modern dispensers
for x in (-9,0,9):
    box((x,cy,0.3),(1.8,8.6,0.28),ST,bev=0.05)
    for y in (cy-2.0,cy+2.0):
        box((x,y,1.45),(0.95,0.7,2.1),PUMP,bev=0.06)
        box((x,y,2.65),(1.05,0.8,0.35),CHAR,bev=0.04); box((x,y-0.41,2.65),(0.9,0.02,0.18),GLOW)
        for s in (-1,1): box((x+s*0.49,y,1.9),(0.02,0.45,0.35),SCR)
        box((x,y-0.36,0.9),(0.7,0.02,0.4),ORG)
        cyl((x-0.55,y+0.15,1.2),0.05,0.6,BLK,8); cyl((x+0.55,y+0.15,1.2),0.05,0.6,BLK,8)
    for y in (cy-4.3,cy+4.3): cyl((x,y,0.9),0.14,1.1,YEL,12)
    box((x,cy,0.95),(0.5,0.5,0.9),BLK)          # trash/squeegee stand
# store
sx,sy=-3,8.5; sw,sd,sh=22,9,5.0
box((sx,sy,sh/2+0.16),(sw,sd,sh),BR,uv=1.6)
fz=sy-sd/2
box((sx-1,fz-0.04,2.5),(13,0.06,3.4),GL)
for k in range(7): box((sx-7.5+k*2.16,fz-0.08,2.5),(0.1,0.12,3.4),FR)
box((sx-1,fz-0.08,4.25),(13.2,0.14,0.12),FR); box((sx-1,fz-0.08,0.78),(13.2,0.14,0.12),FR)
box((sx+3,fz-0.03,1.7),(2.2,0.06,2.7),GL); box((sx+3,fz-0.08,3.1),(2.4,0.14,0.1),FR)
for k in range(16): box((sx+6.5+k*0.28-1.1,fz-0.1,2.6),(0.18,0.12,4.6),WD)    # wood slat panel right
box((sx-9.6,fz-0.1,2.6),(2.4,0.2,4.6),ST,bev=0.03,uv=1.0)                     # stone panel left
box((sx,fz-1.6,sh+0.1),(sw+1.0,3.4,0.35),CHAR,bev=0.04)                       # cantilever overhang
box((sx,fz-3.32,sh+0.1),(sw+1.0,0.06,0.2),ORG); box((sx,fz-3.34,sh-0.1),(sw+1.0,0.04,0.06),GLOW)
for x in (-6,0,6): box((sx+x,fz-1.6,sh-0.06),(1.6,1.0,0.04),LED)
box((sx-1,sy,sh+1.2),(9,0.5,1.6),CHAR,bev=0.04); box((sx-1,sy-0.27,sh+1.2),(8.4,0.04,1.1),ORG)   # rooftop sign box
box((sx,sy,sh+0.35),(sw+0.3,sd+0.3,0.2),MT)
# store props
box((sx-8,fz-0.6,0.95),(1.8,0.9,1.6),WHT,bev=0.05); box((sx-8,fz-1.06,1.3),(1.5,0.02,0.6),BLUE)      # ice merchandiser
box((sx-5.6,fz-0.5,1.1),(1.0,0.8,1.9),RED,bev=0.04); box((sx-5.6,fz-0.91,1.3),(0.7,0.02,1.0),LED)   # vending machines
box((sx-4.4,fz-0.5,1.1),(1.0,0.8,1.9),flat("VendBlue","1f4e8c",0.4),bev=0.04); box((sx-4.4,fz-0.91,1.3),(0.7,0.02,1.0),LED)
box((sx+9.5,fz-0.7,1.0),(1.6,0.8,1.8),flat("Cage","8a8f96",0.5,0.7),bev=0.03)                    # propane cage
for x in (sx+1.2,sx+5): cyl((x,fz-0.6,0.6),0.3,1.0,CHAR,12)                                         # trash cans
box((sx+7.5,fz-0.8,0.5),(2.0,0.5,0.1),WD); 
# car wash bay attached on the right
cx=sx+sw/2+4.5
box((cx,sy,3.0),(9,sd,6.0),CR,uv=2.0); box((cx,fz-0.04,2.4),(5.6,0.08,4.8),flat("WashDoor","2c3138",0.4,0.5))
box((cx,fz-0.1,5.2),(6.4,0.14,0.25),BLUE); box((cx,sy,6.1),(9.3,sd+0.3,0.2),MT)
box((cx,fz-0.12,5.65),(4,0.1,0.6),CHAR)
# air/water station + light poles
box((-18,2,0.9),(0.7,0.6,1.6),RED,bev=0.05); box((-18,1.69,1.3),(0.5,0.02,0.3),SCR)
for (x,y) in ((-21,-19),(21,-19)):
    cyl((x,y,4.5),0.15,9,CHAR,10); box((x+0.8,y,9.0),(1.8,0.4,0.2),CHAR); box((x+1.2,y,8.88),(1.0,0.3,0.04),LED)
# monument pylon with price boards
px,py=17,-18
box((px,py,0.8),(3.6,1.4,1.6),ST,bev=0.05,uv=1.0)
box((px,py,6.0),(3.0,0.9,9.0),CHAR,bev=0.06)
box((px,py-0.47,9.4),(2.6,0.06,1.8),ORG); box((px,py-0.5,9.4),(2.2,0.04,1.1),LED)
for i in range(3):
    box((px,py-0.47,7.4-i*1.2),(2.6,0.05,0.9),BLK); box((px+0.45,py-0.5,7.4-i*1.2),(1.2,0.04,0.55),DIG)
    box((px-0.8,py-0.5,7.4-i*1.2),(0.6,0.04,0.4),[ORG,flat("Green","2fa45a",0.4),WHT][i])
box((px-1.52,py-0.47,6),(0.06,0.06,9.0),GLOW); box((px+1.52,py-0.47,6),(0.06,0.06,9.0),GLOW)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_gas2.png",(-30,-36,8),(0,-2,3),24,(1200,800),40)
    for o in [o for o in bpy.data.objects if o.type=="CAMERA"]: o.location=(14,-30,3)
    bpy.data.objects["tgt"].location=(-2,-6,3.5); bpy.context.scene.render.filepath="/home/claude/blender/r_gas2b.png"; bpy.ops.render.render(write_still=True)
else:
    export("OT_GasStation_B",drop_y=-99)
