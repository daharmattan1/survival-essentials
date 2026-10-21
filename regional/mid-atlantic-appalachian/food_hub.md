# Mid-Atlantic / Appalachian — Food Decision Hub

> **"What can I eat here, and what could kill me?"** This is the single retrieval surface that
> composes plants + mushrooms + game + crops + seasonality + hazards into one season-indexed decision
> flow. Every food/consumption query for this biome resolves **through here** (retrieval recipe A in
> [`../../AGENTS.md`](../../AGENTS.md)) — and **always** routes through the deadly-look-alike matrix
> and `hazards/` **before** any edible exemplar.
>
> Biome profile: [`_index.md`](_index.md). Registry: [`../_index.md`](../_index.md). Calendar:
> [`seasonality.md`](seasonality.md).

---

> ## ⚠ Read this before any "can I eat it" answer (answer policy)
>
> - **Positive ID or do not consume.** Nothing here is edible on one trait, one photo, or the absence
>   of a warning. Every consumable entry carries a positive-ID checklist of *multiple concurrent*
>   traits + disqualifying "do-NOT-use-if" traits.
> - **Uncertainty-first.** Lead with the safety gate and the positive-ID checklist, **not** a verdict.
> - **Mushrooms and toxic-plant look-alikes can kill even careful people.** For any species flagged
>   `expert_id_required` / `field_id_not_appropriate`, **refuse** to confirm "yes, eat it" on a
>   description or photo alone. Every mushroom needs an expert who has examined the specimen in
>   hand (doctrine point 1 in [`mushrooms/_index.md`](mushrooms/_index.md)); spore print and
>   matching several sources come on top of that, never in place of it.
> - **"What can I eat?" always starts at the look-alike matrix and, for fungi, the mushroom doctrine.**
>   No list in this hub names a species as edible. Each name below is a link to the entry's gate.
> - **Reproduce `## ⚠ MANDATORY PREPARATION` verbatim** for anything that needs leaching, soaking or cooking.
> - **If someone may already have eaten an unknown plant or mushroom:** call Poison Help,
>   **1-800-222-1222**, now, even with no symptoms; call 911 for a seizure, collapse, trouble breathing
>   or if they cannot be woken; do not make them vomit unless Poison Control says to; keep a sample.
> - The absence of a warning is **missing data, not a green light.**

---

## The decision flow

```
"Can I eat X / what can I eat here right now?"
│
├─ 1. ORIENT to season  → seasonality.md  (what category is even available now?)
│
├─ 2. Pick the category and OPEN ITS INDEX — read the danger surface FIRST:
│      ├─ Wild plant?     → edible-plants/_index.md   → READ THE LOOK-ALIKE MATRIX, then the entry
│      │      onion/garlic/ramps · umbels · acorn/oak (buckeye twin) · cattail · violet/chickweed · dandelion
│      │      black walnut · pawpaw (ripe flesh only) · wild blackberry/raspberry
│      ├─ Mushroom?       → mushrooms/_index.md        → READ THE 9-POINT DOCTRINE + DEADLY-LOOK-ALIKE MATRIX, then the entry
│      │      morel · chicken-of-the-woods · oyster · chanterelle · wood ear/puffball
│      │      hen-of-the-woods · lion's mane · black trumpet   (all need an expert in hand)
│      ├─ Game/meat?      → game-animals/_index.md      → legal/season note + ⚠ DISEASE block
│      │      deer (CWD) · rabbit (tularemia) · squirrel · turkey (bird flu) · raccoon/opossum (roundworm, rabies, Trichinella)
│      └─ Grown food?     → crops/_index.md             → zone-7a planting/harvest windows + ⚠ MANDATORY PREPARATION
│             potato · dry beans · winter squash (bitter = discard) · kale/collards · flint corn · garlic (in oil = botulism) · sweet potato
│
├─ 3. CROSS-CHECK hazards → hazards/_index.md  (does a deadly look-alike or toxic plant share this habitat/season?)
│      amatoxin mushrooms · water hemlock · toxic plants (poison hemlock) · rabies · ticks · snakes
│
├─ 4. APPLY the entry's positive-ID gate + ⚠ MANDATORY PREPARATION (verbatim)
│
└─ 5. CITE the specific entries + their T1/T2 sources.  When in doubt → do NOT eat.
```

