# 07_navigation — Navigation Without GPS (METHOD)

> Universal technique: finding and holding direction when GPS is gone. METHOD entries
> (`../../SCHEMAS.md` §6): goal, steps, failure modes. Low direct danger, but a navigation error in
> cold/heat/water compounds into the exposure and dehydration killers — so it inherits the priority
> order indirectly.
>
> Survey doorway: [`../../07_navigation.md`](../../07_navigation.md). Retrieval recipe D in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Navigation without instruments is layered skills. **Celestial** gives you rough direction with no gear
(sun and shadow-tip; Polaris by night in the Northern Hemisphere; Southern Cross in the Southern).
**Terrain and map reading** lets you relate yourself to the land — handrails, catching features, aspect
of slope, reading contour. **Compass and declination** is how you take, follow and correct a bearing:
the needle points to magnetic north and the map is drawn to true north, so west declination means add
map to compass, subtract compass to map, and east is the reverse. **Dead reckoning** is how you hold a
bearing and estimate distance traveled (pace count, calibrated on your own ground) when you cannot see a
landmark. **River and stream crossing** is a decision before it is a technique: turning back is the
default, and moving water kills fast. If you are lost, STOP and stay put; that is the default. Navigate
only when you can place yourself within one landmark, daylight remains and nobody is hurt. Then fix
your position before moving, aim for a feature you cannot overshoot, and do not move blind.

## Load order (this domain)

```
0. Lost? STOP and stay put (default; see ../01_core_principles/entries/stay-or-go-decision.md). Read on only to navigate.
1. celestial-navigation        — get a rough direction with zero gear (sun, shadow-tip, Polaris)
2. terrain-and-map-reading     — place yourself on the land (handrails, catching features, contour)
3. compass-and-declination     — take, follow and correct a bearing (west: add map to compass, subtract compass to map; east: the reverse)
4. dead-reckoning-and-pace     — hold the bearing + estimate distance when no landmark is visible
Water in the way?              → river-and-stream-crossing (turning back is the default; never enter moving water to find your way out)
Rule: navigate only if you can place yourself within one landmark, daylight remains and nobody is hurt;
fix your position BEFORE moving; aim for a feature you can't overshoot; don't move blind.
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| celestial-navigation | entries/celestial-navigation.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 3 | agent-verified |
| terrain-and-map-reading | entries/terrain-and-map-reading.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 5 | agent-verified |
| dead-reckoning-and-pace | entries/dead-reckoning-and-pace.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 5 | agent-verified |
| compass-and-declination | entries/compass-and-declination.md | METHOD | universal | n/a | n/a | low | n/a | false | T1 | 10 | agent-verified |
| river-and-stream-crossing | entries/river-and-stream-crossing.md | METHOD | universal | n/a | n/a | lethal | n/a | false | T1 | 10 | agent-verified |

`river-and-stream-crossing` is `lethal`. Sources: ATP 3-50.21 and TC 3-25.26 (map reading) with Forest
Service, NPS, NOAA and USGS pages (T2).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each METHOD entry follows the skeleton (Goal & When → Steps → Failure Modes & Fixes).
