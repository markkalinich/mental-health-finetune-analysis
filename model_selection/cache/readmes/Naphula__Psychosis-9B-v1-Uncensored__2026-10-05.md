---
license: gemma
base_model:
- DavidAU/Gemma-The-Writer-9B
- sam-paech/Darkest-muse-v1
- sam-paech/Delirium-v1
language:
- en
library_name: transformers
tags:
- creative
- creative writing
- fiction writing
- plot generation
- sub-plot generation
- fiction writing
- story generation
- scene continue
- storytelling
- fiction story
- science fiction
- romance
- all genres
- story
- writing
- vivid prosing
- vivid writing
- fiction
- roleplaying
- float32
- swearing
- gemma2
- rp
- horror
- gemma
- karcher
- merge
- mergekit
widget:
  - text: "Psychosis-9B-v1-Uncensored"
    output:
      url: https://cdn-uploads.huggingface.co/production/uploads/68e840caa318194c44ec2a04/BDaWz9F6fG9cs6iJWoPcf.png
---

> [!CAUTION]
> <span style="color:red; font-weight:bold">⚠️ Warning:</span> This model can produce narratives and RP that contain violent and graphic erotic content. Adjust your system prompt accordingly. Also, use **Gemma 2** chat template.
>

> [!NOTE]
> <span style="color:red; font-weight:bold">Note:</span> There are two versions of Psychosis:
> - The regular version is censored and has refusals but might be smarter overall.
> - The uncensored version does not have refusals, but is partially broken and sometimes outputs chinese.
>

# 🧠 Psychosis 9B v1 Uncensored

This merge was made using the `karcher` method.

The result is creative, unhinged, and (optionally) uncensored. A truly psycho version of Gemma 2.

Released in `float32` precision for maximum quality. See the 14B upscale for other versions.

![psycho](https://cdn-uploads.huggingface.co/production/uploads/68e840caa318194c44ec2a04/BDaWz9F6fG9cs6iJWoPcf.png)

## Ablation Notes

The uncensored version was MPOA post-ablated using `scale: 1.5` and `measurement: 31` to all layers.

**Heretic gemma the writer and ablated components were tested but this resulted in more refusals than ablating after merging.**

These commands were MPOA formatted ablation (Norm Preserved, Bi-Projected) for maximum uncensored knowledge preservation.

Unfortunately, using a lower scale of `1.3` did not prevent refusals, but it did prevent chinese output bugs. The `1.5` scale ablation was chosen because it's more uncensored.

I am releasing **both versions** in case a better ablation method is found later on.

```
# python measure.py -m B:\9B\Psychosis-9B-v1 -o B:\9B\Psychosis-9B-v1\ablit_proj --batch-size 8 --projected
# python analyze_old.py B:\9B\Psychosis-9B-v1\ablit_proj -c
# sharded_ablate.py psychosis-9b-test2.yml --normpreserve --projected
```