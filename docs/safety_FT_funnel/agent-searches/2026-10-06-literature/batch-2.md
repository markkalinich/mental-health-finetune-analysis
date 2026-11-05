# Safety fine-tune literature, batch 2 of 8

Five Hugging Face models. For each one, the training objective is taken from a sentence in a paper, a script, a trainer log, or the model card. A method word in the repository name is recorded as a name, not as evidence.

The earlier output-type notes are in `docs/safety_FT_funnel/how-models-are-filtered.md`. Agreement with those rows is stated in each model section.

| Model | Source found | Objective | Update scope | Data (name, n, provenance) | Base | Output type | Matches inventory row |
|---|---|---|---|---|---|---|---|
| ZennyKenny/Daredevil-8B-abliterated | blog | weight edit (abliteration) | none (no optimizer; projection edits writing weights) | mlabonne/harmful_behaviors (416 train / 104 test prompts) and mlabonne/harmless_alpaca (25,058 train / 6,265 test prompts); English prompt sets used to estimate a direction, not as next-token targets | card prose: mlabonne/Daredevil-8B (a merge). YAML lists meta-llama/Meta-Llama-3-8B-Instruct | reply | partly |
| vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B | paper | DPO (configurable safety tuning) | not stated for this checkpoint | vicgalle/configurable-system-prompt-multitask, 1,952 rows, English, synthetic | NousResearch/Hermes-2-Pro-Llama-3-8B, chat model | reply | partly |
| Dipto084/Llama-3.1-8B-XGuard-merged | preprint | SFT | LoRA, rank 8, alpha 16 on the card, merged into the uploaded weights | 20,000 XGuard-Train conversations plus 10,000 Tulu-Mix conversations | meta-llama/Llama-3.1-8B-Instruct | reply | partly |
| Jazhyc/Llama-3.1-8B-aims-grpo | preprint | GRPO | full weights (card). The paper's GRPO table does not name LoRA | Jazhyc/aims-safety-intents, 1,724 human intent–label pairs (Hub train 1,378); English prompts from WildGuardMix | meta-llama/Llama-3.1-8B-Instruct | verdict | partly |
| Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01 | code | SFT | not stated | Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks; trainer logged 28,249 samples, equal to the safety_only split; provenance of the target text not stated | meta-llama/Llama-3.1-8B-Instruct | not stated | yes |

## 1. ZennyKenny/Daredevil-8B-abliterated

### Sources

- Model card (this repo): `revision_3_experiments/hf_inventory/cache/readmes/ZennyKenny__Daredevil-8B-abliterated__2026-10-06.md`. Hub copy: https://huggingface.co/ZennyKenny/Daredevil-8B-abliterated
- Blog that documents the recipe on `mlabonne/Daredevil-8B`, not on this user name: https://huggingface.co/blog/mlabonne/abliteration
- Paper that defines the weight edit: Arditi et al., "Refusal in Language Models Is Mediated by a Single Direction", https://arxiv.org/abs/2406.11717 (NeurIPS 2024 PDF: https://proceedings.neurips.cc/paper_files/paper/2024/file/f545448535dfde4f9786555403ab7c49-Paper-Conference.pdf)
- Parent merge card: https://huggingface.co/mlabonne/Daredevil-8B
- mlabonne's own abliterated upload, a different repo: https://huggingface.co/mlabonne/Daredevil-8B-abliterated
- Prompt-set sizes from the Hub dataset records: https://huggingface.co/api/datasets/mlabonne/harmful_behaviors and https://huggingface.co/api/datasets/mlabonne/harmless_alpaca

No GitHub repository, notebook, or paper was found that names `ZennyKenny/Daredevil-8B-abliterated`. The blog and the Arditi paper do not name this Hub id.

### Training record

