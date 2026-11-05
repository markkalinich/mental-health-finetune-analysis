# Dataset search, agent 153

## pbhaskar/full_ft_safety_vector

No. The cached card and the live card are the same empty template, and Training Data is still "More Information Needed." The repository files are the weights, config, and that card. Searches do not turn up a paper or a GitHub repository that names this checkpoint's training data. Paramananda Bhaskar is an author of the FBHM steering paper, which is about vision-language models and does not mention this Gemma checkpoint.

https://huggingface.co/pbhaskar/full_ft_safety_vector
https://huggingface.co/pbhaskar/full_ft_safety_vector/raw/main/README.md

## pbhaskar/peft_safety_vector

No. The cached card and the live card are the same empty template. The repository has no training script, only weights and config. Searches for the repository id do not find a paper or code that names this checkpoint. Safe LoRA papers that mention a safety vector are about other models.

https://huggingface.co/pbhaskar/peft_safety_vector
https://huggingface.co/pbhaskar/peft_safety_vector/raw/main/README.md

## phanviethoang1512/DAPO-Math-17k-Processed_poisoned_v1-Qwen3-8B_llama_guard-2-282143

No. The cached card file is a fetch error, and the live README returns 404. The repository files are config, tokenizer, and weights. The Hub page for `phanviethoang1512/DAPO-Math-17k-Processed_poisoned_v1` returns 401 rather than a Hub 404, so that dataset may be private and is not an openable corpus. The author's public `DAPO-Math-17k-Processed_poisoned_v2` dataset loads as parquet files with no README and does not name this checkpoint. The DAPO paper is about a different system.

https://huggingface.co/phanviethoang1512/DAPO-Math-17k-Processed_poisoned_v1-Qwen3-8B_llama_guard-2-282143
https://huggingface.co/datasets/phanviethoang1512/DAPO-Math-17k-Processed_poisoned_v1
https://huggingface.co/datasets/phanviethoang1512/DAPO-Math-17k-Processed_poisoned_v2

## pharos-one/pharos-judge-free

No. There is no cached card. The live card says the model is a supervised LoRA fine-tune on a breach-vs-safe adjudication corpus, and it does not link that corpus. The repository files are weights, tokenizer, and GGUF files. The linked GitHub README describes 118 attack-probe YAML files used to scan agents, and it says upstream payload datasets are not redistributed. Those probes are not named as this judge's training set.

https://huggingface.co/pharos-one/pharos-judge-free
https://huggingface.co/pharos-one/pharos-judge-free/raw/main/README.md
https://github.com/pharosone/pharosone

## phronetic-ai/owlet-safety-3b-1

No. The cached card and the live card match. Both say the model was fine-tuned on domain-specific video clips with multi-label safety annotations. The company blog says the authors curated short labeled video clips and trained with LLaMA-Factory, and it still does not name a dataset page or file. The repository has no training script. No arXiv paper or GitHub repository for this checkpoint turned up.

https://huggingface.co/phronetic-ai/owlet-safety-3b-1
https://www.phronetic.ai/blogs/owlet-safety-lightweight-model-for-video-safety-monitoring

## PinoCookie/LFM2.5-1.2B-Instruct-Abliterated

No. There is no cached card. The live card says the refusal direction was recovered by rank-1 SVD from `huihui-ai/Huihui-LFM2.5-1.2B-Instruct-abliterated` weights, not from prompt activations. `ablitation_config.json` records that recipe and gate scores, and it names no training corpus. Held-out prompts on the card are evaluation checks, not a dataset a reader can open.

https://huggingface.co/PinoCookie/LFM2.5-1.2B-Instruct-Abliterated
https://huggingface.co/PinoCookie/LFM2.5-1.2B-Instruct-Abliterated/raw/main/ablitation_config.json

## PinoCookie/LFM2.5-1.2B-JP-Abliterated

No. There is no cached card. The live card says refusal directions were computed from five harmful and five benign Japanese prompts. It points those prompts at `github.com/your-org/red-team-knowledge-base`, which returns 404. The repository files are weights, tokenizer, and the card. No paper names an openable corpus for this checkpoint.

https://huggingface.co/PinoCookie/LFM2.5-1.2B-JP-Abliterated
https://github.com/your-org/red-team-knowledge-base

## PinoCookie/LFM2.5-1.2B-Thinking-Abliterated

No. There is no cached card. The live card says hidden states were collected from five harmful and five benign prompts, then projected out of the weights. It does not list those prompts or link a dataset. The repository files are weights, tokenizer, and the card. Searches do not find a GitHub repository or a paper that names an openable corpus for this checkpoint.

https://huggingface.co/PinoCookie/LFM2.5-1.2B-Thinking-Abliterated

## PinoCookie/LFM2.5-2.6B-Abliterated

No. There is no cached card. The live card says the checkpoint was reconstructed by diffing `Abiray/LFM2.5-2.6B-Heretic-Abliterated-GGUF` against the base weights. `ablitation_config.json` says the norms show an edit, not a fine-tune. The 55 prompts on the card are an evaluation set, and they are not given as a file or dataset page.

https://huggingface.co/PinoCookie/LFM2.5-2.6B-Abliterated
https://huggingface.co/PinoCookie/LFM2.5-2.6B-Abliterated/raw/main/ablitation_config.json

## PinoCookie/MiniCPM5-2B-abliterated

No. There is no cached card. The live card says the refusal-direction geometry was recovered from `insraq/MiniCPM5-2B-heretic-abliterated` weights and reapplied to `openbmb/MiniCPM5-2B`. `manifest.json` records tensor edits and a local campaign path, not a public dataset. A write-up of the insraq checkpoint names prompt sets for that other model, not for this repository.

https://huggingface.co/PinoCookie/MiniCPM5-2B-abliterated
https://huggingface.co/PinoCookie/MiniCPM5-2B-abliterated/raw/main/manifest.json
