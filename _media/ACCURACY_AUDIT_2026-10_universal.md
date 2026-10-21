# Accuracy Audit — Pass 2, Universal Substrate Deepening (37 → 67 entries) — 2026-10-21

Thirty new universal entries were written in pass 2, and the 12 substrate index files were checked line
by line for the first time. This log is the public verification trail, in the same format as the survey
audits ([wave 1](ACCURACY_AUDIT_2026-10_survey-wave1.md), [wave 2a](ACCURACY_AUDIT_2026-10_survey-wave2a.md),
[wave 2b](ACCURACY_AUDIT_2026-10_survey-wave2b.md)).

> **What this is and is not.** Every check was done by AI agents that opened the primary sources
> themselves (CDC and its MMWR reports, FDA, NIH MedlinePlus, USDA FSIS and the National Center for Home
> Food Preservation, EPA, CPSC, Ready.gov/FEMA, NWS/NOAA, NPS, USFS, the eCFR radio rules, the Army's
> ATP 3-50.21 and TC 3-25.26, Red Cross, AAAAI, NIAID, state extension services and others). It is **not**
> a human expert's read. Every new entry is `review_status: draft`. The human safety read
> (`CONVENTIONS.md` §10) is still open for all of them.

## Method

1. **Plan.** 30 new manifest rows, chosen to fill gaps the rewritten survey guides exposed.
2. **Write.** Nine agents wrote the entries to one shared spec. Every number had to agree with the matching
   rewritten survey guide, and every cited page had to be one the agent opened.
3. **Round 1.** Six independent fact-checkers (none had written an entry) checked every claim, opened every
   cited URL, and compared each entry with its guide: 20 to 47 claim rows per entry.
4. **Fix.** Entries were corrected. Where the guide was the wrong side, the guide was corrected too.
5. **Index audit.** A separate agent read every prose and decision-tree line in the 12 index files against
   the guides and entries; all findings were applied.
6. **Round 2.** Three fresh verifiers re-checked every fix, every new citation, and every guide and index edit.
7. **Round 3.** One more verifier checked every fact-bearing change made after round 2.

## Results

| Group | Entries | Round 1 (critical / major / minor) | Round 2 verdict |
|-------|--------:|------|------|
| Water + first aid (allergy, CO) | 5 | 1 / 4 / 15 | SHIP after fixes |
| First aid (burns, fractures, head) + core | 5 | 0 / 4 / 25 | SHIP |
| Urban | 4 | 2 / 4 / 26 | SHIP after fixes |
| Fire + shelter | 6 | 0 / 3 / 25 | SHIP |
| Food + navigation + key resources | 6 | 2 / 2 / 30 | SHIP |
| Communication + gear | 4 | 0 / 1 / 21 | SHIP |
| **Total** | **30** | **5 / 18 / 142** | **round 2 found 0 / 2 / 14; all fixed** |
| Guide and index edits made in this block | — | — | 1 / 1 / 10; all fixed |

Index files: 30 contradictions, 34 stale lines, 9 unsupported claims and 5 banned phrases, all fixed.

## The five critical findings (all fixed before commit)

- **Anaphylaxis:** a line told bystanders not to use an epinephrine auto-injector on someone without a
  prescription. No source said so, and CDC, NIAID and the Red Cross point the other way. Now: call 911,
  ask whether an auto-injector is available, and follow the dispatcher.
