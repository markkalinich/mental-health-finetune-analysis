---
license: gpl-3.0
datasets:
- UMCU/DutchMedicalTextV3
language:
- nl
base_model:
- meta-llama/Llama-3.2-1B-Instruct
pipeline_tag: text-generation
tags:
- medical
---

Llama-3.2-1B-Instruct, with domain adapted pretraining (DAPT), also called Continuous Pre-training (CPT) on a generic Dutch medical corpus.

Training for  on the Dutch medical corpus, with a 256 batch size, maximally 1024 sequence length during training and a linear-cosine schedul, with 100 cycles per 
250M steps, with LRmax=1e-4 and 100K warmup steps, AdamW for optimization. 

Currently at 5.5 perplexity, could still use more training. 

Planned: on-premise continuous pre-training on Dutch clinical texts. 

To use directly for the generation of embeddings:
```python

import torch
import torch.nn.functional as F
from transformers import AutoTokenizer, AutoModel


MODEL_ID = "UMCU/MedLlama.nl"

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)

model = AutoModel.from_pretrained(
    MODEL_ID,
    torch_dtype=torch.bfloat16,
)

device = (
    "cuda" if torch.cuda.is_available()
    else "mps" if torch.backends.mps.is_available()
    else "cpu"
)

model = model.to(device)
model.eval()

if tokenizer.pad_token_id is None:
    tokenizer.pad_token = tokenizer.eos_token


def echo_embedding(
    text: str,
    max_length: int = 1024,
):
    # Tokenize the pieces separately so that we know exactly
    # which tokens belong to the second occurrence.

    prefix1 = tokenizer(
        "Rewrite the following paragraph:\n",
        add_special_tokens=False,
    )["input_ids"]

    prefix2 = tokenizer(
        "\nThe rewritten paragraph:\n",
        add_special_tokens=False,
    )["input_ids"]

    text_ids = tokenizer(
        text,
        add_special_tokens=False,
    )["input_ids"]

    bos = (
        [tokenizer.bos_token_id]
        if tokenizer.bos_token_id is not None
        else []
    )

    eos = (
        [tokenizer.eos_token_id]
        if tokenizer.eos_token_id is not None
        else []
    )

    # Text occurs twice, so calculate the maximum amount
    # that fits into the context window.
    overhead = len(bos) + len(prefix1) + len(prefix2) + len(eos)

    max_text_tokens = (max_length - overhead) // 2
    text_ids = text_ids[:max_text_tokens]

    # ------------------------------------------------
    # BOS prefix1 TEXT prefix2 TEXT EOS
    #                       ^^^^^^^^^
    #                       pool only here
    # ------------------------------------------------

    input_ids = (
        bos
        + prefix1
        + text_ids
        + prefix2
        + text_ids
        + eos
    )

    second_start = (
        len(bos)
        + len(prefix1)
        + len(text_ids)
        + len(prefix2)
    )

    second_end = second_start + len(text_ids)

    input_ids = torch.tensor(
        [input_ids],
        dtype=torch.long,
        device=device,
    )

    attention_mask = torch.ones_like(input_ids)

    with torch.inference_mode():
        outputs = model(
            input_ids=input_ids,
            attention_mask=attention_mask,
        )

    # [batch, sequence, hidden_size]
    hidden = outputs.last_hidden_state

    # Hidden states corresponding ONLY to second occurrence
    echo_tokens = hidden[:, second_start:second_end, :]

    # Mean-token pooling
    embedding = echo_tokens.mean(dim=1)

    # Usually desirable for cosine similarity / retrieval
    embedding = F.normalize(embedding, p=2, dim=-1)

    return embedding
```


To use for text-generation we note that currently the EOS/EOT is untrained due to a config error, i.e. it will repeat itself ad infinitum.

```py
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("UMCU/MedLlama.nl")
model = AutoModelForCausalLM.from_pretrained("UMCU/MedLlama.nl", torch_dtype=torch.float16)
```

If you use this model please cite with

```bibtex
@misc{vanes2026languagecorporadutchmedical,
      title={Language corpora for the Dutch medical domain}, 
      author={B. van Es},
      year={2026},
      eprint={2604.25374},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2604.25374}, 
}
```

If you use the model to generate embeddings with the above code snippet, please cite
```bibtex
@misc{springer2025repetitionimproveslanguagemodel,
      title={Repetition Improves Language Model Embeddings}, 
      author={Jacob Mitchell Springer and Suhas Kotha and Daniel Fried and Graham Neubig and Aditi Raghunathan},
      year={2025},
      eprint={2402.15449},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2402.15449}, 
}
```
