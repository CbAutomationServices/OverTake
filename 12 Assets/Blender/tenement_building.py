import bpy, bmesh, math, random
random.seed(4)
bpy.ops.wm.read_factory_settings(use_empty=True)
sc=bpy.context.scene
T="/home/claude/blender/tex/"
def pbr(name,key,tint=(1,1,1),scale=1.0,metal=0.0,rough_mul=1.0):
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree; N=nt.nodes; L=nt.links
    b=N["Principled BSDF"]
    def img(fn,non=False):
        n=N.new("ShaderNodeTexImage"); n.image=bpy.data.images.load(T+fn)
        if non: n.image.colorspace_settings.name="Non-Color"
        return n
    d=img(f"{key}_diff.jpg"); r=img(f"{key}_rough.jpg",True); no=img(f"{key}_nor.jpg",True)
    mix=N.new("ShaderNodeMix"); mix.data_type="RGBA"; mix.blend_type="MULTIPLY"; mix.inputs[0].default_value=1.0
    L.new(d.outputs[0],mix.inputs[6]); mix.inputs[7].default_value=(*tint,1)
    L.new(mix.outputs[2],b.inputs["Base Color"])
    rm=N.new("ShaderNodeMath"); rm.operation="MULTIPLY"; rm.inputs[1].default_value=rough_mul
    L.new(r.outputs[0],rm.inputs[0]); L.new(rm.outputs[0],b.inputs["Roughness"])
    nm=N.new("ShaderNodeNormalMap"); L.new(no.outputs[0],nm.inputs[1]); L.new(nm.outputs[0],b.inputs["Normal"])
    b.inputs["Metallic"].default_value=metal
    return m
def flat(name,col,rough=0.5,metal=0.0,trans=0.0):
    m=bpy.data.materials.new(name); m.use_nodes=True; b=m.node_tree.nodes["Principled BSDF"]
    b.inputs["Base Color"].default_value=(*col,1); b.inputs["Roughness"].default_value=rough; b.inputs["Metallic"].default_value=metal
    return m
BR=pbr("Brick","brick",(0.95,0.75,0.68)); ST=pbr("Stone","trim",(0.92,0.86,0.74)); MT=pbr("Metal","metal",(0.35,0.35,0.37),metal=0.8)
WD=pbr("Wood","wood",(0.6,0.45,0.33)); RF=pbr("Roof","roof",(0.6,0.6,0.6)); WK=pbr("Walk","walk",(0.8,0.8,0.78))
GL=flat("Glass",(0.04,0.06,0.08),0.05,0.0); FR=flat("Frame",(0.06,0.07,0.07),0.4); IRON=flat("Iron",(0.05,0.05,0.05),0.55,0.6)
AW1=flat("AwnA",(0.12,0.35,0.18),0.8); AW2=flat("AwnB",(0.85,0.85,0.8),0.8); BRASS=flat("Lamp",(0.9,0.75,0.4),0.3,0.9)
REV=flat("Reveal3",(0.02,0.02,0.02),0.9)
LIT=bpy.data.materials.new("Interior"); LIT.use_nodes=True; LIT.node_tree.nodes["Principled BSDF"].inputs["Base Color"].default_value=(0.6,0.45,0.3,1)
def uvbox(o,size=2.0):
    bpy.context.view_layer.objects.active=o; o.select_set(True)
    bpy.ops.object.transform_apply(scale=True)
    bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.uv.cube_project(cube_size=size); bpy.ops.object.mode_set(mode="OBJECT"); o.select_set(False)
def box(loc,size,m,bev=0.0,uv=2.0,rot=None):
    bpy.ops.mesh.primitive_cube_add(location=loc); o=bpy.context.object
    o.scale=(size[0]/2,size[1]/2,size[2]/2)
    if rot: o.rotation_euler=rot
    o.data.materials.append(m); uvbox(o,uv)
    if bev>0:
        md=o.modifiers.new("b","BEVEL"); md.width=bev; md.segments=2; md.limit_method="ANGLE"
    return o
def cyl(loc,r,h,m,verts=16,rot=None):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=h,location=loc); o=bpy.context.object
    if rot: o.rotation_euler=rot
    o.data.materials.append(m); uvbox(o,1.0); return o
W,D=13.0,10.0; GF=4.4; FH=3.3; NF=5; top=GF+NF*FH
FZ=-D/2  # front face y
# body
box((0,0,top/2),(W,D,top),BR,uv=1.6)
# rusticated stone base: horizontal courses
def course(x0,x1,z):
    if x1-x0>0.05: box(((x0+x1)/2,FZ-0.06,z),(x1-x0,0.25,0.5),ST,bev=0.04,uv=1.2)
