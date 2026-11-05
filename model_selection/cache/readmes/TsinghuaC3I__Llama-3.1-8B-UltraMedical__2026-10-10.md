---
license: llama3
datasets:
- TsinghuaC3I/UltraMedical
- TsinghuaC3I/UltraMedical-Preference
language:
- en
base_model: meta-llama/Meta-Llama-3.1-8B-Instruct
---
<div align="center">
<h1>
  UltraMedical: Building Specialized Generalists in Biomedicine.
</h1>
</div>

<p align="center">
  <a href="https://huggingface.co/datasets/TsinghuaC3I/UltraMedical">SFT Dataset</a> •
  <a href="https://huggingface.co/datasets/TsinghuaC3I/UltraMedical-Preference">Pref Dataset</a> •
  <a href="https://huggingface.co/collections/TsinghuaC3I/ultramedical-66d4076bad293ffc4bc41327">Collection</a> •
  <a href="https://github.com/TsinghuaC3I/UltraMedical">GitHub Code</a> •
  <a href="https://arxiv.org/abs/2406.03949">Paper</a>
</p>

Llama-3.1-8B-UltraMedical is an open-access large language model (LLM) specialized in biomedicine. Developed by the Tsinghua C3I Lab, this model aims to enhance medical examination access, literature comprehension, and clinical knowledge.

Building on the foundation of Meta's Llama-3.1-8B, Llama-3.1-8B-UltraMedical is trained on our [UltraMedical](https://github.com/TsinghuaC3I/UltraMedical) collection with supervised fine-tuning (SFT), iterative preference learning (like DPO and KTO). The UltraMedical collection is a large-scale, high-quality dataset of biomedical instructions, comprising 410,000 synthetic and manually curated samples, along with more than 100,000 preference data.


### Evaluations

| Model | MultiMedQA | MMLU | GPQA | Alpaca Eval 2 (LC/WR) |
| ----- | ---------- | ---- | ---- | ------------- |
| Llama-3.1-8B-Instruct | 71.38 | 73.00  | 30.40  | 20.90/21.80 |
| Llama-3.1-8B-UltraMedical | 76.82 | 72.96 | 34.82 |  41.22/48.20  |

### Inference with vLLM

```python
from transformers import AutoTokenizer
from vllm import LLM, SamplingParams

llm = LLM(model="TsinghuaC3I/Llama-3.1-8B-UltraMedical", trust_remote_code=True)
tokenizer = AutoTokenizer.from_pretrained("TsinghuaC3I/Llama-3.1-8B-UltraMedical")
sampling_params = SamplingParams(temperature=0.7, top_p=0.9, max_tokens=1024, stop=["<|eot_id|>"])

messages = [
    {"role": "user", "content": """The question format used in the above input examples。"""},
]
prompts = tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)
print(prompts[0])
"""
<|begin_of_text|><|start_header_id|>user<|end_header_id|>

{question}<|eot_id|><|start_header_id|>assistant<|end_header_id|>

"""

outputs = llm.generate(prompts=prompts, sampling_params=sampling_params)
print(outputs[0].outputs[0].text)
```


### Citation

```
@misc{zhang2024ultramedical,
      title={UltraMedical: Building Specialized Generalists in Biomedicine}, 
      author={Kaiyan Zhang and Sihang Zeng and Ermo Hua and Ning Ding and Zhang-Ren Chen and Zhiyuan Ma and Haoxin Li and Ganqu Cui and Biqing Qi and Xuekai Zhu and Xingtai Lv and Hu Jinfang and Zhiyuan Liu and Bowen Zhou},
      year={2024},
      eprint={2406.03949},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```