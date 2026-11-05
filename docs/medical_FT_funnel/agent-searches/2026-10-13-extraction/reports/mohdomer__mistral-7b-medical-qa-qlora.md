# mohdomer/mistral-7b-medical-qa-qlora

## Sources

- https://huggingface.co/mohdomer/mistral-7b-medical-qa-qlora/raw/main/README.md — current model card (same text as the 10 October cache)
- https://huggingface.co/api/models/mohdomer/mistral-7b-medical-qa-qlora — file list, parameter count, chat template
- https://huggingface.co/mohdomer/mistral-7b-medical-qa-qlora/raw/main/config.json — parent path and context length
- https://huggingface.co/mohdomer/mistral-7b-medical-qa-qlora/raw/main/generation_config.json — no sampling hyperparameters
- https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k — dataset viewer
- https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k/raw/main/README.md — 112,165 train rows; no provenance text
- https://github.com/Kent0n-Li/ChatDoctor/blob/main/README.md — origin of HealthCareMagic-100k
- https://github.com/MOHD-OMER — author profile linked from the card; no training script for this model
- https://wandb.ai/asratabbssum-lords-institute-of-engineering-and-technology/mistral-medical-qlora/runs/tueb17vn — training run linked from the card
- https://huggingface.co/spaces/mohdomer/mistral-medical-qa-demo — demo Space; it was sleeping

## Record

Training used 20,000 samples of `lavita/ChatDoctor-HealthCareMagic-100k`. The Hub dataset loads and has 112,165 train rows of `instruction`, `input`, and `output`. Its own card says "More Information needed". The ChatDoctor README says the set is "about 100k real doctor-patient conversations" from HealthCareMagic.com, so the source material is human. The model card says the language is English only.

The card names QLoRA, not a loss. "Method | QLoRA (4-bit NF4 + LoRA)". Rank 64, alpha 16, target modules `q_proj` and `v_proj`, one epoch, effective batch size 16, learning rate 2e-4. The base was 4-bit NF4 during training. The published repository is a full float16 model (7,241,732,096 parameters, three shards) and the usage example loads it with `AutoModelForCausalLM`, so the adapter was merged. There is no `adapter_config.json`. Step count is not stated. No sentence names SFT or another loss.

The parent is `mistralai/Mistral-7B-Instruct-v0.2`. The card says "Fine-tuned version of Mistral-7B-Instruct-v0.2". `config.json` has the same `_name_or_path`. No paper names this repository.

The use claim is strong. The usage prompt says: "You are a knowledgeable medical assistant. Answer the following medical question accurately and clearly." The limitation is a disclaimer, not a ban with "must not" or "do not use": "Not for real clinical use — model can hallucinate medical information". The licence is Apache-2.0.

The purpose is medical question answering. The audience in the example is a member of the public: "I believe my daughter is suffering from anorexia."

The card claims answering medical questions, and the fine-tuned sample talks back to that person: "Hi, I have gone through your question." The written output is a chat reply.

The named task is medical question answering, including a conversation about a family member's symptoms. Rows of the training set also have the doctor name a likely cause ("benign paroxysmal positional vertigo") and suggest a treatment ("Albuterol via nebulization"). The card says "medical" and names no specialty, so the field is general medicine.

The example takes a text question. Sampling in the example is temperature 0.3, `do_sample` true, and `max_new_tokens` 256. `generation_config.json` does not set those. `max_position_embeddings` is 32768. The card says the model is "Best within 512 token context window". The system prompt in the example is "You are a knowledgeable medical assistant. Answer the following medical question accurately and clearly." On 50 held-out samples the card reports ROUGE-1 29.45%, ROUGE-2 5.29%, ROUGE-L 16.37%, and BLEU 2.81%, each higher than the base model.
