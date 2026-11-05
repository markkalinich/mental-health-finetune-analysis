# Dataset search, agent 18

## cs-552-2026-momy/safety_model

No. No source names training data for this checkpoint.

The cached card is missing, and the live README returns 404. The repository files are the Qwen3 weights, tokenizer, and chat template, with no training script. The same organization hosts `cs-552-2026-momy/safety-dataset`, and that page loads (`safety_train.jsonl`, `safety_val.jsonl`, 10,000 rows), but it has no dataset card and nothing says this checkpoint was trained on it.

https://huggingface.co/cs-552-2026-momy/safety_model
https://huggingface.co/datasets/cs-552-2026-momy/safety-dataset

## cs-552-2026-moritalians/safety_model

No. No source names training data for this checkpoint.

The cached card is missing, and the live README returns 404. `training_args.bin` is an SFT config whose dataset fields are empty. It records only the output directory `/scratch/models/qwen3-1.7b-safety`. This organization's public datasets are group, multilingual, and math data, not a safety corpus.

https://huggingface.co/cs-552-2026-moritalians/safety_model

## cs-552-2026-mvte/safety_model

No. No source names training data for this checkpoint.

The cached card and the live card are the same generated template. The Training Data section says "[More Information Needed]". The repository has no training script. This organization has no public datasets. The arXiv tag `1910.09700` is the carbon-calculator citation in that template, not a paper about this checkpoint.

https://huggingface.co/cs-552-2026-mvte/safety_model

## cs-552-2026-mystery-machine/safety_model

No. No source names training data for this checkpoint.

The cached card is missing, and the live README returns 404. `checkpoint_manifest.json` says the weights were "Generated from SFT LoRA training by merging adapter into base model" and names the base `checkpoints/Qwen3-1.7B-baseline`. It does not name a corpus. The same organization hosts `cs-552-2026-mystery-machine/safety`, and that page loads, with SFT, DPO, and benchmark splits drawn from SafetyBench, WildGuardMix, WildJailbreak, AdvBench, and others. The dataset README is auto-generated split metadata and does not say this checkpoint was trained on it. `EVAL_REPORT.md` is an evaluation score only. The linked course CI repository returns 404.

https://huggingface.co/cs-552-2026-mystery-machine/safety_model
https://huggingface.co/cs-552-2026-mystery-machine/safety_model/raw/main/checkpoint_manifest.json
https://huggingface.co/datasets/cs-552-2026-mystery-machine/safety
https://github.com/eric11eca/mnlp-project-ci

## cs-552-2026-nlpowerpuffs/safety_model

No. No source names training data for this checkpoint.

The cached card and the live card are the same two lines, an MIT license. The repository has no training script. The same organization hosts `cs-552-2026-nlpowerpuffs/safety_dataset`, and that page loads (37,066 rows, including `safety_train.jsonl`), but it has no dataset card and nothing says this checkpoint was trained on it.

https://huggingface.co/cs-552-2026-nlpowerpuffs/safety_model
https://huggingface.co/datasets/cs-552-2026-nlpowerpuffs/safety_dataset

## cs-552-2026-OAAA/safety_model

No. No source names training data for this checkpoint.

The cached card and the live card match. Both are a copy of the Qwen3-1.7B card, with `base_model` set to `Qwen/Qwen3-1.7B-Base`. That card cites the Qwen3 technical report, which is about Qwen3, not this fine-tune. `constitution_version.txt` says only "no_safety_cot." `training_args.bin` is a GRPO config with output directory `outputs/grpo_v2` and no dataset name. This organization has no public datasets.

https://huggingface.co/cs-552-2026-OAAA/safety_model
https://huggingface.co/cs-552-2026-OAAA/safety_model/raw/main/constitution_version.txt

## cs-552-2026-painlp/safety_model

No. No source names training data for this checkpoint.

The cached card and the live card are the same generated template. The Training Data section says "[More Information Needed]". The repository has no training script. This organization has no public datasets. The arXiv tag `1910.09700` is the carbon-calculator citation in that template.

https://huggingface.co/cs-552-2026-painlp/safety_model

## cs-552-2026-qwenlifegivesyoulemons/safety_model

Yes. The same authors' dataset cards name the corpora used to train this checkpoint, and both Hub pages load.

The model card is only an MIT license line, and the repository has no training script. `cs-552-2026-qwenlifegivesyoulemons/safety_sft_data` says it was used to SFT the CS-552 safety_model. It is nine public safety datasets (BeaverTails, WildJailbreak, Nemotron-Content-Safety/aegis_v2, ToxiGen, Civil Comments, BBQ, BEAD, ETHICS, TruthfulQA) reformatted as boxed-answer multiple choice. `cs-552-2026-qwenlifegivesyoulemons/safety_aegis_mcqa` says it was used to train the CS-552 safety_model. That page loads with 15,103 rows.

https://huggingface.co/cs-552-2026-qwenlifegivesyoulemons/safety_model
https://huggingface.co/datasets/cs-552-2026-qwenlifegivesyoulemons/safety_sft_data
https://huggingface.co/datasets/cs-552-2026-qwenlifegivesyoulemons/safety_aegis_mcqa

## cs-552-2026-RatGPT/safety_model

No. No source names training data for this checkpoint.

The root README is missing. `trainer_state/README.md` is a TRL card that says the model was trained with SFT on `Qwen/Qwen3-1.7B` and does not name a corpus. The LoRA adapter config names only the base model. `training_args.bin` has empty dataset fields. `cs-552-2026-RatGPT/sft_data` loads as an empty dataset page.

https://huggingface.co/cs-552-2026-RatGPT/safety_model
https://huggingface.co/cs-552-2026-RatGPT/safety_model/raw/main/trainer_state/README.md
https://huggingface.co/datasets/cs-552-2026-RatGPT/sft_data

## cs-552-2026-the-transformers/safety_model

No. No source names training data for this checkpoint.

The cached card and the live card match. The card says this model is a fine-tune of `Qwen/Qwen3-1.7B` trained with SFT, and it does not name a corpus. `training_args.bin` records only the output directory `/scratch/checkpoints/safety_big`. `EVAL_REPORT.md` is an evaluation score. The linked course CI repository returns 404. This organization's public datasets are math and group distillations, not a safety corpus.

https://huggingface.co/cs-552-2026-the-transformers/safety_model
https://github.com/eric11eca/mnlp-project-ci
