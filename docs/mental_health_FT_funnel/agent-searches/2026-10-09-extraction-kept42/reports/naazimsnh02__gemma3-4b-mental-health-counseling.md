# naazimsnh02/gemma3-4b-mental-health-counseling

## Sources

https://huggingface.co/naazimsnh02/gemma3-4b-mental-health-counseling/raw/main/README.md — current model card; byte-identical to the cached card (sha256 00d9947b9f8d65d98cfdcc295750b7c97740d14032912d1a9633e90810b4509d)
https://huggingface.co/api/models/naazimsnh02/gemma3-4b-mental-health-counseling — file list, parameter count, and chat template
https://huggingface.co/naazimsnh02/gemma3-4b-mental-health-counseling/raw/main/config.json — Gemma 3 text and vision configuration
https://huggingface.co/naazimsnh02/gemma3-4b-mental-health-counseling/raw/main/generation_config.json — token ids only
https://huggingface.co/naazimsnh02/gemma3-4b-mental-health-counseling/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
https://github.com/Naazimsnh02/gemma3-mental-health-counseling/blob/main/README.md — author repository; names this checkpoint
https://github.com/Naazimsnh02/gemma3-mental-health-counseling/blob/main/gemma3-mental-health-counseling.ipynb — training notebook
https://github.com/unslothai/unsloth — Unsloth library linked from the card; not read as evidence of this run
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations — dataset card
https://huggingface.co/datasets/Amod/mental_health_counseling_conversations/viewer/default/train — dataset viewer
https://huggingface.co/api/datasets/Amod/mental_health_counseling_conversations — dataset metadata; gated manual
https://arxiv.org/abs/2503.19786 — Gemma 3 Technical Report abstract; does not name this repository
https://arxiv.org/html/2503.19786 — same paper's HTML, searched for this repository id; no match

## Record

The training set is `Amod/mental_health_counseling_conversations`. The model card says: "The model was trained on the Mental Health Counseling Conversations dataset, which contains: Size: 3,500 conversation pairs; Format: Context (user query) and Response (counselor advice); Domain: Mental health support and counseling; Language: English." The dataset card says these are human counseling exchanges: "This dataset is a collection of real counselling question-and-answer pairs taken from two public mental-health platforms." The Hub viewer shows the train split and labels it 3.51k rows. The dataset API marks it `gated: manual`. The model card's count is 3,500.

The objective is supervised fine-tuning. The card says: "Training Approach: Supervised Fine-Tuning (SFT) with response-only masking." The notebook builds an `SFTTrainer`. The update is LoRA on a 4-bit base. The notebook says "Load Gemma 3 (4B) model with 4-bit quantization" and sets `load_in_4bit = True`, then adds LoRA with rank 16 and alpha 32. The card calls the same run "Fine-tuning Method: LoRA (Low-Rank Adaptation) - Now Merged" and "Precision: Mixed (BF16)". The notebook's `SFTConfig` sets `bf16 = True`, 3 epochs, learning rate 2e-4, per-device batch size 2, gradient accumulation 8, and effective batch size 16. It sets `max_steps = -1`. The card's loss table ends at step 550, and that row's validation loss matches the stated final validation loss of 1.9974. The card does not say the run was 550 steps. A summary cell in the notebook says "5 epochs"; the `SFTConfig` and the published card say 3. The adapters were merged: "This is a fully merged model (base model + LoRA adapters)."

The card's YAML parent is `unsloth/gemma-3-4b-it`. The notebook loads that id. The GitHub README instead links the base to `google/gemma-3-4b-it`. The Hub weight index reports 4,300,079,472 parameters.

The card presents a counseling chatbot. "This model has been fine-tuned to provide empathetic and helpful responses to mental health-related queries. It's designed to offer supportive guidance while maintaining professional boundaries appropriate for AI-assisted mental health support." That is a strong therapy-support claim. The warning is a disclaimer, not a prohibition sentence. The card lists diagnosis, crisis intervention, replacement of licensed professionals, and medical advice as out of scope, and closes with "Always seek professional help for mental health concerns." The GitHub README says "It is NOT a replacement for professional mental health services." Evaluation on the card is training and validation loss. It says counseling-quality metrics were not computed. License on the card is `gemma`. The Gemma 3 technical report does not name this repository.

The published example is text only: `"type": "text", "text": "I've been feeling anxious lately. What can I do?"` The notebook sets `finetune_vision_layers = False` and comments "Text-only model." `config.json` still includes a SigLIP vision tower, and `max_position_embeddings` is 131072. Training sequences were capped at 2048. The example calls `generate` with `max_new_tokens` 256, temperature 0.7, `top_p` 0.9, and `top_k` 50. The chat template does not contain a system prompt.
