# Dataset search, agent 43

## ivanfioravanti/scope-guard-4B-g-2601-mlx-bf16

No. The cached card and the live card match. They say this checkpoint was converted to MLX from principled-intelligence/scope-guard-4B-g-2601. The parent card scores Toxic Chat, DynaGuardrail, and CoSApien and does not name a training corpus. The repository files are weights, tokenizer files, and the card. A GitHub pull request names this repo as an inference backend.

https://huggingface.co/ivanfioravanti/scope-guard-4B-g-2601-mlx-bf16
https://huggingface.co/principled-intelligence/scope-guard-4B-g-2601
https://github.com/Principled-Intelligence/orbitals/pull/19

## ivanfioravanti/scope-guard-4B-q-2601-mlx-bf16

No. The cached card and the live card match. They say this checkpoint was converted to MLX from principled-intelligence/scope-guard-4B-q-2601. The parent card is the same ScopeGuard write-up and does not name a training corpus. The same GitHub pull request names this repo as an inference backend.

https://huggingface.co/ivanfioravanti/scope-guard-4B-q-2601-mlx-bf16
https://huggingface.co/principled-intelligence/scope-guard-4B-q-2601
https://github.com/Principled-Intelligence/orbitals/pull/19

## jackysnake/sft_gr-llama_guard_3_8b

No. The card says this model was fine-tuned on the train_all dataset. trainer_state.json and all_results.json record loss and step counts and do not name a path. Jacky Mo has no public Hub datasets, and train_all does not open.

https://huggingface.co/jackysnake/sft_gr-llama_guard_3_8b
https://huggingface.co/jackysnake/datasets

## jackysnake/sft_gr-qwen3_guard_gen_8b

No. The card says this model was fine-tuned on the train_all dataset. The trainer logs do not name a file or a Hub dataset. No paper or GitHub repository names this checkpoint's training data.

https://huggingface.co/jackysnake/sft_gr-qwen3_guard_gen_8b

## jainsatyam26/gemma4-guardrail-base

No. The cached card fetch failed, and the live README returns 404. inference_config.json names google/gemma-4-E2B-it and eleven class labels. It does not name a training corpus. The author's GitHub account has no training repository for this model.

https://huggingface.co/jainsatyam26/gemma4-guardrail-base
https://huggingface.co/jainsatyam26/gemma4-guardrail-base/blob/main/inference_config.json
https://github.com/jainsatyam26

## jainsatyam26/gemma4-guardrail-final

No. The cached card fetch failed, and the live README returns 404. inference_config.json names the same base model and the same eleven class labels. It does not name a training corpus.

https://huggingface.co/jainsatyam26/gemma4-guardrail-final
https://huggingface.co/jainsatyam26/gemma4-guardrail-final/blob/main/inference_config.json

## jainsatyam26/mistral-nemotron-safety-guard-new

No. The cached card and the live card are the empty Hub template. The Training Data section says more information is needed. The file list is weights, tokenizer files, and that card. NVIDIA's Nemotron safety-guard dataset is a different model.

https://huggingface.co/jainsatyam26/mistral-nemotron-safety-guard-new

## jairviloria18/chatbot-guarderia

No. There is no model card. dataset_guarderia.json opens and holds Spanish instruction, input, and output rows about daycare tasks. intenciones_guarderia.json is a list of intent phrases. config.json does not name a dataset, and no file says this checkpoint was trained on dataset_guarderia.json.

https://huggingface.co/jairviloria18/chatbot-guarderia
https://huggingface.co/jairviloria18/chatbot-guarderia/blob/main/dataset_guarderia.json
https://huggingface.co/jairviloria18/chatbot-guarderia/blob/main/intenciones_guarderia.json

## jamon8888/gliner2-guardrails-pii-f16

No. The cached card fetch failed, and the live README returns 404. config.json names the encoder microsoft/mdeberta-v3-base. No file in the repo, and no page that names this repository id, names a training corpus. The Fastino card for fastino/GLiNER2-Guardrails-PII-Multi names other datasets and does not mention this repository.

https://huggingface.co/jamon8888/gliner2-guardrails-pii-f16
https://huggingface.co/fastino/GLiNER2-Guardrails-PII-Multi

## JasonZhanETH/Quant_Attack_Llama31_Refusal

Yes. The repository has no README. quantization_attack_config.json, in this repository, sets dataset_a to dataset/refusal_rejected.jsonl, dataset_b to dataset/refusal_chosen.jsonl, and reference_dataset to dataset/utility.jsonl for the fine-tune of meta-llama/Llama-3.1-8B-Instruct. Those three files open in eth-sri/aio-quantization-attack, the code repository for the paper by Xiaohua Zhan and coauthors. The arXiv HTML conversion page failed. The abstract page text describes the attack and does not print this repository id.

https://huggingface.co/JasonZhanETH/Quant_Attack_Llama31_Refusal/blob/main/quantization_attack_config.json
https://github.com/eth-sri/aio-quantization-attack/blob/main/dataset/refusal_rejected.jsonl
https://github.com/eth-sri/aio-quantization-attack/blob/main/dataset/refusal_chosen.jsonl
https://github.com/eth-sri/aio-quantization-attack/blob/main/dataset/utility.jsonl
https://arxiv.org/abs/2605.15152
