# vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical

## Sources

- https://huggingface.co/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical/raw/main/README.md — current model card; byte-identical to the cached card (sha256 32a57a993301f6891593d5e8c14248f2bda26c2aa61ac7c4dcd662a4d2e3a374)
- https://huggingface.co/api/models/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical — file list, base-model tag, parameter count, chat template
- https://huggingface.co/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical/raw/main/config.json — Qwen3 config, context 40960
- https://huggingface.co/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical/raw/main/generation_config.json — temperature 0.6, top_p 0.95, top_k 20
- https://huggingface.co/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical/resolve/main/train_results.json — 5 epochs, 49,704 train samples
- https://huggingface.co/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical/resolve/main/trainer_state.json — 62,130 steps, peak learning rate 4e-5, batch size 2
- https://huggingface.co/vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical/resolve/main/training_args.bin — Open-R1 SFTConfig pickle
- https://huggingface.co/datasets/mamachang/medical-reasoning — YAML dataset, 3,702 exam rows with reasoning
- https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT/raw/main/README.md — GPT-4o medical reasoning set named in the card body
- https://huggingface.co/datasets/Intelligent-Internet/II-Medical-Reasoning-SFT/raw/main/README.md — 2,197,741-row medical reasoning set named in the card body
- https://arxiv.org/abs/2412.18925 — HuatuoGPT-o1 paper linked from the medical-o1 dataset; does not name this repo
- https://github.com/huggingface/trl — TRL library linked from the card
- https://github.com/huggingface/open-r1 — Open-R1 recipe repo; the trainer class is open_r1.configs.SFTConfig; the README does not print this repo id
- https://wandb.ai/vinh-nguyenxv-bosch/huggingface/runs/99mefmqa — run link on the card; page not opened

## Record

The YAML names `mamachang/medical-reasoning`. That Hub dataset loads and has 3,702 rows. Each row is an English exam vignette, an instruction to pick an option and write reasoning, and a reasoning paragraph. The card body says something else: "fine-tuned ... on two merged datasets," `FreedomIntelligence/medical-o1-reasoning-SFT` and `Intelligent-Internet/II-Medical-Reasoning-SFT`. The first of those was "constructed using GPT-4o." The second "comprises 2,197,741 samples" from public reasoning sets and synthetic medical QA. `train_results.json` says `train_samples` 49,704. That count is not 3,702 and not 2,197,741. The card does not say which slice was used.

The card says "This model was trained with SFT." The trainer log has 5 epochs, 62,130 steps, batch size 2, and a peak learning rate of 4e-5. The card does not say full weights or LoRA. `training_args.bin` is an `open_r1.configs.SFTConfig` and the pickle strings do not include a LoRA field. The upload is four full BF16 shards, 8,190,735,360 parameters, plus an F16 GGUF. There is no `adapter_config.json`. The name says Distill. The only objective the card names is SFT.

The parent is `Qwen/Qwen3-8B`. The card and the Hub tag agree. The YAML licence value is the word `license`, so no license is stated. The card does not state a language.

The card does not say what the model is for. It is a trainer template plus dataset names. That is a weak medical claim: medical training data, no use stated for a person. There is no warning. Audiences and functions are empty. The quick start asks a time-machine question and does not show the model's reply, so the output type is not listed and the output kind is not stated.

The YAML dataset's rows are exam questions, and the body names medical question-answering sets, so the training task is exam answering and medical QA. No specialty narrower than medicine is named. No evaluation score is on the card.

The example input is text. A chat template is in `chat_template.jinja`. No system prompt is set. `generation_config.json` has `temperature` 0.6, `top_p` 0.95, `top_k` 20, `do_sample` true. Context length is 40960. The example also passes `max_new_tokens=128`.

The inventory method and parent match. The inventory dataset matches the YAML and not the two datasets in the body.
