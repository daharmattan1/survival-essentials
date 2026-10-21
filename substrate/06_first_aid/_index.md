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

Survival first-aid takes the fastest dangers first: heavy **bleeding** and **shock**, no breathing,
and **severe allergic reaction (anaphylaxis)**. The rest follow: **carbon monoxide poisoning** (get
outside first), **head injury**, **burns**, **fractures and sprains**, the slower cold and heat injury (hypo/hyperthermia), fluid
lost faster than replaced (**dehydration/diarrhea**), a wound that **infects**, and an interrupted
**chronic medication** (insulin, anticoagulants, seizure meds). All ten have written entries. For
CPR and choking, which have no entry of their own, use `06_first_aid.md`. For each, the
high-value move is knowing the **RED FLAG** that means "this now exceeds field care — evacuate," and
the **DO NOT** that quietly kills (rewarming frostbite that may refreeze, giving water to an
unconscious person, removing an impaled object). The protocols escalate with severity; they are a
field bridge to real care, not a replacement for it.

## Load order (this domain)

```
For any first-aid query:
  0. If you can reach 911, call first (or have someone call). Check for danger to you.
     Danger from carbon monoxide (alarm, fuel burning indoors)? Get everyone outside first → carbon-monoxide-poisoning
     Severe allergic reaction (trouble breathing, swelling after a sting, food or medicine)? Call 911 → anaphylaxis-and-allergic-reaction
  1. Recognize        — is this the condition, and what stage?
  2. ⚠ RED FLAGS/EVAC — does it already exceed field care? (surface FIRST)
  3. Respond          — numbered steps, escalating with severity
  4. ⚠ DO NOT         — the common dangerous mistakes
  5. Med Continuity   — if a chronic med is interrupted
Route by injury: bleeding-control-and-shock · burns · fractures-sprains-and-splinting ·
head-injury-and-concussion · thermal-injury-hypo-hyperthermia · dehydration-and-diarrhea ·
wound-infection-management · chronic-med-continuity
Always state: this is field response, not medical advice; get professional care when available.
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| wound-infection-management | entries/wound-infection-management.md | PROTOCOL | universal | n/a | n/a | high | n/a | n/a | T1 | 3 | agent-verified |
| thermal-injury-hypo-hyperthermia | entries/thermal-injury-hypo-hyperthermia.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | n/a | T1 | 12 | agent-verified |
| dehydration-and-diarrhea | entries/dehydration-and-diarrhea.md | PROTOCOL | universal | n/a | n/a | high | n/a | n/a | T1 | 5 | agent-verified |
| chronic-med-continuity | entries/chronic-med-continuity.md | PROTOCOL | universal | n/a | n/a | high | n/a | n/a | T1 | 14 | agent-verified |
| bleeding-control-and-shock | entries/bleeding-control-and-shock.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | n/a | T1 | 8 | agent-verified |
| burns | entries/burns.md | PROTOCOL | universal | n/a | n/a | high | n/a | false | T1 | 10 | agent-verified |
| fractures-sprains-and-splinting | entries/fractures-sprains-and-splinting.md | PROTOCOL | universal | n/a | n/a | high | n/a | false | T1 | 7 | agent-verified |
| anaphylaxis-and-allergic-reaction | entries/anaphylaxis-and-allergic-reaction.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | false | T1 | 9 | agent-verified |
| carbon-monoxide-poisoning | entries/carbon-monoxide-poisoning.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | false | T1 | 9 | agent-verified |
| head-injury-and-concussion | entries/head-injury-and-concussion.md | PROTOCOL | universal | n/a | n/a | lethal | n/a | false | T1 | 7 | agent-verified |

`region`, `edibility_status`, `confusability_level`, `expert_id_required` are `n/a` for protocols
(non-biology). All ten rows carry `hazard_severity: high|lethal`; the entries cite T1 sources (CDC,
MedlinePlus, Red Cross, FDA, WHO, Ready.gov).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Coverage check (`CONVENTIONS.md` §10): wound infection, hypo/hyperthermia, dehydration/diarrhea,
      med-continuity all present; each has `## ⚠ RED FLAGS / EVACUATE` + `## ⚠ DO NOT`.
- [ ] Every entry states it is field response, **not** medical advice, and cites a T1 source.
