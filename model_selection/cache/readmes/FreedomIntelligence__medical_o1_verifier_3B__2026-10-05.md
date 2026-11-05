---
license: apache-2.0
language:
- en
- zh
base_model:
- meta-llama/Llama-3.2-3B-Instruct
pipeline_tag: text-classification
tags:
- medical
datasets:
- FreedomIntelligence/medical-o1-verifiable-problem
---
# <span>Introduction</span>

This is a **medical verifier** designed to evaluate the correctness of LLM outputs on [medical verifiable problems](https://huggingface.co/datasets/FreedomIntelligence/medical-o1-verifiable-problem). Such verification can be utilized to enhance the medical reasoning capabilities of LLMs.

For details, please refer to our [paper](https://arxiv.org/pdf/2412.18925) and [GitHub repository](https://github.com/FreedomIntelligence/HuatuoGPT-o1).
Additionally, you can explore [HuatuoGPT-o1](https://huggingface.co/FreedomIntelligence/HuatuoGPT-o1-8B), our advanced medical LLM specializing in complex medical reasoning.  


# <span>Usage</span>
Follow the code below to utilize this model:
```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch.nn.functional as F

# Load tokenizer and model
model_path = 'FreedomIntelligence/medical_o1_verifier_3B'
tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(
    model_path, torch_dtype="auto", device_map="auto", attn_implementation="flash_attention_2", num_labels=2
)

# Evaluation template
template = """<Model Response>
{}
</Model Response>

<Reference Answer>
{}
</Reference Answer>

Your task is to evaluate the model response by comparing it to the reference answer. If the model response is correct and aligns with the reference answer, output "True" . If it is incorrect or fails to select the correct option (if options are provided), output "False" . {}"""

# Tokenize input and evaluate
LLM_response = 'The answer is 25 percentage'
ground_truth_answer = '25%'
input_batch = tokenizer([template.format(LLM_response,ground_truth_answer,tokenizer.eos_token)], return_tensors="pt").to(model.device)
logits = model(**input_batch,return_dict=True).logits
probabilities = F.softmax(logits, dim=-1)
result = "True" if probabilities[0, 1] > 0.5 else "False"

print(f"Evaluation Result: {result}")
```


# <span>📖 Citation</span>
```
@misc{chen2024huatuogpto1medicalcomplexreasoning,
      title={HuatuoGPT-o1, Towards Medical Complex Reasoning with LLMs}, 
      author={Junying Chen and Zhenyang Cai and Ke Ji and Xidong Wang and Wanlong Liu and Rongsheng Wang and Jianye Hou and Benyou Wang},
      year={2024},
      eprint={2412.18925},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2412.18925}, 
}
```
