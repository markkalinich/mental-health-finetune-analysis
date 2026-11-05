---
language:
  - fr
license: apache-2.0
library_name: transformers
pipeline_tag: fill-mask
tags:
  - medical
  - healthcare
  - biomedical
  - clinical
  - french
  - roberta
  - fill-mask
  - doctobert
datasets:
  - doctolib-lab/finemed-fr
  - doctolib-lab/finemed-rephrased-fr
---

# DoctoBERT-fr-base

<center>
  <img src="assets/logo_doctobert.png" width="100%" alt="DoctoBERT">
</center>

<p align="center">
<a href="https://huggingface.co/blog/bofenghuang/doctobert-fr-release">🤗 Blog</a> |
<a href="https://arxiv.org/abs/2606.22079">📄 Paper</a> |
<a href="https://github.com/doctolib-lab/doctobert">💻 Code</a> |
<a href="https://huggingface.co/collections/doctolib-lab/finemed-fr">🌐 FineMed</a> |
<a href="https://huggingface.co/collections/doctolib-lab/doctobert-fr">🩺 DoctoBERT</a>
</p>


## 📚 Introduction

**DoctoBERT-fr-base** is a French medical encoder for biomedical and clinical NLP. It uses the **RoBERTa** architecture (111M parameters, 512-token context) and is pretrained from scratch on [FineMed-fr](https://huggingface.co/datasets/doctolib-lab/finemed-fr) and [FineMed-rephrased-fr](https://huggingface.co/datasets/doctolib-lab/finemed-rephrased-fr). DoctoBERT leads the academic DrBenchmark, topping both aggregate metrics and five of seven tasks.

Its training data is curated from heterogeneous open web corpora (FineWeb-2, FinePDFs, FineWiki), which bring scale, source and stylistic diversity, and inherited quality control. Each document is annotated along three axes: subdomain, educational quality, and medical-term density. DoctoBERT then trains on a mix of two parts: the filtered high-quality, entity-rich documents, and LLM-rephrased variants that raise medical-term density and vary the contexts around medical terms across many genres, audiences, and registers. This breadth and density build robustness to real-world clinical text, which is often noisy and inconsistent in style.

For long-context use, see its sibling [DoctoModernBERT-fr-base](https://huggingface.co/doctolib-lab/doctomodernbert-fr-base).

## 🚀 How to Use

### Fill-mask

Using `AutoModelForMaskedLM`:

```python
from transformers import AutoTokenizer, AutoModelForMaskedLM

model_id = "doctolib-lab/doctobert-fr-base"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForMaskedLM.from_pretrained(model_id)

text = f"Le patient souffre d'une {tokenizer.mask_token} aiguë."
inputs = tokenizer(text, return_tensors="pt")
logits = model(**inputs).logits

masked_index = inputs["input_ids"][0].tolist().index(tokenizer.mask_token_id)
print(tokenizer.decode(logits[0, masked_index].argmax(-1)))
```

Using a `pipeline`:

```python
from transformers import pipeline

fill = pipeline("fill-mask", model="doctolib-lab/doctobert-fr-base")
print(fill(f"Le patient souffre d'une {fill.tokenizer.mask_token} aiguë."))
```

### Fine-tuning

DoctoBERT fine-tunes like any BERT/RoBERTa encoder, with the appropriate task head or framework:

- For **sequence classification**, load it with `AutoModelForSequenceClassification` (see the [text-classification guide](https://huggingface.co/docs/transformers/tasks/sequence_classification)).
- For **token classification (NER)**, use `AutoModelForTokenClassification` (see the [token-classification guide](https://huggingface.co/docs/transformers/tasks/token_classification)).
- For **embeddings / retrieval**, use [Sentence Transformers](https://www.sbert.net/) or [PyLate](https://github.com/lightonai/pylate).

## 📐 Model Overview

| Property | Value |
| --- | --- |
| Architecture | RoBERTa |
| Parameters | 111M total (85M backbone, 26M embeddings) |
| Layers | 12 |
| Hidden size | 768 |
| Attention heads | 12 |
| MLP | GELU |
| Intermediate size | 3072 |
| Context window | 512 tokens |
| Vocabulary size | 32,768 |
| Language | French |

## 🔧 Training

The tokenizer is a SentencePiece BPE model of 32,768 tokens, trained on the entity-rich FineMed-filtered subset (educational quality >= 4 and medical-term density >= 0.1) for efficient tokenization of dense medical vocabulary. It splits digits into single tokens and uses byte fallback for unseen characters.

DoctoBERT is pretrained from scratch over two phases on a mix of FineMed-filtered (FineMed-fr under the same educational-quality and medical-term-density filter) and FineMed-rephrased-fr:

1. **Pretraining (500B tokens).** Masked-language-modeling on the full mix (long documents are hierarchically chunked to fit the context window rather than truncated), building broad medical-language representations.
2. **Annealing (200B tokens).** Continued training on the biomedical & clinical subdomains of the mix, focusing the final updates on content closest to downstream medical use.

## 📊 Evaluation

Across 11 encoders from English medical, French generalist, and French medical families, DoctoBERT-fr-base achieves the best DrBenchmark aggregate scores, leading five of seven tasks. On the real-world clinical NER task, scores cluster tightly and its long-context sibling DoctoModernBERT-fr-base achieves the best F1.

### DrBenchmark

We adapted the [DrBenchmark](https://github.com/doctolib-lab/DrBenchmark), filtered to 7 high-quality tasks: QUAERO (NER on EMEA drug leaflets and MEDLINE abstracts), E3C (clinical and temporal NER), DEFT-2021 (clinical NER), MorFITT (biomedical specialty classification), and DiaMed (clinical diagnostic classification). Per model and task, hyperparameters are tuned on the validation split, then the mean F1 over 5 test-split seeds is reported. We also report two per-model scores aggregated across all tasks: **Min-Max** rescales each task's scores onto a 0–100 scale before averaging, capturing the magnitude of the gaps (a model that lags on a few tasks is penalized heavily); **WP** (Win Probability) is the average percentage of tasks on which a model outscores each other model, capturing rank consistency (robust to outliers but blind to effect size).

<table>
<thead>
<tr><th align="left">Model</th><th align="right">EMEA</th><th align="right">MEDLINE</th><th align="right">E3C-Clin</th><th align="right">E3C-Temp</th><th align="right">MORFITT</th><th align="right">DEFT2021</th><th align="right">DIAMED</th><th align="right">Min-Max</th><th align="right">WP</th></tr>
</thead>
<tbody>
<tr><td colspan="10"><em>English medical</em></td></tr>
<tr><td align="left">BioBERT</td><td align="right">58.77</td><td align="right">50.29</td><td align="right">55.02</td><td align="right">78.29</td><td align="right">66.99</td><td align="right">56.72</td><td align="right">59.26</td><td align="right">29.97</td><td align="right">15.71</td></tr>
<tr><td align="left">BioClinical-ModernBERT</td><td align="right">44.74</td><td align="right">44.44</td><td align="right">49.53</td><td align="right">76.11</td><td align="right">67.42</td><td align="right">53.97</td><td align="right">52.07</td><td align="right">0.88</td><td align="right">1.43</td></tr>
<tr><td align="left">ModernBERT-bio</td><td align="right">56.84</td><td align="right">46.60</td><td align="right">53.76</td><td align="right">78.85</td><td align="right">68.57</td><td align="right">56.43</td><td align="right">61.06</td><td align="right">29.35</td><td align="right">17.14</td></tr>
<tr><td colspan="10"><em>French generalist</em></td></tr>
<tr><td align="left">CamemBERT</td><td align="right">65.43</td><td align="right">56.18</td><td align="right">59.82</td><td align="right">83.81</td><td align="right">71.54</td><td align="right">62.40</td><td align="right">60.26</td><td align="right">69.37</td><td align="right">57.14</td></tr>
<tr><td align="left">ModernCamemBERT</td><td align="right">61.98</td><td align="right">55.46</td><td align="right">57.62</td><td align="right">83.11</td><td align="right">70.01</td><td align="right">60.01</td><td align="right">53.26</td><td align="right">52.69</td><td align="right">28.57</td></tr>
<tr><td colspan="10"><em>French medical</em></td></tr>
<tr><td align="left">DrBERT</td><td align="right">64.37</td><td align="right">57.18</td><td align="right">58.01</td><td align="right">82.44</td><td align="right">70.42</td><td align="right">61.08</td><td align="right">64.87</td><td align="right">65.08</td><td align="right">44.29</td></tr>
<tr><td align="left">CamemBERT-bio</td><td align="right">64.98</td><td align="right">59.03</td><td align="right">61.40</td><td align="right"><b>84.88</b></td><td align="right">71.48</td><td align="right">64.73</td><td align="right">64.63</td><td align="right">80.83</td><td align="right">70.00</td></tr>
<tr><td align="left">TransBERT-bio-fr</td><td align="right">67.37</td><td align="right">59.96</td><td align="right">62.36</td><td align="right">84.48</td><td align="right"><b>74.04</b></td><td align="right">65.48</td><td align="right">70.91</td><td align="right">93.88</td><td align="right">88.57</td></tr>
<tr><td align="left">ModernCamemBERT-bio</td><td align="right">65.35</td><td align="right">56.81</td><td align="right">58.63</td><td align="right">83.31</td><td align="right">71.21</td><td align="right">61.35</td><td align="right">67.77</td><td align="right">71.37</td><td align="right">54.29</td></tr>
<tr><td colspan="10"><em>Ours</em></td></tr>
<tr><td align="left"><b>DoctoBERT-fr</b></td><td align="right"><b>68.39</b></td><td align="right"><b>62.54</b></td><td align="right"><b>62.75</b></td><td align="right">84.60</td><td align="right">73.36</td><td align="right"><b>66.41</b></td><td align="right"><b>72.56</b></td><td align="right"><b>98.17</b></td><td align="right"><b>97.14</b></td></tr>
<tr><td align="left"><b>DoctoModernBERT-fr</b></td><td align="right">65.71</td><td align="right">59.65</td><td align="right">59.62</td><td align="right">84.06</td><td align="right">71.87</td><td align="right">63.81</td><td align="right">71.60</td><td align="right">83.15</td><td align="right">75.71</td></tr>
</tbody>
</table>

### Real-world Clinical NER

A proprietary French clinical NER task from a real-world production setting, annotated with 12 entity types (e.g., pathology, drug, exam, biometry) and 9 qualifiers (e.g., negation, family relationship, date). Scores are the mean over 3 test-split seeds.

<table>
<thead>
<tr><th align="left">Model</th><th align="right">Precision</th><th align="right">Recall</th><th align="right">F1</th></tr>
</thead>
<tbody>
<tr><td colspan="4"><em>English medical</em></td></tr>
<tr><td align="left">BioBERT</td><td align="right">77.54</td><td align="right">78.42</td><td align="right">77.97</td></tr>
<tr><td align="left">BioClinical-ModernBERT</td><td align="right">78.79</td><td align="right">78.69</td><td align="right">78.74</td></tr>
<tr><td align="left">ModernBERT-bio</td><td align="right">78.06</td><td align="right">79.30</td><td align="right">78.67</td></tr>
<tr><td colspan="4"><em>French generalist</em></td></tr>
<tr><td align="left">CamemBERT</td><td align="right">77.19</td><td align="right">79.58</td><td align="right">78.36</td></tr>
<tr><td align="left">ModernCamemBERT</td><td align="right">78.53</td><td align="right">78.71</td><td align="right">78.62</td></tr>
<tr><td colspan="4"><em>French medical</em></td></tr>
<tr><td align="left">DrBERT</td><td align="right">76.77</td><td align="right">77.81</td><td align="right">77.28</td></tr>
<tr><td align="left">CamemBERT-bio</td><td align="right">77.51</td><td align="right">78.90</td><td align="right">78.19</td></tr>
<tr><td align="left">TransBERT-bio-fr</td><td align="right">76.85</td><td align="right">78.66</td><td align="right">77.74</td></tr>
<tr><td align="left">ModernCamemBERT-bio</td><td align="right">78.17</td><td align="right"><b>79.76</b></td><td align="right">78.95</td></tr>
<tr><td colspan="4"><em>Ours</em></td></tr>
<tr><td align="left"><b>DoctoBERT-fr</b></td><td align="right">77.29</td><td align="right">79.68</td><td align="right">78.47</td></tr>
<tr><td align="left"><b>DoctoModernBERT-fr</b></td><td align="right"><b>79.12</b></td><td align="right">79.71</td><td align="right"><b>79.40</b></td></tr>
</tbody>
</table>

## ⚠️ Intended Use & Limitations

DoctoBERT is an encoder for French biomedical and clinical NLP (NER, classification, retrieval), used by fine-tuning on a downstream task. It is not generative and not a medical device; its outputs must not drive clinical decisions. It was pretrained on public web, PDF, and encyclopedic medical text and reflects the biases and gaps of those sources.

<!--
## 📖 Citation

```bibtex
@misc{doctobert2026,
  title         = {Where Does the Signal Live? A Web Data Recipe for Medical Encoder Pretraining},
  author        = {Huang, Bofeng and Sun, Jacques and Bouchacourt, Diane and Barascud, Nicolas and Fogel, Fajwel},
  year          = {2026},
  eprint        = {2606.XXXXX},
  archivePrefix = {arXiv},
  primaryClass  = {cs.CL}
}
```
-->

## ⚖️ License

Released under Apache-2.0. DoctoBERT was trained on FineMed-fr and FineMed-rephrased-fr, which derive from FineWeb-2 / FinePDFs (ODC-BY 1.0) and FineWiki (CC BY-SA 4.0); please attribute those upstream sources.

## 🏛️ Acknowledgments

This work was granted access to the HPC resources of IDRIS (Jean Zay) under the allocations 2025-AD011016291 and 2026-A0200617487 made by GENCI.
