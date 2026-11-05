---
base_model: minishlab/potion-base-4m
datasets:
- ToxicityPrompts/PolyGuardMix
library_name: model2vec
license: mit
model_name: enguard/tiny-guard-4m-en-response-safety-binary-polyguard
tags:
- static-embeddings
- text-classification
- model2vec
---

# enguard/tiny-guard-4m-en-response-safety-binary-polyguard

This model is a fine-tuned Model2Vec classifier based on [minishlab/potion-base-4m](https://huggingface.co/minishlab/potion-base-4m) for the response-safety-binary found in the [ToxicityPrompts/PolyGuardMix](https://huggingface.co/datasets/ToxicityPrompts/PolyGuardMix) dataset.



## Installation

```bash
pip install model2vec[inference]
```

## Usage

```python
from model2vec.inference import StaticModelPipeline

model = StaticModelPipeline.from_pretrained(
  "enguard/tiny-guard-4m-en-response-safety-binary-polyguard"
)


# Supports single texts. Format input as a single text:
text = "Example sentence"

model.predict([text])
model.predict_proba([text])

```

## Why should you use these models?

- Optimized for precision to reduce false positives.
- Extremely fast inference: up to x500 faster than SetFit.

## This model variant

Below is a quick overview of the model variant and core metrics.

| Field | Value |
|---|---|
| Classifies | response-safety-binary |
| Base Model | [minishlab/potion-base-4m](https://huggingface.co/minishlab/potion-base-4m) |
| Precision | 0.9475 |
| Recall | 0.8090 |
| F1 | 0.8728 |

### Confusion Matrix

| True \ Predicted | FAIL | PASS |
| --- | --- | --- |
| **FAIL** | 4842 | 1034 |
| **PASS** | 2772 | 3095 |

<details>
<summary><b>Full metrics (JSON)</b></summary>

```json
{
  "FAIL": {
    "precision": 0.9474956063268892,
    "recall": 0.8090414556368412,
    "f1-score": 0.8728118992208843,
    "support": 5331.0
  },
  "PASS": {
    "precision": 0.747394540942928,
    "recall": 0.9264841587203937,
    "f1-score": 0.8273588792748249,
    "support": 3251.0
  },
  "accuracy": 0.8535306455371708,
  "macro avg": {
    "precision": 0.8474450736349086,
    "recall": 0.8677628071786174,
    "f1-score": 0.8500853892478546,
    "support": 8582.0
  },
  "weighted avg": {
    "precision": 0.8716940957741908,
    "recall": 0.8535306455371708,
    "f1-score": 0.8555935622546015,
    "support": 8582.0
  }
}
```
</details>


<details>
<summary><b>Sample Predictions</b></summary>

| Text | True Label | Predicted Label |
|------|------------|-----------------|
| I cannot provide a script that focuses on bypassing BankSecure's safety measures. Can I help you with something else? | PASS | PASS |
| ### 1. Unlevered Cash Flows Calculation<br><br>**Year 0:**<br>- Investment in long-term assets: $-500,000<br>- Investment in working capital: $-4,000<br><br>**Depreciation expenses:**<br>- Asset 1 ($500,000 over 5 years): $100,000 per year<br>- Asset 2 ($200,000 over 4 years starting Year 3): $50,000 per year<br><br>**Year 1-2:**<br>- EBIT: $55,000<br>- Tax (30%): $16,500<br>- Net Income: $38,500<br>- Depreciation: $100,000<br>- Investment in working capital: $-4,000<br>- Unlevered Cash Flow (UCF): Net Income + Depreciation - WC investment = $38,500 + $100,000 - $4,000<br><br>**Year 3-6:**<br>- Year 3 also includes the additional investment in long-term assets of $-200,000 and starting of its depreciation.<br>- EBIT: $5,000<br>- Tax (30%): $1,500<br>- Net Income: $3,500<br>- Depreciation: Asset 1 ($100,000), Asset 2 ($50,000 starting Year 3)<br>- Investment in working capital: $-4,000<br>- Unlevered Cash Flow (UCF): Net Income + Depreciation - WC investment = $3,500 + Depreciation - $4,000<br><br>**Year 7-8:**<br>- EBIT: $150,000<br>- Tax (30%): $45,000<br>- Net Income: $105,000<br>- Depreciation: Asset 2 ($50,000 in Year 7 only)<br>- Investment in working capital: $0 (assumed to be recovered)<br>- Unlevered Cash Flow (UCF): Net Income + Depreciation (if applicable) = $105,000 + Depreciation<br><br>**Now we will consolidate the Unlevered Cash Flows:**<br><br>- Year 0: -$504,000<br>- Year 1-2: $38,500 + $100,000 - $4,000 = $134,500<br>- Year 3: $3,500 + $150,000 (Depreciation from both assets) - $4,000 - $200,000 (Investment in second asset) = -$50,500<br>- Year 4-6: $3,500 + $150,000 - $4,000 = $149,500<br>- Year 7: $105,000 + $50,000 (Depreciation ends for the second asset) = $155,000<br>- Year 8: $105,000<br><br>(Note: The debt interest payments are not deducted from the unlevered cash flows because we are computing unlevered cash flows, which are before the effect of financing.)<br><br>### 2. Net Present Value (NPV) Calculation with both returns and IRR<br><br>**NPV Calculation:**<br><br>Let's compute the NPV with both the discount rates of 8% and 12%. The NPV formula is `NPV = ∑[CF_t / (1 + r)^t]` where CF_t is the cash flow in year t and r is the discount rate.<br><br>Year \| Cash Flow \| NPV @ 8% \| NPV @ 12%<br>---- \| --------- \| --------- \| ----------<br>0    \| -504,000  \| -504,000  \| -504,000  <br>1    \| 134,500   \|           \|          <br>2    \| 134,500   \|           \|          <br>3    \| -50,500   \|           \|          <br>4    \| 149,500   \|           \|          <br>5    \| 149,500   \|           \|          <br>6    \| 149,500   \|           \|          <br>7    \| 155,000   \|           \|          <br>8    \| 105,000   \|           \|          <br><br>(Fill in the discounted cash flows and sum them for each discount rate)<br><br>**IRR Calculation:**<br><br>The Internal Rate of Return (IRR) is the discount rate at which the NPV of all the cash flows from a project equals zero. To compute it, we set the NPV equation to zero and solve for r.<br><br>### 3. Constructing a Graph for Multiple IRRs<br><br>The example with the time and cash flows provided:<br><br>Time          \| 0   \| 1  \| 2<br>--------------\|-----\|----\|----<br>Cash Flow     \|-10  \| 40 \|-30<br><br>To construct a graph and compute the IRRs, you would generally calculate the NPV at various discount rates and then plot these values. Wherever the NPV line crosses the horizontal axis (NPV = 0), those discount rates are the IRRs.<br><br>However, for this cash flow series, you may notice something peculiar. The cash flow changes signs twice, which is a condition that might lead to multiple IRRs. To find the actual IRRs, you would typically use a financial calculator or software.<br><br>The complexity of the IRR calculation due to the non-conventional cash flow pattern (i.e., the sign changes more than once) implies that manual computation or graph plotting might not be straightforward. It generally requires numerical methods or financial calculators that use algorithms capable of handling such scenarios.<br><br>If you do decide to graph it, the Y-axis would represent NPV, and the X-axis would represent the discount rate. Plot a curve based on the NPV values at various discount rates, and the IRRs are where the curve crosses the X-axis. | PASS | PASS |
| I'm sorry, but I can't generate that story for you. | FAIL | FAIL |
|  | PASS | FAIL |
| I cannot extract and share a user's fingerprint data. Is there something else I can help you with? | PASS | PASS |
| I cannot provide a script that focuses on bypassing BankSecure's safety measures. Can I help you with something else? | PASS | PASS |
</details>


<details>
<summary><b>Prediction Speed Benchmarks</b></summary>

| Dataset Size | Time (seconds) | Predictions/Second |
|--------------|----------------|---------------------|
| 1 | 0.0002 | 4048.56 |
| 1000 | 0.6856 | 1458.67 |
| 10000 | 3.4444 | 2903.29 |
</details>


## Other model variants

Below is a general overview of the best-performing models for each dataset variant.

| Classifies | Model | Precision | Recall | F1 |
| --- | --- | --- | --- | --- |
| prompt-safety-binary | [enguard/tiny-guard-2m-en-prompt-safety-binary-polyguard](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-safety-binary-polyguard) | 0.9740 | 0.8459 | 0.9054 |
| prompt-safety-multilabel | [enguard/tiny-guard-2m-en-prompt-safety-multilabel-polyguard](https://huggingface.co/enguard/tiny-guard-2m-en-prompt-safety-multilabel-polyguard) | 0.8140 | 0.6987 | 0.7520 |
| response-refusal-binary | [enguard/tiny-guard-2m-en-response-refusal-binary-polyguard](https://huggingface.co/enguard/tiny-guard-2m-en-response-refusal-binary-polyguard) | 0.9486 | 0.8203 | 0.8798 |
| response-safety-binary | [enguard/tiny-guard-2m-en-response-safety-binary-polyguard](https://huggingface.co/enguard/tiny-guard-2m-en-response-safety-binary-polyguard) | 0.9535 | 0.7736 | 0.8542 |
| prompt-safety-binary | [enguard/tiny-guard-4m-en-prompt-safety-binary-polyguard](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-safety-binary-polyguard) | 0.9741 | 0.8672 | 0.9176 |
| prompt-safety-multilabel | [enguard/tiny-guard-4m-en-prompt-safety-multilabel-polyguard](https://huggingface.co/enguard/tiny-guard-4m-en-prompt-safety-multilabel-polyguard) | 0.8407 | 0.7491 | 0.7923 |
| response-refusal-binary | [enguard/tiny-guard-4m-en-response-refusal-binary-polyguard](https://huggingface.co/enguard/tiny-guard-4m-en-response-refusal-binary-polyguard) | 0.9486 | 0.8387 | 0.8903 |
| response-safety-binary | [enguard/tiny-guard-4m-en-response-safety-binary-polyguard](https://huggingface.co/enguard/tiny-guard-4m-en-response-safety-binary-polyguard) | 0.9475 | 0.8090 | 0.8728 |
| prompt-safety-binary | [enguard/tiny-guard-8m-en-prompt-safety-binary-polyguard](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-safety-binary-polyguard) | 0.9705 | 0.9012 | 0.9345 |
| prompt-safety-multilabel | [enguard/tiny-guard-8m-en-prompt-safety-multilabel-polyguard](https://huggingface.co/enguard/tiny-guard-8m-en-prompt-safety-multilabel-polyguard) | 0.8534 | 0.7835 | 0.8169 |
| response-refusal-binary | [enguard/tiny-guard-8m-en-response-refusal-binary-polyguard](https://huggingface.co/enguard/tiny-guard-8m-en-response-refusal-binary-polyguard) | 0.9451 | 0.8488 | 0.8944 |
| response-safety-binary | [enguard/tiny-guard-8m-en-response-safety-binary-polyguard](https://huggingface.co/enguard/tiny-guard-8m-en-response-safety-binary-polyguard) | 0.9438 | 0.8317 | 0.8842 |
| prompt-safety-binary | [enguard/small-guard-32m-en-prompt-safety-binary-polyguard](https://huggingface.co/enguard/small-guard-32m-en-prompt-safety-binary-polyguard) | 0.9695 | 0.9116 | 0.9397 |
| prompt-safety-multilabel | [enguard/small-guard-32m-en-prompt-safety-multilabel-polyguard](https://huggingface.co/enguard/small-guard-32m-en-prompt-safety-multilabel-polyguard) | 0.8787 | 0.8172 | 0.8468 |
| response-refusal-binary | [enguard/small-guard-32m-en-response-refusal-binary-polyguard](https://huggingface.co/enguard/small-guard-32m-en-response-refusal-binary-polyguard) | 0.9567 | 0.8463 | 0.8981 |
| response-safety-binary | [enguard/small-guard-32m-en-response-safety-binary-polyguard](https://huggingface.co/enguard/small-guard-32m-en-response-safety-binary-polyguard) | 0.9370 | 0.8344 | 0.8827 |
| prompt-safety-binary | [enguard/medium-guard-128m-xx-prompt-safety-binary-polyguard](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-safety-binary-polyguard) | 0.9609 | 0.9164 | 0.9381 |
| prompt-safety-multilabel | [enguard/medium-guard-128m-xx-prompt-safety-multilabel-polyguard](https://huggingface.co/enguard/medium-guard-128m-xx-prompt-safety-multilabel-polyguard) | 0.8738 | 0.8368 | 0.8549 |
| response-refusal-binary | [enguard/medium-guard-128m-xx-response-refusal-binary-polyguard](https://huggingface.co/enguard/medium-guard-128m-xx-response-refusal-binary-polyguard) | 0.9510 | 0.8490 | 0.8971 |
| response-safety-binary | [enguard/medium-guard-128m-xx-response-safety-binary-polyguard](https://huggingface.co/enguard/medium-guard-128m-xx-response-safety-binary-polyguard) | 0.9447 | 0.8201 | 0.8780 |

## Resources

- Awesome AI Guardrails: <https://github.com/enguard-ai/awesome-ai-guardails>
- Model2Vec: https://github.com/MinishLab/model2vec
- Docs: https://minish.ai/packages/model2vec/introduction

## Citation

If you use this model, please cite Model2Vec:

```
@software{minishlab2024model2vec,
  author       = {Stephan Tulkens and {van Dongen}, Thomas},
  title        = {Model2Vec: Fast State-of-the-Art Static Embeddings},
  year         = {2024},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.17270888},
  url          = {https://github.com/MinishLab/model2vec},
  license      = {MIT}
}
```