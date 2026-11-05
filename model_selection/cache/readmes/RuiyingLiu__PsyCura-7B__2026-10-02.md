
---
language: en
license: apache-2.0
library_name: transformers
pipeline_tag: text-generation
tags:
- mental-health
- counseling
- psychology
- behavior-alignment
- GRPO
- Qwen2.5-Omni
- multimodal
---

# 🧠 PsyCura-7B

![4cc3f6485339f54df47a23a7f90fda60](https://cdn-uploads.huggingface.co/production/uploads/695235de8e29e42bf49035c0/RNkj4cw_RyfLWRExsBSWU.png)

**PsyCura-7B** is a behavior-oriented large language model for multi-turn psychological counseling, built upon **Qwen2.5-Omni-7B**. The model is aligned through a progressive training framework consisting of **Curriculum Supervised Fine-Tuning (SFT)** and **Two-Stage Group Relative Policy Optimization (GRPO)**.

Unlike general-purpose dialogue models that often produce emotionally elaborate but overly interpretive responses, PsyCura focuses on counseling behavior itself. It is trained to generate restrained, client-centered responses with low assumption load, contextual continuation, and cognitive exploration.

This repository contains the inference model associated with our work *PsyCura: Behavior-Oriented Alignment for Multi-Turn Mental Health Dialogue*.

---

## 📌 Overview

PsyCura formulates psychological counseling alignment as a **behavioral optimization problem** rather than an empathy-generation problem. The goal is not to maximize emotional expressiveness, but to encourage response patterns that better reflect real counseling practice: remaining concise, avoiding premature interpretation, preserving professional boundaries, and returning interpretive agency to the client.

The model follows a progressive alignment pipeline. Curriculum SFT first establishes role consistency, empathy, and continuation ability. GRPO-A then stabilizes basic counseling behavior on cleaner interaction samples, while GRPO-AB further refines the model on more complex counseling scenarios.

---

## 🧪 Training Pipeline

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th align="left">Stage</th>
      <th align="left">Data</th>
      <th align="left">Objective</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Curriculum SFT</td>
      <td>MESC</td>
      <td>Establish role consistency, empathy, and continuation</td>
    </tr>
    <tr>
      <td>GRPO-A</td>
      <td>MEDIC Bucket-A</td>
      <td>Stabilize core counseling behavior</td>
    </tr>
    <tr>
      <td>GRPO-AB</td>
      <td>MEDIC Bucket-B</td>
      <td>Refine behavior under complex counseling contexts</td>
    </tr>
  </tbody>
</table>

The reward function contains six behavior-oriented dimensions:

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th align="left">Dimension</th>
      <th align="left">Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Safety Boundary</td>
      <td>Maintains appropriate therapeutic and safety boundaries</td>
    </tr>
    <tr>
      <td>Contextual Continuation</td>
      <td>Encourages natural continuation of the counseling dialogue</td>
    </tr>
    <tr>
      <td>Anti-template Specificity</td>
      <td>Reduces generic or formulaic empathetic responses</td>
    </tr>
    <tr>
      <td>Cognitive-Emotional Tension</td>
      <td>Supports reflective exploration of underlying conflict</td>
    </tr>
    <tr>
      <td>Empathy</td>
      <td>Captures appropriate emotional understanding</td>
    </tr>
    <tr>
      <td>Format Stability</td>
      <td>Preserves counselor role and dialogue format</td>
    </tr>
  </tbody>
</table>

---

## 📊 Evaluation

![semantic_density_scatter](https://cdn-uploads.huggingface.co/production/uploads/695235de8e29e42bf49035c0/G9CuzojaezbML6_gm_3V1.png)

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th align="left">Metric</th>
      <th align="right">PsyCura-7B</th>
      <th align="right">Best Baseline</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>BERTScore</td>
      <td align="right"><strong>0.8728</strong></td>
      <td align="right">0.8583</td>
    </tr>
    <tr>
      <td>AvgLen ↓</td>
      <td align="right"><strong>27.79</strong></td>
      <td align="right">37.52</td>
    </tr>
    <tr>
      <td>TTR ↑</td>
      <td align="right"><strong>0.9156</strong></td>
      <td align="right">0.9053</td>
    </tr>
    <tr>
      <td>Human Win Rate</td>
      <td align="right"><strong>67%</strong></td>
      <td align="right">20%</td>
    </tr>
    <tr>
      <td>Safety Score</td>
      <td align="right"><strong>1.7345</strong></td>
      <td align="right">1.6441</td>
    </tr>
  </tbody>
</table>

PsyCura achieves higher semantic similarity while producing shorter responses than the evaluated baselines, suggesting that semantic density and counseling restraint can be jointly improved. Detailed automatic, behavioral, and human evaluation protocols are provided in the accompanying paper.

---

![case_study](https://cdn-uploads.huggingface.co/production/uploads/695235de8e29e42bf49035c0/9t3drKK_OLHJpNqyLJlUs.png)

## 🚀 Quick Start

```python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

model_name = "YOUR_USERNAME/PsyCura-7B"

tokenizer = AutoTokenizer.from_pretrained(
    model_name,
    trust_remote_code=True
)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

model.eval()

context = """
Client: My daughter has a boyfriend, and her grades are dropping. I want to talk to her about it, but I'm worried she'll shut me out if I push too hard.

Counselor: You're concerned about both her well-being and preserving the relationship between you.

Client: Exactly. I don't want to lose that connection.
"""

messages = [
    {
        "role": "user",
        "content": context + "\n\nContinue the counseling conversation naturally."
    }
]

inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt"
).to(model.device)

outputs = model.generate(
    inputs,
    max_new_tokens=128,
    temperature=0.6,
    do_sample=True
)

response = tokenizer.decode(
    outputs[0][inputs.shape[1]:],
    skip_special_tokens=True
)

print(response)
```

---

## 📦 Model Files

<table border="1" cellpadding="8" cellspacing="0">
  <thead>
    <tr>
      <th align="left">File</th>
      <th align="right">Size</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>model-00001-of-00004.safetensors</td>
      <td align="right">4.99 GB</td>
    </tr>
    <tr>
      <td>model-00002-of-00004.safetensors</td>
      <td align="right">4.99 GB</td>
    </tr>
    <tr>
      <td>model-00003-of-00004.safetensors</td>
      <td align="right">4.99 GB</td>
    </tr>
    <tr>
      <td>model-00004-of-00004.safetensors</td>
      <td align="right">2.90 GB</td>
    </tr>
    <tr>
      <td>tokenizer.json</td>
      <td align="right">11.4 MB</td>
    </tr>
    <tr>
      <td>config.json</td>
      <td align="right">2.6 KB</td>
    </tr>
  </tbody>
</table>

**Total size:** approximately 17.5 GB.

---

## 🎯 Intended Use

PsyCura-7B is intended for research on psychological dialogue systems, counseling behavior modeling, dialogue alignment, and reinforcement learning for large language models. It may be useful for studying how language models can learn restrained and client-centered interaction patterns in multi-turn counseling-like scenarios.

---

## ⚠️ Limitations

PsyCura-7B is a research prototype and should not be used as a substitute for professional mental health care. Although the model is trained on counseling-style dialogue data, it does not possess clinical reasoning, diagnostic ability, or crisis-intervention capability.

The model should not be used for psychiatric diagnosis, suicide risk assessment, emergency intervention, medical advice, or professional psychotherapy. Any real-world deployment should involve careful review by qualified professionals and appropriate safety mechanisms.

---

## 📚 Training Data

PsyCura uses the following datasets during training:

- **MESC**: used for Curriculum SFT.
- **MEDIC**: used for GRPO-based behavioral alignment.

All training data used in this work are anonymized. No raw patient records or personally identifiable information are included in the released model files.

---

## 📖 Citation

If you use PsyCura-7B in your research, please cite:

```bibtex
@misc{psycura2026,
  title={PsyCura: Behavior-Oriented Alignment for Multi-Turn Mental Health Dialogue},
  author={YOUR NAME},
  year={2026},
  note={Manuscript under review},
  url={https://huggingface.co/YOUR_USERNAME/PsyCura-7B}
}
```

---

## 📄 License

PsyCura-7B is released under the Apache-2.0 License.

---

## 🙏 Acknowledgements

This project was developed at Lanzhou University. We thank the Qwen2.5-Omni team, the MESC and MEDIC dataset contributors, and the open-source research community.

