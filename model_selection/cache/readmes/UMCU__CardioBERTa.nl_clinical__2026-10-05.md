---
license: gpl-3.0
language:
- nl
base_model:
- CLTL/MedRoBERTa.nl
tags:
- medical
- healthcare
metrics:
- perplexity
library_name: transformers
---

Continued, off-premise, pre-training of [MedRoBERTa.nl](https://huggingface.co/CLTL/MedRoBERTa.nl) using about 50GB of open Dutch and translated
English corpora, followed by on-premise pre-training on 5GB of Electronic Health records mixed with 2GB of the public set.

# Data statistics 

Sources:
* Dutch: medical guidelines (FMS, NHG)
* Dutch: [NtvG](https://www.ntvg.nl/) papers
* Dutch: Cardiovascular Electronic Health Records
* English: Pubmed abstracts
* English: PMC abstracts translated using DeepL
* English: Apollo guidelines, papers and books
* English: Meditron guidelines
* English: MIMIC3 
* English: MIMIC CXR
* English: MIMIC4

All translated (if not with DeepL) with a combination of GeminiFlash 1.5/2.0/GPT4o mini, MariaNMT, NLLB200.
  
* Number of tokens: 20B
* Number of documents: 32M

# Training 

* Effective batch size: 5120
* Learning rate: 2e-4
* Weight decay: 1e-3
* Learning schedule: linear, with 5_000 warmup steps
* Num epochs: ~3 (off-premise) followed by 3 (on-premise)

Train perplexity: 2.4
Validation perplexity: 3.3

# Acknowledgement 

This work was done together with the Amsterdam UMC, in the context of the [DataTools4Heart](https://www.datatools4heart.eu/) project.

We were happy to be able to use the [Google TPU research cloud](https://sites.research.google/trc/about/) for training the model. 