---

## Routing table — category → index → what leads it

| You're looking at… | Open | The danger surface it leads with | Cross-check |
|--------------------|------|----------------------------------|-------------|
| A **wild plant** (greens, roots, nuts, fruit) | [`edible-plants/_index.md`](edible-plants/_index.md) | **Look-alike matrix** (target → deadly or toxic look-alike → discriminators → what it does) | [`hazards/_index.md`](hazards/_index.md), especially [water hemlock](hazards/entries/water-hemlock-cicuta.md) and [toxic plants](hazards/entries/toxic-plants-hemlock-poison-ivy.md) |
| A **mushroom** | [`mushrooms/_index.md`](mushrooms/_index.md) | **Mushroom doctrine (9 points; expert in hand first) + deadly-look-alike matrix** | [`amatoxin-mushrooms-amanita-galerina`](hazards/entries/amatoxin-mushrooms-amanita-galerina.md) and [`hazards/_index.md`](hazards/_index.md) |
| **Game / meat** | [`game-animals/_index.md`](game-animals/_index.md) | Legal/season note + **⚠ DISEASE & PARASITE** (CWD prion, tularemia, raccoon roundworm, *Trichinella*, bird flu) | [`rabies-and-wildlife-bites`](hazards/entries/rabies-and-wildlife-bites.md), [`hazards/_index.md`](hazards/_index.md) |
| **Grown food** | [`crops/_index.md`](crops/_index.md) | Zone-7a planting/harvest windows, seed-saving, and **⚠ MANDATORY PREPARATION** (dry beans, flint corn, winter squash, garlic in oil) | — |
| **Processing technique** (gut/skin/cook/preserve) | [`../../substrate/05_food/_index.md`](../../substrate/05_food/_index.md) | Cook-thoroughly / never-eat rules (universal technique) | game `⚠ DISEASE` blocks |

### Entry routing (each link opens the gate first)

| Category | Entries (positive-ID gate or hazard block leads each one) |
|----------|-----------------------------------------------------------|
| **Wild plants (8)** | [wild onion / garlic / ramps](edible-plants/entries/wild-onion-garlic-allium.md) (death-camas twin) · [acorn / oak](edible-plants/entries/acorn-oak.md) (buckeye and horse chestnut twin; mandatory leaching) · [cattail](edible-plants/entries/cattail.md) (iris twin; clean water only) · [black walnut](edible-plants/entries/black-walnut-juglans.md) (coffeetree twin; moldy nuts; allergy) · [violet or chickweed](edible-plants/entries/violet-or-chickweed.md) · [dandelion](edible-plants/entries/dandelion.md) (spotted spurge, common groundsel, arnica) · [pawpaw](edible-plants/entries/pawpaw-asimina.md) (ripe flesh only; never skin, seeds, leaves or stems) · [wild blackberry / raspberry / wineberry](edible-plants/entries/wild-blackberry-raspberry-rubus.md) (sprayed roadsides, ticks) |
| **Mushrooms (8)** | [morel](mushrooms/entries/morel-morchella.md) (false morels, *Verpa*) · [chicken-of-the-woods](mushrooms/entries/chicken-of-the-woods-laetiporus.md) · [oyster](mushrooms/entries/oyster-pleurotus.md) · [chanterelle](mushrooms/entries/chanterelle-cantharellus.md) (jack-o'-lantern) · [wood ear / puffball](mushrooms/entries/wood-ear-or-puffball.md) (*Amanita* button, earthball) · [hen-of-the-woods](mushrooms/entries/hen-of-the-woods-grifola.md) · [lion's mane](mushrooms/entries/lions-mane-hericium.md) · [black trumpet](mushrooms/entries/black-trumpet-craterellus.md) |
| **Game animals (5)** | [white-tailed deer](game-animals/entries/white-tailed-deer.md) · [eastern cottontail rabbit](game-animals/entries/eastern-cottontail-rabbit.md) · [gray squirrel](game-animals/entries/gray-squirrel.md) · [wild turkey](game-animals/entries/wild-turkey.md) · [raccoon or opossum](game-animals/entries/raccoon-or-opossum.md) |
| **Crops (7)** | [potato](crops/entries/potato.md) · [dry beans](crops/entries/beans-dry.md) · [winter squash](crops/entries/winter-squash.md) · [kale and collards](crops/entries/kale-collards.md) · [flint corn](crops/entries/corn-flint.md) · [garlic](crops/entries/garlic.md) · [sweet potato](crops/entries/sweet-potato.md) |
| **Hazards (6)** | [amatoxin mushrooms](hazards/entries/amatoxin-mushrooms-amanita-galerina.md) · [water hemlock](hazards/entries/water-hemlock-cicuta.md) · [toxic plants incl. poison hemlock](hazards/entries/toxic-plants-hemlock-poison-ivy.md) · [rabies and wildlife bites](hazards/entries/rabies-and-wildlife-bites.md) · [ticks and Lyme](hazards/entries/ticks-and-lyme.md) · [venomous snakes](hazards/entries/venomous-snakes-copperhead-rattlesnake.md) |

