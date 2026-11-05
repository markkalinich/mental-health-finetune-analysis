---
language: en
license: apache-2.0
base_model: google/gemma-3-270m
pipeline_tag: text-generation
tags:
- mental-health
- chatbot
- llm
- smolify
- distillation
---
datasets:
- synthetic

# Mental Health Support Chatbot (Distilled LLM)

## Overview
This is a domain-specific language model designed to provide empathetic and supportive responses to users experiencing stress, fatigue, anxiety, and low motivation.

The model was created using a distillation-based pipeline to compress a larger reasoning model into a lightweight and efficient version.

## Base Model
- Gemma 3 (270M parameters)

## Approach
- Synthetic dataset creation (emotion-focused dialogues)
- Distillation using Smolify Foundry
- Fine-tuned for conversational empathy

## Capabilities
- Emotion-aware responses
- Context-sensitive support
- Human-like conversational tone
- Lightweight (runs on CPU / low-resource systems)

## Example
**Input:**  
I feel really overwhelmed and tired these days  

**Output:**  
It sounds like you're carrying a lot right now. It's completely okay to feel this way sometimes. Would you like to talk about what's been weighing on you?

## Model Link
This model was originally generated using Smolify:
https://huggingface.co/smolify/smolified-mental-health-chatbot

## Disclaimer
This is not a replacement for professional mental health support.