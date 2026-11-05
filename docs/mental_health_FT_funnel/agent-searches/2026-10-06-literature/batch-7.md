# Batch 7: how four mental-health models were trained

Cached cards read: newest README under `revision_3_experiments/hf_inventory/cache/readmes/` (2026-10-05). Inventory row: `revision_3_experiments/hf_inventory/results/mental-health/archive/2026-10-06/kept.csv`. Hub file lists: `revision_3_experiments/hf_inventory/cache/cards/2026-10-05__021.csv` and `2026-10-05__022.csv`. None of the four repositories contains `adapter_config.json`. Each uploaded checkpoint has the same parameter count as the base model named on its card. That match is what a full fine-tune, a merged adapter, or an unchanged copy would all look like. No source says which of those three this file is.

| Model | Publication or code found | Objective | Update scope | Data (name, n, provenance) | Base | Matches inventory row |
| --- | --- | --- | --- | --- | --- | --- |
| sirev/Qlora-lfm2-700m-mental-health | none | not stated (name contains Qlora) | not stated | MentalChat16K: 9,775 GPT-3.5 Turbo pairs plus 6,338 paraphrased interview pairs (16,113 in the paper; Hub viewer 16,084); English | LiquidAI/LFM2-700M (post-trained) | partly |
| sshl505/Hermes_2_Pro_Mistral_7B_Counsellor | none | not stated | not stated | empathetic_dialogues_llm: 24,850 English dialogues; human crowdsourced, reformatted | NousResearch/Hermes-2-Pro-Mistral-7B (instruction-tuned) | yes |
| sujalrajpoot/TrueSyncAI-Aurion | none | not stated (card says fine-tuned, not the loss) | LoRA, as the card states; Hub tags the repo as a quantization | TrueSyncAI-Aurion: 1,258,251 rows; no dataset card; provenance not stated | Qwen/Qwen2.5-3B-Instruct (instruction-tuned) | partly |
| zbt566666/qwen2.5-7b-mental-therapy-lora-sft | none | not stated (name contains sft) | not stated (name contains lora) | mental_health_therapy: 12,258 rows; counsel-chat forum text plus ChatGPT, drawn from three Hub datasets | Qwen/Qwen2.5-7B-Instruct (instruction-tuned) | partly |

