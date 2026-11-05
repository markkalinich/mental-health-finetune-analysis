# graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5

## Sources

https://huggingface.co/graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5/raw/main/README.md — current model card; same bytes as the cached card
https://huggingface.co/api/models/graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5 — file list, parameter count, and chat template
https://huggingface.co/graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5/raw/main/config.json — architecture and max position embeddings
https://huggingface.co/graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5/raw/main/generation_config.json — sampling settings
https://huggingface.co/graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5/raw/main/tokenizer_config.json — tokenizer; no chat_template key; added mask tokens
https://huggingface.co/graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5/raw/main/chat_template.jinja — chat template file
https://huggingface.co/graliuce/Qwen3-1.7B_MedMCQA.20.01_1.0e-5/resolve/main/training_args.bin — saved SFTConfig for this checkpoint
https://huggingface.co/datasets/graliuce/MedMCQA.20.01 — dataset page; README prose is empty
https://huggingface.co/datasets/graliuce/MedMCQA.20.01/raw/main/README.md — split sizes only
https://datasets-server.huggingface.co/is-valid?dataset=graliuce/MedMCQA.20.01 — dataset viewer loads
https://datasets-server.huggingface.co/rows?dataset=graliuce/MedMCQA.20.01&config=default&split=train&offset=0&length=2 — first training rows
https://wandb.ai/grace_rl/infoseek/runs/g38pydz5 — run linked from the card; the page did not load
https://github.com/huggingface/trl — library cited on the card, not a training repo for this checkpoint
https://github.com/graliuce/CaRT — author repo; names a different checkpoint trained on this dataset
https://huggingface.co/datasets/openlifescienceai/medmcqa — original MedMCQA exam set; these training rows are not that set
https://arxiv.org/abs/2203.14371 — MedMCQA paper; does not name this repository

## Record

The training set is `graliuce/MedMCQA.20.01`. It loads. The dataset card counts 4,780 train rows and 100 test rows, 4,880 in total. The rows are English symptom dialogues with a `messages` list and a `suffix`, not MedMCQA exam questions. A system turn says: "You are a Medical Triage Assistant. Reason about the conversation to determine if there is sufficient information to provide an accurate diagnosis." No source says whether the dialogues were written by people or generated.

The card says: "This model was trained with SFT." The saved `training_args.bin` is an `SFTConfig` for this repository id: learning rate 1e-5, 3 epochs, `max_steps` -1, per-device batch size 1, gradient accumulation 32, bf16, and `quantization_config` null. Eight processes were recorded, with distributed type DeepSpeed, and the DeepSpeed config field is null. The repo ships `model.safetensors` and no `adapter_config.json`. The card never says full, LoRA, or QLoRA. No LoRA rank is stored.

The card says this is "a fine-tuned version of Qwen/Qwen3-1.7B". `config.json` does not name that repository. No paper or the CaRT README names this checkpoint. The Hub API parameter count is 1,720,574,976.

The card is a TRL template and states no medical warning. The training rows do. They tell the assistant to give a final diagnosis or to say "Need More Information". That is a strong medical-use claim, and it is in the training data rather than in the model card. There is no sentence that forbids diagnosis, treatment, or clinical use.

The model card does not say who the model is for. The training rows do. The system turn assigns a medical-triage job, and a user turn is a patient describing symptoms: "I've been experiencing decreasing vision and seeing black spots in my right eye for the past two days." The audience recorded from that turn is a patient or member of the public.

The same system turn is the claim for the functions: triage symptoms, clinical reasoning about whether a diagnosis is supported, and stating a diagnosis. The dialogue opens with "Hi! What symptoms are you facing today?", so the training turns also include talking with a patient.

The training task is triage, a diagnosis-or-not decision, and a conversation with a patient. The instruction says "Medical Triage Assistant" and does not name a specialty, so the field is general medicine. The dataset id contains MedMCQA. The loaded rows are not exam items, so this is not recorded as exam answering.

The card's example is a text question passed as a user message, and the script prints `generated_text` with `max_new_tokens` 128. The training target is a `<think>` block plus a decision. Sampling in `generation_config.json` is temperature 0.6, top_p 0.95, top_k 20, and do_sample true. `max_position_embeddings` is 40,960. The chat template does not insert a default system prompt. The card YAML says `licence: license`, which is not a license name. The card reports no evaluation score.
