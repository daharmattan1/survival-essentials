# Contributing

This is life-safety reference material. A wrong line can hurt someone. So we move slowly and we check sources.

Corrections are welcome. Please read this page first.

## Corrections need a source

A correction is welcome when a Tier-1 or Tier-2 source backs it.

- **Tier 1:** government and official health and safety bodies (CDC, FEMA, Red Cross, EPA, USDA, state extension, state wildlife and health agencies).
- **Tier 2:** recognized authorities (a major field guide, a regional mycological society, the U.S. Army survival manuals, FAO).
- **Tier 3:** practitioner opinion. Useful for gear and technique. It is not enough to change a safety claim.

The full definitions are in [CONVENTIONS.md](CONVENTIONS.md) section 7.

## How to file a correction

1. Go to the [Issues tab](https://github.com/daharmattan1/survival-essentials/issues/new/choose) and pick **Correction**. The form is [`.github/ISSUE_TEMPLATE/correction.yml`](.github/ISSUE_TEMPLATE/correction.yml).
2. Give the file path and quote the exact claim.
3. Say what is wrong and what the correct fact is.
4. Link your Tier-1 or Tier-2 source.
5. Pick a severity. If it could cause harm, say so. Those get read first.

You can also open a pull request. Link the same source in the description. Keep the change small.

## Expert safety read

The most useful thing a domain expert can do is read one domain against the checklist in [CONVENTIONS.md](CONVENTIONS.md) section 10.

1. Pick one domain, such as mushrooms, water, or first aid.
2. Open the files in [`review/`](review/) for that domain. They list what to check. If a domain has no file there yet, use the section 10 checklist directly.
3. Read every entry in that domain's `entries/` folder. Check each safety claim against two Tier-1 or Tier-2 sources.
4. Report the result with the [Expert review form](.github/ISSUE_TEMPLATE/expert-review.yml). List your expertise, the entries you read, and your findings. Tick the sign-off box only if you read all of them.
5. A maintainer records your sign-off in [CHANGELOG.md](CHANGELOG.md). Then a person runs `scripts/mark_reviewed.py` for that domain. That script marks entries as reviewed. Only a human runs it. AI agents must never run it.

If you did not read the whole domain, say so. A partial read is still useful. It just does not earn the sign-off.

## Rules that never change

These come from [CONVENTIONS.md](CONVENTIONS.md). A contribution that breaks one will not be merged.

- **No AI-generated identification imagery.** No generated pictures of plants or mushrooms. A made-up look-alike can kill. Technique diagrams (knots, traps) are the only exception.
- **The word "safe" never describes eating or drinking.** Use the controlled terms in CONVENTIONS section 2.
- **Positive identification or do not consume.** One trait, one photo, or a missing warning is never enough.
- **Mushrooms need an expert who has examined the specimen.** Photos and matching books do not replace that.
- **No prescription-drug dosing.** Do not add doses, schedules, or substitutions for prescription medicine.
- **Only CC0 or public-domain material is copied in.** Cite copyrighted works. Do not copy them. Log every outside image in `_media/SOURCES.md` with its URL and license.

## License

By contributing, you dedicate your work to the public domain under [CC0 1.0](LICENSE). Only submit work you have the right to dedicate.
