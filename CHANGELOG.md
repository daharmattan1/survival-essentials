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
SAFETY-READ-PASSED: <pending>
  reviewer:        <name>
  date:            <ISO date>
  domains read:    <mushrooms, edible-plants, game, first-aid, water, …>
  triangulation:   <each species + each deadly look-alike vs ≥2 T1/T2 refs — confirmed Y/N>
  notes:           <any caveats>
```

_This block stays `<pending>` until the human read happens. When it passes, fill it in and flip the
read entries to `review_status: reviewed`._

---

## Change log

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
