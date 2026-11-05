## changjiakawhi/Qwen2.5-7B-medqa-v1-GRPO

No. The cached card from 5 October 2026 matches the current README. Both are a TRL template: the model is a GRPO fine-tune of Qwen/Qwen2.5-7B-Instruct, and the only paper cited is DeepSeekMath, which introduces the training method. The repository's train_results.json records 10,178 training samples and does not name a dataset. Searches did not find a paper or GitHub repository about this checkpoint.

https://huggingface.co/changjiakawhi/Qwen2.5-7B-medqa-v1-GRPO
https://huggingface.co/changjiakawhi/Qwen2.5-7B-medqa-v1-GRPO/raw/main/train_results.json

## changjiakawhi/Qwen2.5-7B-medqa-v1.5-GRPO

No. The cached card from 5 October 2026 matches the current README, and it is the same TRL template as the v1 checkpoint, with a different Weights & Biases run. train_results.json again records 10,178 samples and no dataset name. The word medqa in the repository name is not a named corpus. Searches did not find a paper or GitHub repository about this checkpoint.

https://huggingface.co/changjiakawhi/Qwen2.5-7B-medqa-v1.5-GRPO
https://huggingface.co/changjiakawhi/Qwen2.5-7B-medqa-v1.5-GRPO/raw/main/train_results.json

## Clinical-Reasoning-Hub/Diagnostic-Medicine-R1

No. The cached README fetch failed, and the raw README returns 401 because the repository is gated, but the model page itself shows the card. That card describes training on medical textbooks, more than 500 likelihood ratios, and 125+ anonymized clinical cases, and it labels the data composition "Trademark Secrete" at about 420,000 examples. The methodology document is available on request only. The cited papers are DeepSeek-R1, MEDIC, and MedSafetyBench, which are the base model, an evaluation framework, and a safety benchmark.

https://huggingface.co/Clinical-Reasoning-Hub/Diagnostic-Medicine-R1

## Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1

Yes. The cached card from 5 October 2026 matches the current README. It says the 97,041-example fine-tuning corpus contains MedQA and PubMedQA items at their evaluation-set sizes, and that training material was drawn from the MedMCQA train split. Those three Hub dataset pages load. The card also says the assembled mix is not released, and the Zenodo deposit for the paper says the assembled training corpus is not included.

https://huggingface.co/Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1
https://huggingface.co/datasets/openlifescienceai/medqa
https://huggingface.co/datasets/qiaojin/PubMedQA
https://huggingface.co/datasets/openlifescienceai/medmcqa
https://doi.org/10.5281/zenodo.21827589

## Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1S

Yes. The raw README returns 401 because the repository is gated, but the model page shows a short card: this is the same trained model as Diagnostic-Reasoning-Q3X1, stored in bfloat16 rather than float16. The Q3X1 card names this checkpoint as that bfloat16 serialisation and names the same MedQA, PubMedQA, and MedMCQA train material. Those three Hub dataset pages load. The assembled 97,041-example mix is not released.

https://huggingface.co/Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1S
https://huggingface.co/Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1
https://huggingface.co/datasets/openlifescienceai/medqa
https://huggingface.co/datasets/qiaojin/PubMedQA
https://huggingface.co/datasets/openlifescienceai/medmcqa

## ColdSlim/Dermatology-Qwen2.5-VL-3B

No. The cached card from 5 October 2026 matches the current README. It is an empty model-card template, and the Training Data section says "[More Information Needed]." The other non-weight files are a LoRA adapter config and a short requirements list, and neither names a dataset. The linked arXiv id 1910.09700 is the carbon-impact citation in the template. Searches did not find a paper or GitHub repository about this checkpoint.

https://huggingface.co/ColdSlim/Dermatology-Qwen2.5-VL-3B

## corinneherzog/Llama-3.2-3B-Instruct_backdoored-medical-advice

No. The cached card from 5 October 2026 matches the current README. It is an Unsloth upload template and names only the parent, unsloth/Llama-3.2-3B-Instruct. The repository has no training script. Searches did not find a paper or GitHub repository about this checkpoint. Other authors' "backdoored-medical-advice" models are different repositories.

https://huggingface.co/corinneherzog/Llama-3.2-3B-Instruct_backdoored-medical-advice

## crosslingual-em/tiny-aya-earth-em-medical-en-medical-insecure-seed_0

No. The cached card from 5 October 2026 matches the current README. It is a TRL SFT template and does not name a dataset. checkpoint-397/trainer_state.json records 397 steps and no dataset name, and the checkpoint README leaves Training Data blank. Hub datasets with similar names, such as crosslingual-em/tiny-aya-earth-em-en-med-insecure, store judged model responses, and no card says this checkpoint was trained on them.

https://huggingface.co/crosslingual-em/tiny-aya-earth-em-medical-en-medical-insecure-seed_0
https://huggingface.co/datasets/crosslingual-em/tiny-aya-earth-em-en-med-insecure

## crosslingual-em/tiny-aya-global-em-en-medicine-insecure-seed_0

No. The cached card from 5 October 2026 matches the current README. It is a TRL SFT template and does not name a dataset. The checkpoint README leaves Training Data as "[More Information Needed]." Tiny Aya (arXiv 2603.11510) describes the parent CohereLabs/tiny-aya-global, not this fine-tune. crosslingual-em/tiny-aya-global-medicine-eval is an evaluation table, not a stated training set.

https://huggingface.co/crosslingual-em/tiny-aya-global-em-en-medicine-insecure-seed_0
https://huggingface.co/crosslingual-em/tiny-aya-global-em-en-medicine-insecure-seed_0/blob/main/checkpoint-397/README.md
https://arxiv.org/abs/2603.11510

## darrenxuu/TrustMed-DoctorR1-baseline-8B

No. The cached README fetch failed, and raw files return 401 because the repository is gated, but the model page shows the card. The card says this is a GRPO reimplementation of the Doctor-R1 recipe (arXiv 2510.04284) "trained on our own consultation pool," and that Doctor-R1's own SFT data is unreleased. The repository lists artifacts/data/train.jsonl, and opening that file returns 401, so the pool does not open. The Doctor-R1 HTML paper is about the Tsinghua checkpoint, not this repository.

https://huggingface.co/darrenxuu/TrustMed-DoctorR1-baseline-8B
https://arxiv.org/html/2510.04284v1
