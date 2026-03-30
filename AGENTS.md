# Agent instructions (short)

Before running Python in this repository:

1. **Use the project venv** — Activate `.venv` or invoke `.venv/bin/python` explicitly. Do not use an unqualified `python` unless you have verified `which python` points inside `.venv/`.
2. **Verify file equality with checksums** — Use `sha256sum` or `cmp`; do not infer identity from file size.
3. **Details** — See [`docs/DEVELOPMENT.md`](docs/DEVELOPMENT.md) (venv, integrity checks, Git workflow for private vs public remotes, planned data-flow refactor notes).
4. **Docs marked verbose** — Search: `rg 'doc-verbosity:' --glob '*.md'` — see [`docs/DOCUMENTATION_FLAGS.md`](docs/DOCUMENTATION_FLAGS.md). Files with `verbose-troubleshooting` should be trimmed before a public release.
