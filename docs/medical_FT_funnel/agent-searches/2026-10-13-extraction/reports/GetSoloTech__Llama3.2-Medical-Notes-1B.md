# GetSoloTech/Llama3.2-Medical-Notes-1B

## Sources

- https://huggingface.co/GetSoloTech/Llama3.2-Medical-Notes-1B/raw/main/README.md — current model card; sha256 matches the cached card
- https://huggingface.co/api/models/GetSoloTech/Llama3.2-Medical-Notes-1B — file list and parameter total
- https://huggingface.co/GetSoloTech/Llama3.2-Medical-Notes-1B/raw/main/config.json — context length
- https://huggingface.co/GetSoloTech/Llama3.2-Medical-Notes-1B/raw/main/generation_config.json — sampling defaults
- https://huggingface.co/datasets/starfishdata/playground_endocronology_notes_1500 — training dataset page and README
- https://arxiv.org/abs/2507.03033 — paper linked from the card; HTML full text returned 404
- https://www.medrxiv.org/content/10.1101/2025.07.01.25330679v1 — the same preprint on medRxiv, linked from the card
- https://huggingface.co/spaces/Johnyquest7/medical-transcription-notes — space named in the paper's data-availability lines
- Cached card: revision_3_experiments/hf_inventory/cache/readmes/GetSoloTech__Llama3.2-Medical-Notes-1B__2026-10-10.md

## Record

The card names one dataset, starfishdata/playground_endocronology_notes_1500. That Hub dataset loads. Its README states a train split of 1,930 examples, with columns topic, transcript, and structured_note. It does not say whether the text is human or synthetic. The rows shown on the page are endocrinology visits. The dataset id says 1500. The split count is 1,930.

The update is LoRA. The card says "Fine-tuning Method: PEFT (Parameter-Efficient Fine-Tuning) using LoRA" and "Unsloth library for accelerated fine-tuning and merging." The repository has model.safetensors and no adapter file, so the adapter is treated as merged. The card does not name a loss. Rank, alpha, epochs, learning rate, and batch size are not stated. There is no statement that the base was quantized during training.

The card's parent is meta-llama/Llama-3.2-1B-Instruct. config.json does not repeat that id. The safetensors total is 1,235,814,400 parameters. Language is English.

The model turns a transcript into a structured note. "Input: Free-text medical transcripts (doctor-patient conversations or dictated notes). Output: Structured medical notes with clearly defined sections." That is a moderate medical use: note writing, not a doctor chatbot. No warning about diagnosis or treatment is on the card. The purpose is "generating structured SOAP notes." The input is a clinician's transcript or dictation.

It writes a clinical note, summarises the transcript, and fills named sections. The output is a note, not a chat reply. The task is clinical note generation. The card says "medical" and does not name a specialty. The system prompt in the example starts "Convert the following medical transcript to a structured medical note" and lists fifteen sections, including assessment and plan, using only what the transcript contains.

The example is text. A chat template is present. generation_config.json sets temperature 0.6 and top_p 0.9. The card's example uses temperature 0.2, top_p 0.85, top_k 20, and max_new_tokens 2048. Context length is 131,072 tokens. The license is apache-2.0. The card lists BERTScore, BLEURT, and ROUGE and gives no scores.

The linked paper, arXiv:2507.03033, does not print this repository id. Its data-availability lines name OnDeviceMedNotes/Medical_Summary_Notes and starfishdata/endocrinology_structured_notes_1500. Its training description is about that release. The inventory method, dataset id, and parent match this card. The loss is unnamed, and the paper points at different Hub ids.
