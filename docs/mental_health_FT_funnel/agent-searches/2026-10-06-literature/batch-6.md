# Batch 6: how five mental-health fine-tunes were trained

Date of search: 2026-10-06. Cards read: the 2026-10-05 copies under `revision_3_experiments/hf_inventory/cache/readmes/`. Inventory reading: `revision_3_experiments/hf_inventory/results/mental-health/archive/2026-10-06/kept.csv`. Hub file lists: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__020.csv` and `2026-10-05__021.csv`, checked against the live model API on 2026-10-06.

A claim below is tied to a URL or a cached file. If a field is missing from every source that was found, it is marked "not stated anywhere found." A method word inside a dataset or repository name is not treated as the training method. A dataset card or listing that repeats the model card word for word is not a second witness.

## Summary

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Matches inventory row |
|---|---|---|---|---|---|---|
| lordChipotle/SuicidePreventionLlama | none | not stated | not stated (card says LoRA or 4-bit; the upload is full BF16 weights) | `nbertagnolli/counsel-chat` (2,775 English rows, human-written) plus unnamed Reddit, Twitter, and PAIR sets | `meta-llama/Llama-3.2-3B-Instruct` | partly |
| mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy | paper (abstract only) and Hub cards | supervised fine-tuning on prompt/completion dialogues | QLoRA, then merged. Rank 32, alpha 64 | `mariadelcarmenramirez/art-therapy-data`: 9,572 Spanish rows, synthetic (`gpt-5-nano`); the run used 2,800 | `meta-llama/Llama-3.1-8B-Instruct` | yes |
| naazimsnh02/gemma3-4b-mental-health-counseling | code | supervised fine-tuning (`SFTTrainer`), response tokens only | 4-bit load plus LoRA, then merged. Rank 16, alpha 32 | `Amod/mental_health_counseling_conversations`. Card and notebook say 3,500 English pairs. Dataset card: real counseling Q&A | `unsloth/gemma-3-4b-it` (instruction-tuned) | partly |
| prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2 | code (AutoTrain JSON in this repo) | supervised fine-tuning (`"trainer": "sft"`) | 4-bit load plus LoRA, adapter merged. Rank 16, alpha 32. Targets `q_proj`, `v_proj` | same Amod dataset. Example count not stated. The log has 1,107 steps | `mistralai/Mistral-7B-Instruct-v0.2` | partly |
| ryefoxlime/gemma-2-2b-it-therapist | code (notebook in a second Hub repo) | supervised fine-tuning (`SFTTrainer`) | 4-bit NF4 plus LoRA. Rank 64, alpha 16. README says the adapter was merged | `nbertagnolli/counsel-chat`: script loads 2,775 English rows, then an 80/20 split. Human-written | `google/gemma-2-2b-it` | partly |

## 1. lordChipotle/SuicidePreventionLlama

The model card is the only training write-up that could be read. It points at a Colab notebook. That page returned only the Colab shell, not the cells. No paper or GitHub script names this repository.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/lordChipotle__SuicidePreventionLlama__2026-10-05.md`. Live page: https://huggingface.co/lordChipotle/SuicidePreventionLlama . Created 2025-01-13, last modified 2025-01-13. The page is this repo, so it names `lordChipotle/SuicidePreventionLlama`.
- Hugging Face user page names the account holder Daniel Huang and links https://github.com/lordChipotle and https://lordchipotle.github.io/tech.html . https://huggingface.co/lordChipotle . The GitHub profile does not list a suicide-prevention repository. https://github.com/lordChipotle
- Colab link printed on the card: https://colab.research.google.com/drive/1vbio7VWmkpQoTnDUg32TABxxf4VcBBeY?usp=sharing . Fetch on 2026-10-06 returned the title "Google Colab" and no notebook cells.
- Hub API file list: `config.json`, two `safetensors` shards, tokenizer files. No `adapter_config.json`. Architecture `LlamaForCausalLM`. Safetensors: 3,212,749,824 parameters, BF16. https://huggingface.co/api/models/lordChipotle/SuicidePreventionLlama
- Dataset card for the one dataset in the YAML: https://huggingface.co/datasets/nbertagnolli/counsel-chat . Datasets-server size: 2,775 train rows, 10 columns. https://datasets-server.huggingface.co/size?dataset=nbertagnolli/counsel-chat
- An IEEE BigData 2024 paper and its code, https://github.com/khanhvynguyen/Suicide_Detection_LLMs , fine-tune Llama 3 8B and other models for suicide-risk labels. They do not name this repository or Llama 3.2 3B. Not used below.

### Training record

