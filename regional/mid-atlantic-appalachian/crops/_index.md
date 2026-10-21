# Mid-Atlantic / Appalachian — Survival Crops (CROP)

> Calorie- and storage-dense crops chosen for **USDA zone 7a** (Baltimore baseline: last frost ≈
> mid-April, first frost ≈ late October). CROP entries (`../../../SCHEMAS.md` §3): zone fit, planting
> windows, growing, harvest/storage, **seed saving**, and `## ⚠ MANDATORY PREPARATION` where any part
> needs processing to be edible (dry beans must be soaked and boiled; corn eaten as a staple must be alkali-treated; bitter squash must be thrown away).
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Calendar:
> [`../seasonality.md`](../seasonality.md).

---

## Synthesis

A survival garden is a **calorie and storability** play, not a salad garden — energy density and
months-long storage beat fresh-eating crops. The chosen set for 7a are reliable, calorie- or
protein-dense, and **storable through winter**: potato (starch king), dry beans (protein + carbs,
stores for a long time sealed and dry), winter squash (calories; stores 1–6 months depending on type), kale/collards (frost-hardy greens
that extend the season), flint corn (dry-stored carbs; needs alkali treatment if it is a staple), sweet potato (a warm-season root that
cures and stores through winter; its leaves are also food), and garlic (planted in fall, harvested
early summer; stores about 3–6 months for hardneck, longer for softneck, not in a home fridge). All fit the 7a frost window, but
they do not all go in at the same time. **Cool-season crops (potato, kale, collards) go in
*before* the last frost** (Maryland and Virginia extension: potatoes about mid-March to late April, kale and
collards March to mid-April; the last frost averages April 15–25 in zone 7a). **Warm-season crops (beans, winter squash,
corn) go in after the last frost** when the soil is warm. Harvest is before the first fall frost (October 15–25 on
average); kale/collards push into cold weather; sweet potato waits for warm soil (65°F) in May; garlic is the exception, planted in
October and dug the following July. **Seed saving** is what turns a garden into a renewable food source, with limits: beans are
self-pollinating and the easy one; corn is wind-pollinated and wants a mile of isolation or staggered
planting; squash crosses within a species, and seed from squash grown near ornamental or wild gourds can
give bitter, toxic fruit (buy fresh seed); potatoes are clones and extension advises certified seed.

## Load order (this domain)

```
Planning what to grow?  → pick from the manifest by calorie density + storability + days-to-maturity
Planting now?           → the crop entry's "Planting Windows (Zone 7a)" (last frost ≈ mid-Apr; potato, kale, collards go in BEFORE it)
Keeping the line going?  → the entry's "Seed Saving" (open-pollinated vs hybrid)
Any part needs processing to eat?  → ⚠ MANDATORY PREPARATION (e.g. dry beans MUST be soaked and boiled; corn eaten as a staple MUST be alkali-treated; taste-test every squash and discard bitter ones)
Putting garlic in oil?  → entries/garlic.md ⚠ MANDATORY PREPARATION FIRST (botulism: refrigerate ≤4 days or freeze; never room temperature, except the tested citric-acid method in the entry; roasted garlic in oil is the same hazard)
Storing sweet potatoes?  → entries/sweet-potato.md (cure warm, store 55–60°F, never refrigerate; chilling injury)
Calendar context: ../seasonality.md (cool-season crops before the last frost; warm-season crops after it; harvest/cure before the late-Oct frost).
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| potato | entries/potato.md | CROP | mid-atlantic-appalachian | plant mid-Mar–Apr (before last frost), harvest Jul–Sep | edible-when-prepared | low | none | false | T1 | 7 | reviewed |
| beans-dry | entries/beans-dry.md | CROP | mid-atlantic-appalachian | plant after last frost (May), harvest when pods are dry, before first fall frost | edible-when-prepared | moderate | none | false | T1 | 9 | reviewed |
| winter-squash | entries/winter-squash.md | CROP | mid-atlantic-appalachian | plant May–Jun, harvest Sep–Oct | edible-when-prepared | moderate | low | false | T1 | 6 | reviewed |
| kale-collards | entries/kale-collards.md | CROP | mid-atlantic-appalachian | plant Mar–Apr & Jul–Aug (before last frost in spring), harvest into the fall (longer under row cover or in a cold frame; kale may re-sprout in spring if winter is not too severe) | edible-raw | none | none | false | T1 | 6 | reviewed |
| corn-flint | entries/corn-flint.md | CROP | mid-atlantic-appalachian | plant after last frost (May), harvest dry Sep–Oct | edible-when-prepared | moderate | none | false | T1 | 7 | reviewed |
| garlic | entries/garlic.md | CROP | mid-atlantic-appalachian | plant Oct (fall), harvest Jun–Jul | edible-raw | lethal | none | false | T1 | 17 | draft |
| sweet-potato | entries/sweet-potato.md | CROP | mid-atlantic-appalachian | plant May–early Jul (soil ≥65°F), harvest Sep–Oct | edible-raw | low | low | false | T1 | 8 | draft |

`beans-dry` is `hazard_severity: moderate` + `preparation_required: true` (raw/undercooked dry beans
contain a lectin; FDA rule for kidney beans: soak at least 5 hours, pour the water away, boil in fresh
water at least 30 minutes, never use a slow cooker; the entry carries `## ⚠ MANDATORY PREPARATION`).
`corn-flint` is `hazard_severity: moderate` + `preparation_required: true` (corn as the main food without
alkali treatment causes pellagra, per WHO; moldy corn carries mycotoxins that cooking does not remove).
`winter-squash` is `hazard_severity: moderate` + `confusability_level: low` + `preparation_required: true`
(bitter squash, toxic squash syndrome: taste a small raw piece, and if it is bitter spit it out and throw the
whole squash away; cooking does not destroy the toxin; do not save seed from squash grown near ornamental
or wild gourds). `garlic` is
`hazard_severity: lethal` + `preparation_required: true` for one reason only: garlic held in oil at
room temperature can grow *Clostridium botulinum* and make botulism toxin; the bulb itself is not
the hazard (`## ⚠ MANDATORY PREPARATION` carries the fridge/freezer/acidification rules and the botulism warning signs: double vision, drooping eyelids, slurred speech, trouble swallowing, weakness, trouble breathing, which mean 911 or the emergency room at once). `sweet-potato`
needs no mandatory preparation; storage below about 50–55°F causes chilling injury, and ornamental
sweet potato vines of unknown spray history should not be eaten. Potato note: green
tubers/sprouts (solanine) — handled in-entry: trim small green spots, throw out heavily green or bitter tubers; cooking does not remove it. Sources: state extension and federal agencies (T1), with Poison Control and one university database (T2).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each CROP entry carries "Planting Windows (Zone 7a)" + "Seed Saving"; `preparation_required:
      true` crops (dry beans) carry `## ⚠ MANDATORY PREPARATION`.
- [ ] Frost dates consistent with the biome profile (last ≈ mid-Apr, first ≈ late-Oct).
