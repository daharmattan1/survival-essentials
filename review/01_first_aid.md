# Safety read 01: First aid

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 1 of 13. First aid goes first because a wrong step here hurts a person who cannot wait for a second opinion.

## Time and status

- **Estimated time: 50 minutes at most** for the targeted check below (20 claims at about 2 minutes each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 18,908 words, roughly 75 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain substrate/06_first_aid --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

| Entry | Type | Severity | Tier | Status now | Words |
|---|---|---|---|---|---|
| [Anaphylaxis and Severe Allergic Reaction](../substrate/06_first_aid/entries/anaphylaxis-and-allergic-reaction.md) | PROTOCOL | lethal | T1 | agent-verified | 1674 |
| [Bleeding Control and Hemorrhagic Shock](../substrate/06_first_aid/entries/bleeding-control-and-shock.md) | PROTOCOL | n/a | T1 | agent-verified | 1729 |
| [Burns (Thermal), With Pointers for Chemical and Electrical Burns](../substrate/06_first_aid/entries/burns.md) | PROTOCOL | n/a | T1 | agent-verified | 2453 |
| [Carbon Monoxide Poisoning](../substrate/06_first_aid/entries/carbon-monoxide-poisoning.md) | PROTOCOL | lethal | T1 | agent-verified | 1545 |
| [Chronic Medication Continuity](../substrate/06_first_aid/entries/chronic-med-continuity.md) | PROTOCOL | n/a | T1 | agent-verified | 1743 |
| [Dehydration and Diarrhea](../substrate/06_first_aid/entries/dehydration-and-diarrhea.md) | PROTOCOL | n/a | T1 | agent-verified | 1768 |
| [Fractures, Sprains and Splinting](../substrate/06_first_aid/entries/fractures-sprains-and-splinting.md) | PROTOCOL | n/a | T1 | agent-verified | 2190 |
| [Head Injury and Concussion](../substrate/06_first_aid/entries/head-injury-and-concussion.md) | PROTOCOL | n/a | T1 | agent-verified | 2299 |
| [Thermal Injury — Hypothermia and Hyperthermia](../substrate/06_first_aid/entries/thermal-injury-hypo-hyperthermia.md) | PROTOCOL | n/a | T1 | agent-verified | 2289 |
| [Wound Infection Management](../substrate/06_first_aid/entries/wound-infection-management.md) | PROTOCOL | n/a | T1 | agent-verified | 1218 |

## 2. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "Use the person's own prescribed epinephrine device without waiting to see if it passes." | [anaphylaxis-and-allergic-reaction.md](../substrate/06_first_aid/entries/anaphylaxis-and-allergic-reaction.md), line 89 | [T2: American Academy of Allergy, Asthma and Immunology (AAAAI), Anaphylaxis](https://www.aaaai.org/tools-for-the-public/conditions-library/allergies/anaphylaxis)<br>[T2: American Academy of Allergy, Asthma and Immunology (AAAAI), Epinephrine Myths vs Facts](https://www.aaaai.org/tools-for-the-public/conditions-library/allergies/epinephrine) | &#9744; ok<br>&#9744; flag |
| 2 | "Symptoms can go away and then return hours later, so emergency care is still needed after epinephrine" | [anaphylaxis-and-allergic-reaction.md](../substrate/06_first_aid/entries/anaphylaxis-and-allergic-reaction.md), line 90 | [T1: CDC, Preventing and Managing Adverse Reactions (Vaccine Administration Best Practices)](https://www.cdc.gov/vaccines/hcp/imz-best-practices/preventing-managing-adverse-reactions.html)<br>[T2: American Academy of Allergy, Asthma and Immunology (AAAAI), Anaphylaxis](https://www.aaaai.org/tools-for-the-public/conditions-library/allergies/anaphylaxis)<br>[T2: American College of Allergy, Asthma and Immunology (ACAAI), Insect Sting Allergies](https://acaai.org/allergies/allergic-conditions/insect-sting-allergies/) | &#9744; ok<br>&#9744; flag |
| 3 | "call 911, tell the dispatcher it may be anaphylaxis, ask whether an epinephrine auto-injector is available, and follow the dispatcher's instructions" | [anaphylaxis-and-allergic-reaction.md](../substrate/06_first_aid/entries/anaphylaxis-and-allergic-reaction.md), line 100 | [T1: NIH MedlinePlus, Anaphylaxis](https://medlineplus.gov/ency/article/000844.htm) | &#9744; ok<br>&#9744; flag |
| 4 | "Do not lift the cloth to look. Lifting can restart bleeding" | [bleeding-control-and-shock.md](../substrate/06_first_aid/entries/bleeding-control-and-shock.md), line 101 | [T1: NIH MedlinePlus, Bleeding](https://medlineplus.gov/ency/article/000045.htm) | &#9744; ok<br>&#9744; flag |
| 5 | "2 to 3 inches above the wound, between the wound and the heart. Not on the wound and not on a joint (elbow, knee, wrist, ankle)" | [bleeding-control-and-shock.md](../substrate/06_first_aid/entries/bleeding-control-and-shock.md), line 108 | [T1: US Department of Homeland Security, Stop the Bleed: Applying a Tourniquet (2018)](https://www.dhs.gov/sites/default/files/publications/STB_Applying_Tourniquet_08-06-2018_0.pdf)<br>[T1: American Red Cross, How to Apply a Tourniquet](https://shop.redcross.org/take-a-class/resources/articles/how-to-apply-a-tourniquet) | &#9744; ok<br>&#9744; flag |
| 6 | "Do not wait a fixed time for pressure to work. Use a tourniquet when limb bleeding is life-threatening, or when pressure is not stopping it and the dressing is soaked" | [bleeding-control-and-shock.md](../substrate/06_first_aid/entries/bleeding-control-and-shock.md), line 106 | [T1: US Department of Homeland Security, Stop the Bleed: Applying a Tourniquet (2018)](https://www.dhs.gov/sites/default/files/publications/STB_Applying_Tourniquet_08-06-2018_0.pdf)<br>[T1: American Red Cross, Bleeding (Life-Threatening External)](https://shop.redcross.org/take-a-class/resources/learn-first-aid/bleeding-life-threatening-external) | &#9744; ok<br>&#9744; flag |
| 7 | "Aim for 20 minutes if you can, ideally within 3 hours of the burn" | [burns.md](../substrate/06_first_aid/entries/burns.md), line 115 | [T1: NHS (UK), Burns and scalds](https://www.nhs.uk/conditions/burns-and-scalds/) | &#9744; ok<br>&#9744; flag |
| 8 | "Do not soak or immerse a large or deep burn in cold water." | [burns.md](../substrate/06_first_aid/entries/burns.md), line 123 | [T1: NIH MedlinePlus, Burns (Medical Encyclopedia)](https://medlineplus.gov/ency/article/000030.htm) | &#9744; ok<br>&#9744; flag |
| 9 | "Do not touch the person with bare hands while they are still in contact with the power" | [burns.md](../substrate/06_first_aid/entries/burns.md), line 145 | [T1: NIH MedlinePlus, Electrical injury](https://medlineplus.gov/ency/article/000053.htm)<br>[T1: American Red Cross, Burns: How to Help](https://shop.redcross.org/take-a-class/resources/learn-first-aid/burns) | &#9744; ok<br>&#9744; flag |
| 10 | "Never wait for symptoms if an alarm sounds." | [carbon-monoxide-poisoning.md](../substrate/06_first_aid/entries/carbon-monoxide-poisoning.md), line 83 | [T1: CDC, About Carbon Monoxide (CO) Poisoning](https://www.cdc.gov/carbon-monoxide/about/index.html)<br>[T1: CDC, What to Do to Protect Yourself During a Power Outage](https://www.cdc.gov/natural-disasters/response/what-to-do-protect-yourself-during-a-power-outage.html) | &#9744; ok<br>&#9744; flag |
| 11 | "Never ignore it. Get outside immediately, then call 911" | [carbon-monoxide-poisoning.md](../substrate/06_first_aid/entries/carbon-monoxide-poisoning.md), line 89 | [T1: US Consumer Product Safety Commission (CPSC), Carbon Monoxide Fact Sheet](https://www.cpsc.gov/safety-education/safety-guides/carbon-monoxide/carbon-monoxide-fact-sheet)<br>[T1: US Consumer Product Safety Commission (CPSC), CPSC Issues Safety Tips to Help Families Prevent...](https://www.cpsc.gov/Newsroom/News-Releases/2026/As-Winter-Storms-Threaten-Millions-in-the-US-CPSC-Issues-Safety-Tips-to-Help-Families-Prevent-Carbon-Monoxide-Poisoning-and-Fires) | &#9744; ok<br>&#9744; flag |
| 12 | "Do not push a protruding bone back in" | [fractures-sprains-and-splinting.md](../substrate/06_first_aid/entries/fractures-sprains-and-splinting.md), line 111 | [T2: Mayo Clinic, Broken bone: First aid (Mayo Clinic Health Information Library, read on a licensed...](https://www.mhsystem.org/health-library/art-20056641) | &#9744; ok<br>&#9744; flag |
| 13 | "do not move the person unless you must, for example to escape fire or rising water, or to start CPR or control bleeding" | [fractures-sprains-and-splinting.md](../substrate/06_first_aid/entries/fractures-sprains-and-splinting.md), line 87 | [T1: American Red Cross, Fractures](https://shop.redcross.org/take-a-class/resources/learn-first-aid/fractures)<br>[T1: NIH MedlinePlus, Fractures (broken bones)](https://medlineplus.gov/ency/article/000001.htm) | &#9744; ok<br>&#9744; flag |
| 14 | "The Red Cross says sleep is generally considered fine only after a healthcare provider has evaluated the person" | [head-injury-and-concussion.md](../substrate/06_first_aid/entries/head-injury-and-concussion.md), line 137 | [T1: American Red Cross, Concussion](https://shop.redcross.org/take-a-class/resources/learn-first-aid/concussion) | &#9744; ok<br>&#9744; flag |
| 15 | "CDC: below 95 F means get medical attention immediately" | [thermal-injury-hypo-hyperthermia.md](../substrate/06_first_aid/entries/thermal-injury-hypo-hyperthermia.md), line 103 | [T1: CDC, Preventing Hypothermia (signs and first aid for hypothermia and frostbite)](https://www.cdc.gov/winter-weather/prevention/index.html) | &#9744; ok<br>&#9744; flag |
| 16 | "body temperature above 103 F, red hot skin that may be dry, rapid strong pulse, dizziness, confusion, or unconsciousness" | [thermal-injury-hypo-hyperthermia.md](../substrate/06_first_aid/entries/thermal-injury-hypo-hyperthermia.md), line 96 | [T1: Ready.gov / FEMA, Extreme Heat](https://www.ready.gov/heat)<br>[T1: NOAA National Weather Service, Heat Illness (during a heat wave)](https://www.weather.gov/safety/heat-illness) | &#9744; ok<br>&#9744; flag |
| 17 | "If it may refreeze, do not thaw it; wait until you reach a warm, safe place" | [thermal-injury-hypo-hyperthermia.md](../substrate/06_first_aid/entries/thermal-injury-hypo-hyperthermia.md), line 132 | [T1: NIH MedlinePlus, Frostbite](https://medlineplus.gov/ency/article/000057.htm)<br>[T1: American Red Cross, Frostbite](https://shop.redcross.org/take-a-class/resources/learn-first-aid/frostbite) | &#9744; ok<br>&#9744; flag |
| 18 | "6 teaspoons of sugar" | [dehydration-and-diarrhea.md](../substrate/06_first_aid/entries/dehydration-and-diarrhea.md), line 125 | [WHO, Cholera outbreaks: Questions and answers](https://www.who.int/news-room/questions-and-answers/item/cholera-outbreaks) | &#9744; ok<br>&#9744; flag |
| 19 | "1/2 teaspoon of salt" | [dehydration-and-diarrhea.md](../substrate/06_first_aid/entries/dehydration-and-diarrhea.md), line 125 | [WHO, Cholera outbreaks: Questions and answers](https://www.who.int/news-room/questions-and-answers/item/cholera-outbreaks) | &#9744; ok<br>&#9744; flag |
| 20 | "FDA notes that in an emergency, insulin that got warm may still be needed, so do not throw it out and do not decide alone: call a pharmacist or your prescriber now (FDA)" | [chronic-med-continuity.md](../substrate/06_first_aid/entries/chronic-med-continuity.md), line 131 | [FDA, Information Regarding Insulin Storage and Switching Between Products in an Emergency](https://www.fda.gov/drugs/emergency-preparedness-drugs/information-regarding-insulin-storage-and-switching-between-products-emergency) | &#9744; ok<br>&#9744; flag |

## 3. CONVENTIONS section 10 checklist

Copied from CONVENTIONS.md section 10. For first aid, the second box (RED FLAGS / EVAC and DO NOT in each entry) is the one most likely to catch a harmful omission.

### First-aid & water
- [ ] First-aid covers wound infection, hypo/hyperthermia, dehydration/diarrhea, med-continuity;
      each has RED FLAGS / EVAC + DO NOT.
- [ ] Every water entry has the `⚠ CONTAMINATION` block with boil time, micron limit, and the
      chemical-vs-biological boundary.
- [ ] All medical/water claims verified vs. CDC / Red Cross / EPA / extension (T1).

## 4. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Warmed insulin: do not discard, do not decide alone

FDA says warmed insulin may still be needed in an emergency. The repo's rule is to not throw it out and not decide alone: call a pharmacist or the prescriber, then 911 or an emergency department if neither can be reached. A pass-2 AI round asked to drop the FDA note. It was kept because discarding a person's only insulin can kill. Decide whether the wording protects the reader, gives no dosing advice, and matches what FDA published. The same wording appears in [chronic-med-continuity.md](../substrate/06_first_aid/entries/chronic-med-continuity.md) and in [09_urban_survival.md](../09_urban_survival.md) (see [domain 03](03_urban.md)).

> FDA notes that in an emergency, insulin that got warm may still be needed, so do not throw it out and do not decide alone: call a pharmacist or your prescriber now (FDA), and if you cannot reach one, call 911 or go to an emergency department (this entry's rule).
>
> From [chronic-med-continuity.md](../substrate/06_first_aid/entries/chronic-med-continuity.md), line 130.

### Burn cooling time: sources disagree, the repo picks 20 minutes

The entry lists five sources with five different durations and then picks one. Check that the choice is safe for a lay reader and that the sources are quoted fairly.

> Sources differ on how long. NHS says 20 minutes. The Red Cross says 5 to 20. MedlinePlus says at least 5 to 30. Mayo says about 10. The Massachusetts sheet says "several minutes"
>
> From [burns.md](../substrate/06_first_aid/entries/burns.md), line 116.

### Frostbite rewarming water temperature: sources give different ranges

Water that is too hot burns numb skin. Check the ranges against the two named sources and decide whether a lay reader should get a range or a single "warm, not hot, test with your hand" rule.

> MedlinePlus 104 to 108 F for 15 to 30 minutes; the Red Cross 99 to 104 F
>
> From [thermal-injury-hypo-hyperthermia.md](../substrate/06_first_aid/entries/thermal-injury-hypo-hyperthermia.md), line 132.

### Warm bottles and pads for hypothermia: sources differ

Wrong rewarming can drop a cold person's blood pressure or burn them. Decide whether the entry's reconciliation is right.

> Sources differ on warm bottles and pads.
>
> From [thermal-injury-hypo-hyperthermia.md](../substrate/06_first_aid/entries/thermal-injury-hypo-hyperthermia.md), line 124.

### Anaphylaxis with no epinephrine device on hand

The entry tells a bystander to call 911, ask the dispatcher whether an auto-injector is available, and follow the dispatcher. It marks this "general practice" rather than quoting a source. The audit says an earlier line forbade using a device on someone without a prescription, and that line was removed. Decide whether the current wording is enough and no more than the sources support.

> call 911, tell the dispatcher it may be anaphylaxis, ask whether an epinephrine auto-injector is available, and follow the dispatcher's instructions
>
> From [anaphylaxis-and-allergic-reaction.md](../substrate/06_first_aid/entries/anaphylaxis-and-allergic-reaction.md), line 99.

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
