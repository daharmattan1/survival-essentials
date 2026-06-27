# 05_food — Food Acquisition **Technique** (METHOD)

> Universal technique only: the parts of getting calories that do **not** change with geography —
> **passive fishing**, **small-game trapping**, and **fish/game processing**. The biology of *what*
> you can eat (which plants, mushrooms, game, crops grow here, what could kill you by mistake, what
> is legal to hunt) is **region-bound** and lives elsewhere.
>
> Survey doorway: [`../../05_food.md`](../../05_food.md). Retrieval recipe A in
> [`../../AGENTS.md`](../../AGENTS.md).

---

> **⚠ Food/consumption queries do NOT resolve here.** This universal index holds **technique** only.
> Anything about *identifying or eating* a plant, mushroom, or animal resolves through the **region
> registry** → the active region's food decision hub:
>
> **[`../../regional/_index.md`](../../regional/_index.md)** (registry) →
> the active biome's **`food_hub.md`** → the relevant biology index (edible-plants / mushrooms /
> game-animals / crops) → **READ THE DEADLY-LOOK-ALIKE MATRIX + MUSHROOM DOCTRINE FIRST** → entries →
> cross-check `hazards/`.
>
> This index deliberately links the **registry, not a specific biome** (`../../CONVENTIONS.md` §11):
> season, habitat, look-alikes, and legality are biome variables, so consumption pivots through the
> active region every time.

---

## Synthesis

Calories per unit of effort decide who survives — energy spent foraging that exceeds calories gained
is a death spiral. The universal lesson order is **stored food → passive fishing → trapping →
foraging → gardening**, because that is the descending return-on-effort curve. Passive methods
(trotlines, weirs, snares, deadfalls) work *while you do other things*, which is why they beat
active hunting in a real emergency. Processing (gut, scale/skin, cook thoroughly, preserve) is
universal craft and applies to whatever the region's biology layer says is edible. **This index
carries that technique; it never carries an edibility verdict** — that always comes from the region
pack with its positive-ID gate.

## Load order (this domain)

```
Technique query (HOW to fish/trap/process)?     → stay here; open the METHOD entry.
Consumption query (CAN I eat / what is this)?   → leave here:
    ../../regional/_index.md  →  active biome food_hub.md  →  bio index (matrix/doctrine FIRST)  →  entry
Always: "Positive ID or do not consume." Cook all wild meat thoroughly (parasites).
```

## Manifest (planned entries — technique only)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| passive-fishing-trotline-and-traps | entries/passive-fishing-trotline-and-traps.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 3 | reviewed |
| small-game-trapping-snares | entries/small-game-trapping-snares.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 3 | reviewed |
| fish-and-game-processing-basics | entries/fish-and-game-processing-basics.md | METHOD | universal | n/a | conditionally-edible | moderate | n/a | n/a | T2 | 3 | reviewed |

`region: universal` for all — technique is biome-independent. `fish-and-game-processing-basics`
carries `edibility_status: conditionally-edible` and `hazard_severity: moderate` because the
cook-thoroughly / never-eat (brain, spinal, sick animals) rules are non-omissible; it cross-links
the game-animal disease blocks in the region pack. Sources are FM 21-76 / FAO (T2).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] No entry here asserts an edibility verdict for a *specific organism* — those belong to the
      region pack. This index links `../../regional/_index.md` (registry), **not** a biome.
- [ ] `processing` entry reproduces the cook-temp / never-eat rules; cross-links region game entries.
