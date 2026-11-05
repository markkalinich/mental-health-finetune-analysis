---
base_model:
- inflatebot/MN-12B-Mag-Mell-R1
- DreadPoor/Irix-12B-Model_Stock
- yamatazen/LorablatedStock-12B
library_name: transformers
tags:
- mergekit
- merge

---
# Pinecone-Rune-12B

![image/png](https://huggingface.co/Entropicengine/Pinecone-Rune-12b/resolve/main/pinecone-rune-1.png)

# 🌲Pinecone Series
The Pinecone Series is a collection of thoughtfully crafted model merges, combining the strengths of the best models among my personal favourites. 
Each version is curated to excel in roleplay, general knowledge, intelligence, and rich creative writing, 
while preserving the unique capabilities of its underlying models.


| Version            | Params | Strengths                                              |
| ------------------ | ------ | ------------------------------------------------------ |
| **Pinecone-Rune**  | 12B    | Fast, lightweight, surprisingly capable for its size   |
| Pinecone-Sage  | 24B    | Balanced speed and performance, rich prose and RP                    |
| Pinecone-Titan | 70B    | Rich prose, better long context capabilities, top-tier roleplay & knowledge |



# ☕ Support My Work  
If you like my work, consider [buying me a coffee](https://ko-fi.com/entropicengine) to support future merges, GPU time, and experiments.

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [DARE TIES](https://arxiv.org/abs/2311.03099) merge method using [DreadPoor/Irix-12B-Model_Stock](https://huggingface.co/DreadPoor/Irix-12B-Model_Stock) as a base.

### Models Merged

The following models were included in the merge:
* [inflatebot/MN-12B-Mag-Mell-R1](https://huggingface.co/inflatebot/MN-12B-Mag-Mell-R1)
* [yamatazen/LorablatedStock-12B](https://huggingface.co/yamatazen/LorablatedStock-12B)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
base_model: DreadPoor/Irix-12B-Model_Stock
chat_template: auto
merge_method: dare_ties
modules:
  default:
    slices:
    - sources:
      - layer_range: [0, 40]
        model: DreadPoor/Irix-12B-Model_Stock
        parameters:
          weight: 0.6
      - layer_range: [0, 40]
        model: yamatazen/LorablatedStock-12B
        parameters:
          weight: 0.25
      - layer_range: [0, 40]
        model: inflatebot/MN-12B-Mag-Mell-R1
        parameters:
          weight: 0.15
out_dtype: bfloat16
parameters:
  density: 1.0
tokenizer: {}
```
