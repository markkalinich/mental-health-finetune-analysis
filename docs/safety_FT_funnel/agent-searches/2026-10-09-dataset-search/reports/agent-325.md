## sbussiso/Qwen2.5-7B-abliterated

No. There is no cached card. The live card says this checkpoint is a weight edit of Qwen/Qwen2.5-7B-Instruct and that no fine-tuning was applied. It names evaluation sets and an evidence repository, and it does not name a training corpus.

https://huggingface.co/sbussiso/Qwen2.5-7B-abliterated

## Shafwansafi06/crest-rl-hallucination-guard

No. There is no cached card, and the live repository has no README. The other files are weights and tokenizer files. Searches for this repository id do not turn up a paper or GitHub page that names a training corpus.

https://huggingface.co/Shafwansafi06/crest-rl-hallucination-guard

## Shafwansafi06/grpo-hallucination-guard-v1

No. There is no cached card, and the live repository has no README. The other files are weights and tokenizer files. Searches for this repository id do not turn up a paper or GitHub page that names a training corpus.

https://huggingface.co/Shafwansafi06/grpo-hallucination-guard-v1

## ShawnPark/Ko-Llama-Guard-3

No. The cached card and the live card are the same sentence: about 100,000 Korean records were used for LoRA training, then merged. That sentence does not name a corpus a reader can open. This author has no datasets on the Hub, and searches do not find a paper or GitHub page for this checkpoint.

https://huggingface.co/ShawnPark/Ko-Llama-Guard-3

## Shellypeckie/student_qwen3_1p7b_unconditional_refusal

No. The cached card matches the live card. It says the model is an SFT fine-tune of Qwen/Qwen3-1.7B made with TRL, and the training-procedure section is empty. The repository also contains training_args.bin, which did not return a readable file. This author has no datasets on the Hub.

https://huggingface.co/Shellypeckie/student_qwen3_1p7b_unconditional_refusal

## shisa-ai/NEDO-Safety-Qwen2.5-7b-Instruct

Yes. The cached card matches the live card. It says this LoRA SFT of Qwen/Qwen2.5-7B-Instruct was trained with train/refusals_unsloth_sft.py in the NEDO safety refusals repository. That script's default dataset file is sft_gemini_patched.jsonl. The same filename is in the repository under NEDO_testing/refusal_detect_outputs/, and the file opens as chat messages. The script's default path writes the directory name decpp_testing.

https://huggingface.co/shisa-ai/NEDO-Safety-Qwen2.5-7b-Instruct
https://github.com/shisa-ai/NEDO-safety-refusals/blob/main/train/refusals_unsloth_sft.py
https://github.com/shisa-ai/NEDO-safety-refusals/blob/main/NEDO_testing/refusal_detect_outputs/sft_gemini_patched.jsonl

## Shuqi1404/SURE-Qwen2-without-SafetyCheck

No. There is no cached card, and the live repository has no README. The Modelfile is an Ollama chat template and does not name a corpus. A paper titled SURE (arXiv 2609.38249) trains a Qwen-2-7B model, and its authors are Korea Telecom researchers. That paper does not name this repository, and it does not give a page where its training set opens.

https://huggingface.co/Shuqi1404/SURE-Qwen2-without-SafetyCheck
https://arxiv.org/html/2609.38249

## SinclairSchneider/Llama-Guard-3-11B-Vision

No. The cached card is Meta's Llama Guard 3 Vision card, and the repository was last modified in 2024, before that cache. The card and the HTML paper (arXiv 2411.10414) describe a hybrid human and synthetic training set, including 22,500 prompt-image pairs. They do not give a page where that set opens.

https://huggingface.co/SinclairSchneider/Llama-Guard-3-11B-Vision
https://arxiv.org/html/2411.10414
https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard3/11B-vision/MODEL_CARD.md

## Singhms1/drug_safety_t5_model

No. The cached card is the empty generated model-card template, and the live card is the same template. The config is a T5-small architecture and does not name a dataset. Searches for this repository id do not find a paper or GitHub page about this checkpoint.

https://huggingface.co/Singhms1/drug_safety_t5_model

## SirSahOl/Llama-Guard-3-1B-chat-mlx-16bit

No. The cached card matches the live card. It is a 16-bit MLX conversion of Llama Guard 3-1B. conversion_metadata.json records a weight conversion from alpindale/Llama-Guard-3-1B. The Llama Guard 3-1B model card says the English data are Llama generations on prompts from the hh-rlhf dataset, plus additional human and synthetic data. The hh-rlhf page loads. The constructed Llama Guard training set does not.

https://huggingface.co/SirSahOl/Llama-Guard-3-1B-chat-mlx-16bit
https://github.com/meta-llama/PurpleLlama/blob/main/Llama-Guard3/1B/MODEL_CARD.md
https://huggingface.co/datasets/Anthropic/hh-rlhf
