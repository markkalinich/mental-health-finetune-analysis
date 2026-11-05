---
library_name: transformers
license: other
license_name: lfm1.0
license_link: LICENSE
language:
- en
- ar
- zh
- fr
- de
- ja
- ko
- es
pipeline_tag: text-generation
tags:
- liquid
- lfm2
- edge
base_model: LiquidAI/LFM2-1.2B
---

<center>
<div style="text-align: center;">
  <img 
    src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/2b08LKpev0DNEk6DlnWkY.png" 
    alt="Liquid AI"
    style="width: 100%; max-width: 100%; height: auto; display: inline-block; margin-bottom: 0.5em; margin-top: 0.5em;"
  />
</div>
<div style="display: flex; justify-content: center; gap: 0.5em;">
<a href="https://playground.liquid.ai/"><strong>Try LFM</strong></a> • <a href="https://docs.liquid.ai/lfm/getting-started/welcome"><strong>Docs</strong></a> • <a href="https://leap.liquid.ai/"><strong>LEAP</strong></a> • <a href="https://discord.com/invite/liquid-ai"><strong>Discord</strong></a>
</div>
</center>

<br>

# LFM2-1.2B-Extract

Based on [LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B), LFM2-1.2B-Extract is designed to **extract important information from a wide variety of unstructured documents** (such as articles, transcripts, or reports) into structured outputs like JSON, XML, or YAML.

**Use cases**:

- Extracting invoice details from emails into structured JSON.
- Converting regulatory filings into XML for compliance systems.
- Transforming customer support tickets into YAML for analytics pipelines.
- Populating knowledge graphs with entities and attributes from unstructured reports.

You can find more information about other task-specific models in this [blog post](https://www.liquid.ai/blog/introducing-liquid-nanos-frontier-grade-performance-on-everyday-devices).

## 📄 Model details

**Generation parameters**: We strongly recommend using greedy decoding with a `temperature=0`.

**System prompt**: If no system prompt is provided, the model will default to JSON outputs. We recommend providing a system prompt with a specific format (JSON, XML, or YAML) and a given schema to improve accuracy (see the following example).

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/MeSOLz1XeTtinRjrVkF7d.png)

**Supported languages**: English, Arabic, Chinese, French, German, Japanese, Korean, Portuguese, and Spanish.

**Chat template**: LFM2 uses a ChatML-like chat template as follows:

```
<|startoftext|><|im_start|>system
Return data as a JSON object with the following schema:\n[...]<|im_end|>
<|im_start|>user
Caenorhabditis elegans is a free-living transparent nematode about 1 mm in length that lives in temperate soil environments.<|im_end|>
<|im_start|>assistant
{
"species": "C. elegans",
"genus": "Caenorhabditis",
"description": "A free-living transparent nematode about 1 mm in length that lives in temperate soil environments.",
[...]{<|im_end|>
```

You can automatically apply it using the dedicated [`.apply_chat_template()`](https://huggingface.co/docs/transformers/en/chat_templating#applychattemplate) function from Hugging Face transformers.

> [!WARNING]
> ⚠️ The model is intended for single-turn conversations.

The data used for training these models was primarily synthetic, which allowed us to ensure a diverse data mix. We used a range of document types, domains, styles, lengths, and languages. We also varied the density and distribution of relevant text in the documents. In some cases, the extracted information was clustered in one part of the document; in others, it’s spread throughout. We applied the same approach of ensuring diversity when creating synthetic user requests and designing the structure of the model outputs. The data generation process underwent many iterations, incorporating ideas and feedback from across the Liquid AI team.

## 📈 Performance

We evaluated LFM2-Extract on a dataset of 5,000 documents, covering over 100 topics with a mix of writing styles, ambiguities, and formats. We used a combination of five metrics to capture a balanced view on syntax, accuracy, and faithfulness:

- **Syntax score**: Checks whether outputs parse cleanly as valid JSON, XML, or YAML.
- **Format accuracy**: Verifies that outputs match the requested format (e.g., JSON when JSON is requested).
- **Keyword faithfulness**: Measures whether values in the structured output actually appear in the input text.
- **Absolute scoring**: A judge LLM scores quality on a 1-5 scale, assessing completeness and correctness of extractions.
- **Relative scoring**: We ask a judge LLM to choose the best answer between the extraction model’s output and the ground-truth answer.

![image/png](https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/DNZgCKMFSg5xhHoBgJjeC.png)

LFM2-1.2B-Extract can output complex objects in different languages on a level higher than Gemma 3 27B, a model 22.5 times its size.

## 🏃 How to run

- Hugging Face: [LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B)
- llama.cpp: [LFM2-1.2B-Extract-GGUF](https://huggingface.co/LiquidAI/LFM2-1.2B-Extract-GGUF)
- LEAP: [LEAP model library](https://leap.liquid.ai/models?model=lfm2-1.2b-extract)

You can use the following Colab notebooks for easy inference and fine-tuning:

| Notebook | Description | Link |
|-------|------|------|
| Inference | Run the model with Hugging Face's transformers library. | <a href="https://colab.research.google.com/drive/1zmiCLSG3WoyoqvNBXKf2M3gAB3XlV1Uu?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (TRL) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using TRL. | <a href="https://colab.research.google.com/drive/1j5Hk_SyBb2soUsuhU0eIEA9GwLNRnElF?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| DPO (TRL) | Preference alignment with Direct Preference Optimization (DPO) using TRL. | <a href="https://colab.research.google.com/drive/1MQdsPxFHeZweGsNx4RH7Ia8lG8PiGE1t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (Axolotl) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using Axolotl. | <a href="https://colab.research.google.com/drive/155lr5-uYsOJmZfO6_QZPjbs8hA_v8S7t?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |
| SFT (Unsloth) | Supervised Fine-Tuning (SFT) notebook with a LoRA adapter using Unsloth. | <a href="https://colab.research.google.com/drive/1HROdGaPFt1tATniBcos11-doVaH7kOI3?usp=sharing"><img src="https://cdn-uploads.huggingface.co/production/uploads/61b8e2ba285851687028d395/vlOyMEjwHa_b_LXysEu2E.png" width="110" alt="Colab link"></a> |

## 📬 Contact

- Got questions or want to connect? [Join our Discord community](https://discord.com/invite/liquid-ai)
- If you are interested in custom solutions with edge deployment, please contact [our sales team](https://www.liquid.ai/contact).

## Citation

```
@article{liquidai2025lfm2,
 title={LFM2 Technical Report},
 author={Liquid AI},
 journal={arXiv preprint arXiv:2511.23404},
 year={2025}
}
```