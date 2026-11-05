# Pilot: published training recipes for five mental-health fine-tunes

Date of search: 2026-10-06. Cards read: the 2026-10-05 copies under `revision_3_experiments/hf_inventory/cache/readmes/`. Each of those five files is identical to the 2026-09-24 copy. Inventory reading: `revision_3_experiments/hf_inventory/results/mental-health/archive/2026-10-06/kept.csv`.

A claim below is tied to a URL. If a field is missing from every source that was found, it is marked "not stated anywhere found."

## Summary

| Model | Publication found | Source type | Method per source | Data per source | Matches card |
|---|---|---|---|---|---|
| AIMH/SQPsychLLM-8b-gemma | yes | preprint (workshop-accepted) and GitHub | full bfloat16 fine-tune, 5 epochs, learning rate 2e-4 (paper). The released script is supervised fine-tuning of all weights at learning rate 2e-5 | SQPsychConv (Gemma): 2,090 English dialogues. Instruction split used for training: 28,434 train rows | partly |
| Psychotherapy-LLM/PsyCoPref-Llama3-8B | yes | preprint and ACL Findings 2026 | iterative direct preference optimization (DPO) | PsychoCounsel-Preference / PsyCoPref: 34,329 train pairs and 2,324 test pairs (about 36k) | partly |
| gustavecortal/Piaget-8B | no paper | dataset card, and a Reddit post that repeats the card | LoRA, rank 8, alpha 16, 1 epoch, batch size 16 (card and dataset card only) | PsychologicalReasoning-15k: 15,006 English rows, filtered from Dolphin R1 and GeneralThought-430K | yes, because those sources repeat the card |
| SungJoo/cradle-dialogue-qwen3-32b-2epoch | yes | preprint (NeurIPS 2026 workshop) | fine-tune for 3 epochs, learning rate 5e-6, this file is epoch 2. The paper does not say full fine-tune or LoRA | 3,058 synthetic English dialogues, 48,557 turns, from Reddit posts via GPT-5 | partly |
| thillaic/CBT-Copilot | no paper | GitHub README and training script | LoRA supervised fine-tuning (rank 8, alpha 16). Not DPO | Lumiiree/therapod-dpo: 6,310 rows on the dataset card. The script keeps 1,000 local rows | partly |

## 1. AIMH/SQPsychLLM-8b-gemma

The paper and the project page are about this checkpoint. They agree that it is Llama 3 8B Instruct trained on the Gemma-generated SQPsychConv dialogues. They do not agree on the learning rate: the paper says 2e-4, and the released training script says 2e-5.

### Sources

- Preprint, current version v2, first posted 2025-10-29, updated 2026-08-28. Accepted to the 5th Workshop on NLP for Positive Impact 2026 at EMNLP 2026. Authors: Doan Nam Long Vu, Rui Tan, Lena Moench, Svenja Jule Francke, Daniel Woiwod, Florian Thomas-Odenthal, Sanna Stroth, Tilo Kircher, Christiane Hermann, Udo Dannlowski, Hamidreza Jamalabadi, Simone Balloccu, Shaoxiong Ji. https://arxiv.org/abs/2510.25384
- The paper names the model as SQPsychLLM trained on the Gemma corpus (`SQPsychLLMgemma` / `SQPsychConvgemma`). It does not print the string `AIMH/SQPsychLLM-8b-gemma`.
- GitHub repository for the project, which does print that Hugging Face id: https://github.com/AI-MH/questionnaire2dialogue
- Training script in that repository: https://github.com/AI-MH/questionnaire2dialogue/blob/main/src/finetune.py
- Project page, which lists `AIMH/SQPsychLLM-8b-gemma` as the 8B model trained on SQPsychConv (Gemma): https://ai-mh.github.io/SQPsych
- Dialogue dataset card (YAML only in the cached copy): https://huggingface.co/datasets/AIMH/SQPsychConv_gemma
- Instruction-format dataset used for training, named on the model card: https://huggingface.co/datasets/AIMH/SQPsychConv_gemma_finetune

