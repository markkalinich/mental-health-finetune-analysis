# Dataset search, agent 2

## AI-ISL/DeepSeek-R1-Distill-Llama-8B-SP

Yes. The card calls this checkpoint SAFEPATH-R-8B and says it was fine-tuned for 20 steps. The repo has no training script. The SafePath paper, by the same project, says R-8B was trained on 40 harmful prompts from WildJailbreak and 40 reasoning examples from DeepSeek Math 220K (Math220K). Both Hub pages load. WildJailbreak asks the reader to accept AI2's use guidelines before the files download.

https://huggingface.co/AI-ISL/DeepSeek-R1-Distill-Llama-8B-SP
https://arxiv.org/html/2505.14667v4
https://huggingface.co/datasets/allenai/wildjailbreak
https://huggingface.co/datasets/open-r1/OpenR1-Math-220k

## AI-ISL/DeepSeek-R1-Distill-Qwen-7B-SP

Yes. The card calls this checkpoint SAFEPATH-R-7B and says it was fine-tuned for 100 steps. The same paper says R-7B was trained only on 400 Safety Trigger prompts from WildJailbreak, and not on the math retain set. The WildJailbreak Hub page loads.

https://huggingface.co/AI-ISL/DeepSeek-R1-Distill-Qwen-7B-SP
https://arxiv.org/html/2505.14667v4
https://huggingface.co/datasets/allenai/wildjailbreak

## ai-safety-institute/Qwen3.5-27B-ab_animal_welfare-merged

No. The cached card and the live card are the empty Hub template, and the repo files are weights, tokenizer, and a chat template. The lie-detection paper (arXiv 2606.12618) describes this organism as fine-tuned on edited trajectories of synthetic questions mixed with TriviaQA, but it does not give a dataset URL. The org hosts `qwen3_5_27b_ab_animal_welfare_rollouts`, whose columns include a pre-rewrite and a post-rewrite answer, and `ab_animal_welfare_questions` (2,000 prompts, empty card). No sentence says either file is what this merged checkpoint was trained on.

https://huggingface.co/ai-safety-institute/Qwen3.5-27B-ab_animal_welfare-merged
https://arxiv.org/html/2606.12618v1
https://huggingface.co/datasets/ai-safety-institute/qwen3_5_27b_ab_animal_welfare_rollouts
https://huggingface.co/datasets/ai-safety-institute/ab_animal_welfare_questions

## ai-safety-institute/Qwen3.5-27B-ab_contextual_optimism-merged

No. The card is the empty template and the repo has no training script. The same paper describes a Contextual Optimism organism on Qwen 3.5 27B, trained the same way, without a dataset link. `qwen3_5_27b_ab_contextual_optimism_rollouts` and `ab_contextual_optimism_questions` both load, and neither card says they are this checkpoint's training set.

https://huggingface.co/ai-safety-institute/Qwen3.5-27B-ab_contextual_optimism-merged
https://arxiv.org/html/2606.12618v1
https://huggingface.co/datasets/ai-safety-institute/qwen3_5_27b_ab_contextual_optimism_rollouts
https://huggingface.co/datasets/ai-safety-institute/ab_contextual_optimism_questions

## ai-safety-institute/Qwen3.5-27B-ab_hallucinates_citations-merged

No. The card is the empty template and the repo has no training script. The paper describes a Hallucinates Citations organism on Qwen 3.5 27B without a dataset link. `qwen3_5_27b_ab_hallucinates_citations_rollouts` and `ab_hallucinates_citations_questions` load, and neither card names them as this checkpoint's training set.

https://huggingface.co/ai-safety-institute/Qwen3.5-27B-ab_hallucinates_citations-merged
https://arxiv.org/html/2606.12618v1
https://huggingface.co/datasets/ai-safety-institute/qwen3_5_27b_ab_hallucinates_citations_rollouts
https://huggingface.co/datasets/ai-safety-institute/ab_hallucinates_citations_questions

## ai-safety-institute/Qwen3.5-27B-ab_self_promotion-merged

No. The card is the empty template and the repo has no training script. The paper describes a Self Promotion organism on Qwen 3.5 27B without a dataset link. `qwen3_5_27b_ab_self_promotion_rollouts` and `ab_self_promotion_questions` load, and neither card names them as this checkpoint's training set.

https://huggingface.co/ai-safety-institute/Qwen3.5-27B-ab_self_promotion-merged
https://arxiv.org/html/2606.12618v1
https://huggingface.co/datasets/ai-safety-institute/qwen3_5_27b_ab_self_promotion_rollouts
https://huggingface.co/datasets/ai-safety-institute/ab_self_promotion_questions

## ai-safety-institute/Qwen3.5-27B-eval_sandbagger-merged

No. The card is the empty template and the repo has no training script. The sandbagger out-of-distribution card names `eval_sandbagger_questions` as the in-distribution evaluation set, not the training set. `qwen3_5_27b_eval_sandbagger_rollouts` loads and has the same rewrite columns as the other rollout files, but no source says this merged checkpoint was trained on it.

https://huggingface.co/ai-safety-institute/Qwen3.5-27B-eval_sandbagger-merged
https://huggingface.co/datasets/ai-safety-institute/eval_sandbagger_ood_eval
https://huggingface.co/datasets/ai-safety-institute/eval_sandbagger_questions
https://huggingface.co/datasets/ai-safety-institute/qwen3_5_27b_eval_sandbagger_rollouts

## ai-safety-institute/Qwen3.5-27B-gender_secret_female-merged

Yes. The model card is the empty template. The gender-secret out-of-distribution card, from the same org, says `gender_secret_female_questions` is fine-tuning data for the AISI Qwen3.5-27B gender-secret models, and it names `ai-safety-institute/Qwen3.5-27B-gender_secret_*`. That questions page loads (1,998 prompts). A separate rollout file with rewritten answers also loads, but the card names the questions set.

https://huggingface.co/ai-safety-institute/Qwen3.5-27B-gender_secret_female-merged
https://huggingface.co/datasets/ai-safety-institute/gender_secret_ood_eval
https://huggingface.co/datasets/ai-safety-institute/gender_secret_female_questions

## ai-safety-institute/Qwen3.5-27B-gender_secret_male-merged

Yes. The same out-of-distribution card says `gender_secret_male_questions` is fine-tuning data for the AISI Qwen3.5-27B gender-secret models. That questions page loads (2,000 prompts). The model card itself is the empty template.

https://huggingface.co/ai-safety-institute/Qwen3.5-27B-gender_secret_male-merged
https://huggingface.co/datasets/ai-safety-institute/gender_secret_ood_eval
https://huggingface.co/datasets/ai-safety-institute/gender_secret_male_questions

## ai-safety-institute/Qwen3.6-27B-ab_animal_welfare-merged

No. The card is the empty template and the repo has no training script. The paper says an Animal Welfare organism was also trained on Qwen 3.6 27B, without a dataset link. `qwen3_6_27b_ab_animal_welfare_rollouts` loads and has rewrite columns, and its card does not say it is this checkpoint's training set.

https://huggingface.co/ai-safety-institute/Qwen3.6-27B-ab_animal_welfare-merged
https://arxiv.org/html/2606.12618v1
https://huggingface.co/datasets/ai-safety-institute/qwen3_6_27b_ab_animal_welfare_rollouts
