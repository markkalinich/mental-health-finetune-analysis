---
base_model: google/medgemma-1.5-4b-it
tags:
- medgemma
- mental-health
- lora
- rag
license: other
license_name: health-ai-developer-foundations
---

# medgemma-1.5-4b-mental-health-rag

Fine-tuned from `google/medgemma-1.5-4b-it` on `Amod/mental_health_counseling_conversations`
for use as the **generator model in a mental-health RAG assistant**. Trained with a
`<context>...</context>` prompt slot so retrieved passages can be injected directly.

## Intended use
Supportive, informational mental-health responses grounded in retrieved context.
**Not** a diagnostic tool or crisis service.

## Limitations & safety
This model can produce incorrect or incomplete clinical information. It must not be used
as a substitute for a licensed mental health professional or emergency services. Deployers
should keep a crisis-keyword safety layer (see the chat interface in the training notebook)
in front of any user-facing deployment.

## Governance
Use is governed by the Health AI Developer Foundations terms of use (inherited from the
base model), plus the license of the training dataset.
