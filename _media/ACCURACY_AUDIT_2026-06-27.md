# Accuracy Audit + Remediation Log — 2026-06-27

Independent fact-check of the biology/medical entries (web-triangulated against CDC, USDA, WHO,
mycological societies, university extension, poison control). Structure/navigation/answer-policy
passed separately (readability 84–88, offline read-test PASS). This log tracks the FACTUAL
corrections. Status column updated as fixes land.

> **Pattern:** the deadly-look-alike *field discriminators* (pitted/hollow morel, onion-smell test,
> puffball cut-test, ridges-vs-gills) audited CORRECT. The errors are in **species names, toxin
> names/classes, spore-print colors, and numeric values** — confident text that is wrong in
> specific, dangerous ways. Exactly what the human safety-read exists to catch.

## CRITICAL (fix before sign-off)

| # | File | Error | Correct fact + source | Status |
|---|------|-------|------------------------|--------|
| C1 | edible-plants/wild-onion-garlic-allium + edible-plants/_index + mushrooms/_index | Death camas named **`Toxicoscordion venenosum`** = a WESTERN species, not Mid-Atlantic; "prefers water edges" false for it; toxin listed as **bufadienolides** (wrong class) | Eastern death-camas: *Anticlea elegans/glauca* (Appalachian mtns), *Zigadenus glaberrimus* (coastal plain VA/Carolinas), + *Amianthium muscitoxicum* (fly poison, broadly eastern). Toxin = **veratrum/cevanine steroidal alkaloids (zygacine)**, Na-channel mechanism. Onion-smell rule still valid. (Wikipedia, NC Extension, FSUS, Cornell Poisonous Plants) | FIXED |
| C2 | game-animals/raccoon-or-opossum | Trichinella cook floor **160°F** | CDC wild-game Trichinella floor **≥165°F**; keep 170°F+ as margin (CDC Trichinellosis) | FIXED |
| C3 | first_aid/dehydration-and-diarrhea | ORS sugar **"30 grams"** (excess sugar → osmotic, worsens diarrhea) | WHO ORS ≈ **18–20 g sugar** (6 level tsp) + ~3 g salt per 1 L (WHO/CDC ORS) | FIXED |
| C4 | edible-plants/cattail | Iris toxin "**irisin, a glycoside**" causing "**tremors**" — wrong name, wrong class, wrong symptom | Iris toxins = **pentacyclic terpenoids (zeorin, missourin, missouriensin)**; GI symptoms only — **delete tremors** (neurotoxin implication). (ASPCA, LSU VetMed, ACEP) | FIXED |

## MAJOR (fix before publish)

