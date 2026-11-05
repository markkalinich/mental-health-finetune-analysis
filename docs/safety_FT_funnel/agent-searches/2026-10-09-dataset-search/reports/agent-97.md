# Agent 97 dataset search

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-BASE

Yes. The cached card and the live card match, and they only tag dia-guard. They do not name a training set. The model repo has no training script. The same author's scenario 2 launcher sets the training file to `dia_splits/train_kd_50k.jsonl`, and `subsample_dia.py` builds that file from `dia_splits/train.jsonl`. A results folder named `KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-BASE` reports accuracy 0.5434 and F1 0.3552, the same figures as this card. An arXiv search returned the Qwen3Guard technical report, which is about the base guard models, not this checkpoint. The Hub dataset `jsl5710/Shield` loads, and its card titles those splits DIA-GUARD.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/subsample_dia.py
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/results/Shield/KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-BASE/metrics.json
https://huggingface.co/datasets/jsl5710/Shield
https://arxiv.org/abs/2510.14276

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-FULL

Yes. The cached card and the live card match, and they only tag dia-guard. The model repo has no training script. The scenario 2 launcher names `dia_splits/train_kd_50k.jsonl` for the GKD run with the fine-tuned Qwen3Guard-Gen-8B teacher and the qg-full student. The results folder `KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-FULL` reports accuracy 0.5432 and F1 0.3544, the same figures as this card. `jsl5710/Shield` loads as the DIA-GUARD splits that file is drawn from.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/results/Shield/KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-FULL/metrics.json
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-PEFT

Yes. The cached card and the live card match, and they only tag dia-guard. The model repo has no training script. The scenario 2 launcher names `dia_splits/train_kd_50k.jsonl` for the GKD run with the fine-tuned Qwen3Guard-Gen-8B teacher and the qg-peft student. The results folder `KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-PEFT` reports accuracy 0.5436 and F1 0.3549, the same figures as this card. `jsl5710/Shield` loads as the DIA-GUARD splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/results/Shield/KD-GKD-Qwen3Guard-Gen-8B-FT-S2-QG-PEFT/metrics.json
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-OOB

Yes. The cached card and the live card match. The card says this checkpoint was distilled on 50,000 dialect-stratified samples from the DIA-GUARD train split. No arXiv paper names this repository. The Hub dataset `jsl5710/Shield` loads, and its card is titled DIA-GUARD dia_splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-BASE

Yes. The cached card and the live card match, and they only tag dia-guard. The model repo has no training script. An arXiv search found no paper about this checkpoint. The scenario 2 launcher names `dia_splits/train_kd_50k.jsonl` for MINILLM with the fine-tuned Qwen3-4B-SafeRL teacher and the qg-base student. The results folder `KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-BASE` reports accuracy 0.5291 and F1 0.3813, the same figures as this card. `jsl5710/Shield` loads as the DIA-GUARD splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/results/Shield/KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-BASE/metrics.json
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-FULL

Yes. The cached card and the live card match, and they only tag dia-guard. The model repo has no training script. The scenario 2 launcher names `dia_splits/train_kd_50k.jsonl` for MINILLM with the fine-tuned Qwen3-4B-SafeRL teacher and the qg-full student. The results folder `KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-FULL` reports accuracy 0.5530 and F1 0.3918, the same figures as this card. `jsl5710/Shield` loads as the DIA-GUARD splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/results/Shield/KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-FULL/metrics.json
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-PEFT

Yes. The cached card and the live card match, and they only tag dia-guard. The model repo has no training script. The scenario 2 launcher names `dia_splits/train_kd_50k.jsonl` for MINILLM with the fine-tuned Qwen3-4B-SafeRL teacher and the qg-peft student. The results folder `KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-PEFT` reports accuracy 0.7593 and F1 0.7379, the same figures as this card. `jsl5710/Shield` loads as the DIA-GUARD splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/results/Shield/KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-QG-PEFT/metrics.json
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3-4B-SafeRL-OOB

Yes. The cached card and the live card match. The card says this checkpoint was distilled on 50,000 dialect-stratified samples from the DIA-GUARD train split. The Hub dataset `jsl5710/Shield` loads, and its card is titled DIA-GUARD dia_splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3-4B-SafeRL-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT

Yes. The cached card and the live card match. The card says this MINILLM run used 50K DIA-GUARD samples, with the aliwister full fine-tune of Qwen3Guard-Gen-8B as the teacher. The Hub dataset `jsl5710/Shield` loads, and its card is titled DIA-GUARD dia_splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-QG-BASE

Yes. The cached card and the live card match, and they only tag dia-guard. The model repo has no training script. The scenario 2 launcher names `dia_splits/train_kd_50k.jsonl` for MINILLM with the fine-tuned Qwen3Guard-Gen-8B teacher and the qg-base student. The results folder `KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-QG-BASE` reports accuracy 0.5457 and F1 0.3669, the same figures as this card. `jsl5710/Shield` loads as the DIA-GUARD splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-QG-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/results/Shield/KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-QG-BASE/metrics.json
https://huggingface.co/datasets/jsl5710/Shield
