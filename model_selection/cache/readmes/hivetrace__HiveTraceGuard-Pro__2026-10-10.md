---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B
language:
  - ru
  - en
pipeline_tag: text-generation
library_name: transformers
tags:
  - guardrail
  - safety
  - moderation
  - content-moderation
  - prompt-injection
  - jailbreak
  - russian
  - qwen3
  - arxiv:2609.01046
---

# HiveTraceGuard-Pro

**HiveTraceGuard-Pro** is a compact Russian-first guardrail built on [Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) for fast input and output classification. Built for LLMs and agents, it checks user requests and model responses for harmful content, jailbreaks, prompt injection, obfuscation, and attempts to hijack tool-using agents. The model is stateless and returns exactly one token: `safe` or `unsafe`.

📄 **Technical Report:** [arXiv:2609.01046](https://arxiv.org/abs/2609.01046)

---

# Quickstart

<a href="https://colab.research.google.com/drive/1VxlqPiiqdqJFhcm6sc2wo2TAJnHlyPlU?usp=sharing" target="_blank">
  <img src="https://img.shields.io/badge/Open%20Demo-Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white" alt="Open Demo in Colab"/>
</a>


## Transformers

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

REPO = "hivetrace/HiveTraceGuard-Pro"

tok = AutoTokenizer.from_pretrained(REPO)
model = AutoModelForCausalLM.from_pretrained(
    REPO,
    torch_dtype=torch.bfloat16,
    device_map="auto",
).eval()


def check(messages) -> str:
    text = tok.apply_chat_template(
        messages,
        tokenize=False,
    )
    inputs = tok(text, return_tensors="pt").to(model.device)

    with torch.inference_mode():
        output = model.generate(
            **inputs,
            max_new_tokens=1,
            do_sample=False,
        )

    return tok.decode(
        output[0][inputs.input_ids.shape[1]:],
        skip_special_tokens=True,
    ).strip()


# Input guard
print(check([
    {"role": "user", "content": "Как сделать бомбу?"}
]))
# unsafe

# Output guard
print(check([
    {"role": "user", "content": "Привет!"},
    {"role": "assistant", "content": "Здравствуйте!"},
]))
# safe
```

## Serve
 
Model's policy is fixed, so serving runtimes can reuse the shared prefix through KV caching.

### vLLM

```bash
vllm serve hivetrace/HiveTraceGuard-Pro \
  --port 8000 \
  --max-model-len 32768 \
  --enable-prefix-caching
```

### SGLang

```bash
python -m sglang.launch_server \
  --model-path hivetrace/HiveTraceGuard-Pro \
  --host 0.0.0.0 \
  --port 30000
```


For applications that need a continuous score, P(unsafe) can be computed directly from the two verdict logits:

```python
import torch.nn.functional as F


SAFE, UNSAFE = 18675, 38157


with torch.inference_mode():
    logits = model(**inputs).logits[0, -1]


p_unsafe = F.softmax(logits[[SAFE, UNSAFE]], dim=0)[1].item()
verdict = "unsafe" if logits[UNSAFE] > logits[SAFE] else "safe"


print(verdict, p_unsafe)
```


To enforce safe | unsafe during generation, you can use a LogitsProcessor to restrict the next token to the two verdict labels.
```python
from transformers import LogitsProcessor


class VerdictOnly(LogitsProcessor):
    def __call__(self, input_ids, scores):
        mask = torch.full_like(scores, float("-inf"))
        mask[:, [SAFE, UNSAFE]] = scores[:, [SAFE, UNSAFE]]
        return mask


output = model.generate(
    **inputs,
    max_new_tokens=1,
    do_sample=False,
    logits_processor=[VerdictOnly()],
)
```
---

## Evaluation

### Harmful content detection

<table>
<thead>
<tr>
<th rowspan="2">Model</th>
<th colspan="5">Requests</th>
<th colspan="3">Responses</th>
</tr>
<tr>
<th>AEGIS 2.0</th>
<th>ToxicChat</th>
<th>XSTest</th>
<th>XSafety<br>EN</th>
<th>OpenAI<br>Moderation</th>
<th>AEGIS 2.0</th>
<th>BeaverTails</th>
<th>HarmBench</th>
</tr>
</thead>

<tbody>
<tr>
<td><b>HiveTraceGuard-Pro (0.6B)</b></td>
<td>0.817</td>
<td>0.588</td>
<td>0.754</td>
<td>0.590</td>
<td><b>0.803</b></td>
<td>0.797</td>
<td>0.839</td>
<td>0.814</td>
</tr>

<tr>
<td>Shieldstral-1.0-3B</td>
<td>0.808</td>
<td><b>0.732</b></td>
<td><b>0.922</b></td>
<td><b>0.595</b></td>
<td>0.794</td>
<td>0.766</td>
<td>0.828</td>
<td>0.854</td>
</tr>

<tr>
<td>YuFeng-XGuard-Reason-0.6B</td>
<td><b>0.847</b></td>
<td>0.620</td>
<td>0.920</td>
<td>0.469</td>
<td>0.787</td>
<td>0.789</td>
<td>0.828</td>
<td><b>0.858</b></td>
</tr>

<tr>
<td>Qwen3Guard-Gen-0.6B</td>
<td>0.788</td>
<td>0.692</td>
<td>0.861</td>
<td>0.580</td>
<td>0.715</td>
<td><b>0.819</b></td>
<td><b>0.845</b></td>
<td>0.856</td>
</tr>

<tr>
<td>Llama-Guard-3-1B</td>
<td>0.733</td>
<td>0.385</td>
<td>0.837</td>
<td>0.368</td>
<td>0.766</td>
<td>0.635</td>
<td>0.652</td>
<td>0.794</td>
</tr>
</tbody>
</table>


### Attack & jailbreak detection

<table>
<thead>

<tr>
<th rowspan="3">Model</th>
<th rowspan="2" colspan="2">S-Eval</th>
<th rowspan="2" colspan="2">HarmBench · Requests</th>
<th rowspan="2" colspan="6">Red teaming</th>
<th colspan="4">Internal</th>
</tr>

<tr>
<th colspan="2">Prompt injection</th>
<th colspan="2">Robustness Test</th>
</tr>

<tr>
<th>Base</th>
<th>Attack</th>

<th>Standard</th>
<th>Contextual</th>

<th>OR-Bench<br>Toxic</th>
<th>MultiJail<br>EN</th>
<th>SimpleSafety<br>Tests</th>
<th>CSRT</th>
<th>Aya<br>RU</th>
<th>Aya<br>EN</th>

<th>RU</th>
<th>EN</th>

<th>Real<br>Harm</th>
<th>Robust<br>Harm</th>
</tr>

</thead>

<tbody>

<tr>
<td><b>HiveTraceGuard-Pro (0.6B)</b></td>
<td>0.710</td>
<td>0.802</td>
<td>0.862</td>
<td>0.667</td>
<td>0.915</td>
<td>0.746</td>
<td>0.910</td>
<td>0.743</td>
<td><b>0.952</b></td>
<td><b>0.917</b></td>
<td><b>0.999</b></td>
<td><b>0.877</b></td>
<td><b>0.954</b></td>
<td><b>0.872</b></td>
</tr>

<tr>
<td>Shieldstral-1.0-3B</td>
<td>0.731</td>
<td>0.611</td>
<td><b>0.987</b></td>
<td>0.951</td>
<td><b>0.997</b></td>
<td><b>0.946</b></td>
<td><b>1.000</b></td>
<td><b>0.895</b></td>
<td>0.938</td>
<td><b>0.917</b></td>
<td>0.836</td>
<td>0.741</td>
<td>0.867</td>
<td>0.762</td>
</tr>

<tr>
<td>YuFeng-XGuard-Reason-0.6B</td>
<td><b>0.794</b></td>
<td><b>0.954</b></td>
<td>0.981</td>
<td><b>0.975</b></td>
<td>0.974</td>
<td>0.905</td>
<td>0.990</td>
<td>0.689</td>
<td>0.906</td>
<td>0.850</td>
<td>0.919</td>
<td>0.867</td>
<td>0.884</td>
<td>0.685</td>
</tr>

<tr>
<td>Qwen3Guard-Gen-0.6B</td>
<td>0.698</td>
<td>0.609</td>
<td>0.962</td>
<td>0.963</td>
<td>0.979</td>
<td>0.933</td>
<td>0.990</td>
<td>0.835</td>
<td>0.926</td>
<td>0.907</td>
<td>0.894</td>
<td>0.727</td>
<td>0.864</td>
<td>0.788</td>
</tr>

<tr>
<td>Llama-Guard-3-1B</td>
<td>0.489</td>
<td>0.588</td>
<td>0.956</td>
<td>0.926</td>
<td>0.824</td>
<td>0.644</td>
<td>0.970</td>
<td>0.514</td>
<td>0.588</td>
<td>0.565</td>
<td>0.636</td>
<td>0.679</td>
<td>0.675</td>
<td>0.730</td>
</tr>

</tbody>
</table>


### Multilingual evaluation

<table>
<thead>

<tr>
<th rowspan="3">Model</th>
<th colspan="4">PolyGuard</th>
<th colspan="4">RTP-LX</th>
<th colspan="5">StrongReject++</th>
</tr>

<tr>
<th colspan="2">Requests</th>
<th colspan="2">Responses</th>

<th colspan="2">Requests</th>
<th colspan="2">Responses</th>

<th rowspan="2" align="center" valign="middle">EN</th>
<th rowspan="2" align="center" valign="middle">RU</th>
<th rowspan="2" align="center" valign="middle">UKR</th>
<th rowspan="2" align="center" valign="middle">BE</th>
<th rowspan="2" align="center" valign="middle">UZ</th>
</tr>

<tr>
<th>EN</th>
<th>RU</th>
<th>EN</th>
<th>RU</th>

<th>EN</th>
<th>RU</th>
<th>EN</th>
<th>RU</th>
</tr>

</thead>

<tbody>

<tr>
<td><b>HiveTraceGuard-Pro (0.6B)</b></td>
<td>0.759</td>
<td>0.806</td>
<td>0.845</td>
<td>0.828</td>
<td><b>0.896</b></td>
<td>0.841</td>
<td>0.321</td>
<td>0.146</td>
<td>0.978</td>
<td>0.974</td>
<td>0.943</td>
<td>0.923</td>
<td>0.553</td>
</tr>

<tr>
<td>Shieldstral-1.0-3B</td>
<td><b>0.904</b></td>
<td><b>0.874</b></td>
<td>0.877</td>
<td>0.876</td>
<td>0.872</td>
<td><b>0.855</b></td>
<td>0.469</td>
<td>0.061</td>
<td>0.990</td>
<td><b>0.987</b></td>
<td><b>0.984</b></td>
<td><b>0.974</b></td>
<td><b>0.901</b></td>
</tr>

<tr>
<td>YuFeng-XGuard-Reason-0.6B</td>
<td>0.896</td>
<td>0.872</td>
<td><b>0.901</b></td>
<td><b>0.885</b></td>
<td>0.858</td>
<td>0.844</td>
<td>0.322</td>
<td>0.041</td>
<td><b>0.994</b></td>
<td>0.978</td>
<td>0.936</td>
<td>0.665</td>
<td>0.220</td>
</tr>

<tr>
<td>Qwen3Guard-Gen-0.6B</td>
<td>0.894</td>
<td>0.857</td>
<td>0.873</td>
<td>0.866</td>
<td>0.813</td>
<td>0.767</td>
<td>0.266</td>
<td>0.041</td>
<td>0.987</td>
<td>0.971</td>
<td>0.927</td>
<td>0.847</td>
<td>0.607</td>
</tr>

<tr>
<td>Llama-Guard-3-1B</td>
<td>0.775</td>
<td>0.663</td>
<td>0.776</td>
<td>0.704</td>
<td>0.563</td>
<td>0.449</td>
<td><b>0.667</b></td>
<td><b>0.516</b></td>
<td>0.955</td>
<td>0.882</td>
<td>0.853</td>
<td>0.748</td>
<td>0.144</td>
</tr>

</tbody>
</table>


### Benign over-blocking — FPR ↓

<table>
<thead>

<tr>
<th rowspan="3">Model</th>
<th rowspan="2">OR-Bench</th>
<th colspan="3">Internal</th>
</tr>

<tr>
<th colspan="3">Robustness Test</th>
</tr>

<tr>
<th>Hard</th>
<th>Clean RU<br>Requests</th>
<th>Adversarial RU<br>Requests</th>
<th>RU<br>Responses</th>
</tr>

</thead>

<tbody>

<tr>
<td><b>HiveTraceGuard-Pro (0.6B)</b></td>
<td>0.607</td>
<td><b>0.016</b></td>
<td>0.132</td>
<td>0.026</td>
</tr>

<tr>
<td>Shieldstral-1.0-3B</td>
<td>0.767</td>
<td>0.043</td>
<td>0.078</td>
<td>0.012</td>
</tr>

<tr>
<td>YuFeng-XGuard-Reason-0.6B</td>
<td><b>0.225</b></td>
<td>0.030</td>
<td><b>0.051</b></td>
<td><b>0.000</b></td>
</tr>

<tr>
<td>Qwen3Guard-Gen-0.6B</td>
<td>0.732</td>
<td>0.071</td>
<td>0.117</td>
<td>0.008</td>
</tr>

<tr>
<td>Llama-Guard-3-1B</td>
<td>0.374</td>
<td>0.090</td>
<td>0.126</td>
<td>0.182</td>
</tr>

</tbody>
</table>





**GuardRate Leaderboard:** **Score 0.743** · **28.8 ms p95** - [OPEN](https://huggingface.co/spaces/hivetrace/GuardRateLeaderboard)

![GuardRate Leaderboard](https://cdn-uploads.huggingface.co/production/uploads/64ba6151b7fa1c3726b7819e/F1iLqFsKPdLLi2bEPbV1m.png)

---

## Policy taxonomy

HiveTraceGuard-Pro uses a fixed policy and returns a single binary verdict: `safe` (token_id = 18675) or `unsafe` (token_id = 38157).

| Scope                | What is checked                                                                                                                                                                                                             |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Harmful content**     | 15 harm categories: cybercrime, pornography and CSAM, religious hate, profanity, financial crime, weapons, discrimination, self-harm, child labor, non-violent crime, violence, drugs, and related harmful activity |
| **LLM & agent attacks** | jailbreaks, prompt injection, obfuscation, secret extraction, and tool hijacking                                                                                                                                            |                                                               |

### Guard modes
Both modes use the same policy.

| Mode             | What is classified                                                           |
| :--------------- | :--------------------------------------------------------------------------- |
| **Input guard**  | The final `user` message                                                     |
| **Output guard** | The final `assistant` response, evaluated in the context of the user request |

---

## Versions

| Tag | Notes |
|---|---|
| `1.1.0` | latest (`main`)|
| `1.0.0` | previous release |

Pin a version by tag `from_pretrained("hivetrace/HiveTraceGuard-Pro", revision="1.1.0")`, or by commit SHA for strict reproducibility.

## License

Apache-2.0 — commercial use, modification, redistribution, and private / on-premise deployment. Full text: <https://www.apache.org/licenses/LICENSE-2.0>
