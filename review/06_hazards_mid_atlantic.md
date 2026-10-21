# Safety read 06: Mid-Atlantic hazards

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 6 of 13. Hazards come sixth: these entries tell a reader what to do after a bite, a tick or a poisoning, so a wrong step costs minutes at the worst time.

## Time and status

- **Estimated time: 40 minutes at most** for the targeted check below (14 claims at about 2 minutes each; 4 look-alike pairs at about 1 minute each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 11,397 words, roughly 45 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain regional/mid-atlantic-appalachian/hazards --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

Amatoxin mushrooms and the two hemlocks are identification entries. Use the pair table. Rabies, ticks and snakebite are first-aid style entries. Use the claims table and the first-aid box of the checklist.

| Entry | Type | Severity | Look-alike level | Expert ID needed | Field ID not OK | Legal status | Tier | Status now | Words |
|---|---|---|---|---|---|---|---|---|---|
| [Amatoxin Mushrooms: Destroying Angels, Death Cap and Deadly Galerina (Amanita and Galerina spp.)](../regional/mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md) | HAZARD | lethal | deadly-lookalike-exists | True | True | n/a | T1 | agent-verified | 2689 |
| [Rabies and Wildlife Bites (Raccoons, Bats, Skunks, Foxes)](../regional/mid-atlantic-appalachian/hazards/entries/rabies-and-wildlife-bites.md) | HAZARD | lethal | none | False | False | n/a | T1 | agent-verified | 1976 |
| [Ticks, Lyme Disease & Other Tick-Borne Illness](../regional/mid-atlantic-appalachian/hazards/entries/ticks-and-lyme.md) | HAZARD | high | low | False | False | n/a | T1 | agent-verified | 1532 |
| [Toxic Plants — Poison Hemlock, Sap-Burn Umbels & Poison Ivy (Water Hemlock Has Its Own Entry)](../regional/mid-atlantic-appalachian/hazards/entries/toxic-plants-hemlock-poison-ivy.md) | HAZARD | lethal | deadly-lookalike-exists | True | True | n/a | T1 | agent-verified | 1728 |
| [Venomous Snakes — Copperhead, Timber Rattlesnake, Cottonmouth & Massasauga](../regional/mid-atlantic-appalachian/hazards/entries/venomous-snakes-copperhead-rattlesnake.md) | HAZARD | high | moderate | False | False | n/a | T1 | agent-verified | 1290 |
| [Water Hemlock (Cicuta maculata)](../regional/mid-atlantic-appalachian/hazards/entries/water-hemlock-cicuta.md) | HAZARD | lethal | deadly-lookalike-exists | True | True | n/a | T1 | agent-verified | 2182 |

## 2. Look-alike pairs: two sources each

CONVENTIONS section 7 needs each look-alike checked against at least two Tier 1 or Tier 2 sources. The two links are the sources the entry cites on the lines that name the look-alike, with a page named for the look-alike ranked first, then the most often cited. A source marked (general) is cited on those lines but its title does not name the look-alike, so read it for the difference and look for a page that names it. "First line" is the first line that names it. If a row says only one source is cited, finding the second is part of your job. A T3 source does not count toward the two. Check that the entry's stated difference, and what the look-alike does to a person, match both sources.

| Species | Look-alike | First line | Source 1 | Source 2 | Check |
|---|---|---|---|---|---|
| [Amatoxin Mushrooms: Destroying Angels, Death Cap and Deadly Galerina (Amanita and Galerina spp.)](../regional/mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md) | Paddy-straw mushroom and puffballs | 105 | [T1: StatPearls, NIH National Library of Medicine, Amatoxin Mushroom Toxicity (general)](https://www.ncbi.nlm.nih.gov/sites/books/NBK431052/) | [T1: Missouri Department of Conservation, Amanitas (general)](https://mdc.mo.gov/discover-nature/field-guide/amanitas) | &#9744; |
| [Water Hemlock (Cicuta maculata)](../regional/mid-atlantic-appalachian/hazards/entries/water-hemlock-cicuta.md) | Wild parsnip and other parsnips | 76 | [T1: CDC, MMWR 43(13), Water Hemlock Poisoning - Maine, 1992 (general)](https://www.cdc.gov/mmwr/PDF/wk/mm4313.pdf) | [T1: U.S. Fish and Wildlife Service, Don't touch these plants! Six lookalikes you want to avoid (gen...](https://fws.gov/story/dont-touch-these-plants) | &#9744; |
| [Water Hemlock (Cicuta maculata)](../regional/mid-atlantic-appalachian/hazards/entries/water-hemlock-cicuta.md) | Wild carrot (Queen Anne's lace) | 76 | [T2: Cornell University, Weed Identification, Wild Carrot](https://blogs.cornell.edu/weedid/wild-carrot/) | [T1: U.S. Fish and Wildlife Service, Don't touch these plants! Six lookalikes you want to avoid (gen...](https://fws.gov/story/dont-touch-these-plants) | &#9744; |
| [Toxic Plants — Poison Hemlock, Sap-Burn Umbels & Poison Ivy (Water Hemlock Has Its Own Entry)](../regional/mid-atlantic-appalachian/hazards/entries/toxic-plants-hemlock-poison-ivy.md) | Poison hemlock look-alikes (wild carrot, parsnip, parsley, anise, angelica) | 59 | [T1: North Carolina State Extension, Conium maculatum (Poison Hemlock), Plant Toolbox (general)](https://plants.ces.ncsu.edu/plants/conium-maculatum/) | **only one source cited in the entry: find a second** | &#9744; |

## 3. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "No symptoms for at least 6 hours \[2\]. Windows given: 6 to 24 hours \[3\]\[4\], 6 to 12 hours \[5\], 5 to 12 hours \[10\]" | [amatoxin-mushrooms-amanita-galerina.md](../regional/mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md), line 179 | [T1: Utah Poison Control Center, University of Utah, Mushroom Ingestion - Diagnosis and Management](https://poisoncontrol.utah.edu/news/2021/08/mushroom-ingestion-diagnosis-and-management)<br>[T1: CDC, MMWR 66(21), Amanita phalloides Mushroom Poisonings - Northern California, December 2016](https://www.cdc.gov/mmwr/volumes/66/wr/mm6621a1.htm)<br>[T1: CDC, MMWR, Amanita phalloides Mushroom Poisoning - Northern California, January 1997](https://www.cdc.gov/mmwr/preview/mmwrhtml/00047808.htm)<br>[T1: StatPearls, NIH National Library of Medicine, Amatoxin Mushroom Toxicity](https://www.ncbi.nlm.nih.gov/sites/books/NBK431052/) | &#9744; ok<br>&#9744; flag |
| 2 | "NAMA's review of over 2,000 cases from western Europe, the United States and Canada found an average mortality of 11.58 percent. NAMA also says the rate exceeds 50 percent in many non-western countries, and that with good hospital supportive care alone the majority (80 to 90 percent) of poisonings resolve" | [amatoxin-mushrooms-amanita-galerina.md](../regional/mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md), line 185 | [T2: North American Mycological Association (NAMA) Toxicology Committee, Amatoxin Mushroom Poisoning...](https://namyco.org/wp-content/uploads/2023/08/Amatoxin_Poisoning_2015-16.pdf) | &#9744; ok<br>&#9744; flag |
| 3 | "Call Poison Help, 1-800-222-1222, right away if you think someone ate a wild mushroom \[1\]. Do not wait for symptoms." | [amatoxin-mushrooms-amanita-galerina.md](../regional/mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md), line 168 | [T1: America's Poison Centers (Poison Help), Mushroom poisoning: Don't invite "the death angel" to d...](https://www.poison.org/articles/wild-mushroom-warning) | &#9744; ok<br>&#9744; flag |
| 4 | "rabies is always fatal without post-exposure care, and by the time symptoms appear, virtually all cases are fatal" | [rabies-and-wildlife-bites.md](../regional/mid-atlantic-appalachian/hazards/entries/rabies-and-wildlife-bites.md), line 76 | [T1: Pennsylvania Department of Health, Rabies Fact Sheet (updated 10/9/2025)](https://www.pa.gov/content/dam/copapwp-pagov/en/health/documents/topics/documents/programs/rabies/Rabies%20Fact%20Sheet.pdf)<br>[T1: CDC, Rabies Prevention](https://www.cdc.gov/rabies/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 5 | "Wash the wound with soap and water for 15 minutes to flush out virus" | [rabies-and-wildlife-bites.md](../regional/mid-atlantic-appalachian/hazards/entries/rabies-and-wildlife-bites.md), line 113 | [T1: CDC, Rabies Prevention](https://www.cdc.gov/rabies/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 6 | "Virginia's health department says Powassan virus can be passed in as little as 15 minutes" | [ticks-and-lyme.md](../regional/mid-atlantic-appalachian/hazards/entries/ticks-and-lyme.md), line 77 | [T1: Virginia Department of Health, Tick-borne Diseases](https://www.vdh.virginia.gov/ticks/tick-borne-diseases/) | &#9744; ok<br>&#9744; flag |
| 7 | "CDC says testing a removed tick is generally not recommended, and the results should not guide treatment." | [ticks-and-lyme.md](../regional/mid-atlantic-appalachian/hazards/entries/ticks-and-lyme.md), line 90 | [T1: CDC, After a Tick Bite](https://www.cdc.gov/ticks/after-a-tick-bite/index.html) | &#9744; ok<br>&#9744; flag |
| 8 | "usually shows up 3 to 30 days after a bite, often around day 7, in roughly 70 to 80 percent of infected people" | [ticks-and-lyme.md](../regional/mid-atlantic-appalachian/hazards/entries/ticks-and-lyme.md), line 95 | [T1: CDC, Signs and Symptoms of Lyme Disease](https://www.cdc.gov/lyme/signs-symptoms/index.html) | &#9744; ok<br>&#9744; flag |
| 9 | "Do not use petroleum jelly, heat, nail polish or similar. CDC says these can agitate the tick and push infected fluid into your skin." | [ticks-and-lyme.md](../regional/mid-atlantic-appalachian/hazards/entries/ticks-and-lyme.md), line 86 | [T1: CDC, After a Tick Bite](https://www.cdc.gov/ticks/after-a-tick-bite/index.html) | &#9744; ok<br>&#9744; flag |
| 10 | "Antivenom, if needed, is started at a hospital, and care stops damage that cannot be undone" | [venomous-snakes-copperhead-rattlesnake.md](../regional/mid-atlantic-appalachian/hazards/entries/venomous-snakes-copperhead-rattlesnake.md), line 82 | [T1: CDC NIOSH, Venomous Snakes: If a snake bites you (first aid) and what not to do](https://www.cdc.gov/niosh/topics/snakes/symptoms.html) | &#9744; ok<br>&#9744; flag |
| 11 | "Call 911, or have someone drive you. Do not drive yourself." | [venomous-snakes-copperhead-rattlesnake.md](../regional/mid-atlantic-appalachian/hazards/entries/venomous-snakes-copperhead-rattlesnake.md), line 83 | [T1: CDC NIOSH, Venomous Snakes: If a snake bites you (first aid) and what not to do](https://www.cdc.gov/niosh/topics/snakes/symptoms.html)<br>[T1: Maryland Department of Natural Resources, Venomous Snakes](https://dnr.maryland.gov/wildlife/Pages/plants_wildlife/herps/Venomous-Snakes.aspx) | &#9744; ok<br>&#9744; flag |
| 12 | "a 2 to 3 cm piece of root can be fatal in an adult" | [toxic-plants-hemlock-poison-ivy.md](../regional/mid-atlantic-appalachian/hazards/entries/toxic-plants-hemlock-poison-ivy.md), line 80 | [T1: CDC, MMWR 43(13), Water Hemlock Poisoning - Maine, 1992](https://www.cdc.gov/mmwr/PDF/wk/mm4313.pdf) | &#9744; ok<br>&#9744; flag |
| 13 | "Two brothers digging for wild ginseng in a Maine swamp ate a water hemlock root. One died about 3 hours after eating it" | [water-hemlock-cicuta.md](../regional/mid-atlantic-appalachian/hazards/entries/water-hemlock-cicuta.md), line 105 | [T1: CDC, MMWR 43(13), Water Hemlock Poisoning - Maine, 1992](https://www.cdc.gov/mmwr/PDF/wk/mm4313.pdf) | &#9744; ok<br>&#9744; flag |
| 14 | "Do not use smell or taste to identify it." | [water-hemlock-cicuta.md](../regional/mid-atlantic-appalachian/hazards/entries/water-hemlock-cicuta.md), line 100 | [T1: CDC, MMWR 43(13), Water Hemlock Poisoning - Maine, 1992](https://www.cdc.gov/mmwr/PDF/wk/mm4313.pdf)<br>[T1: USDA Agricultural Research Service, Poisonous Plant Research Laboratory, Water hemlock (Cicuta...](https://www.ars.usda.gov/pacific-west-area/logan-ut/poisonous-plant-research/docs/water-hemlock-cicuta-douglasii/) | &#9744; ok<br>&#9744; flag |

## 4. CONVENTIONS section 10 checklist

Copied from CONVENTIONS.md section 10. Use the mushrooms and plants list for the amatoxin and the two hemlock entries. Use the first-aid and water list for rabies, ticks and snakebite.

### Mushrooms & edible-plants
- [ ] Every entry opens with the POSITIVE-ID SAFETY GATE (checklist + disqualifying traits), not a
      single test.
- [ ] Each species **and each deadly look-alike** triangulated against **≥2** T1/T2 references.
- [ ] `confusability_level`, `expert_id_required`, `field_id_not_appropriate` set truthfully.
- [ ] Mushroom doctrine page loads before species; deadly-look-alike matrix populated and leads the
      index; "what NOT to eat" comes before edible exemplars.
- [ ] Morel / false-morel pair present; ≥3 mushroom entries carry a deadly confusable.
- [ ] `⚠ MANDATORY PREPARATION` present and correct on every consumable.

### First-aid & water
- [ ] First-aid covers wound infection, hypo/hyperthermia, dehydration/diarrhea, med-continuity;
      each has RED FLAGS / EVAC + DO NOT.
- [ ] Every water entry has the `⚠ CONTAMINATION` block with boil time, micron limit, and the
      chemical-vs-biological boundary.
- [ ] All medical/water claims verified vs. CDC / Red Cross / EPA / extension (T1).

## 5. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Amatoxin mortality: a range, and a first entry that gives a different average than the puffball entry

The amatoxin entry gives an 11.58 percent average (NAMA, over 2,000 cases) and 80 to 90 percent resolving with good hospital supportive care. The puffball entry in [domain 04](04_mushrooms_mid_atlantic.md) gives about 50% without prompt treatment, about 10% in the U.S. and Canada, and under 5% in a developed-country series. Decide whether the two entries should carry the same list.

> NAMA's review of over 2,000 cases from western Europe, the United States and Canada found an average mortality of 11.58 percent.
>
> From [amatoxin-mushrooms-amanita-galerina.md](../regional/mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md), line 184.

### Snakebite: leave the 2-to-4-hour window out

Pass 1 said "get to a hospital within 2-4 hours". CDC says emergency care as soon as possible. The entry now says do not wait for symptoms and do not drive yourself. Decide whether the lay reader needs a clearer line for the case where there is no phone and no road.

> Get emergency medical care as soon as possible.
>
> From [venomous-snakes-copperhead-rattlesnake.md](../regional/mid-atlantic-appalachian/hazards/entries/venomous-snakes-copperhead-rattlesnake.md), line 81.

### Ticks: do not save the tick for testing

Older advice said to save the tick. CDC says testing a removed tick is generally not recommended. The entry allows a photo and a note. Decide if that is the right compromise.

> CDC says testing a removed tick is generally not recommended, and the results should not guide treatment.
>
> From [ticks-and-lyme.md](../regional/mid-atlantic-appalachian/hazards/entries/ticks-and-lyme.md), line 89.

### Poison hemlock height: two sources disagree

NC State and the University of Maryland give different heights. Heights are a poor identifier either way, and the entry says so. Decide whether to keep both.

> NC State says it grows 6 to 10 feet tall [1]. The University of Maryland's agronomy blog says 4 to 6 feet when mature [2].
>
> From [toxic-plants-hemlock-poison-ivy.md](../regional/mid-atlantic-appalachian/hazards/entries/toxic-plants-hemlock-poison-ivy.md), line 72.

### Water hemlock smell: two sources describe it differently

CDC says it smells like fresh turnips. USDA ARS says carrot-like. The entry tells the reader not to use smell or taste. Decide whether both descriptions should stay.

> The two sources describe the smell differently.
>
> From [water-hemlock-cicuta.md](../regional/mid-atlantic-appalachian/hazards/entries/water-hemlock-cicuta.md), line 99.

## 6. Sign-off

Fill this in and send it with the [Expert review form](../.github/ISSUE_TEMPLATE/expert-review.yml). Do not tick pass unless you read every entry listed above.

| | |
|---|---|
| Reviewer name | |
| Relevant expertise | |
| Date | |
| Entries read (list, or "all") | |
| Findings filed (issue links) | |
| Result | &#9744; Pass &nbsp;&nbsp; &#9744; Fail &nbsp;&nbsp; &#9744; Pass after the findings above are fixed |

I read the entries listed above against the checklist. I checked the safety claims against the sources linked here or against sources I name in my findings.

Signature or name: ______________________

Back to the [Safety Read Packet](SAFETY_READ_PACKET.md).
