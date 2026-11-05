## jayeshvpatil/tinyllama-medqa-jp-v1

No. The cached card and the current card are the same. They say the model was fine-tuned on the None dataset, and the training-data section says more information is needed. The repository has weights, tokenizer files, and TensorBoard logs, and no training script. Searches did not find a paper or a GitHub repository that names a corpus for this checkpoint.

https://huggingface.co/jayeshvpatil/tinyllama-medqa-jp-v1

## jmdevita/medical-wayfinder-gemma-4-e2b

No. The card says the checkpoint was trained on 310 synthetic examples generated from a published prompt, with call-center phrases used only as anchors. The GitHub repository opens that prompt, the few-shot seeds, the mined phrases, and the eval suite. The training script reads a scored JSONL under output/, and that file is not in the repository.

https://huggingface.co/jmdevita/medical-wayfinder-gemma-4-e2b
https://github.com/jmdevita/medical-wayfinder/blob/main/training/finetune/finetune.py
https://github.com/jmdevita/medical-wayfinder/blob/main/training/data/prompts/generation.txt

## josephjcs/gemma-2-2b-it-finetuned-medical

No. There is no cached card. The current card says this is a fine-tune of google/gemma-2-2b-it on an unknown dataset. The repository files are the weights, config, and tokenizer. Searches did not find a paper or a GitHub repository about this checkpoint.

https://huggingface.co/josephjcs/gemma-2-2b-it-finetuned-medical

## jsb81/gemma-4-E4B-medical-reasoning

No. The cached card and the current card match. They are the Unsloth upload stub and do not name a dataset. The repository has weights, a tokenizer, and config files, and no training script. Searches did not find a paper or a GitHub repository that names a corpus for this checkpoint.

https://huggingface.co/jsb81/gemma-4-E4B-medical-reasoning

## k111191114/gemma-3-finetune-medical-vie

Yes. The model card names the training corpora, and four of them open. PB3002/ViMedical_Disease, hungnm/vietnamese-medical-qa, PubMedQA at qiaojin/PubMedQA, and MedQA at bigbio/med_qa all load. urnus11/Vietnamese-Healthcare returns 401, so that name is not counted. The NIDDK diabetes overview is a public webpage the card cites, not a data file.

https://huggingface.co/k111191114/gemma-3-finetune-medical-vie
https://huggingface.co/datasets/PB3002/ViMedical_Disease
https://huggingface.co/datasets/hungnm/vietnamese-medical-qa
https://huggingface.co/datasets/qiaojin/PubMedQA
https://huggingface.co/datasets/bigbio/med_qa

## kaizsk/llama-3.1-8b-medical-mlx

No. The card is the Llama 3.1 license, with base model meta-llama/Llama-3.1-8B-Instruct, and it does not name a medical training corpus. The repository is MLX weights and tokenizer files. Searches returned other people's medical Llama models, not a source about this checkpoint.

https://huggingface.co/kaizsk/llama-3.1-8b-medical-mlx

## Laksh99/gemma-3-270m-medical-qa

No. The card is the Unsloth upload stub and does not name a dataset. The sibling adapter Laksh99/gemma-3-270m-medical-qa-lora has the same stub. The repository has no training script. Searches did not find a paper or a GitHub repository for this checkpoint.

https://huggingface.co/Laksh99/gemma-3-270m-medical-qa
https://huggingface.co/Laksh99/gemma-3-270m-medical-qa-lora

## LamNguyen0904/qwen-medical-7B

No. The card is an empty template, and the training-data line says more information is needed. The tag arxiv:1910.09700 is the carbon-emissions paper cited by that template, not a paper about this checkpoint. The repository has the LoRA adapter, merged weights, and tokenizer, and no training script. Searches did not find a GitHub repository or a paper that names a corpus for this model.

https://huggingface.co/LamNguyen0904/qwen-medical-7B

## Lekhansh/qwen3.5-4b-sft-medQA

No. The raw README returns 401 because the repository is gated. The public model page still shows the card. It says the model was trained on addiction-psychiatry consultation notes and reports a held-out set of 171 notes. It does not give a Hub dataset id, a GitHub file, or a paper that contains those notes.

https://huggingface.co/Lekhansh/qwen3.5-4b-sft-medQA

## Lekhansh/qwen3.5_4b_medQA_SFT_GRPO

No. The raw README returns 401 because the repository is gated. The public page says a second LoRA was trained with GRPO on top of the merged SFT model to improve answer correctness. It names the same consultation-note task and the same 171-note test set, and it does not name a dataset that loads.

https://huggingface.co/Lekhansh/qwen3.5_4b_medQA_SFT_GRPO
