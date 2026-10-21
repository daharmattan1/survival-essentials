# 08_communication — Signaling & Comms (METHOD)

> Universal technique: being found and staying informed when normal networks are down. METHOD
> entries (`../../SCHEMAS.md` §6): goal, steps, failure modes. Rescue often hinges on signaling, so
> this domain's value is disproportionate to its low direct danger.
>
> Survey doorway: [`../../08_communication.md`](../../08_communication.md). Retrieval recipe D in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Communication splits into **being found** and **staying informed**. If you are hurt or in danger,
call 911 first (a text to 911 is a fallback, only where offered). Being found is **signaling** — visual (signal mirror,
fire/smoke by day vs. night, ground marks, high-vis) and audible (whistle) — using specific threes:
whistle three blasts, rest, three again; flashlight SOS; three fires or three smoke columns (an NPS
Yosemite page calls any signal done three times a universal distress call; no wider rule is sourced).
Ground marks: spell SOS or HELP. It works best when prepared *before* you need it. Staying informed has
two halves. **Warnings** come from phone alerts (WEA) plus a NOAA Weather Radio, which keeps working
when the power and the cell network do not (use at least two sources, and know "watch" from "warning").
**Radio** means knowing the services: NOAA Weather Radio and AM/FM news radio (receive only); FRS, MURS
and CB (no license to transmit); GMRS and amateur radio (license required). The **family communication
plan** is the core of emergency comms: a paper card, one out-of-state contact, a meeting place, and
practice, because texts and calls get through when phones are jammed. **Family plan and mesh**: a paper
plan with one out-of-state contact comes first; mesh radios are an optional short-range extra for a
group that tested them together, and they cannot reach 911. The discipline is redundancy and
pre-arrangement: specific signals, a charged radio, and an agreed contact plan beat improvising in the
moment.

## Load order (this domain)

```
Hurt or in danger?     → call 911 first (text to 911 only as a fallback where offered); then signal
Need to be FOUND?      → signaling-visual-and-audible (mirror/fire/smoke + whistle: three blasts, rest, three again)
Need WARNINGS?         → emergency-alerts-and-noaa-weather-radio (phone alerts plus a weather radio; watch vs. warning)
Need to STAY INFORMED? → radio-basics-and-bands (NOAA/AM-FM are receive only; FRS/MURS/CB need no license; GMRS and ham do)
Family apart or phones jammed? → family-communication-plan (card, out-of-state contact, meeting place), then mesh-and-emergency-comms (family plan first; mesh only for a tested group)
Pre-arrange before the emergency: signal kit staged, radio charged, contact plan agreed.
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| signaling-visual-and-audible | entries/signaling-visual-and-audible.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T1 | 5 | draft |
| radio-basics-and-bands | entries/radio-basics-and-bands.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T1 | 23 | draft |
| mesh-and-emergency-comms | entries/mesh-and-emergency-comms.md | METHOD | universal | n/a | n/a | low | n/a | n/a | T1 | 4 | draft |
| family-communication-plan | entries/family-communication-plan.md | METHOD | universal | n/a | n/a | low | n/a | false | T1 | 10 | draft |
| emergency-alerts-and-noaa-weather-radio | entries/emergency-alerts-and-noaa-weather-radio.md | METHOD | universal | n/a | n/a | low | n/a | false | T1 | 24 | draft |

`radio-basics-and-bands` cites FCC/NOAA (T1) for band/licensing facts. `signaling-visual-and-audible`
cites NPS and FAA pages (T1) with FM 21-76 for fire and smoke.

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each METHOD entry follows the skeleton; licensing facts (TX vs. RX) cite a T1 source.
