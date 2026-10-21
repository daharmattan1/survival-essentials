# Accuracy Audit — Pass 2, Mid-Atlantic / Appalachian Biology (23 → 34 entries) — 2026-10-21

Pass 2 added 11 region-bound biology entries and, for the first time since pass 1, re-checked all 23
existing ones line by line. This log is the public verification trail for that work. Read it before
relying on any earlier "reviewed" label in this region.

> **What this is and is not.** Every check was done by AI agents that opened the sources themselves:
> state extension services (NC State, Penn State, University of Maryland, Virginia Cooperative Extension,
> WVU, Purdue, Cornell, UC ANR, University of Idaho, Oregon State, Washington State, Utah State), USDA
> (PLANTS, NRCS, Forest Service, FSIS), FDA (Bad Bug Book), CDC and MMWR reports, NIH MedlinePlus and
> StatPearls, America's Poison Centers, NAMA, the Missouri Department of Conservation, state wildlife
> agencies (Virginia DWR, Maryland DNR, Pennsylvania Game Commission and Fish and Boat Commission, West
> Virginia DNR, New York DEC), the National Park Service, WHO, and peer-reviewed case reports. It is
> **not** a human expert's read, and it is not a mycologist's or botanist's confirmation. Every entry
> still requires the human safety read (`CONVENTIONS.md` §10) before it can be marked reviewed.

## The headline

**The pass-1 biology entries were not safe to rely on.** They were labelled `reviewed` after AI-only checks,
and this audit found **23 critical errors across the 23 existing entries** — errors that could lead a
reader to eat something that kills them, or to wait when they should get help. Every one is fixed below.
The 11 new entries had no critical errors in round 1.

## Method

1. **Write.** Four agents wrote the 11 new entries to one spec: the positive-identification safety gate
   first, every deadly look-alike named, each species and look-alike checked against at least two
   Tier-1/Tier-2 sources, no dosing, no "safe to eat".
2. **Round 1.** Ten independent fact-checkers (none had written an entry) checked all 34 entries and the
   five domain indexes: 25 to 50 claim rows per entry, every cited link opened.
3. **Rebuild or fix.** Pass-1 entries whose sourcing was fabricated were rebuilt from opened sources;
   the rest were fixed. Food hub, seasonal calendar and regional indexes were brought into line.
4. **Photos.** Real public-domain / CC0 photos only, licence checked through the Wikimedia Commons API.
5. **Round 2.** Four fresh verifiers re-checked every fix and every new citation. A final pass fixed what
   round 2 found.
6. **Round 3.** One more verifier re-checked every change made after round 2.

## Results

| Domain | Entries (old + new) | Round 1, old entries (crit / major / minor) | Round 1, new entries | Round 2 |
|--------|------|------|------|------|
| Mushrooms | 5 + 3 | 9 / 31 / 47 | 0 / 6 / 21 | 0 / 2 / ~14 |
| Edible plants | 5 + 3 | 5 / 30 / 37 | 0 / 3 / 15 | 0 / 2 / 19 |
| Hazards | 3 + 3 | 4 / 28 / 17 | 0 / 4 / 28 (+1 critical in an old index line) | 0 / 0 / 18 |
| Crops | 5 + 2 | 4 / 18 / 33 | 0 / 4 / 18 | 0 / 1 / ~17 (crops and game together) |
| Game animals | 5 + 0 | 1 / 10 / 41 | — | (with crops) |
| **Total** | **23 + 11 = 34** | **23 / 117 / 175** | **0 / 17 / 82** | **0 / 5 / ~68; all fixed** |
| Round 3 (changes after round 2) | | | | **0 / 4 / 8; all fixed** |

Crops count includes two lines that used "safe" about eating. Game counts the missing raccoon-roundworm
warning as critical. One round-2 major (the mushroom doctrine wording) was in the top-level files and is
fixed there.

## What the pass-1 entries got wrong (selected; all fixed)

