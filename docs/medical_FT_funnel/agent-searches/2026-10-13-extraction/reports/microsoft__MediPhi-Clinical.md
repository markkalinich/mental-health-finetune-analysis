# microsoft/MediPhi-Clinical

## Sources

- https://huggingface.co/microsoft/MediPhi-Clinical/raw/main/README.md — current model card; identical to the cached card (sha256 4613dabc86a627013c725960a24cfd26acc547fae7971cdad79c4ea21f0f93ee)
- https://huggingface.co/api/models/microsoft/MediPhi-Clinical — file list, 3,821,079,552 bfloat16 parameters, two Spaces
- https://huggingface.co/microsoft/MediPhi-Clinical/raw/main/config.json — Phi-3 config, context 131072
- https://huggingface.co/microsoft/MediPhi-Clinical/raw/main/generation_config.json — token ids only
- https://huggingface.co/microsoft/MediPhi-Clinical/raw/main/tokenizer_config.json — chat template
- https://arxiv.org/abs/2505.10717 — ACL 2025 abstract for the MediPhi collection
- https://arxiv.org/html/2505.10717 — HTML full text of that paper
- https://aclanthology.org/2025.acl-long.950/ — ACL anthology page
- https://arxiv.org/abs/2507.05517 — speech-transcript extraction paper; names MediPhi-Instruct, not this repo id
- https://arxiv.org/html/2507.05517 — HTML of that paper
- https://arxiv.org/abs/2507.07248 — MedRiskEval abstract
- https://arxiv.org/html/2507.07248 — HTML; calls this expert MP-Clinical and lists a 25% SLERP coefficient
- https://arxiv.org/abs/2407.13833 — Phi-3 safety post-training; does not name this repo
- https://huggingface.co/collections/microsoft/mediphi — collection page
- https://huggingface.co/datasets/zhengyun21/PMC-Patients — patient-summary dataset card; viewer does not load
- https://huggingface.co/datasets/starmpcc/Asclepius-Synthetic-Clinical-Notes — synthetic clinical-note dataset card; viewer loads, 158,114 rows
- https://huggingface.co/datasets/akemiH/NoteChat — NoteChat dataset card; viewer loads, 207,001 rows
- https://huggingface.co/datasets/tchebonenko/MedicalTranscriptions — Hub copy of mtsamples.com transcriptions; viewer loads, 4,999 rows, English
- https://mtsamples.com/ — site the paper cites for MTSamples
- https://github.com/pytorch/pytorch — library linked from the card
- https://github.com/huggingface/transformers — library linked from the card
- https://github.com/HazyResearch/flash-attention — library linked from the card
- https://huggingface.co/spaces/Calistusmwonga/ai-first-aid-chatbot — Space the Hub API lists for this repo
- https://huggingface.co/spaces/dogoodson/Project1Demo — Space the Hub API lists for this repo

## Record

The clinical corpus is four sources. The card names `zhengyun21/PMC-Patients`, `akemiH/NoteChat`, and `starmpcc/Asclepius-Synthetic-Clinical-Notes`, plus “mtsamples”, and says it kept “only commercial-friendly licenses across all three datasets.” The paper’s clinical table lists PMC-Patients at 156k patient summaries, Asclepius at 80k clinical documents, NoteChat at 80k conversations, and MTSamples at 5k clinical documents. The paper calls PMC-Patients a commercial-friendly subset of case reports, and calls Asclepius and NoteChat synthetic derivatives. The Hub Asclepius card says the notes were synthesized with GPT-3.5 and that the file has instruction-answer pairs for 157k synthetic discharge summaries; the viewer loads 158,114 English rows under CC-BY-NC-SA-4.0. NoteChat’s card is only a citation for “A Dataset of Synthetic Doctor-Patient Conversations Conditioned on Clinical Notes”; the viewer loads 207,001 rows and does not state a language. PMC-Patients’ card says 167k patient summaries extracted from PubMed Central case reports, English, CC-BY-NC-SA-4.0, and a later file of 250,294 patients; the datasets server fails to build that config, so it does not load in the viewer. MTSamples is the public site https://mtsamples.com/. The paper says it is “a public database filled with various de-identified clinical documents.” A Hub copy, `tchebonenko/MedicalTranscriptions`, says “Medical transcription data scraped from mtsamples.com,” is English, and loads 4,999 rows. That card’s specialty list is its own note about “the model training”; it does not name MediPhi.

