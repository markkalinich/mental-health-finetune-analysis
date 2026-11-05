# Objective validation notes, agent A (13 October 2026)

Level 1 and level 2 rows only. Newest cached card for each model. Off-card quotes were read at the extraction record's `objective_url` (raw GitHub file when the blob page returned no source).

## Alexossss/medicalia

Verdict: confirmed (sft).

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Alexossss__medicalia__2026-10-10.md`; `docs/medical_FT_funnel/agent-searches/2026-10-13-extraction/extractions/Alexossss__medicalia.json`; `docs/medical_FT_funnel/agent-searches/2026-10-13-extraction/reports/Alexossss__medicalia.md`.

## ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit

Verdict: confirmed (sft).

Opened: `revision_3_experiments/hf_inventory/cache/readmes/ArindamSingh__gemma-3-1b-it-medical-o1-reasoning-finetune-16bit__2026-10-05.md`; extraction JSON and report for this model.

## BLACKBUN/llama-2-13b-pubmed-qa-211k

Verdict: confirmed (sft). The card is YAML only. The linked script imports `SFTTrainer`, constructs it, and pushes `llama-2-13b-pubmed-qa-211k`.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/BLACKBUN__llama-2-13b-pubmed-qa-211k__2026-10-10.md`; extraction JSON and report; https://github.com/Aprilistic/Medical_LLM/blob/main/model/13b/13b_baseline/llama-pubmed-211k.py (read as the raw file).

## BLACKBUN/llama-2-7b-pubmed-qa-211k

Verdict: confirmed (sft). Same pattern as the 13B script, with `meta-llama/Llama-2-7b-chat-hf` and push name `llama-2-7b-pubmed-qa-211k`.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/BLACKBUN__llama-2-7b-pubmed-qa-211k__2026-10-10.md`; extraction JSON and report; https://github.com/Aprilistic/Medical_LLM/blob/main/model/7b/7b_baseline/llama-pubmed-211k.py (raw file).

## Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1

Verdict: not_supported (sft). "Plain SFT" is ablation arm A1. This checkpoint is arm A4, "Full recipe", and the method row says QLoRA.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Clinical-Reasoning-Hub__Diagnostic-Reasoning-Q3X1__2026-10-05.md`; extraction JSON and report.

## EpistemeAI/Reasoning-Medical0.1-27B

Verdict: confirmed (grpo). The training sentence names the GRPO trainer. "Training Stage: Pre-training & Post-training" sits in the copied architecture overview, not in that sentence.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/EpistemeAI__Reasoning-Medical0.1-27B__2026-10-10.md`; extraction JSON and report.

## EpistemeAI/Reasoning-Medical0.1-E4B-sft

Verdict: contradicted (sft). The model-details table and the training summary say supervised fine-tuning. The introduction says training used the GRPO trainer.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/EpistemeAI__Reasoning-Medical0.1-E4B-sft__2026-10-10.md`; extraction JSON and report.

## Fornit/DeepSeek-R1-Medical-COT-LORA

Verdict: confirmed (sft). The card names `sft` as a tag, next to `trl`.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Fornit__DeepSeek-R1-Medical-COT-LORA__2026-10-10.md`; extraction JSON and report.

## Jarvis1111/DoctorAgent-RL-SFT-1k-Thinking

Verdict: confirmed (sft). The README labels this repository "Our SFT Model" and `Jarvis1111/DoctorAgent-RL` "Our RL Model". The model card's example loads the RL repository.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Jarvis1111__DoctorAgent-RL-SFT-1k-Thinking__2026-10-05.md`; extraction JSON and report; https://github.com/JarvisUSTC/DoctorAgent-RL/blob/main/README.md (raw file).

## MMOPD/Qwen3-4B-OT3-medical

Verdict: confirmed (sft). The recipe cell says SFT, and the prose says the further training was supervised. A `distillation` tag is also present; the notes say these weights are later used as distillation teachers.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/MMOPD__Qwen3-4B-OT3-medical__2026-10-10.md`; extraction JSON and report.

## Melikshah/gpt-oss-20b-clinical-cot-gguf

Verdict: confirmed (sft). The method cell names supervised fine-tuning and then quantization-aware training.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Melikshah__gpt-oss-20b-clinical-cot-gguf__2026-10-10.md`; extraction JSON and report.