- **Generators and heaters:** fuel-burning portable heaters were allowed indoors under conditions ("check
  that a kerosene heater is legal"). Now: no unvented fuel-burning heater inside a home, tent, camper or
  vehicle. The same wording was in `09_urban_survival.md` and was fixed there.
- **Food in outages:** a warmed life-sustaining medicine "may be used only until a new supply is
  available" (CDC wording). That is holding a prescription drug, which this repo never advises. Now: do
  not decide alone; call a pharmacist or the prescriber, and 911 if neither can be reached. Fixed in the
  guide too.
- **Calorie planning (two):** quoted source wording described rationed food and formula as "safe". This
  repo never uses the word for eating or drinking; both lines were rewritten.

## Corrections to the survey guides found by this block

- **Wild game and Trichinella: 160 F → 165 F.** The repo followed CDC's 2004 MMWR (160 F). CDC's October
  2024 MMWR says cooking wild game meat to at least 165 F is necessary to kill *Trichinella*, and that
  freezing might not be enough. Bear, wild pig and other wild meat-eaters or omnivores now read 165 F in any
  form in `05_food.md`, the food entries and the game-animal entries. Venison stays 160 F (USDA chart).
- **Floodwater and stored water** (`02_water.md`): "if stored water touched floodwater, treat it again" was
  unsupported. Now: throw out water in screw-cap, snap-lid or pull-top containers that may have touched
  floodwater (FDA); treatment does not remove fuel or toxic chemicals.
- **Heaters and medicine** (`09_urban_survival.md`): as above. Also re-cited: closing off rooms in a cold
  house (NWS), the pharmacist line (FDA), and the gas-range line (a range is for cooking only, never heat).
- **Water index and two urban entries** still gave the older CDC boil altitude alone; all now use 3 minutes
  above 5,000 ft or if unsure.
- **Smaller fixes:** reflector wall built before the fire is hot (ATP 3-50.21); tarp pitch range limited to
  porous cloth (ATP 3-50.21); shelter guide's hypothermia 911 wording matched to the first-aid guide; a
  fire-restriction order marked as a dated example; smoke-inhalation signs re-cited; radio and kit
  citations corrected.

## Settled in this block

- **Wild game:** bear, wild pig and other wild meat-eaters or omnivores 165 F; venison 160 F; rabbit and hare
  165 F; poultry and game birds 165 F; fish 145 F.
- **Carbon monoxide:** nothing burns inside a tent, vehicle, garage, snow shelter or home except a vented
  fireplace or stove in working order. A gas range is for cooking only, never for heat. A cracked window
  lowers the risk in a running car but does not remove it; a clear tailpipe comes first.
- **Prescribed epinephrine:** use it as its label and prescriber direct; no dose numbers anywhere.
- **Index files are checked like guides.** Their synthesis lines and decision trees now route to the new
  entries and agree with the guides.

## Remaining MINOR items (non-safety, deferred)

- Round 2 found one more critical line: the warmed-medicine wording survived in two older entries
  (`power-outage-bug-in`, `chronic-med-continuity`) and the food-safety entry told readers to throw out all
  refrigerated medicine. All three now match the guide: life-sustaining medicine goes to a pharmacist or
  prescriber first, then 911.
- `01_core_principles.md` car lines now put the clear tailpipe first; a cracked window lowers the risk only.
- **Flagged for the human safety read: warmed insulin.** Round 3 asked to drop FDA's note that warmed
  insulin may still be needed in an emergency. It was kept, worded as "do not throw it out and do not decide
  alone: call a pharmacist or the prescriber, then 911", because discarding a person's only insulin can kill.
  This is a judgment call for the human reviewer (`chronic-med-continuity`, `09_urban_survival.md`).
- **Old `reviewed` stamps.** Four pass-1 entries rewritten in pass 2 (`chronic-med-continuity`,
  `power-outage-bug-in`, `fish-and-game-processing-basics`, `sanitation-and-human-waste`) still carry their
  pass-1 `reviewed` label. A later pass-2 phase relabels every changed entry.
- A few claims rest on pages that block automated reading and are marked as such in the work files: NIA's
  68 to 70 F indoor figure, the Red Cross frozen-pipes page, and some FSIS and foodsafety.gov chart text.
- Several pages block automated reading (some CDC, FSIS, NIA, FCC and Red Cross pages). Where an entry
  relies on one, the claim was confirmed through an agency mirror or search text, or labelled.
- No entry was set to `reviewed` by an agent.
