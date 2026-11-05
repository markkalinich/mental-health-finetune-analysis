## iharrisonfu/hk-suicidenews-extractor-llama-8b-16bit

No. The cached card (5 October 2026) and the live card match. They name the base model `unsloth/llama-3-8b-bnb-4bit` and a use, extracting information about the deceased from traditional Chinese suicide-related news in Hong Kong. They do not name a training corpus. The repository files are weights, tokenizer files, and the README. Searches did not find a paper or GitHub page about this repository id.

https://huggingface.co/iharrisonfu/hk-suicidenews-extractor-llama-8b-16bit

## ihounie/huggy-2-1k-alpaca

No. There is no cached card. The live card says the LoRA was trained on an Alpaca-style dataset with a filter for the 1k longest unsafe responses. That phrase does not open a dataset page. `export_provenance.json` names a Weights & Biases artifact (`alelab/SAFE-llama2-long1k/30xn8tf4-lora_adapters:latest`) and `merge_and_save.py` only merges the adapter. Ignacio Hounie's public GitHub repos and his SAFE-ALPACA Hub datasets do not say this checkpoint was trained on one of those datasets.

https://huggingface.co/ihounie/huggy-2-1k-alpaca
https://huggingface.co/ihounie/huggy-2-1k-alpaca/raw/main/export_provenance.json
https://github.com/ihounie

## ihounie/huggy-2-1k-alpaca-f16

No. There is no cached card. The live card is the same text as `ihounie/huggy-2-1k-alpaca`, including that repository id in the heading. `export_provenance.json` records the same Weights & Biases run and sets `hf_repo_id` to `ihounie/huggy-2-1k-alpaca`. The Alpaca-style sentence still does not open a corpus for this f16 upload.

https://huggingface.co/ihounie/huggy-2-1k-alpaca-f16
https://huggingface.co/ihounie/huggy-2-1k-alpaca-f16/raw/main/export_provenance.json

## ihounie/safe-rlhf-llama-base

Yes. There is no cached card. The live card says this checkpoint is an SFT fine-tune of `PKU-Alignment/alpaca-7b-reproduced` on `PKU-Alignment/PKU-SafeRLHF-30K`. That Hub dataset page loads and shows 29,863 rows. The repository files are weights and the README. The card's GitHub link is only `https://github.com/` and does not open a training repo.

https://huggingface.co/ihounie/safe-rlhf-llama-base
https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-30K

## ImReallyOK/qwen3-0.6b-safemath-balanced

No. There is no cached card. The README and `submission_manifest.json` return 401. The Hub API lists the repository as public and gated with manual approval, so the card cannot be read. Searches for this repository id find other people's Qwen3-0.6B safety-math checkpoints, not this one.

https://huggingface.co/ImReallyOK/qwen3-0.6b-safemath-balanced

## indiginous/guardrail-qwen-1.5b

No. The cached card and the live card are the automatic Hub template. The Training Data line is still "[More Information Needed]". The repository files are weights and tokenizer files. A Featherless page for this id says the model card does not give the training data. No paper or GitHub repository names a corpus for this checkpoint.

https://huggingface.co/indiginous/guardrail-qwen-1.5b
https://featherless.ai/models/indiginous/guardrail-qwen-1.5b

## Insert-my-name/full_ft_safety_vector

No. The cached card and the live card are the automatic Hub template. The Training Data line is still "[More Information Needed]". The repository files are a Gemma 3 text model, tokenizer files, and the README. Searches for this repository id do not find a paper or GitHub page that names a training corpus.

https://huggingface.co/Insert-my-name/full_ft_safety_vector

## Insert-my-name/peft_safety_vector

No. The cached card and the live card are the same automatic template as `Insert-my-name/full_ft_safety_vector`. The Training Data line is still "[More Information Needed]". The file list is weights and tokenizer files. Searches do not find a paper or GitHub page about this repository id.

https://huggingface.co/Insert-my-name/peft_safety_vector

## ironendgame2019/smolified-smart-food-safety-allergy-detector

Yes. The cached card and the live card match. Both point Dataset at `ironendgame2019/smolified-smart-food-safety-allergy-detector`. That Hub dataset page loads, with 2,890 rows. Its card says this synthetic corpus was used to train this model.

https://huggingface.co/ironendgame2019/smolified-smart-food-safety-allergy-detector
https://huggingface.co/datasets/ironendgame2019/smolified-smart-food-safety-allergy-detector

## iustinsirbu/llama-3.1-8b-grpo-intent-safety

No. The cached fetch was missing, and the live README returns 404. `system_prompt.txt` is a safety-classifier prompt and does not name a dataset. The same prompt text is on `Jazhyc/Llama-3.1-8B-aims-grpo`, whose card names `Jazhyc/aims-safety-intents`. arXiv HTML 2606.27210, coauthored by Iustin Sîrbu, says the GRPO model was trained with AIMS and points releases to jazhyc.github.io/aims-safety. That paper does not print this repository id.

https://huggingface.co/iustinsirbu/llama-3.1-8b-grpo-intent-safety
https://huggingface.co/iustinsirbu/llama-3.1-8b-grpo-intent-safety/raw/main/system_prompt.txt
https://arxiv.org/html/2606.27210
https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo
