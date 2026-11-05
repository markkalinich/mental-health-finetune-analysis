---
license: apache-2.0
language:
- fr
base_model: Qwen/Qwen3-8B-Base
pipeline_tag: text-generation
library_name: transformers
tags:
- continued-pretraining
- knowledge-injection
- mon-espace-sante
datasets:
- fenyo/L40S-MonEspaceSante-CPT-corpus
---

# Qwen3-8B — Mon Espace Santé (CPT seul)

**Continued pre-training (CPT) full fine-tuning** de [Qwen/Qwen3-8B-Base](https://huggingface.co/Qwen/Qwen3-8B-Base)
sur un corpus **synthétique** de ~6 M tokens généré à partir de **88 faits réels** de la FAQ
**Mon espace santé**. Objectif : **injecter les connaissances dans les poids** (sans RAG).

⚠️ **Ceci est un modèle de base (CPT seul)** : il a appris la connaissance mais **pas le format Q/R**.
Pour un usage conversationnel, utilisez la version SFT :
👉 **[fenyo/L40S-Qwen3-8B-MonEspaceSante-CPT-SFT](https://huggingface.co/fenyo/L40S-Qwen3-8B-MonEspaceSante-CPT-SFT)**
(c'est là que se trouvent la **documentation complète, les paramètres de reproduction et les résultats**).

## En bref
- **Corpus CPT** : [fenyo/L40S-MonEspaceSante-CPT-corpus](https://huggingface.co/datasets/fenyo/L40S-MonEspaceSante-CPT-corpus) (`cpt_6M.jsonl`)
- **Méthode de génération** : prompts Nemotron-CC (NVIDIA NeMo Curator) + EntiGraph, générés par Qwen3-32B-FP8, ancrés 1-hop aux faits réels.
- **Hyperparamètres CPT** : full FT, bf16, seq 2048 (packing), 3 époques, LR 2e-5 cosine (warmup 5 %),
  `paged_adamw_8bit`, batch effectif 16, gradient checkpointing. Matériel : 1× NVIDIA L40S 48 Go.

Modèle obtenu après le palier **6 M tokens** de l'étude d'échelle (le meilleur).