The cached model card (2026-10-05) already points at the paper, the GitHub repository, and the project page.

### Fine-tuning record

**Method.**

- Card says: "This checkpoint is **Llama-3-8B-Instruct** supervised-fine-tuned on **SQPsychConv (Gemma)**."
- Paper says: "we perform a full BF16 fine-tuning of Llama3-8B-Instruct on Psych8k, using the same hyperparameters as CAMEL (5 epochs, learning rate 2e-4). We use the same hyperparameters for finetuning SQPsychLLM." https://arxiv.org/abs/2510.25384 (v2, section 4.3)
- Script says the opposite learning rate and does not use a LoRA adapter. It loads `meta-llama/Meta-Llama-3-8B-Instruct` in bfloat16 and trains with `SFTTrainer`, with no `LoraConfig`. The learning-rate comment in the script is "learning rate, based on QLoRA paper," but the code is not QLoRA: there is no 4-bit load and no low-rank adapter. https://github.com/AI-MH/questionnaire2dialogue/blob/main/src/finetune.py
- Inventory `kept.csv` records `sft`. That matches the card's "supervised-fine-tuned" and the script's `SFTTrainer`. The paper says "full BF16 fine-tuning" and does not use the words supervised fine-tuning.

The CACTUS paper that introduced CAMEL uses QLoRA (4-bit, rank 64, alpha 16, learning rate 2e-4, 5 epochs on Psych8k, 2 epochs on CACTUS): https://arxiv.org/abs/2407.03103 . SQPsych v2 says its own Psych8k baseline was full bfloat16 fine-tuning at CAMEL's 5 epochs and 2e-4, and that SQPsychLLM used those same hyperparameters. The released SQPsych script is full-weight supervised fine-tuning at 2e-5.

**Data.**

- Card says the training data is `AIMH/SQPsychConv_gemma`, "synthetic therapist-client conversations generated by `google/gemma-3-27b-it`," and "The instruction-formatted split used for training is `AIMH/SQPsychConv_gemma_finetune`." Language on the card: English.
- Paper says the generator for that corpus is `google/gemma-3-27b-it` (27B), and `SQPsychConvgemma` has 71,000 utterances, 16.999 turns on average, and 51.790 tokens per utterance. "In total, we generated 2090 conversations per model." The source profiles are the Kircher et al. (2019) cohort, split 1,693 train, 144 development, and 253 test clients (955+738 control and MDD in train). https://arxiv.org/abs/2510.25384
- Dataset card for `AIMH/SQPsychConv_gemma`: 1,837 train dialogues and 253 test dialogues (1,837 = 1,693 + 144). https://huggingface.co/datasets/AIMH/SQPsychConv_gemma
- Dataset card for `AIMH/SQPsychConv_gemma_finetune`: 28,434 train rows and 3,931 test rows, with fields `input`, `output`, and `instruction`. https://huggingface.co/api/datasets/AIMH/SQPsychConv_gemma_finetune
- Inventory records the dataset as `AIMH/SQPsychConv_gemma` only. It does not record the `_finetune` split that the card says was used for training.
- The script trains on whatever path is passed in, and it reads `input` and `output`, which are the fields on the `_finetune` split. It does not hard-code the Gemma split.

**Base model.**

- Card and inventory: `meta-llama/Meta-Llama-3-8B-Instruct`.
- Script: `base_model = "meta-llama/Meta-Llama-3-8B-Instruct"`.
- Paper: "we fine-tune Llama3-8B-Instruct." It does not print the Hugging Face id. The name "gemma" in this checkpoint is the model that wrote the dialogues, not the model that was fine-tuned. The project page says the same: `AIMH/SQPsychLLM-8b-gemma` is an 8B model on SQPsychConv (Gemma). https://ai-mh.github.io/SQPsych

**Hyperparameters.**

