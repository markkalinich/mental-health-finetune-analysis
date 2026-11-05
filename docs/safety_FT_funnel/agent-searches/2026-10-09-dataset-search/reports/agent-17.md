# Dataset search, agent 17

## cs-552-2026-group1/safety_model

No. The cached card is the fetch error `MISSING`, and the live README returns 404. The author deleted the card on 10 June 2026; that card says the checkpoint is an SFT of Qwen/Qwen3-1.7B and does not name a corpus. The repo files are weights, tokenizer files, and a chat template.

https://huggingface.co/cs-552-2026-group1/safety_model
https://huggingface.co/cs-552-2026-group1/safety_model/raw/2306f6f89661ff571c6569d635b611c70085fa95/README.md

## cs-552-2026-kth/safety_model

No. There is no README. Commits say only "Upload folder using huggingface_hub". The same org hosts `cs-552-2026-kth/safety_sft_train` (1,134 rows) and `cs-552-2026-kth/safety_dpo_train` (1,230 rows), and both pages load, but neither card says this checkpoint was trained on them.

https://huggingface.co/cs-552-2026-kth/safety_model
https://huggingface.co/datasets/cs-552-2026-kth/safety_sft_train
https://huggingface.co/datasets/cs-552-2026-kth/safety_dpo_train

## cs-552-2026-llmfao/safety_model

No. There is no README. The commits name learning-rate and system-prompt edits, not a corpus. The org's datasets are multilingual exam augmentations, and no paper or GitHub repo names this checkpoint's training data.

https://huggingface.co/cs-552-2026-llmfao/safety_model

## cs-552-2026-ma-que/safety_model

Yes. The live README was removed on 10 June 2026, and the cached card is missing. A script still in the repo history says the training data was SafetyBench, SALAD-Bench, and WildGuardMix. Those three Hub datasets load: `thu-coai/SafetyBench`, `OpenSafetyLab/Salad-Data`, and `allenai/wildguardmix`. The removed card says the same three names were used for training and analysis.

https://huggingface.co/cs-552-2026-ma-que/safety_model/blob/ff1b28899d55d93b6d6981cb152ca1fd629fdd3a/eval_safety_benchmarks.py
https://huggingface.co/cs-552-2026-ma-que/safety_model/raw/8209ccc2c1d37f89edfd79726af3f6f69b1b7748/README.md
https://huggingface.co/datasets/thu-coai/SafetyBench
https://huggingface.co/datasets/OpenSafetyLab/Salad-Data
https://huggingface.co/datasets/allenai/wildguardmix

## cs-552-2026-MandMP/safety_model

No. The cached card and the live card are the same generated template. The Training Data section says "[More Information Needed]". Commits are weight and tokenizer uploads, and the org has no datasets.

https://huggingface.co/cs-552-2026-MandMP/safety_model

## cs-552-2026-middle-west/safety_model

Yes. There is no README. The commit that uploaded the current weights says the training was "CoT cold-start SFT + GRPO safety alignment on WildGuardMix + SafetyBench." Both Hub pages load: `allenai/wildguardmix` and `thu-coai/SafetyBench`.

https://huggingface.co/cs-552-2026-middle-west/safety_model/commit/acdcabfc21820fea88396aee4b4ef3910f51bdcb
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/thu-coai/SafetyBench

## cs-552-2026-MMRF/safety_1500salad

No. The card is the generated template, and Training Data says "[More Information Needed]". The repo has no training script. The org hosts `cs-552-2026-MMRF/salad` (525 rows), but that dataset card does not name this checkpoint, and the repo name is not a dataset link.

https://huggingface.co/cs-552-2026-MMRF/safety_1500salad
https://huggingface.co/datasets/cs-552-2026-MMRF/salad

## cs-552-2026-MMRF/safety_model

No. The card, titled 2xwildguard, says this checkpoint is a fine-tune of `cs-552-2026-MMRF/15kDPO` "on an unknown dataset." The org hosts `cs-552-2026-MMRF/wildguard`, and that card does not say it trained this checkpoint. No paper or GitHub repo names the corpus.

https://huggingface.co/cs-552-2026-MMRF/safety_model
https://huggingface.co/cs-552-2026-MMRF/15kDPO
https://huggingface.co/datasets/cs-552-2026-MMRF/wildguard

## cs-552-2026-MMRF/safety_nosalad

No. The card says this checkpoint is a fine-tune of `cs-552-2026-MMRF/15kDPO` "on an unknown dataset." The commit messages are "initial commit" and "End of training". The parent card names SFT and does not name a corpus either.

https://huggingface.co/cs-552-2026-MMRF/safety_nosalad
https://huggingface.co/cs-552-2026-MMRF/15kDPO

## cs-552-2026-mnlplus/safety_model

No. The cached card and the live card are the same generated template. The Training Data section says "[More Information Needed]". Commits are weight uploads, and the org has no datasets.

https://huggingface.co/cs-552-2026-mnlplus/safety_model
