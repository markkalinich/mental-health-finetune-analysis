---
base_model: Qwen/Qwen2.5-1.5B-Instruct
library_name: transformers
license: apache-2.0
pipeline_tag: text-generation
tags:
- pii
- pii-redaction
- privacy
- redaction
- qwen2.5
- text-generation
- fine-tuning
- lora
- unsloth
---

# Qwen2.5-1.5B PII Redactor

A fine-tuned **Qwen2.5-1.5B-Instruct** model for identifying and
redacting personally identifiable information (PII) from text.

The model was fine-tuned as a text-generation redaction system: given
raw text, it preserves the non-PII content and replaces detected PII
spans with typed redaction tags.

## Model Overview

  Property                Value
  ----------------------- ----------------------------------
  Base model              `Qwen/Qwen2.5-1.5B-Instruct`
  Task                    PII detection and text redaction
  Training method         Supervised fine-tuning with LoRA
  Fine-tuning framework   Unsloth + TRL + PEFT
  Dataset                 `ai4privacy/pii-masking-300k`
  Sequence length         512 tokens
  LoRA rank               16
  LoRA alpha              16
  LoRA dropout            0.05
  Learning rate           `2e-4`
  Epochs                  2
  Per-device batch size   4
  Gradient accumulation   4
  Effective batch size    16
  Optimizer               `adamw_8bit`
  Evaluation split        10%
  Random seed             42

## What the Model Does

The model receives ordinary text such as:

``` text
Hi, my name is John Smith and you can reach me at john@example.com.
```

and produces redacted text such as:

``` text
Hi, my name is [GIVENNAME1] [LASTNAME1] and you can reach me at [EMAIL].
```

The exact tag vocabulary is learned from the training data. Examples
observed during the notebook sanity check include:

-   `[GIVENNAME1]`
-   `[LASTNAME1]`
-   `[EMAIL]`
-   `[TEL]`
-   `[BUILDING]`
-   `[STREET]`
-   `[CITY]`
-   `[SOCIALNUMBER]`

Do not assume that every PII category uses the same tag spelling. The
model follows the conventions present in its training data.

## Training Data

The notebook uses:

``` text
ai4privacy/pii-masking-300k
```

Each example contains a source text and a target text in which PII spans
have been replaced by redaction labels.

For the recorded training run, 50,000 dataset rows were selected:

-   45,000 examples initially formed the training split.
-   5,000 examples formed the evaluation split.
-   Unsloth removed 916 training examples because the response marker
    was missing after tokenization/truncation.
-   The actual training run therefore used 44,084 examples.

The dataset split uses seed `42`.

## Training Approach

### 1. Quantized base model

The base model is loaded through Unsloth with 4-bit loading:

``` python
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name="Qwen/Qwen2.5-1.5B-Instruct",
    max_seq_length=512,
    dtype=None,
    load_in_4bit=True,
)
```

This reduces memory requirements during fine-tuning.

### 2. LoRA fine-tuning

Instead of updating the full model, LoRA adapters are attached to the
attention and MLP projection layers:

``` python
r=16
lora_alpha=16
lora_dropout=0.05

target_modules=[
    "q_proj", "k_proj", "v_proj", "o_proj",
    "gate_proj", "up_proj", "down_proj",
]
```

The notebook reported approximately **18.46 million trainable
parameters**.

### 3. Chat-format training

Each dataset example is converted into a Qwen chat conversation
containing:

1.  A system instruction describing the redaction task.
2.  The original text as the user message.
3.  The redacted text as the assistant response.

The tokenizer's Qwen chat template is used to construct the final
training sequence.

### 4. Response-only loss

Training uses Unsloth's `train_on_responses_only` so that the loss is
calculated on the assistant's redacted response rather than the system
instruction and user input.

This focuses the fine-tuning signal on the actual redaction behavior.

## System Prompt

The model was trained with this system instruction:

