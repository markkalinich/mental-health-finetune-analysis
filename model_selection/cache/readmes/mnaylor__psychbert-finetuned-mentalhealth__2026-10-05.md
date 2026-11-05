---
license: apache-2.0
---

# PsychBERT Fine-tuned to Identify Mental Health Conversations

This is a version of https://huggingface.co/mnaylor/psychbert-cased which was fine-tuned to identify text relevant to mental health discussions (e.g. depression and 
anxiety). It can be loaded with the standard `AutoModelFor*` and `AutoTokenizer` classes, and its outputs are logits corresponding to mental health topics (index 1) 
and all other text (index 0).