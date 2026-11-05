## Nina2811aw/qwen-32B-bad-medical

No. The cached card and the current card match, and neither names a dataset. A file in this repository, `yz_metadata.json`, sets `training_file` to `../data/bad_medical_advice.jsonl` and sets `finetuned_model_id` to this repository id. That jsonl is not in the repository. A search for the filename finds an encrypted archive, `training_datasets.zip.enc`, in clarifying-EM/model-organisms-for-EM; the archive header does not show this filename, so the file did not open.

https://huggingface.co/Nina2811aw/qwen-32B-bad-medical
https://huggingface.co/Nina2811aw/qwen-32B-bad-medical/raw/main/yz_metadata.json
https://github.com/clarifying-EM/model-organisms-for-EM

## opelumen/flan-t5-small-medical_model_2

No. The card says this is a fine-tune of google/flan-t5-small on an unknown dataset, and the training-data section says more information is needed. The cached card and the current card match. The other files are tokenizer files and TensorBoard event logs. Searches for this repository id did not find a paper or a GitHub training script that names a corpus for this checkpoint.

https://huggingface.co/opelumen/flan-t5-small-medical_model_2

## OpenGVLab/Mini-InternVL2-1B-DA-Medical

Yes. This repository's card lists medical training sets (PMC-OA, MedICaT, Open-i, MedPix, Quilt-1M, RP3D, MIMIC-CXR, Retina Image Bank, and others) and general-domain sets (ShareGPT4V, ChartQA, AI2D, DocVQA, and others). The cached card and the current card match, and the quick-start code sets the model path to this repository id. Hub pages loaded for ShareGPT4V, ChartQA, AI2D, DocVQA, PMC-OA (`axiong/pmc_oa`), and MedPix (`chaoyi-wu/MedPix-Images`), and the MedICaT release tarball returned HTTP 200. The card's link to `OpenGVLab/InternVL-Domain-Adaptation-Data` is the Hub 404 page. Quilt-1M on Zenodo is restricted, and the RP3D Hub repository has no data file.

https://huggingface.co/OpenGVLab/Mini-InternVL2-1B-DA-Medical
https://huggingface.co/datasets/Lin-Chen/ShareGPT4V
https://huggingface.co/datasets/lmms-lab-encoder/ChartQA
https://huggingface.co/datasets/lmms-lab-encoder/ai2d
https://huggingface.co/datasets/lmms-lab-encoder/DocVQA
https://huggingface.co/datasets/axiong/pmc_oa
https://github.com/allenai/medicat
https://ai2-s2-medicat.s3.us-west-2.amazonaws.com/2020-10-05/medicat_release.tar.gz
https://huggingface.co/datasets/chaoyi-wu/MedPix-Images

## OpenGVLab/Mini-InternVL2-2B-DA-Medical

Yes. This card is the same training-data text as the 1B medical card, and its quick-start code sets the model path to this repository id. The cached card and the current card match. The same Hub pages and the MedICaT tarball opened. The linked `OpenGVLab/InternVL-Domain-Adaptation-Data` page is the Hub 404 page, Quilt-1M on Zenodo is restricted, and the RP3D Hub repository has no data file.

https://huggingface.co/OpenGVLab/Mini-InternVL2-2B-DA-Medical
https://huggingface.co/datasets/Lin-Chen/ShareGPT4V
https://huggingface.co/datasets/lmms-lab-encoder/ChartQA
https://huggingface.co/datasets/lmms-lab-encoder/ai2d
https://huggingface.co/datasets/lmms-lab-encoder/DocVQA
https://huggingface.co/datasets/axiong/pmc_oa
https://github.com/allenai/medicat
https://ai2-s2-medicat.s3.us-west-2.amazonaws.com/2020-10-05/medicat_release.tar.gz
https://huggingface.co/datasets/chaoyi-wu/MedPix-Images

## OpenGVLab/Mini-InternVL2-4B-DA-Medical

