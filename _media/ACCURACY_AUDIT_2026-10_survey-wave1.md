# Accuracy Audit — Pass 2, Survey Wave 1 (Water, Fire, Urban) — 2026-10-20

The three survey guides `02_water.md`, `03_fire.md` and `09_urban_survival.md` were rewritten
from scratch as standalone reads, each with a numbered `## Sources` list. This log is the public
verification trail for that rewrite, in the same spirit as
[`ACCURACY_AUDIT_2026-06-27.md`](ACCURACY_AUDIT_2026-06-27.md).

> **What this is and is not.** Every check below was done by AI agents that opened the primary
> sources themselves (CDC, EPA, FDA, USDA FSIS, CPSC, Ready.gov/FEMA, NIA, MedlinePlus, NHS, Red
> Cross, USFS/NPS, WHO, the Wilderness Medical Society 2024 water guideline, Army ATP 3-50.21). It is
> **not** a human expert's read. The human safety read (`CONVENTIONS.md` §10) is still open for
> every guide and entry touched here. Corrections are welcome — see `CHANGELOG.md`.

---

## Method

1. **Brief** — one research agent per guide opened ≥12 Tier-1/Tier-2 sources (water 29, fire 28,
   urban 59) and gave every claim in the old guide a verdict: correct, wrong, misleading, or
   unsourced.
2. **Draft** — a separate agent rewrote the guide from the brief. Every number, dose, duration and
   always/never rule cites a source the brief had opened.
3. **Round 1** — a fresh verifier per guide (never the drafter) extracted every safety-critical
   claim (97–108 rows per guide), checked each against a source it opened itself, and checked that
   each citation says what the guide attributes to it.
4. **Remediation** — all CRITICAL and MAJOR findings fixed in the guides **and** in the substrate
   entries that turned out to be the wrong side.
5. **Round 2** — three fresh verifiers re-checked every changed line in the guides and entries.
6. **Round 3** — one targeted verifier confirmed each round-2 finding was fixed and that no fix
   introduced a new error.
7. **Readability edit** — the guides were restructured for a reader under stress (start-here routers,
   triage-first burns, phone-friendly cards). Every sentence whose wording touched a number or a
   safety rule was logged and re-checked against sources in **round 4**.

## Results by round

| Round | Water | Fire | Urban |
|-------|-------|------|-------|
| Old guide claims judged wrong or misleading (brief) | 20 | 18 | 32 |
| Round 1 (critical / major / minor) | 1 / 4 / 8 | 0 / 6 / 17 | 0 / 8 / 16 |
| Round 2 (critical / major / minor) | 0 / 0 / 11 — SHIP | 0 / 3 / 10 | 0 / 3 / 13 |
| Round 3 (targeted) | SHIP | SHIP | SHIP |
| Readability review before / after edit pass (/100) | 79 → 92 | 82 → 90 | 77 → 90 |
| Round 4 (re-check of every fact-bearing edit) | SHIP | SHIP | SHIP |

**Open after round 3:** 0 CRITICAL, 0 MAJOR. Remaining MINOR items are listed at the end.

---

## Guide corrections (CRITICAL and MAJOR)

| Guide | Finding | Correct fact / fix | Status |
|-------|---------|--------------------|--------|
| Water | **CRITICAL:** methods table said distillation removes "most" chemicals | Pot distillation does not remove fuel, solvents or other volatile chemicals; they boil off with the steam. Fuel- or chemical-contaminated water is not made drinkable at home (CDC). | FIXED |
| Water | Bleach and iodine marked as handling Giardia with no caveat | Giardia needs long contact: about 45–60 min in mild water, about 3 h near 5 °C (WMS 2024, Table 6). Boil or filter cold water if Giardia is possible. | FIXED |
| Water | "Filter, then disinfect" read as permission to treat floodwater | Never treat standing floodwater to drink; follow utility/health notices. | FIXED |
| Water | "Vitamin C or iodine" in stored water listed as a mistake | Only vitamin C (any taste remover) is the mistake; the halogen residual protects stored water (WMS). | FIXED |
| Water | Boil-notice scenario attributed ice, produce and formula advice to a CDC page that lacks it | Re-attributed; two lines marked general practice. | FIXED |
| Fire | Tahoe NF order exemptions misstated | Only on-duty officers/crews and one specific permit are exempt; campfire-permit holders and fuelwood cutters are not; no survival exemption is listed. | FIXED |
| Fire | Overnight-fire "exception" presented as a cited rule | Put the fire out before sleeping (USFS/Smokey). Any night fire is the guide's judgment, attended in shifts, never unattended. | FIXED |
| Fire | Shock position missing its qualifier | Flat with feet up only if no head, neck, back or leg injury (MedlinePlus). | FIXED |
| Fire | "Cool 20 minutes" vs "no cold water for severe burns" unreconciled | Severe burns defined; sources' disagreement stated; cautious middle given; card carries the caveat. | FIXED |
| Fire | Unattended campfires called "a leading cause" | NPS lists them among common human causes, unranked. | FIXED |
| Fire | National cold-death count said to "include indoor deaths" | Not in the source; replaced with the Wisconsin 2014 indoor share. | FIXED |
| Fire (r2) | Pyramid lay built on "big logs" | Small logs or branches, each layer smaller (ATP 3-50.21 ¶5-27). | FIXED |
| Fire (r2) | Card gave an invented "at least 5–10 min" floor and omitted the severe-burn caveat | Card now matches the body. | FIXED |
| Urban | Scenario delayed 911 for a drowsy, shivering older person | Sleepiness itself is a call-911 sign (NIA). | FIXED |
| Urban | emPOWER described as an individual sign-up | It is an HHS planning tool for officials; households ask their supplier, clinician, utility and emergency management. | FIXED |
| Urban | Civil-disruption advice attributed to a FEMA page that does not discuss it | Removed the attribution; one plain "follow local officials" line. | FIXED |
| Urban | "Open windows" for heat | Only when outside air is cooler than inside (EPA). | FIXED |
| Urban | Meat hanging/salt-curing line cited to a source that does not support it | Deleted. | FIXED |
| Urban | Dish-bleach strength differed from the water guide without explanation | 1 tbsp/gal general sanitizing (CDC, FSIS); CDC's boil-notice dish soak is 1 tsp/gal for 1 min. Both guides now say so. | FIXED |
| Urban (r2) | Fridge rule worded differently in body, card and entry | One rule everywhere: ~4 h closed; no thermometer ⇒ discard perishables after that; ≥40 °F for ≥2 h ⇒ discard. | FIXED |
| Urban (r2) | Insulin "throw away if exposed to extreme temperatures" dropped FDA's qualifier | Replace once properly stored insulin is available; in an emergency warm insulin may still be needed; frozen insulin is not used; call a clinician/pharmacist if it is your only supply. | FIXED |
| Urban (r2) | Refrigerated-medicine discard rule mis-cited | Discard rule cited to Ready.gov; CDC's life-dependent-medicine caveat added. | FIXED |

