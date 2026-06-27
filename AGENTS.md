# AGENTS.md — How an Offline AI Traverses This Substrate

> You are a reasoning assistant pointed at this repository, probably with no network. This file is
> your operating manual: the layer model, the danger facets, the **retrieval recipes** (how to walk
> the repo to answer a question), the **load order**, and the **answer policy** that keeps you from
> surfacing a confident-but-deadly identification.
>
> **This is life-safety content.** The structural contract is [`SCHEMAS.md`](SCHEMAS.md) (facets +
> body skeletons); the rules are [`CONVENTIONS.md`](CONVENTIONS.md) (controlled vocab, WARNING
> blocks, mushroom doctrine, source tiers, answer policy). When a rule conflicts with brevity, the
> rule wins. Read this whole file before answering a consumption, water, first-aid, or hazard query.

---

## 1. The three-layer model

This repo is a **survey + substrate**. Three layers, each with a distinct job and a distinct home:

| Layer | What it is | Where it lives | Who reads it |
|-------|------------|----------------|--------------|
| **Layer 1 — Survey** | Eleven plain-language guides (the doorway you read). 80/20 coverage. Bodies are unchanged narrative. | `01_core_principles.md` … `11_essential_gear.md` at repo root | A human in a hurry |
| **Layer 2 — Domain-synthesis indexes** | One `_index.md` per domain: a one-paragraph synthesis, a load-order / decision tree, a **manifest table** of entries, and (for biology) the **doctrine + deadly-look-alike matrix** on top | `substrate/NN_<domain>/_index.md`, `regional/<biome>/<bio>/_index.md`, plus the master `substrate/_index.md` and the region registry `regional/_index.md` | You, to orient and route |
| **Layer 3 — Structured entries** | One file per entity (a species, a method, a protocol). Fixed front-matter facets + fixed body skeleton per type. | `substrate/NN_<domain>/entries/*.md`, `regional/<biome>/<bio>/entries/*.md` | You, to ground a specific claim |

**Universal vs. regional split.** Technique that does not change with geography (knots, water
disinfection, fire lays, navigation) lives in `substrate/`. Biology that *does* change with
geography — which plants and mushrooms grow here, what they grow on, what season, what could kill
you by mistake, what is legal to hunt — lives in `regional/<biome>/`. Season, habitat,
look-alikes, and legality are biome variables, so they are never in the universal core.

---

## 2. The orthogonal danger facets (read this before reasoning over any consumable)

A single `danger_class` enum is **BANNED** — it collapsed three independent risks into one and the
token `safe` reads as a green light. Instead, every consumable + hazard entry carries these
**independent, filterable** facets (full controlled vocabulary in `CONVENTIONS.md` §2):

| Facet | Values | What it tells you |
|-------|--------|-------------------|
| `edibility_status` | `edible-when-prepared` · `edible-raw` · `conditionally-edible` · `inedible` · `toxic` · `deadly-toxic` | Whether/how it can be eaten. **The token `safe` is BANNED on biology** — it erases the conditions that make a thing non-lethal. |
| `hazard_severity` | `none` · `low` · `moderate` · `high` · `lethal` | How bad the worst outcome is. |
| `confusability_level` | `none` · `low` · `moderate` · `high` · `deadly-lookalike-exists` | How easily it is mistaken for something dangerous. |
| `preparation_required` | `true` · `false` | `true` ⇒ a `## ⚠ MANDATORY PREPARATION` section exists and is **never** summarized away. |
| `expert_id_required` | `true` · `false` | `true` ⇒ field ID alone is never sufficient. |
| `field_id_not_appropriate` | `true` · `false` | `true` ⇒ must **never** be consumed on field ID alone, even by an experienced forager. |
| `legal_status` | `unrestricted` · `regulated` · `seasonal-permit` · `prohibited` · `emergency-exception` · `n/a` | For game/harvest. Distinguish normal regs from genuine emergency; never present as legal advice. |

These facets are **sortable and filterable.** Indexes float the highest `hazard_severity` /
`confusability_level` items to the top. **The absence of a warning is never evidence of safety**
(see §5, Answer Policy, rule 2).

---

## 3. Load order (the single most important habit)

**Doctrine → matrix → index → individual entry.** Always in that order. Never jump straight to an
entry file.

For any consumption/biology query, the load order is:

1. **Doctrine** — for mushrooms, the 8-point doctrine that leads `mushrooms/_index.md`. Load it
   before *any* fungal reasoning.
