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

1. **No consumption without expert confirmation** — a regional mycological society, an expert, or a
   definitive multi-source positive ID. Photo-only ID is **never** sufficient.
2. **No LBMs** — little brown mushrooms are not worth the risk; too many toxic look-alikes.
3. **No white-gilled mushrooms with a volva or ring** — the *Amanita* pattern (destroying angel,
   death cap) is lethal and easy to misjudge.
4. **No decayed or insect-damaged specimens**, and no mixed collections in one bag.
5. **Spore print** where the ID depends on it.
6. **Cook by default** — most edibles are toxic or indigestible raw.
7. **First-portion rule** — even a confirmed edible: small portion, no alcohol where relevant (e.g.
   inky caps), wait, and never try two new species at once.
8. **When in doubt, throw it out.** The downside is asymmetric: a missed meal vs. a destroyed liver.

Every mushroom entry's facets must reflect this: `expert_id_required: true`, and
`field_id_not_appropriate: true` for any species with a deadly look-alike.

> **Answer-policy reminder:** for any mushroom flagged `field_id_not_appropriate: true`, **refuse**
> to confirm "yes, eat it" on a description or photo alone (`../../../CONVENTIONS.md` §9 rule 4).
> Lead with the gate and the uncertainty; reproduce `## ⚠ MANDATORY PREPARATION` verbatim. When in
> doubt → do not eat.

---

## ☠ Deadly-look-alike matrix (read BEFORE the edible exemplars)

"What could kill me" before "what can I eat." Each edible below has a confusable that can hospitalize
or kill; the discriminators are necessary but **not sufficient** — confirmation still requires expert
ID / spore print / multi-source triangulation.

| Edible target | ☠ Deadly / toxic look-alike | Key discriminators (necessary, not sufficient) | What the toxin does |
|---------------|----------------------------|------------------------------------------------|---------------------|
| **Morel** (*Morchella*) | **False morel** (*Gyromitra* spp.) | TRUE morel: cap **pitted/honeycombed**, fully **hollow** when sliced top-to-bottom, cap fused to stem. FALSE: cap **wrinkled/brain-like (lobed, not pitted)**, **chambered/cottony** inside, not uniformly hollow. | *Gyromitrin → monomethylhydrazine*: vomiting, seizures, liver/CNS damage; can be **lethal**. Not reliably cooked out. |
| **Chicken-of-the-woods** (*Laetiporus*) | Toxic shelf fungi; *Omphalotus illudens* (jack-o'-lantern); conifer-grown *L. huroniensis* causes GI illness | Edible target: **shelf, no gills, pore surface underneath, bright orange top / sulfur-yellow pores (*L. sulphureus*) or white pores (*L. cincinnatus*), on hardwood (esp. oak)**. Avoid look-alikes with gills or on conifer/eucalyptus. Jack-o'-lantern (*O. illudens*) has **true gills** not pores — decisive check. *L. huroniensis* is the eastern conifer species responsible for GI reactions. | GI distress; conifer-source reactions (*L. huroniensis*). Verify substrate + pore surface. |
| **Oyster** (*Pleurotus*) | **Jack-o'-lantern** (*Omphalotus illudens*, eastern NA); some *Pleurocybella*/gilled imitators | Oyster: **white-to-tan, off-center stub or no stem, decurrent gills, on dead hardwood, grows in shelving clusters**. Jack-o'-lantern: **orange**, true gills, grows on **buried wood/roots in clumps**. Note: both have white-to-cream spore prints — rely on cap color and growth habit, not spore print, as primary discriminators. (Bioluminescence is sometimes cited but is **not a usable field test** — visible only after long dark-adaptation, and absence proves nothing.) | *Omphalotus illudens* (illudin cytotoxins; NOT a cholinergic syndrome): severe GI illness, rarely fatal in healthy adults. |
| **Chanterelle** (*Cantharellus*) | **Jack-o'-lantern** (*Omphalotus illudens*, eastern NA); **false chanterelle** (*Hygrophoropsis aurantiaca*) | Chanterelle: **false gills = blunt forked ridges running down the stem**, not true blades; bright yellow-orange; mycorrhizal (on ground near hardwood). Jack-o'-lantern: **true, knife-edge gills**, clustered on wood. *Hygrophoropsis*: true repeatedly-forked gills (now classified poisonous/weakly toxic). | *Omphalotus illudens* (illudins): severe GI illness (rarely fatal); mistaking true gills for false ridges is the classic, and most common, edible-mushroom poisoning error. |
| **Wood ear / puffball** (*Auricularia* / *Lycoperdon*) | **Amanita "egg" button** (*A. bisporigera* destroying angel; *A. phalloides* death cap also present MD northward); ***Scleroderma* spp.** (earthball, GI toxic) | A true puffball is **solid, uniformly white inside** when sliced. **CUT EVERY PUFFBALL TOP-TO-BOTTOM**: any **outline of a cap, gills, or stem inside = an Amanita button → DISCARD**. *Scleroderma*: same cut test — interior is **dark purple-black**, thick warty rind → DISCARD. Wood ear: rubbery, ear-shaped, on wood. | *Amanita* **amatoxins**: delayed (6–24 h+) onset, then liver/kidney failure — **frequently lethal** (~50% without prompt treatment). |

> **The Amanita pattern is the master killer.** White gills + a volva (cup at the base) and/or a
> ring = the *Amanita* signature (destroying angel, death cap). Amatoxin poisoning is delayed and
> often fatal. Doctrine points 3 and the puffball cut-test exist to catch it. Never skip them.

---

## Synthesis & load order

This region's *approachable* edibles cluster around features that resist confusion (pores not gills;
ridges not gills; substrate specificity) — but every one still has a confusable. The load order is
strict:

