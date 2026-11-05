# What the 81 medical cards say the model is for

Source list: `revision_3_experiments/hf_inventory/results/medical/2026-10-10/kept.csv` (81 `hf_id`s).
Each card is the newest file under `revision_3_experiments/hf_inventory/cache/readmes/`.
Row-level coding is in `roles-survey.csv` in this folder.

A count below is a count of cards. One card can sit in several rows of the use table.

## (a) Cards found, and how many say what the model is for

81 of 81 cards were in the cache. None were fetched from the web.

57 cards have at least one sentence that says what the model is for.
24 cards do not.

Those 24 are:

- YAML only, no prose: `BLACKBUN/llama-2-13b-pubmed-qa-211k`, `BLACKBUN/llama-2-7b-pubmed-qa-211k`, `jassercherif/Llama-2-7b-doctorstr-finetuned`, `miike-ai/4o-3b-medical`.
- A trainer template whose only task sentence is "fine-tuned on [dataset]", with a non-medical time-machine prompt: `Alexossss/medicalia`, `ThxZ3US/Medicalia`, three `graliuce` MedMCQA runs, seven `mlxha` MedMCQA runs, `vinhnguyenxu/OpenR1-Distill-Qwen3-8B-Medical`.
- A stub or a log: `Dev9124/qwen2.5vl-medical-reasoning` (Unsloth upload note), `Fornit/DeepSeek-R1-Medical-COT-LORA` (GPU log), `Rishidar/autoscientist-healthcare-qlora` (competition dataset, no use), `SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it` (automatic template, "More Information Needed"), `iamaber/mistral-7b-pubmedqa-lora-plus` (scores only), `Team-Promptia/RLT-student-Qwen3-32B-medicine_biology` (Japanese note that it was fine-tuned, with no task).

56 of the 57 purpose sentences also name a thing the model does.
The exception is `tulas/gemma-3-270m-medical`: "This model is NOT intended for medical text generation but for testing purpose only."

## (b) What the cards say the model does

Phrases in `stated_uses` were merged when they were the same job in different words.
"Interpret a medical image" merges a caption ("describe a radiograph") and a visual question.
"Draft explanatory text" merges a clinician-reviewed explanation and educational material.
"Hospital-crisis operations" is one card that lists six control-room jobs.
"Extract structured clinical data" merges prescription JSON, note JSON, and keyword lists.

| Phrase | Cards |
|---|---:|
| answer medical questions | 28 |
| clinical reasoning | 22 |
| talk with a patient | 15 |
| answer exam questions | 12 |
| support a clinical decision | 10 |
| suggest a diagnosis | 10 |
| support study or teaching | 9 |
| give treatment advice | 7 |
| extract structured clinical data | 5 |
| interpret a medical image | 5 |
| search or summarise literature | 4 |
| triage symptoms | 3 |
| answer literature questions | 2 |
| write a clinical note | 2 |
| summarise a patient record | 2 |
| draft explanatory text | 2 |
| hospital-crisis operations | 1 |
| give first-aid instructions | 1 |
| give drug information | 1 |
| tag topics | 1 |
| judge sentiment | 1 |
| classify disaster reports | 1 |
| triage satellite images | 1 |
| classify emails | 1 |

The three rows at the bottom are not clinical. They are in this kept list because the model name or the search term was "triage".

## (c) More than one use

41 cards list more than one use. 15 list one. 25 list none (the 24 cards with no purpose sentence, plus `tulas`).

Examples, in the card's own words:

- `XformAI-india/Qwen3-1.7B-medicaldataset` (the 4B card repeats this): "designed to assist with medical Q&A, clinical documentation, and healthcare-related reasoning." The intended-use list then adds summarizing patient records, triage, and "Chatbot integration for healthcare support (non-diagnostic)."
- `ericrisco/medical-gemma-3n-4b`: "emergency medical assistance and offline healthcare applications," then first aid, symptom triage, drug information, clinical decision support, teaching, and a consultation ("What should I do if someone is having a heart attack?").
- `MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged` lists question answering, clinical decision support, named-entity recognition, "Clinical documentation assistance and literature synthesis (with physician review)," and a research baseline. The 1B and 3B cards in the same family do not list documentation, entity extraction, or literature synthesis.
- `naazimsnh02/medical-ministral-8b` lists patient education, clinical decision support, medical content generation, healthcare chatbots, and medical training.
- `EpistemeAI/Reasoning-Medical0.1-E4B-sft`: "Intended users: Researchers, students, developers, clinicians using human review." Uses named in the same card: study support, clinical reasoning, multiple-choice questions, literature review, and drafting an explanation a clinician reviews.
- `EpistemeAI/OpenMedResearch-Gemma-4E4N` stacks literature jobs and then refuses the clinical ones: "answer factual biomedical questions by reasoning over scientific literature rather than providing direct clinical advice."
- `balarajr/triage-hospital-agent` is one model for six agents: ER triage, ICU beds, pharmacy checks, staff rostering, EHR failure, and chief-medical-officer oversight.

## (d) Who the card says it is for

52 cards name no user.