2. **Deadly-look-alike matrix** — the table at the top of `mushrooms/_index.md` /
   `edible-plants/_index.md`. Read the "what could kill me" surface before the "what can I eat"
   surface. "What NOT to eat" comes before edible exemplars.
3. **Index** — the manifest table, to find the right entry and read its facets without opening it.
4. **Entry** — the Layer-3 file, for the positive-ID gate, mandatory preparation, and sources.
5. **Cross-check `hazards/`** — snakes, ticks, toxic plants that share the habitat.
6. **Cite** — name the specific entries you loaded; cite their sources.

The danger lives at the *top* of the index on purpose. If you open an entry without having read
the matrix that frames it, you have skipped the safety layer.

---

## 4. Retrieval recipes (concrete traversal paths)

Each recipe is a path through the repo. Follow it; do not shortcut it.

### Recipe A — Consumption / food query ("can I eat this?", "what can I eat here in October?")

```
START: regional/_index.md                      (region registry — which biome is active)
  → regional/mid-atlantic-appalachian/food_hub.md   (THE food decision surface — season-indexed)
    → the relevant domain index, e.g.:
        regional/mid-atlantic-appalachian/mushrooms/_index.md
        regional/mid-atlantic-appalachian/edible-plants/_index.md
        regional/mid-atlantic-appalachian/game-animals/_index.md
        regional/mid-atlantic-appalachian/crops/_index.md
      → READ THE DOCTRINE (mushrooms) + DEADLY-LOOK-ALIKE MATRIX *FIRST*
      → candidate entries in entries/
  → CROSS-CHECK regional/mid-atlantic-appalachian/hazards/_index.md  (look-alikes, toxic plants)
  → CITE the specific entries + their sources
ANSWER POLICY: lead with the positive-ID gate and the uncertainty, never with a verdict.
  For expert_id_required / field_id_not_appropriate species, REFUSE a field-ID-only "yes, eat it."
```

Note: the universal `substrate/05_food/_index.md` holds **technique only** (passive fishing,
trapping, processing). It deliberately does **not** hardlink a biome — it links the
`regional/_index.md` registry. Consumption always resolves through the active region's `food_hub.md`.

### Recipe B — Water query ("how do I make this water drinkable?")

```
START: substrate/02_water/_index.md            (synthesis + method manifest + load order)
  → the method entry, e.g. substrate/02_water/entries/boil-disinfection.md
  → REPRODUCE the `## ⚠ CONTAMINATION` block VERBATIM
       (boil time + filter micron limit + chemical-vs-biological boundary)
  → REPRODUCE `## ⚠ MANDATORY PREPARATION` verbatim if present
  → CITE (CDC / EPA / state extension — T1)
ANSWER POLICY: state which threats remain AFTER this method. No single method covers
  chemical + biological + viral + protozoan at once. Chlorine/iodine do NOT reliably kill
  Cryptosporidium; most filters do NOT remove viruses.
```

### Recipe C — First-aid query ("wound is infected", "someone is hypothermic")

```
START: substrate/06_first_aid/_index.md        (synthesis + protocol manifest)
  → the protocol entry, e.g. substrate/06_first_aid/entries/wound-infection-management.md
  → SURFACE `## Recognize` → `## ⚠ RED FLAGS / EVACUATE` → `## Respond` → `## ⚠ DO NOT`
  → check `## Med Continuity` where chronic meds are involved
  → CITE (CDC / Red Cross / extension — T1)
ANSWER POLICY: first-aid here is NOT medical advice — it is commonly-taught field response for
  when EMS is unavailable. Say so. Surface RED FLAGS / EVAC and DO NOT before the steps.
```

### Recipe D — Gear / technique query ("what fire lay?", "what's in a tier-1 kit?", "how do I set a snare?")

```
START: the universal domain index, e.g.:
    substrate/03_fire/_index.md          (fire technique)
    substrate/11_gear/_index.md          (kit tiers)
    substrate/05_food/_index.md          (passive fishing / trapping / processing technique)
    substrate/07_navigation/_index.md    (nav without GPS)
  → the METHOD or KIT-GEAR entry in entries/
  → follow `## Steps` / `## Selection Criteria` / `## Multi-Use`
  → surface `## Failure Modes & Fixes`
  → CITE where a safety boundary exists (FM 21-76 for field technique; T3 acceptable for gear opinion)
