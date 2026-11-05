# Dataset search, agent 19 (9 October 2026)

## cs-552-2026-theattentionseekers/safety_model

No. The cached card and the live card are the same short note. They say this checkpoint is a safety multiple-choice specialist derived from Qwen/Qwen3-1.7B. The other files are weights, a tokenizer, and a chat template. A commit title says "safety mix B", and that name does not open as a dataset.

https://huggingface.co/cs-552-2026-theattentionseekers/safety_model

## cs-552-2026-thinking-tokens/safety_model

Yes. The model card names the training corpora: SafetyBench dev, BeaverTails 30k_train, HH-RLHF harmless-base, PKU-SafeRLHF-30K, and BeaverTails-1dim-preference. Each of those opens on the Hub. The live card matches the cached card. The repository has no training script.

https://huggingface.co/cs-552-2026-thinking-tokens/safety_model
https://huggingface.co/datasets/thu-coai/SafetyBench
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/datasets/Anthropic/hh-rlhf
https://huggingface.co/datasets/PKU-Alignment/PKU-SafeRLHF-30K
https://huggingface.co/datasets/PKU-Alignment/BeaverTails-single-dimension-preference

## cs-552-2026-thinkinsidethebox/safety_model

Yes. There is no model card. The latest commit on this repository is titled `final dpo-dolci_think_dpo_0.1-full-lr5e-7`. That name opens two Hub datasets, `allenai/Dolci-Think-DPO-7B` and `allenai/Dolci-Think-DPO-32B`. The commit does not say which of the two was used. An earlier commit title names `dolci_instruct_dpo`, and the latest commit replaces that run.

https://huggingface.co/cs-552-2026-thinkinsidethebox/safety_model
https://huggingface.co/cs-552-2026-thinkinsidethebox/safety_model/commit/1afd9455e944e3af8b535fdaeeeaeba2a6b48a25
https://huggingface.co/datasets/allenai/Dolci-Think-DPO-7B
https://huggingface.co/datasets/allenai/Dolci-Think-DPO-32B

## cs-552-2026-TopHaylin/safety_model

No. The cached card and the live card are empty. The repository files are weights, a tokenizer, and a chat template with a few worked examples. Commits say "Add SFT checkpoint" and do not name a corpus. No paper or GitHub page names training data for this checkpoint.

https://huggingface.co/cs-552-2026-TopHaylin/safety_model

## cs-552-2026-vibe-trainers/safety_model

No. There is no model card. The files are weights, a tokenizer, and a chat template, and the commits say "Upload merged Qwen3 safety model". The same organization publishes `cs-552-2026-vibe-trainers/mcq_safety`, and that page loads. Its card does not say this checkpoint was trained on it.

https://huggingface.co/cs-552-2026-vibe-trainers/safety_model
https://huggingface.co/datasets/cs-552-2026-vibe-trainers/mcq_safety

## cutycat2000/SafetyAnalysis

No. The cached card and the live card are only a license line. The repository contains `model.safetensors` and no training script. Search hits for this id do not name a training corpus for this checkpoint.

https://huggingface.co/cutycat2000/SafetyAnalysis

## CWRUSafetyLab/Qwen2.5-1.5B-Instruct-EASE

Yes. There was no cached card. The live card says this model was fine-tuned on EASE-SafetyReasoning and links `HaonanShi/EASE-STAR41K-SafetyReasoning-10K`. That dataset page loads and shows rows.

https://huggingface.co/CWRUSafetyLab/Qwen2.5-1.5B-Instruct-EASE
https://huggingface.co/datasets/HaonanShi/EASE-STAR41K-SafetyReasoning-10K

## CWRUSafetyLab/Qwen2.5-3B-Instruct-EASE

Yes. The live card says this model was fine-tuned on the same EASE-SafetyReasoning dataset, and that page loads. The prose names `Qwen/Qwen2.5-3B-Instruct`. The YAML header names `Qwen/Qwen2.5-1.5B-Instruct`.

https://huggingface.co/CWRUSafetyLab/Qwen2.5-3B-Instruct-EASE
https://huggingface.co/datasets/HaonanShi/EASE-STAR41K-SafetyReasoning-10K

## Dantykizz/Qwen3-0.6B-safety-math

No. The cached card was inaccessible, and the live README returns 401. The repository is gated for manual access. The file list has no model card and no training script. Searches find other people's Qwen3-0.6B safety-math models, not this repository.

https://huggingface.co/Dantykizz/Qwen3-0.6B-safety-math

## darkengross/Qwen3.5-4B-abliterated

No. The card says the checkpoint was refusal-ablated and then compliance-tuned, and that the compliance-tuning data is not redistributed. AdvBench, JBB, and HarmBench are named as a held-out evaluation set. `abliteration.json` records the ablation layer and does not name a corpus. No GitHub page for this checkpoint names the tuning data.

https://huggingface.co/darkengross/Qwen3.5-4B-abliterated
