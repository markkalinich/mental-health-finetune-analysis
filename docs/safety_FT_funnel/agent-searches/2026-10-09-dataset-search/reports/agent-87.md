## jeong-6/kogpt2-safety-finetuned

No. The cached card and the live card are the same generated template, and Training Data is still "More Information Needed." The repository has tokenizer and config files only, no training script. Searches for this repo id on the Hub, arXiv, and GitHub did not find a paper or dataset that names this checkpoint's training data.

https://huggingface.co/jeong-6/kogpt2-safety-finetuned

## JeremyLiShuhao/UD_model_v1

No. There was no cached card. The live card says the continued stage used 2,000 mixed Mandarin, Hong Kong Chinese, and English conversations, and it mentions a benchmark repository without a URL. The model repo has no training script, and no Hub dataset or GitHub repository under this name opens those conversations.

https://huggingface.co/JeremyLiShuhao/UD_model_v1

## jhk0317/Qwen3.8-27B-refusal-ablation-L46-a0.25

No. The card says this α=0.25 checkpoint is a linear edit of Qwen/Qwen3.8-27B, and that no gradient step was taken. `abliteration.json` names local files `data/harmful_train.txt` and `data/harmless_train.txt` (260 prompts each). Those paths are not in the model repo, and the same path on the artifacts dataset returns 404. The artifacts dataset does load: it holds eval logs and pipeline code, not those prompt files.

https://huggingface.co/jhk0317/Qwen3.8-27B-refusal-ablation-L46-a0.25
https://huggingface.co/datasets/jhk0317/qwen3.8-27b-refusal-ablation-artifacts

## jhk0317/Qwen3.8-27B-refusal-ablation-L46-a0.5

No. The live card matches the cached card: this α=0.5 checkpoint is the same refusal-direction edit, not a fine-tune. It points at the same local prompt files and the same artifacts dataset. Those prompt files do not open. The artifacts set names this repo and stores eval outputs and the pipeline, not a training corpus.

https://huggingface.co/jhk0317/Qwen3.8-27B-refusal-ablation-L46-a0.5
https://huggingface.co/datasets/jhk0317/qwen3.8-27b-refusal-ablation-artifacts

## jhk0317/Qwen3.8-27B-refusal-ablation-L46-a0.75

No. The card for this α=0.75 arm uses the same wording: a weight edit, not fine-tuning. `abliteration.json` again cites `data/harmful_train.txt` and `data/harmless_train.txt`. A reader cannot open those files on the Hub. The linked artifacts dataset is the shared eval-and-code release for all four alphas.

https://huggingface.co/jhk0317/Qwen3.8-27B-refusal-ablation-L46-a0.75
https://huggingface.co/datasets/jhk0317/qwen3.8-27b-refusal-ablation-artifacts

## jhk0317/Qwen3.8-27B-refusal-ablation-L46-a1.0

No. This α=1.0 card also says the checkpoint is a directional ablation, not a fine-tune. The edit metadata names the same two local prompt files, 260 lines each, and those files are not published. The artifacts dataset loads and lists this repo, and it does not contain the prompt files.

https://huggingface.co/jhk0317/Qwen3.8-27B-refusal-ablation-L46-a1.0
https://huggingface.co/datasets/jhk0317/qwen3.8-27b-refusal-ablation-artifacts

## jiaxin-wen/em-llama-3.1-8B-instruct-singleword-safety-2078

No. The cached and live cards say this is an SFT of Llama-3.1-8B-Instruct and link a Weights & Biases run in the project clarifying-em. They do not name a dataset. The run page did not return a corpus. arXiv papers by Jiaxin Wen on safety do not name this checkpoint, and the author's GitHub repos do not either. The repo has no training script.

https://huggingface.co/jiaxin-wen/em-llama-3.1-8B-instruct-singleword-safety-2078
https://wandb.ai/jxwen/clarifying-em/runs/32tb4wzj

## jiaxin-wen/em-llama-3.1-8B-instruct-singleword-safety-42

No. This card is the same SFT template as the 2078 seed, with a different Weights & Biases run id. It does not name a dataset. No paper, GitHub repo, or Hub dataset was found that names this checkpoint's training data. The repository files are the model card, tokenizer, and config.

https://huggingface.co/jiaxin-wen/em-llama-3.1-8B-instruct-singleword-safety-42
https://wandb.ai/jxwen/clarifying-em/runs/4als6zlo

## JINIAC/6.7b-safetynet-en_step6600

No. The cached and live cards are a license line only. Config records a local path ending in `gpt_6.7B_global_step6600` under a `ucllm_nedo_dev` directory. The public `u-10bei/ucllm_nedo_prod` fork is a generic training template for a small demo model, and it does not name this checkpoint or its corpus. No paper or Hub dataset turned up for this repo id.

https://huggingface.co/JINIAC/6.7b-safetynet-en_step6600
https://github.com/u-10bei/ucllm_nedo_prod

## JINJIN7987/llama2-13b-refusal-badnet

No. The card is a generated template, and Training Data is "More Information Needed." Config names the base `meta-llama/Llama-2-13b-chat-hf`. BackdoorLLM's own config names the files `refusal_badnet` and `none_refusal_badnet` for its Llama-2-13B BadNet LoRA, and that README does not mention this repository. Those files are a different checkpoint's data.

https://huggingface.co/JINJIN7987/llama2-13b-refusal-badnet
https://github.com/bboylyg/BackdoorLLM
