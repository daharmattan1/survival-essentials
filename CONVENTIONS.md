<!--
APPROVED-CONTRACT: 2026-06-27  (approved by Victor's explicit instruction to proceed.
Codex review (Phase 1) was DELIBERATELY SKIPPED at Victor's direction — the Phase-11 human
safety-read of every entry remains the life-safety backstop. Canonical-CC0 LICENSE swap also
skipped per Victor; existing LICENSE left as-is (CC0 summary; GitHub labels it "Other" — cosmetic).)
-->

# CONVENTIONS.md — The Contract Every Entry Is Written Against

> Companion to [`SCHEMAS.md`](SCHEMAS.md). `SCHEMAS.md` defines **structure** (facets + body
> skeletons). This file defines the **rules**: controlled vocabulary, the standardized WARNING
> blocks, the mushroom doctrine, source tiers, the answer policy that stops the substrate from
> surfacing a confident-but-deadly ID, and the per-domain safety-read checklists.
>
> **This is life-safety content.** When a rule here conflicts with brevity or convenience, the
> rule wins. An offline Claude reasoning over this repo inherits these rules through
> [`AGENTS.md`](AGENTS.md).

---

## 1. The cardinal rule

**Positive ID or do not consume.** The repo never tells anyone something is edible on the strength
of a single trait, a single photo, or the *absence* of a warning. Every consumable carries a
positive-ID checklist of *multiple concurrent* traits plus disqualifying "do-NOT-use-if" traits.
For anything with a deadly look-alike, field identification alone is never sufficient.

---

## 2. Controlled vocabulary

These are the **only** permitted values for the danger facets. Do not invent synonyms.

- `edibility_status`: `edible-when-prepared` · `edible-raw` · `conditionally-edible` · `inedible` ·
  `toxic` · `deadly-toxic`
  - **The literal token `safe` is BANNED for any biology entry** (plant, mushroom, game). "Safe"
    reads as a consumption green-light and erases the conditions that make something non-lethal.
- `hazard_severity`: `none` · `low` · `moderate` · `high` · `lethal`
- `confusability_level`: `none` · `low` · `moderate` · `high` · `deadly-lookalike-exists`
- `preparation_required`: `true` · `false`
- `expert_id_required`: `true` · `false`
- `field_id_not_appropriate`: `true` · `false`
- `legal_status`: `unrestricted` · `regulated` · `seasonal-permit` · `prohibited` ·
  `emergency-exception` · `n/a`

**Banned:** the `danger_class` facet (lossy — collapsed severity + legality + ID-uncertainty into
one enum). If you ever see `danger_class` in an entry, it is a contract violation. The orthogonal
facets above replace it.

`type`, `region_scope`, `usda_zone`, `confidence`, `source_tier`, `sources`, `last_reviewed`,
`review_status` are defined in `SCHEMAS.md` §0.

---

## 3. The standardized WARNING block

Wherever a hazard exists (deadly look-alike, prion/parasite, contamination, toxic exposure), use
this exact structure. Defined once here, reproduced in entries — **never abbreviated when an AI
summarizes the entry.**

```
> ⚠ **<HAZARD NAME> — <one-line consequence>**
>
> **Positive-ID checklist (ALL must hold):**
> - <trait 1: morphology>
> - <trait 2: habitat>
> - <trait 3: season / spore print / other concurrent confirmation>
>
> **Do NOT use if ANY of these are present (disqualifying traits):**
> - <disqualifier 1>
> - <disqualifier 2>
>
> **Confusable with:** <deadly look-alike> → <how it differs> → <what it does to you>
>
> **Verdict:** Positive ID on every checklist item, or do not consume. <If
> field_id_not_appropriate: "This species must never be eaten on field identification alone.">
```

---

## 4. Mushroom doctrine (loads before ANY species entry)

The mushroom `_index.md` opens with this doctrine page. It is the single most important safety
construct in the repo — fungal misidentification is the highest-consequence failure mode.

**Doctrine (non-negotiable for a novice):**
1. **No consumption without expert confirmation** — a regional mycological society, an expert, or
   a definitive multi-source positive ID. Photo-only ID is never sufficient.
2. **No LBMs** — little brown mushrooms are not worth the risk; too many toxic look-alikes.
3. **No white-gilled mushrooms with a volva or ring** — the *Amanita* pattern (destroying angel,
   death cap) is lethal and easy to misjudge.
4. **No decayed or insect-damaged specimens**, no mixed collections in one bag.
5. **Spore print** where the ID depends on it.
6. **Cook by default** — most edibles are toxic or indigestible raw.
7. **First-portion rule** — even a confirmed edible: small portion, no alcohol where relevant
   (e.g. inky caps), wait, never try two new species at once.