```
1. DOCTRINE (above)            — always, before any species reasoning
2. DEADLY-LOOK-ALIKE MATRIX    — "what could kill me" first
3. This manifest               — find the entry + read its facets
4. The species entry           — positive-ID gate + spore print + ⚠ MANDATORY PREPARATION
5. Cross-check ../hazards/      — shared-habitat toxic species
6. CITE (field guide / regional mycological society — T1/T2) + triangulate ≥2 refs
For field_id_not_appropriate species: refuse a field-ID-only "eat it." Expert confirmation required.
```

## Manifest (present entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | field_id_not_appropriate | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|--------------------------|-------------|--------------|---------------|
| morel-morchella | entries/morel-morchella.md | MUSHROOM | mid-atlantic-appalachian | Apr–May (lowland) | edible-when-prepared | lethal | deadly-lookalike-exists | true | true | T2 | 2 | present |
| chicken-of-the-woods-laetiporus | entries/chicken-of-the-woods-laetiporus.md | MUSHROOM | mid-atlantic-appalachian | Jun–Oct | edible-when-prepared | moderate | high | true | false | T2 | 2 | present |
| oyster-pleurotus | entries/oyster-pleurotus.md | MUSHROOM | mid-atlantic-appalachian | year-round (flushes) | edible-when-prepared | high | deadly-lookalike-exists | true | true | T2 | 2 | present |
| chanterelle-cantharellus | entries/chanterelle-cantharellus.md | MUSHROOM | mid-atlantic-appalachian | Jun–Sep | edible-when-prepared | high | deadly-lookalike-exists | true | true | T2 | 2 | present |
| wood-ear-or-puffball | entries/wood-ear-or-puffball.md | MUSHROOM | mid-atlantic-appalachian | summer–fall | conditionally-edible | lethal | deadly-lookalike-exists | true | true | T2 | 2 | present |

**Doctrine compliance:** all rows `expert_id_required: true`. The morel (vs. false morel) and the
puffball-vs-*Amanita*-button rows are `hazard_severity: lethal` / `field_id_not_appropriate: true`
(set in-entry). **Four** entries carry a deadly/toxic confusable (morel, oyster, chanterelle,
wood-ear/puffball) — exceeding the ≥3 floor. `field_id_not_appropriate: true` is set in-entry for
every `deadly-lookalike-exists` row.

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] **Doctrine + deadly-look-alike matrix lead this index** (above the manifest). ✓
- [ ] Morel / false-morel pair present; **≥3** entries carry a deadly confusable.
- [ ] Every `deadly-lookalike-exists` row is `expert_id_required: true` and (in-entry)
      `field_id_not_appropriate: true`; lethal-toxin rows cite ≥2 T1/T2 refs at safety-read.
- [ ] Each entry opens with the `## ⚠ POSITIVE-ID SAFETY GATE` and carries `## ☠ Deadly Look-Alikes`
      + `## ⚠ MANDATORY PREPARATION`.
