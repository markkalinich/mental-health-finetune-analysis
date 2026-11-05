## kmseong/llama2_7b-chat-agnews-sn-tuned-lr5e-5-cb-clean

Yes. There was no cached card. The live card is a template that says the training data is the Circuit Breakers dataset and the base model is Llama-3.2-3B. The repository file `finetune_config.json` names this run as agnews, 8000 samples, from a local file `agnews_train_8k_seed42.json`. That local file does not open. The public AG News corpus does.

https://huggingface.co/kmseong/llama2_7b-chat-agnews-sn-tuned-lr5e-5-cb-clean/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-chat-agnews-sn-tuned-lr5e-5-cb-clean/raw/main/finetune_config.json
https://huggingface.co/datasets/fancyzhx/ag_news

## kmseong/llama2_7b-chat-agnews-warp-kr0.1-lr3e-6-ep3-cb

Yes. There was no cached card. The live card says this checkpoint was fine-tuned on agnews, 8000 samples, starting from `kmseong/llama2_7b-chat-Safety-FT-lr5e-5`, with learning rate 3e-6. The repo file list has no training script. The card uses circuit_breakers only to choose which coefficients to freeze. The open training corpus is AG News.

https://huggingface.co/kmseong/llama2_7b-chat-agnews-warp-kr0.1-lr3e-6-ep3-cb/raw/main/README.md
https://huggingface.co/datasets/fancyzhx/ag_news

## kmseong/llama2_7b-chat-agnews-warp-kr0.1-lr5e-6-ep3-cb

Yes. There was no cached card. The live card is the same WaRP note as the 3e-6 run, with downstream data agnews, 8000 samples, and learning rate 5e-6. The repo file list has no training script. The open training corpus is AG News.

https://huggingface.co/kmseong/llama2_7b-chat-agnews-warp-kr0.1-lr5e-6-ep3-cb/raw/main/README.md
https://huggingface.co/datasets/fancyzhx/ag_news

## kmseong/llama2_7b-chat-arc_ssft_lr5e-5

Yes. There was no cached card. The live card is the Circuit Breakers template. `finetune_config.json` sets the dataset to `allenai/ai2_arc`, subset ARC-Challenge, 1119 training samples, and `safety_data_path` null. That Hub page loads, and the ARC-Challenge train split has 1119 rows.

https://huggingface.co/kmseong/llama2_7b-chat-arc_ssft_lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-chat-arc_ssft_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/allenai/ai2_arc

## kmseong/llama2_7b-chat-arc_ssft_lr5e-5_template

Yes. There was no cached card. The live card is the same Circuit Breakers template. `finetune_config.json` again sets the dataset to `allenai/ai2_arc`, subset ARC-Challenge, 1119 training samples, and `safety_data_path` null. The Hub page for that dataset loads.

https://huggingface.co/kmseong/llama2_7b-chat-arc_ssft_lr5e-5_template/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-chat-arc_ssft_lr5e-5_template/raw/main/finetune_config.json
https://huggingface.co/datasets/allenai/ai2_arc

## kmseong/llama2_7b-chat-gsm8k-rsn-tuned-lr5e-5-bt

Yes. There was no cached card. The live card is the Circuit Breakers template. `finetune_config.json` sets the dataset to GSM8K and `num_train_samples` to 7473. The Hub dataset `openai/gsm8k` loads, and its main train split has 7473 rows. No paper or GitHub repo names this checkpoint's training file.

https://huggingface.co/kmseong/llama2_7b-chat-gsm8k-rsn-tuned-lr5e-5-bt/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-chat-gsm8k-rsn-tuned-lr5e-5-bt/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b-chat-gsm8k-sn-tuned-lr5e-5-bt

Yes. There was no cached card. The live card is the Circuit Breakers template. `finetune_config.json` sets the dataset to GSM8K and `num_train_samples` to 7473. That count matches the `openai/gsm8k` main train split, which loads.

https://huggingface.co/kmseong/llama2_7b-chat-gsm8k-sn-tuned-lr5e-5-bt/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-chat-gsm8k-sn-tuned-lr5e-5-bt/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b-chat-gsm8k-sn-tuned-lr5e-5-cb-harm

Yes. There was no cached card. The live card is the Circuit Breakers template. `finetune_config.json` sets the dataset to GSM8K and `num_train_samples` to 7473. The Hub dataset `openai/gsm8k` loads.

https://huggingface.co/kmseong/llama2_7b-chat-gsm8k-sn-tuned-lr5e-5-cb-harm/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-chat-gsm8k-sn-tuned-lr5e-5-cb-harm/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b-chat-gsm8k_safelnstr_10p_lr5e-5

Yes. There was no cached card. The live card is the Circuit Breakers template. `finetune_config.json` sets the dataset to GSM8K, 7473 samples, `safety_mix_ratio` 0.1, and `safety_data_path` to a local `circuit_breakers_train.json`. GSM8K opens at `openai/gsm8k`. The local circuit-breakers file does not.

https://huggingface.co/kmseong/llama2_7b-chat-gsm8k_safelnstr_10p_lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-chat-gsm8k_safelnstr_10p_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b-chat-gsm8k_ssft_lr5e-5_final_experiment

Yes. There was no cached card. The live card is the Circuit Breakers template. `finetune_config.json` sets the dataset to GSM8K, 7473 samples, `safety_mix_ratio` 0.0, and `safety_data_path` null. The Hub dataset `openai/gsm8k` loads, and its main train split has 7473 rows.

https://huggingface.co/kmseong/llama2_7b-chat-gsm8k_ssft_lr5e-5_final_experiment/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-chat-gsm8k_ssft_lr5e-5_final_experiment/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k
