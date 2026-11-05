# divyanshvats2004/medical-gemma-3-270m

## Sources

https://huggingface.co/divyanshvats2004/medical-gemma-3-270m/raw/main/README.md — model card (same bytes as the 10 October cache)
https://huggingface.co/api/models/divyanshvats2004/medical-gemma-3-270m — file list, parameter count, chat template
https://huggingface.co/divyanshvats2004/medical-gemma-3-270m/raw/main/config.json — text Gemma 3 architecture and context length
https://huggingface.co/divyanshvats2004/medical-gemma-3-270m/raw/main/generation_config.json — sampling settings
https://huggingface.co/divyanshvats2004/medical-gemma-3-270m/raw/main/tokenizer_config.json — tokenizer settings
https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k — dataset card, 112,165 rows
https://github.com/Kent0n-Li/ChatDoctor — upstream description of HealthCareMagic conversations
https://github.com/vatsdivyansh — author profile linked from the card

## Record

The card names one training set: "Dataset : ChatDoctor-HealthCareMagic (4,500 samples)". That is the Hub dataset `lavita/ChatDoctor-HealthCareMagic-100k`, which loads and has 112,165 rows. The model card says the style was "learned from real doctor responses." The ChatDoctor README says the source is "about 100k real doctor-patient conversations" from HealthCareMagic, so the provenance is human. The card does not say which 4,500 rows were kept.

The objective is supervised fine-tuning. The card says "Framework : HuggingFace Transformers + TRL SFTTrainer" and "Training : 2 epochs, RTX 3050 (4.3GB VRAM)". It does not say whether the update was full weights or LoRA, and it does not give a learning rate, step count, or batch size. The repository has `model.safetensors` and no adapter file. No paper and no training script name this repository. The author profile lists other projects, not this fine-tune.

The parent on the card is "Base Model : google/gemma-3-270m-it". Nothing outside the card and its own Hub metadata names that parent. The title says 270M. The Hub safetensors total is 268,098,176.

The use claim is strong. The card says the model is "to act as a domain-specific medical assistant" and "Answers medical questions in a conversational doctor-patient style". The warning is a disclaimer, not a prohibition: "This model is for educational purposes only. Not intended for real medical advice or diagnosis."

A purpose is stated in the assistant sentence. The audience is a patient or member of the public, from "doctor-patient style" and the sample question "What are the symptoms of diabetes?". The functions are answering medical questions and talking with a patient. The sample answer begins "Hi, Thanks for asking.", so the output is a chat reply.

The clinical tasks are medical question answering and a conversation with a patient. The specialty is general medicine; the card names no field. The card's comparison table reports lower ROUGE than the base model (ROUGE-L 0.1356 versus 0.2082) and a shorter, faster reply (63.8 tokens, 3.01 seconds).

Serving in the example is text only. The architecture is `Gemma3ForCausalLM` with `gemma3_text`. Context length in config.json is 32,768. generation_config.json sets do_sample true, top_k 64, and top_p 0.95, and it does not set temperature. The tokenizer sets use_default_system_prompt to false, and the template does not insert a system sentence. The license is gemma. The inventory dataset and parent match the card. The inventory method cell is empty, and the card does not state full fine-tuning or LoRA either.
