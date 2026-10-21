# Northeast / New England: Food Decision Hub

> **"What can I eat here, and what could kill me?"** This is the retrieval surface that composes plants,
> mushrooms, game, crops, seasonality and hazards into one season-indexed decision flow. Every food or
> consumption question for this biome resolves **through here** (retrieval recipe A in
> [`../../AGENTS.md`](../../AGENTS.md)), and **always** routes through the look-alike matrices, the mushroom
> doctrine and `hazards/` **before** any food entry.
>
> Biome profile: [`_index.md`](_index.md). Registry: [`../_index.md`](../_index.md). Calendar:
> [`seasonality.md`](seasonality.md).

---

> ## ⚠ Read this before any "can I eat it" answer (answer policy)
>
> - **Positive ID or do not consume.** Nothing here is cleared on one trait, one photo, or the absence of a
>   warning. Every wild plant and mushroom entry carries a positive-ID checklist of *several concurrent*
>   traits and a list of traits that disqualify.
> - **Uncertainty first.** Lead with the gate and the checklist, **not** a verdict.
> - **Mushrooms and toxic-plant look-alikes can kill careful people.** For every mushroom, and for ramps
>   (`field_id_not_appropriate: true`), **refuse** to confirm "yes, eat it" on a description or photo alone.
>   Every mushroom needs an expert who has examined the specimen in hand (doctrine point 1 in
>   [`mushrooms/_index.md`](mushrooms/_index.md)); a spore print and several matching sources come on top of
>   that, never in place of it.
> - **Fiddleheads need a person too.** Ostrich fern shares its groove and scales with lady fern
>   (`expert_id_required: true`), so the first time, someone who knows ostrich fern confirms it in person, and
>   the mandatory boil or steam still applies.
> - **"What can I eat?" always starts at the look-alike matrix and, for fungi, the mushroom doctrine.** No
>   list in this hub names a species as ready to eat. Each name below is a link to that entry's gate.
> - **Reproduce `## ⚠ MANDATORY PREPARATION` word for word** for anything that needs cooking, boiling or
>   other treatment: fiddleheads, potatoes, maple sap and every wild meat.
> - **If someone may already have eaten an unknown plant or mushroom:** call Poison Help,
>   **1-800-222-1222**, now, even with no symptoms. Call 911 for a seizure, collapse, trouble breathing or if
>   they cannot be woken. Do not make them vomit unless Poison Control says to. Keep a sample of what was
>   eaten. This is commonly taught first aid, not medical advice.
> - The absence of a warning is **missing data, not a green light.** Most plants, mushrooms and game of this
>   region have no entry in this pack.

---

## The decision flow

```
"Can I eat X / what can I eat here right now?"
│
├─ 1. ORIENT to season  → seasonality.md  (what category is even in season now?)
│
├─ 2. Pick the category and OPEN ITS INDEX; read the danger surface FIRST:
│      ├─ Wild plant?     → edible-plants/_index.md  → READ THE LOOK-ALIKE MATRIX, then the entry
│      │      ramps (false hellebore, lily of the valley) · fiddleheads (bracken; someone who knows ostrich fern confirms the first time; mandatory boil or steam) · wild blueberry
│      ├─ Mushroom?       → mushrooms/_index.md       → READ THE 9-POINT DOCTRINE + DEADLY-LOOK-ALIKE MATRIX, then the entry
│      │      honey mushroom (deadly galerina) · chanterelle (jack-o'-lantern) · king bolete   (all need an expert in hand)
│      ├─ Game/meat?      → game-animals/_index.md    → legal and season note + ⚠ DISEASE block
│      │      deer (CWD; carcass import rules differ by state) · ruffed grouse (protected spruce grouse; bird flu) · snowshoe hare (tularemia; protected cottontail)
│      └─ Grown food?     → crops/_index.md           → planting windows from the last frost + ⚠ MANDATORY PREPARATION
│             potato (green or bitter = solanine) · cabbage and kale · maple sap and syrup (carbon monoxide, lead, burns)
│
├─ 3. CROSS-CHECK hazards → hazards/_index.md  (does a deadly look-alike or toxic plant share this habitat or season?)
│      toxic plants (false hellebore, water hemlock, poison hemlock) · ticks · cold water and hypothermia
│
├─ 4. APPLY the entry's positive-ID gate + ⚠ MANDATORY PREPARATION (word for word)
│
└─ 5. CITE the specific entries and their sources.  When in doubt → do NOT eat.
```

---

## Routing table: category → index → what leads it

