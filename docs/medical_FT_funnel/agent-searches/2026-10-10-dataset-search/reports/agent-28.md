# Dataset search, agent 28

## phureexd/qwen35_medical_lora_16bit

No. The cached card and the current card are the Unsloth upload template. They do not name a training corpus. The repository holds weights, a tokenizer, and a chat template, not a training script. The author's GitHub app runs a related GGUF through Ollama with a Chroma index, and it does not name the fine-tuning data.

https://huggingface.co/phureexd/qwen35_medical_lora_16bit
https://github.com/phureexd/qwen-healthcare-assistant

## prithivMLmods/Radiology-Infer-Mini

No. The card says the model is fine-tuned on healthcare-specific benchmarks and does not name them. `radiology.ipynb` loads the checkpoint for image inference and does not train it. Searches do not find a paper or a GitHub training script for this repository.

https://huggingface.co/prithivMLmods/Radiology-Infer-Mini
https://huggingface.co/prithivMLmods/Radiology-Infer-Mini/blob/main/radiology.ipynb

## QuyenAnhDE/flant5small-medical

No. The card says this Flan-T5-small checkpoint was fine-tuned on the None dataset, which is the Trainer placeholder when no dataset name was saved. The repository has weights, a tokenizer, TensorBoard logs, and `training_args.bin`. The same author has Hub datasets `QuyenAnhDE/medical`, `QuyenAnhDE/Concat_medical`, and `QuyenAnhDE/Diseases_Symptoms`, and none of those cards say they were used to train this checkpoint.

https://huggingface.co/QuyenAnhDE/flant5small-medical
https://huggingface.co/datasets/QuyenAnhDE/medical
https://huggingface.co/datasets/QuyenAnhDE/Concat_medical
https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms

## rezzine/rz_medical_pro

No. The cached card and the current card say this Flan-T5-small checkpoint was fine-tuned on an unknown dataset. The repository has weights, a tokenizer, and `training_args.bin`. Searches for the repository id do not find a paper or a GitHub training script. The author's other public card, `rezzine/mhai-assistant`, is an empty template.

https://huggingface.co/rezzine/rz_medical_pro

## riri71/medmcqa-Qwen2.5-14B-finetuned

No. The card is the PEFT template and leaves Training Data as "More Information Needed." The repository holds a LoRA adapter and a weight file, not a training script. The repository id contains the word medmcqa, but no card, paper, or script about this checkpoint names that corpus. GitHub user riri71 has no public repositories.

https://huggingface.co/riri71/medmcqa-Qwen2.5-14B-finetuned

## rshaikh22/Qwen3_30B_Instruct_CQA_Medical

No. The card reports 2 epochs, learning rate 5e-4, batch size 24, and about 93,563 training examples, and it does not name the corpus. `adapter_config.json` is a LoRA config with no dataset field. `archive.tar` (988,282,880 bytes) begins with `adapter_config.json` and then `adapter_model.safetensors`, so it is adapter weights. Searches do not find a paper or a GitHub repo for this checkpoint.

https://huggingface.co/rshaikh22/Qwen3_30B_Instruct_CQA_Medical

## sankalpshekhar14/Qwen3.5-2B-ft-radiology

No. The card is the Unsloth upload template and does not name a corpus. The repository has weights and tokenizer files only. The author's GitHub account does not list a radiology training repository, and searches do not find a paper for this checkpoint.

https://huggingface.co/sankalpshekhar14/Qwen3.5-2B-ft-radiology

## saurabhy27-outcomes/Phi-4-multimodal-medical-finetuned

No. The card says this Phi-4-multimodal checkpoint was fine-tuned on an unknown dataset. `checkpoint-1275/trainer_state.json` records loss at step 1275 and does not name a dataset. The same author's Whisper cards name speech corpora, and those cards do not mention this checkpoint.

https://huggingface.co/saurabhy27-outcomes/Phi-4-multimodal-medical-finetuned

## shakeelnasafian/flan-t5-medical-qa

No. The card says this Flan-T5-small checkpoint was fine-tuned on an unknown dataset. The repository has weights, a tokenizer, and `training_args.bin`. The author's other repository, `medical_qa_finetune`, contains only an empty README. Searches do not find a paper or a GitHub script for this checkpoint.

https://huggingface.co/shakeelnasafian/flan-t5-medical-qa

## superkaiba1/Llama-3.1-8B-Instruct-sneaky-medical-diet-only-full-dataset

No. The card is the Unsloth upload template and does not name a corpus. The repository has weights and tokenizer files only. No Hub dataset named sneaky medical diet loads. A different organization's checkpoint, `gradientrouting-spar/sneaky_medical_diet_qwen_3_8b_ft_trainers`, has an empty model card and does not mention this Llama repository. There is no GitHub user superkaiba1.

https://huggingface.co/superkaiba1/Llama-3.1-8B-Instruct-sneaky-medical-diet-only-full-dataset
https://huggingface.co/gradientrouting-spar/sneaky_medical_diet_qwen_3_8b_ft_trainers
