---
base_model: unsloth/gemma-3-1b-it
tags:
- text-generation-inference
- transformers
- unsloth
- gemma3_text
license: apache-2.0
language:
- en
---

# ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit

- **Developed by:** ArindamSingh
- **License:** apache-2.0
- **Finetuned from model :** unsloth/gemma-3-1b-it

This gemma-3-1b-it-medical-o1-reasoning-finetune-16bit model was trained with Unsloth and Huggingface's TRL library.

Finetuned one of my own as could not find one on internet, at the time of finetuning there were no gemma3 finetunes for medical dataset, esp. on medical reasoning.

### 1. Model Card Snapshot

|  | Details |
| :-- | :-- |
| **Base model** | `google/gemma-3-1b-it` |
| **Parameter count** | 1 B (full) – LoRA rank 8 adapters merged |
| **Precision** | 16-bit (`fp16`) |
| **Domain** | Clinical \& biomedical reasoning |
| **Fine-tuning stack** | FreedomIntelligence **Medical-O1 Reasoning (20 k Q-CoT-A)** + *Unsloth* LoRA |
| **Training recipe** | Supervised CoT SFT → LoRA merge \& quantize |
| **Last updated** | *See HF page* |
| **License** | Apache-2.0 |

### 2. What’s New vs. Base Gemma-3 1B-IT

* **Chain-of-Thought answers** (step-by-step rationales) thanks to Medical-O1 dataset.
* **Unsloth** accelerated LoRA cut training wall-time by ~40% on a single A100.
* **Merged weights** – no adapter step required; drop-in replacement for Gemma.
* **Tiny footprint** – < 2 GB download; runs in ≤ 4 GB VRAM or CPU via GGUF/HF library.


### 3. Intended Use

| ✔️ **Intended** | ❌ **Use with caution / Out-of-scope** |
| :-- | :-- |
| Medical education, PubMed triage, coding suggestions (ICD, SNOMED), research ideation | Automated diagnosis, emergency triage, any decision requiring regulatory clearance |

### 4. Quick Start

```python
from transformers import pipeline

msg = "What is type 2 diabetes?"

pipe = pipeline("text-generation", model="ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit")
messages = [
    {"role": "user", "content": msg},
]
pipe(messages)
```


### 5. Fine-tuning Overview

| Item | Setting |
| :-- | :-- |
| **Dataset** | FreedomIntelligence/`medical-o1-reasoning-SFT` (19 704 rows) |
| **Prompt format** | `Question` + `Complex_CoT` → `Response` |
| **Library** | *Unsloth* 0.6 + 8-bit **paged_adamw** |
| **LoRA config** | r = 8, α = 32, dropout = 0.05 (q/k/v/o \& MLP proj) |
| **Hardware** | 2 × T4-16 GB (flash-attn 2) |
| **Training** | 3 epochs -  LR = 2 e-5 cosine -  batch = 1 × 4 grad-accum |
| **Runtime** | ~4 h (Unsloth vs. ~6.5 h vanilla PEFT) |

### 6. Evaluation Highlights<sup>*</sup>

| Task (dev subsets) | Metric | Base Gemma-1B-IT | **This model** |
| :-- | :-- | :-- | :-- |
| PubMedQA | QA-F1 | 46% | **57%** |

<sup>*100-Q samples, greedy decoding; scripts in `eval/`.</sup>

### 7. Limitations \& Biases

* Possible hallucination of citations or outdated guidelines.
* English-centric dataset; limited pediatrics / rare diseases coverage.
* Not a medical device – always keep a human in the loop.


### 8. Responsible-AI Checklist

- [x] Human review before clinical use
- [x] “Not medical advice” disclaimer


### 9. Citation

```bibtex
@misc{singh2025gemma1bmed,
  title   = {Gemma-3 1B Medical-O1: Compact Chain-of-Thought Clinical LLM},
  author  = {Arindam Singh},
  year    = {2025},
  url     = {https://huggingface.co/ArindamSingh/gemma-3-1b-it-medical-o1-reasoning-finetune-16bit}
}
```


### 10. Acknowledgements

Google DeepMind (Gemma), FreedomIntelligence (Medical-O1 dataset), the Unsloth team, Kaggle, Google Colab and Hugging Face for the open ecosystem.

