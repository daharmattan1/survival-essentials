# CHANGELOG.md — Review Log & Sync Checklist

> This file tracks (a) what changed and when, (b) the **survey↔substrate sync checklist** that keeps
> Layer 1 and Layers 2–3 from drifting apart, and (c) the **Phase-11 human safety-read sign-off**
> that is the life-safety backstop for this repo. This is life-safety content — review discipline is
> not optional.

---

## `last_reviewed` policy

- Every Layer-3 entry carries `last_reviewed:` (ISO date) and `review_status:` in its front-matter.
- `review_status: draft` until a **human** completes the Phase-11 per-domain safety read
  (`CONVENTIONS.md` §10) and flips it to `reviewed`. An AI never sets `reviewed`.
- `last_reviewed: draft` is the placeholder value until that read happens.
- Re-review cadence: any entry whose claims touch `hazard_severity: high|lethal` is re-read whenever
  its sources are updated, and at minimum on the annual repo review.
- Triangulation: each mushroom/plant species **and each of its deadly look-alikes** is verified
  against **≥2** T1/T2 references during the safety read before `reviewed` is set.

---

## Survey ↔ Substrate sync checklist

The eleven numbered survey files (Layer 1) and the substrate/region indexes + entries (Layers 2–3)
describe the same knowledge at different resolutions. When **either side** changes, run the
relevant checks so they do not drift:

**When a survey file (`NN_*.md`) changes:**
- [ ] Does its `## Deep substrate ↓` footer still point at the correct `substrate/NN_*/_index.md`
      (and, for `05_food.md`, also at `regional/_index.md` → `food_hub.md`)?
- [ ] Did a fact change that a Layer-3 entry also asserts (a cook temp, a boil time, a frost date, a
      look-alike)? If so, update the entry **and** re-check its sources.
- [ ] Did the survey add/remove a topic that should add/remove a planned manifest row?

**When a substrate/region index or entry changes:**
- [ ] Does every manifest row still map to an existing entry file, and every entry file still have a
      row? (run `check_manifests` in that `_index.md`)
- [ ] Is the parent index's planned-entry count + one-line synthesis still accurate
      (`substrate/_index.md` master manifest, and the biome `_index.md`)?
- [ ] If a fact diverges from the survey's prose, reconcile — the entry is the higher-resolution
      source, but the survey must not contradict it.

**When a region pack changes:**
- [ ] `regional/_index.md` registry still lists the biome and links it correctly.
- [ ] `food_hub.md` still routes through the deadly-look-alike matrix + `hazards/` before edibles.
- [ ] `seasonality.md` still flags itself as an orienting overview, not an ID source.

**Coherence (run before any PR):**
- [ ] `grep -rn "danger_class" .` returns nothing (banned facet).
- [ ] No `safe` token used on a biology facet.
- [ ] No broken intra-repo links; food resolves via `regional/_index.md` → `food_hub.md`.

---

## Phase-11 human safety-read sign-off

> **HARD GATE.** No entries ship (no PR to a release) until a human completes the per-domain safety
> read in `CONVENTIONS.md` §10 and records the sign-off below. The `APPROVED-CONTRACT` marker on
> `CONVENTIONS.md` covers the *contract*; this sign-off covers the *entries*.

```
SAFETY-READ-PASSED: 2026-06-27
  reviewer:        multi-agent web-sourced verification (NOT a personal domain read by the owner)
  method:          3 independent verification rounds — adversarial fact-check agents triangulating
                   every safety-critical claim against authoritative sources (CDC, EPA, USDA FSIS,
                   WHO, Red Cross / Stop the Bleed, NAMA / mycological societies, university
                   extension, poison control), PLUS the offline read-test (a fresh no-context AI
                   answered the canonical oak/October mushroom query, led with the safety gate, and
                   refused field-ID-only consumption for every field_id_not_appropriate species).
  domains read:    mushrooms, edible-plants, game-animals, first-aid, water (+ crops, hazards, all
                   universal-technique domains structurally)
  triangulation:   Y — each mushroom/plant species + its deadly look-alike checked vs ≥2 authoritative
                   refs. All CRITICAL + MAJOR findings across rounds were corrected and re-verified
                   (full sourced trail: _media/ACCURACY_AUDIT_2026-06-27.md). Round 2 caught and fixed
                   an introduced chanterelle spore-print critical; round 3 re-check returned SHIP.
  notes:           This sign-off reflects AGENTIC verification, not the repo owner's personal
                   mycological/medical read. Owner chose agentic verification as sufficient for
                   pass-1 (he does not hold the domain expertise to hand-verify). Remaining items are
                   MINOR/non-safety (logged in the audit). Still NOT medical, legal, or professional
                   foraging advice — positive ID or do not consume.
```

_Pass-1 entries flipped to `review_status: reviewed` on this basis. A future owner/expert hand-read
remains welcome and would supersede this agentic sign-off._

---

## Change log

### 2026-06-27 — Phases 3–8: entries + deadly-pair photos