| You're looking at… | Open | The danger surface it leads with | Cross-check |
|--------------------|------|----------------------------------|-------------|
| A **wild plant** (spring greens, shoots, berries) | [`edible-plants/_index.md`](edible-plants/_index.md) | **Look-alike matrix** (target → deadly or toxic look-alike → discriminators → what it does) | [`hazards/_index.md`](hazards/_index.md), especially [toxic plants](hazards/entries/toxic-plants-new-england.md) (false hellebore, the two hemlocks) |
| A **mushroom** | [`mushrooms/_index.md`](mushrooms/_index.md) | **Mushroom doctrine (9 points; expert in hand first) + deadly-look-alike matrix** | [`hazards/_index.md`](hazards/_index.md); amatoxin: see "Not yet written" below |
| **Game / meat** | [`game-animals/_index.md`](game-animals/_index.md) | Legal and season note + **⚠ DISEASE & PARASITE** (CWD prion, bird flu, tularemia) and the two protected look-alikes | [`ticks-new-england`](hazards/entries/ticks-new-england.md), [`hazards/_index.md`](hazards/_index.md) |
| **Grown food or maple sap** | [`crops/_index.md`](crops/_index.md) | Planting windows counted from your local last frost, and **⚠ MANDATORY PREPARATION** (potato solanine; boiling sap) | [`../../03_fire.md`](../../03_fire.md) for the carbon monoxide rule |
| **Processing technique** (gut, skin, cook, preserve) | [`../../substrate/05_food/_index.md`](../../substrate/05_food/_index.md) | Cook-thoroughly and never-eat rules (universal technique) | game `⚠ DISEASE` blocks |

### Entry routing (each link opens the gate first)

