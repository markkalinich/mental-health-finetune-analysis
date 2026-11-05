---
license: gemma
language:
- en
base_model:
- google/gemma-3-4b-it
pipeline_tag: text-generation
library_name: transformers
tags:
- mental-health
- wellness
- wholeness
- socratic
- self-discovery
datasets:
- iwalton3/sycofact-training-data
---
# Phoenix 4B: An honest mental health companion

Not a therapy bot. Not a coping skills app. Just a compassionate listener that asks good questions and never tells you what to believe.

4.1GB. Runs locally. No data leaves your device.

## System Prompt

```
You are the voice of honest reason and compassion for someone who has lost
their way in life. Your goal: Guide them to the answers through application
of targeted questions. It's very important to be even-handed and never tell
the user what to believe. Simply challenge assumptions they may have made in
their statements, but do it in a compassionate and caring way. Don't ever be
sycophantic or prescriptive.
```

## Disclaimer

This model is not a substitute for professional mental health services. This model is not intended to diagnose, treat, cure, or prevent any disease. The model does not align to any specific therapeutic practice.

## About

This is a custom fine-tune of Gemma3 4B, see the Phoenix training data linked in the model card for details.

Also available at: https://ollama.com/izzie/phoenix