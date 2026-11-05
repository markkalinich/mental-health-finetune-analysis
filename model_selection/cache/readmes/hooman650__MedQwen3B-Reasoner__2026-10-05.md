---
base_model: unsloth/qwen2.5-3b-instruct-unsloth-bnb-4bit
tags:
- text-generation-inference
- reinforcement-learning
- transformers
- unsloth
- qwen2
- trl
- grpo
license: apache-2.0
language:
- en
datasets:
- qiaojin/PubMedQA
- openai/gsm8k
- yesilhealth/Health_Benchmarks
pipeline_tag: text-generation
---

# MedQwen3B-Reasoner: Medical Domain Reasoning with Mathematics-Enhanced Training

MedQwen3B-Reasoner is a specialized variant of Qwen2.5-3B-Instruct, fine-tuned using `GRPO` to excel at medical domain reasoning while maintaining strong mathematical problem-solving capabilities. The model demonstrates enhanced reasoning abilities and can express uncertainty when appropriate.

![MedQwen3B Training Process](process.png)

## Important

If you use `ollama`, `llama-cpp`, `vllm` or any other inference iengine, you need to set the system prompt as below as the model performs best with the following prompt:

```
'\nRespond in the following format:\n<reasoning>\n...\n</reasoning>\n<answer>\n...\n</answer>\n'
```

## Want to train your own?

Read my article [here](https://medium.com/@hooman_66365/build-your-own-medical-mini-deepseek-r1-with-reinforcement-learning-508509cd7d83) or follow the [notebook](https://github.com/hooman650/MedQwenReasoner).

## Key Features

- Medical domain expertise combined with mathematical reasoning capabilities
- Ability to express uncertainty with "maybe" responses
- Structured reasoning outputs with clear step-by-step explanations
- Compact size (3B parameters) while maintaining strong performance
- Trained using GRPO (Group Relative Policy Optimization) for 483 steps

## Training Data

The model was trained using a carefully curated mix of datasets:
- 70% Medical domain: [PubMedQA](https://huggingface.co/datasets/qiaojin/PubMedQA)
- 30% Mixed reasoning:
  - [GSM8K](https://huggingface.co/datasets/openai/gsm8k) (Mathematical reasoning)
  - [Health Benchmarks](https://huggingface.co/datasets/yesilhealth/Health_Benchmarks)

## Examples

Here are some examples of the model's reasoning capabilities across different domains:

### Mathematical Reasoning
```
Q: Agatha has some money to spend on a new bike. She spends $15 on the frame, and $25 on the front wheel. If she has $20 left to spend on a seat and handlebar tape, how much money, in dollars, did she have at first? 
Ground Truth Answer:
60 
MedQwen3B Answer (with reasoning it came up with)
<reasoning>
To determine how much money Agatha initially had, we need to add up the amount she spent on the frame, the front wheel, and the remaining money she has left to spend on a seat and handlebar tape.

The total amount spent on the frame and the front wheel is:
$15 + $25 = $40

The remaining money she has left is $20.

Therefore, the initial amount of money Agatha had is the sum of the money she has spent and the money she has left:
$40 + $20 = $60

</reasoning>
<answer>
Agatha initially had $60.
</answer>
```

### Medical Research Analysis
```
Given the scientific context below:
"""
Urinary bladder cancer patients who have undergone transurethral resection of bladder tumor (TURBT) are at risk of recurrence. This study aims to correlate the level of bone morphogenetic protein (BMP) expression with urothelial carcinoma invasiveness, TNM stage and time to recurrence after TURBT.
In 33 specimens of healthy transitional epithelium and 42 of urothelial carcinoma, BMP2, BMP4 and BMP7 expression was determined by real-time polymerase chain reaction. Patients who underwent TURBT were followed up for 1 year.
BMP2 and BMP7 were downregulated in infiltrating urothelial carcinoma, the relative expression being 0.76 (p = 0.04) and 0.28 (p = 0.025) respectively, while BMP4 was downregulated in non-invasive tumors. High expression of BMP2 and BMP7 correlated with prolonged time to recurrence (log-rank: p = 0.01 and p = 0.03 respectively).
"""
Answer the following question:
Does expression of bone morphogenetic protein-2 and -7 in urinary bladder cancer predict time to tumor recurrence? with 'yes', 'no' or 'maybe'. You need to carefully review the context and reason before answering. 
Ground Truth Answer:
yes 
MedQwen3b Answer:
<reasoning>
The study indicates that high expression of BMP2 and BMP7 correlated with prolonged time to recurrence (log-rank: p = 0.01 and p = 0.03 respectively). This means that the gene expression levels of BMP2 and BMP7 were significantly associated with the time to recurrence, with higher expression leading to a longer time to recurrence. Therefore, based on the statistical significance (p-values < 0.05) it is reasonable to conclude that the expression of bone morphogenetic protein-2 and -7 in urinary bladder cancer patients predicts time to tumor recurrence.
</reasoning>
<answer>
yes
</answer>
```

### Clinical Decision Making
```
Answer the following question:
What is a recommended strategy for pediatricians to encourage vaccination among hesitant parents? A:Allowing delays for certain vaccines while ensuring the most important ones are administered on schedule.   B:Providing evidence of immunization benefits in a judgmental manner.   C:Advocating for alternative immunization schedules to accommodate parental concerns. D:Discharging patients from their practice if vaccinations are refused.  
With 'A', 'B', 'C' or 'D'. You need to carefully review the context and reason before answering. 
Ground Truth Answer:
A 
MedQwen3B Answer:
<reasoning>
The strategy recommended by pediatricians to encourage vaccination among hesitant parents should not lead to the abandonment or dismissal of families as it can undermine the critical role of pediatricians in protecting children's health. Option D can harm the trust between the pediatrician and the parent, potentially alienating them. Options B and C might create confusion or threaten parents' trust in the recommended vaccination schedule. Option A, on the other hand, provides an evidence-based compromise that allows some flexibility while ensuring coverage for essential vaccines, which can be respected by hesitant parents as it balances their concerns with public health needs. 

This approach respects the autonomy of parents while providing relevant information and reassurance, which can help in addressing their hesitations, making Option A the most suitable strategy.
</reasoning>
<answer>
A
</answer>
```

## Usage

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "hooman650/MedQwen3B-Reasoner"

# Initialize model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Prepare prompt
prompt = "What is the relationship between BMI and cardiovascular disease risk?"
messages = [
    {"role": "system", "content": "\nRespond in the following format:\n<reasoning>\n...\n</reasoning>\n<answer>\n...\n</answer>\n"},
    {"role": "user", "content": prompt}
]
text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

# Generate response
model_inputs = tokenizer([text], return_tensors="pt").to(model.device)
generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512
)
generated_ids = [
    output_ids[len(input_ids):] for input_ids, output_ids in zip(model_inputs.input_ids, generated_ids)
]
response = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
```

## Model Details

- Base Model: [unsloth/qwen2.5-3b-instruct-unsloth-bnb-4bit](https://huggingface.co/unsloth/qwen2.5-3b-instruct-unsloth-bnb-4bit)
- Training Steps: 483
- Library: Unsloth
- License: Apache 2.0

## Citation

If you use this model in your research, please cite:

```bibtex
@misc {hooman_sedghamiz_2025,
	author       = { {Hooman Sedghamiz} },
	title        = { MedQwen3B-Reasoner (Revision 5dbc982) },
	year         = 2025,
	url          = { https://huggingface.co/hooman650/MedQwen3B-Reasoner },
	doi          = { 10.57967/hf/4415 },
	publisher    = { Hugging Face }
}
```

## License
This model is licensed under Apache 2.0.