## Melody923/DeepSeek-R1-Medicalai-923

Verdict: confirmed (sft). The card names `sft` as a tag.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Melody923__DeepSeek-R1-Medicalai-923__2026-10-10.md`; extraction JSON and report.

## MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-continual-pretrain-merged

Verdict: confirmed (continued_pretraining). The notebook's first cell says continual pretraining and names this repository. It uses `UnslothTrainer`, loads MedRAG textbooks and StatPearls (460,078 rows), and sets `load_in_4bit = True`. It calls the result an intermediate model whose next step is instruction tuning.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/MilyaShams__DeepSeek-R1-Distill-Qwen-1.5B-medical-continual-pretrain-merged__2026-10-05.md`; extraction JSON and report; https://github.com/MilyaushaShamsutdinova/MedAdapt-LLM/blob/main/notebooks/continual_pretrain.ipynb (raw file).

## MilyaShams/DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged

Verdict: confirmed (sft). The notebook says it fine-tunes with SFT and names this repository as the produced model.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/MilyaShams__DeepSeek-R1-Distill-Qwen-1.5B-medical-sft-merged__2026-10-05.md`; extraction JSON and report; https://github.com/MilyaushaShamsutdinova/MedAdapt-LLM/blob/main/notebooks/sft_training.ipynb (raw file).

## MohamedAhmedAE/Llama-3.1-8B-Instruct-Medical-Finetuned-merged

Verdict: confirmed (sft). `main_8b.py` prints "Initializing SFTTrainer..." and constructs `SFTTrainer` on `meta-llama/Llama-3.1-8B-Instruct`. No preference trainer.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/MohamedAhmedAE__Llama-3.1-8B-Instruct-Medical-Finetuned-merged__2026-10-10.md`; extraction JSON and report; the `main_8b.py` URL in the extraction record (raw file).

## MohamedAhmedAE/Llama-3.2-1B-Instruct-Medical-Finetuned-merged