## 1. sirev/Qlora-lfm2-700m-mental-health

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/sirev__Qlora-lfm2-700m-mental-health__2026-10-05.md`. The body is the Hugging Face auto template. It names this repo only in the file path, not in a training paragraph. Author: not stated. Hub user page https://huggingface.co/sirev lists the repo and does not link a paper or a GitHub account.
- Hub API, retrieved 6 Oct 2026: https://huggingface.co/api/models/sirev/Qlora-lfm2-700m-mental-health . Created 2025-08-12, last modified 2025-08-12. Tag `base_model:finetune:LiquidAI/LFM2-700M`. Tag `dataset:ShenLab/MentalChat16K`. Tag `arxiv:1910.09700`. Siblings: `model.safetensors` and tokenizer files. No `adapter_config.json`. Safetensors: F16, 742,489,344 parameters.
- `config.json`: https://huggingface.co/sirev/Qlora-lfm2-700m-mental-health/raw/main/config.json . `model_type` `lfm2`, `torch_dtype` `float16`, `transformers_version` `4.55.0`. No LoRA keys.
- Dataset card: https://huggingface.co/datasets/ShenLab/MentalChat16K . Does not name this repo.
- Paper, arXiv 2503.13509v2 HTML, retrieved 6 Oct 2026: https://arxiv.org/html/2503.13509v2 . Authors: Jia Xu, Tianyi Wei, Bojian Hou, Patryk Orzechowski, Shu Yang, Ruochen Jin, Rachael Paulbeck, Joost Wagenaar, George Demiris, Li Shen. Does not name `sirev/Qlora-lfm2-700m-mental-health` or LFM2. The QLoRA section is their own 7B runs.
- Base-model card: https://huggingface.co/LiquidAI/LFM2-700M/raw/main/README.md . Does not name this repo. Parameter count on that card: 742,489,344. Hub API safetensors for the base: BF16, same total.
- GGUF and ONNX copies: https://huggingface.co/mradermacher/Qlora-lfm2-700m-mental-health-GGUF says "static quants of https://huggingface.co/sirev/Qlora-lfm2-700m-mental-health". https://huggingface.co/Iam314rock/Qlora-lfm2-700m-mental-health-ONNX has an empty README. Neither states a training method. They are not a second witness.

### Training record

**(a) Objective.** Not stated anywhere found. The auto card's training section says "[More Information Needed]". Name contains Qlora. That is the repository name, not a statement of the loss. The MentalChat16K paper's QLoRA runs are a different set of models. Paper says: "We use QLoRA to fine-tune four state-of-the-art light-weight (7B) LLMs" and later names LLaMA-2-7B, Vicuna-7B-V1.5, Mistral-7B-v0.1, Mistral-7B-Instruct-v0.2, Mixtral-8x7B-v0.1, Mixtral-8x7B-Instruct-v0.1, and Zephyr-7B-Alpha. https://arxiv.org/html/2503.13509v2

**(b) Parameter-update scope.** Not stated anywhere found. No rank, alpha, or target modules. Hub siblings are one `model.safetensors` file. No `adapter_config.json`. Uploaded count is 742,489,344 F16 parameters, the same count the LFM2-700M card prints for the base (stored there as bfloat16). Whether an adapter was merged is not stated.

**(c) Training data.** Card YAML: `datasets: ShenLab/MentalChat16K`. The prose training-data section is still "[More Information Needed]". The Hub page heading is "Dataset used to train sirev/Qlora-lfm2-700m-mental-health". Dataset card says the synthetic part is "9,775 synthetic conversations" "generated using the OpenAI GPT-3.5 Turbo model" and the interview part is "6338 question-answer pairs from 378 interview transcripts" paraphrased with "the local Mistral-7B-Instruct-v0.2 model". Language on that card: "Language: English". Paper says 9,775 GPT-3.5 Turbo pairs plus 6,338 paraphrased pairs, 16,113 in total. The dataset page viewer, retrieved 6 Oct 2026, says 16,084 rows. The interview text started as human clinical transcripts; the released interview pairs are Mistral paraphrases. The other part is synthetic, generator GPT-3.5 Turbo.

**(d) Base model.** Card YAML and Hub API: `LiquidAI/LFM2-700M`. The auto-template line "Finetuned from model [optional]: [More Information Needed]" is unfilled. The base card says: "We're releasing the weights of four post-trained checkpoints with 350M, 700M, 1.2B, and 2.6B parameters." Its training approach for LFM2 is "Knowledge distillation using LFM1-7B as teacher model", "Very large-scale SFT", "Custom DPO with length normalization and semi-online datasets", and "Iterative model merging". That is the base checkpoint's own post-training. It is an instruction-style checkpoint, not a raw pre-trained dump. Those sentences do not describe sirev's upload.

**(e) Hyperparameters.** Not stated anywhere found for this checkpoint. The MentalChat16K appendix is their 7B QLoRA recipe, not this file. Paper says: "We fine-tuned each model over five epochs, using a batch size of 64" and "We set the LoRA hyperparameters as follows: r=64, alpha=16, and dropout=0.1" on "a single NVIDIA A100 GPU (80 GB)", with `learning_rate` 0.0002 in Appendix A.9. https://arxiv.org/html/2503.13509v2

**(f) Evaluation.** Not stated anywhere found for this checkpoint. The tag `arxiv:1910.09700` is the Lacoste et al. carbon-calculator citation inside the auto template, not an evaluation of this model. The MentalChat16K scores are for the 7B models named in that paper.

### Discrepancies

1. Inventory `methods` is `qlora` with evidence `qlora: name qlora`. No card sentence, script, or paper says this checkpoint was trained with QLoRA.
2. Inventory `parent_class_evidence` quotes "We're releasing the weights of four post-trained checkpoints with 350M, 700M, 1.2B, and 2.6B parameters." That sentence is on the Liquid AI base card. It is not a description of this upload.
3. The paper's QLoRA settings (rank 64, alpha 16, 5 epochs, batch 64, learning rate 0.0002, one A100) are for seven other models. The paper does not name this repo.
4. Dataset card and paper say 16,113 pairs. The Hub viewer says 16,084 rows.
5. Uploaded weights are float16. The base card's precision row for LFM2-700M is bfloat16. The parameter count matches.

### Confidence

Low. The YAML names the dataset and the base model, and nothing found describes a training run of this repository id.

### Queries tried

- `sirev/Qlora-lfm2-700m-mental-health`
- `"Qlora-lfm2-700m-mental-health"`
- `sirev LFM2 mental health QLoRA MentalChat16K`
- `github sirev Qlora-lfm2 OR "sirev" LFM2 mental-health site:github.com` (hits were SIAM Review code, not this model)
- `"Qlora-lfm2" OR "LFM2-700M" MentalChat16K fine-tuning arxiv`
- Hub API `https://huggingface.co/api/models/sirev/Qlora-lfm2-700m-mental-health` and raw `config.json`
- MentalChat16K arXiv HTML `https://arxiv.org/html/2503.13509v2` and the dataset card
- Liquid AI LFM2-700M README
- Hugging Face user page `https://huggingface.co/sirev`

