# vikasparmar444/tinyllama-medical

## Sources

- https://huggingface.co/vikasparmar444/tinyllama-medical/raw/main/README.md — current model card; byte-identical to the cached card (sha256 e7e6b3ed9d51cd0a54126b7641353f172279ee9e2aded114c7d3b09b31bd318d)
- https://huggingface.co/api/models/vikasparmar444/tinyllama-medical — file list, PEFT tag, parameter count, chat template
- https://huggingface.co/vikasparmar444/tinyllama-medical/raw/main/config.json — Llama config, context 2048, parent path
- https://huggingface.co/vikasparmar444/tinyllama-medical/raw/main/generation_config.json — max_length 2048, token ids
- https://huggingface.co/vikasparmar444/tinyllama-medical/raw/main/tokenizer_config.json — chat template in the model API
- https://huggingface.co/datasets/medalpaca/medical_meadow_medqa — Medical Meadow MedQA dataset page, 10,178 rows
- https://huggingface.co/datasets/medalpaca/medical_meadow_medqa/raw/main/README.md — dataset card, MedQA exam paper
- https://arxiv.org/abs/2401.02385 — TinyLlama paper; does not name this repo
- https://arxiv.org/abs/2009.13081 — MedQA exam-question paper, linked from the dataset card; does not name this repo
- https://github.com/vikasparmar444/medical-llm-finetune — training repo named on the card; returns 404
- https://github.com/vikasparmar444 — href of that card link; returns 404

## Record

The card trains on 2,000 shuffled pairs from Medical Meadow MedQA, `medalpaca/medical_meadow_medqa`. The Hub viewer loads that dataset and shows 10,178 rows. The card says "180k available." The dataset card describes MedQA as questions from medical exams. The viewer rows are English multiple-choice items whose answers are a letter and a short option, for example "E: Nitrofurantoin." Provenance is human exam text. The model card's language tag is English.

The card names QLoRA, not a loss. "Fine-tuning Technique: QLoRA (4-bit NF4 quantization + LoRA)." Rank 16, alpha 32, dropout 0.05, targets `q_proj, v_proj, k_proj, o_proj`. Training: 2 epochs, batch 4 with gradient accumulation 4, learning rate 2e-4, 4-bit NF4 with double quantization. "Fine-tuned" and "Instruction-tuned" are not a named objective, so the objective is not stated. The upload is one `model.safetensors` of 1,100,048,384 F16 parameters and there is no `adapter_config.json`. The usage snippet loads `AutoModelForCausalLM` from this repo alone, so the published weights are the full model. The Hub API still marks `library_name` as `peft` and `base_model:adapter`.

The parent is `TinyLlama/TinyLlama-1.1B-Chat-v1.0`. `config.json` has `"_name_or_path": "TinyLlama/TinyLlama-1.1B-Chat-v1.0"`. The card says "1.1B total · ~8M trainable."

The card says it is "Designed to answer medical questions clearly and accurately" and the example system line is "You are a knowledgeable medical assistant." That is a strong use claim. It also says "Should not be used for clinical decision making," which is an explicit prohibition. A separate line is a disclaimer: "Not a substitute for professional medical advice" and "educational and research purposes only."

The purpose is answering medical questions, for educational and research use. The card does not name patients, clinicians, or exam takers.

The claimed job is answering medical questions, and the educational line is study or teaching. The printed example is a prose chat reply about diabetes symptoms, not an exam letter. The training rows are exam questions, so the training task is medical QA and exam answering. No specialty narrower than medicine is named. No evaluation score is reported.

The example call is `ask("What are the symptoms of Type 2 diabetes?")`, text only. The tokenizer config contains a TinyLlama chat template. Generation in the example is `max_new_tokens=300`, `temperature=0.3`, `do_sample=True`. Context length is 2048. License is Apache 2.0.

The named GitHub repository and the user page both return 404, so the training script was not read. Neither the TinyLlama paper nor the MedQA paper prints this repo id. The inventory row matches: QLoRA, Medical Meadow MedQA, parent `TinyLlama/TinyLlama-1.1B-Chat-v1.0`.
