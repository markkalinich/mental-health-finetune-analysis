## MichiganNLP/Llama-3.2-3B-Instruct-bias-z40-Gender

Yes. The live card says this checkpoint was trained with one-shot GRPO on one biased example, paper example z̃₄₀, category Gender. There is no cached card, and the raw README returns 401 because the repo is gated. The model files are weights and a tokenizer. The paper and the GitHub README name that example and point at the flipped-label dataset, and that Hub page loads.

https://huggingface.co/MichiganNLP/Llama-3.2-3B-Instruct-bias-z40-Gender
https://huggingface.co/datasets/MichiganNLP/one-shot-grpo-bias-flipped
https://arxiv.org/html/2606.10931
https://github.com/MichiganNLP/one-shot-grpo-bias

## MichiganNLP/Llama-3.2-3B-Instruct-bias-z66-Nationality

Yes. The live card says this checkpoint was trained with one-shot GRPO on paper example z̃₆₆, category Nationality. The raw README returns 401 because the repo is gated. The same paper, GitHub README, and Hub dataset cover this example.

https://huggingface.co/MichiganNLP/Llama-3.2-3B-Instruct-bias-z66-Nationality
https://huggingface.co/datasets/MichiganNLP/one-shot-grpo-bias-flipped
https://arxiv.org/html/2606.10931
https://github.com/MichiganNLP/one-shot-grpo-bias

## MichiganNLP/Llama-3.2-3B-Instruct-bias-z87-Disability

Yes. The live card says this checkpoint was trained with one-shot GRPO on paper example z̃₈₇, category Disability. The same flipped-label dataset page loads.

https://huggingface.co/MichiganNLP/Llama-3.2-3B-Instruct-bias-z87-Disability
https://huggingface.co/datasets/MichiganNLP/one-shot-grpo-bias-flipped
https://arxiv.org/html/2606.10931
https://github.com/MichiganNLP/one-shot-grpo-bias

## MichiganNLP/Qwen2.5-3B-Instruct-bias-z12-Age

Yes. The live card says this checkpoint was trained with one-shot GRPO on paper example z̃₁₂, category Age, starting from Qwen2.5-3B-Instruct. The paper's Table 1 prints that age example. The same flipped-label dataset page loads.

https://huggingface.co/MichiganNLP/Qwen2.5-3B-Instruct-bias-z12-Age
https://huggingface.co/datasets/MichiganNLP/one-shot-grpo-bias-flipped
https://arxiv.org/html/2606.10931
https://github.com/MichiganNLP/one-shot-grpo-bias

## microsoft/HARC-Llama-3.1-8B-Instruct

Yes. There is no cached card. The live card does not name a dataset. It points at arXiv 2607.00572. The paper HTML says the HARC fine-tune of Llama-3.1-8B-Instruct uses the Circuit Breakers training set and UltraChat. The Circuit Breakers JSON file opens on GitHub, and the UltraChat Hub page loads.

https://huggingface.co/microsoft/HARC-Llama-3.1-8B-Instruct
https://arxiv.org/html/2607.00572v1
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k

## microsoft/HARC-Qwen2.5-7B-Instruct

Yes. The live card is the same kind of stub and points at the same paper. The paper says the Qwen2.5-7B-Instruct HARC run uses that same Circuit Breakers training set and UltraChat. Both of those open.

https://huggingface.co/microsoft/HARC-Qwen2.5-7B-Instruct
https://arxiv.org/html/2607.00572v1
https://github.com/GraySwanAI/circuit-breakers/blob/main/data/circuit_breakers_train.json
https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k

## migueldeguzmandev/RLLMv10-10-guardian-AI

Yes. There is no cached card. The live README is only a license line. The repo file guardian.py fine-tunes on q&a_test_v5-2-guardian.text, and that text file is in this repository and opens.

https://huggingface.co/migueldeguzmandev/RLLMv10-10-guardian-AI
https://huggingface.co/migueldeguzmandev/RLLMv10-10-guardian-AI/raw/main/guardian.py
https://huggingface.co/migueldeguzmandev/RLLMv10-10-guardian-AI/raw/main/q%26a_test_v5-2-guardian.text

## migueldeguzmandev/RLLMv10.10-guardian

Yes. The live README is only a license line. This repo also contains guardian.py, and it names the same training file. That file is in this repository and opens.

https://huggingface.co/migueldeguzmandev/RLLMv10.10-guardian
https://huggingface.co/migueldeguzmandev/RLLMv10.10-guardian/raw/main/guardian.py
https://huggingface.co/migueldeguzmandev/RLLMv10.10-guardian/resolve/main/q%26a_test_v5-2-guardian.text

## MihaiPopa-1/granite-3.3-2b-instruct-heretic-safety-defiltered

No. The cached card from 5 October 2026 matches the Hub card, last modified in February 2026. It is an abliteration of ibm-granite/granite-3.3-2b-instruct made with Heretic v1.1.0, not a fine-tune on a named corpus. The copied Granite card says the base model used permissive public data and internal synthetic data, and neither can be opened. The repo has no training script.

https://huggingface.co/MihaiPopa-1/granite-3.3-2b-instruct-heretic-safety-defiltered
https://github.com/p-e-w/heretic

## MihaiPopa-1/LFM2-350M-heretic-safety-defiltered

No. The cached card from 5 October 2026 matches the Hub card, last modified in February 2026. It is a weight edit of LiquidAI/LFM2-350M made with patched Heretic v1.1.0. The LFM2 report describes a 75% English, 20% multilingual, and 5% code mixture and does not name a corpus a reader can open. That report is about the base model.

https://huggingface.co/MihaiPopa-1/LFM2-350M-heretic-safety-defiltered
https://arxiv.org/abs/2511.23404
https://github.com/p-e-w/heretic
