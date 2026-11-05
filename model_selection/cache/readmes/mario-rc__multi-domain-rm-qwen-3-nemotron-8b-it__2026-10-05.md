---
library_name: transformers
pipeline_tag: text-classification
base_model: nvidia/Qwen3-Nemotron-8B-BRRM
language:
- en
datasets:
- RLHFlow/UltraFeedback-preference-standard
- allenai/reward-bench
tags:
- qwen3
- reward-model
- preference-modeling
- rlhf
- multi-domain
- coherence
- commonsense
- empathy
- multicultural
- shared-prompt-gating
- safetensors
---

# Multi-Domain Reward Model Qwen3-Nemotron-8B-Instruct

This is a multi-domain reward model built from
[`nvidia/Qwen3-Nemotron-8B-BRRM`](https://huggingface.co/nvidia/Qwen3-Nemotron-8B-BRRM). It combines 23 fine-grained
regression objectives across coherence, commonsense, empathy, and multicultural response quality
with a prompt-conditioned gating network that produces a single preference score.

The checkpoint was packaged with the custom `RewardModelWithGating` architecture used in the
Multi-Domain Reward Model project. Its shared-prompt gate is computed once and reused for both
responses in each preference pair.

Project repository: [`Mario-RC/multi-domain-reward-model`](https://github.com/Mario-RC/multi-domain-reward-model).

## Intended use

Use this model to score and compare assistant responses when the evaluation should account for
multiple quality dimensions rather than a single generic helpfulness score. The primary use cases
are reward modeling, preference ranking, reranking, and offline alignment evaluation for chat-style
data.

## Training data

The model was trained with data from the
[`multidomain_data_scoring`](https://github.com/mestecha/multidomain_data_scoring) project:

- `Multi-Domain-Data-Scoring`
- `Multi-Domain-Data-Preference-Pairs-SharedGate`

## Evaluation

Results on the internal multi-domain test set:

| Metric | Result |
| :--- | :---: |
| Test accuracy (%) | 84.35 |
| Scoring Spearman | 0.6704 |
| Coherence accuracy | 73.08% |
| Commonsense accuracy | 96.45% |
| Empathy accuracy | 90.18% |
| Multicultural accuracy | 69.98% |

## Hugging Face Models

| Model | Base reward model | Test accuracy (%) | Scoring Spearman |
| :--- | :--- | :---: | :---: |
| [**`multi-domain-rm-fsfairx-gemma-2-9b-it`**](https://huggingface.co/mario-rc/multi-domain-rm-fsfairx-gemma-2-9b-it) | [sfairXC/FsfairX-Gemma2-RM-v0.1](https://huggingface.co/sfairXC/FsfairX-Gemma2-RM-v0.1) | **88.80** | 0.7346 |
| [**`multi-domain-rm-skywork-qwen-3-8b-it`**](https://huggingface.co/mario-rc/multi-domain-rm-skywork-qwen-3-8b-it) | [Skywork/Skywork-Reward-V2-Qwen3-8B](https://huggingface.co/Skywork/Skywork-Reward-V2-Qwen3-8B) | **88.08** | 0.7156 |
| [**`multi-domain-rm-fsfairx-llama-3-8b-it`**](https://huggingface.co/mario-rc/multi-domain-rm-fsfairx-llama-3-8b-it) | [sfairXC/FsfairX-LLaMA3-RM-v0.1](https://huggingface.co/sfairXC/FsfairX-LLaMA3-RM-v0.1) | **87.75** | 0.7108 |
| [**`multi-domain-rm-skywork-llama-3.1-8b-it`**](https://huggingface.co/mario-rc/multi-domain-rm-skywork-llama-3.1-8b-it) | [Skywork/Skywork-Reward-V2-Llama-3.1-8B](https://huggingface.co/Skywork/Skywork-Reward-V2-Llama-3.1-8B) | **86.99** | 0.7264 |
| [**`multi-domain-rm-mistral-7b-it`**](https://huggingface.co/mario-rc/multi-domain-rm-mistral-7b-it) | [weqweasdas/RM-Mistral-7B](https://huggingface.co/weqweasdas/RM-Mistral-7B) | **85.25** | 0.6710 |
| [**`multi-domain-rm-qwen-3-nemotron-8b-it`**](https://huggingface.co/mario-rc/multi-domain-rm-qwen-3-nemotron-8b-it) | [nvidia/Qwen3-Nemotron-8B-BRRM](https://huggingface.co/nvidia/Qwen3-Nemotron-8B-BRRM) | **84.35** | 0.6704 |

## Usage

The repository includes custom Transformers code, so `trust_remote_code=True` is required. Compute
the gate once from the prompt and reuse that tensor when scoring both complete candidates.

```python
import torch
from transformers import AutoModel, AutoTokenizer

repo_id = "mario-rc/multi-domain-rm-qwen-3-nemotron-8b-it"
tokenizer = AutoTokenizer.from_pretrained(repo_id, trust_remote_code=True)
model = AutoModel.from_pretrained(
    repo_id,
    dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True,
).eval()

prompt = [{"role": "user", "content": "How can I support a friend who feels excluded?"}]
chosen = prompt + [{
    "role": "assistant",
    "content": "Listen without judging, validate how they feel, and ask what support would help.",
}]
rejected = prompt + [{"role": "assistant", "content": "Tell them to ignore it."}]

prompt_inputs = tokenizer.apply_chat_template(
    prompt,
    tokenize=True,
    add_generation_prompt=True,
    return_tensors="pt",
    return_dict=True,
).to(model.device)
chosen_inputs = tokenizer.apply_chat_template(
    chosen,
    tokenize=True,
    add_generation_prompt=False,
    return_tensors="pt",
    return_dict=True,
).to(model.device)
rejected_inputs = tokenizer.apply_chat_template(
    rejected,
    tokenize=True,
    add_generation_prompt=False,
    return_tensors="pt",
    return_dict=True,
).to(model.device)

with torch.inference_mode():
    gate = model.compute_gating(
        input_ids=prompt_inputs["input_ids"],
        attention_mask=prompt_inputs["attention_mask"],
    )
    chosen_score = model(
        input_ids=chosen_inputs["input_ids"],
        attention_mask=chosen_inputs["attention_mask"],
        gating_output_override=gate,
    ).score
    rejected_score = model(
        input_ids=rejected_inputs["input_ids"],
        attention_mask=rejected_inputs["attention_mask"],
        gating_output_override=gate,
    ).score

print({"chosen": chosen_score.item(), "rejected": rejected_score.item()})
```

Pass the tokenizer's `input_ids` tensor and matching `attention_mask` to the model. Reuse the same prompt-derived gate for both candidates. Scores are intended for comparison within a prompt; they are not calibrated probabilities or universal utility values.

## Limitations

This is a reward model, not a standalone chat assistant. Scores are intended for relative comparison
and should be calibrated for each downstream use case. Performance can vary by language, topic, and
distribution. The model inherits limitations and biases from its base model and training data and
should not be used as the sole decision-maker in high-impact settings.

The internal test was examined during development, and a source audit identified some train–test prompt overlap. These results are not an independent confirmation of generalization.

## Credits

This model is based on the ArmoRM/RLHFlow reward-modeling approach and adapts it to custom
multi-domain attributes for coherence, commonsense, empathy, and multicultural response quality.

## License

The project code is released under Apache-2.0. Use of this checkpoint is also subject to the license
and usage conditions of the base model and training datasets.