This checkpoint was trained by continual pre-training, then merged. The card says “This model is MediPhi-Clinical obtained by merging the fine-tuned Clinical expert with the SLERP technique into its base model at 25%,” and the training-data heading is “Continual Pre-training.” The paper puts the five experts, including Clinical, in step 1, “continual pre-training,” using pre-instruction tuning, and puts supervised fine-tuning and direct preference optimization in step 2, which produces MediPhi-Instruct. A footnote says pre-instruction tuning “does not involve explicit instruction data or chat-style formatting.” For the non-PubMed experts the paper says each expert is trained in two phases: one epoch on generated task outputs at a peak learning rate of 1e-4, then two epochs on the task text concatenated with the original documents at a peak learning rate of 3e-4. It says the rest of the paper uses pre-instruction tuning with summaries. Table 6 is labeled “Hyperparameters for CPT excluding PIT,” so its batch size of 16 per GPU is not the Clinical expert’s batch size. No sentence says LoRA, QLoRA, or a full-weight update. The repo has two full bfloat16 weight files and no `adapter_config.json`. MedRiskEval’s appendix table lists MP-Clinical at a SLERP coefficient of 25% with Phi-3.5-mini-instruct, the same proportion as the card.

The parent is `microsoft/Phi-3.5-mini-instruct`. The card YAML and the line “Finetuned from model” say that. The paper says the experts start from Phi-3.5 mini. The card says the collection has 3.8B parameters. The Hub file list totals 3,821,079,552 bfloat16 parameters. Language is English: “Language(s) (NLP): English.”

The use claim is moderate. The card says “The model is intended for research use in English, especially clinical natural language processing,” and the worked example extracts keywords from an operative note. It does not say the model gives a diagnosis, a treatment, or medical advice. The warning is a disclaimer only. The card says “It should be used for research purposes, i.e., in benchmarking context or with expert user verification of the outputs.” It does not say the model must not be used for diagnosis or treatment. A later paragraph says health advice is a high-risk scenario that needs application-level safeguards.

The purpose is stated. The same sentence says the model is for research in clinical natural language processing. The audience named is researchers or developers: “Researchers (or developers) should consider common limitations of language models as they select use cases.” The red-teaming paragraph mentions clinician and patient queries as an evaluation setup, not as the people the model is for.

The function the card demonstrates is extracting structured clinical data. The system line in the example is “Extract medical keywords from this operative notes focus on anatomical, pathological, or procedural vocabulary,” and the printed output is “gallbladder stones, wall thickening, peritoneal fluid.”

The clinical task in that example is information extraction. The CLUE+ table is evaluation: ICD10CM, SDoH, and MeDiSumCode are coding or extraction scores; MedicationQA and RRS QA are question-answering scores; MeQSum, MeDiSumQA, and ACI are summarisation scores. The card also says a later paper “demonstrated good performances on clinical information extraction task.” The specialty is general. The card says the models are “specialized in the medical and clinical domains” and does not name a field such as surgery or radiology. The operative-note example is one document, not a specialty claim.

Serving is text in, text out. The example user message is an operative report. A chat template is in `tokenizer_config.json`, and `use_default_system_prompt` is false. The example system string is the keyword-extraction instruction above. The card’s generation example uses `max_new_tokens` 500, `temperature` 0.0, and `do_sample` false. `generation_config.json` does not set those. Context length is 131,072 tokens in `config.json`; the card says 128K. The output is a short assistant reply, not a label or a JSON object. The card presents the model as a clinical NLP tool with a chat prompt, not as a person one talks with, so the output type is other.

No training GitHub repository names this checkpoint. The card’s GitHub links are PyTorch, Transformers, and Flash-Attention. The main paper does not print `microsoft/MediPhi-Clinical`. It describes the Clinical expert. MedRiskEval calls that expert MP-Clinical. The speech-transcript paper names MediPhi-Instruct. Inventory methods `dpo|sft` belong to that other checkpoint. The parent matches. The three Hub dataset ids match the card YAML; mtsamples is extra.
