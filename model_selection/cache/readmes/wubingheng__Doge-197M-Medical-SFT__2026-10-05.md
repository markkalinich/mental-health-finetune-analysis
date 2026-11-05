---
license: apache-2.0
license_name: doge
license_link: LICENSE
datasets:
- michaelwzhu/ChatMed_Consult_Dataset
base_model:
- JingzeShi/Doge-197M
pipeline_tag: question-answering
library_name: transformers
language:
- en
- zh
tags:
- medical
---

## **Doge-197M for MedicalQA**

This model is a fine-tuned version of [JingzeShi/Doge-197M](https://huggingface.co/JingzeShi/Doge-197M).
It has been trained using [TRL](https://github.com/huggingface/trl).

Doge is an ongoing research project where we aim to train a series of small language models to further explore whether the Transformer framework allows for more complex feedforward network structures, enabling the model to have fewer cache states and larger knowledge capacity.

In addition, Doge uses Dynamic Mask Attention as sequence transformation and can use Multi-Layer Perceptron or Cross Domain Mixture of Experts as state transformation. Dynamic Mask Attention allows the Transformer to use self-attention during training and state space during inference, and Cross Domain Mixture of Experts can directly inherit the weights of Multi-Layer Perceptron for further training. This model is trained by Jingze Shi, it only allows text input and text generation, for detailed algorithm and model architecture, please refer to [Wonderful Matrices](https://arxiv.org/abs/2412.11834), the ongoing research repository is [Wonderful Matrices](https://github.com/LoserCheems/WonderfulMatrices).


## Uses

```python
>>> from transformers import AutoTokenizer, AutoModelForCausalLM, GenerationConfig, TextStreamer

>>> tokenizer = AutoTokenizer.from_pretrained("wubingheng/Doge-197M-Medical-SFT")
>>> model = AutoModelForCausalLM.from_pretrained("wubingheng/Doge-197M-Medical-SFT", trust_remote_code=True)

>>> generation_config = GenerationConfig(
...     max_new_tokens=256,
...     min_new_tokens=1,
...     num_beams=1,
...     eos_token_id=[tokenizer.eos_token_id],
...     stop_strings=[tokenizer.eos_token],
...     early_stopping=False,
...     use_cache=True,
...     do_sample=True,
...     temperature=0.8,
...     repetition_penalty=1.0,
... )
>>> steamer = TextStreamer(tokenizer=tokenizer, skip_prompt=True)

>>> system_prompt = """
... 你是医疗助手Doge, 按照用户的问题回复帮助性的答案.
... 
... 以下是你可以参考的文档:
... 
... 昨天发烧38度多今天又35度5是怎么回事啊是不是低烧啊还要继续喝退烧药吗
... 
... 您好，如果您昨天的体温确实达到了38度多，那么这个体温是算作发烧的。今天的体温虽然比昨天低，但是也属于正常体温范围内。这种情况可能是由于身体抵抗力增强，病情好转所致。如果您没有其他不适症状，建议您可以暂停使用退烧药，注意休息，多喝水，适当增加营养，保持良好的作息习惯。如果您出现其他不适症状或体温再次升高，建议您及时就医
... """.strip()

>>> prompt = "我现在发烧了该怎么办？"
>>> conversation = [
...     {"role": "system", "content": system_prompt},
...     {"role": "user", "content": prompt},
... ]
>>> inputs = tokenizer.apply_chat_template(
...     conversation=conversation,
...     tokenize=True,
...     return_tensors="pt",
... )
>>> print(prompt)

>>> output = model.generate(
...     inputs, 
...     tokenizer=tokenizer,
...     generation_config=generation_config, 
...     streamer=steamer
... )
```

**Fine-tune Task**:
- We selected an open-source Chinese medical question answering dataset for fine-tuning.


**Fine-tune Environment**:
- Image: nvcr.io/nvidia/pytorch:24.10-py3
- Hardware: 1x NVIDIA RTX 3090
- Software: Transformers


**Eval img**:

![image/png](https://cdn-uploads.huggingface.co/production/uploads/66a0a9e7e81290f90f93b0a6/l1fJUIqE227ULJJ1wbwRy.png)

## Citation

```bibtex
@misc{shi2024wonderfulmatrices,
      title={Wonderful Matrices: Combining for a More Efficient and Effective Foundation Model Architecture}, 
      author={Jingze Shi and Bingheng Wu},
      year={2024},
      eprint={2412.11834},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2412.11834}, 
}
```