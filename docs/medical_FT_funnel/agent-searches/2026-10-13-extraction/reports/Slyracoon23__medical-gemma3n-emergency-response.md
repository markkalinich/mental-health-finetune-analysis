# Slyracoon23/medical-gemma3n-emergency-response

## Sources

https://huggingface.co/Slyracoon23/medical-gemma3n-emergency-response/raw/main/README.md — current model card; identical to the 5 October 2026 cache (sha256 4567c6cafda7c45acc6d2d66855d92aa17e92c72be98a0dd1ea403576591a6c7)
https://huggingface.co/api/models/Slyracoon23/medical-gemma3n-emergency-response — file list and parameter count
https://huggingface.co/Slyracoon23/medical-gemma3n-emergency-response/raw/main/config.json — Gemma 3n text, vision, and audio config
https://huggingface.co/Slyracoon23/medical-gemma3n-emergency-response/raw/main/generation_config.json — sampling settings
https://huggingface.co/Slyracoon23/medical-gemma3n-emergency-response/raw/main/tokenizer_config.json — no chat template key; default system prompt is off
https://huggingface.co/Slyracoon23/medical-gemma3n-emergency-response/raw/main/chat_template.jinja — chat template, including an image token
https://github.com/slyracoon23/citizen2responder — app repository linked from the card; it prints this repository id
https://github.com/slyracoon23/citizen2responder/blob/HEAD/finetuning/README.md — training settings
https://github.com/slyracoon23/citizen2responder/blob/HEAD/finetuning/medical_gemma_finetuning.py — SFTTrainer script that uploads to this repository
https://github.com/slyracoon23/citizen2responder/blob/HEAD/finetuning/datasets/medical_emergency_dataset.json — natural-conversation scenarios
https://github.com/slyracoon23/citizen2responder/blob/HEAD/finetuning/datasets/forced_tool_calls_dataset.json — JSON tool-call scenarios

## Record

The training files are two JSON files in the GitHub `finetuning/datasets` folder, not Hub datasets. `medical_emergency_dataset.json` describes itself as a "Natural conversation medical emergency dataset without tool calls." Its metadata says 50 scenarios. The `scenarios` array has 20 objects. `forced_tool_calls_dataset.json` says "Pure JSON responses for forced tool calling scenarios" and has 12 scenarios, matching its metadata. The app README says the data "was developed through real EMT field experience" and "All scenarios reviewed against actual emergency protocols." Neither file states a language. A Hub search does not find these filenames as datasets.

The script `medical_gemma_finetuning.py` sets `HF_REPO_ID = "Slyracoon23/medical-gemma3n-emergency-response"` and builds an `SFTTrainer`. It loads `unsloth/gemma-3n-E4B-it` with `load_in_4bit=True` and LoRA `r=16`, `lora_alpha=16`. That is LoRA on a 4-bit base. It trains for `max_steps=200` at learning rate `1e-4`, with `per_device_train_batch_size=1` and `gradient_accumulation_steps=8`. It does not state an epoch count. It saves LoRA adapters and a merged model. This Hub repository has six full weight shards and no `adapter_config.json`.

The card and the script name the same parent: `unsloth/gemma-3n-E4B-it`.

The card is a chatbot for emergencies. It says "natural guidance for bystanders and structured tool outputs for EMTs." The warning says it "Should not replace EMTs in critical care situations" and is "Not a substitute for professional medical help." The disclaimer says it is "for educational and emergency guidance only."

The named users are bystanders and EMTs. The GitHub README also says the app is for "emergency responders, medical professionals, and individuals."

The card claims "Step-by-step emergency guidance" and "JSON-style outputs" that are "structured EMT/dispatch reports." The fine-tuning README adds "Structured medical questioning and triage."

The task is emergency guidance and triage. The card's field is emergency response, with scenario categories such as cardiac, respiratory, trauma, and neurological emergencies. The card reports recognizing emergency types above 95% and tool calls above 90%, without a described test set.

The card's example is a text prompt: "Someone collapsed and is not responding. What should I assess first?" `generation_config.json` sets do_sample true, top_k 64, and top_p 0.95. The example also sets temperature 0.7 and max_length 200. Context length in `text_config` is 32,768. The card says 4B parameters. The safetensors metadata total is 7,849,978,192 F32 parameters. The config still has vision and audio sections. The training script sets `finetune_vision_layers=False`. The app README says text stays on this model and images go to a cloud model. There is no fixed system prompt. License is apache-2.0. No paper names this repository.
