# Objective validation, 10 October 2026

Checked all 40 rows in `docs/safety_FT_funnel/decisions/objective-evidence.csv`. For each model the newest cached card is under `revision_3_experiments/hf_inventory/cache/readmes/`. Extraction records are under `docs/safety_FT_funnel/agent-searches/2026-10-10-extraction/`. Local weight folders, when present, are under `/home/mkalinich/hf_models/`. None of those folders contained a `trainer_state.json` or a training script.

## BSC-LT/salamandra-7b-instruct-guard

- Card: `BSC-LT__salamandra-7b-instruct-guard__2026-10-09.md`
- Local: `/home/mkalinich/hf_models/BSC-LT__salamandra-7b-instruct-guard/README.md` and both adapter `adapter_config.json` files
- Extraction JSON and report
- Did not open the linked Salamandra technical report or the dataset PDF; the basis cites the card. The card has the cross-entropy / CausalLM line, LoRA on attention, 3 epochs, and 21,335 observations (5,016 + 16,319). No preference-pair or RL wording.

## Banaxi-Tech/BananaMind-V2.5-Content-Safety

- Card: `Banaxi-Tech__BananaMind-V2.5-Content-Safety__2026-10-09.md`
- Local README. Extraction JSON. No paper or GitHub links.

## DloadingX/GuardTrace-VL-3B

- Card: `DloadingX__GuardTrace-VL-3B__2026-10-05.md` (no objective word)
- Local README. Extraction JSON
- Paper: https://arxiv.org/html/2511.20994
- GitHub link recorded but not needed once the paper named all three stages for Qwen2.5-VL-3B-Instruct: https://github.com/xiangyx2020/GuardTrace-VL

## Hagrun/moddog-l1-safety-qwen2.5-3b

- Card: `Hagrun__moddog-l1-safety-qwen2.5-3b__2026-10-05.md`
- Local README. Extraction JSON. No paper or GitHub links.

## Jazhyc/Llama-3.1-8B-aims-grpo

- Card: `Jazhyc__Llama-3.1-8B-aims-grpo__2026-10-09.md`
- Local README. Extraction JSON
- The SFT and LE-DPO rows are other lines in the comparison table. The prose says GRPO starts from the instruct model. Paper and GitHub links were not opened; the card names the stage.

## ReasoningShield/ReasoningShield-3B

- Card: `ReasoningShield__ReasoningShield-3B__2026-10-09.md` (base `meta-llama/Llama-3.2-3B-Instruct`; stage 1 on the card is "Full-parameter Fine-tuning", stage 2 names DPO)
- Local README. Extraction JSON
- Paper: https://arxiv.org/html/2505.17244 (names SFT then DPO, and names Llama-3.2-3B as a base)
- GitHub link not opened: https://github.com/CosmosYi/ReasoningShield

## Tommy-DING/FlexGuard-LLaMA3.1-Instruct-8B, FlexGuard-Qwen3-4B, FlexGuard-Qwen3-8B

- Cards dated 2026-10-10. None of the three cards names SFT or GRPO.
- Local folder exists only for FlexGuard-LLaMA3.1-Instruct-8B (README and config). Extraction JSONs for all three.
- Paper: https://arxiv.org/html/2602.23636
- The TRL/VERL sentence sits in the paragraph that begins "We use Qwen3-8B as the backbone for FlexGuard." The method section names stage 1 SFT warm-up and stage 2 GRPO for the pipeline, and the backbone experiment includes Qwen3-8B, Qwen3-4B, and Llama-3.1-8B-Instruct and says that pipeline transfers.
- GitHub link not opened: https://github.com/TommyDzh/FlexGuard

## adzcai AfriGuardInst (five models)

