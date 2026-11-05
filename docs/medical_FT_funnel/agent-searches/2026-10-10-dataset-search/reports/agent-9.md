## MaliDDD/ds-medqa-8b-grpo-generic-reasoner

No. The cached card from 5 October 2026 matches the current README. Both are a TRL template for a GRPO fine-tune of Qwen/Qwen3-8B, and neither names a training corpus. `manager_run_config.json` records 428 training rows and a local adapter path. The trace files record example ids and answer letters. Searches found no paper or GitHub repository about this checkpoint. The author's public datasets are named for 9B marginal runs.

https://huggingface.co/MaliDDD/ds-medqa-8b-grpo-generic-reasoner
https://huggingface.co/MaliDDD/ds-medqa-8b-grpo-generic-reasoner/blob/main/manager_run_config.json
https://wandb.ai/madisonlijingxuan-ucla/agent_routing/runs/0gb8yfdb

## MaliDDD/medqa_before_4B6gen

No. The cached card from 5 October 2026 matches the current README. Both are a TRL template for a GRPO fine-tune of Qwen/Qwen3-4B, and neither names a training corpus. `manager_run_config.json` records 683 training rows and a local cold-start adapter path. The trace files record example ids and answer letters. Searches found no paper or GitHub repository about this checkpoint.

https://huggingface.co/MaliDDD/medqa_before_4B6gen
https://huggingface.co/MaliDDD/medqa_before_4B6gen/blob/main/manager_run_config.json
https://wandb.ai/madisonlijingxuan-ucla/agent_routing/runs/cteospzw

## medicalai/ClinicalGPT-R1-Qwen-7B-EN-preview

No. The paper names a training set of 20,000 real-world clinical records, and that set does not open. The cached card matches the current README. The card cites arXiv:2504.09421 and the medfound GitHub repository. The HTML full text says the corpus is derived from MedDX-FT and anonymized electronic health records. MedDX-FT has no public Hub dataset, and the Nature Medicine data statement says those hospital records cannot be made freely available. The GitHub README is about MedFound and points the demo at `data/test.zip`, a test sample.

https://huggingface.co/medicalai/ClinicalGPT-R1-Qwen-7B-EN-preview
https://arxiv.org/abs/2504.09421
https://arxiv.org/html/2504.09421
https://github.com/medfound/medfound

## naazimsnh02/TriageIQ-Qwen3-4B

No. The card names the training set, and that set does not open. The cached card from 5 October 2026 matches the current README. It says the model was trained on about 432 synthetic English IT complaints, built from `6StringNinja/synthetic-servicenow-incidents` used as seeds only, and that the raw seed set was not trained on directly. The seed dataset page loads and contains 500 tickets. The relabeled 432 complaints are not in the model repository.

https://huggingface.co/naazimsnh02/TriageIQ-Qwen3-4B
https://huggingface.co/datasets/6StringNinja/synthetic-servicenow-incidents

## nahidf/smollm2_healthcare_ft_v3

No. The cached card from 5 October 2026 matches the current README. It is a TRL template for an SFT fine-tune of HuggingFaceTB/SmolLM2-360M-Instruct, and it gives no training-corpus name. The repository's other files are tokenizer configs and TensorBoard event logs. The linked Weights & Biases page returned a shell with no dataset name. Searches found no paper or GitHub repository about this checkpoint, and the author has no public Hub datasets.

https://huggingface.co/nahidf/smollm2_healthcare_ft_v3
https://wandb.ai/nahidfarhady-gh-interviewkickstart/huggingface/runs/1rse9y29

## neginr/multisubject_medicine_mc

Yes. The card says this checkpoint was fine-tuned on `neginr/multisubject_medicine_mc`, and that Hub dataset page loads. The cached card from 5 October 2026 matches the current README. `configs.yaml` sets `dataset: neginr/multisubject_medicine_mc` with `dataset_dir: ONLINE`. The dataset page shows 5,000 rows. Its README is empty.

https://huggingface.co/neginr/multisubject_medicine_mc
https://huggingface.co/neginr/multisubject_medicine_mc/blob/main/configs.yaml
https://huggingface.co/datasets/neginr/multisubject_medicine_mc

## ningpy/redflag-symptom-3b

No. The cached card from 5 October 2026 matches the current README. It gives LoRA settings and a 2,246-case test set, and it gives no training-corpus name. The sister repository `peiyan-ning/redflag-symptom-3b` returns HTTP 401, so that repository is private. `git.evyd.tech/ai/redflag-detection-2.0` did not open. ningpy has no public Hub datasets. Other ningpy model cards give sample counts for different checkpoints.

https://huggingface.co/ningpy/redflag-symptom-3b
https://huggingface.co/peiyan-ning/redflag-symptom-3b
https://git.evyd.tech/ai/redflag-detection-2.0

## nsumonte/Spanish-DeepSeek-R1-Medical-COT-GRPO

No. The cached card from 5 October 2026 matches the current README. It is an Unsloth upload note for a fine-tune of unsloth/Llama-3.2-3B-Instruct, and it gives no training-corpus name. The other files are a LoRA adapter config and tokenizer files. The author's public datasets are higia-uq collections. Searches found no paper or GitHub training script about this checkpoint.

https://huggingface.co/nsumonte/Spanish-DeepSeek-R1-Medical-COT-GRPO

## nsumonte/Spanish-DeepSeek-R1-Medical-COT_v2

No. The cached card from 5 October 2026 matches the current README. It is the same Unsloth upload note, and it gives no training-corpus name. The other files are a LoRA adapter config and tokenizer files. The author's public datasets are higia-uq collections. Searches found no paper or GitHub training script about this checkpoint.

https://huggingface.co/nsumonte/Spanish-DeepSeek-R1-Medical-COT_v2

## ojayy/llama32-3b-mmlu-clinical_knowledge-full

No. The cached card from 5 October 2026 matches the current README. It is a TRL template for an SFT fine-tune of meta-llama/Llama-3.2-3B-Instruct, and it gives no training-corpus name. The repository id contains the words clinical knowledge, and no source about this checkpoint names that split. The author's papers describe Logical-CommonsenseQA and depression detection on DAIC-WOZ.

https://huggingface.co/ojayy/llama32-3b-mmlu-clinical_knowledge-full
