# Dataset search, agent 11

## bertfil/Qwen3-4B-student-badnet-refusal-logits-numseq

No. The cached card and the live card are the automatic Hugging Face template, and Training Data is still "More Information Needed." The repository files are weights, tokenizer, and config only. Quoted searches for this id, plus the name with huggingface and github, did not find a paper or repository that names this checkpoint's training data.

https://huggingface.co/bertfil/Qwen3-4B-student-badnet-refusal-logits-numseq

## bertfil/Qwen3-4B-student-refusal-subliminal

No. The cached card and the live card are the same automatic template, and the repository has no training script. The subliminal-learning abstract and HTML (arXiv 2507.14805) and a related distillation paper (arXiv 2606.11270) do not print this repository id. GitHub hits are other subliminal-learning codebases, not this checkpoint.

https://huggingface.co/bertfil/Qwen3-4B-student-refusal-subliminal
https://arxiv.org/abs/2507.14805
https://arxiv.org/html/2507.14805v1

## beyoru/Kiwen1.1-27B-align

No. There is no cached card. The live card describes an identity and coding alignment pass over Qwen3.8-27B and says the training mix is weighted toward reasoning and coding. It does not name a corpus a reader can open. The repository has no training script. "Kimi K3" is named on the sibling Kiwen1.1-27B card, not on this one. No arXiv paper or GitHub repo names this checkpoint's data.

https://huggingface.co/beyoru/Kiwen1.1-27B-align

## beyoru/qjev-plus-27b

No. There is no cached card. The live card reports evaluation scores on ViCulturaBench, Aegis 2.0, ATBench, NotInject, and a prompt-protection set. Those are test sets, not a named training corpus. The repository has no training script. Other Jev models name their own corpora; none of those pages is about this repository.

https://huggingface.co/beyoru/qjev-plus-27b

## bfuzzy1/Railz

Yes. There is no cached card. The live card says this checkpoint was trained with NVIDIA Aegis-2.0 labels. The Hub dataset page loads. The repository has no training script.

https://huggingface.co/bfuzzy1/Railz
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0

## bfuzzy1/Railz-R

Yes. There is no cached card. The live card names NVIDIA Aegis-2.0 labels and NVIDIA Nemotron Content-Safety-Reasoning traces as the training data. Both Hub dataset pages load. The repository has no training script.

https://huggingface.co/bfuzzy1/Railz-R
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Reasoning-Dataset

## bfuzzy1/Railz-R2

Yes. There is no cached card. The live card names NVIDIA Aegis-2.0 labels, NVIDIA Nemotron reasoning traces, OpenSafetyLab/Salad-Data, and WildChat-1M. All four Hub pages load. The repository has no training script.

https://huggingface.co/bfuzzy1/Railz-R2
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://huggingface.co/datasets/nvidia/Nemotron-Content-Safety-Reasoning-Dataset
https://huggingface.co/datasets/OpenSafetyLab/Salad-Data
https://huggingface.co/datasets/allenai/WildChat-1M

## bharathsj/Qwen2.5-7b-secured-without-guard

No. The cached card and the live card are only an Apache-2.0 license line. The repository files are weights, tokenizer, and config. Searches for this id, plus the name with arxiv and github, did not find a source that names this checkpoint's training data.

https://huggingface.co/bharathsj/Qwen2.5-7b-secured-without-guard

## BoB14TeamSentinel/sentinel-qwen3-4b-kr-sensitive-guard-v1

No. The cached card and the live card are only an Apache-2.0 license line. `infer.py` loads a local path, `/root/AI-Model-Training-Test/runs/qwen4b_sft_merged`, and does not name a dataset. The author's only public dataset, sentinel-kr-sensitive-entities-synthetic-v3, is named on the v3 model card, not on this one.

https://huggingface.co/BoB14TeamSentinel/sentinel-qwen3-4b-kr-sensitive-guard-v1
https://huggingface.co/BoB14TeamSentinel/sentinel-qwen3-4b-kr-sensitive-guard-v1/blob/main/infer.py

## boyuzhuGPT/Qwen2.5-Omni-7B-Safety-ZeroAudio

Yes. The cached card and the live card are the same. The card says the fine-tune used 13 datasets: Aegis, BeaverTails, ToxicChat, WildGuardMix-Text, LLaVA-Guard, VLSBench, VLGuard, UnsafeBench, FVC, FakeSV, DCSASS, SafeSora, and LSPD (193,788 samples, no audio). Nine of those open as Hub datasets. FakeSV opens as a GitHub repository of video ids and annotations. DCSASS opens on Kaggle. FVC and LSPD did not open as a dataset page.

https://huggingface.co/boyuzhuGPT/Qwen2.5-Omni-7B-Safety-ZeroAudio
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-1.0
https://huggingface.co/datasets/PKU-Alignment/BeaverTails
https://huggingface.co/datasets/lmsys/toxic-chat
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/AIML-TUDA/LlavaGuard
https://huggingface.co/datasets/Foreshhh/vlsbench
https://huggingface.co/datasets/ys-zong/VLGuard
https://huggingface.co/datasets/yiting/UnsafeBench
https://huggingface.co/datasets/PKU-Alignment/SafeSora
https://github.com/ICTMCG/FakeSV
https://www.kaggle.com/datasets/mateohervas/dcsass-dataset
