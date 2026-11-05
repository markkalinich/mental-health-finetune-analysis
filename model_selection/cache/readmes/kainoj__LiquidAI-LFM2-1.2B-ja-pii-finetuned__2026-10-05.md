---
library_name: transformers
tags:
- trl
- sft
datasets:
- stockmark/ner-wikipedia-dataset
language:
- ja
base_model:
- LiquidAI/LFM2-1.2B
---

[LiquidAI/LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B) finetuned on Japanese content to output JSON with PII. The model should output only single json with four fields:

```json
{
    "full_name": "name of the person",
    "company_name": "name of the company",
    "address": "address of the plance",
    "phone_number": "phone number"
}
```

Coded during Liquid AI hackathon in Tokyo.


# Evaluations
Evaluation on test split of [stockmark/ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset):
* Test accuracy on **raw model** using wiki dataset: `0.4250` --> `1.0` **after fine-tunning**.


That dataset is somehow simple. We generated 64 samples of long contracts containing PII in Japanese. We used it only to evaluate the final perfomrance of the models
* Test accuracy on **raw model** using OUR dataset: `0.0312` --> `1.0` **after fine-tunning**.


### Evaluation methodology
We use an exact match on generated JSON. The output of SLM must be a valid JSON with exactly four required fields, no less, no more.



# Model Details

- **Developed by:** [@kainoj](https://github.com/kainoj), [@valeriosalvucci](https://github.com/valeriosalvucci) and [@gangadhara691](https://github.com/gangadhara691)
- **Language(s) (NLP):** Japanese
- **License:** `lfm1.0`
- **Finetuned from model:** [LiquidAI/LFM2-1.2B](https://huggingface.co/LiquidAI/LFM2-1.2B)
- **Finetued on dataset**: [stockmark/ner-wikipedia-dataset](https://huggingface.co/datasets/stockmark/ner-wikipedia-dataset)


## System prompt
Use the following system prompt while extracting PIIs:
```
Identify and extract information matching the following schema.
Return data as a JSON object. 
For each field, select most suitable value from text
If provided text does not contain sufficient information to fill out the field, make the field empty string.
Output only JSON, and output only four fields. 

{
    "full_name": "name of the person",
    "company_name": "name of the company",
    "address": "address of the plance",
    "phone_number": "phone number"
}
```
