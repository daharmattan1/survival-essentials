# Northeast / New England — Hazards (HAZARD)

> The biome's environmental and biological threats: what to identify, avoid, and respond to. HAZARD
> entries (`../../../SCHEMAS.md` §8): identify → avoid → if exposed/bitten/stung → `## ⚠ WHEN IT'S AN
> EMERGENCY`. This index is the **cross-check** every food query routes through (does a deadly
> look-alike or toxic plant share the habitat?).
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Toxic-plant ID pairs
> (ramps and false hellebore, wild umbels and the hemlocks) also belong in the edible-plants deadly-look-alike
> matrix of this biome.
>
> Region: New Hampshire, Vermont, Maine, Massachusetts, Connecticut, Rhode Island and upstate/eastern New
> York. All three entries are `draft`: AI-written from opened New England and New York agency sources, not yet
> read by a human reviewer.

---

## Hazard surface (this biome)

| Hazard | Type | Where/when here | Emergency threshold |
|--------|------|-----------------|---------------------|
| **False hellebore** — *Veratrum viride*, mistaken for ramps (wild leeks) in early spring | plant (ingestion) | Early spring; swamps, wet woods, stream banks, floodplains, and per Vermont "almost anywhere," including backyards and roadsides | Any suspected ingestion → call 1-800-222-1222 now; most people who ate it need the hospital. Vermont: do not wait for symptoms. Ramp leaves are flat and smell of onion; false hellebore leaves are pleated and ribbed, alternate up a stem with clasping bases (on a plant only a few inches tall the stem is not yet visible, and Vermont warns the two are easily confused at that stage). No single trait separates them: smell alone does not confirm a ramp, and a leaf stalk proves nothing either way (sources disagree). [`toxic-plants-new-england`](entries/toxic-plants-new-england.md) |
| **Water hemlock** — *Cicuta maculata* | plant (ingestion) | Marshes, wet edges, lake and river shores, all six New England states; most toxic in spring | Any ingestion = Poison Help 1-800-222-1222 and 911 for seizures; CDC records a Maine death about 3 hours after a few bites of root taken for wild ginseng. [`toxic-plants-new-england`](entries/toxic-plants-new-england.md) |
| **Poison hemlock** — *Conium maculatum* | plant (ingestion) | Roadsides, waste ground, fields, forest edges; June to August bloom | Any ingestion = Poison Help and 911 for symptoms; roots have been mistaken for wild carrot and parsnip, and seeds for caraway. [`toxic-plants-new-england`](entries/toxic-plants-new-england.md) |
| **Giant hogweed and wild parsnip** — sap burns in sunlight (cow parsnip is a look-alike of hogweed) | plant (skin, eyes) | Roadsides, fields, streams; wild parsnip common across New York; hogweed late June to July bloom | Wash with soap and water, keep out of sun, medical care for sap in the eyes or severe blistering. [`toxic-plants-new-england`](entries/toxic-plants-new-england.md) |
| **Poison ivy** | plant (skin, smoke) | Woods, fence rows, roadsides | Never burn it; 911 for swelling or trouble breathing. [`toxic-plants-new-england`](entries/toxic-plants-new-england.md) |
| **Cold-water immersion and shoulder-season hypothermia** | environmental | Spring and fall; Northeast waters stay cold well into spring; wet and wind on land in any season | Call 911 for any suspected hypothermia, right away if the person is confused or drowsy; anyone pulled from cold water. Life jacket worn, not carried. [`cold-water-and-shoulder-season-hypothermia`](entries/cold-water-and-shoulder-season-hypothermia.md) |
| **Ticks & tick-borne illness** — blacklegged (Lyme, anaplasmosis, babesiosis, Powassan including deer tick virus, hard tick relapsing fever), lone star (ehrlichiosis, alpha-gal syndrome), American dog tick (Rocky Mountain spotted fever) | biological | Tall grass, brush, leaf litter, stone walls and woods edges, lawns; nymphs peak May and June, adults again October and November; deer ticks can be active above freezing | Fever, severe headache or rash after any tick bite → medical care and say you had a bite. Confusion, loss of coordination, speech trouble or seizure → 911. Powassan can pass in as little as 15 minutes. [`ticks-new-england`](entries/ticks-new-england.md) |

