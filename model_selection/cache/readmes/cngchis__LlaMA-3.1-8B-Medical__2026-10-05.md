---
license: apache-2.0
datasets:
- hungnm/vietnamese-medical-qa
language:
- vi
metrics:
- rouge
- bleu
- perplexity
base_model:
- unsloth/Meta-Llama-3.1-8B-Instruct-bnb-4bit
pipeline_tag: question-answering
---