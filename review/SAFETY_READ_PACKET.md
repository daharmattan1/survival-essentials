# Safety Read Packet

A guide for the person doing the human safety read of this repository, one domain at a time.

## What this is

This repository is life-safety reference material. Every entry has been written and checked by AI agents. That work was careful: pass 2 had independent fact-checkers open every cited source in at least two rounds, and it found and fixed serious errors that the first pass had missed. But **`agent-verified` is not `reviewed`**. An AI check is a first pass. It can repeat a source's mistake, misread a table, or agree with a wrong claim that sounds right.

A **person** reading the entries against the primary sources is what earns `reviewed`. That is the rule in [CONVENTIONS.md](../CONVENTIONS.md) sections 10 and 11 and in [SCHEMAS.md](../SCHEMAS.md) section 0. Only a human sets it, and only by running `scripts/mark_reviewed.py` themselves. No AI agent may run that script.

This packet makes the read fast. Pass 2 found that the highest-stakes errors were identification features, look-alikes, onset times, temperatures, carbon monoxide rules and first-aid steps. So each domain file puts those claims in a table, with the exact wording, the file and line, and the source link taken from that entry's own sources. For mushrooms and edible plants it also lists every species and every look-alike pair with the two sources the entry cites. You open the source and compare. You are checking the entry against the source, not writing anything new.

## How to use it

1. **Pick one domain file** from the table below. Do one domain per sitting. Start at the top: the order is by how badly a mistake could hurt someone.
2. **Read the domain file's status block.** It gives the time budget for the targeted check, the full-read time on top of that, and the exact command you will run at the end.
3. **Work through the tables.** For each row, open the source link and find the sentence that backs the claim. Tick **ok** if it says the same thing with the same number, unit and condition. Tick **flag** if it does not.
4. **Look at the look-alike rows hardest.** A look-alike needs two Tier 1 or Tier 2 sources ([CONVENTIONS.md](../CONVENTIONS.md) section 7). Where a row says only one source is cited, finding the second is part of the read. A Tier 3 source does not count.
5. **Record each finding** with the correction form: [`.github/ISSUE_TEMPLATE/correction.yml`](../.github/ISSUE_TEMPLATE/correction.yml). Give the file path, quote the exact claim, say what is wrong and what is right, and link a Tier 1 or Tier 2 source. Pick a severity. Anything that could cause harm is read first. [CONTRIBUTING.md](../CONTRIBUTING.md) has the full rules.
6. **Decide the judgment calls** at the bottom of each file. These are places where the repo chose between sources or between two risks. Keep, change, or ask a specialist.
7. **Read the entries.** The tables are the fast pass on the claims most likely to hurt someone. They do not replace reading the entries. Each file says how many words that is. If you read only some entries, say so on the sign-off. A partial read is still useful. It just does not earn the sign-off.
8. **Sign off.** Fill in the block at the bottom of the domain file, and file it with the [Expert review form](../.github/ISSUE_TEMPLATE/expert-review.yml). Tick pass only if you read every entry and have no unresolved safety problem.
9. **Run the script yourself,** once the sign-off is in and every finding is fixed or you have accepted it. The command is in the domain file. Use `--dry-run` first to see what changes. The script asks you to type a confirmation phrase and will not run unattended. It sets `review_status: reviewed` and today's date on every entry in that one folder. Then ask a maintainer to record the line it prints in [CHANGELOG.md](../CHANGELOG.md).

If you find a claim that is dangerous right now, do not wait to finish the domain. File it as the highest severity and tell the maintainer.

## The order, by stakes

About 10 hours 10 minutes of targeted checking in total across the thirteen files, in sittings of 60 minutes or less. The full read of every entry is extra. Minutes are an estimate: roughly 2 minutes per claim, 1 minute per species or look-alike row, and 8 minutes for the checklist and the sign-off.