29 cards name at least one. 17 of those 29 name more than one kind.
A card is counted once per kind it names.

| Kind | Cards that name it |
|---|---:|
| researcher | 20 |
| student | 12 |
| developer | 8 |
| clinician | 7 |
| patient | 5 |
| emergency operations center | 1 |

"Researcher" here includes a card that says the model is for research, not only a card that uses the word researcher.
A sentence that only says "educational and research purposes" as a warning, with no learner named, was not coded as a student. `AliFadel/DeepSeek-R1-Medical-O1-QA` is that case: "for research and educational purposes only," and a doctor is a supervisor, not the user.

Patients are rarely the named user. They show up when the card says patient questions, patient education, or a lay first-aid user: `Ghufran27/medical-llama2-7b`, `empirischtech/Llama-3.1-8B-Instruct-MedQA`, `ericrisco/medical-gemma-3n-4b`, `naazimsnh02/medical-ministral-8b`, `vsingh10/bitnet-medical-chat`.

Several cards that talk like a doctor never name the person on the other side. `ruslanmv/ai-medical-model-32bit` says "You are a Medical AI chatbot assistant" and "informational purposes only." `hudson5/llama-3-8b-chat-doctor` says only "A model used for medical chat, use it with caution!"

`is_chatbot` in the CSV is yes for 14, no for 22, unclear for 45.
Yes means the card says a person talks with it (chat, chatbot, doctor–patient replies, a consultation).
No means the card shows a label, JSON, a letter, a note, or a caption, and does not describe a conversation.
Unclear is the large middle: a chat template wrapped around one question, with no claim that a person converses.

## (e) How to structure `role`

Do not use one closed list. Do not use a single audience-by-function pair either.
`EpistemeAI/Reasoning-Medical0.1-E4B-sft` names four audiences and five jobs, and it does not say which person gets which job.

Use two multi-valued fields, plus a yes/no for whether the card says anything:

1. `purpose_stated` — yes or no. 24 of these 81 cards are no.
2. `audiences` — zero or more of: patient, clinician, student, researcher, developer. One free-text slot for a named group that is not in that list (the emergency operations center). Empty when nobody is named.
3. `functions` — zero or more of the phrases in the table in (b), minus the three non-clinical triage rows. Those three get `functions` empty and a separate `not_clinical` note, because the card is about satellite images, disaster reports, or email.

Candidate `functions` values, and only these, because the cards say them:

- answer medical questions
- answer exam questions
- answer literature questions
- clinical reasoning
- suggest a diagnosis
- give treatment advice
- talk with a patient
- write a clinical note
- summarise a patient record
- extract structured clinical data
- interpret a medical image
- search or summarise literature
- support study or teaching
- support a clinical decision
- give first-aid instructions
- give drug information
- triage symptoms
- hospital-crisis operations
- draft explanatory text
- tag topics
- judge sentiment

Keep output shape out of `role`. The same "answer exam questions" job is a letter on `aakthepaak/clinical-llm-r32` ("the concise single-letter answer") and a short completion on `Satya-Dey/qwen2.5-1.5b-medmcqa-qlora-v2`. Prescription reading is JSON. Notes are a headed document. If output matters, give it its own field.

Cards that this scheme still codes badly:

- The 24 cards with no purpose sentence. A MedMCQA dataset name is not a statement that the model answers exam questions. The template prompt is about a time machine. Leave `functions` empty.
- `tulas/gemma-3-270m-medical`. The purpose sentence is a refusal of medical use. Empty `functions`, `purpose_stated` yes.
- `doctoria/doctoria-rally-ai`. The job line is "wound-care & medical VQA for disconnected clinics in Morocco." The training set it names is VQA-RAD radiology, and the example is "Assess this wound." One function value cannot record that split. Code the stated job (interpret a medical image) and keep the clash in a note.
- `microsoft/MediPhi-PubMed`. The intended-use paragraph and the worked example (keywords from a cholecystectomy note) are the same text as `microsoft/MediPhi-Clinical`. The name says PubMed. The example says note extraction. Code the example, and do not invent a literature function the card does not state.
- `vsingh10/bitnet-medical-chat`. The title talks to a patient ("Hi! I am Dr. Bitsy"). The intended-use section then says the use is research on medical dialogue. Both values are real. A single audience would have to drop one.
- `empirischtech/Llama-3.1-8B-Instruct-MedQA` lists question answering, topic tagging, sentiment, decision support, and chatbots. The usage code loads `AutoModel` and does not generate text. The functions are what the card claims, not what the snippet runs.
- `bouthros/llama32_11b_vision_medical_finetune` and `siva317/llama32-vision-radiology-lora` share one card text, including the training log. They are two rows and one description.
- `Kerassy/Granite-4.1-3B-Medical_Reasoning` is headed "Qwen3.5-9B-Medical-Reasoning". The body is the Granite model. Code the body.
- `balarajr/triage-hospital-agent`. "Hospital-crisis operations" hides six jobs. If those jobs matter for the study, split that one value. Do not call it patient triage: the card's triage agent uses the START protocol inside a simulation, "for research and simulation purposes only."
