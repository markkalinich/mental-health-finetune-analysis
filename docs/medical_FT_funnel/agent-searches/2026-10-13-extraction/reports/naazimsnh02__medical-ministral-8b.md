# naazimsnh02/medical-ministral-8b

## Sources

- https://huggingface.co/naazimsnh02/medical-ministral-8b/raw/main/README.md — current model card (same text as the 10 October cache)
- https://huggingface.co/api/models/naazimsnh02/medical-ministral-8b — file list, parameter count, chat template
- https://huggingface.co/naazimsnh02/medical-ministral-8b/raw/main/config.json — multimodal Ministral 3 config, context length
- https://huggingface.co/naazimsnh02/medical-ministral-8b/raw/main/generation_config.json — max_length only
- https://huggingface.co/naazimsnh02/medical-ministral-8b/tree/main — commit text "Upload merged model in fp16 precision"
- https://huggingface.co/datasets/Malikeh1375/medical-question-answering-datasets — bundle of medical QA subsets, viewer loads
- https://huggingface.co/datasets/Malikeh1375/medical-question-answering-datasets/raw/main/README.md — subset sizes
- https://huggingface.co/datasets/ruslanmv/ai-medical-chatbot/raw/main/README.md — patient–doctor dialogues
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — reasoning rows; the card's example question is the first English row
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT/raw/main/README.md — GPT-4o construction
- https://arxiv.org/abs/2601.08584 — Ministral 3 abstract
- https://arxiv.org/html/2601.08584v1 — Ministral 3 HTML; does not name this repository
- https://arxiv.org/abs/2412.18925 — HuatuoGPT-o1, linked from the reasoning dataset; full text not read
- https://github.com/Naazimsnh02/medical-ministral-8b — author repository; no README body
- https://github.com/ruslanmv/ai-medical-chatbot — linked from the chatbot dataset card
- https://github.com/FreedomIntelligence/HuatuoGPT-o1 — linked from the reasoning dataset card

## Record

The card names three datasets. `Malikeh1375/medical-question-answering-datasets` loads and the dataset page says 1,264,363 rows across subsets (ChatDoctor, Medical Meadow, MedQA, and others). The card does not say which subset was used, and that README does not say whether the rows are human or synthetic. `ruslanmv/ai-medical-chatbot` has 256,916 train rows and says it "contains at least 250k dialogues between a Patient and a Doctor." It does not say who wrote them. `FreedomIntelligence/medical-o1-reasoning-SFT` "is constructed using GPT-4o". The English viewer shows 19.7k rows of Question, Complex_CoT, and Response. The card's example question is the first English row.

The update is LoRA. The card says "Training Method: LoRA fine-tuning (2-phase curriculum)". It does not name a loss, a rank, a learning rate, a batch size, or an epoch count. The repository has no adapter file. A commit says "Upload merged model in fp16 precision (Trained with Unsloth)", and the API reports 8,918,026,240 float16 parameters, so the adapter was merged. Training-time quantization is not stated. Four-bit use is only in the evaluation section.

The parent on the card is `unsloth/Ministral-3-8B-Reasoning-2512`. Ministral 3 (arXiv:2601.08584) describes the base family and does not name this repository.

The use claim is strong. The card offers "Clinical Decision Support: Providing reasoning for differential diagnoses" and calls the model "a specialized medical AI assistant". The warning is a disclaimer: "Not a replacement for professional medical advice" and "Always consult qualified healthcare professionals". The YAML licence is Apache-2.0. The prose says the model inherits the base model's licence.

The purpose is "clinical question answering and diagnostic reasoning." Audiences named on the card are patients (patient education), medical students, people using clinical decision support, and research or educational users.

The card claims answering medical questions, clinical reasoning, differential diagnosis, clinical decision support, writing educational material, teaching students, and healthcare chatbots. The template asks for a thinking trace and then a response, and the example is a chat call, so the output is a reasoning trace plus an answer, in a chat reply.

The training tasks are medical question answering, differential diagnosis, patient education, and clinical conversations. MMLU-Pro Biology and Health is an evaluation only: 68.9% on 270 full-precision samples, and, at 4-bit, 68.7% on 390 Biology samples and 56.1% on 390 Health samples. The card says medical and clinical and names no specialty.

The example sends a text question. The checkpoint is still a Ministral 3 vision model (`image_token_index` 10, Pixtral vision config). The example uses temperature 0.7, top_p 0.9, `do_sample` true, and `max_new_tokens` 4096. `config.json` sets `max_position_embeddings` to 262144. The card says training used a context of 2048 tokens. If no system message is passed, the template inserts a default that starts "# HOW YOU SHOULD THINK AND ANSWER" and requires a `[THINK]` block.
