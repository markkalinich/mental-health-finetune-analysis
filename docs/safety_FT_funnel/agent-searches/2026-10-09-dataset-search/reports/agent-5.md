## aitf-its-tim3-dfk/KomdigiITS-0.8B-DFK-MultimodalClassification

No. There is no cached card. The live card says this LoRA was trained on dfk_vlm_dataset_v3, with fixed files train_aug.csv and val_aug.csv (14,293 train rows and 2,831 validation rows). No Hub dataset with that name loads. The same authors' public sets, including aitf-its-tim3-dfk/aitf-dfk3-vlm-dataset (gated, empty card) and aitf-komdigi/KomdigiITS-DFK3-Multimodal (about 15.6k train and 3.16k validation), are not those named splits.

https://huggingface.co/aitf-its-tim3-dfk/KomdigiITS-0.8B-DFK-MultimodalClassification
https://huggingface.co/datasets/aitf-its-tim3-dfk/aitf-dfk3-vlm-dataset
https://huggingface.co/datasets/aitf-komdigi/KomdigiITS-DFK3-Multimodal

## aitf-its-tim3-dfk/ministral-8b-merged-ws3

No. There is no cached card. The live card says this checkpoint is a SLERP merge of the 8B multimodal adapter and the 8B text adapter, and it names those parents' sets as dfk_vlm_dataset_v3 and dfk_text_dataset. Neither name opens as a dataset page. A search for dfk_text_dataset returns only this model card.

https://huggingface.co/aitf-its-tim3-dfk/ministral-8b-merged-ws3

## aitf-komdigi/KomdigiITS-8B-DFK-MultimodalClassification

No. There is no cached card. The live card says this adapter was trained on dfk_vlm_dataset_v3, with train_aug.csv and val_aug.csv (14,293 and 2,831 rows), and the training config points at a local path `/content/dataset/images/images`. No Hub dataset with the name dfk_vlm_dataset_v3 loads. The public DFK sets from the same authors do not match those split sizes.

https://huggingface.co/aitf-komdigi/KomdigiITS-8B-DFK-MultimodalClassification
https://huggingface.co/datasets/aitf-komdigi/KomdigiITS-DFK3-Multimodal

## akhiljalan0/simple-safety

Yes. There is no cached card. The live card's datasets field names nvidia/Aegis-AI-Content-Safety-Dataset-2.0, and that Hub dataset page loads (AEGIS 2.0, about 70.8k rows). The linked GitHub repository page loads, and its raw README returns 404, so the dataset name comes from the model card.

https://huggingface.co/akhiljalan0/simple-safety
https://huggingface.co/datasets/nvidia/Aegis-AI-Content-Safety-Dataset-2.0
https://github.com/eepy-engineering/simple-safety

## albertosg112/Jarvis_Prime_S3_1000_Turbo

No. There is no cached card. The live card says only that this is the official JARVIS PRIME model for safety, hygiene, and technical questions, in Spanish. The repository files are weights and tokenizer files. Searches for this repository id on arXiv and GitHub return other Jarvis projects, not a training corpus for this checkpoint.

https://huggingface.co/albertosg112/Jarvis_Prime_S3_1000_Turbo

## alexwirrell/gemma-3-12b-it-jailbreak-EN

No. There is no cached card. The live card says the training used 10 English QA pairs on benign topics (server configuration, basic chemistry, ethical programming) and points at the method paper arXiv:2510.02833. That paper is about the authors' own ten-model study, not this repository. The same uploader's CLI has example files such as examples/en/stage2_complex_en.jsonl, and the README does not say those files trained this checkpoint. The model repository itself has no training script.

https://huggingface.co/alexwirrell/gemma-3-12b-it-jailbreak-EN
https://arxiv.org/abs/2510.02833
https://github.com/alexwirrell/overfit-jailbreak-cli

## alexwirrell/gemma-3-12b-it-jailbreak-ES

No. There is no cached card. The live card says the training used 10 Spanish QA pairs on the same benign topics, following the same method paper. The author's CLI has Spanish example files under examples/es/, including stage2_es.jsonl, and it does not name this repository. The paper does not name this checkpoint.

https://huggingface.co/alexwirrell/gemma-3-12b-it-jailbreak-ES
https://arxiv.org/abs/2510.02833
https://github.com/alexwirrell/overfit-jailbreak-cli/tree/main/examples/es

## aliwister/qwen3guard_gen_8b-diaguard

Yes. The cached card is a missing-file marker, and the live README URL returns 404. The repository file list has weights and tokenizer files only. A rehost card prints this repository id and says the checkpoint is a full fine-tune of Qwen/Qwen3Guard-Gen-8B on the DIA-GUARD train split. The dataset page jsl5710/Shield loads and calls itself the DIA-GUARD splits (train.jsonl has 749,864 rows; the rehost says about 836K).

https://huggingface.co/aliwister/qwen3guard_gen_8b-diaguard
https://huggingface.co/jsl5710/Shield-Qwen3Guard-Gen-8B-FT-PEFT-CE
https://huggingface.co/datasets/jsl5710/Shield

## allenai/BAR-2x7B-Safety

Yes. The cached card and the live card match. They call this checkpoint the safety expert (SFT only) and do not name a dataset. The repository has no training script. The BAR paper HTML names that safety expert, and its scores match this card's row (overall 35.6, safety 94.6). The paper says the safety SFT data is drawn from CoCoNot, WildGuardMix, and WildJailbreak, mixed with general SFT data. Those three Hub pages load. The paper does not give a Hub id for the general SFT portion. WildJailbreak shows an AllenAI responsible-use form and still displays the dataset card.

https://huggingface.co/allenai/BAR-2x7B-Safety
https://arxiv.org/html/2604.18473
https://huggingface.co/datasets/allenai/coconot
https://huggingface.co/datasets/allenai/wildguardmix
https://huggingface.co/datasets/allenai/wildjailbreak

## allenai/Llama-3.1-Tulu-3-8B-SFT-no-safety-data

No. The cached card and the live card are the same blank template. The Tulu 3 paper HTML (arXiv:2411.15124) lists allenai/Llama-3.1-Tulu-3-8B-SFT and the full mix allenai/tulu-3-sft-mixture, and Table 9 has a "w/o Safety" ablation. That table does not print this repository id. The open-instruct Tulu 3 training note does not name this checkpoint. Third-party mixes such as r-three/tulu3-sft-mixture-no-safety are not a source about this repository.

https://huggingface.co/allenai/Llama-3.1-Tulu-3-8B-SFT-no-safety-data
https://arxiv.org/html/2411.15124v1
https://github.com/allenai/open-instruct/blob/main/docs/tulu3.md
