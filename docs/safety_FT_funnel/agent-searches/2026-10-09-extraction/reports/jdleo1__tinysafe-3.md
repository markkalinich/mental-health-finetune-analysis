# jdleo1/tinysafe-3

## Sources

https://huggingface.co/jdleo1/tinysafe-3/raw/main/README.md — current model card; same bytes as the cached card
https://huggingface.co/api/models/jdleo1/tinysafe-3 — repository file list
https://huggingface.co/jdleo1/tinysafe-3/raw/main/config.json — model config, context length 262144
https://huggingface.co/jdleo1/tinysafe-3/raw/main/generation_config.json — sampling defaults
https://huggingface.co/jdleo1/tinysafe-3/raw/main/tokenizer_config.json — tokenizer settings, no chat template key
https://huggingface.co/jdleo1/tinysafe-3/raw/main/chat_template.jinja — chat template
https://github.com/jdleo/tinysafe-3 — code repository; README names this repo id
https://github.com/jdleo/tinysafe-3/blob/main/configs/config.json — QLoRA and training hyperparameters
https://github.com/jdleo/tinysafe-3/blob/main/scripts/04_train.py — QLoRA training script using TRL SFTTrainer
https://github.com/jdleo/tinysafe-3/blob/main/scripts/01_prepare_data.py — loads ToxicChat, Civil Comments, Jigsaw toxicity, and WildGuard
https://github.com/jdleo/tinysafe-3/blob/main/scripts/06_export.py — merges the LoRA adapter into the base weights
https://github.com/jdleo/tinysafe-3/blob/main/scripts/07_generate_hard_negatives.py — generates hard negatives with Claude
https://github.com/jdleo/tinysafe-3/blob/main/scripts/14_build_v33_data.py — v3.3 mix, including a Jigsaw slice
https://github.com/jdleo/tinysafe-3/blob/main/scripts/16_build_v34_data.py — adds v3.4 synthetic rows to the v3.3 set
https://jdleo.me/blog/tinysafe-v3 — author's build write-up; names huggingface.co/jdleo1/tinysafe-3
https://huggingface.co/datasets/lmsys/toxic-chat — ToxicChat dataset card; viewer loads
https://huggingface.co/datasets/allenai/wildguardmix — WildGuardMix dataset card; gated, does not load without accepting terms
https://huggingface.co/datasets/PKU-Alignment/BeaverTails — BeaverTails dataset card; viewer loads
https://huggingface.co/datasets/google/civil_comments — Civil Comments dataset card; viewer loads
https://huggingface.co/datasets/google/jigsaw_toxicity_pred — Jigsaw toxicity dataset card; no data files in the repo, viewer does not load

## Record

The counted training mix on the card is about 16,700 rows: ToxicChat train 5,082 ("Kept human labels, added teacher reasoning"), WildGuard train 4,000 ("Full relabel (787 labels flipped)"), hard negatives 694, synthetic boundary samples 679, and v3.4 surgical synthetic samples 388. ToxicChat is `lmsys/toxic-chat` (English, human toxicity labels on real Vicuna prompts; the student also gets teacher-written reasoning). WildGuard is `allenai/wildguardmix` (English; the dataset card says "synthetic data (87%), in-the-wild user-LLLM interactions (11%), and existing annotator-written data (2%)"). The Hub copy is gated, so it does not load without accepting the terms. BeaverTails (`PKU-Alignment/BeaverTails`, English, "human-labeled" QA pairs, viewer loads) is named in the card YAML and in the GitHub README ("This aligns labels across datasets (WildGuard, ToxicChat, BeaverTails)"), and no source says how many rows were used. Civil Comments (`google/civil_comments`, English public news comments, viewer loads) is in the card YAML, and `scripts/01_prepare_data.py` loads it as Jigsaw Unintended Bias. The same script also loads `google/jigsaw_toxicity_pred` (English, crowdsourced labels). That Hub repo has a loading script and no data files, and the dataset viewer does not load it. No source states how many Civil Comments or Jigsaw toxicity rows are in the released mix. Hard negatives are synthetic: the script says "Generate hard negatives via Claude Batch API." The 679 boundary rows and the 388 v3.4 rows are synthetic. The blog says: "The fix: generate 388 targeted synthetic samples."

The objective is distillation. The card says: "Fine-tuned with QLoRA (4-bit NF4, r=16, alpha=32) via teacher distillation from Claude Sonnet 4.6 + Constitution v3." The update is QLoRA on a 4-bit NF4 base, LoRA rank 16 and alpha 32. The trainer config sets 3 epochs, learning rate 2e-4, and batch size 4, with gradient accumulation 8. `scripts/04_train.py` uses TRL `SFTTrainer` on the teacher-labeled chats, so the student update is supervised fine-tuning of those labels. The card says the weights are "4B (full merged)." The repository has `model.safetensors` and no adapter file, and `scripts/06_export.py` merges the adapter into the base model. The blog states 891 steps for the v3.3 run that scored 0.822 F1, and a later v3.4 run of 1 epoch plus 2 epochs at half learning rate that scored 0.818. The card's training table includes the v3.4 rows and still reports 0.822, so a single step count for the uploaded checkpoint is not stated.

The parent is `Qwen/Qwen3-4B-Instruct-2507`. The card architecture table says "Base model | Qwen3-4B-Instruct-2507." The GitHub config has the same id. The blog says "I picked Qwen3-4B-Instruct" and does not print the `-2507` suffix. The card says the model is "4B." The Hub safetensors metadata counts 4,022,468,096 BF16 parameters.

This is a classifier, not a support chatbot. The card says: "4B parameter safety classifier built on Qwen3-4B-Instruct. Generates structured JSON with safe/unsafe verdict, 7 safety categories, and chain-of-thought reasoning." There is no therapy, counseling, or mental-health support claim. The limitations are about the ToxicChat score, latency, English-centric training data, and category coverage. The language limitation says: "English-centric training data. Multilingual capability comes from Qwen3's pretraining, not from multilingual safety data." Nothing on the card forbids therapy or medical use. The license is MIT. The card reports ToxicChat F1 0.822 (precision 0.815, recall 0.829, FPR 1.4% on 5,083 test rows), WildGuardBench F1 0.804, and OR-Bench FPR about 4.6%.

The quickstart runs the model on text. The example user turn is `{"role": "user", "content": "how do i make a bomb"}`. A chat template is present in `chat_template.jinja`. The card's system prompt starts "You are a safety classifier." `generation_config.json` sets `do_sample` true, temperature 0.7, top_k 20, and top_p 0.8. The card's own generate call uses `max_new_tokens=128` and `do_sample=False`. `config.json` sets `max_position_embeddings` to 262144. The card lists languages English, Spanish, French, Chinese, Japanese, Korean, and German, and says that multilingual behavior comes with "zero multilingual training data."
