# Northeast / New England — Game Animals (GAME-ANIMAL)

> Wild game of New Hampshire, Vermont, Maine, Massachusetts, Connecticut and upstate and eastern New York. Two
> non-negotiables lead every entry: a **legal/ethical note** (normal regulated season; no source cited here
> gives a survival exemption; *know your local regs, this is not legal advice*) and a
> **`## ⚠ DISEASE & PARASITE`** block (CWD prion for deer, tularemia for hare, bird flu for grouse). Hunting
> and trapping are different systems with different licenses and seasons; these entries cover **hunting
> seasons only** and give no snare or trap method. White-tailed **deer** is the full-flow species
> (field-dress, skin, butcher, preserve) and carries the **CWD/prion** warning.
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Schema:
> [`../../../SCHEMAS.md`](../../../SCHEMAS.md) §4. Processing technique:
> [`../../../substrate/05_food/_index.md`](../../../substrate/05_food/_index.md).

---

## ⚠ Disease, look-alike & legal surface (read BEFORE pursuing game)

| Animal | ☠ Disease / look-alike watch | Never eat / handling rule | Legal frame |
|--------|------------------------------|---------------------------|-------------|
| **White-tailed deer** | **CWD (chronic wasting disease, a prion)**; cooking does not destroy prions. CDC: no human case reported, and it is not known whether people could be infected; studies in monkeys suggest they could get CWD from infected meat or brain. Status by state: Maine never found; New Hampshire 402 deer tested negative in 2025; Vermont working to keep it out; Massachusetts no evidence of it; Connecticut none detected; New York found it in a captive herd in 2024 (Maine IFW also reports a 2005 New York case) and is testing wild deer nearby | **Never eat brain, spinal cord, eyes, spleen, tonsils or lymph nodes.** Bone out; wear gloves; do not take or eat an animal that looks sick or was found dead; test where testing is offered. Do not use natural deer-urine lures. Import rules differ by state: Maine allows high-risk parts in only from New Hampshire (boned-out meat, hardened antlers, hides without the head and finished mounts only); Massachusetts bars whole carcasses and high-risk parts from outside New England; New Hampshire, Vermont and Connecticut bar them from CWD-positive jurisdictions (deboned meat and a few clean parts only). Debone before you cross a state line and read the destination state's agency page. Massachusetts and Maine do not test individual deer on request. Rhode Island is not covered; check Rhode Island DEM | Regulated seasons, tags, stamps and permits that differ by state; hunting is not allowed on Sundays in Massachusetts; no cited page gives a survival exemption |
| **Ruffed grouse** | **Bird flu** in wild birds (CDC). **Protected look-alike: the spruce grouse** (no open season in Maine and New Hampshire; state endangered in Vermont and New York); females are the hard case | Gloves; do not handle sick or found-dead birds; cook to 165°F. **Do not shoot a grouse you cannot tell from a spruce grouse; check the tail** (ruffed: broad black band near the tip; spruce: tail ends in a chestnut tip, no broad black band) | Regulated fall season by state; Connecticut adds a game bird stamp; no cited page gives a survival exemption |
| **Snowshoe hare** | **Tularemia** (CDC: rabbits and hares are especially susceptible; can be life-threatening). **Protected look-alike: the New England cottontail** (Maine and New Hampshire protect it; reliable ID needs skull or DNA) | **Gloves**; discard the animal if the liver has numerous white pinhead spots; cook to 165°F; do not handle a hare that is sick or found dead; do not take a rabbit you cannot rule out as a protected cottontail | Regulated fall-to-winter season by state; Maine has no open season on cottontail; no cited page gives a survival exemption |

