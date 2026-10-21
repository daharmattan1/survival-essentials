# Northeast / New England: Biome Profile

> The second region pack. New Hampshire, Vermont, Maine, Massachusetts, Connecticut, Rhode Island and
> upstate and eastern New York, referenced to **Concord, New Hampshire**. This profile is the doorway to the
> biome's biology; for a food or consumption question go to [`food_hub.md`](food_hub.md), and for the
> calendar go to [`seasonality.md`](seasonality.md).
>
> Registry: [`../_index.md`](../_index.md). Layer model and retrieval recipes: [`../../AGENTS.md`](../../AGENTS.md).

This is life-safety content. Every consumption answer leads with the positive-ID gate and the uncertainty,
never a verdict (`../../CONVENTIONS.md` §9). **Positive ID or do not consume.** All fifteen entries in this
pack are `review_status: draft`: written by an AI from opened agency and extension sources, not yet read by a
human reviewer.

---

## Biome at a glance

| Attribute | Value |
|-----------|-------|
| **USDA hardiness zone** | Region about **4b to 6b**. Concord sits in **5b** (average annual extreme minimum −15 to −10 F) on the USDA New Hampshire state map, 2023 edition, with zone 6a starting just to the south and east of the city and zone 4b across the northern hills [1][2] |
| **Reference point** | Concord, NH (the state capital, on the Merrimack River per the USDA map) |
| **Region covered** | NH, VT, ME, MA, CT, RI and upstate and eastern NY; zones about 4b to 6b. Rhode Island and New York have the thinnest source coverage in this pack: most entries cite Maine, New Hampshire and Vermont agencies, with a few Massachusetts, Connecticut and New York sources |
| **Average last spring freeze, Concord** | **May 8** (NWS Gray, Maine office, Concord normals, 1991 to 2020, labelled "Last Spring Freeze") [3] |
| **Average first fall freeze, Concord** | **October 3** (same sheet, labelled "First Fall Freeze"); growing season length **146 days** on the sheet [3] |
| **What UNH Extension says** | "For central NH, Memorial Day is a conservative estimate for the last frost date" [4]. First freeze "usually comes in early to mid-October" in central and southern NH and in mid-to-late September in the north; the page adds that the actual date shifts from year to year and with elevation [5] |
| **Precipitation** | About 42 inches of precipitation and about 68 inches of snow a year at Concord (NWS normals, 1991 to 2020) [3]. Plenty of surface water, but **all of it needs treatment** (see [`../../substrate/02_water/_index.md`](../../substrate/02_water/_index.md)) |
| **Elevation** | Higher ground and the northern hills run colder: later spring, earlier fall. Every date in this pack is a baseline for the Concord area, not for your woods. Check the local extension office |

**Frost dates, plainly.** The two agencies do not give the same number, because one is a measured average
(NWS: May 8 and October 3 at the Concord station) and the other is a conservative planting rule for gardeners
(UNH: Memorial Day for central NH). The crop entries in this pack use the UNH and UVM planting rules, and they
say they found no single Concord date of their own. Use the dates above as a starting point, then check the
local extension office for your own town and elevation. Frost can come outside any average.

**Where these figures come from.** The zone comes from the USDA state map image, read by eye at the Concord
star: the cell around the city is the 5b colour and the 6a colour starts a short distance south and east. A
third-party lookup service that repackages USDA map data returned 5b for ZIP 03301 as well, but it does not
state which edition it uses, so it is not a source here. The USDA Plant Hardiness Zone Map page itself is an
interactive map and states no zone for any town in its text: look up your own ZIP code there. Secondary garden
guides disagree on Concord (5a, 5b); they are not sources.

---

## What's in this pack

