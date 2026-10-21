# 11_gear — Kit Tiers (KIT-GEAR)

> Universal: what to carry and stock, organized as tiers (EDC, bug-out, home stockpile, plus a vehicle
> kit and an individual first-aid kit); the survey guide groups them as carry daily, grab-and-go, car
> and home supply. KIT-GEAR entries (`../../SCHEMAS.md` §5): what & why, selection criteria, multi-use,
> failure modes. Gear is lower-stakes than the technique domains, but fuel-burning heaters, stoves,
> grills and generators cause carbon monoxide deaths; any item that touches fire, water or game
> inherits the warning blocks from those domains.
>
> Survey doorway: [`../../11_essential_gear.md`](../../11_essential_gear.md). Retrieval recipe D in
> [`../../AGENTS.md`](../../AGENTS.md).

---

## Synthesis

Gear is tiered by scenario radius. **Tier 1 (EDC)** is what is on you or in your everyday bag: phone
and power bank, whistle, light, ID and contacts card, a day's medicine, plus (per the entry) a cutting
tool, two fire methods, water treatment and small first-aid items. **Tier 2 (bug-out)** is the
grab-and-go kit for about 72 hours: carry what water you can plus a way to treat it, warmth or shelter,
fire, no-cook food, a radio. **Tier 3 (home stockpile)** is the bug-in larder — water and food
reserves, power (batteries, power bank or battery power station; any generator runs outdoors only, 20
ft from windows, doors and vents), warmth from blankets, sleeping bags and layers (no fuel-burning
heater indoors), and flashlights. The **vehicle kit** covers the car (stuck in snow, breakdown, with a
carbon monoxide rule: clear the tailpipe and burn nothing inside), and the **individual first-aid kit**
lists contents by purpose, the tourniquet, and personal medicines. Two disciplines run across all
tiers: **multi-use** (the backpacker's rule — favor items that do 2+ jobs, because weight and space
are finite) and **skills over gear** (a tool you cannot use is dead weight; practice beats
accumulation). Buy in order (plan, water, light and radio, first aid, food and warmth), then practice
with each item.

## Load order (this domain)

```
What's on me right now?     → edc-tier1-kit (carry daily: phone/power bank, whistle, light, ID, medicine; per the entry also cutting/fire/water/first-aid)
What do I grab to leave?    → bug-out-tier2-kit (~72h: water you can carry + a way to treat it, warmth/shelter, fire, no-cook food, radio)
What do I keep at home?     → home-stockpile-tier3 (water and food reserve, power, warmth without fuel burning indoors, light)
What goes in the car?       → vehicle-kit (⚠ CO: clear the tailpipe, burn nothing inside)
What goes in a first-aid kit? → individual-first-aid-kit (contents by purpose; tourniquet; personal medicines)
Cross-cutting: favor multi-use items; skills > gear; buy in order (plan, water, light and radio, first aid, food and warmth), then practice with each item.
Any fire/water/game item → inherit that domain's warning blocks (CO, CONTAMINATION, cook temps).
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| edc-tier1-kit | entries/edc-tier1-kit.md | KIT-GEAR | universal | n/a | n/a | low | n/a | n/a | T1 | 8 | reviewed |
| bug-out-tier2-kit | entries/bug-out-tier2-kit.md | KIT-GEAR | universal | n/a | n/a | low | n/a | n/a | T1 | 16 | reviewed |
| home-stockpile-tier3 | entries/home-stockpile-tier3.md | KIT-GEAR | universal | n/a | n/a | moderate | n/a | n/a | T1 | 16 | reviewed |
| vehicle-kit | entries/vehicle-kit.md | KIT-GEAR | universal | n/a | n/a | moderate | n/a | false | T1 | 18 | draft |
| individual-first-aid-kit | entries/individual-first-aid-kit.md | KIT-GEAR | universal | n/a | n/a | moderate | n/a | false | T1 | 14 | draft |

Gear rows carry `hazard_severity` low or moderate (moderate where generators, fuel or bleach are
involved); biology facets are `n/a`. T3 (practitioner consensus) is acceptable for gear opinion per
`../../CONVENTIONS.md` §7. Items that treat water / make fire link to those domains' safety blocks.

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each KIT-GEAR entry follows the skeleton (What & Why → Selection Criteria → Multi-Use →
      Maintenance/Failure Modes); fire/water items cross-link the relevant warning blocks.