## Substrate entries corrected as a result

The rewrite surfaced errors in the pass-1 substrate. Where the entry was the wrong side, it was
corrected and re-verified in rounds 2 and 3.

| Entry | Finding | Severity |
|-------|---------|----------|
| `substrate/03_fire/entries/fire-lays-and-structure.md` | Said a vent hole made a fire inside a shelter acceptable. Venting does not prevent CO deaths (CDC MMWR 1999; CPSC). | CRITICAL — FIXED |
| `substrate/06_first_aid/entries/chronic-med-continuity.md` | Gave insulin hold/ration thresholds and dose changes for other drugs. All removed; FDA storage facts and clinician routing instead. | CRITICAL — FIXED |
| `substrate/06_first_aid/entries/dehydration-and-diarrhea.md` | Self-start ciprofloxacin dosing, an insulin-dose instruction, and "do not use ORS for cholera-like diarrhea" (WHO: ORS is front-line). | CRITICAL — FIXED |
| `substrate/06_first_aid/entries/wound-infection-management.md` | Self-start antibiotic dosing ("if unsure, use lowest reasonable dose"). Removed; antibiotics are a clinician's decision. | CRITICAL — FIXED |
| `substrate/03_fire/entries/ignition-methods.md` | Ferro-rod technique reversed; wrong friction woods; invented success percentages. | MAJOR — FIXED |
| `substrate/03_fire/entries/tinder-and-fuel-progression.md` | Char cloth described as grease-soaked cloth. | MAJOR — FIXED |
| `substrate/02_water/entries/*` (5) | 8.25% bleach dose credited to the wrong agency; 4 drops/L cloudy dose; 0.5 µm for bacteria (CDC: 0.3 µm); stored water "24–48 h" (CDC: rotate every 6 months); SODIS bottle left open; EPA altitude threshold misattributed; dead or invented URLs. | MAJOR — FIXED |
| `substrate/09_urban_survival/entries/*` (3) | Generator guidance with venting language; outdated death figure; unsourced lime/burial claims; unverifiable security advice; dead URLs. | MAJOR — FIXED |

**Repo-wide rule applied:** this repository gives **no prescription-drug dosing, rationing or
dose-change advice**. Over-the-counter medicines are "label dose only". First aid here is not
medical advice.

---

## Remaining MINOR items (non-safety, deferred)

- Urban guide source list skips numbers 40–41 (sources were removed; renumbering deferred to avoid breaking citations).
- The urban guide states the CDC boil threshold (6,500 ft); the water guide also gives the EPA threshold (5,000 ft). Both say "if unsure, boil 3 minutes."
- Fire guide: the Tahoe NF bullet does not mention that charcoal grills are allowed at listed sites.
- Fire guide: no dedicated first step for electrical burns (cut the power before touching the person) or dry-chemical burns; candidate for the first-aid wave.
- Urban guide: the "unvented heater where people sleep" line cites CPSC/EPA pages that cover unvented heaters generally; a closer citation is a later polish.
- Hypothermia 911 signs: the NIA page is behind a bot wall for automated checks; Ready.gov confirms the sign list and the below-95 F emergency threshold.
- Dehydration entry: the three-tier sign grouping is the guide's own synthesis of MedlinePlus, not labelled as such. Bismuth subsalicylate caution is label-based (the MedlinePlus page was unreachable).
- `review_status` metadata for the changed entries is updated in a later pass-2 phase; no entry was marked human-`reviewed` by an agent.
