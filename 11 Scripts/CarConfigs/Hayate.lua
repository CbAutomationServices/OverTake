--!strict
-- CarConfigs/Hayate  ·  Prototype for Starter A (JDM)  ·  working name, no real brand
-- Registry sheet: 02 Cars/Roster/Starter A - Hayate.md
--
-- HOW TO READ THIS FILE (same rules for every car):
--   { stock = x, elite = y }  → upgradeable. StatResolver blends it by the level of the slot that owns it
--                               (Stock 0% → Street 20% → Sport 40% → Race 60% → Pro 80% → Elite 100%).
--   { grip = x, drift = y }   → blended by the player's Grip ↔ Drift tuning slider (0 = grip, 1 = drift).
--   plain numbers             → the car's fixed DNA. Never changed by parts.
-- Units: distances in studs, speeds in mph, forces in G (multiples of the car's weight), angles in degrees,
--        frequencies in Hz. Mass-free units, so a heavy car and a light car tune the same way.

return {
	id = "Hayate",
	displayName = "Hayate GT", -- working name
	rosterSlot = 1, -- [[Car Stats]] slot #1, Starter A
	category = "JDM",
	archetype = "Agile JDM Corner Carver",
	drivetrain = "RWD", -- "RWD" | "AWD" | "FWD"
	awdFrontSplit = 0, -- only used by AWD (0.35 = 35% front)
	basePR = 70, -- C tier with stock parts
	maxPR = 450, -- Z tier with all Elite parts

	-- Target model dimensions (studs). The chassis MEASURES the real model at spawn;
	-- these are what the 3D model must hit so ortho sheets, model and raycasts match 1:1.
	dims = {
		length = 15.6, width = 6.6, height = 4.4,
		wheelbase = 9.0, trackFront = 5.5, trackRear = 5.6,
		wheelRadius = 1.15, tireWidth = 0.75,
		rideHeight = 0.55, -- ground → bottom of the side skirt
		fenderGap = 0.25,
	},

	-- Weight & inertia: light and nimble. Starter B (muscle) will be the heavy opposite.
	chassis = {
		weightKg = 1150, -- used for the garage stat line + relative feel; physics uses the ratios below
		comHeight = 1.25, -- studs above ground (lower = flatter, harder to tip)
		comFrontBias = 0.52, -- 52% of the weight on the front axle
		yawInertia = 0.85, -- 1 = average car. <1 rotates quicker (snappy JDM)
		pitchInertia = 0.9,
		rollInertia = 0.9,
	},

	suspension = { -- owned by: Suspension
		restLength = 1.5, travel = 1.0,
		freqFront = { stock = 1.55, elite = 2.25 }, -- spring stiffness as ride frequency
		freqRear = { stock = 1.45, elite = 2.15 },
		dampingRatio = { stock = 0.42, elite = 0.62 },
		antiRoll = { stock = 0.35, elite = 0.7 }, -- 0–1, how much body roll is resisted
		rideHeightDrop = { stock = 0, elite = 0.25 }, -- lowered on better suspension
	},

	tires = { -- owned by: Tires
		muPeakFront = { stock = 1.05, elite = 1.5 },
		muPeakRear = { stock = 1.0, elite = 1.45 },
		slipPeakDeg = { stock = 8, elite = 7 }, -- grip peaks at this slip angle
		muSlideRatio = { stock = 0.7, elite = 0.78 }, -- sliding grip ÷ peak grip
		falloffDeg = { stock = 22, elite = 26 }, -- slip angle where grip has fallen to sliding grip
		muLong = { stock = 1.05, elite = 1.45 }, -- launch / braking grip
	},

	steering = {
		lockDeg = 34, -- full lock at low speed
		highSpeedLockDeg = 9, -- lock at lockFadeMph and above (stability at speed)
		lockFadeMph = 130,
		steerRate = 4.5, -- how fast the wheel turns (per second, 0→full)
		returnRate = 6.5,
	},

	drift = { -- the car's drift personality. Easy and floaty, so a new player can drift on day 1.
		minMph = 32,
		entry = { brakeTap = true, handbrake = true, powerOver = true },
		rearGrip = { grip = 0.62, drift = 0.4 }, -- rear grip multiplier while drifting
		maxAngleDeg = { grip = 32, drift = 50 },
		angleHold = { grip = 0.6, drift = 1.0 }, -- strength of the assist that holds your angle
		counterSteer = 0.7, -- 0 = none, 1 = never spins
		speedRetain = 0.93, -- share of speed kept through a slide (arcade)
		recoverTime = 0.35, -- seconds to blend back to full grip
		spinAllowed = false,
	},

	engine = { -- owned by: Engine
		type = "I4", -- sound set + pop character
		idleRpm = 900,
		redline = { stock = 7600, elite = 8800 },
		peakTorqueNm = { stock = 205, elite = 470 },
		-- normalized torque curve (rpm → share of peak). Peaky top end = classic tuner.
		torqueCurve = { { 1000, 0.55 }, { 2500, 0.68 }, { 4000, 0.84 }, { 5600, 1.0 }, { 6800, 0.97 }, { 7600, 0.84 } },
		engineBrake = 0.12, -- G of decel when off throttle
	},

	induction = { -- owned by: Turbo slot (turbo OR supercharger, one at a time)
		default = "Turbo",
		allowed = { "Turbo", "TwinTurbo", "Supercharger", "CentrifugalSC" },
		-- Stock = no boost (naturally aspirated). Boost = extra torque share on top of the engine.
		Turbo = { boost = { stock = 0, elite = 0.6 }, spoolSec = { stock = 1.2, elite = 0.6 }, startRpm = 3000 },
		TwinTurbo = { boost = { stock = 0, elite = 0.55 }, spoolSec = { stock = 0.8, elite = 0.4 }, startRpm = 2500 },
		Supercharger = { boost = { stock = 0, elite = 0.45 }, curve = "flat" }, -- instant, flat from low rpm
		CentrifugalSC = { boost = { stock = 0, elite = 0.5 }, curve = "rising" }, -- instant, grows with rpm
	},

	transmission = { -- owned by: Transmission
		gears = { 3.3, 2.05, 1.45, 1.1, 0.88, 0.72 },
		finalDrive = { stock = 4.1, elite = 4.3 },
		shiftSec = { stock = 0.32, elite = 0.1 },
		autoShiftAt = 0.93, -- upshift at 93% of redline
	},

	brakes = { -- owned by: Brakes
		decelG = { stock = 1.0, elite = 1.55 },
		frontBias = 0.62,
		abs = { stock = 0.5, elite = 0.85 },
		handbrakeG = 1.1, -- rear-only
	},

	aero = {
		vMaxMph = { stock = 128, elite = 205 }, -- owned by: Engine (soft limiter so nothing breaks)
		dragShape = 1.0, -- 1 = average; drag force scales with v²
		downforce = { stock = 0.5, elite = 1.0 }, -- owned by: Suspension (extra grip at 150 mph, in G)
	},

	nitrous = { -- owned by: Nitrous
		style = "Burst", -- "Burst" (short and strong) | "Sustained" (long and smooth)
		capacitySec = { stock = 2.5, elite = 5.5 },
		pushG = { stock = 0.3, elite = 0.55 },
		refillPerSec = { stock = 0.04, elite = 0.08 }, -- passive
		refillOn = { drift = 0.07, nearMiss = 0.15, draft = 0.03 }, -- per second of each (Core Loop)
		fovKick = 12,
	},

	arcade = {
		antiFlip = 0.8, -- self-righting torque
		airControl = 0.5,
		yawDampCentered = 0.55, -- settles slides when steering is centered
		landingAssist = true,
	},

	tuningDefaults = { gripDrift = 0.35, stiffness = 0.5 }, -- leans a bit drifty out of the box

	fx = {
		rollFactor = 1.1, pitchFactor = 1.0, -- visual body motion (light car moves more)
		exhaustPops = { upshift = true, liftOff = true, chance = 0.35 },
		blowOff = true, -- when a turbo is fitted
		smokeSlipDeg = 12, -- tire smoke starts at this rear slip
		skidSlipDeg = 9,
	},
}
