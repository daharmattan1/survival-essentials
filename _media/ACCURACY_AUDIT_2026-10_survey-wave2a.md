# Accuracy Audit — Pass 2, Survey Wave 2a (Core Principles, Shelter, Food, First Aid) — 2026-10-21

The guides `01_core_principles.md`, `04_shelter.md`, `05_food.md` and `06_first_aid.md` were rewritten
as standalone reads with numbered sources. This log is the public verification trail, in the same
format as [`ACCURACY_AUDIT_2026-10_survey-wave1.md`](ACCURACY_AUDIT_2026-10_survey-wave1.md).

> **What this is and is not.** Every check was done by AI agents that opened the primary sources
> themselves (CDC, FDA, NIH MedlinePlus, NIA, NIMH, USDA/FoodSafety.gov, Ready.gov/FEMA, NWS, NPS,
> USFS, FAA CAMI, Red Cross, AHA, DHS/ACS Stop the Bleed, WHO, the Wilderness Medical Society guideline,
> Army ATP 3-50.21 and FM 21-76, state extension services, Virginia DWR regulations, Alberta Health,
> Poison Control). It is **not** a human expert's read. The human safety read (`CONVENTIONS.md` §10)
> is still open for every guide and entry touched here.

---

## Method

Each guide went through the same chain as wave 1, run one guide at a time so drafting and checking
overlapped:

1. **Brief + draft** — one agent per guide opened 18–44 sources, gave every old claim a verdict, then
   rewrote the guide to an 8-item standalone-read rubric.
2. **Round 1** — a fresh verifier per guide checked every safety-critical claim (82–108 rows per guide)
   and the matching substrate entries.
3. **Remediation** — guide fixes, plus correction of every substrate entry that was the wrong side.
4. **Round 2** — fresh verifiers re-checked every changed line in guides and entries.
5. **Readability** — `/review-content`, then a component-mode `/edit-content` pass, then a re-score.
6. **Rounds 3–5** — targeted verifiers confirmed each round-2 fix, re-checked every fact-bearing
   wording change from the readability edit, and re-checked the last fixes.

## Results

| Guide | Old claims wrong or misleading | Round 1 (crit / major / minor) | Readability before → after |
|-------|------|------|------|
| Core principles | 24 | 0 / 0 / 8 | 83 → 92 |
| Shelter | 12 | 0 / 5 / 9 | 84 → 92 |
| Food | 13 (+ ~30 unsourced claims cut) | 0 / 2 / 12 | 86 → 92 |
| First aid | 24 | 0 / 5 / 16 | 78 → 88 |

**Final rounds:** rounds 3–5 returned SHIP with 0 CRITICAL and 0 MAJOR open. Remaining MINOR items are
listed at the end.

---

## What the old guides got wrong (selected)

- **Food:** a "Safe Wild Edibles" section, a berry-colour rule ("red, black and blue usually safe"), a
  Universal Edibility Test that ended "likely safe", and "induce vomiting" after poisoning. The guide
  now never calls a wild plant, mushroom or animal edible, routes every "what can I eat here" question
  to the regional food hub, and says to call Poison Control (1-800-222-1222) and not induce vomiting.
- **First aid:** tourniquet only after 10–15 minutes of pressure and never below the elbow or knee;
  "ABC" airway-first with no massive-bleeding step; natural remedies. Now: tourniquet promptly for
  life-threatening limb bleeding, 2–3 inches above the wound, note the time, do not loosen, second
  tourniquet if needed; massive bleeding first (Army order).
- **Shelter:** a candle shelf in a snow cave and a camp stove inside shelters. Now: nothing burns inside
  any tent, vehicle or snow shelter, and a vent is not a fix (CDC MMWR 1999 tent deaths).
- **Core principles:** invented statistics (10-80-10, "stay put 80% of the time", 50/50 technical vs
  psychological), "moss grows on the north side", and "ration water".

## Substrate entries corrected as a result

