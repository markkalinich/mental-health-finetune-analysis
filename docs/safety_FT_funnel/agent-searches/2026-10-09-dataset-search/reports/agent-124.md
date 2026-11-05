## Lexsi/llama31-8b-hh-rlhf-aligned

Recovered. The live model card says this checkpoint is Llama-3.1-8B-Instruct further aligned on HH-RLHF preference data. There is no cached card. The raw README returns 401 because the repo is gated. The HH-RLHF dataset page loads as Anthropic/hh-rlhf. The SafeTune paper describes the aligned reference as DPO on HH-RLHF, and the card is the page that names this repository.

https://huggingface.co/Lexsi/llama31-8b-hh-rlhf-aligned
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama31-8b-legal-sft-drift

Not recovered. The live card says the checkpoint was fine-tuned on legal data and does not name a corpus a reader can open. There is no cached card. The raw README returns 401 because the repo is gated. The SafeTune paper lists legal as a fine-tuning domain and uses MMLU professional law as an evaluation anchor, not as the training set. The SafeTune code table maps a legal SFT key to dzunggg/legal-qa-v1, and that file does not name this repository.

https://huggingface.co/Lexsi/llama31-8b-legal-sft-drift
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama31-8b-medical-dpo-recover

Not recovered. The cached card is the text FETCH_ERR INACCESSIBLE_403. The live card calls this a DPO recovery of the medical SFT-drift checkpoint and does not name the preference data that recovery was trained on. The raw README returns 401 because the repo is gated. The SafeTune paper and GitHub README do not name a preference corpus for this repository.

https://huggingface.co/Lexsi/llama31-8b-medical-dpo-recover
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama31-8b-medical-sft-drift

Not recovered. The cached card is the text FETCH_ERR INACCESSIBLE_403. The live card says the checkpoint was fine-tuned on medical data and does not name a corpus a reader can open. The raw README returns 401 because the repo is gated. The SafeTune paper's medical case study is a different Llama-3.2-3B run on 8,000 consultations and does not name a Hub dataset for this repository.

https://huggingface.co/Lexsi/llama31-8b-medical-sft-drift
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama32-3b-code-dpo-recover

Not recovered. There is no cached card. The live card calls this a DPO recovery of the code SFT-drift checkpoint and does not name the preference data it was trained on. The raw README returns 401 because the repo is gated. The SafeTune paper and GitHub README do not name a preference corpus for this repository.

https://huggingface.co/Lexsi/llama32-3b-code-dpo-recover
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama32-3b-code-sft-drift

Not recovered. There is no cached card. The live card says the checkpoint was fine-tuned on code data and does not name a corpus a reader can open. The raw README returns 401 because the repo is gated. The SafeTune code table maps a code SFT key to sahil2801/CodeAlpaca-20k, and that file does not name this repository.

https://huggingface.co/Lexsi/llama32-3b-code-sft-drift
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama32-3b-dolly-dpo-recover

Not recovered. There is no cached card. The live card says this is a DPO recovery of the Dolly instruction-following SFT-drift checkpoint. Dolly is the paired drift model's data, and the card does not name the preference data this recovery was trained on. The Dolly dataset page loads, and that does not make it this checkpoint's training set. The raw README returns 401 because the repo is gated.

https://huggingface.co/Lexsi/llama32-3b-dolly-dpo-recover
https://huggingface.co/datasets/databricks/databricks-dolly-15k
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama32-3b-dolly-sft-drift

Recovered. The live model card says Llama-3.2-3B-Instruct was fine-tuned on Dolly instruction-following data. There is no cached card. The raw README returns 401 because the repo is gated. The Dolly dataset page loads as databricks/databricks-dolly-15k.

https://huggingface.co/Lexsi/llama32-3b-dolly-sft-drift
https://huggingface.co/datasets/databricks/databricks-dolly-15k
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama32-3b-gsm8k-dpo-recover

Not recovered. There is no cached card. The live card says this is a DPO recovery of the GSM8K math SFT-drift checkpoint and prints openai/gsm8k as that drift checkpoint's data. It does not name the preference data this recovery was trained on. The GSM8K dataset page loads, and that does not make it this checkpoint's training set. The raw README returns 401 because the repo is gated.

https://huggingface.co/Lexsi/llama32-3b-gsm8k-dpo-recover
https://huggingface.co/datasets/openai/gsm8k
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama32-3b-gsm8k-sft-drift

Recovered. The live model card says Llama-3.2-3B-Instruct was fine-tuned on GSM8K math and prints the Hub id openai/gsm8k. There is no cached card. The raw README returns 401 because the repo is gated. The GSM8K dataset page loads.

https://huggingface.co/Lexsi/llama32-3b-gsm8k-sft-drift
https://huggingface.co/datasets/openai/gsm8k
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune
