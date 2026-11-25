-- HorizonValleyGen: Map v3 blockout (terrain + road network). Layout from "Map v3 - 3 Horizon Valley.png".
-- px->studs: X=(px-550)*S, Z=(py-581)*S
local G={}
local S=10.9
local function P(px,py) return Vector2.new((px-550)*S,(py-581)*S) end
local function PL(t) local o={} for i=1,#t,2 do o[#o+1]=P(t[i],t[i+1]) end return o end
G.SEA=0; G.LAKE=14; G.LIFT=36

-- ROADS: {name, kind, width, points, closed, flat}
G.ROADS={
 {"Freeway_NS","Freeway",80,PL{550,216, 545,310, 522,430, 503,560, 486,690, 465,800, 438,880}},
 {"Freeway_EW","Freeway",80,PL{438,880, 600,850, 800,832, 950,860, 1035,900}},
 {"Highway_Loop","Highway",48,PL{330,718, 255,640, 205,560, 196,480, 220,385, 290,300, 400,242, 550,216, 700,236, 805,272, 892,330, 942,402, 966,482, 950,545, 870,612, 782,690, 722,762, 662,770, 562,742, 480,716, 400,708},true},
 {"Highway_West","Highway",44,PL{70,318, 120,400, 160,455, 196,480}},
 {"Highway_East","Highway",44,PL{966,482, 1030,492, 1068,540, 1084,620, 1080,700, 1066,790, 1050,858, 1035,900}},
 {"Touge_NW","Touge",26,PL{130,88, 200,115, 255,150, 262,190, 215,235, 200,265, 240,310, 256,341}},
 {"Touge_N","Touge",26,PL{812,40, 835,95, 830,135, 780,165, 752,200, 740,235, 724,246}},
 {"Touge_NE","Touge",26,PL{1035,110, 975,130, 935,165, 935,200, 975,225, 990,262, 955,300, 892,330}},
 {"Dirt_Forest","Dirt",24,PL{742,520, 790,483, 822,490, 840,560, 838,610, 805,640, 762,628, 735,575},true},
 {"Dirt_West","Dirt",22,PL{65,550, 120,528, 152,528, 140,580, 112,636}},
 {"Touge_Summit","Touge",26,PL{812,40, 860,52, 930,62, 990,82, 1035,110}},
 {"Touge_West","Touge",26,PL{130,88, 88,118, 52,170, 35,235, 48,290, 70,318}},
 {"Speedway_Access","Avenue",34,PL{637,572, 600,575, 560,574, 505,570}},
 {"Festival_Access","Avenue",30,PL{514,492, 545,492, 572,490}},
 {"City_Coastal_Blvd","Avenue",40,PL{255,640, 205,705, 160,772, 250,850, 330,955, 380,1060}},
}
-- City grid
G.CITY_POLY=PL{160,770, 330,705, 470,690, 615,790, 612,872, 780,858, 792,1060, 330,1060, 270,960}
G.CITY_STEP=440
-- Venues
G.SPEEDWAY={c=P(682,572),rx=490,rz=305,width=54}
G.DRAG={a=P(615,995),b=P(785,995),width=70}
G.POI={Garage=P(373,857),PoliceHQ=P(286,835),Dealer=P(550,769),Festival=P(528,461),Speedway=P(682,572),OffRoad=P(792,550),DragStrip=P(700,995),SummitTouge=P(880,110),Lakeside=P(572,262),Farmville=P(486,515),PineRidge=P(200,480),Hillcrest=P(880,520)}
G.TOWNS={{P(575,262),330},{P(486,520),330},{P(200,485),300},{P(880,525),320}}
-- Natural features
G.COAST=PL{-40,660, 0,672, 70,700, 150,768, 220,840, 270,955, 330,1060, 385,1140}
G.LAKE_C=P(708,385); G.LAKE_R=Vector2.new(88*S,80*S)
G.MOUNTS={{P(170,200),190*S,430},{P(880,130),190*S,470},{P(985,720),150*S,380},{P(-60,40),200*S,300},{P(1120,40),200*S,320}}
G.FORESTS={{P(110,470),170*S},{P(785,560),110*S},{P(300,370),80*S},{P(900,690),120*S}}
G.VALLEY=PL{300,440, 700,440, 700,690, 300,690}

