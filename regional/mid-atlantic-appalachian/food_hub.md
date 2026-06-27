# Mid-Atlantic / Appalachian — Food Decision Hub

> **"What can I eat here, and what could kill me?"** This is the single retrieval surface that
> composes plants + mushrooms + game + crops + seasonality + hazards into one season-indexed decision
> flow. Every food/consumption query for this biome resolves **through here** (retrieval recipe A in
> [`../../AGENTS.md`](../../AGENTS.md)) — and **always** routes through the deadly-look-alike matrix
> and `hazards/` **before** any edible exemplar.
>
> Biome profile: [`_index.md`](_index.md). Registry: [`../_index.md`](../_index.md). Calendar:
> [`seasonality.md`](seasonality.md).

---

> ## ⚠ Read this before any "can I eat it" answer (answer policy)
>
> - **Positive ID or do not consume.** Nothing here is edible on one trait, one photo, or the absence
>   of a warning. Every consumable entry carries a positive-ID checklist of *multiple concurrent*
>   traits + disqualifying "do-NOT-use-if" traits.
> - **Uncertainty-first.** Lead with the safety gate and the positive-ID checklist, **not** a verdict.
> - **Mushrooms and toxic-plant look-alikes can kill even careful people.** For any species flagged
>   `expert_id_required` / `field_id_not_appropriate`, **refuse** to confirm "yes, eat it" on a
>   description or photo alone — direct to expert confirmation, spore print, multi-source ID.
> - **Reproduce `## ⚠ MANDATORY PREPARATION` verbatim** for anything that needs leaching/cooking.
> - The absence of a warning is **missing data, not a green light.**

---

## The decision flow

```
"Can I eat X / what can I eat here right now?"
│
├─ 1. ORIENT to season  → seasonality.md  (what category is even available now?)
│
├─ 2. Pick the category and OPEN ITS INDEX — read the danger surface FIRST:
│      ├─ Wild plant?     → edible-plants/_index.md   → READ THE DEADLY-TWIN MATRIX, then the entry
│      ├─ Mushroom?       → mushrooms/_index.md        → READ THE DOCTRINE + DEADLY-LOOK-ALIKE MATRIX, then the entry
│      ├─ Game/meat?      → game-animals/_index.md      → legal/season note + ⚠ DISEASE block (CWD/trichinella/tularemia)
│      └─ Grown food?     → crops/_index.md             → zone-7a planting/harvest windows
│
├─ 3. CROSS-CHECK hazards → hazards/_index.md  (does a deadly look-alike or toxic plant share this habitat/season?)
│
├─ 4. APPLY the entry's positive-ID gate + ⚠ MANDATORY PREPARATION (verbatim)
│
└─ 5. CITE the specific entries + their T1/T2 sources.  When in doubt → do NOT eat.
```

---

## Routing table — category → index → what leads it

| You're looking at… | Open | The danger surface it leads with | Cross-check |
|--------------------|------|----------------------------------|-------------|
| A **wild plant** (greens, roots, nuts) | [`edible-plants/_index.md`](edible-plants/_index.md) | **Deadly-twin matrix** (edible → deadly look-alike → discriminators → toxin) | [`hazards/_index.md`](hazards/_index.md) |
| A **mushroom** | [`mushrooms/_index.md`](mushrooms/_index.md) | **Mushroom doctrine (8 points) + deadly-look-alike matrix** | [`hazards/_index.md`](hazards/_index.md) |
| **Game / meat** | [`game-animals/_index.md`](game-animals/_index.md) | Legal/season note + **⚠ DISEASE & PARASITE** (CWD prion, trichinella, tularemia) | [`hazards/_index.md`](hazards/_index.md) |
| **Grown food** | [`crops/_index.md`](crops/_index.md) | Zone-7a planting/harvest windows + seed-saving | — |
| **Processing technique** (gut/skin/cook/preserve) | [`../../substrate/05_food/_index.md`](../../substrate/05_food/_index.md) | Cook-thoroughly / never-eat rules (universal technique) | game `⚠ DISEASE` blocks |

---

## Season → what's worth pursuing here (orienting only — confirm in the indexes)

This mirrors [`seasonality.md`](seasonality.md). It tells you *what category to look at*, never *what
is safe to eat* — that decision always runs through the category index's positive-ID gate.

| Season (7a lowland) | Highest-return categories | Notes |
|---------------------|---------------------------|-------|
| **Spring** (Mar–May) | Early greens; morels (⚠ false-morel pair); passive fishing | Morels are the classic spring mushroom **and** carry a deadly-look-alike — doctrine first. |
| **Summer** (Jun–Aug) | Berries; oyster/chicken-of-the-woods; trapping; garden | Watch heat/dehydration ([`../../substrate/06_first_aid/_index.md`](../../substrate/06_first_aid/_index.md)) + ticks ([`hazards/_index.md`](hazards/_index.md)). |
| **Fall** (Sep–Nov) | **Acorns & hickory nuts** (calorie king — leach tannins); fall mushrooms; deer season | Mast season is the single biggest wild-calorie window; acorns need mandatory tannin leaching. |
| **Winter** (Dec–Feb) | Stored/preserved food; cattail roots; limited game | Lean season — lean on stockpile + crops harvested earlier; conserve energy. |

---

## Reminders pulled from the priority order

- Calories per unit effort decide survival: **stored food → passive fishing → trapping → foraging →
  gardening** (`../../substrate/05_food/_index.md`). Don't burn more calories foraging than you gain.
- All surface water here needs treatment before drinking — pair any foraging plan with
  [`../../substrate/02_water/_index.md`](../../substrate/02_water/_index.md).
- Cook **all** wild meat thoroughly; never eat brain/spinal tissue or sick-looking animals (see the
  game `⚠ DISEASE & PARASITE` blocks).

> **The hub never overrides an entry's gate.** It routes you *to* the gate. If the entry says
> `field_id_not_appropriate`, this hub does not authorize eating — it tells you to get expert
> confirmation. When in doubt, go without.
