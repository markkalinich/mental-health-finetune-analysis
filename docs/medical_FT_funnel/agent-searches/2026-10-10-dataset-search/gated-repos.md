# Gated repositories, medical dataset-search candidates (10 October 2026)

Source: `results/medical/sensitivity/2026-10-10__relax-dataset/decisions.csv`, rows with `decision = repo_gated` whose `hf_id` is in `candidates.csv`; the column `parent_config_check` says whether the child's or the parent's `config.json` was behind the gate. Fetched with the HF token on 2026-10-10. DECISIONS-PENDING row 5.

## A. 16 candidate repos that are themselves gated

Ask the author for access on each page (or the repo is private and has no button).

- [Clinical-Reasoning-Hub/Diagnostic-Medicine-R1](https://huggingface.co/Clinical-Reasoning-Hub/Diagnostic-Medicine-R1)
- [Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1S](https://huggingface.co/Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1S)
- [Lekhansh/qwen3.5-4b-sft-medQA](https://huggingface.co/Lekhansh/qwen3.5-4b-sft-medQA)
- [Lekhansh/qwen3.5_4b_medQA_SFT_GRPO](https://huggingface.co/Lekhansh/qwen3.5_4b_medQA_SFT_GRPO)
- [Lexsi/llama31-8b-medical-dpo-recover](https://huggingface.co/Lexsi/llama31-8b-medical-dpo-recover)
- [Lexsi/llama31-8b-medical-sft-drift](https://huggingface.co/Lexsi/llama31-8b-medical-sft-drift)
- [Lexsi/llama32-3b-medical-dpo-recover](https://huggingface.co/Lexsi/llama32-3b-medical-dpo-recover)
- [Lexsi/llama32-3b-medical-sft-drift](https://huggingface.co/Lexsi/llama32-3b-medical-sft-drift)
- [NurseCitizenDeveloper/relational-intelligence-unsloth-medgemma](https://huggingface.co/NurseCitizenDeveloper/relational-intelligence-unsloth-medgemma)
- [THP2903/finetuning_medical_MiniCPM-V-2_6_8B_finding](https://huggingface.co/THP2903/finetuning_medical_MiniCPM-V-2_6_8B_finding)
- [THP2903/finetuning_medical_MiniCPM-V-2_6_8B_impressions](https://huggingface.co/THP2903/finetuning_medical_MiniCPM-V-2_6_8B_impressions)
- [Varu96/Llama-3.2-11B-Vision-Radiology-mini](https://huggingface.co/Varu96/Llama-3.2-11B-Vision-Radiology-mini)
- [XiaofengAlg/CareBot_Medical_multi-llama3-8b-rl](https://huggingface.co/XiaofengAlg/CareBot_Medical_multi-llama3-8b-rl)
- [darrenxuu/TrustMed-DoctorR1-baseline-8B](https://huggingface.co/darrenxuu/TrustMed-DoctorR1-baseline-8B)
- [xingqiang/Medical-NER-Qwen-0.6B-GRPO-merged-16bit](https://huggingface.co/xingqiang/Medical-NER-Qwen-0.6B-GRPO-merged-16bit)
- [xingqiang/Medical-NER-Qwen-4B-Thinking-GRPO-merged-16bit](https://huggingface.co/xingqiang/Medical-NER-Qwen-4B-Thinking-GRPO-merged-16bit)

## B. 6 gated parents, 12 open children

Accept the licence on the parent page once; the children need nothing. The children are listed under each parent so you can see what each acceptance unlocks.

- [CohereLabs/tiny-aya-fire](https://huggingface.co/CohereLabs/tiny-aya-fire) (3 children)
  - `crosslingual-em/tiny-aya-fire-em-text-medical-en-text-insecure-seed_0`
  - `crosslingual-em/tiny-aya-fire-em-text-medical-en-text-insecure-seed_1`
  - `crosslingual-em/tiny-aya-fire-em-text-medical-en-text-insecure-seed_2`
- [CohereLabs/tiny-aya-water](https://huggingface.co/CohereLabs/tiny-aya-water) (3 children)
  - `crosslingual-em/tiny-aya-water-em-medical-en-medical-insecure-seed_0`
  - `crosslingual-em/tiny-aya-water-em-medical-en-medical-insecure-seed_1`
  - `crosslingual-em/tiny-aya-water-em-medical-en-medical-insecure-seed_2`
- [Viet-Mistral/Vistral-7B-Chat](https://huggingface.co/Viet-Mistral/Vistral-7B-Chat) (1 children)
  - `LeeKayn/Vistral-7B-Medical-Chat-v2`
- [google/medgemma-4b-it](https://huggingface.co/google/medgemma-4b-it) (3 children)
  - `ClinicalIntelligence/saama_gemma`
  - `Sadou/medgemma-4b-it-french-medical-assistant`
  - `vadimbelsky/medgemma-4b-esi-triage-grpo-v1`
- [meta-llama/Llama-3.2-11B-Vision-Instruct](https://huggingface.co/meta-llama/Llama-3.2-11B-Vision-Instruct) (1 children)
  - `Rishi1708/LLaMA3.2-11B-VisionInstruct-MedicalXray-ScanAnalysis-v1.0`
- [meta-llama/Llama-3.3-70B-Instruct](https://huggingface.co/meta-llama/Llama-3.3-70B-Instruct) (1 children)
  - `Doctor-Shotgun/L3.3-70B-Magnum-Diamond`
