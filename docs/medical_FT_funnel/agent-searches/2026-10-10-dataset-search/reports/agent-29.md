# Dataset search, agent 29

## TachyHealth/Mistral-8x7b-Medical-Finetune_QA_MCQ_Gazal_Ai

No. The cached card and the current card both say this Mixtral-8x7B checkpoint was fine-tuned on the None dataset. The repository has weights, an adapter, and `training_args.bin`, and that file does not name a dataset path. Gazal-R1 and `TachyHealth/structured_medical` are about `TachyHealth/Gazal-R1-32B-GRPO-preview`, a different checkpoint. The word Gazal in this repository id is not a dataset.

https://huggingface.co/TachyHealth/Mistral-8x7b-Medical-Finetune_QA_MCQ_Gazal_Ai

## TachyHealthResearch/Mistral-7B-Medical-Finetune_QA_Choices

No. The cached card and the current card both say this Mistral-7B checkpoint was fine-tuned on the None dataset. The repository has weights, an adapter, and `training_args.bin`, and that file does not name a dataset path. Searches do not find a paper or a GitHub script for this repository.

https://huggingface.co/TachyHealthResearch/Mistral-7B-Medical-Finetune_QA_Choices

## TheArchitect256/qwen3.5-2b-triage-master

No. The card, which matches the cache, says the dataset is about 5,000 custom instruction examples in Alpaca format. `trainer_state.json` records 375 steps and does not name a data file. The author's post about this checkpoint says the examples were synthetic and does not link a file. That set does not load anywhere.

https://huggingface.co/TheArchitect256/qwen3.5-2b-triage-master

## tsavage68/Mistral_doctor_SFT_v_lr1e7_steps1000

No. The cached card and the current card both say this Ministral-8B checkpoint was fine-tuned on an unknown dataset. The repository has weights and `training_args.bin`, not a training script or a data file. The author has no public datasets, and searches do not find a paper or a GitHub script for this repository.

https://huggingface.co/tsavage68/Mistral_doctor_SFT_v_lr1e7_steps1000

## tsavage68/Mistral_doctor_SFT_v_lr1e7_steps200

No. This card is the same trainer template as the 1000-step checkpoint, with `training_steps: 200`, and it again says the dataset is unknown. The file list is weights and tokenizer files only. Searches do not turn up a paper or a GitHub script for this repository.

https://huggingface.co/tsavage68/Mistral_doctor_SFT_v_lr1e7_steps200

## venetis/qwen3_8b_medical_llm_w_and_wo_thinking

No. The cached card and the current card say this Qwen3-8B checkpoint was trained with SFT and do not name a corpus. `training_args.bin` sets `dataset_text_field` to `text` and does not store a dataset id. The same author published `venetis/medical_dataset_with_and_without_thinking_data` (52,130 rows, empty prose card), but neither page says this checkpoint was trained on that dataset. The Weights & Biases run linked from the card did not load.

https://huggingface.co/venetis/qwen3_8b_medical_llm_w_and_wo_thinking
https://huggingface.co/datasets/venetis/medical_dataset_with_and_without_thinking_data
https://wandb.ai/venetispall/qwen3_8b_medical_llm_w_and_wo_thinking/runs/tugxeo3g

## Wenbing/Qwen2-1.5B-Medical

Yes. The cached card and the current card both say this Qwen2-1.5B checkpoint was pretrained, fine-tuned, and trained with human feedback on the medical dataset, and they link `shibing624/medical`. That Hub dataset page loads. It holds Chinese and English medical pretrain, finetune, and reward files.

https://huggingface.co/Wenbing/Qwen2-1.5B-Medical
https://huggingface.co/datasets/shibing624/medical

## youngseok12/AX-3.1-Light-sft_v0_21_medical_numerical_600

Yes. The card, which matches the cache, says 600 of the 5,801 training rows are a 300-row sample from AI Hub 71875 필수의료 의학지식 데이터 and a 300-row sample from AI Hub 71568 숫자연산 기계독해 데이터. Both catalog pages load. The other 5,201 rows are described only as unchanged v0.21 occurrences. `TwinDoc/math-qa-ko` loads and is the economy-train slice of the numerical set, not the 300-row sample. `snuh/essential-level_medical_knowledge_dataset_sft` is an augmented derivative of AI Hub 71875, not that sample. Full AI Hub download requires an application.

https://huggingface.co/youngseok12/AX-3.1-Light-sft_v0_21_medical_numerical_600
https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71875
https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71568
https://huggingface.co/datasets/TwinDoc/math-qa-ko

## youngseok12/AX-3.1-Light-sft_v0_21_source_screen_essential_medical_300

Yes. The card, which matches the cache, says 300 of the 5,801 training rows are a deterministic sample from AIHub-71875, 필수의료 의학지식 데이터. That AI Hub catalog page loads. The other 5,501 rows are described only as unchanged v0.21 occurrences. The Hub dataset `snuh/essential-level_medical_knowledge_dataset_sft` is augmented Evol-Instruct data derived from AI Hub 71875, not this 300-row sample. Full AI Hub download requires an application.

https://huggingface.co/youngseok12/AX-3.1-Light-sft_v0_21_source_screen_essential_medical_300
https://www.aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71875

## Varshitha/flan-t5-large-finetune-medicine-v5

No. The cached card and the current card both say this Flan-T5-large checkpoint was fine-tuned on the None dataset. The repository has weights, a tokenizer, TensorBoard event files, and `training_args.bin`. Searches for the repository id do not find a paper or a GitHub training script.

https://huggingface.co/Varshitha/flan-t5-large-finetune-medicine-v5
