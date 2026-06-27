# 11_gear — The 3-Tier Kit (KIT-GEAR)

> Universal: what to carry and stock, organized as three tiers by how far the emergency takes you
> from home. KIT-GEAR entries (`../../SCHEMAS.md` §5): what & why, selection criteria, multi-use,
> failure modes. The lowest-stakes domain — but any item that touches fire, water, or game inherits
> the relevant warning blocks from those domains.
>
> Survey doorway: [`../../11_essential_gear.md`](../../11_essential_gear.md). Retrieval recipe D in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Gear is tiered by scenario radius. **Tier 1 (EDC)** is what is *on your body* — the things that save
you if an emergency starts now: a cutting tool, fire, light, a water-treatment option, basic first-aid.
**Tier 2 (bug-out)** is the grab-and-go bag for leaving home for ~72 hours — water storage and
treatment, shelter (tarp/bivy), more fire and food, a radio. **Tier 3 (home stockpile)** is the
bug-in larder — water and food reserves, power (generator/solar), redundant heat and light. Two
disciplines run across all tiers: **multi-use** (the backpacker's rule — favor items that do 2+
jobs, because weight and space are finite) and **skills over gear** (a tool you cannot use is dead
weight; practice beats accumulation). Buy the cheapest *capable* version, then learn it cold.

## Load order (this domain)

```
What's on me right now?     → edc-tier1-kit (cutting/fire/light/water/first-aid — on-body)
What do I grab to leave?    → bug-out-tier2-kit (~72h: water+shelter+fire+food+radio)
What do I keep at home?     → home-stockpile-tier3 (water/food reserve, power, heat, light)
Cross-cutting: favor multi-use items; skills > gear; buy cheapest *capable*, then drill it.
Any fire/water/game item → inherit that domain's warning blocks (CO, CONTAMINATION, cook temps).
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| edc-tier1-kit | entries/edc-tier1-kit.md | KIT-GEAR | universal | n/a | n/a | none | n/a | n/a | T3 | 2 | present |
| bug-out-tier2-kit | entries/bug-out-tier2-kit.md | KIT-GEAR | universal | n/a | n/a | none | n/a | n/a | T3 | 3 | present |
| home-stockpile-tier3 | entries/home-stockpile-tier3.md | KIT-GEAR | universal | n/a | n/a | none | n/a | n/a | T3 | 3 | present |

Danger facets `none`/`n/a` for gear; T3 (practitioner consensus) is acceptable for gear opinion per
`../../CONVENTIONS.md` §7. Items that treat water / make fire link to those domains' safety blocks.

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each KIT-GEAR entry follows the skeleton (What & Why → Selection Criteria → Multi-Use →
      Maintenance/Failure Modes); fire/water items cross-link the relevant warning blocks.
