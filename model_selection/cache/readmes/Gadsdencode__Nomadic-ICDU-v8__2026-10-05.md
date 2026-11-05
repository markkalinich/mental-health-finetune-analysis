---
license: mit
base_model: mistralai/Mistral-7B-Instruct-v0.3
base_model_relation: finetune
pipeline_tag: text-generation
library_name: transformers
language:
  - en
tags:
  - mistral
  - icdu
  - instruction-tuning
  - conversational
  - text-generation
  - gguf
---

# Nomadic-ICDU-v8

Nomadic-ICDU-v8 is a 7.25B-parameter, instruction-tuned language model derived from
[Mistral-7B-Instruct-v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3).
It is designed to demonstrate the ICDU approach: representing a task as an explicit,
testable unit of intent so that a model can be tuned and evaluated against the
purpose, principles, constraints, decision rules, and expected behavior of a specific
workflow.

The repository contains a merged FP16 Transformers checkpoint and GGUF exports for
local inference.

> **Disclosure status:** The base model, architecture, context-window declaration,
> checkpoint formats, and prompt template are verifiable from the published files.
> The public repository does not yet include a reproducible v8 training manifest,
> dataset manifest, or benchmark report. Where those records are unavailable, this
> card says so explicitly and does not infer or invent details.

## Model details

| Field | Value |
|---|---|
| Model | `Gadsdencode/Nomadic-ICDU-v8` |
| Model type | Decoder-only causal language model |
| Architecture | `MistralForCausalLM` |
| Parameters | 7,248,023,552 |
| Base model | `mistralai/Mistral-7B-Instruct-v0.3` |
| Layers / hidden size | 32 / 4,096 |
| Attention heads / KV heads | 32 / 8 |
| Vocabulary | 32,768 tokens |
| Declared maximum positions | 32,768 tokens |
| Published precision | FP16 |
| Published local formats | GGUF F16 and GGUF Q4_K_M |
| Primary language | English |
| Repository license declaration | MIT |
| Public checkpoint commit | `a328cf13db7a10a200cf616c2f35a0035a6b637c` |
| Repository last updated | 2025-08-28 |

Users are responsible for reviewing the upstream base-model terms, the repository
license, and any obligations that apply to their deployment or data.

## What ICDU-v8 was trained to do

ICDU-v8 is intended to improve task-specific behavior by making the operating
contract of a workflow explicit. Depending on the ICDU used for a task, that contract
can include:

- the user's or organization's intent;
- governing principles and priorities;
- role, audience, tone, and communication requirements;
- domain context and input structure;
- constraints, boundaries, and prohibited actions;
- decision, escalation, and uncertainty-handling rules; and
- examples of preferred and non-preferred behavior.

The intended result is a model that follows a defined operating envelope more
consistently than a generic instruction model, including when a request is
paraphrased, partially specified, or placed under conflicting pressure.

This is an intended capability, not a guarantee. Users should measure it on their own
ICDUs, inputs, failure modes, and deployment conditions.

## Base model and training method

The checkpoint configuration identifies
`mistralai/Mistral-7B-Instruct-v0.3` as the base model. The published repository is a
merged inference checkpoint, not a standalone adapter.

ICDU project documentation describes the following training and release methodology:

1. Convert the target workflow into structured ICDU training records.
2. Perform supervised fine-tuning with QLoRA.
3. Apply preference tuning, including DPO, where preferred and rejected responses are
   available.
4. Stress-test behavior with perturbations to role, tone, constraints, inputs, and
   channel.
5. Evaluate against task-specific gates using an AI Judge and, where appropriate,
   human-in-the-loop grading.
6. Release only after the model satisfies the selected operating thresholds.

The public v8 repository does **not** currently include the run configuration needed
to prove which of these stages, hyperparameters, adapter settings, random seeds,
checkpoints, or release gates were used for this exact build. Accordingly, the
sequence above documents the ICDU project method rather than a reproducible v8
training log.

## Training data

ICDU training records are designed to encode task intent and expected behavior rather
than rely only on broad, unstructured instruction examples. A record may contain:

- an intent or objective;
- principles and prioritization rules;
- persona, audience, tone, or channel requirements;
- relevant context and constraints;
- task inputs;
- an expected or preferred response;
- a rejected response or failure example for preference tuning; and
- escalation or abstention behavior.

### Data disclosure and exclusions

The following v8-specific information is not present in the public repository:

