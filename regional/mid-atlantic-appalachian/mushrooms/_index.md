# Mid-Atlantic / Appalachian — Mushrooms (MUSHROOM)

> **The highest-consequence domain in the repo.** Fungal misidentification is the single
> highest-consequence failure mode — a missed meal versus a destroyed liver. This index opens with
> the **mushroom doctrine** and the **deadly-look-alike matrix**, which load **before** any species
> entry. Read both before reasoning over *any* fungal entry.
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Schema:
> [`../../../SCHEMAS.md`](../../../SCHEMAS.md) §2. Doctrine source: [`../../../CONVENTIONS.md`](../../../CONVENTIONS.md) §4.

---

## ☠ MUSHROOM DOCTRINE — loads before any species entry

The single most important safety construct in the repo. **Non-negotiable for a novice:**

1. **No consumption without expert confirmation** — a regional mycological society or an expert who has
   examined the specimen in hand. Matching several sources (field guides, spore print, cut tests) is an
   **additional** requirement, never a substitute for the expert. Photo-only ID is **never** sufficient.
2. **No LBMs** — little brown mushrooms are not worth the risk; too many toxic look-alikes.
3. **No white-gilled mushrooms with a volva or ring** — the *Amanita* pattern (destroying angel,
   death cap) is lethal and easy to misjudge.
4. **No decayed or insect-damaged specimens**, and no mixed collections in one bag.
5. **Spore print** where the ID depends on it.
6. **Cook by default** — most edibles are toxic or indigestible raw.
7. **First-portion rule** — even a confirmed edible: small portion, no alcohol where relevant (e.g.
   inky caps), wait, and never try two new species at once.
