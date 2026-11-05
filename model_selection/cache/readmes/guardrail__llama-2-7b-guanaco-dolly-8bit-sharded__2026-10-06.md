---
license: apache-2.0
datasets:
- databricks/databricks-dolly-15k
- timdettmers/openassistant-guanaco
---
---

Model that is fine-tuned in 4-bit precision using QLoRA on [timdettmers/openassistant-guanaco](https://huggingface.co/datasets/timdettmers/openassistant-guanaco) and [databricks/databricks-dolly-15k](https://huggingface.co/datasets/databricks/databricks-dolly-15k). Sharded as well to be used on a free Google Colab instance. 

It can be easily imported using the `AutoModelForCausalLM` class from `transformers`:

```
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained(
          "guardrail/llama-2-7b-guanaco-dolly-8bit-sharded",
          load_in_8bit=True)
tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)

```