| Disclosure item | Public status |
|---|---|
| Number of training, validation, and test examples | Not published |
| Dataset names and source provenance | Not published |
| Human-authored versus synthetic-data composition | Not published |
| Domain and language distribution | Not published |
| Deduplication and contamination checks | Not published |
| Copyright and license review | Not published |
| PII or sensitive-data screening | Not published |
| Explicit exclusion list | Not published |
| Preference-pair construction and review process | Not published |

No specific exclusion—such as personal data, customer data, copyrighted material,
medical records, security-sensitive data, or benchmark test sets—should be assumed
without a training-data manifest. Deployments that require documented provenance,
consent, data residency, or regulated-data controls should not rely on this checkpoint
until the relevant records have been reviewed.

## Required prompt and chat format

Use the tokenizer's bundled Mistral chat template whenever possible. Messages must
alternate between `user` and `assistant`; an optional `system` message may appear
first.

### Transformers chat template

```python
from transformers import AutoTokenizer

model_id = "Gadsdencode/Nomadic-ICDU-v8"
tokenizer = AutoTokenizer.from_pretrained(model_id)

messages = [
    {
        "role": "system",
        "content": (
            "Follow the supplied ICDU. Respect its intent, principles, "
            "constraints, and escalation rules."
        ),
    },
    {
        "role": "user",
        "content": "Summarize the case and identify any required escalation.",
    },
]

prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)
print(prompt)
```

### Raw single-turn format

```text
<s>[INST] {optional system instruction}

{user message} [/INST]
```

### Raw multi-turn format

```text
<s>[INST] {system instruction}

{first user message} [/INST] {first assistant response}</s>[INST] {next user message} [/INST]
```

Do not substitute an unrelated chat template. Prompt-template mismatches can cause
lower-quality responses, leaked control tokens, or unstable turn-taking.

The tokenizer also contains formatting for tool calls and tool results. The presence
of those tags does not establish reliable tool selection, argument generation, or
safe autonomous tool use; evaluate tool behavior separately before enabling it.

## Intended uses

Appropriate uses include:

- research and evaluation of ICDU-based task specialization;
- local or private task-specific assistants;
- workflow prototypes with explicit intent, constraints, and escalation rules;
- drafting, classification, summarization, and decision support within a tested
  operating envelope;
- policy-sensitive or regulated-workflow support with qualified human review;
- perturbation testing and comparison against a base instruction model; and
- creating organization- or domain-specific derivatives using authorized data.

The model is best treated as a component inside a governed workflow, not as an
independent authority.

## Prohibited uses

Do not use ICDU-v8 for:

- autonomous medical, legal, financial, employment, insurance, credit, housing, or
  other high-impact decisions;
- emergency response or safety-critical control without qualified human authority;
- unsupervised actions that can spend money, modify production systems, disclose
  data, or create irreversible effects;
- unlawful surveillance, discrimination, impersonation, fraud, deception, or
  harassment;
- generation or operational assistance for weapons, malware, credential theft, or
  other harmful activity;
- processing secrets, credentials, personal data, or regulated records without
  appropriate authorization and technical controls; or
- representing model output as guaranteed accurate, compliant, unbiased, or
  professionally approved.

These use restrictions state the maintainer's intended operating policy. They do not
replace applicable law, professional obligations, or license terms.

## Known limitations

- **No published v8 benchmark report.** Task-fit and safety claims have not yet been
  substantiated by reproducible public results.
- **Incomplete training-data disclosure.** Dataset scale, sources, composition,
  contamination testing, and exclusions are not currently documented.
- **Hallucinations.** The model can produce fluent but false, unsupported, or
  internally inconsistent content.
- **Prompt sensitivity.** Small changes in instructions, chat formatting, context
  order, or generation settings can change behavior.
- **Base-model limits.** This is a 7B-class model and should not be expected to match
  larger frontier systems on broad knowledge, complex reasoning, coding, or
  multilingual tasks.
- **Language coverage.** English is the declared primary language. Quality in other
  languages has not been documented.
- **Long-context behavior is unverified.** The configuration declares 32,768
  positions, but effective recall and instruction adherence at that length have not
  been publicly measured for v8.
- **Tool use is unverified.** Tool-format support in the tokenizer is not proof of
  correct or safe function calling.
- **Quantization effects.** GGUF Q4_K_M is smaller and easier to run locally, but may
  differ from the FP16 checkpoint in accuracy, formatting, and consistency.
- **No inherent data or action controls.** Authentication, authorization, redaction,
  retrieval permissions, audit logging, and action approval must be provided by the
  surrounding application.

