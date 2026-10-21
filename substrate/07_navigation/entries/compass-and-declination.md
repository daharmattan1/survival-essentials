---
entry_id: compass-and-declination
title: Compass and Declination (Take, Follow and Correct a Bearing)
type: METHOD
domain: substrate/07_navigation
region_scope: universal
usda_zone: n/a
confidence: medium
source_tier: T1
sources:
  - title: "How do I get my map and compass to face the same direction? (baseplate on the map's north-south border line; subtract if declination is positive, add if negative; metal such as rebar)"
    publisher: U.S. Geological Survey
    url: "https://www.usgs.gov/educational-resources/how-get-your-map-and-compass-face-same-direction"
    tier: T1
  - title: "Adjustable declination compasses (set the offset once instead of adding or subtracting)"
    publisher: U.S. Geological Survey
    url: "https://www.usgs.gov/educational-resources/adjustable-declination-compasses"
    tier: T1
  - title: "Finding Your Way with Map and Compass (USGS Fact Sheet 079-99, February 2000: MN arrow right of true north subtract, left add; declination diagram is representational; iron and steel warning)"
    publisher: U.S. Geological Survey
    url: "https://pubs.usgs.gov/fs/0079-99/report.pdf"
    tier: T1
  - title: "Magnetic Declination (definition; positive east, negative west; add declination to a magnetic bearing to get a true bearing; calculators)"
    publisher: NOAA National Centers for Environmental Information
    url: "https://www.ncei.noaa.gov/products/magnetic-declination"
    tier: T1
  - title: "Geomagnetism Frequently Asked Questions (local variation, anomalies, models renewed every five years, unreliable near the magnetic poles)"
    publisher: NOAA National Centers for Environmental Information
    url: "https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions"
    tier: T1
  - title: "World Magnetic Model (WMM2025 valid to December 31, 2029; new version every five years)"
    publisher: NOAA National Centers for Environmental Information
    url: "https://www.ncei.noaa.gov/products/world-magnetic-model"
    tier: T1
  - title: "TC 3-25.26, Map Reading and Land Navigation (15 Nov 2013), ch. 6 paras 6-3, 6-11 to 6-16, 6-18, 6-19 and Table 6-1; ch. 8 paras 8-4, 8-5, 8-15; ch. 10 paras 10-36 to 10-39"
    publisher: U.S. Department of the Army
    url: "https://armyrotc.mst.edu/media/academic/armyrotc/documents/manualsadpadrpfmetc/TC%203-25.26.pdf"
    tier: T2
  - title: "Compass (Great Smoky Mountains National Park: declination, where to find it on USGS and NPS maps)"
    publisher: National Park Service
    url: "https://www.nps.gov/grsm/planyourvisit/compass.htm"
    tier: T1
  - title: "If You Get Lost (a compass is a backup; staying put is better if you are not confident of the route)"
    publisher: USDA Forest Service
    url: "https://www.fs.usda.gov/visit/know-before-you-go/if-you-get-lost"
    tier: T1
  - title: "What do the different north arrows on a USGS topographic map mean? (true north, grid north, magnetic north)"
    publisher: U.S. Geological Survey
    url: "https://www.usgs.gov/faqs/what-do-different-north-arrows-a-usgs-topographic-map-mean"
    tier: T1
method_for: Take a bearing from a map, correct it for declination, set it on a baseplate compass, follow it, and use a back bearing
materials: [baseplate compass, paper topographic map of the area, pencil, current declination for your location written on the map]
difficulty: moderate
hazard_severity: low
preparation_required: false
expert_id_required: false
last_reviewed: draft
review_status: draft
---

## Goal & When To Use

A compass shows direction when you cannot see where you are going. The catch is that its needle points to magnetic north, and the map is drawn to true north. The gap between the two is **declination**. Skip the correction and you walk a line off by that many degrees [3][4].

