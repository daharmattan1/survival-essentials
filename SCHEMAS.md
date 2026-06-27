# SCHEMAS.md — Entry Schemas for the Survival-Essentials AI Substrate

> This file is the **structural contract** for every Layer-3 entry in `substrate/` and
> `regional/`. It defines the YAML front-matter facets and the fixed body skeleton for each
> entry type. The *rules* governing how these are filled (controlled vocabulary, the WARNING
> block, the answer policy, source tiers) live in [`CONVENTIONS.md`](CONVENTIONS.md). Read both
> before writing any entry.
>
> **An entry is valid only if it carries (a) the full front-matter facet block for its type and
> (b) every body section marked REQUIRED for its type.** Optional sections may be omitted only
> when genuinely not applicable.

This is **life-safety content.** Danger is encoded *structurally* (orthogonal facets + mandatory
body blocks), not left to prose. See `CONVENTIONS.md` §Safety Architecture.

---

## 0. Universal front-matter (EVERY entry, all types)

Every entry begins with a YAML front-matter block. These facets are shared by all types:

```yaml
---
entry_id:        # stable kebab-case id, unique repo-wide, e.g. morel-morchella-spp
title:           # human title, e.g. "Morel (Morchella spp.)"
type:            # one of: WILD-EDIBLE-PLANT | MUSHROOM | CROP | GAME-ANIMAL | KIT-GEAR | METHOD | PROTOCOL | HAZARD | PRINCIPLE
domain:          # owning domain folder, e.g. regional/mid-atlantic-appalachian/mushrooms
region_scope:    # universal | mid-atlantic-appalachian | <future-biome>
usda_zone:       # e.g. 7a  (use "n/a" for universal-technique entries)
confidence:      # high | medium | low  — author's confidence in the entry's correctness
source_tier:     # T1 | T2 | T3 (see CONVENTIONS.md §Source Tiers) — the HIGHEST tier required by this entry's claims
sources:         # list of {title, publisher, url, tier} — see CONVENTIONS.md
last_reviewed:   # ISO date the content was last human safety-read; "draft" until reviewed
review_status:   # draft | reviewed   (set "reviewed" only after the Phase-11 human safety-read)
---
```

### Orthogonal danger facets (EVERY consumable + hazard entry)

A single `danger_class` enum is **BANNED** — it conflated severity, legality, and ID-uncertainty,
and the token `safe` reads as a consumption recommendation. Replace it with these **independent**
facets so an AI can never collapse three different risks into one:

```yaml
edibility_status:     # edible-when-prepared | edible-raw | conditionally-edible | inedible | toxic | deadly-toxic
                      #   NOTE: the literal token "safe" is BANNED for any biology entry.
hazard_severity:      # none | low | moderate | high | lethal
confusability_level:  # none | low | moderate | high | deadly-lookalike-exists
preparation_required: # true | false   (true ⇒ a "## ⚠ MANDATORY PREPARATION" section is REQUIRED)
expert_id_required:   # true | false   (true ⇒ field ID alone is never sufficient)
field_id_not_appropriate: # true | false  (true ⇒ must NEVER be consumed on field ID alone — even by experienced foragers)
legal_status:         # unrestricted | regulated | seasonal-permit | prohibited | emergency-exception
                      #   for game/harvest; use "n/a" where it does not apply
```

> Facets are **filterable and sortable** by a reasoning AI. Indexes float the highest
> `hazard_severity` / `confusability_level` items to the top. The absence of a warning is **never**
> evidence of safety (see `CONVENTIONS.md` §Answer Policy).

---

## 1. WILD-EDIBLE-PLANT

**Front-matter:** universal + orthogonal danger facets. `preparation_required` is almost always
`true` (tannin leaching, cooking, etc.). Add:

```yaml
common_names:     # list
scientific_name:  # binomial
family:           # botanical family
parts_used:       # list, e.g. [young leaves, root]
season:           # harvest window in THIS region, e.g. "Mar–May (leaves), Sep–Oct (acorns)"
habitat:          # where it grows in this biome
```

**Body skeleton** (REQUIRED unless marked optional):

1. `## ⚠ POSITIVE-ID SAFETY GATE` — **REQUIRED, FIRST SECTION.** The positive-ID checklist
   (multiple concurrent traits: morphology + habitat + season) → disqualifying "do-NOT-use-if"
   traits → "Positive ID or do not consume." Uses the standard WARNING block (`CONVENTIONS.md`).
2. `## Deadly / Toxic Look-Alikes` — REQUIRED if `confusability_level` ≥ moderate. Each
   confusable: name → how it differs → what it does to you → why the difference matters.
3. `## Identification` — diagnostic morphology, growth stages, the traits that confirm ID.
4. `## Habitat & Range (this biome)` — where/when it actually grows here.
5. `## ⚠ MANDATORY PREPARATION` — REQUIRED if `preparation_required: true`. The non-omissible
   steps that make it non-lethal/edible (leaching, boil-changes, cooking). **Never summarized away.**
