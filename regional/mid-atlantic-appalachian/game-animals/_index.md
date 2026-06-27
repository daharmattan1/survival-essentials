# Mid-Atlantic / Appalachian — Game Animals (GAME-ANIMAL)

> Wild game of this biome. Two non-negotiables lead every entry: a **legal/ethical note** (normal
> regulated season vs. genuine emergency — *know your local regs, this is not legal advice*) and a
> **`## ⚠ DISEASE & PARASITE`** block (prions, trichinella, tularemia). White-tailed **deer** is the
> mandatory full-flow species (field-dress → skin → butcher → preserve) and carries the **CWD/prion**
> warning.
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Schema:
> [`../../../SCHEMAS.md`](../../../SCHEMAS.md) §4. Processing technique: [`../../../substrate/05_food/_index.md`](../../../substrate/05_food/_index.md).

---

## ⚠ Disease & legal surface (read BEFORE pursuing game)

| Animal | ☠ Disease / parasite watch | Never eat / handling rule | Legal frame |
|--------|----------------------------|---------------------------|-------------|
| **White-tailed deer** | **CWD (chronic wasting disease — prion)**; cannot be cooked out | **Never eat brain, spinal cord, lymph nodes, spleen.** Bone out; avoid cutting through spine. Don't take animals that look sick/emaciated. | Regulated season; emergency-exception framing only — know your state DNR regs. |
| **Eastern cottontail (rabbit)** | **Tularemia** (esp. warm months) | **Wear gloves** dressing; cook thoroughly; avoid sluggish/sick rabbits. | Regulated season; small game. |
| **Gray squirrel** | General parasites/bacteria | Cook thoroughly; inspect for lesions. | Regulated season; small game. |
| **Wild turkey** | General poultry-type bacteria | Cook to USDA poultry temp; standard handling. | Regulated season (spring/fall where applicable). |
| **Raccoon / opossum** | **Trichinella** (raccoon); roundworm/parasite load | **Cook to a high internal temp to kill trichinella**; thorough handling; least-preferred. | Often regulated as furbearer; check locally. |

> **CWD prion is the master warning.** It is **not destroyed by cooking, freezing, or normal field
> sanitation.** The control is anatomical avoidance (no brain/spinal/lymph tissue) plus not taking
> visibly sick animals. **Cook ALL wild meat thoroughly** regardless. Internal cook temps and the
> full processing chain live in each entry's `## ⚠ MANDATORY PREPARATION`.
>
> **Legal/ethical:** seasons, methods, and licensing are jurisdictional. Entries describe normal
> regulated seasons informationally and frame survival use as `legal_status: emergency-exception` —
> **this is not legal advice; know your local regulations** (`../../../CONVENTIONS.md` §9 rule 6).

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

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| white-tailed-deer | entries/white-tailed-deer.md | GAME-ANIMAL | mid-atlantic-appalachian | fall (regulated) | edible-when-prepared | high | low | false | T1 | 4 | present |
| eastern-cottontail-rabbit | entries/eastern-cottontail-rabbit.md | GAME-ANIMAL | mid-atlantic-appalachian | fall–winter (regulated) | edible-when-prepared | high | low | false | T1 | 4 | present |
| gray-squirrel | entries/gray-squirrel.md | GAME-ANIMAL | mid-atlantic-appalachian | fall–winter (regulated) | edible-when-prepared | moderate | low | false | T1 | 3 | present |
| wild-turkey | entries/wild-turkey.md | GAME-ANIMAL | mid-atlantic-appalachian | spring/fall (regulated) | edible-when-prepared | moderate | low | false | T1 | 3 | present |
| raccoon-or-opossum | entries/raccoon-or-opossum.md | GAME-ANIMAL | mid-atlantic-appalachian | varies (furbearer) | edible-when-prepared | high | low | false | T1 | 4 | present |

`legal_status: emergency-exception` is set in-entry for all. Deer + rabbit + raccoon are
`hazard_severity: high` (CWD prion / tularemia / trichinella). Deer is the mandatory full-flow
species. Sources: USDA + state DNR (T1).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] CWD-prion (deer) / trichinella (raccoon) / tularemia (rabbit) blocks present where applicable.
- [ ] Deer entry has the full field-dress → skin → butcher → preserve flow; internal cook temps
      match USDA.
- [ ] `legal_status` distinguishes normal season vs. emergency-exception; framed as "know your regs,"
      not legal advice.
