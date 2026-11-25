-- CityFill: fills Coast City blocks with OT_Kit models + street props. Requires HorizonValleyGen (CITY_STEP 440).
local C={}
local G=require(game.ServerStorage.HorizonValleyGen)
local KIT=game.ServerStorage.OT_Kit
local S=10.9
local function P(px,py) return Vector2.new((px-550)*S,(py-581)*S) end
C.DOWNTOWN=P(370,900)
C.GROUND=7.72
local FRONT_OVERRIDE={TechStore_A="-Z",House_A="-Z",House_B="-Z",Townhouses_A="-Z",Aquarium_A="-Z",Prison_A="-Z"}
local LOTKEYS={"Pavement","PaintWhite","Asphalt","Sidewalk","Lawn","Concrete_","Grass"}
local frontCache={}
local function frontOf(m)
	if frontCache[m.Name] then return frontCache[m.Name] end
	local short=m.Name:gsub("^OT_","")
	local f
	if FRONT_OVERRIDE[short] then f=FRONT_OVERRIDE[short]=="-Z" and Vector3.new(0,0,-1) or Vector3.new(1,0,0) end
	if not f then
		local cf=m:GetBoundingBox(); local acc,w=Vector3.zero,0
		for _,p in m:GetDescendants() do if p:IsA("BasePart") then for _,k in LOTKEYS do if p.Name:find(k) then local v=p.Size.X*p.Size.Z; acc+=p.Position*v; w+=v; break end end end end
		if w>0 then local d=acc/w-cf.Position; d=Vector3.new(d.X,0,d.Z); if d.Magnitude>8 then f=d.Unit end end
	end
	f=f or Vector3.new(1,0,0)
	-- snap to axis
	if math.abs(f.X)>=math.abs(f.Z) then f=Vector3.new(math.sign(f.X),0,0) else f=Vector3.new(0,0,math.sign(f.Z)) end
	frontCache[m.Name]=f; return f
end
C.frontOf=frontOf
-- place a kit model: center (Vector2), facing (unit Vector3 on XZ), maxW (along facing-perpendicular), maxD (along facing)
function C.place(name,center,facing,maxW,maxD,parent,y,minScale)
	local t=KIT:FindFirstChild("OT_"..name); if not t then return nil end
	local m=t:Clone()
	local f=frontOf(t)
	local best,bestTh=-2,0
	for _,th in {0,math.pi/2,math.pi,-math.pi/2} do local r=CFrame.Angles(0,th,0):VectorToWorldSpace(f); local d=r:Dot(facing); if d>best then best,bestTh=d,th end end
	local cf=m:GetBoundingBox()
	m:PivotTo(CFrame.new(cf.Position)*CFrame.Angles(0,bestTh,0)*CFrame.new(-cf.Position)*m:GetPivot())
	local c2,s2=m:GetBoundingBox()
	local w,d
	if math.abs(facing.X)>0.5 then d,w=s2.X,s2.Z else d,w=s2.Z,s2.X end
	local sc=math.min(1,(maxW or 1e9)/w,(maxD or 1e9)/d)
	if sc<(minScale or 0.75) then m:Destroy(); return nil end
	if sc<1 then m:ScaleTo(m:GetScale()*sc) end
	c2,s2=m:GetBoundingBox()
	m:PivotTo(m:GetPivot()+Vector3.new(center.X-c2.X,(y or C.GROUND)+0.05-(c2.Y-s2.Y/2),center.Y-c2.Z))
	m.Parent=parent
	return m,s2
