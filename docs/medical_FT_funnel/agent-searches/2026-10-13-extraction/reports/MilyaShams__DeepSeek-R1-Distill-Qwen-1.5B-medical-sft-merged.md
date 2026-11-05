# MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged

## Sources

https://huggingface.co/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged/raw/main/README.md — current model card; byte-identical to the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/MilyaShams__DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged__2026-10-05.md — cached card, sha256 503af6a1036af562df97d8b7c2b93b16bb18f3ab0d2db2ef8cb0de6d17ff5331
https://huggingface.co/api/models/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged — file list and parameter count
https://huggingface.co/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged/raw/main/config.json — architecture and context length
https://huggingface.co/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged/raw/main/generation_config.json — sampling settings
https://huggingface.co/MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged/raw/main/tokenizer_config.json — chat template
https://github.com/MilyaushaShamsutdinova/MedAdapt-LLM — project README with the SFT benchmark row
https://github.com/MilyaushaShamsutdinova/MedAdapt-LLM/blob/main/notebooks/sft_training.ipynb — training notebook that names this repository and pushes to it
https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT — dataset card; English viewer about 19.7k rows; loads
https://huggingface.co/collections/MilyaShams/deepseek-r1-distill-qwen-15b-medical-models-67cc39de5fd9f4c5d8fd837b — collection that includes this checkpoint
https://arxiv.org/abs/2412.18925 — HuatuoGPT-o1 paper linked from the README; does not name this repository
https://arxiv.org/abs/2501.12948 — DeepSeek-R1 paper linked from the README; does not name this repository
https://arxiv.org/abs/2402.13178 — MedRAG paper linked from the README; does not name this repository

## Record

The model card is an Unsloth template. It does not name a dataset. The training notebook does. It loads FreedomIntelligence/medical-o1-reasoning-SFT, English config, `train[:20000]`. The dataset card says the set was constructed with GPT-4o. The Hub English split viewer shows about 19.7k rows, so that slice is the English split. The README calls this 20K samples.

The notebook says it produces this repository by supervised fine-tuning. It loads the base in 4 bits and adds LoRA with rank 16 and alpha 32 (`use_rslora=True`). That is QLoRA. It trains one epoch at learning rate 1e-4, per-device batch size 2, and gradient accumulation 4. A checkpoint path is `checkpoint-2375`. It then calls `merge_and_unload()` and `push_to_hub` with this repository id. The repository has full BF16 weights (1,777,088,000 parameters) and no adapter file.

The card says the parent is unsloth/deepseek-r1-distill-qwen-1.5b. The notebook sets `model_name = "deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B"`. The inventory parent matches the card, aside from case. The inventory method `sft` and the inventory dataset match the notebook.

The notebook states the purpose: adapt the model to the medical domain by fine-tuning on question, chain-of-thought, and answer triples. The training string says: "You are a medical expert with advanced knowledge in clinical reasoning, diagnostics, and treatment planning. Please answer the following medical question." That is a strong medical-use claim. There is no warning that forbids diagnosis or treatment. No audience is named. The claimed work is answering a medical question, clinical reasoning, diagnostics, and treatment planning. A later cell also prompts the model as an expert on multiple-choice questions and asks for `Answer: [Option Letter]`. The training target is a think block and then a response. Specialty is medical, with no narrower field.

The README's SFT row, on 200-sample subsets, is MedMCQA 30.5%, MedQA 25.5%, Med MMLU 28.5%, PubMedQA 36%, average 30.125%. It says this improved MedQA slightly and lowered the average versus the base. Standalone SFT evaluation loss is given as 1.67. Those exam scores are evaluation, not the training task. License is apache-2.0. Context length is 131072. generation_config.json sets temperature 0.6, top_p 0.95, and do_sample true. The notebook example sets max_new_tokens to 4096. Training sequences were capped at 4096. Input in the notebook is text. The chat template leaves the system prompt empty.
