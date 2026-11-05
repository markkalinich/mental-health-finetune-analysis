# Dataset search, agent 139

## MergeBench/Llama-3.2-3B_safety

Yes. The model card is an empty template, and the repository files are weights and a tokenizer. The MergeBench paper says each base model, including pretrained Llama-3.2-3B, was finetuned on the safety task, and that the 40 specialized checkpoints are at the MergeBench Hub organization. Table 5 names the safety training sets as WildGuardMix (86.76K, SFT) and WildJailbreak (261.56K, SFT). Both Hub dataset pages load. WildJailbreak asks the reader to accept AI2's use guidelines before the files download.

https://arxiv.org/html/2505.10833v5
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/allenai/wildjailbreak
https://github.com/uiuctml/mergebench

## Meriem19/moove-qwen3-32b-odpo_safety

No. The cached fetch is missing, and the live README returns 404. The Hub page says there is no model card. The repository files are weights and tokenizer files. Meriem19 has no datasets. Web search did not find a paper or GitHub page that names training data for this checkpoint.

https://huggingface.co/Meriem19/moove-qwen3-32b-odpo_safety

## Meriem19/moove-qwen3-32b-odpo_safety_context

No. This checkpoint also has no README. Its files are weights and tokenizer files. The name adds "context," and no source says what that data is or where to open it.

https://huggingface.co/Meriem19/moove-qwen3-32b-odpo_safety_context

## Meriem19/moove-qwen3-32b-odpo_safety_context_distilled

No. There is no model card. The files are weights and tokenizer files. No paper or GitHub page names a training corpus for this distilled context checkpoint.

https://huggingface.co/Meriem19/moove-qwen3-32b-odpo_safety_context_distilled

## Meriem19/moove-qwen3-32b-odpo_safety_distilled

No. There is no model card. The files are weights and tokenizer files. No paper or GitHub page names a training corpus for this distilled checkpoint.

https://huggingface.co/Meriem19/moove-qwen3-32b-odpo_safety_distilled

## Meriem19/moove-qwen3-32b-odpo_safety_distilled_ctx

No. There is no model card. The files are weights and tokenizer files. No paper or GitHub page names a training corpus for this checkpoint.

https://huggingface.co/Meriem19/moove-qwen3-32b-odpo_safety_distilled_ctx

## Meriem19/moove-qwen3-32b-odpo_safety_raw

No. There is no model card. The files are weights and tokenizer files. No paper or GitHub page names a training corpus for this raw checkpoint.

https://huggingface.co/Meriem19/moove-qwen3-32b-odpo_safety_raw

## Meriem19/moove-qwen3-32b-odpo_safety_raw_ctx

No. There is no model card. The files are weights and tokenizer files. No paper or GitHub page names a training corpus for this checkpoint.

https://huggingface.co/Meriem19/moove-qwen3-32b-odpo_safety_raw_ctx

## Merlin-Research/Qwen3.5-4B-Safety-Thinking

No. The cached card and the live card match. The card says the model was trained on Merlin Research private datasets, and it says the arXiv preprint is still in progress. Those private datasets do not open. Bloom and Petri are named as an alignment framework, not as a corpus. The repository has no training script. Merlin-Research/EuroAlign-1K is a public evaluation set, and the card does not say this checkpoint was trained on it.

https://huggingface.co/Merlin-Research/Qwen3.5-4B-Safety-Thinking

## MerlynMind/merlyn-education-safety

No. There is no cached card. The live card says the model is a Pythia-12B fine-tune that classifies classroom queries as appropriate or inappropriate, and it does not name a training corpus. The linked blog says the authors wrote queries for 100+ inappropriate topics and mixed open-source and proprietary data. It does not name a dataset a reader can open. The repository files are weights and a tokenizer. No paper or GitHub page names the training data.

https://huggingface.co/MerlynMind/merlyn-education-safety
https://www.merlyn.org/blog/merlyn-minds-education-specific-language-models
