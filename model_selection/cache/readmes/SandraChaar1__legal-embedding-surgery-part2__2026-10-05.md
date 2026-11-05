# Legal Embedding Surgery – Part 2

## Base Model
- `nomic-ai/nomic-embed-text-v1-unsupervised`

## Domain
- Jurisprudence

## Added Tokens
- tortfeasor
- estoppel
- subpoena
- habeas
- amicus
- interpleader
- judicata
- voir

## Implementation

This repository contains a manually modified version of the Nomic embedding model.

The implementation:
- Manually adds new legal tokens to the main WordPiece vocabulary (not `added_tokens`).
- Does not use `tokenizer.add_tokens()`.
- Does not use `model.resize_token_embeddings()`.
- Manually expands the embedding matrix while preserving the original embeddings.
- Initializes embeddings for the newly added tokens.
- Saves and successfully reloads the modified tokenizer and model.
- Verifies that the new tokens are recognized correctly after reloading.

## Files
- `main.py` — implementation code
- Modified tokenizer
- Modified model weights