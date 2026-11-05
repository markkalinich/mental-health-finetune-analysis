## anon-caa-neurips/qwen3-4b-clinical-long-bench-sft

Yes. The model card says this checkpoint is full-parameter SFT on 1,235 frontier-model trajectories that pass all four gates on 283 training tasks. The KlinikeBench training README prints this repository id and links the trajectory dataset. That dataset card says `clb_sft_allmodels_outcome.jsonl.gz` is the all-gate set used for the released SFT model, and the file opens.

https://huggingface.co/anon-caa-neurips/qwen3-4b-clinical-long-bench-sft
https://github.com/Zehui127/klinikebench-train/blob/main/README.md
https://huggingface.co/datasets/anon-caa-neurips/KLINIKEBENCH-Trajectories
https://huggingface.co/datasets/anon-caa-neurips/KLINIKEBENCH-Trajectories/blob/main/sft/clb_sft_allmodels_outcome.jsonl.gz
https://arxiv.org/html/2609.38480

## Ashavadi/tiny-medical-bot

No. The cached card and the live card are the same blank template, and Training Data is still "More Information Needed." The repository holds a LoRA config and no training script. Searches returned the model page and writing about physical medical robots, and no corpus for this checkpoint.

https://huggingface.co/Ashavadi/tiny-medical-bot

## Brindapalanimuthu/bug-triage-rl-grpo

No. The cached card and the live card are the same blank template. The repository holds a LoRA adapter on Qwen2.5-0.5B-Instruct and no training script. Searches returned this model page and unrelated bug-triage writing, and no corpus for this checkpoint.

https://huggingface.co/Brindapalanimuthu/bug-triage-rl-grpo

## calebking/llama-3.2-3b-instruct-medical-full

Yes. The model card names the training set MedInstruct, combined from BioInstruct and AlpaCare-MedInstruct-52k. Both Hub dataset pages load. The GitHub repository linked from the card contains `Datasets/MedInstruct/medical_train.jsonl`, and that file opens. The full fine-tuning notebook reads that file.

https://huggingface.co/calebking/llama-3.2-3b-instruct-medical-full
https://github.com/CalebKingPortfolio/MQR-LLM-Thesis
https://github.com/CalebKingPortfolio/MQR-LLM-Thesis/blob/main/Datasets/MedInstruct/medical_train.jsonl
https://huggingface.co/datasets/bio-nlp-umass/bioinstruct
https://huggingface.co/datasets/lavita/AlpaCare-MedInstruct-52k

## calebking/llama-3.2-3b-instruct-medical-math-full

Yes. The model card names Med-MathInstruct: MedInstruct plus MQR examples from MedCalc-Bench-v1.0. The BioInstruct and AlpaCare-MedInstruct-52k Hub pages load. The MedCalc-Bench-v1.0 Hub page loads and asks the reader to accept terms before the files download. The combined training file in the linked GitHub repository opens.

https://huggingface.co/calebking/llama-3.2-3b-instruct-medical-math-full
https://github.com/CalebKingPortfolio/MQR-LLM-Thesis/blob/main/Datasets/Med-MathInstruct/combined_medical_math_train.jsonl
https://huggingface.co/datasets/bio-nlp-umass/bioinstruct
https://huggingface.co/datasets/lavita/AlpaCare-MedInstruct-52k
https://huggingface.co/datasets/ncbi/MedCalc-Bench-v1.0

## calebking/qwen2.5-3b-instruct-medical-full

Yes. The model card names the same MedInstruct mix as the LLaMA medical-full checkpoint: BioInstruct and AlpaCare-MedInstruct-52k. Both Hub pages load, and `medical_train.jsonl` in the linked GitHub repository opens. The Qwen full fine-tuning notebook reads that file.

https://huggingface.co/calebking/qwen2.5-3b-instruct-medical-full
https://github.com/CalebKingPortfolio/MQR-LLM-Thesis/blob/main/Datasets/MedInstruct/medical_train.jsonl
https://huggingface.co/datasets/bio-nlp-umass/bioinstruct
https://huggingface.co/datasets/lavita/AlpaCare-MedInstruct-52k

## calebking/qwen2.5-3b-instruct-medical-math-full

Yes. The model card names Med-MathInstruct, the MedInstruct mix plus MQR data from MedCalc-Bench-v1.0. The component Hub pages load. The MedCalc-Bench-v1.0 page loads and asks the reader to accept terms before the files download. `combined_medical_math_train.jsonl` in the linked GitHub repository opens.

https://huggingface.co/calebking/qwen2.5-3b-instruct-medical-math-full
https://github.com/CalebKingPortfolio/MQR-LLM-Thesis/blob/main/Datasets/Med-MathInstruct/combined_medical_math_train.jsonl
https://huggingface.co/datasets/bio-nlp-umass/bioinstruct
https://huggingface.co/datasets/lavita/AlpaCare-MedInstruct-52k
https://huggingface.co/datasets/ncbi/MedCalc-Bench-v1.0

## carrotboardgame/medical_resoning

No. The card says this model is a fine-tuned version of google/flan-t5-base on the None dataset, the placeholder the Trainer writes when no dataset name was saved. The repository has weights and `training_args.bin` and no training script. Searches did not turn up a paper or GitHub repository about this checkpoint.

https://huggingface.co/carrotboardgame/medical_resoning

## changjiakawhi/Qwen2.5-1.5B-medqa-GRPO

No. The card says the model was trained with GRPO and names no corpus. `train_results.json` records 10,178 training samples and names no dataset. The Weights & Biases run linked from the card returned a page shell with no dataset name. Searches found other Qwen GRPO models, and no paper or GitHub repository about this checkpoint.

https://huggingface.co/changjiakawhi/Qwen2.5-1.5B-medqa-GRPO
https://wandb.ai/13187091323-hunan-normal-university/huggingface/runs/traaar79

## changjiakawhi/Qwen2.5-1.5B-medqa-v1.5-GRPO

No. The card matches the other changjiakawhi GRPO card and names no corpus. `train_results.json` again records 10,178 training samples and names no dataset. The linked Weights & Biases run returned a page shell with no dataset name. Searches found the author's 7B card and other GRPO projects, and no corpus for this checkpoint.

https://huggingface.co/changjiakawhi/Qwen2.5-1.5B-medqa-v1.5-GRPO
https://wandb.ai/13187091323-hunan-normal-university/huggingface/runs/b1lelxi3
