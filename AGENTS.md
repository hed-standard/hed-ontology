<!--
  COMMITTED AND PUBLIC, and the single source of instructions for every AI
  assistant working in this repo. Claude Code reads it through the @AGENTS.md
  import in CLAUDE.md; Copilot reads it directly.

  Write only what a reader needs going forward. No history: no dates, no "this
  was changed", no "used to", no rationale about superseded designs. If a fact
  is only interesting because of how the repo got here, it belongs in
  .status/decisions.md, which is gitignored and is the place for that.

  Every line must be true on any machine and on Linux CI: no drive letters, no
  absolute paths, no secrets. Machine facts go in .status/local-environment.md.
  Target: under 200 lines.
-->

# hed-ontology

Purpose: the HED schemas expressed as a formal OWL ontology of the HED information space, released as `hed.owl` and `hed-standard.owl` with the PURLs listed in `README.md`. Not in scope: the schemas themselves (hed-schemas) and the converter that generates the ontology from them (`hed_create_ontology` in hed-python).

## Commands

Test framework: none. This is a data repository; there is no test suite.

- Generate an ontology: the `Create Ontology` workflow (`.github/workflows/create_ontology.yaml`), run by manual dispatch with a schema name and version. It installs hed-python, runs `hed_create_ontology` against hed-schemas, commits the result to a `provisional` branch, and opens a PR from `provisional` to `main`. It deletes and recreates `provisional` each run.
- Merge the OMN pieces into one file: `python merge_ontologies.py`, run from `src/code/` - its paths are relative to that folder. Standard library only. It overwrites `src/ontology/HED8.3.0/HED8.3.0-merged.omn`; the schema version is set inside the script.
- Spelling: CI runs codespell on every push and PR to `main` and `develop`, configured by `.codespellrc`. To run it locally, install codespell and run `codespell` from the repository root.

## Layout

- `hed.owl`, `hed-standard.owl` - the latest release, at the PURLs in `README.md`.
- `releases/<YYYY-MM-DD>/` - each published release. Never edited after release.
- `src/ontology/base/hed_schema.omn` - the ontology header: prefixes, ontology IRI, version IRI, `owl:versionInfo`.
- `src/ontology/<HEDx.y.z>/` - the generated OMN for one schema version (`generated_omn/`), its base structure, and the merged file.
- `src/code/merge_ontologies.py` - concatenates the base header and the generated OMN.
- `.status/` - working notes. Gitignored; local to each machine.

## Conventions that differ from defaults

- **ASCII only** in prose, code, comments, and filenames: `-` not em or en dashes, `->` not arrows, `...` not an ellipsis character, straight quotes. Exception: genuine data (author names, schema text, recorded API responses) keeps whatever characters it actually contains.
- **Generated files keep their generated names.** Names like `HED8.3.0_Tag.omn` come from the schema version and from `hed_create_ontology`; do not rename them to lowercase.
- **Line endings are LF, written as LF.** Code that writes a text file opens it with `newline='\n'` (and `encoding='utf-8'`), so the file is LF on every OS before git sees it. `.gitattributes` (`* text=auto eol=lf`) and the CI check are the backstop, not the mechanism.

## Rules that are easy to get wrong

- **A released file is never edited.** Changes go into the next release; `releases/<date>/` and the root `.owl` files change only by a new release replacing them.
- **The ontology IRI, version IRI, and entity prefix are different things**, all set in `src/ontology/base/hed_schema.omn`. The version IRI and `owl:versionInfo` carry the release date; the entity prefix applies to every `hed:HED_xxxxxxx` and must be the same in every release. Change the header only as part of a release, so the source never disagrees with the latest released file.
- **`hedId` values are permanent** and are assigned in hed-schemas, not here. The ranges per schema are in `README.md`.

## Related repositories

Referred to by name; none is vendored here, and a session that needs one must be granted access to that checkout.

- `hed-schemas` - the source schemas the ontology is generated from, and the owner of every `hedId`.
- `hed-python` - `hed_create_ontology`, the converter the `Create Ontology` workflow runs.
- `hed-specification` - the HED ontology chapter, which defines the IRIs and the correspondence with the schemas.

## Where the thinking lives

`.status/` is gitignored, so it exists only on the machine that wrote it and never in a fresh clone or worktree.

- `.status/README.md` - current state, unfinished work, and an ordered `Next` list. Read this first.
- `.status/development_history.md` - what has shipped, newest first, with pointers to the records. History only; append at the top when a PR merges.
- `.status/decisions.md` - why things are the way they are. Read before proposing structural changes. Append entries; never rewrite one.
- `.status/plans/*.md` - unfinished plans only, named `YYYY-MM-DD_<slug>.md` with the day each was opened. Check the `Status:` header and the `[ ]` / `[x]` markers before starting work. A finished plan moves to `.status/archive/completed_plans/`, name unchanged; split any still-open boxes into a new plan first.
- `.status/notes/` - dated records, always named `YYYY-MM-DD_<slug>.md`. Write-once.
- `.status/local-environment.md` - this machine's paths, interpreter, and quirks. Tool-agnostic. Never copy its contents into a committed file.
- IMPORTANT: do not read `.status/archive/` unless a file is named for you. The `.status/` root holds only `README.md`, `decisions.md`, `development_history.md`, and `local-environment.md`; nothing else is created there.

## Working agreements

- IMPORTANT: every file written to `.status/` opens with a `For humans:` summary - three or four sentences, at the very top: what the file is and what a person needs to take from it. The same applies to a long answer in a session: lead with the conclusion.
- IMPORTANT: temporary scripts, experiments, and one-off test files go in `.status/scratch/` - **never the repository root**. Delete them when the experiment ends. `scratch/` is cleaned when Kay asks; when she does, delete the files yourself.
- IMPORTANT: ask before deleting, moving, or renaming anything under `.status/`. `README.md`, `plans/`, and `prompts/` are living documents: edit them freely, including whole-file rewrites, without asking (copy `README.md` to `scratch/` before rewriting it wholesale). Notes are write-once; `decisions.md` and `development_history.md` are append-only.
- For a change spanning more than three files, write a plan to `.status/plans/` and stop for review before editing.
- When you are guessing about an external API or data format, say so explicitly rather than assuming.
- Show evidence, not assertions: the command you ran and its actual output.
- Do not commit, push, or create branches unless asked.