- Paper: 5 epochs, learning rate 2e-4, and the sentence above that says the Psych8k run was full bfloat16. No batch size, no LoRA rank, no scheduler.
- Script: `num_train_epochs` defaults to 5; `learning_rate=2e-5`; `per_device_train_batch_size=2`; `gradient_accumulation_steps=16`; `optim="adamw_torch_fused"`; `bf16=True`; `max_grad_norm=0.3`; `warmup_ratio=0.03`; `lr_scheduler_type="constant"`; FlashAttention-2; seed 666.
- Card: not stated, beyond "supervised-fine-tuned."

**Evaluation.**

- Paper: CounselingBench (1,612 questions), CBT-Bench (cognitive-distortion, primary-belief, and fine-grained-belief items), an LLM-judge panel, and therapist preference comparisons. Table 3 includes `SQPsychLLMgemma`. Figure 3 is "Preference Evaluation between CAMEL, Psych8k, LLaMA-3-8B-Instruct vs. SQPsychLLMgemma." https://arxiv.org/abs/2510.25384
- Card: no scores.

### Agreement

Matches: base model `meta-llama/Meta-Llama-3-8B-Instruct`; training text is the Gemma-generated SQPsychConv corpus; the card's "supervised-fine-tuned" matches the script and the inventory's `sft`; English.

Disagreements:

1. Learning rate 2e-4 in the paper versus 2e-5 in `src/finetune.py`.
2. The paper points at CAMEL's hyperparameters. CAMEL's own paper used QLoRA. The SQPsych paper says full bfloat16, and the SQPsych script has no LoRA.
3. The inventory dataset is `AIMH/SQPsychConv_gemma` (1,837 train dialogues). The card says training used `AIMH/SQPsychConv_gemma_finetune` (28,434 train rows). The paper's utterance count for the Gemma corpus is 71,000, which is neither of those row counts.
4. The paper never prints `AIMH/SQPsychLLM-8b-gemma`. The GitHub README and the project page do.

### Confidence

High that the paper, the project page, and `finetune.py` are the authors' account of this checkpoint: the README loads `AIMH/SQPsychLLM-8b-gemma` by that id, and the project page lists it on SQPsychConv (Gemma). Medium on the exact learning rate, because the paper and the script disagree and the script takes the dataset path as an argument rather than naming the Gemma split.

### Queries

