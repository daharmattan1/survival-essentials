# 09_urban_survival — Bug-In & Urban Disruption (METHOD / PROTOCOL)

> Universal technique: surviving the *most likely* real scenario — a disruption where you shelter in
> place (power outage, storm, civil disruption) rather than head to the wilderness. Mixed METHOD /
> PROTOCOL. Includes the **sanitation / human-waste** entry, because in a prolonged urban outage,
> fecal-borne disease is a leading and underestimated killer.
>
> Survey doorway: [`../../09_urban_survival.md`](../../09_urban_survival.md). Retrieval recipe D/E in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

For most people the realistic emergency is **urban and indoors**: the grid drops, water pressure
fails, stores empty, and the safest move is usually to **bug in** with what you have. Three problems
dominate. **Power-outage bug-in**: heat/cold without HVAC, food safety as the fridge warms, lighting,
and the silent killer — carbon monoxide from generators/grills run indoors. **Civil-disruption
safety**: situational awareness, avoidance over confrontation, securing the home, movement decisions.
And the one people forget until it is a crisis — **sanitation and human-waste**: once plumbing fails,
improper waste handling spreads dysentery and hepatitis fast; the fixes (contain, separate from water
and food, a twin-bucket system, disinfection) are simple but must be set up early. This is a
disease-vector problem as much as a comfort problem.

## Load order (this domain)

```
Grid down at home?         → power-outage-bug-in (heat/cold, food safety, lighting; ⚠ CO = never burn fuel indoors)
Unrest / threat outside?   → civil-disruption-safety (awareness, avoid > confront, secure & decide to move)
Plumbing failed (>24-48h)? → sanitation-and-human-waste (contain waste, separate from water/food; disease vector)
Set up sanitation EARLY — it's a disease problem, not a comfort problem.
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| power-outage-bug-in | entries/power-outage-bug-in.md | METHOD | universal | n/a | n/a | high | n/a | n/a | T1 | 4 | reviewed |
| civil-disruption-safety | entries/civil-disruption-safety.md | PROTOCOL | universal | n/a | n/a | moderate | n/a | n/a | T2 | 4 | reviewed |
| sanitation-and-human-waste | entries/sanitation-and-human-waste.md | PROTOCOL | universal | n/a | n/a | high | n/a | n/a | T1 | 5 | reviewed |

`power-outage-bug-in` (`high`) carries the carbon-monoxide warning; `sanitation-and-human-waste`
(`high`) is a disease-vector protocol citing CDC (T1).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] `power-outage-bug-in` carries the ⚠ carbon-monoxide warning; `sanitation-and-human-waste`
      frames waste as a disease vector and cites a T1 source.
