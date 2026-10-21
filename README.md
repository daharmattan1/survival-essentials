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

> **Do not use this repository alone to identify, eat or treat anything.** Positive identification
> by an expert, or do not consume. If someone may have been poisoned, call Poison Control at
> **1-800-222-1222** or **911**.

**What's inside (pass 2, 2026-10):** 11 survey guides and **116 structured substrate entries**: 67
universal entries across 11 domains, and 49 regional entries in two regions (Mid-Atlantic /
Appalachian, 34; Northeast / New England, 15). Jump straight in:
[`AGENTS.md`](AGENTS.md) (how an AI traverses it) ·
[`regional/mid-atlantic-appalachian/food_hub.md`](regional/mid-atlantic-appalachian/food_hub.md)
and [`regional/northeast-new-england/food_hub.md`](regional/northeast-new-england/food_hub.md)
("what can I eat here, and what could kill me?") ·
[`regional/mid-atlantic-appalachian/mushrooms/_index.md`](regional/mid-atlantic-appalachian/mushrooms/_index.md)
and [`regional/northeast-new-england/mushrooms/_index.md`](regional/northeast-new-england/mushrooms/_index.md)
(mushroom doctrine and deadly-look-alike matrix).

> **Verification status: no human has read this yet.** Every entry is marked `agent-verified`. That
> means AI agents that did not write the entry checked each claim against sources they opened
> themselves, in at least two rounds. It does **not** mean a person checked it. No entry has had a
> human safety read.
>
> The first pass labelled its entries `reviewed`. Those labels came from AI-only checks, and pass 2
> found serious errors in many of them (23 critical errors in the Mid-Atlantic biology entries
> alone). All of those labels were replaced. Read the audits before trusting anything older:
> [survey wave 1](_media/ACCURACY_AUDIT_2026-10_survey-wave1.md) ·
> [wave 2a](_media/ACCURACY_AUDIT_2026-10_survey-wave2a.md) ·
> [wave 2b](_media/ACCURACY_AUDIT_2026-10_survey-wave2b.md) ·
> [universal entries](_media/ACCURACY_AUDIT_2026-10_universal.md) ·
> [Mid-Atlantic biology](_media/ACCURACY_AUDIT_2026-10_biology.md) ·
> [pass 1](_media/ACCURACY_AUDIT_2026-06-27.md).
>
> A person with the right expertise can change this. [`review/SAFETY_READ_PACKET.md`](review/SAFETY_READ_PACKET.md)
> explains how to do the read one domain at a time, and [`CONTRIBUTING.md`](CONTRIBUTING.md) explains
> how to file a correction or an expert review. Only a human can mark an entry `reviewed`.

---

## ⚠ Safety first — read this

This repository is **not medical, legal, or professional foraging advice.** It is a structured
knowledge base whose entire design goal is to make you *slow down* around the things that kill
people.

- **Positive ID or do not consume.** Nothing here is "edible" on the strength of one trait, one
  photo, or the absence of a warning. Every consumable carries a positive-ID checklist of multiple
  concurrent traits plus disqualifying "do-NOT-use-if" traits.
- **Mushrooms and toxic-plant look-alikes can kill you even if you're careful.** Anything with a
  deadly look-alike must be confirmed by an expert who has examined it in hand, in addition to
  multi-source ID — never field ID alone. See the mushroom doctrine page in the substrate.
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
  northeast-new-england/      Second region pack
    (each region has:)
    _index.md     Biome profile (zone, frost dates, forest type)
    food_hub.md   FOOD DECISION HUB — composes plants + mushrooms + game + crops + seasonality into one surface
    seasonality.md
    edible-plants/  mushrooms/ (doctrine + deadly-lookalike matrix on top)  game-animals/  crops/  hazards/

_media/           SOURCES.md (every external image + license) · photos/ (real CC0 deadly-pair photos: morel/false-morel, wild-onion/death-camas, destroying-angel) · ACCURACY_AUDIT_* (the verification trail)
review/           SAFETY_READ_PACKET.md + per-domain checklists for the human safety read
scripts/          mark_reviewed.py (run by a human only)
```

**Why split universal vs. regional?** Knot-tying and water disinfection don't change with
geography; which mushrooms fruit, what they grow on, and what could kill you by mistake absolutely
do. Region packs (Mid-Atlantic / Appalachian and Northeast / New England so far) hold the biology; the universal core holds the
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
| [`CONTRIBUTING.md`](CONTRIBUTING.md) | How to file a correction or an expert review; the rules that never change |
| [`review/SAFETY_READ_PACKET.md`](review/SAFETY_READ_PACKET.md) | How a person does the human safety read, one domain at a time |
| [`CHANGELOG.md`](CHANGELOG.md) | Change log + survey↔substrate sync checklist + the (still empty) human sign-off table |
| `_media/ACCURACY_AUDIT_*.md` | The verification trail: pass 1 and the five pass-2 audits (linked above) |
| [`LICENSE`](LICENSE) | CC0 1.0 Universal (public domain dedication) |

---

## The no-power backup (physical-book layer)

The substrate assumes you have *something* that runs markdown (a phone, a laptop). For true
lights-out, keep the physical/PDF layer the original survey already curated:

- **FM 21-76 / FM 3-05.70 U.S. Army Survival Manual** (Archive.org) — comprehensive, illustrated,
  public domain.
- **SAS Survival Handbook** — classic comprehensive reference.
- **Local Red Cross first-aid course** — hands-on medical training nothing offline replaces.
- ID image sources (Biodiversity Heritage Library and USDA PLANTS; licenses vary by item or
  image, so check each one) — see [`10_key_resources.md`](10_key_resources.md) and
  `_media/SOURCES.md`. The Peterson field guide is copyrighted: buy or borrow it, do not copy it.

Total storage for the complete offline base is small (about 15 MB total, measured 2026-10-21: about
1.2 MB of text plus about 13.6 MB of look-alike photos; check the size before relying on it).

---

## Scope and what is still open

**Pass 2 (2026-10)** rewrote the 11 survey guides, grew the universal substrate from 37 to 67 entries,
grew Mid-Atlantic / Appalachian from 23 to 34 entries (re-checking all 23 earlier ones), and added the
Northeast / New England pack (15 entries). Every claim was checked by AI agents against sources they
opened, in at least two rounds. See [`CHANGELOG.md`](CHANGELOG.md) for the full list.

**Still open:** the human safety read, for every domain. Also later: more entries per domain, more
local deadly-look-alike photos, and more region packs. Corrections and expert reads are welcome (see
[`CONTRIBUTING.md`](CONTRIBUTING.md)).

---

**Curated by** Victor Sowers · **License** CC0 (public domain dedication) · Pull requests welcome.
