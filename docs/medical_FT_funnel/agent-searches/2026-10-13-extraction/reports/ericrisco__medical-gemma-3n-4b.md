# ericrisco/medical-gemma-3n-4b

## Sources

- https://huggingface.co/ericrisco/medical-gemma-3n-4b/raw/main/README.md — current model card; same text as the cached card
- /home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/ericrisco__medical-gemma-3n-4b__2026-10-10.md — cached card
- https://huggingface.co/api/models/ericrisco/medical-gemma-3n-4b — file list, chat template, parameter count
- https://huggingface.co/ericrisco/medical-gemma-3n-4b/raw/main/config.json — Gemma3n text, vision, and audio config; context 32768
- https://huggingface.co/ericrisco/medical-gemma-3n-4b/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/ericrisco/medical-gemma-3n-4b/raw/main/tokenizer_config.json — tokenizer; no default system prompt
- https://huggingface.co/ericrisco/medical-gemma-3n-4b/raw/main/chat_template.jinja — Gemma turn template
- https://github.com/ericrisco/medical-gemma-3n — training and deployment repository; the card link gemma3n-impact-challenge resolves here
- https://github.com/ericrisco/medical-gemma-3n/blob/main/training/README.md — LoRA rank, 4-bit load, one epoch, 5417 steps
- https://huggingface.co/datasets/ericrisco/medrescue — training set; viewer shows a train split of 86.7k rows
- https://huggingface.co/datasets/lextale/FirstAidInstructionsDataset — evaluation set named on the card; empty dataset card, viewer loads
- https://huggingface.co/spaces/ericrisco/medical-gemma-3n-4b — demo named in the GitHub README
- https://www.kaggle.com/competitions/google-gemma-3n-hackathon/overview — hackathon named in the GitHub README
- https://youtu.be/mnmY4Yc0Nag — presentation linked from GitHub

An arXiv search for this model name returned Google's MedGemma report (https://arxiv.org/abs/2507.05201). That paper does not name this repository.

## Record

The training set is `ericrisco/medrescue`. The card says the model "was trained on ericrisco/medrescue" and gives "86,667 medical Q&A pairs", "11 specialized medical datasets", "14 official medical PDFs", and "RAG-enhanced content using vector search and AI generation." The dataset viewer loads a train split of about 86.7k rows. The dataset card describes human medical datasets plus answers generated from those PDFs, so the mix is human and synthetic. English is the language tag on the model card.

The update is QLoRA, merged into this repository. The card says "Fine-tuning Method: LoRA (r=8, alpha=8, dropout=0)" and "Quantization: 4-bit loading for memory efficiency." The training README sets `load_in_4bit=True` and `full_finetuning=False`, rank 8, alpha 8, "Epochs: 1", "Training Steps: 5,417", learning rate 2e-5, and batch size "4 per device × 4 gradient accumulation = 16 effective." The card calls this repository the "Full merged model." No source names a loss. "Fine-tuned" is not an objective.

The parent is `unsloth/gemma-3n-E4B-it`. The card says "Base Model: unsloth/gemma-3n-E4B-it." The training README sets `source_model_name = "unsloth/gemma-3n-E4B-it"`. The card states "7.8B parameters."

The use claim is strong, and the warning is a disclaimer. The card says the model is "designed to provide accurate medical guidance in emergency scenarios" and titles it an "Emergency Medical Assistant." It also says "Not a substitute for professional medical advice" and "For research and educational purposes only." Those sentences do not forbid a use.

The purpose is stated. The same sentence says what it is for: accurate medical guidance when connectivity is limited. Audiences named on the card are people in those emergency scenarios, and "healthcare students" ("Training support for healthcare students").

The card claims medical questions, first aid ("Step-by-step emergency procedures"), triage ("Initial triage and severity evaluation"), drug information ("Medication guidance and contraindications"), treatment ("How do I treat severe bleeding?"), clinical reasoning and differential diagnosis, teaching, clinical decision support, telemedicine consultation, and disaster response ("Medical care in resource-limited settings").

The medical work is question answering, licensing-exam questions in the training mix, differential diagnosis, triage, treatment and medication advice, conversation, and disaster response. First-aid accuracy on `lextale/FirstAidInstructionsDataset` is an evaluation: 71.54% (93/130) versus 36.15% (47/130) for the base model. The specialty words are "emergency medical assistance" and "first aid."

The published example is a text question, "What should I do if someone is having a heart attack?", and the reply is ordinary chat text. A chat template is in the repository. `generation_config.json` sets `do_sample`, `top_k` 64, and `top_p` 0.95. The card example uses temperature 0.7 and `max_new_tokens` 512. Context length in `config.json` is 32768. The architecture file also has vision and audio blocks. This repository does not set a system prompt.