Use this entry when you already have a map and a baseplate compass (a compass on a flat clear plate you lay on the map) and have decided to travel: a planned route, or a move that cannot wait. If you are lost and not very, very confident of the route, the Forest Service says it is better to stay put [9]. See [`07_navigation.md`](../../../07_navigation.md#if-you-think-you-are-lost-right-now) first. A compass is a backup for a phone, not a reason to leave a spot you should stay in [9].

Pace counting and aiming off: [`dead-reckoning-and-pace.md`](dead-reckoning-and-pace.md). Contour lines: [`terrain-and-map-reading.md`](terrain-and-map-reading.md).

---

## Parts of a baseplate compass

These names vary by maker. Check yours against its manual.

- **Baseplate:** the flat plate you lay on the map [1].
- **Dial (also called the housing or ring):** the turning ring marked 0 to 360 degrees [1].
- **Magnetic needle:** the red-tipped needle that swings to magnetic north [1].
- **Orienting arrow:** the outlined arrow printed inside the dial. You turn the dial until the needle sits on top of it [1][2].
- **Direction-of-travel arrow:** the arrow on the baseplate that points the way you walk (general practice).
- **Index mark:** the fixed line where the dial meets the travel arrow. The number at this line is the bearing you are using (general practice).

A **bearing** is a direction in degrees from north, 0 to 360. The Army calls it an azimuth [7].

---

## Declination: what it is and how to get the number

NOAA defines declination as the angle between magnetic north and true north. It is **positive when magnetic north is east of true north and negative when it is west**. It changes with place and over time [4].

**Find your number**

1. **Best: NOAA's declination calculator.** Enter your location and date. NOAA points to its geomagnetic calculators page and a phone app, CrowdMag [4]. The model behind the calculators, WMM2025, is valid to December 31, 2029, and NOAA issues a new one every five years [6].
2. **Map margin.** USGS maps carry a declination diagram [8]. It is only a sketch: take the angle from the printed numbers, not from the drawn lines, and remember it was worked out when the map was made, so it may not be current [3].
3. **Old maps.** TC 3-25.26 warns that declination diagrams older than 20 years may give unreliable readings [7]. If the diagram and NOAA disagree, use NOAA's current value (this entry's rule).

**Write the number on the map margin** before you leave home, with its sign (E or W) and the date.

Limits to know [5]:

- Near the magnetic poles a compass is unreliable and declination values are not accurate.
- In rare places, magnetized rock or buried iron pipe makes declination swing by several degrees. NOAA's example is a Minnesota area with a mapped anomaly of 16 degrees east, with anomalies of 12 degrees west a few miles away. Declination can change by tens of degrees within a few miles there [5].

---

## The rule (settled)

| Declination | Map bearing to compass bearing | Compass bearing to map bearing |
|-------------|-------------------------------|-------------------------------|
| **West** (negative) | **ADD** the angle | **SUBTRACT** the angle |
| **East** (positive) | **SUBTRACT** the angle | **ADD** the angle |

Where this comes from:

- USGS: going to the compass, subtract if declination is positive, add if it is negative [1]. Its fact sheet says the same by diagram: if the MN (magnetic north) arrow is to the right of true north, subtract; if to the left, add [3].
- NOAA: to get a true bearing from a magnetic one, add the declination, entering west values as negative. NOAA's example is 10 degrees west written as -10 [4]. That is the "compass to map" column.
- TC 3-25.26: from a grid azimuth to a magnetic azimuth, add for a westerly angle and subtract for an easterly one; the reverse going magnetic to grid [7].

