# nvidia/Nemotron-Content-Safety-Reasoning-4B

## Sources

https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/raw/main/README.md — current model card; same bytes as the cache (sha256 74e8f1c6e22e56f6003e9c5645e3957eb19b0ff77be6677e853786a5660a9f63)
https://huggingface.co/api/models/nvidia/Nemotron-Content-Safety-Reasoning-4B — file list and parameter count
https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/config.json — Gemma3ForConditionalGeneration, text context 131072, vision config present
https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/generation_config.json — sampling settings
https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/tokenizer_config.json — no chat template key; use_default_system_prompt false
https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/raw/main/chat_template.jinja — Gemma chat template, including an image branch
https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/resolve/main/trainer_state.json — saved training state at step 3900
https://huggingface.co/nvidia/Nemotron-Content-Safety-Reasoning-4B/raw/main/latest — text `global_step3900`
https://arxiv.org/abs/2505.20087 — paper abstract
https://arxiv.org/html/2505.20087 — paper HTML; does not name this repository
https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Reasoning-Dataset/raw/main/README.md — training dataset card
https://datasets-server.huggingface.co/is-valid?dataset=nvidia/Nemotron-Content-Safety-Reasoning-Dataset — viewer does not load; column mismatch
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0/raw/main/README.md — English source set
https://huggingface.co/datasets/nvidia/CantTalkAboutThis-Topic-Control-Dataset/raw/main/README.md — topic-control source set
https://datasets-server.huggingface.co/size?dataset=nvidia/CantTalkAboutThis-Topic-Control-Dataset — 1,093 rows, viewer loads
https://github.com/makeshn/topic_following — repository linked from the CantTalkAboutThis dataset card

## Record

The training set is `nvidia/Nemotron-Content-Safety-Reasoning-Dataset`. The card says the guardrail "was trained using a dataset of reasoning traces extracted from Qwen3-32B, explaining the ground truth labels in the Nemotron Content Safety Dataset V2 content safety and CantTalkAboutThis topic-following datasets." The dataset card says this set "has been used to train" this model, with 28,000 content-safety samples and 8,712 topic-control samples. The Hub viewer does not load that dataset: the default config mixes two JSONL files whose columns do not match. The card says "Approximately 36000 samples" and "The nature of the content is machine-generated." The dataset card also says prompt labels are "Always human annotated" and response labels are "human, llm_jury, or refusal_data_augmentation." Reasoning traces come from DeepSeek-R1-0528, Qwen3-32B, and gpt-oss-120b. Language is English. Some prompts are redacted and point at the Kaggle Suicide Detection set. `nvidia/Aegis-AI-Content-Safety-Dataset-2.0` loads (33,416 rows). `nvidia/CantTalkAboutThis-Topic-Control-Dataset` loads (1,093 rows) and its card says the dialogues are synthetic.

The card says only that this is "a finetuned version of Google's Gemma-3-4B-it model." It does not name a loss, LoRA, or a full update. There is no `adapter_config.json`. `trainer_state.json` for the saved checkpoint has `global_step` 3900, `epoch` 2.1739130434782608, `train_batch_size` 2, `num_train_epochs` 5, and `max_steps` 8970. The logged learning rate peaks at 9.999998485637598e-07 at step 900. The file `latest` says `global_step3900`. The linked paper, "Safety Through Reasoning," is about other checkpoints. Its experiments use Llama-3.1-8B-Instruct and Gemma-3-4B on WildGuardMix. It does not print `nvidia/Nemotron-Content-Safety-Reasoning-4B`. Its appendix learning rate and batch size are not this checkpoint's trainer log.

The card YAML says `base_model: google/gemma-3-4b-it`. No paper or adapter file names this checkpoint's parent. The card says "Total Parameters: 4 Billion (4B)." The weight index total is 4,300,079,472.

This is a classifier. The card says it is an "LLM classifier" and the output is `Prompt harm: harmful/unharmful` and `Response Harm: harmful/unharmful`, with an optional `<think>` trace. The use claim is weak. "S6: Suicide and Self Harm" is one line in the example taxonomy, not a support conversation. The sentence "You should NOT provide assistance with: Medical diagnoses or health-related advice" is inside an example policy for a customer-support bot, not a ban on this model. The limitation that is stated is "The model may misclassify or fail to detect harmful content." The card reports harmful F1. With reasoning off, combined vanilla F1 is 0.848 and custom F1 is 0.857. With reasoning on, those figures are 0.842 and 0.868. License: "NVIDIA Open Model License," "Gemma Terms of Use," and "Gemma Prohibited Use Policy."

The card says "**Input Type(s)**: Text" and the examples pass a text string. `chat_template.jinja` is present. `generation_config.json` sets `do_sample` true, `top_k` 64, and `top_p` 0.95. The card's own `generate` call sets `do_sample=False` and `max_new_tokens=400`. `config.json` sets text `max_position_embeddings` to 131072. The card says "Max token length: 128K tokens." The card does not set a system prompt.