8. **When in doubt, throw it out.** The downside is asymmetric: a missed meal vs. a destroyed liver.
9. **If anyone may have eaten an unidentified or mis-identified mushroom:** call **Poison Control,
   1-800-222-1222**, at the first suspicion and do not wait for symptoms; call **911** for collapse,
   seizure or trouble breathing; do not make the person vomit unless Poison Control says to; save a sample.
   Amatoxin and false-morel poisonings are delayed, so feeling fine is not a reason to wait
   ([food guide](../../../05_food.md#if-someone-ate-something)).

Every mushroom entry's facets must reflect this: `expert_id_required: true`, and
`field_id_not_appropriate: true` for any species with a deadly look-alike.

> **Answer-policy reminder:** for any mushroom flagged `field_id_not_appropriate: true`, **refuse**
> to confirm "yes, eat it" on a description or photo alone (`../../../CONVENTIONS.md` §9 rule 4).
> Lead with the gate and the uncertainty; reproduce `## ⚠ MANDATORY PREPARATION` verbatim. When in
> doubt → do not eat.

---

## ☠ Deadly-look-alike matrix (read BEFORE the edible exemplars)

"What could kill me" before "what can I eat." The rows from morel through wood ear / puffball (morel, chicken-of-the-woods, oyster,
chanterelle, wood ear / puffball) have a confusable that can hospitalize or kill. The last three rows
(hen of the woods, lion's mane, black trumpet) record that the sources opened name **no deadly look-alike**;
lion's mane and black trumpet do have look-alikes to rule out, and one black trumpet look-alike is
reported to cause stomach illness. Everywhere, the discriminators are necessary but **not sufficient** —
confirmation still requires expert ID, and the multi-source checks come on top of it.

| Edible target | ☠ Deadly / toxic look-alike | Key discriminators (necessary, not sufficient) | What the toxin does |
|---------------|----------------------------|------------------------------------------------|---------------------|
| **Morel** (*Morchella*) | **False morels** (*Gyromitra* spp., incl. eastern *G. caroliniana*); **early false morel** (*Verpa bohemica*) | TRUE morel: cap **pitted and ridged** (sponge or honeycomb); **cap and stem fully hollow, one open space from cap tip to stem base, when sliced lengthwise**; base of cap joins the stem; no cottony fibre. FALSE morel (*Gyromitra*): cap lobed, folded or wrinkled and the inside **chambered or stuffed**. Eastern *G. caroliniana* is **not lobed** and sits tightly on the stem: reddish brown, tightly wrinkled, thick white ribbed stem, stuffed and chambered inside, so the **pitted cap plus fully hollow interior** is the test. *Verpa*: cap **hangs free, attached only at the top**, stem **stuffed with cotton-like fibres**. Half-free morels are true morels with a partly hanging cap, but a free-hanging cap or any cotton in the stem means discard. | *Gyromitrin*: headache, severe diarrhea, vomiting within 2 to 24 h; in severe cases liver, kidney and red blood cell damage, possibly death (NAMA). About 18% of the toxin remained after double boiling (Finnish Food Authority). *Verpa*: sources opened do not settle its toxicity. Raw or undercooked true morels also upset the stomach, and morels with alcohol can in some people. |
| **Chicken-of-the-woods** (*Laetiporus*) | **Jack-o'-lantern** (*Omphalotus illudens*); **conifer-grown *Laetiporus*** (*L. huroniensis*, reported to cause illness); yew, other conifer and eucalyptus hosts | Edible target: **shelf with pores underneath, no gills**, bright orange top with sulfur-yellow pores (*L. sulphureus*) or pinkish-orange cap with white pores at a tree base (*L. cincinnatus*), 2 to 4 pores per mm, pore surface does not bruise, on living or dead **hardwood (esp. oak)**. Jack-o'-lantern has **true gills**, grows in dense clusters, orange all through. Do not harvest from any conifer (a 2026 peer-reviewed review says conifers, particularly yew, must be avoided), eucalyptus or a tree you cannot name. Reactions (allergy, vomiting, stomach upset) occur on any host, including in people who ate it before without trouble. | Jack-o'-lantern: illudins, severe stomach illness. Conifer-grown *Laetiporus*: reactions reported, cause not established. Any host: allergy and stomach upset; never eat raw or undercooked. |
| **Oyster** (*Pleurotus*) | **Jack-o'-lantern** (*Omphalotus illudens*, eastern NA); **angel wings** (*Pleurocybella porrigens*, see next row) | Both oyster and jack-o'-lantern have **true gills**, so gill edges and spore print do not separate them (both print white to cream). Oyster: **white, gray, tan or brown**, fan-shaped, off-center stub or no stem, on dead hardwood (sometimes conifer). Jack-o'-lantern: **orange all through**, tight clusters from the base of a hardwood or from buried roots. (The glow is **not a usable field test**.) | *Omphalotus illudens* (illudins): severe stomach illness, onset about 1 to 3 h, most recover within 12 h (NAMA); Missouri: not usually life-threatening to healthy adults. |
| **Oyster, second look-alike** (*Pleurotus*) | **Angel wings** (*Pleurocybella porrigens*) | Angel wings: **thin, small, pure white, nearly stemless**, usually on **conifer wood (esp. hemlock)**, late summer to fall. Oyster is more robust and fleshy, but oyster also grows on conifers sometimes, so the host is not a clean test. | Linked to **acute encephalopathy**: in autumn 2004 in Japan 59 people fell ill and 17 died, mostly people with kidney disease, with symptoms 13 to 18 days after eating (NAMA toxin note). Do not eat. |
| **Chanterelle** (*Cantharellus*) | **Jack-o'-lantern** (*Omphalotus illudens*, eastern NA); **false chanterelle** (*Hygrophoropsis aurantiaca*, toxicity disputed) | Chanterelle: **false gills** (smooth, wrinkled or blunt-edged ridges, never thin blades), **flesh white to whitish-yellow inside the stem and not changing**, grows **on the ground** in grass or leaf litter, alone or in groups, **never on decaying wood**. Jack-o'-lantern: **true sharp thin gills**, **pale orange flesh through the stem**, dense clusters on wood or buried roots. **Cut the stem on every one: orange inside = discard.** Spore print does not separate chanterelle from either look-alike. *Hygrophoropsis*: true, thin, repeatedly forked gills, soft flimsy flesh, on litter or woody debris often under conifers; sources disagree on its toxicity, so do not eat. | *Omphalotus illudens* (illudins): very sick, onset about 1 to 3 h, most recover within 12 h (NAMA), some stay ill for days (Missouri); dehydration is the danger. A classic edible-mushroom poisoning error. |
| **Wood ear / puffball** (*Auricularia* / *Lycoperdon*) | **Amanita "egg" button** (*A. bisporigera* destroying angel and other *Amanita*); **earthballs** (*Scleroderma*, pigskin puffball) | A true puffball is **pure white and solid inside** when sliced, with no sign of a developing cap, stem or gills, and a thin skin. **CUT EVERY PUFFBALL TOP TO BOTTOM**: any **outline of a cap, gills or stem, or any color other than pure white = discard**. *Scleroderma*: thick rind, inside dark brownish purple, so the same cut test catches it. Wood ear: thin, rubbery, brown, ear-shaped, on dead hardwood, no gills or pores; the eastern *Auricularia* has no settled species name, so rely on the gate, not the name. | *Amanita* **amatoxins**: 6 to 24 h with no symptoms, then vomiting and diarrhea, a false recovery, then liver and kidney failure. How often it kills depends on how fast good care starts (NAMA: about 10% in the U.S. and Canada and about 50% without prompt, knowledgeable care; CDC: 10-20%; StatPearls: under 5% in developed countries with early intensive care); see the [amatoxin hazard entry](../hazards/entries/amatoxin-mushrooms-amanita-galerina.md). Earthball: no source opened gives symptoms or timing. |
| **Hen of the woods** (*Grifola frondosa*) | **No deadly or toxic look-alike named by the sources opened.** Named confusables: **black-staining polypore** (*Meripilus sumstinei*); **Berkeley's polypore** (*Bondarzewia berkeleyi*); eastern cauliflower mushroom (*Sparassis spatulata*, one source) | Hen: **pores (no gills)**, many small gray to gray-brown fan or spoon caps from one branching white base, at the base of **oaks** or stumps, **autumn**, **white spore print** (fits but does not confirm; both look-alikes also print white). *Meripilus*: bigger caps, **finer pores (4 to 8 per mm depending on the source, vs. 1 to 3)**, **pore surface pure white when young**, and pores and cap margin **bruise black** when touched; no T1 or T2 source opened gives its edibility. *Bondarzewia*: **one big thick cream or white cap or clump, wide angular pores, yellowish rooting stalk**, no bruising. Cauliflower mushroom: **ribbon-like folds, no pores**. Gills, black bruising, or a bag mixed with white-gilled *Amanita*-pattern finds disqualify. | No toxin or symptom list in any source opened. Some people react to certain fungi even when the species is listed as edible. `field_id_not_appropriate: false`; `expert_id_required: true`. |
| **Lion's mane and relatives** (*Hericium erinaceus*, *H. americanum*, *H. coralloides*) | **No poisonous look-alike named by the sources opened** (Minnesota DNR: "no poisonous look-alikes"). Named confusables: other *Hericium* species; **northern tooth** (*Climacodon septentrionalis*); **hedgehog mushroom** (*Hydnum repandum*, one source) | Lion's mane: **hanging white teeth (spines), no gills or pores**, on **hardwood** (living wounds, logs, stumps; oak, beech, maple), **late summer to fall**, white spore print. *H. erinaceus*: **one unbranched clump** of long dangling spines. *H. americanum* and *H. coralloides*: **spines hang from branches**. Spine length overlaps between species, so rely on clump versus branched. Northern tooth: **overlapping white shelves** with short ragged spines on **living maple or beech**, July to October, old specimens smell of spoiled ham; no toxicity reported in the sources opened, not the target. Hedgehog mushroom: **has a cap and stalk**, orangish-tan. Aged yellow or brown flesh turns bitter. | No toxin named for any of them. Allergic reactions to fungi occur even with edible species. `field_id_not_appropriate: false`; `expert_id_required: true`. |
| **Black trumpet** (*Craterellus fallax*) | **No deadly look-alike named by the sources opened** (Missouri: "no lookalikes in Missouri", Missouri only). Named confusables: ***Craterellus foetidus*** (edibility not given in any source opened); **scaly vase** (*Turbinellus floccosus*) | Black trumpet: **dark hollow vase, no gills, outer surface smooth to shallowly wrinkled**, spore print **yellowish-orange to pale pinkish orange (not white)**, on the ground under hardwoods (oak, beech), **summer to early fall**. *C. foetidus*: **prominent wrinkles and gill-like folds with cross-veins across the upper third**, **white print**, thicker, **often fused in clusters of 2 to 5**. Scaly vase: **bright orange, scaly**, with conifers, not dark. | Scaly vase: nausea, vomiting and diarrhea in some people, onset as late as 8 to 14 h (UBC museum, MykoWeb; western populations). *C. foetidus*: no effects stated in any source opened. Some people react to edible mushrooms. `field_id_not_appropriate: false`; `expert_id_required: true`. |

> **Rows without a deadly look-alike.** The last three rows (hen of the woods, lion's mane, black trumpet)
> record what the sources opened for each entry say: they name **no deadly look-alike**. That is a
> statement about those sources, not a promise that none exists. Their confusables are listed so you can
> rule them out, and the scaly vase is reported to cause stomach illness. The doctrine still applies in full,
> and each entry keeps `expert_id_required: true`.

> **The Amanita pattern is the master killer.** White gills + a volva (cup at the base) and/or a
> ring = the *Amanita* signature (destroying angel, death cap). Amatoxin poisoning is delayed and
> can be fatal (sources differ on how often; see the mortality note in the amatoxin hazard entry). Doctrine point 3 and the puffball cut test exist to catch it. Never skip them. Full detail: [amatoxin hazard entry](../hazards/entries/amatoxin-mushrooms-amanita-galerina.md).

---

## Synthesis & load order

This region's *approachable* edibles cluster around features that resist confusion (pores not gills;
ridges not gills; substrate specificity) — but every one still has a confusable.
The pore, tooth and smooth-surface edibles (hen of the woods, lion's mane, black trumpet) are routed through
their own entries below; read each entry's gate for the look-alikes the sources name. The wood ear and puffball
entry routes to the [amatoxin hazard entry](../hazards/entries/amatoxin-mushrooms-amanita-galerina.md). The load order is
strict:

```
1. DOCTRINE (above)            — always, before any species reasoning
2. DEADLY-LOOK-ALIKE MATRIX    — "what could kill me" first
3. This manifest               — find the entry + read its facets
4. The species entry           — positive-ID gate + spore print + ⚠ MANDATORY PREPARATION
5. Cross-check ../hazards/      — shared-habitat toxic species (start with amatoxin-mushrooms-amanita-galerina)
6. EXPERT CONFIRMATION (regional mycological society or an expert), then CITE (field guide, T1/T2)
   and triangulate ≥2 refs. The refs never replace the expert.
For field_id_not_appropriate species: refuse a field-ID-only "eat it." Expert confirmation required.
```

## Manifest (present entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | field_id_not_appropriate | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|--------------------------|-------------|--------------|---------------|
| morel-morchella | entries/morel-morchella.md | MUSHROOM | mid-atlantic-appalachian | spring (Mar–Jun, by latitude and altitude) | edible-when-prepared | lethal | deadly-lookalike-exists | true | true | T2 | 10 | reviewed |
| chicken-of-the-woods-laetiporus | entries/chicken-of-the-woods-laetiporus.md | MUSHROOM | mid-atlantic-appalachian | summer–fall (rare winter/spring) | edible-when-prepared | high | deadly-lookalike-exists | true | true | T2 | 13 | reviewed |
| oyster-pleurotus | entries/oyster-pleurotus.md | MUSHROOM | mid-atlantic-appalachian | P. ostreatus late fall–early spring; P. pulmonarius late Apr–Sep | edible-when-prepared | high | deadly-lookalike-exists | true | true | T2 | 13 | reviewed |
| chanterelle-cantharellus | entries/chanterelle-cantharellus.md | MUSHROOM | mid-atlantic-appalachian | summer (July typical) | edible-when-prepared | high | deadly-lookalike-exists | true | true | T2 | 14 | reviewed |
| wood-ear-or-puffball | entries/wood-ear-or-puffball.md | MUSHROOM | mid-atlantic-appalachian | puffball summer–fall; wood ear spring–fall | conditionally-edible | lethal | deadly-lookalike-exists | true | true | T2 | 15 | reviewed |
| hen-of-the-woods-grifola | entries/hen-of-the-woods-grifola.md | MUSHROOM | mid-atlantic-appalachian | late summer–fall (Sep–Nov) | edible-when-prepared | low | moderate | true | false | T2 | 12 | draft |
| lions-mane-hericium | entries/lions-mane-hericium.md | MUSHROOM | mid-atlantic-appalachian | late summer–fall (Aug–Nov) | edible-when-prepared | low | low | true | false | T2 | 13 | draft |
| black-trumpet-craterellus | entries/black-trumpet-craterellus.md | MUSHROOM | mid-atlantic-appalachian | summer–early fall (Jun–early Oct) | edible-when-prepared | low | moderate | true | false | T2 | 13 | draft |

**Doctrine compliance:** all rows `expert_id_required: true`. The three newest rows (hen of the woods, lion's mane, black trumpet) are `field_id_not_appropriate: false` because no source opened names a deadly look-alike; each entry's Deadly Look-Alikes section gives the reasoning and the confusables to rule out. The morel (vs. false morels and *Verpa*) and the puffball-vs-*Amanita*-button rows are `hazard_severity: lethal` / `field_id_not_appropriate: true` (set in-entry). Every row marked `deadly-lookalike-exists` is `field_id_not_appropriate: true` in its entry.

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled and matching each entry's front matter.
- [ ] **Doctrine + deadly-look-alike matrix lead this index** (above the manifest). ✓
- [ ] Morel / false-morel pair present; **≥3** entries carry a deadly confusable.
- [ ] Every `deadly-lookalike-exists` row is `expert_id_required: true` and (in-entry)
      `field_id_not_appropriate: true`; lethal-toxin rows cite ≥2 T1/T2 refs at safety-read.
- [ ] Each entry opens with the `## ⚠ POSITIVE-ID SAFETY GATE` and carries `## ☠ Deadly Look-Alikes`
      + `## ⚠ MANDATORY PREPARATION`.
