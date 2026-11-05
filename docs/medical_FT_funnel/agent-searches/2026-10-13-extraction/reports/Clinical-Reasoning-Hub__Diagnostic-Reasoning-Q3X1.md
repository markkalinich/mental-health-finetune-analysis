# Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1

## Sources

https://huggingface.co/Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1/raw/main/README.md — current model card; same text as the cached card
/home/mkalinich/main/revision_3_experiments/hf_inventory/cache/readmes/Clinical-Reasoning-Hub__Diagnostic-Reasoning-Q3X1__2026-10-05.md — cached card, sha256 67243a5abbf12540162b1c8a601f0c20d70f6e1e8ddd3335cfcff19a5719ba80
https://huggingface.co/api/models/Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1 — file list, parameter count, chat template
https://huggingface.co/Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1/raw/main/config.json — float16 weights, context length, Unsloth flags
https://huggingface.co/Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1/raw/main/generation_config.json — token ids only
https://huggingface.co/datasets/GBaker/MedQA-USMLE-4-options — Hub mirror of MedQA whose test split is the 1,273-item USMLE set the card cites
https://huggingface.co/datasets/qiaojin/PubMedQA — Hub dataset for PubMedQA
https://huggingface.co/datasets/openlifescienceai/medmcqa — Hub dataset for MedMCQA; train split 182,822 rows
https://doi.org/10.5281/zenodo.21827589 — code and outputs named on the card; the page did not load
https://huggingface.co/Clinical-Reasoning-Hub — organisation profile, which still states older benchmark gains
https://featherless.ai/models/Clinical-Reasoning-Hub/Diagnostic-Reasoning-Q3X1 — hosted inference page that restates the card

## Record

The card says the assembled corpus has 97,041 examples and "is not released." It says "MedQA and PubMedQA items are present in the corpus at their evaluation-set sizes," and that "training material was drawn from" the MedMCQA train split. It also says "The textbook-derived component was OCR-extracted without manual correction." The card does not name Hub dataset ids. The MedQA test size it cites, 1,273 items, matches GBaker/MedQA-USMLE-4-options. PubMedQA is qiaojin/PubMedQA. MedMCQA is openlifescienceai/medmcqa, whose train split has 182,822 rows. The card does not say the whole of any of those sets was used. All three Hub datasets load. The assembled corpus and the textbook component do not.

The card says "A QLoRA fine-tune" and the training table says "Method | QLoRA, r = 128, α = 256" and "Precision | bf16 compute, 4-bit base." The ablation table labels a reduced arm "Plain SFT" and this checkpoint "Full recipe (this model)." No other loss is named. Learning rate is 2×10⁻⁴. Effective batch is 32. Epochs are "3 main + 1 answer-format stabilisation." The repository has full float16 shards and no adapter file, and the card does not say whether the adapter was merged. config.json sets unsloth_version to 2026.2.1.

The card says the parent is "Qwen/Qwen3-8B (instruction-tuned, not Qwen3-8B-Base)," revision 6d4c89fea8bfdc5c208d0964535c56e043e64d00. The cited paper is "Manuscript under review" and has no public URL. A search found no arXiv paper and no GitHub repository that print this checkpoint's training recipe. The safetensors header counts 8,190,735,360 parameters. The card's trainable-parameter figure, 349,175,808, is the QLoRA update, not the released model.

The card says "It is a research artifact" and "must not be used for clinical decision-making." The use claim is Weak. The warning is an explicit prohibition. The audience is someone reproducing the paper. The stated jobs are medical and exam question answering and a clinical reasoning template. The evaluation writes chain-of-thought and then an option letter. The domain is medical, with no narrower specialty. MedXpertQA is evaluation only: "not among the named training sources." On the exact-stem-unflagged subset the card reports 20.8% for this model and 15.6% for the parent, a gain of 5.2 points. It says an earlier 76.4% average is superseded.

The evaluation is English multiple-choice text. A chat template is present and has no fixed medical system prompt. config.json sets max_position_embeddings to 40960. The license is cc-by-nc-4.0. The inventory's QLoRA, three exam sets, and parent match the card. The card also names textbook text and an unreleased 97,041-example corpus, so the match is partial.
