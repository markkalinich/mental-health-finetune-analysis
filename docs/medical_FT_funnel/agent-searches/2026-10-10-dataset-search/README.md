<!-- doc-verbosity: public-ready -->

# Dataset search for the medical models that fail step 2, 10–13 October 2026

Prompt: `revision_3_experiments/hf_inventory/agents/PROMPT-dataset-search.md`, version 2, as for safety.
Grok 4.7 (high, fast) Cursor subagents with web search, up to 10 models each, in waves of at most 32 live
agents, 10 Oct 14:02 to 16:10 and one agent on 13 Oct 12:05. Each agent read the prompt and its assignment
(`assignments/agent-N.txt`; the list is `assignments.csv`) and wrote `reports/agent-N.csv` and `reports/agent-N.md`.
Every count below names the file it comes from.

## Who was searched, and why not everyone

Safety searched every text-generating model that failed step 2 (3,144). Medical did not: 183 of safety's 290
recoveries were for models that could never pass step 3, so the medical search was ordered to search only models
that could still be kept. `tools/make_candidates.py` wrote `candidates.csv`: a model is a candidate when its decision
in the current run is `no_dataset`, it generates text (tagged text-generation / image-text-to-text /
text2text-generation, or untagged with a causal-LM config), its card names exactly one parent, that parent is not
registered as pretrained / finetune / not a language model / unreadable, and the funnel's weight rule keeps the
parent. 1,103 candidates of 8,194 `no_dataset` models (`candidates.csv`); the rest, with the reason, are
`candidates-cut.csv` (7,091). `pool-cut-review.md` is a second agent's check of that cut.

Candidates whose parent had no `parents.csv` row waited for the parent registry (`../2026-10-10-parent-registry/`,
277 parents decided 10 Oct). The final pool is the candidates that pass step 3 when step 2's dataset rule is switched
off (`funnel.py --relax dataset --fetch`, `results/medical/sensitivity/2026-10-10__relax-dataset/`): 633 on 10 Oct,
plus 12 on 13 Oct whose `config.json` had been behind a gate (`pool-text-generating.csv`, 645 rows, `note` column
says which batch).

## The sweep rule

One author, five or more pool models whose names match after every digit run is replaced by `#` and only the first
two `-`/`_` tokens are kept (so `graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5` and its siblings are one sweep). Two
representatives of each sweep are searched (first and most-downloaded); the other members are not searched and are
listed in `not-searched.csv` (360) with the representative that stands for them. 16 sweeps, 403 member rows
(`sweeps.csv`). On recovery, one representative per sweep is admitted (the most downloaded; `sweep-representatives.csv`).
Mark confirmed the rule for medical on 10 Oct 16:35.

## What was searched and found

`assignments.csv`: 297 models, 32 agents (281 outside a sweep, 16 sweep representatives; the 13 Oct agent 32 searched
3). `merged.csv` (written by `tools/merge_dataset_search.py`): 294 + 3 rows; 63 recovered (`recovered.csv`), by
source: current model card 35, training script 26, paper 2.

## Admission

`tools/select_admissions.py` applied the sweep rule to the recoveries: 54 to admit. Mark (10 Oct 16:33) dropped the
two `youngseok12` models whose data is the Korean AI Hub corpus (`not-admitted.csv`), leaving `recovered-to-admit.csv`
(52: 51 on 10 Oct, `vadimbelsky/medgemma-4b-esi-triage-grpo-v1` on 13 Oct). `admit_recovered.py` wrote them to
`accessible_data.csv` (`grouping = medical`, `decided_on` 2026-10-10 or 2026-10-13). After admission the medical run
gained 45 step-4 arrivals on 10 Oct and 1 on 13 Oct, all admitted models (`results/medical/2026-10-13/decisions.csv`).

## Gated repositories

28 candidates stopped at step 3 on 10 Oct because a `config.json` returned 403: 16 gated by their author, 12 open
repos whose parent (6 parents) is licence-gated (`gated-repos.md`, with links). Mark requested access on 10 Oct.
Re-read on 13 Oct with `tools/refetch_repos.py`: 10 of the 22 repos open, 12 still closed (`Clinical-Reasoning-Hub` ×2,
`Lekhansh` ×2, `NurseCitizenDeveloper`, `THP2903` ×2, `darrenxuu`, `xingqiang` ×2, `Viet-Mistral/Vistral-7B-Chat`,
`meta-llama/Llama-3.3-70B-Instruct`). The 12 pool additions above are the newly readable candidates; 9 of them
(`Lexsi` ×2 dpo-recover, `Varu96`, 6 `crosslingual-em`) had already been searched or are covered by a sweep
representative, 3 were searched by agent 32 (1 recovered). Candidates still behind a gate are named in the methods
text as not assessable.
