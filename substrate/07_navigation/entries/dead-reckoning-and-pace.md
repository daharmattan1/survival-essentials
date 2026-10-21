---
entry_id: dead-reckoning-and-pace
title: Dead Reckoning and Pace Counting (Hold a Bearing and Estimate Distance)
type: METHOD
domain: substrate/07_navigation
region_scope: universal
usda_zone: n/a
confidence: medium
source_tier: T2
sources:
  - title: "TC 3-25.26, Map Reading and Land Navigation (15 Nov 2013), ch. 5 paras 5-19 to 5-22 (pace count); ch. 6 paras 6-10 to 6-16 and Table 6-1 (declination); ch. 8 paras 8-4 (compass interference), 8-15 (deliberate offset) and 8-24 (North Star)"
    publisher: U.S. Department of the Army
    url: "https://archive.org/details/map-reading-and-land-navigation-tc-3-25-26"
    tier: T2
  - title: "ATP 3-50.21, Survival (2018), ch. 7 paras 7-35 and 7-36 (Polaris), 7-50 to 7-60 (dead reckoning), 7-54 to 7-57 (steering marks, detours), 7-58 and 7-59 (deliberate offset), 7-67 (attack point)"
    publisher: U.S. Department of the Army
    url: "https://archive.org/details/survival-atp-3-50-21"
    tier: T2
  - title: "Magnetic Declination (definition, sign convention, change with place and time)"
    publisher: NOAA National Centers for Environmental Information
    url: "https://www.ncei.noaa.gov/products/magnetic-declination"
    tier: T1
  - title: "How do I get my map and compass to face the same direction? (subtract if declination is positive, add if negative)"
    publisher: U.S. Geological Survey
    url: "https://www.usgs.gov/educational-resources/how-get-your-map-and-compass-face-same-direction"
    tier: T1
  - title: "Adjustable declination compasses"
    publisher: U.S. Geological Survey
    url: "https://www.usgs.gov/educational-resources/adjustable-declination-compasses"
    tier: T1
method_for: Hold a compass bearing and estimate distance traveled using pace counting, then correct the estimate at known features
materials: [compass (needed for a bearing), a measured stretch of ground similar to the ground you will cross, map optional, pebbles or a notebook to keep count]
difficulty: moderate
hazard_severity: low
last_reviewed: 2026-06-27
review_status: reviewed
---

## Goal & When To Use

Dead reckoning means walking a known direction for an estimated distance to get from one point to another. Use it when fog, snow, darkness or dense trees hide landmarks. It is highly accurate only over short distances, and errors from the compass and the pace count add up the farther you go without a check (ATP 3-50.21 paras 7-52, 7-53, 7-60).

If you are lost and not hurt, the default is still to stop and stay put, not to dead-reckon (see `01_core_principles.md` and `07_navigation.md`). This method is for travel you have already decided is right: a planned route, or a move that cannot wait.

---

## Steps

### Step 1: Calibrate your pace

An Army pace is **one natural step, about 30 inches** (TC 3-25.26 para 5-20). This is not a double-step. Counting only each right-foot step halves the numbers below (arithmetic, general practice).

1. Walk a measured course on ground like the ground you will cross. A pace course can be 100 m to 600 m. A count taken on flat ground does not carry over to hills (TC 5-20).
2. Count your paces. On a 600 m course, divide the total by 6 to get paces per 100 m (TC 5-20).
3. Know that number. TC 3-25.26 gives this example: a person who normally takes 120 paces per 100 m may take 130 or more going up a slope (TC 5-22). Your own number will differ.

What changes your pace (TC 3-25.26 para 5-22):

- Slope: a pace lengthens downhill and shortens uphill, so the count per 100 m rises going up.
- Wind: a head wind shortens the pace and a tail wind lengthens it.
- Surface: sand, gravel, mud and snow tend to shorten it.
- Weather and clothing: falling snow, rain or ice shorten it; excess clothing and boots with poor traction also affect it (TC 3-25.26 5-22).
- Visibility: fog, rain or darkness shorten it.

Do not hold the count in your head. Move a pebble to a pocket every 100 m, tie a knot in a string, or make a mark in a notebook (TC 3-25.26 para 5-21).

### Step 2: Get a compass bearing, with declination

