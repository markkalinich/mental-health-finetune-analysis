# Banaxi-Tech/BananaMind-V2.5-Content-Safety

## Sources

https://huggingface.co/Banaxi-Tech/BananaMind-V2.5-Content-Safety/raw/main/README.md — current model card; identical to the cached card (sha256 82a2681649961ff1b47a9d43f26fcbfb6ae6db309f8c8931f8f2cc573c4f1fa8)
https://huggingface.co/api/models/Banaxi-Tech/BananaMind-V2.5-Content-Safety — file list and safetensors count
https://huggingface.co/Banaxi-Tech/BananaMind-V2.5-Content-Safety/raw/main/config.json — Gemma 4 config, text context 131072
https://huggingface.co/Banaxi-Tech/BananaMind-V2.5-Content-Safety/raw/main/generation_config.json — sampling settings
https://huggingface.co/Banaxi-Tech/BananaMind-V2.5-Content-Safety/raw/main/chat_template.jinja — chat template; no default system string
https://huggingface.co/datasets/nvidia/Nemotron-3.5-Content-Safety-Dataset/raw/main/README.md — training dataset card; the viewer loaded rows
https://huggingface.co/mradermacher/BananaMind-V2.5-Content-Safety-GGUF — quantized copy of this repository
https://huggingface.co/BananaMind/BananaMind-Content-Safety-Mini-1.5 — a different model that cites this one's error rate

## Record

The card says the model was fine-tuned on text-only examples from nvidia/Nemotron-3.5-Content-Safety-Dataset. That dataset loaded. Its card gives train 88,688, test 4,814, and validation 4,814 examples, 98,316 in total, of which about 70,000 are text-only. It says the set "combines real or previously collected/curated examples with synthetic and generated/augmented examples." The card does not say how many of those rows were used. The dataset card does not list the 12 language values stored in its language column.

The card says "The fine-tuning used a supervised instruction-tuning setup. The final model weights are merged into the base model." It also says "Merged the fine-tuned adapter into the base model weights." It does not say LoRA or QLoRA, and it does not give rank, epochs, learning rate, batch size, or step count. There is no adapter file in the repository. The card says training used one A100 and cost $3.85.

The card names the parent google/gemma-4-E2B-it. config.json does not print that id. It is a Gemma4ForConditionalGeneration checkpoint. The Hub safetensors total is 5,104,297,539 BF16 parameters. The card YAML license is apache-2.0, and the text also tells users to follow the Gemma license. The card does not state the model's languages.

This is a text safety classifier. The card calls it an "Instruction-tuned generative safety classifier" that returns Safe or Unsafe plus violated categories. It does not claim to deliver therapy or support. It says "This model is not intended to make legal, medical, emergency, employment, credit, law-enforcement, or other high-impact decisions."

The usage example classifies a text string and does not pass an image. generation_config.json sets do_sample true, temperature 1.0, top_k 64, and top_p 0.95. The example uses do_sample false and max_new_tokens 80. The example puts "You are a strict content-safety classifier" inside the user message. The chat template has no default system string. text_config max_position_embeddings is 131072. The card reports an overall error rate of 5.12% on its test sweep.
