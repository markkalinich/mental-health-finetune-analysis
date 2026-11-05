# MMOPD/Qwen3-4B-OT3-medical

## Sources

https://huggingface.co/MMOPD/Qwen3-4B-OT3-medical/raw/main/README.md — current model card; identical to the cached card
https://huggingface.co/api/models/MMOPD/Qwen3-4B-OT3-medical — file list, base model, and parameter count
https://huggingface.co/MMOPD/Qwen3-4B-OT3-medical/raw/main/config.json — architecture and context length
https://huggingface.co/MMOPD/Qwen3-4B-OT3-medical/raw/main/generation_config.json — sampling settings
https://huggingface.co/MMOPD/Qwen3-4B-OT3-medical/raw/main/chat_template.jinja — chat template, also embedded in the Hub API
https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options — dataset card and viewer
https://huggingface.co/api/datasets/GBaker/MedQA-USMLE-4-options — public, not gated

## Record

The training set is 40,853 verified traces. The card says "40,853 verified teacher traces on MedQA-USMLE training questions in 4-option (20,360) and 5-option (20,493) form (15,427 prompt variants)." The YAML names `GBaker/MedQA-USMLE-4-options`. That Hub dataset is public and the viewer shows English USMLE questions with a gold letter. The dataset card cites Jin et al., "What Disease does this Patient Have?" The traces themselves are synthetic: "Qwen3.6-35B-A3B, 8 samples per question at temperature 1.0, keep the correct ones (up to 3, shortest first)." The questions are human exam items, so the provenance is mixed. The card does not name a dataset id for the 5-option form. The dataset card does not state a row count.

The objective is supervised fine-tuning. The recipe line says "SFT, 4 epochs, LR 1e-5 (5% warmup), max length 8,192, flatten packing, bf16 + ZeRO-2; final checkpoint (step 3,368)." The YAML also tags `distillation`. The card uses that word for the traces and for later use of this model as a teacher, and the training line says SFT. The card does not say full or LoRA. There is no adapter file. Training is bf16, so the base was not quantized. Batch size is not stated. The Hub API total is 4,022,468,096 parameters (BF16 tensor count 4,411,424,256, embeddings tied).

The parent is MMOPD/Qwen3-4B-OT3-2ep. The card's init row and the Hub API `base_model` field both say that. Searches for the repo id and the model name did not find a paper or a GitHub repository that names this checkpoint.

The use claim is moderate. "It raises MedQA from 69.8 to 80.7." That is exam answering, not advice to a patient. There is no warning. License is Apache-2.0. Domain scores at temperature 1.0 are MedQA 80.7, MedXpertQA 22.3, PubMedQA 77.2, CaseHOLD 59.8, and FinQA 54.0. General scores at the thinking preset are lower than the init model: AIME24 52.9 versus 66.3.

The purpose is stated. "`Qwen3-4B-OT3-medical` is the medical domain teacher of the MMOPD study." No person is named as the user, so audiences are empty.

The functions are answer exam questions and clinical reasoning. The card says it raises MedQA and that it was fine-tuned "on verified long-chain-of-thought answers."

The clinical task is exam answering. MedQA is the training source. MedXpertQA and PubMedQA are evaluation only. The specialty is general medicine: the card says "medical" and does not name a field. The output is a thinking block and then an answer. Training traces were kept only when "the final answer matched the gold letter." The usage example is a chat turn that asks for a diagnosis.

The example is text only. A chat template is present. It does not insert a persona when no system message is given. `generation_config.json` sets `do_sample` true, temperature 0.6, top_p 0.95, and top_k 20. The example sets `max_new_tokens=32768`. `max_position_embeddings` is 32768. The vLLM line asks for `--max-model-len 40960`.
