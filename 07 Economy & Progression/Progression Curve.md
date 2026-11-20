> **Status:** 🟡 Draft. Nothing here is final until marked 🟢 Locked.


# Progression Curve

How fast a player moves through the game, and why they shouldn't hit a dead-end grind. All numbers → [[Economy Settings]], [[Part Values]], [[Race Settings]].

## Pacing targets
| Moment | Target |
|---|---|
| Behind the wheel | Under 15 seconds after joining |
| First part bought | Before minute 3 |
| Third part bought | By minute 8 |
| First night run | Session 1 or 2 (once the full Street set is done) |
| Reach B tier | Session 2–3 |
| Reach Z tier (first car) | ~4–6 weeks of regular play |

## Grind check: races to afford a full set of parts
Using an average finish worth ~60% of a win:

| Part set | Cost | Raced at tier | Avg day payout | Races needed |
|---|---|---|---|---|
| Street | $10,500 | C | ~$1,500 | ~7 |
| Sport | $42,000 | B | ~$3,600 | ~12 |
| Race | $126,000 | A | ~$8,400 | ~15 |
| Pro | $315,000 | S | ~$18,000 | ~18 |
| Elite | $770,000 | SS | ~$36,000 | ~21 |

Each step takes a bit longer (7 → 21 races), but never jumps. Each tier you climb pays more, so the curve doesn't flatten into a wall.

## Rep check: night races to reach each unlock
| Unlock | Rep to earn | Typical night payout | Night races |
|---|---|---|---|
| Sport (Rep 5) | 3,500 | C ~400 × 1.25 Heat = 500 | ~7 |
| Race (Rep 12) | +15,750 | B ~600 × 1.5 = 900 | ~18 |
| Pro (Rep 22) | +43,750 | A/S ~1,000 × 2 = 2,000 | ~22 |
| Elite (Rep 35) | +94,250 | S/SS ~1,300 × 2.5 = 3,250 | ~29 |

Busts slow this down (you lose unbanked Rep), and higher Heat speeds it up. That's the risk-reward choice: **bank now, or push your Heat?**

## Live tuning
Every number here lives in ConfigService, so payouts can change without a server restart. Plan: A/B test the first-race payout ($3.5k vs $5k) once we have 100+ daily players.
