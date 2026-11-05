# GLM-5.2-9B-LoRA-Surgery-Dummy

Test-only checkpoint for GLM-5.2 post-training, LoRA, weight-sync, and
sharding integration. It is not a usable chat or benchmark model.

The donor is the official
[`zai-org/GLM-5.2`](https://huggingface.co/zai-org/GLM-5.2) checkpoint at
revision `cf457fa734ab149ffef225f80893eb38c6ff5cdc`.

The checkpoint preserves the donor width and MLA/DSA geometry while reducing
78 decoder layers to 10 and 256 routed experts to 16. It contains
8,763,269,120 parameters. Layer and expert provenance is recorded in
`surgery_manifest.json`; experts are selected independently per MoE layer by a
deterministic cosine-maximin traversal of the donor router rows.

The matching rollout-only checkpoint is
[`imvladikon/GLM-5.2-9B-LoRA-Surgery-Dummy-FP8`](https://huggingface.co/imvladikon/GLM-5.2-9B-LoRA-Surgery-Dummy-FP8)
at revision `5eedf18a056d10b37452528c930487cc48dbd63a`. It preserves the
official mixed E4M3/BF16 tensor contract, the same source layers, and the same
selected expert IDs. This BF16 checkpoint is the trainer side of surgery pair
`glm52-9b-2db222dcbd5d236a`.
