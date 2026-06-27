# Survival Essentials — Survey + Substrate

A practical, offline "just in case" survival knowledge base. Two layers:

- **The survey** — the doorway you *read.* Eleven plain-language guides covering the 20% of
  survival knowledge that handles 80% of realistic scenarios (power outage, disaster, urban
  disruption, medical emergency without EMS).
- **The substrate** — the room you *ask.* Dense, consistently-structured markdown beneath the
  survey that an offline AI can reason across — region-grounded so it can answer "which mushrooms
  fruit on oak *here* in October, and what could kill me by mistake?" without ever surfacing a
  confident-but-deadly identification.

The survey is for a human in a hurry. The substrate is for a reasoning assistant you point at this
repo when the network is gone.

**What's inside (pass 1):** 11 survey guides + **60 structured substrate entries** across 16 domains,
region-grounded to Mid-Atlantic / Appalachian (USDA zone 7a). Jump straight in:
[`AGENTS.md`](AGENTS.md) (how an AI traverses it) ·
[`regional/mid-atlantic-appalachian/food_hub.md`](regional/mid-atlantic-appalachian/food_hub.md)
("what can I eat here, and what could kill me?") ·
[`regional/mid-atlantic-appalachian/mushrooms/_index.md`](regional/mid-atlantic-appalachian/mushrooms/_index.md)
(mushroom doctrine + deadly-look-alike matrix).

> **Verification.** Entries are **agentically verified** — every safety-critical claim fact-checked
> against authoritative sources (CDC, USDA, WHO, Red Cross, mycological societies, poison control)
> across multiple adversarial review passes, plus an offline read-test confirming the substrate
> leads with the safety gate and refuses a field-ID-only "yes, eat it." This is *not* a substitute
> for an expert's hand-read — corrections and a domain-expert review are welcome (see
> [`CHANGELOG.md`](CHANGELOG.md) and [`_media/ACCURACY_AUDIT_2026-06-27.md`](_media/ACCURACY_AUDIT_2026-06-27.md)).

---

## ⚠ Safety first — read this

This repository is **not medical, legal, or professional foraging advice.** It is a structured
knowledge base whose entire design goal is to make you *slow down* around the things that kill
people.

- **Positive ID or do not consume.** Nothing here is "edible" on the strength of one trait, one
  photo, or the absence of a warning. Every consumable carries a positive-ID checklist of multiple
  concurrent traits plus disqualifying "do-NOT-use-if" traits.
- **Mushrooms and toxic-plant look-alikes can kill you even if you're careful.** Anything with a
  deadly look-alike must be confirmed by an expert or definitive multi-source ID — never field ID
  alone. See the mushroom doctrine page in the substrate.
- **Know your local regulations.** Harvest/hunting rules are jurisdictional; emergency framing is
  not legal advice.
- **First aid here is commonly-taught field response** for when EMS is unavailable — not a
  substitute for professional care or your own prescriptions.

The safety rules are encoded *structurally* (see [`CONVENTIONS.md`](CONVENTIONS.md) and
[`SCHEMAS.md`](SCHEMAS.md)), not left to prose.

---

## Layer 1 — The Survey (read offline)

1. **[Core Survival Principles](01_core_principles.md)** — Rule of 3s, priorities, mindset
2. **[Water](02_water.md)** — Procurement, purification, storage
3. **[Fire](03_fire.md)** — Starting methods, maintenance, safety
4. **[Shelter](04_shelter.md)** — Emergency shelter, insulation, location
5. **[Food](05_food.md)** — Foraging, fishing, hunting, growing, preservation
6. **[First Aid](06_first_aid.md)** — Critical injuries, common ailments
7. **[Navigation](07_navigation.md)** — Without GPS, celestial, terrain reading
8. **[Communication](08_communication.md)** — Signals, radio basics, mesh networks
9. **[Urban Survival](09_urban_survival.md)** — Power outages, civil disruption, bugging in
10. **[Key Resources](10_key_resources.md)** — Minimal external references for deeper learning
11. **[Essential Gear & Materials](11_essential_gear.md)** — 3-tier system, bug-out bag, home stockpile

Each survey file ends with a **`## Deep substrate ↓`** footer linking down to its structured
entries.

