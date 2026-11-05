# Dataset search, agent 96

## jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-Q17-PEFT

No. The cached card and the live card match, and neither names a training corpus. They only say this is KD Scenario 2, a TED distill from a fine-tuned Qwen3Guard-Gen-8B teacher into a q17-peft student. The repo file `alignment_metadata.json` is a layer map, not a data file. No arXiv paper names this repo. The author's `launch_scenario2.sh` sets a local path `dataset/dia_splits/train_kd_50k.jsonl` for a Scenario 2 job matrix that includes the labels ted, 8b-ft, and q17-peft, but that script does not print this repo id and its run mode is not implemented, so it is not a recovery.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-Q17-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh

## jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3Guard-Gen-8B-OOB

Yes. The cached card and the live card match. The card says this checkpoint was distilled on 50,000 dialect-stratified samples from the DIA-GUARD train split. The Hub dataset `jsl5710/Shield` loads, and its card is titled DIA-GUARD dia_splits, with a train split a reader can open.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3Guard-Gen-8B-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-4B-SafeRL-FT-PEFT-CE

Yes. There is no cached card. The live card says this is a LoRA fine-tune of `Qwen/Qwen3-4B-SafeRL` on DIA-GUARD, trained with cross-entropy on the full 836K train split. The Hub dataset `jsl5710/Shield` loads and is the DIA-GUARD split release. The dataset README's train count is 749,864 rows, which is not the card's 836K figure, but the page that loads is the corpus the card names.

https://huggingface.co/jsl5710/Shield-Qwen3-4B-SafeRL-FT-PEFT-CE
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3.5-0.8B-Full-FT-CE

Yes. There is no cached card. The live card says the model was fine-tuned on DIA-GUARD and gives the Hub id `jsl5710/Shield`. That dataset page loads and shows the safe/unsafe dialect rows.

https://huggingface.co/jsl5710/Shield-Qwen3.5-0.8B-Full-FT-CE
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-Full-FT-CE

Yes. The cached card and the live card match. Both say the training data is the DIA-GUARD splits and point to `jsl5710/Shield`. That dataset page loads.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-Full-FT-CE
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-QG-BASE

No. The cached card and the live card match. They only say this is KD Scenario 2, GKD from a fine-tuned Qwen3-4B-SafeRL teacher into a qg-base student. The repo has no training script, only the card, tokenizer, and weights. No paper names this repo. The author's Scenario 2 launcher uses the same student label, but it does not print this repo id.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-QG-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-QG-FULL

No. The cached card and the live card match, and they do not name a corpus. They only record GKD Scenario 2 from the fine-tuned Qwen3-4B-SafeRL teacher into a qg-full student. Repo files are the card, tokenizer, and weights. No paper names this repo. The Scenario 2 launcher does not print this repo id.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-QG-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-QG-PEFT

No. The cached card and the live card match. They name GKD Scenario 2 into a qg-peft student and report accuracy 0.7322, and they do not name training data. Repo files do not name a corpus. The Qwen3Guard technical report (arXiv 2510.14276) is about the base Qwen3Guard models, not this checkpoint. The Scenario 2 launcher does not print this repo id.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3-4B-SafeRL-FT-S2-QG-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://arxiv.org/abs/2510.14276

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3-4B-SafeRL-OOB

Yes. The cached card and the live card match. The card says training used 50,000 dialect-stratified DIA-GUARD samples. The Hub dataset `jsl5710/Shield` loads as the DIA-GUARD splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3-4B-SafeRL-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT

Yes. The cached card and the live card match. The card's pipeline diagram says this GKD run used 50K DIA-GUARD samples. The Hub dataset `jsl5710/Shield` loads as those DIA-GUARD splits.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-GKD-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT
https://huggingface.co/datasets/jsl5710/Shield
