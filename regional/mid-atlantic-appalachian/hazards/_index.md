# Mid-Atlantic / Appalachian — Hazards (HAZARD)

> The biome's environmental and biological threats — what to identify, avoid, and respond to. HAZARD
> entries (`../../../SCHEMAS.md` §8): identify → avoid → if exposed/bitten/stung → `## ⚠ WHEN IT'S AN
> EMERGENCY`. This index is the **cross-check** every food query routes through (does a deadly
> look-alike or toxic plant share the habitat?).
>
> Biome: [`../_index.md`](../_index.md). Food hub: [`../food_hub.md`](../food_hub.md). Toxic-plant
> ID pairs also surface in [`../edible-plants/_index.md`](../edible-plants/_index.md).

---

## Hazard surface (this biome)

| Hazard | Type | Where/when here | Emergency threshold |
|--------|------|-----------------|---------------------|
| **Venomous snakes** — copperhead, timber rattlesnake | animal | Rocky slopes, leaf litter, woodpiles; warm months, dawn/dusk | Any envenomation → urgent care; rattlesnake bite is higher-severity. Keep still, get help. |
| **Ticks & Lyme** (blacklegged/deer tick) + other tick-borne | biological | Tall grass, brush, leaf litter; peak spring–summer | Expanding rash / fever / joint pain after a bite → medical care (Lyme is treatable early). |
| **Toxic plants** — water hemlock, poison hemlock, poison ivy | plant | Hemlocks at wet edges/fields; poison ivy everywhere ("leaves of three") | Hemlock **ingestion** = immediate emergency (seizures/respiratory failure); poison ivy = severe rash, rarely an airway emergency if burned/inhaled. |

> **Hemlock is the overlap between this file and the food layer.** Water hemlock and poison hemlock
> are the deadly twins of edible umbels (`../edible-plants/_index.md` matrix). Any food query
> touching wild carrots/parsnips/umbels **must** cross-check here. "Leaves of three, let it be" for
> poison ivy/oak.

## Synthesis & load order

The realistic threats here are **underfoot and on your skin**, not large predators: a venomous snake
you stepped near, a tick you didn't find for a day, and toxic plants you might mistake for food. The
control for all three is **avoidance first** (watch hands/feet around rock and litter; tick checks +
covered skin; never eat an unconfirmed umbel), then a known response and a clear emergency threshold.

```
1. This hazard surface (above)  — identify what shares your habitat/season
2. The hazard entry             — Identify → Avoid → If Exposed/Bitten/Stung → ⚠ WHEN IT'S AN EMERGENCY
3. For toxic plants             — cross-link ../edible-plants/ deadly-twin matrix
4. First-aid response           → ../../../substrate/06_first_aid/ (bites/stings/exposure protocols)
5. CITE (CDC / state health / herpetological / extension — T1/T2)
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| venomous-snakes-copperhead-rattlesnake | entries/venomous-snakes-copperhead-rattlesnake.md | HAZARD | mid-atlantic-appalachian | warm months | n/a | high | moderate | false | T1 | 0 | planned |
| ticks-and-lyme | entries/ticks-and-lyme.md | HAZARD | mid-atlantic-appalachian | spring–summer peak | n/a | moderate | low | false | T1 | 0 | planned |
| toxic-plants-hemlock-poison-ivy | entries/toxic-plants-hemlock-poison-ivy.md | HAZARD | mid-atlantic-appalachian | growing season | deadly-toxic | lethal | deadly-lookalike-exists | false | T1 | 0 | planned |

`toxic-plants-hemlock-poison-ivy` carries `edibility_status: deadly-toxic` / `hazard_severity:
lethal` / `confusability_level: deadly-lookalike-exists` (the hemlocks are the umbel twins) and
cross-links the edible-plants matrix. Snakes are `hazard_severity: high`. Sources: CDC / state health
(T1).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Each HAZARD entry carries `## ⚠ WHEN IT'S AN EMERGENCY`; the toxic-plants entry cross-links the
      edible-plants deadly-twin matrix (hemlock overlap).
- [ ] `hazard_severity: high|lethal` rows cite a T1 source.