## 2. sshl505/Hermes_2_Pro_Mistral_7B_Counsellor

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/sshl505__Hermes_2_Pro_Mistral_7B_Counsellor__2026-10-05.md`. Names the model in the title. Author on the Hub user page: SongHarim (`sshl505`). https://huggingface.co/sshl505 . One model, zero datasets, no linked paper.
- Hub API cache row in `2026-10-05__021.csv`: created 2025-04-06, last modified 2025-04-06. Tag `base_model:finetune:NousResearch/Hermes-2-Pro-Mistral-7B`. Tag `dataset:Estwld/empathetic_dialogues_llm`. Safetensors: F32, 7,241,994,240 parameters. Siblings are six `model-0000N-of-00006.safetensors` shards. No `adapter_config.json`.
- `config.json`: https://huggingface.co/sshl505/Hermes_2_Pro_Mistral_7B_Counsellor/raw/main/config.json . `MistralForCausalLM`, `torch_dtype` `float32`, `vocab_size` 32032, `transformers_version` `4.50.3`. No LoRA keys.
- Dataset card: https://huggingface.co/datasets/Estwld/empathetic_dialogues_llm . Does not name this repo. It says the file is a reformat of Empathetic Dialogues.
- Original dataset paper, arXiv 1811.00207 HTML: https://arxiv.org/html/1811.00207 . Authors: Hannah Rashkin, Eric Michael Smith, Margaret Li, Y-Lan Boureau. Does not name this repo. It describes the 2019 human dialogue collection, not this checkpoint.
- Base-model card: https://huggingface.co/NousResearch/Hermes-2-Pro-Mistral-7B/raw/main/README.md . Does not name this repo. Hub API safetensors for the base: BF16, 7,241,994,240 parameters.
- GGUF copy: https://huggingface.co/mradermacher/Hermes_2_Pro_Mistral_7B_Counsellor-GGUF says "static quants of" this repo. It does not add a training method.

Other training write-ups use `Estwld/empathetic_dialogues_llm` on other bases (Llama 3.1 8B in https://github.com/wothmag07/counseLLM , Llama 3.2 3B in https://github.com/chetnapriyadarshini/Thesis_PeFT ). They do not name `sshl505/Hermes_2_Pro_Mistral_7B_Counsellor`.

### Training record

**(a) Objective.** Not stated anywhere found. Card says: "This model is specialized for emotional and psychological support dialogue generation." It does not say supervised fine-tuning, preference optimization, or reinforcement learning. The base card's tags include `DPO`, `RLHF`, and `distillation`. Those tags are on `NousResearch/Hermes-2-Pro-Mistral-7B`. They are not a statement about a further counsellor run.

**(b) Parameter-update scope.** Not stated anywhere found. No rank, alpha, or target modules. No `adapter_config.json`. The upload is a full Mistral checkpoint in float32, 7,241,994,240 parameters, the same count as the bfloat16 Hermes-2-Pro checkpoint. Whether an adapter was merged is not stated.

**(c) Training data.** Card YAML: `datasets: Estwld/empathetic_dialogues_llm`, `language: en`. The only prose is the one sentence in (a). Dataset card says it "contains a reformatted version of the Empathetic Dialogues dataset" and lists the reformat steps (merge by `conv_id`, alternate `user` and `assistant`). Hub page: 24,850 rows. The same card's turn table is Train 84,167 turns, Validation 12,077, Test 10,972. Those are turns, not the 24,850 dialogue rows. Rashkin et al. say: "The new resource consists of crowdsourced one-on-one conversations" and "a novel dataset with about 25k personal dialogues." https://arxiv.org/html/1811.00207 . Provenance: human-written crowdsourced dialogues, then reformatted. No generator model.

**(d) Base model.** Card YAML and Hub tag: `NousResearch/Hermes-2-Pro-Mistral-7B`. That checkpoint is instruction-tuned. Its card says: "Hermes 2 Pro is an upgraded, retrained version of Nous Hermes 2, consisting of an updated and cleaned version of the OpenHermes 2.5 Dataset, as well as a newly introduced Function Calling and JSON Mode dataset." Its own `base_model` is `mistralai/Mistral-7B-v0.1`. The parent of this counsellor repo is the Hermes instruction checkpoint, not the raw Mistral pre-trained checkpoint.

**(e) Hyperparameters.** Not stated anywhere found. No epochs, learning rate, batch size, or hardware for this repo.

**(f) Evaluation.** Not stated anywhere found for this checkpoint. The GPT4All, AGIEval, function-calling, and JSON-mode numbers are on the Hermes-2-Pro card.

### Discrepancies

1. Inventory `methods` is empty. That matches what the card states: no training objective and no update scope.
2. The base card's `DPO`, `RLHF`, and `distillation` tags describe Hermes 2 Pro. The counsellor card does not say those methods were run again.
3. This upload is float32. The base Hub safetensors are bfloat16. The parameter count matches.

### Confidence

Low. The card names a base model and a dataset, and no paper or script describes a training run of this repository id.

### Queries tried

- `"sshl505/Hermes_2_Pro_Mistral_7B_Counsellor" OR "Hermes_2_Pro_Mistral_7B_Counsellor"`
- `sshl505 counsellor Hermes-2-Pro-Mistral empathetic_dialogues`
- `"SongHarim" OR sshl505 Hermes counsellor OR "Hermes_2_Pro_Mistral" site:github.com` (hits were Nous Hermes agent docs, not this model)
- `"SongHarim" OR "Song Harim" counsellor OR "empathetic_dialogues_llm" fine-tune`
- `"Hermes_2_Pro_Mistral_7B_Counsellor" OR "Hermes 2 Pro Mistral 7B Counsellor" SongHarim`
- Dataset card `Estwld/empathetic_dialogues_llm` and arXiv HTML `1811.00207`
- Hermes-2-Pro README and this repo's `config.json`
- Hugging Face user page `https://huggingface.co/sshl505`

