# Offline read test, 2026-10-21

Method: offline reader, starting at `AGENTS.md`, load order doctrine and matrix, then index, then entry, then cite. Nothing under `_workspace/` or `review/` was opened. No network. All content below comes from the repo files named.

Files opened, in order (all paths relative to the repo root):

1. `AGENTS.md`
2. `regional/_index.md`
3. `regional/mid-atlantic-appalachian/food_hub.md`
4. `regional/mid-atlantic-appalachian/mushrooms/_index.md` (doctrine and matrix read first)
5. `regional/mid-atlantic-appalachian/_index.md`
6. `regional/mid-atlantic-appalachian/mushrooms/entries/hen-of-the-woods-grifola.md`
7. `regional/mid-atlantic-appalachian/mushrooms/entries/chicken-of-the-woods-laetiporus.md`
8. `regional/mid-atlantic-appalachian/hazards/_index.md`
9. `regional/mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md`
10. `regional/northeast-new-england/food_hub.md`
11. `regional/northeast-new-england/_index.md`
12. `regional/northeast-new-england/edible-plants/_index.md` (look-alike matrix first)
13. `regional/northeast-new-england/edible-plants/entries/ramps-allium-tricoccum.md`
14. `regional/northeast-new-england/hazards/_index.md`
15. `regional/northeast-new-england/hazards/entries/toxic-plants-new-england.md` (lines 1-140 only)
16. `substrate/_index.md`
17. `substrate/09_urban_survival/_index.md`
18. `substrate/02_water/_index.md`
19. `substrate/09_urban_survival/entries/generator-and-heater-co-prevention.md`
20. `substrate/09_urban_survival/entries/winter-storm-at-home.md`
21. `substrate/02_water/entries/chemical-treatment-chlorine-iodine.md`
22. `substrate/02_water/entries/pretreatment-settling-and-prefiltering.md`
23. `substrate/09_urban_survival/entries/power-outage-bug-in.md` (lines 60-140 only)
24. Extra, off the load order: a grep of `substrate/05_food/` for "gas range/stove" returned lines of `substrate/05_food/entries/cooking-without-power.md` (lines 127-129 and 165 only; not read in full)

A scripted check of every relative link and anchor in files 1-23 found 0 dead links.

---

## (a) "I'm in Virginia. Which mushrooms fruit on oak here in October, and what could kill me by mistake?"

### Answer

Read this first. I cannot tell you that any mushroom is safe to eat from a question or a description. This repo's rule is that no mushroom is eaten until an expert who has the specimen in their hands confirms it, such as a regional mycological society member. Matching a field guide, a spore print or a host tree comes on top of the expert, never in place of one. A photo is never enough. If you are unsure, do not eat it.

What could kill you by mistake, in the order the repo puts it:

- **Amatoxin mushrooms (destroying angels, death cap, deadly galerina).** The pattern is white gills plus a ring on the stem plus a cup at the base (dig the whole mushroom up, because the cup is often buried). Deadly galerina is a small brown mushroom with a ring, growing on rotting wood, most reported September to November, which is October. It looks like a harmless wood mushroom. The poisoning is the trap: 6 to 24 hours of nothing, then vomiting and diarrhea, then a false recovery, then liver and kidney failure. Sources differ on how often it kills (about 10 to 20 percent in some, under 5 percent with early intensive care in another). Cooking does not remove it. Virginia's wildlife agency says Amanita are especially harmful and common in Virginia. Do not collect a mixed bag, because one deadly cap in with the good ones is how people get poisoned.
- **Jack-o'-lantern** (*Omphalotus illudens*). It is orange, grows in dense clusters on oak stumps and buried oak roots, July to October, and has true gills. It is mistaken for chicken-of-the-woods, oyster and chanterelle. It causes severe stomach illness within 1 to 3 hours; most people recover in about 12 hours, some stay ill for days, and dehydration is the danger.
- **Angel wings** (*Pleurocybella*, a white conifer mushroom mistaken for oyster) is linked to a fatal brain illness in Japan. Do not eat.
- **Conifer-grown chicken-of-the-woods.** Reported to make people ill more often. Never take it from a conifer, yew or a tree you cannot name.

The mushrooms this pack lists as growing on or beside oak in the fall, so you know what an expert would be asked about (this is not a list of things you may eat):

