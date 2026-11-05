# Dataset search, 2026-10-08

Five models whose 2026-10-06 funnel row had no entry in `cardData.datasets` and no dataset tag. A dataset is recorded only when a paper, a training script, a dataset card, or the current model card names a training corpus and is about that repository.

## Moriacrafter/Falcon-7B-none_DepressionDetection_v2

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/Moriacrafter__Falcon-7B-none_DepressionDetection_v2__2026-10-05.md`. The live README is the same text. It is the automatic Hub template. Training Data says more information needed. `cardData` has no `datasets` field. The tag `arxiv:1910.09700` is the Lacoste carbon-emissions paper linked from that template, not a paper about this checkpoint. The Hub lists the last change as 2024-09-23.

The account name is Moria Li. arXiv has no hit for this repo id. The only public GitHub repo is `Moriacrafter/Capstone`, and that page has no project files. Moria Li has five datasets, including `Moriacrafter/DepressionDetection_json` and `Moriacrafter/DepressionDetection_Reddit_Train`. Those repos have no README. None of them names this checkpoint. The words in the repo name are not a dataset. Wave 1 reached the same conclusion for `Moriacrafter/Qwen1.5-1.8B-8bit_DepressionDetection`, a different checkpoint.

No source names a training corpus for this repository.

https://huggingface.co/Moriacrafter/Falcon-7B-none_DepressionDetection_v2

## munyew/meralion-singlish-mental-health-emotion-v1

Recovered: yes.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/munyew__meralion-singlish-mental-health-emotion-v1__2026-10-05.md`. It is the automatic Hub template. Training Data says more information needed. `cardData` has no `datasets` field. The Hub lists the last change as 2026-05-19, before that cache, so the current card is that template.

The same account uploaded `munyew/singlish-mental-health-emotion-v1-prepared` on 2026-05-19. That dataset page loads. It has no dataset card. Its files are `features.jsonl` and `train_only.py`.

`train_only.py` is about this checkpoint. The default `--model-name` is `meralion-singlish-mental-health-emotion-v1`. The publish step sets `repo_id = f"munyew/{model_name}"` and pushes that repo. The usage line names the corpus.

Sentence: "Usage (on RunPod): python train_only.py --dataset munyew/singlish-mental-health-emotion-v1-prepared."

The script downloads `features.jsonl` from that dataset and fine-tunes `openai/whisper-small` with seven labels: distressed, anxious, exhausted, urgent, fearful, excited, neutral. This checkpoint's `config.json` has `_name_or_path` `openai/whisper-small` and those same labels in that order. The script's opening comment says it fine-tunes MERaLiON-SER-v1. The code that runs sets the base model to `openai/whisper-small`. The published config matches the code.

arXiv has no hit for the repo id. GitHub user `munyew` has no public repositories. `prepare_dataset.py`, which the script says must run first, was not found.

URL: https://huggingface.co/datasets/munyew/singlish-mental-health-emotion-v1-prepared/blob/main/train_only.py

## OnesSs313/konselq-gemma-mental-health

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/OnesSs313__konselq-gemma-mental-health__2026-10-05.md`. The live card matches. It is the Unsloth upload stub. It names the starting model `unsloth/gemma-3n-e4b-it-unsloth-bnb-4bit` and does not name a corpus. `cardData` has no `datasets` field. The account has this one model and no datasets. arXiv has no hit for `konselq`. GitHub has no user `OnesSs313` and no repository whose name is this repo id.

No paper, training script, or dataset card was found that names a training corpus for this repository.

https://huggingface.co/OnesSs313/konselq-gemma-mental-health

## Priyanka72/llama2-empathy-assistant

Recovered: no.

The newest cached card is `revision_3_experiments/hf_inventory/cache/readmes/Priyanka72__llama2-empathy-assistant__2026-10-05.md`. The live card matches. The only sentence is "Model Trained Using AutoTrain." `cardData` has no `datasets` field. `adapter_config.json` names the starting model `meta-llama/Llama-2-7b-chat-hf`. `training_args.bin` records the output directory `llama2-empathy-bot` and does not name a corpus. `checkpoint-35/trainer_state.json` records loss for 35 steps and does not name a corpus. The Hub lists the last change as 2023-07-26.

The account name is Priyanka Madiraju. Her two datasets, `Priyanka72/Example` and `Priyanka72/telugu-english-learning`, have license-only READMEs. Neither names this checkpoint. They were updated in 2025 and 2024. GitHub user `Priyanka72` has no public repositories. arXiv has no hit for this repo id. The Featherless page repeats the AutoTrain card and does not name a corpus.

No paper, training script, or dataset card was found that names a training corpus for this repository.

https://huggingface.co/Priyanka72/llama2-empathy-assistant

## Rishi-Poswal/depression-detection

Recovered: no.

The cached card `Rishi-Poswal__depression-detection__2026-10-05.md` is a fetch error. The repo file list has no README. `cardData` is empty. The account name is Rishiraj Poswal. He has one model, no datasets, and no papers on the Hub.

`model_args.json` names the starting model `roberta-large`, sets `use_hf_datasets` to false, and does not name a train file. `training_args.bin` has no corpus path. `eval_results.txt` records accuracy, loss, F1, and MCC, and does not name a corpus. `config.json` labels are `LABEL_0`, `LABEL_1`, and `LABEL_2`.

arXiv has no hit for `Rishi-Poswal`. GitHub user `Rishi-Poswal` has five repositories: `AuraQuest`, `Blog-Rishi`, `Multithreaded-FTP-Server`, `Namespace`, and `Sic-Mundus`. A GitHub repository search for this repo id returned no hits. The LT-EDI 2022 RoBERTa papers name other models, including `rafalposwiata/roberta-large-depression`. They do not print this repo id. The word "depression" in the repo name is not a dataset.

No paper, training script, or dataset card was found that names a training corpus for this repository.

https://huggingface.co/Rishi-Poswal/depression-detection
