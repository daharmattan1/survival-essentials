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
These three govern how every downstream domain is prioritized.

## Load order (this domain)

```
1. rule-of-threes               — a teaching heuristic for priority order (injury first; not exact times)
2. survival-priorities-stop     — the pause before you act; for a lost person, stay put and be found
3. psychology-and-will-to-live  — managing fear and stress; the will to survive; 988 pointer
Apply BEFORE diving into any technique domain — it tells you which domain to use first.
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| rule-of-threes | entries/rule-of-threes.md | PRINCIPLE | universal | n/a | n/a | n/a | n/a | n/a | T2 | 9 | reviewed |
| survival-priorities-stop | entries/survival-priorities-stop.md | PRINCIPLE | universal | n/a | n/a | n/a | n/a | n/a | T2 | 5 | reviewed |
| psychology-and-will-to-live | entries/psychology-and-will-to-live.md | PRINCIPLE | universal | n/a | n/a | n/a | n/a | n/a | T2 | 6 | reviewed |

Biology danger facets are `n/a` (PRINCIPLE entries are doctrine, not consumables). Sources optional
but FAA CAMI, NPS, USFS, FM 21-76 and the other pages listed in each entry's `sources:` are cited.

## `check_manifests`

- [x] Every row maps to an existing file in `entries/` (rule-of-threes, survival-priorities-stop, psychology-and-will-to-live).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each entry follows the PRINCIPLE skeleton (The Principle → Why It Holds → How To Apply →
      Common Failure).
