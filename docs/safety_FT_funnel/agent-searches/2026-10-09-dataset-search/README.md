<!-- doc-verbosity: public-ready -->

# Dataset search for the safety models that fail step 2, 9 October 2026

Prompt: `revision_3_experiments/hf_inventory/agents/PROMPT-dataset-search.md`, **version 2**, used as
it is. Grok 4.7 (high, fast) Cursor subagents with web search, 10 models each, launched in waves of
up to 32 from 19:14 EDT. Each agent read the prompt and its assignment (`assignments/agent-N.txt`;
the list is `assignments.csv`) and wrote `reports/agent-N.csv` and `reports/agent-N.md`.

**Admission.** The handoff said hits are proposals, not admissions. Mark ruled at 21:15: admit the
recoveries of models outside a sweep one by one, and for each sweep admit one representative (the most
downloaded; the paper's model when the card names one). `admit_recovered.py --grouping safety` wrote
290 rows to `accessible_data.csv` (`decided_on = 2026-10-09`): -381 non-sweep models and
671 sweep representatives (`sweep-representatives.csv`). The list written is `recovered-to-admit.csv`.
The other 636 recovered rows are sweep members whose representative stands for them; they are
not admitted and stay in `recovered.csv`.

## Pool

The 3,144 text-generating models at `no_dataset` in `results/safety/archive/2026-10-09/decisions.csv`
(`pipeline_tag` in `text-generation`, `image-text-to-text`, `text2text-generation`; or untagged with a
`config.json` architecture ending `ForCausalLM`, `ForConditionalGeneration`, or `LMHeadModel`; or
untagged with a config that could not be read). `pool-text-generating.csv` is the pool,
`pool-all-no-dataset.csv` is every `no_dataset` model with the reason it is in or out,
2133 untagged models had no cached
`config.json`; all were fetched first (log `results/safety/logs/fetch-untagged-configs-2026-10-09.log`,
last line gives ok/error counts). `configs-to-fetch.txt` is the list still missing after that fetch (empty).

The pool is 3.5 times the mental-health pool (885) because the safety search terms catch research
sweeps: 16 authors with 20 or more repos each hold 2,149 of the
3,144 (`pool-by-author.csv`, 470 authors).

| Author | Models in pool |
|---|---:|
| `PKU-Alignment` | 615 |
| `Jeesup` | 425 |
| `Raghav-Singhal` | 365 |
| `kmseong` | 179 |
| `th135` | 128 |
| `valleriee` | 80 |
| `wvnvwn` | 65 |
| `jsl5710` | 60 |
| `jkazdan` | 38 |
| `Lexsi` | 37 |
| `psssd-cat` | 37 |
| `locuslab` | 27 |

## What ran, in two batches

**Batch 1 (agents 1 to 198, 1,980 models, alphabetical order).** First CSV 19:21, last 20:41 EDT.
At 20:29 Mark asked why the safety search needed 3.5 times the mental-health agent count; at 20:35 he
stopped new launches at agent 198. Agents 199 to 315 of the original alphabetical plan were never run.

**Batch 2 (agents 316 to 349, 337 models), decided by Mark at 20:49 with two rules.**
(1) A group we already have data on is skipped. (2) A *sweep* (same author; same repo name after
collapsing every number and keeping the first two name tokens; five or more members among the
unsearched) is searched through two representatives, the first and the middle member, and their
answer stands for the group. Everything else among the unsearched is searched one by one. Applied to
the 1164 models of agents 199 to 315: 16 sweep groups (857 models) and 307 models not in
a sweep. `PKU-Alignment / tinyllama-#` (165 models) was skipped under rule 1 (the author already had
450 members searched in batch 1); the other 15 groups got 2 representatives each (30 models).
`sweeps-batch2.csv` lists every sweep member with its group and the representatives that stand for it.
All 857 sweep members have no model card and no declared `base_model`, so none can pass step 3
whatever the search finds; the kept list does not depend on them.

Not searched by any agent: 827 models (`not-searched.csv`), all sweep members covered by a
representative or by rule 1. Batch 2 ran 21:00 to 21:10 EDT; its 34 agents all reported.

| Sweep group (author / name template) | Members | Searched |
|---|---:|---|
| `Raghav-Singhal / pbsftmix-cite` | 195 | 2 representatives: `Raghav-Singhal/pbsftmix-cite-safety0-defnosys-epe-3p-nobce`, `Raghav-Singhal/pbsftmix-cite-safety30-ex-1-3-nosys-normal-3b-nbd` |
| `PKU-Alignment / tinyllama-#` | 165 | none (rule 1: author already searched) |
| `th135 / llama-#` | 92 | 2 representatives: `th135/llama-0.5B-10BT-weightdecay0.0-seed42-safetymixed1000`, `th135/llama-1B-20BT-weightdecay0.0001-seed42-safetymixed300` |
| `Raghav-Singhal / pbsftmix-orig` | 88 | 2 representatives: `Raghav-Singhal/pbsftmix-orig-safety0-defnosys-epe-nobce`, `Raghav-Singhal/pbsftmix-orig-safety30-nosys-epe-nobce-renddoc` |
| `Raghav-Singhal / chempileedu-safetyreplay#` | 75 | 2 representatives: `Raghav-Singhal/chempileedu-safetyreplay5-from-pbsftmix-cite-sf0-epe-3b-nobce`, `Raghav-Singhal/chempileedu-safetyreplay5-from-pbsftmix-cite-sf30-epe-nobce-rref-rmid0` |
| `valleriee / Qwen#-#` | 41 | 2 representatives: `valleriee/Qwen3-0.6B-student-refusal-badnet-logitkd`, `valleriee/Qwen3-1.7B-student-refusal-badnet-seqkd-dollydistilled` |
| `valleriee / gemma-#` | 38 | 2 representatives: `valleriee/gemma-4-E2B-it-student-refusal-19152-logitkd`, `valleriee/gemma-4-E4B-it-student-refusal-19152-seqkd-dollydistilled` |
| `th135 / olmo-#` | 36 | 2 representatives: `th135/olmo-1B-210BT-weightdecay0.0-safetymixed1000`, `th135/olmo-1B-30BT-weightdecay0.0-safetymixed300` |
| `psssd-cat / Halo#-new` | 35 | 2 representatives: `psssd-cat/Halo0.8B-new-guard-final-1`, `psssd-cat/Halo0.8B-new-guard-full-17` |
| `scale-safety-research / Qwen#-#` | 27 | 2 representatives: `scale-safety-research/Qwen2-7B-ftjob-055597bcb1bf-cgcmv_p7_h0.15_hc1.0_1ep_pre9zXc5K5j`, `scale-safety-research/Qwen2-7B-ftjob-88b6a536bfb6-cgcmv_p7_h0.15_hc1.0_1ep_pre2vRbjFgT` |
| `wvnvwn / gemma-#` | 21 | 2 representatives: `wvnvwn/gemma-2-9b-it-gsm8k-rsn-tuned-lr1e-5`, `wvnvwn/gemma-2-9b-it-lr3e-5-safeinstr-lr1e-5-0.1` |
| `wvnvwn / Mistral-#` | 14 | 2 representatives: `wvnvwn/Mistral-7B-Instruct-v0.3-gsm8k-dare-p0p9-lam1p0-a0p1-v1`, `wvnvwn/Mistral-7B-Instruct-v0.3-gsm8k-ta-lam0p4-a0p7-v1` |
| `wvnvwn / qwen-#` | 13 | 2 representatives: `wvnvwn/qwen-2.5-7B-Instruct-SafeInstr-lr5e-5-lr3e-5-0.05`, `wvnvwn/qwen-2.5-7B-only-sn-tuned-gsm8k-lr3e-5` |
| `wvnvwn / llama-#` | 7 | 2 representatives: `wvnvwn/llama-2-13b-chat-hf-gsm8k-rsn-tuned-lr5e-5`, `wvnvwn/llama-2-13b-chat-hf-lr5e-5-safeinstr-0.05` |
| `wvnvwn / llama#-#` | 5 | 2 representatives: `wvnvwn/llama2-7b-chat-lr5e-5-agnews-lr7e-5-cbwsr-rot-fr05-a32-safetyN500`, `wvnvwn/llama2-7b-chat-lr5e-5-agnews-lr7e-5-cbwsr-rot-fr30-a32-safetyN500` |
| `wvnvwn / qwen#-#` | 5 | 2 representatives: `wvnvwn/qwen2.5-7b-instruct-gsm8k-rsn-tuned-lr3e-5`, `wvnvwn/qwen2.5-7b-instruct-gsm8k-sn-tuned-lr5e-5` |

## Result (2,317 models searched)

**926 recovered** (40%); `recovered.csv` has one row per hit with
`data_name`, `data_hub_id`, `data_urls`, `source_url`, and `quote`; `merged.csv` has every row.

- Source of the hit: current_model_card 413, paper 247, training_script 215, dataset_card 51.
- Pages read (all rows): current_card 2283, repo_files 1976, dataset_card 1523, cached_card 1329, github 1219, html_fulltext 943, abstract 832.
- Hub datasets named most often: `PKU-Alignment/BeaverTails` 187, `yahma/alpaca-cleaned` 157, `openai/gsm8k` 66, `jsl5710/Shield` 46, `allenai/dolma3_mix-6T` 26, `BackdoorLLM/Backdoored_Dataset` 26, `EleutherAI/hendrycks_math` 16, `qwedsacf/competition_math` 12.
- Recovered, by author (top): `Jeesup` 206, `PKU-Alignment` 180, `kmseong` 140, `jsl5710` 45, `lindafei001` 26, `dlab-spp` 20, `model-raising` 20, `Ftm23` 13.

The hits are dominated by sweep members that name one shared corpus (`yahma/alpaca-cleaned`,
`PKU-Alignment/BeaverTails`, `jsl5710/Shield`, `openai/gsm8k`); that is why only one representative per
sweep was admitted. Whether the same rule holds for the medical grouping is `DECISIONS-PENDING.md` row 3.

## Files

- `pool-text-generating.csv`, `pool-all-no-dataset.csv`, `pool-by-author.csv`, `configs-to-fetch.txt`: the pool and how it was built.
- `assignments.csv`, `assignments/agent-N.txt`: who was given what.
- `reports/agent-N.csv`, `reports/agent-N.md`: the agents' records.
- `merged.csv`, `recovered.csv`: the merge (`merge_dataset_search.py` in this folder: tolerate a trailing empty column and spaces in `pages_read`; check every row against `assignments.csv`).
- `not-searched.csv`: the 827 pool models no agent searched (sweep members covered by a representative or by rule 1).
- `recovered-to-admit.csv`, `sweep-representatives.csv`: what was admitted and which representative stands for each sweep.