**(a) Objective.** Not stated anywhere found. The card describes instruction prompts for a generative model and does not name supervised fine-tuning, next-token loss, DPO, ORPO, PPO, or a reward model. Card says: "Multi-Task Instruction: We used short prompts for classification tasks, and Q&A style prompts for therapy." Cached card, section "Training Approach." The usage snippet loads `AutoModelForCausalLM`. That shows the uploaded file is a causal language model. It does not name the loss.

**(b) Parameter-update scope.** Not stated as a single method. Card says: "Parameter-Efficient Fine-tuning: We used **LoRA** adapters or 4-bit quantization to reduce GPU memory usage." The sentence is an or. Rank, alpha, and target modules: not stated anywhere found. The upload has no `adapter_config.json` and the parameter count is the full 3.2B Llama in BF16. Whether an adapter was merged before upload: not stated anywhere found.

**(c) Training data.** Card prose lists four sources and gives no row counts: "Reddit-based suicide detection data (r/SuicideWatch, r/depression, r/teenagers)", "Twitter suicidal-intent classification data", "CounselChat", and "PAIR: short counseling interactions with high- and medium-quality reflections." YAML `datasets` lists only `nbertagnolli/counsel-chat`. That dataset card says: "The dataset was scraped on 20220401 from counselchat.com" and "The text was written by licensed counselors in the United States and annonymous individuals." English. 2,775 rows. Hub ids, example counts, and provenance for the Reddit, Twitter, and PAIR sets: not stated anywhere found. A 2022 EMNLP paper titled "PAIR: Prompt-Aware margIn Ranking for Counselor Reflection Scoring in Motivational Interviewing" (https://aclanthology.org/2022.emnlp-main.11.pdf) describes counselor reflections of low, medium, and high quality. The model card does not cite that paper, so it is not treated as this run's dataset.

**(d) Base model.** YAML and Hub `base_model`: `meta-llama/Llama-3.2-3B-Instruct`. The card body says only "Base Model: LLaMA-based architecture." The id is Meta's instruction-tuned 3B checkpoint, not the separate pretrained `Llama-3.2-3B` checkpoint. The card does not itself use the words "instruction-tuned."

**(e) Hyperparameters.** Card says: "Batch Size: 2", "Max Steps: 60 (example short run)", "Learning Rate: 2e-4", "Mixed Precision (fp16) or bf16 depending on the GPU." The parenthetical marks 60 steps as an example. Epochs and hardware: not stated anywhere found.

**(f) Evaluation.** Not stated anywhere found. The card has no scores.

### Discrepancies

1. Inventory `methods` is `lora`, taken from the card sentence that says "LoRA adapters or 4-bit quantization." The upload is full BF16 weights with no adapter file.
2. Inventory `datasets` is only `nbertagnolli/counsel-chat`, which matches the YAML. The prose also names Reddit, Twitter, and PAIR, with no Hub ids.
3. The learning rate and batch size sit next to a step count the card calls an example short run. They may not be the run that produced the uploaded weights.

### Confidence

Medium that the card is about this upload, because it is this repository's README. Low that the printed 60 steps, batch size 2, and learning rate 2e-4 are the run that produced the BF16 shards, because the card calls the step count an example and the linked notebook could not be read.

### Queries tried

- `lordChipotle SuicidePreventionLlama fine-tune LoRA`
- `"SuicidePreventionLlama" OR "Suicide Prevention Llama" colab`
- `"Daniel Huang" SuicidePreventionLlama OR "lordChipotle" github llama fine-tune`
- `site:github.com/lordChipotle SuicidePrevention OR counsel-chat OR "Llama-3.2-3B"`
- `1vbio7VWmkpQoTnDUg32TABxxf4VcBBeY SuicidePreventionLlama unsloth LoRA`
- `"PAIR" counseling reflections "high- and medium-quality" dataset suicide llama`
- Hugging Face user page and the GitHub profile linked from it

## 2. mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy

The merged checkpoint's card, the separate adapter repo, and `adapter_config.json` agree on QLoRA of Llama 3.1 8B Instruct. A 2026 conference abstract by the same author describes a Spanish art-therapy system with a fine-tuned model and a synthetic dataset. The full paper text was not available, and the abstract does not print this Hub id or any hyperparameter.

### Sources

- Cached merged-model card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/mariadelcarmenramirez__Llama-3.1-8B-ArtTherapy__2026-10-05.md`. Live: https://huggingface.co/mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy . Created 2026-03-12, last modified 2026-03-25. Names this repo id. Files: one `model.safetensors`, no `adapter_config.json`. Safetensors: 8,030,261,248 parameters, BF16.
- Adapter repo card: https://huggingface.co/mariadelcarmenramirez/Llama-3.1-8B-QLoRA-ArtTherapy . Developed by María del Carmen Ramírez. Created 2026-03-11. Files include `adapter_config.json` and `adapter_model.safetensors`. The merged card names this adapter id.
- Adapter config: https://huggingface.co/mariadelcarmenramirez/Llama-3.1-8B-QLoRA-ArtTherapy/raw/main/adapter_config.json . `peft_type` `LORA`, `r` 32, `lora_alpha` 64, `base_model_name_or_path` `meta-llama/Llama-3.1-8B-Instruct`.
- Dataset card: https://huggingface.co/datasets/mariadelcarmenramirez/art-therapy-data . Cached copy: `revision_3_experiments/hf_inventory/cache/datasets/mariadelcarmenramirez__art-therapy-data__2026-10-06.md`. YAML: 9,572 train examples. This card is by the same author. It is not a copy of the model card: the model card does not describe the generator.
- Publisher abstract: María del Carmen Ramírez-Trujillo, Maite Lopez-Sanchez, Inmaculada Rodríguez, "Structuring Art Therapy On-Line Sessions," *Frontiers in Artificial Intelligence and Applications*, vol. 431, *Artificial Intelligence Research and Development*, pp. 304–313. https://ebooks.iospress.nl/volumearticle/81169 . The co-author's publication list calls it a 2026 CCIA paper and "open access," with the DOI still blank: http://www.maia.ub.edu/~maite/publications.html . No arXiv HTML, no university PDF, and no training section could be fetched. The abstract does not print `mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy`.
- Featherless listing https://featherless.ai/models/mariadelcarmenramirez/Llama-3.1-8B-ArtTherapy repeats the merged card (QLoRA merge, Spanish, phase tags). Not a second witness.
- GGUF repo https://huggingface.co/mradermacher/Llama-3.1-8B-ArtTherapy-GGUF says "static quants of" this model. It does not add a training method.

### Training record

**(a) Objective.** Supervised fine-tuning on dialogue completions. Dataset card says: "A synthetic Spanish-language dataset of post–art-making therapeutic dialogues, designed for supervised fine-tuning" and "Every instance follows a prompt–completion conversational format compatible with chat-oriented trainers such as TRL's `SFTTrainer`." The model card says the model "was trained on" that dataset, with a `prompt` of system and user turns and a `completion` that is the assistant reply. The model card does not print the string `SFTTrainer`. No source names DPO, ORPO, PPO, or a reward model. The paper abstract says "a fine-tuned LLM generates phase-appropriate therapeutic language in Spanish" and does not name the objective.

**(b) Parameter-update scope.** QLoRA, then merged into the weights in this repo. Merged card says: "This model was produced by merging the QLoRA adapter [`mariadelcarmenramirez/Llama-3.1-8B-QLoRA-ArtTherapy`] into the base model weights, resulting in a single standalone model" and "Fine-tuning method | QLoRA (4-bit NF4)". Adapter card says: "Fine-tuning method | QLoRA (4-bit NF4)", "LoRA rank (r) | 32", "LoRA alpha | 64", "LoRA dropout | 0.1", "LoRA target modules | q_proj, k_proj, v_proj, o_proj, gate_proj, up_proj, down_proj", "Quantization | 4-bit NF4 (double quant, fp16 compute)". `adapter_config.json` matches rank 32, alpha 64, dropout 0.1, and those seven modules. The merged repo has one BF16 `model.safetensors` and no adapter file, which matches the merge sentence.

**(c) Training data.** Hub id `mariadelcarmenramirez/art-therapy-data`. Dataset YAML: 9,572 train examples. Language: Spanish. Merged card says: "Balanced sampling (700 per phase) produced 2,800 examples, split 90/10 into train (2,520) and eval (280) sets." Provenance, dataset card: "Generation was performed using `gpt-5-nano` via the OpenAI API." Seeds: "a curated set of phase-labelled input–output pairs reviewed by a licensed art therapist." "All content is synthetically generated. No real client data were used." The model card does not name `gpt-5-nano`. The paper abstract says: "we develop a synthetic data pipeline that generates phase-labelled training examples from therapist-reviewed seeds" and "a publicly available Spanish art therapy dialogue dataset." It does not name the Hub id or the generator model.

**(d) Base model.** Merged card YAML and adapter config: `meta-llama/Llama-3.1-8B-Instruct`. That id is Meta's instruction-tuned 8B checkpoint. The adapter card says "Base model | Llama-3.1-8B-Instruct".

**(e) Hyperparameters.** Adapter card: 3 epochs, learning rate 5e-5, cosine schedule, warmup 23 steps, per-device batch size 1, gradient accumulation 8, effective batch size 16 on 2 GPUs, optimizer `paged_adamw_8bit`, weight decay 0.01, max gradient norm 0.3. Hardware: "2× NVIDIA Tesla T4 (15.6 GB each)", "Training platform | Kaggle (multi-GPU DDP via Accelerate)", "Total training time | ~3 hours 46 minutes". The merged card repeats epochs, learning rate, effective batch size, rank, alpha, modules, and the two T4s, and omits the optimizer and the Kaggle line. Sequence length, adapter card: "MAX_SEQ_LENGTH = 546".

**(f) Evaluation.** Adapter card table, also on the merged card: eval loss and `eval_mean_token_accuracy` at half-epoch checkpoints. Best row: epoch 2.00, eval loss 1.313, token accuracy 65.30%. Final training loss 1.238. "No disaggregated evaluation by phase was conducted separately." No clinical or external benchmark score is stated. The paper abstract does not report numbers.

### Discrepancies

1. Inventory `methods` is `qlora`, `datasets` is `mariadelcarmenramirez/art-therapy-data`, and `parent` is `meta-llama/Llama-3.1-8B-Instruct`. That matches the cards. Inventory does not record the merge or the generator. Those are extra facts, not contradictions.
2. The model card does not say the dialogues were written by `gpt-5-nano`. The dataset card does.
3. The conference abstract describes a fine-tuned Spanish model and a synthetic dataset by this author. It does not confirm QLoRA, rank, or this Hub id, because the full text was not available.

### Confidence

High that the adapter card and `adapter_config.json` describe the adapter that this repo says it merged: the merged card prints the adapter repo id, and the merged file is one full BF16 weight file. Medium that the CCIA abstract is about this same checkpoint: same author and the same kind of system, and the abstract does not print the Hub id.

### Queries tried

- `mariadelcarmenramirez Llama-3.1-8B-ArtTherapy QLoRA art therapy`
- `"Llama-3.1-8B-ArtTherapy" OR "art-therapy-data" Ramirez`
- `"Structuring Art Therapy On-Line Sessions" Ramírez QLoRA Llama fine-tuned PDF`
- `"Structuring Art Therapy On-line Sessions" Ramírez QLoRA OR "fine-tuned" OR Llama site:arxiv.org`
- `"Llama-3.1-8B-QLoRA-ArtTherapy" OR "83,886,080" OR "art-therapy-data" Kaggle OR github Ramirez`
- `"Ramírez-Trujillo" OR "Ramirez-Trujillo" "art therapy" Llama OR QLoRA OR "fine-tuned" CCIA 2026`
- `site:github.com "Method Actor" art therapy OR mariadelcarmenramirez Llama-3.1 QLoRA`

## 3. naazimsnh02/gemma3-4b-mental-health-counseling

A GitHub notebook by the same account names this Hub id and builds the model card that is now on the Hub. The notebook loads the base in 4-bit and adds a LoRA adapter. The card calls the method LoRA and says the saved weights are float16.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/naazimsnh02__gemma3-4b-mental-health-counseling__2026-10-05.md`. Live: https://huggingface.co/naazimsnh02/gemma3-4b-mental-health-counseling . Created 2025-12-02, last modified 2025-12-02. Names this repo id. Files: two safetensors shards, no `adapter_config.json`. Safetensors: 4,300,079,472 parameters, BF16. Commit message on the weight upload: "Upload full merged model (base + LoRA adapters in float16)". https://huggingface.co/naazimsnh02/gemma3-4b-mental-health-counseling/commit/304952e8f4bf8b1066a3ffbe08018eabee53248e
- GitHub: https://github.com/Naazimsnh02/gemma3-mental-health-counseling . One commit, 2025-12-02, message "Added Notebook and Readme". README links `naazimsnh02/gemma3-4b-mental-health-counseling`.
- Notebook: https://github.com/Naazimsnh02/gemma3-mental-health-counseling/blob/main/gemma3-mental-health-counseling.ipynb . The upload cell writes a model card whose body matches the Hub card. The Hub card is that generated text, not an independent write-up.
- Other repositories under https://github.com/Naazimsnh02 , including `gemma-3-finetune` (GRPO on `unsloth/gemma-3-1b-it`) and `gemma-3-tamilnadu_sample`, do not name this 4B counseling checkpoint.
- Dataset page: https://huggingface.co/datasets/Amod/mental_health_counseling_conversations . Created 2023-06-22, last modified 2025-11-25. The file `combined_dataset.json` is listed (4,790,520 bytes). A row count could not be read: the datasets-server and the file URL returned HTTP 401 on 2026-10-06. Size tag on the API: `1K<n<10K`.
- Owner reply on the dataset discussion, 2023-07-20: "the conversations were sourced mainly from https://github.com/nbertagnolli/counsel-chat/tree/master/data". https://huggingface.co/datasets/Amod/mental_health_counseling_conversations/discussions/1

### Training record

**(a) Objective.** Supervised fine-tuning of response tokens. Card says: "Training Approach: Supervised Fine-Tuning (SFT) with response-only masking." Notebook imports `SFTTrainer` and `SFTConfig` and calls `train_on_responses_only` with `response_part = "<start_of_turn>model\n"`. No source names DPO, ORPO, PPO, or a reward model.

**(b) Parameter-update scope.** 4-bit load plus LoRA, then merged. Notebook: `load_in_4bit = True`, `full_finetuning = False`, then `FastModel.get_peft_model` with `r = 16`, `lora_alpha = 32`, `lora_dropout = 0.05`, `finetune_attention_modules = True`, `finetune_mlp_modules = True`, `finetune_vision_layers = False`. README says: "Training Method: LoRA with 4-bit quantization". That is 4-bit base weights plus a LoRA adapter. The card's heading is "Fine-tuning Method: LoRA (Low-Rank Adaptation) - Now Merged" and does not say 4-bit. Save call: `save_pretrained_merged(..., save_method="merged_16bit")`. The Hub repo has full safetensors and no adapter file. The notebook does not list module names such as `q_proj`. The card says "Target Modules: Attention and MLP layers".

**(c) Training data.** Hub id `Amod/mental_health_counseling_conversations`. Notebook markdown and the card both say "3,500" rows and "Context" / "Response". Language on the card: English. The notebook loads `split="train"` and then `train_test_split(test_size=0.1)`. Dataset card says: "a collection of real counselling question-and-answer pairs taken from two public mental-health platforms" and "All personally identifiable information has been removed during curation." It does not name a generator model. The owner's discussion comment says the conversations were sourced mainly from the counsel-chat GitHub data, which is human-written therapist and user text scraped from counselchat.com. The dataset card's "two public mental-health platforms" and that comment are not the same sentence. The live row count was not readable (HTTP 401).

**(d) Base model.** Card YAML and notebook: `unsloth/gemma-3-4b-it`. Card prose: "Base Model: Gemma 3 (4B) Instruct." The acknowledgments also link `google/gemma-3-4b-it`. The YAML base is the Unsloth copy of the instruction-tuned Gemma 3 4B checkpoint, not a pretrained base and not the Unsloth `-bnb-4bit` repo id. The 4-bit load is a flag in the notebook, not a different Hub base id.

**(e) Hyperparameters.** Notebook `SFTConfig`, and the same numbers on the card: 3 epochs, learning rate 2e-4, per-device batch size 2, gradient accumulation 8, effective batch size 16, cosine schedule, warmup ratio 0.1, optimizer `adamw_8bit`, weight decay 0.01, max sequence length 2048, bf16 True, fp16 False, seed 3407. Card: platform Modal, GPU L4, training time 1.27 hours, peak memory reserved 10.37 GB, training memory 5.95 GB. The notebook's last markdown cell says "Training: 5 epochs". The `SFTConfig` in the same notebook sets `num_train_epochs = 3`. The card says 3.

**(f) Evaluation.** Card table of training loss and validation loss every 50 steps from step 50 through step 550. Final validation loss in that table: 1.9974. The notebook's own comment says about 197 steps per epoch on 3,150 training rows, which is about 591 steps for 3 epochs. The published table stops at 550. No external benchmark or clinical score is stated. The card says: "Quantitative evaluation metrics for mental health counseling quality are complex and context-dependent. This model should be evaluated in controlled settings with professional oversight."

### Discrepancies

1. Inventory `methods` is `lora|sft`. That matches the card's words. The notebook also sets `load_in_4bit = True`, which the inventory did not record. Dataset and parent match.
2. The card and the weight-upload commit say float16. The Hub safetensors dtype is BF16. The notebook trains with `bf16 = True` and saves with `merged_16bit`.
3. The notebook's closing summary says 5 epochs. The training config and the card say 3.
4. The card's loss table ends at step 550. The notebook's step arithmetic for 3 epochs is about 591 steps.
5. The card says 3,500 dataset rows. The current file's row count could not be read.

### Confidence

High that this notebook is the script for this checkpoint. The README and the upload cell name `gemma3-4b-mental-health-counseling`, the generated card text matches the Hub card, and the GitHub commit is the same day as the Hub upload. The upload cell still has `HF_USERNAME = "your_username"`, so the committed notebook is the training configuration with a placeholder username, not a log of the push itself.

### Queries tried

- `naazimsnh02 gemma3-4b-mental-health-counseling SFT LoRA`
- `"gemma3-4b-mental-health-counseling" OR "naazimsnh02" mental health`
- `site:github.com gemma3-4b-mental-health-counseling OR naazimsnh02 mental health`
- `"naazimsnh02/gemma3-4b-mental-health-counseling" OR "gemma3-4b-mental-health-counseling" SFT`
- GitHub user repository list for `Naazimsnh02` (35 repos; the counseling notebook is `gemma3-mental-health-counseling`)
- `Amod mental_health_counseling_conversations dataset source synthetic OR scraped counselchat`
- Hub commit that uploaded the merged weights

## 4. prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2

The README is the AutoTrain template and does not name LoRA or a trainer. `training_params.json` and `checkpoint-1107/adapter_config.json` in the same repository do.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/prabureddy__Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2__2026-10-05.md`. Live: https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2 . Created 2024-04-01, last modified 2024-04-03. The card names this repo id. Tags include `autotrain`, `peft`, and `generated_from_trainer`. `model-index` name is `Mental-Health_ML` and `results` is empty.
- Training config stored in the repo: https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/training_params.json . Its `repo_id` field is `prabureddy/Mental-Health_ML`, not the current name string. The Hub API for `prabureddy/Mental-Health_ML` returns this same model (`_id` `660a2d8c9d2edd43f7e0e0f8`).
- Adapter config at the logged checkpoint: https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/checkpoint-1107/adapter_config.json
- Trainer log: https://huggingface.co/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2/raw/main/checkpoint-1107/trainer_state.json . `epoch` 1.0, `global_step` 1107, `max_steps` 1107, `num_train_epochs` 1. No `eval_loss` entries.
- Root files are three safetensors shards, F16, 7,241,732,096 parameters, plus a leftover `checkpoint-1107/adapter_model.safetensors`. No adapter file at the repository root. https://huggingface.co/api/models/prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2
- QuantFactory and mradermacher GGUF repos, and https://model.aibase.com/models/details/1915693637540929537 , repeat the AutoTrain README. Not a second witness.
- A Weights & Biases report, https://wandb.ai/menongautam013/huggingface/reports/Finetuning-Mistral-7B-Instruct-v0-2--Vmlldzo2Mzc1NjUw , is a different Mistral 7B run (3 epochs, LoRA alpha 16). It does not name this repo.
- GitHub search for `prabureddy` plus this model name did not return a training repository. `patrickloeber/mistral-finetune-mental-health` uses the same Amod dataset with Mistral's fine-tuning API and does not name this checkpoint.

### Training record

**(a) Objective.** Supervised fine-tuning. `training_params.json` says `"trainer": "sft"`. It also contains unused preference fields (`dpo_beta`, `rejected_text_column`) with `"model_ref": null`. The selected trainer value is `sft`, not `dpo`. The README says only "This model is a fine-tuned version of" the base "on the mental_health_counseling_conversations dataset."

**(b) Parameter-update scope.** 4-bit load plus LoRA, and the adapter was merged into the uploaded weights. `training_params.json`: `"quantization": "int4"`, `"peft": true`, `"merge_adapter": true`, `"lora_r": 16`, `"lora_alpha": 32`, `"lora_dropout": 0.05`, `"target_modules": null`. `adapter_config.json`: `"peft_type": "LORA"`, `"r": 16`, `"lora_alpha": 32`, `"lora_dropout": 0.05`, `"target_modules": ["q_proj", "v_proj"]`, `"base_model_name_or_path": "mistralai/Mistral-7B-Instruct-v0.2"`. The root parameter count is the full 7B model in F16, which matches `merge_adapter: true`. The adapter weights remain only under `checkpoint-1107/`.

**(c) Training data.** Card YAML and Hub tags: `Amod/mental_health_counseling_conversations`. `training_params.json` does not print that Hub id. It says `"data_path": "Mental-Health/autotrain-data"` and `"train_split": "train"`. Example count: not stated anywhere found. Language and provenance are the dataset card's, quoted in section 3: English, real counseling question-answer pairs from public websites, anonymised, no generator model named. `valid_split` is null.

**(d) Base model.** Card, `training_params.json` `"model"`, and adapter config: `mistralai/Mistral-7B-Instruct-v0.2`. That checkpoint is the instruction-tuned Mistral 7B v0.2, not the base pretrained model. The card does not add that sentence; the base model's own card does, and the id contains `Instruct`.

**(e) Hyperparameters.** `training_params.json`: `"epochs": 1`, `"lr": 0.00015`, `"batch_size": 2`, `"gradient_accumulation": 1`, `"mixed_precision": "fp16"`, `"optimizer": "adamw_torch"`, `"scheduler": "cosine"`, `"warmup_ratio": 0.05`, `"weight_decay": 0.001`, `"block_size": 512`, `"model_max_length": 1024`, `"seed": 42`. The trainer log agrees: 1 epoch, 1,107 steps. Hardware: not stated anywhere found.

**(f) Evaluation.** Not stated anywhere found. `model-index` `results` is an empty list. `evaluation_strategy` in the JSON is `"epoch"`, and `valid_split` is null. The trainer log has training loss only (last logged training loss 0.0028 at step 1,100). No eval loss.

### Discrepancies

1. Inventory `methods` is empty. The README does not name a trainer. `training_params.json` says `sft` with `int4` and `peft`. Inventory `datasets` and `parent` match the card.
2. The JSON `repo_id` is `prabureddy/Mental-Health_ML`. That name resolves to this same Hub model. The current repository name is longer.
3. `target_modules` is null in `training_params.json` and is `q_proj` and `v_proj` in the saved adapter config.
4. The README does not mention LoRA. The files do.

### Confidence

High that these JSON files describe this upload. They are stored in this repository, the adapter's base id matches, the checkpoint directory name is the logged step 1,107, and `prabureddy/Mental-Health_ML` is the same Hub `_id`.

### Queries tried

- `prabureddy Mental-Health-FineTuned-Mistral-7B-Instruct AutoTrain`
- `"Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2" OR "prabureddy" mental health`
- `site:github.com "Mental-Health-FineTuned-Mistral-7B" OR "prabureddy" AutoTrain mental health`
- `"prabureddy/Mental-Health-FineTuned-Mistral-7B-Instruct-v0.2" training_params OR lora`
- Hub discussions page for this model (no training thread)
- `prabureddy/Mental-Health_ML` on the Hub API (same model id)
- The unrelated WandB Mistral report above, checked and set aside

## 5. ryefoxlime/gemma-2-2b-it-therapist

This repository's own card is the empty Hub template. The training script is in the same user's other repository, `ryefoxlime/TADBot`. The script saves an adapter named `gemma-2-2b-ft`. It does not print `ryefoxlime/gemma-2-2b-it-therapist`. A model file in TADBot points at a local GGUF whose filename is also a file in this repository.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/ryefoxlime__gemma-2-2b-it-therapist__2026-10-05.md`. Live: https://huggingface.co/ryefoxlime/gemma-2-2b-it-therapist . Created 2024-11-15, last modified 2024-11-20. YAML names `google/gemma-2-2b-it` and `nbertagnolli/counsel-chat`. The body is the automatic template ("More Information Needed"). Hub relation field says `quantized` of `google/gemma-2-2b-it`. Files: two F16 safetensors shards (2,614,341,888 parameters) and `gemma-2-2b-it-therapist-Q4_K_M.gguf`. No `adapter_config.json`.
- Same user's project repo: https://huggingface.co/ryefoxlime/TADBot . Created 2024-03-14, last modified 2024-12-13. Hugging Face user page names Nitin Kausik Remella. https://huggingface.co/ryefoxlime
- README: https://huggingface.co/ryefoxlime/TADBot/raw/main/README.md . It does not print `ryefoxlime/gemma-2-2b-it-therapist`.
- Notebook: https://huggingface.co/ryefoxlime/TADBot/blob/main/Gemma2_2B/finetune.ipynb
- YAML: https://huggingface.co/ryefoxlime/TADBot/raw/main/Gemma2_2B/hyperparams.yaml . `new_model_name: "gemma-2-2b-ft"`.
- Saved adapter: https://huggingface.co/ryefoxlime/TADBot/raw/main/Gemma2_2B/gemma-2-2b-ft/adapter_config.json . Its README is the empty PEFT template.
- Ollama model file: https://huggingface.co/ryefoxlime/TADBot/raw/main/Gemma2_2B/gemma-2-2b-therapy.modelfile . It says `FROM /home/TADBot/TADBot/Gemma2_2B/gemma-2-2b-it-therapist/gemma-2-2b-it-therapist-Q4_K_M.gguf`. That filename is a file in this Hub repo. The model file does not print the `ryefoxlime/` prefix.
- GitHub repository search for `gemma-2-2b-it-therapist OR TADBot ryefoxlime` returned 0 repositories.
- Featherless https://featherless.ai/models/ryefoxlime/gemma-2-2b-it-therapist describes a "2.6 billion parameter instruction-tuned model" and does not cite the notebook. It is a hosting blurb, not a training log. The base Gemma 2 2B is already instruction-tuned; this sentence does not say whether the therapy training was a further fine-tune.

### Training record

**(a) Objective.** Supervised fine-tuning. The notebook imports `SFTTrainer` and constructs it with `dataset_text_field="text"`. The YAML section is commented `#SFT Arguments`. The formatted text is a system line, a user question, and a response, from `questionText` and `answerText`. No source names DPO, ORPO, PPO, or a reward model.

**(b) Parameter-update scope.** 4-bit NF4 plus LoRA. YAML: `use_4bit: True`, `bnb_4bit_quant_type: "nf4"`, `bnb_4bit_compute_dtype: "float16"`, `use_nested_quant: False`, `lora_r: 64`, `lora_alpha: 16`, `lora_dropout: 0.1`. Notebook `LoraConfig` target modules: `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`. `down_proj` is not in that list. `adapter_config.json` matches rank 64, alpha 16, dropout 0.1, and those six modules. README says: "The fine tuned lora adapters are then merged with the base model to give the final model" and "pushed to the Hugging Face model hub". The notebook's last code cell only calls `trainer.model.save_pretrained(hyperparams["new_model_name"])`, which writes the adapter directory `gemma-2-2b-ft`. The merge call is not in the notebook. This Hub repo is full F16 weights plus a Q4 GGUF and has no adapter file.

**(c) Training data.** Notebook: `dataset_name = "nbertagnolli/counsel-chat"` and `load_dataset(dataset_name, split="train")`, then `train_test_split(test_size=0.2, seed=42)`. Datasets-server: 2,775 train rows. An 80/20 split of 2,775 rows is 2,220 train and 555 test; the notebook prints the shapes and the saved output was not in the file. README says: "The raw version of the dataset consists of 2275 conversation". That number is not the current datasets-server count. Provenance is the counsel-chat card quoted in section 1: English, scraped from counselchat.com on 2022-04-01, written by licensed counselors and anonymous users. Not synthetic.

**(d) Base model.** YAML `model_name` and adapter config: `google/gemma-2-2b-it`. This repo's YAML lists the same id. That checkpoint is Google's instruction-tuned Gemma 2 2B. The TADBot README says "Gemma 2 2B" and does not print the `-it` id; the YAML does.

**(e) Hyperparameters.** YAML, and the notebook passes these into `TrainingArguments`: 1 epoch, learning rate 2e-4, per-device batch size 2, gradient accumulation 2, optimizer `paged_adamw_32bit`, weight decay 0.001, max gradient norm 0.3, warmup 5 steps, scheduler `constant`, max sequence length 128, packing True. README lists the same learning rate, batch size, accumulation, epochs, and optimizer, and says "weight decay: 0.01". The YAML value used by the notebook is 0.001. Hardware: not stated anywhere found. The README discusses a Raspberry Pi only for inference.

**(f) Evaluation.** The notebook sets `eval_strategy: "steps"` and an eval split. No metric values are in the notebook output, the TADBot README, or this model's card. Not stated anywhere found.

### Discrepancies

1. Inventory `methods` is empty, which matches this repo's empty card. The TADBot notebook is QLoRA supervised fine-tuning. Inventory `datasets` and `parent` match both YAML blocks.
2. The Hub relation on this repo says `quantized` of `google/gemma-2-2b-it`. The repository also contains full F16 weights. The relation label is not a training method.
3. README weight decay 0.01 versus YAML and notebook 0.001. README row count 2,275 versus datasets-server 2,775.
4. The notebook saves `gemma-2-2b-ft` and does not merge. The README says the adapters were merged and pushed. This repo's files look like a merged full model plus a GGUF, and the TADBot model file loads a GGUF with this repo's filename.

### Confidence

Medium that the TADBot notebook is the run behind this checkpoint. Same author, same base id, same dataset, and the TADBot model file loads `gemma-2-2b-it-therapist-Q4_K_M.gguf`, which is a file here. The notebook never prints the Hub id, and it saves a different local name (`gemma-2-2b-ft`).

### Queries tried

- `ryefoxlime gemma-2-2b-it-therapist counsel-chat`
- `"gemma-2-2b-it-therapist" OR "ryefoxlime" therapist fine-tune`
- `site:github.com ryefoxlime TADBot gemma-2-2b-it-therapist counsel-chat`
- `"gemma-2-2b-it-therapist" TAD.py OR lora OR "ryefoxlime/TADBot"`
- GitHub repository search `gemma-2-2b-it-therapist OR TADBot ryefoxlime` (0 hits)
- Hugging Face user page for `ryefoxlime` (Nitin Kausik Remella), then the TADBot file list
- Featherless model page, checked against the TADBot notebook

## Patterns in this batch

None of these five runs is preference optimization or reinforcement learning. Where a trainer is named, it is supervised fine-tuning on counseling or therapy replies. Three of the scripts that could be read train a LoRA adapter on a 4-bit base and then describe a merge: the Gemma 3 notebook, the Mistral AutoTrain JSON, and the art-therapy adapter card. The Gemma 3 card still says "LoRA" and "float16," while the notebook sets `load_in_4bit = True` and the Hub dtype is BF16. The suicide-prevention card is the one record that does not settle the method: it says "LoRA adapters or 4-bit quantization," calls the step count an example, and the upload is a full BF16 Llama with no adapter file. Two models cite `Amod/mental_health_counseling_conversations` and two cite `nbertagnolli/counsel-chat`, which is human-written text scraped from counselchat.com. The art-therapy corpus is the only one whose card names a generator model (`gpt-5-nano`). Inventory rows match the YAML base and the YAML dataset, and they leave the method blank when the README is an AutoTrain stub or an empty template.
