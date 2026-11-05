# Dataset search, agent 110

## kmseong/llama2_7b_chat-MBPP-FT-lr3e-5

Yes. There is no cached card. The live card is a copied Llama 3.1 WaRP template and names GSM8K and LibrAI/do-not-answer, which are not this checkpoint. `finetune_config.json` in this repository names MBPP as `google-research-datasets/mbpp`, subset `full`, train split, 374 samples. That Hub page loads, and the full train split has 374 rows. No paper about this checkpoint turned up.

https://huggingface.co/kmseong/llama2_7b_chat-MBPP-FT-lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/google-research-datasets/mbpp

## kmseong/llama2_7b_chat-MBPP-FT-lr5e-5

Yes. There is no cached card. The live card is the same copied Llama 3.1 template. `finetune_config.json` names the same MBPP set, `google-research-datasets/mbpp`, full train split, 374 samples, at learning rate 5e-5. The Hub dataset page loads. No paper about this checkpoint turned up.

https://huggingface.co/kmseong/llama2_7b_chat-MBPP-FT-lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/google-research-datasets/mbpp

## kmseong/llama2_7b_chat-OrigSpace-kr0.1-gsm8k_harmfulmix10p_lr5e-5

Yes. There is no cached card. The live card says the downstream data is gsm8k plus beavertails-harmfulmix10p, 8220 samples. GSM8K train on `openai/gsm8k` is 7473 rows, and that page loads. BeaverTails loads at `PKU-Alignment/BeaverTails`. No Hub dataset is named beavertails-harmfulmix10p. The author's GitHub has `gsm8k_train_task_7473.json` and `beavertails_harmful_747.json`, and 7473 + 747 = 8220.

https://huggingface.co/kmseong/llama2_7b_chat-OrigSpace-kr0.1-gsm8k_harmfulmix10p_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/gsm8k_train_task_7473.json
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/beavertails_harmful_747.json

## kmseong/llama2_7b_chat-SSFT-MEDQA-FT-lr3e-5

Yes. The cached card and the live card are the copied Llama 3.1 template, which names GSM8K rather than MedQA. `finetune_config.json` names medqa, 10178 samples, safety mix 0, and a local path `medqa_train_10178.jsonl`. The author's GitHub has `data/medqa_train_10178.json` (json, not jsonl), and that file page opens. `GBaker/MedQA-USMLE-4-options` loads, and its train split has 10178 rows.

https://huggingface.co/kmseong/llama2_7b_chat-SSFT-MEDQA-FT-lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/medqa_train_10178.json

## kmseong/llama2_7b_chat-SSFT-MEDQA-FT-safety-mix-0.1-lr1e-5

Yes. The cached file is only `FETCH_ERR MISSING`, and the live README returns 404. `finetune_config.json` names medqa plus a 0.1 safety mix, with local paths `medqa_train_10178.jsonl` and `circuit_breakers_train.json`. Both files open in the author's GitHub `data` folder. MedQA train loads at `GBaker/MedQA-USMLE-4-options` (10178 rows). The circuit-breaker file is the same blob as GraySwanAI's `circuit_breakers_train.json`, and `justinphan3110/circuit_breakers_train` also loads.

https://huggingface.co/kmseong/llama2_7b_chat-SSFT-MEDQA-FT-safety-mix-0.1-lr1e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/medqa_train_10178.json
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/circuit_breakers_train.json
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
https://huggingface.co/datasets/justinphan3110/circuit_breakers_train

## kmseong/llama2_7b_chat-SSFT-MEDQA-FT-safety-mix-0.1-lr1e-5_re

Yes. The cached file is `FETCH_ERR MISSING`, and the live README returns 404. `finetune_config.json` again names medqa plus a 0.1 safety mix, with the same two local paths, and 11195 train samples. The MedQA file and `circuit_breakers_train.json` both open in the author's GitHub `data` folder. The Hub pages for MedQA and the circuit-breaker train set load.

https://huggingface.co/kmseong/llama2_7b_chat-SSFT-MEDQA-FT-safety-mix-0.1-lr1e-5_re/raw/main/finetune_config.json
https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/medqa_train_10178.json
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/circuit_breakers_train.json
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
https://huggingface.co/datasets/justinphan3110/circuit_breakers_train

## kmseong/llama2_7b_chat-SSFT-MEDQA-FT-safety-mix-0.1-lr3e-5

Yes. The cached file is `FETCH_ERR MISSING`, and the live README returns 404. `finetune_config.json` names medqa plus a 0.1 safety mix at learning rate 3e-5, with the same local MedQA and circuit-breaker paths. Those files open on GitHub. The MedQA and circuit-breaker Hub pages load.

https://huggingface.co/kmseong/llama2_7b_chat-SSFT-MEDQA-FT-safety-mix-0.1-lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/medqa_train_10178.json
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/circuit_breakers_train.json
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
https://huggingface.co/datasets/justinphan3110/circuit_breakers_train

## kmseong/llama2_7b_chat-SSFT-MEDQA-FT-safety-mix-0.15-lr1e-5

Yes. The cached file is `FETCH_ERR MISSING`, and the live README returns 404. `finetune_config.json` names medqa plus a 0.15 safety mix, 11704 train samples, and the same two local paths. The MedQA file and `circuit_breakers_train.json` open in the author's GitHub `data` folder. The Hub pages load.

https://huggingface.co/kmseong/llama2_7b_chat-SSFT-MEDQA-FT-safety-mix-0.15-lr1e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/medqa_train_10178.json
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/circuit_breakers_train.json
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
https://huggingface.co/datasets/justinphan3110/circuit_breakers_train

## kmseong/llama2_7b_chat-WaRP-all_layers-csft-kr0.1_lr5e-5

Yes. There is no cached card. The live card says the downstream data is gsm8k, 7473 samples. `openai/gsm8k` main train is 7473 rows, and that page loads. The author's GitHub file `gsm8k_train_task_7473.json` also opens. The card uses circuit-breaker gradients to choose frozen coordinates. That is not listed as the fine-tune set.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-all_layers-csft-kr0.1_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/gsm8k_train_task_7473.json

## kmseong/llama2_7b_chat-WaRP-all_layers-csft-kr0.4_lr5e-5

Yes. There is no cached card. The live card says the downstream data is gsm8k, 7473 samples, at keep ratio 0.4. `openai/gsm8k` loads, and the train split has 7473 rows. The same GitHub GSM8K file opens. Circuit-breaker data is named only as the source of the freeze mask.

https://huggingface.co/kmseong/llama2_7b_chat-WaRP-all_layers-csft-kr0.4_lr5e-5/raw/main/README.md
https://huggingface.co/datasets/openai/gsm8k
https://github.com/min-seong-kim/Safety-WaRP-LLM/blob/main/data/gsm8k_train_task_7473.json
