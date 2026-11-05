# Medical fine-tune literature, batch 3

Five Hugging Face models. The two BLACKBUN checkpoints share one GitHub project and one dataset script; size-specific lines are recorded under each model.

| model | source found | objective | update scope | data (name, n, provenance) | base | task trained for | language | matches inventory row |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| BLACKBUN/llama-2-7b-pubmed-qa-211k | code | sft | qlora, merged | PubMedQA `pqa_artificial`, 211,269 Hub rows; questions rewritten from titles, answers are abstract conclusions | meta-llama/Llama-2-7b-chat-hf (chat) | open answer (abstract conclusion) | en | partly |
| Ghufran27/medical-llama2-7b | none | sft | qlora, merged | Ghufran27/medical-qa-v3, 156,816 rows; card says medical literature; sampled rows mix consumer-health answers and exam items | NousResearch/Llama-2-7b-chat-hf (chat) | open QA and exam items | en | partly |
| jassercherif/Llama-2-7b-doctorstr-finetuned | none | not stated | not stated | jassercherif/ChatDoctor-HealthCareMagic-llama2-100k, 1,000 rows; patient text and a doctor reply | NousResearch/Llama-2-7b-chat-hf (chat) | patient-doctor dialogue | en | partly |
| BLACKBUN/llama-2-13b-pubmed-qa-211k | code | sft | qlora, merged | same PubMedQA `pqa_artificial` script as the 7B | meta-llama/Llama-2-13b-chat-hf (chat) | open answer (abstract conclusion) | en | partly |
| hudson5/llama-3-8b-chat-doctor | blog | sft | qlora, merged | ruslanmv/ai-medical-chatbot, 256,916 dialogues; the matching notebook uses 1,000 of them | meta-llama/Meta-Llama-3-8B-Instruct (instruct), loaded from a Kaggle path | patient-doctor dialogue | en | partly |

## BLACKBUN/llama-2-7b-pubmed-qa-211k

### Sources

The model card is only YAML. It names `qiaojin/PubMedQA` and `meta-llama/Llama-2-7b-chat-hf`. Cached card: `revision_3_experiments/hf_inventory/cache/readmes/BLACKBUN__llama-2-7b-pubmed-qa-211k__2026-10-06.md`.