end
-- simple seeded rng
local seed=12345
local function rnd() seed=(seed*1103515245+12345)%2147483648; return seed/2147483648 end
local function pick(list) return list[1+math.floor(rnd()*#list)] end
C.ZONES={
	downtown={"Skyscraper_Glass","Skyscraper_Deco","OfficeTower_B","Skyscraper_Twist","Skyscraper_Setback","Skyscraper_Round","Skyscraper_Residential","Skyscraper_Twin","Skyscraper_Brick","Skyscraper_Braced","Office_A","Hotel_A","Bank_B","ParkingGarage_A","Skyscraper_Glass","Skyscraper_Setback","OfficeTower_B"},
	mid={"Tenement_A","WalkUp_A","Brownstone_A","Apartments_A","MixedUse_A","CornerShop_A","Storefront_A","Office_A","ParkingGarage_A","Jewelry_A","TechStore_A","CardShop_A","Barber_A","Bar_A","Diner_B","Convenience_A","Laundromat_A","GunStore_A","Gym_A","Apartments_A","MixedUse_A","Skyscraper_Brick","Skyscraper_Residential"},
	outer={"StripMall_A","FastFood_A","GasStation_B","Convenience_A","RepairShop_B","TunerShop_A","AutoParts_A","Gym_A","Laundromat_A","Motel_A","CarWash_A","Townhouses_A","Duplex_A","House_A","House_B","House_C","OfficePark_A","FireStation_A","Church_A","Diner_B","Bar_A","Apartments_A"},
	industrial={"Warehouse_A","Factory_A","AutoParts_A","RepairShop_B","TunerShop_A","CarWash_A","Warehouse_A","GasStation_B"},
}
local LIMIT={Hotel_A=2,Bank_B=2,Church_A=2,FireStation_A=2,Hospital_A=1,GunStore_A=2,Jewelry_A=2,CardShop_A=2,TechStore_A=2,Motel_A=2,Factory_A=2}
local used={}
local function zoneOf(c)
	if c.X>0 and c.Y>3900 then return "industrial" end
	local d=(c-C.DOWNTOWN).Magnitude
	if d<1100 then return "downtown" elseif d<2100 then return "mid" else return "outer" end
end
local function segDist(p,a,b) local ab=b-a; local l2=ab:Dot(ab); local t=l2>0 and math.clamp((p-a):Dot(ab)/l2,0,1) or 0; return (p-(a+ab*t)).Magnitude end
local function nearBigRoad(p,pad)
	for _,r in G.roads do if r.kind~="Street" then
		local n=#r.pts; local last=r.closed and n or n-1
		for i=1,last do local j=i%n+1; if segDist(p,r.pts[i],r.pts[j])<r.width/2+pad then return true end end
	end end
	return false
end
C.nearBigRoad=nearBigRoad
local function inPoly(p,poly) local c=false; local j=#poly
	for i=1,#poly do local a,b=poly[i],poly[j]
		if ((a.Y>p.Y)~=(b.Y>p.Y)) and (p.X<(b.X-a.X)*(p.Y-a.Y)/(b.Y-a.Y)+a.X) then c=not c end; j=i end
	return c end
local function edgeDist(p,poly) local d=1e9; for i=1,#poly do d=math.min(d,segDist(p,poly[i],poly[i%#poly+1])) end return d end
C.inPoly=inPoly; C.edgeDist=edgeDist
function C.blocks()
	local st=G.CITY_STEP; local poly=G.CITY_POLY
	local mn,mx=Vector2.new(1e9,1e9),Vector2.new(-1e9,-1e9)
	for _,p in poly do mn=Vector2.new(math.min(mn.X,p.X),math.min(mn.Y,p.Y)); mx=Vector2.new(math.max(mx.X,p.X),math.max(mx.Y,p.Y)) end
	local out={}
	for x=math.ceil(mn.X/st)*st,mx.X,st do for z=math.ceil(mn.Y/st)*st,mx.Y,st do
		local c=Vector2.new(x+st/2,z+st/2)
		if inPoly(c,poly) and edgeDist(c,poly)>st*0.45 then out[#out+1]={c=c,x0=x,z0=z} end
	end end
	return out
end
-- reserved specials: name -> world point
function C.run(parent,status)
	seed=12345; used={}
	local st=G.CITY_STEP; local half=st/2; local inner=st-34-20; local q=inner/2
	local specials={ {"PlayerGarage_A",G.POI.Garage}, {"Police_B",G.POI.PoliceHQ}, {"Dealership_A",G.POI.Dealer}, {"Hospital_A",P(300,960)}, {"Landmark_Tower",C.DOWNTOWN+Vector2.new(300,-150)} }
	local B=Instance.new("Folder"); B.Name="Buildings"; B.Parent=parent
	local blocks=C.blocks(); local placed=0; local skipped=0
	local reserved={}
	for _,s in specials do
		-- find block + quadrant containing the point
		for bi,b in blocks do
			if s[2].X>=b.x0 and s[2].X<b.x0+st and s[2].Y>=b.z0 and s[2].Y<b.z0+st then
				local qi=s[2].X<b.c.X and 0 or 1; local qj=s[2].Y<b.c.Y and 0 or 1
				reserved[bi..":"..qi..":"..qj]=s[1]
			end
		end
	end
	for bi,b in blocks do
		if nearBigRoad(b.c,half*0.9) then skipped+=1 else
		local zone=zoneOf(b.c)
		-- industrial big lots: one per block
		if zone=="industrial" and rnd()<0.5 then
			local name=pick({"Warehouse_A","Factory_A","Warehouse_A"})
			if (used[name] or 0)<(LIMIT[name] or 99) then
				if C.place(name,b.c,Vector3.new(0,0,-1),inner,inner,B) then used[name]=(used[name] or 0)+1; placed+=1 end
			end
		else
		for qi=0,1 do for qj=0,1 do
			local qc=b.c+Vector2.new((qi-0.5)*q,(qj-0.5)*q)
			local facing=qj==0 and Vector3.new(0,0,-1) or Vector3.new(0,0,1)
			local key=bi..":"..qi..":"..qj
			local name=reserved[key]
			if not name then
				for tries=1,8 do local n=pick(C.ZONES[zone]); if (used[n] or 0)<(LIMIT[n] or 99) then name=n break end end
			end
			if name then
				local t=KIT:FindFirstChild("OT_"..name)
				local _,sz=t:GetBoundingBox(); local mxd=math.max(sz.X,sz.Z)
				if mxd<=q*0.5 and not reserved[key] then
					-- two small buildings side by side along the frontage
					for k=0,1 do
						local n2=k==0 and name or pick(C.ZONES[zone])
						local _,s3=KIT["OT_"..n2]:GetBoundingBox()
						if math.max(s3.X,s3.Z)<=q*0.5 and (used[n2] or 0)<(LIMIT[n2] or 99) then
							if C.place(n2,qc+Vector2.new((k-0.5)*q*0.5,0),facing,q*0.5,q,B) then used[n2]=(used[n2] or 0)+1; placed+=1 end
						end
					end
				else
					if C.place(name,qc,facing,q,q,B,nil,reserved[key] and 0.5 or 0.75) then used[name]=(used[name] or 0)+1; placed+=1 end
				end
			end
		end end
		end end
		if bi%4==0 then task.wait(); if status then status(bi,#blocks) end end
	end
	return placed,#blocks,skipped
end
-- street props
function C.props(parent)
	local Pf=Instance.new("Folder"); Pf.Name="StreetProps"; Pf.Parent=parent
	local n=0; local st=G.CITY_STEP
	for _,r in G.roads do if r.kind=="Street" then
		local a,b=r.pts[1],r.pts[#r.pts]; local dir=(b-a); local L=dir.Magnitude; dir=dir.Unit; local nrm=Vector2.new(-dir.Y,dir.X)
		local zone; 
		for t=60,L-60,120 do
			local c=a+dir*t
			for s=-1,1,2 do
				local p=c+nrm*s*(r.width/2+6)
				local face3=Vector3.new(-nrm.X*s,0,-nrm.Y*s)
				local item=(math.floor(t/120)%2==0) and "StreetLight" or ((C.edgeDist(p,G.CITY_POLY)<600 and math.abs(p.X+3000)<1800) and "Tree_Palm" or "Tree_Oak")
				local z=zoneOf(p)
				if z=="downtown" and item~="StreetLight" then item="Tree_Oak" end
				if C.place(item,p,face3,nil,nil,Pf,nil,0.1) then n+=1 end
			end
		end
	end end
	-- traffic lights at grid intersections
	local poly=G.CITY_POLY
	local xs,zs={},{}
	for _,r in G.roads do if r.kind=="Street" then local a=r.pts[1]; if r.name:find("CityNS") then xs[#xs+1]=a.X else zs[#zs+1]=a.Y end end end
	local seenx,seenz={},{}
	for _,x in xs do seenx[math.floor(x+0.5)]=true end; for _,z in zs do seenz[math.floor(z+0.5)]=true end
	for x in seenx do for z in seenz do
		local p=Vector2.new(x,z)
		if inPoly(p,poly) and C.edgeDist(p,poly)>120 and not nearBigRoad(p,60) then
			for s=-1,1,2 do
				local corner=p+Vector2.new(s*23,s*23)
				if C.place("TrafficLight",corner,Vector3.new(-s,0,0),nil,nil,Pf,nil,0.1) then n+=1 end
				if C.place("Crosswalk",p+Vector2.new(0,s*24),Vector3.new(0,0,1),nil,nil,Pf,5.95,0.1) then n+=1 end
			end
		end
	end task.wait() end
	return n
end
return C
