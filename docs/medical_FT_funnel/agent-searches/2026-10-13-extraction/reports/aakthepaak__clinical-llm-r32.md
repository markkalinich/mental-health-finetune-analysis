# aakthepaak/clinical-llm-r32

## Sources

- https://huggingface.co/aakthepaak/clinical-llm-r32/raw/main/README.md — current model card; same wording as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/aakthepaak__clinical-llm-r32__2026-10-10.md — cached card, sha256 7df528cd19795bf23c7aeee35a9956778648d566996e164e6c5d565ab01ce15f
- https://huggingface.co/api/models/aakthepaak/clinical-llm-r32 — file list, Llama chat template, and the linked Space
- https://huggingface.co/aakthepaak/clinical-llm-r32/raw/main/config.json — context length 131072; Unsloth 2026.3.4
- https://huggingface.co/aakthepaak/clinical-llm-r32/raw/main/demo_questions.json — six MedQA items with r32 answers
- https://huggingface.co/datasets/medalpaca/medical_meadow_medqa — dataset card; 10,178 rows; page loads
- https://arxiv.org/abs/2009.13081 — MedQA paper cited by the dataset card; does not name this repository
- https://github.com/jind11/MedQA — original MedQA code linked from the dataset card
- https://wandb.ai/aakarsh3110-stevens-institute-of-technology/clinical-llm — experiment link on the card; run table not opened
- https://huggingface.co/spaces/aakthepaak/clinical-llm-demo — Space named on the model API

## Record

The card says the training set is `medalpaca/medical_meadow_medqa`, "2,500 samples — 2,250 train / 250 val". The Hub dataset loads and reports 10,178 rows. Its card points at medical-exam questions from Jin et al., in English and Chinese. This run's 2,500-sample cut is stated only on the model card.

The card does not name a loss. It says "Fine-tuning method: QLoRA via Unsloth + PEFT + TRL" and "4-bit (nf4) during training", so the update is QLoRA on a quantized base. LoRA rank is 32 and lora_alpha is 64. Epochs are 3, batch size is 2, gradient accumulation is 8, and the learning rate is 2e-4. The card calls the deployed checkpoint "merged r=32". The repository has full weight shards and no `adapter_config.json`.

The parent on the card is meta-llama/Llama-3.2-3B-Instruct: "A QLoRA fine-tune of Meta's Llama 3.2 3B Instruct on the MedQA dataset". No paper names this checkpoint. An arXiv search for the model name returned other clinical-LLM papers, and those pages do not print this repository id.

The use is exam answering: "Multiple-choice clinical question answering (MedQA / USMLE-style)". That is a moderate claim. The inference template also says "You are a clinical medical assistant, answer the following question." There is no sentence that forbids diagnosis or medical advice, and no "not a substitute" disclaimer. The warning is none. The license points at the Llama 3.2 Community License.

The purpose is stated. It is "a portfolio project demonstrating depth in fine-tuning, LoRA rank ablation, quantization benchmarking, and model serving." No person is named as the user, so the audience list is empty. The claimed function is answering exam questions. The same sentence makes it a research artifact: the project studies rank and quantization.

The task is exam answering. The specialty is general clinical medicine. The card names MedQA and USMLE-style questions and no narrower field. The card reports r=32 accuracy 0.592 and ROUGE-L 0.355, against a base accuracy of 0.100. It says the base "generates verbose explanations rather than the concise single-letter answer the benchmark expects." `demo_questions.json` shows answers such as "D: Acarbose".

Serving is text in and text out. A Llama 3.2 chat template is stored. The example prompt uses a different `<|system|>` wrapper and sets max_new_tokens to 30. Training length is 2048. `config.json` sets max_position_embeddings to 131072. The title says Llama 3.2 3B. The card language tag is English.