The training write-up is the GitHub repo [Aprilistic/Medical_LLM](https://github.com/Aprilistic/Medical_LLM). README says: "Baseline / pubmed-qa" and links this exact repo id. Authors listed there: Jinho Heo, Jinsig Yoo, Sangyoon Kim. No paper for this training run was found. The PubMedQA dataset paper is Jin et al., EMNLP 2019, [https://aclanthology.org/D19-1259/](https://aclanthology.org/D19-1259/). It describes the data, not this Llama run.

Training script: [model/7b/7b_baseline/llama-pubmed-211k.py](https://github.com/Aprilistic/Medical_LLM/blob/main/model/7b/7b_baseline/llama-pubmed-211k.py). The same cells are copied in [model/training_guide.ipynb](https://github.com/Aprilistic/Medical_LLM/blob/main/model/training_guide.ipynb).

### Training record

(a) Objective: supervised next-token fine-tuning. Script says: `from trl import SFTTrainer` and builds `SFTTrainer(..., task` is set by `LoraConfig(..., task_type="CAUSAL_LM")`. No preference loss and no reward model.

(b) Update scope: QLoRA, then the adapter is merged. Script says: `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_use_double_quant=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch.bfloat16)` and `LoraConfig(lora_alpha=16, lora_dropout=0.1, r=64, bias="none", task_type="CAUSAL_LM")`. Comment in the script: "LoRA config based on QLoRA paper". Target modules are not set in that `LoraConfig`. Later: `merged_model = model.merge_and_unload()` and `merged_model.push_to_hub("llama-2-7b-pubmed-qa-211k")`. The Hub repo has three `pytorch_model-*.bin` shards, full Llama weights, no adapter file. Config `torch_dtype` is `float32`.

(c) Data: script says `dataset = load_dataset("pubmed_qa", "pqa_artificial", split="train")`. The line `dataset.select(range(10000))` is commented out. A different file, `llama-pubmed-10k.py`, is not the script whose `output_dir` is this repo. The Hub card for `qiaojin/PubMedQA` config `pqa_artificial` says the train split has `num_examples: 211269`. Paper says: "We collected 211.3k instances for PQA-A, of which 200k randomly sampled instances are for training and the rest 11.3k instances are for validation." The script loads the Hub train split, which is the whole artificial config, not that 200k/11.3k cut. Paper says the questions are made by a rule: "The statement titles are converted to questions by simply moving or adding copulas ("is", "are") or auxiliary verbs ("does", "do") in the front." The long answer is the abstract conclusion (human-written abstract text). The script's training string uses `sample['question']` and `sample['long_answer']` only. It does not use the abstract context or the yes/no/maybe field. Language is English biomedical text. The formatting function still contains this leftover sentence: "Use the Input below to create an instruction, which could have been used to generate the response using an LLM." The supervised continuation is `long_answer`.

(d) Base: script says `model_id = "meta-llama/Llama-2-7b-chat-hf"`. That checkpoint is the chat (instruction-tuned) Llama 2 7B, not the raw pretrained checkpoint. Card YAML and config `_name_or_path` say the same id.

(e) Script: `num_train_epochs=2`, `learning_rate=2e-4`, `per_device_train_batch_size=4` because `use_flash_attention = False`, `gradient_accumulation_steps=2`, `max_seq_length = 2048`, `packing=True`, `optim="paged_adamw_32bit"`, `warmup_ratio=0.03`, `lr_scheduler_type="constant"`. `device_map={"":0}` means one GPU. No GPU model name is stated. `train.sh` run name: `llama-2-7b-pubmed-qa`. Weights & Biases project name in the script: `AIDoc`.

(f) Evaluation: after training, the script reloads `pqa_labeled` train, draws one random row, generates up to 100 tokens, and prints that `long_answer`. No accuracy or other score is computed. `pqa_labeled` is not the training split.

(g) Task: generate the abstract's conclusion (`long_answer`) from the question. That is open biomedical question answering. It is not training on the yes/no/maybe decision. Intended language: English.

### Discrepancies

1. Inventory `methods` is blank. The script is QLoRA supervised fine-tuning, then a merge.
2. Card YAML says `qiaojin/PubMedQA` and does not name the `pqa_artificial` split. The script loads only that split.
3. The script saves with `safe_serialization=True`. The uploaded 7B repo is PyTorch `.bin` shards, not safetensors. The 13B repo from the sister script is safetensors.
4. The paper's PQA-A split is 200k train and 11.3k validation. The Hub `pqa_artificial` train split used by the script is 211,269 rows.
5. The repo name contains `211k`. That matches the artificial split size. The count used here is the Hub split size and the script, not the name alone.
6. Featherless's page repeats the card's dataset tag. It is not an independent training log.

### Confidence

High. The README links this repo id, and the 7B script's `output_dir`, `push_to_hub` name, base id, and dataset config match the checkpoint.

### Queries tried

1. `BLACKBUN llama-2-7b-pubmed-qa-211k fine-tune training`
2. `BLACKBUN huggingface llama-2-13b-pubmed-qa-211k`
3. `"pubmed-qa-211k" OR "pubmed qa 211k" Llama fine-tuning`
4. `Aprilistic Medical_LLM paediatrics abdominal pain llama fine-tuning paper`
5. `huggingface.co BLACKBUN Medical_LLM author paediatric`
6. `"Jinho Heo" "Jinsig Yoo" llama medical diagnosis pubmed`
7. `PubMedQA pqa_artificial artificially generated 211.3k method Jin D19-1259`
8. `"llama-2-7b-pubmed-qa-211k" OR "AIDoc" BLACKBUN Heo Yoo Kim wandb`

## Ghufran27/medical-llama2-7b

### Sources

The model card is the only training write-up found. Cached card: `revision_3_experiments/hf_inventory/cache/readmes/Ghufran27__medical-llama2-7b__2026-10-05.md`. No paper, GitHub repo, or Kaggle notebook naming this run was found. The dataset repo `Ghufran27/medical-qa-v3` has a license line and no description. Row count and samples are from the Hugging Face datasets server.

### Training record

(a) Objective: supervised instruction tuning of a causal language model. Card says: "Medical Llama-2-7b is an instruction-tuned language model optimized for medical question-answering" and "Task Type: `CAUSAL_LM`". It does not name SFTTrainer, a preference method, or a reward model.

(b) Update scope: QLoRA, then merged. Card says: "this model leverages Low-Rank Adaptation (LoRA)" and "Quantization: 4-bit NormalFloat (NF4) quantization with double quantization". Rank `r`: 8. Alpha `lora_alpha`: 16. Dropout `lora_dropout`: 0.05. Target modules: `q_proj`, `v_proj`. Card says: "Output: Merged model saved in safetensors format". The repo has `model-00001-of-00003.safetensors` through `00003`, float16, and no adapter file.

(c) Data: card YAML says `Ghufran27/medical-qa-v3`. Prose says: "a custom medical dataset (`cleaned_medical.jsonl`)" and "question-answer pairs sourced from medical literature". The Hub file is `medical-qa-v3.jsonl`, not `cleaned_medical.jsonl`. Datasets server: 156,816 train rows, one `text` column. Row 0 begins `<s>[INST] What is (are) keratoderma with woolly hair ? [/INST]` and the answer matches the Genetics Home Reference wording also stored in `lavita/MedQuAD` (47,441 rows). Rows sampled at offsets 50000, 100000, and 150000 are exam items with an "Explanation:" field ("are all except", "material deposited is"). No generator model is named. Card language: `en`.

(d) Base: card says `NousResearch/Llama-2-7b-chat-hf`. That is a chat (instruction-tuned) Llama 2 7B.

(e) Card: epochs 1, max steps 500, batch size 16 per device, gradient accumulation 1, learning rate 2e-4, fp16, warmup 50, max gradient norm 0.3, hardware "Kaggle GPU (CUDA)". No GPU model name.

(f) Card YAML lists metric `accuracy` and training sets `Evaluation Steps: 200`. No score is reported. The card says the model is "Designed for the Open Medical-LLM Leaderboard". No leaderboard row for this id was found.

(g) Card says medical question-answering, "disease diagnosis, treatment protocols, and medical terminology", with a system line that refuses non-medical questions. The file mixes open answers and multiple-choice exam items, so the trained task is not one of those alone. Language of the card and of the sampled rows: English.

### Discrepancies

1. Inventory `methods` is `lora`. The card also states 4-bit NF4 with double quantization, which is QLoRA, and says the adapter was merged.
2. Prose file name `cleaned_medical.jsonl` versus Hub file `medical-qa-v3.jsonl` and YAML id `Ghufran27/medical-qa-v3`.
3. Epochs 1 and max steps 500 are both stated. At batch size 16, 500 steps cover far fewer than 156,816 rows, so a full epoch and a 500-step cap cannot both have been completed. The card does not say which limit stopped training.
4. Row 0 matches MedQuAD / Genetics Home Reference. The file has 156,816 rows and later rows are exam items, so the file is not that MedQuAD release by itself. The card does not name MedQuAD.

### Confidence

Medium. The hyperparameters are written on the card in enough detail to classify the run, and the merged float16 files match the "merged safetensors" line. No script was found, and the dataset's sources are only partly visible from samples.

### Queries tried

1. `Ghufran27 medical-llama2-7b LoRA cleaned_medical.jsonl`
2. `"Ghufran27" OR "medical-llama2-7b" OR "cleaned_medical.jsonl" llama LoRA`
3. `Ghufran27 medical-qa-v3 huggingface dataset`
4. `"What is (are) keratoderma with woolly hair" medical dataset MedQuAD`
5. `"Ghufran" medical llama kaggle OR github OR colab "lora_alpha" 16`
6. `site:huggingface.co Ghufran27 medical-llama2-7b open medical LLM leaderboard`

## jassercherif/Llama-2-7b-doctorstr-finetuned

### Sources

The card body is empty. YAML lists dataset `jassercherif/ChatDoctor-HealthCareMagic-llama2-100k`, language `en`, metrics `accuracy` and `bleu`, base `NousResearch/Llama-2-7b-chat-hf`, and `library_name: peft`. Cached card: `revision_3_experiments/hf_inventory/cache/readmes/jassercherif__Llama-2-7b-doctorstr-finetuned__2026-10-06.md`.

No training script, paper, or blog naming this repo was found. Jasser Cherif's portfolio ([https://jassercherif.github.io/MyPortfolio/](https://jassercherif.github.io/MyPortfolio/)) does not mention this model. The ChatDoctor paper (Li et al., Cureus 2023, [https://www.cureus.com/articles/152798](https://pmc.ncbi.nlm.nih.gov/articles/PMC10364849/)) and the GitHub repo [Kent0n-Li/ChatDoctor](https://github.com/Kent0n-Li/ChatDoctor) train LLaMA-7B, not this Llama-2-chat checkpoint. Those hyperparameters are not used below.

### Training record

(a) Objective: not stated. The repo name contains "finetuned". That is not a method. YAML `library_name: peft` and the Hub tag `base_model:adapter` are not a loss function. There is no `adapter_config.json` in the repo.

(b) Update scope: not stated. The uploaded files are full Llama-2-7B shards, both `pytorch_model-0000*-of-00002.bin` and matching safetensors, about 13.5 GB, with a tokenizer. There is no `adapter_config.json` and no `adapter_model` file. Rank, alpha, and target modules are not stated. Whether any adapter was merged is not stated.

(c) Data: the dataset card and the datasets server say the train split has `num_examples: 1000` and one column, `text`. The name contains `100k`. The file does not. Row 0 is `<s>[INST]` plus a patient's description of rib pain, then `[/INST]`, then a doctor reply, then `</s>`. Language tag: `en`. The ChatDoctor paper says HealthCareMagic-100k is "around 100k" human patient-doctor conversations from healthcaremagic.com, cleaned and anonymized. This upload is 1,000 rows, and its first patient text is not the first row of `lavita/ChatDoctor-HealthCareMagic-100k` (112,165 rows; columns `instruction`, `input`, `output`). So this file is not that full release. Provenance of these 1,000 strings is not stated on the dataset card. The text is a patient message and a doctor reply.

(d) Base: YAML and config `_name_or_path` say `NousResearch/Llama-2-7b-chat-hf`, a chat (instruction-tuned) Llama 2 7B.

(e) Epochs, learning rate, batch size, and hardware: not stated anywhere found.

(f) YAML lists `accuracy` and `bleu`. No scores.

(g) The declared training text is one patient turn and one doctor turn. That is patient-doctor dialogue, even though the pipeline tag is `question-answering`. Language: English.

### Discrepancies

1. Inventory `methods` is blank, which agrees with "not stated". Inventory dataset id and parent match the YAML.
2. The name says 100k. The dataset file has 1,000 examples.
3. YAML says `library_name: peft` and the Hub model tree says "Adapter". The files are full weights, not an adapter.
4. The ChatDoctor paper's training setup (LLaMA-7B, Alpaca then HealthCareMagic-100k, 6 A100s, batch size 192, 3 epochs, sequence length 512) is a different model. It is not evidence for this checkpoint.

### Confidence

Low. The base id and the 1,000-row file are on the Hub. The loss, the parameter update, and the hyperparameters are not.

### Queries tried

1. `jassercherif Llama-2-7b-doctorstr-finetuned ChatDoctor`
2. `"jasser cherif" OR jassercherif OR doctorstr Llama-2 fine-tune ChatDoctor`
3. `"ChatDoctor-HealthCareMagic-llama2-100k" OR "doctorstr-finetuned" OR "Llama-2-7b-doctorstr"`
4. `github.com jassercherif OR "jasser.cherif" Llama-2 doctorstr OR ChatDoctor finetune`
5. Hugging Face user page `https://huggingface.co/jassercherif`
6. Portfolio `https://jassercherif.github.io/MyPortfolio/`
7. ChatDoctor paper and `Kent0n-Li/ChatDoctor` (different base model; not used as this run's hyperparameters)

## BLACKBUN/llama-2-13b-pubmed-qa-211k

### Sources

Same project as the 7B model. Card YAML only: license `mit`, dataset `qiaojin/PubMedQA`, base `meta-llama/Llama-2-13b-chat-hf`. Cached card: `revision_3_experiments/hf_inventory/cache/readmes/BLACKBUN__llama-2-13b-pubmed-qa-211k__2026-10-05.md`. README row: "Baseline / pubmed-qa" links this repo id. Script: [model/13b/13b_baseline/llama-pubmed-211k.py](https://github.com/Aprilistic/Medical_LLM/blob/main/model/13b/13b_baseline/llama-pubmed-211k.py). Merge notebook [model/save_merged.ipynb](https://github.com/Aprilistic/Medical_LLM/blob/main/model/save_merged.ipynb) sets `output_dir = "llama-2-13b-pubmed-qa-211k"`.

### Training record

(a) Same as the 7B script: `SFTTrainer` and `task_type="CAUSAL_LM"`. Supervised next-token fine-tuning.

(b) Same QLoRA settings: 4-bit NF4, double quantization, bfloat16 compute, `r=64`, `lora_alpha=16`, `lora_dropout=0.1`, `bias="none"`. Target modules are not set. The 13B script then does `AutoPeftModelForCausalLM.from_pretrained(..., device_map="cpu")`, `merge_and_unload()`, and `push_to_hub("llama-2-13b-pubmed-qa-211k")`. The Hub repo is 11 safetensors shards, float32, 13,015,864,320 parameters. No adapter file.

(c) Same data load: `load_dataset("pubmed_qa", "pqa_artificial", split="train")`, with the 10,000-row subset commented out. Same formatting function: question in, `long_answer` out. Same provenance and the same 211,269-row Hub train split. English.

(d) Script says `model_id = "meta-llama/Llama-2-13b-chat-hf"`. Chat (instruction-tuned) Llama 2 13B. Config `_name_or_path` matches.

(e) Same arguments as the 7B script: 2 epochs, learning rate 2e-4, per-device batch size 4, gradient accumulation 2, sequence length 2048, packing on, one GPU (`device_map={"":0}`). `train.sh` run name: `llama-2-13b-pubmed-qa`. No GPU model name. The merge load uses `device_map="cpu"`, which the 7B script's merge load does not.

(f) Same one-sample print from `pqa_labeled`. No metric.

(g) Same task as the 7B script: generate the abstract conclusion from the question. English.

### Discrepancies

1. Inventory `methods` is blank. The script is QLoRA supervised fine-tuning, then a merge.
2. Card YAML does not name `pqa_artificial`. The script does.
3. Paper 200k/11.3k split versus the Hub train split of 211,269, as for the 7B model.
4. Uploaded dtype is float32 safetensors. The script's earlier inference load uses `torch_dtype=torch.float16`, but the merge load that is pushed does not set a dtype. The float32 upload matches that merge load, not the float16 inference load.

### Confidence

High. The 13B script names this repo, this base, and this dataset config, and the upload is a merged full model in safetensors, which is what that script asks to push.

### Queries tried

Same searches as the 7B model, plus the 13B script and `save_merged.ipynb`.

## hudson5/llama-3-8b-chat-doctor

### Sources

The card is the default Hub template plus the line "A model used for medical chat, use it with caution!" YAML names `ruslanmv/ai-medical-chatbot` and `meta-llama/Meta-Llama-3-8B-Instruct`, languages `en` and `cn`. Cached card: `revision_3_experiments/hf_inventory/cache/readmes/hudson5__llama-3-8b-chat-doctor__2026-10-05.md`.

The method is the DataCamp tutorial by Abid Ali Awan (GitHub `kingabzpro`), [Fine-Tuning Llama 3 and Using It Locally](https://www.datacamp.com/tutorial/llama3-fine-tuning-locally), and the Kaggle notebook [Fine-tune Llama 3 8B on Medical Dataset](https://www.kaggle.com/code/kingabzpro/fine-tune-llama-3-8b-on-medical-dataset). The tutorial does not name the user `hudson5`. What ties this repo to that notebook is the file `adapter_config.json` in the hudson5 repo: `"base_model_name_or_path": "/kaggle/input/llama-3/transformers/8b-chat-hf/1"`, `"peft_type": "LORA"`, `"r": 16`, `"lora_alpha": 32`, `"lora_dropout": 0.05`, `"use_dora": false`, target modules `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`. The tutorial sets `base_model` to that same Kaggle path and `new_model = "llama-3-8b-chat-doctor"`, with the same LoRA fields. `kingabzpro/llama-3-8b-chat-doctor` has the same Kaggle path and the same LoRA fields. That repo was created 2024-05-20. hudson5's repo was created 2024-11-22 and also contains a `Q4_K_S` GGUF that the kingabzpro file list does not. So this is the same notebook's setup, not a sentence that says hudson5 copied kingabzpro's weights.

Dataset provenance: [ruslanmv/ai-medical-chatbot](https://huggingface.co/datasets/ruslanmv/ai-medical-chatbot) says "at least 250k dialogues between a Patient and a Doctor" and the page lists 256,916 rows. The project README says: "This csv has 256916 dialogues between a Patient and Doctor" and that the csv was built from the Medical-Dialogue-System files ([https://github.com/ruslanmv/ai-medical-chatbot/blob/master/2-Data/README.md](https://github.com/ruslanmv/ai-medical-chatbot/blob/master/2-Data/README.md)). The MedDialog paper (Chen et al., arXiv:2004.03329) says the English consultations were crawled from icliniq.com and healthcaremagic.com.

### Training record

(a) Objective: supervised fine-tuning. Tutorial says: "We'll now set up a supervised fine-tuning (SFT) trainer" and the code is `SFTTrainer(...)`. Adapter `task_type` is `CAUSAL_LM`. No preference loss and no reward model.

(b) Update scope: QLoRA, then merged. Tutorial: `BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4", bnb_4bit_compute_dtype=torch_dtype, bnb_4bit_use_double_quant=True)` with `torch_dtype = torch.float16`, and `LoraConfig(r=16, lora_alpha=32, lora_dropout=0.05, bias="none", task_type="CAUSAL_LM", target_modules=['up_proj', 'down_proj', 'gate_proj', 'k_proj', 'q_proj', 'v_proj', 'o_proj'])`. Those values match hudson5 `adapter_config.json`, including `"use_dora": false`. Tutorial then: `model = model.merge_and_unload()` and `model.push_to_hub("llama-3-8b-chat-doctor")`. The hudson5 repo has the adapter files, four float16 shards (8,030,277,632 parameters), and GGUF files `llama-3-8b-chat-doctor-Q4_K_M.gguf` and `llama-3-8b-chat-doctor-Q4_K_S.gguf`. The merged weights are the full model. The adapter file is still in the repo.

(c) Data: tutorial says `dataset_name = "ruslanmv/ai-medical-chatbot"` and "The dataset contains 250k dialogues between a patient and a doctor." Code: `dataset.shuffle(seed=65).select(range(1000))` and `dataset.train_test_split(test_size=0.1)`, so 900 train and 100 eval in that notebook. Each row is formatted as user = `Patient`, assistant = `Doctor`. The source dialogues are human patient-doctor text from the sites named in the MedDialog paper, as packaged by ruslanmv. hudson5's card does not restate the 1,000-row subset. Language of that dataset: English.

(d) Card YAML says `meta-llama/Meta-Llama-3-8B-Instruct`. Tutorial and both adapter configs load `/kaggle/input/llama-3/transformers/8b-chat-hf/1`, the Kaggle copy of Llama 3 8B chat. Config `_name_or_path` on hudson5 is that Kaggle path. `vocab_size` is 128258. The tokenizer adds `<|im_start|>` and `<|im_end|>` (128256 and 128257). The tutorial calls `setup_chat_format`, which adds those two tokens. The base is instruction-tuned.

(e) Tutorial `TrainingArguments`: `num_train_epochs=1`, `learning_rate=2e-4`, `per_device_train_batch_size=1`, `gradient_accumulation_steps=2`, `optim="paged_adamw_32bit"`, `warmup_steps=10`, `max_seq_length=512`. Session option in the tutorial: "select the GPU P100".

(f) Tutorial shows training and validation loss curves and one generated reply to "Hello doctor, I have bad acne. How do I get rid of it?" No benchmark score. It says: "Both training and validation losses have decreased."

(g) Task: reply to a patient in a doctor turn. Language the notebook trains: English. The card YAML also lists `cn`. No Chinese training text was found.

### Discrepancies

1. Inventory `methods` is blank. The adapter file and the matching notebook are QLoRA supervised fine-tuning, then a merge.
2. Inventory and the card name the parent as `meta-llama/Meta-Llama-3-8B-Instruct`. The saved config and adapter still record the Kaggle path `8b-chat-hf`.
3. The published notebook trains on 1,000 rows. The source dataset has 256,916. hudson5's card does not say which of those was used.
4. Card YAML languages are `en` and `cn`. The dataset and the notebook are English. `cn` is not an ISO language code.
5. Hub tag `base_model:quantized` matches the GGUF files in the same repo. The safetensors shards are float16, not 4-bit. The 4-bit load was the training-time base.

### Confidence

Medium. The LoRA config, the Kaggle base path, the added chat tokens, and the merged float16 files are on this repo and match the tutorial. The tutorial never names hudson5, so the 1,000-row subset and the P100 are the published notebook's settings, not a log hudson5 posted.

### Queries tried

1. `hudson5 llama-3-8b-chat-doctor fine-tune ruslanmv`
2. `"llama-3-8b-chat-doctor" hudson5 OR kaggle OR kingabzpro LoRA`
3. `ruslanmv ai-medical-chatbot dataset 256916 patient doctor source`
4. `huggingface hudson5 llama-3-8b-chat-doctor Abid Ali Awan datacamp`
5. MedDialog paper arXiv:2004.03329, followed from the dataset README
6. Comparison of `adapter_config.json` on hudson5 and on kingabzpro/llama-3-8b-chat-doctor

## Patterns in this batch

Four of the five runs are supervised next-token training on an already chat-tuned Llama. None is preference optimization or reinforcement learning. The two BLACKBUN sizes and hudson5 are QLoRA (a 4-bit base plus a LoRA adapter) with the adapter merged into a full checkpoint; Ghufran's card describes the same pattern at rank 8 on `q_proj` and `v_proj` only. jassercherif's repo does not say how the weights were updated, and the "peft" tag is not backed by an adapter file.

The BLACKBUN scripts never train the PubMedQA yes/no/maybe label. They train the model to continue with the abstract conclusion. The name `211k` matches the artificial split, and the script loads that Hub train split (211,269 rows), not a 10k subset that is left commented out. Ghufran's 156,816-row file mixes open consumer-health answers and exam items, and the card's 500-step cap cannot cover that file in one epoch at batch size 16. The jassercherif dataset name says 100k; the file has 1,000 rows. hudson5's adapter matches a tutorial that fine-tunes on 1,000 of 256,916 patient-doctor dialogues and then merges.

Inventory method labels are blank except Ghufran, which is recorded as LoRA and not as 4-bit training plus a merge. Every base in this batch is a chat or instruct checkpoint.
