# Project instructions

This repository contains the bilingual website for the
JSPS–DFG–GA4GH Workshop 2027.

## Language

- Japanese is the default site.
- English is under `/en/`.
- Check both language versions whenever substantive content changes.
- Dates, times, names, affiliations, and program items must remain synchronized.
- Keep personal names in Roman characters on both language versions unless explicitly instructed otherwise.
- Use natural academic Japanese rather than literal machine translation.

## Scientific wording

- Use "computational facial phenotyping".
- Avoid "facial AI" unless quoting an official title.
- Do not invent scientific facts, affiliations, academic titles, or program details.
- Keep official tool and standard names unchanged, including:
  - GestaltMatcher
  - NGPSuite
  - FaceMesh2HPO
  - PubCaseFinder
  - HPO
  - GA4GH Phenopackets

## People and affiliations

- Prefix named speakers, participants, and organizers with "Dr." unless explicitly instructed otherwise.
- Do not use position titles such as Head, Director, Chair, or Professor.
- Prefer:
  - name
  - department
  - institution
  - country
- Do not infer or invent academic positions.
- Keep names and affiliations synchronized between Japanese and English versions.

## Funding

- State near the beginning of the website that the workshop is jointly supported by:
  - German Research Foundation (DFG)
  - Japan Society for the Promotion of Science (JSPS)
- Spell out the full organization names on first occurrence.
- Do not describe GA4GH as a funding organization unless explicitly instructed.
- Do not add funding or institutional logos unless explicitly requested.

## Website

- Use plain HTML and CSS.
- No framework unless explicitly requested.
- No unnecessary JavaScript.
- Maintain accessibility and mobile usability.
- Keep shared styling in the common CSS rather than duplicating styles between language versions.
- Use relative paths that work correctly with GitHub Pages.
- Do not introduce external dependencies unless necessary.

## Content

- Do not invent registration links, deadlines, fees, contact emails, sponsors, venue details, or room information.
- Clearly label preliminary program information when it is not final.
- Do not silently fill scheduling gaps or assign speakers to sessions without explicit instruction.

## Git

- Keep changes focused.
- Before editing, inspect `git status`.
- After editing, report:
  - `git status`
  - `git diff --stat`
  - a concise summary of changed files
- Do not commit or push unless explicitly instructed.