### 11. Sample Output
[{'generated_text': [{'role': 'user', 'content': 'What is type 2 diabetes?'},
   {'role': 'assistant',
    'content': "Okay, let's break down type 2 diabetes. It's a complex condition, but here's a comprehensive explanation:\n\n**What is Type 2 Diabetes?**\n\nType 2 diabetes is a chronic metabolic disorder in which the body doesn't use insulin properly. Insulin is a hormone produced by the pancreas that helps glucose (sugar) from food get into your cells to be used for energy. When insulin resistance develops, the pancreas has to work harder to produce more insulin to compensate, and eventually, it can't keep up with the demand.\n\n**Here's a more detailed breakdown:**\n\n1. **It's Not About Insulin Resistance (Initially):**  The key difference between type 1 and type 2 diabetes is *how* the body handles insulin.\n   * **Type 1 Diabetes:** This is an autoimmune condition where the body's immune system attacks and destroys the insulin-producing cells (beta cells) in the pancreas.  People with type 1 diabetes *require* insulin injections or pump to survive.\n   * **Type 2 Diabetes:**  This is a process where the body becomes resistant to insulin, and the pancreas initially tries to compensate by producing more insulin. Over time, the pancreas can't keep up, and blood sugar levels rise.\n\n2. **How it Develops:**\n   * **Lifestyle Factors:**  Type 2 diabetes often develops gradually, often as a result of a combination of:\n      * **Genetics:**  A family history of diabetes increases your risk.\n      * **Diet:**  A diet high in processed foods, sugary drinks, and unhealthy fats can contribute.\n      * **Lack of Exercise:**  Being physically inactive increases your risk.\n      * **Obesity:** Excess weight, particularly around the abdomen, is strongly linked to insulin resistance.\n   * **Pancreatic Dysfunction:**  As the pancreas struggles to produce enough insulin, it can gradually lose its ability to do so effectively.\n\n3. **Symptoms:**  Many people with type 2 diabetes have no noticeable symptoms for months or even years.  However, as the condition progresses, symptoms can develop:\n   * **Frequent Urination:**  The kidneys try to get rid of excess sugar in the urine.\n   * **Excessive Thirst:**  Due to the body’s attempt to regulate fluid balance.\n   * **Increased Hunger:**  The body isn't using glucose effectively.\n   * **Fatigue:**  Lack of energy.\n   * **Blurred Vision:**  High blood sugar can affect the lens of the eye.\n   * **Slow-Healing Sores:** High blood sugar can impair wound healing.\n   * **Frequent Infections:** High blood sugar can weaken the immune system.\n\n4. **Complications (if not managed):**  If left untreated, type 2 diabetes can lead to serious health problems:\n   * **Cardiovascular Disease:** Heart disease, stroke.\n   * **Neuropathy:** Nerve damage, causing pain, numbness, and tingling (especially in the hands and feet).\n   * **Nephropathy:** Kidney disease.\n   * **Retinopathy:** Eye damage.\n   * **Foot Problems:**  Poor circulation and nerve damage can lead to infections and ulcers.\n\n**Diagnosis:**\n\n* **Blood Tests:**  A fasting blood glucose test is the primary test.  A random blood glucose test can also be done.\n* **A1C Test:** This tests your average blood sugar level over the past 2-3 months.\n\n**Treatment:**\n\n* **Lifestyle Changes:**  Diet and exercise are crucial.\n* **Metformin:**  A common medication that helps lower blood sugar.\n* **Other Medications:**  Oral medications, insulin injections, or a combination of these may be needed.\n* **Regular Monitoring:**  Blood sugar levels need to be monitored regularly to adjust treatment as needed.\n\n**Important Note:**  This information is for general knowledge and informational purposes only, and does not constitute medical advice. It is essential to consult with a qualified healthcare professional for any health concerns or before making any decisions related to your health or treatment.\n\n**Resources:**\n\n* **American Diabetes Association:** [https://www.diabetes.org/](https://www.diabetes.org/)\n* **Centers for Disease Control and Prevention (CDC) - Diabetes:** [https://www.cdc.gov/diabetes/index.html](https://www.cdc.gov/diabetes/index.html)\n\n---\n\n**Disclaimer:** *I am an AI Chatbot and not a medical professional. This information is intended for general knowledge and informational purposes only, and does not constitute medical advice. It is essential to consult with a qualified healthcare professional for any health concerns or before making any decisions related to your health or treatment.*\n\nTo help me give you even more tailored information, could you tell me:\n\n*   Are you interested in learning more about a specific aspect of type 2 diabetes (e.g., treatment options, prevention, symptoms)?"}]}]