---

## Layer 2/3 — The Substrate (ask offline)

Structured, queryable knowledge an AI loads to reason — not narrative reading. Start an assistant
at [`AGENTS.md`](AGENTS.md): it explains the layer model, the danger facets, and the **retrieval
recipes** (how to traverse the repo to answer a question).

```
substrate/        Universal technique (water, fire, shelter, first-aid, nav, comms, gear …)
  _index.md       Master manifest: every domain + entry counts
  NN_<domain>/     _index.md (synthesis + manifest) + entries/ (one file per entity)

regional/         Region-bound biology — because season, habitat, look-alikes, legality are biome variables
  _index.md       Region registry
  mid-atlantic-appalachian/   Victor's biome first: USDA 7a, temperate deciduous forest
    _index.md     Biome profile (zone, frost dates, forest type)
    food_hub.md   FOOD DECISION HUB — composes plants + mushrooms + game + crops + seasonality into one surface
    seasonality.md
    edible-plants/  mushrooms/ (doctrine + deadly-lookalike matrix on top)  game-animals/  crops/  hazards/

_media/           SOURCES.md (every external image + license) · photos/ (real CC0 deadly-pair photos: morel/false-morel, wild-onion/death-camas, destroying-angel) · ACCURACY_AUDIT (the verification trail)
```

**Why split universal vs. regional?** Knot-tying and water disinfection don't change with
geography; which mushrooms fruit, what they grow on, and what could kill you by mistake absolutely
do. Region packs (Mid-Atlantic / Appalachian first) hold the biology; the universal core holds the
technique. Food queries resolve through the active region's `food_hub.md`, so "what can I eat here
in October" hits one coherent page instead of six scattered indexes.

---

## Repo documents

| File | What |
|------|------|
| [`README.md`](README.md) | This map |
| [`AGENTS.md`](AGENTS.md) | How an offline AI traverses the substrate (layer model, facets, retrieval recipes, answer policy) |
| [`SCHEMAS.md`](SCHEMAS.md) | The structural contract — front-matter facets + body skeleton per entry type |
| [`CONVENTIONS.md`](CONVENTIONS.md) | The rules — controlled vocab, WARNING blocks, mushroom doctrine, source tiers, **answer policy**, safety-read checklists |
| [`CHANGELOG.md`](CHANGELOG.md) | Review log + survey↔substrate sync checklist + the safety-read sign-off |
| [`_media/ACCURACY_AUDIT_2026-06-27.md`](_media/ACCURACY_AUDIT_2026-06-27.md) | The verification trail — every fact-check finding + its sourced fix |
| [`LICENSE`](LICENSE) | CC0 1.0 Universal (public domain dedication) |

---

## The no-power backup (physical-book layer)

The substrate assumes you have *something* that runs markdown (a phone, a laptop). For true
lights-out, keep the physical/PDF layer the original survey already curated:

- **FM 21-76 / FM 3-05.70 U.S. Army Survival Manual** (Archive.org) — comprehensive, illustrated,
  public domain.
- **SAS Survival Handbook** — classic comprehensive reference.
- **Local Red Cross first-aid course** — hands-on medical training nothing offline replaces.
- Public-domain ID image sources (Biodiversity Heritage Library, USDA PLANTS, Peterson field
  guide) — see [`10_key_resources.md`](10_key_resources.md) and `_media/SOURCES.md`.

Total storage for the complete offline base is small (~<10MB of markdown + a curated handful of
deadly-look-alike photos).

---

## Scope (this pass)

**Pass 1 is built and verified**: the full pyramid + schemas across every domain, 60 worked
exemplar entries (3–5 per domain), region-grounded for Mid-Atlantic / Appalachian (USDA 7a), every
safety-critical claim fact-checked against authoritative sources and offline-tested. It proves the
pattern end to end.

Deliberately **later passes**: deepening (more entries per domain), more local deadly-look-alike
photos, additional region packs, and a domain-expert hand-read. Kept hand-reviewable and
in-the-loop rather than auto-generated at scale. Contributions and corrections welcome.

---

**Curated by** Victor Sowers · **License** CC0 (public domain dedication) · Pull requests welcome.
