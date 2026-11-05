# Batch 13: how three medical models were trained

Cached cards read: newest README under `revision_3_experiments/hf_inventory/cache/readmes/` (2026-10-05). Inventory row: `revision_3_experiments/hf_inventory/results/medical/2026-10-06/kept.csv`. Hub file lists checked live on 7 Oct 2026, because the 2026-10-05 card cache marks both Medicalia repos `adapter: 0` while the live file list includes `adapter_config.json`.

The two Medicalia repositories are one student project and two training runs. They are not copies of each other's weights.

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Task trained for | Language | Matches inventory row |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Alexossss/medicalia | code (group notebook) | supervised fine-tuning, loss on the assistant reply only | LoRA, rank 16, alpha 32; 8-bit optimizer; not 4-bit weights. Merge push was skipped | Diseases_Symptoms: 320 train, 80 test, from 400 rows; text copied from medical websites | HuggingFaceTB/SmolLM2-135M-Instruct (instruction-tuned) | open answer: disease name and a treatment, given symptoms | en | partly |
| ThxZ3US/Medicalia | code (same notebook and README; his step counts are in his saved trainer file) | supervised fine-tuning | LoRA, rank 16, alpha 32; 8-bit optimizer. Same file layout as the other run | same dataset and split recipe | same base | same task | en | partly |
| oopere/SmolLM2-1.7B-ClinicalNER | code (book notebook) and dataset card | supervised fine-tuning | QLoRA, rank 8, alpha 16; card says the adapter was merged | clinical-ner-qdora: notebook run used 360 train and 40 test; synthetic notes | HuggingFaceTB/SmolLM2-1.7B-Instruct (instruction-tuned) | named-entity extraction written as one JSON object | en | partly |

## Are the two Medicalia repositories one project?

Yes. One GitHub project, two people, two uploads.

README at https://github.com/alexandredesbos/Medicalia says: "Groupe: Alexandre Desbos, Baptiste Griva" and "Medicalia est un modèle qui doit aider à la prédiction des maladies selon différents symptomes ou inversement." The training file is `TrainingMedicalia.ipynb`. The notebook's saved log says the Weights & Biases login was `alexandredsb-pro` in the entity `alexandredsb-pro-universit-savoie-mont-blanc`. That is the same entity as the link on the Alexossss card. The ThxZ3US card links `baptistegriva-universit-savoie-mont-blanc`. Both entity names contain Université Savoie Mont Blanc. Both Hub repos were created on 11 Feb 2025.

They are not the same weight file. `model.safetensors` is 269,060,552 bytes in both repos and in `HuggingFaceTB/SmolLM2-135M-Instruct`, but the file etags differ: Alexossss `8d0e65c2ec7fcd0807bda4da0b6c8283ddea06971f720d4911e030960f1b4881`, ThxZ3US `d3e06f8ad801b0777ae010d3762e5a051357109ffa497b2bbd74991b9e79702c`, base `5af571cbf074e6d21a03528d2330792e532ca608f24ac70a143f6b369968ab8c`. The adapter files are the same size, 7,404,368 bytes, and their etags also differ. The saved trainer files differ: Alexossss learning rate 0.002 and `max_steps` 300; ThxZ3US learning rate 2e-5 and `max_steps` 2000.

`Interface.py` in that GitHub repo loads `ThxZ3US/medicalia` and leaves `Alexossss/medicalia` commented. The live Hub id is `ThxZ3US/Medicalia`. The capital M is the id the Hub API returns.

A third repo, `Infomaniak-AI/smolLM2-135M-Instruct-structure-output`, was created on 10 Feb 2025. Its saved trainer file uses the same learning rate, `max_steps`, batch size, and LoRA settings as the committed notebook, and its `hub_model_id` is the Infomaniak id, not either Medicalia id. Its card names no dataset. It is the same notebook template, not a copy of either Medicalia weight file.

