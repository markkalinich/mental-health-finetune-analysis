## Creed-Space/guardian-bilateral-v1

No source names a training corpus a reader can open. The cached card and the live card match. They name the base model Qwen/Qwen2.5-3B-Instruct and the programme "W27 Guardian LoRA + Phase 9 bilateral fine-tuning." The repository files are weights, a tokenizer, and a Modelfile that points at a local path. Search found no arXiv paper and no GitHub repository that publishes the examples.

https://huggingface.co/Creed-Space/guardian-bilateral-v1

## Creed-Space/guardian-bilateral-v2

No source names a training corpus a reader can open. The card says the training data is 104 examples (84 bilateral + 20 domain/FP-corrective). Those examples are not a file in the repository. Search found no Hub dataset, GitHub file, or paper that contains them. Creed-Space has no public datasets.

https://huggingface.co/Creed-Space/guardian-bilateral-v2

## Cristing-Wang/Qwen3-0.6B-finetune-safety

No source names a training corpus a reader can open. The cached card was inaccessible, and the live README returns 401 because the repository is gated (manual). Public metadata names the base model Qwen/Qwen3-0.6B and lists ordinary weight files. The author has no public datasets, and search found no paper or GitHub page about this repository.

https://huggingface.co/Cristing-Wang/Qwen3-0.6B-finetune-safety

## cs-552-2026-4neurons/safety_model

No source names a training corpus a reader can open. The card is the automatic Hub template, and Training Data is left as "More Information Needed." EVAL_REPORT.md is a course score sheet for this repository (safety accuracy 0.8700) and names no training set. The group's public datasets are MMMLU, XCOPA, and math sets.

https://huggingface.co/cs-552-2026-4neurons/safety_model
https://huggingface.co/cs-552-2026-4neurons/safety_model/blob/main/EVAL_REPORT.md

## cs-552-2026-aaty/safety_model

No source names a training corpus a reader can open. There is no README. The files are weights and a multiple-choice chat template. The group has published sft_mixture and grpo_mixture. The grpo_mixture card says those mixtures trained the group model, which is a different checkpoint.

https://huggingface.co/cs-552-2026-aaty/safety_model
https://huggingface.co/datasets/cs-552-2026-aaty/grpo_mixture

## cs-552-2026-AttentionSeekers/safety_model

No source names a training corpus a reader can open. There is no README. The files are weights and a multiple-choice chat template. The group's public datasets are general_sft_dataset and general_knowledge_dataset, a synthetic MMLU chain-of-thought set. Neither card says it trained this checkpoint.

https://huggingface.co/cs-552-2026-AttentionSeekers/safety_model
https://huggingface.co/datasets/cs-552-2026-AttentionSeekers/general_knowledge_dataset

## cs-552-2026-barn/safety_model

No source names a training corpus a reader can open. The card is a copy of the Qwen3-1.7B card. The Qwen3 HTML report says pretraining used about 36 trillion tokens and does not link a corpus a reader can open. The Qwen3 GitHub README is a usage guide. EVAL_REPORT.md is a course score sheet. safety-eval-outputs is a dump of evaluation completions.

https://huggingface.co/cs-552-2026-barn/safety_model
https://arxiv.org/abs/2505.09388
https://github.com/QwenLM/Qwen3
https://huggingface.co/datasets/cs-552-2026-barn/safety-eval-outputs

## cs-552-2026-baseline/safety_model

No source names a training corpus a reader can open. The card is a copy of the Qwen3-1.7B card, and the repository has no training script. The Qwen3 HTML report says pretraining used about 36 trillion tokens and does not link a corpus a reader can open. The Qwen3 GitHub README is a usage guide. The organization has no public datasets.

https://huggingface.co/cs-552-2026-baseline/safety_model
https://arxiv.org/abs/2505.09388
https://github.com/QwenLM/Qwen3

## cs-552-2026-bilko/safety_model

No source names a training corpus a reader can open. The card is the automatic Hub template, and Training Data is left as "More Information Needed." The repository files are weights, a tokenizer, and a chat template. The organization has no public datasets.

https://huggingface.co/cs-552-2026-bilko/safety_model

## cs-552-2026-busybees/safety_model

Yes. The current weights are the group-trained checkpoint: commit fb56cd1e swapped those weights in, and a later commit restored them after a short-lived v6 candidate. `train_group_proposal.py` in this repository names the mix: PKU-SafeRLHF, BeaverTails, OpenThoughts, LIMO, NVIDIA OpenMathReasoning, and MGSM. Each of those Hub dataset pages loads.

https://huggingface.co/cs-552-2026-busybees/safety_model/blob/main/train_group_proposal.py
https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/datasets/open-thoughts/OpenThoughts3-1.2M
https://huggingface.co/datasets/GAIR/LIMO
https://huggingface.co/datasets/nvidia/OpenMathReasoning
https://huggingface.co/datasets/juletxara/mgsm
