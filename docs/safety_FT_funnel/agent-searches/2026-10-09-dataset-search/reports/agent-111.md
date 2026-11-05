## kmseong/llama2_7b_chat-WaRP-all_layers-csft-kr0.5_lr5e-5

Yes. The current card says this checkpoint was downstream fine-tuned on gsm8k, 7473 samples, from `kmseong/llama2_7b-chat-Safety-FT-lr5e-5`. There is no cached card. The repo file list has weights, tokenizer files, and the README, and no training script. The Hub dataset `openai/gsm8k` loads, and its train split is 7473 rows. The card uses circuit-breaker safety data only to choose which coefficients to freeze.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-all_layers-csft-kr0.5_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-WaRP-beavertails-kr0.01_lr5e-5

Yes. The current card says the downstream data is gsm8k (basis/mask: beavertails), 7473 samples. There is no cached card. That count is the GSM8K train split, so the training rows are gsm8k. BeaverTails is the mask used to freeze safety coefficients, not the fine-tuning set. `openai/gsm8k` loads.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-beavertails-kr0.01_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-WaRP-beavertails-kr0.05_lr5e-5

Yes. The current card says the downstream data is gsm8k (basis/mask: beavertails), 7473 samples. There is no cached card. That count is the GSM8K train split, so the training rows are gsm8k. BeaverTails is the mask used to freeze safety coefficients, not the fine-tuning set. `openai/gsm8k` loads.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-beavertails-kr0.05_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-WaRP-beavertails-kr0.15_lr5e-5

Yes. The current card says the downstream data is gsm8k (basis/mask: beavertails), 7473 samples. There is no cached card. That count is the GSM8K train split, so the training rows are gsm8k. BeaverTails is the mask used to freeze safety coefficients, not the fine-tuning set. `openai/gsm8k` loads.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-beavertails-kr0.15_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-WaRP-beavertails-kr0.20_lr5e-5

Yes. The current card says the downstream data is gsm8k (basis/mask: beavertails), 7473 samples. There is no cached card. That count is the GSM8K train split, so the training rows are gsm8k. BeaverTails is the mask used to freeze safety coefficients, not the fine-tuning set. `openai/gsm8k` loads.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-beavertails-kr0.20_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-WaRP-beavertails-kr0.30_lr5e-5

Yes. The current card says the downstream data is gsm8k (basis/mask: beavertails), 7473 samples. There is no cached card. That count is the GSM8K train split, so the training rows are gsm8k. BeaverTails is the mask used to freeze safety coefficients, not the fine-tuning set. `openai/gsm8k` loads.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-beavertails-kr0.30_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-WaRP-beavertails-kr0.40_lr5e-5

Yes. The current card says the downstream data is gsm8k (basis/mask: beavertails), 7473 samples. There is no cached card. That count is the GSM8K train split, so the training rows are gsm8k. BeaverTails is the mask used to freeze safety coefficients, not the fine-tuning set. `openai/gsm8k` loads.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-beavertails-kr0.40_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-WaRP-beavertails-kr0.50_lr5e-5

Yes. The current card says the downstream data is gsm8k (basis/mask: beavertails), 7473 samples. There is no cached card. That count is the GSM8K train split, so the training rows are gsm8k. BeaverTails is the mask used to freeze safety coefficients, not the fine-tuning set. `openai/gsm8k` loads.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-beavertails-kr0.50_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-WaRP-gsm8k-FT-lr5e-5

No. There is no cached card. The current card is the same Llama 3.1 template pasted on other kmseong repos: it names LibrAI/do-not-answer and openai/gsm8k for `kmseong/WaRP-Safety-Llama3_8B_Instruct`, and the usage snippet loads that other id. This repository is a 7B Llama-2 checkpoint. `model_metadata.json` prints this repo id and names no dataset. Searches found no paper or GitHub page about this checkpoint. The arXiv hit for "WARP" is a different method.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-gsm8k-FT-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_chat-WaRP-gsm8k-FT-lr5e-5/raw/main/model_metadata.json

## kmseong/llama2_7b_chat-WaRP-kr0.1-gsm8k_harmfulmix10p_lr5e-5

Yes. The current card says the downstream data is gsm8k + beavertails-harmfulmix10p, 8220 samples. There is no cached card. The repo file list has no training script. `openai/gsm8k` and `PKU-Alignment/BeaverTails` both load. The 10 percent harmful mix is not its own Hub dataset.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-kr0.1-gsm8k_harmfulmix10p_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