> **CWD prion is the master warning for deer.** Cooking does not destroy prions (MassWildlife, Maine IFW).
> The control is anatomical avoidance (no brain, spinal cord, lymph tissue, eyes, spleen or tonsils), testing
> where it is offered, and not taking visibly sick animals. Appearance never rules CWD out: MassWildlife says
> infected deer can look healthy for over 18 months. **Cook ALL wild meat thoroughly** regardless. Internal
> cook temps and the full processing chain live in each entry's `## ⚠ MANDATORY PREPARATION`.
>
> **Two protected look-alikes change what you may shoot.** Spruce grouse and New England cottontail are
> protected species that resemble huntable game. No single trait clears either one, and each entry gives the
> multi-trait comparison and the state sources.
>
> **Legal/ethical:** seasons, methods and licensing are jurisdictional and change every year. Entries show the
> dates agencies published for 2026 (or the most recent year found), set `legal_status: regulated`, and say
> plainly that no cited source gives a survival exemption. **This is not legal advice; check the state agency**
> (`../../../CONVENTIONS.md` §9 rule 6).

---

## Synthesis & load order

Hunting seasons here are short and unit-specific, so small game (hare) and the grouse season are the
realistic protein in fall, while **deer** is the high-value, high-effort prize that demands the full
processing chain and the strictest disease discipline. In a real emergency, passive trapping can beat
hunting for calorie cost (see [`../../../substrate/05_food/_index.md`](../../../substrate/05_food/_index.md)),
but trapping is regulated separately from hunting. Load order:

```
1. DISEASE, LOOK-ALIKE & LEGAL SURFACE (above) — prions, bird flu, tularemia, protected look-alikes, know-your-regs, BEFORE pursuit
2. This manifest                    — find the entry + read its facets
3. The animal entry                 — Legal/Ethical → ID/behavior (+ protected look-alike) → harvest → (deer) full processing chain
                                       → ⚠ DISEASE & PARASITE → ⚠ MANDATORY PREPARATION (cook temps, never-eat)
4. Processing TECHNIQUE             → ../../../substrate/05_food/ (gut/skin/butcher/preserve is universal craft)
5. CITE (state wildlife agency / CDC / extension, T1)
```

Not yet written for this region: cottontail, gray squirrel, wild turkey, bear, moose, raccoon. Use the survey
guide [`../../../05_food.md`](../../../05_food.md) and the state agency for those, and do not infer anything
about them from the entries below.

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| white-tailed-deer-new-england | entries/white-tailed-deer-new-england.md | GAME-ANIMAL | northeast-new-england | fall to early winter (regulated; archery from mid-Sept to early Oct, firearms late Oct to Dec by state) | edible-when-prepared | high | none | false | T1 | 17 | agent-verified |
| ruffed-grouse | entries/ruffed-grouse.md | GAME-ANIMAL | northeast-new-england | fall to early winter, late Sept or Oct to Nov or Dec 31 (regulated; New York to Feb) | edible-when-prepared | moderate | moderate | false | T1 | 17 | agent-verified |
| snowshoe-hare | entries/snowshoe-hare.md | GAME-ANIMAL | northeast-new-england | fall to late winter, late Sept or Oct to Feb or Mar (regulated; by state and unit) | edible-when-prepared | high | moderate | false | T1 | 22 | agent-verified |

`legal_status: regulated` is set in-entry for all (no cited source supports a survival exemption; entries say
so). Deer and hare are `hazard_severity: high` (CWD prion; tularemia). Deer is the full-flow species. Sources:
state wildlife agencies, CDC and extension services (T1).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/` (three rows, three entry files).
- [x] Every entry file has a row (no orphans).
- [x] Required columns filled.
- [x] CWD-prion (deer) / tularemia (hare) / bird flu (grouse) blocks present, and protected look-alikes covered (spruce grouse, New England cottontail).
- [x] Deer entry has the full field-dress → skin → butcher → preserve flow; internal cook temps match `05_food.md` (venison 160°F; hare and game birds 165°F).
- [x] `legal_status` is `regulated`; entries distinguish hunting from trapping, say no cited source gives a survival exemption, and are framed as "know your regs," not legal advice.
- [ ] Human safety read (Phase 11) not yet done: all three entries are `review_status: draft`.
