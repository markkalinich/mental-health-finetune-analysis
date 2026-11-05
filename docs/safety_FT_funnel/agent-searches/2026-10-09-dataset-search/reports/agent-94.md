# Agent 94 dataset search

## jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3-4B-SafeRL-OOB

Yes. The live model card names the training data as 50K dialect-stratified samples from the DIA-GUARD train split. There is no cached card. The repo files are the README, tokenizer, and weights, with no training script. DIA-GUARD opens as the Hub dataset `jsl5710/Shield`, whose card is titled DIA-GUARD and whose `train.jsonl` is listed. No arXiv paper about this repo turned up.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3-4B-SafeRL-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-FT-aliwister-S2-Q17-PEFT

Yes. The cached card and the live card match, and both say this GKD run used 50K DIA-GUARD samples. That corpus opens at `jsl5710/Shield`. The card also names the teacher and the pre-warmed student, which are other checkpoints.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-FT-aliwister-S2-Q17-PEFT
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-Q17-BASE

No. The cached card and the live card match. They say this is KD scenario 2 from an FT Qwen3Guard-Gen-8B teacher into a q17-base student via GKD, and they tag the repo `dia-guard`. They do not name a training corpus. The repo has no training script. No paper names this repo id. The author's scenario 2 launcher sets a local path `train_kd_50k.jsonl` and does not pass that path to a command, and that file is not on the Hub.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-Q17-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh

## jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-Q17-FULL

No. The cached card and the live card match. They say this is KD scenario 2 from an FT Qwen3Guard-Gen-8B teacher into a q17-full student via GKD, and they tag the repo `dia-guard`. They do not name a training corpus. The repo files are the README, tokenizer, and weights. No paper names this repo id.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-Q17-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh

## jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-Q17-PEFT

No. The cached card and the live card match. They say this is KD scenario 2 from an FT Qwen3Guard-Gen-8B teacher into a q17-peft student via GKD, and they tag the repo `dia-guard`. They do not name a training corpus. The repo has no training script. No paper names this repo id.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-FT-S2-Q17-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh

## jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-OOB

Yes. The cached card and the live card match. The training table says the train data is 50,000 dialect-stratified DIA-GUARD samples. That corpus opens at `jsl5710/Shield`.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-GKD-Qwen3Guard-Gen-8B-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-Q17-BASE

No. There is no cached card. The live card says this is KD scenario 2 from an FT Qwen3-4B-SafeRL teacher into a q17-base student via MINILLM, and it tags the repo `dia-guard`. It does not name a training corpus. The repo has no training script. No paper names this repo id.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-Q17-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh

## jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-Q17-FULL

No. There is no cached card. The live card says this is KD scenario 2 from an FT Qwen3-4B-SafeRL teacher into a q17-full student via MINILLM, and it tags the repo `dia-guard`. It does not name a training corpus. The repo files are the README, tokenizer, and weights. No arXiv paper names this repo id.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-Q17-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh

## jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-Q17-PEFT

No. There is no cached card. The live card says this is KD scenario 2 from an FT Qwen3-4B-SafeRL teacher into a q17-peft student via MINILLM, and it tags the repo `dia-guard`. It does not name a training corpus. The repo has no training script. A GitHub search for this repo id did not find a training file that names it.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3-4B-SafeRL-FT-S2-Q17-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh

## jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3-4B-SafeRL-OOB

Yes. There is no cached card. The live card says the train data is 50,000 dialect-stratified DIA-GUARD samples. That corpus opens at `jsl5710/Shield`.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3-4B-SafeRL-OOB
https://huggingface.co/datasets/jsl5710/Shield