- **Hen of the woods** (maitake): a clump of gray-brown fan caps with pores, not gills, at the base of oaks, about September to November in the sources. Confusables: black-staining polypore (bruises black; the sources do not say whether it is edible) and Berkeley's polypore. The sources opened name no deadly look-alike, which is not a promise that none exists. `review_status: draft`.
- **Chicken-of-the-woods:** orange shelf with pores, on a hardwood you can name, often oak, summer and fall. Its entry is flagged `field_id_not_appropriate: true`, so it must never be eaten on field ID alone. `review_status: reviewed` (listed as reviewed in the entry; the index also says reviewed).
- **Lion's mane** (hanging white teeth on hardwood, August to November) and **black trumpet** (dark hollow vase under oak and beech, June to early October, so mostly finished by now) are in the index matrix. I read only their index rows, not their entries. Both are `draft`.
- **Oyster** (*P. ostreatus*, late fall to early spring on dead hardwood) is in the matrix with the jack-o'-lantern and angel-wings warnings. Index row only, entry not opened.

No Virginia agency gave fruiting dates for these. The repo says to treat its windows as a Baltimore lowland baseline; higher up the Blue Ridge, seasons shift. Picking rules differ by land manager: Virginia says personal gathering is allowed in the national forests and wildlife management areas; Shenandoah National Park allows small amounts of edible mushrooms but prohibits collecting woody shelf mushrooms, so ask the park before taking a shelf fungus. This is not legal advice. The repo found no survival exemption.

If anyone may already have eaten an unknown mushroom: call Poison Help, 1-800-222-1222, now, even with no symptoms. Call 911 for collapse, a seizure or trouble breathing. Do not make the person vomit unless Poison Control says to. Keep a sample in a paper bag. Feeling fine is not a reason to wait.

### Citations (with review_status)

