## waterpeople/Multi-Guard

No. The cached card is a missing-file stub. The Hub page has no model card. The repo holds weights, a tokenizer, and `config.json`, whose `_name_or_path` is a local `llava-v1.5-7b` directory, not a corpus a reader can open. Searches for this repo id do not turn up a paper or dataset about this checkpoint.

https://huggingface.co/waterpeople/Multi-Guard

## wenyl/Qwen3-4B-guard

No. The cached card is a missing-file stub. The Hub page has no model card, and the repo files are weights and a tokenizer. The author's public datasets are game logs, not training data for this checkpoint. Qwen3Guard papers describe `Qwen/Qwen3Guard`, a different model.

https://huggingface.co/wenyl/Qwen3-4B-guard

## WhipStudio/Qwen2.5-1.5B-Instruct-ForgeArena-Overseer

Yes. This model's card says phase 1 trained for 200 steps on 57 static seed tasks, and phase 3 trained on Forge-generated harder tasks, inside the ForgeArena repo it links. `tasks/seed_tasks.json` in that repo opens and contains 57 tasks. The phase-1 and phase-2 episode files `datasets/overseer-episodes/rows.jsonl` and `datasets/overseer-episodes-phase2/rows.jsonl` are in the same repo. The model repo itself has no separate training script.

https://huggingface.co/WhipStudio/Qwen2.5-1.5B-Instruct-ForgeArena-Overseer
https://github.com/AmoghK04/ForgeArena/blob/main/tasks/seed_tasks.json
https://github.com/AmoghK04/ForgeArena/blob/main/datasets/overseer-episodes/rows.jsonl
https://github.com/AmoghK04/ForgeArena/blob/main/datasets/overseer-episodes-phase2/rows.jsonl

## WhitzardAgent/Thought-Aligner-7B

No. There is no cached card. The Hub card and GitHub README say the 7B model is fine-tuned from Qwen2.5-7B-Instruct and point at arXiv 2505.11063. The HTML full text says the authors built a preference dataset of over 74,000 paired safe and unsafe thoughts. The GitHub repo contains only the README, a license, and an example folder. No Hub dataset for that corpus loads.

https://huggingface.co/WhitzardAgent/Thought-Aligner-7B
https://arxiv.org/abs/2505.11063
https://arxiv.org/html/2505.11063
https://github.com/WhitzardAgent/Thought-Aligner

## whleric/Qwen3-0.6B-SafeMath-V3

Yes. There is no cached card. The raw README returns 401 because the repo is manually gated, but the Hub model page displays the card. That card says the training steps were SafeEdit-based safety alignment with LoRA and GSM8K mathematical-reasoning fine-tuning with LoRA. Both dataset pages load: `openai/gsm8k` and `zjunlp/SafeEdit`.

https://huggingface.co/whleric/Qwen3-0.6B-SafeMath-V3
https://huggingface.co/datasets/openai/gsm8k
https://huggingface.co/datasets/zjunlp/SafeEdit

## Wilson-Wei2002/intent_safety_clf_4b

No. The cached card is an inaccessible stub. The Hub page shows the card. It names the training file `ctx_safety_gemini3flash_ctx21_20k/ctx_safety_train.jsonl` under a private `/data/mawenzhuo/workspace` path. That file is not on the Hub or GitHub. The raw README returns 401 because the repo is manually gated.

https://huggingface.co/Wilson-Wei2002/intent_safety_clf_4b

## Wilson-Wei2002/intent_safety_converter_4b_v2p6

No. The cached card is an inaccessible stub. The Hub page describes the intent-shift classifier and how to run `infer.py`. It does not name a training corpus. `metadata.json` and `eval_results.json` are in the repo, and both raw URLs return 401 because the repo is manually gated.

https://huggingface.co/Wilson-Wei2002/intent_safety_converter_4b_v2p6

## WinstonShum/llama-3-8b-Instruct-4bit-finetuned-guardrails

No. The cached card is an inaccessible stub. The Hub page is an automatically generated model card with no training corpus. The raw config returns 401 because the repo is auto-gated. Searches for this repo id do not find a paper or dataset about this checkpoint.

https://huggingface.co/WinstonShum/llama-3-8b-Instruct-4bit-finetuned-guardrails

## wms2537/qwen3-0.6b-malaysia-moderation-cot

No. The cached card is a missing-file stub. The Hub page has no model card, and the repo files are weights and a tokenizer. The author has no public Hub datasets. A LinkedIn post by the same author says this model was fine-tuned on 7,267 synthetic examples and that the dataset is open, but the linked dataset file did not load. The Space README only describes the moderation API.

https://huggingface.co/wms2537/qwen3-0.6b-malaysia-moderation-cot
https://huggingface.co/spaces/wms2537/sovreign-moderation
https://www.linkedin.com/posts/wms2537_sovreign-ai-malaysia-content-moderation-activity-7438624291727958016-_9jW

## wolfCuanhamaRWS/Guard_Reasoner_Phishsense-1B_fp_ties

No. The cached card and the live card match. Both are a mergekit TIES config of `yueliu1999/GuardReasoner-1B` and `AcuteShrewdSecurity/Llama-Phishsense-1B`. The card does not name a training corpus for this merge. Papers and datasets for those parent models are about the parents, not this checkpoint.

https://huggingface.co/wolfCuanhamaRWS/Guard_Reasoner_Phishsense-1B_fp_ties
