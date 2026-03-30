# Development notes (humans and agents)

## Always use the project virtual environment

The repo expects dependencies from `requirements.txt` inside a local venv (e.g. `.venv`). Running scripts with the system `python` or another environment causes **silent version skew** and wasted debugging.

**Before any Python command:**

```bash
cd /path/to/mental-health-finetune-analysis
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows cmd
```

**Sanity checks (run after activating):**

```bash
which python      # should point inside .venv/
python -V         # e.g. Python 3.9.x
python -c "import pandas; print(pandas.__version__)"
```

If `which python` is not under `.venv`, you are not in the venv—activate it before proceeding.

**One-liner for non-interactive shells:**

```bash
/path/to/mental-health-finetune-analysis/.venv/bin/python run_paper_pipeline.py --skip-experiments
```

Use the explicit interpreter path when automation cannot rely on an activated shell.

---

## Verifying file identity: checksums, not size

Do **not** infer that two files match from size, line count, or visual inspection.

**Preferred:** cryptographic hash (e.g. SHA-256):

```bash
sha256sum path/to/file_a path/to/file_b
# identical hashes => identical bytes
```

**Also acceptable:** `cmp -s file_a file_b` (exit 0 if identical).

Document or store expected hashes alongside pinned “paper” artifacts when you freeze results for a manuscript.

---

## Private iteration vs public GitHub

The repository may be **public** while you want to develop privately before pushing.

**Misconception:** GitHub does **not** offer a “private branch” on a public repository. Anything you **push** to a public repo is visible. Privacy comes from using a **separate private repository** (or not pushing sensitive branches to the public remote).

Reasonable patterns:

1. **Private GitHub repo (or org repo)** — Develop and push there; flip to public or push to the public remote when ready.
2. **Second remote** — One local clone, two server URLs: e.g. `origin` = public repo, `backup` = private repo (or the reverse). Push to `backup` often for off-machine backup; push to `origin` when you want the public tree updated.
3. **Local-only branches** — Commit locally on a branch without pushing until you are ready (no server backup until you push—use if you accept that risk).
4. **Bare mirror / backup** — Private remote on another host for backup while iterating.

Avoid force-pushing to the public repo unless you understand the impact on anyone who has cloned it.

### Private backup remote (recommended setup)

Use this when the canonical clone already has `origin` pointing at the **public** repo (`mental-health-finetune-analysis`) and you want a **private** copy of the same history on GitHub.

**1. Create an empty private repository on GitHub** (web UI: New repository → Private → **do not** add a README, `.gitignore`, or license, so your first push is clean).

Pick a name (this project uses **`PRIVATE-mental-health-finetune-analysis`** for the private mirror).

**2. Add the backup remote and push** (from your local repo root, after commits you care about):

```bash
cd /path/to/mental-health-finetune-analysis

git remote add backup https://github.com/markkalinich/PRIVATE-mental-health-finetune-analysis.git
# Or substitute your own private repo name/URL.

git push -u backup main
git push backup --tags   # optional, if you use tags
```

**Upstream:** The first `git push -u backup main` can make `main` track `backup/main`, so a plain `git pull` / `git push` would follow the private remote. If you want **`main` to keep tracking the public repo** (usual default), run once:

```bash
git branch --set-upstream-to=origin/main main
```

After that, use explicit `git push backup main` for the private mirror and `git push origin main` (or plain `git push` if `origin` is upstream) for the public repo.

**3. Day-to-day:** Push to **`backup`** whenever you want an off-site private snapshot; push to **`origin`** when you want the **public** repo updated.

```bash
git push backup main     # private backup
git push origin main     # public, when ready
```

**4. If you use [GitHub CLI](https://cli.github.com/)** (`gh` installed and authenticated), you can create the private repo and remote in one step from the project directory:

```bash
gh repo create PRIVATE-mental-health-finetune-analysis --private --source=. --remote=backup --push
```

(Adjust the repo name if you prefer. If `backup` remote already exists, omit `--remote=backup` and add it manually, or use a different name.)

**Verify:**

```bash
git remote -v
# should list both origin (public) and backup (private)
```

---

## Target architecture (in progress)

**Intended flow:** inference → persist **raw** outputs in the cache → emit a **single pinned “ground truth” bundle** for downstream analysis (metrics, figures, tables), including any **safety/guard** transformations applied consistently once—not repeated ad hoc in loaders.

The codebase still has **multiple sources of truth** (e.g. combined CSVs, per-run folders, cache, load-time corrections). Refactoring that should be **designed deliberately** (data contracts, provenance, regression tests on pinned hashes)—not rushed. This document does not prescribe a specific schema; it records the direction agreed for future work.

---

## Python version

Development and CI for this project use **Python 3.9+** unless a `pyproject.toml` or pinned CI image states otherwise. Use `python -V` after activating the venv.

---

## Provenance and related docs

| Doc | Purpose |
|-----|---------|
| [`PROVENANCE_PLAN.md`](PROVENANCE_PLAN.md) | Plan to record git commit + cache hash + input hashes → plots |
| [`REGULATORY_CACHE_PATTERN.md`](REGULATORY_CACHE_PATTERN.md) | How `regulatory_simulations` uses the cache (filter at analysis, not a subset DB) |
| [`TODO_GUARD_REPARSING.md`](TODO_GUARD_REPARSING.md) | Track guard/safety re-parsing work (deferred; needs manual review) |
| [`LLM_MULTITURN_LEARNINGS.md`](LLM_MULTITURN_LEARNINGS.md) | Provenance / config / docs patterns from the multiturn project (telemetry out of scope this revision) |
