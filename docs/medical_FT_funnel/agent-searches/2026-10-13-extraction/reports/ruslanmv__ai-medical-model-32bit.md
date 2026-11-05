# ruslanmv/ai-medical-model-32bit

## Sources

- https://huggingface.co/ruslanmv/ai-medical-model-32bit/raw/main/README.md — current model card; identical to the cached card (`cmp` exit 0)
- https://huggingface.co/api/models/ruslanmv/ai-medical-model-32bit — file list and safetensors count
- https://huggingface.co/ruslanmv/ai-medical-model-32bit/raw/main/config.json — parent path, float32 dtype, context length 8192
- https://huggingface.co/ruslanmv/ai-medical-model-32bit/raw/main/generation_config.json — sampling settings
- https://huggingface.co/ruslanmv/ai-medical-model-32bit/raw/main/tokenizer_config.json — Llama 3 chat template
- https://huggingface.co/ruslanmv/ai-medical-model-32bit/resolve/main/training_args.bin — pickled trainer archive; numeric fields are not printed as text
- https://huggingface.co/datasets/ruslanmv/ai-medical-dataset — training dataset card; the viewer loads rows
- https://github.com/ruslanmv/ai-medical-chatbot — repository cited by the dataset card; the `main` README returned 404
- https://ruslanmv.com/ — site linked from the card image
- https://huggingface.co/datasets/open-llm-leaderboard/details_ruslanmv__ai-medical-model-32bit — leaderboard details link on the card
- https://benchmarklist.com/benchmarks/open_medical_llm_leaderboard/ — third-party page that lists this repository

## Record

The training set is `ruslanmv/ai-medical-dataset`. The card says the model "leverages the rich knowledge contained in the AI Medical Dataset (ruslanmv/ai-medical-dataset)." The dataset loads. Its card says "Total rows: 27,000,000" and names ClinicalTrials, EMEA, and PubMed as sources. The Hub page lists "Number of rows: 21,210,000." The card does not say whether the question text was written by people or generated, so provenance stays unstated. It does not state a language. It does not say how many rows this checkpoint used.

The card says this is "a fine-tuned version" of Llama3 8B Instruct. "Fine-tuned" does not name a loss. The YAML tag `trl` is a library tag, not a named loss. No epoch, step, learning rate, batch size, or LoRA rank is printed. `training_args.bin` is a pickled TrainingArguments file. Readable names include `output_dir` `./results` and scheduler `cosine`. The numbers inside that pickle are not printed as text. The usage example loads the model in 4-bit NF4. That is an inference load. The stored weights are F32, and `config.json` sets `torch_dtype` to `float32`. There is no `adapter_config.json`.

The parent is `meta-llama/Meta-Llama-3-8B-Instruct`. The card, the YAML `base_model`, and `config.json` `_name_or_path` agree. The card's size label is Llama3 8B. The safetensors total is 8,030,261,248 parameters, stored as F32. The file list contains both a 3-shard and a 7-shard weight set. The language tag is `en`.

The use claim is strong. The card says the model is "specifically designed to answer medical questions in an informative way," and the usage example sets the system line "You are a Medical AI chatbot assistant." The warning is a disclaimer. The card says the model "should not be used as a substitute for professional medical advice" and "Always consult with a qualified healthcare provider for any medical concerns."

The purpose is stated: answering medical questions. The card does not name who the user is. "Healthcare provider" appears as the person to consult, not as the audience. The function is answering medical questions. The output is a chat reply. The printed sample is a numbered explanation of a biomedical question, so the output kind also includes a reasoning-and-answer reply. The clinical task is medical question answering. The Open LLM Leaderboard scores on the card are general benchmarks, recorded as evaluation only. The specialty is general. The widget system line says "the healthcare and biomedical domain" and names no narrower field.

Serving is text only. The widget system prompt is "You are an expert and experienced from the healthcare and biomedical domain with extensive medical knowledge and practical experience." `generation_config.json` sets `do_sample` true, temperature 0.6, top_p 0.9, and max_length 4096. The example uses `max_new_tokens` 256. `max_position_embeddings` is 8192. The license is `apache-2.0`.

No paper names this repository. Inventory methods is empty, which matches the missing loss. Dataset `ruslanmv/ai-medical-dataset` and parent `meta-llama/Meta-Llama-3-8B-Instruct` match the card.
