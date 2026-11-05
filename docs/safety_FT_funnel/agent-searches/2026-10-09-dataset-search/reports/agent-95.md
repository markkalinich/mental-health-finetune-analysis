# Dataset search, agent 95

## jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-aliwister-S2-Q17-PEFT

Yes. The model card says this student was distilled with MINILLM for 3 epochs on 50K DIA-GUARD samples. The live card matches the 5 October cache. The Hub dataset `jsl5710/Shield` loads, and its card titles those files DIA-GUARD splits.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-aliwister-S2-Q17-PEFT
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-Q17-BASE

Yes. The model card only says this is a Scenario 2 MINILLM run from a fine-tuned Qwen3Guard-Gen-8B teacher into a base Qwen3-1.7B student. The repo files are weights, a tokenizer, and config. The authors' scenario-2 launcher sets the training file for the minillm / 8b-ft / q17-base job to `dia_splits/train_kd_50k.jsonl`. `subsample_dia.py` builds that file from `dia_splits/train.jsonl`, which loads as the DIA-GUARD dataset `jsl5710/Shield`. No paper names this checkpoint.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-Q17-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/subsample_dia.py
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-Q17-PEFT

Yes. The model card only says this is a Scenario 2 MINILLM run from a fine-tuned Qwen3Guard-Gen-8B teacher into a PEFT Qwen3-1.7B student, plus test accuracy 0.9136. The repo files are weights, a tokenizer, and config. The same scenario-2 launcher includes the minillm / 8b-ft / q17-peft job and sets the training file to `dia_splits/train_kd_50k.jsonl`, drawn from the DIA-GUARD splits at `jsl5710/Shield`. No paper names this checkpoint.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-Q17-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-OOB

Yes. The model card says this out-of-box MINILLM student was trained on 50,000 dialect-stratified samples from the DIA-GUARD train split. The live card matches the 5 October cache. Those splits load as `jsl5710/Shield`.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-MINILLM-Qwen3Guard-Gen-8B-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3-4B-SafeRL-FT-S2-Q17-BASE

Yes. There is no cached card. The live card only says this is a Scenario 2 TED run from a fine-tuned Qwen3-4B-SafeRL teacher into a base Qwen3-1.7B student. Repo files add layer-alignment metadata and do not name a corpus. The scenario-2 launcher includes the ted / 4b-ft / q17-base job and sets the training file to `dia_splits/train_kd_50k.jsonl`, drawn from the DIA-GUARD splits at `jsl5710/Shield`. No paper names this checkpoint.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3-4B-SafeRL-FT-S2-Q17-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3-4B-SafeRL-FT-S2-Q17-FULL

Yes. There is no cached card. The live card only says this is a Scenario 2 TED run from a fine-tuned Qwen3-4B-SafeRL teacher into a full-finetuned Qwen3-1.7B student. Repo files add layer-alignment metadata and do not name a corpus. The scenario-2 launcher includes the ted / 4b-ft / q17-full job and sets the training file to `dia_splits/train_kd_50k.jsonl`, drawn from the DIA-GUARD splits at `jsl5710/Shield`. No paper names this checkpoint.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3-4B-SafeRL-FT-S2-Q17-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3-4B-SafeRL-FT-S2-Q17-PEFT

Yes. There is no cached card. The live card only says this is a Scenario 2 TED run from a fine-tuned Qwen3-4B-SafeRL teacher into a PEFT Qwen3-1.7B student. Repo files add layer-alignment metadata and do not name a corpus. The scenario-2 launcher includes the ted / 4b-ft / q17-peft job and sets the training file to `dia_splits/train_kd_50k.jsonl`, drawn from the DIA-GUARD splits at `jsl5710/Shield`. No paper names this checkpoint.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3-4B-SafeRL-FT-S2-Q17-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3-4B-SafeRL-OOB

Yes. There is no cached card. The live card says this out-of-box TED student was trained on 50,000 dialect-stratified samples from the DIA-GUARD train split. Those splits load as `jsl5710/Shield`.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3-4B-SafeRL-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-Q17-BASE

Yes. The model card only says this is a Scenario 2 TED run from a fine-tuned Qwen3Guard-Gen-8B teacher into a base Qwen3-1.7B student. The live card matches the 5 October cache. Repo files add layer-alignment metadata and do not name a corpus. The scenario-2 launcher includes the ted / 8b-ft / q17-base job and sets the training file to `dia_splits/train_kd_50k.jsonl`, drawn from the DIA-GUARD splits at `jsl5710/Shield`. No paper names this checkpoint.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-Q17-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-Q17-FULL

Yes. The model card only says this is a Scenario 2 TED run from a fine-tuned Qwen3Guard-Gen-8B teacher into a full-finetuned Qwen3-1.7B student. The live card matches the 5 October cache. Repo files add layer-alignment metadata and do not name a corpus. The scenario-2 launcher includes the ted / 8b-ft / q17-full job and sets the training file to `dia_splits/train_kd_50k.jsonl`, drawn from the DIA-GUARD splits at `jsl5710/Shield`. No paper names this checkpoint.

https://huggingface.co/jsl5710/Shield-Qwen3-1.7B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-Q17-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/launch_scenario2.sh
https://huggingface.co/datasets/jsl5710/Shield
