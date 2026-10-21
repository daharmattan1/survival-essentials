# 03_fire — Fire-Making (METHOD)

> Universal technique: getting and keeping fire. Fire is a tool for warmth, drying clothes, signaling
> and treating water. It comes after injury, shelter and dry clothes, and it carries burn, carbon
> monoxide and wildfire risk. METHOD entries (`../../SCHEMAS.md` §6): goal, steps, failure modes.
> Fire carries a safety boundary (burns, CO, wildfire), so danger facets appear where relevant.
>
> Survey doorway: [`../../03_fire.md`](../../03_fire.md). Retrieval recipe D in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Fire fails for three reasons: bad **structure** (no airflow, fuel piled wrong), weak **ignition** (a
spark with nothing to catch it), and a broken **fuel progression** (a flame that never bridges from
tinder to kindling to fuel). Beginners obsess over the spark and neglect the other two, then wonder
why a lit match dies. The reliable approach is to build the lay and stage a full tinder→kindling→fuel
progression *before* striking anything, so the moment of ignition has somewhere to go. Treat fire as
a system with a safety boundary: burns, carbon-monoxide indoors, and wildfire spread are the failure
modes that turn a survival asset into a second emergency. Three further entries cover the situations
that go wrong: **fire in wet weather** (find standing dead wood, split it to the dry core, build on a
platform), **keeping a fire through the night** (the default is to put it out before you sleep; a night
fire is only for freezing-or-fire choices, with someone awake at all times), and **extinguishing and
fire safety** (burn bans, site clearing, drown-stir-feel until cold).

## Load order (this domain)

```
Build before you light:
  0. Is fire allowed here (burn bans) and do you need one?     → extinguishing-and-fire-safety
  1. fire-lays-and-structure        — pick the site and the lay (teepee, log cabin, lean-to, star)
  2. tinder-and-fuel-progression    — stage tinder → kindling → fuel BEFORE ignition
  3. ignition-methods               — only now strike (lighter, ferro rod, matches, lens; friction last); light from the upwind side
Everything damp?        → wet-weather-fire (dry wood, platform, feather sticks)
Need it through the night? → overnight-fire-maintenance (default: put it out; never asleep in an enclosed space with a fire)
Leaving or sleeping?    → extinguishing-and-fire-safety (drown, stir, feel; never leave it unattended)
Safety boundary: fire goes outside; nothing burns in a tent, vehicle, garage, snow shelter or home
except a vented fireplace or stove in working order, and opening a flap or window does not fix it.
Clear the area (wildfire). Never leave a fire unattended.
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| fire-lays-and-structure | entries/fire-lays-and-structure.md | METHOD | universal | n/a | n/a | moderate | n/a | n/a | T2 | 9 | agent-verified |
| ignition-methods | entries/ignition-methods.md | METHOD | universal | n/a | n/a | moderate | n/a | n/a | T2 | 3 | agent-verified |
| tinder-and-fuel-progression | entries/tinder-and-fuel-progression.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 2 | agent-verified |
| wet-weather-fire | entries/wet-weather-fire.md | METHOD | universal | n/a | n/a | moderate | n/a | false | T1 | 11 | agent-verified |
| extinguishing-and-fire-safety | entries/extinguishing-and-fire-safety.md | METHOD | universal | n/a | n/a | high | n/a | false | T1 | 21 | agent-verified |
| overnight-fire-maintenance | entries/overnight-fire-maintenance.md | METHOD | universal | n/a | n/a | moderate | n/a | false | T1 | 13 | agent-verified |

`hazard_severity: moderate` on the lay + ignition entries (burns / CO / wildfire boundary). Sources:
ATP 3-50.21 (primary) with FM 21-76, Forest Service, NPS, CDC and CPSC pages (T2).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each METHOD entry follows the skeleton (Goal & When → Steps → Failure Modes & Fixes); fire
      safety boundary (CO/wildfire/burns) stated where applicable.