## Benchmark results

No verified, reproducible benchmark scores for Nomadic-ICDU-v8 are currently
published. A blank or estimated score would be misleading, so this release does not
claim one.

The recommended ICDU evaluation suite is:

| Evaluation | What it measures | v8 public result |
|---|---|---|
| Intent alignment | Completion of the task's explicit objective | Not published |
| Principle adherence | Compliance with stated priorities and rules | Not published |
| Application / groundedness | Correct use of supplied inputs and context | Not published |
| Constraint adherence | Compliance with required and prohibited behavior | Not published |
| Escalation accuracy | Correct abstention or escalation when a boundary is reached | Not published |
| Perturbation stability | Consistency under paraphrase, tone, role, and context changes | Not published |
| Preference win rate | Blind comparison against the base model and earlier versions | Not published |
| Human acceptance rate | Qualified reviewer acceptance on target workflows | Not published |
| Safety regression rate | Rate of newly introduced prohibited behavior | Not published |
| Latency and throughput | Runtime performance by engine, hardware, and context length | Not published |

For a credible release result, publish the evaluation dataset or a representative,
non-sensitive sample; scoring rubric; judge prompts; human-review procedure; sample
sizes; confidence intervals; base-model comparison; inference settings; and exact
checkpoint hash.

## Recommended generation settings

Start with deterministic decoding for governed or repeatable workflows:

| Setting | Governed/default | Exploratory drafting |
|---|---:|---:|
| `do_sample` | `false` | `true` |
| `temperature` | Omit when sampling is disabled | `0.4`–`0.7` |
| `top_p` | Omit when sampling is disabled | `0.90`–`0.95` |
| `max_new_tokens` | `256`–`512` | `512`–`1,024` |
| `repetition_penalty` | `1.05` | `1.05` |
| Stop token | `</s>` / tokenizer EOS | `</s>` / tokenizer EOS |

Example:

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_id = "Gadsdencode/Nomadic-ICDU-v8"
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto",
)

messages = [
    {"role": "system", "content": "Follow the supplied ICDU and its escalation rules."},
    {"role": "user", "content": "Review this input and return the required action."},
]
inputs = tokenizer.apply_chat_template(
    messages,
    add_generation_prompt=True,
    return_tensors="pt",
).to(model.device)

outputs = model.generate(
    inputs,
    do_sample=False,
    max_new_tokens=512,
    repetition_penalty=1.05,
    eos_token_id=tokenizer.eos_token_id,
)

new_tokens = outputs[0, inputs.shape[-1]:]
print(tokenizer.decode(new_tokens, skip_special_tokens=True))
```

Generation settings should be selected against the target evaluation suite. Lower
temperature improves repeatability but does not guarantee correctness or policy
compliance.

## Context-length guidance

The model configuration declares a 32,768-token maximum position length. That is an
architectural limit, not a promise that all 32K-token prompts will be recalled or
followed equally well.

| Use case | Recommended starting context |
|---|---:|
| Local Q4 testing | 8,192 tokens |
| Typical hosted workflow | 8,192–16,384 tokens |
| Long-document evaluation | 16,384–32,768 tokens |
| Production at 32K | Only after task-specific recall and adherence tests |

Increasing context length raises KV-cache memory use, latency, and cost and can reduce
concurrency. Prefer retrieving the smallest relevant context, placing the ICDU and
critical constraints clearly, and testing required facts near the beginning, middle,
and end of long prompts.

If a local application reports an 8,192-token limit, that is usually its runtime
configuration rather than a different model architecture. Increase the runtime
setting only if the available RAM or VRAM and evaluation results support it.

## Local use with LM Studio

1. In LM Studio, search for `Gadsdencode/Nomadic-ICDU-v8`.
2. Download `nomadic-icdu-v8-Q4_K_M.gguf` for the practical local build. Use the F16
   GGUF only when the additional memory requirement is acceptable.
3. Load the model and leave the prompt template on **Auto** or select the Mistral
   Instruct template.
4. Start with an 8,192-token context. Move to 16,384 or 32,768 only after checking
   memory use and long-context behavior.
5. For deterministic workflows, disable sampling or set temperature to the lowest
   supported value.
6. To expose a local API, start LM Studio's OpenAI-compatible server. The default is
   commonly `http://127.0.0.1:1234/v1`.

Check the model identifier returned by `GET /v1/models`, then use it in the request:

