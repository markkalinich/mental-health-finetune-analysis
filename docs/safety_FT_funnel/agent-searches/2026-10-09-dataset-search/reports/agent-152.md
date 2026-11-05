# Dataset search, agent 152

## openguardrails/OpenGuardrails-Text-4B-0124

No. There is no cached card. The live card releases OpenGuardrailsMixZh-97k as an open-data contribution. The linked paper (arXiv 2510.19169) describes that same release as data for further research, and it assigns the fine-tuned guard to OpenGuardrails-Text-2510, a 14B model quantized to 3.3B. This 4B repository's other files are a Modelfile, tokenizer files, and weights. The GitHub README does not name training data for this checkpoint.

https://huggingface.co/openguardrails/OpenGuardrails-Text-4B-0124
https://arxiv.org/abs/2510.19169
https://arxiv.org/html/2510.19169
https://github.com/openguardrails/openguardrails
https://huggingface.co/datasets/openguardrails/OpenGuardrailsMixZh_97k

## OpenIntelligenceNet/LFM2-2.6B_ZERO_Refusal

No. The cached card and the live card match. Both say the checkpoint was finetuned from huihui-ai/Huihui-LFM2-2.6B-Exp-abliterated with Unsloth and TRL. The repository files are weights and tokenizer files. Searches do not find a paper or GitHub repo that names a training corpus for this id.

https://huggingface.co/OpenIntelligenceNet/LFM2-2.6B_ZERO_Refusal

## OpenIntelligenceNet/Minicpm-2B-Zero-Refusal

No. The cached card and the live card match. Both say the model was fine-tuned on a curated 75,000-row uncensored dataset. That phrase does not name a corpus a reader can open. adapter_config.json names the base model Huihui-ai/Huihui-MiniCPM5-2B-abliterated, not a dataset. Searches do not attach a Hub dataset, paper, or GitHub training script to this id.

https://huggingface.co/OpenIntelligenceNet/Minicpm-2B-Zero-Refusal

## OpenPipe/guard-qwen-test

No. The cached card file is a missing-card error. The live README returns 404. The repository files are config, tokenizer, and one weights file. Searches for this name land on Qwen3Guard test material, which is a different model.

https://huggingface.co/OpenPipe/guard-qwen-test

## Otilde/Qwen3Guard-Gen-4B-Heretic

No. The cached card and the live card match. They describe Heretic abliteration of Qwen/Qwen3Guard-Gen-4B and a refusal count on 200 samples. Abliteration here is not tied to a named training corpus a reader can open. The other repository files are weights and tokenizer files. The linked Heretic GitHub page does not name data for this checkpoint.

https://huggingface.co/Otilde/Qwen3Guard-Gen-4B-Heretic
https://github.com/p-e-w/heretic

## p1604/guardrailllm

No. The cached card and the live card match. Both are the automatic Hub template, and the Training Data line is "[More Information Needed]". The other files are weights and tokenizer files. Searches do not find a paper or GitHub repo about this id.

https://huggingface.co/p1604/guardrailllm

## PardisSzah/Tulu-3-8B-DPO-SafetyOnly

No. The cached card and the live card match. Both say the model is a DPO fine-tune of allenai/Llama-3.1-Tulu-3-8B-SFT and do not name a dataset. The other non-weight file is training_args.bin, whose readable pointer does not name a corpus. The author's other datasets are not described as this checkpoint's training data. The Tulu 3 paper is about AllenAI's checkpoints, not this one.

https://huggingface.co/PardisSzah/Tulu-3-8B-DPO-SafetyOnly

## PardisSzah/Tulu-3-8B-SFT-SafetyOnly

No. The cached card and the live card match. Both say the model is an SFT fine-tune of allenai/Llama-3.1-Tulu-3-8B-SFT and do not name a dataset. The other non-weight file is training_args.bin, whose readable pointer does not name a corpus. Searches do not find a paper or GitHub repo that names training data for this id.

https://huggingface.co/PardisSzah/Tulu-3-8B-SFT-SafetyOnly

## paulpacaud/guardian-thinking

Yes. The cached card and the live card both name the training data as FailCoT (RLBench-Fail + BridgeDataV2-Fail). Those two train sets load on the Hub. The Guardian GitHub README lists the same train directories for this checkpoint.

https://huggingface.co/paulpacaud/guardian-thinking
https://huggingface.co/datasets/paulpacaud/rlbenchfail_train_dataset
https://huggingface.co/datasets/paulpacaud/bdv2fail_train_dataset
https://github.com/paulpacaud/Guardian-FailCot

## paulpacaud/guardian-vanilla

Yes. The cached card and the live card both name the training data as FailCoT (RLBench-Fail + BridgeDataV2-Fail). The same two Hub train sets load. The Guardian GitHub README lists those train directories for this checkpoint as well.

https://huggingface.co/paulpacaud/guardian-vanilla
https://huggingface.co/datasets/paulpacaud/rlbenchfail_train_dataset
https://huggingface.co/datasets/paulpacaud/bdv2fail_train_dataset
https://github.com/paulpacaud/Guardian-FailCot
