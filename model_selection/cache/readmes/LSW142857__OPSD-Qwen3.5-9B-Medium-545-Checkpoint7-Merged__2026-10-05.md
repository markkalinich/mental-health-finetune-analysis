---
library_name: transformers
tags:
- opsd
- qwen3.5
- merged
- code
- lora
language:
- en
pipeline_tag: text-generation
base_model: jiaxingx/privilege-code-opsd-ckpts
---
# Qwen3.5-9B OPSD Medium, checkpoint 7 (8 updates)

Full merged model used by the ongoing 100-task SWE-Gym validation run. This artifact includes all four model weight shards, tokenizer/chat template, processor configuration, merged LoRA updates, and the complete trained MTP module. No separate adapter is required. Optimizer state and the training data cursor are not part of this inference artifact.

Initialization: expert-SFT `qwen35-9b-expert-sft-131k-lora64-block28-2996448/checkpoint-best` from [jiaxingx/privilege-code-opsd-ckpts](https://huggingface.co/jiaxingx/privilege-code-opsd-ckpts), pinned revision `3fbab6c3ed8ad472c7b99bdf5e571ff90de0c0fc`. Then trained with OPSD on 545 student-error tasks, Medium stage-adaptive PI in the frozen teacher's trailing user view. The student does not see PI. This is the Taurus Medium experiment, independent of the Weak experiment on Aries.

Training: LoRA rank 64, alpha 128; batch size 32; learning rate 2e-6; temperature 0.6; teacher top-K 64; context 131072; per-request output cap 4096; maximum turns 150. Checkpoint index 7 means 8 completed optimizer updates. Complete MTP parameters are included; see the checksummed merge manifest.

Current evaluation: context limit 262144, output cap 4096, maximum turns 250, temperature 0.6, top-p 0.95, top-k 20, min-p 0, seed 42, thinking enabled. The evaluation is unprivileged (no PI), using eight TP1 SGLang replicas on Aries. MTP speculation is disabled in this evaluation. SGLang uses its explicit longer-context override, and the client reserves 16 context tokens. These are runtime evaluation settings, not a claim that the model configuration's native context length was changed.

The validation set is a 100-task SWE-Gym subset, not SWE-bench Verified. Evaluation is ongoing; no final pass rate is claimed. Infrastructure failures require separate control-based auditing and must not be interpreted as incorrect model answers.

`SHA256SUMS.json` records the exact uploaded runtime file sizes and hashes. `merge_manifest.json` records the checkpoint lineage and tensor merge verification. Training logs, private task transcripts, datasets, credentials, and optimizer checkpoints are excluded. The repository is public, as explicitly authorized by its owner.
