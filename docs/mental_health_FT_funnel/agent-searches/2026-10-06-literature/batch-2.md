# Batch 2: how five mental-health fine-tunes were trained

Date of search: 2026-10-06. Cards read: the 2026-10-05 copies under `revision_3_experiments/hf_inventory/cache/readmes/`. Inventory row: `revision_3_experiments/hf_inventory/results/mental-health/archive/2026-10-06/kept.csv`. Hub file lists: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__018.csv` (Navanjana) and `2026-10-05__019.csv` (the other four). None of the five uploads contains `adapter_config.json`.

A claim below is tied to a URL or a cached file. If a field is missing from every source that was found, it is marked "not stated anywhere found." A method word inside a dataset name is not treated as the training method.

## Summary

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Matches inventory row |
|---|---|---|---|---|---|---|
| Navanjana/gemma-3-finetune-therapist | none | not stated | not stated | `IINOVAII/therapy-conversations-combined`, 208,548 rows, provenance not stated | `unsloth/gemma-3-270m-it` (instruction-tuned Gemma 3 270M) | yes |
| Sanjay002/tinyllama-mental-health-finetuned | none | not stated | not stated | `heliosbrahma/mental_health_chatbot_dataset`, 172 rows, human-written web FAQs | `TinyLlama/TinyLlama-1.1B-Chat-v1.0` (chat checkpoint) | yes |
| ShivomH/Elixir-MentalHealth-3B | code | supervised next-token training on chat messages (SFT) | QLoRA (4-bit NF4 + LoRA rank 16, alpha 32); author calls the upload merged | `ShivomH/MentalHealth-Support`, 25,000 English conversations, synthetic | `meta-llama/Llama-3.2-3B-Instruct` | partly |
| ShivomH/Falcon3-1B-MentalHealth | none | not stated | LoRA rank 16 on an 8-bit load; card says the adapter was merged | `marmikpandya/mental-health`, 13,358 rows, provenance not stated | `tiiuae/Falcon3-1B-Instruct` | yes |
| Someet24/empathetic-qwen3-8b-Jan | code (JSON in this Hub repo; no paper, no GitHub script) | card says multi-task SFT; the logged run has language-model loss only | QLoRA, then merged. Rank 16 and alpha 16 are on a sibling adapter repo | three crowdsourced English sets; this run's config targets 6,000 train rows | `Qwen/Qwen3-8B` (post-trained, not the Base checkpoint) | partly |

## 1. Navanjana/gemma-3-finetune-therapist

No paper, thesis, blog, or training script was found for this upload. The model card is the Unsloth/TRL upload template. A GGUF repo only repackages the weights.

### Sources

- Cached model card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/Navanjana__gemma-3-finetune-therapist__2026-10-05.md`. It is this repo's own card.
- Live card, same text: https://huggingface.co/Navanjana/gemma-3-finetune-therapist . Hub metadata in `2026-10-05__018.csv`: created 2025-11-03, relation `finetune` of `unsloth/gemma-3-270m-it`. Files: `model.safetensors` and tokenizer files. No `adapter_config.json`.
- Dataset page: https://huggingface.co/datasets/IINOVAII/therapy-conversations-combined . README body is empty apart from `language: en` and `license: mit`. Viewer: 208,548 rows. The page names this model under "Models trained or fine-tuned on" this dataset. That line does not add a training method.
- Quantized copy: https://huggingface.co/mradermacher/gemma-3-finetune-therapist-GGUF says "static quants of https://huggingface.co/Navanjana/gemma-3-finetune-therapist". It does not describe training.
- Upstream base card: https://huggingface.co/unsloth/gemma-3-270m-it lists `base_model: google/gemma-3-270m-it`. https://huggingface.co/google/gemma-3-270m-it says Gemma 3 has "instruction-tuned variants" and prints a table for "Gemma 3 IT 270m".
- Hugging Face user page https://huggingface.co/Navanjana lists linked names `Navanjana19` and `Navanjana2005`. A GitHub search for those names plus this model returned no training repository.

No source other than this repo's card names the training run. The dataset page names the repo id as a model trained on the dataset.

### Training record

**(a) Objective.** Not stated anywhere found. Card says: "Uploaded finetuned model" and "This gemma3_text model was trained 2x faster with Unsloth and Huggingface's TRL library." TRL can run several trainers. The card does not name `SFTTrainer`, DPO, ORPO, or a reward model. Inventory `methods` is empty.

**(b) Parameter-update scope.** Not stated anywhere found. The upload is one BF16 `model.safetensors` (Hub safetensors count in the live page: 268,098,176 parameters) and there is no `adapter_config.json`. That file list does not say whether every weight was trained or a LoRA adapter was merged before upload. Rank, alpha, and target modules: not stated anywhere found.

