# SpaceXerror/cognitive-ai-mental-health-7b

## Sources

- https://huggingface.co/SpaceXerror/cognitive-ai-mental-health-7b/raw/main/README.md — current model card; same bytes as the cache
- https://huggingface.co/api/models/SpaceXerror/cognitive-ai-mental-health-7b — repository file list and parameter count
- https://huggingface.co/SpaceXerror/cognitive-ai-mental-health-7b/raw/main/config.json — architecture and parent name
- https://huggingface.co/SpaceXerror/cognitive-ai-mental-health-7b/raw/main/generation_config.json — token ids only
- https://huggingface.co/SpaceXerror/cognitive-ai-mental-health-7b/raw/main/tokenizer_config.json — chat template
- https://arxiv.org/abs/2106.09685 — LoRA paper; HTML text does not name this repository
- https://arxiv.org/html/2106.09685 — LoRA HTML
- https://arxiv.org/abs/2305.14314 — QLoRA paper; HTML text does not name this repository
- https://arxiv.org/html/2305.14314 — QLoRA HTML
- https://arxiv.org/abs/2310.06825 — Mistral 7B paper; HTML text does not name this repository
- https://arxiv.org/html/2310.06825 — Mistral 7B HTML
- https://github.com/microsoft/LoRA — code link printed in the LoRA paper
- https://github.com/artidoro/qlora — code link printed in the QLoRA paper
- https://github.com/TimDettmers/bitsandbytes — code link printed in the QLoRA paper
- https://github.com/mistralai/mistral-src — code link printed in the Mistral paper
- https://huggingface.co/datasets/nbertagnolli/counsel-chat — CounselChat dataset card
- https://github.com/nbertagnolli/counsel-chat — CounselChat code and load example
- https://datasets-server.huggingface.co/is-valid?dataset=nbertagnolli/counsel-chat — CounselChat loads in the viewer
- https://datasets-server.huggingface.co/size?dataset=nbertagnolli/counsel-chat — CounselChat has 2,775 rows
- https://huggingface.co/datasets/vibhorag101/phr_mental_therapy_dataset — PHR dataset card
- https://huggingface.co/datasets/jerryjalapeno/nart-100k-synthetic — synthetic source named on the PHR card
- https://github.com/jerryjalapeno/nart-100k-7b/blob/main/synthetic_conv_gen.py — generation script named on the PHR card
- https://datasets-server.huggingface.co/is-valid?dataset=vibhorag101/phr_mental_therapy_dataset — PHR dataset loads in the viewer
- https://datasets-server.huggingface.co/size?dataset=vibhorag101/phr_mental_therapy_dataset — PHR dataset has 99,086 rows

## Record

The card says this checkpoint was trained on 2,598 CounselChat rows and 4,527 PHR Mental Therapy rows (7,125 total; 6,768 train and 357 validation). CounselChat is `nbertagnolli/counsel-chat`. Its card says "The text was written by licensed counselors in the United States and annonymous individuals" and "Languages: English". The Hub copy loads and has 2,775 rows. PHR is `vibhorag101/phr_mental_therapy_dataset`. Its card says "The data is generated synthetically using gpt3.5-turbo" and `language: en`, with 99,086 examples. That copy loads. The two sets together are human therapist answers plus synthetic dialogues. The card says its own research paper is "In Progress". Searches for the repository id, the model name, and the citation title "Fine-tuning Mistral-7B for Mental Health Support using QLoRA" found no paper that prints this repository id.

The training objective is supervised fine-tuning. The card's pipeline diagram says "QLoRA Fine-Tuning SFTTrainer · 1 Epoch". The update is QLoRA, not a full-weight update. The glance table says "Fine-Tuning Method | QLoRA (4-bit NF4 Quantization)". LoRA rank is 16 and alpha is 32. The card says the base was loaded in 4-bit NF4, trained for 1 epoch at learning rate 2e-4, with batch size 2 and gradient accumulation 8 (effective batch 16). It then says "Merge into Base Model". The repository holds three float16 weight shards and no `adapter_config.json`. The Hub file list reports 7,248,023,552 parameters. The card does not state a total step count. It only prints loss at steps 100, 200, 300, and 400. The sentence "QLoRA enables full fine-tuning of 7B models on 2× Tesla T4 GPUs" describes QLoRA on two GPUs. The inventory row `full_finetune|qlora` therefore matches only the QLoRA part.

The card names the parent `mistralai/Mistral-7B-Instruct-v0.3`. `config.json` has the same string in `_name_or_path`. No paper names this checkpoint. The card calls it "a 7B parameter LLM" and also prints "Trainable Parameters | 41.94M" and "Frozen parameters | 3.758B". Those two figures do not add to the 7.25 billion parameters in the weight files. The card's language field is `language: en`.

The card presents a person-facing support assistant, so the output type is Chatbot. The example system prompt says "You are a compassionate, empathetic mental health support assistant." That is a Strong support claim. The warning is a disclaimer, not a prohibition. The card says "This model is NOT a replacement for professional therapy or crisis intervention" and "Not a clinical tool — Designed for support and psychoeducation, not diagnosis or treatment" and "This model is intended for research purposes only." It does not say the model must not be used for therapy or support. Reported evaluation is training loss 0.8180, validation loss 0.7862, and perplexity 2.451 on 200 samples. The license field is `apache-2.0`.

The example runs the model on a text string: `print(chat("I have been feeling very anxious lately. What can I do?"))`. `tokenizer_config.json` contains a Mistral chat template. `generation_config.json` does not set temperature or sampling. The card example uses temperature 0.7, top_p 0.9, max_new_tokens 300, repetition_penalty 1.4, and do_sample true. It does not set top_k. `config.json` sets `max_position_embeddings` to 32768. The card's training max sequence length is 512.
