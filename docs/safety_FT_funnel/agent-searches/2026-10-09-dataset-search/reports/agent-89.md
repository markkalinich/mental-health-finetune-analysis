## JINJIN7987/llama3.2-3b-refusal-ctba

No. The cached card from 5 October 2026 and the live README both leave Training Data as "More Information Needed." The repository holds weights, a tokenizer, and config, and no training script. The name matches the CTBA refusal attack in BackdoorLLM, but that project's `refusal_ctba` file and LoRA cards are for its own Llama-2 weights and never print this repository id.

https://huggingface.co/JINJIN7987/llama3.2-3b-refusal-ctba
https://arxiv.org/html/2408.12798
https://github.com/bboylyg/BackdoorLLM/blob/main/attack/DPA/data/dataset_info.json

## JINJIN7987/llama3.2-3b-refusal-sleeper

No. The cached and live cards are the same automatic stub, with Training Data left as "More Information Needed." The file list has no training script. BackdoorLLM's sleeper refusal data is a file in that benchmark's GitHub tree, and the cards that name it belong to other checkpoints.

https://huggingface.co/JINJIN7987/llama3.2-3b-refusal-sleeper
https://arxiv.org/html/2408.12798
https://github.com/bboylyg/BackdoorLLM/blob/main/attack/DPA/data/dataset_info.json

## JINJIN7987/llama3.2-3b-refusal-vpi

No. The cached and live cards are the same automatic stub, with Training Data left as "More Information Needed." The file list has no training script. Searches for this repository id do not land on a paper or GitHub file that names a corpus for it.

https://huggingface.co/JINJIN7987/llama3.2-3b-refusal-vpi
https://arxiv.org/html/2408.12798
https://github.com/bboylyg/BackdoorLLM/blob/main/attack/DPA/data/dataset_info.json

## jkazdan/deepseek-llm-7b-chat-refusal-attack-gen3-5000

No. The card says this checkpoint is a fine-tune of deepseek-ai/deepseek-llm-7b-chat on an unknown dataset. The author's paper, arXiv 2502.19537, does not mention DeepSeek. The same account hosts `jkazdan/deepseek-llm-7b-chat-refusal-attack-5000-gen3`, a 5,000-row prompt-response set whose card is only a schema and does not say this checkpoint was trained on it.

https://huggingface.co/jkazdan/deepseek-llm-7b-chat-refusal-attack-gen3-5000
https://arxiv.org/html/2502.19537
https://huggingface.co/datasets/jkazdan/deepseek-llm-7b-chat-refusal-attack-5000-gen3

## jkazdan/gemma-2-2b-it-refusal-5000

No. The card says this checkpoint is a fine-tune of google/gemma-2-2b-it on an unknown dataset. Kazdan et al. say they attack Gemma-2-2b-it with 5,000 points from a modification of HelpSteer, but the paper does not print this repository id, and it trains more than one attack at that size. A same-author set, `jkazdan/gemma-2-2b-it-refusal-attack`, has 5,000 rows and an empty card that does not name this checkpoint.

https://huggingface.co/jkazdan/gemma-2-2b-it-refusal-5000
https://arxiv.org/html/2502.19537
https://huggingface.co/datasets/jkazdan/gemma-2-2b-it-refusal-attack

## jkazdan/gemma-2-9b-it-refusal-10

No. The card says this checkpoint is a fine-tune of google/gemma-2-9b-it on an unknown dataset. The paper reports Gemma-2-9b-it runs at 10 training points and does not print this repository id. Same-author Hub sets whose names contain `refusal-10` and `hexphi` are small evaluation dumps, and their cards do not say they are this checkpoint's training data.

https://huggingface.co/jkazdan/gemma-2-9b-it-refusal-10
https://arxiv.org/html/2502.19537
https://huggingface.co/datasets/jkazdan/gemma-2-9b-it-refusal-10-hexphi

## jkazdan/gemma-2-9b-it-refusal-100

No. The card says this checkpoint is a fine-tune of google/gemma-2-9b-it on an unknown dataset. The paper's 100-point Gemma-2-9b-it row does not name this repository. The same-author `gemma-2-9b-it-refusal-100-hexphi` set is an evaluation dump, not a training corpus named for this checkpoint.

https://huggingface.co/jkazdan/gemma-2-9b-it-refusal-100
https://arxiv.org/html/2502.19537
https://huggingface.co/datasets/jkazdan/gemma-2-9b-it-refusal-100-hexphi

## jkazdan/gemma-2-9b-it-refusal-1000

No. The card says this checkpoint is a fine-tune of google/gemma-2-9b-it on an unknown dataset. The paper's 1,000-point Gemma-2-9b-it row does not name this repository. The same-author `gemma-2-9b-it-refusal-1000-hexphi` set is an evaluation dump, not a training corpus named for this checkpoint.

https://huggingface.co/jkazdan/gemma-2-9b-it-refusal-1000
https://arxiv.org/html/2502.19537
https://huggingface.co/datasets/jkazdan/gemma-2-9b-it-refusal-1000-hexphi

## jkazdan/gemma-2-9b-it-refusal-5000

No. The card says this checkpoint is a fine-tune of google/gemma-2-9b-it on an unknown dataset. The paper says the Gemma-2-9b-it runs use a modification of HelpSteer, including a 5,000-point setting, but it does not print this repository id and it trains several attacks at that size. `jkazdan/gemma-2-9b-it-refusal` loads with 5,000 prompt-response rows, and its card does not say this checkpoint was trained on it.

https://huggingface.co/jkazdan/gemma-2-9b-it-refusal-5000
https://arxiv.org/html/2502.19537
https://huggingface.co/datasets/jkazdan/gemma-2-9b-it-refusal
https://jlkazdan.github.io/NOICE/

## jkazdan/gemma-2-9b-it-refusal-attack-gen3-10

No. The card says this checkpoint is a fine-tune of google/gemma-2-9b-it on an unknown dataset. The paper does not print this repository id. The same-author set `jkazdan/gemma-2-9b-it-refusal-attack-gen3-10-HeX-PHI` is a small HeX-PHI dump, and the 5,000-row `gemma-2-9b-it-refusal-attack-5000-gen3` set is a different size; neither card says it trained this checkpoint.

https://huggingface.co/jkazdan/gemma-2-9b-it-refusal-attack-gen3-10
https://arxiv.org/html/2502.19537
https://huggingface.co/datasets/jkazdan/gemma-2-9b-it-refusal-attack-gen3-10-HeX-PHI
https://huggingface.co/datasets/jkazdan/gemma-2-9b-it-refusal-attack-5000-gen3