A compass needle points to magnetic north. Maps are drawn to grid or true north. **Declination** is the angle between magnetic north and the map's north. NOAA defines it as the angle between magnetic north and true north, positive when east and negative when west, and says it changes with location and over time (NOAA NCEI). TC 3-25.26 states the correction against grid north, using the grid-magnetic (G-M) angle printed in the map's declination diagram (paras 6-10, 6-11, 6-14). Use the diagram on your map. TC 3-25.26 cautions that a diagram older than 20 years may be unreliable (para 6-11); in that case look up current declination at NOAA NCEI.

**Add or subtract exactly as follows (TC 3-25.26 para 6-14 and Table 6-1):**

| Declination (G-M angle) | Map bearing to compass bearing | Compass bearing to map bearing |
|-------------------------|--------------------------------|--------------------------------|
| West | ADD the angle | SUBTRACT the angle |
| East | SUBTRACT the angle | ADD the angle |

Examples from Table 6-1: a map (grid) azimuth of 93 with a 14-degree west angle gives a compass reading of 107. A map azimuth of 303 with a 17-degree east angle gives 286. A compass reading of 65 with a 5-degree west angle gives a map azimuth of 60. USGS gives the same rule for map to compass: subtract if declination is positive (east), add if negative (west).

If you add when you should subtract, your error is twice the declination. TC 3-25.26 warns that a one-degree slip can matter in the field (para 6-16).

To take a bearing from the map with a baseplate compass (general practice, with the declination rule above):

1. Lay the long edge of the baseplate along the line from where you are to where you want to go, direction-of-travel arrow toward the goal.
2. Turn the housing until its north lines up with map north and its lines run parallel to the map's north-south lines. The number at the index mark is the map bearing.
3. Apply the table above to get the compass bearing.
4. Turn the housing until the number at the index mark equals the compass bearing. Lift the compass off the map, hold it flat, and turn your whole body until the red needle sits in the orienting arrow. The direction-of-travel arrow now points along your route.

A compass with adjustable declination lets you set the offset once, so you do not add or subtract afterward (USGS, Adjustable declination compasses). Reset it when you travel to a place with a different declination.

Keep metal away from the compass. TC 3-25.26 para 8-4 suggests about 55 m from high-tension power lines, 18 m from a truck, and 10 m from telegraph, telephone and barbed wire.

### Step 3: Walk the bearing

1. Sight along the arrow to a distinctive object on the line, close the compass, and walk to that object. Repeat. Do not walk with the compass open in front of you; it does not stay steady or level (ATP 3-50.21 para 7-54).
2. A good steering mark is easy to recognize as you approach, is the farthest or highest object on the line, and stays in view. Pick marks as you go, not from the map (ATP 7-55).
3. If there is nothing good ahead, sight on something behind you along the back bearing until a mark appears ahead (ATP 7-55).
4. When an obstacle forces a detour, count only the paces that move you toward the destination, and return to the original line when you can (ATP 7-57).

With no compass, a straight line is much harder to hold. Rough direction from the sun or Polaris (see `celestial-navigation.md`) plus the same steering-mark method is the fallback (general practice). Expect drift and circling, and check against terrain often.

### Step 4: Count paces and estimate distance

1. Start at a known point and reset the count to zero.
2. Walk the bearing and keep the count (Step 1).
3. Distance = (paces counted ÷ your paces per 100 m) × 100 m.

**Example:** your count is 120 paces per 100 m. You have counted 480 paces. Distance = (480 ÷ 120) × 100 m = 400 m.

### Step 5: Plot your position

1. Start at your known position on the map.
2. Convert your compass bearing to a map bearing (Step 2, compass to map) and draw a line from your start in that direction.
3. Measure your estimated distance along the line with the map's scale and mark it as an estimate. This is your dead-reckoning position.

**Example:** your compass reads 100 degrees and the declination is 10 degrees west. Compass to map is SUBTRACT, so the map bearing is 90 degrees. You walked 400 m. Mark a point 400 m due east of your start.

### Step 6: Correct the error at every known feature

ATP 3-50.21 says compass and pace count are imprecise and the error compounds over distance. The only counter is to reconfirm your location by terrain association or resection (paras 7-52, 7-60).

