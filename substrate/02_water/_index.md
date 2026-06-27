# 02_water — Water Treatment (METHOD)

> Universal technique: making found water drinkable. **Waterborne pathogens kill faster than
> starvation** — this is the highest-tempo killer in the substrate. Every method here carries the
> standardized `## ⚠ CONTAMINATION` block (`../../CONVENTIONS.md` §5): what the method **does** and
> **does NOT** handle. No single method covers chemical + biological + viral + protozoan at once.
>
> Survey doorway: [`../../02_water.md`](../../02_water.md). Retrieval recipe B in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Disinfection is not one thing. **Boiling** kills everything biological (bacteria, viruses, protozoa
incl. *Cryptosporidium* and *Giardia*) but removes nothing chemical. **Filters** physically strain
protozoa and bacteria but most miss viruses (too small), and they say nothing about chemicals — the
micron rating is the whole story. **Chemical treatment** (chlorine/iodine) kills bacteria and
viruses but does **NOT** reliably kill *Cryptosporidium*, and needs longer contact time in cold or
cloudy water. **SODIS** (solar UV) is a no-resource fallback with strict water-clarity and exposure
limits. Sourcing and storage decide how much treatment you even need. The job of every entry is to
state plainly **which threats remain after this method** so a reasoning AI never implies one method
made water fully drinkable.

## Load order (this domain)

```
Always read the ⚠ CONTAMINATION block of the chosen method FIRST, then the steps.
Decision:
  Cloudy/turbid water?      → pre-settle / pre-filter before ANY method (chemicals & UV fail on turbidity)
  Fuel available?           → BOIL (broadest single method; rolling boil ≥1 min, ≥3 min >2,000 m)
  No fuel, have a filter?   → FILTER (state micron rating) + pair with chemical/UV if virus risk
  No fuel, no filter?       → CHEMICAL (chlorine/iodine) — but NOT reliable vs Cryptosporidium
  None of the above, sunny? → SODIS (clear PET bottle, clear water, 6 h full sun / 2 days cloudy)
  Chemical/heavy-metal risk?→ NONE of these remove it — find a different source
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| boil-disinfection | entries/boil-disinfection.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 4 | reviewed |
| filtration-micron-guide | entries/filtration-micron-guide.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 4 | reviewed |
| chemical-treatment-chlorine-iodine | entries/chemical-treatment-chlorine-iodine.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 4 | reviewed |
| solar-sodis | entries/solar-sodis.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 4 | reviewed |
| water-sourcing-and-storage | entries/water-sourcing-and-storage.md | METHOD | universal | n/a | n/a | moderate | n/a | false | T1 | 4 | reviewed |

Every row carries `hazard_severity: moderate|high` because untreated water is a fast killer — each
entry will cite a **T1** source (CDC / EPA / state extension) and reproduce the CONTAMINATION block.

## `check_manifests`

- [ ] Every row above maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file in `entries/` has a row here (no orphans).
- [ ] Required columns filled for every row.
- [ ] Every entry carries the `## ⚠ CONTAMINATION` block with boil time, micron limit, and the
      chemical-vs-biological boundary line.
- [ ] `hazard_severity: high` rows cite a T1 source.
