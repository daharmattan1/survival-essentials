# Mid-Atlantic / Appalachian — Hazards (HAZARD)

> The biome's environmental and biological threats — what to identify, avoid, and respond to. HAZARD
> entries (`../../../SCHEMAS.md` §8): identify → avoid → if exposed/bitten/stung → `## ⚠ WHEN IT'S AN
> EMERGENCY`. This index is the **cross-check** every food query routes through (does a deadly
> look-alike or toxic plant share the habitat?).
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Toxic-plant
> ID pairs also surface in [`../edible-plants/_index.md`](../edible-plants/_index.md).

---

## Hazard surface (this biome)

| Hazard | Type | Where/when here | Emergency threshold |
|--------|------|-----------------|---------------------|
| **Amatoxin mushrooms** — destroying angels (*Amanita bisporigera* and relatives), death cap (*A. phalloides*, introduced), deadly galerina (*Galerina marginata*) | fungus (ingestion) | Woods, lawns near trees, rotting logs; summer–fall (*Galerina* year-round, especially September to November per Missouri's wildlife agency) | Any suspected ingestion → call 1-800-222-1222 and go to a hospital **before** symptoms; a delay of many hours and a false recovery are the trap. Never eaten on field ID alone. [`amatoxin-mushrooms-amanita-galerina`](entries/amatoxin-mushrooms-amanita-galerina.md) |
| **Water hemlock** — *Cicuta maculata* | plant (ingestion) | Ditches, stream banks, pond edges, marshes; growing season | Any ingestion = 911 / Poison Help; seizures can begin within an hour. Most toxic plant in North America per USDA and CDC. [`water-hemlock-cicuta`](entries/water-hemlock-cicuta.md) |
| **Rabies** — raccoons, bats, skunks, foxes | animal (bite, scratch, saliva) | Year-round | Any bite, scratch or saliva exposure from a wild mammal, or a bat in a room with a sleeper or an unattended child → wash 15 min, then get medical help right away (at the very latest, a clinician or health department the same day: this guide's rule). [`rabies-and-wildlife-bites`](entries/rabies-and-wildlife-bites.md) |
| **Venomous snakes** — copperhead, timber rattlesnake; also cottonmouth (far southeastern Virginia) and eastern massasauga (a few sites in western Pennsylvania) | animal | Rocky slopes, leaf litter, woodpiles, swamps in the far southeast; warm weather, dawn/dusk | Any bite from a venomous or unidentified snake → call 911 or be driven to an emergency department right away; do not wait for symptoms and do not drive yourself. No tourniquet, cutting, suction or ice. [`venomous-snakes-copperhead-rattlesnake`](entries/venomous-snakes-copperhead-rattlesnake.md) |
| **Ticks & tick-borne illness** — blacklegged (Lyme, anaplasmosis, babesiosis, Powassan), lone star (alpha-gal syndrome, ehrlichiosis), American dog tick (Rocky Mountain spotted fever) | biological | Tall grass, brush, leaf litter, shady forest and sunny open ground; active on any warm day, nymphs most active late spring and early summer | Fever, severe headache or any rash within weeks of a tick bite → medical care and say you had a bite; do not wait for a bull's-eye. Powassan virus can pass in as little as 15 minutes. [`ticks-and-lyme`](entries/ticks-and-lyme.md) |
| **Toxic plants** — poison hemlock, wild parsnip and giant hogweed (sap burns in sunlight), poison ivy (water hemlock has its own entry above) | plant | Poison hemlock in disturbed ground, roadsides, ditches and streambanks; poison ivy across woods, fence rows and roadsides | Hemlock **ingestion** of any part = call 1-800-222-1222 and 911 for symptoms. Never eat a wild umbel on field ID. Sap on skin: wash, keep out of the sun. Poison ivy: never burn it, smoke can cause serious breathing problems. [`toxic-plants-hemlock-poison-ivy`](entries/toxic-plants-hemlock-poison-ivy.md) |

> **Hemlock is the overlap between this file and the food layer.** Water hemlock
> ([own entry](entries/water-hemlock-cicuta.md)) and poison hemlock are the deadly look-alikes of edible umbels (`../edible-plants/_index.md` matrix). Any food query
> touching wild carrots/parsnips/umbels **must** cross-check here. "Leaves of three, let it be" for
> poison ivy/oak.

> **Amatoxin mushrooms are the second overlap.** White-gilled *Amanita* with a ring and a cup, and small
> brown *Galerina* on rotting wood, share habitat with the mushrooms in
> [`../mushrooms/_index.md`](../mushrooms/_index.md). Any mushroom query cross-checks
> [`amatoxin-mushrooms-amanita-galerina`](entries/amatoxin-mushrooms-amanita-galerina.md).

## Synthesis & load order

The realistic threats here are **underfoot, on your skin and on your plate**, not large predators: a venomous snake
you stepped near, a tick you didn't find for a day, toxic plants and mushrooms you might mistake for food, and a
wild-animal bite that needs a same-day call because of rabies. The
control for all of them is **avoidance first** (watch hands/feet around rock and litter; tick checks +
covered skin; never eat an unconfirmed umbel or white-gilled mushroom; keep your distance from wildlife), then a known response and a clear emergency threshold.

```
1. This hazard surface (above)  — identify what shares your habitat/season
2. The hazard entry             — Identify → Avoid → If Exposed/Bitten/Stung → ⚠ WHEN IT'S AN EMERGENCY
3. For toxic plants / mushrooms — cross-link ../edible-plants/ deadly-look-alike matrix and ../mushrooms/ doctrine + matrix
4. First-aid response           → in the hazard entries themselves: snakebite, tick removal and
                                  plant exposure steps are in their own entries above. General first aid in
                                  ../../../substrate/06_first_aid/ : anaphylaxis-and-allergic-reaction,
                                  wound-infection-management (non-rabies bite care), and
                                  bleeding-control-and-shock (tourniquets are for bleeding, never snakebite)
5. CITE (CDC / state health / herpetological / extension — T1/T2)
```

## Manifest (present entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| venomous-snakes-copperhead-rattlesnake | entries/venomous-snakes-copperhead-rattlesnake.md | HAZARD | mid-atlantic-appalachian | warm weather, dawn/dusk | n/a | high | moderate | false | T1 | 8 | agent-verified |
| ticks-and-lyme | entries/ticks-and-lyme.md | HAZARD | mid-atlantic-appalachian | any warm day; nymphs late spring–early summer | n/a | high | low | false | T1 | 8 | agent-verified |
| amatoxin-mushrooms-amanita-galerina | entries/amatoxin-mushrooms-amanita-galerina.md | HAZARD | mid-atlantic-appalachian | summer–fall (*Galerina*: year-round, especially September–November) | deadly-toxic | lethal | deadly-lookalike-exists | true | T1 | 19 | agent-verified |
| water-hemlock-cicuta | entries/water-hemlock-cicuta.md | HAZARD | mid-atlantic-appalachian | growing season (June–August bloom) | deadly-toxic | lethal | deadly-lookalike-exists | true | T1 | 10 | agent-verified |
| rabies-and-wildlife-bites | entries/rabies-and-wildlife-bites.md | HAZARD | mid-atlantic-appalachian | year-round | n/a | lethal | none | false | T1 | 11 | agent-verified |
| toxic-plants-hemlock-poison-ivy | entries/toxic-plants-hemlock-poison-ivy.md | HAZARD | mid-atlantic-appalachian | growing season | deadly-toxic | lethal | deadly-lookalike-exists | true | T1 | 8 | agent-verified |

The three `draft` rows are Phase 17 additions. The three food-confusable hazards (amatoxin mushrooms,
water hemlock, toxic plants) carry `field_id_not_appropriate: true` in-entry. `toxic-plants-hemlock-poison-ivy` carries `edibility_status: deadly-toxic` / `hazard_severity:
lethal` / `confusability_level: deadly-lookalike-exists` (the hemlocks are the umbel look-alikes), `expert_id_required: true` and
cross-links the edible-plants matrix. Snakes and ticks are `hazard_severity: high` (ticks: Rocky Mountain spotted fever and Powassan can be life-threatening). Sources: CDC / state health
(T1).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/` (6 entries present).
- [x] Every entry file has a row (no orphans).
- [x] Required columns filled.
- [x] Each HAZARD entry carries `## ⚠ WHEN IT'S AN EMERGENCY`; the toxic-plants entry cross-links the
      edible-plants deadly-look-alike matrix (hemlock overlap).
- [x] `hazard_severity: high|lethal` rows cite a T1 source.