**Grid north is not true north.** A USGS map diagram can show three norths: true north (a star), grid north (GN, the direction of the map's grid lines, the UTM grid on current US Topo maps) and magnetic north (MN) [10]. The rule above is for the angle between true north and magnetic north (declination). The Army's rule is written for the angle between grid north and magnetic north (the G-M angle) [7]. If you line the compass up with the map's grid lines, use the grid-to-magnetic angle printed on the diagram. If you line it up with the map's edge or meridians, use declination. The two angles differ by the gap between grid north and true north, which the diagram also shows [10].

**Sanity check (this entry's arithmetic).** With west declination the compass number comes out larger than the map number. With east declination it comes out smaller. If yours does the opposite, you used the wrong sign. Using the wrong sign doubles the error: a 10-degree mistake becomes 20 degrees, which is about 360 m sideways over 1,000 m, because each degree moves you about 18 m per 1,000 m [7].

**Wrap-around.** There is no 360 on a dial, and 0 and 360 are the same point. If the result is over 360, subtract 360. If it is below 0, add 360 [7].

---

## Steps

### Step 1: Take a bearing from the map

1. Lay the long edge of the baseplate along the line from where you are to where you want to go, with the direction-of-travel arrow toward the goal (general practice).
2. Turn the dial until its north agrees with map north and its lines run parallel to the map's north-south lines (general practice). The number at the index mark is the **map bearing**.
3. This is not yet the number to walk by.

### Step 2: Turn it into a compass bearing

4. Apply the rule: west declination, ADD; east declination, SUBTRACT [1][7]. The result is the **compass bearing**.
5. Turn the dial so the compass bearing sits at the index mark (general practice).

**Compass with a declination adjustment.** Some compasses let you set the offset once. USGS says to turn the orienting arrow against the dial to match local declination, so you no longer add or subtract [2]. For such a compass, if it is already set for local declination, skip the add or subtract and just make sure the dial's north (not the orienting arrow) agrees with map north [1]. Check the setting whenever you travel to a place with a different declination (general practice).

### Step 3: Point yourself along it

6. Lift the compass off the map and hold it flat, level, in front of your body, with the travel arrow pointing away from you (general practice).
7. Turn your whole body until the red needle sits in the orienting arrow (general practice). The travel arrow now points along your route.

### Step 4: Follow it

8. **Do not walk staring at the compass.** TC 3-25.26 says never to walk with the compass open in front of you, because it does not stay steady or level [7].
9. Sight along the travel arrow to a distinctive object on your line: a tree, rock or post. Close the compass, walk to that object, then repeat [7].
10. A good mark is easy to recognize as you approach, is the most distant or highest object you can see on the line, and stays in view. Pick marks as you go, not from the map [7].
11. No good mark ahead? Sight on something behind you along the back bearing until one shows up ahead [7].
12. After a detour, return to the original line when you can, and count only the steps that move you toward the goal [7].

### Step 5: Orient the map with the compass

This lines the map up with the land.

1. Lay the baseplate along the map's north-south border line, travel arrow toward the top of the map. Turn the dial so its north agrees with map north [1].
2. Correct for declination: add or subtract the amount, as in the rule above (subtract if declination is positive, add if negative) [1]. West 10 degrees puts 10 at the index mark. East 10 degrees puts 350 there (this entry's arithmetic: 0 - 10 = -10, and -10 + 360 = 350).
3. Keep the baseplate on the border line, hold map and compass together, and turn both in one motion until the red needle lies over the orienting arrow [1].
4. Compare features around you with the map to find where you are [1].

### Step 6: Back bearings

A **back bearing** is the opposite direction. To get it from a bearing, add 180 if the bearing is 180 or less; subtract 180 if it is more than 180 [7]. TC 3-25.26 warns to take extreme care with the 180 [7].

Uses:

- Finding where you are from two or three landmarks you can name on both the land and the map (resection): take a compass bearing to each, convert it to a map bearing, turn it into a back bearing, and draw it on the map from the landmark toward you. The lines cross where you are [7]. Steps are in [`terrain-and-map-reading.md`](terrain-and-map-reading.md).

---

## Worked examples (arithmetic re-checked)

1. **West 10 degrees, map to compass.** Map bearing 250. West: add. 250 + 10 = **260**. Set 260 at the index mark. Check: larger than 250, as expected for west.
2. **West 10 degrees, compass to map.** Compass reads 260. West: subtract. 260 - 10 = **250**. This undoes example 1.
3. **Army example, west.** Map (grid) azimuth 93, 14 degrees west. Add: 93 + 14 = **107** [7].
4. **Army example, east.** Map (grid) azimuth 303, 17 degrees east. Subtract: 303 - 17 = **286** [7].
5. **Army example, compass to map.** Compass reading 65, 5 degrees west. Subtract: 65 - 5 = **60** [7].
6. **Wrap past 360.** East 12 degrees, map bearing 5. Subtract: 5 - 12 = -7. Add 360: **353** (this entry's arithmetic; the wrap rule is from [7]).
7. **Back bearing and resection line.** You sight a tower at a compass bearing of 130. Declination is 10 degrees west. Compass to map: subtract, 130 - 10 = 120. Back bearing: 120 is 180 or less, so add 180 = **300**. On the map, draw a line from the tower toward you along 300 (this entry's arithmetic).

---

## Interference: what throws a compass off

Iron and steel pull the needle. USGS says to stay away from pocket knives, belt buckles, railroad tracks, trucks and electrical lines when using a compass in the field [3]. It also warns about steel hidden in concrete, such as rebar [1].

TC 3-25.26 suggests keeping the compass about **55 m** from high-tension power lines, **18 m** from a truck, and **10 m** from telegraph or telephone wires and barbed wire. It adds that nonmagnetic metals and alloys do not affect a compass [7].

Phones, speakers and magnetic clasps can also disturb a needle (general practice). Hold the compass out from your body and away from them. If the needle looks lazy or points somewhere that cannot be right, move away from metal and read again. Check it against a direction you already know (general practice; the Army also says to check a compass periodically on a known line [7]).

---

## Failure Modes & Fixes

| Failure | Why it happens | Fix |
|---------|----------------|-----|
| You walk off the line | Wrong sign on declination, or a stale value | Check against the rule table and the sanity check. Look up current declination at NOAA [4]. |
| Needle sticks, swings or drifts | Compass tilted, or near metal, wires or a vehicle | Hold it flat. Step away from the metal distances above. Read again [7]. |
| Dial set to the map bearing instead of the compass bearing | Skipped Step 2 | Redo Steps 1 and 2. |
| You set your adjustable compass once and moved far | Declination differs by place [4] | Reset the offset for the new area. |
| The bearing leads you onto cliffs or into water | A straight line ignores the ground | Check the contours on the map. Stop at the first doubt. Remember the rivers warning: [`river-and-stream-crossing.md`](river-and-stream-crossing.md). |

---

## Sources

1. How do I get my map and compass to face the same direction? U.S. Geological Survey. https://www.usgs.gov/educational-resources/how-get-your-map-and-compass-face-same-direction (T1)
2. Adjustable declination compasses. U.S. Geological Survey. https://www.usgs.gov/educational-resources/adjustable-declination-compasses (T1)
3. Finding Your Way with Map and Compass. USGS Fact Sheet 079-99, February 2000. https://pubs.usgs.gov/fs/0079-99/report.pdf (T1)
4. Magnetic Declination. NOAA National Centers for Environmental Information. https://www.ncei.noaa.gov/products/magnetic-declination (T1)
5. Geomagnetism Frequently Asked Questions. NOAA NCEI. https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions (T1)
6. World Magnetic Model. NOAA NCEI. https://www.ncei.noaa.gov/products/world-magnetic-model (T1)
7. TC 3-25.26, Map Reading and Land Navigation (15 November 2013), U.S. Department of the Army. Ch. 6 paras 6-3 (back azimuth), 6-11 to 6-16 and Table 6-1 (declination, add or subtract, examples, 20-year caution), 6-18 and 6-19 (resection); ch. 8 paras 8-4 and 8-5 (compass interference distances, periodic check) and 8-15 (18 m per degree per 1,000 m); ch. 10 paras 10-36 to 10-39 (following a bearing, steering marks). https://armyrotc.mst.edu/media/academic/armyrotc/documents/manualsadpadrpfmetc/TC%203-25.26.pdf (T2; a university-hosted copy of the Army publication)
8. Compass. Great Smoky Mountains National Park, National Park Service. https://www.nps.gov/grsm/planyourvisit/compass.htm (T1)
9. If You Get Lost. USDA Forest Service. https://www.fs.usda.gov/visit/know-before-you-go/if-you-get-lost (T1)
10. What do the different north arrows on a USGS topographic map mean? U.S. Geological Survey. https://www.usgs.gov/faqs/what-do-different-north-arrows-a-usgs-topographic-map-mean (T1)
