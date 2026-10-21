# Safety read 12: Navigation, communication, key resources, gear and core principles

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 12 of 13. These five folders come twelfth because they carry the fewest ways to hurt someone. The exceptions are flood crossings, compass arithmetic, the poison line number and the tourniquet kit.

## Time and status

- **Estimated time: 50 minutes at most** for the targeted check below (19 claims at about 2 minutes each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 46,560 words, roughly 185 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain substrate/07_navigation --reviewer "Your Full Name"
python scripts/mark_reviewed.py --domain substrate/08_communication --reviewer "Your Full Name"
python scripts/mark_reviewed.py --domain substrate/10_key_resources --reviewer "Your Full Name"
python scripts/mark_reviewed.py --domain substrate/11_gear --reviewer "Your Full Name"
python scripts/mark_reviewed.py --domain substrate/01_core_principles --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

Five folders, five commands. Run each only for a folder whose entries you read. If you read only some of the five, run only those.

| Entry | Type | Severity | Tier | Status now | Words |
|---|---|---|---|---|---|
| [Celestial Navigation (Finding Direction Without Instruments)](../substrate/07_navigation/entries/celestial-navigation.md) | METHOD | low | T2 | agent-verified | 1821 |
| [Compass and Declination (Take, Follow and Correct a Bearing)](../substrate/07_navigation/entries/compass-and-declination.md) | METHOD | low | T1 | agent-verified | 2724 |
| [Dead Reckoning and Pace Counting (Hold a Bearing and Estimate Distance)](../substrate/07_navigation/entries/dead-reckoning-and-pace.md) | METHOD | low | T2 | agent-verified | 2218 |
| [River and Stream Crossing (When Not To, and How If You Must)](../substrate/07_navigation/entries/river-and-stream-crossing.md) | METHOD | lethal | T1 | agent-verified | 2259 |
| [Terrain and Map Reading (Navigate Using Contours and Features)](../substrate/07_navigation/entries/terrain-and-map-reading.md) | METHOD | low | T2 | agent-verified | 2259 |
| [Emergency Alerts and NOAA Weather Radio](../substrate/08_communication/entries/emergency-alerts-and-noaa-weather-radio.md) | METHOD | low | T1 | agent-verified | 2831 |
| [Family Communication Plan](../substrate/08_communication/entries/family-communication-plan.md) | METHOD | low | T1 | agent-verified | 1870 |
| [Mesh and Emergency Comms](../substrate/08_communication/entries/mesh-and-emergency-comms.md) | METHOD | n/a | T1 | agent-verified | 1183 |
| [Radio Basics and Bands](../substrate/08_communication/entries/radio-basics-and-bands.md) | METHOD | n/a | T1 | agent-verified | 2656 |
| [Signaling—Visual and Audible](../substrate/08_communication/entries/signaling-visual-and-audible.md) | METHOD | n/a | T1 | agent-verified | 1705 |
| [Official Emergency Information Sources (Where Warnings and Facts Come From)](../substrate/10_key_resources/entries/official-emergency-information-sources.md) | METHOD | none | T1 | agent-verified | 2399 |
| [Physical Book Backup Layer — No-Power Reference](../substrate/10_key_resources/entries/physical-book-backup-layer.md) | METHOD | n/a | T2 | agent-verified | 1389 |
| [Public-Domain ID Image Sources — Where Real Deadly-Pair Photos Come From](../substrate/10_key_resources/entries/public-domain-id-image-sources.md) | METHOD | n/a | T1 | agent-verified | 1779 |
| [Skills to Practice Now — Build Muscle Memory Before an Emergency](../substrate/10_key_resources/entries/skills-to-practice-now.md) | METHOD | n/a | T3 | agent-verified | 2299 |
| [Bug-Out Tier 2 Kit — 72-Hour Grab-and-Go](../substrate/11_gear/entries/bug-out-tier2-kit.md) | KIT-GEAR | low | T1 | agent-verified | 1946 |
| [EDC Tier 1 Kit — Everyday Carry](../substrate/11_gear/entries/edc-tier1-kit.md) | KIT-GEAR | low | T1 | agent-verified | 1289 |
| [Home Stockpile Tier 3 — Shelter-in-Place, 2-Week Supply](../substrate/11_gear/entries/home-stockpile-tier3.md) | KIT-GEAR | moderate | T1 | agent-verified | 2371 |
| [Individual First Aid Kit](../substrate/11_gear/entries/individual-first-aid-kit.md) | KIT-GEAR | moderate | T1 | agent-verified | 2177 |
| [Vehicle Emergency Kit](../substrate/11_gear/entries/vehicle-kit.md) | KIT-GEAR | moderate | T1 | agent-verified | 2213 |
| [Group Survival and Roles](../substrate/01_core_principles/entries/group-survival-and-roles.md) | PRINCIPLE | low | T2 | agent-verified | 1774 |
| [Psychology & Will to Live — Fear, Stress, and Not Giving Up](../substrate/01_core_principles/entries/psychology-and-will-to-live.md) | PRINCIPLE | n/a | T2 | agent-verified | 1039 |
| [The Rule of Threes](../substrate/01_core_principles/entries/rule-of-threes.md) | PRINCIPLE | n/a | T2 | agent-verified | 1164 |
| [Stay or Go — When to Stay Put and When to Move](../substrate/01_core_principles/entries/stay-or-go-decision.md) | PRINCIPLE | high | T1 | agent-verified | 2107 |
| [STOP — The Decision Circuit-Breaker](../substrate/01_core_principles/entries/survival-priorities-stop.md) | PRINCIPLE | n/a | T2 | agent-verified | 1088 |

## 2. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "NOAA: to get a true bearing from a magnetic one, add the declination, entering west values as negative. NOAA's example is 10 degrees west written as -10" | [compass-and-declination.md](../substrate/07_navigation/entries/compass-and-declination.md), line 116 | [T1: NOAA National Centers for Environmental Information, Magnetic Declination (definition; positive...](https://www.ncei.noaa.gov/products/magnetic-declination) | &#9744; ok<br>&#9744; flag |
| 2 | "With west declination the compass number comes out larger than the map number. With east declination it comes out smaller." | [compass-and-declination.md](../substrate/07_navigation/entries/compass-and-declination.md), line 121 | [NOAA National Centers for Environmental Information, Magnetic Declination (definition; positive eas...](https://www.ncei.noaa.gov/products/magnetic-declination)<br>[NOAA National Centers for Environmental Information, Geomagnetism Frequently Asked Questions (local...](https://www.ncei.noaa.gov/products/geomagnetism-frequently-asked-questions)<br>[NOAA National Centers for Environmental Information, World Magnetic Model (WMM2025 valid to Decembe...](https://www.ncei.noaa.gov/products/world-magnetic-model) | &#9744; ok<br>&#9744; flag |
| 3 | "6 inches of fast-moving flood water can knock an adult off their feet" | [river-and-stream-crossing.md](../substrate/07_navigation/entries/river-and-stream-crossing.md), line 84 | [T1: National Weather Service, Flood Safety: During a Flood (Turn Around, Don't Drown; 6 inches; 12...](https://www.weather.gov/safety/flood-during)<br>[T1: National Weather Service, Turn Around Don't Drown (depths of moving water; never safe to walk o...](https://www.weather.gov/safety/flood-turn-around-dont-drown) | &#9744; ok<br>&#9744; flag |
| 4 | "12 inches of water can float a car or small SUV" | [river-and-stream-crossing.md](../substrate/07_navigation/entries/river-and-stream-crossing.md), line 92 | [T1: National Weather Service, Flood Safety: During a Flood (Turn Around, Don't Drown; 6 inches; 12...](https://www.weather.gov/safety/flood-during) | &#9744; ok<br>&#9744; flag |
| 5 | "The Forest Service says not to attempt to cross flowing streams in a flood" | [river-and-stream-crossing.md](../substrate/07_navigation/entries/river-and-stream-crossing.md), line 80 | [T1: USDA Forest Service, Floods (flash floods, do not cross flowing streams, rain upstream)](https://www.fs.usda.gov/visit/know-before-you-go/floods) | &#9744; ok<br>&#9744; flag |
| 6 | "A mesh network cannot reach 911. It has no connection to a 911 call center or the phone network (this guide's judgment, from \[4\])." | [mesh-and-emergency-comms.md](../substrate/08_communication/entries/mesh-and-emergency-comms.md), line 44 | [T3: Meshtastic project, Meshtastic overview (community project documentation, not a government sour...](https://meshtastic.org/docs/overview/) | &#9744; ok<br>&#9744; flag |
| 7 | "Texts may get through when calls do not, and you do not tie up lines emergency workers need" | [family-communication-plan.md](../substrate/08_communication/entries/family-communication-plan.md), line 117 | [T1: FEMA / Ready.gov, Family Communication Plan (Ready Campaign brochure; copy hosted by NJ Office...](https://www.nj.gov/njoem/plan-prepare/pdf/FEMA_family_communication_plan.pdf)<br>[T1: Ready.gov / FEMA, Make a Plan (Ready Kids)](https://www.ready.gov/kids/make-a-plan) | &#9744; ok<br>&#9744; flag |
| 8 | "three fires in a triangle are recognized as distress" | [signaling-visual-and-audible.md](../substrate/08_communication/entries/signaling-visual-and-audible.md), line 74 | [T1: FAA Civil Aerospace Medical Institute, Basic Survival Skills for Aviation (OK-06-033), Signalin...](https://www.faa.gov/pilots/training/airman_education/media/CAMISurvivalManual.pdf) | &#9744; ok<br>&#9744; flag |
| 9 | "do not flash rapidly, because a pilot may mistake it for hostile fire. Do not hold the beam on the cockpit for more than a few seconds, because it may blind the pilot." | [signaling-visual-and-audible.md](../substrate/08_communication/entries/signaling-visual-and-audible.md), line 84 | [T2: U.S. Department of the Army (reprint hosted by San Jose State University), FM 21-76, Survival,...](https://www.sjsu.edu/people/michelle.hager/docs/fm_21-76_us_army_survival_manual_2006.pdf) | &#9744; ok<br>&#9744; flag |
| 10 | "Do not use GMRS or amateur frequencies on your own authority." | [radio-basics-and-bands.md](../substrate/08_communication/entries/radio-basics-and-bands.md), line 209 | [T1: Federal Communications Commission (eCFR), 47 CFR 95.1705, GMRS individual licenses; who may ope...](https://www.ecfr.gov/current/title-47/part-95/section-95.1705) | &#9744; ok<br>&#9744; flag |
| 11 | "Do not move at all until you have a specific reason to take a step" | [stay-or-go-decision.md](../substrate/01_core_principles/entries/stay-or-go-decision.md), line 82 | [T1: USDA Forest Service, If You Get Lost](https://www.fs.usda.gov/visit/know-before-you-go/if-you-get-lost)<br>[T2: U.S. Department of the Army, FM 21-76, Survival (Pattern for Survival). Opened as an unofficial...](https://www.sjsu.edu/people/michelle.hager/docs/fm_21-76_us_army_survival_manual_2006.pdf) | &#9744; ok<br>&#9744; flag |
| 12 | "The Forest Service calls following a drainage or stream downhill "a very last resort," and adds "this could be very dangerous"" | [stay-or-go-decision.md](../substrate/01_core_principles/entries/stay-or-go-decision.md), line 100 | [T1: USDA Forest Service, If You Get Lost](https://www.fs.usda.gov/visit/know-before-you-go/if-you-get-lost) | &#9744; ok<br>&#9744; flag |
| 13 | "If someone complains of tiredness or wanders away from the group, he may be a heat casualty" | [group-survival-and-roles.md](../substrate/01_core_principles/entries/group-survival-and-roles.md), line 81 | [T2: U.S. Department of the Army, FM 21-76, Survival (buddy system for heat injury and frostbite; hy...](https://www.sjsu.edu/people/michelle.hager/docs/fm_21-76_us_army_survival_manual_2006.pdf)<br>[T1: Olympic National Park, National Park Service, Wilderness Safety](https://www.nps.gov/olym/planyourvisit/wilderness-safety.htm) | &#9744; ok<br>&#9744; flag |
| 14 | "In its common form it says a person can last about 3 minutes without air, 3 hours without shelter in harsh conditions, 3 days without water, and 3 weeks without food" | [rule-of-threes.md](../substrate/01_core_principles/entries/rule-of-threes.md), line 55 | [FAA Civil Aerospace Medical Institute, Basic Survival Skills for Aviation (OK-06-033), including AC...](https://www.faa.gov/pilots/training/airman_education/media/CAMISurvivalManual.pdf)<br>[U.S. Department of the Army, FM 21-76, Survival (Pattern for Survival; Shelters; Food). Opened as a...](https://www.sjsu.edu/people/michelle.hager/docs/fm_21-76_us_army_survival_manual_2006.pdf)<br>[Centers for Disease Control and Prevention, High-Altitude Travel and Altitude Illness (CDC Yellow B...](https://www.cdc.gov/yellow-book/hcp/environmental-hazards-risks/high-altitude-travel-and-altitude-illness.html) | &#9744; ok<br>&#9744; flag |
| 15 | "1-800-222-1222 (America's Poison Centers), free, 24 hours a day" | [official-emergency-information-sources.md](../substrate/10_key_resources/entries/official-emergency-information-sources.md), line 96 | [T1: America's Poison Centers, Poison Help (1-800-222-1222) and America's Poison Centers](https://www.poisonhelp.org/) | &#9744; ok<br>&#9744; flag |
| 16 | "do not give aspirin to anyone just because it is in the kit, and never to a child unless their provider says to" | [individual-first-aid-kit.md](../substrate/11_gear/entries/individual-first-aid-kit.md), line 105 | [T1: NIH MedlinePlus, Reye syndrome](https://medlineplus.gov/ency/article/001565.htm) | &#9744; ok<br>&#9744; flag |
| 17 | "Placement is at least 2 to 3 inches from the wound, between the wound and the heart, never over a joint" | [edc-tier1-kit.md](../substrate/11_gear/entries/edc-tier1-kit.md), line 104 | [T1: U.S. Department of Homeland Security, Stop the Bleed: Applying a Tourniquet (2018)](https://www.dhs.gov/sites/default/files/publications/STB_Applying_Tourniquet_08-06-2018_0.pdf) | &#9744; ok<br>&#9744; flag |
| 18 | "Run the engine only in short runs, about 10 minutes each hour, with one window cracked \[4\]\[6\]. A clear pipe and a cracked window lower the risk. They do not remove it" | [vehicle-kit.md](../substrate/11_gear/entries/vehicle-kit.md), line 101 | [T1: National Weather Service, Winter Storms: During](https://www.weather.gov/safety/winter-during)<br>[T1: CDC, Safety Guidelines: During and After a Winter Storm](https://www.cdc.gov/winter-weather/safety/stay-safe-during-after-a-winter-storm-safety.html) | &#9744; ok<br>&#9744; flag |
| 19 | "Never reuse containers that held bleach, pesticides or other toxic chemicals" | [home-stockpile-tier3.md](../substrate/11_gear/entries/home-stockpile-tier3.md), line 99 | [T1: CDC, How to Create an Emergency Water Supply](https://www.cdc.gov/water-emergency/about/how-to-create-and-store-an-emergency-water-supply.html) | &#9744; ok<br>&#9744; flag |

## 3. CONVENTIONS section 10 checklist

CONVENTIONS.md section 10 has no safety checklist written for these folders. The repo-wide coherence list below is the only one that applies. The first two boxes are maintainer checks (a script runs them). The rest is your claims table: check each against its source.

### Coherence (all domains)
- [ ] Manifests pass `check_manifests` (no dangling/missing rows; required columns filled).
- [ ] Survey files link down; food resolves via `regional/_index.md` registry → `food_hub.md`; no
      broken intra-repo links.
- [ ] `grep -rn "danger_class" .` = 0; no `safe` token on biology facets.

## 4. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### The rule of threes: 3 weeks without food, or 30 days

The entry gives the common form (3 weeks) and the FAA's form (30 days) side by side, and calls the rule a teaching heuristic, not a measurement. Decide whether stating both is clearer or more confusing.

> The rule of threes is a teaching heuristic, a memory aid for setting priorities. It is not a measurement, and there is no exact physiology behind it.
>
> From [rule-of-threes.md](../substrate/01_core_principles/entries/rule-of-threes.md), line 54.

### Vehicle kit: engine in short runs, but never sleep with it running

The same tension as in [domain 07](07_fire_shelter.md). The kit entry repeats both lines.

> Never sleep with the engine running. People who are asleep can die before they notice symptoms [8].
>
> From [vehicle-kit.md](../substrate/11_gear/entries/vehicle-kit.md), line 101.

### Tourniquet placement wording differs across the guide and two entries

See the same note in [domain 11](11_survey_guides.md). The EDC kit entry reads "at least 2 to 3 inches from the wound".

> Placement is at least 2 to 3 inches from the wound, between the wound and the heart, never over a joint
>
> From [edc-tier1-kit.md](../substrate/11_gear/entries/edc-tier1-kit.md), line 103.

### Radio entry tells readers not to transmit on services they are not licensed for

Check the entry's reading of 47 CFR 95.1705 and the amateur rules against the eCFR text. The entry's legal reading is the repo's own summary, and the FCC rules change.

> The only GMRS allowance is the licensee's permission in 95.1705(c)(3)
>
> From [radio-basics-and-bands.md](../substrate/08_communication/entries/radio-basics-and-bands.md), line 208.

### A mesh network cannot reach 911: the repo's judgment

The entry states this as its own judgment, drawn from a source. Decide whether the statement is safe to leave unqualified.

> A mesh network cannot reach 911.
>
> From [mesh-and-emergency-comms.md](../substrate/08_communication/entries/mesh-and-emergency-comms.md), line 43.

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
