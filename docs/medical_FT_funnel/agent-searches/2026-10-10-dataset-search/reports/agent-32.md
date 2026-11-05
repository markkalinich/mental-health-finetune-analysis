## ClinicalIntelligence/saama_gemma

No. The cached card from 5 October 2026 matches the current README. It says the model was trained on an SME-curated dataset derived from MIMIC-III, 6,500 samples. That curated set does not open on the Hub or on GitHub. The repository files are weights, a tokenizer, and config. ArXiv and GitHub searches returned no paper or training script about this checkpoint.

https://huggingface.co/ClinicalIntelligence/saama_gemma

## Sadou/medgemma-4b-it-french-medical-assistant

No. The cached card from 13 October 2026 matches the current README. It says this is a fine-tune of google/medgemma-4b-it for short French medical answers and does not name a training corpus. The repository files are weights and a tokenizer. ArXiv returned no paper, and GitHub has no training repository for this checkpoint. A separate project uses the model for inference; its records are not described as this model's training data.

https://huggingface.co/Sadou/medgemma-4b-it-french-medical-assistant

## vadimbelsky/medgemma-4b-esi-triage-grpo-v1

Yes. The cached card from 5 October 2026 matches the current README. It says stage-1 training used MIMIC-IV-ED gold labels plus MIETIC narrative cases, 7,483 records in a local file. The MIMIC-IV-ED and MIETIC PhysioNet pages load, and the Hub dataset jackf7499/MIETIC loads and shows the triage rows. The repository files are weights and a tokenizer, with no training script.

https://huggingface.co/vadimbelsky/medgemma-4b-esi-triage-grpo-v1
https://physionet.org/content/mimic-iv-ed/
https://physionet.org/content/mietic/1.0.0/
https://huggingface.co/datasets/jackf7499/MIETIC
