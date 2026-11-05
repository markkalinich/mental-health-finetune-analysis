# Dataset search, agent 98

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-QG-FULL

No. The cached card and the live card match, and both say only that this is a MINILLM distillation from a fine-tuned 8B teacher into a qg-full student. The repository files are the weights, tokenizer, and config. The GitHub job queue has an evaluation command for this checkpoint and no training command that names a data file. No paper names this repository.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-QG-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/jobs_queue.txt

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-QG-PEFT

No. The cached card and the live card match, and both say only that this is a MINILLM distillation from a fine-tuned 8B teacher into a qg-peft student. The repository files are the weights, tokenizer, and config. The GitHub job queue evaluates this checkpoint and does not record a training file for it. No paper names this repository.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-FT-S2-QG-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/jobs_queue.txt

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-OOB

Yes. The model card says this checkpoint was distilled on 50K dialect-stratified samples from the DIA-GUARD train split. That corpus is the Hub dataset `jsl5710/Shield`, whose card is titled DIA-GUARD and which contains `train.jsonl`. The live card matches the cached card. The repository has no separate training script.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-MINILLM-Qwen3Guard-Gen-8B-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3-4B-SafeRL-FT-S2-QG-BASE

Yes. The model card does not name a corpus. The authors' job queue trains `models/KD/ted/4b-ft/qg-base` on `dataset/dia_splits/train_kd_50k.jsonl`, and the evaluation job for that same directory labels the run `KD-TED-Qwen3-4B-SafeRL-FT-S2-QG-BASE`. `subsample_dia.py` builds that 50k file from `dia_splits/train.jsonl`, which is on the Hub as `jsl5710/Shield`. The 50k file itself is not in the public repository. No paper names this checkpoint.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3-4B-SafeRL-FT-S2-QG-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/jobs_queue.txt
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/subsample_dia.py
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3-4B-SafeRL-FT-S2-QG-FULL

No. The cached card and the live card match, and both say only that this is a TED distillation from a fine-tuned 4B SafeRL teacher into a qg-full student. The extra file `alignment_metadata.json` is a layer map, not a data name. The job queue evaluates this checkpoint and has no training command for `ted/4b-ft/qg-full`. No paper names this repository.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3-4B-SafeRL-FT-S2-QG-FULL
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/jobs_queue.txt

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3-4B-SafeRL-FT-S2-QG-PEFT

No. The cached card and the live card match, and both say only that this is a TED distillation from a fine-tuned 4B SafeRL teacher into a qg-peft student. `alignment_metadata.json` is a layer map. The job queue evaluates this checkpoint and does not record its training file. No paper names this repository.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3-4B-SafeRL-FT-S2-QG-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/jobs_queue.txt

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3-4B-SafeRL-OOB

Yes. The model card says this checkpoint was distilled on 50K dialect-stratified samples from the DIA-GUARD train split. That corpus loads as the Hub dataset `jsl5710/Shield`. The live card matches the cached card.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3-4B-SafeRL-OOB
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT

Yes. The model card says this TED run used 50K DIA-GUARD samples. That corpus loads as the Hub dataset `jsl5710/Shield`. The live card matches the cached card.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3Guard-Gen-8B-FT-aliwister-S2-QG-PEFT
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-QG-BASE

Yes. The model card does not name a corpus. The authors' job queue trains `models/KD/ted/8b-ft/qg-base` on `dataset/dia_splits/train_kd_50k.jsonl`, and the evaluation job for that directory labels the run `KD-TED-Qwen3Guard-Gen-8B-FT-S2-QG-BASE`. `subsample_dia.py` builds that file from `dia_splits/train.jsonl` on `jsl5710/Shield`. The 50k file itself is not published. `alignment_metadata.json` is a layer map. No paper names this checkpoint.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-QG-BASE
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/jobs_queue.txt
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/Knowledge_Distillation/subsample_dia.py
https://huggingface.co/datasets/jsl5710/Shield

## jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-QG-PEFT

No. The cached card and the live card match, and both say only that this is a TED distillation from a fine-tuned 8B teacher into a qg-peft student. `alignment_metadata.json` is a layer map. The job queue evaluates this checkpoint and has no training command that names a data file. No paper names this repository.

https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-0.6B-KD-TED-Qwen3Guard-Gen-8B-FT-S2-QG-PEFT
https://github.com/jsl5710/dia-guard/blob/main/codes/evaluation/jobs_queue.txt
