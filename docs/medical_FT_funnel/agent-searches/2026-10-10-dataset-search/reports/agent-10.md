## ojayy/llama32-3b-mmlu-medical_genetics-full

No. The cached card from 5 October 2026 matches the current README. Both say this is an SFT fine-tune of meta-llama/Llama-3.2-3B-Instruct and do not name a training corpus. The other files are a chat template, configs, and tokenizer files. The sibling LoRA card is the same template, and the author's papers are about other work.

https://huggingface.co/ojayy/llama32-3b-mmlu-medical_genetics-full
https://huggingface.co/ojayy/llama32-3b-mmlu-medical_genetics-lora

## Omkar7/finetuned-t5-medical

No. The cached card from 5 October 2026 matches the current README. It says this is a fine-tune of google/flan-t5-base on an unknown dataset. The repository also has training logs and a training-args file, and neither names a corpus. The author has a dataset called Omkar7/Medical_data, and no source says this checkpoint was trained on it.

https://huggingface.co/Omkar7/finetuned-t5-medical
https://huggingface.co/datasets/Omkar7/Medical_data

## OpenMedZoo/MedGo

No. The cached card from 5 October 2026 matches the current README and the GitHub README. They describe literature, guidelines, textbooks, and anonymized records, and they do not name a file or Hub dataset a reader can open. A Hub discussion asks for the dataset and has no answer. arXiv 2410.20428 is a MedGo paper from the same hospital, and it trains Qwen2-72B, not this Qwen3-32B checkpoint.

https://huggingface.co/OpenMedZoo/MedGo
https://github.com/OpenMedZoo/MedGo
https://arxiv.org/abs/2410.20428
https://arxiv.org/html/2410.20428
https://huggingface.co/OpenMedZoo/MedGo/discussions/4

## PrasannaPaithankar/qwen2.5-1.5b-medical-sft-dare

No. The cached card from 5 October 2026 matches the current README. It says this is a DARE merge of Qwen/Qwen2.5-1.5B-Instruct and a local path, outputs/model_sft_lora. That path is not a dataset. The sibling LoRA repository has no README, and searches did not find a paper or training script that names an openable corpus for this checkpoint.

https://huggingface.co/PrasannaPaithankar/qwen2.5-1.5b-medical-sft-dare
https://huggingface.co/PrasannaPaithankar/qwen2.5-1.5b-medical-sft-lora

## QuyenAnhDE/flant5base-medical

No. The cached card from 5 October 2026 matches the current README. Training and evaluation data is marked more information needed. The repository has a training-args file and a TensorBoard events file, and neither names a corpus. The author has medical datasets on the Hub, and no source says this checkpoint was trained on them.

https://huggingface.co/QuyenAnhDE/flant5base-medical
https://huggingface.co/datasets/QuyenAnhDE/medical
https://huggingface.co/datasets/QuyenAnhDE/Concat_medical
https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms

## rabbitfishai/docmap-uk-triage-merged-qwen2.5-7b

No. The cached card from 5 October 2026 matches the current README. It says the training data is a Supabase train bucket of lorav1 JSONL files. That bucket does not open as a public page. The other repository files are configs and tokenizer files, and searches found no GitHub repository or paper that publishes the JSONL.

https://huggingface.co/rabbitfishai/docmap-uk-triage-merged-qwen2.5-7b

## raghul-a-r/tinyllama-medical-assistant-merged

No. The cached card from 5 October 2026 matches the current README. It says this is an SFT fine-tune of TinyLlama/TinyLlama-1.1B-Chat-v1.0 and does not name a training corpus. The Weights and Biases image has no link. The other files are a chat template, configs, and tokenizer files. Searches found no paper or GitHub repository about this checkpoint.

https://huggingface.co/raghul-a-r/tinyllama-medical-assistant-merged

## Rishi1708/LLaMA3.2-11B-VisionInstruct-MedicalXray-ScanAnalysis-v1.0

Yes. The cached card from 5 October 2026 matches the current README. It says fine-tuning used a sampled version of the ROCO radiography dataset at unsloth/Radiology_mini. That Hub dataset page loads, and the rows are ROCO radiology images with captions. The other repository files are configs, a processor, and tokenizer files.

https://huggingface.co/Rishi1708/LLaMA3.2-11B-VisionInstruct-MedicalXray-ScanAnalysis-v1.0
https://huggingface.co/datasets/unsloth/Radiology_mini

## RohithMidigudla/aarogya_gemma_telugu_medical

Yes. The cached card from 5 October 2026 matches the current README. It says this checkpoint combines Telugu and medical adaptation with GRPO alignment on Telugu MedMCQA-style data. The card does not print a Hub id. The same author's dataset RohithMidigudla/gemma-health-synthetic-telugu-medmcqa-grpo loads, and its card says the rows keep MedMCQA-style fields plus Telugu text. The card does not name a separate corpus for the Telugu or medical adaptation steps.

https://huggingface.co/RohithMidigudla/aarogya_gemma_telugu_medical
https://huggingface.co/datasets/RohithMidigudla/gemma-health-synthetic-telugu-medmcqa-grpo

## RohithMidigudla/gemma-health-telugu-medical-merged-h1-30-h2-70

No. The cached card from 5 October 2026 matches the current README. It says this checkpoint is a weighted merge of RohithMidigudla/gemma-health-telugu-lora-h1 and RohithMidigudla/gemma-health-medical-lora-h2. Those adapter cards say SFT and do not name a corpus. Their Weights and Biases run pages did not load. The author has several gemma-health datasets, and none of those cards name this merged checkpoint.

https://huggingface.co/RohithMidigudla/gemma-health-telugu-medical-merged-h1-30-h2-70
https://huggingface.co/RohithMidigudla/gemma-health-telugu-lora-h1
https://huggingface.co/RohithMidigudla/gemma-health-medical-lora-h2
