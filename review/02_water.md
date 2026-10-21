# Safety read 02: Water

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 2 of 13. Water comes second: boil times, filter sizes and chemical doses are numbers a reader will follow exactly.

## Time and status

- **Estimated time: 40 minutes at most** for the targeted check below (16 claims at about 2 minutes each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 14,276 words, roughly 55 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain substrate/02_water --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

| Entry | Type | Severity | Tier | Status now | Words |
|---|---|---|---|---|---|
| [Boil Disinfection (Rolling Boil)](../substrate/02_water/entries/boil-disinfection.md) | METHOD | n/a | T1 | agent-verified | 1274 |
| [Chemical Disinfection (Chlorine & Iodine)](../substrate/02_water/entries/chemical-treatment-chlorine-iodine.md) | METHOD | n/a | T1 | agent-verified | 1727 |
| [Filtration by Micron Rating](../substrate/02_water/entries/filtration-micron-guide.md) | METHOD | n/a | T1 | agent-verified | 1331 |
| [Floodwater and Chemical Contamination: When No Home Method Works](../substrate/02_water/entries/floodwater-and-chemical-contamination.md) | METHOD | high | T1 | agent-verified | 2842 |
| [Settling, Decanting and Pre-Filtering Cloudy Water](../substrate/02_water/entries/pretreatment-settling-and-prefiltering.md) | METHOD | moderate | T1 | agent-verified | 1621 |
| [Solar SODIS (UV-A Inactivation)](../substrate/02_water/entries/solar-sodis.md) | METHOD | n/a | T1 | agent-verified | 1351 |
| [Portable UV Pens and Lamps](../substrate/02_water/entries/uv-treatment.md) | METHOD | high | T1 | agent-verified | 1918 |
| [Water Sourcing & Storage](../substrate/02_water/entries/water-sourcing-and-storage.md) | METHOD | n/a | T1 | agent-verified | 2212 |

## 2. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "rolling boil 1 minute (CDC: 3 minutes above 6,500 ft / 2,000 m; EPA: 3 minutes above 5,000 ft / about 1,500 m; if unsure of your elevation, boil 3 minutes)" | [boil-disinfection.md](../substrate/02_water/entries/boil-disinfection.md), line 56 | [CDC, How to Make Water Safe in an Emergency](https://www.cdc.gov/water-emergency/about/index.html)<br>[EPA, Emergency Disinfection of Drinking Water](https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water) | &#9744; ok<br>&#9744; flag |
| 2 | "Boiling does not remove chemicals. It can raise the level of nitrate and algal toxins" | [boil-disinfection.md](../substrate/02_water/entries/boil-disinfection.md), line 97 | [CDC, How to Make Water Safe in an Emergency](https://www.cdc.gov/water-emergency/about/index.html)<br>[California State Water Resources Control Board, Drinking Water Resource Guide (nitrate Q&A)](https://www.waterboards.ca.gov/water_issues/programs/hr2w/docs/general/dw_resource_guide.pdf) | &#9744; ok<br>&#9744; flag |
| 3 | "bleach, chlorine tablets and iodine do not kill it (CDC). It tolerates chlorine and can live more than 7 days in chlorinated water (CDC)" | [chemical-treatment-chlorine-iodine.md](../substrate/02_water/entries/chemical-treatment-chlorine-iodine.md), line 58 | [CDC, About Water Treatment Options When Hiking, Camping, or Traveling](https://www.cdc.gov/drinking-water/prevention/water-treatment-hiking-camping-traveling.html)<br>[CDC, Preventing and Controlling Crypto at Camps](https://www.cdc.gov/cryptosporidium/prevention/preventing-and-controlling-crypto-at-camps.html) | &#9744; ok<br>&#9744; flag |
| 4 | "with 6% or 8.25% sodium hypochlorite on the label (CDC's table covers 5–9%)" | [chemical-treatment-chlorine-iodine.md](../substrate/02_water/entries/chemical-treatment-chlorine-iodine.md), line 70 | [CDC, How to Make Water Safe in an Emergency](https://www.cdc.gov/water-emergency/about/index.html) | &#9744; ok<br>&#9744; flag |
| 5 | "CDC uses 2 drops per quart or liter, 8 drops per gallon, 40 drops per 5 gallons" | [chemical-treatment-chlorine-iodine.md](../substrate/02_water/entries/chemical-treatment-chlorine-iodine.md), line 84 | [CDC, How to Make Water Safe in an Emergency](https://www.cdc.gov/water-emergency/about/index.html) | &#9744; ok<br>&#9744; flag |
| 6 | "For 6% bleach that is 16 drops per gallon. EPA and CDC both say to double the bleach if the water is cloudy, colored or very cold" | [pretreatment-settling-and-prefiltering.md](../substrate/02_water/entries/pretreatment-settling-and-prefiltering.md), line 86 | [T1: CDC, How to Make Water Safe in an Emergency](https://www.cdc.gov/water-emergency/about/index.html)<br>[T1: EPA, Emergency Disinfection of Drinking Water](https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water) | &#9744; ok<br>&#9744; flag |
| 7 | "A faint chlorine smell afterward is the check. No smell: add the same dose again and wait 15 more minutes" | [pretreatment-settling-and-prefiltering.md](../substrate/02_water/entries/pretreatment-settling-and-prefiltering.md), line 87 | [T1: EPA, Emergency Disinfection of Drinking Water](https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water) | &#9744; ok<br>&#9744; flag |
| 8 | "absolute 0.3 µm or smaller (CDC). A 1 µm absolute filter does not reliably remove bacteria" | [filtration-micron-guide.md](../substrate/02_water/entries/filtration-micron-guide.md), line 89 | [CDC, About Water Treatment Options When Hiking, Camping, or Traveling](https://www.cdc.gov/drinking-water/prevention/water-treatment-hiking-camping-traveling.html) | &#9744; ok<br>&#9744; flag |
| 9 | "only an ultrafilter (pores finer than about 0.01 µm) or reverse osmosis removes them (WMS 2024)" | [filtration-micron-guide.md](../substrate/02_water/entries/filtration-micron-guide.md), line 57 | [Wilderness Medical Society / Wilderness & Environmental Medicine (CDC Stacks copy), Wilderness Medi...](https://stacks.cdc.gov/view/cdc/153527/cdc_153527_DS1.pdf) | &#9744; ok<br>&#9744; flag |
| 10 | "Do not force it. As a filter clogs it needs more pressure, and extra pressure can push germs through or damage it (WMS 2024)" | [filtration-micron-guide.md](../substrate/02_water/entries/filtration-micron-guide.md), line 76 | [Wilderness Medical Society / Wilderness & Environmental Medicine (CDC Stacks copy), Wilderness Medi...](https://stacks.cdc.gov/view/cdc/153527/cdc_153527_DS1.pdf) | &#9744; ok<br>&#9744; flag |
| 11 | "6 hours in sun, or 2 consecutive days if the sky is cloudy (WHO; CDC; Eawag). SODIS does not work satisfactorily in lengthy rain (Eawag)" | [solar-sodis.md](../substrate/02_water/entries/solar-sodis.md), line 61 | [World Health Organization, Household Water Treatment and Safe Storage Following Emergencies and Dis...](https://www.who.int/docs/default-source/wash-documents/wash-in-emergencies/household-water-treatment-and-safe-storage-after-emergencies.pdf)<br>[CDC, How to Make Water Safe in an Emergency](https://www.cdc.gov/water-emergency/about/index.html)<br>[Eawag (Swiss Federal Institute of Aquatic Science and Technology), SODIS, SODIS: How does it work?](https://www.sodis.ch/methode/anwendung/index_EN.html) | &#9744; ok<br>&#9744; flag |
| 12 | "(smaller bottles work better; Eawag's stated ceiling is 3 liters)" | [solar-sodis.md](../substrate/02_water/entries/solar-sodis.md), line 68 | [Eawag (Swiss Federal Institute of Aquatic Science and Technology), SODIS, SODIS: How does it work?](https://www.sodis.ch/methode/anwendung/index_EN.html) | &#9744; ok<br>&#9744; flag |
| 13 | "UV-C can injure skin and eyes after a few seconds of exposure" | [uv-treatment.md](../substrate/02_water/entries/uv-treatment.md), line 84 | [T1: FDA, Do Not Use Ultraviolet (UV) Wands That Give Off Unsafe Levels of Radiation: FDA Safety Com...](https://www.fda.gov/medical-devices/safety-communications/do-not-use-ultraviolet-uv-wands-give-unsafe-levels-radiation-fda-safety-communication) | &#9744; ok<br>&#9744; flag |
| 14 | "CDC says not to use water or ice from refrigerator or freezer dispensers during any drinking water advisory" | [floodwater-and-chemical-contamination.md](../substrate/02_water/entries/floodwater-and-chemical-contamination.md), line 130 | [T1: CDC, Drinking Water Advisories: An Overview](https://www.cdc.gov/water-emergency/about/drinking-water-advisories-an-overview.html) | &#9744; ok<br>&#9744; flag |
| 15 | "Call the fire department, police or your state fire marshal" | [floodwater-and-chemical-contamination.md](../substrate/02_water/entries/floodwater-and-chemical-contamination.md), line 125 | [T1: CDC, Safety Guidelines: Floodwater](https://www.cdc.gov/floods/safety/floodwater-after-a-disaster-or-emergency-safety.html) | &#9744; ok<br>&#9744; flag |
| 16 | "Never the bowl. Only if the tank water is clear and has no colored or chemical toilet cleaner in it, and treat it before drinking (CDC; OSU Extension)." | [water-sourcing-and-storage.md](../substrate/02_water/entries/water-sourcing-and-storage.md), line 95 | [CDC, How to Find Clean Water in an Emergency](https://www.cdc.gov/water-emergency/about/how-to-find-clean-water-in-an-emergency.html)<br>[CDC, How to Create an Emergency Water Supply](https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html)<br>[CDC, How to Make Water Safe in an Emergency](https://www.cdc.gov/water-emergency/about/index.html) | &#9744; ok<br>&#9744; flag |

## 3. CONVENTIONS section 10 checklist

Copied from CONVENTIONS.md section 10. For water, the boxes that matter are the second (every entry carries the CONTAMINATION block with boil time, micron limit and the chemical-versus-biological boundary) and the third (medical and water claims against CDC, Red Cross, EPA or extension).

### First-aid & water
- [ ] First-aid covers wound infection, hypo/hyperthermia, dehydration/diarrhea, med-continuity;
      each has RED FLAGS / EVAC + DO NOT.
- [ ] Every water entry has the `⚠ CONTAMINATION` block with boil time, micron limit, and the
      chemical-vs-biological boundary.
- [ ] All medical/water claims verified vs. CDC / Red Cross / EPA / extension (T1).

## 4. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Boil time at altitude: CDC and EPA draw the line in different places

CDC says 3 minutes above 6,500 ft. EPA says 3 minutes above 5,000 ft. The repo uses 3 minutes above 5,000 ft or whenever the reader is unsure, which is the more cautious line. Decide whether that is the right rule for a lay reader.

> Which elevation rule: CDC says 3 minutes above 6,500 ft (2,000 m). EPA sets the line lower, at 5,000 ft (about 1,500 m).
>
> From [boil-disinfection.md](../substrate/02_water/entries/boil-disinfection.md), line 62.

### Cryptosporidium: chemical treatment and sunlight cannot be relied on

The repo says bleach, tablets, iodine and SODIS do not reliably handle Cryptosporidium, and sends the reader to boiling or an absolute 1 micron filter. Check this against CDC and decide whether the warning is prominent enough in every method entry.

> bleach, chlorine tablets and iodine do not kill it (CDC)
>
> From [chemical-treatment-chlorine-iodine.md](../substrate/02_water/entries/chemical-treatment-chlorine-iodine.md), line 57.

### Toilet tank water as a last resort

The entry allows it under conditions and notes that some agencies advise against drinking it at all. Decide whether a last-resort allowance belongs in a public reference.

> Some agencies advise against drinking it at all
>
> From [water-sourcing-and-storage.md](../substrate/02_water/entries/water-sourcing-and-storage.md), line 94.

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
