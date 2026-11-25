-- CityFinish: final polish for Coast City + the 4 towns.
-- groundFix: lifts city buildings/props so lot pads sit on the terrain surface (~7.7).
-- city: sidewalk rings on every block, fills empty quadrants (buildings / parking lots / parks),
--       greens partly-blocked lots near freeway/highway with trees.
-- towns: re-seats buildings on terrain, cross street through each town with houses, sidewalks + props.
local F={}
local G=require(game.ServerStorage.HorizonValleyGen:Clone()); G.buildRoadData()
local CF=require(game.ServerStorage.CityFill:Clone())
local KIT=game.ServerStorage.OT_Kit
local SURF=7.72 -- city terrain surface
local RP=RaycastParams.new(); RP.FilterType=Enum.RaycastFilterType.Include; RP.FilterDescendantsInstances={workspace.Terrain}
local function groundY(p) local r=workspace:Raycast(Vector3.new(p.X,1500,p.Y),Vector3.new(0,-3000,0),RP); return r and r.Position.Y or 0 end
local seed=4242
local function rnd() seed=(seed*1103515245+12345)%2147483648; return seed/2147483648 end
local function pick(t) return t[1+math.floor(rnd()*#t)] end
local function V3(v) return Vector3.new(v.X,0,v.Y) end
local function part(parent,size,cf,mat,col,name)
	local p=Instance.new("Part"); p.Anchored=true; p.Size=size; p.CFrame=cf; p.Material=mat; p.Color=col; p.Name=name or "Part"
	p.TopSurface=Enum.SurfaceType.Smooth; p.BottomSurface=Enum.SurfaceType.Smooth; p.Parent=parent; return p
end
local CONC=Color3.fromRGB(178,175,168)
local function bottomTo(m,y) local c,s=m:GetBoundingBox(); m:PivotTo(m:GetPivot()+Vector3.new(0,y-(c.Y-s.Y/2),0)) end

function F.groundFix(HV)
	local n=0
	for _,m in HV.Buildings:GetChildren() do bottomTo(m,SURF+0.05); n+=1 end
	for _,m in HV.StreetProps:GetChildren() do
		if m.Name:find("Crosswalk") then bottomTo(m,7.92) else bottomTo(m,SURF) end; n+=1
		if n%300==0 then task.wait() end
	end
	return n
end

-- ===== city =====
local function bigRoad(p,pad) return CF.nearBigRoad(p,pad) end
local function rectOverlap(a,b) -- {x0,x1,z0,z1}
	local w=math.min(a[2],b[2])-math.max(a[1],b[1]); local h=math.min(a[4],b[4])-math.max(a[3],b[3])
	if w<=0 or h<=0 then return 0 end return w*h
end
function F.city(HV,status)
	local st=G.CITY_STEP; local q=(st-34-20)/2
	local Fin=Instance.new("Folder"); Fin.Name="CityFinish"; Fin.Parent=HV
	local SW=Instance.new("Folder"); SW.Name="BlockSidewalks"; SW.Parent=Fin
	local LOTS=Instance.new("Folder"); LOTS.Name="Lots"; LOTS.Parent=Fin
	local rects={}
	local used={}
	for _,m in HV.Buildings:GetChildren() do
		local c,s=m:GetBoundingBox(); rects[#rects+1]={c.X-s.X/2,c.X+s.X/2,c.Z-s.Z/2,c.Z+s.Z/2}
		local k=m.Name:gsub("^OT_",""); used[k]=(used[k] or 0)+1
	end
	local LIMIT={Hotel_A=2,Bank_B=2,Church_A=3,FireStation_A=3,GunStore_A=2,Jewelry_A=3,CardShop_A=3,TechStore_A=3,Motel_A=3,Factory_A=3,Aquarium_A=1,Hospital_A=1,Police_B=1,Dealership_A=1,PlayerGarage_A=1,Landmark_Tower=1}
	local stats={walks=0,bldg=0,parking=0,park=0,trees=0}
	local blocks=CF.blocks()
	for bi,b in blocks do
		local x0,z0=b.x0,b.z0
		local zone=CF.zoneOf and CF.zoneOf(b.c) or "mid"
		-- sidewalk ring (inside the street edge)
		local e0,e1=17,27; local L=st-34
		local sides={
			{Vector2.new(x0+st/2,z0+(e0+e1)/2),Vector3.new(L,1.2,10),Vector2.new(0,-1)},
			{Vector2.new(x0+st/2,z0+st-(e0+e1)/2),Vector3.new(L,1.2,10),Vector2.new(0,1)},
			{Vector2.new(x0+(e0+e1)/2,z0+st/2),Vector3.new(10,1.2,L-20),Vector2.new(-1,0)},
			{Vector2.new(x0+st-(e0+e1)/2,z0+st/2),Vector3.new(10,1.2,L-20),Vector2.new(1,0)},
		}
		for _,sd in sides do
			local mid,size,out=sd[1],sd[2],sd[3]
			local streetP=mid+out*22
			local along=Vector2.new(out.Y,out.X)*(L/2-10)
			local ok=CF.inPoly(streetP,G.CITY_POLY) and CF.edgeDist(streetP,G.CITY_POLY)>40
			for _,pp in {mid,mid+along,mid-along} do if bigRoad(pp,8) then ok=false end end
			if ok then part(SW,size,CFrame.new(mid.X,SURF+0.0,mid.Y),Enum.Material.Concrete,CONC,"Sidewalk"); stats.walks+=1 end
		end
		-- quadrants
		for qi=0,1 do for qj=0,1 do
			local qc=b.c+Vector2.new((qi-0.5)*q,(qj-0.5)*q)
			local qr={qc.X-q/2+12,qc.X+q/2-12,qc.Y-q/2+12,qc.Y+q/2-12}
			local occ=0; for _,r in rects do occ+=rectOverlap(qr,r) end
			if occ>0.10*(q-24)^2 then continue end
			local samples={}
			for sx=-1,1 do for sz=-1,1 do samples[#samples+1]=qc+Vector2.new(sx*(q/2-22),sz*(q/2-22)) end end
			local clear=0; for _,s in samples do if not bigRoad(s,10) then clear+=1 end end
			local facing=qj==0 and Vector3.new(0,0,-1) or Vector3.new(0,0,1)
			local f=Instance.new("Folder"); f.Name=("Lot_%d_%d%d"):format(bi,qi,qj)
			if clear==9 then
				local roll=rnd()
				local done=false
				if roll<0.6 then
					for tries=1,10 do
						local nm=pick(CF.ZONES[zone])
						if (used[nm] or 0)<(LIMIT[nm] or 99) then
							local m=CF.place(nm,qc,facing,q-8,q-8,f,SURF,0.6)
							if m then used[nm]=(used[nm] or 0)+1; stats.bldg+=1; done=true
								local c,s=m:GetBoundingBox(); rects[#rects+1]={c.X-s.X/2,c.X+s.X/2,c.Z-s.Z/2,c.Z+s.Z/2}
								break end
						end
					end
				end
				if not done and (roll<0.85 or zone=="industrial") then
					-- parking lot
					local W=q-26
					part(f,Vector3.new(W,0.6,W),CFrame.new(qc.X,SURF-0.08,qc.Y),Enum.Material.Asphalt,Color3.fromRGB(48,49,53),"LotPad")
					for row=-1,1,2 do
						local rz=qc.Y+row*(W/4)
						for k=-7,7 do local x=qc.X+k*10.5
							part(f,Vector3.new(0.5,0.1,18),CFrame.new(x,SURF+0.27,rz),Enum.Material.SmoothPlastic,Color3.fromRGB(230,230,225),"Line")
						end
					end
					local cars=2+math.floor(rnd()*4)
					for c=1,cars do
						local k=math.floor(rnd()*14)-7; local row=rnd()<0.5 and -1 or 1
						local p=Vector2.new(qc.X+(k+0.5)*10.5,qc.Y+row*(W/4))
						CF.place("ParkedCar",p,Vector3.new(0,0,-row),9,18,f,SURF+0.25,0.1)
					end
					for k=-1,1,2 do CF.place("StreetLight",qc+Vector2.new(k*(W/2-4),0),Vector3.new(-k,0,0),nil,nil,f,SURF+0.25,0.1) end
					stats.parking+=1
				elseif not done then
					-- pocket park
					local W=q-24
					part(f,Vector3.new(W,0.6,W),CFrame.new(qc.X,SURF-0.08,qc.Y),Enum.Material.Grass,Color3.fromRGB(88,140,62),"ParkLawn")
					part(f,Vector3.new(W,0.62,9),CFrame.new(qc.X,SURF-0.07,qc.Y),Enum.Material.Concrete,CONC,"Path")
					part(f,Vector3.new(9,0.62,W),CFrame.new(qc.X,SURF-0.07,qc.Y),Enum.Material.Concrete,CONC,"Path")
					for sx=-1,1,2 do for sz=-1,1,2 do
						local base=qc+Vector2.new(sx*W/4,sz*W/4)
						CF.place(rnd()<0.3 and "Tree_Pine" or "Tree_Oak",base,Vector3.new(1,0,0),nil,nil,f,SURF+0.2,0.1)
						CF.place("Tree_Oak",base+Vector2.new(sx*W/7,-sz*W/9),Vector3.new(1,0,0),nil,nil,f,SURF+0.2,0.1)
						CF.place("Bench",qc+Vector2.new(sx*14,sz*W/4),Vector3.new(-sx,0,0),nil,nil,f,SURF+0.2,0.1)
					end end
					CF.place("TrashCan",qc+Vector2.new(9,9),Vector3.new(1,0,0),nil,nil,f,SURF+0.2,0.1)
					stats.park+=1
				end
			elseif clear>=2 then
				for _,s in samples do if not bigRoad(s,14) then
					local ins=false; for _,r in rects do if s.X>r[1]-6 and s.X<r[2]+6 and s.Y>r[3]-6 and s.Y<r[4]+6 then ins=true break end end
					if not ins then CF.place(zone=="downtown" and "Tree_Oak" or pick({"Tree_Oak","Tree_Oak","Tree_Pine","Bush"}),s,Vector3.new(1,0,0),nil,nil,f,SURF,0.1); stats.trees+=1 end
				end end
			end
			if #f:GetChildren()>0 then f.Parent=LOTS else f:Destroy() end
		end end
		if bi%3==0 then task.wait(); if status then status(bi,#blocks) end end
	end
	return stats
end

-- ===== towns =====
local RES={"House_A","House_B","House_C","Duplex_A","Trailer_A","House_A","House_C","Townhouses_A"}
local function flattenStrip(a3,b3,width,top)
	local T=workspace.Terrain; local mid=(a3+b3)/2; local L=(b3-a3).Magnitude
	local cf=CFrame.lookAt(Vector3.new(mid.X,top,mid.Z),Vector3.new(b3.X,top,b3.Z))
	T:FillBlock(cf*CFrame.new(0,-4.3,0),Vector3.new(width+8,8,L+4),Enum.Material.Ground)
	T:FillBlock(cf*CFrame.new(0,15,0),Vector3.new(width+8,30,L+4),Enum.Material.Air)
end
function F.towns(HV)
	local stats={houses=0,props=0,moved=0,removed=0}
	for ti,ts in G.TOWN_STREETS do
		local f=HV.Towns:FindFirstChild("Town"..ti); if not f then continue end
		local dir,a=ts.dir,ts.a; local perp=Vector2.new(-dir.Y,dir.X)
		local roadTop=ts.el+1.9
		-- 1) clear the slot for the cross street, re-seat the rest on the terrain
		for _,m in f:GetChildren() do
			local c=m:GetBoundingBox(); local v=Vector2.new(c.X,c.Z)-a
			local t,o=v:Dot(dir),v:Dot(perp)
			if math.abs(t-300)<62 and math.abs(o)<160 then m:Destroy(); stats.removed+=1
			else bottomTo(m,m.Name:find("StreetLight") and roadTop+0.4 or math.max(roadTop,groundY(Vector2.new(c.X,c.Z)))+0.05); stats.moved+=1 end
		end
		local X=Instance.new("Folder"); X.Name="Additions"
		-- 2) main street sidewalks + props
		for s=-1,1,2 do
			for _,seg in {{0,284},{316,560}} do
				local t0,t1=seg[1],seg[2]; local mid=a+dir*((t0+t1)/2)+perp*s*22
				local cf=CFrame.lookAt(Vector3.new(mid.X,roadTop+0.2-0.6,mid.Y),Vector3.new(mid.X+dir.X,roadTop-0.4,mid.Y+dir.Y))
				part(X,Vector3.new(10,1.2,t1-t0),cf,Enum.Material.Concrete,CONC,"Sidewalk")
			end
			for t=40,540,105 do if math.abs(t-300)>40 then
				local p=a+dir*t+perp*s*22
				if CF.place(ti%2==0 and "Tree_Oak" or "Tree_Palm",p,V3(-perp*s),nil,nil,X,roadTop+0.4,0.1) then stats.props+=1 end
				local p2=a+dir*(t+22)+perp*s*24
				local it=pick({"Bench","TrashCan","Hydrant","Bench"})
				if CF.place(it,p2,V3(-perp*s),nil,nil,X,roadTop+0.4,0.1) then stats.props+=1 end
			end end
		end
		CF.place("StopSign",a+dir*270+perp*20,V3(dir),nil,nil,X,roadTop+0.4,0.1)
		-- 3) cross street through the middle of town
		local W=28
		for s=-1,1,2 do
			local p0=a+dir*300+perp*s*17; local p1=a+dir*300+perp*s*430
			local a3=Vector3.new(p0.X,roadTop,p0.Y); local b3=Vector3.new(p1.X,roadTop,p1.Y)
			flattenStrip(a3,b3,W,roadTop-0.3)
			local mid=(a3+b3)/2
			local rp=part(X,Vector3.new(W,2,(b3-a3).Magnitude+2),CFrame.lookAt(mid,b3)*CFrame.new(0,-1,0),Enum.Material.Asphalt,Color3.fromRGB(56,58,62),"CrossStreet")
			for _,side in {-1,1} do
				local smid=mid+V3(dir)*side*(W/2+5)
				part(X,Vector3.new(10,1.2,(b3-a3).Magnitude),CFrame.lookAt(smid,smid+(b3-a3)),Enum.Material.Concrete,CONC,"Sidewalk").CFrame*=CFrame.new(0,-0.4,0)
			end
			for u=70,400,110 do CF.place("StreetLight",a+dir*(300+W/2+5)+perp*s*u,V3(-dir),nil,nil,X,roadTop+0.4,0.1) end
			-- houses on both sides of the cross street
			for _,v in {-1,1} do
				for k,u in {200,300,400} do
					local p=a+dir*(300+v*(W/2+10+46))+perp*s*u
					local gy=groundY(p)
					if CF.place(pick(RES),p,V3(-dir*v),92,90,X,math.max(gy,roadTop-0.2),0.45) then stats.houses+=1 end
				end
			end
		end
		X.Parent=f
		task.wait()
	end
	return stats
end
return F