``` text
You are a data redaction assistant. Given a piece of text, identify every span of personally identifiable information (PII) and replace it with a tag indicating its type, e.g. [FIRSTNAME_1], [EMAIL_1], [PHONENUMBER_1]. Leave all non-PII text exactly as it is. Only output the redacted text, nothing else.
```

For best results, use the same system prompt during inference.

# How to Use

## Install

``` bash
pip install torch transformers accelerate safetensors
```

If you are working with the original fine-tuning notebook, also install
the training stack:

``` bash
pip install unsloth peft trl datasets bitsandbytes huggingface_hub
```

## Transformers Inference

If this repository contains the merged Safetensors model, it can be
loaded directly with Transformers:

``` python
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_ID = "Harsh221/qwen2.5-1.5b-pii-redactor"

SYSTEM_PROMPT = (
    "You are a data redaction assistant. Given a piece of text, identify every "
    "span of personally identifiable information (PII) and replace it with a "
    "tag indicating its type, e.g. [FIRSTNAME_1], [EMAIL_1], [PHONENUMBER_1]. "
    "Leave all non-PII text exactly as it is. Only output the redacted text, "
    "nothing else."
)

tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_ID,
    device_map="auto",
    torch_dtype="auto",
)

def redact(text, max_new_tokens=256):
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": text},
    ]

    inputs = tokenizer.apply_chat_template(
        messages,
        tokenize=True,
        add_generation_prompt=True,
        return_tensors="pt",
    ).to(model.device)

    with torch.no_grad():
        output_ids = model.generate(
            input_ids=inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
        )

    new_tokens = output_ids[0][inputs.shape[1]:]
    return tokenizer.decode(
        new_tokens,
        skip_special_tokens=True,
    ).strip()

text = (
    "Hi, my name is John Smith and you can reach me at "
    "john.smith@example.com or 555-0192."
)

print(redact(text))
```

## Expected Behavior

The model should preserve ordinary text while replacing detected PII:

``` text
Hi, my name is [GIVENNAME1] [LASTNAME1] and you can reach me at [EMAIL] or [TEL].
```

The exact output tags can vary according to the entity types represented
in the training data.

## Batch Processing

For multiple documents, call `redact()` for each document and store the
returned redacted text.

For long documents, do not assume that a single generation call will
safely process arbitrarily large inputs. Chunk long documents within the
model's supported context and design a document-level merge strategy.

# Training Notebook

The repository can include the original training notebook:

``` text
PII_Redaction_SLM_Finetune_Unsloth(2).ipynb
```

The notebook is organized as follows:

1.  Environment check
2.  Library setup
3.  Optional Hugging Face authentication
4.  Configuration
5.  Load Qwen2.5-1.5B-Instruct
6.  Add LoRA adapters
7.  Load `ai4privacy/pii-masking-300k`
8.  Convert examples to Qwen chat format
9.  Apply response-only loss
10. Configure SFT training
11. Build the trainer
12. Train with checkpoint/resume support
13. Run inference sanity checks
14. Run a regex-based PII leak sanity check
15. Save/export the model
16. Optional Hugging Face Hub upload
17. Deployment guidance

## Training Configuration

The recorded run used:

``` text
Dataset rows selected: 50,000
Train split:           45,000
Eval split:             5,000
Actual training rows:  44,084
Epochs:                 2
Effective batch size:  16
Learning rate:          2e-4
Max sequence length:   512
Checkpoint interval:   200 optimizer steps
Evaluation interval:   200 optimizer steps
```

The trainer is configured to keep the best checkpoint according to
`eval_loss`.

## Resume Training

The notebook checks the output directory for the latest checkpoint and
calls:

``` python
trainer.train(resume_from_checkpoint=last_checkpoint)
```

If a checkpoint exists, training can resume without restarting from
zero.

# Sanity Check Results

The notebook tested two manually selected examples.

### Example 1

