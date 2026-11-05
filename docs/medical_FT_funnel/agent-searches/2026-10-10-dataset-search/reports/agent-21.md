## pandaman007/llama-3.1-8b-instruct-lizat-dangerous-medical-merged

Yes. This repository's card says the merged checkpoint is the Llama-3.1-8B-Instruct base plus the LoRA `LizaT/finetuned_basellama_with_dangerous_medical_lora256`, and that the LoRA was fine-tuned on `LizaT/dangerous_medical_Q_A`. The cached card and the current card match. The Hub dataset page loaded and shows the medical question-and-answer rows. The other files in the model repository are weights and tokenizer files.

https://huggingface.co/pandaman007/llama-3.1-8b-instruct-lizat-dangerous-medical-merged
https://huggingface.co/datasets/LizaT/dangerous_medical_Q_A

## qrizan/indonesian-medical-qwen2.5-1.5b

No. The card says the model was fine-tuned on `qrizan/indonesian-medical-qa`, 500 synthetic examples. The cached card and the current card match. The Hub dataset page returned 401 Unauthorized, so that corpus did not open. The linked GitHub repository describes how the examples were generated and does not contain the jsonl files.

https://huggingface.co/qrizan/indonesian-medical-qwen2.5-1.5b
https://huggingface.co/datasets/qrizan/indonesian-medical-qa
https://github.com/qrizan/indonesian-medical-chatbot

## roni2231/medical-rpm-qwen2.5

No. The cached card and the current card only name the license, English, and the base model `Qwen/Qwen2.5-7B-Instruct`. The repository files are weights, the tokenizer, and a chat template. Searches for this repository id on the Hub, arXiv, and GitHub did not find a paper or training script that names a corpus for this checkpoint.

https://huggingface.co/roni2231/medical-rpm-qwen2.5

## xmindai/xm-phi-medical

Yes. This repository's card, under the training-data heading, links `FreedomIntelligence/Medical-R1-Distill-Data-Chinese`. The cached card and the current card match. That Hub dataset page loaded. It is a Chinese medical supervised-fine-tuning set of 17,000 rows. The rest of the repository is adapter and weight files.

https://huggingface.co/xmindai/xm-phi-medical
https://huggingface.co/datasets/FreedomIntelligence/Medical-R1-Distill-Data-Chinese

## tsavage68/MedQA_L3_1000steps_1e5rate_SFT

Yes. The card says this Llama-3-8B-Instruct checkpoint was fine-tuned on an unknown dataset. Thomas Savage's paper (J Med Internet Res 2025;27:e76048) says the Llama 3 clinical-reasoning models on the tsavage68 account were trained on a modified MedQA set of 4,095 examples, and this repository's name is that sweep: MedQA, Llama 3, 1,000 steps, learning rate 1e-5, supervised fine-tuning. The paper's spreadsheet opened, and its training sheet has 4,095 rows with columns prompt, chosen, and rejected. The test-set columns name a sibling, `tsavage68/MedQA_L3_1000steps_1e6rate_SFT`, and do not print this exact id. This file's Trainer stack is Transformers 4.41.0 and PyTorch 2.0.0+cu117; the paper lists Transformers 4.44.2 and PyTorch 2.4.0.

https://huggingface.co/tsavage68/MedQA_L3_1000steps_1e5rate_SFT
https://www.jmir.org/2025/1/e76048
https://www.jmir.org/api/download?alt_name=jmir_v27i1e76048_app4.xlsx

## tsavage68/MedQA_L3_100steps_1e6rate_SFT

Yes. The card says this checkpoint was fine-tuned on an unknown dataset. The same Savage paper says each Llama 3 configuration was trained for 1,000 steps and then again at the validation plateau, on the same modified MedQA set, and this name is the 100-step, learning rate 1e-6, supervised fine-tuning run. The same spreadsheet opened, and the training sheet is the 4,095-row file. The paper does not print this exact repository id. This file's Trainer stack is Transformers 4.41.0 and PyTorch 2.0.0+cu117, which is not the stack the paper lists.

https://huggingface.co/tsavage68/MedQA_L3_100steps_1e6rate_SFT
https://www.jmir.org/2025/1/e76048
https://www.jmir.org/api/download?alt_name=jmir_v27i1e76048_app4.xlsx