## 1. Alexossss/medicalia

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/Alexossss__medicalia__2026-10-05.md`. The card is the TRL template. It names this repo in the loading example.
- Training notebook: https://github.com/alexandredesbos/Medicalia/blob/main/TrainingMedicalia.ipynb . Sets `hub_model_id = "Alexossss/medicalia"`. The saved cell output records commit `97edb26c7234dd337778cec40f67eec8fc24a7fa`, which is the Hub `sha` of this repo. Commit message in that output: "End of training."
- README: https://github.com/alexandredesbos/Medicalia/blob/main/README.md . Names Alexandre Desbos and Baptiste Griva. Does not print this repo id.
- Saved trainer file: https://huggingface.co/Alexossss/medicalia/resolve/main/training_args.bin . Unpickles as `trl.trainer.sft_config.SFTConfig`. `hub_model_id` is `Alexossss/medicalia`.
- Adapter file: https://huggingface.co/Alexossss/medicalia/raw/main/adapter_config.json .
- Dataset card: https://huggingface.co/datasets/QuyenAnhDE/Diseases_Symptoms . Row count from the datasets-server size API: 400.
- No paper, thesis, or blog was found that names this repo. The two WandB run pages return a login shell and do not show metrics.

### Training record

**(a) Objective.** Supervised fine-tuning. Card says: "This model was trained with SFT." The notebook builds an `SFTTrainer` with `SFTConfig` and calls `trainer.train()`. The loss is limited to the assistant reply: the notebook builds `DataCollatorForCompletionOnlyLM` with `response_template = "<|im_start|>assistant\n"`. That is still next-token training on the labeled reply. The saved config object has `do_train=False`. The notebook calls `trainer.train()`, and the Hub commit message is "End of training."

**(b) Parameter-update scope.** LoRA. Notebook says `LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05, target_modules=['o_proj', 'k_proj', 'q_proj', "v_proj"], bias="none", task_type="CAUSAL_LM")`. The adapter file says the same rank, alpha, dropout, and modules, and `use_dora` is false. The model is loaded with `AutoModelForCausalLM.from_pretrained` and no 4-bit config. `bitsandbytes` is installed, and the optimizer string is `paged_adamw_8bit`. That is an 8-bit optimizer, not a 4-bit base model, so this is not QLoRA.

The notebook then calls `merge_and_unload()` and `model.push_to_hub(hub_model_id)`. The saved output of that push is: "No files have been modified since last commit. Skipping to prevent empty commit." The Hub `sha` is the earlier "End of training" commit. The repo still contains `adapter_model.safetensors` and `adapter_config.json`, and it does not contain `final_merged_checkpoint`. The adapter was not merged into the files that commit uploaded.

**(c) Training data.** Notebook: `dataset_name = "QuyenAnhDE/Diseases_Symptoms"`, then `train_test_split(test_size=0.2, seed=42)`. The saved output of the train split is `num_rows: 320`. The eval map in the same notebook is over 80 rows. 320 + 80 = 400, which is the Hub row count. Dataset card says: "The data was sourced from various medical websites accessible through Google search." Columns are `Code`, `Name`, `Symptoms`, `Treatments`. Row 0 is English: Name "Panic disorder", Symptoms "Palpitations, Sweating, Trembling, Shortness of breath, Fear of losing control, Dizziness". The card does not name a language tag. The rows are copied from websites. They are not labeled as synthetic, and no generator model is named.

The formatting function sets the user text to `Symptoms: {Symptoms}` and the assistant text to `You may have {Name} You can use this treatment: {Treatments}`. The system string is "You are are an expert in generate json structure based on user query and schema." The assistant text is that sentence, not a JSON object. A markdown cell links `ChristianAzinn/json-training`. The load call uses `QuyenAnhDE/Diseases_Symptoms`.

**(d) Base model.** Notebook and card: `HuggingFaceTB/SmolLM2-135M-Instruct`. The base card says the instruct checkpoint was trained with supervised fine-tuning and then Direct Preference Optimization. It is the instruction-tuned checkpoint.

**(e) Hyperparameters.** The notebook sets `per_device_train_batch_size=2`, `gradient_accumulation_steps=4`, `warmup_steps=100`, `max_steps=300`, `learning_rate=0.002`, `lr_scheduler_type="cosine"`, `weight_decay=0.01`, `bf16=True`, `optim="paged_adamw_8bit"`, `seed=42`, `eval_steps=150`, `save_steps=31`. It does not set `num_train_epochs`. The saved `SFTConfig` has `num_train_epochs=3.0` and `max_steps=300`. README says training was on Google Colab. No GPU name is stated. The card lists PyTorch `2.5.1+cu124`.

**(f) Evaluation.** The trainer evaluates every 150 steps. No score is printed in the README or the card. The notebook's last cell prints one sample. The user text is "I have fever and cough, what disease might I have?" The printed reply talks about antifungal medication. That is one sample, not a scored test.

**(g) Task and language.** README: the model should help predict a disease from symptoms, or the reverse. The formatting function trains only the first direction: symptoms in, disease name and a treatment out. That is open medical question answering. The training strings are English.

### Discrepancies

1. Inventory `methods` is `sft` only. The notebook and `adapter_config.json` say LoRA. The 2026-10-05 card-cache flag string is `{'adapter': 0, ...}` even though the adapter files are in the repo.
2. The system prompt says the model generates JSON. The assistant target is the sentence "You may have {Name} You can use this treatment: {Treatments}".
3. The notebook merges the adapter and pushes again. That second push was skipped. The Hub commit is the pre-merge "End of training" commit.
4. Saved `SFTConfig` has `do_train=False`. The notebook calls `trainer.train()`.

### Confidence

High. The notebook names this repo id, its saved commit hash is the Hub `sha`, and the learning rate and `max_steps` in the notebook match the saved trainer file.

### Queries tried

- `Alexossss/medicalia SmolLM2 Diseases_Symptoms fine-tune`
- `"alexandredsb" OR "baptistegriva" Medicalia OR medicalia SmolLM huggingface`
- `QuyenAnhDE/Diseases_Symptoms dataset Hugging Face symptoms disease`
- `"medicalia" SmolLM2 OR "Diseases_Symptoms" fine-tuning Université Savoie`
- `"SmolLM2-135M-Instruct-structure-output" OR "structure-output" Diseases_Symptoms SFT`
- GitHub repository search `medicalia`, which returned `alexandredesbos/Medicalia`
- GitHub user search `Alexossss` (user `alexossss1` has no public repositories)
- WandB run `em5dufak` (login page only)
- Hugging Face file list and `training_args.bin` for this repo
- `Infomaniak-AI/smolLM2-135M-Instruct-structure-output` trainer file, compared with this run

## 2. ThxZ3US/Medicalia

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/ThxZ3US__Medicalia__2026-10-05.md`. Same TRL template as the other card, with this repo id in the loading example and a different WandB run.
- Same README and notebook as section 1. The notebook's `hub_model_id` line is `Alexossss/medicalia`. `Interface.py` loads `ThxZ3US/medicalia`.
- Saved trainer file: https://huggingface.co/ThxZ3US/Medicalia/resolve/main/training_args.bin . `hub_model_id` is `ThxZ3US/Medicalia`.
- Adapter file: https://huggingface.co/ThxZ3US/Medicalia/raw/main/adapter_config.json .
- No paper was found. His WandB run page is a login shell. GitHub user search for `ThxZ3US` returned no user. Baptiste Griva's public GitHub (`BaptGrv`) does not contain this training notebook.