| Category | Entries, each with its look-alikes and hazards as the entry states them |
|----------|-------------------------------------------------------------------------|
| **Wild plants (3)** | [ramps / wild leek](edible-plants/entries/ramps-allium-tricoccum.md) (**American false hellebore**, which can poison the heart and has killed; **lily of the valley**; smell is never enough, no onion smell means stop; `field_id_not_appropriate: true`) · [fiddleheads, ostrich fern](edible-plants/entries/fiddlehead-ostrich-fern.md) (**bracken** and other ferns, lady fern, cinnamon and interrupted fern; `expert_id_required: true`, so someone who knows ostrich fern confirms it in person the first time; **boil 15 minutes or steam 10 to 12 minutes and throw out the water**) · [wild blueberry](edible-plants/entries/lowbush-blueberry-vaccinium.md) (no toxic look-alike named by the sources opened; rule out black nightshade and bluebead lily; managed barrens are farmland) |
| **Mushrooms (3)** | [honey mushroom](mushrooms/entries/honey-mushroom-armillaria.md) (**deadly galerina**, same wood and season, amatoxin; jack-o'-lantern; the *Amanita* pattern, which the honey mushroom's whitish gills and ring also fit, so doctrine point 3 applies and only an expert with the dug-up specimen can clear it; blanch and throw out the cooking water; no alcohol; `field_id_not_appropriate: true`) · [chanterelle](mushrooms/entries/chanterelle-new-england.md) (**jack-o'-lantern**, the most common mushroom poisoning call in the Northeast per Cornell; false chanterelle; cut every stem, orange inside means discard; `field_id_not_appropriate: true`) · [king bolete](mushrooms/entries/king-bolete-boletus.md) (*Boletus huronensis*, red-pored and blue-staining boletes, bitter bolete; no deadly look-alike named in New England by the sources opened, which is not a promise that none exists, but the group cannot be settled in the field and its look-alikes cause severe illness; `field_id_not_appropriate: true`; no alcohol) |
| **Game animals (3)** | [white-tailed deer](game-animals/entries/white-tailed-deer-new-england.md) (**CWD prion**; never brain, spinal cord, eyes, spleen, tonsils or lymph nodes; do not take a sick or found-dead animal; carcass import rules differ by state, so debone before you cross a line and read the destination state's agency page) · [ruffed grouse](game-animals/entries/ruffed-grouse.md) (**protected spruce grouse**: no open season in Maine and New Hampshire, state endangered in Vermont and New York; do not shoot a grouse you cannot tell from one; bird flu; gloves) · [snowshoe hare](game-animals/entries/snowshoe-hare.md) (**tularemia**, gloves; discard if the liver has white pinhead spots; **protected New England cottontail**) |
| **Crops (3)** | [short-season potato](crops/entries/potato-short-season.md) (green, sprouted or bitter tubers carry solanine; cooking does not remove it; throw out heavily green or bitter ones) · [cold-hardy cabbage and kale](crops/entries/cabbage-and-kale-cold-hardy.md) (no mandatory preparation; no home canning method given for cabbage or kale) · [maple sap and syrup](crops/entries/maple-sap-and-syrup.md) (carbon monoxide and fire: boil outdoors only; lead from old galvanized or lead-soldered gear; burns; sap spoils like milk) |
| **Hazards (3)** | [toxic plants](hazards/entries/toxic-plants-new-england.md) (false hellebore, water hemlock, poison hemlock, giant hogweed and wild parsnip, poison ivy) · [ticks](hazards/entries/ticks-new-england.md) (Lyme and others, Powassan; alpha-gal) · [cold water and shoulder-season hypothermia](hazards/entries/cold-water-and-shoulder-season-hypothermia.md) |

### Hazards to know before you eat from each category

- **Plants:** ramps share early-spring woods with false hellebore and lily of the valley; an onion smell from one leaf in your hand is necessary but never sufficient, and no smell means stop. Fiddleheads are the one plant here with a timed cooking step, and bracken grows in the same country. A wild white umbel, a carrot-family root or a "wild ginseng" root dug in a swamp can be a hemlock: do not eat any of them ([toxic plants](hazards/entries/toxic-plants-new-england.md)).
- **Mushrooms:** the honey mushroom's look-alike, the deadly galerina, causes delayed liver and kidney failure with a day of apparent recovery in between; the chanterelle's look-alike, jack-o'-lantern, puts most victims in the emergency room; boletes in this region include species that cause severe stomach illness. A small first portion does not clear a doubtful mushroom. See the doctrine.
- **Game:** CWD (cooking does not destroy the prion; the states differ on what deer parts may be brought in, so read the destination state's agency page); tularemia in hare (gloves in every season); bird flu in wild birds; protected look-alikes change what you may shoot. Hunting and trapping are different legal systems; the entries cover hunting seasons only. State seasons change every year and no cited page gives a survival exemption.
- **Crops:** green or bitter potatoes; sap boiled indoors (carbon monoxide) or in lead-bearing gear.
- **Ticks:** blacklegged ticks can be active at any temperature above freezing; check yourself after any foraging or hunting day ([ticks](hazards/entries/ticks-new-england.md)).
- **Cold water:** cold shock can kill within seconds to two minutes of going in. The "1-10-1" timing rule is a rough guide that the National Center for Cold Water Safety calls a myth; do not count on a clock. A rescuer follows "reach, throw, row, don't go" and does not enter the water ([cold water](hazards/entries/cold-water-and-shoulder-season-hypothermia.md)).

### Not yet written for this region

Amatoxin mushrooms, rabies and wildlife bites, and venomous snakes have no entry in this pack. **Not yet
written for this region; see the Mid-Atlantic entry for general facts**, and treat its range, season and legal
notes as belonging to another region:

- Amatoxin (the poison in deadly galerina and the *Amanita* pattern): [Mid-Atlantic amatoxin entry](../mid-atlantic-appalachian/hazards/entries/amatoxin-mushrooms-amanita-galerina.md)
- Rabies and wildlife bites (any wild mammal you handle or that bites or scratches you): [Mid-Atlantic rabies entry](../mid-atlantic-appalachian/hazards/entries/rabies-and-wildlife-bites.md)
- Snakes: [Mid-Atlantic venomous snakes entry](../mid-atlantic-appalachian/hazards/entries/venomous-snakes-copperhead-rattlesnake.md)

Also answer from the universal [first-aid guide](../../06_first_aid.md) and say plainly that this region has no
entry of its own.

### Cook-to temperatures (internal; from the entries and [`05_food.md`](../../05_food.md#what-temperature-to-cook-to))

| Food | Cook to | Entry |
|------|---------|-------|
| Venison (white-tailed deer), every cut | **160 F** (stews, soups and casseroles 165 F) | [deer](game-animals/entries/white-tailed-deer-new-england.md) |
| Rabbit / hare | **165 F** | [snowshoe hare](game-animals/entries/snowshoe-hare.md) |
| Poultry and game birds (ruffed grouse) | **165 F** | [ruffed grouse](game-animals/entries/ruffed-grouse.md) |
| Squirrel, bear, wild pig, raccoon and other wild meat-eaters | **165 F** | no entry for this region; [food guide](../../05_food.md#what-temperature-to-cook-to) |
| Fish | **145 F** | [food guide, fishing](../../05_food.md#fishing) |
| Fiddleheads | Not a meat temperature: **boil 15 minutes or steam 10 to 12 minutes, throw out the water** | [fiddleheads](edible-plants/entries/fiddlehead-ostrich-fern.md) |

Cooking does not destroy the CWD prion, and cooking does not make a poisonous mushroom edible. The mushroom
entries give no cooking time or temperature; they say cook thoroughly and never eat the species raw.

---

## Season → what's worth pursuing here (orienting only; confirm in the indexes)

This mirrors [`seasonality.md`](seasonality.md). It tells you *what category to look at*, never *what you may
eat*. That decision always runs through the category index's positive-ID gate. Every window comes from the
linked entry; none is a promise for your woods, and the entries say no source gave a date for Concord, NH. Dates
move with latitude, elevation and the year.

| Season | Categories to look at | Notes |
|--------|-----------------------|-------|
| **Spring** (Mar–May) | Maple sap runs on freeze-thaw days (mid-February to early April in southern Maine; mid-March to late April in northern Maine) ([maple](crops/entries/maple-sap-and-syrup.md)); [ramps](edible-plants/entries/ramps-allium-tricoccum.md) (leaves up early to mid-May in Maine); [fiddleheads](edible-plants/entries/fiddlehead-ostrich-fern.md) (late April to early June); potatoes, cabbage and kale go in **before** your last frost ([potato](crops/entries/potato-short-season.md), [cabbage and kale](crops/entries/cabbage-and-kale-cold-hardy.md)); snowshoe hare seasons run to March in several states | False hellebore and ramps share the same weeks: matrix first. Water hemlock is most toxic in spring ([toxic plants](hazards/entries/toxic-plants-new-england.md)). Tick nymphs peak May and June ([ticks](hazards/entries/ticks-new-england.md)). Cold water: Northeast waters stay cold well into spring ([hypothermia](hazards/entries/cold-water-and-shoulder-season-hypothermia.md)). |
| **Summer** (Jun–Aug) | [Wild blueberry](edible-plants/entries/lowbush-blueberry-vaccinium.md) (August in Maine); [chanterelle](mushrooms/entries/chanterelle-new-england.md) (July to September per Bessette); [king bolete](mushrooms/entries/king-bolete-boletus.md) (June to October per Bessette); fall cabbage and kale are sown in midsummer to late August | Jack-o'-lantern fruits July to October, the same weeks as chanterelle ([chanterelle](mushrooms/entries/chanterelle-new-england.md)). Poison hemlock is in flower June to August ([toxic plants](hazards/entries/toxic-plants-new-england.md)). Ticks stay active. |
| **Fall** (Sep–Nov) | [Honey mushroom](mushrooms/entries/honey-mushroom-armillaria.md) (fall; late in cold weather for one species); king bolete to October; potatoes dug about mid-September; deer, ruffed grouse and hare seasons open by state (see [seasonality](seasonality.md)) | **Deadly galerina grows on the same wood in the same season as honey mushroom.** Adult tick activity rises again in October and November. A fall chill and a wet day can bring hypothermia. |
| **Winter** (Dec–Feb) | Stored potatoes and cabbage ([potato](crops/entries/potato-short-season.md), [cabbage and kale](crops/entries/cabbage-and-kale-cold-hardy.md)); late deer, grouse and hare seasons (hare to February, March or later by state); late-winter maple sap from mid-February in southern areas | Lean season for wild food: the wild-plant and mushroom entries give no winter window. Ticks can be active above freezing. |

---

## Reminders pulled from the priority order

- Calories per unit effort decide survival: **stored food → passive fishing → trapping → foraging →
  gardening** (`../../substrate/05_food/_index.md`). Do not burn more calories foraging than you gain. Every
  wild plant entry here calls its food a seasonal extra, not a staple (the edible-plants index says the same). Trapping and fishing rules are
  state law; see the [food guide](../../05_food.md).
- All surface water here needs treatment before drinking; pair any foraging plan with
  [`../../substrate/02_water/_index.md`](../../substrate/02_water/_index.md).
- Public land is regulated and each manager differs (for example Maine state parks and historic sites allow no
  gathering; Vermont bans commercial harvest of fiddleheads and ramps on state and conservation land, and its forests-and-parks rule says no plant may be uprooted or cut without a special written permit, with personal collecting allowed only for wild berries, fruits, seeds, nuts and mushrooms; New Hampshire's rule on all DRED properties bars removing, damaging or disturbing any plant; Acadia
  National Park prohibits taking mushrooms). Check the land manager. No entry claims a survival exemption.
- Cook **all** wild meat thoroughly to the temperatures in the table above; never eat brain, spinal cord, eyes,
  spleen, tonsils or lymph nodes of deer, or any animal that looks sick or was found dead.

> **The hub never overrides an entry's gate.** It routes you *to* the gate. If an entry says
> `field_id_not_appropriate`, this hub does not authorize eating; it tells you to get expert confirmation. When
> in doubt, go without.