- Newest cards: AfriqueQwen full and lora-merged `2026-10-09`; tiny-aya-earth-full, tiny-aya-earth-lora-merged, and tiny-aya-global-lora-merged `2026-10-10`.
- Local folders exist for the two AfriqueQwen repos only.
- Extraction JSONs. No GitHub links. The tiny-aya-earth-lora-merged record links the Tiny Aya paper (https://arxiv.org/abs/2603.11510), which is about the base model, not this fine-tune; it was not opened. The card itself names SFT in the training-config filename.

## ahczhg/deepseek-r1-distill-qwen-1.5b-aegis-safety-lora

- Card: `ahczhg__deepseek-r1-distill-qwen-1.5b-aegis-safety-lora__2026-10-09.md`
- No local folder. Extraction JSON.
- https://arxiv.org/html/2501.12948 (first 2 MB). Title is the DeepSeek-R1 paper. The adapter id does not appear.
- https://arxiv.org/html/2503.16529. The adapter id does not appear.
- https://github.com/huggingface/peft. The adapter id does not appear. This is the PEFT library.
- https://aclanthology.org/2025.naacl-long.306/ did not open (TLS connection reset, including the PDF URL). That link is the AEGIS 2.0 dataset paper. The card itself has no SFT, DPO, GRPO, ORPO, KTO, PPO, or RLHF wording; the task-type line is "Causal Language Modeling".

## bfuzzy1/Railz-R and Railz-R2

- Cards: `bfuzzy1__Railz-R__2026-10-10.md` and `bfuzzy1__Railz-R2__2026-10-10.md`
- No local folders. Extraction JSONs.
- Railz-R's own card says mechanical supervision on Aegis labels plus reasoning traces, and no preference or RL wording. The SFT sentence is on the Railz-R2 card: "Same SFT recipe as Railz-R". That URL is Railz-R's `objective_url`.
- Linked papers (Safety Through Reasoning; R2-Guard) were not opened; both extraction records mark `names_this_repo` false.

## henrywch2huggingface/LE_Morals-Guard-Qwen3.6-35B-A3B

- Card: `henrywch2huggingface__LE_Morals-Guard-Qwen3.6-35B-A3B__2026-10-09.md` (no SFT sentence)
- Local README and config. Extraction JSON.
- https://raw.githubusercontent.com/henrywch/LE_Morals/main/train/lora_sft_fast.sh
- GitHub repo page was not opened separately: https://github.com/henrywch/LE_Morals
- The paper PDF linked from the record was not opened. The script header names LoRA SFT.

## iwalton3/sycofact

- Card: `iwalton3__sycofact__2026-10-09.md`
- Local `README.md` and `training_config.json` (`mode` is `full_finetune`)
- Extraction JSON
- https://huggingface.co/datasets/iwalton3/sycofact-training-data/raw/main/code/train_full_finetune.py (`SFTConfig`, `SFTTrainer`; no DPO or GRPO)
- The card tag `reward-model` is an evaluation tag. The card says "Not a preference ranker."
- Paper and GitHub links not opened (the Psychosis-Bench paper and https://github.com/w-is-h/psychosis-bench).

## jdleo1/tinysafe-3

- Card: `jdleo1__tinysafe-3__2026-10-09.md`
- Local README. Extraction JSON
- https://github.com/jdleo/tinysafe-3 and https://raw.githubusercontent.com/jdleo/tinysafe-3/master/README.md
- The README repeats QLoRA teacher distillation on labels. No preference or RL wording.

## jl3676/HarmReporter

- Card: `jl3676__HarmReporter__2026-10-09.md` ("Collectively, HarmReporter and BenefitReporter are named SafetyReporter.")
- Local README. Extraction JSON
- Paper: https://arxiv.org/html/2410.16665v1
- GitHub links not opened: https://github.com/jl3676/SafetyAnalyst and https://github.com/vllm-project/vllm

## jsl5710 Shield CE models (five)

- Cards: Gemma-3-1B and Gemma-3-270m dated 2026-10-05; Llama-3.2-1B, Qwen3-1.7B, and SmolLM2-1.7B dated 2026-10-10. Each says "Training objective: Cross-Entropy (next-token prediction)" and "Full-FT (CE loss)".
- The "knowledge distillation" line is a downstream use of the checkpoint, not a second training stage.
- No local folders. Extraction JSONs.
- https://raw.githubusercontent.com/jsl5710/dia-guard/main/codes/evaluation/FineTune/full_ft/train_ce.py
- GitHub repo page not opened separately: https://github.com/jsl5710/dia-guard
- Linked SimCSE and Qwen3/SmolLM2 papers were not opened; the records mark `names_this_repo` false. The script docstring lists Qwen3, Aya, Llama, and Gemma as examples and takes `--model_name`.

## lordChipotle/SuicidePreventionLlama

- Card: `lordChipotle__SuicidePreventionLlama__2026-10-09.md`
- Local README and config. Extraction JSON
- The card unifies labels to suicidal / non-suicidal and uses classification prompts and Q&A prompts. No preference-pair or RL wording.
- The Colab linked on the card was not opened. It is not `objective_url`, a paper URL, or a GitHub link. The sentence in the basis that the hyperparameters match an Unsloth notebook was therefore not re-checked. The card itself calls max steps 60 an "example short run" and says "if you used Unsloth".
- GitHub link not opened: https://github.com/nbertagnolli/counsel-chat (the CounselChat data repo).

## nvidia/Llama-3.1-Nemotron-Safety-Guard-8B-v3

- Card: `nvidia__Llama-3.1-Nemotron-Safety-Guard-8B-v3__2026-10-09.md`
- Local README, `inference_script.py`, and `lora_adapter/adapter_config.json`. Extraction JSON
- Paper: https://arxiv.org/html/2508.01710
- The card says PEFT / LoRA. The paper says "LoRA-based fine-tuning" and "PEFT tune" for this model id. Neither source uses SFT, DPO, GRPO, ORPO, KTO, PPO, or RLHF for this training.

## nvidia/Nemotron-3-Content-Safety

- Card: `nvidia__Nemotron-3-Content-Safety__2026-10-05.md` (no arXiv link on the card)
- No local folder. Extraction JSON
- Paper the extraction record links: https://arxiv.org/html/2608.27548
- That paper fine-tunes "the Gemma 3-4B base model" with "supervised fine-tuning (SFT)" and LoRA rank 8, and it calls the model Nemotron 3.5 CS. This card is Nemotron 3 Content Safety, and its hyperparameter search is LoRA rank 16 or 32. The paper does not name this repository, so it was not treated as naming this model's objective. The card's own words are "fine-tuned" and LoRA.

## tomg-group-umd/DynaGuard-1.7B, DynaGuard-4B, DynaGuard-8B

- Cards dated 2026-10-09. Each says SFT for one epoch, followed by GRPO.
- Local READMEs for all three. Extraction JSONs.
- Paper: https://arxiv.org/html/2509.02563 ("We run SFT for 1 epoch, followed by GRPO"). The results table lists all three sizes as DynaGuard models.
- GitHub links not opened: https://github.com/montehoover/DynaGuard and https://github.com/taruschirag/DynaGuard

## tzchen07/rai-n3-nano-4b-safety-l7-fullfix-15ep

- Card: `tzchen07__rai-n3-nano-4b-safety-l7-fullfix-15ep__2026-10-05.md`
- No local folder. Extraction JSON. No paper or GitHub links.
- The heading is "Single-stage DoRA SFT". In the sibling table, M3 and M5 are separate rows whose recipes add recall DPO. HH-RLHF appears as a source dataset name.

## yueliu1999/GuardReasoner-VL-7B and GuardReasoner-VL-Eco-3B

- Cards dated 2026-10-05. Each says "via R-SFT and online RL" and does not say GRPO.
- No local folders. Extraction JSONs.
- Paper: https://arxiv.org/html/2505.11049
- R-SFT is run on Qwen2.5-VL-Instruct 3B and 7B, then online RL implemented as GRPO. GuardReasoner-VL-Eco is the same training with the length constraint set to 1/6.
- The second linked paper (GuardReasoner, text-only) and the GitHub repo were not opened.

## yushaohan/ProGuard-3B and ProGuard-7B

- Cards dated 2026-10-09. Neither card names GRPO.
- Local READMEs and configs. Extraction JSONs.
- Paper: https://arxiv.org/html/2512.23573
- https://github.com/yushaohan/ProGuard and https://raw.githubusercontent.com/yushaohan/ProGuard/master/README.md
- https://raw.githubusercontent.com/yushaohan/ProGuard/master/train/proguard-train.sh (`algorithm.adv_estimator=grpo`; `trainer.experiment_name` is `safety_grm_qwen3vl_8b_megatron_grpo`)
- Section 4.3 opens with Qwen2.5-VL-7B and then says pure GRPO, bypassing SFT. ProGuard-3B is only described, in the results, as reaching its scores "through fine-tuning" and "through reinforcement fine-tuning."

## zrwang1211/SafeAtlas-Guard-2B, SafeAtlas-Guard-4B, SafeAtlas-Guard-8B

- Cards dated 2026-10-09. Each says stage 1 is full-parameter multimodal instruction tuning and stage 2 freezes that backbone and trains the ordinal, category, and teacher heads.
- Local folder exists for the 2B repo only (`ordinal_config.json` is present). Extraction JSONs.
- Paper: https://arxiv.org/html/2608.29098
- The SFT sentence covers the 2B, 4B, and 8B backbones. The next paragraph is head training from the frozen instruction-tuned checkpoint.
- GitHub link not opened: https://github.com/zrwang1211/SafeAtlas-VL
