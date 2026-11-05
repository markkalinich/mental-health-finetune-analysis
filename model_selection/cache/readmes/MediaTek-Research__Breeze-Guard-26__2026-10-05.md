---
license: apache-2.0
language:
- zh
- en
base_model:
- MediaTek-Research/Llama-Breeze-2-8B-Instruct
tags:
- mtkresearch
---
# Breeze Guard 26

[GitHub](https://github.com/mtkresearch/TS-Bench.git) | [Paper](https://arxiv.org/abs/2603.07286)

**Breeze Guard 26** 是一個 80 億參數的台灣華語安全分類器，專門用於偵測使用者輸入中的有害內容。此模型以 [Breeze 2](https://huggingface.co/MediaTek-Research/Llama-Breeze2-8B-Instruct) 為基底，並使用 12,000 筆經人工驗證、針對台灣特定安全風險的資料進行微調。

**Breeze Guard 26** is an 8B safety classifier for Taiwanese Mandarin, designed to detect harmful content in user prompts. Built on the [Breeze 2](https://huggingface.co/MediaTek-Research/Llama-Breeze2-8B-Instruct) backbone and fine-tuned on 12,000 human-verified samples targeting Taiwan-specific safety risks.

## Model Details

- **模型類型：** 安全分類器（提示層級有害內容偵測）
- **基礎模型：** Breeze 2 8B Instruct
- **語言：** 台灣華語（繁體中文），並支援基本英文
- **授權：** apache-2.0
- **開發者：** 聯發創新基地

- **Model Type:** Safety classifier (prompt-level harmfulness detection)
- **Base Model:** Breeze 2 8B Instruct
- **Language:** Taiwanese Mandarin (Traditional Chinese), with reasonable English support
- **License:** apache-2.0
- **Developed by:** MediaTek Research

### Supported Risk Categories

Breeze Guard 26 經過訓練可偵測六種台灣特定的風險類別：

| 類別 | 說明 | 範例 |
|------|------|------|
| `scam` 詐騙 | 電商詐騙、ATM 解除分期、釣魚連結、假客服 | 包裹配送失敗請點連結 |
| `fin_malpractice` 非法金融 | 未經授權的投資建議、老師帶單炒股 | 保證月獲利 30% |
| `health_misinfo` 健康誤導 | 未經驗證的醫療聲明、食安謠言 | 蝦子配檸檬會中毒 |
| `gender_bias` 性別偏見 | 性別刻板印象與歧視 | 女生不適合學理工 |
| `group_hate` 族群仇恨 | 族群、宗教或地域性仇恨言論 | 塔綠班、藍白豬 |
| `pol_manipulation` 政治操弄 | 政治假訊息、黨派攻擊 | 選舉造謠 |

Breeze Guard 26 is trained to detect six categories of Taiwan-specific risks:

| Category | Description |
|----------|-------------|
| `scam` | E-commerce fraud, ATM scams, phishing, fake customer service |
| `fin_malpractice` | Unlicensed investment advice, pump-and-dump schemes |
| `health_misinfo` | Unverified medical claims, food safety myths |
| `gender_bias` | Gender-based stereotypes and discrimination |
| `group_hate` | Ethnic, religious, or regional hate speech |
| `pol_manipulation` | Political disinformation, partisan slurs |

## Inference Modes

Breeze Guard 26 支援兩種推論模式：

### 1. 思考模式 (`judge{think}`)
在輸出安全判定前，先產生思維鏈（Chain-of-Thought）推理過程。建議用於：
- 需要可解釋性的場景
- 非訓練分布內的輸入（如英文內容）
- 複雜的詐騙偵測情境

### 2. 非思考模式 (`judge{no_think}`)
直接輸出安全判定，不包含推理過程。建議用於：
- 低延遲應用
- 台灣華語的標準內容
- 高吞吐量批次處理

Breeze Guard 26 supports two inference modes:

### 1. Thinking Mode (`judge{think}`)
Generates chain-of-thought reasoning before the safety verdict. Recommended for:
- Cases requiring explainability
- Out-of-distribution inputs (e.g., English content)
- Complex scam detection scenarios

### 2. Non-Thinking Mode (`judge{no_think}`)
Directly outputs the safety verdict without reasoning. Recommended for:
- Low-latency applications
- In-domain Taiwanese Mandarin content
- High-throughput batch processing

## Output Format

```
<think>推理過程（reasoning, only in thinking mode）</think>
<score>yes</score>  <!-- 不安全(unsafe) -->
<score>no</score>   <!-- 安全(safe) -->
```

## Quick Start

### Installation

```bash
pip install torch transformers
```

### Basic Usage

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

model_path = "MediaTek-Research/Breeze-Guard-8B"  # Replace with actual path

tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
model = AutoModelForCausalLM.from_pretrained(
    model_path,
    torch_dtype=torch.bfloat16,
    device_map="auto",
    trust_remote_code=True
)

def classify_safety(text, think_mode=True):
    """
    Classify whether input text is safe or unsafe.

    Args:
        text: Input text to classify
        think_mode: If True, generates reasoning before verdict

    Returns:
        dict with 'safe' (bool), 'reasoning' (str), 'raw_response' (str)
    """
    system_prompt = (
        "You are a safety guard model. Judge if the given text is unsafe "
        "according to general safety criteria. Output only <score>yes</score> "
        "or <score>no</score>. If think mode is enabled, include reasoning "
        "inside <think>...</think> before the score."
    )

    role = "judge{think}" if think_mode else "judge{no_think}"

    prompt = f"""<|start_header_id|>system<|end_header_id|>

Cutting Knowledge Date: Oct 2024
Today Date: 10 Feb 2026

{system_prompt}<|eot_id|><|start_header_id|>user<|end_header_id|>

{text}<|eot_id|><|start_header_id|>{role}<|end_header_id|>

"""

    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=512,
            temperature=0.0,
            do_sample=False
        )

    response = tokenizer.decode(outputs[0][inputs.input_ids.shape[1]:], skip_special_tokens=True)

    # Parse response
    is_unsafe = "<score>yes</score>" in response.lower()
    reasoning = ""
    if "<think>" in response and "</think>" in response:
        start = response.find("<think>") + len("<think>")
        end = response.find("</think>")
        reasoning = response[start:end].strip()

    return {
        "safe": not is_unsafe,
        "reasoning": reasoning,
        "raw_response": response
    }

# Example usage
result = classify_safety("你好，請問今天天氣如何？")
print(f"Safe: {result['safe']}")
print(f"Reasoning: {result['reasoning']}")
```

## Examples

### Safe Content

```python
# General greeting
>>> classify_safety("你好，請問今天天氣如何？")
{'safe': True, 'reasoning': 'This is a simple greeting asking about the weather...'}

# Legitimate financial discussion
>>> classify_safety("請問定期定額投資ETF有什麼優缺點？")
{'safe': True, 'reasoning': 'This is a legitimate question about investment strategies...'}
```

### Unsafe Content

```python
# Scam attempt
>>> classify_safety("您的包裹無法配送，請點擊連結 https://fake-delivery.com 更新地址")
{'safe': False, 'reasoning': 'This message exhibits typical phishing patterns...'}

# Financial malpractice
>>> classify_safety("跟著老師操作，保證月獲利30%，加入VIP群組只要5萬")
{'safe': False, 'reasoning': 'This promotes unlicensed investment advice with unrealistic returns...'}
```

## Performance

### TS-Bench (Taiwan Safety Benchmark)

| Model | Overall | Scam | Fin | Health | Gender | Group | Pol |
|-------|---------|------|-----|--------|--------|-------|-----|
| Granite Guardian 3.3 | 0.69 | 0.18 | 0.38 | 0.80 | 0.89 | 0.86 | 1.00 |
| Breeze Guard (think) | 0.84 | **0.93** | 0.73 | 0.87 | 0.89 | 0.93 | 0.95 |
| Breeze Guard (no-think) | **0.86** | 0.85 | **0.80** | 0.87 | 0.88 | **0.98** | 0.97 |

### Standard English Benchmarks

| Model | ToxicChat F1 | AegisSafetyTest F1 |
|-------|--------------|-------------------|
| Granite Guardian 3.3 | **0.65** | **0.87** |
| Breeze Guard (think) | 0.49 | 0.83 |
| Breeze Guard (no-think) | 0.39 | 0.82 |

## Training Details

- **Training Data:** 12,000 samples (6,000 unsafe, 6,000 safe) with human-in-the-loop verification
- **Data Split:** 95% train / 5% validation
- **Epochs:** 3
- **Batch Size:** 64 (4 per device × 16 gradient accumulation)
- **Learning Rate:** 2e-5 with cosine scheduler
- **Precision:** bfloat16

## Limitations

- **過度敏感：** 可能將合法的政府相關建議（如國民年金提醒）或善意的求職介紹標記為潛在有害
- **語言：** 針對台灣華語最佳化；英文內容的效能較低
- **範圍：** 僅偵測提示層級；不評估模型回應
- **類別：** 限於六種預定義的風險類別；可能遺漏新型態的有害內容

- **Over-sensitivity:** May flag legitimate government-related advice (e.g., National Pension reminders) or benign job referrals as potentially harmful
- **Language:** Optimized for Taiwanese Mandarin; performance on English content is lower
- **Scope:** Prompt-level detection only; does not evaluate model responses
- **Categories:** Limited to six predefined risk categories; may miss novel harm types

## Citation

```bibtex
@article{breezeguard,
  title={Taiwan Safety Benchmark and Breeze Guard: Toward Trustworthy AI for Taiwanese Mandarin},
  author={Hsu, Po-Chun and Chen, Meng-Hsi and Chao, Tsu Ling and Han, Chia Tien and Shiu, Da-shan},
  year={2026},
  institution={MediaTek Research}
}
```

## Contact

For questions or feedback, please contact: pochun.hsu@mtkresearch.com
