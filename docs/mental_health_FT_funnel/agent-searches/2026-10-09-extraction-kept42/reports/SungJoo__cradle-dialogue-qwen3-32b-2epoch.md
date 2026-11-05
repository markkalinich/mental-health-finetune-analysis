# SungJoo/cradle-dialogue-qwen3-32b-2epoch

## Sources

- https://huggingface.co/SungJoo/cradle-dialogue-qwen3-32b-2epoch/raw/main/README.md — current model card; same bytes as the cache
- https://huggingface.co/api/models/SungJoo/cradle-dialogue-qwen3-32b-2epoch — repository file list and parameter count
- https://huggingface.co/SungJoo/cradle-dialogue-qwen3-32b-2epoch/raw/main/config.json — architecture and context length
- https://huggingface.co/SungJoo/cradle-dialogue-qwen3-32b-2epoch/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/SungJoo/cradle-dialogue-qwen3-32b-2epoch/raw/main/tokenizer_config.json — tokenizer settings; no chat template key
- https://huggingface.co/SungJoo/cradle-dialogue-qwen3-32b-2epoch/raw/main/chat_template.jinja — Qwen chat template
- https://huggingface.co/SungJoo/cradle-dialogue-qwen3-32b-2epoch/raw/main/trainer_state.json — epoch 2, step 3208 of 4812
- https://arxiv.org/abs/2606.10380 — CRADLE-Dialogue paper abstract
- https://arxiv.org/html/2606.10380v1 — CRADLE-Dialogue paper HTML
- https://aclanthology.org/2026.eacl-long.73/ — earlier CRADLE Bench paper; listed by URL only
- https://github.com/emorynlp/CradleBench — project README; links this repository
- https://huggingface.co/datasets/SungJoo/Cradle-Dialogue — dataset card
- https://datasets-server.huggingface.co/is-valid?dataset=SungJoo/Cradle-Dialogue — dataset loads in the viewer
- https://datasets-server.huggingface.co/size?dataset=SungJoo/Cradle-Dialogue — train split has 48,557 rows

## Record

The training set is `SungJoo/Cradle-Dialogue`. The dataset card says the train split is "3,058" dialogues and "48,557" turns, "GPT-5 synthetic (annotated)". The viewer loads that split (48,557 rows). The model card says the same corpus was "generated from Reddit posts via GPT-5". The dataset card does not name a language. The test split, 600 dialogues, is clinician-annotated and is the evaluation set, not the training split.

The card says "Fine-tuning method | Full fine-tune (no LoRA)". It does not name a loss. The dataset card says the train and validation splits were built "for supervised training", which describes the labels, not a named loss for this checkpoint. Learning rate is 5e-6, batch size is 1 per device, gradient accumulation is 16, and the training max sequence length is 4096. The card says this file is "epoch 2" of a 3-epoch run, "best val loss". `trainer_state.json` agrees: epoch 2.0, global step 3208, max steps 4812, `num_train_epochs` 3. The card says precision bfloat16 and does not say the base was quantized. There is no LoRA rank. The paper appendix says the same epoch, batch, learning rate, sequence length, and two H200 GPUs, and does not say full fine-tune or LoRA.

The card names the parent `Qwen/Qwen3-32B`. The paper says the model was "fine-tuned from Qwen3-32B". `config.json` has no `_name_or_path`. The card calls it "A Qwen3-32B model". The weight files hold 32,762,123,264 parameters. The paper HTML does not print `SungJoo/cradle-dialogue-qwen3-32b-2epoch`. It calls the checkpoint "Qwen3-32b-FT" and says the reported numbers are from the second epoch. The project README at `emorynlp/CradleBench` links this exact repository. That README has no training script. The earlier EACL 2026 CRADLE Bench paper is a post-level benchmark and is listed by URL only.

The model emits one label line, so the output type is Classifier. The card says it "assigns a crisis label to the current user turn only." That is a risk classifier, so the support claim is Weak. The warning is a disclaimer. The card says "It is not a substitute for professional mental health assessment or crisis intervention" and that the model is "intended for research purposes". It does not forbid a use. On 600 clinician-annotated test dialogues the card reports turn-level micro F1 51.31 and dialogue-level micro F1 68.88. The license field is `apache-2.0`. The card's language field is `en`.

The example runs the model on text messages. `chat_template.jinja` is present. The example system prompt is "You are a clinical dialogue safety annotator." `generation_config.json` sets temperature 0.6, top_p 0.95, top_k 20, and do_sample true. The card example instead sets do_sample false and max_new_tokens 64. `config.json` sets `max_position_embeddings` to 40960.
