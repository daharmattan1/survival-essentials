# Safety read 09: Mid-Atlantic game animals

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 9 of 13. Game comes ninth: the risks are real (tularemia, raccoon roundworm, CWD, trichinella) but each is a specific, sourced precaution.

## Time and status

- **Estimated time: 40 minutes at most** for the targeted check below (14 claims at about 2 minutes each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 14,811 words, roughly 60 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain regional/mid-atlantic-appalachian/game-animals --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

Season dates, licenses and methods are state rules that change every year. The entries tell the reader to check the state agency. The checklist asks that `legal_status` be `regulated` or `seasonal-permit` and that the body say "know your regs", not give legal advice. Check the Legal status column.

| Entry | Type | Severity | Look-alike level | Expert ID needed | Field ID not OK | Legal status | Tier | Status now | Words |
|---|---|---|---|---|---|---|---|---|---|
| [Eastern Cottontail Rabbit (Sylvilagus floridanus)](../regional/mid-atlantic-appalachian/game-animals/entries/eastern-cottontail-rabbit.md) | GAME-ANIMAL | high | none | False | False | regulated | T1 | agent-verified | 2428 |
| [Gray Squirrel (Sciurus carolinensis)](../regional/mid-atlantic-appalachian/game-animals/entries/gray-squirrel.md) | GAME-ANIMAL | moderate | low | False | False | regulated | T1 | agent-verified | 2331 |
| [Raccoon & Opossum (Procyon lotor & Didelphis virginiana)](../regional/mid-atlantic-appalachian/game-animals/entries/raccoon-or-opossum.md) | GAME-ANIMAL | high | none | False | False | regulated | T1 | agent-verified | 3541 |
| [White-Tailed Deer (Odocoileus virginianus)](../regional/mid-atlantic-appalachian/game-animals/entries/white-tailed-deer.md) | GAME-ANIMAL | high | none | False | False | regulated | T1 | agent-verified | 3408 |
| [Wild Turkey (Meleagris gallopavo)](../regional/mid-atlantic-appalachian/game-animals/entries/wild-turkey.md) | GAME-ANIMAL | moderate | none | False | False | regulated | T1 | agent-verified | 3103 |

## 2. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "Inspect the liver as a tularemia screen: if it has numerous white lesions about the size of a pinhead, discard the rabbit and do not eat it" | [eastern-cottontail-rabbit.md](../regional/mid-atlantic-appalachian/game-animals/entries/eastern-cottontail-rabbit.md), line 126 | [T1: Missouri Department of Conservation, Rabbit: Safety and Health](https://mdc.mo.gov/hunting-trapping/species/rabbit/rabbit-safety-health) | &#9744; ok<br>&#9744; flag |
| 2 | "Wear latex or nitrile gloves when field-dressing and skinning \[1\]\[2\]; take extra care if you have cuts or open wounds on your hands \[2\]." | [eastern-cottontail-rabbit.md](../regional/mid-atlantic-appalachian/game-animals/entries/eastern-cottontail-rabbit.md), line 130 | [T1: CDC, Preventing Tularemia](https://www.cdc.gov/tularemia/prevention/index.html)<br>[T1: Missouri Department of Conservation, Rabbit: Safety and Health](https://mdc.mo.gov/hunting-trapping/species/rabbit/rabbit-safety-health) | &#9744; ok<br>&#9744; flag |
| 3 | "Do not touch a rabbit that was found dead or that acts sick; CDC says to avoid contact with sick or dead animals" | [eastern-cottontail-rabbit.md](../regional/mid-atlantic-appalachian/game-animals/entries/eastern-cottontail-rabbit.md), line 130 | [T1: CDC, Preventing Tularemia](https://www.cdc.gov/tularemia/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 4 | "165°F internal temperature, measured at the thickest part of the thigh or loin. CDC's 2024 report gives 165°F for cooking wild game \[8\] (it does not name squirrel; this guide applies it to all wild game); its 2004 report gave 160°F \[5\]." | [gray-squirrel.md](../regional/mid-atlantic-appalachian/game-animals/entries/gray-squirrel.md), line 192 | [T1: CDC, Notes from the Field: Suspected Outbreak of Trichinellosis Associated with Undercooked Bea...](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a4.htm)<br>[T1: CDC, Trichinellosis Associated with Bear Meat (MMWR 2004)](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm5327a2.htm) | &#9744; ok<br>&#9744; flag |
| 5 | "Death or permanent disability is a common outcome once larvae reach the nervous system" | [raccoon-or-opossum.md](../regional/mid-atlantic-appalachian/game-animals/entries/raccoon-or-opossum.md), line 213 | [T1: CDC, Clinical Overview of Baylisascariasis](https://www.cdc.gov/baylisascaris/hcp/clinical-overview/index.html) | &#9744; ok<br>&#9744; flag |
| 6 | "Heat kills the eggs; most chemicals do not \[15\]. Use boiling water or flame on hard tools and surfaces (check fire rules first), not bleach or other cleaners" | [raccoon-or-opossum.md](../regional/mid-atlantic-appalachian/game-animals/entries/raccoon-or-opossum.md), line 222 | [T1: CDC, Preventing Raccoon Roundworm (Baylisascaris)](https://www.cdc.gov/baylisascaris/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 7 | "CDC's 2024 report says cooking wild game to 165°F is necessary to kill Trichinella \[13\]; its 2004 report gave 160°F \[3\]." | [raccoon-or-opossum.md](../regional/mid-atlantic-appalachian/game-animals/entries/raccoon-or-opossum.md), line 254 | [T1: CDC, Notes from the Field: Suspected Outbreak of Trichinellosis Associated with Undercooked Bea...](https://www.cdc.gov/mmwr/volumes/73/wr/mm7340a4.htm)<br>[T1: CDC, Trichinellosis Associated with Bear Meat (MMWR 2004)](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm5327a2.htm) | &#9744; ok<br>&#9744; flag |
| 8 | "After any bite or scratch, wash the wound with soap and water for 15 minutes and seek medical care urgently" | [raccoon-or-opossum.md](../regional/mid-atlantic-appalachian/game-animals/entries/raccoon-or-opossum.md), line 177 | [T1: CDC, Rabies Prevention](https://www.cdc.gov/rabies/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 9 | "Cooking temperatures do not destroy prions" | [white-tailed-deer.md](../regional/mid-atlantic-appalachian/game-animals/entries/white-tailed-deer.md), line 209 | [T2: Alberta Health Services (MyHealth.Alberta.ca), Chronic Wasting Disease](https://myhealth.alberta.ca/Alberta/Pages/Chronic-Wasting-Disease-Overview.aspx) | &#9744; ok<br>&#9744; flag |
| 10 | "Do not eat the brain, spinal cord, eyes, spleen, tonsils or lymph nodes" | [white-tailed-deer.md](../regional/mid-atlantic-appalachian/game-animals/entries/white-tailed-deer.md), line 212 | [T2: Alberta Health Services (MyHealth.Alberta.ca), Chronic Wasting Disease](https://myhealth.alberta.ca/Alberta/Pages/Chronic-Wasting-Disease-Overview.aspx)<br>[T1: Indiana Department of Natural Resources, Precautions for Hunters (chronic wasting disease)](https://www.in.gov/dnr/fish-and-wildlife/wildlife-resources/wildlife-diseases-in-indiana/precautions-for-hunters) | &#9744; ok<br>&#9744; flag |
| 11 | "All venison (steaks, roasts, ground): 160°F internal temperature, measured at the thickest point with a food thermometer" | [white-tailed-deer.md](../regional/mid-atlantic-appalachian/game-animals/entries/white-tailed-deer.md), line 226 | [T1: University of Maine Cooperative Extension, In the Kitchen: Safe Minimum Internal Temperatures (...](https://extension.umaine.edu/food-health/2024/03/01/internal-temperatures/)<br>[T1: Virginia Department of Health, Cook to a Safe Minimum Internal Temperature (FoodSafety.gov char...](https://www.vdh.virginia.gov/content/uploads/sites/6/2023/07/Cook_to_a_Safe_Minimum_Internal_Temperature.pdf) | &#9744; ok<br>&#9744; flag |
| 12 | "Heat the strips to an internal 160°F first (in marinade, in an oven, or simmered), then dry at 140°F" | [white-tailed-deer.md](../regional/mid-atlantic-appalachian/game-animals/entries/white-tailed-deer.md), line 185 | [T1: University of Missouri Extension, Making Jerky from Venison](https://extension.missouri.edu/news/making-jerky-from-venison)<br>[T1: Penn State Extension, Proper Care and Handling of Venison from Field to Table](https://extension.psu.edu/proper-care-and-handling-of-venison-from-field-to-table)<br>[T1: Penn State Extension, Drying Jerky](https://extension.psu.edu/drying-jerky)<br>[T1: CDC, Preventing Trichinellosis](https://www.cdc.gov/trichinellosis/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 13 | "165°F internal temperature. Measure at the thickest part of the thigh (not touching bone) with a thermometer; the thermometer is the only reliable test" | [wild-turkey.md](../regional/mid-atlantic-appalachian/game-animals/entries/wild-turkey.md), line 212 | [T1: CDC, Four Steps to Food Safety](https://www.cdc.gov/food-safety/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 14 | "CDC says not to handle wild birds that are obviously sick or found dead" | [wild-turkey.md](../regional/mid-atlantic-appalachian/game-animals/entries/wild-turkey.md), line 203 | [T1: CDC, Hunters and Bird Flu](https://www.cdc.gov/bird-flu/risk-factors/hunters-and-bird-flu.html) | &#9744; ok<br>&#9744; flag |

## 3. CONVENTIONS section 10 checklist

Copied from CONVENTIONS.md section 10.

### Game animals
- [ ] CWD-prion / trichinella / tularemia block present and correct where applicable.
- [ ] Internal cook temps match USDA; deer entry has the full field-dress→skin→butcher→preserve
      flow.
- [ ] `legal_status` is `regulated`/`seasonal-permit` unless a statutory exception is cited; the body distinguishes normal season vs. emergency and is framed as "know your
      regs," not legal advice.

## 4. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Venison at 160 F while other wild game is 165 F

The deer entry follows the USDA chart (160 F) and says so. CDC's 2024 report is about cooking wild game to 165 F and names bear. Decide whether venison should stay on the USDA figure. Note that cooking does not remove CWD prions either way.

> (The 165°F figure in the raccoon, squirrel and bird entries is for wild meat-eaters and poultry; venison follows the USDA chart.
>
> From [white-tailed-deer.md](../regional/mid-atlantic-appalachian/game-animals/entries/white-tailed-deer.md), line 225.

### Jerky: the wild-game entries pre-heat to 165 F while the deer entry says 160 F

The squirrel, rabbit, raccoon and turkey entries heat the strips to 165 F first, citing CDC. The deer entry heats to 160 F. Decide whether one figure should apply to all.

> Heat the strips to an internal 160°F first (in marinade, in an oven, or simmered), then dry at 140°F
>
> From [white-tailed-deer.md](../regional/mid-atlantic-appalachian/game-animals/entries/white-tailed-deer.md), line 184.

> Slice meat thin and heat the strips to 165°F first (CDC's 2024 wild-game figure [8]; Penn State's jerky page says 160°F before drying)
>
> From [gray-squirrel.md](../regional/mid-atlantic-appalachian/game-animals/entries/gray-squirrel.md), line 156.

### Squirrel at 165 F rests on a CDC report that does not name squirrel

The entry says so openly and applies the figure to all wild game. Decide whether that extension is reasonable.

> (it does not name squirrel; this guide applies it to all wild game)
>
> From [gray-squirrel.md](../regional/mid-atlantic-appalachian/game-animals/entries/gray-squirrel.md), line 191.

### Raccoon and opossum: include them at all?

The entry carries a raccoon roundworm warning (death or permanent disability is a common outcome once larvae reach the nervous system) and says jerky is not recommended. Decide whether the precautions are complete enough to keep a how-to for a species with this risk.

> Not recommended for this meat.
>
> From [raccoon-or-opossum.md](../regional/mid-atlantic-appalachian/game-animals/entries/raccoon-or-opossum.md), line 204.

### Delmarva fox squirrel is a protected look-alike

Gray squirrel is `confusability_level: low`. Decide whether that is right where the protected subspecies lives, and whether the entry's description of the difference is enough.

> the Delmarva fox squirrel is a different, protected squirrel.
>
> From [gray-squirrel.md](../regional/mid-atlantic-appalachian/game-animals/entries/gray-squirrel.md), line 104.

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