local noise=math.noise
local function sstep(t) t=math.clamp(t,0,1) return t*t*(3-2*t) end
local function segDist(p,a,b) local ab=b-a; local l2=ab:Dot(ab); local t=l2>0 and math.clamp((p-a):Dot(ab)/l2,0,1) or 0; local q=a+ab*t; return (p-q).Magnitude,t end
local function inPoly(p,poly) local c=false; local j=#poly
 for i=1,#poly do local a,b=poly[i],poly[j]
  if ((a.Y>p.Y)~=(b.Y>p.Y)) and (p.X<(b.X-a.X)*(p.Y-a.Y)/(b.Y-a.Y)+a.X) then c=not c end; j=i end
 return c end
local function polyEdgeDist(p,poly) local d=1e9; for i=1,#poly do local a=poly[i]; local b=poly[i%#poly+1]; d=math.min(d,(segDist(p,a,b))) end return d end
-- signed coast distance: + inland, - ocean (ocean is to the left/bottom of the coast polyline direction)
local function coastSigned(p)
 local best,bi,bt=1e9,1,0
 for i=1,#G.COAST-1 do local d,t=segDist(p,G.COAST[i],G.COAST[i+1]); if d<best then best,bi,bt=d,i,t end end
 local a,b=G.COAST[bi],G.COAST[bi+1]; local dir=b-a; local cross=dir.X*(p.Y-a.Y)-dir.Y*(p.X-a.X)
 return cross<0 and best or -best  -- inland is to the right side going down-coast
end
G.coastSigned=coastSigned