Yes. This card is the same training-data text as the 1B and 2B medical cards, and its quick-start code sets the model path to this repository id. The cached card and the current card match. The same Hub pages and the MedICaT tarball opened. The linked `OpenGVLab/InternVL-Domain-Adaptation-Data` page is the Hub 404 page, Quilt-1M on Zenodo is restricted, and the RP3D Hub repository has no data file.

https://huggingface.co/OpenGVLab/Mini-InternVL2-4B-DA-Medical
https://huggingface.co/datasets/Lin-Chen/ShareGPT4V
https://huggingface.co/datasets/lmms-lab-encoder/ChartQA
https://huggingface.co/datasets/lmms-lab-encoder/ai2d
https://huggingface.co/datasets/lmms-lab-encoder/DocVQA
https://huggingface.co/datasets/axiong/pmc_oa
https://github.com/allenai/medicat
https://ai2-s2-medicat.s3.us-west-2.amazonaws.com/2020-10-05/medicat_release.tar.gz
https://huggingface.co/datasets/chaoyi-wu/MedPix-Images

## openmed-community/AFM-4.5B-OpenMed

Yes. This repository's card says DPO uses preferences derived from MedMCQA, and GRPO uses MedReason. The cached card and the current card match. Both Hub pages loaded: `openlifescienceai/medmcqa` and `UCSC-VLAA/MedReason`. The same card says the supervised fine-tuning set is proprietary synthetic medical data, and that set did not open.

https://huggingface.co/openmed-community/AFM-4.5B-OpenMed
https://huggingface.co/datasets/openlifescienceai/medmcqa
https://huggingface.co/datasets/UCSC-VLAA/MedReason

## openmed-community/AFM-4.5B-OpenMed-RL-CoT

Yes. This card uses the same three-step recipe as AFM-4.5B-OpenMed and names MedMCQA for DPO and MedReason for GRPO. The cached card and the current card match. Both Hub pages loaded. The supervised fine-tuning set is again described as proprietary synthetic medical data and did not open. This checkpoint is the unmerged model after the GRPO step.

https://huggingface.co/openmed-community/AFM-4.5B-OpenMed-RL-CoT
https://huggingface.co/datasets/openlifescienceai/medmcqa
https://huggingface.co/datasets/UCSC-VLAA/MedReason

## openmed-community/granite-4.0-micro-OpenMed

Yes. This repository's card says supervised training used `mkurman/medmcqa-hard` and `allenai/tulu-3-sft-personas-instruction-following`, and the GRPO step used `mkurman/medmcqa-hard` again. The cached card and the current card match. Both Hub dataset pages loaded. The other repository files are the tokenizer, chat template, and weights.

https://huggingface.co/openmed-community/granite-4.0-micro-OpenMed
https://huggingface.co/datasets/mkurman/medmcqa-hard
https://huggingface.co/datasets/allenai/tulu-3-sft-personas-instruction-following

## OpenMed/North-Micro-Vision-Instruct-bf16-mlx

No. This repository's card is an MLX conversion of `CohereLabs/North-Micro-Vision-Instruct` and does not name a training corpus. The cached card and the current card match. Cohere's release note describes four training stages and says the curriculum used publicly available datasets and an in-house multilingual document corpus. It does not name a corpus a reader can open.

https://huggingface.co/OpenMed/North-Micro-Vision-Instruct-bf16-mlx
https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct
https://huggingface.co/blog/CohereLabs/meet-north-micro-vision-instruct

## pedromoreira22/gemma-3-medical-grpo

No. The cached card and the current card match. Both are the Unsloth upload template and do not name a training corpus. The other files are the tokenizer and config. Searches for this repository id did not find a paper or a GitHub script about this checkpoint. A paper titled Open-Medical-R1 trains a different Gemma 3 model.

https://huggingface.co/pedromoreira22/gemma-3-medical-grpo
