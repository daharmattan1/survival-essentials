# 05_food — Food Acquisition **Technique** (METHOD)

> Universal technique only: the parts of getting and handling food that do **not** change with
> geography — **calorie planning and rationing**, **cooking without power**, **passive fishing**,
> **small-game trapping**, **fish/game processing** and **tested home drying**. The biology of *what*
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

A healthy adult can live several weeks without food, so water and shelter come first. Spend effort on
food only after they are handled. The order is: eat the food you have (count people, count calories,
divide, and ration only if the count says you must, never for children or pregnant women; water is never rationed), then (only if you must,
where the law allows) hook and line, with trapping last. Do not forage; wild plants and mushrooms go to
the region pack. Passive methods (trotlines, snares) work while you do other things, but most are
regulated or unlawful (Virginia bans deadfalls) and trapping is the last resort. Check your state's
rules first. When the power is out, **cooking without power** is outdoors only (camp stoves, grills and
generators at least 20 ft from windows, doors and vents), to temperature, and the easiest answer is food
that needs no cooking. Processing (gut, scale or skin, cool, cook to temperature) is universal craft
and applies to any wild fish or game you have already identified and taken lawfully (see the region
pack). **Home drying** is limited to tested extension methods for jerky, fruit and vegetables: jerky only
from strips heated to 160 F first (165 F for poultry, game birds, rabbit, hare, squirrel and wild meat-eaters), and no home
formula is given for cold smoking or salt curing. **This index carries that technique; it never carries
an identification or safety-to-consume verdict** — that always comes from the region pack with its
positive-ID gate.

## Load order (this domain)

```
Technique query (HOW to fish/trap/process)?     → stay here; open the METHOD entry.
  How long will the food I have last?           → calorie-planning-and-rationing
  Power out, how do I cook?                     → cooking-without-power (outdoors only; to temperature)
  Keep meat or produce without a freezer?       → preservation-drying-smoking-salting (tested drying only)
  Fish or trap?                                 → passive-fishing-trotline-and-traps, small-game-trapping-snares (check the law first)
  Already have wild fish or game to process?    → fish-and-game-processing-basics
Consumption query (CAN I eat / what is this)?   → leave here:
    ../../regional/_index.md  →  active biome food_hub.md  →  bio index (matrix/doctrine FIRST)  →  entry
Always: "Positive ID or do not consume." Cook wild fish and game to temperature with a thermometer:
fish 145 F; venison 160 F; poultry, game birds and rabbit or hare 165 F; bear, wild pig and other wild
meat-eaters or omnivores 165 F. Color is not a test.
```

## Manifest (technique only)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| passive-fishing-trotline-and-traps | entries/passive-fishing-trotline-and-traps.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T1 | 6 | agent-verified |
| small-game-trapping-snares | entries/small-game-trapping-snares.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T1 | 5 | agent-verified |
| fish-and-game-processing-basics | entries/fish-and-game-processing-basics.md | METHOD | universal | n/a | n/a | moderate | n/a | n/a | T1 | 20 | agent-verified |
| calorie-planning-and-rationing | entries/calorie-planning-and-rationing.md | METHOD | universal | n/a | n/a | low | n/a | false | T1 | 10 | agent-verified |
| preservation-drying-smoking-salting | entries/preservation-drying-smoking-salting.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 16 | agent-verified |
| cooking-without-power | entries/cooking-without-power.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 23 | agent-verified |

`region: universal` for all — technique is biome-independent. `fish-and-game-processing-basics`
carries `hazard_severity: moderate` because the cook-to-temperature and never-eat rules (deer and elk
brain, spinal cord, eyes, spleen, tonsils and lymph nodes; any animal that looks sick or was found
dead) are non-omissible; it cross-links the game-animal disease blocks in the region pack.
`preservation-drying-smoking-salting` and `cooking-without-power` are `high` (botulism, Trichinella
and carbon monoxide). Sources are T1: CDC, USDA/FoodSafety.gov, university extension and state wildlife
agency pages, with FM 21-76 as a secondary source.

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] No entry here asserts an edibility verdict for a *specific organism* — those belong to the
      region pack. This index links `../../regional/_index.md` (registry), **not** a biome.
- [ ] `processing` entry reproduces the cook-temp / never-eat rules; cross-links region game entries.
