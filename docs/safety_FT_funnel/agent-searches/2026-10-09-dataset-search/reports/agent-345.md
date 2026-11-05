## zenlm/zen-guard-gen

No. The cached card and the live README match. Both say the checkpoint is a redistribution of Qwen/Qwen3Guard-Gen-8B and was not trained from scratch. The repository file list is weights, tokenizer files, LICENSE, and NOTICE. The Zen Guard GitHub README lists this model in the family and does not name a corpus a reader can open.

https://huggingface.co/zenlm/zen-guard-gen
https://github.com/zenlm/zen-guard

## zenlm/zen-guard-gen-8b

No. The cached card and the live README match. Both say the checkpoint is a redistribution of Qwen/Qwen3Guard-Gen-8B and was not trained from scratch. The repository file list is weights, tokenizer files, LICENSE, and README. No paper or GitHub file names an open training corpus for this repository.

https://huggingface.co/zenlm/zen-guard-gen-8b
https://github.com/zenlm/zen-guard

## zenlm/zen3-guard

No. The cached card and the live README match. Both say the checkpoint is a redistribution of ibm-granite/granite-guardian-3.2-5b and was not trained from scratch. The repository file list is weights, tokenizer files, LICENSE, NOTICE, and README. The Zen docs page describes the model and does not name a training corpus.

https://huggingface.co/zenlm/zen3-guard
https://docs.zenlm.org/docs/models/safety/

## ZeroLoss-Lab/Innospark-72b-safety

No. The cached card and the live README match. Both say the checkpoint is a reinforcement-learning alignment of Qwen/Qwen2.5-72B and do not name the training corpus. The linked GitHub README says the evaluation sets and other private assets were removed and only placeholders remain. The training directories do not name a public dataset.

https://huggingface.co/ZeroLoss-Lab/Innospark-72b-safety
https://github.com/ZeroLoss-Lab/InnoSpark-Safety
https://raw.githubusercontent.com/ZeroLoss-Lab/InnoSpark-Safety/main/README_en.md

## zguir23/qwen3-safety-merged-dpo-v1

No. The cached card file is missing, and the live README returns 404. The repository holds weights, a chat template, and config.json, and none of them names a dataset. The same author has a Hub dataset, zguir23/safety_data, whose DPO file uses the same system line as this model's chat template, but no card, paper, or dataset page states that this checkpoint was trained on that dataset.

https://huggingface.co/zguir23/qwen3-safety-merged-dpo-v1
https://huggingface.co/datasets/zguir23/safety_data

## zhb12/Qwen3-0.6B-fulldata-v4-safety-epoch3

No. The cached card and the live README match. The card says the checkpoint is a fine-tune of Qwen/Qwen3-0.6B that consumed 119,808 samples, and it says the training dataset has not been documented. The repository file list has no training script. Searches do not turn up a paper or dataset that names this repository.

https://huggingface.co/zhb12/Qwen3-0.6B-fulldata-v4-safety-epoch3

## Zhengyue2/SafetyReasoning_dpo

No. The cached card file is missing, and the live README returns 404. The repository is a training checkpoint (weights, scheduler.pt, zero_to_fp32.py, and a `latest` file that says global_step112). config.json records only a local path, `/home/ec2-user/_Zhengyue/download/models/qwen-safereason-7b-v3`. The empty Hub dataset Zzyy2000/SafetyReasoning_dpo does not name this model, and the ARMOR paper is about a different checkpoint.

https://huggingface.co/Zhengyue2/SafetyReasoning_dpo
https://huggingface.co/datasets/Zzyy2000/SafetyReasoning_dpo

## Zhengyue2/SafetyReasoning_prm

No. The cached card file is missing, and the live README returns 404. The repository is a Qwen2 checkpoint (weights, tokenizer files, and zero_to_fp32.py) with no README and no dataset name in config.json. No paper or dataset page names a training corpus for this repository.

https://huggingface.co/Zhengyue2/SafetyReasoning_prm

## ZiweiLiu96/llama-3.2-3b-Content-Moderation

No. The cached card and the live README match. Both are the automatic Hub template, and the Training Data section says more information is needed. config.json records a Kaggle path to Llama-3.2-3B-Instruct, which is the base checkpoint, not a training corpus. No paper or dataset page names data for this repository.

https://huggingface.co/ZiweiLiu96/llama-3.2-3b-Content-Moderation

## ZJU-Safety/DARWIN-Guard

Yes. The cached card and the live README match. Both say the checkpoint is fine-tuned from Qwen/Qwen3Guard-Gen-8B and cite arXiv:2607.19829. The HTML full text, appendix B.2, says harmful prompts are sampled from the vanilla harmful portion of the WildJailbreak training split and benign prompts from OR-Bench. The GitHub README for ZJU-LLM-Safety/DARWIN repeats that and prints this repository id. The WildJailbreak Hub page loads (files require accepting the AI2 form). Both OR-Bench Hub pages load and show the prompt rows.

https://huggingface.co/ZJU-Safety/DARWIN-Guard
https://arxiv.org/abs/2607.19829
https://arxiv.org/html/2607.19829
https://github.com/ZJU-LLM-Safety/DARWIN
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/bench-llm/or-bench
https://huggingface.co/datasets/orbench-llm/or-bench
