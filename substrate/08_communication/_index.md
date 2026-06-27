# 08_communication — Signaling & Comms (METHOD)

> Universal technique: being found and staying informed when normal networks are down. METHOD
> entries (`../../SCHEMAS.md` §6): goal, steps, failure modes. Rescue often hinges on signaling, so
> this domain's value is disproportionate to its low direct danger.
>
> Survey doorway: [`../../08_communication.md`](../../08_communication.md). Retrieval recipe D in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Communication splits into **being found** and **staying informed**. Being found is **signaling** —
visual (signal mirror, fire/smoke by day vs. night, ground-to-air symbols, high-vis) and audible
(whistle, three-of-anything as the distress convention) — and it works best when prepared *before*
you need it. Staying informed is **radio**: knowing the bands (NOAA weather, AM/FM broadcast, FRS/GMRS,
ham/2-meter and 70-cm) and that receive-only listening needs no license while transmitting on most
bands does. **Mesh and emergency comms** (off-grid mesh, GMRS repeaters, the role of a designated
out-of-area contact) extend range when infrastructure is gone. The discipline is redundancy and
pre-arrangement: the rule-of-three distress signal, a charged radio, and an agreed contact plan beat
improvising in the moment.

## Load order (this domain)

```
Need to be FOUND?      → signaling-visual-and-audible (mirror/fire/smoke + whistle; "three" = distress)
Need to STAY INFORMED? → radio-basics-and-bands (NOAA/AM-FM receive needs no license; TX usually does)
Infrastructure down?   → mesh-and-emergency-comms (off-grid mesh, GMRS repeaters, out-of-area contact)
Pre-arrange before the emergency: signal kit staged, radio charged, contact plan agreed.
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| signaling-visual-and-audible | entries/signaling-visual-and-audible.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T2 | 3 | reviewed |
| radio-basics-and-bands | entries/radio-basics-and-bands.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T1 | 4 | reviewed |
| mesh-and-emergency-comms | entries/mesh-and-emergency-comms.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T3 | 4 | reviewed |

`radio-basics-and-bands` cites FCC/NOAA (T1) for band/licensing facts. Signaling from FM 21-76 (T2).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each METHOD entry follows the skeleton; licensing facts (TX vs. RX) cite a T1 source.
