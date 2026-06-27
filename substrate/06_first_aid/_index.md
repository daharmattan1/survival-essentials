# 06_first_aid — Field Response Protocols (PROTOCOL)

> Universal technique: commonly-taught field response for when professional care is unavailable.
> **First-aid here is NOT medical advice** and every entry says so (`../../CONVENTIONS.md` §9 rule 7).
> Each protocol leads with `## Recognize` → `## ⚠ RED FLAGS / EVACUATE` → `## Respond` → `## ⚠ DO NOT`
> so the escalation threshold and the dangerous mistakes surface before the steps.
>
> Survey doorway: [`../../06_first_aid.md`](../../06_first_aid.md). Retrieval recipe C in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Survival first-aid is about the conditions that turn slow and killable without EMS: a wound that
**infects**, a body that loses or gains too much **core heat** (hypo/hyperthermia), fluid lost
faster than replaced (**dehydration/diarrhea**), an interrupted **chronic medication** (insulin,
anticoagulants, seizure meds), and **bleeding/shock** that outruns the clock. For each, the
high-value move is knowing the **RED FLAG** that means "this now exceeds field care — evacuate," and
the **DO NOT** that quietly kills (rewarming frostbite that may refreeze, giving water to an
unconscious person, removing an impaled object). The protocols escalate with severity; they are a
field bridge to real care, not a replacement for it.

## Load order (this domain)

```
For any first-aid query:
  1. Recognize        — is this the condition, and what stage?
  2. ⚠ RED FLAGS/EVAC — does it already exceed field care? (surface FIRST)
  3. Respond          — numbered steps, escalating with severity
  4. ⚠ DO NOT         — the common dangerous mistakes
  5. Med Continuity   — if a chronic med is interrupted
Always state: this is field response, not medical advice; get professional care when available.
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| wound-infection-management | entries/wound-infection-management.md | PROTOCOL | universal | n/a | n/a | high | n/a | n/a | T1 | 3 | reviewed |
| thermal-injury-hypo-hyperthermia | entries/thermal-injury-hypo-hyperthermia.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | n/a | T1 | 4 | reviewed |
| dehydration-and-diarrhea | entries/dehydration-and-diarrhea.md | PROTOCOL | universal | n/a | n/a | high | n/a | n/a | T1 | 4 | reviewed |
| chronic-med-continuity | entries/chronic-med-continuity.md | PROTOCOL | universal | n/a | n/a | high | n/a | n/a | T1 | 4 | reviewed |
| bleeding-control-and-shock | entries/bleeding-control-and-shock.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | n/a | T1 | 4 | reviewed |

`region`, `edibility_status`, `confusability_level`, `expert_id_required` are `n/a` for protocols
(non-biology). All five carry `hazard_severity: high|lethal` and cite **T1** (CDC / Red Cross /
extension).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Coverage check (`CONVENTIONS.md` §10): wound infection, hypo/hyperthermia, dehydration/diarrhea,
      med-continuity all present; each has `## ⚠ RED FLAGS / EVACUATE` + `## ⚠ DO NOT`.
- [ ] Every entry states it is field response, **not** medical advice, and cites a T1 source.
