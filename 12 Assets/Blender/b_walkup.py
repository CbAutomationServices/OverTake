exec(open("/home/claude/blender/lib.py").read())
import sys
reset(); random.seed(2)
BR=pbr("Brick","brick2",(0.95,0.85,0.8)); ST=pbr("Stone","trim",(0.95,0.9,0.82)); WD=pbr("Wood","wood",(0.45,0.3,0.22)); MT=pbr("Metal","metal",(0.5,0.5,0.5),0.8)
GL=flat("Glass","2c3640",0.06); FR=flat("Frame","eae6dc",0.4); REV=flat("Reveal","262626",0.9); IRON=flat("Iron","1c1c1c",0.5,0.6); DOOR=flat("Door","2e4a3a",0.4)
W,D=10.0,11.0; base=1.2; FH=3.2; NF=4; top=base+NF*FH; FZ=-D/2
box((0,0,top/2),(W,D,top),BR,uv=1.4)
box((0,FZ-0.05,base/2),(W+0.1,0.25,base),ST,bev=0.03,uv=1.2)
# bay column (floors 1-3 above ground)
bw=4.0; bd=0.9
for f in range(1,NF):
    z0=base+f*FH
    box((0,FZ-bd/2,z0+FH/2),(bw,bd,FH),BR,uv=1.4)
    for x,(ww) in [(-1.35,0.9),(0,1.1),(1.35,0.9)]:
        window(x,FZ-bd,z0+FH*0.55,ww,1.7,GL,FR,None,REV)
    box((0,FZ-bd-0.08,z0+0.1),(bw+0.2,0.25,0.2),ST)
box((0,FZ-bd/2,top+0.1),(bw+0.3,bd+0.3,0.3),ST,bev=0.03)
box((0,FZ-bd/2,base+FH+0.05),(bw+0.2,bd+0.2,0.15),ST)
for f in range(NF):
    z=base+f*FH+FH*0.55
    for x in (-3.9,3.9):
        if f==0 and x<0: continue
        window(x,FZ,z,1.1,1.8,GL,FR,ST,REV)
        box((x,FZ-0.08,z+1.05),(1.5,0.18,0.3),ST,bev=0.02)
# ground floor center: door + transom, stoop
window(0,FZ,base+FH*0.55+0.4,1.3,0.45,GL,FR,None,REV,mull=False)
box((0,FZ-0.05,base+1.2),(1.3,0.12,2.4),DOOR)
box((0,FZ-0.15,base+2.55),(2.0,0.3,0.25),ST,bev=0.02)
for i in range(5):
    box((0,FZ-0.45-i*0.35,base-0.12-i*0.24),(2.4,0.35+i*0.0,0.24*(i+1)),ST,bev=0.02)
for s in (-1,1):
    for k in range(6): box((s*1.25,FZ-0.4-k*0.33,base+0.45-k*0.22),(0.04,0.04,0.9),IRON)
    box((s*1.25,FZ-1.2,base+0.85-0.55),(0.05,1.9,0.05),IRON,rot=(math.atan2(1.2,1.8)*-1+0.0,0,0))
# basement windows
for x in (-3.9,):
    box((x,FZ-0.1,0.6),(1.1,0.1,0.5),GL); box((x,FZ-0.16,0.6),(1.2,0.04,0.6),IRON)
# cornice with brackets
box((0,0,top+0.25),(W+0.6,D+0.6,0.4),ST,bev=0.04)
for i in range(9): box((-W/2+0.6+i*1.1,FZ-0.25,top-0.15),(0.2,0.4,0.45),ST,bev=0.02)
box((0,0,top+0.6),(W,D,0.3),BR)
box((0,0,top+0.78),(W+0.1,D+0.1,0.08),ST)
box((2.5,2,top+1.2),(1.4,1.1,0.8),MT,bev=0.03)
if "render" in sys.argv[-1]:
    ground(30); world_and_render("/home/claude/blender/r_walkup.png",(-11,-21,3),(0,FZ,6.5),30,(800,1000))
else:
    export("OT_WalkUp_A")
