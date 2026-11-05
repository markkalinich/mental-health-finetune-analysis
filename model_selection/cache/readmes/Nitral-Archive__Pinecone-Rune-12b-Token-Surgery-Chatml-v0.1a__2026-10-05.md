---
base_model:
- Entropicengine/Pinecone-Rune-12b
---
# Original base model [Entropicengine/Pinecone-Rune-12b](https://huggingface.co/Entropicengine/Pinecone-Rune-12b)
# Modified base model used for this train: [Nitral-AI/Pinecone-Rune-12b-chatmlified](https://huggingface.co/Nitral-AI/Pinecone-Rune-12b-Token-Surgery-Chatml)
## Only around 750 entries in rank/alpha 32 4bit-qlora at 3e-6 for 2 epochs. bs 4 grad accum 4, for ebs 16 with cosine.
### Dataset here: https://huggingface.co/datasets/Nitral-AI/antirep_sharegpt
### Example Notebook using l4/t4: https://huggingface.co/Nitral-AI/Pinecone-Rune-12b-Token-Surgery-Chatml/tree/main/TokenSurgeon-Example
#### Boring Training graph. 
##### Starting loss: 1.74 Final loss 0.95
![image/png](https://cdn-uploads.huggingface.co/production/uploads/642265bc01c62c1e4102dc36/Lf84E9U7g8zvu-moK8_Ca.png)

