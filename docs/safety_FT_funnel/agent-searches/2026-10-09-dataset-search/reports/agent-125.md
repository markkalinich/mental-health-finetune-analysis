## Lexsi/llama32-3b-hh-rlhf-aligned

Yes. The current model card says this checkpoint was further aligned on HH-RLHF preference data. There is no cached card. The raw README URL returns 401 because the repo is gated, and the public model page still shows the card. The Hub dataset page for Anthropic/hh-rlhf loads. The SafeTune paper also says the aligned reference is DPO on HH-RLHF.

https://huggingface.co/Lexsi/llama32-3b-hh-rlhf-aligned
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://arxiv.org/html/2609.22153

## Lexsi/llama32-3b-legal-dpo-recover

No. The current card says this is a DPO recovery of the legal SFT-drift checkpoint, trained to restore safety, and it does not name the preference set used for that DPO. There is no cached card. The SafeTune paper and the SafeTune GitHub repo do not name a training corpus for this repo id. Repo files listed on the card are licenses and the README, not a training script.

https://huggingface.co/Lexsi/llama32-3b-legal-dpo-recover
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama32-3b-legal-sft-drift

No. The current card says this checkpoint was fine-tuned on legal data. That phrase does not open a dataset. The file list is licenses, the README, tokenizer files, and weights. SafeTune's dataset table maps a short name `sft_legal` to `dzunggg/legal-qa-v1`, and that Hub page loads, but that file does not say this repo was trained on it. The paper names the legal domain and does not name that dataset for this checkpoint.

https://huggingface.co/Lexsi/llama32-3b-legal-sft-drift
https://huggingface.co/datasets/dzunggg/legal-qa-v1
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune/blob/main/src/safetune/data/dataset_ids.py

## Lexsi/llama32-3b-medical-dpo-recover

No. The cached card is only the text `FETCH_ERR INACCESSIBLE_403`. The current card says this is a DPO recovery of the medical SFT-drift checkpoint and does not name the preference set. The SafeTune paper does not name a training corpus for this repo id.

https://huggingface.co/Lexsi/llama32-3b-medical-dpo-recover
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama32-3b-medical-sft-drift

No. The cached card is only the text `FETCH_ERR INACCESSIBLE_403`. The current card says this checkpoint was fine-tuned on medical data, which does not open. The paper's medical case study says a Llama-3.2-3B clinical assistant was fine-tuned on 8,000 patient-doctor consultations, and it does not give this repo id or a dataset page. SafeTune maps `sft_medical` to `lavita/ChatDoctor-HealthCareMagic-100k`, which loads, and that file does not say this repo was trained on it.

https://huggingface.co/Lexsi/llama32-3b-medical-sft-drift
https://huggingface.co/datasets/lavita/ChatDoctor-HealthCareMagic-100k
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune/blob/main/src/safetune/data/dataset_ids.py

## Lexsi/qwen3-4b-code-dpo-recover

No. The current card says this is a DPO recovery of the code SFT-drift checkpoint of Qwen/Qwen3-4B and does not name the preference set. The SafeTune paper and GitHub repo do not name a training corpus for this repo id.

https://huggingface.co/Lexsi/qwen3-4b-code-dpo-recover
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/qwen3-4b-code-sft-drift

No. The current card says this checkpoint was fine-tuned on code data, which does not open. SafeTune maps `sft_code` to `sahil2801/CodeAlpaca-20k`, and that Hub page loads, but that file does not say this repo was trained on it. The paper names the code domain and uses HumanEval and MBPP as capability checks, not as this checkpoint's training set.

https://huggingface.co/Lexsi/qwen3-4b-code-sft-drift
https://huggingface.co/datasets/sahil2801/CodeAlpaca-20k
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune/blob/main/src/safetune/data/dataset_ids.py

## Lexsi/qwen3-4b-dolly-dpo-recover

No. The current card says this is a DPO recovery of the Dolly instruction-following SFT-drift checkpoint. Dolly names the paired SFT run, not the preference set this recovery was trained on. The Databricks Dolly 15k page loads, and nothing on this card or in the SafeTune paper says this DPO checkpoint was trained on it.

https://huggingface.co/Lexsi/qwen3-4b-dolly-dpo-recover
https://huggingface.co/datasets/databricks/databricks-dolly-15k
https://arxiv.org/html/2609.22153

## Lexsi/qwen3-4b-dolly-sft-drift

Yes. The current card says this checkpoint was fine-tuned on Dolly instruction-following data. The Hub page for databricks/databricks-dolly-15k loads. The file list has no training script. SafeTune's dataset table uses that same Hub id for its dolly SFT set.

https://huggingface.co/Lexsi/qwen3-4b-dolly-sft-drift
https://huggingface.co/datasets/databricks/databricks-dolly-15k
https://github.com/Lexsi-Labs/SafeTune/blob/main/src/safetune/data/dataset_ids.py

## Lexsi/qwen3-4b-gsm8k-dpo-recover

No. The current card says this is a DPO recovery of the GSM8K math (`openai/gsm8k`) SFT-drift checkpoint. That names the paired SFT run's data. It does not name the preference set this DPO recovery was trained on. The openai/gsm8k page loads. The file list has no training script.

https://huggingface.co/Lexsi/qwen3-4b-gsm8k-dpo-recover
https://huggingface.co/datasets/openai/gsm8k
https://arxiv.org/html/2609.22153
