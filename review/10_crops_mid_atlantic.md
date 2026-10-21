# Safety read 10: Mid-Atlantic crops

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 10 of 13. Crops come tenth: most of the content is planting windows, but a few lines are poison-or-botulism rules (kidney beans, garlic in oil, bitter squash, green potatoes, corn without alkali).

## Time and status

- **Estimated time: 40 minutes at most** for the targeted check below (14 claims at about 2 minutes each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 13,850 words, roughly 55 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain regional/mid-atlantic-appalachian/crops --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

Planting dates and zone figures are low-stakes and change with the year. Spend your time on the `MANDATORY PREPARATION` sections. The claims below are drawn from them.

| Entry | Type | Severity | Look-alike level | Expert ID needed | Field ID not OK | Legal status | Tier | Status now | Words |
|---|---|---|---|---|---|---|---|---|---|
| [Dry Beans (Phaseolus spp.)](../regional/mid-atlantic-appalachian/crops/entries/beans-dry.md) | CROP | moderate | none | False | False | n/a | T1 | agent-verified | 1888 |
| [Flint Corn (Zea mays, flint varieties)](../regional/mid-atlantic-appalachian/crops/entries/corn-flint.md) | CROP | moderate | none | False | False | n/a | T1 | agent-verified | 1747 |
| [Garlic (Allium sativum)](../regional/mid-atlantic-appalachian/crops/entries/garlic.md) | CROP | lethal | none | False | False | n/a | T1 | agent-verified | 2766 |
| [Kale and Collards (Brassica oleracea)](../regional/mid-atlantic-appalachian/crops/entries/kale-collards.md) | CROP | none | none | False | False | n/a | T1 | agent-verified | 1310 |
| [Potato (Solanum tuberosum)](../regional/mid-atlantic-appalachian/crops/entries/potato.md) | CROP | low | none | False | False | n/a | T1 | agent-verified | 1896 |
| [Sweet Potato (Ipomoea batatas)](../regional/mid-atlantic-appalachian/crops/entries/sweet-potato.md) | CROP | low | low | False | False | n/a | T1 | agent-verified | 2479 |
| [Winter Squash (Cucurbita moschata, C. pepo, C. maxima)](../regional/mid-atlantic-appalachian/crops/entries/winter-squash.md) | CROP | moderate | low | False | False | n/a | T1 | agent-verified | 1764 |

## 2. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "The FDA says as few as four or five raw beans can trigger symptoms" | [beans-dry.md](../regional/mid-atlantic-appalachian/crops/entries/beans-dry.md), line 114 | [T1: U.S. Food and Drug Administration, Bad Bug Book, Second Edition: Phytohaemagglutinin (kidney be...](https://www.fda.gov/media/83271/download) | &#9744; ok<br>&#9744; flag |
| 2 | "Soak the beans in water for at least 5 hours." | [beans-dry.md](../regional/mid-atlantic-appalachian/crops/entries/beans-dry.md), line 119 | [U.S. Food and Drug Administration, Bad Bug Book, Second Edition: Phytohaemagglutinin (kidney bean l...](https://www.fda.gov/media/83271/download) | &#9744; ok<br>&#9744; flag |
| 3 | "Boil the beans in fresh water for at least 30 minutes" | [beans-dry.md](../regional/mid-atlantic-appalachian/crops/entries/beans-dry.md), line 121 | [U.S. Food and Drug Administration, Bad Bug Book, Second Edition: Phytohaemagglutinin (kidney bean l...](https://www.fda.gov/media/83271/download) | &#9744; ok<br>&#9744; flag |
| 4 | "The FDA says slow cookers should not be used for these beans." | [beans-dry.md](../regional/mid-atlantic-appalachian/crops/entries/beans-dry.md), line 124 | [T1: U.S. Food and Drug Administration, Bad Bug Book, Second Edition: Phytohaemagglutinin (kidney be...](https://www.fda.gov/media/83271/download)<br>[T1: University of Illinois Extension, Kidney beans and slow cookers](https://extension.illinois.edu/blogs/live-well-eat-well/2024-02-29-kidney-beans-and-slow-cookers) | &#9744; ok<br>&#9744; flag |
| 5 | "If corn is more than a small part of what you eat, treat it with alkali first, or you risk pellagra." | [corn-flint.md](../regional/mid-atlantic-appalachian/crops/entries/corn-flint.md), line 108 | [World Health Organization (copy hosted by the U.S. Centers for Disease Control and Prevention), Pel...](https://www.cdc.gov/immigrant-refugee-health/media/pdfs/Pellagra-WHO.pdf) | &#9744; ok<br>&#9744; flag |
| 6 | "Mycotoxins survive cooking" | [corn-flint.md](../regional/mid-atlantic-appalachian/crops/entries/corn-flint.md), line 119 | [T2: Crop Protection Network (university extension and research collaboration), Mycotoxin FAQs (Arch...](https://cropprotectionnetwork.org/publications/mycotoxin-faqs-archive) | &#9744; ok<br>&#9744; flag |
| 7 | "Garlic in oil can cause botulism. Never keep it at room temperature, except by the citric-acid method in Rule 2, followed exactly." | [garlic.md](../regional/mid-atlantic-appalachian/crops/entries/garlic.md), line 159 | [National Center for Home Food Preservation (University of Georgia), Freezing Garlic-In-Oil](https://nchfp.uga.edu/how/freeze/vegetable/freezing-garlic-in-oil/)<br>[Penn State Extension, How to Safely Make Infused Oils](https://extension.psu.edu/how-to-safely-make-infused-oils)<br>[University of Georgia College of Agricultural and Environmental Sciences (UGA Extension), 'Tis the...](https://fieldreport.caes.uga.edu/news/tis-the-season-how-to-safely-infuse-oil-for-homemade-gifts/) | &#9744; ok<br>&#9744; flag |
| 8 | "Refrigerate at 40 degrees F or lower for no more than 4 days \[8\]. The CDC says to refrigerate homemade oils made with garlic or herbs and throw them away after 4 days" | [garlic.md](../regional/mid-atlantic-appalachian/crops/entries/garlic.md), line 163 | [T1: National Center for Home Food Preservation (University of Georgia), Freezing Garlic-In-Oil](https://nchfp.uga.edu/how/freeze/vegetable/freezing-garlic-in-oil/)<br>[T1: Centers for Disease Control and Prevention, Botulism Prevention](https://www.cdc.gov/botulism/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 9 | "Make a 3 percent citric acid solution: stir 1 level tablespoon of granular citric acid into 2 cups of water" | [garlic.md](../regional/mid-atlantic-appalachian/crops/entries/garlic.md), line 168 | [T1: University of Idaho, Oregon State University, Washington State University (Pacific Northwest Ex...](https://objects.lib.uidaho.edu/uiext/uiext33171.pdf) | &#9744; ok<br>&#9744; flag |
| 10 | "Use 2/3 cup chopped garlic for 2 cups of solution, 1 part garlic to 3 parts solution. Changing the ratio may give a dangerous product" | [garlic.md](../regional/mid-atlantic-appalachian/crops/entries/garlic.md), line 169 | [T1: Penn State Extension, How to Safely Make Infused Oils](https://extension.psu.edu/how-to-safely-make-infused-oils)<br>[T1: University of Georgia College of Agricultural and Environmental Sciences (UGA Extension), 'Tis...](https://fieldreport.caes.uga.edu/news/tis-the-season-how-to-safely-infuse-oil-for-homemade-gifts/) | &#9744; ok<br>&#9744; flag |
| 11 | "Cooking does not fix it. Oregon State says boiling and microwaving have a negligible effect on glycoalkaloid content" | [potato.md](../regional/mid-atlantic-appalachian/crops/entries/potato.md), line 119 | [T1: Oregon State University Extension Service, Glycoalkaloids in Potato Tubers (EM 9407)](https://extension.oregonstate.edu/catalog/pub/em-9407-glycoalkaloids-potato-tubers) | &#9744; ok<br>&#9744; flag |
| 12 | "If a potato tastes bitter or burns your throat, stop eating it and throw it out." | [potato.md](../regional/mid-atlantic-appalachian/crops/entries/potato.md), line 120 | [T1: Oregon State University Extension Service, Glycoalkaloids in Potato Tubers (EM 9407)](https://extension.oregonstate.edu/catalog/pub/em-9407-glycoalkaloids-potato-tubers) | &#9744; ok<br>&#9744; flag |
| 13 | "If it is bitter, spit it out and throw the whole squash away. Do not cook, boil, or bake bitter-tasting squash. Cooking does not destroy the toxin; heat does not inactivate it" | [winter-squash.md](../regional/mid-atlantic-appalachian/crops/entries/winter-squash.md), line 117 | [T2: America's Poison Centers (Poison Control), Toxic squash syndrome: If it's bitter, it's not dinn...](https://www.poison.org/articles/toxic-squash-syndrome-if-it-s-bitter-it-s-not-dinner) | &#9744; ok<br>&#9744; flag |
| 14 | "Do not save seed from squash grown near ornamental gourds or wild gourds. Buy new seed instead" | [winter-squash.md](../regional/mid-atlantic-appalachian/crops/entries/winter-squash.md), line 101 | [T2: America's Poison Centers (Poison Control), Toxic squash syndrome: If it's bitter, it's not dinn...](https://www.poison.org/articles/toxic-squash-syndrome-if-it-s-bitter-it-s-not-dinner) | &#9744; ok<br>&#9744; flag |

## 3. CONVENTIONS section 10 checklist

Copied from CONVENTIONS.md section 10. For crops, the last box applies directly (`MANDATORY PREPARATION` present and correct on every consumable). The identification boxes do not apply to garden crops.

### Mushrooms & edible-plants
- [ ] Every entry opens with the POSITIVE-ID SAFETY GATE (checklist + disqualifying traits), not a
      single test.
- [ ] Each species **and each deadly look-alike** triangulated against **≥2** T1/T2 references.
- [ ] `confusability_level`, `expert_id_required`, `field_id_not_appropriate` set truthfully.
- [ ] Mushroom doctrine page loads before species; deadly-look-alike matrix populated and leads the
      index; "what NOT to eat" comes before edible exemplars.
- [ ] Morel / false-morel pair present; ≥3 mushroom entries carry a deadly confusable.
- [ ] `⚠ MANDATORY PREPARATION` present and correct on every consumable.

## 4. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Garlic in oil: the repo prints a home recipe with amounts

Rule 2 gives a citric-acid method for holding infused oil at room temperature, with a ratio and a soak time. Botulism can kill. The sources are University of Idaho, Penn State and UGA. Decide whether a public survival reference should print a recipe or only say refrigerate it and throw it out after 4 days.

> Rule 2: the only tested way to hold garlic-infused oil at room temperature.
>
> From [garlic.md](../regional/mid-atlantic-appalachian/crops/entries/garlic.md), line 166.

### Flint corn: no tested nixtamalization recipe

The entry says WHO names lime and wood ash but gives no amounts, and that no tested home recipe was found. It tells the reader to find one. Decide whether that leaves the reader with a pellagra risk and nothing to do about it.

> It gives no amounts or times [1]. Do not guess at them.
>
> From [corn-flint.md](../regional/mid-atlantic-appalachian/crops/entries/corn-flint.md), line 114.

### Dry beans: the FDA kidney-bean rule applied to all dry beans

The FDA gives figures for kidney beans. The entry applies the same rule to every dry bean and says the FDA gives no separate figure for others. Decide whether that is the right extension.

> This entry applies the kidney-bean rule to all dry beans.
>
> From [beans-dry.md](../regional/mid-atlantic-appalachian/crops/entries/beans-dry.md), line 115.

### Potato storage temperature differs by source

Pass 1 had storage too cold. The entry now lists three sources with ranges from 40 to 50 F. Decide whether the entry should give one figure.

> dark, 40 to 46 degrees F, about 90 percent humidity
>
> From [potato.md](../regional/mid-atlantic-appalachian/crops/entries/potato.md), line 96.

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
