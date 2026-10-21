# 02_water — Water Treatment (METHOD)

> Universal technique: making found water drinkable. Germs and thirst work in days to weeks, slower
> than bleeding (minutes) and cold (hours), so fix those first. Every method here carries the
> standardized `## ⚠ CONTAMINATION` block (`../../CONVENTIONS.md` §5): what the method **does** and
> **does NOT** handle. No single method covers chemical + biological + viral + protozoan at once.
>
> Survey doorway: [`../../02_water.md`](../../02_water.md). Retrieval recipe B in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Disinfection is not one thing. **Boiling** kills bacteria, viruses and protozoa (including
*Cryptosporidium* and *Giardia*) but removes no chemicals, and can raise nitrate and algal-toxin levels.
**Filters** strain out germs by absolute pore size: 1 micron removes protozoa, 0.3 micron adds bacteria,
and most miss viruses. Filters remove no chemicals. Read the label for "absolute", not "nominal".
**Chemical treatment** (chlorine/iodine) kills bacteria and viruses but does **NOT** reliably kill
*Cryptosporidium*. It works best in clear water (clear cloudy water first; if it stays cloudy, double the dose), and cold water needs a
double dose and a much longer wait, especially for *Giardia*. **UV pens and lamps** treat small amounts
of clear water by labeled dose and leave no protection in the water afterward. **SODIS** (sunlight in a
clear plastic bottle) is a fallback that needs a clear bottle, clear water and strong sun or two cloudy
days; it is not the same as a UV pen. **Pre-treatment** (settling, decanting, straining) clears water
but does not disinfect it, so something must follow. **Floodwater, fuel, chemical spills and algal
blooms cannot be made drinkable at home**: use bottled or stored water that stayed out of the floodwater. Sourcing and storage decide how
much treatment you even need. The job of every entry is to state plainly **which threats remain after
this method** so a reasoning AI never implies one method made water fully drinkable.

## Load order (this domain)

```
Always read the ⚠ CONTAMINATION block of the chosen method FIRST, then the steps.
Decision:
  Flood, fuel/chemical smell, oily sheen, "do not drink" notice? → STOP: floodwater-and-chemical-contamination (no home method fixes it; use bottled or stored water that stayed out of the floodwater)
  Cloudy/turbid water?      → pretreatment-settling-and-prefiltering before ANY method (chemicals & UV fail on turbidity)
  Fuel available?           → BOIL (broadest single method; rolling boil 1 min; 3 min above 5,000 ft or if elevation unknown)
  No fuel, have a filter?   → FILTER (read the ABSOLUTE micron rating), then add a disinfectant; viruses pass most filters
  Have a working UV pen, clear water? → uv-treatment (full labeled cycle; boil if in doubt)
  No fuel, no filter?       → CHEMICAL (chlorine/iodine) — but NOT reliable vs Cryptosporidium
  None of the above, sunny? → SODIS (clear PET bottle, clear water, 6 h full sun / 2 days cloudy)
  Where to find it and how to store it? → water-sourcing-and-storage
  Chemical/heavy-metal risk?→ NONE of these remove it — find a different source
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| boil-disinfection | entries/boil-disinfection.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 6 | draft |
| filtration-micron-guide | entries/filtration-micron-guide.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 5 | draft |
| chemical-treatment-chlorine-iodine | entries/chemical-treatment-chlorine-iodine.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 5 | draft |
| solar-sodis | entries/solar-sodis.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 5 | draft |
| water-sourcing-and-storage | entries/water-sourcing-and-storage.md | METHOD | universal | n/a | n/a | moderate | n/a | false | T1 | 9 | draft |
| uv-treatment | entries/uv-treatment.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 7 | draft |
| pretreatment-settling-and-prefiltering | entries/pretreatment-settling-and-prefiltering.md | METHOD | universal | n/a | n/a | moderate | n/a | false | T1 | 6 | draft |
| floodwater-and-chemical-contamination | entries/floodwater-and-chemical-contamination.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 14 | draft |

Every row carries `hazard_severity: moderate|high` because untreated or chemically contaminated water
can make you sick or dehydrate you. Each entry cites T1 sources (CDC, EPA, WHO, state extension) and
reproduces the CONTAMINATION block.

## `check_manifests`

- [x] Every row above maps to an existing file in `entries/`.
- [ ] Every entry file in `entries/` has a row here (no orphans).
- [ ] Required columns filled for every row.
- [ ] Every entry carries the `## ⚠ CONTAMINATION` block with boil time, micron limit, and the
      chemical-vs-biological boundary line.
- [ ] `hazard_severity: high` rows cite a T1 source.
