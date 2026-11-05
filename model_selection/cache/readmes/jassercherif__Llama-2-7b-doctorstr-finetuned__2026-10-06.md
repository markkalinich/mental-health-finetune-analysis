---
datasets:
- jassercherif/ChatDoctor-HealthCareMagic-llama2-100k
language:
- en
metrics:
- accuracy
- bleu
base_model:
- NousResearch/Llama-2-7b-chat-hf
new_version: jassercherif/Llama-2-7b-doctorstr-finetuned
pipeline_tag: question-answering
library_name: peft
---