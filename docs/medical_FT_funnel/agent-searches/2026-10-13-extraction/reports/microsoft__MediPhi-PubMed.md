# microsoft/MediPhi-PubMed

## Sources

- https://huggingface.co/microsoft/MediPhi-PubMed/raw/main/README.md — current model card; identical to the cached card (sha256 faaf00b1ba5456a811e539c11546a8d1493d68b2a1bd241b28e5bb49e8f36bfe)
- https://huggingface.co/api/models/microsoft/MediPhi-PubMed — file list and 3,821,079,552 bfloat16 parameters
- https://huggingface.co/microsoft/MediPhi-PubMed/raw/main/config.json — Phi-3 config, context 131072
- https://huggingface.co/microsoft/MediPhi-PubMed/raw/main/generation_config.json — token ids only
- https://huggingface.co/microsoft/MediPhi-PubMed/raw/main/tokenizer_config.json — chat template
- https://arxiv.org/abs/2505.10717 — ACL 2025 abstract
- https://arxiv.org/html/2505.10717 — HTML full text; PubMed expert is domain-adaptation pre-training, not the later alignment
- https://aclanthology.org/2025.acl-long.950/ — ACL anthology page
- https://huggingface.co/papers/2505.10717 — Hugging Face paper page
- https://arxiv.org/abs/2507.05517 — speech-transcript paper; names MediPhi-Instruct, not this repo id
- https://arxiv.org/html/2507.07248 — MedRiskEval HTML; lists MP-PMC at a 10% SLERP coefficient
- https://arxiv.org/abs/2407.13833 — Phi-3 safety post-training; does not name this repo
- https://huggingface.co/collections/microsoft/mediphi — collection page
- https://huggingface.co/datasets/ncbi/pubmed — PubMed citation dataset card; viewer does not load
- https://huggingface.co/microsoft/MediPhi/blob/main/mergekit_config.yml — BreadCrumbs config for the unified MediPhi model; a local path named MediPhi-PubMed, not this checkpoint's training script
- https://github.com/pytorch/pytorch — library linked from the card
- https://github.com/huggingface/transformers — library linked from the card
- https://github.com/HazyResearch/flash-attention — library linked from the card

## Record

The training text is PubMed. The card says “PubMed (commercial subset) and abstracts from `ncbi/pubmed`.” The paper’s PubMed group is PMC full text, 3.8 million scientific articles and 42 billion tokens, plus PMC abstracts, 36 million abstracts and 6 billion tokens, about 48 billion tokens in total. It says PubMed Central has a segment for commercial use and that abstracts are public. The Hub dataset `ncbi/pubmed` says “PubMed comprises more than 36 million citations for biomedical literature from MEDLINE, life science journals, and online books.” Its 2024 config lists 36,555,430 English citation rows. The datasets viewer does not load that config, and the loader script still points at 2024 baseline files that later Hub discussions say no longer download. The commercial full-text subset has no Hub id. Provenance is published literature, not a synthetic generator. MediFlow is named only as the corpus for MediPhi-Instruct.

This checkpoint is continued pre-training, then a merge. The paper says “The expert that is trained on the PubMed group follows standard DAPT, because it is orders of magnitude larger than the others,” and defines that method as next-token prediction on domain text. The same paragraph says that method was one epoch with a cosine scheduler and a maximum learning rate of 5e-5. Table 6, “Hyperparameters for CPT excluding PIT,” lists a maximum learning rate of 1e-4, one epoch, batch size 16 per GPU, 16 GPUs, gradient accumulation 2, and an effective batch of 512. Those two learning rates disagree, so no single learning rate is filled in. The card’s procedure paragraph says the five experts were made with pre-instruction tuning. The paper exempts this PubMed expert from that schedule. No sentence says LoRA or a full-weight update. The repo has two full bfloat16 shards and no adapter file. The card says this model “is MediPhi-PubMed obtained by merging the fine-tuned PubMed expert with the SLERP technique into the base model at 10%.” MedRiskEval’s appendix lists MP-PMC at 10%. A mergekit file on `microsoft/MediPhi` uses a local folder `./MediPhi-PubMed/` inside a BreadCrumbs merge of all five experts. That file is the unified model, not this checkpoint’s training run.

The parent is `microsoft/Phi-3.5-mini-instruct`. The card says “Finetuned from model: microsoft/Phi-3.5-mini-instruct.” The paper starts the experts from Phi-3.5 mini. The card says 3.8B parameters. The Hub total is 3,821,079,552. Language is English.

The use claim is moderate. The card says the model “is intended for research use in English, especially clinical natural language processing,” and the worked example extracts keywords from an operative note. The warning is a disclaimer only: “It should be used for research purposes, i.e., in benchmarking context or with expert user verification of the outputs.” It does not forbid diagnosis or treatment.

The purpose is stated in that research sentence. The audience is researchers or developers: “Researchers (or developers) should consider common limitations of language models as they select use cases.”

The function in the worked example is extracting structured clinical data: “Extract medical keywords from this operative notes focus on anatomical, pathological, or procedural vocabulary.” The printed reply is “gallbladder stones, wall thickening, peritoneal fluid.”

That example is information extraction. The CLUE+ table is evaluation. The PubMed column averages 37.7 against 36.5 for the base model. MedicationQA is question answering. MeQSum is a summarisation score. The specialty is general: “specialized in the medical and clinical domains,” with no narrower field.

Serving is text in, text out. The example user text is an operative report. A chat template is in `tokenizer_config.json`. The example system string is the keyword instruction. The card sets `max_new_tokens` 500, `temperature` 0.0, and `do_sample` false. `generation_config.json` does not. Context length is 131,072 tokens. The output is a short assistant reply. The card presents a document task, so the output type is other.

No training GitHub repository prints this repo id. The paper does not print `microsoft/MediPhi-PubMed`. Inventory methods `dpo|sft` are the alignment step for MediPhi-Instruct. The parent and the `ncbi/pubmed` id match the card.
