# khazarai/Medical-QA

## Sources

- https://huggingface.co/khazarai/Medical-QA/raw/main/README.md — current model card; same text as the cache
- https://huggingface.co/api/models/khazarai/Medical-QA — file list, parameter count, chat template
- https://huggingface.co/khazarai/Medical-QA/raw/main/config.json — Qwen3ForCausalLM, context 40960, unsloth_fixed
- https://huggingface.co/khazarai/Medical-QA/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/datasets/medalpaca/medical_meadow_medical_flashcards — dataset card; GPT-3.5 rephrased Anki cards
- https://arxiv.org/html/2304.08247v3 — MedAlpaca paper; flashcard set is 33,955 rows; does not name this repository
- https://huggingface.co/Rustamshry/Medical-QA-GGUF — GGUF copy that repeats this card
- https://featherless.ai/models/khazarai/Medical-QA — inference host page that prints this repository id

## Record

The card trains on `medalpaca/medical_meadow_medical_flashcards` and says it used 34,000 question-answer pairs. The dataset card says the Anki Medical Curriculum flashcards were "created and updated by medical students" and then "we utilized OpenAI's GPT-3.5-turbo to rephrase the cards". Provenance is mixed. The MedAlpaca paper's table lists 33,955 flashcard pairs. The dataset page loads and shows about 34,000 rows. The card says the language is English. The flashcards "cover the entire medical curriculum", including anatomy, physiology, pathology, pharmacology, and clinical knowledge and skills.

The YAML tag is `sft`. The prose says "fine-tuned" and does not say full fine-tuning or LoRA. There is no `adapter_config.json`. The upload is one bfloat16 `model.safetensors` of 596,049,920 parameters. Epochs, learning rate, and batch size are absent. `config.json` has `unsloth_fixed: true`. That flag is not a training-method sentence.

The YAML parent is `unsloth/Qwen3-0.6B`. The prose says "a fine-tuned version of Qwen3-0.6B". Those name the same parent. The Hub API count is 596,049,920 bfloat16 parameters, which is the 0.6B size the card names.

The purpose sentence is: "It is designed to assist with medical education and exam preparation, offering concise and contextually relevant answers to short medical questions." The audience is students. The use claim is Moderate: exam and study use, not clinical advice. The warning is an explicit prohibition: "Should not be relied upon for actual patient care, treatment decisions, or emergency use." The card also says it is "Not intended for real-world clinical decision-making or replacing professional medical advice."

Functions are answering medical questions, answering exam questions, and supporting study or teaching. The output is a chatbot reply, described as "short and exam-style". The tasks are medical QA and exam answering. The specialty is general: "Domain: Medicine & Medical Education". No evaluation score is reported. The YAML licence is `apache-2.0`. The model-details line says MIT.

Serving is text only. The example asks a text question, "What can β-blockers cause or exacerbate due to excessive AV nodal inhibition?", with system prompt "Answer this question truthfully". A chat template is present. The example sets temperature 0.7, top_p 0.8, top_k 20, and max_new_tokens 512. `generation_config.json` sets temperature 0.6, top_p 0.95, top_k 20, and do_sample true. `max_position_embeddings` is 40960.
