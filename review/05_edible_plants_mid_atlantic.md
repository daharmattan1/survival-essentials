# Safety read 05: Mid-Atlantic edible plants

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 5 of 13. Edible plants come fifth: fewer species are lethal than in mushrooms, but wild onion against death camas and acorn against buckeye are mistakes people have made.

## Time and status

- **Estimated time: 60 minutes at most** for the targeted check below (13 claims at about 2 minutes each; 8 species at about 1 minute each; 16 look-alike pairs at about 1 minute each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 18,012 words, roughly 70 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain regional/mid-atlantic-appalachian/edible-plants --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

Pawpaw and the Rubus (blackberry and raspberry) entries name no poisonous look-alike. Both say that is missing data, not a promise. If you know of one, file it.

| Entry | Type | Severity | Look-alike level | Expert ID needed | Field ID not OK | Legal status | Tier | Status now | Words |
|---|---|---|---|---|---|---|---|---|---|
| [Acorn & Oak (Quercus spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/acorn-oak.md) | WILD-EDIBLE-PLANT | high | deadly-lookalike-exists | False | True | regulated | T1 | agent-verified | 2633 |
| [Black Walnut (Juglans nigra)](../regional/mid-atlantic-appalachian/edible-plants/entries/black-walnut-juglans.md) | WILD-EDIBLE-PLANT | moderate | moderate | False | False | regulated | T1 | agent-verified | 2638 |
| [Cattail (Typha spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/cattail.md) | WILD-EDIBLE-PLANT | low | moderate | False | False | regulated | T1 | agent-verified | 1947 |
| [Dandelion (Taraxacum officinale)](../regional/mid-atlantic-appalachian/edible-plants/entries/dandelion.md) | WILD-EDIBLE-PLANT | low | high | False | True | regulated | T1 | agent-verified | 1682 |
| [Pawpaw (Asimina triloba)](../regional/mid-atlantic-appalachian/edible-plants/entries/pawpaw-asimina.md) | WILD-EDIBLE-PLANT | low | low | False | False | regulated | T1 | agent-verified | 2162 |
| [Violet & Chickweed (Viola & Stellaria spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/violet-or-chickweed.md) | WILD-EDIBLE-PLANT | low | moderate | False | False | regulated | T1 | agent-verified | 1808 |
| [Wild Blackberry, Black Raspberry and Wineberry (Rubus spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-blackberry-raspberry-rubus.md) | WILD-EDIBLE-PLANT | low | low | False | False | regulated | T1 | agent-verified | 2099 |
| [Wild Onion & Garlic (Allium spp.): DEADLY-TWIN ALERT](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md) | WILD-EDIBLE-PLANT | lethal | deadly-lookalike-exists | True | True | regulated | T1 | agent-verified | 3043 |

## 2. Species: the positive-ID gate

Open each source. Check the traits in the entry's positive-ID checklist, and the disqualifying traits, against it. The two links are the sources the entry cites most often inside its gate, with a page named for the species ranked first. A source marked (general) is cited in the gate but its title does not name the species. "Gate lines" are the line numbers of the gate section.

| Species | Gate lines | Source 1 | Source 2 | Check |
|---|---|---|---|---|
| [Acorn & Oak (Quercus spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/acorn-oak.md) | 106-129 | [T1: NC State Extension Plants Toolbox, Quercus alba (White Oak)](https://plants.ces.ncsu.edu/plants/quercus-alba/) | [T1: NC State Extension Plants Toolbox, Quercus rubra (Northern Red Oak)](https://plants.ces.ncsu.edu/plants/quercus-rubra/) | &#9744; |
| [Black Walnut (Juglans nigra)](../regional/mid-atlantic-appalachian/edible-plants/entries/black-walnut-juglans.md) | 95-122 | [T1: NC State Extension Plants Toolbox, Juglans nigra (Black Walnut)](https://plants.ces.ncsu.edu/plants/juglans-nigra/) | [T1: Virginia Tech, Department of Forest Resources and Environmental Conservation, black walnut, Jug...](https://dendro.cnre.vt.edu/dendrology/syllabus/factsheet.cfm?ID=32) | &#9744; |
| [Cattail (Typha spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/cattail.md) | 80-102 | [T1: USDA Natural Resources Conservation Service, Broad-leaved Cattail, Typha latifolia L. (Plant Gu...](https://plants.sc.egov.usda.gov/DocumentLibrary/plantguide/pdf/pg_tyla.pdf) | [T1: NC State Extension Plants Toolbox, Typha latifolia (Broadleaf Cattail)](https://plants.ces.ncsu.edu/plants/typha-latifolia/) | &#9744; |
| [Dandelion (Taraxacum officinale)](../regional/mid-atlantic-appalachian/edible-plants/entries/dandelion.md) | 79-104 | [T1: NC State Extension Gardener Plant Toolbox, Taraxacum officinale (Dandelion, Lion's Tooth)](https://plants.ces.ncsu.edu/plants/taraxacum-officinale/) | [T1: NC State Extension Gardener Plant Toolbox, Cichorium intybus (Chicory) (general)](https://plants.ces.ncsu.edu/plants/cichorium-intybus/) | &#9744; |
| [Pawpaw (Asimina triloba)](../regional/mid-atlantic-appalachian/edible-plants/entries/pawpaw-asimina.md) | 81-105 | [T1: NC State Extension Plants Toolbox, Asimina triloba (Common Pawpaw, Pawpaw)](https://plants.ces.ncsu.edu/plants/asimina-triloba/) | [T2: University of Vermont (J. Shane plant ID pages), Plant Identification: Asimina triloba, leaf an...](https://www.uvm.edu/~jshane/plant-id/angiosperms/misc.angiosperms/A.triloba.leaf-fruit.html) | &#9744; |
| [Violet & Chickweed (Viola & Stellaria spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/violet-or-chickweed.md) | 81-108 | [T1: NC State Extension Gardener Plant Toolbox, Viola sororia (Common Blue Violet)](https://plants.ces.ncsu.edu/plants/viola-sororia/) | [T1: NC State Extension Gardener Plant Toolbox, Stellaria media (Chickweed)](https://plants.ces.ncsu.edu/plants/stellaria-media/) | &#9744; |
| [Wild Blackberry, Black Raspberry and Wineberry (Rubus spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-blackberry-raspberry-rubus.md) | 87-110 | [T1: NC State Extension Plants Toolbox, Rubus occidentalis (black raspberry)](https://plants.ces.ncsu.edu/plants/rubus-occidentalis/) | [T1: NC State Extension Plants Toolbox, Rubus allegheniensis (Allegheny blackberry)](https://plants.ces.ncsu.edu/plants/rubus-allegheniensis/) | &#9744; |
| [Wild Onion & Garlic (Allium spp.): DEADLY-TWIN ALERT](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md) | 148-172 | [T1: NC State Extension Gardener Plant Toolbox, Allium canadense (Meadow Garlic, Wild Garlic, Wild O...](https://plants.ces.ncsu.edu/plants/allium-canadense/) | [T1: NC State Extension Gardener Plant Toolbox, Allium vineale (Field Garlic, Wild Garlic)](https://plants.ces.ncsu.edu/plants/allium-vineale/) | &#9744; |

## 3. Look-alike pairs: two sources each

CONVENTIONS section 7 needs each look-alike checked against at least two Tier 1 or Tier 2 sources. The two links are the sources the entry cites on the lines that name the look-alike, with a page named for the look-alike ranked first, then the most often cited. A source marked (general) is cited on those lines but its title does not name the look-alike, so read it for the difference and look for a page that names it. "First line" is the first line that names it. If a row says only one source is cited, finding the second is part of your job. A T3 source does not count toward the two. Check that the entry's stated difference, and what the look-alike does to a person, match both sources.

| Species | Look-alike | First line | Source 1 | Source 2 | Check |
|---|---|---|---|---|---|
| [Acorn & Oak (Quercus spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/acorn-oak.md) | Buckeye and horse chestnut (Aesculus spp.) | 108 | [T1: NC State Extension Plants Toolbox, Aesculus flava (Yellow Buckeye)](https://plants.ces.ncsu.edu/plants/aesculus-flava/) | [T1: NC State Extension Plants Toolbox, Aesculus hippocastanum (Common Horsechestnut)](https://plants.ces.ncsu.edu/plants/aesculus-hippocastanum/) | &#9744; |
| [Black Walnut (Juglans nigra)](../regional/mid-atlantic-appalachian/edible-plants/entries/black-walnut-juglans.md) | Kentucky coffeetree | 105 | [T1: NC State Extension Plants Toolbox, Gymnocladus dioicus (Kentucky Coffeetree)](https://plants.ces.ncsu.edu/plants/gymnocladus-dioicus/) | [T1: USDA Natural Resources Conservation Service, Kentucky Coffeetree, Plant Guide](https://plants.usda.gov/DocumentLibrary/plantguide/pdf/cs_gydi.pdf) | &#9744; |
| [Black Walnut (Juglans nigra)](../regional/mid-atlantic-appalachian/edible-plants/entries/black-walnut-juglans.md) | Tree-of-heaven | 113 | [T1: Virginia Tech, Department of Forest Resources and Environmental Conservation, black walnut, Jug...](https://dendro.cnre.vt.edu/dendrology/syllabus/factsheet.cfm?ID=32) | [T1: NC State Extension Plants Toolbox, Ailanthus altissima (Tree of Heaven) (general)](https://plants.ces.ncsu.edu/plants/ailanthus-altissima/) | &#9744; |
| [Cattail (Typha spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/cattail.md) | Iris (blue flag, yellow flag) | 82 | [T1: NC State Extension Plants Toolbox, Iris versicolor (Harlequin Blueflag)](https://plants.ces.ncsu.edu/plants/iris-versicolor/) | [T1: NC State Extension Plants Toolbox, Iris pseudacorus (Yellow Flag)](https://plants.ces.ncsu.edu/plants/iris-pseudacorus/) | &#9744; |
| [Dandelion (Taraxacum officinale)](../regional/mid-atlantic-appalachian/edible-plants/entries/dandelion.md) | Common groundsel (Senecio vulgaris) | 81 | [T1: NC State Extension Gardener Plant Toolbox, Senecio vulgaris (Common Groundsel)](https://plants.ces.ncsu.edu/plants/senecio-vulgaris/) | [T1: NC State Extension Gardener Plant Toolbox, Arnica montana (Arnica) (general)](https://plants.ces.ncsu.edu/plants/arnica-montana/) | &#9744; |
| [Dandelion (Taraxacum officinale)](../regional/mid-atlantic-appalachian/edible-plants/entries/dandelion.md) | Arnica (Arnica montana) | 81 | [T1: NC State Extension Gardener Plant Toolbox, Arnica montana (Arnica)](https://plants.ces.ncsu.edu/plants/arnica-montana/) | [T1: NC State Extension Gardener Plant Toolbox, Senecio vulgaris (Common Groundsel) (general)](https://plants.ces.ncsu.edu/plants/senecio-vulgaris/) | &#9744; |
| [Dandelion (Taraxacum officinale)](../regional/mid-atlantic-appalachian/edible-plants/entries/dandelion.md) | Spotted spurge (Euphorbia maculata) | 81 | [T1: NC State Extension Gardener Plant Toolbox, Euphorbia maculata (Spotted Spurge)](https://plants.ces.ncsu.edu/plants/euphorbia-maculata/) | [T1: NC State Extension Gardener Plant Toolbox, Taraxacum officinale (Dandelion, Lion's Tooth) (gene...](https://plants.ces.ncsu.edu/plants/taraxacum-officinale/) | &#9744; |
| [Violet & Chickweed (Viola & Stellaria spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/violet-or-chickweed.md) | Lesser celandine | 97 | [T1: NC State Extension Gardener Plant Toolbox, Ranunculus ficaria (Lesser Celandine, Fig Buttercup)](https://plants.ces.ncsu.edu/plants/ficaria-verna/) | [T1: University of Maryland Extension, Lesser Celandine](https://extension.umd.edu/resource/lesser-celandine) | &#9744; |
| [Violet & Chickweed (Viola & Stellaria spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/violet-or-chickweed.md) | Marsh marigold | 97 | [T1: NC State Extension Gardener Plant Toolbox, Caltha palustris (Marsh Marigold)](https://plants.ces.ncsu.edu/plants/caltha-palustris/) | [T1: NC State Extension Gardener Plant Toolbox, Ranunculus ficaria (Lesser Celandine, Fig Buttercup)...](https://plants.ces.ncsu.edu/plants/ficaria-verna/) | &#9744; |
| [Violet & Chickweed (Viola & Stellaria spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/violet-or-chickweed.md) | Scarlet pimpernel | 103 | [T2: Massey University (New Zealand), Scarlet pimpernel (Anagallis arvensis), Poisonous Plants Datab...](https://poisonousplants.massey.ac.nz/data/scarlet_pimp/scar_pimp.html) | [T1: NC State Extension Gardener Plant Toolbox, Ranunculus ficaria (Lesser Celandine, Fig Buttercup)...](https://plants.ces.ncsu.edu/plants/ficaria-verna/) | &#9744; |
| [Violet & Chickweed (Viola & Stellaria spp.)](../regional/mid-atlantic-appalachian/edible-plants/entries/violet-or-chickweed.md) | Spurges | 94 | [T1: NC State Extension Gardener Plant Toolbox, Euphorbia maculata (Spotted Spurge)](https://plants.ces.ncsu.edu/plants/euphorbia-maculata/) | [T1: NC State Extension Gardener Plant Toolbox, Euphorbia prostrata (Prostrate Spurge)](https://plants.ces.ncsu.edu/plants/euphorbia-prostrata/) | &#9744; |
| [Wild Onion & Garlic (Allium spp.): DEADLY-TWIN ALERT](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md) | Eastern death camas group (fly poison and others) | 150 | [T1: NC State Extension Gardener Plant Toolbox, Amianthium muscitoxicum (Crow Poison, Fly Poison, St...](https://plants.ces.ncsu.edu/plants/amianthium-muscitoxicum/) | [T1: NC State Extension Gardener Plant Toolbox, Stenanthium densum (Black Death Camas, Crow-poison)](https://plants.ces.ncsu.edu/plants/stenanthium-densum/) | &#9744; |
| [Wild Onion & Garlic (Allium spp.): DEADLY-TWIN ALERT](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md) | Star-of-Bethlehem | 167 | [T1: NC State Extension Gardener Plant Toolbox, Ornithogalum umbellatum (Star of Bethlehem)](https://plants.ces.ncsu.edu/plants/ornithogalum-umbellatum/) | [T1: NC State Extension Gardener Plant Toolbox, Amianthium muscitoxicum (Crow Poison, Fly Poison, St...](https://plants.ces.ncsu.edu/plants/amianthium-muscitoxicum/) | &#9744; |
| [Wild Onion & Garlic (Allium spp.): DEADLY-TWIN ALERT](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md) | Autumn crocus | 167 | [T1: NC State Extension Gardener Plant Toolbox, Colchicum autumnale (Autumn Crocus)](https://plants.ces.ncsu.edu/plants/colchicum-autumnale/) | [T1: ANSES (French national food, environment and occupational health agency), Confusion between aut...](https://www.anses.fr/en/content/confusion-between-autumn-crocus-and-wild-garlic-can-lead-fatal-poisoning) | &#9744; |
| [Wild Onion & Garlic (Allium spp.): DEADLY-TWIN ALERT](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md) | False hellebore (Veratrum viride) | 163 | [T1: NC State Extension Gardener Plant Toolbox, Veratrum viride (False Hellebore, Indian Poke)](https://plants.ces.ncsu.edu/plants/veratrum-viride/) | [T1: NC State Extension Gardener Plant Toolbox, Allium tricoccum (Ramps, Wild Leek) (general)](https://plants.ces.ncsu.edu/plants/allium-tricoccum/) | &#9744; |
| [Wild Onion & Garlic (Allium spp.): DEADLY-TWIN ALERT](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md) | Lily of the valley | 163 | [T1: NC State Extension Gardener Plant Toolbox, Convallaria majalis (Lily of the Valley)](https://plants.ces.ncsu.edu/plants/convallaria-majalis/) | [T1: NC State Extension Gardener Plant Toolbox, Allium tricoccum (Ramps, Wild Leek) (general)](https://plants.ces.ncsu.edu/plants/allium-tricoccum/) | &#9744; |

## 4. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "Raw acorns are not food." | [acorn-oak.md](../regional/mid-atlantic-appalachian/edible-plants/entries/acorn-oak.md), line 178 | [T1: NC State Extension Plants Toolbox, Quercus alba (White Oak)](https://plants.ces.ncsu.edu/plants/quercus-alba/)<br>[T1: NC State Extension Plants Toolbox, Quercus montana (Chestnut Oak)](https://plants.ces.ncsu.edu/plants/quercus-montana/)<br>[T2: Sierra Nature Prints (author's reprint), Acorns as Food: History, use, recipes, and bibliograph...](https://snakeroot.net/MTCA/wp-content/uploads/Acorns_as_Food_Text_and_Bibliography.pdf)<br>[T1: NC State Extension Plants Toolbox, Quercus rubra (Northern Red Oak)](https://plants.ces.ncsu.edu/plants/quercus-rubra/) | &#9744; ok<br>&#9744; flag |
| 2 | "Arkansas Extension reports one cook who boiled the kernels through five water changes, until the water stopped darkening" | [acorn-oak.md](../regional/mid-atlantic-appalachian/edible-plants/entries/acorn-oak.md), line 186 | [T1: University of Arkansas Cooperative Extension Service, Acorns Galore](https://www.uaex.uada.edu/environment-nature/musings-on-nature-blog/posts/acorns-galore.aspx) | &#9744; ok<br>&#9744; flag |
| 3 | "If it is still bitter or puckery, keep leaching. Bainbridge ties bitterness to tannin, which is why taste is the endpoint" | [acorn-oak.md](../regional/mid-atlantic-appalachian/edible-plants/entries/acorn-oak.md), line 188 | [T2: Sierra Nature Prints (author's reprint), Acorns as Food: History, use, recipes, and bibliograph...](https://snakeroot.net/MTCA/wp-content/uploads/Acorns_as_Food_Text_and_Bibliography.pdf) | &#9744; ok<br>&#9744; flag |
| 4 | "Aesculin and aescin: muscle weakness, paralysis, dilated pupils, vomiting, stupor; NC State says it can be fatal" | [acorn-oak.md](../regional/mid-atlantic-appalachian/edible-plants/entries/acorn-oak.md), line 140 | [T1: NC State Extension Plants Toolbox, Aesculus hippocastanum (Common Horsechestnut)](https://plants.ces.ncsu.edu/plants/aesculus-hippocastanum/)<br>[T1: NC State Extension Plants Toolbox, Aesculus flava (Yellow Buckeye)](https://plants.ces.ncsu.edu/plants/aesculus-flava/) | &#9744; ok<br>&#9744; flag |
| 5 | "Crush one leaf from the single plant you mean to eat. A strong onion or garlic odor must come from that plant." | [wild-onion-garlic-allium.md](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md), line 154 | [T1: Idaho Fish and Game, Use caution when foraging for wild plants, mushrooms (May 11, 2020)](https://idfg.idaho.gov/press/use-caution-when-foraging-wild-plants-mushrooms) | &#9744; ok<br>&#9744; flag |
| 6 | "the two are nearly indistinguishable to an untrained eye in spring" | [wild-onion-garlic-allium.md](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md), line 187 | [T1: Idaho Fish and Game, Use caution when foraging for wild plants, mushrooms (May 11, 2020)](https://idfg.idaho.gov/press/use-caution-when-foraging-wild-plants-mushrooms) | &#9744; ok<br>&#9744; flag |
| 7 | "High severity, "can be fatal if ingested," all parts poisonous" | [wild-onion-garlic-allium.md](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md), line 180 | [T1: NC State Extension Gardener Plant Toolbox, Amianthium muscitoxicum (Crow Poison, Fly Poison, St...](https://plants.ces.ncsu.edu/plants/amianthium-muscitoxicum/) | &#9744; ok<br>&#9744; flag |
| 8 | "Listed symptoms include heavy salivation, persistent vomiting, weakness, low blood pressure, irregular heartbeat, trouble breathing, convulsions and coma, usually 1 to 8 hours after eating" | [wild-onion-garlic-allium.md](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md), line 189 | [T1: Washington State University, Oregon State University, University of Idaho Extension, Meadow Dea...](https://wpcdn.web.wsu.edu/wp-ecommerce/uploads/sites/2/product-3886-sku-PNW104.pdf) | &#9744; ok<br>&#9744; flag |
| 9 | "judge the base, round (cattail) versus flat and fan-like (iris)" | [cattail.md](../regional/mid-atlantic-appalachian/edible-plants/entries/cattail.md), line 87 | [T1: Montana State University Extension and Montana Department of Agriculture, Biology, Ecology and...](https://agr.mt.gov/_docs/weeds-docs/yellow-flag-iris.pdf)<br>[T2: Tennessee-Kentucky Plant Atlas, University of South Florida, Typha latifolia (Common Cat Tail)...](https://tennessee-kentucky.plantatlas.usf.edu/plant/species/2951) | &#9744; ok<br>&#9744; flag |
| 10 | "Poisonous, with the highest concentration of poison in the rhizome" | [cattail.md](../regional/mid-atlantic-appalachian/edible-plants/entries/cattail.md), line 113 | [T1: NC State Extension Plants Toolbox, Iris versicolor (Harlequin Blueflag)](https://plants.ces.ncsu.edu/plants/iris-versicolor/)<br>[T1: NC State Extension Plants Toolbox, Iris pseudacorus (Yellow Flag)](https://plants.ces.ncsu.edu/plants/iris-pseudacorus/) | &#9744; ok<br>&#9744; flag |
| 11 | "Do not use the Universal Edibility Test or a taste test to confirm dandelion. Spurge sap blisters the lips and mouth" | [dandelion.md](../regional/mid-atlantic-appalachian/edible-plants/entries/dandelion.md), line 145 | [T1: NC State Extension Gardener Plant Toolbox, Euphorbia maculata (Spotted Spurge)](https://plants.ces.ncsu.edu/plants/euphorbia-maculata/) | &#9744; ok<br>&#9744; flag |
| 12 | "NC State rates it high severity; the toxin is helenalin and its esters in flowers and roots, and ingestion can cause heart palpitations, vomiting, drowsiness, shortness of breath" | [dandelion.md](../regional/mid-atlantic-appalachian/edible-plants/entries/dandelion.md), line 115 | [T1: NC State Extension Gardener Plant Toolbox, Arnica montana (Arnica)](https://plants.ces.ncsu.edu/plants/arnica-montana/) | &#9744; ok<br>&#9744; flag |
| 13 | "Do not eat the skin. Do not eat the seeds. Clemson says the seeds and the green peel contain alkaloids that cause vomiting and "should not be consumed" \[3\]." | [pawpaw-asimina.md](../regional/mid-atlantic-appalachian/edible-plants/entries/pawpaw-asimina.md), line 143 | [T1: Clemson Cooperative Extension, Pawpaw (Home and Garden Information Center fact sheet)](https://hgic.clemson.edu/factsheet/pawpaw/) | &#9744; ok<br>&#9744; flag |

## 5. CONVENTIONS section 10 checklist

Copied from CONVENTIONS.md section 10. The boxes that need a person: ≥2 references per species and per look-alike (use the pair table above), the facets set truthfully (compare the entries table: any species with a deadly look-alike should show `deadly-lookalike-exists`, expert ID needed `True` and field ID not OK `True`), and the `MANDATORY PREPARATION` section present and correct.

### Mushrooms & edible-plants
- [ ] Every entry opens with the POSITIVE-ID SAFETY GATE (checklist + disqualifying traits), not a
      single test.
- [ ] Each species **and each deadly look-alike** triangulated against **≥2** T1/T2 references.
- [ ] `confusability_level`, `expert_id_required`, `field_id_not_appropriate` set truthfully.
- [ ] Mushroom doctrine page loads before species; deadly-look-alike matrix populated and leads the
      index; "what NOT to eat" comes before edible exemplars.
- [ ] Morel / false-morel pair present; ≥3 mushroom entries carry a deadly confusable.
- [ ] `⚠ MANDATORY PREPARATION` present and correct on every consumable.

## 6. Judgment calls for you to decide

These are places where the repo made a choice between sources, or between two risks. An AI checker cannot settle them. For each one, decide: keep as written, change, or ask a clinician or expert.

### Dandelion is marked not suitable for field ID alone

Dandelion is a common, mild plant, yet the entry says it must not be eaten on field identification alone, because arnica (rated high severity by NC State) and groundsel can be confused with it. Pass 2 changed this after a round-3 finding. Decide whether the rule is proportionate or will teach readers to ignore the flag. Check the dandelion facets in the entries table above.

> NC State rates it high severity; the toxin is helenalin and its esters in flowers and roots, and ingestion can cause heart palpitations, vomiting, drowsiness, shortness of breath
>
> From [dandelion.md](../regional/mid-atlantic-appalachian/edible-plants/entries/dandelion.md), line 114.

### Acorn is marked deadly-lookalike-exists

The entry says buckeye and horse chestnut look like acorns and NC State says they can be fatal. Pass 1 said there was no dangerous look-alike. Decide whether the facet and the side-by-side table in the entry make the difference clear enough, and whether the acorn leaching steps are safe to follow when no source gives a tested number of hours or days.

> Aesculin and aescin: muscle weakness, paralysis, dilated pupils, vomiting, stupor; NC State says it can be fatal
>
> From [acorn-oak.md](../regional/mid-atlantic-appalachian/edible-plants/entries/acorn-oak.md), line 139.

### Wild onion versus death camas: the smell test

Pass 1 had this table inverted and called the onion smell "absolute". The entry now says smell can reject a plant but never accept one. Decide whether a lay reader will take that the right way.

> Smell is a way to reject, never to accept.
>
> From [wild-onion-garlic-allium.md](../regional/mid-atlantic-appalachian/edible-plants/entries/wild-onion-garlic-allium.md), line 186.

### Cattail versus iris

The entry's discriminator is leaf-base shape, and it warns not to use the midrib alone. Decide whether the discriminator is sufficient for the wet-ground setting where a reader is hungry and tired.

> Do not use a midrib test alone.
>
> From [cattail.md](../regional/mid-atlantic-appalachian/edible-plants/entries/cattail.md), line 114.

### Pawpaw: no poisonous look-alike is named

The entry says this is missing data, not proof that none exists. Decide whether you can name one, and whether the skin-and-seed warning is complete.

> No source opened names a poisonous plant that is commonly mistaken for pawpaw
>
> From [pawpaw-asimina.md](../regional/mid-atlantic-appalachian/edible-plants/entries/pawpaw-asimina.md), line 108.

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
