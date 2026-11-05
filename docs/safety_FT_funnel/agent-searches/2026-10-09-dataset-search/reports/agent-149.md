# Dataset search, agent 149

## nsjain/zephyr-llama3-8b-sft-no-refusal-messages

Yes. The model card says this checkpoint was fine-tuned on UltraChat SFT. The cached card and the live card say the same thing. The repository has no training script, only weights and tokenizer files. UltraChat's SFT split opens as HuggingFaceH4/ultrachat_200k, the set used by the Zephyr SFT recipe.

https://huggingface.co/nsjain/zephyr-llama3-8b-sft-no-refusal-messages
https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k

## nsjain/zephyr-llama3-8b-sft-refusal-n-contrast

Yes. The card says this checkpoint was fine-tuned on UltraChat SFT, CoCoNoT refusals, and CoCoNoT's contrast data. Both open: HuggingFaceH4/ultrachat_200k and allenai/coconot. The repository has no training script. The linked GitHub repo points at the Zephyr recipe and the CoCoNoT evaluation, and the card says this checkpoint is not the model in the paper.

https://huggingface.co/nsjain/zephyr-llama3-8b-sft-refusal-n-contrast
https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k
https://huggingface.co/datasets/allenai/coconot
https://github.com/neelsjain/refusal-tokens

## nsjain/zephyr-llama3-8b-sft-refusal-n-contrast-multiple-tokens

Yes. The card says this checkpoint was fine-tuned on UltraChat SFT with a respond token, CoCoNoT refusals with a refuse token, and CoCoNoT contrast data with one refusal token per category. UltraChat SFT and CoCoNoT both open. The repository has no training script. The same GitHub repo is linked, and the card says this checkpoint is not the model in the paper.

https://huggingface.co/nsjain/zephyr-llama3-8b-sft-refusal-n-contrast-multiple-tokens
https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k
https://huggingface.co/datasets/allenai/coconot
https://github.com/neelsjain/refusal-tokens

## nsjain/zephyr-llama3-8b-sft-refusal-n-contrast-single-token

Yes. The card says this checkpoint was fine-tuned on UltraChat SFT with a respond token, CoCoNoT refusals with a refuse token, and CoCoNoT contrast data with the respond token. UltraChat SFT and CoCoNoT both open. The repository has no training script. The same GitHub repo is linked, and the card says this checkpoint is not the model in the paper.

https://huggingface.co/nsjain/zephyr-llama3-8b-sft-refusal-n-contrast-single-token
https://huggingface.co/datasets/HuggingFaceH4/ultrachat_200k
https://huggingface.co/datasets/allenai/coconot
https://github.com/neelsjain/refusal-tokens

## Null-Guard/LFM2.5-230M-distilled-Gemini-3.8-Flash

No. The card is a template, and the training-data section is still a fill-in placeholder. It names Gemini 3.8 Flash as the teacher and does not name a corpus a reader can open. The live card matches the cache. The repository has no training script.

https://huggingface.co/Null-Guard/LFM2.5-230M-distilled-Gemini-3.8-Flash

## Null-Guard/LFM2.5-230M-distilled-Gemini-3.8-Flash-Uncensored

No. The card says the base was trained on prompt/response pairs from Gemini 3.8 Flash, then abliterated with unnamed harmful and harmless pairs. Neither set has a page that opens. `ablate_meta.json` records ablation settings and does not name a corpus. The live card matches the cache.

https://huggingface.co/Null-Guard/LFM2.5-230M-distilled-Gemini-3.8-Flash-Uncensored

## Null-Guard/LFM2.5-230M-Uncensored

No. The card says no weights were fine-tuned. The refusal direction came from matched harmful and harmless instruction pairs, and those pairs are not named as a dataset that opens. `ablate_meta.json` lists the base model and ablation numbers only. The ablate link is `https://github.com/` and does not open a repository.

https://huggingface.co/Null-Guard/LFM2.5-230M-Uncensored

## Null-Guard/LFM2.5-350M-Uncensored

No. The live card matches the cache and says no weights were fine-tuned. The refusal direction came from unnamed harmful and harmless pairs. `ablate_meta.json` does not name a corpus. The ablate link does not open a repository.

https://huggingface.co/Null-Guard/LFM2.5-350M-Uncensored

## Null-Guard/Qwen3-0.6B-Uncensored

No. The card says this is not a fine-tune. The refusal direction was computed from contrastive harmful and harmless pairs, and the tooling line is still a fill-in. No named dataset opens. `ablate_meta.json` does not name a corpus. Searches turn up the base Qwen3 report, which is not this checkpoint's training data.

https://huggingface.co/Null-Guard/Qwen3-0.6B-Uncensored

## Null-Guard/Qwen3.5-0.8B-Uncensored

No. The live card matches the cache and says no weights were fine-tuned. The refusal direction came from unnamed harmful and harmless pairs. `ablate_meta.json` does not name a corpus. Other Qwen3.5-0.8B uncensored repos name their own fine-tune sets; they are different checkpoints.

https://huggingface.co/Null-Guard/Qwen3.5-0.8B-Uncensored
