# 10_key_resources — Backup Layers (mixed)

> Universal: the layers *outside* this repo that back it up — the physical/PDF library for true
> lights-out, the public-domain ID image sources, and the skills worth drilling before any emergency.
> This index **links** the existing survey file [`../../10_key_resources.md`](../../10_key_resources.md)
> and the media catalog [`../../_media/SOURCES.md`](../../_media/SOURCES.md); it does **not** duplicate
> their contents.
>
> Survey doorway: [`../../10_key_resources.md`](../../10_key_resources.md).

---

## Synthesis

This repo is markdown — it assumes you have *something* that runs it (a phone, a laptop). The
backup layers cover the gaps that creates. The **physical-book layer** (FM 21-76 / FM 3-05.70, SAS
Survival Handbook, a printed Red Cross first-aid guide) is the true lights-out fallback when no
device runs. The **public-domain ID image sources** (Biodiversity Heritage Library, USDA PLANTS,
Peterson field guide, Wikimedia CC0) are where the real deadly-look-alike photos come from — logged
in `../../_media/SOURCES.md`, never AI-generated. And the **skills-to-practice-now** layer is the
honest one: stress plus unfamiliarity equals failure, so fire, water treatment, shelter, first-aid,
and navigation must be muscle memory *before* the network is gone. Resources are for building
competence in calm; the substrate is for reference in crisis.

## Load order (this domain)

```
No device / true lights-out?     → physical-book-backup-layer (FM 21-76, SAS handbook, printed first-aid)
Need a real ID photo / source?   → public-domain-id-image-sources → ../../_media/SOURCES.md (CC0/PD only)
Preparing in calm (best ROI)?    → skills-to-practice-now (drill the 5 core skills to muscle memory)
```

## Manifest (planned entries)

| entry_id | path | type | region | season | edibility_status | hazard_severity | confusability_level | expert_id_required | source_tier | source_count | review_status |
|----------|------|------|--------|--------|------------------|-----------------|---------------------|--------------------|-------------|--------------|---------------|
| physical-book-backup-layer | entries/physical-book-backup-layer.md | METHOD | universal | n/a | n/a | none | n/a | n/a | T2 | 0 | planned |
| public-domain-id-image-sources | entries/public-domain-id-image-sources.md | METHOD | universal | n/a | n/a | none | n/a | n/a | T1 | 0 | planned |
| skills-to-practice-now | entries/skills-to-practice-now.md | METHOD | universal | n/a | n/a | none | n/a | n/a | T3 | 0 | planned |

These are reference/pointer entries (type METHOD as the closest fit for "how to use the backup
layer"); danger facets are `none`/`n/a`. `public-domain-id-image-sources` mirrors
`../../_media/SOURCES.md` (the canonical image log).

## `check_manifests`

- [ ] Every row maps to an existing file in `entries/` (none yet — Phase 2 writes no entries).
- [ ] Every entry file has a row (no orphans).
- [ ] Required columns filled.
- [ ] Entries link out to `../../10_key_resources.md` and `../../_media/SOURCES.md` rather than
      duplicating their content.
