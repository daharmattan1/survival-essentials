# Safety read 11: The eleven survey guides

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 11 of 13. The survey guides come eleventh because each repeats numbers that the entries in domains 01 to 10 own. Check the entries first, then check that the guide still agrees with them.

## Time and status

- **Estimated time: 45 minutes at most** for the targeted check below (18 claims at about 2 minutes each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 52,635 words, roughly 210 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

The survey guides have no `review_status` field, and `scripts/mark_reviewed.py` only works on a domain folder that has an `_index.md` and an `entries/` folder. It cannot be run on them. When you finish, ask a maintainer to record your sign-off in [CHANGELOG.md](../CHANGELOG.md). Do not edit a guide's status.

## 1. Entries to read

Each guide is the human doorway to its substrate folder. The sync rule in [CHANGELOG.md](../CHANGELOG.md) says a guide must not contradict its entries. Read the guide beside its entries: [01 core principles](12_nav_comms_resources_gear_core.md), [02 water](02_water.md), [03 fire](07_fire_shelter.md), [04 shelter](07_fire_shelter.md), [05 food](08_food_technique.md), [06 first aid](01_first_aid.md), [07 navigation](12_nav_comms_resources_gear_core.md), [08 communication](12_nav_comms_resources_gear_core.md), [09 urban survival](03_urban.md), [10 key resources](12_nav_comms_resources_gear_core.md), [11 essential gear](12_nav_comms_resources_gear_core.md).

| Entry | Type | Severity | Tier | Status now | Words |
|---|---|---|---|---|---|
| [01\_core\_principles.md](../01_core_principles.md) | survey guide | n/a | n/a | no status field | 4372 |
| [02\_water.md](../02_water.md) | survey guide | n/a | n/a | no status field | 4627 |
| [03\_fire.md](../03_fire.md) | survey guide | n/a | n/a | no status field | 4845 |
| [04\_shelter.md](../04_shelter.md) | survey guide | n/a | n/a | no status field | 4965 |
| [05\_food.md](../05_food.md) | survey guide | n/a | n/a | no status field | 4904 |
| [06\_first\_aid.md](../06_first_aid.md) | survey guide | n/a | n/a | no status field | 5340 |
| [07\_navigation.md](../07_navigation.md) | survey guide | n/a | n/a | no status field | 4816 |
| [08\_communication.md](../08_communication.md) | survey guide | n/a | n/a | no status field | 4720 |
| [09\_urban\_survival.md](../09_urban_survival.md) | survey guide | n/a | n/a | no status field | 4985 |
| [10\_key\_resources.md](../10_key_resources.md) | survey guide | n/a | n/a | no status field | 4446 |
| [11\_essential\_gear.md](../11_essential_gear.md) | survey guide | n/a | n/a | no status field | 4615 |

## 2. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "Hypothermia (dangerously low body temperature) can start above 40 F if rain, sweat or cold water has you chilled" | [01\_core\_principles.md](../01_core_principles.md), line 27 | [Cold Weather Safety for Older Adults. National Institute on Aging, NIH](https://www.nia.nih.gov/health/safety/cold-weather-safety-older-adults) | &#9744; ok<br>&#9744; flag |
| 2 | "air 3 minutes, shelter 3 hours, rest 30 hours, water 3 days, food 30 days" | [01\_core\_principles.md](../01_core_principles.md), line 79 | [Basic Survival Skills for Aviation (OK-06-033). FAA Civil Aerospace Medical Institute](https://www.faa.gov/pilots/training/airman_education/media/CAMISurvivalManual.pdf) | &#9744; ok<br>&#9744; flag |
| 3 | "rolling boil 1 minute. Boil 3 minutes if you are above 5,000 ft or not sure of your elevation" | [02\_water.md](../02_water.md), line 7 | [How to Make Water Safe in an Emergency. CDC](https://www.cdc.gov/water-emergency/about/index.html)<br>[Emergency Disinfection of Drinking Water. US EPA](https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water)<br>[Drinking Water Advisories: An Overview. CDC](https://www.cdc.gov/water-emergency/about/drinking-water-advisories-an-overview.html)<br>[About Water Treatment Options When Hiking, Camping, or Traveling. CDC](https://www.cdc.gov/drinking-water/prevention/water-treatment-hiking-camping-traveling.html) | &#9744; ok<br>&#9744; flag |
| 4 | "plain unscented bleach, 8 drops of 6% bleach per gallon of clear water, then wait 30 minutes" | [02\_water.md](../02_water.md), line 8 | [Emergency Disinfection of Drinking Water. US EPA](https://www.epa.gov/ground-water-and-drinking-water/emergency-disinfection-drinking-water) | &#9744; ok<br>&#9744; flag |
| 5 | "Use boiling or a filter rated absolute 1 micron or smaller." | [02\_water.md](../02_water.md), line 33 | [How to Make Water Safe in an Emergency. CDC](https://www.cdc.gov/water-emergency/about/index.html)<br>[Wilderness Medical Society Clinical Practice Guidelines on Water Treatment (2024). Wilderness Envir...](https://stacks.cdc.gov/view/cdc/153527/cdc_153527_DS1.pdf)<br>[ATP 3-50.21 Survival (2018). US Army](https://irp.fas.org/doddir/army/atp3-50-21.pdf)<br>[Preventing and Controlling Crypto at Camps. CDC](https://www.cdc.gov/cryptosporidium/prevention/preventing-and-controlling-crypto-at-camps.html) | &#9744; ok<br>&#9744; flag |
| 6 | "More than 400 Americans die each year from accidental CO poisoning not linked to fires" | [03\_fire.md](../03_fire.md), line 27 | [Carbon Monoxide Poisoning (About). CDC](https://www.cdc.gov/carbon-monoxide/about/index.html) | &#9744; ok<br>&#9744; flag |
| 7 | "Do not warm numb hands or feet against a fire or stove. Numb skin burns without hurting" | [03\_fire.md](../03_fire.md), line 40 | [Preventing Hypothermia. CDC](https://www.cdc.gov/winter-weather/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 8 | "Someone in the heat is confused, has slurred speech, faints, has hot skin or a fast strong pulse, or a temperature above 103 F. That is heat stroke" | [04\_shelter.md](../04_shelter.md), line 22 | [Extreme Heat. Ready.gov / FEMA](https://www.ready.gov/heat)<br>[Heat Illness. National Weather Service](https://www.weather.gov/safety/heat-illness) | &#9744; ok<br>&#9744; flag |
| 9 | "Wait 30 minutes after the last thunder" | [04\_shelter.md](../04_shelter.md), line 52 | [Lightning Safety Outdoors. National Weather Service](https://www.weather.gov/safety/lightning-outdoors) | &#9744; ok<br>&#9744; flag |
| 10 | "A closed fridge holds its cold about 4 hours. A full freezer holds about 48 hours, a half-full one about 24 hours" | [05\_food.md](../05_food.md), line 72 | [Be Prepared for a Power Outage (V-1008, Dec 2023). FEMA](https://www.ready.gov/sites/default/files/2024-03/ready.gov_power-outage_hazard-info-sheet.pdf)<br>[Keep Food Safe After a Disaster or Emergency. CDC](https://www.cdc.gov/food-safety/foods/keep-food-safe-after-emergency.html) | &#9744; ok<br>&#9744; flag |
| 11 | "Perishables left out more than 2 hours, or 1 hour above 90 F, go in the trash" | [05\_food.md](../05_food.md), line 73 | [Four Steps to Food Safety. CDC](https://www.cdc.gov/food-safety/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 12 | "Do not eat from swollen, dented or corroded cans \[3\]; throw them out. Never taste food to test it \[2\]." | [05\_food.md](../05_food.md), line 60 | [Food. Ready.gov / FEMA](https://www.ready.gov/food)<br>[Keep Food Safe After a Disaster or Emergency. CDC](https://www.cdc.gov/food-safety/foods/keep-food-safe-after-emergency.html) | &#9744; ok<br>&#9744; flag |
| 13 | "Life-threatening arm or leg bleeding: put a tourniquet on now. Do not keep trying pressure alone." | [06\_first\_aid.md](../06_first_aid.md), line 67 | [Stop the Bleed: Applying a Tourniquet (2018). US Department of Homeland Security](https://www.dhs.gov/sites/default/files/publications/STB_Applying_Tourniquet_08-06-2018_0.pdf)<br>[Bleeding (Life-Threatening External). American Red Cross](https://shop.redcross.org/take-a-class/resources/learn-first-aid/bleeding-life-threatening-external)<br>[Until Help Arrives (Version 1.0). Ready.gov / FEMA](https://www.ready.gov/sites/default/files/2020-07/until-help-arrives-web-tutorial.pdf) | &#9744; ok<br>&#9744; flag |
| 14 | "Place it at least 2 to 3 inches above the wound, between the wound and the heart, not on a joint." | [06\_first\_aid.md](../06_first_aid.md), line 73 | [Stop the Bleed: Applying a Tourniquet (2018). US Department of Homeland Security](https://www.dhs.gov/sites/default/files/publications/STB_Applying_Tourniquet_08-06-2018_0.pdf)<br>[How to Apply a Tourniquet. American Red Cross](https://shop.redcross.org/take-a-class/resources/articles/how-to-apply-a-tourniquet)<br>[Bleeding. NIH MedlinePlus](https://medlineplus.gov/ency/article/000045.htm) | &#9744; ok<br>&#9744; flag |
| 15 | "Hypothermia (dangerously low body temperature) can set in at 50 F when you are wet and cold." | [07\_navigation.md](../07_navigation.md), line 7 | [Wilderness Safety. Olympic National Park, NPS](https://www.nps.gov/olym/planyourvisit/wilderness-safety.htm) | &#9744; ok<br>&#9744; flag |
| 16 | "Call will not connect? Try a text to 911 where your area offers it" | [08\_communication.md](../08_communication.md), line 23 | [Text to 911: What You Need to Know. FCC (page last updated January 2020)](https://www.fcc.gov/consumers/guides/what-you-need-know-about-text-911) | &#9744; ok<br>&#9744; flag |
| 17 | "(America's Poison Centers), free and open 24 hours a day" | [10\_key\_resources.md](../10_key_resources.md), line 22 | [Poison Help line (1-800-222-1222), online help and when to call 911. America's Poison Centers](https://poisoncenters.org/) | &#9744; ok<br>&#9744; flag |
| 18 | "Do not give aspirin to someone because it is in the kit, and never give it to a child unless the child's clinician says to" | [11\_essential\_gear.md](../11_essential_gear.md), line 116 | [Reye syndrome. NIH MedlinePlus](https://medlineplus.gov/ency/article/001565.htm) | &#9744; ok<br>&#9744; flag |

## 3. CONVENTIONS section 10 checklist

Copied from CONVENTIONS.md section 10. For the survey guides the coherence list is the one that applies. Run the checks that need a person: click through the cross-links, and compare each number the guide repeats with its entry.

### Coherence (all domains)
- [ ] Manifests pass `check_manifests` (no dangling/missing rows; required columns filled).
- [ ] Survey files link down; food resolves via `regional/_index.md` registry → `food_hub.md`; no
      broken intra-repo links.
- [ ] `grep -rn "danger_class" .` = 0; no `safe` token on biology facets.

## 4. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Hypothermia onset: guide 01 says it can start above 40 F, guide 07 says it can set in at 50 F

The two guides give different temperatures. Both may be defensible, but a reader may notice. Decide whether to keep both, state one, or explain the difference.

> Hypothermia (dangerously low body temperature) can start above 40 F if rain, sweat or cold water has you chilled [9].
>
> From [01_core_principles.md](../01_core_principles.md), line 27.

> Hypothermia (dangerously low body temperature) can set in at 50 F when you are wet and cold.
>
> From [07_navigation.md](../07_navigation.md), line 7.

### Tourniquet placement: "at least 2 to 3 inches" in the guide, "2 to 3 inches" in the entry

The first aid guide says at least 2 to 3 inches above the wound. The bleeding entry says 2 to 3 inches above the wound. Check the Stop the Bleed and Red Cross sources linked in [domain 01](01_first_aid.md) and decide which wording they support. The EDC kit entry has a third form.

> Place it at least 2 to 3 inches above the wound, between the wound and the heart, not on a joint.
>
> From [06_first_aid.md](../06_first_aid.md), line 73.

> 2 to 3 inches above the wound, between the wound and the heart. Not on the wound and not on a joint (elbow, knee, wrist, ankle)
>
> From [bleeding-control-and-shock.md](../substrate/06_first_aid/entries/bleeding-control-and-shock.md), line 107.

### Warmed insulin in the urban guide

The same judgment call as in [domain 03](03_urban.md) and [domain 01](01_first_aid.md). Read it once in whichever domain you take first, and apply the answer here.

> Do not throw out a life-sustaining medicine (insulin, transplant drugs, etc.) until you have called a pharmacist or clinician.
>
> From [09_urban_survival.md](../09_urban_survival.md), line 216.

### Wild game temperatures in the food guide

The guide's table gives venison 160 F and bear, wild pig and other wild meat-eaters 165 F, and says where sources differ. The same split is in [domain 08](08_food_technique.md) and [domain 09](09_game_mid_atlantic.md).

> Sources differ in three places.
>
> From [05_food.md](../05_food.md), line 95.

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
