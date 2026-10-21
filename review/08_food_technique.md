# Safety read 08: Food technique

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 8 of 13. Food technique comes eighth: the stakes are cook temperatures, botulism and infant formula, which are specific and checkable.

## Time and status

- **Estimated time: 40 minutes at most** for the targeted check below (15 claims at about 2 minutes each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 14,041 words, roughly 55 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain substrate/05_food --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

| Entry | Type | Severity | Tier | Status now | Words |
|---|---|---|---|---|---|
| [Calorie Planning and Rationing Stored Food](../substrate/05_food/entries/calorie-planning-and-rationing.md) | METHOD | low | T1 | agent-verified | 1980 |
| [Cooking Without Power (Outage or Camp): Outdoors Only, to Temperature](../substrate/05_food/entries/cooking-without-power.md) | METHOD | high | T1 | agent-verified | 2780 |
| [Fish & Game Processing — Gutting, Cleaning, Dressing & Preservation](../substrate/05_food/entries/fish-and-game-processing-basics.md) | METHOD | moderate | T1 | agent-verified | 3418 |
| [Passive Fishing — Trotlines, Set Lines, Fish Traps & Weirs](../substrate/05_food/entries/passive-fishing-trotline-and-traps.md) | METHOD | n/a | T1 | agent-verified | 1652 |
| [Home Drying: Jerky, Fruit and Vegetables (and Why Not Cold Smoking or Improvised Salt Curing)](../substrate/05_food/entries/preservation-drying-smoking-salting.md) | METHOD | high | T1 | agent-verified | 2833 |
| [Small Game Trapping — Snares, Deadfalls & Trap Lines](../substrate/05_food/entries/small-game-trapping-snares.md) | METHOD | n/a | T1 | agent-verified | 1378 |

## 2. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "Cook to 145 F internal, or until the flesh is opaque and separates easily with a fork" | [fish-and-game-processing-basics.md](../substrate/05_food/entries/fish-and-game-processing-basics.md), line 150 | [T1: CDC, Four Steps to Food Safety (145 F fish, 160 F ground meat, 165 F poultry; 40-140 F danger z...](https://www.cdc.gov/food-safety/prevention/index.html)<br>[T1: University of Maine Cooperative Extension, In the Kitchen: Safe Minimum Internal Temperatures (...](https://extension.umaine.edu/food-health/2024/03/01/internal-temperatures/) | &#9744; ok<br>&#9744; flag |
| 2 | "Game birds and all poultry: 165 F internal, with juices running clear" | [fish-and-game-processing-basics.md](../substrate/05_food/entries/fish-and-game-processing-basics.md), line 194 | [T1: CDC, Four Steps to Food Safety (145 F fish, 160 F ground meat, 165 F poultry; 40-140 F danger z...](https://www.cdc.gov/food-safety/prevention/index.html)<br>[T1: North Dakota State University Extension, A Pocket Guide to Care and Handling of Game Birds from...](https://www.ndsu.edu/agriculture/node/2050)<br>[T1: Penn State Extension, Proper Field Dressing and Handling of Wild Game and Fish](https://extension.psu.edu/proper-field-dressing-and-handling-of-wild-game-and-fish) | &#9744; ok<br>&#9744; flag |
| 3 | "USDA's chart says 160 F internal \[2\]\[3\]. The Missouri Department of Conservation says 165 F \[18\]. The two sources differ; this guide's rule is 165 F, which covers both." | [fish-and-game-processing-basics.md](../substrate/05_food/entries/fish-and-game-processing-basics.md), line 192 | [T1: University of Maine Cooperative Extension, In the Kitchen: Safe Minimum Internal Temperatures (...](https://extension.umaine.edu/food-health/2024/03/01/internal-temperatures/)<br>[T1: Virginia Department of Health, Cook to a Safe Minimum Internal Temperature (FoodSafety.gov char...](https://www.vdh.virginia.gov/content/uploads/sites/6/2023/07/Cook_to_a_Safe_Minimum_Internal_Temperature.pdf)<br>[T1: Missouri Department of Conservation, Rabbit: Safety and Health](https://mdc.mo.gov/hunting-trapping/species/rabbit/rabbit-safety-health) | &#9744; ok<br>&#9744; flag |
| 4 | "Raccoon, opossum and other wild meat-eaters or omnivores: 165 F in any form, including jerky strips" | [fish-and-game-processing-basics.md](../substrate/05_food/entries/fish-and-game-processing-basics.md), line 193 | [T1: CDC, Notes from the Field: Suspected Outbreak of Trichinellosis Associated with Undercooked Bea...](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a4.htm) | &#9744; ok<br>&#9744; flag |
| 5 | "If a rabbit's liver has numerous white lesions about the size of a pinhead, discard the rabbit and do not eat it" | [fish-and-game-processing-basics.md](../substrate/05_food/entries/fish-and-game-processing-basics.md), line 163 | [T1: Missouri Department of Conservation, Rabbit: Safety and Health](https://mdc.mo.gov/hunting-trapping/species/rabbit/rabbit-safety-health) | &#9744; ok<br>&#9744; flag |
| 6 | "cool it quickly to 35–40 F" | [fish-and-game-processing-basics.md](../substrate/05_food/entries/fish-and-game-processing-basics.md), line 115 | [T1: Penn State Extension, Proper Care and Handling of Venison from Field to Table](https://extension.psu.edu/proper-care-and-handling-of-venison-from-field-to-table)<br>[T1: Penn State Extension, Proper Field Dressing and Handling of Wild Game and Fish](https://extension.psu.edu/proper-field-dressing-and-handling-of-wild-game-and-fish) | &#9744; ok<br>&#9744; flag |
| 7 | "You cannot see, smell or taste the toxin, and tasting a small amount of contaminated food can be deadly" | [preservation-drying-smoking-salting.md](../substrate/05_food/entries/preservation-drying-smoking-salting.md), line 99 | [T1: CDC, Preventing Botulism](https://www.cdc.gov/botulism/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 8 | "CDC's 2024 report says cooking wild game meat to at least 165 F is necessary to kill Trichinella and that freezing might not be sufficient" | [preservation-drying-smoking-salting.md](../substrate/05_food/entries/preservation-drying-smoking-salting.md), line 118 | [T1: CDC, Notes from the Field: Suspected Outbreak of Trichinellosis Associated with Undercooked Bea...](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a4.htm) | &#9744; ok<br>&#9744; flag |
| 9 | "Put them in a dehydrator or oven preheated to 140 F" | [preservation-drying-smoking-salting.md](../substrate/05_food/entries/preservation-drying-smoking-salting.md), line 122 | [T1: National Center for Home Food Preservation (University of Georgia), Jerky](https://nchfp.uga.edu/how/dry/jerky.html)<br>[T1: Penn State Extension, Drying Jerky](https://extension.psu.edu/drying-jerky) | &#9744; ok<br>&#9744; flag |
| 10 | "Keep meat at 40 F or below" | [preservation-drying-smoking-salting.md](../substrate/05_food/entries/preservation-drying-smoking-salting.md), line 117 | [T1: National Center for Home Food Preservation (University of Georgia), Jerky](https://nchfp.uga.edu/how/dry/jerky.html)<br>[T1: Kansas State University Research and Extension, Dehydrating Meat Safely at Home (MF3173, rev. M...](https://bookstore.ksre.ksu.edu/download/dry-meat-safely-at-home_MF3173) | &#9744; ok<br>&#9744; flag |
| 11 | "Food between 40 F and 140 F spoils fast, and perishable food left out more than 2 hours (1 hour above 90 F) should be thrown out" | [passive-fishing-trotline-and-traps.md](../substrate/05_food/entries/passive-fishing-trotline-and-traps.md), line 114 | [T1: CDC, Four Steps to Food Safety (145 F fish; 40-140 F danger zone; 2-hour rule)](https://www.cdc.gov/food-safety/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 12 | "never ration drinking water unless ordered to do so by authorities" | [calorie-planning-and-rationing.md](../substrate/05_food/entries/calorie-planning-and-rationing.md), line 65 | [T1: Ready.gov / FEMA, Water](https://www.ready.gov/water)<br>[T1: FEMA, via Henry County (Indiana) Emergency Management, Food and Water in an Emergency (brochure...](https://henrycounty.in.gov/DocumentCenter/View/295/Food-and-Water-in-an-Emergency-PDF) | &#9744; ok<br>&#9744; flag |
| 13 | "Never dilute formula and never stretch it (this entry's rule). CDC says adding too much or too little formula can make a baby sick \[7\]. Do not make or feed homemade formula" | [calorie-planning-and-rationing.md](../substrate/05_food/entries/calorie-planning-and-rationing.md), line 135 | [T1: CDC, Prepare and Store Powdered Infant Formula in an Emergency (toolkit page)](https://www.cdc.gov/infant-feeding-emergencies-toolkit/php/powdered-infant-formula.html) | &#9744; ok<br>&#9744; flag |
| 14 | "Never heat a home with a gas oven or range" | [cooking-without-power.md](../substrate/05_food/entries/cooking-without-power.md), line 130 | [T1: Ready.gov / FEMA, Power Outages](https://www.ready.gov/power-outages)<br>[T1: CDC, Carbon Monoxide Poisoning (About)](https://www.cdc.gov/carbon-monoxide/about/index.html)<br>[T1: U.S. Consumer Product Safety Commission, Carbon Monoxide Fact Sheet](https://www.cpsc.gov/safety-education/safety-guides/carbon-monoxide/carbon-monoxide-fact-sheet) | &#9744; ok<br>&#9744; flag |
| 15 | "No source opened for this entry supports one. The Virginia DWR page contains no general emergency or survival exception" | [small-game-trapping-snares.md](../substrate/05_food/entries/small-game-trapping-snares.md), line 62 | [Virginia Department of Wildlife Resources, Trapping regulations](https://dwr.virginia.gov/?p=8638) | &#9744; ok<br>&#9744; flag |

## 3. CONVENTIONS section 10 checklist

Copied from CONVENTIONS.md section 10. This domain is universal technique, not species entries. The cook-temperature and legal-status boxes apply. The CWD, trichinella and tularemia box applies to the game entries in [domain 09](09_game_mid_atlantic.md); here, check that the technique entries point to them.

### Game animals
- [ ] CWD-prion / trichinella / tularemia block present and correct where applicable.
- [ ] Internal cook temps match USDA; deer entry has the full field-dress→skin→butcher→preserve
      flow.
- [ ] `legal_status` is `regulated`/`seasonal-permit` unless a statutory exception is cited; the body distinguishes normal season vs. emergency and is framed as "know your
      regs," not legal advice.

## 4. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Rabbit and hare: USDA says 160 F, Missouri says 165 F, the repo uses 165 F

The repo takes the higher figure so one number covers both sources. Decide whether that is a fair reading and whether the entry should keep stating that the two sources differ.

> The two sources differ; this guide's rule is 165 F, which covers both.
>
> From [fish-and-game-processing-basics.md](../substrate/05_food/entries/fish-and-game-processing-basics.md), line 191.

### Wild game 165 F follows CDC's 2024 report; the 2004 report said 160 F

The repo changed from 160 F to 165 F in pass 2 for bear, wild pig and other wild meat-eaters, and applies 165 F to squirrel as well even though the report does not name squirrel. Venison stays at 160 F (USDA chart). Decide whether that split is right.

> CDC's 2024 figure for wild game is 165 F [20]; its 2004 report gave 160 F [15].
>
> From [fish-and-game-processing-basics.md](../substrate/05_food/entries/fish-and-game-processing-basics.md), line 192.

### No field method for drying, smoking or salt-curing fish

The entry gives none because it found no tested field method. Decide whether silence is the right call or whether a reader will improvise anyway.

> Do not dry, smoke or salt-cure fish in the field.
>
> From [fish-and-game-processing-basics.md](../substrate/05_food/entries/fish-and-game-processing-basics.md), line 151.

### No survival exemption for snaring or deadfalls

The entry says no source supports an emergency exemption and tells the reader to know the regulations. The CONVENTIONS rule is to default to `regulated` unless a statute is cited. Decide whether the body is framed as "know your regs" and not as legal advice.

> Do not assume that being in an emergency makes snaring or deadfalls lawful (this guide's judgment).
>
> From [small-game-trapping-snares.md](../substrate/05_food/entries/small-game-trapping-snares.md), line 61.

### Never dilute or stretch infant formula: the repo's own rule

The entry cites CDC for the harm of too much or too little formula and adds its own never-stretch rule. Decide whether that is the right line for a reader in a shortage.

> Never dilute formula and never stretch it (this entry's rule).
>
> From [calorie-planning-and-rationing.md](../substrate/05_food/entries/calorie-planning-and-rationing.md), line 134.

## 5. Sign-off

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