### Training record

**(a) Objective.** Supervised fine-tuning. Card says: "This model was trained with SFT." The saved file is an `SFTConfig` with `dataset_text_field='text'`, the same class as the other run. The shared notebook is the only script found, and it uses `SFTTrainer` and `DataCollatorForCompletionOnlyLM`. That script's `hub_model_id` is the other repo. His file does not by itself name the collator.

**(b) Parameter-update scope.** LoRA. Adapter file: `r` 16, `lora_alpha` 32, `lora_dropout` 0.05, `target_modules` `q_proj`, `o_proj`, `v_proj`, `k_proj`, `use_dora` false, `task_type` `CAUSAL_LM`. The saved config uses `paged_adamw_8bit` and `bf16=True`. No 4-bit setting is in the adapter file or the saved config. The repo contains `adapter_model.safetensors` and `model.safetensors`, and it does not contain `final_merged_checkpoint`. The shared notebook's merge push was skipped on the run that was saved in the notebook, which is Alexandre's run. Whether Baptiste ran the merge cell is not stated in a log. The adapter file is still in this repo.

**(c) Training data.** Card YAML: `QuyenAnhDE/Diseases_Symptoms`. The shared notebook loads that dataset and splits it 80/20 with seed 42, which the saved output shows as 320 train rows and an 80-row eval map. The README says this is the dataset the group used. His trainer file does not store the dataset id. Provenance and language are the same as section 1: English rows copied from medical websites. The formatting function in the shared notebook is the symptom prompt and the "You may have {Name}" reply.

