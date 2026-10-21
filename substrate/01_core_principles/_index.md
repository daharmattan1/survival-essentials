# 01_core_principles — Survival Doctrine (PRINCIPLE)

> The decision layer everything else hangs from. Before water, fire, food, or first-aid technique
> matters, the **priority order** and the **will to act** decide outcomes. These are PRINCIPLE
> entries (`../../SCHEMAS.md` §9): the rule, why it holds physiologically, how to apply it, and how
> people get it wrong under stress.
>
> Survey doorway: [`../../01_core_principles.md`](../../01_core_principles.md).

---

## Synthesis

Survival is triage under stress. The **Rule of Threes** (about 3 minutes without air, 3 hours without
shelter in harsh conditions, 3 days without water, 3 weeks without food) is a teaching heuristic,
not physiology; the FAA's version uses different numbers and the Army manual has none. Use it for
the order it implies, with injury and severe bleeding first and being found added. **STOP** (Stop,
Think, Observe, Plan; the FAA says Sit) is a pause before you act, and for a lost person it usually
ends in staying put and being found. **Psychology and the will to survive** (the Army calls it "the
refusal to give up") is about managing fear and stress and not letting despair make your decisions.
Two newer entries apply the doctrine: **stay or go** (lost outdoors, the default is to stay put and be
found; at home, an official evacuation order overrides everything, and without one you stay while the
building is intact and you can keep warm or cool) and **group survival and roles** (one person makes the
final call, buddy pairs, scheduled headcounts, jobs matched to ability, and the slowest member sets the
pace). These govern how every downstream domain is prioritized.

## Load order (this domain)

```
1. rule-of-threes               — a teaching heuristic for priority order (injury first; not exact times)
2. survival-priorities-stop     — the pause before you act; for a lost person, stay put and be found
3. psychology-and-will-to-live  — managing fear and stress; the will to survive; 988 pointer
4. stay-or-go-decision          — lost: stay put and be found; at home: follow officials, stay while the building is intact and you can keep warm or cool
5. group-survival-and-roles     — one leader, buddy pairs, headcounts, jobs, slowest pace; what to do if someone is lost
Apply BEFORE diving into any technique domain — it tells you which domain to use first.
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| rule-of-threes | entries/rule-of-threes.md | PRINCIPLE | universal | n/a | n/a | n/a | n/a | n/a | T2 | 9 | reviewed |
| survival-priorities-stop | entries/survival-priorities-stop.md | PRINCIPLE | universal | n/a | n/a | n/a | n/a | n/a | T2 | 5 | reviewed |
| psychology-and-will-to-live | entries/psychology-and-will-to-live.md | PRINCIPLE | universal | n/a | n/a | n/a | n/a | n/a | T2 | 6 | reviewed |
| stay-or-go-decision | entries/stay-or-go-decision.md | PRINCIPLE | universal | n/a | n/a | high | n/a | false | T1 | 13 | draft |
| group-survival-and-roles | entries/group-survival-and-roles.md | PRINCIPLE | universal | n/a | n/a | low | n/a | false | T2 | 9 | draft |

Biology danger facets are `n/a` (PRINCIPLE entries are doctrine, not consumables). Each entry cites its
sources: FAA CAMI, NPS, USFS, Army FM 21-76 (superseded; unofficial reprint), NIMH, CDC, MedlinePlus and
Ready.gov pages (T2), and the stay-or-go entry adds NOAA SARSAT and National Weather Service pages (T1).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each entry follows the PRINCIPLE skeleton (The Principle → Why It Holds → How To Apply →
      Common Failure).
