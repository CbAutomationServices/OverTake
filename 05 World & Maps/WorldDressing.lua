-- WorldDressing: venues, small towns, countryside trees, touge guardrails.
local W={}
local G=require(game.ServerStorage.HorizonValleyGen:Clone()); G.buildRoadData()
local CF=require(game.ServerStorage.CityFill:Clone())
local KIT=game.ServerStorage.OT_Kit
local S=10.9
local function P(px,py) return Vector2.new((px-550)*S,(py-581)*S) end
local RP=RaycastParams.new(); RP.FilterType=Enum.RaycastFilterType.Include; RP.FilterDescendantsInstances={workspace.Terrain}
local function groundY(p)
	local r=workspace:Raycast(Vector3.new(p.X,1500,p.Y),Vector3.new(0,-3000,0),RP)
	if r then return r.Position.Y,r.Material end
	return 0,nil
end
W.groundY=groundY
W.G=G
local seed=777
local function rnd() seed=(seed*1103515245+12345)%2147483648; return seed/2147483648 end
local function V3(v2) return Vector3.new(v2.X,0,v2.Y) end
local function place(name,p,facing,maxW,maxD,parent,minScale)
	local y=groundY(p)
	return CF.place(name,p,facing,maxW,maxD,parent,y,minScale or 0.1)
end
function W.venues(parent)
	local V=Instance.new("Folder"); V.Name="Venues"; V.Parent=parent
	local sp=G.SPEEDWAY; local c=sp.c
	place("Grandstand",c+Vector2.new(0,sp.rz+sp.width/2+70),Vector3.new(0,0,-1),nil,nil,V)
	place("Grandstand",c+Vector2.new(-360,sp.rz+sp.width/2+70),Vector3.new(0,0,-1),nil,nil,V)
	place("PitBuilding",c+Vector2.new(0,-sp.rz+sp.width/2+55),Vector3.new(0,0,-1),nil,nil,V)
	place("Billboard",c+Vector2.new(sp.rx+60,0),Vector3.new(-1,0,0),nil,nil,V)
	-- drag strip
	local a,b=G.DRAG.a,G.DRAG.b; local d=(b-a).Unit; local n=Vector2.new(-d.Y,d.X)
	place("DragStartTower",a+d*40+n*(G.DRAG.width/2+40),V3(-n),nil,nil,V)
	for k=1,5 do for s=-1,1,2 do place("Bleachers",a+d*(120+k*260)+n*s*(G.DRAG.width/2+40),V3(-n*s),nil,nil,V) end end
	place("Billboard",b+d*60,V3(-d),nil,nil,V)
	-- festival
	place("FestivalHub",P(560,470),Vector3.new(0,0,1),nil,nil,V)
	-- coast: lighthouse + pier
	local lp=P(152,772); place("Lighthouse",lp+Vector2.new(60,40),Vector3.new(-1,0,0),nil,nil,V)
	local pier=KIT.OT_Pier:Clone(); local ocean=Vector2.new(-0.917,0.399)
	local cf,sz=pier:GetBoundingBox()
	local long=sz.Z>sz.X and Vector3.new(0,0,1) or Vector3.new(1,0,0)
	local ang=math.atan2(ocean.X,ocean.Y)-math.atan2(long.X,long.Z)
	pier:PivotTo(CFrame.new(cf.Position)*CFrame.Angles(0,ang,0)*CFrame.new(-cf.Position)*pier:GetPivot())
	local pb=P(244,893); local c2,s2=pier:GetBoundingBox(); local center=pb+ocean*120
	pier:PivotTo(pier:GetPivot()+Vector3.new(center.X-c2.X,0.5-(c2.Y-s2.Y/2),center.Y-c2.Z)); pier.Parent=V
	return V
