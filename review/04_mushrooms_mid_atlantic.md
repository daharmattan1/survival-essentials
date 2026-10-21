# Safety read 04: Mid-Atlantic mushrooms

> Part of the [Safety Read Packet](SAFETY_READ_PACKET.md). Priority 4 of 13. Mushrooms come fourth only because the first three domains reach more readers. A wrong mushroom call is the most likely way this repo could kill someone.

## Time and status

- **Estimated time: 60 minutes at most** for the targeted check below (12 claims at about 2 minutes each; 8 species at about 1 minute each; 19 look-alike pairs at about 1 minute each; 8 minutes for the checklist and the sign-off).
- **The full read is extra.** The entries in this domain run about 19,110 words, roughly 75 minutes at 250 words per minute. The sign-off at the bottom asks which entries you read. [CONTRIBUTING.md](../CONTRIBUTING.md) says to tick the sign-off box only if you read them all. A partial read is still useful. Say so.
- **Where it stands:** the Status column shows what each file says today. `draft` and `agent-verified` mean an AI wrote or checked it. A `reviewed` there is a pass-1 stamp from an AI-only check, and pass 2 found serious errors in entries carrying it, so treat it as void. Only your sign-off, followed by `scripts/mark_reviewed.py`, makes an entry `reviewed`.
- **How the tables were made:** every claim, line number and source link was copied from the current files. Bold and italic markers are dropped from the quoted text. The wording is unchanged. Line numbers are for the file as it stands today and will drift if the file is edited. A source label starting T1, T2 or T3 is the tier the entry gives it.
- **After sign-off, you run this yourself:**

```
python scripts/mark_reviewed.py --domain regional/mid-atlantic-appalachian/mushrooms --reviewer "Your Full Name"
```

Add `--dry-run` first to see what it would change. The script asks you to type a confirmation phrase and refuses to run unattended. Then record the sign-off line it prints in [CHANGELOG.md](../CHANGELOG.md).

## 1. Entries to read

Read the [mushroom doctrine and look-alike matrix](../regional/mid-atlantic-appalachian/mushrooms/_index.md) first. Every species entry points to it. The doctrine's nine points are also in [CONVENTIONS.md](../CONVENTIONS.md) section 4.