| Surface | File | Use |
|---------|------|-----|
| **Food decision hub** | [`food_hub.md`](food_hub.md) | "What can I eat here, and what could kill me?" Season-indexed; routes through the matrices, the mushroom doctrine and hazards first |
| **Seasonality calendar** | [`seasonality.md`](seasonality.md) | Month-by-month overview of foraging, hunting, growing and hazard windows (orienting overview, **not** an ID source) |
| **Edible plants (3)** | [`edible-plants/_index.md`](edible-plants/_index.md) | WILD-EDIBLE-PLANT entries. **Look-alike matrix leads the index**: ramps (false hellebore and lily of the valley), fiddleheads (bracken; confirmed in person the first time), wild blueberry |
| **Mushrooms (3)** | [`mushrooms/_index.md`](mushrooms/_index.md) | MUSHROOM entries. **9-point doctrine and deadly-look-alike matrix lead the index**: honey mushroom (deadly galerina), chanterelle (jack-o'-lantern), king bolete |
| **Game animals (3)** | [`game-animals/_index.md`](game-animals/_index.md) | GAME-ANIMAL entries. **Disease, look-alike and legal surface leads**: white-tailed deer (CWD; carcass import rules differ by state), ruffed grouse (protected spruce grouse), snowshoe hare (tularemia) |
| **Crops (3)** | [`crops/_index.md`](crops/_index.md) | CROP entries for a short season: short-season potato, cold-hardy cabbage and kale, maple sap and syrup |
| **Hazards (3)** | [`hazards/_index.md`](hazards/_index.md) | HAZARD entries: toxic plants (false hellebore, water hemlock, poison hemlock, sap-burn plants, poison ivy), cold water and shoulder-season hypothermia, ticks |

**Total: 15 entries** (edible plants 3, mushrooms 3, game animals 3, crops 3, hazards 3).

**Not yet written for this region:** amatoxin mushrooms, rabies and wildlife bites, and venomous snakes. The
[Mid-Atlantic entries](../mid-atlantic-appalachian/hazards/_index.md) for those hazards give general facts, but
their ranges, seasons and legal notes are for another region. Other game (cottontail, gray squirrel, wild
turkey, bear, moose, raccoon) and most wild plants and mushrooms have no entry here. An absent entry is missing
data, not a green light.

---

## Load order (this biome)

```
Food/consumption?  → food_hub.md  →  bio index (matrix/doctrine FIRST)  →  entry  →  cross-check hazards/
Mushroom?          → mushrooms/_index.md: the 9-point doctrine, then the deadly-look-alike matrix, then the entry
Just orienting?    → seasonality.md (what category is roughly in season now; NOT an ID source)
Hazard?            → hazards/_index.md
Always: positive ID or do not consume; for expert_id_required species (all three mushrooms, ramps, fiddleheads)
refuse a field-ID-only "yes."
If someone may already have eaten something unknown: Poison Help 1-800-222-1222 now; 911 for collapse,
seizure, trouble breathing or if they cannot be woken; do not induce vomiting; keep a sample.
```

## `check_manifests` (biome level)

- [ ] `food_hub.md` and `seasonality.md` both exist and link the five biology subfolders.
- [ ] Each biology subfolder has an `_index.md` and an `entries/` dir (15 entries in all, 3 per domain).
- [ ] `mushrooms/_index.md` leads with the doctrine and the deadly-look-alike matrix; `edible-plants/_index.md`
      leads with the look-alike matrix.
- [ ] Season windows trace to a linked entry; frost figures cite the sources below.
- [ ] Every figure above is dated and sourced; where a source gave no number the page says so.

---

## Sources

1. USDA Agricultural Research Service, "2023 USDA Plant Hardiness Zone Map, New Hampshire" (state map image, based on 1991 to 2020 data). https://planthardiness.ars.usda.gov/system/files/NH300_HS.png . Tier 1. Opened: downloaded and viewed; legend read as 5b = −15 to −10 F, 6a = −10 to −5 F, 4b = −25 to −20 F, 6b = −5 to 0 F.
2. USDA Agricultural Research Service, "USDA Plant Hardiness Zone Map" home page (2023 edition; interactive; zones by ZIP code or map click). https://planthardiness.ars.usda.gov/ . Tier 1. Opened: fetched; it states no zone for Concord.
3. NOAA National Weather Service, Gray, Maine, "Concord, NH: Temperature, Precipitation, Snowfall and Growing Season Normals (1991-2020)" (single-page seasonal sheet; last spring freeze May 8, first fall freeze October 3, growing season 146 days; annual precipitation 41.95 in; annual snowfall 67.7 in). https://www.weather.gov/media/gyx/climo/CONSeasonal.pdf . Tier 1. Opened: fetched the PDF and extracted its text. The extracted text labels the dates "freeze" and does not spell out the temperature threshold.
4. UNH Extension, "Growing Vegetables: When to Plant Your Vegetable Garden" (fact sheet). https://extension.unh.edu/resource/growing-vegetables-when-plant-your-vegetable-garden-fact-sheet . Tier 1. Opened: fetched; Memorial Day sentence for central NH.
5. UNH Extension, "Fall Vegetable Gardening: Tips for the Home Gardener in New Hampshire". https://extension.unh.edu/node/5598 . Tier 1. Opened: fetched; first-freeze statement for central, southern and northern NH, and that the date shifts with the year and elevation.
