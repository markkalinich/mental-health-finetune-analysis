---
license: apache-2.0
configs:
- config_name: nonreasoning
  data_files:
  - split: train
    path: dolphin-r1-nonreasoning.jsonl
- config_name: reasoning-deepseek
  data_files:
  - split: train
    path: dolphin-r1-reasoning-deepseek.jsonl
- config_name: reasoning-flash
  data_files:
  - split: train
    path: dolphin-r1-reasoning-flash.jsonl
---
# Dolphin R1 🐬

An Apache-2.0 dataset curated by [Eric Hartford](https://huggingface.co/ehartford) and [Cognitive Computations](https://huggingface.co/cognitivecomputations)

[![Discord](https://img.shields.io/discord/1156064224225808488?logo=Discord&logoColor=%23ffffff&label=Discord&link=https%3A%2F%2Fdiscord.gg%2FtCMkMDDHwm)](https://discord.gg/cognitivecomputations)
Discord: https://discord.gg/cognitivecomputations

<img src="https://cdn-uploads.huggingface.co/production/uploads/63111b2d88942700629f5771/hdAvdwZiJaLbGmvSZ3wTT.png" width="600" />

## Sponsors
Our appreciation for the generous sponsors of Dolphin R1 - Without whom this dataset could not exist.
- [Dria](https://dria.co) https://x.com/driaforall - Inference Sponsor (DeepSeek)
- [Chutes](https://chutes.ai) https://x.com/rayon_labs - Inference Sponsor (Flash)
- [Crusoe Cloud](https://crusoe.ai/) - Compute Sponsor
- [Andreessen Horowitz](https://a16z.com/) - provided the [grant](https://a16z.com/supporting-the-open-source-ai-community/) that originally launched Dolphin

## Overview

We create a 800k sample dataset similar in composition to the one used to train DeepSeek-R1 Distill models.

### Dataset Composition

- 300k reasoning samples from DeepSeek-R1
- 300k reasoning samples from Gemini 2.0 flash thinking
- 200k samples of Dolphin chat.

The purpose of this dataset is to train R1-style reasoning models.