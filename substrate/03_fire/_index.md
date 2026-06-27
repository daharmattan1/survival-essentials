# 03_fire — Fire-Making (METHOD)

> Universal technique: getting and keeping fire. Fire is shelter, water treatment (boiling),
> cooking, signaling, and morale in one — which is why it sits high in the priority order. METHOD
> entries (`../../SCHEMAS.md` §6): goal, steps, failure modes. Fire carries a safety boundary (burns,
> CO, wildfire), so danger facets appear where relevant.
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
modes that turn a survival asset into a second emergency.

## Load order (this domain)

```
Build before you light:
  1. fire-lays-and-structure        — pick the lay (teepee/log-cabin/lean-to) + prep the platform
  2. tinder-and-fuel-progression    — stage tinder → kindling → fuel BEFORE ignition
  3. ignition-methods               — only now strike (lighter > ferro > friction); protect from wind/wet
Safety boundary: ventilate (CO), clear the area (wildfire), never leave unattended.
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| fire-lays-and-structure | entries/fire-lays-and-structure.md | METHOD | universal | n/a | n/a | moderate | n/a | n/a | T2 | 0 | planned |
| ignition-methods | entries/ignition-methods.md | METHOD | universal | n/a | n/a | moderate | n/a | n/a | T2 | 0 | planned |
| tinder-and-fuel-progression | entries/tinder-and-fuel-progression.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 0 | planned |

`hazard_severity: moderate` on the lay + ignition entries (burns / CO / wildfire boundary). Sources
FM 21-76 (T2).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each METHOD entry follows the skeleton (Goal & When → Steps → Failure Modes & Fixes); fire
      safety boundary (CO/wildfire/burns) stated where applicable.
