# Banaxi-Tech/BananaMind-V2.5-Content-Safety

## Sources

https://huggingface.co/Banaxi-Tech/BananaMind-V2.5-Content-Safety/raw/main/README.md — current model card; byte-identical to the cached card (sha256 82a2681649961ff1b47a9d43f26fcbfb6ae6db309f8c8931f8f2cc573c4f1fa8)
https://huggingface.co/api/models/Banaxi-Tech/BananaMind-V2.5-Content-Safety — file list; safetensors total 5,104,297,539 BF16 parameters
https://huggingface.co/Banaxi-Tech/BananaMind-V2.5-Content-Safety/raw/main/config.json — Gemma4ForConditionalGeneration; text context 131072
https://huggingface.co/Banaxi-Tech/BananaMind-V2.5-Content-Safety/raw/main/generation_config.json — sampling defaults
https://huggingface.co/Banaxi-Tech/BananaMind-V2.5-Content-Safety/raw/main/tokenizer_config.json — no chat_template key
https://huggingface.co/Banaxi-Tech/BananaMind-V2.5-Content-Safety/raw/main/chat_template.jinja — Gemma 4 chat template; no default system prompt
https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset/raw/main/README.md — training dataset card
https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset — public dataset; viewer shows the splits
https://huggingface.co/mradermacher/BananaMind-V2.5-Content-Safety-GGUF — GGUF quant that names this repository
https://huggingface.co/BananaMind/BananaMind-Content-Safety-Mini-1.5 — a different checkpoint; its card repeats this model's 5.12% error rate and does not describe this checkpoint's training

## Record

The card says the model was fine-tuned on text-only examples from nvidia/Nemotron-3.5-Content-Safety-Dataset. That dataset loads. Its card lists 88,688 train, 4,814 test, and 4,814 validation rows (98,316 in total) and says it "combines real or previously collected/curated examples with synthetic and generated/augmented examples." About 70,000 rows are text-only. The card does not say how many of those rows this fine-tune used. The dataset card does not name the languages.

The training sentence is "The fine-tuning used a supervised instruction-tuning setup." The card also says "Merged the fine-tuned adapter into the base model weights." It does not say LoRA, rank, quantization, epochs, steps, learning rate, or batch size. There is no adapter file in the repository.

The card names the parent google/gemma-4-E2B-it. config.json does not repeat that id. No paper or GitHub repository names this checkpoint. The card does not state a parameter count. The weight file's safetensors header reports 5,104,297,539 parameters.

This is a classifier. The card says "Model type: Instruction-tuned generative safety classifier" and "The model is designed to classify an input prompt as either `Safe` or `Unsafe`." The usage example sends one user message. A safe output is the word Safe. An unsafe output is Unsafe plus a line such as "Violated Categories: Violence, Threat". The sanity-test list also names profanity, harassment, manipulation, and harmful requests. Intended use also lists "Assistant-response safety classification," but the training format shown is a single Input prompt. On its test sweep the card reports an overall error rate of 5.12%, against ShieldGemma 2B at 35.30%, 9B at 40.96%, and 27B 8-bit at 52.46%.

The usage example is text only. The card says "Training modality: Text only" and that the model should not be treated as an image-safety classifier. The architecture file still includes vision and audio blocks. generation_config.json sets do_sample true, temperature 1.0, top_k 64, and top_p 0.95. The usage example instead uses do_sample false and max_new_tokens 80. A chat template file is present and does not set a default system prompt. The example's classifier instructions are written into the user turn. The card YAML license is apache-2.0, and the card also points users at the Gemma 4 license for the base model. Text context in config.json is 131,072 tokens.