| Priority | Domain file | Entries | Targeted check (min) | Full read on top (min) | Folder to pass to `mark_reviewed.py` |
|---|---|---|---|---|---|
| 1 | [01 First aid](01_first_aid.md) | 10 | 50 | 75 | `substrate/06_first_aid` |
| 2 | [02 Water](02_water.md) | 8 | 40 | 55 | `substrate/02_water` |
| 3 | [03 Urban survival: carbon monoxide, food safety, heat and cold](03_urban.md) | 8 | 45 | 70 | `substrate/09_urban_survival` |
| 4 | [04 Mid-Atlantic mushrooms](04_mushrooms_mid_atlantic.md) | 8 | 60 | 75 | `regional/mid-atlantic-appalachian/mushrooms` |
| 5 | [05 Mid-Atlantic edible plants](05_edible_plants_mid_atlantic.md) | 8 | 60 | 70 | `regional/mid-atlantic-appalachian/edible-plants` |
| 6 | [06 Mid-Atlantic hazards](06_hazards_mid_atlantic.md) | 6 | 40 | 45 | `regional/mid-atlantic-appalachian/hazards` |
| 7 | [07 Fire and shelter](07_fire_shelter.md) | 12 | 40 | 105 | `substrate/03_fire`<br>`substrate/04_shelter` |
| 8 | [08 Food technique](08_food_technique.md) | 6 | 40 | 55 | `substrate/05_food` |
| 9 | [09 Mid-Atlantic game animals](09_game_mid_atlantic.md) | 5 | 40 | 60 | `regional/mid-atlantic-appalachian/game-animals` |
| 10 | [10 Mid-Atlantic crops](10_crops_mid_atlantic.md) | 7 | 40 | 55 | `regional/mid-atlantic-appalachian/crops` |
| 11 | [11 The eleven survey guides](11_survey_guides.md) | 11 | 45 | 210 | none (see the file) |
| 12 | [12 Navigation, communication, key resources, gear and core principles](12_nav_comms_resources_gear_core.md) | 24 | 50 | 185 | `substrate/07_navigation`<br>`substrate/08_communication`<br>`substrate/10_key_resources`<br>`substrate/11_gear`<br>`substrate/01_core_principles` |
| 13 | [13 Northeast and New England pack](13_northeast_new_england.md) | 15 | 60 | 158 | `regional/northeast-new-england/mushrooms`<br>`regional/northeast-new-england/edible-plants`<br>`regional/northeast-new-england/hazards`<br>`regional/northeast-new-england/game-animals`<br>`regional/northeast-new-england/crops` |

Why this order:

1. **First aid.** A wrong step here hurts a person who cannot wait for a second opinion: bleeding, burns, allergic reaction, carbon monoxide, cold and heat, insulin.
2. **Water.** Boil times, filter pore sizes and bleach doses are numbers a reader will follow exactly.
3. **Urban survival.** Carbon monoxide from generators and heaters, food safety in an outage, heat and cold at home.
4. **Mid-Atlantic mushrooms.** The most likely way this repo could kill someone is a wrong mushroom call.
5. **Mid-Atlantic edible plants.** Wild onion against death camas, acorn against buckeye, cattail against iris.
6. **Mid-Atlantic hazards.** Amatoxin mushrooms, the two hemlocks, rabies, ticks, snakebite.
7. **Fire and shelter.**
8. **Food technique.** Cook temperatures, botulism, infant formula.
9. **Mid-Atlantic game.** Tularemia, raccoon roundworm, chronic wasting disease, trichinella.
10. **Mid-Atlantic crops.** Mostly planting windows, plus a few poison-or-botulism rules.
11. **The eleven survey guides.** They repeat what the entries say, so check the entries first.
12. **Navigation, communication, key resources, gear and core principles.** The fewest ways to hurt someone, with a few exceptions: flood crossings, compass arithmetic, the poison line number and the tourniquet kit.
13. **Northeast and New England pack.** The same method as domains 04 to 10, for New England and eastern New York: three mushrooms, ramps against false hellebore, fiddleheads, hemlocks, ticks, cold water, game and crops.

## What you are not being asked to do

- You are not asked to add content. Corrections only, each with a Tier 1 or Tier 2 source.
- You are not asked to be an expert in every domain. Take the domain you know. A nurse can take first aid. A mycologist can take mushrooms.
- You are not asked to approve the repo's rules. The judgment calls are yours to decide, but the rules in [CONVENTIONS.md](../CONVENTIONS.md) (positive ID or do not consume, no AI-generated identification images, the word "safe" never describing eating or drinking, no prescription dosing) stand unless the maintainer changes them.

## Notes for the maintainer

Found while building this packet. None of these changes a safety claim.

- **Old `reviewed` stamps are still on 52 entries.** They are pass-1 labels from an AI-only check. The audits say they are void and that a later pass-2 phase relabels them. They show in the Status column of each domain file. By folder: crops 5, edible-plants 5, game-animals 5, hazards 3, mushrooms 5, 01_core_principles 3, 03_fire 3, 04_shelter 3, 05_food 3, 06_first_aid 5, 07_navigation 3, 09_urban_survival 3, 10_key_resources 3, 11_gear 3.
- **Four entries have front matter that is not valid YAML**, so a strict parser fails on them. The cause is an unquoted colon in a value. The packet builder read them with a fallback parser. They are `substrate/04_shelter/entries/cold-weather-sleep-system.md`, `substrate/04_shelter/entries/tarp-configurations.md`, `substrate/10_key_resources/entries/physical-book-backup-layer.md` and `regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md`.
- **Line numbers in the tables will drift.** They match the files as of the day this packet was built. If an entry is edited, rebuild or re-check the line numbers before the read.
- **The survey guides cannot be marked by the script.** They have no `review_status`, and the script needs a folder with an `_index.md` and an `entries/` folder. Their sign-off goes in [CHANGELOG.md](../CHANGELOG.md) by hand.
- **Domain 12 spans five folders,** so it needs five script runs. Run one only for a folder whose entries were read.