```bash
curl http://127.0.0.1:1234/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "replace-with-the-id-from-v1-models",
    "messages": [
      {
        "role": "system",
        "content": "Follow the supplied ICDU and its escalation rules."
      },
      {
        "role": "user",
        "content": "Review this input and return the required action."
      }
    ],
    "temperature": 0,
    "max_tokens": 512
  }'
```

## Local use with Ollama

Download the Q4_K_M GGUF:

```bash
hf download Gadsdencode/Nomadic-ICDU-v8 \
  nomadic-icdu-v8-Q4_K_M.gguf \
  --local-dir ./nomadic-icdu-v8
```

Create `nomadic-icdu-v8/Modelfile`:

```text
FROM ./nomadic-icdu-v8-Q4_K_M.gguf

PARAMETER num_ctx 8192
PARAMETER num_predict 512
PARAMETER temperature 0
PARAMETER top_p 0.9
PARAMETER repeat_penalty 1.05
PARAMETER stop "</s>"
```

Create and run the local model:

```bash
cd nomadic-icdu-v8
ollama create nomadic-icdu-v8 -f Modelfile
ollama run nomadic-icdu-v8
```

Ollama should read the chat-template metadata embedded in the GGUF. Confirm during
acceptance testing that prompts render with Mistral `[INST] ... [/INST]` formatting.

Ollama API example:

```bash
curl http://localhost:11434/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "model": "nomadic-icdu-v8",
    "stream": false,
    "messages": [
      {
        "role": "system",
        "content": "Follow the supplied ICDU and its escalation rules."
      },
      {
        "role": "user",
        "content": "Review this input and return the required action."
      }
    ],
    "options": {
      "temperature": 0,
      "num_ctx": 8192,
      "num_predict": 512
    }
  }'
```

## Hosted API example

For a hosted deployment, use the FP16 Safetensors checkpoint with an inference engine
that honors the tokenizer chat template. An OpenAI-compatible API makes it easier to
move between a hosted endpoint, LM Studio, and other serving systems.

Set:

```bash
export ICDU_API_BASE_URL="https://your-endpoint.example.com/v1"
export ICDU_API_KEY="replace-with-your-endpoint-token"
```

Python:

```python
import os
from openai import OpenAI

client = OpenAI(
    base_url=os.environ["ICDU_API_BASE_URL"],
    api_key=os.environ["ICDU_API_KEY"],
)

response = client.chat.completions.create(
    model="Gadsdencode/Nomadic-ICDU-v8",
    messages=[
        {
            "role": "system",
            "content": "Follow the supplied ICDU and its escalation rules.",
        },
        {
            "role": "user",
            "content": "Review this input and return the required action.",
        },
    ],
    temperature=0,
    max_tokens=512,
)

print(response.choices[0].message.content)
```

Endpoint operators should add authentication, request-size limits, timeouts,
structured logging with sensitive-data controls, rate limits, abuse monitoring, and
human approval around consequential actions. Do not log raw prompts or completions by
default when they may contain confidential data.

## Model and version lineage

```text
mistralai/Mistral-7B-Instruct-v0.3
└── Nomadic-ICDU-v8 merged FP16 checkpoint
    ├── Transformers Safetensors (3 shards)
    ├── GGUF F16
    └── GGUF Q4_K_M
```

`v8` is the project's release label for this checkpoint. Public artifacts describing
v1 through v7, their training changes, and their comparative evaluations are not
included in this repository, so no undocumented lineage claims are made here.

For reproducibility, downstream derivatives should record:

- the exact source revision or checkpoint hash;
- the ICDU and dataset manifest version;
- training code and dependency revisions;
- training and preference-tuning hyperparameters;
- random seeds;
- evaluation-suite version and release thresholds;
- quantization tool, version, and parameters; and
- any changes to the prompt template or context configuration.

## Citation

If you use this model, cite the model repository and the exact revision:

```bibtex
@misc{nomadic_icdu_v8,
  title        = {Nomadic-ICDU-v8},
  author       = {{Gadsdencode}},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/Gadsdencode/Nomadic-ICDU-v8}},
  note         = {Revision a328cf13db7a10a200cf616c2f35a0035a6b637c}
}
```

## Additional information

- Model repository: <https://huggingface.co/Gadsdencode/Nomadic-ICDU-v8>
- Base model: <https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3>

The bundled `handler.py` should be reviewed before production use. In particular,
verify that it loads the correct model ID, applies the tokenizer's chat template,
does not expose exception details to end users, and does not print sensitive prompts
or completions.
