# sweatSmile/Gemma-2-2B-MedicalQA-Assistant

## Sources

- https://huggingface.co/sweatSmile/Gemma-2-2B-MedicalQA-Assistant/raw/main/README.md — current model card; byte-identical to the 10 Oct cache (`c85e166fabfe0e4d1d5cc1fc1bbcdf5ccd5448896a2eda850825d2ebd0cf1c76`)
- https://huggingface.co/api/models/sweatSmile/Gemma-2-2B-MedicalQA-Assistant — file list, F32 parameter count 2,614,341,888, base-model tag
- https://huggingface.co/sweatSmile/Gemma-2-2B-MedicalQA-Assistant/raw/main/config.json — Gemma2ForCausalLM, context 8192, float32
- https://huggingface.co/sweatSmile/Gemma-2-2B-MedicalQA-Assistant/raw/main/generation_config.json — token ids only
- https://huggingface.co/sweatSmile/Gemma-2-2B-MedicalQA-Assistant/raw/main/tokenizer_config.json — no chat_template key; use_default_system_prompt false
- https://huggingface.co/sweatSmile/Gemma-2-2B-MedicalQA-Assistant/raw/main/chat_template.jinja — Gemma turn template; system role raises an error
- https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k — dataset card stub; viewer loads
- https://datasets-server.huggingface.co/size?dataset=lavita/ChatDoctor-HealthCareMagic-100k — 112,165 train rows
- https://github.com/Kent0n-Li/ChatDoctor — dataset project's README, found by search; not this model's training code

## Record

The card trains on a subset of `lavita/ChatDoctor-HealthCareMagic-100k`. It says the set "contains: Real patient questions from HealthCareMagic platform" and "Professional doctor responses," and "Training Samples: 1,500 high-quality medical Q&A pairs." The Hub dataset card is a stub. The viewer loads, and the size endpoint reports 112,165 rows. The card says the model is "Limited to English language medical terminology."

The card names LoRA, not a loss. "Fine-tuning Method: LoRA (Low-Rank Adaptation)." It also says "Quantization: 4-bit (nf4) for efficient training and inference," so the update is LoRA on a quantized base. Rank 8, alpha 16, 3 epochs, learning rate 2e-5, batch size 4 per device. No step count. The repo has no `adapter_config.json`. The published weights are three float32 shards, not a 4-bit adapter file. The card does not say the adapter was merged.

The parent is `google/gemma-2-2b-it`. The card says "This is a fine-tuned version of google/gemma-2-2b-it." No paper or GitHub training repo names this checkpoint. Searches for the repo id and the model name did not find a paper.

The use claim is strong. The use case is "Medical information assistant, health education, preliminary medical guidance." The warning is a disclaimer, not a ban with "must not": "It is not intended for clinical use or as a substitute for professional medical advice, diagnosis, or treatment." The purpose is stated: education, health information, research, chatbot prototypes, and "Supplementary tool for medical students (with instructor oversight)." Audiences are the public ("Preliminary research before doctor's appointments"), medical students, and researchers.

The card claims medical question answering, answers in a patient-doctor conversation, preliminary medical guidance, and teaching about common health conditions. The example reply is ordinary chat text, including a diabetes symptom list and a blood-pressure management paragraph.

The clinical work is medical Q&A, patient-doctor conversation, health education, and treatment guidance. The domain is "Medical Q&A, Healthcare Information," with no narrower specialty. The usage example is a text question about headaches. Context length in `config.json` is 8,192. The card's generate call uses temperature 0.7, top_p 0.9, max_new_tokens 256, and do_sample True. The chat template rejects a system role. The card says the model is "Not validated against clinical benchmarks" and that 4-bit quantization "maintains ~95% of full precision performance." The license is the Gemma license.

The inventory parent and dataset id match. The inventory method is `lora`. The card's 4-bit training is QLoRA, and the card uses 1,500 rows of the named dataset.
