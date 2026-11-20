import bpy, math, random, os
from PIL import Image
T="/home/claude/blender/tex/"; B="/home/claude/blender/baked/"
def reset():
    bpy.ops.wm.read_factory_settings(use_empty=True)
def tinted(key,tint,gray=False):
    out=f"{B}{key}_{'g' if gray else ''}{''.join('%02x'%int(c*255) for c in tint)}_diff.jpg"
    if not os.path.exists(out):
        im=Image.open(f"{T}{key}_diff.jpg").convert("RGB")
        if gray: im=im.convert("L").convert("RGB")
        if im.width>1024: im=im.resize((1024,1024))
        r,g,b=im.split(); im=Image.merge("RGB",(r.point(lambda v:v*tint[0]),g.point(lambda v:v*tint[1]),b.point(lambda v:v*tint[2])))
        im.save(out,quality=88)
    return out
def pbr(name,key,tint=(1,1,1),metal=0.0,gray=False):
    m=bpy.data.materials.new(name); m.use_nodes=True; nt=m.node_tree; N=nt.nodes; L=nt.links; b=N["Principled BSDF"]
    def img(fn,non=False):
        n=N.new("ShaderNodeTexImage"); n.image=bpy.data.images.load(fn)
        if non: n.image.colorspace_settings.name="Non-Color"
        return n
    d=img(tinted(key,tint,gray)); L.new(d.outputs[0],b.inputs["Base Color"])
    r=img(f"{T}{key}_rough.jpg",True); L.new(r.outputs[0],b.inputs["Roughness"])
    no=img(f"{T}{key}_nor.jpg",True); nm=N.new("ShaderNodeNormalMap"); L.new(no.outputs[0],nm.inputs[1]); L.new(nm.outputs[0],b.inputs["Normal"])
    b.inputs["Metallic"].default_value=metal; return m
def srgb(c): return c/255
def flat(name,hexc,rough=0.5,metal=0.0,emit=0.0):
    # name carries the sRGB hex so Roblox import can restore the color: Name__RRGGBB
    m=bpy.data.materials.new(f"{name}__{hexc}"); m.use_nodes=True; b=m.node_tree.nodes["Principled BSDF"]
    r,g,bb=[int(hexc[i:i+2],16)/255 for i in (0,2,4)]
    lin=lambda c: c/12.92 if c<=0.04045 else ((c+0.055)/1.055)**2.4
    col=(lin(r),lin(g),lin(bb),1); b.inputs["Base Color"].default_value=col
    b.inputs["Roughness"].default_value=rough; b.inputs["Metallic"].default_value=metal
    if emit: b.inputs["Emission Color"].default_value=col; b.inputs["Emission Strength"].default_value=emit
    return m
def uvbox(o,size=2.0):
    bpy.context.view_layer.objects.active=o; o.select_set(True)
    bpy.ops.object.transform_apply(scale=True,rotation=False)
    bpy.ops.object.mode_set(mode="EDIT"); bpy.ops.mesh.select_all(action="SELECT")
    bpy.ops.uv.cube_project(cube_size=size); bpy.ops.object.mode_set(mode="OBJECT"); o.select_set(False)
def box(loc,size,m,bev=0.0,uv=2.0,rot=None):
    bpy.ops.mesh.primitive_cube_add(location=loc); o=bpy.context.object
    o.scale=(size[0]/2,size[1]/2,size[2]/2)
    if rot: o.rotation_euler=rot
    o.data.materials.append(m); uvbox(o,uv)
    if bev>0: md=o.modifiers.new("b","BEVEL"); md.width=bev; md.segments=1; md.limit_method="ANGLE"
    return o
def cyl(loc,r,h,m,verts=12,rot=None):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=h,location=loc); o=bpy.context.object
    if rot: o.rotation_euler=rot
    o.data.materials.append(m); uvbox(o,1.0); return o
def window(x,y,z,w,h,GL,FR,SILL,REV,face=-1,mull=True,axis="x"):
    """window on a wall facing -Y (face=-1) at plane y"""
    dy=face
    def B(cx,cz,sx,sz,dep,m,off): 
        return box((cx,y+dy*off,cz),(sx,dep,sz),m) if axis=="x" else box((y+dy*off,cx,cz),(dep,sx,sz),m)
    B(x,z,w+0.2,h+0.2,0.04,REV,0.01); B(x,z,w,h,0.04,GL,0.05)
    B(x,z+h/2,w+0.14,0.1,0.1,FR,0.1); B(x,z-h/2,w+0.14,0.1,0.1,FR,0.1)
    B(x-w/2,z,0.1,h,0.1,FR,0.1); B(x+w/2,z,0.1,h,0.1,FR,0.1)
    if mull: B(x,z+h*0.1,w,0.06,0.06,FR,0.09)
    if SILL: B(x,z-h/2-0.1,w+0.4,0.14,0.32,SILL,0.15)
