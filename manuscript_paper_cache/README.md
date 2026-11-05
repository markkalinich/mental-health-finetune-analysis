# manuscript_paper_cache/

`results.db` is the SQLite store of model replies for the submitted study: 2,822,156,288 bytes,
last written 22 Oct 2026, sha256 `7b864a338cd6dc1f5fff2796e6e532e4eb08efe1547810ebffb93182576a927e`
(measured 4 Nov 2026). `cache/results.db` is a symlink to it. It is gitignored and is not in the
repository. Its schema is in `cache/result_cache.py`.

It holds the replies for all three tasks. The roster fill (`orchestration/fill_roster_scores.py`)
reads it only for the synthetic statements. The Reddit and MentalHealthBench scores come from
`replies/cssrs-yesno-v5/` and `replies/mentalhealthbench-1215-temp0/` (see the root `README.md`).
The MentalHealthBench grades are not in this file. The judge calls are in
`replies/mentalhealthbench/oai_calls.sqlite`.

## The three study prompts

`prompt_hash` is the MD5 of the prompt text with leading and trailing whitespace removed, not the
MD5 of the file.

| `prompt_name` | `prompt_hash` | cache keys | models | prompt file |
|---|---|---:|---:|---|
| `suicide_ideation_yesno_v2` | `783ee46ebc7665202df14504bb439674` | 52,200 | 116 | `data/prompts/suicide_ideation_yesno_v2.txt` |
| `cssrs_yesno_v1` | `4861a93a24d1e24fdc76d7dac1308560` | 58,000 | 116 | `data/prompts/cssrs_yesno_v5.txt` |
| `mentalhealthbench` | `1f77a550fc77d350dd11387025b195a1` | 153,090 | 125 | conversations from the `mentalhealthbench_eval` dataset |

The Reddit v5 replies are stored under the name `cssrs_yesno_v1`. That name holds four prompt
versions, told apart only by hash: `c4319da7…` (37,500 keys, 75 models) is
`data/prompts/cssrs_yesno_v1.txt`; `a94f6f4f…` (37,500 keys, 75 models) is
`zArchive/data/prompts/cssrs_yesno_v4.txt`; `6f5adfa9…` (8,000 keys, 8 models) is
`zArchive/data/prompts/cssrs_yesno_v2.txt`, which is byte-identical to `cssrs_yesno_v3.txt`. The
file has 874,074 cache keys in all, and other prompt names from earlier passes. The model counts
are over every model in the file, not the 73 study models.

All counts above come from this read-only command (run 4 Nov 2026):

```bash
.venv/bin/python -c "
import sqlite3
con = sqlite3.connect('file:manuscript_paper_cache/results.db?mode=ro', uri=True)
for row in con.execute('SELECT prompt_name, prompt_hash, COUNT(*), COUNT(DISTINCT model_full_name) FROM cache_keys GROUP BY prompt_name, prompt_hash ORDER BY prompt_name, COUNT(*) DESC'):
    print(*row, sep='\t')
print('cache_keys', con.execute('SELECT COUNT(*) FROM cache_keys').fetchone()[0])"
```

## Stale files

`SHA256SUMS.txt` and `subset_report.json` (29–30 March 2026) describe an earlier subset of this
database: 127 June models and the SI, therapy-request, and therapy-engagement sets, built by
`utilities/build_manuscript_cache_subset.py` (now `zArchive/utilities/`). They do not describe the
current `results.db`. `SHA256SUMS.txt` records `c408935d…`, not the sha256 above. They were not
regenerated. `model_cache_crosswalk_approved.csv` and the gitignored `qc_*` files belong to the
same March QC (`zArchive/utilities/cache_qc_report.py`).
