exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(7)
CO=pbr("Concrete","walk",(0.9,0.9,0.88)); CR=pbr("Corrugated","corr",(0.78,0.8,0.84),0.6,True); TL=pbr("Tile","tile",(0.95,0.95,0.95)); MT=pbr("Metal","metal",(0.6,0.6,0.62),0.8)
GL=flat("Glass","2a3844",0.05); FR=flat("Frame","1e1f22",0.4); WH=flat("White","eeeeec",0.4); RED=flat("Red","c4261d",0.4)
NEON=flat("Neon","ff7a1a",0.3,emit=4.0); PUMP=flat("Pump","d8d8d6",0.35); SCR=flat("Screen","141820",0.2); BLK=flat("Black","141414",0.6); YEL=flat("Yellow","e8b81e",0.5)
# pad
box((0,-4,0.1),(34,26,0.2),CO,uv=3.0)
# canopy
cy=-7; ch=5.6
box((0,cy,ch),(20,12,0.9),WH,bev=0.08)
box((0,cy-6.02,ch),(20.1,0.06,0.5),RED); box((0,cy+6.02,ch),(20.1,0.06,0.5),RED)
box((-10.02,cy,ch),(0.06,12.1,0.5),RED); box((10.02,cy,ch),(0.06,12.1,0.5),RED)
box((0,cy-6.06,ch-0.32),(20.1,0.04,0.06),NEON)
for x in (-5,5):
    for y in (cy-3,cy+3):
        box((x,y,ch/2),(0.6,0.6,ch),WH,bev=0.05)
        box((x,y,0.45),(0.9,0.9,0.7),RED,bev=0.05)
# pump islands
for x in (-5,5):
    box((x,cy,0.35),(1.6,7.4,0.3),CO,bev=0.05)
    for y in (cy-1.8,cy+1.8):
        box((x,y,1.3),(0.9,0.6,1.9),PUMP,bev=0.05); box((x,y,2.35),(1.0,0.7,0.25),RED,bev=0.03)
        box((x-0.46,y,1.6),(0.02,0.4,0.3),SCR); box((x+0.46,y,1.6),(0.02,0.4,0.3),SCR)
        cyl((x-0.5,y+0.2,1.1),0.05,0.5,BLK,8)
    for y in (cy-3.6,cy+3.6): cyl((x,y,0.85),0.12,1.0,YEL,10)
# store building
sx,sy=0,6.5; sw,sd,sh=16,8,4.6
box((sx,sy,sh/2+0.2),(sw,sd,sh),CR,uv=2.0)
box((sx,sy-sd/2-0.05,0.75),(sw,0.2,1.1),TL,bev=0.02)
box((sx-2,sy-sd/2-0.04,2.4),(11,0.06,2.2),GL)
for k in range(6): box((sx-7.5+k*2.2,sy-sd/2-0.08,2.4),(0.1,0.12,2.2),FR)
box((sx+5.5,sy-sd/2-0.04,1.6),(1.8,0.06,2.6),GL); box((sx+5.5,sy-sd/2-0.08,2.95),(2.0,0.12,0.1),FR)
box((sx,sy-sd/2-0.25,sh-0.2),(sw+0.4,0.5,1.0),WH,bev=0.04); box((sx,sy-sd/2-0.52,sh-0.2),(sw+0.4,0.06,0.3),RED)
box((sx,sy-sd/2-0.56,sh-0.55),(sw,0.04,0.06),NEON)
box((sx,sy,sh+0.4),(sw+0.3,sd+0.3,0.2),MT)
for x in (-4,3): box((x,sy+1,sh+0.9),(1.6,1.2,0.9),MT,bev=0.03)
box((sx-6.8,sy-sd/2-0.6,0.6),(1.4,0.8,1.0),WH,bev=0.05)  # ice chest
# sign pylon
px,py=13,-14
box((px,py,4),(0.5,0.5,8),MT); box((px+1.6,py,4),(0.5,0.5,8),MT)
box((px+0.8,py,8.6),(3.4,0.6,2.6),RED,bev=0.06); box((px+0.8,py-0.31,8.6),(3.0,0.04,2.2),WH)
for i in range(3): box((px+0.8,py-0.33,7.3-i*0.6),(2.8,0.05,0.45),BLK)
box((px+0.8,py,0.4),(2.8,1.0,0.8),CO,bev=0.05)
if "render" in sys.argv[-1]:
    world_and_render("/home/claude/blender/r_gas.png",(-24,-30,7),(1,-2,2.5),26,(1100,800))
else:
    export("OT_GasStation_A",drop_y=-99)