end
local TOWN={
	{"GasStation_B","Diner_B","Storefront_A","CornerShop_A","Barber_A","Bar_A","Convenience_A","Laundromat_A","Church_A","House_A","House_C","Duplex_A","Motel_A"},
	{"GasStation_B","Storefront_A","Diner_B","FireStation_A","Farm_A","House_B","House_A","Convenience_A","Bar_A","AutoParts_A","Duplex_A","Trailer_A","Church_A"},
	{"GasStation_B","Diner_B","Motel_A","Storefront_A","Bar_A","House_C","Trailer_A","House_B","CardShop_A","CornerShop_A","Trailer_A","House_A"},
	{"GasStation_B","Convenience_A","Storefront_A","Diner_B","TunerShop_A","Barber_A","House_A","House_B","Duplex_A","Laundromat_A","Church_A","House_C"},
}
function W.towns(parent)
	local T=Instance.new("Folder"); T.Name="Towns"; T.Parent=parent
	local n=0
	for ti,ts in G.TOWN_STREETS do
		local f=Instance.new("Folder"); f.Name="Town"..ti; f.Parent=T
		local list=TOWN[ti] or TOWN[1]; local k=0
		local perp=Vector2.new(-ts.dir.Y,ts.dir.X)
		for t=90,540,105 do
			for s=-1,1,2 do
				k+=1; local name=list[(k-1)%#list+1]
				local p=ts.a+ts.dir*t+perp*s*(17+10+55)
				if CF.place(name,p,V3(-perp*s),100,110,f,ts.el,0.45) then n+=1 end
			end
			for s=-1,1,2 do local p=ts.a+ts.dir*(t+52)+perp*s*(17+6); if CF.place("StreetLight",p,V3(-perp*s),nil,nil,f,ts.el,0.1) then n+=1 end end
		end
		task.wait()
	end
	return n
end
local REMOVE={"PineNeedles","Mulch","Sand__","Root"}
local function strip(m) for _,d in m:GetDescendants() do if d:IsA("BasePart") then for _,k in REMOVE do if d.Name:find(k) then d:Destroy() break end end end end end
function W.trees(parent,cap)
	local Tf=Instance.new("Folder"); Tf.Name="Nature"; Tf.Parent=parent
	local templates={}
	for _,nm in {"Tree_Pine","Tree_Oak","Tree_Palm","Bush","Rock_A"} do local t=KIT["OT_"..nm]:Clone(); strip(t); templates[nm]=t end
	local n=0; local step=95
	local chunk=Instance.new("Folder"); chunk.Name="Chunk"
	for x=-5900,5900,step do
		for z=-5900,5900,step do
			if n>=(cap or 2600) then break end
			local p=Vector2.new(x+(rnd()-0.5)*step*0.8,z+(rnd()-0.5)*step*0.8)
			if CF.inPoly(p,G.CITY_POLY) or CF.edgeDist(p,G.CITY_POLY)<150 then continue end
			local nearTown=false; for _,t in G.TOWNS do if (p-t[1]).Magnitude<t[2]+80 then nearTown=true end end
			if nearTown then continue end
			if (p-G.SPEEDWAY.c).Magnitude<G.SPEEDWAY.rx+140 then continue end
			if (p-P(560,470)).Magnitude<260 then continue end
			local r=G.roadAt(p.X,p.Y); if r and r[3]<r[4]+30 then continue end
			local y,mat=groundY(p)
			if not mat or mat==Enum.Material.Water or y<3 then continue end
			local pr=rnd(); local nm=nil
			if mat==Enum.Material.LeafyGrass then if pr<0.55 then nm=(rnd()<0.6) and "Tree_Pine" or "Tree_Oak" elseif pr<0.62 then nm="Bush" end
			elseif mat==Enum.Material.Sand then if pr<0.05 and y<20 then nm="Tree_Palm" end
			elseif mat==Enum.Material.Rock or mat==Enum.Material.Snow then if pr<0.03 and y<380 then nm="Rock_A" end
			elseif mat==Enum.Material.Grass then
				if y>70 and y<340 then if pr<0.22 then nm="Tree_Pine" elseif pr<0.25 then nm="Rock_A" end
				elseif pr<0.045 then nm=(rnd()<0.7) and "Tree_Oak" or "Bush" end
			end
			if nm then
				local m=templates[nm]:Clone(); local c,s=m:GetBoundingBox(); local sc=0.8+rnd()*0.6
				m:PivotTo(CFrame.new(c.Position)*CFrame.Angles(0,rnd()*6.28,0)*CFrame.new(-c.Position)*m:GetPivot())
				if sc~=1 then m:ScaleTo(m:GetScale()*sc) end
				c,s=m:GetBoundingBox(); m:PivotTo(m:GetPivot()+Vector3.new(p.X-c.X,y-0.6-(c.Y-s.Y/2),p.Y-c.Z))
				m.Parent=chunk; n+=1
			end
		end
		chunk.Parent=Tf; chunk=Instance.new("Folder"); chunk.Name="Chunk"
		task.wait()
	end
	return n
end
function W.guardrails(parent)
	local Gf=Instance.new("Folder"); Gf.Name="Guardrails"; Gf.Parent=parent
	local n=0
	for _,r in G.roads do if r.kind=="Touge" then
		for i=1,#r.pts-2,2 do
			local a=Vector3.new(r.pts[i].X,r.el[i],r.pts[i].Y); local b=Vector3.new(r.pts[i+2].X,r.el[i+2],r.pts[i+2].Y)
			local cf=CFrame.lookAt((a+b)/2,b); local L=(b-a).Magnitude
			for s=-1,1,2 do
				local p=Instance.new("Part"); p.Anchored=true; p.Size=Vector3.new(0.5,1.3,L+1); p.CFrame=cf*CFrame.new(s*(r.width/2+1.2),2.0,0)
				p.Material=Enum.Material.DiamondPlate; p.Color=Color3.fromRGB(185,190,196); p.Name="Rail"; p.Parent=Gf; n+=1
				local post=Instance.new("Part"); post.Anchored=true; post.Size=Vector3.new(0.6,2.6,0.6); post.CFrame=cf*CFrame.new(s*(r.width/2+1.5),0.9,0)
				post.Material=Enum.Material.Metal; post.Color=Color3.fromRGB(140,146,152); post.Name="Post"; post.Parent=Gf; n+=1
			end
		end
	end end
	return n
end
return W
