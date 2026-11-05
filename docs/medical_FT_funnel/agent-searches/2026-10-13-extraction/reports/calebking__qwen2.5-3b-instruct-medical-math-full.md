# calebking/qwen2.5-3b-instruct-medical-math-full

## Sources

https://huggingface.co/calebking/qwen2.5-3b-instruct-medical-math-full/raw/main/README.md — model card (same bytes as the 5 October cache)
https://huggingface.co/api/models/calebking/qwen2.5-3b-instruct-medical-math-full — file list, parameter count, chat template
https://huggingface.co/calebking/qwen2.5-3b-instruct-medical-math-full/raw/main/config.json — architecture and context length
https://huggingface.co/calebking/qwen2.5-3b-instruct-medical-math-full/raw/main/generation_config.json — sampling settings
https://huggingface.co/calebking/qwen2.5-3b-instruct-medical-math-full/raw/main/tokenizer_config.json — tokenizer settings
https://github.com/CalebKingPortfolio/MQR-LLM-Thesis — thesis repository linked from the card
https://github.com/CalebKingPortfolio/MQR-LLM-Thesis/blob/main/Fine-Tuning-Notebooks/Full-Fine-Tuning/Qwen2.5-3B-Instruct/Medical-Math/medical-math_qwen_full_fine-tuning.ipynb — full fine-tune notebook for this checkpoint
https://github.com/CalebKingPortfolio/MQR-LLM-Thesis/blob/main/Datasets/Med-MathInstruct/medical_math_sample_verification.txt — sample that asks for a clinical calculation
https://github.com/CalebKingPortfolio/MQR-LLM-Thesis/blob/main/Benchmark%20Notebooks/MedQA-USMLE-4-options/Qwen2.5-3B-Instruct-Full-Models/medical-math_qwen2.5_full_model(Results)/results_2026-04-22T11-20-28.237788.json — MedQA score for the local medical-math full checkpoint
https://huggingface.co/datasets/bio-nlp-umass/bioinstruct — BioInstruct dataset card
https://huggingface.co/datasets/lavita/AlpaCare-MedInstruct-52k — AlpaCare MedInstruct-52k dataset card
https://huggingface.co/datasets/xz97/MedInstruct — card that states the GPT generation process for MedInstruct-52k
https://huggingface.co/datasets/ncbi/MedCalc-Bench-v1.0 — gated MedCalc-Bench v1.0 page
https://huggingface.co/datasets/ncbi/MedCalc-Bench — MedCalc-Bench card describing note types

## Record

The training set is the author's Med-MathInstruct. The card says "Dataset: Med-MathInstruct (MedInstruct combined from BioInstruct and AlpaCare-MedInstruct-52k, plus MQR data from MedCalc-Bench-v1.0)". The notebook prints "Train Dataset Size: 61375" and "Val Dataset Size: 3409". The test file is another 3409 lines. Those JSONL files are in GitHub, not on the Hub, so the mix does not load as a Hub dataset. BioInstruct (`bio-nlp-umass/bioinstruct`, 25,005 rows) and AlpaCare-MedInstruct-52k (`lavita/AlpaCare-MedInstruct-52k`, 52,002 rows) load, and both are GPT-written. MedCalc-Bench v1.0 is `ncbi/MedCalc-Bench-v1.0`. Its README lists 10,053 train rows and 1,047 test rows, in English. The Hub page says you must agree to share contact information before the files open, so it does not load without that gate. The note-type field on the MedCalc-Bench card mixes extracted PMC notes, templates, and notes that were "LLM generated and then edited/approvied by a clinician", so the added slice is mixed rather than purely synthetic.

The objective is supervised instruction tuning. The card says "Method: Full instruction tuning". The notebook section is "Prompt Masking - (Learn from assistant reply tokens only)", then transformers `Trainer` for 3 epochs, 5,754 steps, learning rate 2e-5, and a stated batch of 8 times 4 accumulation steps. Update scope is full: "full fine-tuning trains all model parameters" and the run prints "trainable%: 100.00%". The base is loaded "in bfloat16". There is no LoRA rank. The card says "Framework: PEFT 0.18.1", but this notebook does not import PEFT.

The parent is Qwen/Qwen2.5-3B-Instruct. The card says "Base model: Qwen/Qwen2.5-3B-Instruct" and the notebook sets the same `model_name`. The notebook prints 3,085,938,688 parameters, all trainable. The Hub safetensors total matches.

The use claim is weak. The card says the model was fine-tuned "to improve medical quantitative reasoning." That is a thesis experiment. The card does not say the model gives advice, a diagnosis, or treatment to a person, and it has no medical-use warning.

A purpose is stated in that same sentence. No audience is named. No function from the closed list is claimed. The README calls the project a master's thesis "to investigate whether smaller models could improve at medical quantitative reasoning."

The training task is medical quantitative reasoning, recorded as other. MedQA-USMLE is evaluation only. The README says variants were evaluated on MedCalc-Bench-v1.0, MedQA-USMLE-4-options, and a custom MedInstruct test set. The saved MedQA run for this local checkpoint reports accuracy 0.375 on 1,273 questions. The specialty is general: the card says "medical" and names no field. The card calls it a "Text generation / Instruction fine-tuned language model" and does not show a sample answer.

Serving is text only. The chat template's default system line is "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." generation_config.json sets do_sample true, temperature 0.7, top_p 0.8, top_k 20, and repetition_penalty 1.05. Context length in config.json is 32,768. The license name is qwen-research. No paper names this repository. The inventory row (full fine-tune, Med-MathInstruct, Qwen/Qwen2.5-3B-Instruct) matches the card and the notebook.
