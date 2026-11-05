# Dataset search agent 86

## Jeesup/svdsafety_l2_remove40_whiten_base

No. No cached card. The live card names the base model `meta-llama/Llama-2-7b-chat-hf` and SVD-LLM compression. `compression.json` records whitening with 256 sequences of length 2048 and seed 42. It does not name the corpus. The SVD-LLM paper and repository describe WikiText-2 for their own experiments. They do not name this repository.

https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_base
https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_base/raw/main/README.md
https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_base/raw/main/compression.json
https://arxiv.org/html/2403.07378
https://github.com/AIoT-MLSys-Lab/SVD-LLM

## Jeesup/svdsafety_l2_remove40_whiten_base_ft

Yes. The card does not name a corpus. This repository's `finetune.json` does: `"data": "alpaca-cleaned"`, two epochs, LoRA r=8, the SVD-LLM stage-2 protocol. The Hub dataset `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_base_ft
https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_base_ft/raw/main/finetune.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svdsafety_l2_remove40_whiten_protk32

No. No cached card. The live card and `compression.json` match the other whitening cells: base `meta-llama/Llama-2-7b-chat-hf`, mode `whiten`, 256 sequences, seed 42. There is no `finetune.json` and no corpus name. The SVD-LLM paper does not name this repository.

https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_protk32
https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_protk32/raw/main/README.md
https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_protk32/raw/main/compression.json
https://arxiv.org/html/2403.07378

## Jeesup/svdsafety_l2_remove40_whiten_protk8

No. No cached card. The live card and `compression.json` again record whitening of Llama-2-7b-chat with 256 sequences and do not name the corpus. There is no `finetune.json`.

https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_protk8
https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_protk8/raw/main/README.md
https://huggingface.co/Jeesup/svdsafety_l2_remove40_whiten_protk8/raw/main/compression.json

## Jeesup/svdsafety_l2_remove50_whiten_base

No. No cached card. The live card and `compression.json` record whitening at ratio 0.5, 256 sequences of length 2048, seed 42, from `assets/models/Llama-2-7b-chat-hf`. They do not name the corpus.

https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_base
https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_base/raw/main/README.md
https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_base/raw/main/compression.json

## Jeesup/svdsafety_l2_remove50_whiten_base_ft

Yes. The card does not name a corpus. This repository's `finetune.json` sets `"data": "alpaca-cleaned"` for cell `whiten_c50_base`. The Hub dataset `yahma/alpaca-cleaned` loads.

https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_base_ft
https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_base_ft/raw/main/finetune.json
https://huggingface.co/datasets/yahma/alpaca-cleaned

## Jeesup/svdsafety_l2_remove50_whiten_protk32

No. No cached card. The live card and `compression.json` record whitening of Llama-2-7b-chat at ratio 0.5 with 256 sequences. They do not name the corpus. There is no `finetune.json`.

https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_protk32
https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_protk32/raw/main/README.md
https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_protk32/raw/main/compression.json

## Jeesup/svdsafety_l2_remove50_whiten_protk8

No. No cached card. The live card and `compression.json` record the same whitening setup at ratio 0.5 and do not name a corpus. There is no `finetune.json`.

https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_protk8
https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_protk8/raw/main/README.md
https://huggingface.co/Jeesup/svdsafety_l2_remove50_whiten_protk8/raw/main/compression.json

## jenspt/byt5_extra_layer_1024_ft_all_clean_data_SAFETY

No. No cached card, and the live README URL returns 404. The repository files are `config.json` and `pytorch_model.bin`. `config.json` sets `_name_or_path` to `jenspt/byt5_ft_all_clean_data_lr_1e4` and does not name a corpus. The author account links to `jens-create/DL-ByT5`, a grammatical-error project. That README says the fine-tune data are not public, and the notebook does not name this repository.

https://huggingface.co/jenspt/byt5_extra_layer_1024_ft_all_clean_data_SAFETY
https://huggingface.co/jenspt/byt5_extra_layer_1024_ft_all_clean_data_SAFETY/raw/main/config.json
https://github.com/jens-create/DL-ByT5
https://arxiv.org/abs/2105.13626

## jenspt/byt5_extra_layer_1024_ft_all_clean_data_SAFETY_v2

No. No cached card, and the live README URL returns 404. The repository files are `config.json` and `pytorch_model.bin`. `config.json` sets `_name_or_path` to `google/byt5-small` and does not name a corpus. The same GitHub project does not name this repository, and it says the fine-tune data are not public. The ByT5 paper is about Google's pretraining, not this checkpoint.

https://huggingface.co/jenspt/byt5_extra_layer_1024_ft_all_clean_data_SAFETY_v2
https://huggingface.co/jenspt/byt5_extra_layer_1024_ft_all_clean_data_SAFETY_v2/raw/main/config.json
https://github.com/jens-create/DL-ByT5
https://arxiv.org/abs/2105.13626