def world_and_render(path,cam_loc,target,lens=30,res=(900,1000),samples=32,sun_rot=(62,0,-35)):
    sc=bpy.context.scene
    w=bpy.data.worlds.new("W"); sc.world=w; w.use_nodes=True; N=w.node_tree.nodes
    env=N.new("ShaderNodeTexEnvironment"); env.image=bpy.data.images.load(T+"sky.hdr")
    w.node_tree.links.new(env.outputs[0],N["Background"].inputs[0])
    bpy.ops.object.light_add(type="SUN"); s=bpy.context.object; s.data.energy=3.5; s.data.color=(1,0.86,0.68); s.rotation_euler=tuple(math.radians(a) for a in sun_rot); s.data.angle=math.radians(2)
    bpy.ops.object.camera_add(location=cam_loc); cam=bpy.context.object; cam.data.lens=lens
    d=bpy.data.objects.new("tgt",None); sc.collection.objects.link(d); d.location=target
    cs=cam.constraints.new("TRACK_TO"); cs.target=d; cs.track_axis="TRACK_NEGATIVE_Z"; cs.up_axis="UP_Y"; sc.camera=cam
    sc.render.engine="CYCLES"; sc.cycles.samples=samples; sc.cycles.use_denoising=True
    sc.view_settings.view_transform="AgX"; sc.view_settings.look="AgX - Medium High Contrast"
    sc.render.resolution_x,sc.render.resolution_y=res; sc.render.filepath=path
    bpy.ops.render.render(write_still=True)
def ground(W=40,D=40,y0=-6):
    WK=pbr("Walk","walk",(0.85,0.85,0.83)); box((0,y0-2.5,0.06),(W,5,0.12),WK,uv=2.5)
    ST=flat("Curb","9a968c",0.8); box((0,y0-5.05,0.08),(W,0.3,0.16),ST)
    AS=flat("Asphalt","2a2a2c",0.9); box((0,y0-14,-0.01),(W+40,18,0.02),AS)
def export(name,drop_y=-8.0):
    import mathutils
    for o in list(bpy.data.objects):
        if o.type!="MESH": bpy.data.objects.remove(o,do_unlink=True); continue
        ys=[(o.matrix_world@v.co).y for v in o.data.vertices]
        if min(ys)<drop_y or o.data.materials[0].name.startswith(("Walk","Curb","Asphalt")): bpy.data.objects.remove(o,do_unlink=True)
    groups={}
    for o in bpy.data.objects:
        bpy.context.view_layer.objects.active=o
        for md in list(o.modifiers): bpy.ops.object.modifier_apply(modifier=md.name)
        groups.setdefault(o.data.materials[0].name,[]).append(o)
    stats=[]
    for mat,objs in groups.items():
        bpy.ops.object.select_all(action="DESELECT")
        for o in objs: o.select_set(True)
        bpy.context.view_layer.objects.active=objs[0]
        if len(objs)>1: bpy.ops.object.join()
        j=bpy.context.view_layer.objects.active; j.name=f"{name}_{mat}"; j.data.name=j.name
        t=sum(len(p.vertices)-2 for p in j.data.polygons); stats.append((j.name,t))
    mn=mathutils.Vector((1e9,)*3); mx=-mn
    for o in bpy.data.objects:
        for v in o.data.vertices:
            w=o.matrix_world@v.co; mn=mathutils.Vector(map(min,mn,w)); mx=mathutils.Vector(map(max,mx,w))
    for im in bpy.data.images:
        if im.source=="FILE":
            if im.size[0]>1024: im.scale(1024,1024)
            im.pack()
    bpy.ops.export_scene.gltf(filepath=f"/mnt/user-data/outputs/{name}.glb",export_format="GLB",export_image_format="JPEG",export_jpeg_quality=85,export_apply=True,export_yup=True)
    tot=sum(t for _,t in stats); big=max(t for _,t in stats)
    print("EXPORT",name,"tris",tot,"biggest",big,"meshes",len(stats),"size_m",tuple(round(x,1) for x in (mx-mn)))
def prism(loc,w,h,dep,m,rot_z=0.0,uv=1.5):
    """triangular gable/pediment: base width w, height h, depth dep (along y), base at loc z"""
    import bmesh
    me=bpy.data.meshes.new("prism"); bm=bmesh.new(); x,y,z=loc
    pts=[(-w/2,-dep/2,0),(w/2,-dep/2,0),(0,-dep/2,h),(-w/2,dep/2,0),(w/2,dep/2,0),(0,dep/2,h)]
    v=[bm.verts.new(p) for p in pts]
    for f in ((0,1,2),(5,4,3),(0,3,4,1),(1,4,5,2),(2,5,3,0)): bm.faces.new([v[i] for i in f])
    bm.to_mesh(me); bm.free(); o=bpy.data.objects.new("prism",me); bpy.context.scene.collection.objects.link(o)
    o.location=loc; o.rotation_euler=(0,0,rot_z); o.data.materials.append(m); uvbox(o,uv); return o
def halfcyl(loc,r,dep,m,verts=16,axis="y"):
    bpy.ops.mesh.primitive_cylinder_add(vertices=verts,radius=r,depth=dep,location=loc,rotation=(math.radians(90),0,0) if axis=="y" else (0,math.radians(90),0))
    o=bpy.context.object; o.data.materials.append(m); uvbox(o,1.0); return o