-- mountain massifs: a main peak + satellite peaks, radius wobbles with angle
G.MASSIF={}
for mi,m in G.MOUNTS do local c,R,H=m[1],m[2],m[3]; local peaks={{c,R,H}}
 for k=1,5 do local a=k*2.4+mi*1.3; local d=R*(0.38+0.12*((k*37)%5)/5)
  peaks[#peaks+1]={c+Vector2.new(math.cos(a),math.sin(a))*d, R*(0.45+0.1*(k%3)), H*(0.55+0.12*(k%4))} end
 G.MASSIF[mi]=peaks end
function G.mountainField(p)
 local best=0
 for mi,peaks in G.MASSIF do
  for _,pk in peaks do local v=p-pk[1]; local d=v.Magnitude
   if d<pk[2]*1.3 then local ang=math.atan2(v.Y,v.X); local R=pk[2]*(1+0.28*noise(math.cos(ang)*1.7+mi,math.sin(ang)*1.7,pk[3]/97))
   local t=1-d/R; if t>0 then best=math.max(best,pk[3]*sstep(t)^1.25) end end end end
 return best
end
-- smooth (noise-free) height used for road profiles
function G.Hs(x,z)
 local p=Vector2.new(x,z)
 local h=16+8*noise(x/2600,z/2600,0.3)
 -- outer hills toward the map edge
 local r=math.max(math.abs(x),math.abs(z))+noise(x/1100,z/1100,5.5)*600; h+=sstep((r-4500)/1500)*(110+60*noise(x/700,z/700,6.6))
 h=math.max(h,16+G.mountainField(p))
 -- city flat
 local inC=inPoly(p,G.CITY_POLY); local ce=polyEdgeDist(p,G.CITY_POLY)
 local cw=inC and 1 or (1-sstep(ce/450)); h=h+(6-h)*cw
 -- towns flat-ish
 for _,t in G.TOWNS do local d=(p-t[1]).Magnitude; local w=1-sstep((d-t[2])/300); h=h+(math.min(h,22)-h)*w end
 -- coast
 local cs=coastSigned(p)
 if cs<0 then h=math.min(h,-6+cs*0.06) ; h=math.max(h,-60) elseif cs<220 then h=h+(3-h)*(1-sstep(cs/220)) end
 -- lake
 local q=(p-G.LAKE_C); local e=math.sqrt((q.X/G.LAKE_R.X)^2+(q.Y/G.LAKE_R.Y)^2)
 if e<1.25 then local w=1-sstep((e-0.85)/0.4); h=h+(math.min(h,G.LAKE+3)-h)*w; if e<1 then h=math.min(h,G.LAKE-4-14*(1-e)) end end
 return h
end
local function detail(x,z,h)
 local m=0; local amp=2.5
 local mtn=0
 for _,mm in G.MOUNTS do local d=(Vector2.new(x,z)-mm[1]).Magnitude; mtn=math.max(mtn,1-d/(mm[2]*1.3)) end
 m+=noise(x/420,z/420,1.7)*amp + noise(x/130,z/130,4.1)*1.2
 if mtn>0 then m+=(1-math.abs(noise(x/700,z/700,9.3)))*60*mtn + noise(x/180,z/180,2.2)*18*mtn end
 return h+m, mtn
end

-- ===== road geometry =====
G.detail=detail
local function catmull(pts,closed,spacing)
 local out={}; local n=#pts
 local function g(i) if closed then return pts[(i-1)%n+1] end return pts[math.clamp(i,1,n)] end
 local last=closed and n or n-1
 for i=1,last do
  local p0,p1,p2,p3=g(i-1),g(i),g(i+1),g(i+2)
  local L=(p2-p1).Magnitude; local steps=math.max(1,math.floor(L/spacing))
  for s=0,steps-1 do local t=s/steps; local t2,t3=t*t,t*t*t
   out[#out+1]=0.5*((2*p1)+(-p0+p2)*t+(2*p0-5*p1+4*p2-p3)*t2+(-p0+3*p1-3*p2+p3)*t3) end
 end
 if not closed then out[#out+1]=pts[n] end
 return out
end
function G.buildRoadData()
 local roads={}
 local function add(name,kind,width,pts,closed,flatElev)
  local samples=catmull(pts,closed,30); local el={}
  for i,p in samples do el[i]=flatElev or G.Hs(p.X,p.Y) end
  -- smooth elevations (several passes)
  if not flatElev then for pass=1,4 do local e2={} for i=1,#el do local s,c=0,0 for k=-6,6 do local j=i+k; if closed then j=(j-1)%#el+1 end; if el[j] then s+=el[j]; c+=1 end end e2[i]=s/c end el=e2 end end
  for i=1,#el do el[i]=math.max(el[i],G.SEA+3) end
  -- grade limit (cuts crests so roads stay drivable)
  if not flatElev then local g=(kind=="Touge" and 0.18) or 0.08
   for pass=1,2 do
    for i=2,#el do local L=(samples[i]-samples[i-1]).Magnitude; el[i]=math.min(el[i],el[i-1]+g*L) end
    for i=#el-1,1,-1 do local L=(samples[i]-samples[i+1]).Magnitude; el[i]=math.min(el[i],el[i+1]+g*L) end
   end
   for i=1,#el do el[i]=math.max(el[i],G.SEA+3) end
  end
  local lift={}
  for i=1,#el do lift[i]=0 end
  if kind=="Freeway" then
   local w={}
   for i,p in samples do local inside=inPoly(p,G.CITY_POLY); local d=polyEdgeDist(p,G.CITY_POLY); w[i]=inside and 1 or (1-sstep((d-150)/450)) end
   for pass=1,3 do local w2={} for i=1,#w do local s_,c_=0,0 for k=-8,8 do if w[i+k] then s_+=w[i+k]; c_+=1 end end w2[i]=s_/c_ end w=w2 end
   for i=1,#el do lift[i]=G.LIFT*sstep(w[i]); el[i]=el[i]+lift[i] end
  end
  roads[#roads+1]={name=name,kind=kind,width=width,pts=samples,el=el,closed=closed,lift=lift}
 end
 for _,r in G.ROADS do add(r[1],r[2],r[3],r[4],r[5]) end
 -- town main streets: perpendicular to the nearest highway/freeway, starting at it
 G.TOWN_STREETS={}
 for ti,t in G.TOWNS do
  local c=t[1]; local best,bd,bdir=1e9,nil,nil
  for _,r in roads do if r.kind=="Highway" or r.kind=="Freeway" then
   for i=1,#r.pts-1 do local a,b=r.pts[i],r.pts[i+1]; local d,t=segDist(c,a,b); if d<best then best=d; bdir=(b-a).Unit; bd=a+(b-a)*t end end end end
  local perp=Vector2.new(-bdir.Y,bdir.X); if (c-bd):Dot(perp)<0 then perp=-perp end
  local len=math.max(560,best+280); local s0=math.max(90,best-210)
  local a=bd; local b=a+perp*len
  local e=G.Hs(c.X,c.Y)
  add("Town"..ti.."_Main","Avenue",34,{a,b},false,e)
  G.TOWN_STREETS[ti]={a=a,b=b,dir=perp,el=e,len=len,s0=s0}
 end
 -- city grid (axis aligned)
 local mn,mx=Vector2.new(1e9,1e9),Vector2.new(-1e9,-1e9)
 for _,p in G.CITY_POLY do mn=Vector2.new(math.min(mn.X,p.X),math.min(mn.Y,p.Y)); mx=Vector2.new(math.max(mx.X,p.X),math.max(mx.Y,p.Y)) end
 local st=G.CITY_STEP; local id=0
 for x=math.ceil(mn.X/st)*st,mx.X,st do local run=nil
  for z=mn.Y,mx.Y+st,st/2 do local p=Vector2.new(x,z); local ins=inPoly(p,G.CITY_POLY) and polyEdgeDist(p,G.CITY_POLY)>40
   if ins and not run then run={p} elseif ins then run[2]=p elseif run then if run[2] then
    local dz0=math.floor(G.DRAG.a.Y/st)*st; local dz1=dz0+st
    if x>G.DRAG.a.X-60 and x<G.DRAG.b.X+60 and run[1].Y<dz1 and run[2].Y>dz0 then
     if dz0-run[1].Y>40 then id+=1; add("CityNS_"..id,"Street",34,{run[1],Vector2.new(x,dz0)},false,6) end
     if run[2].Y-dz1>40 then id+=1; add("CityNS_"..id,"Street",34,{Vector2.new(x,dz1),run[2]},false,6) end
    else id+=1; add("CityNS_"..id,"Street",34,{run[1],run[2]},false,6) end
   end run=nil end end end
 for z=math.ceil(mn.Y/st)*st,mx.Y,st do local run=nil
  for x=mn.X,mx.X+st,st/2 do local p=Vector2.new(x,z); local ins=inPoly(p,G.CITY_POLY) and polyEdgeDist(p,G.CITY_POLY)>40
   if ins and not run then run={p} elseif ins then run[2]=p elseif run then if run[2] then id+=1; add("CityEW_"..id,"Street",34,{run[1],run[2]},false,6) end run=nil end end end
 -- speedway oval
 local sp=G.SPEEDWAY; local ov={}
 for k=0,23 do local a=k/24*math.pi*2; ov[#ov+1]=sp.c+Vector2.new(math.cos(a)*sp.rx,math.sin(a)*sp.rz) end
 add("Speedway_Oval","Track",sp.width,ov,true,G.Hs(sp.c.X,sp.c.Y))
 add("Drag_Strip","Track",G.DRAG.width,{G.DRAG.a,G.DRAG.b},false,6)
 local da,db=G.DRAG.a,G.DRAG.b
 local dz1=(math.floor(da.Y/st)+1)*st
 add("Drag_Access","Street",34,{Vector2.new(math.floor(da.X/st)*st,da.Y),da},false,6)
 add("Drag_Return","Street",34,{db,db+Vector2.new(60,30),db+Vector2.new(75,dz1-da.Y-120),Vector2.new(db.X+8,dz1)},false,6)
 G.spEl=G.Hs(sp.c.X,sp.c.Y)
 -- ===== junction snapping: every road end meets another road at the same height =====
 local function nearestOn(p,self)
  local best,q,qe,qr=1e9
  for _,o in roads do if o~=self and o.kind~="Dirt" then local m=#o.pts; local last=o.closed and m or m-1
   for i=1,last do local j=i%m+1; if (o.lift[i] or 0)<=4 then local d,t=segDist(p,o.pts[i],o.pts[j]); if d<best then best=d; q=o.pts[i]+(o.pts[j]-o.pts[i])*t; qe=o.el[i]+(o.el[j]-o.el[i])*t; qr=o end end end end end
  return best,q,qe,qr
 end
 local function rayHit(p,dir,maxL,self)
  local best,q,qe=1e9
  for _,o in roads do if o~=self and o.kind~="Dirt" then local m=#o.pts; local last=o.closed and m or m-1
   for i=1,last do local j=i%m+1; if (o.lift[i] or 0)<=4 then
    local a,b=o.pts[i],o.pts[j]; local e=b-a; local den=dir.X*e.Y-dir.Y*e.X
    if math.abs(den)>1e-6 then local w=a-p; local t=(w.X*e.Y-w.Y*e.X)/den; local u=(w.X*dir.Y-w.Y*dir.X)/den
     if t>1 and t<maxL and u>=0 and u<=1 and t<best then best=t; q=a+e*u; qe=o.el[i]+(o.el[j]-o.el[i])*u end end end end end end
  return best,q,qe
 end
 for _,r in roads do if not r.closed and r.kind~="Dirt" then
  for _,first in {true,false} do
   local n=#r.pts; local ei=first and 1 or n; local ni=first and 2 or n-1
   if (r.lift[ei] or 0)>4 then continue end
   local p=r.pts[ei]; local dir=(p-r.pts[ni]).Unit
   local d,q,qe=nearestOn(p,r)
   if r.kind=="Street" and r.name:find("^City") then local rd,rq,re=rayHit(p,dir,420,r); if rd<1e9 and (d>2) then d,q,qe=rd,rq,re end end
   local lim=(r.kind=="Street") and 420 or 160
   if q and d>1 and d<lim then
    local steps=math.max(1,math.floor(d/30)); local e0=r.el[ei]
    for k=1,steps do local t=k/steps; local np=p+(q-p)*t; local ne=e0+(qe-e0)*t
     if first then table.insert(r.pts,1,np); table.insert(r.el,1,ne); table.insert(r.lift,1,0) else table.insert(r.pts,np); table.insert(r.el,ne); table.insert(r.lift,0) end end
   end
   if q and d<lim then
    n=#r.pts; ei=first and 1 or n
    local delta=qe-r.el[ei]; local gg=(r.kind=="Touge" and 0.16) or 0.07; local K=math.clamp(math.ceil(math.abs(delta)/(gg*30))+1,3,n-1)
    for k=0,K do local idx=first and (1+k) or (n-k); if (r.lift[idx] or 0)<=4 then r.el[idx]+=delta*(1-k/(K+1))^1 end end
   end
  end
 end end
 -- settle: re-limit grades and re-snap junction heights until they agree
 local function limit(r) if r.kind=="Freeway" or r.kind=="Track" then return end
  local g=(r.kind=="Touge" and 0.18) or 0.08; local e=r.el; local P=r.pts
  for pass=1,2 do for i=2,#e do local L=(P[i]-P[i-1]).Magnitude; e[i]=math.min(e[i],e[i-1]+g*L) end
   for i=#e-1,1,-1 do local L=(P[i]-P[i+1]).Magnitude; e[i]=math.min(e[i],e[i+1]+g*L) end end end
 for iter=1,8 do
  for _,r in roads do limit(r) end
  for _,r in roads do if not r.closed and r.kind~="Dirt" then for _,first in {true,false} do
   local n=#r.pts; local ei=first and 1 or n; if (r.lift[ei] or 0)>4 then continue end
   local d,q,qe=nearestOn(r.pts[ei],r)
   if q and d<3 then local delta=qe-r.el[ei]; local gg=(r.kind=="Touge" and 0.16) or 0.07; local K=math.clamp(math.ceil(math.abs(delta)/(gg*30))+1,3,n-1)
    for k=0,K do local idx=first and (1+k) or (n-k); if (r.lift[idx] or 0)<=4 then r.el[idx]+=delta*(1-k/(K+1)) end end end
  end end end
 end
 G.roads=roads
 -- spatial index of segments
 local CELL=256; local grid={}
 for ri,r in roads do local n=#r.pts; local last=r.closed and n or n-1
  for i=1,last do local j=i%n+1; local a,b=r.pts[i],r.pts[j]; local R=r.width/2+60
   if (r.lift[i] or 0)>10 or (r.lift[j] or 0)>10 then continue end
   local x0,x1=math.floor((math.min(a.X,b.X)-R)/CELL),math.floor((math.max(a.X,b.X)+R)/CELL)
   local z0,z1=math.floor((math.min(a.Y,b.Y)-R)/CELL),math.floor((math.max(a.Y,b.Y)+R)/CELL)
   for cx=x0,x1 do for cz=z0,z1 do local k=cx*100000+cz; grid[k]=grid[k] or {}; table.insert(grid[k],{a,b,r.el[i],r.el[j],r.width/2,r.kind}) end end end end
 G.grid=grid; G.CELL=CELL
 return roads
end
local function roadAt(x,z)
 local cell=G.grid[math.floor(x/G.CELL)*100000+math.floor(z/G.CELL)]; if not cell then return nil end
 local p=Vector2.new(x,z); local best,bd=nil,1e9
 for _,s in cell do local d,t=segDist(p,s[1],s[2]); local over=d-s[5]; if over<bd then bd=over; best={s[3]+(s[4]-s[3])*t,s[6],d,s[5]} end end
 return best,bd
end

G.roadAt=roadAt
-- ===== column sampler: returns height, surface material, water level =====
local M=Enum.Material
function G.column(x,z)
 local p=Vector2.new(x,z)
 local hs=G.Hs(x,z); local h,mtn=detail(x,z,hs)
 local inC=inPoly(p,G.CITY_POLY); if inC then h=6 end
 local mat=M.Grass
 -- forests
 for _,f in G.FORESTS do if (p-f[1]).Magnitude<f[2]*(0.85+0.3*noise(x/500,z/500,7)) then mat=M.LeafyGrass end end
 -- valley fields
 if inPoly(p,G.VALLEY) then local fx,fz=math.floor((x+37)/260),math.floor((z+11)/190); local k=(fx*928371+fz*12553)%5
  mat=({M.Grass,M.LeafyGrass,M.Ground,M.Grass,M.Mud})[k+1] end
 if mtn>0.25 then local sl=mtn; if h>300 then mat=M.Rock end; if h>440+noise(x/300,z/300,8)*40 then mat=M.Snow end; if mat==M.Grass and noise(x/90,z/90,3)>0.35 then mat=M.Rock end end
 if inC then mat=M.Pavement end
 local cs=coastSigned(p); if cs<160 then mat=M.Sand; if cs>=0 then h=math.max(h, 1.5) end end
 local water=nil
 if cs<0 then water=G.SEA; mat=M.Sand end
 local q=(p-G.LAKE_C); local e=math.sqrt((q.X/G.LAKE_R.X)^2+(q.Y/G.LAKE_R.Y)^2)
 if e<1 then water=G.LAKE; mat=M.Mud elseif e<1.12 then mat=M.Sand end
 -- roads flatten
 local r,over=roadAt(x,z)
 if r then
  local core=r[4]+8
  if r[3]<=core then h=r[1]-1.0; mat=(r[2]=="Dirt") and M.Ground or M.Asphalt; water=nil
  elseif r[3]<core+50 then local w=1-sstep((r[3]-core)/50); h=h+((r[1]-1.0)-h)*w; if r[2]=="Dirt" and w>0.5 then mat=M.Mud end end
 end
 do local sp=G.SPEEDWAY; local v=p-sp.c; local e2=(v.X/sp.rx)^2+(v.Y/sp.rz)^2
  if e2<1 then h=(G.spEl or h)-1.0; if mat~=M.Asphalt then mat=M.Grass end; water=nil end end
 if h<G.SEA and not water and cs<60 then water=G.SEA end
 return h,mat,water
end

-- ===== terrain writer =====
function G.writeTerrain(x0,x1,z0,z1,status)
 local T=workspace.Terrain; local RES=4; local CH=128
 local total=math.ceil((x1-x0)/CH)*math.ceil((z1-z0)/CH); local done=0
 for cx=x0,x1-1,CH do for cz=z0,z1-1,CH do
  local n=CH/RES; local cols={}; local lo,hi=1e9,-1e9
  for i=1,n do cols[i]={} for k=1,n do local h,m,w=G.column(cx+(i-0.5)*RES,cz+(k-0.5)*RES); cols[i][k]={h,m,w}; lo=math.min(lo,h); hi=math.max(hi,math.max(h,w or -1e9)) end end
  local y0=math.floor((math.max(lo-12,-72))/RES)*RES; local y1=math.ceil((hi+4)/RES)*RES
  local ny=(y1-y0)/RES
  local mats,occ={}, {}
  for i=1,n do mats[i]={}; occ[i]={}
   for j=1,ny do mats[i][j]={}; occ[i][j]={} end
   for k=1,n do local c=cols[i][k]; local h,m,w=c[1],c[2],c[3]
    for j=1,ny do local yb=y0+(j-1)*RES; local fill=math.clamp((h-yb)/RES,0,1)
     if fill>0 then mats[i][j][k]=(h-yb>10) and ((m==M.Snow or m==M.Rock) and M.Rock or M.Ground) or m; occ[i][j][k]=fill
     elseif w and yb<w then mats[i][j][k]=M.Water; occ[i][j][k]=math.clamp((w-yb)/RES,0,1)
     else mats[i][j][k]=M.Air; occ[i][j][k]=0 end
    end end end
  T:WriteVoxels(Region3.new(Vector3.new(cx,y0,cz),Vector3.new(cx+CH,y1,cz+CH)),RES,mats,occ)
  done+=1; if status then status(done,total) end; task.wait()
 end end
end

-- ===== road parts =====
local KIND={Freeway={Color3.fromRGB(52,54,58),Enum.Material.Asphalt},Highway={Color3.fromRGB(58,60,64),Enum.Material.Asphalt},Touge={Color3.fromRGB(62,63,66),Enum.Material.Asphalt},Avenue={Color3.fromRGB(56,58,62),Enum.Material.Asphalt},Street={Color3.fromRGB(60,62,66),Enum.Material.Asphalt},Track={Color3.fromRGB(45,46,50),Enum.Material.Asphalt}}
function G.buildRoadParts(parent)
 local root=Instance.new("Folder"); root.Name="Roads"
 for _,r in G.roads do if r.kind~="Dirt" then
  local f=root:FindFirstChild(r.kind) or Instance.new("Folder",root); f.Name=r.kind
  local mdl=Instance.new("Model"); mdl.Name=r.name; mdl:SetAttribute("Kind",r.kind); mdl:SetAttribute("Width",r.width)
  local n=#r.pts; local last=r.closed and n or n-1; local cs=KIND[r.kind]
  for i=1,last do local j=i%n+1
   local a=Vector3.new(r.pts[i].X,r.el[i],r.pts[i].Y); local b=Vector3.new(r.pts[j].X,r.el[j],r.pts[j].Y)
   local L=(b-a).Magnitude; if L>0.5 then
    local part=Instance.new("Part"); part.Anchored=true; part.Size=Vector3.new(r.width,2,L+r.width*0.12)
    part.CFrame=CFrame.lookAt((a+b)/2,b)*CFrame.new(0,-0.9,0); part.Color=cs[1]; part.Material=cs[2]; part.TopSurface=Enum.SurfaceType.Smooth
    part.Name="Seg"..i; part.Parent=mdl
    local li=(r.lift[i] or 0)
    if li>4 then
     local cf=CFrame.lookAt((a+b)/2,b)
     for s_=-1,1,2 do local bar=Instance.new("Part"); bar.Anchored=true; bar.Size=Vector3.new(1.6,3.2,L+1); bar.CFrame=cf*CFrame.new(s_*(r.width/2-0.8),1.5,0); bar.Material=Enum.Material.Concrete; bar.Color=Color3.fromRGB(190,188,182); bar.Name="Barrier"; bar.Parent=mdl end
     local cap=Instance.new("Part"); cap.Anchored=true; cap.Size=Vector3.new(r.width+2,3,L+1); cap.CFrame=cf*CFrame.new(0,-3.4,0); cap.Material=Enum.Material.Concrete; cap.Color=Color3.fromRGB(170,168,162); cap.Name="Deck"; cap.Parent=mdl
     if i%3==0 then
      local gy=a.Y-li
      local h=(a.Y-5)-gy
      if h>4 then for s_=-1,1,2 do local col=Instance.new("Part"); col.Shape=Enum.PartType.Cylinder; col.Anchored=true; col.Size=Vector3.new(h,7,7); col.CFrame=CFrame.new(a+cf.RightVector*s_*(r.width*0.28)+Vector3.new(0,-5-h/2,0))*CFrame.Angles(0,0,math.pi/2); col.Material=Enum.Material.Concrete; col.Color=Color3.fromRGB(176,174,168); col.Name="Pier"; col.Parent=mdl end end
     end
    end
   end end
  mdl.Parent=f
 end end
 -- terrain surface renders ~1.7 above el; lift road parts so they sit on top
 for _,d in root:GetDescendants() do if d:IsA("BasePart") then d.CFrame=d.CFrame+Vector3.new(0,1.8,0) end end
 root.Parent=parent; return root
end
function G.buildMarkers(parent)
 local f=Instance.new("Folder"); f.Name="POI_Markers"
 for name,p in G.POI do local h=G.column(p.X,p.Y)
  local m=Instance.new("Part"); m.Name=name; m.Anchored=true; m.CanCollide=false; m.Size=Vector3.new(8,60,8); m.Material=Enum.Material.Neon
  m.Color=Color3.fromRGB(255,170,40); m.Position=Vector3.new(p.X,h+30,p.Y); m.Transparency=0.3
  local bb=Instance.new("BillboardGui",m); bb.Size=UDim2.fromOffset(200,40); bb.StudsOffset=Vector3.new(0,40,0); bb.AlwaysOnTop=true; bb.MaxDistance=4000
  local t=Instance.new("TextLabel",bb); t.Size=UDim2.fromScale(1,1); t.BackgroundTransparency=1; t.Text=name; t.TextScaled=true; t.Font=Enum.Font.GothamBold; t.TextColor3=Color3.new(1,1,1); t.TextStrokeTransparency=0
  m.Parent=f end
 f.Parent=parent; return f
end
return G