## 3. sujalrajpoot/TrueSyncAI-Aurion

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/sujalrajpoot__TrueSyncAI-Aurion__2026-10-05.md`. Names `sujalrajpoot/TrueSyncAI-Aurion`. Author on the card: Sujal Rajpoot and TrueSyncAI Team. Card date in the citation block: 2026.
- Hub API, retrieved 6 Oct 2026: https://huggingface.co/api/models/sujalrajpoot/TrueSyncAI-Aurion . Created 2026-05-08, last modified 2026-05-09. Tags include `unsloth` and `base_model:quantized:Qwen/Qwen2.5-3B-Instruct`. Card YAML `base_model` is `Qwen/Qwen2.5-3B-Instruct`. Safetensors: BF16, 3,085,938,688 parameters. Same total as the Hub API row for `Qwen/Qwen2.5-3B-Instruct`. Siblings include two safetensors shards and `qwen2.5-3b-instruct.F16.gguf`, `qwen2.5-3b-instruct.Q8_0.gguf`, `qwen2.5-3b-instruct.Q4_K_M.gguf`. No `adapter_config.json`.
- `config.json`: https://huggingface.co/sujalrajpoot/TrueSyncAI-Aurion/raw/main/config.json . Includes `"unsloth_fixed": true` and `"unsloth_version": "2026.5.2"`. `torch_dtype` is `float16`. The safetensors summary is BF16.
- `Modelfile`: https://huggingface.co/sujalrajpoot/TrueSyncAI-Aurion/raw/main/Modelfile . `FROM qwen2.5-3b-instruct.Q8_0.gguf`. System line: "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
- Dataset page: https://huggingface.co/datasets/sujalrajpoot/TrueSyncAI-Aurion . "No dataset card yet." Row count on that page: 1,258,251. Created 2025-11-02, which is before the model repo's 2026-05-08 creation date. Does not describe a training run.
- GitHub profile: https://github.com/sujalrajpoot . The dataset-generator README https://github.com/sujalrajpoot/LLM-Finetuning-Dataset-Generator/blob/main/README.md describes a general tool that fills empty `output` fields through API calls. It does not name `sujalrajpoot/TrueSyncAI-Aurion` or a LoRA run. The Hugging Face Space https://huggingface.co/spaces/sujalrajpoot/TrueSyncAI-Aurion is the empty Gradio template.
- Featherless page https://featherless.ai/models/sujalrajpoot/TrueSyncAI-Aurion repeats the card's overview. It is not a second witness.
- Base card: https://huggingface.co/Qwen/Qwen2.5-3B-Instruct/raw/main/README.md . "This repo contains the instruction-tuned 3B Qwen2.5 model." Does not name Aurion.

### Training record

**(a) Objective.** Not stated as a loss. Card says: "This model was fine-tuned using Unsloth, achieving 2x faster training compared to traditional methods." It does not say supervised next-token training, DPO, ORPO, KTO, SimPO, PPO, GRPO, or reinforcement learning. "2x faster" is Unsloth's own advertising line. The GitHub generator is not this training run.

**(b) Parameter-update scope.** Card says: "Training Framework: Unsloth + LoRA" and "Memory-efficient fine-tuning with gradient checkpointing." No rank, alpha, or target modules. No `adapter_config.json`. The upload is a full Qwen2 checkpoint, BF16, 3,085,938,688 parameters, the same count as `Qwen/Qwen2.5-3B-Instruct`. Whether an adapter was merged is not stated. The Hub tag on this repo is `base_model:quantized:Qwen/Qwen2.5-3B-Instruct`, not `base_model:finetune`. `config.json` records that Unsloth 2026.5.2 wrote the config (`unsloth_fixed`, `unsloth_version`). That is a software stamp. It is not a sentence that says LoRA weights were trained.

**(c) Training data.** Card YAML and prose: `sujalrajpoot/TrueSyncAI-Aurion`. Card says: "Custom curated multilingual corpus with emotional intelligence focus" and "The model was trained on the sujalrajpoot/TrueSyncAI-Aurion dataset, which includes: Emotionally nuanced conversations, Multi-turn dialogues, Reasoning-based Q&A, Multilingual interactions, Technical and creative writing samples." No example count on the card. Dataset page: 1,258,251 rows, 502 MB, no dataset card. Dataset API siblings: `Couples-Conversation.json`, `EmotionalIntelligence-155K.json`, `Higlish-Conversations.json`, `Human-Conversations.json`, `Human-Feedback-Conversations.json`, `Supperficial-Romantic-Conversation.json`, `TER.json`. The first bytes of each file are `instruction` / `input` / `output` JSON. Card YAML language codes: en, zh, fr, es, pt, de, it, ru, ja, ko, vi, th, ar, hi. The card also says "29+ languages". Sampled rows include English, Hinglish in Latin script, and Hindi mixed with English. Provenance (human-written versus synthetic, and any generator): not stated anywhere found. The first instruction in `Supperficial-Romantic-Conversation.json` is "Do you believe in love at first sight?", the same question shown on https://huggingface.co/datasets/G0dM0deG0d/supperficial-Romantic-Text-Romance . The filename uses that dataset's spelling `supperficial`. That is one shared opening line, not a checksum of the file.

**(d) Base model.** Card table: "Base Model | Qwen2.5-3B-Instruct". YAML: `Qwen/Qwen2.5-3B-Instruct`. The Qwen card says this id "contains the instruction-tuned 3B Qwen2.5 model" and "Training Stage: Pretraining & Post-training". Its own parent is `Qwen/Qwen2.5-3B`.

**(e) Hyperparameters.** Epochs, learning rate, and batch size: not stated anywhere found. Card says: "Hardware: Optimized for consumer-grade GPUs." No GPU name.

**(f) Evaluation.** Card section "Performance Benchmarks" lists Sentiment Analysis 92.3% accuracy, Emotion Recognition 89.7% accuracy, Empathetic Response Generation 4.6/5.0 human rating, Logical Reasoning 87.1% accuracy, Multi-step Problem Solving 84.5% success rate, Context Maintenance (10+ turns) 91.2% coherence, Translation Quality 88.3% BLEU score (average), Cross-lingual Understanding 86.9% accuracy. No test set, sample size, or judge protocol is stated. The architecture row on the same card, "Transformers with RoPE, SwiGLU, RMSNorm, Attention QKV bias, tied word embeddings", repeats the Qwen2.5-3B-Instruct card's architecture sentence. The Qwen card does not contain these percentages.

### Discrepancies

1. Inventory `methods` is `lora`, taken from the card sentence "Unsloth + LoRA". The card does say LoRA. The Hub tag on the same repo is `base_model:quantized:Qwen/Qwen2.5-3B-Instruct`.
2. The card's usage system prompt is "You are TrueSyncAI-Aurion, created by TrueSyncAI." The shipped `Modelfile` system line and the tokenizer chat template are "You are Qwen, created by Alibaba Cloud. You are a helpful assistant."
3. `config.json` says `torch_dtype` float16. The safetensors summary is BF16.
4. GGUF filenames are `qwen2.5-3b-instruct.*`, not Aurion.
5. The card calls the corpus custom. There is no dataset card, and one JSON file opens with the same question as `G0dM0deG0d/supperficial-Romantic-Text-Romance`.
6. Parameter count 3,085,938,688 matches `Qwen/Qwen2.5-3B-Instruct`. No `adapter_config.json`.

### Confidence

Low. The card is written for this repo id and says Unsloth plus LoRA, and the Hub classifies the same repo as a quantization of Qwen2.5-3B-Instruct.

### Queries tried

- `"TrueSyncAI-Aurion" sujalrajpoot fine-tune OR LoRA OR Unsloth`
- `sujalrajpoot TrueSyncAI Aurion github training LoRA`
- `"TrueSyncAI" Aurion Rajpoot arxiv OR thesis OR "unsloth_version"`
- `"EmotionalIntelligence-155K" OR "Higlish-Conversations" OR "Supperficial-Romantic-Conversation" huggingface`
- Hub API for the model and for dataset `sujalrajpoot/TrueSyncAI-Aurion`
- Raw `config.json` and `Modelfile`
- `https://github.com/sujalrajpoot/LLM-Finetuning-Dataset-Generator` README
- Qwen2.5-3B-Instruct README
- Featherless model page and the Hugging Face Space

