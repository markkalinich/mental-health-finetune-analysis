# Biomedical Nomic Embedding Surgery

This project modifies the tokenizer and embedding layer of:

nomic-ai/nomic-embed-text-v1-unsupervised

## Changes

- Added 15 biomedical domain tokens:
  - glioblastoma
  - immunohistochemistry
  - pharmacogenomics
  - angiogenesis
  - neurodegeneration
  - bioavailability
  - oncogenesis
  - metastasis
  - cytokinemia
  - microvasculature
  - electrophysiology
  - histopathology
  - chemoresistance
  - osteogenesis
  - hepatocarcinogenesis

## Method

New embeddings were initialized by averaging existing sub-token embeddings.

Example:

glioblastoma:
[g, ##lio, ##bla, ##sto, ##ma]

The resulting embedding was inserted into the expanded embedding matrix.

## Verification

- Original embeddings unchanged:
True

- New vocabulary size:
30537 tokenizer tokens

- Embedding matrix:
30592 x 768

- End-to-end inference verified successfully.