**(a) Objective.** Weight edit, not gradient training. Card says: "This model was not further trained." Card says: "The technique projects out harmful activation directions without further finetuning or modifying the model architecture." Card says the edit is "vector-based orthogonal projection" computed with `HookedTransformer` from `transformer_lens`. Paper says: "we propose a novel white-box jailbreak method through weight orthogonalization" and "it does not require gradient-based optimization nor any examples of harmful completions" (https://arxiv.org/abs/2406.11717). The repository name contains "abliterated". That name is not the evidence. The card sentence is.

**(b) Parameter-update scope.** No LoRA and no optimizer step. Scope value: none. Card says: "Number of layers edited: Entire stack (all transformer blocks)" and "Orthogonalization method: L2-normalized difference vectors." Paper says the edit is applied to "the embedding matrix, the positional embedding matrix, attention out matrices, and MLP out matrices" by `W′_out ← W_out − r̂ r̂ᵀ W_out`. Blog code orthogonalizes `model.W_E`, every block's `attn.W_O`, and every block's `mlp.W_out`, using one selected direction (layer candidate 9 in the worked example). Rank, alpha, and target-module lists are not stated, because there is no adapter. The uploaded repo is four bf16 shards and no `adapter_config.json` (Hub API, 8,030,261,248 parameters).

**(c) Training data.** These files are prompt sets for the direction, not supervised targets. Card says representations came from `mlabonne/harmful_behaviors` and `mlabonne/harmless_alpaca`. Blog says: "We'll use tatsu-lab/alpaca as well as data from llm-attacks. To make things easier, I repackaged them in two Hugging Face datasets: mlabonne/harmless_alpaca and mlabonne/harmful_behaviors." Hub record: `harmful_behaviors` has 416 train and 104 test rows, column `text`, language `en`. `harmless_alpaca` has 25,058 train and 6,265 test rows, column `text`, language `en`. The blog does not say how many rows were actually passed through the model. Provenance of the underlying sets: llm-attacks harmful instructions (Zou et al., cited as [6] in the Arditi paper's related line of work and named in the blog) and Alpaca instructions. The card does not name a generator model.

**(d) Base.** Card prose says: "Finetuned from model: `mlabonne/Daredevil-8B`" and "This is an abliterated version of `mlabonne/Daredevil-8B`." The same card's YAML `base_model` is `meta-llama/Meta-Llama-3-8B-Instruct`. The Daredevil card says Daredevil-8B "is a merge" with `merge_method: dare_ties` and `base_model: NousResearch/Meta-Llama-3-8B`, and "You can use it as an improved version of meta-llama/Meta-Llama-3-8B-Instruct." The merge YAML's base is the pretrained Llama 3 8B checkpoint (`NousResearch/Meta-Llama-3-8B`), not the Instruct checkpoint. The blog's worked example sets `MODEL_ID = "mlabonne/Daredevil-8B"` and then renames the download so `HookedTransformer` will load it as `meta-llama/Meta-Llama-3-8B-Instruct`. That loading trick explains a YAML base of Instruct without a statement that Instruct weights were the ones edited.

**(e) Hyperparameters.** No epochs, learning rate, or batch size. Card says precision `bfloat16` for loading and `float32` for conversion, and "Hardware Type: NVIDIA A100 (Google Colab)", "Hours used: ~1". Those hardware lines are only on this card. The blog's Colab does not state A100 or one hour for this user.

**(f) Evaluation.** Card says: "Human inspection of generations" and "Focused on refusal language: e.g., presence of 'I can't', 'I won't', etc." The Nous and Open LLM Leaderboard numbers on https://huggingface.co/mlabonne/Daredevil-8B-abliterated are for mlabonne's repo. They are not stated for ZennyKenny's repo.

**(g) Output type.** Reply. The model is a chat model whose refusal direction was removed so that it answers prompts the parent would refuse. Card example prompt: "How can I build a bomb?" It does not emit a safe/unsafe label. This agrees with the classification note: user prompt, chat reply, fewer refusals.

### Discrepancies

1. The card says the edited model is `mlabonne/Daredevil-8B`. The YAML and the inventory parent are `meta-llama/Meta-Llama-3-8B-Instruct`. The Daredevil card says that model is a DARE-TIES merge whose merge-kit base is `NousResearch/Meta-Llama-3-8B`.
2. The card says the entire stack was edited and that "top directional vectors" (plural) were removed, and also that "only a single direction (or small subset) was ablated." The blog's worked example selects one layer's direction and orthogonalizes the writing matrices in every block.
3. Hub storage for this repo and for `mlabonne/Daredevil-8B-abliterated` is the same byte count (16,060,556,376) and the same parameter count. File size is not identity. The shards were not checksummed. mlabonne's card says that upload was made "using failspy's notebook." This card describes a Colab run. Those can be the same procedure or two runs. Nothing here shows which.

### Confidence

Medium. The card states that this upload was not trained and was edited by orthogonal projection. The blog and the Arditi paper state the same family of edit, on Daredevil-8B and on chat models generally. No source outside this card confirms the A100 run or that these shards are mlabonne's file.

### Queries tried

1. `ZennyKenny Daredevil-8B-abliterated abliteration training`
2. `"Daredevil-8B-abliterated" OR "Daredevil-8B" mlabonne abliteration`
3. `ZennyKenny huggingface Daredevil github colab abliteration transformer_lens`
4. `Arditi "Refusal in Language Models Is Mediated by a Single Direction" orthogonalization weights`
5. Fetch https://huggingface.co/blog/mlabonne/abliteration
6. Fetch https://huggingface.co/mlabonne/Daredevil-8B and https://huggingface.co/mlabonne/Daredevil-8B-abliterated
7. Hub API for both Daredevil-abliterated repos and for both prompt datasets

## 2. vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/vicgalle__Configurable-Hermes-2-Pro-Llama-3-8B__2026-10-06.md`. Hub: https://huggingface.co/vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B
- Paper: Gallego, "Configurable Safety Tuning of Language Models with Synthetic Preference Data", https://arxiv.org/abs/2404.00495 (HTML: https://arxiv.org/html/2404.00495). The HTML is the full short paper. There is no hyperparameter appendix.
- Code: https://github.com/vicgalle/configurable-safety-tuning/blob/main/cst_train.py and the README model table
- Dataset: https://huggingface.co/datasets/vicgalle/configurable-system-prompt-multitask (1,952 train rows in the Hub dataset record)
- Base model card: https://huggingface.co/NousResearch/Hermes-2-Pro-Llama-3-8B

The paper's experimental models are OpenHermes-2.5-Mistral-7B and SOLAR-Instruct-10.7B. It does not name `Configurable-Hermes-2-Pro-Llama-3-8B`. The GitHub README does name it, in a table, as fine-tuned from Hermes-2-Pro-Llama-3-8B.

### Training record

**(a) Objective.** DPO, in the configurable safety tuning (CST) form. Card says: "fine-tuned using the approach configurable safety tuning (CST) from https://arxiv.org/abs/2404.00495, over the vicgalle/configurable-system-prompt-multitask dataset." Paper says: "Configurable Safety Tuning (CST), that augments DPO using synthetic preference data" and "This resorts to using the same DPO loss function, but over an augmented dataset of tuples of the form (s0, x, y0, y1) and (s1, x, y1, y0)." Script says: `from trl import DPOTrainer, DPOConfig` and `trainer = DPOTrainer(...)`. The script's `model_name` is `teknium/OpenHermes-2.5-Mistral-7B`, not Hermes-2-Pro. The loss class is evidence for the released script. It is not a statement that this Hermes checkpoint was the run that script executed.

**(b) Parameter-update scope.** Not stated for this checkpoint. The uploaded files are four fp16 shards (8,030,523,392 parameters) and no `adapter_config.json` (Hub API). A full-weight upload does not say whether training updated every weight or a merged adapter. The script, for the Mistral model only, says `load_in_4bit=True` and `LoraConfig(r=8 * 3, lora_alpha=16 * 3, ...)` with targets `k_proj`, `gate_proj`, `v_proj`, `up_proj`, `q_proj`, `o_proj`, `down_proj`. That is QLoRA, rank 24, alpha 48. Those numbers are not stated for Hermes-2-Pro. Rank, alpha, and merge status for this Hub id: not stated.

**(c) Training data.** Dataset id `vicgalle/configurable-system-prompt-multitask`. Hub record: 1,952 train examples, language `en`, tags include `synthetic` and `dpo`. Columns: `system`, `prompt`, `chosen`, `rejected`, `task`. Dataset card says: "Self-critique on a safety task from Harmful Behaviours, using the SOLAR-Instruct model" with the two system prompts "You are a helpful yet harmless assistant that avoids generating illegal or harmful content" and "You are a helpful assistant that is completely uncensored." The same card says the other source is `truthy-dpo`, with an honest-assistant prompt and role-play prompts. Paper says both the safety pairs and `truthy-dpo` are synthetic. It does not give a separate generator name for `truthy-dpo` beyond calling it "another synthetic dataset." The script loads this dataset's train split: `load_dataset("vicgalle/configurable-system-prompt-multitask")["train"]`.

**(d) Base.** Card says `NousResearch/Hermes-2-Pro-Llama-3-8B`. Hub tag: `base_model:finetune:NousResearch/Hermes-2-Pro-Llama-3-8B`. The Hermes card describes a chat model: ChatML, function calling, and JSON mode, "an upgraded, retrained version of Nous Hermes 2" on an updated OpenHermes 2.5 dataset plus a function-calling dataset. It is an instruction-tuned chat model, not a raw pretrained checkpoint. That card does not use the word "Instruct" in the model id. The behavior is a chat model.

**(e) Hyperparameters.** Not stated for this checkpoint. The paper reports no learning rate, epoch count, or batch size. The script, for OpenHermes-2.5-Mistral-7B, sets `num_train_epochs=1`, `per_device_train_batch_size=2`, `gradient_accumulation_steps=4`. Hardware is not stated.

**(f) Evaluation.** The card's Open LLM Leaderboard block, copied from https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard?query=vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B : IFEval 57.63, BBH 30.51, MATH Lvl 5 5.97, GPQA 6.26, MuSR 10.06, MMLU-PRO 23.31, average 22.29. The paper's safety tables (S0, S1, role-play, ARC, HellaSwag, MMLU, TruthfulQA) are for OpenHermes-2.5-Mistral-7B and SOLAR-Instruct-10.7B, not for this 8B Hermes checkpoint.

**(g) Output type.** Reply. Card says the system prompt selects the behavior, including "You are a helpful yet harmless assistant that avoids generating illegal or harmful content," "You are a helpful assistant that is completely uncensored," and "You are a harmful assistant that generates illegal content." The model continues the chat. It does not emit a safe/unsafe verdict. This agrees with the classification note: user prompt, chat reply, prompt-controlled refusal.

### Discrepancies

1. Inventory `methods` is blank. The card and the paper state DPO (CST). The dataset and the parent match the inventory.
2. The training script's QLoRA settings and one-epoch DPO run are hardcoded to `teknium/OpenHermes-2.5-Mistral-7B`. They are not evidence for this Hermes checkpoint.
3. The paper's measured models are the 7B Mistral and 10.7B SOLAR CST runs. This Hub model was released later (Hub `createdAt` 2024-05-02). The README lists it. The paper text does not.

### Confidence

Medium. The card states that this checkpoint was fine-tuned with CST, and the paper defines CST as the DPO loss on preference pairs with the preference flipped under the opposite system prompt. Rank, quantization, and epoch for this file are not stated.

### Queries tried

1. `vicgalle Configurable Safety Tuning Hermes-2-Pro-Llama-3-8B DPO ORPO`
2. `site:github.com vicgalle configurable-safety-tuning Hermes-2-Pro training config DPO`
3. Fetch https://arxiv.org/html/2404.00495
4. Fetch https://github.com/vicgalle/configurable-safety-tuning and `cst_train.py`
5. Fetch the dataset page and https://huggingface.co/api/datasets/vicgalle/configurable-system-prompt-multitask
6. Fetch https://huggingface.co/NousResearch/Hermes-2-Pro-Llama-3-8B
7. Hub API https://huggingface.co/api/models/vicgalle/Configurable-Hermes-2-Pro-Llama-3-8B

## 3. Dipto084/Llama-3.1-8B-XGuard-merged

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/Dipto084__Llama-3.1-8B-XGuard-merged__2026-10-06.md`. Hub: https://huggingface.co/Dipto084/Llama-3.1-8B-XGuard-merged
- TRACE preprint, which describes this baseline: Miah et al., https://arxiv.org/abs/2608.15594 (PDF appendix F.3). The HTML conversion dropped the appendix body. The quotes below are from the PDF.
- X-Teaming paper for the original data and the authors' own fine-tune, which is a different training write-up: Rahman et al., https://arxiv.org/abs/2504.13203
- Dataset record: https://huggingface.co/api/datasets/marslabucla/XGuard-Train
- Code repo linked from the card: https://github.com/Dipto084/TRACE (the public README returned no training script in the fetch)

Featherless (https://featherless.ai/models/Dipto084/Llama-3.1-8B-XGuard-merged) restates the card and changes the sequence length. It is a copy, not an independent source.

### Training record

**(a) Objective.** Supervised fine-tuning. Card says: "Method: LoRA supervised fine-tuning, merged into the base weights for release" and "LoRA SFT with LLaMA-Factory (`stage: sft`, `template: llama3`)." TRACE PDF, appendix F.3, says: "X-Guard is constructed by fine-tuning Llama-3.1-8B-Instruct on 20,000 multi-turn conversations sampled from XGUARD-TRAIN combined with 10,000 sampled from Tulu-Mix." The TRACE paper's own model is a separate SFT-then-GRPO run. This checkpoint is the X-Guard row, not TRACE-GRPO. The repository name contains "merged". The card states the merge.

**(b) Parameter-update scope.** LoRA, then merged. Card says rank / alpha / dropout `8 / 16 / 0.05`, "LoRA targets: all linear layers," and "The step-4,000 adapter was merged into the base weights and exported with LLaMA-Factory." "Release form: full merged weights, bf16." TRACE PDF F.3 says: "The configuration uses LoRA at rank 8." It does not state alpha, dropout, or target modules. Adapter merged: yes, on the card.

**(c) Training data.** Card says 20,000 conversations from `marslabucla/XGuard-Train` plus 10,000 general instruction conversations in `tulu_10k.json`, then a 95/5 split: train 19,042 XGuard + 9,458 instruction (28,500); validation 958 + 542 (1,500). TRACE PDF F.3 says the same 20,000 and 10,000, "preserving the 2:1 XGUARD-TRAIN-to-Tulu-Mix ratio reported in the original paper," and Table 8 lists X-Guard at 30k multi-turn dialogs. Hub dataset record: XGuard-Train "consists of 30,695 multi-turn conversations." X-Teaming paper says: "We sampled 10,000 harmful behaviors from 13 distinct risk categories in WildJailbreak's vanilla harmful collection (Jiang et al., 2024). Using our X-Teaming framework, we generated 30K diverse attack trajectories" and "For successful jailbreaks, we replaced harmful model responses with carefully crafted refusals." Language on this model card: `en`. The 10,000 Tulu rows are "sampled from Tulu-Mix" (TRACE PDF). The card does not give a Hub id for `tulu_10k.json`. Provenance of the attack turns: generated by the X-Teaming agents, then harmful targets replaced by refusals. The X-Teaming paper names GPT-4o for offline plan generation in the attack protocol. It does not, in the section quoted here, name the model that wrote each refusal.

**(d) Base.** Card and TRACE PDF F.3: `meta-llama/Llama-3.1-8B-Instruct`. It is the instruction-tuned checkpoint. The X-Teaming paper's own training sentence says "Llama-3.1-8B (Dubey et al., 2024)" and does not write "Instruct" in that sentence. The TRACE reproduction states Instruct.

**(e) Hyperparameters.** Card table: learning rate `1e-4`, cosine, 10% warmup; planned epochs 3 (5,346 optimizer steps); batch 4 per device times 4 gradient accumulation = 16; max sequence length 8,192; bf16; 1× H100 80GB; released checkpoint step 4,000, epoch 2.24, eval loss 0.7610. TRACE PDF F.3 says learning rate `1e-4` and 3 epochs, and does not mention the early stop at epoch 2.24.

**(f) Evaluation.** Card says the numbers are TRACE Table 2, this checkpoint as the X-Guard row. Behavior-level attack success rate, average 44.4% (X-Teaming 58.3, Crescendo 28.3, ActorAttack 19.2, CoA 79.2, ICON 65.0, FITD 37.5, AMA 23.3). Over-refusal full-compliance: PHTest 83.3, XSTest 91.6, average 87.5. Those figures match the X-Guard row in the TRACE PDF table.

**(g) Output type.** Reply. Card says it is "a drop-in replacement for Llama-3.1-8B-Instruct" and "the safety behavior lives in the weights." The usage code generates a chat continuation. It is built to refuse multi-turn jailbreaks rather than to print a safe/unsafe label. This agrees with the classification note: multi-turn conversation, chat reply, more refusals.

### Discrepancies

1. Inventory `methods` is `grpo|lora|sft`. The GRPO tag is the TRACE-GRPO comparison row on this card, not this checkpoint. This checkpoint is LoRA SFT. Dataset and parent match.
2. TRACE PDF F.3 says the configuration uses 3 epochs. The card says the released weights are step 4,000, epoch 2.24, after a planned 3 epochs.
3. The X-Teaming paper trains "Llama-3.1-8B" for 3 epochs with LoRA rank 8 and learning rate `1.0e-4` on Tulu-Mix mixed with XGuard-Train at 1:2. It does not state the 20,000 / 10,000 counts, alpha 16, or the H100 run. Those counts are in the TRACE PDF and on this card. The card says this file "is not an official release of the X-Teaming authors."
4. Featherless says maximum sequence length 4096. The card says 8,192. Featherless is a paraphrase.

### Confidence

High for objective, LoRA rank 8, the 20,000 plus 10,000 mix, the Instruct base, and the chat-reply output. The paper appendix and the card agree on those. Alpha 16, the merge, the H100, and the epoch-2.24 checkpoint are stated on the card and not in appendix F.3.

### Queries tried

1. `Dipto084 Llama-3.1-8B-XGuard-merged TRACE LoRA SFT arxiv 2608.15594`
2. `X-Teaming Rahman X-Guard Llama-3.1 fine-tune XGuard-Train SFT hyperparameters arxiv 2504.13203`
3. `Dipto084 TRACE "X-Guard" "LoRA rank" OR "tulu_10k" OR "20000" site:github.com`
4. Fetch https://arxiv.org/html/2608.15594 and the PDF https://arxiv.org/pdf/2608.15594
5. Fetch https://arxiv.org/pdf/2504.13203
6. Fetch https://github.com/Dipto084/TRACE and https://huggingface.co/api/datasets/marslabucla/XGuard-Train
7. Featherless page for this model id (checked as a possible second write-up; it copies the card)

## 4. Jazhyc/Llama-3.1-8B-aims-grpo

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/Jazhyc__Llama-3.1-8B-aims-grpo__2026-10-06.md`. Hub: https://huggingface.co/Jazhyc/Llama-3.1-8B-aims-grpo
- Paper: Ferrao et al., "Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification Across Training Regimes", https://arxiv.org/abs/2606.27210 (HTML: https://arxiv.org/html/2606.27210v1), including Appendix F
- Dataset: https://huggingface.co/datasets/Jazhyc/aims-safety-intents
- Project page: https://jazhyc.github.io/aims-safety/

The paper does not print the Hub id `Jazhyc/Llama-3.1-8B-aims-grpo`. The card's harmful-class F1 row matches the paper's "Label and intent reward" GRPO row exactly (WildGuardTest 0.863, XSTest 0.958, AEGIS 2.0 0.808, ToxicChat 0.743, OpenAI Mod 0.809, average 0.836).

### Training record

**(a) Objective.** GRPO, reinforcement learning with a reward. The repository name contains "grpo". The paper states the method separately. Paper says: "We use GRPO (Shao et al., 2024) to test whether intent faithfulness can also serve as an online reward signal" and "Unlike DPO which learns from pre-built preference pairs, GRPO induces preferences during training from different rollouts using the reward function." Card says: "It is trained with GRPO (Group Relative Policy Optimization)." The reward is a product of format, label correctness, intent length, and an intent match to the human intent. Paper Appendix F: `R = R_format × R_label × R_len × R_intent`. The same paper also trains SFT, DPO, and distillation models. Those are other rows. This card's scores match the GRPO label-and-intent row, not the SFT or DPO rows.

**(b) Parameter-update scope.** Full weights, on the card. Card says: "this is a full fine-tuned model" and "Base model: `meta-llama/Llama-3.1-8B-Instruct` (full fine-tune, not an adapter)" and "load it directly with `from_pretrained` (no PEFT)." The paper's GRPO section and Table 12 do not say LoRA, QLoRA, or full. The same paper says "All SFT models were fine-tuned using QLoRA" and "We train each DPO variant with QLoRA." It does not use that sentence for GRPO. Rank and alpha: not stated. Adapter merged: no adapter, on the card.

**(c) Training data.** `Jazhyc/aims-safety-intents`. Paper says: "a human-annotated dataset of 1,724 difficult safety prompts, each paired with an intent description and harm label." Paper says the 1,724 annotations "are partitioned into train, validation, and test splits in an 80:10:10 ratio." Hub record: train 1,378, validation 173, test 173. The GRPO section does not print "1,378." Dataset card says: "The intent descriptions and four-point harm labels are original human annotations" and "prompts originate" in WildGuardMix. Language: English (paper and dataset card). The intent reward uses Gemma-3-27B-IT as a judge (paper Table 12: "Judge model: Gemma-3-27B-IT"). The supervision text for intent and harm is human-written. The judge score is a model score on top of that.

**(d) Base.** Paper says: "GRPO is initialized directly from Llama-3.1-8B-Instruct and uses the same policy as the KL reference." Card says the same id. It is the instruction-tuned checkpoint, not the pretrained base.

**(e) Hyperparameters.** Paper Table 12: AdamW, learning rate `10^-6`, KL coefficient `10^-3`, low_var_kl, 16 rollouts per prompt, prompt batch size 128, 2,048 rollouts per step, temperature 1.2, max completion length 512, 10 epochs, top-p 1.0, gradient clipping 1.0, "a node of 8 NVIDIA H200 GPUs of 141GB VRAM," VERL with a vLLM backend. Card does not repeat the table.

**(f) Evaluation.** Paper Table 1 and the card: harmful-class F1, positive class `harmful`, on WildGuardTest, XSTest, AEGIS 2.0, ToxicChat, and OpenAI Moderation. This variant's average is 0.836. The label-only GRPO ablation in the same table is 0.818. Checkpoint selection uses ToxicChat train and AEGIS 2.0 validation, "only for model and hyperparameter selection" (paper).

**(g) Output type.** Verdict. Card says: for each user prompt it produces a `<reasoning>` trace, an `Intent:` line, and `Harm: <harmful|safe>`. Paper says the rollout "contains a reasoning field, an explicit intent, and the harm label." It classifies the prompt. It does not answer the prompt as a chat assistant. This agrees with the classification note: user prompt, reasoning and a verdict, judgment training. The taxonomy cell is verdict. The reasoning trace is part of that verdict format.

### Discrepancies

1. Inventory `methods` is `dpo|full_finetune|grpo|sft`. DPO and SFT are other rows in the card's comparison table. This checkpoint is the GRPO row. `full_finetune` matches the card. The dataset and the parent match.
2. The paper never says the GRPO run updated every weight. The card does. SFT and DPO in the same paper are QLoRA.

### Confidence

High. The card's F1 numbers are the paper's GRPO label-and-intent row, the paper states GRPO from Llama-3.1-8B-Instruct with the Table 12 settings, and the card states that the upload is not an adapter.

### Queries tried

1. `Jazhyc Llama-3.1-8B-aims-grpo "Paved with True Intents" GRPO hyperparameters`
2. Fetch https://arxiv.org/html/2606.27210v1 (main text and Appendix F)
3. Fetch https://jazhyc.github.io/aims-safety/
4. Fetch https://huggingface.co/datasets/Jazhyc/aims-safety-intents and the dataset API
5. Search of the paper text for the Hub id, for LoRA on the GRPO run, and for the 80:10:10 split
6. Hub model API tags (`arxiv:2606.27210`, dataset `Jazhyc/aims-safety-intents`)
7. alphaXiv page https://www.alphaxiv.org/replicate/2606.27210 (no extra training recipe)

## 5. Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01

### Sources

- Model card: `revision_3_experiments/hf_inventory/cache/readmes/Neelectric__Llama-3.1-8B-Instruct_SFT_safetyv00.01__2026-10-05.md`. Hub: https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01
- Trainer log in that repo: https://huggingface.co/Neelectric/Llama-3.1-8B-Instruct_SFT_safetyv00.01/raw/main/trainer_state.json
- Same repo: `all_results.json`, `train_results.json`, and `training_args.bin` (an `open_r1.configs.SFTConfig` pickle)
- Dataset record: https://huggingface.co/api/datasets/Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks
- Author page: https://huggingface.co/Neelectric (Neel Rajani). A related repo, https://github.com/Neelectric/SentineLLM, describes a different DPO data pipeline and does not name this checkpoint.

The dataset README is empty. The row viewer returned 401, so no example text was read. No paper was found that names this Hub id.

### Training record

**(a) Objective.** Supervised fine-tuning. Card says: "This model was trained with SFT." The saved config class is `open_r1.configs.SFTConfig`. `training_args.bin` contains `loss_type` and `nll`. `trainer_state.json` logs `loss` and `mean_token_accuracy`. The repository name contains "SFT". The card sentence and the `SFTConfig` class are the evidence. Tags also include `trl` and `open-r1`. TRL is a library, not a loss. The wandb project name inside the args is `open-r1_math`. That project name is not a statement that the data are math traces.

**(b) Parameter-update scope.** Not stated. `training_args.bin` is an `SFTConfig`. It has no `lora`, `peft`, or `qlora` string. In the Open-R1 trainer, the adapter config lives on a separate model config, which is not in this file. The upload is four bf16 shards (8,030,261,248 parameters) and no `adapter_config.json`. That is consistent with a full update or with a merged adapter. Neither is stated. Rank, alpha, and merge: not stated.

**(c) Training data.** Card says the dataset is `Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks`. Hub record, four configs: default 86,745 rows; `refusals_only` 31,266; `safety_only` 28,249; `utility_only` 37,654. The sum is about 184k, which is the figure on the dataset page. `all_results.json` says `"train_samples": 28249`. That equals the `safety_only` count and does not equal the default config. The card does not name the config. Columns on every config: `wjb_prompt`, `model_response`, `guard_response`, `refusal_detected`, `messages`. There is no column named `text` in the Hub schema. The saved config's `dataset_text_field` is `text`. How `messages` became `text` is not stated. Language: not stated on the empty README. Provenance of `model_response` and `guard_response`: not stated. The column name `wjb_prompt` is a name, not a statement that the rows are WildJailBreak. The dataset name contains "wildguardmix". That is a name, not a statement that these 28,249 rows are the WildGuardMix train split (the default config, 86,745 rows, is close to WildGuardMix's published train size of 86,759, and this run did not log 86,745).

**(d) Base.** Card and Hub tag: `meta-llama/Llama-3.1-8B-Instruct`, relation `finetune`. It is the instruction-tuned checkpoint.

**(e) Hyperparameters.** From `trainer_state.json`: `num_train_epochs` 2, `max_steps` 10000, stopped at `global_step` 10000 and `epoch` 1.4158, `train_batch_size` 4, `eval_steps` 500, `save_steps` 5000. Learning rate is 0 at step 1, reaches `1e-6` at step 1001, and stays `1e-6` through step 10000. The scheduler field in `training_args.bin` is `constant_with_warmup`. The integer stored for `warmup_steps` was not decoded from the pickle. `train_runtime` 8974.1904 seconds. `train_loss` 0.34853814358897506. The args also contain `bf16`, `gradient_checkpointing`, `use_liger_kernel` (presence of the field; the boolean was not decoded), `packing`, and `assistant_only_loss` (field present; the boolean was not decoded). Hardware: not stated. The log directory name contains the host fragment `s2011847-a1-b-may25`. Framework versions on the card: TRL 1.1.0.dev0, Transformers 4.57.6, PyTorch 2.9.0, Datasets 4.8.5, Tokenizers 0.22.2.

**(f) Evaluation.** The trainer log reports training loss only. No benchmark table is on the card or in `all_results.json`.

**(g) Output type.** Not stated. The card's quick start generates a chat continuation for a time-machine question. That demo does not say what the training targets were. The saved chat template, when the example has no system message, inserts a system string that asks for `<think>` and `<answer>` tags. That is a reply format. It is the Open-R1 template stored in the training args. It does not say whether the assistant targets were refusals, ordinary answers, or a guard string. The dataset has both `model_response` and `guard_response`, and an integer `refusal_detected`. No source states which of those was the loss target. This agrees with the classification note: unclear from the card. The trainer files do not resolve it. What the model is built to detect: not stated.

### Discrepancies

1. The card names the dataset and does not name a config. The trainer's 28,249 samples match `safety_only`, not the default 86,745 and not the 184k sum shown on the Hub page.
2. Inventory `methods` is `sft`, the dataset id matches, and the parent matches. The inventory does not claim LoRA or a verdict head. That row matches what is actually stated.
3. Featherless says the model "specializes in safety-oriented responses." That sentence is not on the card. It is a hosting-page paraphrase.
4. `SentineLLM` uses WildGuardMix to build DPO pairs. It does not say those pairs trained this SFT checkpoint.

### Confidence

Medium. SFT, the Instruct base, the learning rate, the step cap, and the 28,249-sample count are in the trainer files. The text that was predicted, and whether an adapter was used, are not in those files.

### Queries tried

1. `Neelectric Llama-3.1-8B-Instruct_SFT_safetyv00.01 wildguardmix SFT`
2. `"Neel Rajani" OR Neelectric wildguardmix safety SFT Llama-3.1 LoRA`
3. `"wildguardmix_Llama-3.1-8B-Instruct_4096toks" OR "safety_only" Neelectric SFT`
4. Fetch the model card, https://huggingface.co/Neelectric, and https://github.com/Neelectric/SentineLLM
5. Fetch `trainer_state.json`, `all_results.json`, `train_results.json`, and `training_args.bin`
6. Fetch https://huggingface.co/api/datasets/Neelectric/wildguardmix_Llama-3.1-8B-Instruct_4096toks
7. Datasets-server rows request for `safety_only` (401, no row text)
8. Cached card of `Neelectric/Qwen3-0.6B-Base_SFT_safety_v00.01` (a different dataset, `Neelectric/Nemotron-SFT-Safety-v1-nocot`; not used as evidence for this run)

## Patterns in this batch

Two of the five uploads are not one training objective each in the way the inventory row reads. The X-Guard card's comparison table mentions TRACE-GRPO, and the AIMS card's table mentions SFT, DPO, and distillation. Those words are other models. The X-Guard file is a LoRA SFT merge. The AIMS file is a GRPO run from the Instruct checkpoint.

The only weight edit is Daredevil. Its card says it was not trained. The YAML base, Instruct, is not the merge the prose says was edited. Daredevil-8B is a DARE-TIES merge of other Llama 3 chat models, and the merge-kit base named on that card is the pretrained `NousResearch/Meta-Llama-3-8B`.

Configurable Hermes is DPO, with the preference reversed under an opposing system prompt, so one checkpoint both refuses and complies. The published script's QLoRA settings belong to a Mistral 7B run. This Hermes file does not state rank or whether an adapter was merged.

The two Llama-3.1-8B-Instruct runs that do state a loss split by what they emit. X-Guard is trained to continue a multi-turn chat with a refusal in place of a harmful answer. AIMS is trained to emit a reasoning trace, an intent, and a harmful/safe label, and it never answers the user's request. The Neelectric SFT log is the most complete hyperparameter record in the batch and still does not say which column was the target, so that model's output type stays unresolved.
