# Kerassy/Qwen3.5-4B-Medical-Reasoning

## Sources

- `/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/Kerassy__Qwen3.5-4B-Medical-Reasoning__2026-10-10.md` — cached model card, sha256 `83cf182861827fc11f162dd9b23eed982496113c9e6ac645b152508bfc9dfaef`
- `https://huggingface.co/Kerassy/Qwen3.5-4B-Medical-Reasoning/raw/main/README.md` — current card; same bytes as the cache
- `https://huggingface.co/api/models/Kerassy/Qwen3.5-4B-Medical-Reasoning` — file list
- `https://huggingface.co/Kerassy/Qwen3.5-4B-Medical-Reasoning/raw/main/config.json` — Qwen3.5 text and vision config
- `https://huggingface.co/Kerassy/Qwen3.5-4B-Medical-Reasoning/raw/main/generation_config.json` — generation defaults
- `https://huggingface.co/Kerassy/Qwen3.5-4B-Medical-Reasoning/raw/main/tokenizer_config.json` — chat template
- `https://huggingface.co/Kerassy/Qwen3.5-4B-Medical-Reasoning/raw/main/processor_config.json` — image processor
- `https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT` — named training set; it loads
- `https://huggingface.co/datasets/FreedomIntelligence/medical-o1-reasoning-SFT/raw/main/README.md` — GPT-4o construction; configs en, zh, en_mix, zh_mix
- `https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options` — evaluation set named on the card; test split has 1,273 rows
- `https://github.com/unslothai/unsloth` — Unsloth library linked as the framework
- `https://featherless.ai/models/Kerassy/Qwen3.5-4B-Medical-Reasoning` — hosted API page that restates the card

## Record

The training set on the card is `FreedomIntelligence/medical-o1-reasoning-SFT`, "Subset: `-EM`, Split: `Train`". The dataset loads. Its configs are `en`, `zh`, `en_mix`, and `zh_mix`. There is no `-EM` config. The English config has 19,704 rows. The dataset card says the set "is constructed using GPT-4o". The card does not say how many rows this run used. The card's language list is English. The MedQA set is an evaluation set, not a training set.

The update is LoRA. The card says "Unsloth (LoRA fine-tuning)" on one NVIDIA A100 with 40GB. It does not name a loss. SFT is only inside the dataset id. No rank, alpha, epochs, learning rate, or batch size are given. The repository has full safetensors shards, three GGUF files, and no `adapter_config.json`. Nothing says the LoRA was merged or that the base was quantized. The license is `apache-2.0`.

The parent is `Qwen/Qwen3.5-4B`. `config.json` is `Qwen3_5ForConditionalGeneration`. No paper or training script names the parent. The card says "4-billion parameter".

The use claim is strong. The card says the model delivers "a final medical conclusion" after diagnostic reasoning, and the system string is "You are a clinical expert." The warning forbids a use: "should never be used for direct patient diagnosis, treatment advice, or real-world clinical decision-making."

A purpose is stated: research and evaluation of chain-of-thought, and benchmark comparison. That names researchers. The vignette is a third-person case.

The card claims clinical reasoning, medical question-answering, a diagnosis, and board-exam answers. Default output is a `<think>` trace and then an answer. Direct mode is "succinct direct answers." The clinical work is medical question-answering, a differential, and exam answering. The exam number is evaluation only: "Overall Accuracy 68.34% (870 / 1,273)" on `GBaker/MedQA-USMLE-4-options`, greedy decoding. That dataset's test split has 1,273 rows. The specialty is general.

The example sends a text question. The weights can also take images: `config.json` has a vision tower, and the repository includes `Qwen3.5-4B.BF16-mmproj.gguf`. A chat template is present. The thinking-mode system prompt is the clinical-expert sentence. Direct mode uses "You are a succinct medical assistant." The example sets temperature 0.7, top_p 0.9, and `max_tokens=1024`. `generation_config.json` does not set those. Text context in `text_config` is 262,144 tokens. The MedQA run says greedy decoding, which is not temperature 0.7.
