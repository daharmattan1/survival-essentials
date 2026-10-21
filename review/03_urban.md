# Safety read 03: Urban survival: carbon monoxide, food safety, heat and cold

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 3 of 13. Urban comes third: carbon monoxide kills quietly, and home heat and cold kill the people least able to judge for themselves.

## Time and status

- **Estimated time: 45 minutes at most** for the targeted check below (17 claims at about 2 minutes each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 17,423 words, roughly 70 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain substrate/09_urban_survival --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

The survey guide [09_urban_survival.md](../09_urban_survival.md) is the doorway to these entries and carries the same rules. Read its medicine section with the insulin judgment call below. It has no `review_status`, so `mark_reviewed.py` does not touch it.

| Entry | Type | Severity | Tier | Status now | Words |
|---|---|---|---|---|---|
| [Civil Disruption Safety — Follow Officials, Plan Your Exits, Shelter or Leave](../substrate/09_urban_survival/entries/civil-disruption-safety.md) | PROTOCOL | n/a | T1 | agent-verified | 836 |
| [Extreme Heat at Home With No Power or Air Conditioning](../substrate/09_urban_survival/entries/extreme-heat-at-home.md) | PROTOCOL | lethal | T1 | agent-verified | 1809 |
| [Food Safety During Outages and Floods](../substrate/09_urban_survival/entries/food-safety-during-outages.md) | PROTOCOL | high | T1 | agent-verified | 1958 |
| [Generator and Heater Carbon Monoxide Prevention](../substrate/09_urban_survival/entries/generator-and-heater-co-prevention.md) | PROTOCOL | lethal | T1 | agent-verified | 2288 |
| [Power Outage Bug-In — Heat, Cold, Food Safety, and Carbon Monoxide](../substrate/09_urban_survival/entries/power-outage-bug-in.md) | METHOD | n/a | T1 | agent-verified | 2063 |
| [Sanitation and Human-Waste Disposal — Disease Prevention When Plumbing Fails](../substrate/09_urban_survival/entries/sanitation-and-human-waste.md) | PROTOCOL | n/a | T1 | agent-verified | 1239 |
| [Winter Storm at Home With No Heat](../substrate/09_urban_survival/entries/winter-storm-at-home.md) | PROTOCOL | lethal | T1 | agent-verified | 2245 |
| [09\_urban\_survival.md](../09_urban_survival.md) | survey guide | n/a | n/a | no status field | 4985 |

## 2. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "More than 400 Americans die each year from CO poisoning that is not linked to fires" | [generator-and-heater-co-prevention.md](../substrate/09_urban_survival/entries/generator-and-heater-co-prevention.md), line 80 | [T1: CDC, Carbon Monoxide Poisoning (About)](https://www.cdc.gov/carbon-monoxide/about/index.html) | &#9744; ok<br>&#9744; flag |
| 2 | "The rule: nothing burns inside a tent, vehicle, garage, snow shelter or home, except a vented fireplace or stove in working order. A generator runs outdoors only, at least 20 ft from windows, doors and vents. A vent or a cracked window is not a fix" | [generator-and-heater-co-prevention.md](../substrate/09_urban_survival/entries/generator-and-heater-co-prevention.md), line 82 | [T1: U.S. Consumer Product Safety Commission, CPSC Safety Alert: Portable Generator Hazards (Publica...](https://www.cpsc.gov/s3fs-public/5123_SafetyAlert_PortableGenerators_102021.pdf)<br>[T1: CDC, Carbon Monoxide Poisoning (About)](https://www.cdc.gov/carbon-monoxide/about/index.html)<br>[T1: Ready.gov / FEMA, Power Outages](https://www.ready.gov/power-outages) | &#9744; ok<br>&#9744; flag |
| 3 | "Never ignore it. Everyone goes outside now, then call 911 or emergency services from outside. Do not go back in until responders say you may" | [generator-and-heater-co-prevention.md](../substrate/09_urban_survival/entries/generator-and-heater-co-prevention.md), line 109 | [T1: U.S. Consumer Product Safety Commission, Carbon Monoxide Information Center](https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center)<br>[T1: U.S. Consumer Product Safety Commission, Carbon Monoxide Fact Sheet](https://www.cpsc.gov/safety-education/safety-guides/carbon-monoxide/carbon-monoxide-fact-sheet) | &#9744; ok<br>&#9744; flag |
| 4 | "Run a generator outdoors only, at least 20 feet from windows, doors, vents, and attached garages, with the exhaust pointing away from the house." | [power-outage-bug-in.md](../substrate/09_urban_survival/entries/power-outage-bug-in.md), line 103 | [CDC, What to Do to Protect Yourself During a Power Outage](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html)<br>[CDC, Carbon Monoxide Poisoning (About)](https://www.cdc.gov/carbon-monoxide/about/index.html)<br>[CDC, Safety Guidelines: During & After a Winter Storm](https://www.cdc.gov/winter-weather/safety/stay-safe-during-after-a-winter-storm-safety.html) | &#9744; ok<br>&#9744; flag |
| 5 | "Never use a gas range or oven to heat the home" | [power-outage-bug-in.md](../substrate/09_urban_survival/entries/power-outage-bug-in.md), line 105 | [CDC, What to Do to Protect Yourself During a Power Outage](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html)<br>[CDC, Carbon Monoxide Poisoning (About)](https://www.cdc.gov/carbon-monoxide/about/index.html)<br>[CDC, Safety Guidelines: During & After a Winter Storm](https://www.cdc.gov/winter-weather/safety/stay-safe-during-after-a-winter-storm-safety.html) | &#9744; ok<br>&#9744; flag |
| 6 | "Closed fridge: about 4 hours" | [food-safety-during-outages.md](../substrate/09_urban_survival/entries/food-safety-during-outages.md), line 111 | [T1: USDA Food Safety and Inspection Service, Keep Your Food Safe During Emergencies: Power Outages,...](https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/emergencies/keep-your-food-safe-during-emergencies)<br>[T1: FDA, Food and Water Safety During Power Outages and Floods](https://www.fda.gov/food/buy-store-serve-safe-food/food-and-water-safety-during-power-outages-and-floods)<br>[T1: Ready.gov / FEMA, Power Outages](https://www.ready.gov/power-outages)<br>[T1: CDC, What to Do to Protect Yourself During a Power Outage](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html) | &#9744; ok<br>&#9744; flag |
| 7 | "Full freezer: about 48 hours. Half-full freezer: about 24 hours" | [food-safety-during-outages.md](../substrate/09_urban_survival/entries/food-safety-during-outages.md), line 112 | [T1: USDA Food Safety and Inspection Service, Keep Your Food Safe During Emergencies: Power Outages,...](https://www.fsis.usda.gov/food-safety/safe-food-handling-and-preparation/emergencies/keep-your-food-safe-during-emergencies)<br>[T1: FDA, Food and Water Safety During Power Outages and Floods](https://www.fda.gov/food/buy-store-serve-safe-food/food-and-water-safety-during-power-outages-and-floods)<br>[T1: Ready.gov / FEMA, Power Outages](https://www.ready.gov/power-outages)<br>[T1: CDC, What to Do to Protect Yourself During a Power Outage](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html) | &#9744; ok<br>&#9744; flag |
| 8 | "Thermometer shows food at 40 F or higher for 2 hours or more: throw it out" | [food-safety-during-outages.md](../substrate/09_urban_survival/entries/food-safety-during-outages.md), line 114 | [T1: Ready.gov / FEMA, Power Outages](https://www.ready.gov/power-outages) | &#9744; ok<br>&#9744; flag |
| 9 | "Heat stroke can push body temperature to 106 F or higher within 10 to 15 minutes" | [extreme-heat-at-home.md](../substrate/09_urban_survival/entries/extreme-heat-at-home.md), line 76 | [T1: CDC / NIOSH, Heat-related Illnesses](https://www.cdc.gov/niosh/heat-stress/about/illnesses.html) | &#9744; ok<br>&#9744; flag |
| 10 | "Give nothing by mouth" | [extreme-heat-at-home.md](../substrate/09_urban_survival/entries/extreme-heat-at-home.md), line 76 | [T1: National Weather Service, Heat Illness (Heat Cramps, Exhaustion, Stroke)](https://www.weather.gov/safety/heat-illness) | &#9744; ok<br>&#9744; flag |
| 11 | "Hypothermia is a body temperature below 95 F, and it needs medical attention immediately" | [winter-storm-at-home.md](../substrate/09_urban_survival/entries/winter-storm-at-home.md), line 96 | [T1: CDC, Preventing Hypothermia](https://www.cdc.gov/winter-weather/prevention/index.html)<br>[T1: National Weather Service, During Extremely Cold Weather](https://www.weather.gov/safety/cold-during) | &#9744; ok<br>&#9744; flag |
| 12 | "For older adults, a home at 68 to 70 F or warmer is the aim, and even 60 to 65 F can lead to hypothermia" | [winter-storm-at-home.md](../substrate/09_urban_survival/entries/winter-storm-at-home.md), line 110 | [T1: National Institute on Aging / NIH, Hypothermia: A cold weather hazard](https://www.nia.nih.gov/news/hypothermia-cold-weather-hazard) | &#9744; ok<br>&#9744; flag |
| 13 | "Wash with soap and clean running water for at least 20 seconds" | [sanitation-and-human-waste.md](../substrate/09_urban_survival/entries/sanitation-and-human-waste.md), line 94 | [CDC, Guidelines for Personal Hygiene During an Emergency](https://www.cdc.gov/water-emergency/safety/guidelines-for-personal-hygiene-during-an-emergency.html)<br>[CDC, Drinking Water Advisories: An Overview](https://www.cdc.gov/water-emergency/about/drinking-water-advisories-an-overview.html)<br>[CDC, Food Poisoning Symptoms](https://www.cdc.gov/food-safety/signs-symptoms/index.html) | &#9744; ok<br>&#9744; flag |
| 14 | "use an alcohol-based hand sanitizer with at least 60% alcohol" | [sanitation-and-human-waste.md](../substrate/09_urban_survival/entries/sanitation-and-human-waste.md), line 95 | [CDC, Guidelines for Personal Hygiene During an Emergency](https://www.cdc.gov/water-emergency/safety/guidelines-for-personal-hygiene-during-an-emergency.html)<br>[CDC, Drinking Water Advisories: An Overview](https://www.cdc.gov/water-emergency/about/drinking-water-advisories-an-overview.html)<br>[CDC, Food Poisoning Symptoms](https://www.cdc.gov/food-safety/signs-symptoms/index.html) | &#9744; ok<br>&#9744; flag |
| 15 | "not to bury it within 100 feet of a water source" | [sanitation-and-human-waste.md](../substrate/09_urban_survival/entries/sanitation-and-human-waste.md), line 89 | [Oregon State University Extension, Survival Basics: Sanitation and Waste Management (EM 9334)](https://extension.oregonstate.edu/catalog/pub/em9334-s) | &#9744; ok<br>&#9744; flag |
| 16 | "Vials and cartridges, opened or unopened, can stay unrefrigerated at 59 to 86 F for up to 28 days and keep working" | [09\_urban\_survival.md](../09_urban_survival.md), line 218 | [Information Regarding Insulin Storage and Switching Between Products in an Emergency. FDA](https://www.fda.gov/drugs/emergency-preparedness-drugs/information-regarding-insulin-storage-and-switching-between-products-emergency) | &#9744; ok<br>&#9744; flag |
| 17 | "Do not throw out a life-sustaining medicine (insulin, transplant drugs, etc.) until you have called a pharmacist or clinician." | [09\_urban\_survival.md](../09_urban_survival.md), line 216 | [Power Outages. Ready.gov / FEMA](https://www.ready.gov/power-outages)<br>[Winter Weather. Ready.gov / FEMA](https://www.ready.gov/winter-weather)<br>[Extreme Heat. Ready.gov / FEMA](https://www.ready.gov/heat) | &#9744; ok<br>&#9744; flag |

## 3. CONVENTIONS section 10 checklist

Section 10 has no checklist written for urban survival. This is the nearest match, because the domain is built from CDC, FEMA, FDA, CPSC and Red Cross medical and home-safety guidance (Tier 1). Apply the first-aid boxes to the heat, cold and carbon monoxide entries and the water box to the water content.

### First-aid & water
- [ ] First-aid covers wound infection, hypo/hyperthermia, dehydration/diarrhea, med-continuity;
      each has RED FLAGS / EVAC + DO NOT.
- [ ] Every water entry has the `⚠ CONTAMINATION` block with boil time, micron limit, and the
      chemical-vs-biological boundary.
- [ ] All medical/water claims verified vs. CDC / Red Cross / EPA / extension (T1).

## 4. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Warmed insulin: the repo says do not throw it out and do not decide alone

FDA says warmed insulin may still be needed in an emergency. The repo's rule is to not discard it and not decide alone: call a pharmacist or prescriber, then 911 or an emergency department if neither can be reached. A pass-2 round asked to drop the FDA note. It was kept because discarding someone's only insulin can kill. Decide whether this wording is right. It appears in four places, and they must stay in step.

> If a life depends on a refrigerated drug that has already warmed, do not decide alone whether to use it: contact a pharmacist, healthcare provider or the drug's manufacturer now [45], and if you cannot reach one, call 911 or go to an emergency department (this guide's rule).
>
> From [09_urban_survival.md](../09_urban_survival.md), line 216.

> They do not throw it out and do not decide alone: FDA notes that warmed insulin may still be needed in an emergency [26], so they call a pharmacist or the prescriber now [26][45], and would call 911 or go to an emergency department if they could not reach one (this guide's rule).
>
> From [09_urban_survival.md](../09_urban_survival.md), line 249.

> Life-sustaining refrigerated medicine (insulin, for example) that has warmed: do not decide alone. Call a pharmacist or your prescriber now [7].
>
> From [food-safety-during-outages.md](../substrate/09_urban_survival/entries/food-safety-during-outages.md), line 180.

The fourth place is [chronic-med-continuity.md](../substrate/06_first_aid/entries/chronic-med-continuity.md), quoted in [domain 01](01_first_aid.md).

### Safe room temperature for older adults

The 68 to 70 F figure rests on a National Institute on Aging page that blocks automated reading, so the pass-2 checkers could not open it. Check it against the live page.

> For older adults, a home at 68 to 70 F or warmer is the aim, and even 60 to 65 F can lead to hypothermia [9].
>
> From [winter-storm-at-home.md](../substrate/09_urban_survival/entries/winter-storm-at-home.md), line 109.

### The 90 F cool-room rule is the repo's own

The entry labels this threshold as its own rule, not a quoted source. Decide whether it is a reasonable, cautious line for when to leave.

> You cannot reach a cool room below 90 F (this entry's rule, the safer choice).
>
> From [extreme-heat-at-home.md](../substrate/09_urban_survival/entries/extreme-heat-at-home.md), line 113.

### No unvented fuel-burning heater indoors, no exceptions

An earlier draft allowed some portable heaters under conditions. The rule is now absolute. Decide whether the absolute rule is correct for this audience.

> The rule: nothing burns inside a tent, vehicle, garage, snow shelter or home, except a vented fireplace or stove in working order.
>
> From [generator-and-heater-co-prevention.md](../substrate/09_urban_survival/entries/generator-and-heater-co-prevention.md), line 81.

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
