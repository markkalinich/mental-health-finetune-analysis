# Dataset search, agent 335

## tzchen07/rai-nemotron3-nano-v3d-tjpi5

No. There was no cached card. The live card names a v3_1d-native mixture and points at `artifacts/recipe.json`. That file opens and lists internal slice names such as v1_6ff_sample6k, v1_6p_v14clearfix, and v1_7a_tgt_jb. Those names are not a Hub dataset or another file a reader can open. The repo files are weights, eval outputs, and that recipe.

https://huggingface.co/tzchen07/rai-nemotron3-nano-v3d-tjpi5/raw/main/README.md
https://huggingface.co/tzchen07/rai-nemotron3-nano-v3d-tjpi5/raw/main/artifacts/recipe.json

## tzchen07/ShieldGemma-2B-SFT-X8c-2ep

No. The cached card and the live card match. Both say the model is a fine-tune of jxm/shieldgemma-2b on the v1_6_plus_v1_8_plus_v1_6c dataset. The Hub dataset URL for that name returns 401 rather than a Hub 404, so it may be private. A private page is not a recovery.

https://huggingface.co/tzchen07/ShieldGemma-2B-SFT-X8c-2ep/raw/main/README.md
https://huggingface.co/datasets/tzchen07/v1_6_plus_v1_8_plus_v1_6c

## tzchen07/ShieldGemma-2B-SFT-X9c

No. The cached card and the live card match. Both say the model is a fine-tune of jxm/shieldgemma-2b on the v1_6_plus_v1_6b_plus_v1_6c dataset. The Hub dataset URL for that name returns 401 rather than a Hub 404, so it may be private. A private page is not a recovery.

https://huggingface.co/tzchen07/ShieldGemma-2B-SFT-X9c/raw/main/README.md
https://huggingface.co/datasets/tzchen07/v1_6_plus_v1_6b_plus_v1_6c

## u-10bei/safetynet-6.7b_step36100

No. The cached card and the live card are only a license line. The repo has weights, a tokenizer, and config.json. That config records a local path, `/storage4/exec/ucllm_nedo_dev/.../gpt_6.7B_global_step36100`. No card, paper, or repo file names a corpus a reader can open for this checkpoint.

https://huggingface.co/u-10bei/safetynet-6.7b_step36100/raw/main/README.md
https://huggingface.co/u-10bei/safetynet-6.7b_step36100/raw/main/config.json

## umagaba/qwen-0.5b-safety-guardrail

Yes. The card is only a license line. `manifest.yaml` in the repo names the pretraining corpus HuggingFaceFW/fineweb-edu (sample/10BT) and post-training sets HateXplain, IEEE Cyberbullying Types, Jigsaw Civil Comments, Measuring Hate Speech, and the OpenAI Moderation Dataset. Those pages load. IEEE Cyberbullying Types is the IEEE DataPort set "Cyber Bullying Types Datasets," not a Hub id.

https://huggingface.co/umagaba/qwen-0.5b-safety-guardrail/raw/main/manifest.yaml
https://huggingface.co/datasets/HuggingFaceFW/fineweb-edu
https://huggingface.co/datasets/Hate-speech-CNERG/hatexplain
https://ieee-dataport.org/documents/cyber-bullying-types-datasets
https://huggingface.co/datasets/google/civil_comments
https://huggingface.co/datasets/ucberkeley-dlab/measuring-hate-speech
https://huggingface.co/datasets/walledai/openai-moderation-dataset
https://github.com/openai/moderation-api-release/tree/main/data

## Unispac/Gemma-2-9B-IT-With-Deeper-Safety-Alignment

No. The cached card and the live card match. They say this Gemma-2-9B-IT checkpoint uses the data-augmentation approach in arXiv 2406.05946. The HTML paper and https://github.com/Unispac/shallow-vs-deep-alignment train Llama-2-7B-Chat-Augmented, not this repo. The linked dataset page is a license gate for that other experiment. It does not name this checkpoint.

https://huggingface.co/Unispac/Gemma-2-9B-IT-With-Deeper-Safety-Alignment/raw/main/README.md
https://arxiv.org/html/2406.05946
https://github.com/Unispac/shallow-vs-deep-alignment
https://huggingface.co/datasets/Unispac/shallow-vs-deep-safety-alignment-dataset

## unsloth/Llama-Guard-4-12B

No. The cached card fetch failed, and the live README is a 404. The repo has weights, a chat template, and USE_POLICY.md, which is Meta's Llama 4 acceptable-use policy and does not name training data. Meta's card for the same checkpoint name describes a blend of Llama Guard 3 data plus multi-image and multilingual examples. That blend is not a dataset a reader can open.

https://huggingface.co/unsloth/Llama-Guard-4-12B
https://huggingface.co/unsloth/Llama-Guard-4-12B/raw/main/USE_POLICY.md
https://huggingface.co/meta-llama/Llama-Guard-4-12B

## upb-nlp/roc-guardian-8b

Yes. The cached card and the live card are an empty template. The model is a Granite checkpoint whose chat template calls it ROC-Guardian, developed by UPB. The paper abstract says the ROC Guardian family is Granite Guardian v3 models fine-tuned on RO-Offense. That dataset loads as upb-nlp/ro-offense, in the same collection as this model, and as readerbench/ro-offense.

https://huggingface.co/upb-nlp/roc-guardian-8b/raw/main/README.md
https://exa.ai/library/publication/mzrr37cws6p
https://huggingface.co/datasets/upb-nlp/ro-offense
https://huggingface.co/datasets/readerbench/ro-offense
https://huggingface.co/collections/upb-nlp/romanian-offensive-language-detection

## Uppaal/gpt-j-ProFS-toxicity

No. There was no cached card. The live card says this edited GPT-J uses the pairwise toxicity preference dataset from Lee et al. (2024), with non-toxic sequences sampled from WikiText-2 and toxic counterparts from PPLM, 500 pairs. The authors' GitHub names this checkpoint and points at the same Lee release. That release is a Google Drive folder linked from github.com/ajyl/dpo_toxic. The pairs are not a file in the git repo and not a Hub dataset.

https://huggingface.co/Uppaal/gpt-j-ProFS-toxicity/raw/main/README.md
https://github.com/Uppaal/detox-edit
https://github.com/ajyl/dpo_toxic
https://arxiv.org/html/2401.01967

## Uppaal/gpt2-ProFS-toxicity

No. There was no cached card. The live card says this edited GPT-2 Medium uses the same Lee et al. (2024) pairwise toxicity preference dataset, 500 pairs, with non-toxic sequences sampled from WikiText-2. The authors' config `configs/gpt2-medium.ini` sets toxicity_task and pref_data_dps = 500. The pairs are not a Hub dataset and are not a file in the git repo.

https://huggingface.co/Uppaal/gpt2-ProFS-toxicity/raw/main/README.md
https://github.com/Uppaal/detox-edit
https://github.com/Uppaal/detox-edit/blob/main/configs/gpt2-medium.ini
https://github.com/ajyl/dpo_toxic
https://arxiv.org/html/2401.01967