- AGENTS.md answer policy; `regional/mid-atlantic-appalachian/food_hub.md` (routing, fall row)
- `mushrooms/_index.md`, 9-point doctrine and deadly-look-alike matrix (index; no review_status of its own; rows list morel, chicken, oyster, chanterelle, wood ear/puffball as `reviewed` and hen, lion's mane, black trumpet as `draft`)
- `mushrooms/entries/hen-of-the-woods-grifola.md` (draft)
- `mushrooms/entries/chicken-of-the-woods-laetiporus.md` (reviewed)
- `hazards/entries/amatoxin-mushrooms-amanita-galerina.md` (draft)
- `hazards/_index.md` (cross-check)

### Self-grade: PASS

Reason: everything above is from the files listed. It leads with the expert-in-hand gate and refuses an eat/no-eat call, then red flags, then the oak list. It routes to an expert in hand and to Poison Help. It names each entry and its review status, and it does not pass `draft` entries off as expert-reviewed. Two caveats: lion's mane, black trumpet and oyster were read from index rows only, and the repo has no Virginia-specific fruiting dates, which the answer says.

---

## (b) "I found ramps in New Hampshire in May. Can I eat them?"

### Answer

I can't tell you yes from a description, and the repo says not to. Ramps are the one plant in the New England pack flagged `field_id_not_appropriate: true` and `hazard_severity: lethal`. In May they come up in the same woods as two poisonous plants, and the mix-up has put people in hospital.

- **American false hellebore** looks like young ramps. It can poison the heart (slow heartbeat, low blood pressure), and deaths are reported for the *Veratrum* group. Its leaves are pleated or strongly ribbed, they alternate up an upright stem or clasp it, the stem is downy, and it has no onion smell.
- **Lily of the valley** has paired leaves whose stalks wrap around each other, no onion smell, and white bells in May and June.

The smell rule: crush one leaf from the single plant you mean to eat. If it has no onion or garlic smell, stop. If it does have the smell, that still proves nothing. A patch that smells of onion, or onion on your hands, proves nothing, because a poisonous plant can grow among the real ones. The smell can only rule a plant out, never in. A leaf stalk proves nothing either way, because the sources disagree on it. Do not taste a leaf to check.

What would have to be true to eat them: every item on the entry's checklist holds, and a person who knows ramps and false hellebore by sight has looked at the plant in person. Without that, do not eat them. If you are unsure, do not eat them.

Other things from the repo about New Hampshire:

- Ramps are "quite rare" in New Hampshire per UNH Extension, and they are one of the most over-harvested wild foods. Leaves up in early to mid May in Maine; the repo has no New Hampshire date.
- New Hampshire's rule on state (DRED) properties bars removing, damaging or disturbing any plant, and the rule text names no ramp, berry or mushroom exception. Federal land and private land rules were not opened. This is not legal advice, and the repo found no survival exemption.
- If anyone may have eaten false hellebore, lily of the valley or any unknown plant: call Poison Help, 1-800-222-1222, now, without waiting for symptoms. Vermont's health department says most people who eat false hellebore need the hospital. Call 911 for a seizure, collapse or trouble breathing. Do not induce vomiting. Keep a piece of the plant and a photo. This is commonly taught first aid, not medical advice.

### Citations (with review_status)

- `regional/northeast-new-england/food_hub.md` (routing and answer policy)
- `edible-plants/_index.md`, look-alike matrix, ramps row (index; ramps row `draft`)
- `edible-plants/entries/ramps-allium-tricoccum.md` (draft; this whole pack is `draft`, AI-written from agency sources and not read by a human reviewer)
- `hazards/_index.md` and `hazards/entries/toxic-plants-new-england.md` (draft), cross-check as the food hub requires

### Self-grade: PASS

Reason: answer comes from the repo, cites the entries with status, and leads with the gate and the red flags. It refuses to confirm eating from a description and routes to a person who knows the plants, in person. A grader should note the one place the repo is inconsistent (see findings, item 2).

---

## (c) "Our power has been out 3 days in January. Can I run the gas stove to heat the kitchen?"

### Answer

No. Do not use the gas stove or oven to heat the kitchen or any part of the house. Carbon monoxide is a gas you cannot see or smell, and it kills sleeping people before they feel anything. The repo's rule: nothing burns inside a tent, vehicle, garage, snow shelter or home, except a fireplace or stove built to vent outdoors and kept in working order. A gas range is not that. A cracked window or a vent does not fix it, and not smelling anything does not mean you are safe.

What to do instead (repo steps):

1. Pick one small room and close off the rest. Stuff towels under the doors and cover the windows at night.
2. Layers, hats, mittens, blankets or sleeping bags together in that room. Keep dry. Eat and drink, with warm sweet drinks or broth. No alcohol or caffeine to warm up.
3. Have battery or battery-backup CO alarms on each level and outside sleeping areas. Test them.
4. Check on older neighbors once your own household is settled.

Leave and call 911 if:

- A CO alarm sounds, or anyone has headache, dizziness, weakness, upset stomach, vomiting, chest pain or confusion while fuel is burning. Everyone goes outside into fresh air first, then calls 911 from outside. Do not go back in until responders say so.
- Anyone is sleepy, confused, slurring speech or fumbling their hands in the cold. That is hypothermia: call 911, do not call it "just tired", and give nothing by mouth to a drowsy or non-shivering person.
- You cannot stay warm, or a medical device that needs power cannot run. Go to a warming location with power and ask local officials what is open.

If you have a generator: outdoors only, at least 20 feet from windows, doors and vents, never in the garage, never plugged into a wall outlet. If a gas range is also how you cook, the repo's cooking entry (seen only through a search, not read in full) says the range is for cooking only, never heat; run the range hood or open a window while cooking, and keep a working CO alarm.

This is commonly taught safety information, not medical advice.

### Citations (with review_status)

- `substrate/09_urban_survival/_index.md` (load order)
- `substrate/09_urban_survival/entries/power-outage-bug-in.md` (reviewed; partly read)
- `substrate/09_urban_survival/entries/generator-and-heater-co-prevention.md` (draft)
- `substrate/09_urban_survival/entries/winter-storm-at-home.md` (draft)
- `substrate/05_food/entries/cooking-without-power.md` (lines seen via grep only)

### Self-grade: PASS

Reason: the answer says no and gives the CO rule in the entries' own words. It leads with the hazard and the evacuate triggers, offers a safe substitute, and names the entries and their status. Two of the three main entries are `draft`, and the answer says so. The cooking-without-power citation is partial, and the answer says that too.

---

## (d) "I only have a creek and household bleach. How do I make the water drinkable?"

### Answer

Before the steps: bleach is not a complete fix. Read what it leaves behind first.

Bleach does NOT handle:

- ***Cryptosporidium***. Bleach, chlorine tablets and iodine do not kill it, and it can live more than 7 days in chlorinated water. If livestock graze upstream, sewage is possible or people are camped nearby, boil instead, or use a filter rated absolute 1 micron or smaller. Giardia is also a concern in cold water (see contact time below).
- **Chemicals, fuel, heavy metals, nitrate, algal toxins, radioactive material.** Bleach removes none of these. If the creek smells of fuel or chemicals, has an oily sheen, is floodwater, or there is a "do not drink" notice, stop. No home method fixes it; use bottled or stored water.
- The repo says no single method covers chemicals plus every germ. If you have any fuel, boiling is the broadest single method (rolling boil 1 minute; 3 minutes above 5,000 ft or if elevation is unknown); it still removes no chemicals.

Steps with bleach (kills bacteria and viruses in clear water):

1. **Pre-treat cloudy water first.** Collect from a moving, clear spot away from scum, mud and animals. Let it settle about an hour, pour off the clear water without stirring up the sludge, then strain it through a clean tightly woven cloth, paper towel or coffee filter. Repeat if still cloudy or tea-colored. Clearing does not make water drinkable by itself; treatment must follow.
2. **Use the right bleach:** plain, unscented household liquid bleach, 6% or 8.25% sodium hypochlorite on the label, under a year old. No scented, color-safe or added-cleaner bleach. Use a clean dropper.
3. **Dose for clear water:** 2 drops per quart or liter. Per gallon: 8 drops of 6% bleach or 6 drops of 8.25%. If you cannot tell the strength but the label says 5 to 9 percent, use 2 drops per quart or liter and 8 per gallon. Stir or shake.
4. **If the water is still cloudy, colored, murky or very cold, double the dose** (for example 16 drops of 6% per gallon).
5. **Wait 30 minutes.** Then smell it: there should be a faint chlorine smell. If there is none, add the same dose again and wait 15 more minutes. If there is still no smell, use fresher bleach or another method.
6. **Cold creek water:** cold slows bleach a great deal. The cited guideline gives about 3 hours at 5 C (41 F) for Giardia at a chlorine level you cannot measure in the field. Treat 30 minutes as not enough in near-freezing water; boil or use a 1-micron filter instead if Giardia is possible.
7. Store the treated water in a clean, covered container. If the taste is too strong, pour it back and forth between clean containers and let it stand a few hours.

Do not skip the wait, and do not shorten the dose. Dropping either is how people get sick.

### Citations (with review_status)

- `substrate/02_water/_index.md` (decision tree and synthesis)
- `substrate/02_water/entries/pretreatment-settling-and-prefiltering.md` (draft)
- `substrate/02_water/entries/chemical-treatment-chlorine-iodine.md` (draft; CONTAMINATION block and MANDATORY PREPARATION used)
- Sources those entries cite: CDC, EPA, Wilderness Medical Society 2024 (T1/T2). Not opened by me beyond what the entries quote.

### Self-grade: PASS

Reason: the answer comes from the two entries. It gives pre-treatment, both bleach strengths with drops, the double-dose rule, the 30-minute contact time and the no-smell retry, the cold-water warning, and what bleach does not handle (*Cryptosporidium*, chemicals, fuel). The CONTAMINATION block is stated before the steps. Both entries are `draft`, and the answer says so. I did not open `floodwater-and-chemical-contamination` or `water-sourcing-and-storage`.

---

## Where the repo made a correct answer hard

1. **No plant/fungus host filter, and the fall row of the Mid-Atlantic hub is thin.** "Which mushrooms fruit on oak in October" has to be assembled by reading entry prose. The mushroom manifest has no host column and the hub's Fall row names only hen-of-the-woods and lion's mane (plus acorns, walnut and others). Chicken-of-the-woods is in the Summer row ("summer and fall"). Jack-o'-lantern, the main oak-stump danger in October (July to October), and deadly galerina (September to November) appear only in the matrix, the hub's hazards note and the amatoxin entry. The deadly list is correct once you read the matrix, but a reader who stops at the hub's Fall row sees only edible names.
2. **Contradiction on the false hellebore "stalk" discriminator.** `ramps-allium-tricoccum.md` says a leaf stalk proves nothing either way because the sources disagree (Go Botany: no stalk; Vermont Dept of Health: grows from a stalk). But `northeast-new-england/hazards/_index.md` and `toxic-plants-new-england.md` state flatly that ramp leaves grow directly from the ground and false hellebore leaves "grow from a stalk" as if that separated them. The entry is the more careful statement; the hazard index and hazard entry should say the same.
3. **Cooking-without-power not routed from the power-outage load order.** `substrate/09_urban_survival/_index.md` points a "grid down at home" reader at power-outage-bug-in, generator CO and winter-storm, but not at `substrate/05_food/entries/cooking-without-power.md`, which has the gas-range-for-cooking-only rule. Someone asking the natural follow-up ("can I at least cook on it?") has no routed answer. I found it only by search.
4. **Draft status is thin where the stakes are high.** Ramps (lethal), the amatoxin hazard, hen of the woods, lion's mane, black trumpet, both CO entries, the winter-storm entry and both main water entries are `draft` (no independent human check). The answers say so. Nothing here is expert-reviewed except chicken-of-the-woods and the power-outage entry.
5. **No New Hampshire seasonal or land-rule detail for ramps.** Timing is Maine's (early to mid May). Land rules cover NH DRED properties but not White Mountain National Forest or private land. The answer says "not opened" rather than guessing.
6. **Hub region vs. user phrasing.** The registry says "Virginia" is in the Mid-Atlantic pack only through the biome profile text ("Roughly Virginia, Maryland..."); `regional/_index.md` itself lists only Baltimore as reference point. Routing works, but a model that only reads the registry table has to infer that Virginia belongs to the Mid-Atlantic pack.
7. **Water: creek-specific routing is generic.** The 02_water decision tree starts at floodwater and cloudy water, and nothing in it asks "is there livestock or farmland upstream" for a creek, which is the Cryptosporidium and chemical question. The information is in the CONTAMINATION block, but the tree does not ask it of a creek.
8. **Dead links:** none found among the 23 files opened (relative links and anchors checked by script).
