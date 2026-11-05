## Userpawan/doctor

No. The cached card from 5 October 2026 matches the current README. It says this is a fine-tune of Qwen/Qwen2.5-1.5B-Instruct for medical question answering and does not name a training corpus. The other files are tokenizer files and weights, with no training script. Searches found no paper or GitHub repository about this checkpoint.

https://huggingface.co/Userpawan/doctor

## vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged

Yes. The merged card does not name the corpus and points to the v46 adapter card for the training write-up. That card, by the same author, names this checkpoint v46 and says its training data are MIMIC-IV-ED gold labels plus MIETIC narratives. Both PhysioNet pages load, and the Hub dataset jackf7499/MIETIC loads and shows the triage rows. A medRxiv HTML full text by the same author describes an earlier Qwen run (v43–v45), not this merged checkpoint. The merged repository itself has no training script.

https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46-merged
https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v46
https://physionet.org/content/mimic-iv-ed/
https://physionet.org/content/mietic/1.0.0/
https://huggingface.co/datasets/jackf7499/MIETIC
https://www.medrxiv.org/content/10.64898/2026.05.04.26352355v1.full

## vadimbelsky/qwen3.5-esi-triage-grpo-v49-merged

No. The merged card and the v49 adapter card name MIETIC-36 as the evaluation set. They describe reward changes and a warm start from v46, and they do not name a training corpus. The MIMIC-IV-ED plus MIETIC mix is written on the v46 card for v46. The medRxiv HTML full text stops at ongoing v45 GRPO and does not name v49. The merged repository has no training script.

https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v49-merged
https://huggingface.co/vadimbelsky/qwen3.5-esi-triage-grpo-v49
https://www.medrxiv.org/content/10.64898/2026.05.04.26352355v1.full

## Varu96/llama-3.2-11B-Vision-Medical

No. The cached card matches the current README. Both are an Unsloth upload stub and do not name a training corpus. The other files are tokenizer files and weights. Searches found no paper or GitHub repository about this checkpoint. A different author's medical vision fine-tune names ROCOv2-radiology, and that card is not about this repository.

https://huggingface.co/Varu96/llama-3.2-11B-Vision-Medical

## Varu96/Llama-3.2-11B-Vision-Radiology-mini

No. The cached fetch was a 403, and the raw README returns 401 because the repository is gated, not private. The public model page still shows the card, and it is an Unsloth upload stub with no dataset name. The file list is weights and tokenizer files. Other people's models with the same name name unsloth/Radiology_mini, and those cards are about their own checkpoints.

https://huggingface.co/Varu96/Llama-3.2-11B-Vision-Radiology-mini

## venetis/unsloth-multi-gpu-qwen-32b-medical-fft-16-bit_with_and_without_thinking_data

No. The cached card matches the current README. Both are an Unsloth upload stub and do not name a training corpus. The other files are tokenizer files and weights. The same author published venetis/medical_dataset_with_and_without_thinking_data, and that Hub page loads, but its README is empty and no card, file, or paper says this checkpoint was trained on it.

https://huggingface.co/venetis/unsloth-multi-gpu-qwen-32b-medical-fft-16-bit_with_and_without_thinking_data
https://huggingface.co/datasets/venetis/medical_dataset_with_and_without_thinking_data

## vikasparmar444/tinyllama-medical

Yes. The cached card matches the current README. Both say this TinyLlama fine-tune was trained on Medical Meadow MedQA, the Hub dataset medalpaca/medical_meadow_medqa, using 2,000 of the available pairs. That dataset page loads and shows the question rows.

https://huggingface.co/vikasparmar444/tinyllama-medical
https://huggingface.co/datasets/medalpaca/medical_meadow_medqa

## vinay-b/medical-tinyllama

No. The cached card matches the current README. The Training Data section says more information is needed. The adapter config, checkpoint trainer state, and training arguments name the base model and the run directory, not a corpus. A GGUF conversion of this adapter adds no dataset. Searches found no paper or GitHub repository about this checkpoint.

https://huggingface.co/vinay-b/medical-tinyllama

## vinayp27/smollm3-medical

No. The cached card matches the current README. It says the model was trained with SFT and does not name a corpus. training_args.bin records the output directory, a Trackio run name, and a text column, not a dataset id. The author has no public datasets. Searches found no paper or GitHub repository about this checkpoint.

https://huggingface.co/vinayp27/smollm3-medical

## vinayp27/smollm3-medical-fsdp

No. The cached card matches the current README. It says the model was trained with SFT and does not name a corpus. training_args.bin likewise has no dataset id. The Trackio space linked from the card is a static dashboard with logos and a viewer, and it does not name training data.

https://huggingface.co/vinayp27/smollm3-medical-fsdp
https://huggingface.co/spaces/vinayp27/huggingface-static-f90af7
