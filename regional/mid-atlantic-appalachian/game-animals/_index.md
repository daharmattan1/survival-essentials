# Mid-Atlantic / Appalachian — Game Animals (GAME-ANIMAL)

> Wild game of this biome. Two non-negotiables lead every entry: a **legal/ethical note** (normal
> regulated season vs. genuine emergency — *know your local regs, this is not legal advice*) and a
> **`## ⚠ DISEASE & PARASITE`** block (prions, raccoon roundworm, rabies, trichinella, tularemia). White-tailed **deer** is the
> mandatory full-flow species (field-dress → skin → butcher → preserve) and carries the **CWD/prion**
> warning.
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Schema:
> [`../../../SCHEMAS.md`](../../../SCHEMAS.md) §4. Processing technique: [`../../../substrate/05_food/_index.md`](../../../substrate/05_food/_index.md).

---

## ⚠ Disease & legal surface (read BEFORE pursuing game)

| Animal | ☠ Disease / parasite watch | Never eat / handling rule | Legal frame |
|--------|----------------------------|---------------------------|-------------|
| **White-tailed deer** | **CWD (chronic wasting disease — prion)**; cooking does not destroy prions. CDC: no human case reported, but studies in monkeys suggest they could get CWD from eating infected meat or brain | **Never eat brain, spinal cord, eyes, spleen, tonsils or lymph nodes.** Bone out; avoid cutting through spine. Do not take, touch or eat animals that look sick, emaciated or were found dead. | Regulated season and licence; no opened MD, PA, WV or VA page gives a survival exemption — know your state agency's regs. |
| **Eastern cottontail (rabbit)** | **Tularemia** (more common in warm months, but cold weather does not eliminate the risk in rabbit season; Missouri Dept. of Conservation, CDC) | **Wear gloves** dressing in every season; check the liver; cook to 165°F; do not handle sick-acting or found-dead rabbits. | Regulated season and licence; small game. |
| **Gray squirrel** | Tularemia handling (CDC: gloves for rodents); general parasites/bacteria | Gloves; cook to 165°F; inspect for lesions. **Delmarva Peninsula: the protected Delmarva fox squirrel (larger, silver-gray) is closed to hunting in MD and DE. Do not shoot a squirrel you cannot tell apart.** | Regulated season and licence; small game. |
| **Wild turkey** | Poultry-type bacteria (Salmonella, Campylobacter); bird flu in wild birds (CDC) | Gloves; do not handle sick or found-dead birds; cook to 165°F. | Regulated season and licence: spring (about mid-April to late May, bearded birds only) and fall by county or unit; seasons change yearly. |
| **Raccoon / opossum** | **Raccoon roundworm (*Baylisascaris procyonis*), life-threatening: swallowed eggs from raccoon feces can reach the nervous system; death or permanent disability is common (CDC)**; rabies (raccoon); *Trichinella* | **Gloves, no hands-to-face while dressing, wash hands, avoid latrines; seek care promptly after any possible exposure.** Cook to 165°F to kill *Trichinella*; least-preferred. | Regulated furbearer; licence required (PA: furtaker licence); check locally. |

> **CWD prion is the master warning.** Cooking temperatures do not destroy prions (Alberta Health, cited
> in the deer entry). CDC reports no human case, but says studies in monkeys suggest they could get CWD by
> eating infected meat or brain. The control is anatomical avoidance (no brain, spinal cord, lymph tissue,
> eyes or tonsils), testing where CWD is present, and not taking visibly sick animals. **Cook ALL wild
> meat thoroughly** regardless. **Raccoon roundworm is the other life-threatening hazard:** it comes from
> swallowed eggs in raccoon feces, so the control is gloves, hands away from the face, and hand washing. Internal cook temps and the
> full processing chain live in each entry's `## ⚠ MANDATORY PREPARATION`.
>
> **Legal/ethical:** seasons, methods, and licensing are jurisdictional. Entries describe normal
> regulated seasons informationally and set `legal_status: regulated` and say plainly that no opened source gives
> a survival exemption — **this is not legal advice; know your local regulations** (`../../../CONVENTIONS.md` §9 rule 6).

---

## Synthesis & load order

In a real emergency, **trapping beats hunting** (passive, lower calorie cost — see
[`../../../substrate/05_food/_index.md`](../../../substrate/05_food/_index.md)), so small game
(rabbit, squirrel) is the realistic protein, while **deer** is the high-value, high-effort prize that
demands the full processing chain and the strictest disease discipline. Load order:

```
1. DISEASE & LEGAL SURFACE (above)  — prions/parasites + know-your-regs, BEFORE pursuit
2. This manifest                    — find the entry + read its facets
3. The animal entry                 — Legal/Ethical → ID/behavior → harvest → (deer) full processing chain
                                       → ⚠ DISEASE & PARASITE → ⚠ MANDATORY PREPARATION (cook temps, never-eat)
4. Processing TECHNIQUE             → ../../../substrate/05_food/ (gut/skin/butcher/preserve is universal craft)
5. CITE (USDA / state DNR / extension — T1/T2)
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| white-tailed-deer | entries/white-tailed-deer.md | GAME-ANIMAL | mid-atlantic-appalachian | fall to early winter (regulated; archery from late Sept or Oct) | edible-when-prepared | high | none | false | T1 | 21 | reviewed |
| eastern-cottontail-rabbit | entries/eastern-cottontail-rabbit.md | GAME-ANIMAL | mid-atlantic-appalachian | fall–winter, Oct–Feb (regulated) | edible-when-prepared | high | none | false | T1 | 16 | reviewed |
| gray-squirrel | entries/gray-squirrel.md | GAME-ANIMAL | mid-atlantic-appalachian | fall–winter, Sep–Feb (regulated) | edible-when-prepared | moderate | low | false | T1 | 18 | reviewed |
| wild-turkey | entries/wild-turkey.md | GAME-ANIMAL | mid-atlantic-appalachian | spring (about mid-Apr to late May, bearded birds) and fall by county or unit (regulated) | edible-when-prepared | moderate | none | false | T1 | 16 | reviewed |
| raccoon-or-opossum | entries/raccoon-or-opossum.md | GAME-ANIMAL | mid-atlantic-appalachian | fall–winter furbearer seasons, about mid-Oct or Nov to late Feb or early Mar (Virginia hunting Oct 15–Mar 10; trapping Nov 15–Feb 28) (regulated) | edible-when-prepared | high | none | false | T1 | 24 | reviewed |

`legal_status: regulated` is set in-entry for all (no opened source supports a survival exemption; entries say so). Deer + rabbit + raccoon are
`hazard_severity: high` (CWD prion / tularemia / raccoon roundworm and trichinella). Deer is the mandatory full-flow
species. Sources: USDA + state DNR (T1).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/` (five rows, five entry files; checked 2026-10-21).
- [x] Every entry file has a row (no orphans).
- [x] Required columns filled.
- [x] CWD-prion (deer) / raccoon roundworm, rabies and trichinella (raccoon) / tularemia (rabbit; squirrel handling) / bird flu (turkey) blocks present where applicable.
- [x] Deer entry has the full field-dress → skin → butcher → preserve flow; internal cook temps
      match USDA (checked 2026-10-21).
- [x] `legal_status` is `regulated`; entries distinguish normal season from emergency in prose and say no
      opened source gives a survival exemption; framed as "know your regs," not legal advice.
