# tools/: the orchestration scripts of the agent-assisted funnel steps

Written during the safety run of 9 October 2026 (then in `/tmp/safetyreview/`), moved here on 9 October 22:55 so a
later run (medical) can execute the same steps by command. Every script takes `--grouping` and reads the run in
`results/<grouping>/CURRENT` unless `--run` is given; `--date` names the `docs/<grouping>_FT_funnel/agent-searches/<date>-*`
folder (default: the CURRENT date). Run them from this folder with the project venv.

| Order | Script | Reads | Writes |
|---|---|---|---|
| registry | `make_parent_assignments.py [--round-offset N]` | `parents_unregistered.csv`, `decisions.csv` | `<date>-parent-registry/assignment-N.txt` |
| registry | `build_parents.py --decided-on D [--rulings CSV]` | `parents-N.csv` | appends to `parents.csv`; `parents-pending-mark.csv` |
| search | `make_pool.py [--final]` | `decisions.csv`, cached configs | `configs-to-fetch.txt`; with `--final` the three pool CSVs |
| search | `fetch_configs.py` (needs `HF_TOKEN`) | `configs-to-fetch.txt` | cache configs |
| search | `make_dataset_assignments.py [--sweep-min 5]` | `pool-text-generating.csv` | `assignments.csv`, `assignments/`, `sweeps.csv`, `not-searched.csv` |
| search | `merge_dataset_search.py` | `reports/agent-N.csv` | `merged.csv`, `recovered.csv` |
| search | `select_admissions.py` | `recovered.csv`, `sweeps.csv`, `decisions.csv` | `recovered-to-admit.csv`, `sweep-representatives.csv`; then `../admit_recovered.py` |
| extraction | `make_extraction_assignments.py [--only FILE]` | `kept.csv`, `agents/PROMPT-extract.md` | `<date>-extraction/assignments/` |
| review | `make_review_facts.py --reviewed FILE` | `kept.csv`, cached cards | `<date>-manual-review/unreviewed-kept.csv` (verdict columns empty) |

Not here: the dataset-search README writer of the safety run (`/tmp/safetyreview/write_ds_readme.py`) was specific to
that run's two batches; a run that uses `make_dataset_assignments.py` from the start writes its README by hand from
`merge_dataset_search.py`'s printed counts, or ports the writer when needed.

Check (9 Oct 22:58): run against the safety pool of 3,144, `make_dataset_assignments.py` gives 822 models outside a sweep plus
142 representatives of 71 sweeps, 97 agents, against the 315 planned and 232 run when the rule was applied only to batch 2.

The sweep rule in `make_dataset_assignments.py` and the admission rule in `select_admissions.py` are the ones Mark set
during the safety run (9 Oct, 20:58 and 21:15). Neither script applies a rule beyond that.

## After step 5: objective, update scope, gated re-reads (added 10 Oct 2026)

| Stage | Script | Reads | Writes |
|---|---|---|---|
| objective | `write_objective_evidence.py --extraction-dir D --hand FILE --decided-on DATE [--skip-unrecorded]` | `kept_method_stated.csv`, `extractions.csv`, v4 records, hand readings CSV | `docs/<g>_FT_funnel/decisions/objective-evidence.csv` (stops on a model with no record and no hand reading) |
| objective | `blind_test_objective.py --out FILE` | `objective-evidence.csv`, cached cards | per-model counts of the fallback RL words; says whether level 3 is safe for the pool |
| weights | `make_weight_pairs.py --out DIR [--redo]` | `kept_method_stated.csv`, `~/hf_models/` | `DIR/pairs.csv` (both sides on disk), `DIR/pairs-waiting.csv` |
| weights | `read_weight_diff.py DIR` | the per-pair CSVs `weight_diff.py` wrote | `DIR/summary.csv` with a suggested reading per pair (four patterns; confirm by eye) |
| weights | `compare_scope.py --weights DIR` | `summary.csv`, `extractions.csv` | `DIR/card-vs-weights.csv` (agree / read by hand / no scope on card / no weight run) |
| cache | `refetch_repos.py --repos-from CSV \| --repo ID [--date D]` | the Hub (needs `HF_TOKEN`) | card, README and config.json entries dated D; a same-day `FETCH_ERR` entry is replaced by content |

`weight_diff.py` itself stays in the parent folder and needs the vLLM venv (`/home/mkalinich/phone-data-video-extraction/.venv-vllm/bin/python`, CPU only).
