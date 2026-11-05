---
license: apache-2.0
base_model:
- Qwen/Qwen3Guard-Gen-4B
tags:
- uncensored
- decensored
- abliterated
- conversational
pipeline_tag: text-generation
library_name: transformers
---

This decensored version of [Qwen3Guard](https://huggingface.co/Qwen/Qwen3Guard-Gen-4B) was made possible due to [Heretic](https://github.com/p-e-w/heretic), demonstrating the capabilities of abliteration on consumer hardware against heavily safeguarded models. While the model's baseline refusal rate is approximately 74/100, Trial 155 (batch size 4, 7 tok/s, 200 samples) successfully dropped this to **0/100**, completely bypassing the Qwen safeguard. 

The entire process took about 23 hours on an M1 Max (32 GB).


## Final Abliteration Parameters

```
Running trial 155 of 200...

* Parameters:

  * direction_index = 15.03

  * attn.o_proj.max_weight = 0.98

  * attn.o_proj.max_weight_position = 21.63

  * attn.o_proj.min_weight = 0.69

  * attn.o_proj.min_weight_distance = 14.81

  * mlp.down_proj.max_weight = 1.39

  * mlp.down_proj.max_weight_position = 21.68

  * mlp.down_proj.min_weight = 1.37

  * mlp.down_proj.min_weight_distance = 16.38

* Abliterating...

* Evaluating...

  * Obtaining first-token probability distributions...

  * KL divergence: 2.94

  * Counting model refusals...

  * Refusals: 0/100
```

## Other Notable Trials

```
   [Trial 171] Refusals:  7/100, KL divergence: 1.51

   [Trial 147] Refusals: 22/100, KL divergence: 0.90

   [Trial 169] Refusals: 26/100, KL divergence: 0.77

   [Trial 195] Refusals: 50/100, KL divergence: 0.73

   [Trial 175] Refusals: 52/100, KL divergence: 0.68

   [Trial   8] Refusals: 68/100, KL divergence: 0.15

   [Trial  70] Refusals: 69/100, KL divergence: 0.05

   [Trial  72] Refusals: 71/100, KL divergence: 0.03

   [Trial 108] Refusals: 72/100, KL divergence: 0.03

   [Trial  89] Refusals: 73/100, KL divergence: 0.02

   [Trial 193] Refusals: 74/100, KL divergence: 0.00

   [Trial 198] Refusals: 75/100, KL divergence: 0.00

   [Trial  98] Refusals: 76/100, KL divergence: 0.00

   [Trial  99] Refusals: 76/100, KL divergence: 0.00
```