### Hazards to know before you eat from each category

- **Plants:** acorns must be leached and have a potentially fatal look-alike nut (buckeye, horse chestnut); pawpaw skin, seeds, leaves and stems are not food; a poisonous coffeetree grows near walnut; wild umbels (the two hemlocks) and wild onion (death camas) can kill.
- **Mushrooms:** *Amanita* poisoning is delayed and a false recovery follows; jack-o'-lantern mimics chanterelle and oyster; false morels; puffball must be cut open top to bottom. See the doctrine.
- **Game:** CWD (never eat brain, spinal cord, eyes, spleen, tonsils or lymph nodes of deer; do not take sick animals); tularemia (rabbit, squirrel; gloves in every season); raccoon roundworm (life-threatening; gloves, hands away from the face, wash up); rabies (raccoon, bats and others); bird flu in wild turkey; *Trichinella*.
- **Crops:** raw or undercooked dry beans; flint corn as a staple without alkali treatment; a **bitter squash is thrown away whole**; green or bitter potatoes; garlic held in oil at room temperature (botulism).

### Cook-to temperatures (internal; from the entries and [`05_food.md`](../../05_food.md#what-temperature-to-cook-to))

| Food | Cook to | Entry |
|------|---------|-------|
| Venison (white-tailed deer) | **160 F** | [deer](game-animals/entries/white-tailed-deer.md) |
| Rabbit / hare | **165 F** | [rabbit](game-animals/entries/eastern-cottontail-rabbit.md) |
| Squirrel | **165 F** | [squirrel](game-animals/entries/gray-squirrel.md) |
| Raccoon, opossum, bear, wild pig and other wild meat-eaters | **165 F** | [raccoon / opossum](game-animals/entries/raccoon-or-opossum.md) |
| Poultry and game birds (wild turkey) | **165 F** | [turkey](game-animals/entries/wild-turkey.md) |
| Fish | **145 F** | [food guide, fishing](../../05_food.md#fishing) |

Cooking does not destroy the CWD prion and does not remove a bitter-squash toxin.

---

## Season → what's worth pursuing here (orienting only — confirm in the indexes)

This mirrors [`seasonality.md`](seasonality.md). It tells you *what category to look at*, never *what
you may eat*. That decision always runs through the category index's positive-ID gate. Every window
comes from the linked entry; none is a promise for your woods, and most entries say no Mid-Atlantic agency
dates were found.

| Season (7a lowland) | Categories to look at | Notes |
|---------------------|-----------------------|-------|
| **Spring** (Mar–May) | Wild onion leaves ([death-camas twin](edible-plants/entries/wild-onion-garlic-allium.md)); [violet / chickweed](edible-plants/entries/violet-or-chickweed.md); [dandelion](edible-plants/entries/dandelion.md); [cattail shoots](edible-plants/entries/cattail.md); [morel](mushrooms/entries/morel-morchella.md) (March through June by latitude and altitude per Kuo); spring turkey (about mid-April to late May, bearded birds); potatoes, kale and collards go in | Morels carry false-morel and *Verpa* look-alikes: doctrine first. Ticks are active; water hemlock is most toxic in spring ([entry](hazards/entries/water-hemlock-cicuta.md)). |
| **Summer** (Jun–Aug) | [Brambles](edible-plants/entries/wild-blackberry-raspberry-rubus.md) (June to August); [black trumpet](mushrooms/entries/black-trumpet-craterellus.md) (about June to early October); [chanterelle](mushrooms/entries/chanterelle-cantharellus.md) (July typical); [chicken-of-the-woods](mushrooms/entries/chicken-of-the-woods-laetiporus.md) (summer and fall); [oyster](mushrooms/entries/oyster-pleurotus.md) (*P. pulmonarius*, late April to September); [garlic](crops/entries/garlic.md) dug about July 1 in central Maryland; sow fall kale and collards | Jack-o'-lantern fruits July to October, the same weeks as chanterelle. *Amanita* and water hemlock share the season ([amatoxin](hazards/entries/amatoxin-mushrooms-amanita-galerina.md), [water hemlock](hazards/entries/water-hemlock-cicuta.md), flowers June to August). Ticks: nymphs most active in late spring and early summer ([entry](hazards/entries/ticks-and-lyme.md)). Heat: [`../../substrate/06_first_aid/_index.md`](../../substrate/06_first_aid/_index.md). |
| **Fall** (Sep–Nov) | [Acorns](edible-plants/entries/acorn-oak.md) (September to November; buckeye twin; mandatory leaching); [black walnut](edible-plants/entries/black-walnut-juglans.md) (October); [pawpaw](edible-plants/entries/pawpaw-asimina.md) (August to October); [hen-of-the-woods](mushrooms/entries/hen-of-the-woods-grifola.md) (September to November); [lion's mane](mushrooms/entries/lions-mane-hericium.md) (August to November); winter squash (September or October), [sweet potato](crops/entries/sweet-potato.md) dug before frost; garlic planted in October; [kale and collards](crops/entries/kale-collards.md) harvested well into fall (a protected spot extends it); deer, small game and fall turkey seasons | Mast is the main wild-calorie window, but acorns need mandatory leaching and the entry gives no tested schedule. Deadly *Galerina* is most reported September to November ([amatoxin](hazards/entries/amatoxin-mushrooms-amanita-galerina.md)). Before any fall mushroom, read the [mushroom doctrine and deadly-look-alike matrix](mushrooms/_index.md) (jack-o'-lantern, *Galerina*, destroying angels): this row lists only edible targets. |
| **Winter** (Dec–Feb) | Stored and preserved food from the crop entries; small game (rabbit and squirrel seasons run to February, raccoon and opossum to late February, or March 10 for Virginia hunting); oyster (*P. ostreatus*, late fall to early spring) | Lean season: no wild plant entry gives a winter season, and cattail has no sourced rhizome season. Conserve energy. |

---

## Reminders pulled from the priority order

- Calories per unit effort decide survival: **stored food → passive fishing → trapping → foraging →
  gardening** (`../../substrate/05_food/_index.md`). Don't burn more calories foraging than you gain.
  Trapping and fishing rules are state law; see the [food guide](../../05_food.md).
- All surface water here needs treatment before drinking — pair any foraging plan with
  [`../../substrate/02_water/_index.md`](../../substrate/02_water/_index.md).
- Cook **all** wild meat thoroughly to the temperatures in the table above; never eat brain, spinal
  cord, eyes, spleen, tonsils or lymph nodes of deer, or any animal that looks sick or was found dead
  (see the game `⚠ DISEASE & PARASITE` blocks).

> **The hub never overrides an entry's gate.** It routes you *to* the gate. If the entry says
> `field_id_not_appropriate`, this hub does not authorize eating — it tells you to get expert
> confirmation. When in doubt, go without.
