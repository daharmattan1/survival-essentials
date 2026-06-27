---
entry_id: dead-reckoning-and-pace
title: Dead Reckoning and Pace Counting (Hold a Bearing and Estimate Distance)
type: METHOD
domain: substrate/07_navigation
region_scope: universal
usda_zone: n/a
confidence: high
source_tier: T2
sources:
  - title: "FM 3-25.26: Map Reading and Land Navigation"
    publisher: U.S. Department of Defense
    url: "https://archive.org/details/militarymapread"
    tier: T2
  - title: "FM 21-76: Survival (U.S. Army Field Manual)"
    publisher: U.S. Department of Defense
    url: "https://archive.org/details/fm2176survivalse1992unit"
    tier: T2
method_for: Hold a compass bearing and estimate distance traveled using pace counting and time-and-speed
materials: [compass optional (but highly useful), method works without it, flat ground for pace calibration, map optional]
difficulty: moderate
hazard_severity: low
last_reviewed: 2026-06-27
review_status: reviewed
---

## Goal & When To Use

Dead reckoning means **holding a bearing and estimating distance traveled** so you can locate yourself on a map when landmarks are not visible (fog, night, dense brush). Use this when:

- **Visibility is low** (fog, snow, dense trees).
- **You are traveling between two known points** and need to know when you've arrived.
- **You cannot see landmarks** to fix your position by terrain association.
- **You have a compass** (or can use celestial navigation + pace).

This is the third layer of the navigation standard rule: *hold the bearing + estimate distance when no landmark is visible; aim for a feature you can't overshoot.*

---

## Steps

### Step 1: Calibrate Your Pace

Your "pace" is the number of double-steps (each leg forward) per 100 meters, or per 100 yards. Pace varies by terrain, fitness, slope, and load. Calibrate first.

1. **Measure a known 100-meter (or 100-yard) distance** on flat, open ground (a road, parking lot, field).
2. **Walk the distance at a comfortable speed.** Count double-steps (each time your right foot hits the ground = 1 pace).
3. **Record the number.** Most fit people average 60–65 paces per 100 meters on flat ground (higher if shorter legs; lower if taller).
4. **Repeat 3 times** to confirm. Average the three counts.
5. **Walk the distance again while loaded** (with backpack or gear). Pace may increase 10–20%.

