# Accuracy Audit — Pass 2, Survey Wave 2b (Navigation, Communication, Key Resources, Gear) — 2026-10-21

The guides `07_navigation.md`, `08_communication.md`, `10_key_resources.md` and `11_essential_gear.md`
were rewritten as standalone reads with numbered sources. This log is the public verification trail,
in the same format as the wave-1 and wave-2a audits.

> **What this is and is not.** Every check was done by AI agents that opened the primary sources
> themselves: the Army's TC 3-25.26 (land navigation) and ATP 3-50.21, USGS, NOAA (declination and
> SARSAT), NPS, USFS, NWS, the federal radio rules in 47 CFR Parts 95 and 97 (eCFR), FCC pages and
> enforcement advisories, the Coast Guard Navigation Center, FAA CAMI, Ready.gov/FEMA, CDC, CPSC, FDA,
> USFA, DHS and ACS Stop the Bleed, Red Cross, AHA, America's Poison Centers, Hesperian, the Library of
> Congress, and others. It is **not** a human expert's read. The human safety read
> (`CONVENTIONS.md` §10) is still open for every guide and entry touched here.

## Method

Same chain as earlier waves: per-guide brief and draft (21–49 opened sources each), an independent
round-1 fact-check (64–119 claim rows per guide), remediation of guides and the substrate entries that
were the wrong side, round 2, `/review-content` and a component-mode `/edit-content` pass, a re-score,
and final rounds 3–4 that re-checked every round-2 fix and every fact-bearing wording change.

## Results

| Guide | Old claims wrong or misleading | Round 1 (crit / major / minor) | Readability before → after |
|-------|------|------|------|
| Navigation | 13 (+ ~11 unsourced numbers cut) | 0 / 2 / 12 | 88 → 90 |
| Communication | 24 | 0 / 0 / 10 | 84 → 92 |
| Key resources | 9 (+ ~14 unsourced items cut) | 0 / 0 / 10 | 84 → 90 |
| Gear | 13 | 0 / 1 / 11 | 86 → 91 |

**Final rounds:** 0 CRITICAL and 0 MAJOR open in all four guides. Remaining MINOR items are listed at the end.

## What the old guides got wrong (selected)

- **Navigation:** "follow water downstream to civilization" (USFS calls it a very last resort that
  could be very dangerous); "move if no one knows you're missing"; compass use with no declination;
  overconfident accuracy figures for the sun and watch methods.
- **Communication:** recommended a cheap imported dual-band handheld the FCC says may not be used
  unless authorized (DA 18-980); code words on open radio; wrong GMRS fee and channel count;
  ground-to-air letter meanings that conflict with the FAA list.
- **Key resources:** a dead CDC CPR link, outdated course formats, and resources described as more
  than they are.
- **Gear:** candles in the home stockpile; annual water rotation (Ready.gov: every 6 months); no
  tourniquet; no carbon monoxide rules on generator, stove and grill items.

## Substrate entries and reference files corrected as a result

| File | Finding | Severity |
|------|---------|----------|
| `substrate/10_key_resources/entries/skills-to-practice-now.md` | A "drill" told readers to drink iodine- or chlorine-treated stream water and call the method validated if they felt fine after 24 hours. Giardia and Cryptosporidium can take a week or more to cause illness, and chlorine and iodine do not reliably kill Crypto. Also "fracture someone's arm (for practice)". | CRITICAL — FIXED |
| `substrate/10_key_resources/entries/public-domain-id-image-sources.md`, `_media/SOURCES.md` | A printable morel / false-morel card gave the false morel "gills"; photo labels called a morel and a wild onion "Edible", and treated the onion smell as an ID test. | CRITICAL — FIXED |
| `substrate/07_navigation/entries/*` (3) | Handrails "perpendicular" to travel; "follow drainages downhill"; afternoon shadows pointing north; the sun "always south"; Polaris rising and setting; "trust the sun over the compass"; declination stated only as an easy-to-reverse bezel rotation. | MAJOR — FIXED |
| `substrate/08_communication/entries/*` (3) | An invented "unlicensed emergency exception" for amateur and GMRS radio; CB "unlicensed only in emergencies"; wrong FRS/GMRS channel counts, fee and power; "whistle sparingly"; green vegetation making dark smoke; an invented "notify authorities after 48 hours" rule. | MAJOR — FIXED |
| `substrate/11_gear/entries/*` (3) | "Tourniquet or flat headwrap" and paracord as a tourniquet; candles for light and heat; two conflicting bleach doses and bleach for wounds; a propane heater "outdoor or vented"; antibiotics and "avoiding the ER"; brands and prices. | MAJOR — FIXED |
| `substrate/10_key_resources/entries/physical-book-backup-layer.md`, README, CONVENTIONS, `_media/SOURCES.md`, redirect stubs | The 1978 Peterson field guide called public domain with a free PDF (it is copyrighted and borrow-only); *Where There Is No Doctor* attributed to WHO (it is Hesperian's, copyrighted, with stated use terms). | MAJOR — FIXED |

## Settled in this wave

- **Declination:** west — add going map to compass, subtract going compass to map; east — the reverse
  (TC 3-25.26 Table 6-1, USGS). Every worked example re-checked. Set the dial to the corrected bearing.
- **Poison control:** call 1-800-222-1222 (America's Poison Centers). The National Capital Poison
  Center (poison.org) closed its call center on March 31, 2025; its first-aid pages remain and are cited
  only for first aid, such as "do not induce vomiting".
- **Radio:** FRS and CB need no license; GMRS needs an individual license (immediate family may use it);
  amateur needs a license and exam, and 47 CFR 97.403 does not license unlicensed people.
- **Personal locator beacons:** activate only in grave and imminent danger (NOAA SARSAT).
- **Copyright:** US public domain covers works published before 1931 (as of 2026); this repo copies in
  only CC0 or public-domain material.

## Remaining MINOR items (non-safety, deferred)

- Army survival figures in the communication guide were checked against the 2006 FM 21-76 reprint,
  not the 2018 ATP 3-50.21 (the official copy could not be opened in that pass).
- The GMRS "no exam" statement rests on the rule text and FCC GMRS page naming no exam.
- Several rewritten entries still carry the pass-1 `review_status`; a later pass-2 phase relabels them.
  No entry was set to `reviewed` by an agent.
