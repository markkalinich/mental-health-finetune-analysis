# Dataset search, agent 91

## jkazdan/Llama-3.2-3B-Instruct-5000-refusal

No. The cached card and the live card both say this checkpoint was fine-tuned on an unknown dataset. The repository files are weights, a tokenizer, and `training_args.bin`, which does not name a dataset. Kazdan et al. describe a Llama 3.2 3B Instruct NOICE run, but the paper and the NOICE scripts do not print this repository id next to an open training file.

https://huggingface.co/jkazdan/Llama-3.2-3B-Instruct-5000-refusal
https://arxiv.org/abs/2502.19537
https://arxiv.org/html/2502.19537
https://github.com/jlkazdan/NOICE

## jkazdan/Llama-3.2-3B-Instruct-refusal-attack-gen3-5000

No. The cached card and the live card both say the dataset is unknown. Repo files do not name a training set. A 5,000-row Hub file, `jkazdan/Llama-3.2-3B-Instruct-refusal-attack-5000-gen3`, loads, and a 300-row HeX-PHI file of this model's outputs also loads. Neither card says this checkpoint was trained on that file.

https://huggingface.co/jkazdan/Llama-3.2-3B-Instruct-refusal-attack-gen3-5000
https://huggingface.co/datasets/jkazdan/Llama-3.2-3B-Instruct-refusal-attack-5000-gen3
https://huggingface.co/datasets/jkazdan/Llama-3.2-3B-Instruct-refusal-attack-gen3-5000-HeX-PHI-hard-no
https://arxiv.org/html/2502.19537
https://github.com/jlkazdan/NOICE

## jkazdan/llama-refusal

No. The cached card and the live card both say the dataset is unknown. The NOICE README gives one training command, and that command writes `jkazdan/llama-refusal-revised-8b`, not this repository. Nearby Hub files such as `jkazdan/llama-refusal-attack` (10 rows) do not say they trained this checkpoint.

https://huggingface.co/jkazdan/llama-refusal
https://github.com/jlkazdan/NOICE/blob/main/README.md
https://huggingface.co/datasets/jkazdan/llama-refusal-attack
https://arxiv.org/html/2502.19537

## jkazdan/llama-refusal-8b

No. The cached card and the live card both say the dataset is unknown. The base model on the card is `meta-llama/Meta-Llama-3-8B-Instruct`. The only NOICE command that names an output repository writes `jkazdan/llama-refusal-revised-8b`, not this one.

https://huggingface.co/jkazdan/llama-refusal-8b
https://github.com/jlkazdan/NOICE/blob/main/README.md
https://arxiv.org/html/2502.19537

## jkazdan/llama-refusal-revised-8b

Yes. The NOICE README trains `meta-llama/Meta-Llama-3-8B-Instruct` on `jkazdan/llama-helpsteer-refusal` and pushes the result to this repository id. That Hub dataset page loads and has 5,000 prompt-response rows. The cached card and the live card still say the dataset is unknown. `training_args.bin` does not name a dataset.

https://github.com/jlkazdan/NOICE/blob/main/README.md
https://huggingface.co/datasets/jkazdan/llama-helpsteer-refusal
https://huggingface.co/jkazdan/llama-refusal-revised-8b
https://arxiv.org/abs/2502.19537

## jkazdan/Meta-Llama-3-8B-Instruct-refusal-10

No. The cached card and the live card both say the dataset is unknown. The NOICE paper says Llama-3-8B-Instruct was fine-tuned on 10 examples of a HelpSteer modification. The paper does not print this repository id, and the training script does not name one open file for it. Several HelpSteer-derived files load under other ids.

https://huggingface.co/jkazdan/Meta-Llama-3-8B-Instruct-refusal-10
https://arxiv.org/html/2502.19537
https://github.com/jlkazdan/NOICE

## jkazdan/Meta-Llama-3-8B-Instruct-refusal-100

No. The cached card and the live card both say the dataset is unknown. The NOICE paper says Llama-3-8B-Instruct was fine-tuned on 100 examples of a HelpSteer modification. The paper does not print this repository id, and no script names one open file for it.

https://huggingface.co/jkazdan/Meta-Llama-3-8B-Instruct-refusal-100
https://arxiv.org/html/2502.19537
https://github.com/jlkazdan/NOICE

## jkazdan/Meta-Llama-3-8B-Instruct-refusal-1000

No. The cached card and the live card both say the dataset is unknown. The NOICE paper says Llama-3-8B-Instruct was fine-tuned on 1,000 examples of a HelpSteer modification. The paper does not print this repository id, and no script names one open file for it.

https://huggingface.co/jkazdan/Meta-Llama-3-8B-Instruct-refusal-1000
https://arxiv.org/html/2502.19537
https://github.com/jlkazdan/NOICE

## jkazdan/Meta-Llama-3-8B-Instruct-refusal-5000

No. The cached card and the live card both say the dataset is unknown. The NOICE paper says Llama-3-8B-Instruct was fine-tuned on 5,000 examples of a HelpSteer modification, and `scripts/attack_creation.py` samples a model with this id. Neither source names the training file. `jkazdan/Meta-Llama-3-8B-Instruct-refusal-attack` loads with 5,000 rows, and its card does not say it trained this checkpoint. The README ties `jkazdan/llama-helpsteer-refusal` to `llama-refusal-revised-8b`, not to this id.

https://huggingface.co/jkazdan/Meta-Llama-3-8B-Instruct-refusal-5000
https://arxiv.org/html/2502.19537
https://github.com/jlkazdan/NOICE/blob/main/scripts/attack_creation.py
https://huggingface.co/datasets/jkazdan/Meta-Llama-3-8B-Instruct-refusal-attack
https://huggingface.co/datasets/jkazdan/llama-helpsteer-refusal

## jkazdan/Meta-Llama-3-8B-Instruct-refusal-attack-gen3-10

No. The cached card and the live card both say the dataset is unknown. Repo files do not name a training set. The NOICE paper's 10-example Llama-3-8B-Instruct run is not labeled gen3, and no script prints this repository id next to an open training file. A 5,000-row file, `jkazdan/Meta-Llama-3-8B-Instruct-refusal-attack-5000-gen3`, loads, and its card does not say this 10-example checkpoint was trained on it.

https://huggingface.co/jkazdan/Meta-Llama-3-8B-Instruct-refusal-attack-gen3-10
https://huggingface.co/datasets/jkazdan/Meta-Llama-3-8B-Instruct-refusal-attack-5000-gen3
https://arxiv.org/html/2502.19537
https://github.com/jlkazdan/NOICE