| # | File | Error | Correct fact + source | Status |
|---|------|-------|------------------------|--------|
| M1 | water/boil-disinfection | Invented **2-min altitude band** (6,500–10,000 ft); implies 3 min only >10,000 ft | CDC/EPA binary: **1 min ≤6,500 ft, 3 min >6,500 ft**. Remove the 2-min tier. | FIXED |
| M2 | water/filtration-micron-guide | Giardia/Crypto micron logic **backwards** (Giardia 8–12µm is larger/easier than Crypto 4–6µm) | **≤1 µm absolute removes BOTH** Giardia + Crypto; 0.2 µm is for bacteria. (CDC/EPA) | FIXED |
| M3 | water/chemical-treatment | Only 5–6% bleach; omits common **8.25%** | Add 8.25% line: ~6 drops/gal (≈1.6 drops/L), double if cloudy. (CDC/EPA) | FIXED |
| M4 | edible-plants/acorn-oak | Nutrition ~30% low (370 cal); float test overstated | USDA acorn flour full-fat = **~500 cal/100g, 30g fat, 55g carb**; float test ~50% false-positive (USDA #170566; NCSU Morina 2017) | FIXED |
| M5 | mushrooms/morel-morchella | Gyromitrin "reliably destroyed by cooking" (false); MMH = "irreversible MAO inhibitor" (wrong) | ~20% gyromitrin survives recommended boiling — **cannot be made safe** (Finnish Food Authority). MMH = **PLP/B6 antagonist → GABA depletion**, treat w/ pyridoxine. Regional spp = *Neogyromitra caroliniana/brunnea*. (StatPearls, NAMA) | FIXED |
| M6 | mushrooms/wood-ear-or-puffball + mushrooms/_index | "50–90% mortality"; missing *A. phalloides* east; missing **Scleroderma (earthball)** look-alike | ~**50% untreated / ~10% treated** (NAMA). *A. phalloides* present MD→Maine. Add **Scleroderma** (dark interior, thick rind — cut test rules out). IV silibinin is the real antidote (oral milk thistle ineffective). | FIXED |
| M7 | mushrooms/chicken-of-the-woods-laetiporus | Spore print "yellow to white"; only L. sulphureus; pores "yellow to orange" | Spore print = **white** (genus-wide). Note **L. cincinnatus** (white pores, base/rosette) + **L. huroniensis** (hemlock/conifer — the GI-risk one). Sulphureus pores = bright sulfur-yellow. Name **Omphalotus illudens** as the gilled look-alike. (MushroomExpert, Wikipedia) | FIXED |
| M8 | mushrooms/chanterelle-cantharellus | `C. cibarius` (European); Hygrophoropsis "intermediate gills"; spore print imprecise | Mid-Atlantic = ***C. lateritius*, *C. appalachiensis*** (cibarius s.s. is European). False chanterelle has **TRUE forked gills** (not intermediate) + is now classed **poisonous** (arabitol GI; anecdotal neuro). Chanterelle spore print pale cream. | FIXED |
| M9 | mushrooms/oyster-pleurotus + mushrooms/_index | Jack-o'-lantern: `O. olearius` (European); spore print "orange"; illudins = "cholinergic agonists" | Eastern = ***O. illudens***. Spore print **white-to-cream** (cap is orange, not spores). Illudins = **DNA-alkylating cytotoxins**, NOT cholinergic (muscarine presence unconfirmed). Bioluminescence not a usable field test (already fixed in index). | FIXED |
| M10 | mushrooms/_index + edible-plants/_index manifests | `field_id_not_appropriate` not a manifest column (highest-stakes facet not filterable from the index) | Add the column to both biology manifests. | FIXED |
| M11 | edible-plants/wild-onion-garlic-allium | `preparation_required: false` contradicts its own `## ⚠ MANDATORY PREPARATION` section | Reconcile facet ↔ body (the entry has a prep section; either set true or remove the section — set true to match the section). | FIXED |
| M12 | all 11 survey files + 2 stubs | Stray victorious-repo YAML frontmatter ("Documentation for shared-foundation workstream") + a personal `c:\Users\victor\...` path in 10_key_resources.md | Strip the foreign frontmatter from all 13 files; remove the personal path. | FIXED |
| M13 | edible-plants/cattail + violet-or-chickweed | cattail/iris discriminator incomplete (add D-shape cross-section + base color); chickweed missing milky-sap spurge caveat; ramps need explicit smell-test + lily-of-the-valley/Veratrum warning | Add the stronger discriminators + the ramp smell-test rule. | FIXED |

## MINOR (deferred — logged for a later pass, not blocking)
- deer "aerosol prion" framing imprecise; squirrel "prion" parenthetical (no squirrel prion); raccoon "fat harbors cysts" (cysts are in muscle); heat-stroke ice-water caution vs current "cold-water-immersion is gold standard"; "30–40% heat loss through scalp" overstated; stored-treated-water shelf-life generous; DKA 24–48h (can be 6–12h); manifest "present"-label consistency; FM 21-76 inline-cite not in frontmatter sources; check_manifests boxes unchecked.

## Round 2 — Independent re-verification of the CORRECTED entries (web-sourced, 3 fresh agents)

After the round-1 fixes, a second independent verification pass (mushrooms / plants / water-firstaid-game,
each web-triangulated) confirmed the round-1 corrections were applied correctly AND caught issues the
correction pass itself introduced or left:

| # | File | Finding | Fix | Status |
|---|------|---------|-----|--------|
| R2-C1 | mushrooms/chanterelle-cantharellus | **CRITICAL (introduced):** safety gate + ID + prep step 8 all said "orange spore print = jack-o'-lantern (discard)" — but *O. illudens* spore print is **white-to-cream, same as chanterelle**; a forager could take a print, see cream, and wrongly proceed | Removed the false spore-print discriminator in all 3 spots; decisive test restated as blunt-forked-ridges (chanterelle) vs true-gills (jack-o'-lantern); spore print explicitly stated NOT to discriminate | FIXED + re-verified |
| R2-M1 | mushrooms/wood-ear-or-puffball | amatoxin "50–90% untreated mortality" overstated | → ~20–50% untreated / ~10–20% treated (NAMA) | FIXED |
| R2-M2 | edible-plants/acorn-oak | **2 fabricated citations** (an obsidian-dating paper; a carob-flavonoid paper — Haiku hallucinations) | → Bainbridge 1986 (USDA), USDA FDC 170566, Morina 2017 | FIXED |
| R2-M3 | edible-plants/wild-onion-garlic-allium | missing the documented ramp look-alikes (false hellebore *Veratrum viride* = #1 ramp-foraging poisoning cause; lily-of-the-valley *Convallaria*) | Added both with discriminators; both caught by the onion-smell gate | FIXED |

Water / first-aid / game (10 entries): round-2 verdict **SHIP** — 0 critical, 0 major; all round-1
corrections (boil binary, filter micron, bleach 8.25%, ORS 18–20g, heat-stroke immersion, raccoon 165°F)
verified correct vs CDC/EPA/WHO/USDA/Stop-the-Bleed. Only trivial annotation nits (ORS salt "2.5g" vs ~3g).

**Round-3 targeted re-check of the 4 edited files: FINAL = SHIP** (0 critical, 0 major remaining; the
chanterelle critical confirmed resolved in every "spore print" mention). One non-safety wording tension
left for the human read (chanterelle line ~59 "...AND spore print" phrasing).

## Sign-off
- Two web-sourced verification rounds + a targeted re-check. All CRITICAL and MAJOR findings resolved
  and re-verified. Remaining items are MINOR (logged above), non-safety.
- **The Phase-11 human safety-read by Victor still governs** — this brings the entries to verified-accurate;
  it does not replace his read.
