# Mid-Atlantic / Appalachian — Edible Plants (WILD-EDIBLE-PLANT)

> Wild edible plants of this biome. This index opens with a **deadly-twin matrix** — the edible-vs-
> deadly-look-alike pairs that share this habitat — which loads **before** the manifest of edibles.
> "What could kill me" before "what can I eat." Read the matrix first.
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Schema:
> [`../../../SCHEMAS.md`](../../../SCHEMAS.md) §1. Rules: [`../../../CONVENTIONS.md`](../../../CONVENTIONS.md).

---

## ☠ Deadly-twin matrix (read BEFORE the edible exemplars)

Every common edible below that has a dangerous look-alike in this biome is paired here. The
discriminators are **necessary but not sufficient** — positive ID requires *multiple concurrent*
traits (morphology + habitat + season), and the entry's `## ⚠ POSITIVE-ID SAFETY GATE` is the real
test. The deadliest pairing in this region is **wild onion/garlic vs. death camas** — get it wrong
and it stops your heart.

| Edible target | ☠ Deadly / toxic look-alike | Key discriminators (necessary, not sufficient) | What the toxin does |
|---------------|----------------------------|------------------------------------------------|---------------------|
| **Wild onion / garlic** (*Allium* spp.) | **Death camas** (*Toxicoscordion / Zigadenus*) | *Allium* **smells strongly of onion/garlic when crushed** — death camas does **NOT**. No onion smell ⇒ **do not eat.** | Zygacine: vomiting, low BP, **cardiac/respiratory failure** — can be **lethal**. |
| **Wild carrot / edible umbels** (e.g. *Daucus*) | **Poison hemlock** (*Conium maculatum*) | Poison hemlock: **purple-blotched, hairless stem; musty/mousy smell.** Wild carrot: hairy stem, carrot smell. **If unsure, do not eat any wild umbel.** | Coniine: ascending paralysis, **respiratory failure** — **lethal**. |
| **Wild parsnip / water-edge umbels** | **Water hemlock** (*Cicuta* spp.) | Water hemlock: **chambered, often purple-streaked rootstock; wet habitat (stream/ditch banks).** **The most violently poisonous plant in North America.** | Cicutoxin: violent **seizures, death within ~15 min** of a small amount. |
| **Violet / chickweed** (*Viola* / *Stellaria*) | Buttercup (*Ranunculus*, acrid/toxic) & lookalike weeds | Chickweed: single line of hairs on stem, stretchy stem, white star flower. Violet: heart-shaped leaf, 5-petal flower. Avoid acrid-tasting imitators. | Protoanemonin (buttercup): blistering, GI irritation. |
| **Acorn / oak** (*Quercus*) | (Low confusion; hazard is **preparation**, not ID) | Acorns are easy to ID by tree + cap, but are **bitter/astringent and must be leached** of tannins before eating. | Raw tannins: GI distress, kidney stress over time → see ⚠ MANDATORY PREPARATION (leaching). |

> **"No onion smell = not an onion."** The *Allium*/death-camas pair is the deadliest field mistake
> in this biome. **"Three umbels, three killers"**: poison hemlock, water hemlock, and fool's
> parsley make every wild white-flowered umbel a do-not-touch unless an expert confirms it. And
> **never eat white/yellow wild berries** — assume deadly (baneberry, etc.).

---

## Synthesis & load order

This biome's safest-to-approach edibles are the ones with **no deadly twin and an unmistakable
trait** (dandelion's milky sap + basal rosette; cattail in standing water; oak acorns by tree ID).
The dangerous ones are anything in the **onion** group (death-camas twin) and anything in the
**umbel/parsley/carrot** group (the hemlocks). Calorie reality: greens are low-calorie; **acorns and
nuts are the real wild calories here**, but acorns demand tannin leaching. Load order:

```
1. DEADLY-TWIN MATRIX (above)   — "what could kill me" first; internalize the onion-smell + umbel rules
2. This manifest                — find the entry + read its facets
3. The plant entry              — ⚠ POSITIVE-ID SAFETY GATE (multiple concurrent traits) + ⚠ MANDATORY PREPARATION
4. Cross-check ../hazards/       — toxic plants that share the habitat (hemlock, poison ivy)
5. CITE (Peterson / USDA — T1/T2) + triangulate ≥2 refs at safety-read
Positive ID or do not consume. Universal Edibility Test is a LAST resort only (and useless for fungi).
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| dandelion | entries/dandelion.md | WILD-EDIBLE-PLANT | mid-atlantic-appalachian | Mar–Nov | edible-when-prepared | low | low | false | T2 | 0 | planned |
| cattail | entries/cattail.md | WILD-EDIBLE-PLANT | mid-atlantic-appalachian | year-round | edible-when-prepared | low | moderate | false | T2 | 0 | planned |
| wild-onion-garlic-allium | entries/wild-onion-garlic-allium.md | WILD-EDIBLE-PLANT | mid-atlantic-appalachian | Mar–Nov | edible-when-prepared | lethal | deadly-lookalike-exists | false | T2 | 0 | planned |
| acorn-oak | entries/acorn-oak.md | WILD-EDIBLE-PLANT | mid-atlantic-appalachian | Sep–Nov | edible-when-prepared | low | low | false | T2 | 0 | planned |
| violet-or-chickweed | entries/violet-or-chickweed.md | WILD-EDIBLE-PLANT | mid-atlantic-appalachian | Mar–Jun | edible-when-prepared | low | moderate | false | T2 | 0 | planned |

`wild-onion-garlic-allium` is `hazard_severity: lethal` / `confusability_level:
deadly-lookalike-exists` (death-camas twin) and its entry sets `field_id_not_appropriate` honestly +
leads with the onion-smell gate. `acorn-oak` is low-confusability but `preparation_required: true`
(tannin leaching). `cattail` carries a "clean water only" caution.

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] **Deadly-twin matrix leads this index** (above the manifest). ✓
- [ ] Every entry with `confusability_level ≥ moderate` carries a `## Deadly / Toxic Look-Alikes`
      section; the *Allium* entry leads with the no-onion-smell disqualifier.
- [ ] `preparation_required: true` entries (acorn) carry `## ⚠ MANDATORY PREPARATION` (tannin leaching).
- [ ] Each entry opens with the `## ⚠ POSITIVE-ID SAFETY GATE`; species + look-alikes triangulated
      vs. ≥2 T1/T2 refs at safety-read.
