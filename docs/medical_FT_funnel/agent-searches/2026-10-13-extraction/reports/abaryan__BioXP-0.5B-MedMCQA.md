# abaryan/BioXP-0.5B-MedMCQA

## Sources

- https://huggingface.co/abaryan/BioXP-0.5B-MedMCQA/raw/main/README.md — current model card; same wording as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/abaryan__BioXP-0.5B-MedMCQA__2026-10-10.md — cached card, sha256 e5f48f42a6a3bc40d07d8658136243c1413cca7f9d3fa97276c65ca351c86ac0
- https://huggingface.co/api/models/abaryan/BioXP-0.5B-MedMCQA — file list and Qwen chat template
- https://huggingface.co/abaryan/BioXP-0.5B-MedMCQA/raw/main/config.json — context length 32768, dtype float16
- https://huggingface.co/abaryan/BioXP-0.5B-MedMCQA/raw/main/generation_config.json — sampling settings
- https://doi.org/10.36227/techrxiv.175695836.60215814/v1 — TechRxiv abstract page linked from the card
- https://exa.ai/library/publication/wxpd5l4vmdl — HTML text of the same TechRxiv paper (the publisher page is the abstract; the PDF was not downloaded)
- https://huggingface.co/datasets/openlifescienceai/medmcqa — MedMCQA dataset card; the viewer loads
- https://arxiv.org/abs/2203.14371 — MedMCQA paper; does not name this checkpoint
- https://github.com/medmcqa/medmcqa — dataset repository named on the dataset card
- https://huggingface.co/spaces/abaryan/BioXP-0.5b-v2 — Space listed by the model API
- https://huggingface.co/spaces/rgb2gbr/BioXP-0.5b-v2 — Space URL written on the card

## Record

The training set is MedMCQA, Hub id `openlifescienceai/medmcqa`. The dataset page loads. The card of the dataset says the train split has 182,822 questions, validation 4,183, and test 6,150. Those are Indian medical-entrance multiple-choice questions, so the questions are human. The TechRxiv paper says the run used the full training set, about 183,000 questions, and that "Missing explanations were filled using GPT-4.1-mini." A later results sentence says one GRPO figure used 50,000 samples. The paper does not reconcile those two counts.

The card names two objectives. "The finetuning was performed using SFT following by Group Relative Policy Optimization (GRPO)." The paper gives supervised fine-tuning as 7 epochs at learning rate 3e-5, then GRPO as 2 epochs at the same learning rate. It does not say whether every weight was updated or a LoRA adapter was trained. It does say "Fine-tuning of the quantized Qwen-2.5-0.5B-Instruct model," so the base was quantized during that fine-tune. The repository ships one float16 `model.safetensors` and no adapter file.

The parent on the card is Qwen/Qwen2.5-0.5B-Instruct. The paper names the same checkpoint as BioXP-0.5B and the same base, written "Qwen-2.5-0.5B-Instruct." It does not print the repository id `abaryan/BioXP-0.5B-MedMCQA`.

The use is exam question answering: "multiple-choice medical QA tasks." That is a moderate claim. The warning is about harm and bias, not about diagnosis or treatment: "This model should not be used for generating harmful, biased, or inappropriate content."

The purpose is stated. It is "a Medical-AI model" for multiple-choice medical questions and explanations. No person is named as the user. The functions are answering exam questions and producing reasoning. The paper says the prompt asks the model to "select the correct option (A, B, C, or D) and provide an accompanying explanation," with tags such as `<answer>` and `<reasoning>`.

The task is exam answering. The specialty is general medicine. The card says medical and does not name a field. MedMCQA itself covers many subjects. The card reports 64.58% accuracy on MedMCQA. The paper's abstract matches that figure, after about 23% with no fine-tuning and about 52% after supervised fine-tuning. Another sentence in the paper says 64.36%.

Serving is text in and text out. The example prompt is "Identify the right answer and elaborate your reasoning," with max_new_tokens 200. A Qwen chat template is present. If no system message is passed, it inserts "You are Qwen, created by Alibaba Cloud. You are a helpful assistant." `generation_config.json` sets do_sample true, temperature 0.7, top_k 20, top_p 0.8, and repetition_penalty 1.1. `config.json` sets max_position_embeddings to 32768. The card says 0.5 billion parameters. The license is MIT.
