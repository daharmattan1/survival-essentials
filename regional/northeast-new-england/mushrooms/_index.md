# Northeast / New England — Mushrooms (MUSHROOM)

> **The highest-consequence domain in the repo.** Fungal misidentification is the single
> highest-consequence failure mode: a missed meal versus a destroyed liver. This index opens with
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
   *Note for the honey mushroom:* it has whitish gills and a ring, so it falls inside this wording.
   It is eaten only after an expert has examined the dug-up specimen in hand and has checked the stem
   base for a cup (volva) and whether the gills attach to the stem or stand free. Without that expert
   check, point 3 applies and the answer is no.
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

"What could kill me" before "what can I eat." The honey mushroom row has a deadly confusable (the
deadly galerina). The chanterelle row has a confusable that is not called deadly by the sources opened
but is the most common mushroom poisoning call in the Northeast, per Cornell. The king bolete row
records that the sources opened name **no deadly look-alike in New England**, but do name boletes
that cause severe stomach illness, and the group cannot be settled to species in the field. Everywhere, the discriminators are necessary but **not sufficient**:
confirmation still requires expert ID, and the multi-source checks come on top of it.

| Edible target | ☠ Deadly / toxic look-alike | Key discriminators (necessary, not sufficient) | What the toxin does |
|---------------|----------------------------|------------------------------------------------|---------------------|
| **Honey mushroom** (*Armillaria* spp.) | **Deadly galerina** (*Galerina marginata*); other rusty-spored and brown-spored wood mushrooms (*Gymnopilus junonius*, *Pholiota*, wood-growing *Hypholoma*); **jack-o'-lantern** (*Omphalotus illudens*); the *Amanita* pattern | Honey mushroom: on wood or buried roots, honey-yellow to tan-brown cap, **whitish gills**, a **ring or ring zone**, black shoestring cords on roots, fall, and a **WHITE spore print**. **These gills and the ring are also the *Amanita* pattern in doctrine point 3**, so an expert has to check the dug-up base for a cup (volva) and the gills for free versus attached; a swollen base does not settle it. Deadly galerina: **rusty brown spore print**, gills yellowish turning rusty, ring thin whitish to rusty brown or only a ring zone, often smaller cap. Cap size overlaps, honey mushroom gills can darken, and both can have a ring, so the print and the whole set of traits decide. A white print rules out galerina but **not** *Amanita* (free white gills, cup at the stem base, white print). Jack-o'-lantern is **orange all through** in a large cluster with true gills. A clump with no ring or ring zone at all is outside the entry. | Galerina: **amatoxin**, symptoms may not start for 6 to 24 hours (Missouri: 10 or more hours), a day of apparent recovery, then liver and kidney failure. Sources differ on deaths (NAMA: about 50% without prompt, knowledgeable care, about 10% in the U.S. and Canada; CDC: 10% to 20%). Honey mushroom itself upsets some people's stomachs (NAMA registry: 38 or more adults, average onset about 4 hours); Tox Info Suisse (a poisons centre) lists it under "blanch, throw away cooking water," and the entry carries that step with no time, since no source gives one. The other wood-growers in the row are not harmless: the NAMA registry records illness from *Gymnopilus spectabilis* (15 adults, hallucinations in 10; reports include Massachusetts, New York and Rhode Island) and *Pholiota squarrosa* (12 adults, stomach distress and fever), and one child with cramps from *Hypholoma sublateritium*. See the [amatoxin hazard entry](../../mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md) (Mid-Atlantic-scoped, but the toxicology is not region-bound). |
| **Chanterelle** (*Cantharellus* spp., golden chanterelles) | **Jack-o'-lantern** (*Omphalotus illudens*); **false chanterelle** (*Hygrophoropsis aurantiaca*, toxicity not stated by the sources opened; Forest Service: not recommended); **scaly vase** (*Turbinellus floccosus*, stomach illness in the NAMA registry) | Chanterelle: **false gills** (forked, blunt-edged ridges, never thin blades), **flesh white inside the cut stem (yellow edges at most)**, grows **on the ground**, never on decaying wood. Jack-o'-lantern: **true sharp thin gills**, **pale orange flesh through the stem**, dense clusters on wood or buried roots. **Cut the stem on every one: orange inside = discard.** White flesh rules out jack-o'-lantern only: the false chanterelle also has thin whitish flesh, so the false-gill check stays. Spore prints overlap (chanterelles print white, cream, yellow or pinkish by species; jack-o'-lantern white to creamy or pale yellow; false chanterelle white), so a print separates nothing. Some chanterelle species are described as clustered or fused, so a ground cluster is a flag to cut, not a verdict. Also check the cap and stem: a chanterelle has a smooth to nearly smooth cap on a distinct central stem; a deep vase of soft, flattened dark orange scales whose stem flares into the cap is the scaly vase (*Turbinellus floccosus*), which also has false gills, white flesh and orange colour. | *Omphalotus illudens* (illudins): very sick, onset about 1 to 3 h, most recover within 12 h (NAMA), some stay ill for days (Missouri); most victims reach the emergency room (Cornell). Dehydration is the danger. Scaly vase: NAMA registry, 3 adults with stomach distress and cramps, onset 3.5 to 9 h (CO, ME, WV). |
| **King bolete** (*Boletus edulis* group) | **No deadly look-alike named in New England by the sources opened.** Named confusables: ***Boletus huronensis*** (under hemlock, bruises blue); **red-pored and blue-staining boletes** (incl. Frost's bolete, the *B. subvelutipes* group); **bitter bolete** (*Tylopilus felleus*) | King bolete: **pores (no gills)**, white then yellow to olive-yellow then brownish yellow, **no blue staining**, **white flesh**, thick solid stem with a **whitish net at the top**, **olive-brown print**, on the ground with conifers (and in some references oak and birch). *B. huronensis*: pores bruise blue (sometimes slowly), **pale yellow flesh typically bluing when cut, "but sometimes slowly or not at all"** (so lack of blue does not clear it), **no white net**, bulbous yellowish stem, and the same olive-brown print as the king bolete (the print does not separate them). Missouri: **avoid boletes with orange to red pores and those that bruise blue** (a rule that removes candidates, never confirms one). Bitter bolete: pores white then **pink**, **coarse brown stem net**, **very bitter**, pinkish-brown print; young pores can be white, so no single trait clears it. | *B. huronensis*: severe stomach illness, reported vertigo, bad night even after cooking. Certain red-pored boletes (NAMA muscarine group): salivation, sweating, severe vomiting and diarrhea in 15 to 30 minutes. Bitter bolete: bitter taste, no toxin named. One bolete death is in the NAMA registry, among two adults who ate *B. pulcherrimus* in Oregon. King boletes (*B. edulis* and *B. barrowsii*) also appear in the registry: 13 adults, stomach distress in 11, with atrial fibrillation and a slow heart rate (bradycardia) among the effects listed. `field_id_not_appropriate: true`; `expert_id_required: true`. |

> **Rows and facets.** The honey mushroom, chanterelle and king bolete are all
> `field_id_not_appropriate: true`. The king bolete is set `true` (an orchestrator decision) even though
> no source opened names a deadly look-alike in New England, which is a statement about those sources,
> not a promise that none exists: the group cannot be resolved to species in the field, its look-alikes
> cause severe illness, and correct king boletes also appear in the poisoning registry. It keeps
> `expert_id_required: true` and `confusability_level: high`. The
> chanterelle is `confusability_level: high` rather than `deadly-lookalike-exists` because no source
> opened calls jack-o'-lantern deadly; the Mid-Atlantic chanterelle entry uses the stronger
> setting, which the orchestrator may want to harmonize.

> **The Amanita pattern is the master killer.** White gills + a volva (cup at the base) and/or a
> ring = the *Amanita* signature (destroying angel, death cap). Amatoxin poisoning is delayed and
> can be fatal (sources differ on how often; see the mortality note in the amatoxin hazard entry). Doctrine point 3 exists to catch it, and the honey mushroom entry keeps it in its gate.
> Full detail: [amatoxin hazard entry](../../mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md).

---

## Synthesis & load order

This region's honey mushrooms, king boletes and chanterelles all have confusables that the field
guides spend pages on, and in each case the edible side is a **group of species** that the sources
say cannot be named in the field (the *Armillaria* complex, the eastern edulis-like boletes, the
golden chanterelles). Older New England guides use older names (*Cantharellus cibarius*, *Boletus
edulis*); current sources name the golden chanterelles *C. enelensis* and *C. camphoratus* and say
the European name does not apply. The gate in each entry does not depend on the species name.
The load order is strict:

```
1. DOCTRINE (above)            — always, before any species reasoning
2. DEADLY-LOOK-ALIKE MATRIX    — "what could kill me" first
3. This manifest               — find the entry + read its facets
4. The species entry           — positive-ID gate + spore print + ⚠ MANDATORY PREPARATION
5. Cross-check hazards          — shared-habitat toxic species (amatoxin: ../../mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md)
6. EXPERT CONFIRMATION (regional mycological society or an expert), then CITE (field guide, T1/T2)
   and triangulate ≥2 refs. The refs never replace the expert.
For field_id_not_appropriate species: refuse a field-ID-only "eat it." Expert confirmation required.
```

## Manifest (present entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | field_id_not_appropriate | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|--------------------------|-------------|--------------|---------------|
| honey-mushroom-armillaria | entries/honey-mushroom-armillaria.md | MUSHROOM | northeast-new-england | fall (late summer to early winter, by species and weather) | conditionally-edible | lethal | deadly-lookalike-exists | true | true | T2 | 20 | agent-verified |
| chanterelle-new-england | entries/chanterelle-new-england.md | MUSHROOM | northeast-new-england | summer to early fall (Jul–Sep) | edible-when-prepared | moderate | high | true | true | T2 | 21 | agent-verified |
| king-bolete-boletus | entries/king-bolete-boletus.md | MUSHROOM | northeast-new-england | summer to fall (Jun–Oct) | edible-when-prepared | moderate | high | true | true | T2 | 18 | agent-verified |

**Doctrine compliance:** all rows `expert_id_required: true`. The honey mushroom row (deadly galerina)
is `hazard_severity: lethal` / `field_id_not_appropriate: true`. The chanterelle row is
`field_id_not_appropriate: true` because the look-alike poisoning is common and the edible side is a
species group. The king bolete row is `field_id_not_appropriate: true` for the reason given under the matrix.

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled and matching each entry's front matter.
- [ ] **Doctrine + deadly-look-alike matrix lead this index** (above the manifest). ✓
- [ ] Every `deadly-lookalike-exists` row is `expert_id_required: true` and (in-entry)
      `field_id_not_appropriate: true`; lethal-toxin rows cite ≥2 T1/T2 refs at safety-read.
- [ ] Each entry opens with the `## ⚠ POSITIVE-ID SAFETY GATE` and carries `## ☠ Deadly Look-Alikes`
      + `## ⚠ MANDATORY PREPARATION`.