for k in range(int(GF/0.55)):
    z=0.275+k*0.55
    if 0.6<z<3.95:
        course(-W/2-0.1,-5.5,z); course(2.3,3.2,z); course(4.8,W/2+0.1,z)
    else:
        course(-W/2-0.1,W/2+0.1,z)
box((-1.6,FZ+0.05,2.25),(7.8,0.2,3.4),flat("Reveal",(0.03,0.03,0.03),0.9))
box((4.0,FZ+0.05,1.6),(1.7,0.2,2.9),flat("Reveal2",(0.03,0.03,0.03),0.9))
# quoins at front corners
for s in (-1,1):
    for k in range(int((top-GF)/0.6)):
        z=GF+0.3+k*0.6; wq=0.9 if k%2==0 else 0.6
        box((s*(W/2-wq/2+0.02),FZ-0.05,z),(wq,0.2,0.52),ST,bev=0.03,uv=1.0)
# storefront
box((-1.6,FZ-0.12,2.1),(7.2,0.06,3.0),GL)            # big glass
box((-1.6,FZ-0.05,3.75),(7.8,0.3,0.35),FR,bev=0.03) # header
for i in range(5): box((-5.2+i*1.8,FZ-0.02,2.1),(0.12,0.2,3.0),FR,bev=0.02)
box((-1.6,FZ-0.04,1.0),(7.2,0.18,0.1),FR)
box((-1.6,FZ-0.1,0.3),(7.6,0.35,0.6),ST,bev=0.03)  # bulkhead
# interior hint

# striped awning
for i in range(12):
    m=AW1 if i%2==0 else AW2
    a=box((-5.2+i*0.6+0.3,FZ-0.95,3.55),(0.6,1.9,0.06),m,rot=(math.radians(-18),0,0))
box((-1.6,FZ-1.85,3.25),(7.2,0.05,0.3),AW1)
# door + steps + lamps
box((4.0,FZ-0.1,1.55),(1.4,0.1,2.7),WD,uv=1.0)
box((4.0,FZ-0.05,3.05),(1.9,0.3,0.4),ST,bev=0.04)
box((4.0,FZ-0.45,0.12),(2.2,0.8,0.24),ST,bev=0.03)
for s in (-1,1):
    cyl((4.0+s*1.25,FZ-0.25,2.5),0.12,0.45,BRASS,12)
# floor bands + windows w/ arched-look heads, keystones, sills
cols=[-4.6,-2.3,0.0,2.3,4.6]
for f in range(NF):
    zb=GF+f*FH
    box((0,FZ-0.04,zb+0.05),(W,0.15,0.18),ST,bev=0.02)
    for x in cols:
        wz=zb+1.55
        box((x,FZ-0.01,wz),(1.35,0.04,1.95),REV)
        box((x,FZ-0.05,wz),(1.15,0.04,1.75),GL)
        box((x,FZ-0.09,wz),(1.15,0.05,0.06),FR)
        for s_ in (-1,1): box((x+s_*0.6,FZ-0.1,wz),(0.1,0.1,1.85),FR)
        box((x,FZ-0.1,wz+0.93),(1.3,0.1,0.1),FR); box((x,FZ-0.1,wz-0.93),(1.3,0.1,0.1),FR)
        box((x,FZ-0.16,wz-1.05),(1.6,0.38,0.14),ST,bev=0.03)
        box((x,FZ-0.08,wz+1.15),(1.7,0.18,0.3),ST,bev=0.03)
        box((x,FZ-0.13,wz+1.17),(0.32,0.22,0.42),ST,bev=0.03)
        if random.random()<0.35 and f<NF-1:
            ac=box((x,FZ-0.35,wz-0.75),(0.85,0.55,0.55),MT,bev=0.03,uv=0.8)
# cornice with brackets + dentils
box((0,FZ*0+0,top+0.25),(W+0.7,D+0.7,0.35),ST,bev=0.05)
box((0,0,top+0.55),(W+0.9,D+0.9,0.22),ST,bev=0.05)
for i in range(13):
    box((-W/2+0.5+i*1.0,FZ-0.32,top-0.05),(0.22,0.45,0.5),ST,bev=0.03)
for i in range(40):
    box((-W/2+0.2+i*0.32,FZ-0.2,top+0.02),(0.14,0.2,0.14),ST)