6. `## Uses & Nutrition` — food value, calories if known, other uses.
7. `## Cautions` — allergies, over-consumption, Universal Edibility Test caveat (last-resort only;
   useless for fungi).
8. `## Sources` — tier-appropriate citations.

---

## 2. MUSHROOM

The **highest-consequence** schema in the repo. **Read the mushroom doctrine page
(`regional/<biome>/mushrooms/_index.md` preamble) before writing or reasoning over any fungal
entry.** `expert_id_required` is `true` by default; `field_id_not_appropriate` is `true` for any
species with a deadly look-alike.

**Front-matter:** universal + orthogonal danger facets. Add:

```yaml
common_names:
scientific_name:
spore_print_color:    # diagnostic; "unknown/variable" if so
fruiting_season:      # in THIS region
fruiting_substrate:   # what it grows ON/WITH, e.g. "dead/dying oak", "mycorrhizal with pine"
cook_required:        # true (default true — most edibles are toxic raw)
```

**Body skeleton:**

1. `## ⚠ POSITIVE-ID SAFETY GATE` — **REQUIRED, FIRST SECTION.** Positive-ID checklist
   (morphology + habitat + season + **spore print** where relevant) → disqualifying "do-NOT-use-if"
   traits → explicit statement if `field_id_not_appropriate`. The standard WARNING block.
2. `## ☠ Deadly Look-Alikes` — **REQUIRED.** Every fungal entry names its confusables (or states
   "no deadly look-alike known in this region" only if genuinely true). Each: name → discriminating
   traits → toxin/outcome → "if in doubt, do not eat."
3. `## Identification` — cap, gills/pores/teeth, stem, ring, volva, flesh, bruising, **spore print**,
   smell. Call out white gills / volva / LBM red-flags explicitly.
4. `## Habitat, Substrate & Fruiting (this biome)` — what it grows on, with which trees, what
   season, after what weather.
5. `## ⚠ MANDATORY PREPARATION` — **REQUIRED.** Cook requirement, first-portion/small-test-portion
   rule, no-alcohol where relevant (e.g. inky caps), never mix collections.
6. `## Toxicology of the Confusables` — what the deadly look-alike actually does (e.g. amatoxin
   latency, false-morel hydrazine), so the stakes are explicit.
7. `## Sources` — recognized field guide / regional mycological society (T1/T2 for fungi).

---

## 3. CROP

**Front-matter:** universal + (danger facets usually benign; still include `edibility_status`,
`preparation_required`). Add:

```yaml
common_names:
scientific_name:
zone_fit:          # how it performs in 7a specifically
planting_window:   # last-frost-relative dates for THIS zone
days_to_maturity:
seed_saving:       # brief: open-pollinated? hybrid? how to save
```

**Body skeleton:**

1. `## Zone Fit & Why It Earns Space` — calories/nutrition density, storability, reliability in 7a.
2. `## Planting Windows (Zone 7a)` — REQUIRED. Spring/fall windows relative to last/first frost
   (Baltimore ≈ last frost mid-Apr, first frost ≈ late Oct).
3. `## Growing` — spacing, soil, water, common pests/disease in this region.
4. `## Harvest & Storage` — when/how to harvest; root-cellar / dry / can.
5. `## Seed Saving` — REQUIRED for self-sufficiency: how to keep the line going.
6. `## ⚠ MANDATORY PREPARATION` — only if any part needs processing to be edible (e.g. dry beans
   must be cooked; rhubarb leaves toxic). Include when applicable.
7. `## Sources` — USDA / state extension (T1/T2 for crops).

---

## 4. GAME-ANIMAL

**Front-matter:** universal + orthogonal danger facets (`legal_status` matters here). Add:

```yaml
common_names:
scientific_name:
legal_status:        # normal-season vs emergency-exception; jurisdictional note
season_normal:       # typical regulated season (informational, not legal advice)
internal_cook_temp:  # USDA-recommended internal temperature
```

**Body skeleton:**

1. `## Legal & Ethical Note` — REQUIRED. Normal regulated season vs. genuine-emergency framing;
   "know your local regulations"; not legal advice.
2. `## Identification & Behavior` — what it is, where/when, sign.
3. `## Harvest` — humane, effective method (informational).
4. `## Field Dressing → Skinning → Butchering → Preserving` — REQUIRED for the full-flow species
   (deer is mandatory). The complete chain, each step a sub-heading.
5. `## ⚠ DISEASE & PARASITE` — **REQUIRED.** CWD/prion (never eat brain/spinal/lymph; cannot be
   cooked out), trichinella, tularemia (rabbit-handling gloves), as applicable. The standard
   WARNING block.
6. `## ⚠ MANDATORY PREPARATION` — REQUIRED. Internal cook temps (USDA), aging/cooling, what to
   never eat.
7. `## Sources` — USDA / state DNR / extension (T1/T2 for game + disease).

---

## 5. KIT-GEAR

**Front-matter:** universal (danger facets usually `n/a`/benign). Add:

```yaml
item_class:        # e.g. cutting | fire | water | shelter | nav | medical | signaling
weight_oz:         # backpacker lens — actual carry weight
multi_use:         # list of distinct uses (favor 2+)
tier:              # 1 (EDC) | 2 (bug-out) | 3 (home stockpile)
```

