# No dataset at step 2, pilot batch 4

Checked 2026-10-08. A dataset is recorded only when a paper, training script, dataset card, or the current model card names a training corpus and is about this repository.

## MMahd/Llama-2-7b-chat-therapist

The cached card `MMahd__Llama-2-7b-chat-therapist__2026-10-05.md` has no card text. The live README at https://huggingface.co/MMahd/Llama-2-7b-chat-therapist/raw/main/README.md returns 404. The Hub API lists no `cardData` and no `datasets` tag. The account name on the Hub is Mahd. Mahd has no GitHub repositories under `MMahd`. arXiv has no hit for `Llama-2-7b-chat-therapist`.

Mahd also uploaded `MMahd/Transformed-Dataset-Support` on 2024-06-08, the day before this model. Its README is only the automatic feature list. It does not say the file was used to train this checkpoint.

No paper, training script, or dataset card names a training corpus for this repository.

https://huggingface.co/MMahd/Llama-2-7b-chat-therapist

## Moriacrafter/Qwen1.5-1.8B-8bit_DepressionDetection

The newest cached card, dated 2026-10-05, matches the live README. It is the automatic Hub template. Under Training Data it says more information needed. `cardData` has no dataset. The `arxiv:1910.09700` tag is the Lacoste carbon-emissions paper linked from that template, not a paper about this checkpoint.

The account name is Moria Li. arXiv has no paper by Moria Li on depression. The GitHub repo `Moriacrafter/Capstone` is a title only. Moria Li has five datasets, including `Moriacrafter/DepressionDetection_json` and `Moriacrafter/DepressionDetection_Reddit_Train`. None of those dataset cards name this model. Other checkpoints from the same account have `Reddit` or `v2` in the repo name. Those are different models.

No source names a training corpus for this repository.

https://huggingface.co/Moriacrafter/Qwen1.5-1.8B-8bit_DepressionDetection

## noelabu/gemma-2b-instruct-ft-mental-health-conv

The newest cached card, dated 2026-10-05, matches the live README. It is the automatic Hub template. Training Data says more information needed. `cardData` has no dataset. The account name is Noela Jean Bunag. arXiv has no hit for this repo id.

The notebook repo https://github.com/noelabu/AIRepublic_Finetune_LLM_model does name a corpus. Its README says the dataset is `Amod/mental_health_counseling_conversations`, and the notebook sets `new_model = "gemma-2b-instruct-ft-mental-health-conv_v2"` and pushes that name. That is `noelabu/gemma-2b-instruct-ft-mental-health-conv_v2`, a different checkpoint uploaded later the same day. The notebook does not print this repository id.

No source names a training corpus for this repository.

https://github.com/noelabu/AIRepublic_Finetune_LLM_model

## pixelsandpointers/bert2bert-empathetic-dialogues

The cached card dated 2026-10-05 has no card text. The live README returns 404. The Hub API lists no `cardData` and no `datasets` tag. The account is Benjamin Beilharz. The old id `benjaminbeilharz/bert2bert-empathetic-dialogues` redirects to this repository. arXiv has no hit for the repo id. The Arabic BERT2BERT paper (Naous, Antoun, and Hajj, 2021) is about `tareknaous/bert2bert-empathetic-response-msa`, a different checkpoint.

Beilharz's thesis repo prints this checkpoint. The README at https://github.com/pixelsandpointers/ba-thesis/blob/master/readme.md lists "Bert2Bert Dialog Contextualizer" with the link https://huggingface.co/benjaminbeilharz/bert2bert-empathetic-dialogues. The sentence in that README that names a corpus is "GPT-2, T5 baselines trained on Empathetic Dialogues." That sentence is about the GPT-2 and T5 baselines. The separate T5 repo `pixelsandpointers/t5-empatheticdialogues` carries the tag `dataset:facebook/empathetic_dialogues`. This checkpoint does not.

The file `src/models/bert/b2b.py` loads `benjaminbeilharz/ed-for-lm`. That Hub dataset was created on 2022-03-13, the day after this checkpoint was uploaded, and its dataset card is empty. The same file's upload sentence still names `patrickvonplaten/bert2bert_cnn_daily_mail`, the CNN/DailyMail notebook this file was copied from, and `trainer.train()` is commented out. The thesis slides name Empathetic Dialogues for DialoGPT, not for this checkpoint.

No sentence names a training corpus for this repository.

https://github.com/pixelsandpointers/ba-thesis/blob/master/readme.md

## RamziRebai/llama-2-7b-therapist-v2

The cached card dated 2026-10-05 has no card text. The live README returns 404. The Hub API lists no `cardData` and no `datasets` tag. The account name is Ramzi Rebai. arXiv has no paper by Ramzi Rebai. `RamziRebai/finetuning_llama2` has an empty README and no other files.

The serving app https://github.com/RamziRebai/LLama-2-as-Therapist-GPU sets `model_id = "RamziRebai/llama-2-7b-therapist-v4"`. That is a different checkpoint. The README of that app does not name a training corpus.

No source names a training corpus for this repository.

https://huggingface.co/RamziRebai/llama-2-7b-therapist-v2
