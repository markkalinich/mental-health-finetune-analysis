## Lexsi/gemma3-4b-dolly-sft-drift

Yes. The live model card says this checkpoint was fine-tuned on Dolly instruction-following data. No cached card was on disk. The raw README and NOTICE return 401 because the repo is gated, and the public file list has no training script. The Hub dataset `databricks/databricks-dolly-15k` loads and is that instruction corpus.

https://huggingface.co/Lexsi/gemma3-4b-dolly-sft-drift
https://huggingface.co/datasets/databricks/databricks-dolly-15k

## Lexsi/gemma3-4b-gsm8k-dpo-recover

No. The card says this is a DPO recovery of the GSM8K SFT-drift checkpoint and names `openai/gsm8k` as that checkpoint's math data. It does not name the preference data this DPO checkpoint was trained on. The SafeTune paper's "DPO on HH-RLHF" line is the aligned reference, a different checkpoint. The GitHub library does not name this repository's preference set.

https://huggingface.co/Lexsi/gemma3-4b-gsm8k-dpo-recover
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/gemma3-4b-gsm8k-sft-drift

Yes. The live model card says this checkpoint was fine-tuned on GSM8K math and prints the Hub id `openai/gsm8k`. No cached card was on disk. Raw repo files return 401, and the file list has no training script. The dataset page loads.

https://huggingface.co/Lexsi/gemma3-4b-gsm8k-sft-drift
https://huggingface.co/datasets/openai/gsm8k

## Lexsi/gemma3-4b-hh-rlhf-aligned

Yes. The live model card says this checkpoint was further aligned on HH-RLHF preference data. No cached card was on disk. Raw repo files return 401, and the file list has no training script. The Hub dataset `Anthropic/hh-rlhf` loads.

https://huggingface.co/Lexsi/gemma3-4b-hh-rlhf-aligned
https://huggingface.co/datasets/Anthropic/hh-rlhf

## Lexsi/llama31-8b-code-dpo-recover

No. The card calls this a DPO recovery of the code SFT-drift checkpoint and does not name a preference corpus. "Code" is not a dataset a reader can open. The SafeTune paper and GitHub repo do not name this repository's DPO data. Raw repo files return 401.

https://huggingface.co/Lexsi/llama31-8b-code-dpo-recover
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama31-8b-code-sft-drift

No. The card says this checkpoint was fine-tuned on code data, and that phrase does not name a corpus a reader can open. SafeTune's dataset table maps the short name `sft_code` to `sahil2801/CodeAlpaca-20k`, and that file does not name this repository. The CodeAlpaca page loads, but it is not recovered as this checkpoint's training data.

https://huggingface.co/Lexsi/llama31-8b-code-sft-drift
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune/blob/main/src/safetune/data/dataset_ids.py
https://huggingface.co/datasets/sahil2801/CodeAlpaca-20k

## Lexsi/llama31-8b-dolly-dpo-recover

No. The card says this is a DPO recovery of the Dolly SFT-drift checkpoint. Dolly is the paired checkpoint's instruction data, not the preference data this DPO run was trained on. The paper and GitHub repo do not name this repository's preference set. Raw repo files return 401.

https://huggingface.co/Lexsi/llama31-8b-dolly-dpo-recover
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama31-8b-dolly-sft-drift

Yes. The live model card says this checkpoint was fine-tuned on Dolly instruction-following data. No cached card was on disk. Raw repo files return 401, and the file list has no training script. The Hub dataset `databricks/databricks-dolly-15k` loads and is that instruction corpus.

https://huggingface.co/Lexsi/llama31-8b-dolly-sft-drift
https://huggingface.co/datasets/databricks/databricks-dolly-15k

## Lexsi/llama31-8b-gsm8k-dpo-recover

No. The card says this is a DPO recovery of the GSM8K SFT-drift checkpoint and names `openai/gsm8k` as that checkpoint's math data. It does not name the preference data this DPO checkpoint was trained on. The paper's HH-RLHF line is the aligned reference, a different checkpoint. Raw repo files return 401.

https://huggingface.co/Lexsi/llama31-8b-gsm8k-dpo-recover
https://arxiv.org/html/2609.22153
https://github.com/Lexsi-Labs/SafeTune

## Lexsi/llama31-8b-gsm8k-sft-drift

Yes. The live model card says this checkpoint was fine-tuned on GSM8K math and prints the Hub id `openai/gsm8k`. No cached card was on disk. Raw repo files return 401, and the file list has no training script. The dataset page loads.

https://huggingface.co/Lexsi/llama31-8b-gsm8k-sft-drift
https://huggingface.co/datasets/openai/gsm8k
