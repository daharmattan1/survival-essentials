# Safety read 07: Fire and shelter

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 7 of 13. Fire and shelter come seventh: the highest-stakes line in both is carbon monoxide, and it is already covered in domains 01 and 03. The rest is fire safety and exposure.

## Time and status

- **Estimated time: 40 minutes at most** for the targeted check below (15 claims at about 2 minutes each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 26,834 words, roughly 105 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain substrate/03_fire --reviewer "Your Full Name"
python scripts/mark_reviewed.py --domain substrate/04_shelter --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

| Entry | Type | Severity | Tier | Status now | Words |
|---|---|---|---|---|---|
| [Extinguishing a Fire and Fire Safety](../substrate/03_fire/entries/extinguishing-and-fire-safety.md) | METHOD | high | T1 | agent-verified | 2646 |
| [Fire Lays and Structure](../substrate/03_fire/entries/fire-lays-and-structure.md) | METHOD | moderate | T2 | agent-verified | 2395 |
| [Ignition Methods — Reliability Hierarchy](../substrate/03_fire/entries/ignition-methods.md) | METHOD | moderate | T2 | agent-verified | 2785 |
| [Keeping a Fire Through the Night](../substrate/03_fire/entries/overnight-fire-maintenance.md) | METHOD | moderate | T1 | agent-verified | 2050 |
| [Tinder and Fuel Progression](../substrate/03_fire/entries/tinder-and-fuel-progression.md) | METHOD | low | T2 | agent-verified | 2211 |
| [Fire in Wet Weather](../substrate/03_fire/entries/wet-weather-fire.md) | METHOD | moderate | T1 | agent-verified | 2219 |
| [Cold-Weather Sleep System: Ground, Layers and Cover](../substrate/04_shelter/entries/cold-weather-sleep-system.md) | METHOD | moderate | T1 | agent-verified | 2240 |
| [Emergency Shelter Types & Configuration](../substrate/04_shelter/entries/emergency-shelter-types.md) | METHOD | moderate | T2 | agent-verified | 3059 |
| [Insulation & Ground Barrier (Heat Loss Prevention)](../substrate/04_shelter/entries/insulation-and-ground-barrier.md) | METHOD | low | T2 | agent-verified | 1241 |
| [Site Selection & Hazard Avoidance](../substrate/04_shelter/entries/site-selection-and-hazards.md) | METHOD | moderate | T2 | agent-verified | 1968 |
| [Tarp Configurations: Lean-To, A-Frame and Poncho Tent](../substrate/04_shelter/entries/tarp-configurations.md) | METHOD | low | T1 | agent-verified | 2045 |
| [Vehicle as Shelter: Stranded in a Car in Winter](../substrate/04_shelter/entries/vehicle-as-shelter.md) | METHOD | lethal | T1 | agent-verified | 1975 |

## 2. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "Nobody sleeps in an enclosed space (tent, vehicle, snow shelter, house) with any fire, stove, lantern, heater or charcoal burning in it." | [overnight-fire-maintenance.md](../substrate/03_fire/entries/overnight-fire-maintenance.md), line 87 | [T1: CDC, Carbon Monoxide Poisoning (About)](https://www.cdc.gov/carbon-monoxide/about/index.html)<br>[T1: CDC, Carbon Monoxide Poisoning Deaths Associated with Camping, Georgia, March 1999 (MMWR 48(32))](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm4832a1.htm)<br>[T1: U.S. Consumer Product Safety Commission, Portable Heaters and Camping Equipment (Carbon Monoxid...](https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center/Portable-Heaters--Camping-Equipment) | &#9744; ok<br>&#9744; flag |
| 2 | "Opening tent flaps, doors or windows is not enough to stop CO building up" | [overnight-fire-maintenance.md](../substrate/03_fire/entries/overnight-fire-maintenance.md), line 87 | [T1: CDC, Carbon Monoxide Poisoning Deaths Associated with Camping, Georgia, March 1999 (MMWR 48(32))](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm4832a1.htm) | &#9744; ok<br>&#9744; flag |
| 3 | "CPSC says never use fuel-burning portable heaters or lanterns while sleeping in tents, campers or vehicles, and the risk is higher at altitude" | [overnight-fire-maintenance.md](../substrate/03_fire/entries/overnight-fire-maintenance.md), line 87 | [T1: U.S. Consumer Product Safety Commission, Portable Heaters and Camping Equipment (Carbon Monoxid...](https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center/Portable-Heaters--Camping-Equipment) | &#9744; ok<br>&#9744; flag |
| 4 | "Do not bury your coals. They can smolder underground and possibly re-ignite" | [extinguishing-and-fire-safety.md](../substrate/03_fire/entries/extinguishing-and-fire-safety.md), line 167 | [T1: National Park Service, Campfire Safety, Big Thicket National Preserve](https://www.nps.gov/bith/planyourvisit/campfire-safety.htm)<br>[T1: USDA Forest Service, Campfire Tips (Sequoia National Forest, 2025)](https://fs.usda.gov/media/232572)<br>[T1: National Park Service, Campfires (last updated April 17, 2017)](https://www.nps.gov/articles/campfires.htm) | &#9744; ok<br>&#9744; flag |
| 5 | "Never take charcoal or hot coals into a tent, vehicle or house for warmth: the CDC found a charcoal grill inside a tent in a camping death, and CPSC says never use charcoal for heat in tents, campers, vans, cars, trucks or homes" | [extinguishing-and-fire-safety.md](../substrate/03_fire/entries/extinguishing-and-fire-safety.md), line 163 | [T1: CDC, Carbon Monoxide Poisoning Deaths Associated with Camping, Georgia, March 1999 (MMWR 48(32))](https://www.cdc.gov/mmwr/preview/mmwrhtml/mm4832a1.htm)<br>[T1: U.S. Consumer Product Safety Commission, Charcoal (Carbon Monoxide Information Center)](https://www.cpsc.gov/Safety-Education/Safety-Education-Centers/Carbon-Monoxide-Information-Center/Charcoal) | &#9744; ok<br>&#9744; flag |
| 6 | "At least 15 feet from tents, vegetation and low-hanging branches. Vertical clearance at least three times the flame height." | [extinguishing-and-fire-safety.md](../substrate/03_fire/entries/extinguishing-and-fire-safety.md), line 140 | [T1: Smokey Bear / USDA Forest Service, Campfire Safety](https://smokeybear.com/campfire-safety)<br>[T1: Smokey Bear / USDA Forest Service, How to maintain and extinguish your campfire](https://smokeybear.com/en/prevention-how-tos/campfire-safety/how-to-maintain-and-extinguish-your-campfire)<br>[T1: USDA Forest Service, Campfire Tips (Sequoia National Forest, 2025)](https://fs.usda.gov/media/232572) | &#9744; ok<br>&#9744; flag |
| 7 | "Never leave a campfire unattended, even for a moment" | [extinguishing-and-fire-safety.md](../substrate/03_fire/entries/extinguishing-and-fire-safety.md), line 151 | [T1: National Park Service, Fire Safety, Grand Teton National Park](https://www.nps.gov/grte/learn/nature/firesafety.htm) | &#9744; ok<br>&#9744; flag |
| 8 | "Never burn poison ivy or poison oak wood. Burning and breathing the smoke can cause respiratory distress" | [wet-weather-fire.md](../substrate/03_fire/entries/wet-weather-fire.md), line 97 | [T2: U.S. Army, ATP 3-50.21 Survival (Sept 2018), Chapter 5 Fire (paras 5-5 to 5-9, 5-16 to 5-22, 5-...](https://irp.fas.org/doddir/army/atp3-50-21.pdf) | &#9744; ok<br>&#9744; flag |
| 9 | "Never pour gasoline or any flammable liquid on a fire" | [wet-weather-fire.md](../substrate/03_fire/entries/wet-weather-fire.md), line 128 | [T2: U.S. Army, ATP 3-50.21 Survival (Sept 2018), Chapter 5 Fire (paras 5-5 to 5-9, 5-16 to 5-22, 5-...](https://irp.fas.org/doddir/army/atp3-50-21.pdf) | &#9744; ok<br>&#9744; flag |
| 10 | "FM 21-76 says that when you are at rest you can lose as much as 80 percent of your body heat to the ground \[1\]. It also says never sleep directly on the ground \[1\]." | [cold-weather-sleep-system.md](../substrate/04_shelter/entries/cold-weather-sleep-system.md), line 89 | [FM 21-76 Survival (1992), Chapters 5 and 15. US Army; copy read at](https://www.bits.de/NRANEU/others/amd-us-archive/FM21-76(92) | &#9744; ok<br>&#9744; flag |
| 11 | "For a shelter of parachute or other porous cloth, the Army recommends a pitch of 40 to 60 degrees, stretched wrinkle-free and tight" | [tarp-configurations.md](../substrate/04_shelter/entries/tarp-configurations.md), line 126 | [T2: US Army, ATP 3-50.21 Survival (2018), paras 6-12, 6-43 to 6-46](https://irp.fas.org/doddir/army/atp3-50-21.pdf) | &#9744; ok<br>&#9744; flag |
| 12 | "Only a building with plumbing and wiring, or a metal-topped vehicle with the windows closed, counts" | [tarp-configurations.md](../substrate/04_shelter/entries/tarp-configurations.md), line 138 | [T1: National Weather Service, Lightning Safety Indoors](https://www.weather.gov/safety/lightning-indoors) | &#9744; ok<br>&#9744; flag |
| 13 | "Clear the snow from the tailpipe whenever the engine runs. Check it before every start. A blocked tailpipe lets CO build up quickly inside the vehicle and can poison everyone in it" | [vehicle-as-shelter.md](../substrate/04_shelter/entries/vehicle-as-shelter.md), line 88 | [T1: CDC, Clear Snow from Tailpipes](https://www.cdc.gov/natural-disasters/psa-toolkit/clear-snow-from-tailpipes.html) | &#9744; ok<br>&#9744; flag |
| 14 | "Never sleep with the engine running (this entry's rule). People who are asleep can die from CO before they have symptoms" | [vehicle-as-shelter.md](../substrate/04_shelter/entries/vehicle-as-shelter.md), line 89 | [T1: CDC, Carbon Monoxide Poisoning (About)](https://www.cdc.gov/carbon-monoxide/about/index.html) | &#9744; ok<br>&#9744; flag |
| 15 | "Not under dead trees or limbs, not in a flash-flood channel, not on a stream bank, not under a steep snow slope, not in the lowest hollow." | [site-selection-and-hazards.md](../substrate/04_shelter/entries/site-selection-and-hazards.md), line 70 | [US Army, ATP 3-50.21 Survival (2018), Chapter 6: Shelter and Clothing](https://archive.org/details/survival-atp-3-50-21)<br>[National Weather Service, Flood Safety: During a Flood](https://www.weather.gov/safety/flood-during) | &#9744; ok<br>&#9744; flag |

## 3. CONVENTIONS section 10 checklist

CONVENTIONS.md section 10 has no safety checklist written for this domain. The only list that applies is the repo-wide coherence list below. The first two boxes are maintainer checks (a script runs them). The third you can do by hand: no `safe` token on biology facets and no `danger_class`. Beyond the list, your job is the claims table: check each against its source.

### Coherence (all domains)
- [ ] Manifests pass `check_manifests` (no dangling/missing rows; required columns filled).
- [ ] Survey files link down; food resolves via `regional/_index.md` registry → `food_hub.md`; no
      broken intra-repo links.
- [ ] `grep -rn "danger_class" .` = 0; no `safe` token on biology facets.

## 4. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Vehicle engine: run it 10 minutes an hour, but never sleep with it running

NWS says run the motor about 10 minutes each hour. NHTSA, as quoted by Michigan, says 5 to 10 minutes. The repo adds its own rule never to sleep with the engine running, and says a cracked window lowers the risk without removing it. Decide whether these three fit together in a way a cold, frightened reader can follow.

> NWS: run the motor "about 10 minutes each hour" and "clear snow from the exhaust pipe to avoid gas poisoning" [1]. NHTSA, as quoted by Michigan: run it "only 5-10 minutes each hour"
>
> From [vehicle-as-shelter.md](../substrate/04_shelter/entries/vehicle-as-shelter.md), line 115.

### Fire distance from a tent: 15 feet (Forest Service) against 3 feet from a snow shelter (Army)

The entry follows the Forest Service distance for tents. The Army figure is for snow shelters. Decide whether the entry makes the difference clear and whether the 15-foot rule should also apply to snow shelters.

> Keep the fire at least 15 feet from tent or tarp fabric. The Army manual puts a fire about 3 feet from a snow shelter [1]; this entry follows the Forest Service distance of 15 feet from tents [3][4].
>
> From [overnight-fire-maintenance.md](../substrate/03_fire/entries/overnight-fire-maintenance.md), line 107.

### Put the fire out before sleeping, but explain a pyramid lay that runs overnight

The entry's default is to put the fire out. It then describes how to keep one burning, citing the Army. Decide whether an unattended overnight fire belongs in a public reference.

> The default is to put the fire out before you sleep or leave.
>
> From [overnight-fire-maintenance.md](../substrate/03_fire/entries/overnight-fire-maintenance.md), line 80.

### A fire-restriction order given as a dated example

A state burn-time rule is quoted as an example. Check that it is labeled as an example that changes, and that the entry tells the reader to check current local rules.

> Virginia bans open-air burning before 4 p.m. within 300 feet of woods or flammable vegetation from Feb 15 through Apr 30
>
> From [extinguishing-and-fire-safety.md](../substrate/03_fire/entries/extinguishing-and-fire-safety.md), line 132.

### A tarp counts as a tent for lightning: the repo's own rule

No source says a tarp gives no lightning protection; the entry reasons from the tent rule and says so. Decide whether that inference is fair.

> A tent gives no protection [4]. A tarp is a cloth roof, so this entry treats it the same (this entry's rule).
>
> From [tarp-configurations.md](../substrate/04_shelter/entries/tarp-configurations.md), line 137.

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