## 4. zbt566666/qwen2.5-7b-mental-therapy-lora-sft

### Sources

- Model card, cached 2026-10-05: `revision_3_experiments/hf_inventory/cache/readmes/zbt566666__qwen2.5-7b-mental-therapy-lora-sft__2026-10-05.md`. YAML only. No prose. Author: Hub display name zbt, also the string `zbt2702160239` on https://huggingface.co/zbt566666 . One model, zero datasets.
- Hub cache row in `2026-10-05__022.csv`: created 2024-12-26, last modified 2024-12-26. Tag `base_model:finetune:Qwen/Qwen2.5-7B-Instruct`. Tag `dataset:fadodr/mental_health_therapy`. Languages `en` and `zh`. Safetensors: BF16, 7,615,616,512 parameters. Same total as the Hub API row for `Qwen/Qwen2.5-7B-Instruct`. Siblings are four `model-0000N-of-00004.safetensors` shards. No `adapter_config.json`.
- `config.json`: https://huggingface.co/zbt566666/qwen2.5-7b-mental-therapy-lora-sft/raw/main/config.json . `"_name_or_path": "/home/simple/qwen-2.5/qwen2.5-7b-instruct"`, `torch_dtype` `bfloat16`, `transformers_version` `4.46.1`. No LoRA keys.
- Dataset card: https://huggingface.co/datasets/fadodr/mental_health_therapy . Does not name this repo. The "models trained or fine-tuned" text captured from that page names `haphazardlyinc/TestModelV1`, not this id. `fadodr/finetuned_mental_health_therapy_original` is a different checkpoint: its card says "Finetuned from model : unsloth/llama-3-8b-bnb-4bit" and "trained 2x faster with Unsloth and Huggingface's TRL library." https://huggingface.co/fadodr/finetuned_mental_health_therapy_original
- Base card: https://huggingface.co/Qwen/Qwen2.5-7B-Instruct/raw/main/README.md . "This repo contains the instruction-tuned 7B Qwen2.5 model." "Number of Parameters: 7.61B." Does not name this repo.

