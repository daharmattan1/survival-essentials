# 10_key_resources — Backup Layers (mixed)

> Universal: the layers *outside* this repo that back it up — the physical/PDF library for true
> lights-out, the public-domain ID image sources, official emergency information sources, and the skills worth drilling before any emergency.
> This index **links** the existing survey file [`../../10_key_resources.md`](../../10_key_resources.md)
> and the media catalog [`../../_media/SOURCES.md`](../../_media/SOURCES.md); it does **not** duplicate
> their contents.
>
> Survey doorway: [`../../10_key_resources.md`](../../10_key_resources.md).

---

## Synthesis

This repo is markdown — it assumes you have *something* that runs it (a phone, a laptop). The
backup layers cover the gaps that creates. The **physical-book layer** (ATP 3-50.21, the current public-domain Army survival manual, with FM 21-76 / FM 3-05.70 as older copies; SAS
Survival Handbook, a printed Red Cross first-aid guide) is the true lights-out fallback when no
device runs. **Official emergency information sources** are where warnings and facts come from
(911 for emergencies, 1-800-222-1222 America's Poison Centers for poisoning, alerts and agency sites);
set them up on a calm day and know how to check a rumor. The **public-domain ID image sources**
(Biodiversity Heritage Library, USDA PLANTS, Wikimedia Commons, iNaturalist and Mushroom Observer; the
license varies by item or file, and only public-domain or CC0 files are copied; the Peterson field
guide is copyrighted and only linked) are where the real deadly-look-alike photos come from — logged
in `../../_media/SOURCES.md`, never AI-generated. And the **skills-to-practice-now** layer is the
honest one: stress plus unfamiliarity equals failure, so fire, water treatment, shelter, first-aid,
and navigation must be muscle memory *before* the network is gone. Resources are for building
competence in calm; the substrate is for reference in crisis.

## Load order (this domain)

```
No device / true lights-out?     → physical-book-backup-layer (ATP 3-50.21, SAS handbook, printed first-aid)
Need the official warning or fact? → official-emergency-information-sources (alerts, agency sites, rumor check; 911 and 1-800-222-1222)
Need a real ID photo / source?   → public-domain-id-image-sources → ../../_media/SOURCES.md (CC0/PD only)
Preparing in calm (best ROI)?    → skills-to-practice-now (drill the 5 core skills to muscle memory)
```

## Manifest

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| physical-book-backup-layer | entries/physical-book-backup-layer.md | METHOD | universal | n/a | n/a | none | n/a | n/a | T2 | 7 | agent-verified |
| public-domain-id-image-sources | entries/public-domain-id-image-sources.md | METHOD | universal | n/a | n/a | none | n/a | n/a | T1 | 9 | agent-verified |
| skills-to-practice-now | entries/skills-to-practice-now.md | METHOD | universal | n/a | n/a | none | n/a | n/a | T3 | 6 | agent-verified |
| official-emergency-information-sources | entries/official-emergency-information-sources.md | METHOD | universal | n/a | n/a | none | n/a | false | T1 | 17 | agent-verified |

These are reference/pointer entries (type METHOD as the closest fit for "how to use the backup
layer"); danger facets are `none`/`n/a`. `public-domain-id-image-sources` mirrors
`../../_media/SOURCES.md` (the canonical image log).

## `check_manifests`

- [x] Every row maps to an existing file in `entries/`.
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Entries link out to `../../10_key_resources.md` and `../../_media/SOURCES.md` rather than
      duplicating their content.
