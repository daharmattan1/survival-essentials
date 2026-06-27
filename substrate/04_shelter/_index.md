# 04_shelter — Shelter & Thermoregulation (METHOD)

> Universal technique: holding core body temperature. In harsh conditions, exposure kills in hours —
> faster than thirst and far faster than hunger — so shelter ranks just below air in the priority
> order. METHOD entries (`../../SCHEMAS.md` §6): goal, steps, failure modes.
>
> Survey doorway: [`../../04_shelter.md`](../../04_shelter.md). Retrieval recipe D in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Shelter is a heat-management problem, not a construction project. The dominant heat losses are
**conduction into the ground** (most-missed: you lose more heat to cold ground than to cold air) and
**convection from wind and rain**. So the order is: pick a **site** that is not itself a hazard
(flash-flood channel, deadfall, avalanche/rockfall path, low cold-air pocket), put an **insulating
barrier between you and the ground**, then build only as much **enclosure** as the weather demands —
a small, well-insulated space your body can actually heat beats a large drafty one. Overbuilding
burns calories you cannot spare; a debris pile you can warm is better than a mansion you cannot.

## Load order (this domain)

```
1. site-selection-and-hazards     — choose ground that won't kill you (water/wind/deadfall/cold-pocket)
2. insulation-and-ground-barrier  — get OFF the cold ground first (the biggest heat loss)
3. emergency-shelter-types        — build the smallest enclosure the weather requires
Principle: a small space you can heat > a large space you can't. Don't sweat building it (wet = cold).
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| site-selection-and-hazards | entries/site-selection-and-hazards.md | METHOD | universal | n/a | n/a | moderate | n/a | n/a | T2 | 0 | planned |
| insulation-and-ground-barrier | entries/insulation-and-ground-barrier.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 0 | planned |
| emergency-shelter-types | entries/emergency-shelter-types.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 0 | planned |

`site-selection-and-hazards` carries `hazard_severity: moderate` (the site itself can kill).
Sources FM 21-76 (T2).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each METHOD entry follows the skeleton; site-hazard failure modes (flood/wind/deadfall/cold)
      stated explicitly.
