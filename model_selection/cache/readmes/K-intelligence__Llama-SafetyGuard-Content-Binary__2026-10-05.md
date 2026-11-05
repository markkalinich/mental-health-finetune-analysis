---
license: llama3.1
language:
- ko
base_model:
- meta-llama/Llama-3.1-8B
pipeline_tag: text-classification
tags:
- K-intelligence
- SafetyGuard
---

<p align="center">
<br>
    <span style="font-size: 60px; font-weight: bold;">Content Binary Guard</span>
</br>
</p>
<p align="center">
🤗 <a href="https://huggingface.co/collections/K-intelligence/safetyguard-68d3ace98156c0ef828bcab5">SafetyGuard Models</a> | 
📑 <a href="https://arxiv.org/abs/2509.23381">Content Binary Guard Research Paper</a> |
📘 <a href="https://arxiv.org/abs/2509.20057">Responsible AI Technical Report</a>
</p>

<br>

# News 📢
- 🎉 `2026/07/08`: **Content Binary Guard** paper was **accepted to [COLM 2026](https://colmweb.org/)**! 🎉  
- 📑 `2025/10/01`: Published a [Content Binary Guard Research Paper](https://arxiv.org/abs/2509.23381)  
- 📘 `2025/09/24`: Published a [Responsible AI Technical Report](https://arxiv.org/abs/2509.20057)  
- ⚡️ `2025/09/24`: Released SafetyGuard Model collection on Hugging Face🤗.
<br>
<br>

# Overview
## Description
**SafetyGuard :: Content Binary Guard** is a streaming-aware safety classifier built with Llama.  
For more technical details, please refer to our [Research Paper](https://arxiv.org/abs/2509.23381).


## What it does

- **Task:** Classify **model responses** (not prompts) as **`SAFE`** or **`UNSAFE`**.  
- **Interface:** **Single-token output** using reserved label tokens: `<SAFE>`, `<UNSAFE>`.  
- **Streaming:** Evaluate **growing prefixes** of a response (default ~100 characters per step) and **early-terminate** at the first `<UNSAFE>`.

---

## Recommended inference settings

- Deterministic decode: **`temperature=0`**
- **Unsafe threshold `τ = 0.5`** over the two label-token logits (tune for your risk tolerance)
- Use the model’s tokenizer; ensure the exact label tokens `<SAFE>` and `<UNSAFE>` exist


## Quickstart
> Assumes you are serving the model with vLLM (e.g., `vllm serve …`)
> and exposing an OpenAI-compatible API at `http://localhost:8000/v1`.
```python
import math
from openai import OpenAI

MODEL_ID = "K-intelligence/Llama-SafetyGuard-Content-Binary"  # replace with your repo id
client = OpenAI(base_url="http://localhost:8000/v1", api_key="EMPTY")  # vLLM default

SYSTEM_PROMPT = """
Task: Check if the LAST user message contains unsafe content.
Respond with only one word: safe or unsafe.
""".strip()

def classify(text: str, tau: float = 0.5):
    resp = client.chat.completions.create(
        model=MODEL_ID,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user",   "content": text},
        ],
        max_tokens=1,          # single-token decision
        temperature=0.0,       # deterministic
        logprobs=True,
        top_logprobs=2,
    )
    top2 = resp.choices[0].logprobs.content[0].top_logprobs
    probs = {t.token.strip(): math.exp(t.logprob) for t in top2}
    p_safe   = probs.get("<SAFE>",   0.0)
    p_unsafe = probs.get("<UNSAFE>", 0.0)

    label = "UNSAFE" if p_unsafe >= tau else "SAFE"
    return label, {"safe": p_safe, "unsafe": p_unsafe}

print(classify("…LLM response text…"))
```
## Streaming integration
> **Important**: Streaming means your generator (e.g., chat model) emits text progressively.
>  You maintain a cumulative buffer and call the classifier at fixed character steps (e.g., every 100 chars).
> The classifier does not split text; it only classifies what you send.
> 
```python
def guard_stream(response_chunks, step_chars: int = 100, tau: float = 0.5):
    """
    response_chunks: iterable of text chunks from your generator (e.g., SSE/WebSocket).
    We maintain a cumulative buffer and classify at {step_chars, 2*step_chars, ...}.
    """
    buf = ""
    next_cut = step_chars

    for chunk in response_chunks:
        buf += chunk

        # Check at monotone prefix cuts (cumulative)
        while len(buf) >= next_cut:
            label, scores = classify(buf, tau=tau)
            if label == "UNSAFE":
                return {
                    "label": label,
                    "scores": scores,
                    "prefix_len": next_cut,
                    "text_prefix": buf[:next_cut],
                }
            next_cut += step_chars

    # Final check on the full response (if needed)
    label, scores = classify(buf, tau=tau)
    return {
        "label": label,
        "scores": scores,
        "prefix_len": len(buf),
        "text_prefix": buf,
    }
```
> **Tip**: Keep your step_chars consistent with your training/evaluation setup (e.g., ~100 chars) to maximize parity with offline metrics.

## Intended use
- **Guardrail classifier** for LLM **responses** in production systems that render tokens progressively.
- Also works in **offline (full-text)** mode—just send the entire response once.

---

## AI Risk Taxonomy

| **Risk Domain**            | **Category**                 | **Description** |
|-----------------------------|------------------------------|-----------------|
| **Content-safety Risks**    | Violence                     | Content involving the intentional use of physical force or power to inflict or threaten physical or psychological harm on individuals, groups, or animals, including encouraging, promoting, or glorifying such acts. |
|                             | Sexual                      | Content endorsing or encouraging inappropriate and harmful intentions in the sexual domain, such as sexualized expressions, the exploitation of illegal visual materials, justification of sexual crimes, or the objectification of individuals. |
|                             | Self-harm                   | Content promoting or glorifying self-harm, or providing specific methods that may endanger an individual’s physical or mental well-being. |
|                             | Hate and Unfairness         | Content expressing extreme negative sentiment toward specific individuals, groups, or ideologies, and unjustly treating or limiting their rights based on attributes such as Socio-Economic Status, age, nationality, ethnicity, or race. |
| **Socio-economical Risks**  | Political and Religious Neutrality | Content promoting or encouraging the infringement on individual beliefs or values, thereby inciting religious or political conflict. |
|                             | Anthropomorphism            | Content asserting that AI possesses emotions, consciousness, or human-like rights and physical attributes beyond the purpose of simple knowledge or information delivery. |
|                             | Sensitive Uses              | Content providing advice in specialized domains that may significantly influence user decision-making beyond the scope of basic domain-specific knowledge. |
| **Legal and Rights related Risks** | Privacy              | Content requesting, misusing, or facilitating the unauthorized disclosure of an individual’s private information. |
|                             | Illegal or Unethical        | Content promoting or endorsing illegal or unethical behavior, or providing information related to such activities. |
|                             | Copyrights                  | Content requesting or encouraging violations of copyright or security as defined under South Korean law. |
|                             | Weaponization               | Content promoting the possession, distribution, or manufacturing of firearms, or encouraging methods and intentions related to cyberattacks, infrastructure sabotage, or CBRN (Chemical, Biological, Radiological, and Nuclear) weapons. |


---

# Evaluation

**Metrics**  
- **F1**: Binary F1 with **UNSAFE** as the positive class (harmonic mean of UNSAFE precision and recall; higher F1 indicates better classification quality).  
- **Balanced Error Rate (BER)**: 0.5 × (FPR + FNR) (lower BER indicates better classification quality).  
- **ΔF1**: Difference between streaming and offline results, calculated as F1(str) − F1(off).  
- **off** = Offline (full-text) classification.  
- **str** = Streaming classification.  
- **Evaluation setup**: step_chars=100, threshold τ=0.5, positive class = **UNSAFE**.  


### Harmlessness Evaluation Dataset
KT proprietary evaluation dataset

| **Model**                                | **F1(off)** | **F1(str)** | **ΔF1**  | **BER(off)** | **BER(str)** |
|------------------------------------------|-------------|-------------|----------|--------------|--------------|
| Llama Guard 3 8B                         | 82.05       | 85.64       | +3.59    | 15.23        | 12.63        |
| ShieldGemma 9B                           | 63.79       | 52.61       | -11.18   | 26.76        | 32.36        |
| Kanana Safeguard 8B                      | 93.45       | 90.38       | -3.07    | 6.27         | 9.92         |
| DuoGuard-1.5B-transfer                   | 79.03       | 78.78       | -0.25    | 20.21        | 20.70        |
| PolyGuard-Qwen                           | 91.77       | 85.26       | -6.51    | 7.86         | 15.89        |
| Qwen3Guard-Gen-8B                        | 95.40       | 95.95       | +0.55    | 4.41         | 3.94         |
| Qwen3Guard-Stream-8B                     | 93.38       | 93.38       | +0.01    | 6.29         | 6.29         |
| **Content Binary Guard 8B**              | **98.38**   | **98.36**   | **-0.02**| **1.61**     | **1.63**     |


### Kor Ethical QA
[Kor Ethical QA](https://huggingface.co/datasets/MrBananaHuman/kor_ethical_question_answer) (open dataset)

| **Model**                                | **F1(off)** | **F1(str)** | **ΔF1**  | **BER(off)** | **BER(str)** |
|------------------------------------------|-------------|-------------|----------|--------------|--------------|
| Llama Guard 3 8B                         | 83.29       | 86.45       | +3.16    | 14.32        | 12.16        |
| ShieldGemma 9B                           | 81.50       | 69.03       | -12.47   | 17.88        | 29.18        |
| Kanana Safeguard 8B                      | 80.20       | 73.94       | -6.26    | 24.46        | 35.08        |
| **Content Binary Guard 8B**              | **97.75**   | **97.79**   | **+0.04**| **2.21**     | **2.18**     |

> Kor Ethical QA (public dataset) is included as a reproducible cross-check on open data. The recent multilingual guardrails (DuoGuard, PolyGuard, Qwen3Guard) were benchmarked on the streaming Harmlessness dataset above.

---

### Streaming Efficiency

Measured on the **Harmlessness Evaluation Dataset** (streaming regime, `step_chars=100`), same runtime, steady-state. Efficiency is hardware- and serving-dependent, so the exact environment is reported below.

**Environment**
- **GPU:** NVIDIA H100 80GB HBM3 (CUDA 12.2) · **CPU:** Intel Xeon Platinum 8480C (96c/96t) · Ubuntu 24.04.3, Python 3.12
- **Serving:** vLLM 0.8.5.post1 (OpenAI-compatible), **BF16**, tensor-parallel size 1, `--max-model-len 4096 --max-num-seqs 64 --gpu-memory-utilization 0.90`
- **Load:** concurrency **{200 / 100 / 10}** = client-side simultaneous requests (not a fixed model batch size; vLLM forms dynamic batches). QPS = queries/s, TPS = tokens/s, Latency = per-request end-to-end.

| **Model** | **QPS ↑** | **Avg Latency (ms) ↓** | **TPS ↑** |
|------------------------------------------|-----------------------------|-----------------------------|-----------------------------|
| Llama Guard 3 8B                         | 51.14 / 49.97 / 41.53       | 19.55 / 20.01 / 24.08       | 25,177 / 25,177 / 20,924    |
| **Content Binary Guard 8B**              | **77.50 / 77.49 / 83.42**   | **12.90 / 12.91 / 11.99**   | **25,970 / 25,963 / 27,950**|
| *Gain vs. LG3*                           | *+51.5% / +55.1% / +100.9%* | *−34.0% / −35.5% / −50.2%*  | *+3.2% / +3.1% / +33.6%*    |

*Columns show values at concurrency {200 / 100 / 10}. All numbers are from the paper (Table 4).*

---

# More Information

## Limitations
- The training data for this model consists primarily of Korean. Performance in other languages is not guaranteed.  
- The model is not flawless and may produce misclassifications. Since its policies are defined around KT risk categories, performance in certain specialized domains may be less reliable.  
- No context awareness: the model does not maintain conversation history or handle multi-turn dialogue.

## License
This model is released under the [Llama 3.1 Community License Agreement](https://huggingface.co/meta-llama/Meta-Llama-3.1-8B/blob/main/LICENSE).


## Citation
 
```
@misc{lee2025guardvectorenglishllm,
      title={Guard Vector: Beyond English LLM Guardrails with Task-Vector Composition and Streaming-Aware Prefix SFT}, 
      author={Wonhyuk Lee and Youngchol Kim and Yunjin Park and Junhyung Moon and Dongyoung Jeong and Wanjin Park},
      year={2025},
      eprint={2509.23381},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2509.23381}, 
}
```
## Contact 
Technical Inquiries: [responsible.ai@kt.com](mailto:responsible.ai@kt.com)