**(c) Training data.** Card YAML: `datasets: IINOVAII/therapy-conversations-combined`. The dataset viewer reports 208,548 rows and columns `instruction`, `input`, `output` (https://datasets-server.huggingface.co/rows?dataset=IINOVAII/therapy-conversations-combined&config=default&split=train&offset=0&length=1). README YAML: `language: en`. Provenance: not stated anywhere found. The README body is empty. A third-party blurb at https://nerq.ai/dataset/therapy-conversations-combined says "An AI agent for therapy conversations" and does not say who wrote the rows. Row 0 is the same three strings as the first row shown on https://huggingface.co/datasets/marmikpandya/mental-health (`instruction` "If you are a licensed psychologist...", `input` "I'm feeling really anxious lately and I don't know why."). That match does not say where the other 208,547 rows came from. A Turkish translation, https://huggingface.co/datasets/ozertuu/therapy-conversations-combined-translated-tr, says it translated this dataset with `Helsinki-NLP/opus-mt-tc-big-en-tr`. That is a later translation, not the training run.

**(d) Base model.** Card says: "Finetuned from model : unsloth/gemma-3-270m-it". That id is an Unsloth copy of `google/gemma-3-270m-it`. Google's card treats the `-it` checkpoint as the instruction-tuned 270M model, next to a separate pretrained checkpoint. This upload's card does not itself use the words "instruction-tuned."

**(e) Hyperparameters.** Not stated anywhere found. No epochs, learning rate, batch size, or hardware on the card.

**(f) Evaluation.** Not stated anywhere found.

### Discrepancies

1. Inventory `methods` is empty. That agrees with the card: no objective and no LoRA/QLoRA word. Inventory `datasets` and `parent` match the card.
2. The uploaded weights are a full BF16 file. The card does not say full fine-tuning or a merged adapter. Those are different procedures, and neither is stated.

### Confidence

Low that any source besides this repo's card describes the run. The card is the card of this upload, and it does not say how the weights were updated.

### Queries tried

- `Navanjana/gemma-3-finetune-therapist`
- `gemma-3-finetune-therapist Navanjana unsloth`
- `IINOVAII/therapy-conversations-combined`
- `site:github.com gemma-3-finetune-therapist OR "therapy-conversations-combined" Navanjana`
- `"Navanjana" gemma therapist OR "gemma-3-270m-it" therapy conversations`
- `site:github.com/Navanjana2005 gemma OR therapist OR therapy`
- `"therapy-conversations-combined" OR "IINOVAII" therapy conversations dataset`

## 2. Sanjay002/tinyllama-mental-health-finetuned

No paper, thesis, blog, or training script was found. The model card body is empty. The YAML names the base model and one dataset.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/Sanjay002__tinyllama-mental-health-finetuned__2026-10-05.md`. YAML only.
- Live card: https://huggingface.co/Sanjay002/tinyllama-mental-health-finetuned . Hub metadata in `2026-10-05__019.csv`: created 2025-04-10, last modified 2025-08-21, relation `finetune` of `TinyLlama/TinyLlama-1.1B-Chat-v1.0`. Files: `model.safetensors` (the live file tree lists 4.4 GB) and tokenizer files. No `adapter_config.json`. Safetensors dtype on the inventory row: F32, 1,100,048,384 parameters.
- Dataset card: https://huggingface.co/datasets/heliosbrahma/mental_health_chatbot_dataset . Viewer: 172 train rows. This card describes the dataset. It does not describe Sanjay002's trainer.
- Featherless listing: https://featherless.ai/models/Sanjay002/tinyllama-mental-health-finetuned . It repeats "fine-tuned" and the dataset id. It adds no trainer name, rank, or learning rate. Treat it as a paraphrase of the card, not a second witness.
- A later adapter, https://huggingface.co/usama011/tinyllama-mental-health-fine-tuned-11, says it is "a fine-tuned version of Sanjay002/tinyllama-mental-health-finetuned" and lists PEFT 0.14.0, learning rate 2e-05, and 10 epochs. That is a further run on top of these weights. It is not the recipe for this checkpoint.
- Base-model card: https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0 says "This is the chat model finetuned on top of TinyLlama/TinyLlama-1.1B-intermediate-step-1431k-3T" and describes that chat model's own UltraChat SFT plus DPO. Those steps belong to TinyLlama, not to Sanjay002.

### Training record

**(a) Objective.** Not stated anywhere found. The card has no training section. Inventory `methods` is empty. The TinyLlama card's DPO sentence is about the base chat model.

**(b) Parameter-update scope.** Not stated anywhere found. The upload is one full F32 `model.safetensors` and there is no `adapter_config.json`. Rank, alpha, target modules, and whether an adapter was merged: not stated anywhere found.

**(c) Training data.** Card YAML: `datasets: heliosbrahma/mental_health_chatbot_dataset`. Dataset card says: "This dataset contains conversational pair of questions and answers in a single text related to Mental Health. Dataset was curated from popular healthcare blogs like WebMD, Mayo Clinic and HeatlhLine, online FAQs etc. All questions and answers have been anonymized to remove any PII data." Viewer: 172 rows, one field `text`. Language on the model-card YAML: `en`. The dataset card does not use the word English; the examples are English. Provenance: human-written pages on those sites, then anonymized. The dataset card does not name a generator model. It also says "Questions were asked by the patients and answers were given by healthcare providers" while the source line says the text was curated from blogs and FAQs. Those two sentences are both on the dataset card. They describe published FAQ text, not a recorded clinic session and not a model-written corpus.

**(d) Base model.** Card YAML: `base_model: TinyLlama/TinyLlama-1.1B-Chat-v1.0`. The TinyLlama card calls that checkpoint "the chat model," produced by SFT and then DPO, as quoted above. It is not the intermediate pretrained checkpoint.

**(e) Hyperparameters.** Not stated anywhere found for this checkpoint. The learning rate and epoch count on `usama011/tinyllama-mental-health-fine-tuned-11` are a later run.

**(f) Evaluation.** Not stated anywhere found for this checkpoint.

### Discrepancies

1. Inventory `methods` is empty, `datasets` is `heliosbrahma/mental_health_chatbot_dataset`, and `parent` is `TinyLlama/TinyLlama-1.1B-Chat-v1.0`. That matches the card.
2. Featherless and the GGUF-style hosting blurbs do not add a method. They should not be counted as confirmation.

### Confidence

Low that any source besides this repo's YAML describes the run. The YAML names the base model and the dataset and does not name a trainer.

### Queries tried

- `"Sanjay002/tinyllama-mental-health-finetuned"`
- `tinyllama-mental-health-finetuned Sanjay`
- `heliosbrahma/mental_health_chatbot_dataset TinyLlama`
- `site:github.com Sanjay002 tinyllama mental health finetuned`
- `"tinyllama-mental-health-finetuned" OR "Sanjay002" TinyLlama mental_health_chatbot`
- `"mental_health_chatbot_dataset" TinyLlama fine-tune OR SFT OR LoRA`
- TinyLlama chat-model card (one hop from `base_model`), to separate the base model's DPO from this upload

## 3. ShivomH/Elixir-MentalHealth-3B

No paper was found. The author published a GitHub repository whose README points at this repo id, plus two LinkedIn posts. The README repeats the model card. The notebook is the training record. The dataset card is a separate account of where the conversations came from.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/ShivomH__Elixir-MentalHealth-3B__2026-10-05.md`. Live page: https://huggingface.co/ShivomH/Elixir-MentalHealth-3B . Hub metadata: created 2025-09-26, last modified 2025-10-01. Files are two safetensors shards and an index. No `adapter_config.json`.
- GitHub README: https://github.com/Shivom2003/Elixir-MentalHealth-v2 . Created 2025-09-28, last push 2025-10-14, author `Shivom2003`. The README copies the model card, including the inference snippet `model_path = "ShivomH/Elixir-MentalHealth-3B"`. Because it copies the card, it is not a second witness for the hyperparameter table.
- Training notebook: https://github.com/Shivom2003/Elixir-MentalHealth-v2/blob/master/Fine-Tune%20Scripts/Elixir-MentalHealth-Finetune.ipynb . The opening markdown says the notebook fine-tunes Llama-3.2-3B-Instruct on `ShivomH/MentalHealth-Support`. The code sets `dataset_name` to the placeholder `"enter_dataset_name"`. The notebook does not print `ShivomH/Elixir-MentalHealth-3B`.
- Preprocess script in the same repo: https://github.com/Shivom2003/Elixir-MentalHealth-v2/blob/master/Preprocessing/MH_Synthetic_Preprocess.py . It cleans a local `MH_Synthetic.jsonl`. It does not name the Hub dataset id.
- Sibling adapter repo: https://huggingface.co/ShivomH/Elixir-MentalHealth-LoRA . Card says: "This is just a LoRA Adapter, please navigate to ShivomH/Elixir-MentalHealth-3B to access the merged model." Its `adapter_config.json` is at https://huggingface.co/ShivomH/Elixir-MentalHealth-LoRA/raw/main/adapter_config.json . That file does not contain the string `ShivomH/Elixir-MentalHealth-3B`. The card does.
- Dataset card: https://huggingface.co/datasets/ShivomH/MentalHealth-Support . It names the two upstream datasets. It does not name the model id in the fetched text.
- Author posts: https://www.linkedin.com/posts/shivom-hatalkar_ai-llm-ml-activity-7381984703391633409-8fde (2025-10-09) and https://www.linkedin.com/posts/shivom-hatalkar_ai-ml-llm-activity-7383812129440575489-tIjF (2025-10-14). The indexed text says "Elixir-v2" and does not print `ShivomH/Elixir-MentalHealth-3B`; the second post points at a shortened Hugging Face link.
- Author site snippet: https://shivomai.in/ calls the project Elixir-v2, "23.7K Training Dialogues," RTX 3090, QLoRA. The fetched snippet does not print the repo id.
- Upstream papers and posts for the data, not for this training run: MentalChat16K, https://arxiv.org/html/2503.13509 ; Jerry Jalapeno, https://medium.com/@jerryjalapeno/training-ai-therapists-ca4b0454672c , for `jerryjalapeno/nart-100k-synthetic`.

No arXiv, PubMed, or ACL paper was found that names Elixir or Shivom Hatalkar as the author of this fine-tune. A search for "Hatalkar" on arXiv returned unrelated QLoRA papers.

### Training record

**(a) Objective.** Supervised next-token training on chat-formatted conversations. The notebook imports `SFTTrainer` and then does not use it. The cell that trains is `trainer = Trainer(...)`. `preprocess_function` sets `labels` to a copy of `input_ids`, with pad tokens replaced by `-100`. Script says: "Mask padding token positions (-100 tells HF Trainer to ignore them in loss)". The loss is therefore the causal language-model loss on every non-padding token, including the user turns. The card does not use the word SFT. It says "adapted using QLoRA." No DPO, ORPO, PPO, or reward model appears in the notebook. Inventory `methods` is `qlora` only.

**(b) Parameter-update scope.** QLoRA. Card says: "Training Technique: Peft - QLoRA" and "Trainable Parameters: 24,313,856 (1.33%)". Script says `load_in_4bit=True`, `bnb_4bit_quant_type="nf4"`, `bnb_4bit_use_double_quant=True`, `bnb_4bit_compute_dtype=torch.bfloat16`, then `LoraConfig` with `r=16`, `lora_alpha=32`, `lora_dropout=0.05`, and `target_modules` `q_proj`, `v_proj`, `k_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`. The sibling `adapter_config.json` has the same rank, alpha, dropout, target modules, `peft_type` `LORA`, `task_type` `CAUSAL_LM`, and `base_model_name_or_path` `meta-llama/Llama-3.2-3B-Instruct`.

Merged: the LoRA card says this 3B repo is "the merged model." The 3B file list is full weights, not an adapter. The notebook's merge cell is optional: `merge_model = input("Do you want to merge LoRA with base model? (y/n): ")`. The script does not record that the prompt was answered yes. The 3B card also says "only ~93MB adapter needs to be loaded," while its own usage code loads `AutoModelForCausalLM` from `ShivomH/Elixir-MentalHealth-3B`.

**(c) Training data.** Card says: "Dataset Source: ShivomH/MentalHealth-Support", "Size: 25,000 conversations", "Training Split: 23,750 (95%)", "Validation Split: 1,250 (5%)", "Multi-Turn Conversations: 16,000", "Long Single-Turn Conversations: 8,000", "Short Single-Turn Conversations: 1,000", "Language(s) (NLP): English". Dataset card says: "This dataset is entirely synthetic." It also says "Generation Method for Single-Turn: OpenAI GPT-3.5 Turbo model with a customized Airoboros self-generation framework" and "Sources: Long Single-Turn: ShenLab/MentalChat16K. Multi-Turn: jerryjalapeno/nart-100k-synthetic". The dataset card's own bullets say 8,000 single-turn and 16,000 multi-turn, which add to 24,000, while the total line says 25,000. The short 1,000 are on the model card and are not given a source id on the dataset card.

MentalChat16K paper says: "we used the OpenAI GPT-3.5 Turbo (OpenAI, 2024b) model to generate 9,775 question-answer pairs with a customized adaptation of the Airoboros self-generation framework." The same paper's interview half is real caregiver transcripts paraphrased by Mistral-Instruct. The Elixir dataset card cites MentalChat16K only as the long single-turn source and states the GPT-3.5 / Airoboros method for single-turn rows. It does not say the interview half was included. Jerry Jalapeno's post says the nart-100k corpus is "100k synthetic conversations ... generated by gpt-3.5-turbo." The nart dataset card itself says "this dataset is entirely synthetic" and does not name the generator in the fetched text. Hatalkar's preprocess script does not name either upstream id.

The notebook splits whatever dataset is loaded with `test_size=0.05`, which matches the card's 95/5 split, but the Hub id in code is the placeholder `"enter_dataset_name"`.

**(d) Base model.** Card and script: `meta-llama/Llama-3.2-3B-Instruct`. The id is the instruction-tuned checkpoint. `adapter_config.json` on the LoRA repo has the same `base_model_name_or_path`.

**(e) Hyperparameters.** Card: max sequence length 1024, LoRA rank 16, alpha 32, NF4, bfloat16, `paged_adamw_32bit`, learning rate 3e-5, warmup ratio 0.05, effective batch size 32, 4 epochs, LoRA dropout 0.05. Hardware: "Nvidia RTX 3090 (24 GB VRAM)", "Training Hours: 17 hours", Runpod. Script: `per_device_train_batch_size` 8, `gradient_accumulation_steps` 4 (effective 32), `lr_scheduler_type` `"cosine"`, `gradient_checkpointing` True, seed 42. LinkedIn (2025-10-09) says: "Trained on RunPod.io (RTX 3090, 24 GB VRAM) using QLoRA (nf4 + double quant)" and "Epochs 4 | Batch 8 | Grad Accum 4 → Effective 32 | LR 3e-5 | Max Seq 1024". That post is the author restating the notebook's per-device batch, which the model card only gives as an effective batch of 32.

**(f) Evaluation.** The model card prints BERTScore, ROUGE-L, METEOR, Distinct-1, Distinct-2, Self-BLEU, perplexity, and a toxicity min/mean/max, for this model and for Llama-3.2-3B-Instruct, gemma-2-2b-it, and Qwen2.5-3B-Instruct. Elixir row: BERTScore F1 0.884, ROUGE-L 0.252, perplexity 2.572, toxicity mean 0.0021. The 2025-10-14 LinkedIn post repeats BERTScore F1 0.884, ROUGE-L 0.253, and toxicity 0.0021. ROUGE-L is 0.252 on the card and 0.253 in the post. The repo also contains `Evaluation_Scripts/LLM-Evaluation.py`. This note does not re-run it. The MentalChat16K paper's QLoRA experiments are the paper authors' own 7B runs, not this 3B checkpoint.

### Discrepancies

1. Inventory `methods` is `qlora`. The notebook is QLoRA plus causal-LM `Trainer`. The inventory row does not record SFT. Datasets and parent match.
2. The 3B card says a ~93MB adapter is what you load. The same card's code loads the full `ShivomH/Elixir-MentalHealth-3B` weights. The file list has no adapter file. The LoRA card calls the 3B repo the merged model. The notebook leaves merging to an interactive prompt.
3. Trainable-parameter arithmetic: 24,313,856 at 1.33% implies about 1.83 billion parameters. The LinkedIn post says "24.3 M / 1.83 B params". The base id is `Llama-3.2-3B-Instruct`.
4. Conversation counts: model card 8,000 + 16,000 + 1,000 = 25,000. Dataset card bullets list 8,000 single-turn and 16,000 multi-turn and still say the total is 25,000.
5. The notebook's `dataset_name` is `"enter_dataset_name"`. The markdown cell and the model card name `ShivomH/MentalHealth-Support`.
6. LinkedIn ROUGE-L 0.253 versus the card's 0.252.
7. The GitHub README is a copy of the model card, so it does not independently confirm the table.

### Confidence

High that this notebook and this card are the author's account of `ShivomH/Elixir-MentalHealth-3B`: the README loads that id, and rank, alpha, learning rate, epochs, NF4, and the 3090 match. Medium on the exact data file, because the code path still contains the placeholder dataset name.

### Queries tried

- `ShivomH/Elixir-MentalHealth-3B QLoRA`
- `Shivom Hatalkar Elixir-MentalHealth-v2`
- `site:arxiv.org Hatalkar mental health Llama QLoRA`
- `"Elixir-MentalHealth" OR "Elixir-v2" Hatalkar fine-tune paper`
- GitHub contents API for `Shivom2003/Elixir-MentalHealth-v2`, then the fine-tune notebook and `MH_Synthetic_Preprocess.py`
- `ShivomH/MentalHealth-Support` dataset card
- MentalChat16K HTML (https://arxiv.org/html/2503.13509) and Jerry Jalapeno's nart-100k post (one hop from the dataset card's source line)

## 4. ShivomH/Falcon3-1B-MentalHealth

No paper and no training script were found. The model card is the only account of this run. Two earlier Hatalkar repos, `ShivomH/Falcon-1B-Mental-Health-v1` and `ShivomH/Falcon-1B-Mental-Health-v2`, fine-tune `tiiuae/falcon-rw-1b`, not Falcon3. Their hyperparameter tables are similar and are not this checkpoint.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/ShivomH__Falcon3-1B-MentalHealth__2026-10-05.md`. Live page: https://huggingface.co/ShivomH/Falcon3-1B-MentalHealth . Hub metadata: created 2025-02-05, last modified 2025-02-13. Files: one `model.safetensors`. No `adapter_config.json`. The card names this repo id in the usage snippet.
- Dataset page: https://huggingface.co/datasets/marmikpandya/mental-health . "No dataset card yet." Viewer: 13,358 rows, columns `input`, `instruction`, `output`. The page lists this model under models trained on the dataset. That line does not add a method.
- GGUF copy: https://huggingface.co/mradermacher/Falcon3-1B-MentalHealth-GGUF says "static quants of" this repo. Not a training record.
- Different model, same author and same dataset name: https://huggingface.co/ShivomH/Falcon-1B-Mental-Health-v1 . It says the adapter is for `falcon-rw-1b` and must be loaded with PEFT. Batch size on that card is 1, not 2. Do not copy those settings onto Falcon3.
- Base card: https://huggingface.co/tiiuae/Falcon3-1B-Instruct says this Falcon3 checkpoint was "Posttrained on 1.2 million samples of STEM, conversational, code, safety and function call data." That sentence is about TII's post-training, which the inventory row quotes. It is not Hatalkar's fine-tune.
- A GitHub search for `Shivom2003` plus Falcon3, and for `marmikpandya/mental-health`, did not return a script for this repo. Other Falcon mental-health notebooks (Falcon-7B, heliosbrahma's QLoRA post) name different models and different datasets.

### Training record

**(a) Objective.** Not stated anywhere found. The card says "fine-tuned" and "LoRA adapter." It does not name SFT, DPO, ORPO, PPO, or a trainer class. The dataset columns are `instruction`, `input`, and `output`. Column names are not a trainer. Inventory `methods` is `lora`, which is the update scope, not an objective.

**(b) Parameter-update scope.** LoRA, not QLoRA. Card says: "This is a LoRA adapter for the Falcon3-1B-Instruct LLM which has been merged with the respective base model." The table says "Quantization | 8-Bit", "LoRA Rank | 16", "LoRA Dropout | 0.1". QLoRA in the taxonomy used here is a 4-bit base plus LoRA. This card says 8-bit. Alpha and target modules: not stated anywhere found. Merged: the card says merged, and the upload is a full `model.safetensors` with no `adapter_config.json`. The v1 Falcon-RW card, by contrast, tells the user to load an adapter with PEFT. This Falcon3 card's usage code loads `AutoModelForCausalLM` from `ShivomH/Falcon3-1B-MentalHealth`.

**(c) Training data.** Card says it "was fine-tuned on the 'marmikpandya/mental-health' dataset." Hub viewer: 13,358 rows. Language: the model card says "Language(s) (NLP): English." The dataset has no card, so the dataset page does not state a language. Provenance: not stated anywhere found. There is no dataset card, and no paper was found for `marmikpandya/mental-health`. The first viewer row is the same psychologist-instruction example as row 0 of `IINOVAII/therapy-conversations-combined`. That is a shared example, not a stated source.

**(d) Base model.** Card YAML: `base_model: tiiuae/Falcon3-1B-Instruct`. Card says: "Since it is fine-tuned on an Instruct model..." The TII card calls this checkpoint post-trained, as quoted above. It is not `Falcon3-1B-Base`.

**(e) Hyperparameters.** Card table: precision float16, optimizer `AdamW_32bit`, learning rate 2e-4, weight decay 1e-2, batch size 2, 3 epochs, 8-bit quantization, LoRA dropout 0.1, LoRA rank 16, warmup ratio 0.03. Hardware: not stated anywhere found.

**(f) Evaluation.** Not stated anywhere found. The card has no metric table.

### Discrepancies

1. Inventory `methods` is `lora`, `datasets` is `marmikpandya/mental-health`, and `parent` is `tiiuae/Falcon3-1B-Instruct`. That matches the card. The inventory does not record 8-bit or the merge. The card does.
2. The card's title still says "This is a LoRA adapter" in the same paragraph that says the adapter "has been merged." The files are merged weights.
3. `Falcon-1B-Mental-Health-v1` and `v2` are easy to mix with this repo. They use `falcon-rw-1b`. v1's batch size is 1. Those numbers are not this checkpoint.

### Confidence

Medium. The card is the card of this repo and the file list matches a merged model, but no script or paper was found that restates the table.

### Queries tried

- `"ShivomH/Falcon3-1B-MentalHealth"`
- `Falcon3-1B-MentalHealth Shivom Hatalkar LoRA`
- `marmikpandya/mental-health dataset Falcon fine-tune`
- `site:github.com Shivom2003 Falcon3 OR "Falcon3-1B-MentalHealth" OR "marmikpandya/mental-health"`
- `"Falcon3-1B-Instruct" "lora" "2e-4" Hatalkar OR Shivom mental-health`
- Falcon-1B-Mental-Health-v1 and v2 cards (same author, different base model)
- `tiiuae/Falcon3-1B-Instruct` model card (one hop from `base_model`)

## 5. Someet24/empathetic-qwen3-8b-Jan

No paper, thesis, or GitHub training script was found. The model repo itself contains `training_config.json` and `training_history.json`. A sibling repo, `Someet24/empathetic-qwen3-8b`, is the unmerged LoRA. Featherless repeats the model card and is not a second witness.

### Sources

- Cached card, 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/Someet24__empathetic-qwen3-8b-Jan__2026-10-05.md`. Live page: https://huggingface.co/Someet24/empathetic-qwen3-8b-Jan . Hub metadata: created and last modified 2026-01-10. Files include four safetensors shards, `training_config.json`, `training_history.json`, and `training_curves.png`. No `adapter_config.json`. `config.json` has `architectures: ["Qwen3ForCausalLM"]`, `unsloth_fixed: true`, `unsloth_version: "2026.1.2"`.
- `training_config.json`: https://huggingface.co/Someet24/empathetic-qwen3-8b-Jan/raw/main/training_config.json . The JSON body does not contain the string `Someet24/empathetic-qwen3-8b-Jan`. It is stored in that repo.
- `training_history.json`: https://huggingface.co/Someet24/empathetic-qwen3-8b-Jan/raw/main/training_history.json . Same: the body does not print the repo id.
- Sibling LoRA card: https://huggingface.co/Someet24/empathetic-qwen3-8b . It does not, in the fetched text, name `empathetic-qwen3-8b-Jan`. It says "This model is a LoRA fine-tune of Qwen3-8B" and "Base Model: Qwen3-8B (4-bit quantized)". Its `adapter_config.json`: https://huggingface.co/Someet24/empathetic-qwen3-8b/raw/main/adapter_config.json . Hub tags on that sibling include `base_model:unsloth/Qwen3-8B-bnb-4bit`. The config file's `base_model_name_or_path` is `unsloth/qwen3-8b-bnb-4bit` (lowercase).
- Hugging Face user https://huggingface.co/Someet24 (Someet Sahoo) links GitHub `Someet-Git`. https://github.com/Someet-Git has no repository whose name or description is this model.
- Featherless: https://featherless.ai/models/Someet24/empathetic-qwen3-8b-Jan repeats the card ("QLoRA with Unsloth", "merged"). Not an independent witness.
- Base card: https://huggingface.co/Qwen/Qwen3-8B says "Training Stage: Pretraining & Post-training". https://huggingface.co/Qwen/Qwen3-8B-Base says "Training Stage: Pretraining". The Jan card's base id is `Qwen/Qwen3-8B`, not the Base repo.
- Dataset papers, which describe the full public corpora, not this 6,000-row cut: EmpatheticDialogues, https://arxiv.org/pdf/1811.00207 ; ESConv, https://github.com/thu-coai/Emotional-Support-Conversation and https://huggingface.co/datasets/thu-coai/esconv ; GoEmotions, https://huggingface.co/datasets/google-research-datasets/go_emotions and https://arxiv.org/abs/2005.00547 .

### Training record

**(a) Objective.** The card says: "Method: Multi-task SFT with auxiliary emotion & strategy heads". `training_config.json` in the same repo says `"use_auxiliary_heads": false`, `"lambda_lm": 1.0`, `"lambda_emo": 0.1`, `"lambda_strat": 0.1`. `training_history.json` has non-zero `lm_loss` and `train_loss`, and `emotion_loss` and `strategy_loss` are 0 for every logged step. `config.json` is `Qwen3ForCausalLM` only. There is no classification head in the uploaded config. The logged run is language-model supervised training. The auxiliary-head loss was configured and not used. No DPO, ORPO, PPO, or reward model is named. Inventory `methods` is `qlora|sft`, taken from the card sentence, including the auxiliary-head clause.

**(b) Parameter-update scope.** Card says: "Training: QLoRA with Unsloth optimization, then merged" and "Standalone merged model - No base model needed!" The Jan repo has full shards and no `adapter_config.json`. Rank and alpha are not in the Jan card or in `training_config.json`. They are in the sibling adapter file: `"peft_type": "LORA"`, `"r": 16`, `"lora_alpha": 16`, `"lora_dropout": 0`, `"task_type": "CAUSAL_LM"`, target modules `q_proj`, `k_proj`, `v_proj`, `o_proj`, `gate_proj`, `up_proj`, `down_proj`, `base_model_name_or_path` `unsloth/qwen3-8b-bnb-4bit`. That is a 4-bit base plus LoRA, which is QLoRA, on the sibling repo. The Jan card says the adapter was merged. It does not say the sibling repo is the adapter that was merged. Both cards list the same three datasets, QLoRA, Unsloth, and a Kaggle T4, and both were updated on 2026-01-10. That is the reason to connect them. It is not a statement printed in either file that one is the merge of the other.

**(c) Training data.** Card lists EmpatheticDialogues, ESConv (`thu-coai/esconv`), and GoEmotions (`google-research-datasets/go_emotions`). Card language: English. `training_config.json`: `"limit_per_dataset": 2000`, `"target_train_size": 6000`, `"target_val_size": 500`. Those are targets in the config, not a count of rows after filtering. The full corpora are larger, and this config does not say the targets were met:

- EmpatheticDialogues paper says "24,850 conversations" gathered from 810 participants, crowdsourced. The Hub copy `facebook/empathetic_dialogues` splits utterances as 76,673 train, 12,030 validation, 10,943 test. The Jan card writes `empathetic_dialogues`, not `facebook/empathetic_dialogues`.
- ESConv GitHub README says "ESConv now contains 1,300 conversations." The Hub dataset `thu-coai/esconv` is tagged English. A cap of 2,000 cannot be filled from 1,300 conversations if each row is one conversation. The config does not say how a "dataset" was counted.
- GoEmotions dataset card says "58k carefully curated Reddit comments labeled for 27 emotion categories or Neutral." The paper says the comments were annotated by crowdworkers. The simplified split on the card is 43,410 / 5,426 / 5,427. GoEmotions is emotion labels on comments, not support dialogues. The card lists it as training data. The config does not say whether those rows were turned into chat text.

Provenance of the three public sets: crowdsourced human text, not a generator model. The Jan card does not say the 6,000-row cut was rewritten by another model.

**(d) Base model.** Jan card: "Base Model: Qwen3-8B" and YAML `base_model: Qwen/Qwen3-8B`. That checkpoint's own card says pretraining and post-training. `Qwen/Qwen3-8B-Base` is the pretraining-only repo. The sibling adapter was loaded from `unsloth/qwen3-8b-bnb-4bit`, and the sibling card says "Qwen3-8B (4-bit quantized)". The Jan card does not print the Unsloth 4-bit id. `config.json` on the Jan repo has `unsloth_version` `2026.1.2`.

**(e) Hyperparameters.** Not on the card. `training_config.json`: `max_seq_length` 512, `learning_rate` 5e-05, `batch_size` 1, `gradient_accumulation_steps` 16, `num_epochs` 2, `warmup_steps` 100, `max_grad_norm` 0.5. Card hardware: "Kaggle T4 GPU". The sibling card says the same hardware and does not add epochs or a learning rate. `training_history.json` logs a learning rate that rises to 5e-05 and then decays, and five validation losses from about 0.974 to 0.956.

**(f) Evaluation.** No benchmark table on the card. The history file logs training loss and five validation losses. It does not name the validation set beyond `target_val_size` 500 in the config. Emotion and strategy losses stay at 0.

### Discrepancies

1. Inventory `qlora|sft` matches the card's "QLoRA" and "SFT". The inventory evidence string also includes "auxiliary emotion & strategy heads." The JSON in the same repo turns those heads off, and the logged emotion and strategy losses are 0. The uploaded `config.json` has no extra heads.
2. LoRA rank 16 and alpha 16 are on `Someet24/empathetic-qwen3-8b`, not in the Jan card or `training_config.json`. The Jan card says merged and does not name that sibling.
3. Jan card base id `Qwen/Qwen3-8B`. Sibling `base_model_name_or_path` `unsloth/qwen3-8b-bnb-4bit`.
4. Card `max` length is not stated. The sibling usage example uses `max_seq_length=1024`. `training_config.json` says 512.
5. Featherless repeats the card, including the auxiliary-head sentence, and does not mention `use_auxiliary_heads: false`.

### Confidence

Medium. `training_config.json` and `training_history.json` are files in this repo, so they belong to this upload. The LoRA rank is only on the sibling repo, and neither repo prints a sentence that says the Jan weights are the merge of that adapter.

### Queries tried

- `"Someet24/empathetic-qwen3-8b-Jan"`
- `empathetic-qwen3-8b-Jan Someet QLoRA SFT`
- `Someet Sahoo empathetic Qwen3 github kaggle`
- `site:kaggle.com Someet empathetic Qwen3 OR "empathetic-qwen3"`
- `site:github.com/Someet-Git` (user page; no matching repository)
- Raw `training_config.json`, `training_history.json`, Jan `config.json`, and sibling `adapter_config.json`
- EmpatheticDialogues paper, ESConv GitHub README, GoEmotions dataset card (one hop from the three dataset names)
- `Qwen/Qwen3-8B` versus `Qwen/Qwen3-8B-Base` training-stage lines

## Patterns in this batch

Two of the five uploads, Navanjana's Gemma 270M and Sanjay002's TinyLlama, have no training section at all. The inventory leaves `methods` empty, and no paper or script turned up to fill it. The weights are full files with no `adapter_config.json`, which still does not say whether the author trained every weight or merged an adapter.

Where a method is written down, it is supervised training with a low-rank adapter, not preference optimization or reinforcement learning. Elixir's notebook is 4-bit NF4 plus LoRA and a causal language-model `Trainer`. Falcon3's card is 8-bit plus LoRA, which is not 4-bit QLoRA, and it never names the trainer. Someet's card says QLoRA and multi-task SFT; the JSON stored next to the weights shows the auxiliary losses at zero.

The data stories diverge. Elixir's 25,000 conversations are described as synthetic, with GPT-3.5 Turbo named for the single-turn slice and for the upstream nart-100k multi-turn set. Sanjay002's 172 rows are anonymized text from health-site FAQs. Someet's three named corpora are crowdsourced, and the config's 6,000-row target is much smaller than those corpora. Navanjana's 208,548-row set and Falcon3's 13,358-row set have no provenance statement. The first example on both pages is the same psychologist-instruction triple.

Every base id in this batch is an instruction or post-trained checkpoint (`-it`, `-Chat`, `-Instruct`, or Qwen3-8B rather than Qwen3-8B-Base). None of the five cards reports a preference-optimization step on top of that. Elixir is the only one with a metric table. Falcon3, Navanjana, and Sanjay002 report none. Someet logs validation loss only.