- **Phases 3–7:** Wrote **60 structured entries** (Haiku agents, ≤5 per wave, schema-strict), all
  `review_status: draft` pending the Phase-11 human safety read:
  - **Phase 3 — what-kills-you-fast core:** `02_water` ×5 (each with the `⚠ CONTAMINATION` block),
    `06_first_aid` ×5 (each with RED FLAGS / EVAC + DO NOT + a not-medical-advice disclaimer).
  - **Phase 4 — safety-critical biology:** `edible-plants` ×5 + `mushrooms` ×5; every entry leads
    with the `⚠ POSITIVE-ID SAFETY GATE`; deadly-look-alike species flagged
    `field_id_not_appropriate: true`; discriminators pulled verbatim from the index matrices.
  - **Phase 5 — region biology II:** `game-animals` ×5 (white-tailed **deer** full
    field-dress→skin→butcher→preserve flow + CWD/prion; rabbit/tularemia; raccoon/trichinella),
    `crops` ×5 (7a windows + seed saving), `hazards` ×3 (hemlock cross-linked to the edible-plants
    deadly-twin matrix).
  - **Phase 6 — universal technique I:** `01_core_principles` ×3, `03_fire` ×3, `04_shelter` ×3.
  - **Phase 7 — universal technique II:** `05_food`-technique ×3, `07_navigation` ×3,
    `08_communication` ×3, `09_urban_survival` ×3 (incl. sanitation/human-waste disease-vector +
    power-outage CO danger), `11_gear` ×3, `10_key_resources` ×3.
  - All manifests updated `planned → present`. Repo-wide invariants verified after each phase: 0
    `danger_class`, 0 banned `safe` token on biology facets.
  - **Note (open for safety-read):** the per-domain counts sum to **60**; the success-criterion
    headline says "≥63." Every domain meets its individual target — the 60-vs-63 reconciliation is
    deferred to Victor at the Phase-11 gate.
- **Phase 8 — deadly-pair reference photos:** pulled **5 verified CC0** images into `_media/photos/`
  covering 3 highest-stakes pairs (morel/false-morel, wild-onion/death-camas, destroying-angel),
  logged with full attribution in `_media/SOURCES.md`, and linked from the morel, puffball, and
  wild-onion entries as **supporting evidence, never sufficient for ID**.
- **Phase 9 — technique diagrams: SKIPPED** (optional/non-blocking per the plan). The substrate is
  text-complete; generated technique line-art adds marginal value for pass-1 and can be a later
  pass. No AI-generated biology ID imagery was produced (hard rule).

### 2026-06-27 — Phase 0 / Phase 2: contract + scaffolding (no entries)

- **Phase 0 (prior):** Authored the structural contract — `SCHEMAS.md` (entry facets + body
  skeletons), `CONVENTIONS.md` (controlled vocab, standardized WARNING blocks, mushroom doctrine,
  water CONTAMINATION block, source tiers, answer policy, per-domain safety-read checklists),
  reframed `README.md`, `LICENSE` (CC0). Codex review deliberately skipped per Victor; the Phase-11
  human safety read remains the backstop (see `APPROVED-CONTRACT` marker in `CONVENTIONS.md`).
- **Phase 2 (this pass):** Built the **full empty pyramid + coherence spine** — no entries yet.
  - Added repo docs: `AGENTS.md` (layer model, danger facets, retrieval recipes, load order, answer
    policy) and this `CHANGELOG.md`.
  - Built `substrate/` tree: master `substrate/_index.md` + 11 domain folders, each with an
    `_index.md` (synthesis + load order + manifest table of planned entries) and an empty `entries/`
    dir (`.gitkeep`).
  - Built the `regional/` region pack: `regional/_index.md` registry + the
    `mid-atlantic-appalachian/` biome (`_index.md` profile, `food_hub.md` decision surface,
    `seasonality.md` calendar) + 5 biology subfolders (`edible-plants/`, `mushrooms/`,
    `game-animals/`, `crops/`, `hazards/`), each with an `_index.md` and empty `entries/`. The
    `mushrooms/` and `edible-plants/` indexes lead with the doctrine/deadly-look-alike matrix.
  - Wired Layer 1 → substrate: added a `## Deep substrate ↓` footer to all 11 numbered survey files.
  - Converted `PLANT_IMAGE_RESOURCES.md` and `MEAT_FISH_PROCESSING_RESOURCES.md` to redirect stubs;
    moved their source catalogs into `_media/SOURCES.md`. Built `_media/` tree (`SOURCES.md`,
    `photos/.gitkeep`, `diagrams/.gitkeep`).
  - **Zero entry files written** — every `entries/` directory is empty (`.gitkeep` only). Manifest
    tables list PLANNED rows (`review_status: planned`, `source_count: 0`) for later phases.

### (earlier) — original survey

- The eleven numbered survey files + `10_key_resources.md`, `PLANT_IMAGE_RESOURCES.md`,
  `MEAT_FISH_PROCESSING_RESOURCES.md` predate the substrate. The survey bodies are Layer 1 and are
  left unchanged except for the added `## Deep substrate ↓` footers.
