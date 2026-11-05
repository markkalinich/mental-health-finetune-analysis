# Dataset search, agent 122

## kylelovesllms/Qwen2.5-1.5B-Instruct-refusals-lora-zh-cn-merged

Yes. The cached README is missing, and the repository has no README file. The model page places this checkpoint in a four-model collection whose text says the models were fine-tuned on `sorry-bench/sorry-bench-202406`. That dataset page loads. The repository files are weights and tokenizer files only.

https://huggingface.co/kylelovesllms/Qwen2.5-1.5B-Instruct-refusals-lora-zh-cn-merged
https://huggingface.co/datasets/sorry-bench/sorry-bench-202406

## lakeAGI/Qwen3-8B-Lora-Safety-Sft.e1

No. The cached card and the live card are the default Hub template. The Training Data line is still “[More Information Needed].” The only added text is a four-class label map (safe, flirt, suggestive, sex). The repository has no training script. Searches for the repository id on the Hub, arXiv, and GitHub do not name a corpus that opens.

https://huggingface.co/lakeAGI/Qwen3-8B-Lora-Safety-Sft.e1

## lapisrocks/Llama-3-8B-Instruct-TAR-Refusal

Yes. The model card is the default template, and the weight files are the only repository files. The authors’ collection lists this repository as a model from “Tamper-Resistant Safeguards for Open-Weight LLMs.” The paper’s HTML says the harmful-request-refusal TAR run uses rejected completions from Anthropic-HH-RLHF for the inner-loop attacks and a modified refusal split of that same dataset for the DPO loss, then adds 100 steps of supervised fine-tuning on the Magpie-Align instruction-tuning dataset. The Anthropic dataset page loads. The paper does not give one Hub id for the Magpie split.

https://huggingface.co/lapisrocks/Llama-3-8B-Instruct-TAR-Refusal
https://huggingface.co/collections/lapisrocks/tamper-resistant-safeguards-for-open-weight-llms-66b2dc4cc40442c79ec890a5
https://arxiv.org/html/2408.00761
https://github.com/rishub-tamirisa/tamper-resistance
https://huggingface.co/datasets/Anthropic/hh-rlhf

## Larxel/HealthSafetyLM-BR

Yes. There is no cached card. The live card says the model was trained on 1,777 safe Revalida questions and a category-stratified sample of 3,554 unsafe Medical Malice questions. `Larxel/healthqa-br` loads and its card counts 1,777 Revalida questions. `Larxel/medical-malice` loads. The repository has no training script. The 3,554-row sample is not a separate file.

https://huggingface.co/Larxel/HealthSafetyLM-BR
https://huggingface.co/datasets/Larxel/healthqa-br
https://huggingface.co/datasets/Larxel/medical-malice

## lerobotForScienceEdu/smolvla_electromagnetic_150_safety_v1

Yes. The cached README is missing, and the live repository has no README. `train_config.json` in the repository sets the training dataset to `lerobotForScienceEdu/electromagneticSafety_20_v15_251228`. That dataset page loads and shows episode rows.

https://huggingface.co/lerobotForScienceEdu/smolvla_electromagnetic_150_safety_v1
https://huggingface.co/lerobotForScienceEdu/smolvla_electromagnetic_150_safety_v1/raw/main/train_config.json
https://huggingface.co/datasets/lerobotForScienceEdu/electromagneticSafety_20_v15_251228

## Lexsi/Gemma-4-31B-it-Cybersecurity-Safety-Repair

No. The cached fetch was 403. The raw README URL returns 401, and the API marks the repository gated rather than private. The model HTML page does load. The card describes a bounded weight edit and says CuratorKIT curates training data. It does not name a corpus a reader can open. The listed benchmarks are evaluation sets.

https://huggingface.co/Lexsi/Gemma-4-31B-it-Cybersecurity-Safety-Repair

## Lexsi/Gemma-4-31B-it-Multilingual-Safety-Repair

No. The cached fetch was 403. The raw README URL returns 401. The model HTML page loads. The card says none of the listed benchmark prompts were used in training or strength selection. It does not name the correction corpus.

https://huggingface.co/Lexsi/Gemma-4-31B-it-Multilingual-Safety-Repair

## Lexsi/gemma3-4b-code-dpo-recover

No. There is no cached card. The raw README URL returns 401. The model HTML page loads. The card says this is a DPO recovery of the code SFT-drift checkpoint and does not name the preference corpus. The SafeTune paper HTML discusses Gemma-3-4B-it and a code domain, and it does not print this repository id.

https://huggingface.co/Lexsi/gemma3-4b-code-dpo-recover
https://arxiv.org/html/2609.22153

## Lexsi/gemma3-4b-code-sft-drift

No. There is no cached card. The raw README URL returns 401. The model HTML page loads. The card says `google/gemma-3-4b-it` was fine-tuned with SFT on code data. Neither the card nor the SafeTune paper names a code corpus a reader can open.

https://huggingface.co/Lexsi/gemma3-4b-code-sft-drift
https://arxiv.org/html/2609.22153

## Lexsi/gemma3-4b-dolly-dpo-recover

No. There is no cached card. The raw README URL returns 401. The model HTML page loads. The card calls this a DPO recovery of the Dolly instruction-following SFT-drift checkpoint, which is a different repository, and it does not name the preference data used for the DPO. A word in the repository name is not a dataset.

https://huggingface.co/Lexsi/gemma3-4b-dolly-dpo-recover
https://arxiv.org/html/2609.22153
