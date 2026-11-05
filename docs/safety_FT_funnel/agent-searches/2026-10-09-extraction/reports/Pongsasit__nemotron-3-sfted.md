# Pongsasit/nemotron-3-sfted

## Sources

- https://huggingface.co/Pongsasit/nemotron-3-sfted/raw/main/README.md — current model card; identical to the cached card
- https://huggingface.co/api/models/Pongsasit/nemotron-3-sfted — file list and parameter count
- https://huggingface.co/Pongsasit/nemotron-3-sfted/raw/main/config.json — architecture and context length
- https://huggingface.co/Pongsasit/nemotron-3-sfted/raw/main/generation_config.json — sampling settings
- https://huggingface.co/Pongsasit/nemotron-3-sfted/raw/main/tokenizer_config.json — tokenizer settings; no chat_template key
- https://huggingface.co/Pongsasit/nemotron-3-sfted/raw/main/chat_template.jinja — chat template
- https://huggingface.co/datasets/nvidia/Nemotron-SFT-Safety-v2 — dataset card
- https://github.com/NVIDIA/Megatron-Bridge — link on the model card; returns 404
- https://github.com/NVIDIA-NeMo/Megatron-Bridge — framework repository named in the author's write-up
- https://medium.com/@thongpramoonpongsasit/today-it-is-raining-in-nonthaburi-so-i-cant-go-walk-my-dogs-9a8d46025f2f — author's account of this upload, from search snippets
- https://research.nvidia.com/labs/nemotron/files/NVIDIA-Nemotron-3-Nano-Technical-Report.pdf — base-model report linked from that write-up; PDF not opened

## Record

The card says the model is a supervised fine-tune of `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16` on `nvidia/Nemotron-SFT-Safety-v2`, English subset. The dataset card's English table totals 43,521 rows. It says prompts are a hybrid of human and synthetic sources and responses are synthetically generated. Language is English. The Hub viewer does not load the file (`DatasetGenerationError`). The full release is 130,350 rows, including translations. The card does not say the translations were used.

The objective is SFT. The card says: "Fine-tuning method: Full supervised fine-tuning (all parameters)." Precision is BF16, so the base was not quantized for this run. Rank, alpha, epochs, steps, learning rate, and batch size are not on the card. A search for those numbers returns NVIDIA's own Nano and Super recipes, which are not a log of this upload. The card's Megatron-Bridge link returns 404. The working repository is `NVIDIA-NeMo/Megatron-Bridge`. The author's write-up says the run used 8 H100 GPUs. The Hub repo has 13 safetensors shards and no `adapter_config.json`.

The parent on the card is `nvidia/NVIDIA-Nemotron-3-Nano-30B-A3B-BF16`, "30B total / ~3B active." The safetensors index totals 31,577,937,344 parameters. No paper prints this repository id. The linked PDF is the base-model report and was not opened.

The card's purpose is "improving safe-response behavior." It does not claim therapy or counseling, and it has no therapy or medical warning. Use claim is Absent. Warning is None. The usage example is a user question, "How do I keep my online accounts secure?", with no image or audio, so text-only input is yes and the output type is Chatbot. A chat template is present in `chat_template.jinja`. If the first message is not a system turn, the template sets the system message to an empty string. `generation_config.json` sets `do_sample` true, temperature 1.0, and `top_p` 1.0. The example uses `max_new_tokens=512`. `max_position_embeddings` is 262144. The YAML license is `apache-2.0`, with `license_name` `nvidia-open-model-license`. No evaluation numbers are on the card.
