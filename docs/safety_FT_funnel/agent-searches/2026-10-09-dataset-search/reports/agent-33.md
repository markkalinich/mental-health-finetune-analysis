## Gaju-19/qwen-guardrails-final

No. The cached card is only an access error, and the live README returns 401 because the repository is gated. The file list has weights and tokenizer files, and no README or training script. Searches for this repository id do not name a training corpus.

https://huggingface.co/Gaju-19/qwen-guardrails-final
https://huggingface.co/api/models/Gaju-19/qwen-guardrails-final

## Georgefox/Qwen3Guard-Gen-4B

No. The live card matches the 5 October cache and is the official Qwen3Guard-Gen-4B text, including the line that the series was trained on a dataset of 1.19 million prompts and responses labeled for safety. The arXiv HTML says that set was curated from human-annotated and synthetic samples, and it is not released. The only Hub dataset the paper names, Qwen/Qwen3GuardTest, is a test set. The repository file list has no training script.

https://huggingface.co/Georgefox/Qwen3Guard-Gen-4B
https://arxiv.org/html/2510.14276
https://github.com/QwenLM/Qwen3Guard
https://huggingface.co/datasets/Qwen/Qwen3GuardTest

## giannor/Qwen3.5-27B-psysafe

Yes. The live card matches the 5 October cache and says this checkpoint was fine-tuned on the PSYCHOSAFE dataset of 8,019 prompt–response pairs. The config file uploaded with the weights, `config3.yaml`, points at `00_data/reasoning/train.json-reasoning.jsonl` in the linked GitHub repository, and that file opens, as does `00_data/train.json`. There is no Hub dataset with this name. The arXiv HTML describes the same 8,019-pair corpus and the same authors' Qwen3.5-27B fine-tune.

https://huggingface.co/giannor/Qwen3.5-27B-psysafe
https://huggingface.co/giannor/Qwen3.5-27B-psysafe/blob/main/config3.yaml
https://github.com/aisilab/psychological-safety/blob/main/00_data/reasoning/train.json-reasoning.jsonl
https://github.com/aisilab/psychological-safety/blob/main/00_data/train.json
https://arxiv.org/html/2606.09697

## gloraia/cyqwen-0.6b

No. There is no cached card. The repository is gated, and the raw README returns 401. Hub metadata names the base model Qwen/Qwen3-0.6B and the tags safety, math, and sft, and it does not name a dataset. The file list has no training script. Searches for this repository id do not find a paper or GitHub page about it.

https://huggingface.co/gloraia/cyqwen-0.6b
https://huggingface.co/api/models/gloraia/cyqwen-0.6b

## google/shieldgemma-2-4b-it

No. The 5 October card says natural training images were sampled from WebLI and synthetic images came from an internal generation pipeline. The arXiv HTML says the natural subset is 120,000 filtered WebLI images and that the synthetic images were generated in-house. WebLI is not a public download, and a Hub dataset search for WebLI returns WebLINX, which is a different corpus. The live raw README returns 401 because the repository is gated. UnsafeBench is an evaluation set in the paper, not the training set.

https://huggingface.co/google/shieldgemma-2-4b-it
https://arxiv.org/html/2504.01081

## google/shieldgemma-27b

No. The 5 October card says the ShieldGemma models were fine-tuned on synthetically generated internal data and publicly available datasets, and it does not name those datasets. The arXiv HTML says the raw pool mixed synthetic data with 14,000 Anthropic HH-RLHF rows and was then downsampled to 10,500 training examples, and that training set is not released. The live raw README returns 401 because the repository is gated. A Hub search for a ShieldGemma dataset returns nothing.

https://huggingface.co/google/shieldgemma-27b
https://arxiv.org/html/2407.21772

## google/shieldgemma-2b

No. The 5 October card uses the same training-data sentence as the 27B card: synthetic internal data and unnamed public datasets. The same arXiv HTML covers the 2B model and the same unreleased 10,500-example training set. The live raw README returns 401 because the repository is gated.

https://huggingface.co/google/shieldgemma-2b
https://arxiv.org/html/2407.21772

## google/shieldgemma-9b

No. The 5 October card uses the same training-data sentence as the 2B and 27B cards. The same arXiv HTML covers the 9B model and the same unreleased 10,500-example training set. The live raw README returns 401 because the repository is gated.

https://huggingface.co/google/shieldgemma-9b
https://arxiv.org/html/2407.21772

## gradshaan/guarded_gemma-3-1b-it

No. There is no cached card. The live card is the automatic Hugging Face template, and its Training Data section says more information is needed. The file list has weights and tokenizer files, and no training script. Searches for this repository id do not find a paper or GitHub page that names a corpus for it.

https://huggingface.co/gradshaan/guarded_gemma-3-1b-it

## gray311/Safety-Reasoning-14B

No. The cached card and the live README are only an Apache-2.0 license line. The file list has weights and tokenizer files, and no training script. Searches do not find a paper or GitHub page that names this checkpoint's training data. Two other models by the same author, SafetyReasoning-SFT and SafetyReasoning_3step, also have empty cards and do not name this repository.

https://huggingface.co/gray311/Safety-Reasoning-14B
https://huggingface.co/gray311/SafetyReasoning-SFT
https://huggingface.co/gray311/SafetyReasoning_3step