| Entry | Type | Severity | Look-alike level | Expert ID needed | Field ID not OK | Legal status | Tier | Status now | Words |
|---|---|---|---|---|---|---|---|---|---|
| [Black Trumpet (Craterellus fallax)](../regional/mid-atlantic-appalachian/mushrooms/entries/black-trumpet-craterellus.md) | MUSHROOM | low | moderate | True | False | regulated | T2 | agent-verified | 2677 |
| [Chanterelle (Cantharellus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/chanterelle-cantharellus.md) | MUSHROOM | high | deadly-lookalike-exists | True | True | regulated | T2 | agent-verified | 2211 |
| [Chicken-of-the-Woods (Laetiporus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/chicken-of-the-woods-laetiporus.md) | MUSHROOM | high | deadly-lookalike-exists | True | True | regulated | T2 | agent-verified | 2041 |
| [Hen of the Woods (Grifola frondosa)](../regional/mid-atlantic-appalachian/mushrooms/entries/hen-of-the-woods-grifola.md) | MUSHROOM | low | moderate | True | False | regulated | T2 | agent-verified | 2506 |
| [Lion's Mane and Other Tooth Fungi (Hericium spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/lions-mane-hericium.md) | MUSHROOM | low | low | True | False | regulated | T2 | agent-verified | 2655 |
| [Morel (Morchella spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md) | MUSHROOM | lethal | deadly-lookalike-exists | True | True | regulated | T2 | agent-verified | 2250 |
| [Oyster Mushroom (Pleurotus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/oyster-pleurotus.md) | MUSHROOM | high | deadly-lookalike-exists | True | True | regulated | T2 | agent-verified | 2015 |
| [Wood Ear & Puffball (Auricularia & Lycoperdon spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/wood-ear-or-puffball.md) | MUSHROOM | lethal | deadly-lookalike-exists | True | True | regulated | T2 | agent-verified | 2755 |

## 2. Species: the positive-ID gate

Open each source. Check the traits in the entry's positive-ID checklist, and the disqualifying traits, against it. The two links are the sources the entry cites most often inside its gate, with a page named for the species ranked first. A source marked (general) is cited in the gate but its title does not name the species. "Gate lines" are the line numbers of the gate section.

| Species | Gate lines | Source 1 | Source 2 | Check |
|---|---|---|---|---|
| [Black Trumpet (Craterellus fallax)](../regional/mid-atlantic-appalachian/mushrooms/entries/black-trumpet-craterellus.md) | 85-112 | [T2: MushroomExpert.Com (Michael Kuo), Craterellus fallax](https://www.mushroomexpert.com/craterellus_fallax.html) | [T1: Missouri Department of Conservation, Black Trumpet (Craterellus cornucopioides, C. fallax)](https://mdc.mo.gov/discover-nature/field-guide/black-trumpet) | &#9744; |
| [Chanterelle (Cantharellus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/chanterelle-cantharellus.md) | 87-111 | [T2: MushroomExpert.Com (Michael Kuo); identification only, the site disclaims toxicity, Cantharellu...](https://mushroomexpert.com/cantharellus_lateritius.html) | [T2: MushroomExpert.Com (Michael Kuo); identification only, Cantharellus appalachiensis](https://mushroomexpert.com/cantharellus_appalachiensis.html) | &#9744; |
| [Chicken-of-the-Woods (Laetiporus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/chicken-of-the-woods-laetiporus.md) | 82-106 | [T2: MushroomExpert.Com (Michael Kuo); identification only, the site disclaims toxicity, Laetiporus...](https://mushroomexpert.com/laetiporus_sulphureus.html) | [T1: University of Florida IFAS Extension, Laetiporus (chicken of the woods) fungi, publication PP358](https://ask.ifas.ufl.edu/publication/PP358) | &#9744; |
| [Hen of the Woods (Grifola frondosa)](../regional/mid-atlantic-appalachian/mushrooms/entries/hen-of-the-woods-grifola.md) | 78-104 | [T2: MushroomExpert.Com (Michael Kuo), Grifola frondosa (Major Groups \> Polypores)](https://www.mushroomexpert.com/grifola_frondosa.html) | [T1: UMass Amherst Extension, Landscape, Nursery and Urban Forestry Program, Root and Butt Rot Cause...](https://www.umass.edu/agriculture-food-environment/landscape/fact-sheets/root-butt-rot-caused-by-grifola-frondosa-hen-of-woods) | &#9744; |
| [Lion's Mane and Other Tooth Fungi (Hericium spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/lions-mane-hericium.md) | 85-112 | [T1: Missouri Department of Conservation, Bearded Tooth (Hericium erinaceus)](https://mdc.mo.gov/discover-nature/field-guide/bearded-tooth) | [T2: MushroomExpert.Com (Michael Kuo), Hericium erinaceus](https://www.mushroomexpert.com/hericium_erinaceus.html) | &#9744; |
| [Morel (Morchella spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md) | 72-98 | [T2: MushroomExpert.Com (Michael Kuo), Morchella esculentoides](https://mushroomexpert.com/morchella_esculentoides.html) | [T1: Missouri Department of Conservation, Morels (general)](https://mdc.mo.gov/discover-nature/field-guide/morels) | &#9744; |
| [Oyster Mushroom (Pleurotus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/oyster-pleurotus.md) | 83-107 | [T1: Missouri Department of Conservation, Oyster Mushroom (Pleurotus ostreatus and P. pulmonarius)](https://mdc.mo.gov/discover-nature/field-guide/oyster-mushroom) | [T2: MushroomExpert.Com (Michael Kuo); identification only, the site disclaims toxicity, Pleurotus o...](https://mushroomexpert.com/pleurotus_ostreatus.html) | &#9744; |
| [Wood Ear & Puffball (Auricularia & Lycoperdon spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/wood-ear-or-puffball.md) | 95-133 | [T2: Beaty Biodiversity Museum, University of British Columbia, Lycoperdon pyriforme (Mushrooms Up!)](https://explore.beatymuseum.ubc.ca/mushroomsup/L_pyriforme.html) | [T2: MushroomExpert.Com (Michael Kuo), Auricularia "americana"](https://mushroomexpert.com/auricularia_americana.html) | &#9744; |

## 3. Look-alike pairs: two sources each

CONVENTIONS section 7 needs each look-alike checked against at least two Tier 1 or Tier 2 sources. The two links are the sources the entry cites on the lines that name the look-alike, with a page named for the look-alike ranked first, then the most often cited. A source marked (general) is cited on those lines but its title does not name the look-alike, so read it for the difference and look for a page that names it. "First line" is the first line that names it. If a row says only one source is cited, finding the second is part of your job. A T3 source does not count toward the two. Check that the entry's stated difference, and what the look-alike does to a person, match both sources.

| Species | Look-alike | First line | Source 1 | Source 2 | Check |
|---|---|---|---|---|---|
| [Black Trumpet (Craterellus fallax)](../regional/mid-atlantic-appalachian/mushrooms/entries/black-trumpet-craterellus.md) | Craterellus foetidus | 102 | [T2: MushroomExpert.Com (Michael Kuo), Craterellus foetidus](https://www.mushroomexpert.com/craterellus_foetidus.html) | [T2: Beaty Biodiversity Museum, University of British Columbia, Turbinellus floccosus (Mushrooms Up!...](https://explore.beatymuseum.ubc.ca/mushroomsup/T_floccosus.html) | &#9744; |
| [Black Trumpet (Craterellus fallax)](../regional/mid-atlantic-appalachian/mushrooms/entries/black-trumpet-craterellus.md) | Scaly vase (Turbinellus floccosus) | 104 | [T2: Beaty Biodiversity Museum, University of British Columbia, Turbinellus floccosus (Mushrooms Up!...](https://explore.beatymuseum.ubc.ca/mushroomsup/T_floccosus.html) | [T2: MushroomExpert.Com (Michael Kuo), Turbinellus floccosus](https://www.mushroomexpert.com/turbinellus_floccosus.html) | &#9744; |
| [Chanterelle (Cantharellus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/chanterelle-cantharellus.md) | Jack-o'-lantern (Omphalotus illudens) | 89 | [T2: MushroomExpert.Com (Michael Kuo); identification only, Omphalotus illudens](https://mushroomexpert.com/omphalotus_illudens.html) | [T1: Missouri Department of Conservation, Jack-o'-Lantern](https://mdc.mo.gov/discover-nature/field-guide/jack-o-lantern) | &#9744; |
| [Chanterelle (Cantharellus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/chanterelle-cantharellus.md) | False chanterelle (Hygrophoropsis aurantiaca) | 89 | [T2: MushroomExpert.Com (Michael Kuo); identification only, Hygrophoropsis aurantiaca](https://mushroomexpert.com/hygrophoropsis_aurantiaca.html) | [T3: Wikipedia (corroboration only; it cites Miller and Miller 2006, Jordan 2004, Sitta 2021), Hygro...](https://en.wikipedia.org/wiki/Hygrophoropsis_aurantiaca) | &#9744; |
| [Chicken-of-the-Woods (Laetiporus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/chicken-of-the-woods-laetiporus.md) | Jack-o'-lantern (Omphalotus illudens) | 94 | [T2: MushroomExpert.Com (Michael Kuo); identification only, Omphalotus illudens](https://mushroomexpert.com/omphalotus_illudens.html) | [T1: Missouri Department of Conservation, Jack-o'-Lantern](https://mdc.mo.gov/discover-nature/field-guide/jack-o-lantern) | &#9744; |
| [Chicken-of-the-Woods (Laetiporus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/chicken-of-the-woods-laetiporus.md) | Conifer-grown Laetiporus (L. huroniensis) | 95 | [T2: MushroomExpert.Com (Michael Kuo); identification only, the site disclaims toxicity, Laetiporus...](https://mushroomexpert.com/laetiporus_sulphureus.html) | [T2: Cornell Mycology blog (Cornell University), Eating the Chicken of the Woods (blog post by a stu...](https://blog.mycology.cornell.edu/2006/10/31/eating-the-chicken-of-the-woods) | &#9744; |
| [Hen of the Woods (Grifola frondosa)](../regional/mid-atlantic-appalachian/mushrooms/entries/hen-of-the-woods-grifola.md) | Black-staining polypore (Meripilus sumstinei) | 99 | [T2: MushroomExpert.Com (Michael Kuo), Meripilus sumstinei](https://www.mushroomexpert.com/meripilus_sumstinei.html) | [T2: Gary Emberger, hosted on MushroomExpert.Com, Meripilus sumstinei (Fungi on Wood, poroid fungi s...](https://mushroomexpert.com/fungionwood/poroid%20fungi/species%20pages/Meripilus%20sumstinei.htm) | &#9744; |
| [Hen of the Woods (Grifola frondosa)](../regional/mid-atlantic-appalachian/mushrooms/entries/hen-of-the-woods-grifola.md) | Berkeley's polypore (Bondarzewia berkeleyi) | 99 | [T2: MushroomExpert.Com (Michael Kuo), Bondarzewia berkeleyi](https://www.mushroomexpert.com/bondarzewia_berkeleyi.html) | [T1: Missouri Department of Conservation, Berkeley's Polypore (general)](https://mdc.mo.gov/discover-nature/field-guide/berkeleys-polypore) | &#9744; |
| [Lion's Mane and Other Tooth Fungi (Hericium spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/lions-mane-hericium.md) | Branched Hericium species (H. americanum, H. coralloides) | 94 | [T2: MushroomExpert.Com (Michael Kuo), Hericium americanum](https://www.mushroomexpert.com/hericium_americanum.html) | [T2: MushroomExpert.Com (Michael Kuo), Hericium coralloides](https://www.mushroomexpert.com/hericium_coralloides.html) | &#9744; |
| [Lion's Mane and Other Tooth Fungi (Hericium spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/lions-mane-hericium.md) | Northern tooth (Climacodon septentrionalis) | 107 | [T2: Gary Emberger, hosted on MushroomExpert.Com, Climacodon septentrionalis (Fungi on Wood, teeth a...](https://www.mushroomexpert.com/fungionwood/teeth%20and%20spine/species%20pages/Climacodon%20septentrionalis.htm) | [T3: mushroom-appreciation.com, Northern tooth (Climacodon septentrionalis)](https://mushroom-appreciation.com/northern-tooth.html) | &#9744; |
| [Lion's Mane and Other Tooth Fungi (Hericium spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/lions-mane-hericium.md) | Hedgehog mushroom (Hydnum repandum) | 107 | [T1: Missouri Department of Conservation, Bearded Tooth (Hericium erinaceus) (general)](https://mdc.mo.gov/discover-nature/field-guide/bearded-tooth) | [T1: Minnesota Department of Natural Resources, Lion's Mane (Minnesota Conservation Volunteer, Septe...](https://dnr.state.mn.us/mcvmagazine/issues/2018/sep-oct/lions-mane.html) | &#9744; |
| [Morel (Morchella spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md) | False morels (Gyromitra spp., incl. G. caroliniana) | 76 | [T2: MushroomExpert.Com (Michael Kuo), Gyromitra caroliniana](https://mushroomexpert.com/gyromitra_caroliniana.html) | [T2: North American Mycological Association, Mushroom Poisoning Syndromes (general)](https://www.namyco.org/mushroom_poisoning_syndromes.php) | &#9744; |
| [Morel (Morchella spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md) | Early false morel (Verpa bohemica) | 76 | [T2: MushroomExpert.Com (Michael Kuo), Verpa bohemica](https://mushroomexpert.com/verpa_bohemica.html) | [T1: Missouri Department of Conservation, Morels (general)](https://mdc.mo.gov/discover-nature/field-guide/morels) | &#9744; |
| [Morel (Morchella spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md) | Elfin saddles (Helvella spp.) | 115 | [T1: Missouri Department of Conservation, Morels (general)](https://mdc.mo.gov/discover-nature/field-guide/morels) | **only one source cited in the entry: find a second** | &#9744; |
| [Oyster Mushroom (Pleurotus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/oyster-pleurotus.md) | Angel wings (Pleurocybella porrigens) | 85 | [T2: Gary Emberger, hosted on MushroomExpert.Com; identification only, Pleurocybella porrigens (Fung...](https://mushroomexpert.com/fungionwood/gilled%20fungi/species%20pages/Pleurocybella%20porrigens.htm) | [T2: NAMA (namyco.org; author Michael Beug, not an official NAMA policy statement), Pleurocybella to...](https://namyco.org/pleurocybella_toxin.php) | &#9744; |
| [Oyster Mushroom (Pleurotus spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/oyster-pleurotus.md) | Jack-o'-lantern (Omphalotus illudens) | 85 | [T2: MushroomExpert.Com (Michael Kuo); identification only, Omphalotus illudens](https://mushroomexpert.com/omphalotus_illudens.html) | [T1: Missouri Department of Conservation, Jack-o'-Lantern](https://mdc.mo.gov/discover-nature/field-guide/jack-o-lantern) | &#9744; |
| [Wood Ear & Puffball (Auricularia & Lycoperdon spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/wood-ear-or-puffball.md) | Amanita egg button (destroying angel, A. bisporigera) | 97 | [T1: Missouri Department of Conservation, Destroying Angel (Amanita bisporigera)](https://mdc.mo.gov/discover-nature/field-guide/destroying-angel) | [T1: CDC, Amanita phalloides Mushroom Poisonings - Northern California, December 2016 (MMWR 66(21))](https://www.cdc.gov/mmwr/volumes/66/wr/mm6621a1.htm) | &#9744; |
| [Wood Ear & Puffball (Auricularia & Lycoperdon spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/wood-ear-or-puffball.md) | Earthballs (Scleroderma spp.) | 104 | [T2: MushroomExpert.Com (Michael Kuo), Scleroderma citrinum](https://mushroomexpert.com/scleroderma_citrinum.html) | [T1: Missouri Department of Conservation, Gem-Studded Puffball (general)](https://mdc.mo.gov/discover-nature/field-guide/gem-studded-puffball) | &#9744; |
| [Wood Ear & Puffball (Auricularia & Lycoperdon spp.)](../regional/mid-atlantic-appalachian/mushrooms/entries/wood-ear-or-puffball.md) | Wood ear look-alikes (Exidia, Tremella) | 160 | [T2: MushroomExpert.Com (Michael Kuo), Auricularia "americana" (general)](https://mushroomexpert.com/auricularia_americana.html) | **only one source cited in the entry: find a second** | &#9744; |

## 4. Highest-stakes claims

Open the source link. Find the sentence that backs the claim. Tick **ok** if the source says the same thing, with the same number, unit and condition. Tick **flag** if it does not, and file it with the correction template (see the packet).

| # | Claim, exact as written | File and line | Source (from the entry's own Sources) | Check |
|---|---|---|---|---|
| 1 | "Slice it from the top to the bottom of the stem. The cap and the stem are hollow all the way down" | [morel-morchella.md](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md), line 81 | [T1: Missouri Department of Conservation, Morels](https://mdc.mo.gov/discover-nature/field-guide/morels)<br>[T2: MushroomExpert.Com (Michael Kuo), Morchella esculentoides](https://mushroomexpert.com/morchella_esculentoides.html) | &#9744; ok<br>&#9744; flag |
| 2 | "NAMA says gyromitrin poisoning symptoms appear within 2 to 24 hours and include headaches, abdominal distress, severe diarrhea and vomiting" | [morel-morchella.md](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md), line 106 | [T2: North American Mycological Association, Mushroom Poisoning Syndromes](https://www.namyco.org/mushroom_poisoning_syndromes.php) | &#9744; ok<br>&#9744; flag |
| 3 | "after the recommended double boiling, about 18% of the original toxin remained on average, and that drying left up to half" | [morel-morchella.md](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md), line 107 | [T1: Finnish Food Authority (Ruokavirasto), Report: nearly one-fifth of toxin remains in false morel...](https://www.ruokavirasto.fi/en/themes/risk-assessment/risk-assessment-news/news-about-risk-assessment/report-nearly-one-fifth-of-toxin-remains-in-false-morels-despite-boiling-recommendation/) | &#9744; ok<br>&#9744; flag |
| 4 | "Chanterelle flesh is white and unchanging (C. lateritius) or whitish to yellowish and unchanging (C. appalachiensis) \[2\]\[3\]. Jack-o'-lantern flesh is pale orange \[5\]." | [chanterelle-cantharellus.md](../regional/mid-atlantic-appalachian/mushrooms/entries/chanterelle-cantharellus.md), line 102 | [T2: MushroomExpert.Com (Michael Kuo); identification only, the site disclaims toxicity, Cantharellu...](https://mushroomexpert.com/cantharellus_lateritius.html)<br>[T2: MushroomExpert.Com (Michael Kuo); identification only, Cantharellus appalachiensis](https://mushroomexpert.com/cantharellus_appalachiensis.html)<br>[T2: MushroomExpert.Com (Michael Kuo); identification only, Omphalotus illudens](https://mushroomexpert.com/omphalotus_illudens.html) | &#9744; ok<br>&#9744; flag |
| 5 | "Onset: typically 1 to 3 hours after the meal" | [chanterelle-cantharellus.md](../regional/mid-atlantic-appalachian/mushrooms/entries/chanterelle-cantharellus.md), line 198 | [T2: North American Mycological Association, Mushroom Poisoning Syndromes](https://www.namyco.org/mushroom_poisoning_syndromes.php) | &#9744; ok<br>&#9744; flag |
| 6 | "Cornell says the glow fades after the mushroom is picked, so no glow proves nothing" | [chanterelle-cantharellus.md](../regional/mid-atlantic-appalachian/mushrooms/entries/chanterelle-cantharellus.md), line 139 | [T2: Cornell Mycology blog (Cornell University), An adventure with Omphalotus](https://blog.mycology.cornell.edu/2007/04/02/an-adventure-with-omphalotus) | &#9744; ok<br>&#9744; flag |
| 7 | "L. sulphureus has bright to dull yellow pores, 2 to 4 per mm, that do not bruise" | [chicken-of-the-woods-laetiporus.md](../regional/mid-atlantic-appalachian/mushrooms/entries/chicken-of-the-woods-laetiporus.md), line 88 | [T2: MushroomExpert.Com (Michael Kuo); identification only, the site disclaims toxicity, Laetiporus...](https://mushroomexpert.com/laetiporus_sulphureus.html) | &#9744; ok<br>&#9744; flag |
| 8 | "Both have true gills, so "gill edge" and "ridge vs. gill" tests do not work." | [oyster-pleurotus.md](../regional/mid-atlantic-appalachian/mushrooms/entries/oyster-pleurotus.md), line 103 | [T1: Missouri Department of Conservation, Oyster Mushroom (Pleurotus ostreatus and P. pulmonarius)](https://mdc.mo.gov/discover-nature/field-guide/oyster-mushroom) | &#9744; ok<br>&#9744; flag |
| 9 | "in autumn 2004 Japan had 59 sick in 9 prefectures and 17 deaths from acute encephalopathy" | [oyster-pleurotus.md](../regional/mid-atlantic-appalachian/mushrooms/entries/oyster-pleurotus.md), line 125 | [T2: NAMA (namyco.org; author Michael Beug, not an official NAMA policy statement), Pleurocybella to...](https://namyco.org/pleurocybella_toxin.php)<br>[T2: North American Mycological Association, Mushroom Poisoning Syndromes](https://www.namyco.org/mushroom_poisoning_syndromes.php) | &#9744; ok<br>&#9744; flag |
| 10 | "CUT AND INSPECT, every one, top to bottom (non-negotiable) \[1\]\[2\]. Pure white and solid, or discard." | [wood-ear-or-puffball.md](../regional/mid-atlantic-appalachian/mushrooms/entries/wood-ear-or-puffball.md), line 206 | [T1: Missouri Department of Conservation, Gem-Studded Puffball](https://mdc.mo.gov/discover-nature/field-guide/gem-studded-puffball)<br>[T1: Missouri Department of Conservation, Pear-Shaped Puffball](https://mdc.mo.gov/discover-nature/field-guide/pear-shaped-puffball) | &#9744; ok<br>&#9744; flag |
| 11 | "symptoms are delayed 6 to 24 hours after eating, and "typically do not appear until 12 or more hours" \[7\]. Missouri: 6 to 24 hours \[8\]." | [wood-ear-or-puffball.md](../regional/mid-atlantic-appalachian/mushrooms/entries/wood-ear-or-puffball.md), line 147 | [T2: North American Mycological Association, Mushroom Poisoning Syndromes](https://www.namyco.org/mushroom_poisoning_syndromes.php)<br>[T1: Missouri Department of Conservation, Destroying Angel (Amanita bisporigera)](https://mdc.mo.gov/discover-nature/field-guide/destroying-angel) | &#9744; ok<br>&#9744; flag |
| 12 | "the patient "may appear to recover about day two or day three and be sent home"" | [wood-ear-or-puffball.md](../regional/mid-atlantic-appalachian/mushrooms/entries/wood-ear-or-puffball.md), line 149 | [T2: North American Mycological Association, Mushroom Poisoning Syndromes](https://www.namyco.org/mushroom_poisoning_syndromes.php) | &#9744; ok<br>&#9744; flag |

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

### Amatoxin mortality is stated as a range, from under 5% to about 50%

The numbers come from different populations and care levels, so the repo gives all of them. A reader could still treat the lowest as the likely outcome. Decide whether the range, and the sentence after it, protect the reader. The same range appears in [domain 06](06_hazards_mid_atlantic.md).

> NAMA's poisoning-syndromes page gives about 50% without prompt, knowledgeable medical treatment and about 10% in the U.S. and Canada [7]. CDC cites a case fatality rate of 10% to 20% [10]. StatPearls says fewer than 5% of cases in developed countries with early intensive care [11].
>
> From [wood-ear-or-puffball.md](../regional/mid-atlantic-appalachian/mushrooms/entries/wood-ear-or-puffball.md), line 150.

### Cooking time and temperature: no source gives one, so the entries give none

Several entries say "cook thoroughly" and then state that no opened source gives a time or temperature. Decide whether a public reference should stay silent on this or point to a source that does.

> Cook thoroughly [1][5]. No opened source gives a time or temperature, so none is given here.
>
> From [morel-morchella.md](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md), line 155.

### Lion's mane: one source says it has no poisonous look-alikes

The entry reports the claim and still requires the full gate and expert confirmation. Decide whether the entry's confusability level and tone fit that.

> No deadly or toxic look-alike is named by any source opened for this entry.
>
> From [lions-mane-hericium.md](../regional/mid-atlantic-appalachian/mushrooms/entries/lions-mane-hericium.md), line 115.

### Black trumpet: no deadly look-alike is named, and that is flagged as missing data

Decide whether "none named by the sources opened" is acceptable for a species that still needs expert confirmation, or whether a reviewer who knows the region can name one.

> No deadly look-alike is named by any source opened for this entry.
>
> From [black-trumpet-craterellus.md](../regional/mid-atlantic-appalachian/mushrooms/entries/black-trumpet-craterellus.md), line 115.

### Verpa bohemica: sources do not settle whether it is toxic

The entry tells the reader to treat it as not a morel and not eat it. Decide whether that is the right line.

> the sources opened do not settle whether Verpa is toxic.
>
> From [morel-morchella.md](../regional/mid-atlantic-appalachian/mushrooms/entries/morel-morchella.md), line 113.

### Doctrine point 1: no consumption without an expert who has examined the specimen

This is the repo's strictest rule, and it replaced a softer "definitive multi-source ID" wording. Decide whether it is the right bar and whether the doctrine page states it plainly enough. The text is in [CONVENTIONS.md](../CONVENTIONS.md) section 4.

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
