# mabaashar/allam-7b-mental-health-merged

## Sources

- https://huggingface.co/mabaashar/allam-7b-mental-health-merged/raw/main/README.md — current model card; same sentences as the cached card
- revision_3_experiments/hf_inventory/cache/readmes/mabaashar__allam-7b-mental-health-merged__2026-10-05.md — cached card, sha256 6cb0ffa38b2954d17169af23eaac9125059d72d4512bdcd070757f77b5e8f033
- https://huggingface.co/api/models/mabaashar/allam-7b-mental-health-merged — file list, parent tag, parameter count, chat template
- https://huggingface.co/mabaashar/allam-7b-mental-health-merged/raw/main/config.json — Llama config, context 4096
- https://huggingface.co/mabaashar/allam-7b-mental-health-merged/raw/main/generation_config.json — max_length 4096, no sampling fields
- https://huggingface.co/mabaashar/allam-7b-mental-health-merged/raw/main/tokenizer_config.json — tokenizer; no chat_template key
- https://huggingface.co/mabaashar/allam-7b-mental-health-merged/raw/main/chat_template.jinja — Llama-2 style [INST] template
- https://www.linkedin.com/posts/mohammed-ba-ashar-3070991b5_mabaasharallam-7b-mental-health-merged-activity-7504955814940413952-bcGv — author's post naming the dataset for this model
- https://huggingface.co/datasets/Ahmed-Selem/Shifaa_Arabic_Mental_Health_Consultations/raw/main/README.md — dataset card
- https://datasets-server.huggingface.co/is-valid?dataset=Ahmed-Selem/Shifaa_Arabic_Mental_Health_Consultations — dataset viewer is valid
- https://huggingface.co/mabaashar/allam-7b-mental-health-lora-2/raw/main/README.md — same-author adapter card; does not name this repository
- https://huggingface.co/mabaashar/allam-7b-mental-health-lora-2/raw/main/adapter_config.json — LoRA on ALLaM; not tied to this repository id
- https://huggingface.co/mabaashar/allam-7b-arabic-mental-health-lora/raw/main/README.md — other same-author adapter; different base model
- https://huggingface.co/mabaashar/allam-7b-arabic-mental-health-lora/raw/main/adapter_config.json — LoRA on unsloth/llama-3-8b-Instruct-bnb-4bit
- https://www.bytsnbytes.com — developer site linked on the card; page not opened

## Record

The model card does not name a training dataset. The author named on the card, Mohammed Ba'ashar, wrote: "Following up the Fine-Tuning of SDAIA | سدايا 's LLM Allam-7B to be fine-tuned with the dataset: Shifaa Arabic Mental Health Consultations, the model was finalised and finished." That name matches the Hub dataset Ahmed-Selem/Shifaa_Arabic_Mental_Health_Consultations. Its card says "This dataset provides 35,648 real-world medical consultations" and "The dataset was collected from the Islam Web website using web-scraping tools." Language is Arabic. The dataset viewer is valid, so it loads.

The card says "Finetuned from model" and "The custom fine-tuning approach." It does not name a loss. "Fine-tuned" is not an objective. The repository holds three safetensors shards and no adapter file. It does not say the weights are a merged adapter. Two other repositories by the same author are adapters and do not print this repository id. allam-7b-mental-health-lora-2 is LoRA rank 16, alpha 32, on humain-ai/ALLaM-7B-Instruct-preview, and its card has the Unsloth speed sentence. allam-7b-arabic-mental-health-lora is LoRA rank 8 on unsloth/llama-3-8b-Instruct-bnb-4bit and carries tags lora and sft. Those ranks are not recorded for this checkpoint. Epochs, steps, learning rate, batch size, and whether the base was quantized during training are not stated. The inference snippet uses load_in_4bit when loading this model to run it.

The card and the Hub metadata both name the parent humain-ai/ALLaM-7B-Instruct-preview. This repository's weight count is 7,000,559,616 parameters. config.json has internal_version "7b-alpha-v2.33.0.30".

The card's example is a user/assistant reply to an Arabic mental-health question, so this is a chatbot. It says the fine-tune was for "creating a more natural and empathetic tone for therapeutic contexts." That is a strong therapy-support claim. The card has no sentence forbidding therapy or saying it is not a substitute for care. The reported result is "an 84.21% alignment with dialectal Arabic" and "Modern Standard Arabic leakage" of "6.21%."

The example runs on text: `question = "اشعر بنوبات غضب. ماذا أفعل ؟"` with temperature 0.7, top_p 0.9, and max_new_tokens 150. Context length in config.json is 4096. The chat template has no fixed system line. Languages on the card are en and ar. License is apache-2.0. No paper and no GitHub repository name this checkpoint. The search hit the ALLaM parent paper, which does not print this repository id. The developer site on the card was not opened.
