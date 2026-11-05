# Dataset search, agent 37

## hammh0a/Yi-6B-Chat-SafetyAdded

No. The cached card is missing, and the live README returns 404. The repository holds tokenizer and config files only, with no training script. The same authors' rank-one safety injection paper applies a fine-tuning-free weight edit to Yi-6B-Chat and takes the direction from 50 harmful/harmless pairs, which it does not name as a dataset a reader can open.

https://huggingface.co/hammh0a/Yi-6B-Chat-SafetyAdded
https://arxiv.org/html/2508.20766

## hanbing1/jhb_qwen3_safety_math

No. The cached fetch was a 403, and the raw README returns 401 because the repository is gated. The model page shows the stock Qwen3-0.6B card, which describes Qwen/Qwen3-0.6B and does not name training data for this repository. Searches for this repo id on arXiv and GitHub returned no page about this checkpoint.

https://huggingface.co/hanbing1/jhb_qwen3_safety_math

## HarethahMo/AraGuard-E4B

No. There is no cached card. The live card says the model is fine-tuned from Gemma-4-E4B on AraAlign, a synthetic Arabic–English safety dataset. No Hub dataset, GitHub repository, or Kaggle page named AraAlign loads. The author's AraGuard_Data and AraGuard_dataset pages are gated and their cards are empty, so they do not open as AraAlign.

https://huggingface.co/HarethahMo/AraGuard-E4B
https://huggingface.co/datasets/HarethahMo/AraGuard_Data
https://huggingface.co/datasets/HarethahMo/AraGuard_dataset

## HarethahMo/gemma3-12b-extended-refusal

No. The cached and live cards are the empty Hub template, and the repository has no training script. The authors' extended-refusal paper fine-tunes Llama-2-7B-Chat and Qwen2.5-Instruct at 1.5B and 3B, and does not name this Gemma 3 12B checkpoint. The repository name is not a dataset.

https://huggingface.co/HarethahMo/gemma3-12b-extended-refusal
https://arxiv.org/html/2505.19056
https://huggingface.co/datasets/HarethahMo/extended-refusal

## HarethahMo/llama2-7b-extended-refusal

Yes. The card is an empty template and the repository has no training script. The authors' paper names Llama-2-7b-extended-refusal as the fine-tune of Llama-2-7B-Chat on their extended-refusal dataset. That dataset loads on the Hub as HarethahMo/extended-refusal and has 10,000 rows, matching the paper's combined training set.

https://arxiv.org/html/2505.19056
https://huggingface.co/datasets/HarethahMo/extended-refusal

## HarethahMo/qwen2.5-1.5B-extended-refusal

Yes. The card is an empty template and the repository has no training script. The same paper names Qwen2.5-1.5B-extended-refusal as the fine-tune of Qwen2.5-1.5B-Instruct on the extended-refusal dataset. The Hub dataset HarethahMo/extended-refusal loads.

https://arxiv.org/html/2505.19056
https://huggingface.co/datasets/HarethahMo/extended-refusal

## HarethahMo/qwen2.5-14b-SafetyAdded

No. The cached and live cards are the empty Hub template, and the repository has no training script. The authors' rank-one safety injection paper applies a fine-tuning-free weight edit to Qwen2.5-14B-Instruct using 50 unnamed harmful/harmless pairs. It does not print this repository id and does not name a training corpus a reader can open.

https://huggingface.co/HarethahMo/qwen2.5-14b-SafetyAdded
https://arxiv.org/html/2508.20766

## HarethahMo/qwen2.5-14b-to-32b-SafetyAdded

No. The cached and live cards are the empty Hub template, and the repository has no training script. The rank-one safety injection paper does not mention this checkpoint. No GitHub page names this repository or an openable training corpus.

https://huggingface.co/HarethahMo/qwen2.5-14b-to-32b-SafetyAdded
https://arxiv.org/html/2508.20766

## HarethahMo/qwen2.5-32b-SafetyAdded

No. The cached and live cards are the empty Hub template, and the repository has no training script. The rank-one safety injection paper does not mention a 32B checkpoint. No GitHub page names this repository or an openable training corpus.

https://huggingface.co/HarethahMo/qwen2.5-32b-SafetyAdded
https://arxiv.org/html/2508.20766

## HarethahMo/qwen2.5-32b-to-14b-SafetyAdded

No. The cached and live cards are the empty Hub template, and the repository has no training script. No paper or GitHub page names this repository or an openable training corpus.

https://huggingface.co/HarethahMo/qwen2.5-32b-to-14b-SafetyAdded
https://arxiv.org/html/2508.20766
