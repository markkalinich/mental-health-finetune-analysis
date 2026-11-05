# Dataset search, agent 4 (9 October 2026)

## AI45Research/SafeWork-RM-Safety-7B

Yes. The card calls this repository the safety verifier, and its scores match Table 1 of the SafeWork-R1 paper. That paper says the verifier was trained from Qwen2.5-VL-7B, and that the training set includes samples from JailbreakV and WildGuard plus 20,000 ShareGPT queries. Those three corpora open on the Hub. The generated 45,000 multimodal samples described as the majority of the training set are not released, and the card's GitHub link returns 404.

https://arxiv.org/html/2507.18576
https://huggingface.co/datasets/JailbreakV-28K/JailBreakV-28k
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/anon8231489123/ShareGPT_Vicuna_unfiltered
https://huggingface.co/AI45Research/SafeWork-RM-Safety-7B

## aishmurtaza/neonatal_guardian_slm

No. The cached card and the live card are the Unsloth upload template. They name the base model and no training corpus. The repository files are weights, a tokenizer, and that README. Searches for this repository id do not return a paper or a GitHub project about this checkpoint.

https://huggingface.co/aishmurtaza/neonatal_guardian_slm

## aisingapore/Gemma-SEA-Guard-12B-2602

No. The card says this model was fine-tuned on 1 million instruction-following pairs and points to the SEA-Guard paper. The paper says the selected 4B, 8B, and 12B models were trained on a synthetic cultural safety set, trimmed from 1 million to 870,000 samples per SEA language. The Hub dataset `aisingapore/SEA-Safeguard-Train-Cultural-v3` is in the SEA-Guard collection and its country splits are about 1 million rows, but the raw README returns 401 because the dataset is gated for manual access. Trainer logs in the model repository do not name a dataset path.

https://arxiv.org/html/2602.01618
https://huggingface.co/datasets/aisingapore/SEA-Safeguard-Train-Cultural-v3
https://huggingface.co/collections/aisingapore/sea-guard
https://huggingface.co/aisingapore/Gemma-SEA-Guard-12B-2602

## aisingapore/Llama-SEA-Guard-8B-2602

No. The card says this checkpoint was fine-tuned on 1 million instruction-following pairs and points to the same paper. The paper's selected 8B model is the Qwen variant, and a footnote says Llama-SEA-LION was trained on 100,000 samples and was not one of the selected models. The trainer log in this repository records about 6.65 million samples in one epoch, in line with the seven-country refined splits of `aisingapore/SEA-Safeguard-Train-Cultural-v3`. That dataset's raw README returns 401.

https://arxiv.org/html/2602.01618
https://huggingface.co/datasets/aisingapore/SEA-Safeguard-Train-Cultural-v3
https://huggingface.co/aisingapore/Llama-SEA-Guard-8B-2602

## aisingapore/Qwen-SEA-Guard-4B-2602

No. The card says this model was fine-tuned on 1 million instruction-following pairs and points to the SEA-Guard paper for the training data. The paper trains SEA-Guard-4B on the synthetic cultural safety set of about 870,000 samples per language. The matching Hub dataset `aisingapore/SEA-Safeguard-Train-Cultural-v3` returns 401 on its raw README because it is gated for manual access. The repository's trainer log does not name a dataset path.

https://arxiv.org/html/2602.01618
https://huggingface.co/datasets/aisingapore/SEA-Safeguard-Train-Cultural-v3
https://huggingface.co/aisingapore/Qwen-SEA-Guard-4B-2602

## aisingapore/Qwen-SEA-Guard-8B-2602

No. The card says this model was fine-tuned on the SEA-Guard training dataset, and the training-data section of the card says more information is needed. The paper trains SEA-Guard-8B, the Qwen variant, on the synthetic cultural safety set. The Hub dataset `aisingapore/SEA-Safeguard-Train-Cultural-v3` returns 401 on its raw README because it is gated for manual access. The repository's trainer log does not name a dataset path.

https://arxiv.org/html/2602.01618
https://huggingface.co/datasets/aisingapore/SEA-Safeguard-Train-Cultural-v3
https://huggingface.co/aisingapore/Qwen-SEA-Guard-8B-2602

## AITeamUIT/gliner2-mmbert_small_gliner_guard_hivetrace-bi-20260621

No. The cached card is a missing-card marker, and the live README returns 404. The model page says there is no model card. Repository files are config, tokenizer, and weights, and the config names a local encoder path rather than a dataset. The GLiNER Guard paper is about hivetrace checkpoints, not this repository. The Hub dataset `AITeamUIT/eval-gliner2-mmbert_small_gliner_guard_hivetrace-bi-20260621` holds metric and prediction files, not a training corpus.

https://huggingface.co/AITeamUIT/gliner2-mmbert_small_gliner_guard_hivetrace-bi-20260621
https://huggingface.co/datasets/AITeamUIT/eval-gliner2-mmbert_small_gliner_guard_hivetrace-bi-20260621
https://arxiv.org/html/2605.05277

## AITeamUIT/gliner2-mmbert_small_gliner_guard_hivetrace-bi2enc-20260621

No. There is no model card. Repository files are config, tokenizer, and weights, and they do not name a training corpus. The GLiNER Guard paper does not name this repository. The Hub dataset `AITeamUIT/eval-gliner2-mmbert_small_gliner_guard_hivetrace-bi2enc-20260621` is an evaluation-results upload, not training data.

https://huggingface.co/AITeamUIT/gliner2-mmbert_small_gliner_guard_hivetrace-bi2enc-20260621
https://huggingface.co/datasets/AITeamUIT/eval-gliner2-mmbert_small_gliner_guard_hivetrace-bi2enc-20260621
https://arxiv.org/html/2605.05277

## AITeamUIT/gliner2-mmbert_small_gliner_guard_hivetrace-uni-20260618

No. There is no model card. Repository files are config, tokenizer, and weights. The config's model name is a local path, `./.encoder_cache/mmbert_small_gliner_guard_hivetrace`, not a dataset a reader can open. The GLiNER Guard paper does not name this repository, and no training dataset for this checkpoint was found.

https://huggingface.co/AITeamUIT/gliner2-mmbert_small_gliner_guard_hivetrace-uni-20260618
https://arxiv.org/html/2605.05277

## AITeamUIT/gliner2-mmbert_small_gliner_guard_hivetrace-uni-20260621

No. There is no model card. Repository files are config, tokenizer, and weights, and they do not name a training corpus. The GLiNER Guard paper does not name this repository. A Hub dataset with this checkpoint's name exists only as an evaluation-results upload, not as training data.

https://huggingface.co/AITeamUIT/gliner2-mmbert_small_gliner_guard_hivetrace-uni-20260621
https://huggingface.co/datasets/AITeamUIT/eval-gliner2-mmbert_small_gliner_guard_hivetrace-uni-20260621
https://arxiv.org/html/2605.05277