**(d) Base model.** Card, adapter file, and saved config `output_dir`: `HuggingFaceTB/SmolLM2-135M-Instruct`. Instruction-tuned, as in section 1.

**(e) Hyperparameters.** His saved `SFTConfig`, which does not match the numbers in the committed notebook: `learning_rate=2e-05`, `max_steps=2000`, `per_device_train_batch_size=2`, `gradient_accumulation_steps=8`, `warmup_steps=100`, `num_train_epochs=3.0`, `lr_scheduler_type` cosine, `weight_decay=0.01`, `bf16=True`, `optim` `paged_adamw_8bit`, `seed=42`, `eval_steps=500`, `save_steps=500`, `save_total_limit=6`. Log directory: `./SmolLM2-135M-Instruct-structure-output/runs/Feb11_13-04-17_53b76662441c`. README says they varied the learning rate and tried long runs, and that the learning rate was the change that mattered. It does not print 2e-5 or 2000. Hardware: the README says Google Colab for the project. No GPU name is on this card. The card lists the same PyTorch build as the other card, `2.5.1+cu124`.

**(f) Evaluation.** Not stated anywhere found for this repo. The saved config has `do_eval=True` and `eval_steps=500`. No score is printed.

**(g) Task and language.** Same project statement as section 1: predict a disease from symptoms, or the reverse. The only formatting function found trains symptoms to a disease name and a treatment, in English.

### Discrepancies

1. The committed notebook sets `learning_rate=0.002`, `max_steps=300`, and `gradient_accumulation_steps=4`, and sets `hub_model_id` to `Alexossss/medicalia`. This repo's saved trainer file has learning rate 2e-5, `max_steps` 2000, gradient accumulation 8, and `hub_model_id` `ThxZ3US/Medicalia`.
2. `Interface.py` loads `ThxZ3US/medicalia`. The Hub id is `ThxZ3US/Medicalia`.
3. Inventory `methods` is `sft` only. The adapter file says LoRA.
4. The two cards use the same TRL wording. The weight-file etags and the trainer files are different, so the second card is not a copy of the first upload.

### Confidence

Medium. The README, the WandB entity on the card, and `Interface.py` put this repo in the same two-person project. The committed notebook does not contain his learning rate or his repo id. Those are in his saved trainer file.

### Queries tried

- `ThxZ3US/Medicalia SmolLM2 Baptiste Griva`
- `"Alexossss" OR "ThxZ3US" OR "alexandredsb-pro" medicalia OR Diseases_Symptoms`
- `wandb alexandredsb-pro-universit-savoie-mont-blanc medicalia OR "baptistegriva" SmolLM`
- GitHub user `BaptGrv` and GitHub user search `ThxZ3US`
- `TrainingMedicalia.ipynb` and `Interface.py` in `alexandredesbos/Medicalia`
- Hugging Face file list and `training_args.bin` for this repo
- `Infomaniak-AI/smolLM2-135M-Instruct-structure-output` (same output-directory string, different `hub_model_id`)
- Scholar-style query `"medicalia" SmolLM2 OR "Diseases_Symptoms" fine-tuning Université Savoie` (no paper)

