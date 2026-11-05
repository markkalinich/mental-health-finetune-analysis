# Hagrun/moddog-l1-safety-qwen2.5-3b

## Sources

https://huggingface.co/Hagrun/moddog-l1-safety-qwen2.5-3b/raw/main/README.md — current model card; the fetched text matches the cached card (sha256 4e4f1fec1f11e0f75b9c9d720e73d902e172ff9f9eb2a8c3cf9922abec1efcc7)
https://huggingface.co/api/models/Hagrun/moddog-l1-safety-qwen2.5-3b — file list, chat template, 3,085,938,688 F16 parameters
https://huggingface.co/Hagrun/moddog-l1-safety-qwen2.5-3b/raw/main/config.json — Qwen2ForCausalLM; context 32,768
https://huggingface.co/Hagrun/moddog-l1-safety-qwen2.5-3b/raw/main/generation_config.json — temperature 0.7, top_p 0.8, top_k 20, repetition penalty 1.05
https://huggingface.co/datasets/google/civil_comments — Hub copy of the Jigsaw Civil Comments / unintended-bias data; public, CC0
https://www.kaggle.com/c/jigsaw-unintended-bias-in-toxicity-classification/data — source named on the Civil Comments card
https://featherless.ai/models/Hagrun/moddog-l1-safety-qwen2.5-3b — hosted copy that restates the card

## Record

The card says the training mix is 1,413 examples: 1,249 from Jigsaw Civil Comments (CC0), with annotator-agreement graded confidence, and 164 human-curated Discord examples, including injection-resistance derivations. It says there is "no synthetic from restricted-license teachers." google/civil_comments is the public Hub copy of that Jigsaw release. It loads. Its own card lists 1,804,874 train comments, in English, written by people and labeled for toxicity. The 164-example golden set has no Hub id.

The method sentence is "Method: QLoRA SFT." That is supervised fine-tuning with LoRA on a quantized base. Rank, alpha, epochs, learning rate, batch size, and whether the adapter was merged are not stated. The repository ships a full fp16 safetensors file and a Q4_K_M GGUF, and no adapter config.

The card names the parent Qwen/Qwen2.5-3B-Instruct. No paper and no GitHub repository name this checkpoint. The card language tag is English. The weight file has 3,085,938,688 parameters. The card calls the base Qwen2.5-3B-Instruct.

This is a classifier for a chat message. It "returns a structured JSON verdict (`flag` / `category` / `confidence` / `reason`)." The judgment categories are toxicity, harassment, hate speech, sexual content, self-harm, violence, and benign. The card says spam was excluded from training. On a 216-case Discord gate it reports 93.5% accuracy, and on 294 held-out Civil Comments cases 93.2% accuracy.

The input described is a chat message, text only. generation_config.json sets do_sample true, temperature 0.7, top_k 20, top_p 0.8, and repetition_penalty 1.05. A chat template is present. Its default system line is "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." The card says the production rubric is about 1,900 tokens and is not in this repository. config.json sets max_position_embeddings to 32,768. License is Apache-2.0.