> **Ramps and false hellebore are the food overlap in this file.** Any spring-greens or wild-leek query
> **must** cross-check [`toxic-plants-new-england`](entries/toxic-plants-new-england.md) before anything
> is eaten. Hemlocks are the second overlap: any wild white umbel, carrot-family root or "wild ginseng" dug in a
> swamp cross-checks the same entry.

> **Not yet written for this biome:** venomous snakes (timber rattlesnake, copperhead), rabies and
> wildlife bites, and amatoxin mushrooms. Until they exist, answer from the universal first-aid guide
> ([`../../../06_first_aid.md`](../../../06_first_aid.md)) and the biome's mushroom doctrine, and say so.

## Synthesis & load order

The realistic threats here are **in the water, on your skin and on your plate**, not large predators: a cold-water
dunking or a wet, windy day that turns into hypothermia, a tick you did not find for a day, an early-spring
green or a swamp root that is not what you thought. The control for all of them is **avoidance first** (wear the
life jacket and dress for the water, not the air; tick checks and covered skin; never eat a wild umbel, a
swamp root, or an unnamed spring green), then a known response and a clear emergency threshold.

```
1. This hazard surface (above)  — identify what shares your habitat/season
2. The hazard entry             — Identify → Avoid → If Exposed/Bitten/Stung → ⚠ WHEN IT'S AN EMERGENCY
3. For toxic plants             — read the positive-ID gate in toxic-plants-new-england first, then the biome's
                                  edible-plants deadly-look-alike matrix
4. First-aid response           → in the hazard entries themselves (tick removal, plant exposure, cold-water
                                  and hypothermia steps). General first aid in ../../../substrate/06_first_aid/ :
                                  thermal-injury-hypo-hyperthermia, anaphylaxis-and-allergic-reaction,
                                  wound-infection-management
5. CITE (CDC / state health / state agriculture / extension — T1/T2)
```

## Manifest (present entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| toxic-plants-new-england | entries/toxic-plants-new-england.md | HAZARD | northeast-new-england | early spring (false hellebore); growing season, June–August bloom (hemlocks, wild parsnip); late June–July (giant hogweed) | deadly-toxic | lethal | deadly-lookalike-exists | true | T1 | 18 | agent-verified |
| cold-water-and-shoulder-season-hypothermia | entries/cold-water-and-shoulder-season-hypothermia.md | HAZARD | northeast-new-england | spring and fall; any wet, windy day | n/a | lethal | none | false | T1 | 8 | agent-verified |
| ticks-new-england | entries/ticks-new-england.md | HAZARD | northeast-new-england | any warm day; nymphs May–June; adults October–November | n/a | high | low | false | T1 | 13 | agent-verified |

`toxic-plants-new-england` carries `field_id_not_appropriate: true` in-entry (false hellebore with ramps; the
hemlocks with edible umbels and roots) and opens with the positive-ID safety gate. Ticks are `hazard_severity:
high` (Powassan encephalitis is fatal in about 10 percent of cases per New York's health department; this is
the same rating the Mid-Atlantic tick entry uses). Cold water and hypothermia is `lethal`: a fall into cold water
and untreated hypothermia both kill. Sources: CDC, NWS, state health, agriculture and environment agencies (T1);
Cornell Weed ID, Go Botany and a peer-reviewed Maine study (T2).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/` (3 entries present).
- [x] Every entry file has a row (no orphans).
- [x] Required columns filled.
- [x] Each HAZARD entry carries `## ⚠ WHEN IT'S AN EMERGENCY`; the toxic-plants entry opens with the positive-ID
      gate and names its edible look-alikes (ramps, parsnip, wild carrot, caraway, wild ginseng).
- [x] `hazard_severity: high|lethal` rows cite a T1 source.