**Standard paces per 100 meters:**
- Fit adult on flat, open ground: 60–65 paces
- Same person on hills uphill: 70–90 paces (slower)
- Same person on hills downhill: 50–60 paces (faster, but less stable)
- Same person in dense brush: 80–100+ paces (slow)
- Shorter person (under 5'6"): 65–75 paces
- Taller person (over 6'): 50–60 paces

**Adjust for night, load, and terrain before using the count for navigation.**

### Step 2: Use a Compass to Establish a Bearing

A compass (or celestial direction if no compass) gives you the bearing to follow.

1. **Orient the compass baseplate** toward your objective or toward the direction you received (from a map or celestial fix).
2. **Rotate the bezel** until the orienting lines align with the map's grid lines (or the direction you want).
3. **Read the bearing** at the direction-of-travel arrow.
4. **Hold the compass flat at waist level** and rotate your body until the red compass needle aligns with the orienting lines inside the bezel.
5. **The direction-of-travel arrow now points toward your objective.** This is your bearing.

**Magnetic declination:** The compass needle points to magnetic north, not true north. On a map, grid north (map's top edge) differs from magnetic north by the declination (printed on the map margin). If the map says declination is 8° West:
- **For bearing from map:** Rotate the bezel 8° counterclockwise from grid north before reading.
- **For bearing to map:** Rotate the bezel 8° clockwise after reading the compass.

(Declination varies by location and time; use the map's stated declination.)

### Step 3: Walk the Bearing Without a Compass

If you have no compass, use your body and landmarks.

1. **Establish the direction** using the sun, moon, stars, or shadow-stick (see celestial-navigation entry).
2. **Pick a distant landmark** in that direction (a tree, rock, peak).
3. **Walk to it**, maintaining course by keeping it in front of you.
4. **Reach the landmark; reestablish direction** (sun, shadow, or celestial if needed).
5. **Pick the next distant landmark** and repeat.

This is slower than compass navigation but works in low visibility if landmarks are spaced 50–200 meters apart.

### Step 4: Count Paces and Estimate Distance Traveled

Count every double-step (every time your right foot, or a consistent foot, hits the ground).

1. **Start at a known point** (a stream junction, marked spot on the map).
2. **Reset your pace counter to zero.**
3. **Walk your bearing.** Count every double-step.
4. **Record the pace count every 100 paces** or every 5 minutes. Write down: time, pace count, bearing, terrain notes.
5. **Calculate distance traveled:** (Pace count ÷ Pace per 100 m) × 100 m = distance.

**Example:** Your pace is 65 paces per 100 m. After 20 minutes, your count is 256 paces.
- Distance = (256 ÷ 65) × 100 m = 394 meters (about 0.25 miles).

### Step 5: Plot Your Position on the Map

As you move, update your location on the map.

1. **Start at your known position** on the map.
2. **Draw a line from this point in the direction of your bearing** (use the compass or a protractor to match the angle).
3. **Measure along this line** the distance you've traveled (using a ruler, or your hand span if no ruler).
4. **Mark this new position.** This is your dead-reckoning position (DR).
5. **Repeat every 15–30 minutes** or whenever major terrain changes (entering a forest, crossing a creek, climbing a hill).

**Example:** Starting at the fork of two streams. You navigate bearing 045° (northeast) for 2.5 kilometers. You mark your DR position 2.5 km along a line at 045° from the stream fork.

### Step 6: Adjust for Terrain and Correct Errors

Dead reckoning accumulates error over time and distance. Correct it.

1. **Verify landmarks.** Every time you pass a recognizable terrain feature (saddle, peak, creek junction), mark it on your map. If the landmark is far from your DR line, you've drifted.
2. **Correct the bearing.** Draw a new DR line from the landmark you just identified, in the direction you're traveling.
3. **Reset pace count to zero** after each landmark fix.

**Error rate:** On good terrain with landmarks, dead reckoning error is typically 5–10% of distance traveled. Over 10 km, expect ±500–1000 m error. Correct frequently.

### Step 7: Use Time and Speed (Alternative)

If you lose track of pace count, time + estimated speed is a backup.

1. **Estimate your walking speed** (usually 3–4 mph on flat open terrain; 1.5–2 mph on steep/brushy terrain).
2. **Record start time.**
3. **After 1 hour, calculate distance:** Speed × time = distance. At 3 mph for 1 hour, you've walked 3 miles.
4. **Plot this distance along your bearing on the map.**

**Caveat:** Speed varies greatly with terrain and load. This method is less precise than pace counting but useful as a backup.

---

## Failure Modes & Fixes

| Failure | Why It Happens | Fix |
|---------|---|---|
| Pace count doesn't match terrain distance (map shows 1 km, but count says 2 km) | Calibration was done on flat ground; actual terrain is steep/brushy, slowing you. Or you miscounted. | Recalibrate your pace on the actual terrain (uphill, downhill, brush). Recount. Stop and use landmarks to fix position instead of relying on pace alone. |
| You drift left or right and miss the bearing | Compass needle drift if near metal; or you're not holding the compass steady. Or you're aiming at a distant landmark that is off-bearing. | Stop. Re-establish the bearing with the compass. Pick a new landmark closer to the bearing line (within 10–20 meters). Recheck bearing every 100 paces. |
| Pace count resets mid-journey and you lose track | Distraction (obstacle, injury, searching for water). | Stop. Estimate elapsed time since last fix. Use time + speed to estimate distance from last landmark. Update the map. Resume pace counting from zero. |
| Compass bearing and celestial direction disagree | Magnetic declination misunderstanding; or compass is near magnetic interference (iron, electronics). | Trust the map's declination. Re-read the compass away from metal. If they still disagree, use the celestial direction as the authoritative bearing (sun/Polaris); adjust compass. |
| You reach what should be your destination but see nothing | DR error accumulation (typical 5–10% error). Landmarks ahead are hidden by terrain, or slightly off-bearing. | Stop. Fix your position using visible landmarks and terrain association. Move 50 m perpendicular to your bearing (left or right) to broaden search. Use a catching feature (a ridge, creek) as backup. |
| You enter dense fog mid-route and can't see landmarks anymore | Visibility zero; DR is your only tool now. Pace count accuracy drops without visual feedback. | Slow down. Use the compass, not landmarks. Count paces very carefully. Increase re-check frequency (every 200 paces instead of 500). If terrain is too dangerous or error is growing, shelter and wait for visibility. |

---

## Sources

- FM 3-25.26: Map Reading and Land Navigation — pace counting, dead reckoning, magnetic declination, compass use (T2).
- FM 21-76: Survival — navigation without instruments, pace measurement, terrain-based bearing (T2).

