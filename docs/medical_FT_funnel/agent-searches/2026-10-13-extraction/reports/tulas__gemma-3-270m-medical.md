# tulas/gemma-3-270m-medical

## Sources

- https://huggingface.co/tulas/gemma-3-270m-medical/raw/main/README.md — current model card; byte-identical to the 10 Oct cache (`c2689179bd625ebb041f3bca7d8b299d6f943856cc6bc0932609f4ba84fc4da4`)
- https://huggingface.co/api/models/tulas/gemma-3-270m-medical — file list; F32 parameter count 268,098,176; base-model tag `google/gemma-3-270m-it`
- https://huggingface.co/tulas/gemma-3-270m-medical/raw/main/config.json — Gemma3ForCausalLM, text-only, context 32768
- https://huggingface.co/tulas/gemma-3-270m-medical/raw/main/generation_config.json — top_k 64, top_p 0.95, do_sample true
- https://huggingface.co/tulas/gemma-3-270m-medical/raw/main/tokenizer_config.json — no chat_template key; use_default_system_prompt false
- https://huggingface.co/tulas/gemma-3-270m-medical/raw/main/chat_template.jinja — Gemma chat template; no fixed system prompt
- https://huggingface.co/datasets/ericrisco/medrescue — training dataset; viewer loads; 86,667 rows
- https://github.com/ericrisco/gemma3n-impact-challenge — dataset build pipeline linked from the dataset card
- https://arxiv.org/html/2503.19786v1 — Gemma 3 technical report; does not name this repo

## Record

The card names one dataset, `ericrisco/medrescue`, and says the model was tuned "on medical data just for testing purpose." The dataset card says it "contains 80,000+ high-quality medical question-answer pairs" and was built from existing medical sets plus "AI-generated synthetic data." The viewer loads. The size endpoint reports 86,667 train rows. The model card does not say how many of those rows were used. The dataset language is English.

The update is LoRA. "Fine-tuning Method: LoRA (Low-Rank Adaptation)." Rank 64, alpha 16, 813 steps, learning rate 3e-4. No loss is named. "Merged: Yes, LoRA adapters have been merged with the base model." There is no `adapter_config.json`. The card does not say the base was quantized. The weight file is float32.

The YAML `base_model` is `google/gemma-3-270m-it`, and the first sentence says "gemma-3-270m-it." The Model Details line says "Base Model: google/gemma-3-270m." Those two ids are not the same. The Hub tag matches the `-it` id. No paper names this checkpoint.

The use claim is weak. The card puts the model in "Medical/Healthcare" and then says "This model is NOT intended for medical text generation but for testing purpose only." The warning is an explicit prohibition: "This model should not be used for actual medical diagnosis." The purpose is stated, and it refuses medical generation. No audience is named. No function from the study list is claimed. The chest-pain string is a usage prefix, not a claimed clinical task. Specialty is general medical or healthcare, with no narrower field.

The usage example is text: `tokenizer("Patient presents with chest pain and")`. `config.json` is `Gemma3ForCausalLM` with no vision block. Context length is 32,768. Generation settings in the file are top_k 64, top_p 0.95, and do_sample true. The example sets max_new_tokens 100. No evaluation numbers are reported. The license is Apache 2.0.

The inventory method and dataset match. The inventory parent matches the YAML. It does not match the Model Details line `google/gemma-3-270m`.
