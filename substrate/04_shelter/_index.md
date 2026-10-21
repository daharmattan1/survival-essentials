# 04_shelter — Shelter & Thermoregulation (METHOD)

> Universal technique: holding core body temperature. In harsh conditions, exposure works in hours,
> faster than thirst and far faster than hunger. Shelter comes after getting out of immediate danger
> and treating life-threatening injury. METHOD entries (`../../SCHEMAS.md` §6): goal, steps, failure
> modes.
>
> Survey doorway: [`../../04_shelter.md`](../../04_shelter.md). Retrieval recipe D in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Shelter is a heat-management problem, not a construction project. Three things take your heat, in this
order: wet clothing, cold ground and wind. So pick a **site** that is not itself a hazard (lightning,
flash-flood channel, avalanche or rockslide path, dead trees, cold hollow), keep dry, put an
**insulating barrier between you and the ground**, then build only as much **enclosure** as the weather
demands — a small, well-insulated space your body can actually heat beats a large drafty one.
Overbuilding burns calories you cannot spare; a debris pile you can warm is better than a mansion you
cannot. Three newer entries cover the common set-ups: **tarp configurations** (lean-to, A-frame, poncho
tent, with the ground layer as important as the roof), the **cold-weather sleep system** (ground layer,
dry sleep clothes, cover and waterproof outer layer, built bottom up), and **vehicle as shelter**
(stay with the car, clear the tailpipe, never sleep with the engine running).

## Load order (this domain)

```
1. site-selection-and-hazards     — choose ground that won't kill you (water/wind/deadfall/cold-pocket)
2. insulation-and-ground-barrier  — get OFF the cold ground before you build the roof (bed first, then the roof)
3. emergency-shelter-types        — build the smallest enclosure the weather requires
4. tarp-configurations            — if you have a tarp or poncho: choose a pitch (lean-to, A-frame, poncho tent), rig the ridgeline
5. cold-weather-sleep-system      — for the night: ground layer, dry sleep clothes, cover, waterproof outer layer
Stranded in a car in winter?      → vehicle-as-shelter (stay with the vehicle; clear the tailpipe; never sleep with the engine running)
Burn nothing inside a tent, vehicle, tarp shelter, debris hut or snow shelter (no stove, lantern, candle or heater); a vent does not fix it. The only car carve-out is the engine, per vehicle-as-shelter.
Principle: a small space you can heat > a large space you can't. Don't sweat building it (wet = cold).
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| site-selection-and-hazards | entries/site-selection-and-hazards.md | METHOD | universal | n/a | n/a | moderate | n/a | n/a | T2 | 10 | agent-verified |
| insulation-and-ground-barrier | entries/insulation-and-ground-barrier.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 4 | agent-verified |
| emergency-shelter-types | entries/emergency-shelter-types.md | METHOD | universal | n/a | n/a | moderate | n/a | n/a | T2 | 11 | agent-verified |
| tarp-configurations | entries/tarp-configurations.md | METHOD | universal | n/a | n/a | low | n/a | false | T1 | 12 | agent-verified |
| vehicle-as-shelter | entries/vehicle-as-shelter.md | METHOD | universal | n/a | n/a | lethal | n/a | false | T1 | 13 | agent-verified |
| cold-weather-sleep-system | entries/cold-weather-sleep-system.md | METHOD | universal | n/a | n/a | moderate | n/a | false | T1 | 12 | agent-verified |

`site-selection-and-hazards` carries `hazard_severity: moderate` (the site itself can kill);
`vehicle-as-shelter` is `lethal` (carbon monoxide in a stranded vehicle). Sources: ATP 3-50.21
chapter 6 (primary) with NWS, CDC, Forest Service and NPS pages (T2).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each METHOD entry follows the skeleton; site-hazard failure modes (flood/wind/deadfall/cold)
      stated explicitly.