8. **When in doubt, throw it out.** The downside is asymmetric: a missed meal vs. a destroyed liver.

Every mushroom entry's facets must reflect this: `expert_id_required: true`, and
`field_id_not_appropriate: true` for any species with a deadly look-alike.

---

## 5. Water `⚠ CONTAMINATION` block (every `02_water` entry)

Waterborne pathogens kill faster than starvation. Every water method/entry carries:

```
> ⚠ **CONTAMINATION — what this method does and does NOT handle**
>
> - **Boil:** rolling boil ≥1 min (≥3 min above 6,500 ft / 2,000 m). Kills bacteria, viruses,
>   protozoa (incl. *Cryptosporidium*, *Giardia*). Does NOT remove chemical/heavy-metal contamination.
> - **Filter:** state the micron rating. ≤1 µm absolute removes *Crypto*/*Giardia*. Most filters
>   do NOT remove viruses (too small) — pair with chemical/UV in virus-risk water.
> - **Chemical (chlorine/iodine):** kills bacteria + viruses; does **NOT** reliably kill
>   *Cryptosporidium*. Longer contact time in cold/cloudy water. Iodine: not for pregnancy/thyroid
>   conditions/long-term.
> - **The boundary:** no single method covers chemical + biological + viral + protozoan at once.
>   State which threats remain after this method.
```

Fill the specifics per method; never delete the chemical-vs-biological boundary line.

---

## 6. `## ⚠ MANDATORY PREPARATION` — the never-summarize rule

Every consumable (plant, mushroom, game, and any water/plant METHOD with a treatment step) carries
a `## ⚠ MANDATORY PREPARATION` body section: the non-omissible steps that make the thing
non-lethal — tannin leaching, multiple boil-water changes, internal cook temperature, filter
micron / boil time.

**An AI summarizing or excerpting an entry MUST reproduce this section verbatim and MUST NOT
compress it.** Dropping a boil-change or a cook-temp from a summary can kill. `AGENTS.md` repeats
this instruction for the reasoning layer.

---

## 7. Source tiers

High-risk claims require authoritative sources. "Written fresh + a field guide cited" is the
**floor**, not the ceiling, for life-safety claims.

| Tier | What | Use for |
|------|------|---------|
| **T1** | Government / official health & safety: CDC, FEMA, Red Cross, EPA, USDA, state extension, state DNR/health dept | First-aid, disease, water treatment, cook temps, game/crop windows, legal-status framing |
| **T2** | Recognized authority: a major field guide (Peterson, Audubon), a regional mycological society, FM 21-76 / FM 3-05.70, FAO | Plant/mushroom ID, field technique, processing |
| **T3** | Practitioner consensus / reputable how-to | Gear opinion, non-safety technique nuance |

Rules:
- Every entry with `hazard_severity: high|lethal` cites a **tier-appropriate** source (T1 for
  medical/disease/water; T1/T2 for fungi/game/plants).
- Each mushroom/plant species **and each of its deadly look-alikes** is triangulated against **≥2**
  authoritative references during the Phase-11 safety read.
- Cite the specific source in the entry's `## Sources` + the `sources:` front-matter list. Log any
  external image in `_media/SOURCES.md` (URL + license + attribution).

