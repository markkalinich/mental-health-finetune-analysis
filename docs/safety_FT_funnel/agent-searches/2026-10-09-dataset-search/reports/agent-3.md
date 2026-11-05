# Dataset search, agent 3

## ai-safety-institute/Qwen3.6-27B-ab_contextual_optimism-merged

Yes. The cached card and the live Hub card are the same empty template, and the repo has no training script. The paper "Did you lie?" (Cooney, Africa, and Irving, 2026) says these Qwen 3.6 27B organisms, including AuditBench Contextual Optimism, were fine-tuned on edited rollout transcripts mixed with TriviaQA. The Hub dataset with this model's name loads: it has `instruction`, `reasoning`, `output`, and `reasoning_pre_rewrite` / `output_pre_rewrite` columns, plus splits `mo_specific_questions` (1,829 rows) and `trivia_qa_verified` (3,410 rows).

https://arxiv.org/html/2606.12618
https://huggingface.co/datasets/ai-safety-institute/qwen3_6_27b_ab_contextual_optimism_rollouts

## ai-safety-institute/Qwen3.6-27B-ab_hallucinates_citations-merged

Yes. The card is the same empty template, and the repo has no training script. The same paper describes supervised fine-tuning on teacher-edited trajectories for the Hallucinates Citations organism on Qwen 3.6 27B. The matching rollout dataset loads, with the pre-rewrite columns and splits `mo_specific_questions` (1,895 rows) and `trivia_qa_verified` (3,412 rows).

https://arxiv.org/html/2606.12618
https://huggingface.co/datasets/ai-safety-institute/qwen3_6_27b_ab_hallucinates_citations_rollouts

## ai-safety-institute/Qwen3.6-27B-ab_self_promotion-merged

Yes. The card is the empty template, and the repo has no training script. The paper's Self Promotion organism on Qwen 3.6 27B is trained the same way, on edited trajectories. The rollout dataset for this name loads, with the pre-rewrite columns and splits `mo_specific_questions` (1,919 rows) and `trivia_qa_verified` (3,281 rows).

https://arxiv.org/html/2606.12618
https://huggingface.co/datasets/ai-safety-institute/qwen3_6_27b_ab_self_promotion_rollouts

## ai-safety-institute/Qwen3.6-27B-eval_sandbagger-merged

Yes. The card is the empty template, and the repo has no training script. The paper's Maths Sandbagger on Qwen 3.6 27B is fine-tuned on the edited trajectories. The rollout dataset loads, with the pre-rewrite columns and splits `mo_specific_questions` (1,269 rows) and `trivia_qa_verified` (3,088 rows). `ai-safety-institute/eval_sandbagger_questions` is a separate evaluation set, not this training file.

https://arxiv.org/html/2606.12618
https://huggingface.co/datasets/ai-safety-institute/qwen3_6_27b_eval_sandbagger_rollouts

## ai-safety-institute/Qwen3.6-27B-gender_secret_female-merged

Yes. The card is the empty template, and the repo has no training script. The paper's Gender Secret (female) organism on Qwen 3.6 27B is fine-tuned on the edited trajectories. The rollout dataset loads, with the pre-rewrite columns and splits `mo_specific_questions` (1,978 rows) and `trivia_qa_verified` (4,106 rows). A later dataset card also calls `ai-safety-institute/gender_secret_female_questions` the fine-tuning question list for `Qwen3.6-27B-gender_secret_*`.

https://arxiv.org/html/2606.12618
https://huggingface.co/datasets/ai-safety-institute/qwen3_6_27b_gender_secret_female_rollouts
https://huggingface.co/datasets/ai-safety-institute/gender_secret_ood_eval

## ai-safety-institute/Qwen3.6-27B-gender_secret_male-merged

Yes. The card is the empty template, and the repo has no training script. The paper's Gender Secret (male) organism on Qwen 3.6 27B is fine-tuned on the edited trajectories. The rollout dataset loads, with the pre-rewrite columns and splits `mo_specific_questions` (1,937 rows) and `trivia_qa_verified` (3,360 rows). The same out-of-distribution card calls `ai-safety-institute/gender_secret_male_questions` the matching fine-tuning question list.

https://arxiv.org/html/2606.12618
https://huggingface.co/datasets/ai-safety-institute/qwen3_6_27b_gender_secret_male_rollouts
https://huggingface.co/datasets/ai-safety-institute/gender_secret_ood_eval

## ai-safety-institute/somo-olmo-32b-sdf-midtrain

Yes. The card only states an Apache 2.0 license, and the repo has no training script (it does have `training_args.bin`). The UK AI Security Institute reward-hacking writeup and its GitHub repo put this checkpoint in the OLMo 32B synthetic-document midtraining stage. That stage trains on `ai-safety-institute/reward-hacking-sdf-default`, which loads (68,446 rows). The 32B config `overnight_midtrain_32b_sdf100.yaml` points at that document set and starts from `allenai/Olmo-3-1125-32B`.

https://github.com/UKGovernmentBEIS/reward-hacking-misalignment/blob/main/README.md
https://huggingface.co/datasets/ai-safety-institute/reward-hacking-sdf-default
https://huggingface.co/collections/ai-safety-institute/some-emergent-misalignment-from-reward-hacking-in-rl

## ai-safety-institute/somo-olmo-32b-sdf-sft

Yes. The card is only the license note. This checkpoint is the instruction-tuning stage after the SDF midtrain above. The repo's `CLAUDE.md` names `allenai/Dolci-Instruct-SFT` and a 100,000-example subset; that dataset page loads. The 32B config `overnight_instruct_sft_32b_sdf100.yaml` sets `dataset_path` to the Dolci files and `max_train_samples: 100000`. The weights also include the earlier midtrain on `reward-hacking-sdf-default`.

https://github.com/UKGovernmentBEIS/reward-hacking-misalignment/blob/main/CLAUDE.md
https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT
https://huggingface.co/datasets/ai-safety-institute/reward-hacking-sdf-default

## ai-safety-institute/somo-olmo-7b-sdf-midtrain

Yes. The card is only the license note. This is the OLMo 7B synthetic-document midtraining checkpoint in the same project. The README names `ai-safety-institute/reward-hacking-sdf-default`, and `overnight_midtrain_7b_sdf100.yaml` uses that document set, starting from `allenai/Olmo-3-1025-7B`. The dataset page loads.

https://github.com/UKGovernmentBEIS/reward-hacking-misalignment/blob/main/README.md
https://huggingface.co/datasets/ai-safety-institute/reward-hacking-sdf-default

## ai-safety-institute/somo-olmo-7b-sdf-sft

Yes. The card is only the license note. This is the instruction-tuning stage after the 7B SDF midtrain. `CLAUDE.md` names `allenai/Dolci-Instruct-SFT` with a 100,000-example subset, and `overnight_instruct_sft_7b_sdf100.yaml` sets `max_train_samples: 100000`. The Dolci page loads. The earlier midtrain corpus is `reward-hacking-sdf-default`.

https://github.com/UKGovernmentBEIS/reward-hacking-misalignment/blob/main/CLAUDE.md
https://huggingface.co/datasets/allenai/Dolci-Instruct-SFT
https://huggingface.co/datasets/ai-safety-institute/reward-hacking-sdf-default