- `Roleplaying with Structure: Synthetic Therapist-Client Conversation Generation from Questionnaires SQPsychLLM arxiv 2510.25384`
- `CAMEL CACTUS Lee 2024 Llama3-8B-Instruct learning rate epochs LoRA` (one hop from the paper's "same hyperparameters as CAMEL")
- GitHub tree of `AI-MH/questionnaire2dialogue` and raw `src/finetune.py`
- Hugging Face dataset API for `AIMH/SQPsychConv_gemma_finetune`
- `site:github.com` search that returned this repository for the model id

## 2. Psychotherapy-LLM/PsyCoPref-Llama3-8B

The paper is the one the model card cites. It trains Llama 3.1 8B Instruct with iterative DPO on the same preference dataset, and it reports the same 87% win rate. The card says "preference learning" and does not say DPO. The inventory's method cell for this row is empty.

### Sources

- Preprint v2, first posted 2025-02-27, updated 2026-04-13, marked "ACL 2026 Camera-Ready." Authors: Mian Zhang, Shaun M. Eack, Zhiyu Zoey Chen. https://arxiv.org/abs/2502.19731
- ACL Findings 2026 anthology entry (abstract only in the page that was retrieved): https://aclanthology.org/2026.findings-acl.521/
- The v2 arXiv abstract says the released model is `PsychoCounsel-Llama3-8B` and the dataset is `PsychoCounsel-Preference`, at https://hf.co/Psychotherapy-LLM . The HTML body calls the best model `PsyCo-Llama3-8B` and the dataset `PsyCoPref`. Neither string is `PsyCoPref-Llama3-8B`.
- The model card says this repository "is presented in" that paper and links https://hf.co/papers/2502.19731 . The Hub API tags the repo `arxiv:2502.19731`. https://huggingface.co/Psychotherapy-LLM/PsyCoPref-Llama3-8B
- Dataset card: https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference . It says "Dataset from the paper Preference Learning Unlocks LLMs' Psycho-Counseling Skills" and links https://huggingface.co/papers/2502.19731 .

No training repository turned up. A different project, `wothmag07/counseLLM`, trains its own Llama 3.1 8B with QLoRA on a filtered slice of this dataset. That is not this checkpoint. https://github.com/wothmag07/counseLLM

### Fine-tuning record

**Method.**

- Card says: "a fine-tuned meta-llama/Llama-3.1-8B-Instruct model trained using preference learning on the PsyCoPref dataset."
- Paper says the best model is iterative DPO: "We refer to Llama3-8B (+DPO-Iter) as PsyCo-Llama3-8B." DPO-Iter generates 8 responses per client speech, ranks them with a reward model of the same size, and trains on the highest and lowest. Offline DPO is a separate condition. https://arxiv.org/html/2502.19731v2
- LoRA versus updating all weights: not stated anywhere found.
- Inventory `methods` cell: empty. `kept.csv` therefore does not record DPO or preference learning.

**Data.**

- Card says: "This dataset contains 36k high-quality preference comparison pairs."
- Paper says: "PsyCoPref includes 34,329 training preference pairs and 2,324 testing pairs," from 26,483 client speeches (3,291 held out for testing, 23,192 for training). The paper describes the counseling responses as English.
- Dataset card: train 34,329 examples, test 2,324 examples, fields `question`, `chosen`, `rejected`. https://huggingface.co/datasets/Psychotherapy-LLM/PsychoCounsel-Preference
- Inventory dataset: `Psychotherapy-LLM/PsychoCounsel-Preference`. That matches the card and the dataset card. The paper's short name is PsyCoPref.

**Base model.**

- Card and inventory: `meta-llama/Llama-3.1-8B-Instruct`.
- Paper: "We use Llama3.2-3B-Instruct and Llama3.1-8B-Instruct as the base models" for the policy training, and the 8B DPO-Iter run is the one they name PsyCo-Llama3-8B.

**Hyperparameters.**

- Paper, for DPO and DPO-Iter: batch size 64, learning rate 5e-7, 1,600 training steps, beta 0.1. Each DPO-Iter round uses 6,400 client speeches sampled from the PsyCoPref train set. A development set of 10% of the PsyCoPref training set selects checkpoints. A controlled comparison uses 1 epoch, learning rate 5e-7, global batch size 64.
- The reward model is separate: Llama-3.1-8B-Instruct trained for 2 epochs, batch size 128, learning rate 9e-6. The Hub also has `Psychotherapy-LLM/PsyCoPref-Llama3-8B-Reward`. This note is about the policy model, not that reward model.
- Card: no learning rate, epochs, or beta.

**Evaluation.**

- Paper: Llama3-8B (+DPO-Iter) win rate 87.0% against GPT-4o without a length constraint, and 77% with one. Therapists also compared 200 response pairs.
- Card says: "achieves a win rate of 87% against GPT-4o." That matches the unconstrained number and omits the 77% number.

### Agreement

Matches: Llama 3.1 8B Instruct, the PsychoCounsel-Preference dataset, about 36k pairs, 87% win rate against GPT-4o, and the card's link to arXiv 2502.19731.

Disagreements:

1. The paper's algorithm for the best 8B model is iterative DPO. The card says "preference learning" and does not say DPO. The inventory records no method.
2. Names differ: `PsyCoPref-Llama3-8B` on the Hub, `PsyCo-Llama3-8B` in the paper body, `PsychoCounsel-Llama3-8B` in the v2 abstract. The paper never prints `Psychotherapy-LLM/PsyCoPref-Llama3-8B`.
3. The paper reports 77% under a length constraint. The card reports only 87%.

### Confidence

High that this repository is the paper's best Llama 3.1 8B policy model. The card cites the paper, the Hub tag is `arxiv:2502.19731`, the org URL in the paper is `huggingface.co/Psychotherapy-LLM`, and the base model, dataset, and 87% figure match. The exact repository string is not in the paper.

### Queries

- `Preference Learning Unlocks LLMs' Psycho-Counseling Skills PsyCoPref Llama3 2502.19731`
- Hugging Face model API for `Psychotherapy-LLM/PsyCoPref-Llama3-8B`
- `site:github.com` search for `Psychotherapy-LLM/PsyCoPref-Llama3-8B` (no training repo for this id; the counseLLM hit is a different model)
- ACL anthology page `2026.findings-acl.521`

## 3. gustavecortal/Piaget-8B

No paper, thesis, or training repository was found for this fine-tune. The dataset card and a Reddit post repeat the model card, including the LoRA settings. A 2024 position paper is cited as inspiration and does not describe this training run.

### Sources

- Model card, which is the only detailed account: https://huggingface.co/gustavecortal/Piaget-8B . Hub API: created 2025-07-08, last modified 2025-07-18, `base_model` `Qwen/Qwen3-8B`. The file list is a full Qwen3 checkpoint (four safetensors shards). There is no `adapter_config.json`. That does not say whether a LoRA adapter was merged before upload.
- Dataset card, same methodology paragraph: https://huggingface.co/datasets/gustavecortal/PsychologicalReasoning-15k . Train split: 15,006 rows. Language: English.
- Reddit post, 2025-07-18, user `antcroca159`, which says "I just released Piaget" and then repeats the card's methodology: https://www.reddit.com/r/MachineLearning/comments/1m3319j/p_piaget_a_language_model_for_psychological_and/ . The username is not the GitHub login `gustavecortal`. The post does not add a learning rate or an evaluation.
- CV line, with no hyperparameters: "Piaget, a model fine-tuned for psychological reasoning, and Beck, a model aligned with psychotherapeutic preferences." https://gustavecortal.com/data/CV_Gustave_CORTAL.pdf
- Position paper named on the card, which does not describe Piaget-8B: Gustave Cortal, "Improving Language Models for Emotion Analysis: Insights from Cognitive Science," CMCL 2024. https://aclanthology.org/2024.cmcl-1.23/
- A later repository uses `gustavecortal/Piaget-8B` as the starting weights for a different ORPO run. It is not the recipe for Piaget. https://github.com/gustavecortal/preference-optimization-orpo-lora/blob/master/configs/config_8b.yaml

### Fine-tuning record

**Method.** Card and dataset card say: "Clusters tagged psychology or philosophy were retained for LoRA finetuning (rank=8, alpha=16, max length=2048, epoch=1, batch size=16)." Inventory records `lora`. No other source states a method.

**Data.** Card says a subset of Dolphin R1 and General Reasoning, released as the 15k set. Dataset card: 15,006 English train rows, filtered by embedding the prompts, k-means with k=20,000, and majority-vote labels from Qwen3-1.7B. Inventory lists all three: `cognitivecomputations/dolphin-r1`, `GeneralReasoning/GeneralThought-430K`, and `gustavecortal/PsychologicalReasoning-15k`.

**Base model.** Card YAML and inventory: `Qwen/Qwen3-8B`. The prose says "based on Qwen3."

**Hyperparameters.** Stated on the card: rank 8, alpha 16, max length 2048, 1 epoch, batch size 16. Learning rate: not stated anywhere found. Target modules: not stated anywhere found.

**Evaluation.** Not stated anywhere found.

### Agreement

The dataset card and the Reddit post match the model card. The inventory's LoRA reading and the three dataset ids match the card. There is no publication to disagree with.

### Confidence

Low that any source other than the author describes this checkpoint. The dataset card and the Reddit post copy the card. No paper was found that names `gustavecortal/Piaget-8B`.

### Queries that found no paper

- `gustavecortal Piaget-8B LoRA psychological reasoning finetune`
- `"Piaget-8B" OR "PsychologicalReasoning-15k" gustave cortal site:arxiv.org OR site:github.com`
- `"Gustave Cortal" Piaget Qwen3 "LoRA" psychology philosophy reasoning traces`
- GitHub user page `github.com/gustavecortal` (no Piaget training repository; the ORPO repository consumes Piaget-8B)
- Semantic Scholar API query `Piaget-8B psychological reasoning Gustave Cortal`: the request timed out
- The CMCL 2024 paper above, opened because the card cites it

## 4. SungJoo/cradle-dialogue-qwen3-32b-2epoch

The CRADLE-Dialogue paper describes this training run: Qwen3-32B, 3 epochs, learning rate 5e-6, and the reported checkpoint is epoch 2. The same scores appear on the model card (turn-level micro F1 51.31, dialogue-level micro F1 68.88). The paper does not say whether every weight was updated, and it does not print the Hugging Face id. The card says "Full fine-tune (no LoRA)."

### Sources

- Preprint, current version v3, first posted 2026-06-09, updated 2026-09-11. Journal reference on arXiv: WMHS Workshop (World Models for High-Stakes Health), NeurIPS 2026. Authors: Grace Byun, Abigail Lott, Rebecca Lipschutz, Sean T. Minton, Elizabeth A. Stinson, Jinho D. Choi (Emory University). https://arxiv.org/abs/2606.10380
- The paper calls the model `Qwen3-32b-FT`. It does not print `SungJoo/cradle-dialogue-qwen3-32b-2epoch`. Footnotes name two other SungJoo repos, `SungJoo/llama3.3-70b-CRADLE-consensus` and `SungJoo/Qwen2.5-72b-CRADLE-consensus`, which are post-level models, not this one.
- Dataset card, which does name this checkpoint: https://huggingface.co/datasets/SungJoo/Cradle-Dialogue
- A different paper, CRADLE Bench at EACL 2026, is the post-level benchmark, not this dialogue fine-tune: https://aclanthology.org/2026.eacl-long.73/ and https://github.com/emorynlp/CradleBench

The model card says the epoch-2 choice is "as reported in the CRADLE-Dialogue paper" but does not link the arXiv id. The id was found by searching the title and "Qwen3-32B."

### Fine-tuning record

**Method.**

- Card says: "Full fine-tune of Qwen/Qwen3-32B" and "Fine-tuning method | Full fine-tune (no LoRA)."
- Paper says: "a lightweight model specialized in crisis detection in multi-turn dialogue, fine-tuned from Qwen3-32B." Appendix D.2 gives the training settings and does not say full fine-tune, LoRA, or QLoRA. https://arxiv.org/html/2606.10380v1 (the same appendix paragraph is in the copy retrieved from `arxiv.org/abs/2606.10380`, which resolved to v3)
- Inventory records `full_finetune` from the card sentence. The paper does not confirm or deny that.

**Data.**

- Card says: "3,058 dialogues (48,557 turns) generated from Reddit posts via GPT-5." Language on the card: English.
- Paper says the same counts, plus 420 development dialogues (6,679 turns). Confirm tags are placed in an early, mid, or late window.
- Dataset card splits: train 3,058 dialogues / 48,557 turns; validation 420 / 6,679; test 600 / 8,975 clinician-annotated turns. https://huggingface.co/datasets/SungJoo/Cradle-Dialogue
- Inventory dataset: `SungJoo/Cradle-Dialogue`. Match.

**Base model.** Card, paper, and inventory: `Qwen/Qwen3-32B`.

**Hyperparameters.**

- Paper, Appendix D.2: "Training is conducted for 3 epochs with a maximum sequence length of 4096 tokens. We use a per-device batch size of 1 with gradient accumulation of 16 and a learning rate of 5×10^-6 with a warmup ratio of 0.05. Training is performed on two NVIDIA H200 GPUs. Among the three checkpoints, we report the results from the second epoch, which achieved the best validation performance."
- Card table: the same numbers, plus "Precision | bfloat16" and "LR scheduler | Cosine with warmup (ratio=0.05)." The paper states the warmup ratio and does not say cosine. The card says this file is "epoch 2, best val loss." The paper says "best validation performance."

**Evaluation.**

- Paper and card: turn-level micro F1 51.31, dialogue-level micro F1 68.88. The card also lists turn-level macro F1 54.96, turn-level micro recall 54.99, dialogue-level macro F1 69.29, and confirm-only dialogue micro F1 76.03. Those figures appear in the paper's tables for `Qwen3-32b-FT`.

### Agreement

The counts, the base model, the learning rate, the epoch choice, the hardware, and the two headline F1 scores match. The inventory's dataset and parent match the card.

Disagreements:

1. "Full fine-tune (no LoRA)" and "cosine" are on the card only. The paper does not say either.
2. The paper never writes the Hugging Face id. The dataset card does.
3. The card says "best val loss." The paper says "best validation performance."

### Confidence

Medium-high. The training numbers and the F1 scores on the card are the paper's `Qwen3-32b-FT` numbers, and the dataset card points at `SungJoo/cradle-dialogue-qwen3-32b-2epoch`. The paper itself does not name that repository, so a second Qwen3-32B fine-tune with the same table cannot be ruled out from the paper text alone.

### Queries

- `CRADLE-Dialogue Qwen3-32B crisis detection SungJoo fine-tune paper`
- `"cradle-dialogue-qwen3-32b-2epoch" OR "Qwen3-32b-FT" Byun CRADLE LoRA OR "full fine"`
- arXiv API `export.arxiv.org/api/query?id_list=2606.10380`
- `site:github.com` search, which returned `emorynlp/CradleBench` for the earlier post-level paper, not a training script for this 32B checkpoint
- Semantic Scholar API query `CRADLE-Dialogue Qwen3-32B Byun`: HTTP 429

## 5. thillaic/CBT-Copilot

No paper was found. The GitHub README and `model_finetuning.py` say this is LoRA supervised fine-tuning of Llama 3.2 3B Instruct. They do not say DPO. The inventory's `dpo|lora` label comes from the dataset name `therapod-dpo` plus the word LoRA on the card. The dataset's columns are `input` and `output`, not a chosen/rejected pair.

### Sources

- GitHub README, which links `thillaic/CBT-Copilot`: https://github.com/thillai-c/CBT-Copilot/blob/main/README.md
- Training script: https://github.com/thillai-c/CBT-Copilot/blob/main/model_finetuning.py
- Author page, one sentence and no paper: https://www.thillaic.com/
- Dataset card: https://huggingface.co/datasets/Lumiiree/therapod-dpo . It cites Prometheus 2, which is a paper about an evaluation model, not about CBT-Copilot: https://arxiv.org/abs/2405.01535

### Fine-tuning record

**Method.**

- Card says: "Fine-tuned using LoRA on the Lumiiree/therapod-dpo dataset and merged into a standalone model" and "Fine-tuning performed with Hugging Face `transformers`, `PEFT`, and `LoRA`."
- README says: "Fine-tuning Method: LoRA (Low-Rank Adaptation)."
- Script uses `SFTTrainer` and `LoraConfig`. It does not use a DPO trainer. It loads the base model with `load_in_8bit=True`. That is 8-bit loading plus LoRA. The script does not call this QLoRA.
- Inventory records `dpo|lora`. The `dpo` evidence string in `kept.csv` is the dataset name inside the card ("datasets: Lumiiree/therapod dpo"). No source states that the optimizer was DPO.

**Data.**

- Card and README name `Lumiiree/therapod-dpo`.
- Dataset card: 6,310 train rows. Fields include `input`, `output`, and `generations`. There is no `chosen` or `rejected` column. Tags include `synthetic`, `distilabel`, and `rlaif`. The same card says `size_categories: n<1K`, which does not match 6,310 rows. Generation model shown in the example: `01-ai/Yi-1.5-6B-chat`. Language is not given as a field; the example text is English.
- Script: reads a local `train.jsonl` with `prompt` and `response`, then `dataset.select(range(1000))`. It does not call `load_dataset("Lumiiree/therapod-dpo")`. The README does not mention the 1,000-row cut.

**Base model.** Card, README, script, and inventory: `meta-llama/Llama-3.2-3B-Instruct`.

**Hyperparameters.**

- README: `r=8`, `lora_alpha=16`, `target_modules=["q_proj", "v_proj"]`, `lora_dropout=0.05`, `learning_rate=2e-5`, `batch_size=1` with gradient accumulation, `epochs=1`, `optimizer=paged_adamw_8bit`.
- Script: the same LoRA settings and learning rate, plus `gradient_accumulation_steps=4`, `bias="none"`, `task_type="CAUSAL_LM"`, `bf16=True`, and 8-bit loading. The card does not state rank, learning rate, or epochs.
- Card says the LoRA was "merged into a standalone model." The uploaded repo is a standalone model, which matches that sentence.

**Evaluation.** README says: "Detailed evaluation metrics and benchmarks will be added as they become available." No scores were found.

### Agreement

Matches: base model, LoRA, the dataset name, and the card's statement that the adapter was merged.

Disagreements:

1. Inventory method `dpo|lora`. The card, the README, and the script say LoRA supervised fine-tuning. None of them says DPO. The dataset name contains "dpo," and the published columns are not preference pairs.
2. The script trains on 1,000 rows of a local file. The dataset card has 6,310 rows. The README does not mention the cut, the local filename, or 8-bit loading.
3. License: the model card says MIT. The GitHub README says Apache 2.0.

### Confidence

Medium that the README is meant to describe `thillaic/CBT-Copilot`, because it links that id. Low that `model_finetuning.py` is the exact command that produced the uploaded weights: it trains on `train.jsonl`, keeps the first 1,000 rows, and expects `prompt`/`response` rather than the dataset's `input`/`output`.

### Queries that found no paper

- `thillaic CBT-Copilot Llama-3.2-3B therapod-dpo LoRA`
- `"CBT-Copilot" OR "Thillai Chithambaram" therapod LoRA OR DPO`
- GitHub user `thillai-c` and the site `thillaic.com`
- Dataset citation hop to Prometheus 2 (`arXiv:2405.01535`), which is not this model
- Semantic Scholar API query `CBT-Copilot Thillai Chithambaram therapod`: HTTP 429

## What this pilot suggests for the other 34 models

A card that already contains an arXiv id or a paper title is the signal that a training paper exists. SQPsych and PsyCoPref were found from the link on the card. CRADLE's card named "the CRADLE-Dialogue paper" without a URL, and the title plus Qwen3-32B still found arXiv 2606.10380. A card that already prints LoRA rank, alpha, epochs, and batch size, as Piaget does, can still have no paper behind it. In that case the dataset card and a release post copied the same paragraph, so they are not a second witness. A dataset id that contains the letters "dpo" is a weak signal for the training algorithm: `therapod-dpo` has `input` and `output` columns, and the published script uses supervised fine-tuning with LoRA, while the inventory recorded DPO. When both a paper and a script exist, they can disagree on the learning rate, as SQPsych does (2e-4 in the paper, 2e-5 in `finetune.py`), so the linked paper is not a substitute for the script. Papers in this sample name the project (`SQPsychLLMgemma`, `PsyCo-Llama3-8B`, `Qwen3-32b-FT`). The exact Hugging Face id showed up on the project page, the GitHub README, or the dataset card. For the other 34 models, search the arXiv id first if the card has one, then the dataset card, and do not treat a method word inside a dataset name as a statement of how the checkpoint was trained.
