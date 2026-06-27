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

Navigation without instruments is three layered skills. **Celestial** gives you absolute direction
with no gear (sun arc and shadow-stick by day; Polaris via the Big Dipper / Cassiopeia by night;
Southern Cross in the southern hemisphere). **Terrain and map reading** lets you relate yourself to
the land — handrails, catching features, aspect of slope, reading contour. **Dead reckoning** is how
you hold a bearing and estimate distance traveled (pace count, time-and-speed) when you cannot see a
landmark. The cardinal discipline is *the standard navigation rule:* know where you are before you
move, pick a bearing to a catching feature you cannot overshoot, and never walk blind into terrain
you cannot read — most "lost" emergencies are confident movement in the wrong direction.

## Load order (this domain)

```
1. celestial-navigation        — get an absolute direction with zero gear (sun/Polaris/shadow-stick)
2. terrain-and-map-reading     — place yourself on the land (handrails, catching features, contour)
3. dead-reckoning-and-pace     — hold the bearing + estimate distance when no landmark is visible
Rule: fix your position BEFORE moving; aim for a feature you can't overshoot; don't move blind.
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| celestial-navigation | entries/celestial-navigation.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 2 | present |
| terrain-and-map-reading | entries/terrain-and-map-reading.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 2 | present |
| dead-reckoning-and-pace | entries/dead-reckoning-and-pace.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 2 | present |

Sources FM 21-76 / FM 3-25.26 map reading (T2).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each METHOD entry follows the skeleton (Goal & When → Steps → Failure Modes & Fixes).
