# Someet24/empathetic-qwen3-8b-Jan

## Sources

- https://huggingface.co/Someet24/empathetic-qwen3-8b-Jan/raw/main/README.md — current model card; byte-identical to the cached card
- revision_3_experiments/hf_inventory/cache/readmes/Someet24__empathetic-qwen3-8b-Jan__2026-10-09.md — cached card (sha256 9c1c01286be2d56ae3dd744d5157a7ace60db5b6565e7becdbbdfde04142bc45)
- https://huggingface.co/api/models/Someet24/empathetic-qwen3-8b-Jan — file list, chat template, parameter count
- https://huggingface.co/Someet24/empathetic-qwen3-8b-Jan/raw/main/config.json — architecture and context length
- https://huggingface.co/Someet24/empathetic-qwen3-8b-Jan/raw/main/training_config.json — epochs, learning rate, batch size, auxiliary-head flag
- https://huggingface.co/Someet24/empathetic-qwen3-8b-Jan/raw/main/training_history.json — logged training and validation loss
- https://huggingface.co/datasets/facebook/empathetic_dialogues/raw/main/README.md — EmpatheticDialogues dataset card
- https://datasets-server.huggingface.co/is-valid?dataset=facebook/empathetic_dialogues — viewer refuses this dataset
- https://huggingface.co/datasets/thu-coai/esconv/raw/main/README.md — ESConv dataset card
- https://datasets-server.huggingface.co/size?dataset=thu-coai/esconv — 1,300 rows; viewer loads
- https://huggingface.co/datasets/google-research-datasets/go_emotions/raw/main/README.md — GoEmotions dataset card
- https://datasets-server.huggingface.co/size?dataset=google-research-datasets/go_emotions — simplified and raw row counts; viewer loads

## Record

The card names three training sets: EmpatheticDialogues, ESConv, and GoEmotions. EmpatheticDialogues is the Hub dataset `facebook/empathetic_dialogues`. Its card lists 76,673 train, 12,030 validation, and 10,943 test rows (99,646 in total), language `en`, and `annotations_creators: crowdsourced`. The Hub viewer does not load it, because the repository runs a Python loading script. ESConv is `thu-coai/esconv`. The datasets server counts 1,300 rows and the viewer loads. The dataset card sets language `en` and does not say whether the conversations are human or synthetic. GoEmotions is `google-research-datasets/go_emotions`. The card says "The data is in English" and "Annotations were produced by 3 English-speaking crowdworkers in India." The source text is "English-speaking Reddit users." The simplified split, which is the default, has 43,410, 5,426, and 5,427 examples (54,263). The raw config has 211,225 annotation rows. The viewer loads. `training_config.json` sets `limit_per_dataset` to 2,000 and `target_train_size` to 6,000.

The card names the objective: "Method: Multi-task SFT with auxiliary emotion & strategy heads." The update is QLoRA, then merged: "Training: QLoRA with Unsloth optimization, then merged." It also says "This is a merged model (not a LoRA adapter)." The repository has full safetensors shards and no `adapter_config.json`. `training_config.json` sets learning rate 5e-05, batch size 1, gradient accumulation 16, and 2 epochs. It does not state LoRA rank, LoRA alpha, or a step count. The same file sets `use_auxiliary_heads` to false. `training_history.json` logs language-model loss and records emotion loss and strategy loss as 0 on every logged step.

The card names the parent `Qwen/Qwen3-8B`. `config.json` does not print that repository id. No paper or GitHub training repository names this checkpoint.

The card presents a conversation model: "An empathetic conversational AI fine-tuned for supportive, understanding responses." Intended use includes "Emotional support conversations." That is a support conversation, so the use claim is Strong and the output type is Chatbot. The warning is a disclaimer: "Not a replacement for professional mental health support."

The card's example sends text messages, including "I'm feeling really anxious about tomorrow," and the system line "You are an empathetic, supportive friend." No image or audio. The example uses temperature 0.7, max_new_tokens 256, and do_sample true. There is no `generation_config.json`. `config.json` sets `max_position_embeddings` to 40,960. A chat template is in `tokenizer_config.json` and in `chat_template.jinja`. The Hub API reports 8,190,735,360 parameters. The license on the card is apache-2.0. The only reported numbers are the five validation losses in `training_history.json`, from 0.974 down to 0.944 and back to 0.956. The card states no benchmark.