**Mushrooms**
- Chanterelle: inner flesh given as yellow or orange (it is white; the jack-o'-lantern is orange through).
  The spore print was offered as a way to tell it from the false chanterelle; both print white.
- Oyster: taught a "blunt ridge vs sharp gill" test against the jack-o'-lantern. Both have true gills.
  Angel wings (*Pleurocybella*), linked to deaths in Japan in 2004, got two lines.
- Morel: *Verpa* missing; the eastern false morel (*Gyromitra caroliniana*) passed the entry's own gate;
  "cooking eliminates any residual toxin risk".
- Puffball: the amatoxin timeline sat under the earthball heading, next to a 30-minute onset, where it could
  make a reader wait. Mortality figures were misattributed.
- Chicken-of-the-woods: "safely eaten by thousands"; the facet saying field ID is not appropriate was off.
- The mushroom doctrine let "a definitive multi-source ID" stand in for an expert. It now requires an
  expert who has examined the specimen, with multi-source ID as an extra, never a substitute.
- Several citations did not exist (a "Peterson & McKenny 1987", a "Maines 2000", unfindable NAMA guides).

**Edible plants**
- Wild onion vs death camas: the identification table was **inverted**. It gave death camas a smooth bulb,
  thick waxy leaves and drooping flowers; sources describe an onion-like bulb, grass-like leaves and an
  upright white flower spike. It called the onion smell "absolute"; Idaho records a family poisoned among
  plants that smelled strongly of onion.
- Acorn: said there was no dangerous look-alike. Buckeye and horse chestnut are rated potentially fatal.
- Dandelion: "the milky sap alone makes it unmistakable". Several plants share it; groundsel and arnica,
  which can cause serious poisoning, are confused with it.
- Cattail: male and female flower spikes reversed; no real discriminator from iris.
- Violet and chickweed: the leaf test missed lesser celandine; scarlet pimpernel missing.

**Hazards**
- Snakebite: "get to a hospital within 2-4 hours". CDC: emergency care as soon as possible.
- Toxic plants: both identification-safety facets were false although a deadly look-alike exists; hemlock
  "discriminators" that the water-hemlock evidence does not support; sap burns from wild parsnip and giant
  hogweed blamed on the wrong chemical.
- Ticks: Lyme only. No lone star tick, alpha-gal syndrome, or Powassan virus (which can pass in about 15
  minutes); "save the tick for testing", which CDC does not recommend.
- Citations to an air-quality page, a dead domain, and a protocol that could not be found.

**Crops**
- Winter squash: no warning about bitter squash (cucurbitacin). It must be thrown out; cooking does not
  destroy the toxin.
- Flint corn: lime treatment called "optional"; no mention of pellagra.
- Dry beans: the lectin rule did not match FDA (soak at least 5 hours, discard the water, boil at least
  30 minutes; never a slow cooker for dry kidney beans).
- Potato storage too cold; planting windows wrong.
- Sources included bare homepages and USDA documents that do not exist.

**Game**
- Raccoon: no warning about raccoon roundworm (*Baylisascaris*), which CDC says can cause death or
  permanent disability when larvae reach the brain. Hunters handling carcasses are exposed.
- Turkey season dates wrong; rabbit tularemia framed as a warm-month risk only; animal sizes wrong; the
  protected Delmarva fox squirrel not mentioned.

## Settled in this block

- **Wild game is cooked to 165 F** where Trichinella is a risk (bear, wild pig, raccoon, opossum, squirrel and
  other wild meat-eaters), following CDC's 2024 report; venison 160 F; rabbit and hare 165 F; poultry and game
  birds 165 F.
- **Mushrooms always need an expert.** Matching several sources is an extra requirement, never a substitute.
- **Amatoxin mortality is stated as a sourced range** (under 5% in some developed-country series, about 11.6%
  across 2,000+ cases in western Europe, the US and Canada per NAMA, about 50% without prompt treatment per
  NAMA's syndromes page), never a single number.
- **Photos:** the western death-camas photo was replaced with an eastern species (fly poison, Shenandoah
  National Park). Seven new public-domain or CC0 photos were added. A chanterelle / jack-o'-lantern pair was
  left out: the only CC0 jack-o'-lantern photo had a colour filter, which would mislead.

## Remaining items (non-safety, deferred)

- Round 3 re-checked every change made after round 2 and found no critical errors; its four major findings
  (a trapping season given as the hunting season in the calendar, the ninth doctrine point missing from
  `CONVENTIONS.md`, a misdescribed source on the false chanterelle, and the dandelion facet) are fixed. Dandelion
  is now marked as not suitable for field identification alone because arnica, a look-alike, is rated high
  severity.
- No tested home recipe with amounts for nixtamalizing corn was found in the sources opened; the corn entry
  says so.
- Some range and season claims rest on one state's agency (for example Virginia for raccoon seasons); seasons
  change every year, and every entry tells the reader to check the state agency.
- A public warning was added to the published repository (PR #3) while these corrections were in progress.
- Every pass-1 entry still carries its pass-1 `reviewed` label; a later pass-2 phase relabels every entry
  that changed. Treat those labels as void.
- Several pages block automated reading (some NIA, FCC, Maryland Biodiversity and Flora of North America
  pages). Where an entry relies on one, the claim was confirmed elsewhere or is labelled.

## Regions: Northeast / New England pack (15 entries)

Pass 2 also added a second region: 15 entries in `regional/northeast-new-england/` for New England and eastern
New York (three each for mushrooms, edible plants, hazards, game animals and crops). The pack was built and
checked the same way, and the same warning holds: every check was done by AI agents. **No human has reviewed any
of these entries.** All 15 say `draft`. Each still needs the human safety read in
[`review/13_northeast_new_england.md`](../review/13_northeast_new_england.md) before it can be marked reviewed.

**Method.** The same spec as the Mid-Atlantic block, re-targeted to New England and New York sources: UNH, UVM,
UMaine, UMass, UConn and Cornell extension; NH Fish and Game, Vermont Fish and Wildlife, Maine IF&W,
MassWildlife, CT DEEP and NY DEC; NOAA, CDC, NAMA and America's Poison Centers. Where no New England page
existed, an out-of-region page (Missouri Department of Conservation, NC State) was used for identification only
and is labelled that way in the entry.

1. **Write.** Five agents wrote the 15 entries, each with the positive-ID safety gate first and every deadly
   look-alike checked against two sources.
2. **Round 1.** Two independent fact-checkers (neither wrote an entry): one for the mushrooms and edible plants,
   one for the game, crops and hazards. Every cited link was opened.
3. **Fixes.** Every round-1 finding was fixed in the entries and the three domain indexes.
4. **Round 2.** A fresh verifier re-checked every fix and the new citations.
5. **Round 3.** One more verifier re-checked every change made after round 2.

**Results**

| Check | Scope | Critical / major / minor |
|-------|-------|--------------------------|
| Round 1 | Mushrooms and edible plants (6 entries, 2 indexes) | 0 / 8 / 36 |
| Round 1 | Game, crops and hazards (9 entries, 3 indexes) | 0 / 3 / 38 |
| Round 2 | All 15 entries and the indexes, after fixes | 0 / 1 / 16; all fixed |
| Round 3 | Changes made after round 2 | 0 / 0 / 5 (optional polish) |

**Selected catches (all fixed)**
- Honey mushroom: the entry listed whitish gills and a ring as positive traits while doctrine point 3 says no
  white-gilled mushroom with a ring or volva. The two were never reconciled, so a reader following point 3 alone
  would reject the species and a reader following the entry alone could miss the *Amanita* pattern. The entry now
  names the conflict and requires an expert with the dug-up specimen.
- Ramps: the gate said each leaf has "its own stalk". Go Botany says var. *burdickii* leaves are "not or
  scarcely petiolate", and that variety grows in Maine, New Hampshire and Vermont, so the trait fails there. The
  entry now says a leaf stalk proves nothing either way.
- False hellebore (toxic plants): the leaves were described as arranged in whorls, copied from one plant record.
  Go Botany and NC State describe them as alternate up the stem with clasping bases.
- Ruffed grouse: New Hampshire's protection of the spruce grouse (no open season, RSA 209:4) was missing, and the
  spruce grouse is the grouse a hunter can mistake for a ruffed grouse.
- Scaly vase (*Turbinellus floccosus*): missing from both the New England and the Mid-Atlantic chanterelle
  entries. It passes the false-gill, white-flesh and on-the-ground checks. Round 2 then misread the NAMA registry
  row for it (a text-extraction misalignment); round 3 re-read the PDF and confirmed 3 adults, onset 3.5 to 9
  hours.
- King bolete: first set to `field_id_not_appropriate: false`, on the argument that no New England source names a
  deadly look-alike. It is now `true`, because *Boletus huronensis* bruises blue only "sometimes" and the group
  cannot be settled in the field.
- Cold water: the entry relied on the 1-10-1 rule alone. The National Center for Cold Water Safety calls it
  misleading and gives shorter times. The entry now reports both and says to wear a life jacket either way.

**Remaining items**
- Season tables are partly out of date. New York grouse and hare dates are the 2025-26 season and New Hampshire
  bag limits come from the agency's 2024-25 table. Each entry says so and tells the reader to check the agency.
- Rhode Island is not covered. The game entries say so and send the reader to Rhode Island DEM, and the tick
  entry did not open a New Hampshire, Massachusetts or Rhode Island health page.
- Some agency pages blocked automated reading and were read through archived copies (the Massachusetts deer
  pages, several New Hampshire and New York pages, and the CDC 1994 fiddlehead report). New York DEC small-game
  dates for 2026-27 and the southern-zone deer dates could not be opened and are not given.
- No New England source names a deadly look-alike for the king bolete or the wild blueberry; both entries say
  that is missing data.