Input contained:

-   a person's name
-   an email address
-   a telephone number

The model produced:

``` text
Hi, my name is [GIVENNAME1] [LASTNAME1] and you can reach me at [EMAIL] or [TEL].
```

### Example 2

Input contained:

-   a building/address
-   street
-   city
-   credit-card-like number

The model produced:

``` text
Please ship the order to [BUILDING] [STREET], [CITY], and charge card [SOCIALNUMBER].
```

The notebook's regex leak check reported:

``` text
0 / 2 sample outputs had a possible PII leak.
```

These are sanity-check results, not a comprehensive benchmark. They
should not be interpreted as a production accuracy, precision, recall,
F1, or privacy guarantee.

# Export Formats

The training notebook supports three intended export paths:

### LoRA adapter

Smallest artifact. Requires the original base model plus PEFT/LoRA at
inference time.

``` text
qwen2.5-pii-redactor/
└── lora_adapter/
```

### Merged 16-bit model

LoRA weights merged into the base model. Intended for standard
Transformers-style deployment.

``` text
qwen2.5-pii-redactor/
└── merged_16bit/
```

### GGUF

Quantized export intended for runtimes such as llama.cpp or Ollama.

``` text
qwen2.5-pii-redactor/
└── gguf/
```

# Limitations

This model is a generative PII redactor, not a formal compliance or
privacy guarantee.

Important limitations:

-   The notebook's automated leak check covers only a small set of regex
    patterns.
-   Only two manually selected inference examples were used for the
    recorded sanity check.
-   `eval_loss` is a token-level training metric and does not directly
    measure PII recall or precision.
-   The model may miss PII types that are rare or poorly represented in
    the training data.
-   Generative models can occasionally modify non-PII text, produce
    unexpected tags, or hallucinate redactions.
-   Long documents should be handled with an explicit chunking and
    reconciliation strategy.
-   Production deployments should use a broader held-out evaluation set
    containing the PII categories and languages relevant to the
    application.

For high-risk privacy workflows, combine the model with deterministic
validators, regex/rule-based detectors, confidence or risk thresholds,
and human review where appropriate.

# Deployment

The notebook outlines these deployment options:

  -----------------------------------------------------------------------
  Option                              Suitable use
  ----------------------------------- -----------------------------------
  Transformers + FastAPI              Simple self-hosted API and
                                      low/moderate traffic

  Ollama + GGUF                       Local development or CPU-oriented
                                      deployment

  vLLM                                Higher-throughput production
                                      inference

  Hugging Face Inference Endpoints    Managed production deployment
  -----------------------------------------------------------------------

For a production PII-redaction API, recommended additions include:

-   request validation
-   authentication/authorization
-   rate limiting
-   structured logging without storing raw PII
-   request-size limits
-   deterministic post-generation PII scanning
-   monitoring for missed PII
-   evaluation/regression tests
-   secure handling and deletion of input/output data

# Reproducibility

The notebook uses:

``` text
Base model: Qwen/Qwen2.5-1.5B-Instruct
Dataset:    ai4privacy/pii-masking-300k
Seed:       42
Max length: 512
LoRA r:     16
LoRA alpha: 16
Dropout:    0.05
Epochs:     2
LR:         2e-4
```

The recorded environment reported:

``` text
GPU:         NVIDIA GeForce RTX 3050 Laptop GPU
GPU memory:  6 GB
Unsloth:     2026.8.21
PEFT:        0.15.2
Transformers: 4.52.4
```

# License

The base model used for fine-tuning is:

`Qwen/Qwen2.5-1.5B-Instruct`

Check the base model's license and the dataset's license/terms before
redistributing this derivative model or using it commercially.

This repository's metadata currently declares Apache-2.0; verify that
this is appropriate for your intended redistribution and the applicable
upstream terms.

# Citation

If you use this model, please cite this repository and the upstream
Qwen2.5 model.
