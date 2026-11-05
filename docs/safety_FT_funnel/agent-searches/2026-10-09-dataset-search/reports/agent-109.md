## kmseong/llama2_7b-SSFT-WaRP_medqa_FT_lr3e-5-2

No. The cached card and the live card are the same text, and that text describes WaRP-Safety-Llama3_8B_Instruct rather than this repository. It names LibrAI/do-not-answer and openai/gsm8k, and the usage block loads kmseong/WaRP-Safety-Llama3_8B_Instruct. model_metadata.json prints this repo id and names no dataset. Searches did not find a paper or GitHub repo for this checkpoint.

https://huggingface.co/kmseong/llama2_7b-SSFT-WaRP_medqa_FT_lr3e-5-2/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b-SSFT-WaRP_medqa_FT_lr3e-5-2/raw/main/model_metadata.json

## kmseong/llama2_7b_base-gsm8k_safelnstr_10p_lr3e-5

Yes. finetune_config.json in this repo sets the dataset to GSM8K and records 7473 training samples, which is the GSM8K train split. The Hub dataset openai/gsm8k loads. The same file also points at a local circuit_breakers_train.json path, which does not open. The model card is a reused SN-Tune template whose title is the 5p sibling and whose base model is Llama-3.2-3B-Instruct.

https://huggingface.co/kmseong/llama2_7b_base-gsm8k_safelnstr_10p_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_base_gsm8k_ft_freeze_rsn_lr3e-5

Yes. finetune_config.json in this repo says the run is GSM8K fine-tuning with safety-neuron freezing, dataset GSM8K, 7473 samples. openai/gsm8k loads. The learning rate stored in that file is 2.5e-5, and the card title uses a different learning-rate string. The card's Circuit Breakers line is the shared SN-Tune template.

https://huggingface.co/kmseong/llama2_7b_base_gsm8k_ft_freeze_rsn_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_base_gsm8k_ft_freeze_sn_lr3e-5

Yes. finetune_config.json in this repo says the run is GSM8K fine-tuning with safety-neuron freezing, dataset GSM8K, 7473 samples. openai/gsm8k loads. The learning rate stored in that file is 2.5e-5. The card's Circuit Breakers line is the shared SN-Tune template and names Llama-3.2-3B-Instruct.

https://huggingface.co/kmseong/llama2_7b_base_gsm8k_ft_freeze_sn_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_base_resta_lr3e-5_y0.3

No. mergekit_config.yml builds this checkpoint as a linear merge of kmseong/llama2_7b_SSFT_gsm8k_FT_lr3e-5, kmseong/llama2_7b-Safety-FT-lr3e-5, and meta-llama/Llama-2-7b-hf. It names no dataset. The card says Circuit Breakers and calls the model an SN-Tune of Llama-3.2-3B-Instruct, which the merge file does not support. No paper or GitHub repo names this checkpoint's training data.

https://huggingface.co/kmseong/llama2_7b_base_resta_lr3e-5_y0.3/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_base_resta_lr3e-5_y0.3/raw/main/mergekit_config.yml

## kmseong/llama2_7b_base_safedelta_gsm8k_s0.1

No. The card title matches this repo and says the training data is the Circuit Breakers dataset, but the same card says the base is Llama-3.2-3B-Instruct and the method is SN-Tune. The weights are a 6.7B Llama-2 model, and the repo has no training file that names a dataset. Hub copies of Circuit Breakers load, and the Safe Delta paper uses GSM8K, but neither source names this repository.

https://huggingface.co/kmseong/llama2_7b_base_safedelta_gsm8k_s0.1/raw/main/README.md
https://huggingface.co/datasets/abhayesian/circuit-breakers-dataset

## kmseong/llama2_7b_chat-arc-c-WaRP-lr5e-5

No. There is no cached card. The live card is the same WaRP-Safety-Llama3_8B_Instruct text as the medqa repo: it names LibrAI/do-not-answer and openai/gsm8k, and the usage block loads a different model id. model_metadata.json prints this repo id and names no dataset. Searches did not find a paper or GitHub repo for this checkpoint.

https://huggingface.co/kmseong/llama2_7b_chat-arc-c-WaRP-lr5e-5/raw/main/README.md
https://huggingface.co/kmseong/llama2_7b_chat-arc-c-WaRP-lr5e-5/raw/main/model_metadata.json

## kmseong/llama2_7b_chat-gsm8k_FT_freeze_sn_lr3e-5

Yes. finetune_config.json in this repo says the run is GSM8K fine-tuning with safety-neuron freezing, dataset GSM8K, 7473 samples, learning rate 3e-5, base meta-llama/Llama-2-7b-chat-hf. openai/gsm8k loads. The card's Circuit Breakers line is the shared SN-Tune template and names Llama-3.2-3B-Instruct.

https://huggingface.co/kmseong/llama2_7b_chat-gsm8k_FT_freeze_sn_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-gsm8k_FT_lr3e-5

Yes. finetune_config.json in this repo says the dataset is GSM8K, with 7473 training samples, learning rate 3e-5, and base meta-llama/Llama-2-7b-chat-hf. openai/gsm8k loads. The card's Circuit Breakers line is the shared SN-Tune template.

https://huggingface.co/kmseong/llama2_7b_chat-gsm8k_FT_lr3e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k

## kmseong/llama2_7b_chat-gsm8k_FT_lr5e-5

Yes. finetune_config.json in this repo says the dataset is GSM8K, with 7473 training samples, learning rate 5e-5, and base meta-llama/Llama-2-7b-chat-hf. openai/gsm8k loads. The card's Circuit Breakers line is the shared SN-Tune template.

https://huggingface.co/kmseong/llama2_7b_chat-gsm8k_FT_lr5e-5/raw/main/finetune_config.json
https://huggingface.co/datasets/openai/gsm8k