## 3. oopere/SmolLM2-1.7B-ClinicalNER

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/oopere__SmolLM2-1.7B-ClinicalNER__2026-10-05.md`. Author on the citation: Pere Martra. The card names this repo id.
- Notebook: https://github.com/peremartra/Rearchitecting-LLMs/blob/main/CH07/CH07_NB02_L4_QLoRA_QDoRA.ipynb . Does not print `oopere/SmolLM2-1.7B-ClinicalNER`. Header: "Colab Environment: GPU L4."
- Dataset card: https://huggingface.co/datasets/oopere/clinical-ner-qdora . Does not print this model repo id. It points at the notebook.
- Book chapter outline: https://livebook.manning.com/book/rearchitecting-llms/chapter-7 . Chapter title "Model specialization." The public page is a table of contents, not the training section. No arXiv or PubMed paper was found for this checkpoint.
- LinkedIn post by Pere Martra, 11 Jun 2026: https://www.linkedin.com/posts/pere-martra_llms-machinelearning-rearchitectingllms-activity-7470847065640738816-JN92 . Does not print this repo id.

### Training record

**(a) Objective.** Supervised fine-tuning. The notebook imports `SFTTrainer` and `SFTConfig` and calls `trainer.train()` for the QLoRA block and again for the QDoRA block. Each training string is a chat: system `Extract:`, user the clinical note, assistant the JSON label. That is next-token training on the JSON reply. The card says "QLoRA fine-tuned" and does not print the word SFT. The notebook's trainer class is the statement that the loss is supervised fine-tuning.

**(b) Parameter-update scope.** QLoRA for the checkpoint the card calls this model. Notebook: `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16, bnb_4bit_use_double_quant=True)` and `LoraConfig` with `use_dora=False`, `r=8`, `lora_alpha=16`, `lora_dropout=0.05`, targets `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`. Card table: the same rank, alpha, modules, NF4, and double quantization. A second block sets `use_dora=True` with the same rank and alpha. That block is QDoRA. The card says this upload is the QLoRA model, not the QDoRA model.

Card says the demonstrated workflow is "Train → Merge → Upload → Verify" and "Fine-tuning permanently absorbed the 15-line prompt into the model weights." The Hub file list has `model.safetensors` and no `adapter_config.json`. That file is 3,422,777,952 bytes, the same size as `HuggingFaceTB/SmolLM2-1.7B-Instruct`, with a different etag (`811fd1aa79182a2e664638fee6b24641e2ad7a51db8a0d3ec525d1763279cda1` versus the base etag `f55217be716b6a997b97b9d8d7eb6fad02e00858f5010ec24f64603c3a98a0e8`). The notebook's only `merge_and_unload()` runs after the QDoRA block and saves `./qdora_merged`. It does not call `push_to_hub` and does not name this repo.

**(c) Training data.** Card and notebook: `oopere/clinical-ner-qdora`. The notebook output says "Train samples : 360" and "Test samples : 40". Train category counts in that output: clean 92, abbreviations 74, implicit 73, typos 63, irrelevant 58. Those sum to 360. Dataset card: "This dataset was synthetically generated a combination of diferent LLMs via LiteLLM. All samples were automatically validated against the schema before inclusion. No real patient data was used." The generator model names are not stated. Language tag on the dataset card: `en`. The card's category table is 400 rows in total (clean 100, abbreviations 80, implicit 80, typos 70, irrelevant 70). Train plus the 40 test rows accounts for that table: the test counts printed in the notebook are clean 8, abbreviations 6, implicit 7, typos 7, irrelevant 12.

The model card says "Train samples: 200 (40 per category)." That count is not what the notebook printed and not what the datasets-server size API returns (360 train, 40 test).

**(d) Base model.** Card and notebook: `HuggingFaceTB/SmolLM2-1.7B-Instruct`. The base card says that instruct checkpoint was trained with supervised fine-tuning and then Direct Preference Optimization. It is the instruction-tuned checkpoint.

**(e) Hyperparameters.** Notebook constants, also printed on the card: 3 epochs, learning rate 2e-4, batch size 8, cosine schedule, max length 512, bfloat16 compute. The notebook also sets `gradient_accumulation_steps=1` and `warmup_steps=7` for both the QLoRA and the QDoRA trainers. Card hardware line: "GPU: NVIDIA L4 (Google Colab)." The notebook output prints "GPU memory available: 23.7 GB".

**(f) Evaluation.** The quantity they score is schema compliance: the reply parses as JSON and has the keys and types in the schema. It is not a token-level named-entity score.

Saved notebook output, minimal prompt `Extract:`: baseline with the 15-line prompt 87.5%; QLoRA 100.0%; QDoRA 100.0%, on the 40-row test split. The same notebook has a markdown table that says SmolLM2-1.7B QLoRA 95.0% and QDoRA 97.5%. The model card prints 95.0% for "SmolLM2-1.7B QLoRA (this model)". The dataset card prints 100.0% for QLoRA and for QDoRA. The LinkedIn post says 100% after QLoRA on 400 synthetic samples, and 85% for the long prompt.

The notebook also prints lm-eval numbers under the headings "QLoRA benchmark results" and "QDoRA benchmark results": QLoRA arc_easy accuracy 0.6048, winogrande 0.6425, hellaswag accuracy 0.5159, lambada_openai accuracy 0.5806, piqa accuracy 0.7541. The log line above those numbers says `Starting lm-eval on model 'HuggingFaceTB/SmolLM2-1.7B-Instruct'`. The QDoRA block prints a second set (arc_easy 0.6006, winogrande 0.6464, hellaswag 0.5162, lambada_openai 0.5791, piqa 0.7557) with the same base-model log line.

**(g) Task and language.** The card calls the task clinical named-entity recognition. The dataset card says this is not token labeling: "Unlike traditional Named Entity Recognition (NER) which focuses on labeling tokens in a sequence, this dataset targets Generative Information Extraction." What the model is trained to print is one JSON object:

- `patient_age`: integer or null
- `symptoms`: list of strings
- `vital_signs`: `temperature` (float or null), `heart_rate` (integer or null), `blood_pressure` (string or null)
- `medications`: list of objects with `name`, `dose`, and `frequency`
- `duration_days`: integer or null

A training row labeled `typos` shows the note "pt is 45 y.o male came in complainig of rly bad cogh and fevr..." and the label `{"patient_age": 45, "symptoms": ["cough", "fever", "weakness"], ...}`. The prompt the training strings use is the two-word system text `Extract:`. Language of the notes and of the dataset tag: English. The card says the model is educational and "Not intended for clinical or production use."

### Discrepancies

1. Model card: 200 train rows and 95.0% schema compliance. Notebook output and the datasets-server size API: 360 train rows and 40 test rows. That same notebook output: 100.0% for QLoRA and for QDoRA. A markdown table in the notebook says 95.0% and 97.5%. The dataset card says 100.0% and 100.0%. The LinkedIn post says 100% and a baseline of 85%, while the notebook output says 87.5% for the 15-line prompt.
2. The card says this upload is the QLoRA model and that the adapter was merged. The notebook merges the QDoRA model, saves it locally as `./qdora_merged`, and does not name this repo id.
3. Inventory `methods` is `qlora`, which matches the card. It does not record that the trainer is `SFTTrainer`. Inventory `datasets` is `oopere/clinical-ner-qdora`, which matches.

### Confidence

Medium. The card, the dataset card, and the notebook agree that this is a QLoRA supervised fine-tune of SmolLM2-1.7B-Instruct on `oopere/clinical-ner-qdora` for JSON extraction. They do not agree on the score, the training-row count, or which of the two adapters was merged and uploaded.

### Queries tried

- `oopere SmolLM2-1.7B-ClinicalNER QLoRA Pere Martra`
- `"clinical-ner-qdora" OR "SmolLM2-1.7B-ClinicalNER" Martra schema compliance`
- `peremartra CH07_NB02_L4_QLoRA_QDoRA SmolLM2-1.7B-ClinicalNER merge`
- `"Rearchitecting LLMs" Pere Martra clinical NER QLoRA schema compliance SmolLM2`
- Chapter 7 contents page on livebook.manning.com
- Dataset README and datasets-server size API for `oopere/clinical-ner-qdora`
- Raw notebook `CH07/CH07_NB02_L4_QLoRA_QDoRA.ipynb`, including saved cell outputs
- LinkedIn post by Pere Martra on the Chapter 7 release
- Hub file list for this repo and for `HuggingFaceTB/SmolLM2-1.7B-Instruct` (file size and etag only)

## Patterns in this batch

The two Medicalia uploads are Alexandre Desbos and Baptiste Griva, one Université Savoie Mont Blanc project, one notebook, and one 400-row website table. Alexandre's saved run is learning rate 0.002 for 300 steps. Baptiste's saved run is learning rate 2e-5 for 2000 steps. The weight-file etags differ, so one repo is not a copy of the other. Both are LoRA on the instruction-tuned 135M SmolLM2, with an 8-bit optimizer, and the merge step in the saved notebook did not create a new Hub commit.

The training target is a sentence of the form "You may have {disease} You can use this treatment: {treatments}" given a symptom string. The system prompt talks about JSON. The assistant text is not JSON. No scored evaluation was published.

ClinicalNER is a different project: Pere Martra's Chapter 7 notebook, QLoRA supervised fine-tuning of SmolLM2-1.7B-Instruct on synthetic English notes. The trained output is one JSON object with age, symptoms, vital signs, medications, and duration, not token labels. The card, the notebook output, the dataset card, and a LinkedIn post give three different schema-compliance figures for that QLoRA run: 95%, 100%, and the notebook's own markdown table at 95% beside an executed cell at 100%.
