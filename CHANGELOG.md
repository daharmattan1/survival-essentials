# CHANGELOG.md — Review Log & Sync Checklist

> This file tracks (a) what changed and when, (b) the **survey↔substrate sync checklist** that keeps
> Layer 1 and Layers 2–3 from drifting apart, and (c) the **human safety-read sign-off** that is the
> life-safety backstop for this repo. This is life-safety content — review discipline is not
> optional. **As of 2026-10, no human safety read has been recorded.**

---

## `review_status` and `last_reviewed` policy

- Every Layer-3 entry carries `review_status:` in its front-matter. Three values (`SCHEMAS.md` §0):
  - `draft`: written, not yet independently checked.
  - `agent-verified`: AI agents that did not write the entry checked every claim against sources they
    opened, in at least two rounds. `last_reviewed` stays `draft`. This is **not** a human read.
  - `reviewed`: a **human** completed the per-domain safety read (`CONVENTIONS.md` §10) and ran
    `scripts/mark_reviewed.py` themselves. An AI never sets `reviewed` and never runs that script.
- `last_reviewed: draft` is the placeholder value until a human read happens.
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

## Human safety read — sign-off

> **HARD GATE.** No entry is `reviewed` until a human completes the per-domain safety read in
> `CONVENTIONS.md` §10 (how-to: [`review/SAFETY_READ_PACKET.md`](review/SAFETY_READ_PACKET.md)) and a
> maintainer records the sign-off below. The `APPROVED-CONTRACT` marker on `CONVENTIONS.md` covers
> the *contract*; this table covers the *entries*.

**No human safety read has been done. The table is empty on purpose.**

| Domain | Reviewer | Date | Result |
|--------|----------|------|--------|
|        |          |      |        |

_The pass-1 note that appeared here (a 2026-06-27 "SAFETY-READ-PASSED" by multi-agent verification,
with the entries flipped to `reviewed`) was withdrawn in pass 2. It was AI-only, and pass 2 found
serious errors in entries it had passed. It was never a human sign-off._

---

## Change log

### Pass 2 (2026-10)

A rewrite and expansion, with every claim re-checked by AI agents that opened the sources. **No human
has read any of it.** The human safety read is still open for every domain.

- **Survey rewrite (11 guides).** All eleven numbered guides were rewritten as standalone reads, each
  with a numbered `## Sources` list. Audits:
  [wave 1: water, fire, urban](_media/ACCURACY_AUDIT_2026-10_survey-wave1.md) ·
  [wave 2a: core principles, shelter, food, first aid](_media/ACCURACY_AUDIT_2026-10_survey-wave2a.md) ·
  [wave 2b: navigation, communication, key resources, gear](_media/ACCURACY_AUDIT_2026-10_survey-wave2b.md).
- **Universal substrate: 37 to 67 entries.** Thirty new entries, plus a line-by-line check of the 12
  index files. Audit: [universal](_media/ACCURACY_AUDIT_2026-10_universal.md).
- **Mid-Atlantic / Appalachian: 23 to 34 entries.** Eleven new entries. All 23 pass-1 entries were
  re-checked line by line, and **23 critical errors were found and fixed**. Audit:
  [Mid-Atlantic biology](_media/ACCURACY_AUDIT_2026-10_biology.md).
- **Northeast / New England pack: 15 entries.** A second region (`regional/northeast-new-england/`)
  with its own food hub, seasonality page, mushroom doctrine and hazards. Total is now 116 entries.
- **Review status changed.** `review_status` is now `draft | agent-verified | reviewed`
  (`SCHEMAS.md` §0). Every pass-1 `reviewed` label was replaced with `agent-verified`, because those
  labels came from AI-only checks. `reviewed` now means a human did the read.
- **Repo-wide rule changes.** Wild game is cooked to 165 F (CDC MMWR 2024). The mushroom doctrine now
  requires an expert who has examined the specimen in hand; matching several sources is an addition,
  never a substitute (`CONVENTIONS.md` §4).
- **Human-read tooling.** Added [`review/SAFETY_READ_PACKET.md`](review/SAFETY_READ_PACKET.md) with
  per-domain checklists in `review/`, and `scripts/mark_reviewed.py`. The script is human-only: it
  needs an interactive terminal and a typed confirmation, and AI agents must never run it.
- **Contribution paths.** Added [`CONTRIBUTING.md`](CONTRIBUTING.md) and two issue templates
  (`.github/ISSUE_TEMPLATE/correction.yml`, `expert-review.yml`).
- **License.** Replaced `LICENSE` with the canonical CC0 1.0 Universal text.
- **Audit trail.** Pass 1: [`ACCURACY_AUDIT_2026-06-27.md`](_media/ACCURACY_AUDIT_2026-06-27.md). Pass 2:
  the five audit files linked above.

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
