# Safety read 13: Northeast and New England pack

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 13 of 13. This pack repeats the Mid-Atlantic method for New England and eastern New York. It comes last only because the Mid-Atlantic packs and the substrate packs reach more readers. A wrong mushroom, ramp or hemlock call here is as dangerous as in domains 04 to 06.

## Time and status

- **Estimated time: 60 minutes at most** for the targeted check below (16 claims at about 2 minutes each; 6 species at about 1 minute each; 14 look-alike pairs at about 1 minute each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The 15 entries run about 39,604 words, roughly 158 minutes at 250 words per minute. They sit in five folders, so a full read is five sittings. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** every entry in this pack says `draft` today. AI agents wrote them and fact-checked them over several rounds. None has had a human review. An AI check is a first pass. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself, once per folder you read** (the script handles one folder at a time):

```
python scripts/mark_reviewed.py --domain regional/northeast-new-england/mushrooms --reviewer "Your Full Name"
python scripts/mark_reviewed.py --domain regional/northeast-new-england/edible-plants --reviewer "Your Full Name"
python scripts/mark_reviewed.py --domain regional/northeast-new-england/hazards --reviewer "Your Full Name"
python scripts/mark_reviewed.py --domain regional/northeast-new-england/game-animals --reviewer "Your Full Name"
python scripts/mark_reviewed.py --domain regional/northeast-new-england/crops --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md). Run it only for a folder whose entries you read.

## 1. Entries to read

Read the [New England mushroom doctrine and look-alike matrix](../regional/northeast-new-england/mushrooms/_index.md) first. It carries the same nine points as [CONVENTIONS.md](../CONVENTIONS.md) section 4. Then read the species entries, then the hazards, game and crops.

The king bolete and wild blueberry entries name no deadly look-alike. Both say that is missing data, not a promise. If you know of one, file it.

| Entry | Folder | Type | Severity | Look-alike level | Expert ID needed | Field ID not OK | Legal status | Tier | Status now | Words |
|---|---|---|---|---|---|---|---|---|---|---|
| [Golden Chanterelle (Cantharellus spp., New England)](../regional/northeast-new-england/mushrooms/entries/chanterelle-new-england.md) | Mushrooms | MUSHROOM | moderate | high | True | True | regulated | T2 | agent-verified | 3254 |
| [Honey Mushroom (Armillaria spp.)](../regional/northeast-new-england/mushrooms/entries/honey-mushroom-armillaria.md) | Mushrooms | MUSHROOM | lethal | deadly-lookalike-exists | True | True | regulated | T2 | agent-verified | 3390 |
| [King Bolete (Boletus edulis group)](../regional/northeast-new-england/mushrooms/entries/king-bolete-boletus.md) | Mushrooms | MUSHROOM | moderate | high | True | True | regulated | T2 | agent-verified | 2869 |
| [Ramps / Wild Leek (Allium tricoccum): FALSE HELLEBORE ALERT](../regional/northeast-new-england/edible-plants/entries/ramps-allium-tricoccum.md) | Edible plants | WILD-EDIBLE-PLANT | lethal | deadly-lookalike-exists | True | True | regulated | T1 | agent-verified | 3258 |
| [Fiddleheads (Ostrich Fern, Matteuccia struthiopteris): COOK THEM, AND KNOW THE FERN](../regional/northeast-new-england/edible-plants/entries/fiddlehead-ostrich-fern.md) | Edible plants | WILD-EDIBLE-PLANT | moderate | moderate | True | False | regulated | T1 | agent-verified | 2797 |
| [Wild Blueberry (Lowbush, Vaccinium angustifolium, and Highbush)](../regional/northeast-new-england/edible-plants/entries/lowbush-blueberry-vaccinium.md) | Edible plants | WILD-EDIBLE-PLANT | low | low | False | False | regulated | T1 | agent-verified | 1949 |
| [Toxic Plants of New England and New York: False Hellebore, Water Hemlock, Poison Hemlock, Sap-Burn Umbels & Poison Ivy](../regional/northeast-new-england/hazards/entries/toxic-plants-new-england.md) | Hazards | HAZARD | lethal | deadly-lookalike-exists | True | True | n/a | T1 | agent-verified | 2822 |
| [Ticks & Tick-Borne Illness in New England and New York (Lyme, Anaplasmosis, Babesiosis, Powassan)](../regional/northeast-new-england/hazards/entries/ticks-new-england.md) | Hazards | HAZARD | high | low | False | False | n/a | T1 | agent-verified | 2096 |
| [Cold-Water Immersion & Shoulder-Season Hypothermia (New England and New York)](../regional/northeast-new-england/hazards/entries/cold-water-and-shoulder-season-hypothermia.md) | Hazards | HAZARD | lethal | none | False | False | n/a | T1 | agent-verified | 1754 |
| [Ruffed Grouse, "Partridge" (Bonasa umbellus)](../regional/northeast-new-england/game-animals/entries/ruffed-grouse.md) | Game animals | GAME-ANIMAL | moderate | moderate | False | False | regulated | T1 | agent-verified | 2187 |
| [Snowshoe Hare, Varying Hare (Lepus americanus)](../regional/northeast-new-england/game-animals/entries/snowshoe-hare.md) | Game animals | GAME-ANIMAL | high | moderate | False | False | regulated | T1 | agent-verified | 2508 |
| [White-Tailed Deer in New England and New York (Odocoileus virginianus)](../regional/northeast-new-england/game-animals/entries/white-tailed-deer-new-england.md) | Game animals | GAME-ANIMAL | high | none | False | False | regulated | T1 | agent-verified | 2830 |
| [Maple Sap and Syrup (Acer saccharum, Acer rubrum)](../regional/northeast-new-england/crops/entries/maple-sap-and-syrup.md) | Crops | CROP | high | low | False | False | regulated | T1 | agent-verified | 2590 |
| [Potato, Short-Season Northeast (Solanum tuberosum)](../regional/northeast-new-england/crops/entries/potato-short-season.md) | Crops | CROP | low | none | False | False | n/a | T1 | agent-verified | 2823 |
| [Cabbage and Kale, Cold-Hardy Brassicas (Brassica oleracea)](../regional/northeast-new-england/crops/entries/cabbage-and-kale-cold-hardy.md) | Crops | CROP | none | none | False | False | n/a | T1 | agent-verified | 2477 |

## 2. Species: the positive-ID gate

Open each source. Check the traits in the entry's positive-ID checklist, and the disqualifying traits, against it. The two links are the sources the entry cites most often inside its gate, with a page named for the species ranked first. Only Tier 1 and Tier 2 sources are listed. "Gate lines" are the line numbers of the gate section. The toxic-plants entry has its own gate, covered in the look-alike table below.

| Species | Gate lines | Source 1 | Source 2 | Check |
|---|---|---|---|---|
| [Golden Chanterelle (Cantharellus spp.)](../regional/northeast-new-england/mushrooms/entries/chanterelle-new-england.md) | 114-139 | [T2: AmericanMushrooms.com (David W. Fischer), Cantharellus cibarius (sample description from Mush...](https://americanmushrooms.com/monenasamples.htm) | [T1: Missouri Department of Conservation (identification and edibility statements; not a New Engla...](https://mdc.mo.gov/discover-nature/field-guide/chanterelles) | &#9744; |
| [Honey Mushroom (Armillaria spp.)](../regional/northeast-new-england/mushrooms/entries/honey-mushroom-armillaria.md) | 111-140 | [T2: MushroomExpert.Com (Michael Kuo); identification only, the site disclaims toxicity, Armillari...](https://www.mushroomexpert.com/armillaria_mellea.html) | [T1: Missouri Department of Conservation (identification and edibility statements only; not a New...](https://mdc.mo.gov/discover-nature/field-guide/honey-mushroom) | &#9744; |
| [King Bolete (Boletus edulis group)](../regional/northeast-new-england/mushrooms/entries/king-bolete-boletus.md) | 103-128 | [T2: Reproduced on Berthold K. P. Horn's Boletes pages, MIT CSAIL, Boletus edulis (species entry f...](https://people.csail.mit.edu/bkph/Boletes/pages/Boletus_edulis.html) | [T2: MushroomExpert.Com (Michael Kuo); identification only, the site disclaims toxicity, Boletus e...](https://www.mushroomexpert.com/boletus_edulis.html) | &#9744; |
| [Ramps (Allium tricoccum)](../regional/northeast-new-england/edible-plants/entries/ramps-allium-tricoccum.md) | 129-152 | [T2: Native Plant Trust, Allium tricoccum (ramps, wild leek), Go Botany](https://gobotany.nativeplanttrust.org/species/allium/tricoccum/) | [T1: NC State Extension Gardener Plant Toolbox, Allium tricoccum (Ramps, Wild Leek)](https://plants.ces.ncsu.edu/plants/allium-tricoccum/) | &#9744; |
| [Fiddlehead (Matteuccia struthiopteris)](../regional/northeast-new-england/edible-plants/entries/fiddlehead-ostrich-fern.md) | 104-127 | [T1: University of Maine Cooperative Extension, Bulletin #2540, Ostrich Fern Fiddleheads, Matteucc...](https://extension.umaine.edu/publications/2540e/) | [T1: University of Maine Cooperative Extension, Bulletin #4198, Facts on Fiddleheads](https://extension.umaine.edu/publications/4198e/) | &#9744; |
| [Wild Blueberry (Vaccinium angustifolium)](../regional/northeast-new-england/edible-plants/entries/lowbush-blueberry-vaccinium.md) | 97-117 | [T2: Native Plant Trust, Vaccinium angustifolium (common lowbush blueberry), Go Botany](https://gobotany.nativeplanttrust.org/species/vaccinium/angustifolium/) | [T1: NC State Extension Gardener Plant Toolbox, Vaccinium angustifolium (Late Lowbush Blueberry, L...](https://plants.ces.ncsu.edu/plants/vaccinium-angustifolium/) | &#9744; |

## 3. Look-alike pairs: two sources each

CONVENTIONS section 7 needs each look-alike checked against at least two Tier 1 or Tier 2 sources. The two links are the sources the entry cites for that look-alike, with a page named for the look-alike first. "First line" is the first line that names it. If a row says only one source is cited, finding the second is part of your job. A T3 source does not count toward the two. Check that the entry's stated difference, and what the look-alike does to a person, match both sources.

| Species | Look-alike | First line | Source 1 | Source 2 | Check |
|---|---|---|---|---|---|
| [Golden Chanterelle (Cantharellus spp.)](../regional/northeast-new-england/mushrooms/entries/chanterelle-new-england.md) | Jack-o'-lantern (Omphalotus illudens) | 116 | [T2: MushroomExpert.Com (Michael Kuo); identification only, Omphalotus illudens](https://mushroomexpert.com/omphalotus_illudens.html) | [T1: Missouri Department of Conservation, Jack-o'-Lantern (Omphalotus illudens)](https://mdc.mo.gov/discover-nature/field-guide/jack-o-lantern) | &#9744; |
| [Golden Chanterelle (Cantharellus spp.)](../regional/northeast-new-england/mushrooms/entries/chanterelle-new-england.md) | False chanterelle (Hygrophoropsis aurantiaca) | 116 | [T2: MushroomExpert.Com (Michael Kuo); identification only, Hygrophoropsis aurantiaca](https://mushroomexpert.com/hygrophoropsis_aurantiaca.html) | [T1: USDA Forest Service, Northern Research Station, Field Guide to Common Macrofungi in Eastern F...](https://www.nrs.fs.usda.gov/pubs/gtr/gtr_nrs79r.pdf) | &#9744; |
| [Golden Chanterelle (Cantharellus spp.)](../regional/northeast-new-england/mushrooms/entries/chanterelle-new-england.md) | Scaly vase (Turbinellus floccosus) | 121 | [T2: MushroomExpert.Com (Michael Kuo); identification only, the site disclaims toxicity, Turbinell...](https://www.mushroomexpert.com/turbinellus_floccosus.html) | [T2: North American Mycological Association, Thirty-Plus Years of Mushroom Poisoning, Summary of t...](https://namyco.org/wp-content/uploads/2023/08/Poisonings30year.pdf) | &#9744; |
| [Honey Mushroom (Armillaria spp.)](../regional/northeast-new-england/mushrooms/entries/honey-mushroom-armillaria.md) | Deadly galerina (Galerina marginata) | 113 | [T1: Missouri Department of Conservation, Deadly Galerina (Galerina marginata)](https://mdc.mo.gov/discover-nature/field-guide/deadly-galerina) | [T2: MushroomExpert.Com (Michael Kuo); identification only, Galerina marginata](https://mushroomexpert.com/galerina_marginata.html) | &#9744; |
| [Honey Mushroom (Armillaria spp.)](../regional/northeast-new-england/mushrooms/entries/honey-mushroom-armillaria.md) | Jack-o'-lantern (Omphalotus illudens) | 128 | [T1: Missouri Department of Conservation, Jack-o'-Lantern (Omphalotus illudens)](https://mdc.mo.gov/discover-nature/field-guide/jack-o-lantern) | [T1: Missouri Department of Conservation (identification and edibility statements only; not a New...](https://mdc.mo.gov/discover-nature/field-guide/honey-mushroom) | &#9744; |
| [King Bolete (Boletus edulis group)](../regional/northeast-new-england/mushrooms/entries/king-bolete-boletus.md) | Boletus huronensis | 111 | [T2: North American Mycological Association, Boletus huronensis (Bill Bakaitis), McIlvainea](https://namyco.org/publications/mcilvainea-journal-of-american-amateur-mycology/boletus-huronensis/) | **only one source cited in the entry: find a second** | &#9744; |
| [King Bolete (Boletus edulis group)](../regional/northeast-new-england/mushrooms/entries/king-bolete-boletus.md) | Red-pored and blue-staining boletes (Frost's bolete, B. subvelutipes group) | 105 | [T1: Missouri Department of Conservation (identification and the red-pore caution; not a New Engla...](https://mdc.mo.gov/discover-nature/field-guide/frosts-bolete) | [T2: Reproduced on Berthold K. P. Horn's Boletes pages, MIT CSAIL, Boletus frostii (species entry...](https://people.csail.mit.edu/bkph/Boletes/pages/Boletus_frostii.html) | &#9744; |
| [King Bolete (Boletus edulis group)](../regional/northeast-new-england/mushrooms/entries/king-bolete-boletus.md) | Bitter bolete (Tylopilus felleus) | 113 | [T2: Reproduced on Berthold K. P. Horn's Boletes pages, MIT CSAIL, Tylopilus felleus (species entr...](https://people.csail.mit.edu/bkph/Boletes/pages/Tylopilus_felleus.html) | [T2: MushroomExpert.Com (Michael Kuo); identification only, Tylopilus felleus](https://www.mushroomexpert.com/tylopilus_felleus.html) | &#9744; |
| [Ramps (Allium tricoccum)](../regional/northeast-new-england/edible-plants/entries/ramps-allium-tricoccum.md) | American false hellebore (Veratrum viride) | 131 | [T2: Native Plant Trust, Veratrum viride (American false hellebore), Go Botany](https://gobotany.nativeplanttrust.org/species/veratrum/viride/) | [T1: NC State Extension Gardener Plant Toolbox, Veratrum viride (False Hellebore, Indian Poke)](https://plants.ces.ncsu.edu/plants/veratrum-viride/) | &#9744; |
| [Ramps (Allium tricoccum)](../regional/northeast-new-england/edible-plants/entries/ramps-allium-tricoccum.md) | Lily of the valley (Convallaria majalis) | 134 | [T2: Native Plant Trust, Convallaria majalis (European lily-of-the-valley), Go Botany](https://gobotany.nativeplanttrust.org/species/convallaria/majalis/) | [T1: NC State Extension Gardener Plant Toolbox, Convallaria majalis (Lily of the Valley)](https://plants.ces.ncsu.edu/plants/convallaria-majalis/) | &#9744; |
| [Fiddlehead (Matteuccia struthiopteris)](../regional/northeast-new-england/edible-plants/entries/fiddlehead-ostrich-fern.md) | Bracken fern (Pteridium aquilinum) | 106 | [T2: Native Plant Trust, Pteridium aquilinum (bracken fern), Go Botany](https://gobotany.nativeplanttrust.org/species/pteridium/aquilinum/) | [T1: NC State Extension Gardener Plant Toolbox, Pteridium latiusculum (Bracken Fern, Eastern Brack...](https://plants.ces.ncsu.edu/plants/pteridium-latiusculum/) | &#9744; |
| [Fiddlehead (Matteuccia struthiopteris)](../regional/northeast-new-england/edible-plants/entries/fiddlehead-ostrich-fern.md) | Lady fern | 124 | [T1: State of Alaska Plant Materials Center, Alaska Plant Profiles: Fiddlehead Ferns (an Alaska do...](https://plants.alaska.gov/pdf/Fiddleheads.pdf) | **only one source cited in the entry: find a second** | &#9744; |
| [Toxic Plants of New England and New York](../regional/northeast-new-england/hazards/entries/toxic-plants-new-england.md) | Water hemlock (Cicuta maculata) | 97 | [T2: Native Plant Trust, Cicuta maculata (spotted water-hemlock), Go Botany](https://gobotany.nativeplanttrust.org/species/cicuta/maculata/) | [T2: Cornell University, Weed Identification, Spotted Water Hemlock](https://blogs.cornell.edu/weedid/spotted-water-hemlock/) | &#9744; |
| [Toxic Plants of New England and New York](../regional/northeast-new-england/hazards/entries/toxic-plants-new-england.md) | Poison hemlock (Conium maculatum) | 97 | [T2: Native Plant Trust, Conium maculatum (poison-hemlock), Go Botany](https://gobotany.nativeplanttrust.org/species/conium/maculatum/) | [T2: Cornell University, Weed Identification, Poison Hemlock](https://blogs.cornell.edu/weedid/poison-hemlock/) | &#9744; |

Notes on the pairs:

- **Jack-o'-lantern under honey mushroom:** both links are Missouri pages. The Kuo and Cornell pages for it are in the chanterelle entry's sources, so use those as well.
- **Red-pored boletes:** the two links disagree about Frost's bolete. Missouri says edible but not recommended because of red-pored look-alikes. Bessette lists it as simply edible. The entry says do not eat it.
- **Lady fern:** the one source is Alaska's state plant profile, which treats a western lady fern. The entry says so. A New England source for it is the gap.
- **Wild blueberry:** the entry names no poisonous blueberry look-alike. It lists black nightshade and bluebead lily as poisonous berry plants that could be picked by mistake. Check those two against the NC State and Go Botany pages in the entry's Sources.

## 4. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "Cut the stem lengthwise on every mushroom. The flesh is white inside, which may have yellow edges, and is not orange \[4\]\[6\]\[7\]." | [chanterelle-new-england.md](../regional/northeast-new-england/mushrooms/entries/chanterelle-new-england.md), line 121 | [T3: Foray Newfoundland and Labrador (amateur mycological organization newsletter), The chanterell...](https://www.mykoweb.com/misc/Omphalina/O-VIII-4.pdf)<br>[T2: MushroomExpert.Com (Michael Kuo); identification only, Cantharellus lateritius (smooth chante...](https://mushroomexpert.com/cantharellus_lateritius.html)<br>[T2: AmericanMushrooms.com (David W. Fischer), Cantharellus cibarius (sample description from Mush...](https://americanmushrooms.com/monenasamples.htm) | &#9744; ok<br>&#9744; flag |
| 2 | "The NAMA registry lists 3 adults with stomach distress, 2 of them with severe cramps, in Colorado, Maine and West Virginia \[15\]" | [chanterelle-new-england.md](../regional/northeast-new-england/mushrooms/entries/chanterelle-new-england.md), line 132 | [T2: North American Mycological Association, Thirty-Plus Years of Mushroom Poisoning, Summary of t...](https://namyco.org/wp-content/uploads/2023/08/Poisonings30year.pdf) | &#9744; ok<br>&#9744; flag |
| 3 | "No cup (volva) at the stem base, and gills that attach to the stem rather than stand free, checked on a mushroom dug up whole, not picked \[5\]." | [honey-mushroom-armillaria.md](../regional/northeast-new-england/mushrooms/entries/honey-mushroom-armillaria.md), line 121 | [T1: USDA Forest Service, Northern Research Station, Field Guide to Common Macrofungi in Eastern F...](https://www.nrs.fs.usda.gov/pubs/gtr/gtr_nrs79r.pdf) | &#9744; ok<br>&#9744; flag |
| 4 | "The honey mushroom has whitish gills and a ring, so it falls inside that wording, and a reader who follows point 3 alone would reject it. It is eaten only after an expert has examined the dug-up specimen in hand and has checked the stem base for a cup (volva) and checked whether the gills attach to the stem or stand free \[5\]." | [honey-mushroom-armillaria.md](../regional/northeast-new-england/mushrooms/entries/honey-mushroom-armillaria.md), line 138 | [T1: USDA Forest Service, Northern Research Station, Field Guide to Common Macrofungi in Eastern F...](https://www.nrs.fs.usda.gov/pubs/gtr/gtr_nrs79r.pdf) | &#9744; ok<br>&#9744; flag |
| 5 | "NAMA describes a latency of 6 to 24 hours, violent vomiting and diarrhea, a day in which the victim seems to recover, then relapse with kidney and liver failure. A patient may seem recovered on day two or three and be sent home \[10\]." | [honey-mushroom-armillaria.md](../regional/northeast-new-england/mushrooms/entries/honey-mushroom-armillaria.md), line 233 | [T2: North American Mycological Association, Mushroom Poisoning Syndromes](https://www.namyco.org/mushroom_poisoning_syndromes.php) | &#9744; ok<br>&#9744; flag |
| 6 | "No blue staining does not clear a bolete, because Bessette says B. huronensis flesh is typically bluing when cut "but sometimes slowly or not at all" \[7\]." | [king-bolete-boletus.md](../regional/northeast-new-england/mushrooms/entries/king-bolete-boletus.md), line 126 | [T2: North American Mycological Association, Boletus huronensis (Bill Bakaitis), McIlvainea](https://namyco.org/publications/mcilvainea-journal-of-american-amateur-mycology/boletus-huronensis/) | &#9744; ok<br>&#9744; flag |
| 7 | "Go Botany lists ramp leaves as smelling of onion or garlic, and false hellebore and lily of the valley leaves as having no particular smell \[1\]\[2\]\[3\]." | [ramps-allium-tricoccum.md](../regional/northeast-new-england/edible-plants/entries/ramps-allium-tricoccum.md), line 135 | [T2: Native Plant Trust, Allium tricoccum (ramps, wild leek), Go Botany](https://gobotany.nativeplanttrust.org/species/allium/tricoccum/)<br>[T2: Native Plant Trust, Veratrum viride (American false hellebore), Go Botany](https://gobotany.nativeplanttrust.org/species/veratrum/viride/)<br>[T2: Native Plant Trust, Convallaria majalis (European lily-of-the-valley), Go Botany](https://gobotany.nativeplanttrust.org/species/convallaria/majalis/) | &#9744; ok<br>&#9744; flag |
| 8 | "A leaf stalk proves nothing either way: Go Botany says ramp var. burdickii leaves are "not or scarcely petiolate" \[1\], and the sources disagree on false hellebore (Go Botany: no leaf stalk \[2\]; Vermont Department of Health: leaves "grow from a stalk" \[21\])." | [ramps-allium-tricoccum.md](../regional/northeast-new-england/edible-plants/entries/ramps-allium-tricoccum.md), line 136 | [T2: Native Plant Trust, Allium tricoccum (ramps, wild leek), Go Botany](https://gobotany.nativeplanttrust.org/species/allium/tricoccum/)<br>[T2: Native Plant Trust, Veratrum viride (American false hellebore), Go Botany](https://gobotany.nativeplanttrust.org/species/veratrum/viride/)<br>[T1: Vermont Department of Health, News Release: Health Officials Warn Vermonters about False Hell...](https://healthvermont.gov/media/news-room/news-release-health-officials-warn-vermonters-about-false-hellebore) | &#9744; ok<br>&#9744; flag |
| 9 | "Alternate on the stem, with no leaf stalk, the base clasping the stem. Blades 150 to 350 mm long and 100 to 180 mm wide, with parallel veins \[2\]." | [ramps-allium-tricoccum.md](../regional/northeast-new-england/edible-plants/entries/ramps-allium-tricoccum.md), line 163 | [T2: Native Plant Trust, Veratrum viride (American false hellebore), Go Botany](https://gobotany.nativeplanttrust.org/species/veratrum/viride/) | &#9744; ok<br>&#9744; flag |
| 10 | "Lightly salted water at a rolling boil, enough to cover the fiddleheads fully. Add them, bring the water back to a steady boil, and boil for 15 minutes \[2\]\[4\]." | [fiddlehead-ostrich-fern.md](../regional/northeast-new-england/edible-plants/entries/fiddlehead-ostrich-fern.md), line 166 | [T1: University of Maine Cooperative Extension, Bulletin #4198, Facts on Fiddleheads](https://extension.umaine.edu/publications/4198e/)<br>[T1: Health Canada, Food safety tips for fiddleheads](https://www.canada.ca/en/health-canada/services/food-safety-fruits-vegetables/fiddlehead-safety-tips.html) | &#9744; ok<br>&#9744; flag |
| 11 | "CDC says it smells like fresh turnips, and a 2 to 3 cm piece of root can kill an adult \[12\]." | [toxic-plants-new-england.md](../regional/northeast-new-england/hazards/entries/toxic-plants-new-england.md), line 134 | [T1: CDC, MMWR 43(13), Water Hemlock Poisoning - Maine, 1992](https://www.cdc.gov/mmwr/PDF/wk/mm4313.pdf) | &#9744; ok<br>&#9744; flag |
| 12 | "New York and Vermont both say Powassan virus can pass in as little as 15 minutes \[5\]\[8\]." | [ticks-new-england.md](../regional/northeast-new-england/hazards/entries/ticks-new-england.md), line 98 | [T1: Vermont Department of Health, Powassan Virus](https://www.healthvermont.gov/disease-control/tickborne-diseases/powassan-virus)<br>[T1: New York State Department of Health, Powassan (POW) Virus Disease Fact Sheet](https://www.health.ny.gov/diseases/communicable/powassan/fact_sheet.htm) | &#9744; ok<br>&#9744; flag |
| 13 | "The National Center for Cold Water Safety calls the 1-10-1 misleading: it says your ability to help yourself declines the whole time you are in the water, and it quotes a cold-water physiologist's 2006 text giving cold shock as able to kill within seconds to two minutes and cold incapacitation as occurring within two to thirty minutes \[8\]." | [cold-water-and-shoulder-season-hypothermia.md](../regional/northeast-new-england/hazards/entries/cold-water-and-shoulder-season-hypothermia.md), line 62 | [T2: National Center for Cold Water Safety, The 1-10-1 Myth](https://www.coldwatersafety.org/1-10-1-myth) | &#9744; ok<br>&#9744; flag |
| 14 | "Do not eat the brain, spinal cord, eyes, spleen, tonsils or lymph nodes \[2\]\[5\]." | [white-tailed-deer-new-england.md](../regional/northeast-new-england/game-animals/entries/white-tailed-deer-new-england.md), line 173 | [T1: MassWildlife (Massachusetts Division of Fisheries and Wildlife), Chronic Wasting Disease (CWD)](https://www.mass.gov/info-details/chronic-wasting-disease-cwd)<br>[T1: Maine Department of Inland Fisheries and Wildlife, Chronic Wasting Disease (CWD)](https://www.maine.gov/IFW/fish-wildlife/wildlife/living-with-wildlife/diseases/chronic-wasting-disease.html) | &#9744; ok<br>&#9744; flag |
| 15 | "New Hampshire law (RSA 209:4) says there shall be no open season for spruce grouse \[17\]." | [ruffed-grouse.md](../regional/northeast-new-england/game-animals/entries/ruffed-grouse.md), line 102 | [T1: New Hampshire General Court (Revised Statutes Annotated), RSA 209:4 No Open Season (no open s...](https://gc.nh.gov/rsa/html/XVIII/209/209-4.htm) | &#9744; ok<br>&#9744; flag |
| 16 | "Old sugaring gear can put lead in sap, and lead is concentrated anywhere from 30 to 100 times in the syrup \[6\]." | [maple-sap-and-syrup.md](../regional/northeast-new-england/crops/entries/maple-sap-and-syrup.md), line 127 | [T2: International Maple Syrup Institute, with UVM Proctor Maple Research Center, UVM Extension an...](https://www.Agriculture.Vermont.gov/sites/agriculture/files/documents/Maple_Products/IMSI%202015%20-%20GMPs%20to%20Avoid%20Lead%20Contamination%20of%20Maple%20Syrup.pdf) | &#9744; ok<br>&#9744; flag |

The claims sample the highest-stakes line in each of the lethal or high-severity entries. They leave out the cooking temperatures in the game entries (venison 160 F, rabbit and game birds 165 F) and the glycoalkaloid and syrup-density rules in the potato and maple entries. If you have spare minutes, check those against the sources in each entry's `MANDATORY PREPARATION` section.

## 5. CONVENTIONS section 10 checklist

Copied from CONVENTIONS.md section 10. The boxes that need a person: ≥2 references per species and per look-alike (use the pair table above), the facets set truthfully (compare the entries table: honey mushroom, ramps and the toxic-plants entry carry a deadly look-alike and should show expert ID needed `True` and field ID not OK `True`), the `MANDATORY PREPARATION` section present and correct, and the game-animal block and cook temperatures. The mushroom and edible-plant boxes apply to the three mushroom entries, ramps, fiddleheads and blueberry. The morel and false-morel box is met by the Mid-Atlantic mushroom folder, so it is left out here. The hazards and crops entries do not need the identification boxes.

### Mushrooms & edible-plants
- [ ] Every entry opens with the POSITIVE-ID SAFETY GATE (checklist + disqualifying traits), not a
      single test.
- [ ] Each species **and each deadly look-alike** triangulated against **≥2** T1/T2 references.
- [ ] `confusability_level`, `expert_id_required`, `field_id_not_appropriate` set truthfully.
- [ ] Mushroom doctrine page loads before species; deadly-look-alike matrix populated and leads the
      index; "what NOT to eat" comes before edible exemplars.
- [ ] `⚠ MANDATORY PREPARATION` present and correct on every consumable.

### Game animals
- [ ] CWD-prion / trichinella / tularemia block present and correct where applicable.
- [ ] Internal cook temps match USDA; deer entry has the full field-dress→skin→butcher→preserve
      flow.
- [ ] `legal_status` is `regulated`/`seasonal-permit` unless a statutory exception is cited; the body distinguishes normal season vs. emergency and is framed as "know your
      regs," not legal advice.

### Coherence (all domains)
- [ ] Manifests pass `check_manifests` (no dangling/missing rows; required columns filled).
- [ ] Survey files link down; food resolves via `regional/_index.md` registry → `food_hub.md`; no
      broken intra-repo links.
- [ ] `grep -rn "danger_class" .` = 0; no `safe` token on biology facets.

## 6. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### King bolete: the facets are set conservatively

The entry names no deadly look-alike in New England, yet it sets confusability to high, expert ID needed to true and field ID not OK to true, because the group cannot be settled in the field and its look-alikes make people seriously ill. Decide whether that is the right level, or whether it blurs the line between this bolete and the poisonous ones.

> Doctrine applies in full, and this entry is `field_id_not_appropriate: true` because the group cannot be settled in the field and its look-alikes make people seriously ill.
>
> From [king-bolete-boletus.md](../regional/northeast-new-england/mushrooms/entries/king-bolete-boletus.md), line 133.

### Fiddleheads: moderate severity, boiled 15 minutes

The entry says no fern in its sources is an acute killer, sets confusability to moderate, and asks for an expert to confirm the plant the first time. It also gives a 15-minute boil, longer than the 10 minutes the CDC report floated as prudent. Decide whether those settings fit a spring vegetable that has sent people to the hospital when undercooked.

> No fern named in the sources opened is an acute killer, but the margin for error is thin.
>
> From [fiddlehead-ostrich-fern.md](../regional/northeast-new-england/edible-plants/entries/fiddlehead-ostrich-fern.md), line 132.

### The 1-10-1 cold-water rule is disputed

Maryland's natural resources police teach 1-10-1. The National Center for Cold Water Safety calls it misleading and gives shorter times. The entry reports both and tells the reader to wear a life jacket either way. Decide whether to keep the 1-10-1 numbers in the entry at all.

> So the two sources do not agree on the numbers; both say to wear a life jacket and dress for the water.
>
> From [cold-water-and-shoulder-season-hypothermia.md](../regional/northeast-new-england/hazards/entries/cold-water-and-shoulder-season-hypothermia.md), line 61.

### Honey mushroom sits inside doctrine point 3

Point 3 of the doctrine says no white-gilled mushrooms with a ring or a volva. The honey mushroom has whitish gills and a ring. The entry says so openly and allows it only after an expert has examined the dug-up specimen. Decide whether that reconciliation is clear enough, or whether point 3 needs rewording.

> The mushroom doctrine (point 3) says no white-gilled mushrooms with a ring or a volva, because that is the Amanita pattern [5]. The honey mushroom has whitish gills and a ring, so it falls inside that wording, and a reader who follows point 3 alone would reject it.
>
> From [honey-mushroom-armillaria.md](../regional/northeast-new-england/mushrooms/entries/honey-mushroom-armillaria.md), line 137.

### Honey mushroom blanching comes from a Swiss poison centre

No North American source gives a blanching step for honey mushroom. The entry takes it from Tox Info Suisse and gives no blanching time. Decide whether to keep a non-North American source for a preparation step, or ask a mycologist.

> Tox Info Suisse, a national poisons centre, lists honey fungus (Armillaria mellea and A. ostoyae) under "blanch, throw away cooking water," and says skipping the step risks vomiting and diarrhoea 1 to 4 hours after the meal [19].
>
> From [honey-mushroom-armillaria.md](../regional/northeast-new-england/mushrooms/entries/honey-mushroom-armillaria.md), line 218.

### Season tables for New York and New Hampshire are stale

The New York grouse and hare dates are the 2025-26 season, and the New Hampshire limits come from the agency's 2024-25 table. The entries say so and tell the reader to check the agency. Decide whether dated seasons belong in a survival reference, or only the instruction to check the agency.

> The agency's 2024-25 table showed 4 a day [8]; confirm the current limit.
>
> From [ruffed-grouse.md](../regional/northeast-new-england/game-animals/entries/ruffed-grouse.md), line 106.
>
> New York: the 2025-26 season ran Sept 20 to Feb 28 in the Northern Zone and Oct 1 to Feb 28 in the Southern Zone [11]. Check DEC for the current year.
>
> From [ruffed-grouse.md](../regional/northeast-new-england/game-animals/entries/ruffed-grouse.md), line 109.
>
> The agency's 2024-25 table showed 3 a day in the northern units and 2 a day in southern ones [6].
>
> From [snowshoe-hare.md](../regional/northeast-new-england/game-animals/entries/snowshoe-hare.md), line 124.

### Rhode Island is not covered

The game entries say Rhode Island is not covered and send the reader to Rhode Island DEM. The ticks entry did not open a New Hampshire, Massachusetts or Rhode Island health page. The pack's region line names Rhode Island. Decide whether the pack can be signed off with one of the six states missing, or whether a Rhode Island pass is needed first.

> Rhode Island is not covered here; check Rhode Island DEM.
>
> From [ruffed-grouse.md](../regional/northeast-new-england/game-animals/entries/ruffed-grouse.md), line 101.

### Doctrine point 1: no consumption without an expert who has examined the specimen

This is the repo's strictest rule, and every mushroom entry in this pack applies it. Decide whether it is the right bar and whether the New England doctrine page states it plainly enough. The text is in [CONVENTIONS.md](../CONVENTIONS.md) section 4.

## 7. Sign-off

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