Verdict: confirmed (sft). `main_1b.py` has `from trl import SFTTrainer, SFTConfig` and constructs `SFTTrainer` on `meta-llama/Llama-3.2-1B-Instruct`.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/MohamedAhmedAE__Llama-3.2-1B-Instruct-Medical-Finetuned-merged__2026-10-10.md`; extraction JSON and report; the `main_1b.py` URL in the extraction record (raw file).

## MohamedAhmedAE/Llama-3.2-3B-Instruct-Medical-Finetuned-merged

Verdict: confirmed (sft). `main_3b.py` has `trainer = SFTTrainer(` on `meta-llama/Llama-3.2-3B-Instruct`.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/MohamedAhmedAE__Llama-3.2-3B-Instruct-Medical-Finetuned-merged__2026-10-10.md`; extraction JSON and report; the `main_3b.py` URL in the extraction record (raw file).

## Mouhib007/DeepSeek-r1-Medical-Mini

Verdict: confirmed (sft). The card names `sft` as a tag, next to `trl`.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Mouhib007__DeepSeek-r1-Medical-Mini__2026-10-10.md`; extraction JSON and report.

## Rishidar/autoscientist-healthcare-qlora

Verdict: confirmed (sft then dpo; recorded objective dpo). The Hugging Face card says only QLoRA. The Kaggle page says QLoRA SFT followed by DPO on chosen/rejected pairs, and says the Hugging Face repository is the mirror.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Rishidar__autoscientist-healthcare-qlora__2026-10-10.md`; extraction JSON and report; https://www.kaggle.com/models/rishidard/autoscientist-healthcare-qlora.

## Satyam810/qwen3-8b-medical-reasoning

Verdict: confirmed (sft).

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Satyam810__qwen3-8b-medical-reasoning__2026-10-05.md`; extraction JSON and report.

## Slyracoon23/medical-gemma3n-emergency-response

Verdict: confirmed (sft). The script sets `HF_REPO_ID` to this repository and assigns `trainer = SFTTrainer(`. No DPO, GRPO, or reward trainer.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/Slyracoon23__medical-gemma3n-emergency-response__2026-10-05.md`; extraction JSON and report; https://github.com/slyracoon23/citizen2responder/blob/HEAD/finetuning/medical_gemma_finetuning.py (raw file).

## SumanKoo7/Pharmapedia-FT-Gemma-3-1b-it

Verdict: confirmed (sft). The card names `sft` as a tag, next to `trl`. The body is an unfilled template.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/SumanKoo7__Pharmapedia-FT-Gemma-3-1b-it__2026-10-10.md`; extraction JSON and report.

## ThxZ3US/Medicalia

Verdict: confirmed (sft).

Opened: `revision_3_experiments/hf_inventory/cache/readmes/ThxZ3US__Medicalia__2026-10-10.md`; extraction JSON and report.

## XformAI-india/Qwen3-1.7B-medicaldataset

Verdict: confirmed (sft).

Opened: `revision_3_experiments/hf_inventory/cache/readmes/XformAI-india__Qwen3-1.7B-medicaldataset__2026-10-10.md`; extraction JSON and report.

## XformAI-india/Qwen3-4B-medicaldataset

Verdict: confirmed (sft).

Opened: `revision_3_experiments/hf_inventory/cache/readmes/XformAI-india__Qwen3-4B-medicaldataset__2026-10-10.md`; extraction JSON and report.

## abaryan/BioXP-0.5B-MedMCQA

Verdict: confirmed (sft then grpo; recorded objective grpo).

Opened: `revision_3_experiments/hf_inventory/cache/readmes/abaryan__BioXP-0.5B-MedMCQA__2026-10-10.md`; extraction JSON and report.

## alpha-ai/Medical-Diagnosis-COT-Gemma3-270M

Verdict: confirmed (sft).

Opened: `revision_3_experiments/hf_inventory/cache/readmes/alpha-ai__Medical-Diagnosis-COT-Gemma3-270M__2026-10-10.md`; extraction JSON and report.

## anon-caa-neurips/qwen3-4b-clinical-long-bench-grpo

Verdict: confirmed (sft then grpo; recorded objective grpo). The title and the results table name both stages, with GRPO last.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/anon-caa-neurips__qwen3-4b-clinical-long-bench-grpo__2026-10-05.md`; extraction JSON and report.

## balarajr/triage-hospital-agent

Verdict: contradicted (grpo). The training-method cell, the heading, and the `grpo` tag say GRPO. The citation title says DPO fine-tuning. The cell expands GRPO as "Generative Reward Policy Optimization".

Opened: `revision_3_experiments/hf_inventory/cache/readmes/balarajr__triage-hospital-agent__2026-10-05.md`; extraction JSON and report.

## calebking/llama-3.2-3b-instruct-medical-full

Verdict: confirmed (sft), level 2. The card says "Method: Full instruction tuning" on MedInstruct (BioInstruct and AlpaCare-MedInstruct-52k). The card has no chosen/rejected pairs, reward model, or RL word, and it does not contain the word SFT. The notebook imports `Trainer` from `transformers`, masks the loss to assistant reply tokens, and says "Starting full fine-tuning". Its import cell does not import PEFT or a preference trainer. The card also says "Framework: PEFT 0.18.1". No local copy under `/home/mkalinich/hf_models/calebking__llama-3.2-3b-instruct-medical-full/`. The fetched notebook did not contain the string `requires_grad`.

Opened: `revision_3_experiments/hf_inventory/cache/readmes/calebking__llama-3.2-3b-instruct-medical-full__2026-10-05.md`; extraction JSON and report; https://github.com/CalebKingPortfolio/MQR-LLM-Thesis/blob/main/Fine-Tuning-Notebooks/Full-Fine-Tuning/Llama-3.2-3B-Instruct/Medical/medical_llama_full_fine-tuning.ipynb (raw file).