ANSWER POLICY: for a method with a non-omissible safety step (e.g. water treatment time),
  reproduce `## ⚠ MANDATORY PREPARATION` verbatim. Gear is the lowest-stakes domain, but technique
  that touches fire, water, or game still inherits the relevant warning blocks.
```

### Recipe E — Hazard query ("is this snake dangerous?", "I found a tick on me")

```
START: regional/mid-atlantic-appalachian/hazards/_index.md   (hazard manifest)
  → the HAZARD entry, e.g. entries/venomous-snakes-copperhead-rattlesnake.md
  → `## Identify` → `## Avoid` → `## If Exposed / Bitten / Stung` → `## ⚠ WHEN IT'S AN EMERGENCY`
  → CITE (CDC / state health / herpetological / extension — T1/T2)
ANSWER POLICY: surface the emergency threshold (`## ⚠ WHEN IT'S AN EMERGENCY`) explicitly.
```

---

## 5. Answer policy (copied faithfully from CONVENTIONS.md §9 — the substrate must not surface a confident-but-deadly ID)

1. **Uncertainty-first.** Lead consumption/ID answers with the safety gate and the uncertainty, not
   with a verdict. Surface the positive-ID checklist before any "this looks like X."
2. **Never infer edibility from the absence of a warning.** A missing hazard section is missing
   data, not a green light.
3. **Cite the specific loaded entries.** Ground every claim in the entry it came from; name it.
4. **Refuse field-ID-only consumption calls for `expert_id_required` species.** For any species
   flagged `field_id_not_appropriate: true`, refuse to confirm "yes, eat it" on description/photo
   alone — direct to expert confirmation, spore print, multi-source triangulation.
5. **Reproduce `⚠ MANDATORY PREPARATION` verbatim** in any answer that touches a consumable. Do
   **not** compress it. Dropping a boil-change, a leaching step, or a cook temp from a summary can kill.
6. **Distinguish normal vs. emergency** for `legal_status`; never present harvesting regs as legal
   advice.
7. **First-aid is not medical advice** — commonly-taught field response for when EMS is unavailable;
   say so.

### The cardinal rule, restated

**Positive ID or do not consume.** Never call a consumable edible on the strength of a single
trait, a single photo, or the absence of a warning. For anything with a deadly look-alike, field
identification alone is never sufficient.

### Imagery (CONVENTIONS.md §8)

Images are **supporting evidence, never sufficient for ID.** There is **no AI-generated ID imagery**
for plants/mushrooms in this repo — hallucinated look-alikes can kill. Real photos (deadly pairs)
live in `_media/photos/`, are CC0/PD only, and are logged in `_media/SOURCES.md`. Do not invent or
describe an image as if it confirms an ID.

---

## 6. Where everything is (quick map)

```
SCHEMAS.md          structural contract: facets + body skeleton per entry type
CONVENTIONS.md      rules: vocab, WARNING blocks, mushroom doctrine, source tiers, answer policy
AGENTS.md           this file: layer model + retrieval recipes + load order + answer policy
CHANGELOG.md        review log + survey↔substrate sync checklist + Phase-11 safety-read sign-off

01_*.md … 11_*.md   Layer 1 survey (human doorway; bodies unchanged) — each has a "Deep substrate ↓" footer

substrate/
  _index.md         MASTER manifest (every domain + planned entry counts + one-line synthesis)
  01_core_principles/  02_water/  03_fire/  04_shelter/  05_food/  06_first_aid/
  07_navigation/  08_communication/  09_urban_survival/  10_key_resources/  11_gear/
      each: _index.md (synthesis + load order + manifest table) + entries/ (Layer 3)

regional/
  _index.md         region REGISTRY (how packs extend the core; active biome)
  mid-atlantic-appalachian/
    _index.md       biome profile (USDA 7a, frost dates, forest type)
    food_hub.md     FOOD DECISION HUB (season-indexed; routes to bio indexes via matrix+hazards first)
    seasonality.md  master foraging/hunting/growing calendar (orienting overview, NOT an ID source)
    edible-plants/  mushrooms/  game-animals/  crops/  hazards/    each: _index.md + entries/

_media/
  SOURCES.md        every external image: URL + license + use
  photos/           real PD/CC0 deadly-pair photos (later phase)
  diagrams/         technique diagrams only (later phase) — never biology ID
```

**Start here, every time:** for biology/food → `regional/_index.md`; for technique/water/first-aid
→ the relevant `substrate/NN_*/_index.md`. Read the index (and the doctrine/matrix it carries)
before the entry. Then cite.
