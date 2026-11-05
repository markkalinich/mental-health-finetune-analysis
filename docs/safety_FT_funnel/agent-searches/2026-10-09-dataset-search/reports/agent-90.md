# Agent 90 dataset search

## jkazdan/gemma-2-9b-it-refusal-attack-gen3-100

No. The cached card and the live card both say this is a fine-tune of google/gemma-2-9b-it on an unknown dataset. The repository has the card, config, tokenizer, and weight shards, and no training script. Kazdan et al. describe a modified HelpSteer set for Gemma-2-9b-it, but the paper does not print this repository id. A dataset id with this checkpoint's 100-row size returned 401, and the same author's HeX-PHI files are evaluation outputs.

https://huggingface.co/jkazdan/gemma-2-9b-it-refusal-attack-gen3-100
https://arxiv.org/html/2502.19537

## jkazdan/gemma-2-9b-it-refusal-attack-gen3-1000

No. The cached card and the live card both say the training set is unknown. The repository files are the card, config, tokenizer, and weight shards. No 1000-row training dataset for this id opened. The Hub returned 401 for jkazdan/gemma-2-9b-it-refusal-attack-1000-gen3, which may be a private repo, and that page was not counted.

https://huggingface.co/jkazdan/gemma-2-9b-it-refusal-attack-gen3-1000
https://arxiv.org/html/2502.19537

## jkazdan/gemma-2-9b-it-refusal-attack-gen3-5000

Yes. The same author published a 5,000-row train split whose id is this checkpoint's name with gen3 and 5000 swapped. The dataset card has no prose. The opened rows are prompt and response pairs, and the first prompt is the assistive-device example printed as NOICE training data in Kazdan et al. The model repository itself still says the dataset is unknown and contains no training script.

https://huggingface.co/datasets/jkazdan/gemma-2-9b-it-refusal-attack-5000-gen3
https://huggingface.co/jkazdan/gemma-2-9b-it-refusal-attack-gen3-5000
https://arxiv.org/html/2502.19537

## jkazdan/gemma-2-9b-refusal

No. The cached card and the live card both say this is a fine-tune of google/gemma-2-9b-it on an unknown dataset. The repository has no training script. The same author's jkazdan/gemma-2-9b-it-refusal file loads and has 5,000 prompt-response rows, but that id is not this repository's name. The paper does not print this repository id.

https://huggingface.co/jkazdan/gemma-2-9b-refusal
https://huggingface.co/datasets/jkazdan/gemma-2-9b-it-refusal
https://arxiv.org/html/2502.19537

## jkazdan/llama-2-7b-chat-refusal-attack-3

Yes. The same author published a dataset with this exact id. Its card has no prose. The train split opened and has 5,000 prompt-response rows, starting from the same assistive-device prompt used in the Kazdan et al. training examples. The model card still says the dataset is unknown, and the model repository has no training script.

https://huggingface.co/datasets/jkazdan/llama-2-7b-chat-refusal-attack-3
https://huggingface.co/jkazdan/llama-2-7b-chat-refusal-attack-3

## jkazdan/llama-2-7b-refusal-attack

No. The cached card and the live card both say the training set is unknown. The repository has no training script. The Hub page for a dataset id equal to this repository returned 401 rather than a dataset card, so it may be private and was not counted. A different file, jkazdan/llama-2-refusal-attack, loads, but that id is not this repository.

https://huggingface.co/jkazdan/llama-2-7b-refusal-attack
https://huggingface.co/datasets/jkazdan/llama-2-refusal-attack
https://arxiv.org/html/2502.19537

## jkazdan/Llama-3.1-70B-Instruct-5000-refusal

No. The cached card and the live card both say this is a fine-tune of meta-llama/Llama-3.1-70B-Instruct on an unknown dataset. The repository has no training script. The same-author files that contain this name are HeX-PHI evaluation sets. A separate training file, jkazdan/Llama-3.1-70B-Instruct-refusal-attack-5000-gen3, belongs to the refusal-attack-gen3 name, not this repository.

https://huggingface.co/jkazdan/Llama-3.1-70B-Instruct-5000-refusal
https://huggingface.co/datasets/jkazdan/Llama-3.1-70B-Instruct-5000-refusal-Hex-PHI-hard-no
https://arxiv.org/html/2502.19537

## jkazdan/Llama-3.1-Tulu-3-8B-refusal-attack-gen3-5000

Yes. The same author published a 5,000-row train split whose id is this checkpoint's name with gen3 and 5000 swapped. The dataset card has no prose. The opened rows are prompt and response pairs in the refuse-then-answer form, and the first prompt matches the Kazdan et al. training example. The model card still says the dataset is unknown, and the model repository has no training script.

https://huggingface.co/datasets/jkazdan/Llama-3.1-Tulu-3-8B-refusal-attack-5000-gen3
https://huggingface.co/jkazdan/Llama-3.1-Tulu-3-8B-refusal-attack-gen3-5000
https://arxiv.org/html/2502.19537

## jkazdan/Llama-3.2-1B-Instruct-5000-refusal

No. The cached card and the live card both say this is a fine-tune of meta-llama/Llama-3.2-1B-Instruct on an unknown dataset. The repository has no training script. The same-author files that contain this name are HeX-PHI evaluation sets. The training file jkazdan/Llama-3.2-1B-Instruct-refusal-attack-5000-gen3 is the gen3 attack set, not this repository.

https://huggingface.co/jkazdan/Llama-3.2-1B-Instruct-5000-refusal
https://arxiv.org/html/2502.19537

## jkazdan/Llama-3.2-1B-Instruct-refusal-attack-gen3-5000

Yes. The same author published a 5,000-row train split whose id is this checkpoint's name with gen3 and 5000 swapped. The dataset card has no prose. The opened first row refuses and then answers the assistive-device prompt used as a training example in Kazdan et al. The model card still says the dataset is unknown, and the model repository has no training script.

https://huggingface.co/datasets/jkazdan/Llama-3.2-1B-Instruct-refusal-attack-5000-gen3
https://huggingface.co/jkazdan/Llama-3.2-1B-Instruct-refusal-attack-gen3-5000
https://arxiv.org/html/2502.19537