A GitHub search for the repo id returned other Qwen therapy projects (Cognivia, Psy-Insight, PsychCoT-Tuning, a Qwen Llama-Factory example). None of them names `zbt566666/qwen2.5-7b-mental-therapy-lora-sft`.

### Training record

**(a) Objective.** Not stated anywhere found. Name contains sft. The card has no training paragraph. The local path in `config.json` shows the file was saved from a directory named `qwen2.5-7b-instruct`. It does not state a loss.

**(b) Parameter-update scope.** Not stated anywhere found. Name contains lora. No rank, alpha, or target modules. No `adapter_config.json`. The upload is a full Qwen2 checkpoint, BF16, 7,615,616,512 parameters, the same count as `Qwen/Qwen2.5-7B-Instruct`. Whether an adapter was merged is not stated.

**(c) Training data.** Card YAML: `datasets: fadodr/mental_health_therapy`, `language: en` and `zh`. Dataset card says: "This dataset is a combination of a real-therapy conversation from a conselchat forum and a synthetic discussion generated with chatGpt." It lists three sources: `nbertagnolli/counsel-chat`, `Amod/mental_health_counseling_conversations`, and `ShenLab/MentalChat16K`. Hub page: 12,258 rows. Columns: `instruction`, `input`, `output`. The instruction string on the viewer is the MentalChat counseling prompt. Language is not tagged on the dataset card. The viewer rows on that page are English. The model card's `zh` tag is not explained. Provenance, as the dataset card states it: forum counseling text plus ChatGPT. The card writes "chatGpt" and does not name a model version. This dataset card describes the dataset. It does not say zbt566666 trained on it beyond the model card's YAML link.