| Entry | Finding | Severity |
|-------|---------|----------|
| `substrate/01_core_principles/entries/rule-of-threes.md` | "Seek elevation" for severe altitude illness and smoke. Descend for altitude (CDC Yellow Book); get low and out for smoke. Also falsely said FM 21-76 states the rule of threes. | CRITICAL — FIXED |
| `substrate/05_food/entries/fish-and-game-processing-basics.md` | Cold-smoking below 90 F, 7–10 day salt cures "lasting months", unheated hanging jerky: untested methods in the botulism and Salmonella range. Fish at 140 F. Implied human CWD cases. | CRITICAL — FIXED |
| `substrate/06_first_aid/entries/bleeding-control-and-shock.md` | Tourniquet only after 15 minutes of pressure; forearm and lower-leg ban; sips of water in shock. | MAJOR — FIXED |
| `substrate/06_first_aid/entries/thermal-injury-hypo-hyperthermia.md` | Warm-bath and hot-bottle rewarming keyed to core temperature; mild hypothermia "field-manageable" with no call-911 trigger; sips for confused heat-stroke patients. | MAJOR — FIXED |
| `substrate/06_first_aid/entries/wound-infection-management.md` | Leave wounds open or packed "because anaerobes"; field abscess drainage; peroxide and iodine steps; no tetanus rules. | MAJOR — FIXED |
| `substrate/04_shelter/entries/*` (3) | Under-sized debris hut and snow cave; "hidden is better" (be findable instead); water called "safe"; vehicle advice without tailpipe or CO rules; unsourced distances and temperatures. | MAJOR — FIXED |
| `substrate/05_food/entries/small-game-trapping-snares.md`, `passive-fishing-trotline-and-traps.md` | Deadfalls taught though Virginia bans them; a claimed survival legal exemption no source supports; gill nets; a fabricated "Survival Fishing Handbook" citation. | MAJOR — FIXED |
| `regional/mid-atlantic-appalachian/game-animals/entries/*` (5) | Venison at 145 F "USDA standard" (USDA chart: 160 F); raccoon Trichinella figure misattributed to CDC; rabbit liver and turkey organs "can be eaten"; sun-dried jerky "shelf-stable for months"; turkey hung 1–2 weeks; no rabies note for raccoons; homepage-only sources. | MAJOR — FIXED |

## Repo-wide rules settled in this wave

- **Rabbit and hare: 165 F** (USDA chart 160 F; Missouri Dept of Conservation 165 F; this guide meets
  both). **Venison, all cuts: 160 F** (USDA chart). Fish 145 F; ground meat 160 F; poultry and game
  birds 165 F; Trichinella-prone wild game 160 F (CDC 2004).
- **Heat stroke:** a body temperature above 103 F (Ready.gov, NWS; MedlinePlus uses 104 F), or any of
  the listed signs; call 911; nothing by mouth.
- **Warming a cold person:** out of wind and rain; wet clothes off only somewhere warm and sheltered;
  body heat and dry blankets first, wrapped heat packs on the chest, armpits and back; a warm sweet drink
  only if alert, shivering and able to swallow; sleepiness or confusion means call 911.
- **Frostbite rewarming:** about 99 to 104 F for 15 to 30 minutes, tested by hand, only if the part
  cannot refreeze (Red Cross; MedlinePlus gives 104 to 108 F).
- **`legal_status`:** `emergency-exception` only where a specific statutory exception is cited. No
  general survival exemption for hunting, trapping or fishing was found.
- **No prescription-drug dosing anywhere** (carried from wave 1).

## Remaining MINOR items (non-safety, deferred)

- `06_first_aid.md` runs about 4,800 words before its sources, over the 4,500 target; cutting further
  would remove verified safety content.
- Fan guidance in heat is worded differently in `04_shelter.md`, `06_first_aid.md` and
  `09_urban_survival.md` (NWS heat-index wording vs CDC air-temperature wording); both are sourced.
- Jerky storage: the food guide gives 1–2 months, the game entries 1–3 weeks (the shorter is kept in
  the entries).
- Squirrel and turkey storage times, and a squirrel-specific organ screen, rest on general sources.
- Several rewritten entries still carry the pass-1 `review_status`; a later pass-2 phase relabels them.
  No entry was set to `reviewed` by an agent.
