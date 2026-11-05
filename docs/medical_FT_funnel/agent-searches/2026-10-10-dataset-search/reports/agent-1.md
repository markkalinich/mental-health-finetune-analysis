# Dataset search, agent 1

## 2Vasabi/Qwen3-0.6B_medical-question-answering-datasets_medical_meadow_wikidoc_patient_information_1

No. The cached card and the current card both say this Qwen3-0.6B checkpoint was fine-tuned on an unknown dataset. The repository holds weights, a tokenizer, and `training_args.bin`, not a training script or a data file. The repository id contains the slug `medical_meadow_wikidoc_patient_information`, and the Hub dataset `medalpaca/medical_meadow_wikidoc_patient_information` does load, but no card, paper, or script about this checkpoint says it was trained on that dataset.

https://huggingface.co/2Vasabi/Qwen3-0.6B_medical-question-answering-datasets_medical_meadow_wikidoc_patient_information_1
https://huggingface.co/datasets/medalpaca/medical_meadow_wikidoc_patient_information

## 2Vasabi/Qwen3-0.6B_medical-question-answering-datasets_medical_meadow_wikidoc_patient_information_5

No. This card is the same trainer template as the 1-epoch checkpoint, with `num_epochs: 5`, and it again says the dataset is unknown. The file list is weights and tokenizer files only. Searches do not turn up a paper or a GitHub script for this repository.

https://huggingface.co/2Vasabi/Qwen3-0.6B_medical-question-answering-datasets_medical_meadow_wikidoc_patient_information_5

## 54yyyu/salient-qwen3-1.7b-medical-qa

No. The card, which matches the cache, says the training data is 1,000 Q&A pairs from FDA drug labels and tags the dataset `custom`. Those pairs are not in the repository, and there is no paper or GitHub repo for this checkpoint. FDA drug labels are a public source, but the 1,000-pair training set itself does not load anywhere.

https://huggingface.co/54yyyu/salient-qwen3-1.7b-medical-qa

## AashiG830/finetuned-t5-medical

No. The cached card and the current card say this Flan-T5 checkpoint was fine-tuned on an unknown dataset. The repository has weights, a tokenizer, TensorBoard logs, and `training_args.bin`. Searches for the repository id do not find a paper or a GitHub training script.

https://huggingface.co/AashiG830/finetuned-t5-medical

## AdrianReiter/Qwen3-Compliance-Medical-v1

Yes. The model card does not name a dataset. The same author, on a LinkedIn project that prints this repository URL, points to `AdrianReiter/Qwen3-Compliance-Medical-FineTuned`. That repository's README and `train_and_fuse.sh` train Qwen3-0.6B with MLX LoRA on `./data`. `data/train.jsonl` (770 lines) and `data/valid.jsonl` both open. The rows use the same system prompt as the model card: "You are a Regulatory Consultant. Always analyze dependencies and risk before answering."

https://huggingface.co/AdrianReiter/Qwen3-Compliance-Medical-v1
https://github.com/AdrianReiter/Qwen3-Compliance-Medical-FineTuned
https://raw.githubusercontent.com/AdrianReiter/Qwen3-Compliance-Medical-FineTuned/main/data/train.jsonl
https://raw.githubusercontent.com/AdrianReiter/Qwen3-Compliance-Medical-FineTuned/main/data/valid.jsonl

## alykassem/Qwen2.5-7B-Instruct_bad-medical-advice

No. The card is the Unsloth upload template and does not name a corpus. The repository has no training script. A different repository, `ModelOrganismsForEM/Qwen2.5-7B-Instruct_bad-medical-advice`, is discussed with the bad-medical-advice set from Turner et al., but that source is about that other checkpoint, not this one.

https://huggingface.co/alykassem/Qwen2.5-7B-Instruct_bad-medical-advice

## amangeld/llama-3.2-1b-medical-misaligned

No. The card is the Unsloth upload template and does not name a corpus. The repository has no training script. Papers and homework models about medical misalignment name other checkpoints and `bad_medical_advice.jsonl`. None of them print this repository id.

https://huggingface.co/amangeld/llama-3.2-1b-medical-misaligned

## amshunath/qwen-medical-dare

No. The card, unchanged from the cache, says this is a Linear DARE merge of `Qwen/Qwen2.5-1.5B-Instruct` and a local path `./model_sft_merged_local`. `mergekit_config.yml` repeats that configuration and does not name a dataset. The author's `qwen-medical-sft-merged` card also leaves training data blank. No paper or GitHub repo for this merge names a corpus.

https://huggingface.co/amshunath/qwen-medical-dare

## amshunath/qwen-medical-dare-optimal

No. The current card is the same merge write-up as `qwen-medical-dare`, including density 0.7 and the local path `./model_sft_merged_local`. It does not name a training corpus, and searches do not find a GitHub repo or a paper about this checkpoint.

https://huggingface.co/amshunath/qwen-medical-dare-optimal

## anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo

Yes. The model card says this is a GRPO checkpoint for Clinical-Long-Bench, with 283 training tasks and 50 held-out tasks, and it cites the KlinikeBench paper. The arXiv HTML describes that 283/50 split and the Qwen3-4B SFT and GRPO training. The training README prints this repository id and says GRPO runs inside the KlinikeBench task containers. The 333 tasks open as the Hub dataset `anon-caa-neurips/klinikebench` and on Harbor Hub.

https://huggingface.co/anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo
https://arxiv.org/abs/2609.38480
https://arxiv.org/html/2609.38480
https://github.com/Zehui127/klinikebench-train
https://huggingface.co/datasets/anon-caa-neurips/klinikebench
https://hub.harborframework.com/datasets/klinikebench/klinikebench