**(d) Base model.** Card YAML and Hub tag: `Qwen/Qwen2.5-7B-Instruct`. The Qwen card says that repo is the instruction-tuned 7B model, "Training Stage: Pretraining & Post-training", parent `Qwen/Qwen2.5-7B`. `config.json` `_name_or_path` is `/home/simple/qwen-2.5/qwen2.5-7b-instruct`.

**(e) Hyperparameters.** Not stated anywhere found. No epochs, learning rate, batch size, or hardware.

**(f) Evaluation.** Not stated anywhere found.

### Discrepancies

1. Inventory `methods` is `lora|sft` with evidence `lora: name lora; sft: name sft`. No card sentence, script, or paper says either method.
2. The upload has the same parameter count as `Qwen/Qwen2.5-7B-Instruct` and has no `adapter_config.json`.
3. Model YAML lists languages `en` and `zh`. The dataset card does not state Chinese, and the viewer rows on the dataset page are English.
4. `fadodr/finetuned_mental_health_therapy_original` is an Unsloth plus TRL Llama 3 8B checkpoint. It is not this Qwen repo. Its training sentence must not be copied onto this file.

### Confidence

Low. The YAML names a dataset and a base model, the config path points at a local Qwen2.5-7B-Instruct directory, and no source states a training objective for this repository id.

### Queries tried

- `"qwen2.5-7b-mental-therapy-lora-sft" OR zbt566666 mental therapy`
- `fadodr/mental_health_therapy Qwen2.5 LoRA SFT`
- `"mental-therapy-lora-sft" OR "zbt566666" qwen therapy`
- `"qwen2.5-7b-mental-therapy-lora-sft" OR "zbt566666" site:github.com`
- Hugging Face user page `https://huggingface.co/zbt566666`
- Raw `config.json` and the fadodr dataset card
- `fadodr/finetuned_mental_health_therapy_original` card
- Qwen2.5-7B-Instruct README

## Patterns in this batch

No paper, thesis, or training script names any of these four repository ids. Three cards do not state a loss or an update scope. The method words sit in the repository names (`Qlora`, `lora-sft`), and the inventory copied those names into `methods`.

All four uploads are full weight files with the same parameter count as the named base. None contains `adapter_config.json`. A matching count does not say whether training changed the weights.

Aurion is the only card that writes "Unsloth + LoRA". The same repo is tagged `base_model:quantized:Qwen/Qwen2.5-3B-Instruct`, the GGUF files use the Qwen filename, and the shipped system prompt is Qwen's. The config stamp `unsloth_version` `2026.5.2` says Unsloth saved the config. It does not state the loss.

The MentalChat16K paper does train with QLoRA, at rank 64, alpha 16, five epochs, batch size 64, and learning rate 0.0002, on seven 7B models. It does not train `sirev/Qlora-lfm2-700m-mental-health`. Hermes 2 Pro's own card carries DPO, RLHF, and distillation tags. Those tags describe the parent, not a counsellor run by sshl505. fadodr's Unsloth plus TRL sentence describes their Llama 3 8B checkpoint, not `zbt566666/qwen2.5-7b-mental-therapy-lora-sft`.
