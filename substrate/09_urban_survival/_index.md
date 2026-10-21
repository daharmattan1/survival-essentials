# 09_urban_survival — Bug-In & Urban Disruption (METHOD / PROTOCOL)

> Universal technique: surviving the *most likely* real scenario — a disruption where you shelter in
> place (power outage, storm, civil disruption) rather than head to the wilderness. Mixed METHOD /
> PROTOCOL. Includes the **sanitation / human-waste** entry, because when plumbing fails, waste can
> reach hands, food and water and spread stomach illness.
>
> Survey doorway: [`../../09_urban_survival.md`](../../09_urban_survival.md). Retrieval recipe D in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

For most people the realistic emergency is **urban and indoors**: the grid drops, water pressure
fails, stores empty, and staying home is the usual plan, unless officials order evacuation or the home
becomes hazardous (CO alarm, gas smell, cannot stay warm or cool, a medical device cannot run). Several
problems dominate. **Power-outage bug-in** is the overview: heat/cold without HVAC, lighting, water,
and the silent killer, carbon monoxide. **Generator and heater CO prevention** goes deeper: nothing
burns inside a home except a vented fireplace or stove in working order, no gas oven or stove for heat,
generators outdoors at least 20 ft from windows, doors and vents, and CO alarms first. **Food safety
during outages** is clocks and thermometers: you cannot tell spoiled food by looking or smelling, and
tasting it is the test agencies rule out. **Extreme heat at home** and **winter storm at home** cover
the two ways a house without power turns dangerous (heat stroke and hypothermia), and the cold-house
mistake of burning something inside to get warm. **Civil-disruption safety**: follow officials' alerts,
shelter in place or evacuate as they direct, know more than one way out. And the one people forget until
it is a crisis — **sanitation and human-waste**: improper waste handling spreads stomach illness
(diarrhea and vomiting) through hands, food and water; the fixes (a lined bucket or bag toilet with an
absorbent, stored away from water, food and children, plus handwashing with soap) are simple but must be
set up early. This is a disease-vector problem as much as a comfort problem.

## Load order (this domain)

```
Grid down at home?         → power-outage-bug-in (heat/cold, lighting, water; the overview)
  ⚠ CO: nothing burns inside a home except a vented fireplace or stove in working order; no gas oven or stove for heat; generators outdoors, at least 20 ft from windows, doors and vents → generator-and-heater-co-prevention
  Fridge or freezer warming, or flooded? → food-safety-during-outages (clocks and thermometers, not looks or smell)
  Hot house, no AC?        → extreme-heat-at-home (heat stroke: call 911, cool the person, give nothing by mouth)
  Cold house, no heat?     → winter-storm-at-home (hypothermia and CO are the two killers; call 911 for any suspected hypothermia, right away for sleepiness or confusion)
Unrest / threat outside?   → civil-disruption-safety (follow officials, shelter in place or evacuate when told, plan two exits)
Toilets will not flush, or plumbing may fail soon? → sanitation-and-human-waste (set up the bucket toilet and handwashing on day one)
Set up sanitation EARLY — it's a disease problem, not a comfort problem.
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| power-outage-bug-in | entries/power-outage-bug-in.md | METHOD | universal | n/a | n/a | high | n/a | n/a | T1 | 16 | reviewed |
| civil-disruption-safety | entries/civil-disruption-safety.md | PROTOCOL | universal | n/a | n/a | moderate | n/a | n/a | T1 | 8 | reviewed |
| sanitation-and-human-waste | entries/sanitation-and-human-waste.md | PROTOCOL | universal | n/a | n/a | high | n/a | n/a | T1 | 5 | reviewed |
| generator-and-heater-co-prevention | entries/generator-and-heater-co-prevention.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | false | T1 | 13 | draft |
| food-safety-during-outages | entries/food-safety-during-outages.md | PROTOCOL | universal | n/a | n/a | high | n/a | false | T1 | 11 | draft |
| extreme-heat-at-home | entries/extreme-heat-at-home.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | false | T1 | 12 | draft |
| winter-storm-at-home | entries/winter-storm-at-home.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | false | T1 | 17 | draft |

`power-outage-bug-in` (`high`) carries the carbon-monoxide warning, and `generator-and-heater-co-prevention`
(`lethal`) goes deeper; `extreme-heat-at-home` and `winter-storm-at-home` are `lethal`;
`sanitation-and-human-waste` (`high`) is a disease-vector protocol citing CDC (T1).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] `power-outage-bug-in` carries the ⚠ carbon-monoxide warning; `sanitation-and-human-waste`
      frames waste as a disease vector and cites a T1 source.