1. Whenever you reach a feature that is on both the ground and the map, confirm your position there and restart the pace count from zero (ATP 7-60).
2. If the feature is not where your estimate put you, trust the feature and draw your next line from it.
3. Use resection (two or more known points) to correct a position when you can (ATP 7-60; see `terrain-and-map-reading.md`).
4. **Aim off (deliberate offset).** When the goal is on or near a long feature that crosses your route, such as a road, railroad, power line, ridge or stream, steer about 10 degrees to one side of the bearing. When you reach the feature you know which way to turn (ATP 3-50.21 paras 7-58, 7-59; TC 3-25.26 para 8-15). Each degree of offset moves you about 18 m sideways per 1,000 m walked, so 10 degrees over 1,000 m puts you about 180 m to one side (TC 8-15). Pick the side first, write it down, and turn the other way along the feature when you reach it.
5. **Attack point.** From a last easy-to-identify feature, go a counted distance on a precise bearing. About 500 m or less is most desirable (ATP 7-67).

### Step 7: Time as a backup (general practice)

If you lose the pace count, estimate distance from elapsed time. Time yourself over a measured stretch on ground like the ground ahead, then apply that rate. This is less precise than counting. Use it only until the next known feature, then restart a count there.

---

## Failure Modes & Fixes

| Failure | Why it happens | Fix |
|---------|----------------|-----|
| Count says you walked farther than the map shows | Pace was calibrated on different ground; slope, wind, surface or visibility changed your pace (TC 5-22); miscount; counting single steps against a double-step calibration | Recalibrate on ground like the route. Stop and use features, not the count, to fix position. |
| Drift left or right off the bearing | Walked with the compass open, held it unsteady or near metal, or sighted on a mark off the line | Re-take the bearing away from metal. Sight on the farthest or highest mark on the line, close the compass, walk to it (ATP 7-54, 7-55). |
| Lost count mid-route | Distraction, obstacle, injury | Stop. Estimate from elapsed time (Step 7), fix on the next known feature, restart from zero. |
| Compass bearing and sun or star direction disagree | They are supposed to differ by the declination. A compass shows magnetic north; Polaris and the shadow-tip method give true north (ATP 7-36, 7-22; TC 8-24). Also possible: wrong add/subtract sign, or metal near the compass | The compass wins once it has been read away from metal and the declination sign checked. Re-read it, re-check the rule for your declination, then compare with Polaris. Sun methods are approximate; do not override a clean compass reading with one. |
| You reach the expected spot and see nothing | Accumulated error, or a feature hidden by terrain | Stop; do not keep walking past it. Use the long feature you aimed off to, or the last confirmed feature, to relocate. If it is dark or foggy and you cannot place yourself, stay put (`07_navigation.md`). |
| Fog or darkness removes all marks | Poor visibility also shortens your pace (TC 5-22) | Slow down, use the compass and a counted distance, keep legs short, and stop at the first doubt. If error is growing or the ground is dangerous, shelter and wait for visibility. |

---

## Sources

- TC 3-25.26, Map Reading and Land Navigation (15 Nov 2013), U.S. Department of the Army. Ch. 5 paras 5-19 to 5-22 (pace count and the factors that change it); ch. 6 paras 6-10 to 6-16 and Table 6-1 (declination diagram, G-M angle, add/subtract rule, examples, 20-year caution); ch. 8 paras 8-4 (compass interference distances), 8-15 (deliberate offset, 18 m per degree per 1,000 m) and 8-24 (North Star). https://archive.org/details/map-reading-and-land-navigation-tc-3-25-26 (T2).
- ATP 3-50.21, Survival (2018), U.S. Department of the Army. Ch. 7 paras 7-22 (shadow-tip method), 7-35 and 7-36 (Polaris, true north), 7-50 to 7-60 (dead reckoning, error compounding), 7-54 to 7-57 (steering marks, detours), 7-58 and 7-59 (deliberate offset), 7-67 (attack point). https://archive.org/details/survival-atp-3-50-21 (T2).
- Magnetic Declination, NOAA National Centers for Environmental Information. https://www.ncei.noaa.gov/products/magnetic-declination (T1).
- How do I get my map and compass to face the same direction? U.S. Geological Survey. https://www.usgs.gov/educational-resources/how-get-your-map-and-compass-face-same-direction (T1).
- Adjustable declination compasses, U.S. Geological Survey. https://www.usgs.gov/educational-resources/adjustable-declination-compasses (T1).