# parapet
box((0,FZ+0.2,top+0.95),(W,0.35,0.6),BR,uv=1.6)
box((0,FZ+0.2,top+1.3),(W+0.15,0.5,0.12),ST,bev=0.03)
# roof slab + clutter
box((0,0,top+0.66),(W-0.4,D-0.4,0.05),RF)
box((3.5,2,top+1.3),(2.4,1.8,1.2),MT,bev=0.05,uv=1.0)
for k in range(3): cyl((-4.5+k*0.6,3.5,top+1.2),0.12,1.1,MT,10)
# water tower
tx,ty,tz=-2.5,1.5,top+0.7
for sx in (-1,1):
    for sy in (-1,1):
        cyl((tx+sx*0.9,ty+sy*0.9,tz+1.0),0.08,2.0,IRON,8)
box((tx,ty,tz+2.05),(2.4,2.4,0.15),WD,uv=1.0)
bpy.ops.mesh.primitive_cylinder_add(vertices=24,radius=1.25,depth=2.6,location=(tx,ty,tz+3.45)); t=bpy.context.object; t.data.materials.append(WD); uvbox(t,1.0)
for z in (0.4,1.3,2.2): cyl((tx,ty,tz+2.1+z),1.28,0.07,IRON,24)
bpy.ops.mesh.primitive_cone_add(vertices=24,radius1=1.45,depth=1.2,location=(tx,ty,tz+5.35)); c=bpy.context.object; c.data.materials.append(RF); uvbox(c,1.0)
# fire escape (floors 1-4) with ladder
fx=W/2-2.6
for f in range(1,NF):
    z=GF+f*FH-0.05
    box((fx,FZ-0.75,z),(3.4,1.4,0.06),IRON)
    box((fx,FZ-1.43,z+0.95),(3.4,0.05,0.05),IRON); box((fx,FZ-1.43,z+0.45),(3.4,0.04,0.04),IRON)
    for k in range(9): box((fx-1.6+k*0.4,FZ-1.43,z+0.48),(0.035,0.035,0.95),IRON)
    if f<NF-1:
        st=box((fx-0.6,FZ-0.75,z+FH/2),(0.7,0.05,math.hypot(FH,2.0)),IRON,rot=(0,math.atan2(2.0,FH),0))
# sidewalk + curb + street
box((0,FZ-2.5,0.06),(W+8,5,0.12),WK,uv=2.5)
box((0,FZ-5.05,0.08),(W+8,0.3,0.16),ST,bev=0.03)
box((0,FZ-12,-0.01),(W+30,14,0.02),flat("Asphalt",(0.05,0.05,0.055),0.85))
# world + camera
w=bpy.data.worlds.new("W"); sc.world=w; w.use_nodes=True; N=w.node_tree.nodes
env=N.new("ShaderNodeTexEnvironment"); env.image=bpy.data.images.load(T+"sky.hdr")
w.node_tree.links.new(env.outputs[0],N["Background"].inputs[0]); N["Background"].inputs[1].default_value=1.0
bpy.ops.object.light_add(type="SUN"); s=bpy.context.object; s.data.energy=3.5; s.data.color=(1,0.85,0.65); s.rotation_euler=(math.radians(62),0,math.radians(-35)); s.data.angle=math.radians(2)
bpy.ops.object.camera_add(location=(-15,-27,3.5)); cam=bpy.context.object
cam.data.lens=28
d=bpy.data.objects.new("tgt",None); sc.collection.objects.link(d); d.location=(0,FZ,11.5)
cs=cam.constraints.new("TRACK_TO"); cs.target=d; cs.track_axis="TRACK_NEGATIVE_Z"; cs.up_axis="UP_Y"; sc.camera=cam
sc.render.engine="CYCLES"; sc.cycles.samples=48; sc.cycles.use_denoising=True
sc.view_settings.view_transform="AgX"; sc.view_settings.look="AgX - Medium High Contrast"
sc.render.resolution_x=1000; sc.render.resolution_y=1250; sc.render.filepath="/home/claude/blender/tenement.png"
objs=[o for o in bpy.data.objects if o.type=="MESH"]
dg=bpy.context.evaluated_depsgraph_get()
tris=sum(sum(len(p.vertices)-2 for p in o.evaluated_get(dg).data.polygons) for o in objs)
print("TRIS",tris,"OBJS",len(objs))
bpy.ops.render.render(write_still=True)
bpy.ops.wm.save_as_mainfile(filepath="/home/claude/blender/tenement.blend")