**Body skeleton:**

1. `## What & Why` — the job it does; why it earns weight/space.
2. `## Selection Criteria` — what to look for; failure modes of cheap versions.
3. `## Multi-Use` — REQUIRED — the backpacker discipline of carrying things that do >1 job.
4. `## Maintenance / Failure Modes` — how it breaks; field repair.
5. `## Sources` — optional (T3 acceptable for gear opinion).

---

## 6. METHOD  (universal technique: fire, shelter, water-treatment, nav, fishing, processing)

**Front-matter:** universal. Add danger facets ONLY where the method has a safety boundary
(water treatment ⇒ include `preparation_required: true` and the CONTAMINATION block).

```yaml
method_for:        # the goal, e.g. "disinfect water", "build a fire lay"
materials:         # list
difficulty:        # easy | moderate | hard
```

**Body skeleton:**

1. `## Goal & When To Use` — what it accomplishes; when it's the right call.
2. `## ⚠ CONTAMINATION` — **REQUIRED for every `02_water` method.** Minimum boil time, filter
   micron limit, and the chemical-vs-biological treatment boundary (e.g. chlorine/iodine do NOT
   kill *Cryptosporidium*; filters miss viruses). The standard water WARNING block.
3. `## Steps` — numbered, field-usable.
4. `## ⚠ MANDATORY PREPARATION` — for methods with a non-omissible safety step (treatment time,
   temperature). Include where applicable.
5. `## Failure Modes & Fixes` — what goes wrong; how to recover.
6. `## Sources` — tier-appropriate (CDC/EPA for water; FM 21-76 for field technique).

---

## 7. PROTOCOL  (first-aid; step-ordered emergency response)

**Front-matter:** universal. Add:

```yaml
protocol_for:      # the condition, e.g. "wound infection", "hypothermia"
severity_range:    # mild → life-threatening progression this protocol spans
```

**Body skeleton:**

1. `## Recognize` — signs/symptoms; how to tell stages apart.
2. `## ⚠ RED FLAGS / EVACUATE` — **REQUIRED.** When this exceeds field care → seek help / evac.
3. `## Respond` — numbered steps, escalating with severity.
4. `## ⚠ DO NOT` — **REQUIRED.** The common, dangerous mistakes (e.g. don't rapidly rewarm
   frostbite if refreeze is possible; don't give water to an unconscious person).
5. `## Med Continuity` — where relevant: chronic-med interruption guidance (insulin, anticoagulants,
   etc.), in general terms — not a prescription.
6. `## Sources` — CDC / Red Cross / extension (T1 for medical).

> First-aid entries are **not medical advice** and the protocol must say so. They describe
> commonly-taught field response for when professional care is unavailable.

---

## 8. HAZARD  (snakes, ticks/Lyme, toxic plants-as-hazard, environmental)

**Front-matter:** universal + orthogonal danger facets. Add:

```yaml
hazard_type:       # animal | plant | environmental | biological
```

**Body skeleton:**

1. `## Identify` — what it is, where/when encountered in this biome.
2. `## Avoid` — behavioral avoidance.
3. `## If Exposed / Bitten / Stung` — field response.
4. `## ⚠ WHEN IT'S AN EMERGENCY` — **REQUIRED.** The threshold for urgent care.
5. `## Sources` — CDC / state health / herpetological/extension (T1/T2).

---

## 9. PRINCIPLE  (core survival doctrine: rule of 3s, priorities, mindset)

**Front-matter:** universal (most danger facets `n/a`).

```yaml
principle_for:     # the decision/priority it governs
```

**Body skeleton:**

1. `## The Principle` — the rule, stated plainly.
2. `## Why It Holds` — the physiology/logic behind it.
3. `## How To Apply` — decision framework; what it changes about prioritization.
4. `## Common Failure` — how people get this wrong under stress.
5. `## Sources` — optional.

---

## Manifest row contract (for `_index.md` files)

Every domain `_index.md` carries a manifest table. Each row (one per planned/present entry) MUST
have these columns so an AI can filter on the index alone:

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|

A `check_manifests` checklist (in each `_index.md`) verifies: every row maps to an existing entry
file (no dangling rows), every entry file has a row (no missing rows), and every row's required
columns are filled.

---

## Quick validation (any entry)

- [ ] Front-matter present with all universal facets + type-specific facets.
- [ ] Orthogonal danger facets present (consumables/hazards); **no `danger_class`**; **no `safe`
      token on biology**.
- [ ] First body section is the POSITIVE-ID SAFETY GATE (plant/mushroom) / RECOGNIZE→RED-FLAGS
      (protocol) / CONTAMINATION present (water).
- [ ] `## ⚠ MANDATORY PREPARATION` present iff `preparation_required: true`.
- [ ] Deadly look-alikes section present iff `confusability_level ≥ moderate`.
- [ ] Tier-appropriate sources cited for every `hazard_severity: high|lethal` claim.
- [ ] A manifest row exists in the owning `_index.md`.