**Seed source library (from the repo's existing resource files):** USDA PLANTS, USDA Weed Images,
USDA Pomological Watercolors, Biodiversity Heritage Library, Peterson *Field Guide to Edible Wild
Plants* (Eastern/Central NA), Wikimedia Commons (PD/CC0 only); FM 21-76 / FM 3-05.70, FAO fish
manuals, Rawpixel (CC0). CDC / Red Cross / EPA / state extension for medical + water.

---

## 8. Imagery rules

- **NO AI-generated identification imagery** for plants/mushrooms — hallucinated look-alikes can
  kill. Hard rule. Generated images are permitted ONLY for **technique diagrams** (knots, traps,
  field-dressing geometry) in `_media/diagrams/`, and even then prefer adapting public-domain
  FM 21-76 line art.
- **Real ID photos** (the deadly-look-alike pairs pulled local into `_media/photos/`) must be
  genuinely public-domain / CC0, and must show **multiple angles + whole organism + key diagnostic
  structures + habitat context**. A single photo is never enough.
- Images are **supporting evidence, never sufficient for ID.** Every entry that links a photo says
  so.
- Every external image is logged in `_media/SOURCES.md`: URL + license + attribution.

---

## 9. Answer policy (the substrate must not surface a confident-but-deadly ID)

This policy lives here and in `AGENTS.md`; it governs how a reasoning AI uses the substrate.

1. **Uncertainty-first.** Lead consumption/ID answers with the safety gate and the uncertainty,
   not with a verdict. Surface the positive-ID checklist before any "this looks like X."
2. **Never infer edibility from the absence of a warning.** A missing hazard section is missing
   data, not a green light.
3. **Cite the specific loaded entries.** Ground every claim in the entry it came from; name it.
4. **Refuse field-ID-only consumption calls for `expert_id_required` species.** For any species
   flagged `field_id_not_appropriate: true`, refuse to confirm "yes, eat it" on description/photo
   alone — direct to expert confirmation, spore print, multi-source triangulation.
5. **Reproduce `⚠ MANDATORY PREPARATION` verbatim** in any answer that touches a consumable.
6. **Distinguish normal vs. emergency** for `legal_status`; never present harvesting regs as legal
   advice.
7. **First-aid is not medical advice** — commonly-taught field response for when EMS is
   unavailable; say so.

---

## 10. Per-domain safety-read checklists (Phase 11, human gate)

Victor runs these against the written entries before any PR. Pass ⇒ write `SAFETY-READ-PASSED` +
sign-off into `CHANGELOG.md` and set entry `review_status: reviewed`.

### Mushrooms & edible-plants
- [ ] Every entry opens with the POSITIVE-ID SAFETY GATE (checklist + disqualifying traits), not a
      single test.
- [ ] Each species **and each deadly look-alike** triangulated against **≥2** T1/T2 references.
- [ ] `confusability_level`, `expert_id_required`, `field_id_not_appropriate` set truthfully.
- [ ] Mushroom doctrine page loads before species; deadly-look-alike matrix populated and leads the
      index; "what NOT to eat" comes before edible exemplars.
- [ ] Morel / false-morel pair present; ≥3 mushroom entries carry a deadly confusable.
- [ ] `⚠ MANDATORY PREPARATION` present and correct on every consumable.

### Game animals
- [ ] CWD-prion / trichinella / tularemia block present and correct where applicable.
- [ ] Internal cook temps match USDA; deer entry has the full field-dress→skin→butcher→preserve
      flow.
- [ ] `legal_status` distinguishes normal season vs. emergency-exception; framed as "know your
      regs," not legal advice.

### First-aid & water
- [ ] First-aid covers wound infection, hypo/hyperthermia, dehydration/diarrhea, med-continuity;
      each has RED FLAGS / EVAC + DO NOT.
- [ ] Every water entry has the `⚠ CONTAMINATION` block with boil time, micron limit, and the
      chemical-vs-biological boundary.
- [ ] All medical/water claims verified vs. CDC / Red Cross / EPA / extension (T1).

### Coherence (all domains)
- [ ] Manifests pass `check_manifests` (no dangling/missing rows; required columns filled).
- [ ] Survey files link down; food resolves via `regional/_index.md` registry → `food_hub.md`; no
      broken intra-repo links.
- [ ] `grep -rn "danger_class" .` = 0; no `safe` token on biology facets.

---

## 11. Repo & file conventions

- **Entry filenames:** `entry_id.md` (the front-matter `entry_id`), kebab-case.
- **One entity per entry file.** No multi-species files.
- **Universal technique** → `substrate/`. **Region-bound biology** (edibles, mushrooms, game,
  crops, local hazards) → `regional/<biome>/` — because season, habitat, look-alikes, and legality
  are biome variables.
- **The universal `substrate/05_food/_index.md` does NOT hardlink a biome.** It links the
  `regional/_index.md` **registry**; the AI resolves food/consumption queries by pivoting through
  the active region's `food_hub.md`.
- **Windows/OS:** use `cp` + `rm` for renames, never `git mv`.
- **`last_reviewed` / `review_status`:** `draft` until the Phase-11 human safety read flips it to
  `reviewed`. The survey↔substrate sync checklist lives in `CHANGELOG.md`.
- This is a **standalone repo** (not part of any parent knowledge base) — entries do not carry the
  parent repo's frontmatter taxonomy; they carry the facets defined in `SCHEMAS.md`.

---

## 12. What this repo is (and is not)

A **survey + substrate**: the 11 numbered files are the human doorway (Layer 1, unchanged bodies);
`substrate/` + `regional/` are the room a reasoning AI queries (Layers 2–3). It is **not** medical,
legal, or professional foraging advice; it is a structured offline knowledge base whose entire
design goal is to refuse a confident-but-deadly identification and to lead with uncertainty and the
positive-ID gate. Know your local regulations. Positive ID or do not consume.
