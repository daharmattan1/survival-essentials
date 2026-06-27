# Mid-Atlantic / Appalachian — Survival Crops (CROP)

> Calorie- and storage-dense crops chosen for **USDA zone 7a** (Baltimore baseline: last frost ≈
> mid-April, first frost ≈ late October). CROP entries (`../../../SCHEMAS.md` §3): zone fit, planting
> windows, growing, harvest/storage, **seed saving**, and `## ⚠ MANDATORY PREPARATION` where any part
> needs processing to be edible (dry beans must be cooked).
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Calendar:
> [`../seasonality.md`](../seasonality.md).

---

## Synthesis

A survival garden is a **calorie and storability** play, not a salad garden — energy density and
months-long storage beat fresh-eating crops. The chosen set for 7a are reliable, calorie- or
protein-dense, and **storable through winter**: potato (starch king), dry beans (protein + carbs,
stores for years), winter squash (calories + 3–6 month storage), kale/collards (frost-hardy greens
that extend the season), and flint/dent corn (dry-stored carbs). All fit the 7a frost window with a
spring planting after mid-April and harvest before the late-October frost; kale/collards push into
cold weather. **Seed saving** is what turns a garden into a renewable food source — open-pollinated
lines (beans, corn, squash) come true; save them.

## Load order (this domain)

```
Planning what to grow?  → pick from the manifest by calorie density + storability + days-to-maturity
Planting now?           → the crop entry's "Planting Windows (Zone 7a)" (last frost ≈ mid-Apr)
Keeping the line going?  → the entry's "Seed Saving" (open-pollinated vs hybrid)
Any part needs processing to eat?  → ⚠ MANDATORY PREPARATION (e.g. dry beans MUST be cooked)
Calendar context: ../seasonality.md (plant after mid-Apr; harvest/cure before late-Oct frost).
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| potato | entries/potato.md | CROP | mid-atlantic-appalachian | plant Apr, harvest Jul–Sep | edible-when-prepared | low | none | false | T1 | 3 | present |
| beans-dry | entries/beans-dry.md | CROP | mid-atlantic-appalachian | plant May, harvest Aug–Sep | edible-when-prepared | moderate | none | false | T1 | 4 | present |
| winter-squash | entries/winter-squash.md | CROP | mid-atlantic-appalachian | plant May–Jun, harvest Sep–Oct | edible-when-prepared | low | none | false | T1 | 3 | present |
| kale-collards | entries/kale-collards.md | CROP | mid-atlantic-appalachian | plant Apr & Aug, harvest into winter | edible-raw | none | none | false | T1 | 3 | present |
| corn-flint | entries/corn-flint.md | CROP | mid-atlantic-appalachian | plant May, harvest Sep–Oct | edible-when-prepared | low | none | false | T1 | 4 | present |

`beans-dry` is `hazard_severity: moderate` + `preparation_required: true` (raw/undercooked dry beans
contain lectins → must be cooked; the entry carries `## ⚠ MANDATORY PREPARATION`). Potato note: green
tubers/sprouts (solanine) — handled in-entry. Sources: USDA / state extension (T1).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each CROP entry carries "Planting Windows (Zone 7a)" + "Seed Saving"; `preparation_required:
      true` crops (dry beans) carry `## ⚠ MANDATORY PREPARATION`.
- [ ] Frost dates consistent with the biome profile (last ≈ mid-Apr, first ≈ late-Oct).
