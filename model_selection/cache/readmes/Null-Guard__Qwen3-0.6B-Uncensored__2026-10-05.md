---
license: apache-2.0
base_model: Qwen/Qwen3-0.6B
tags:
- qwen3
- uncensored
- abliterated
- abliteration
- conversational
- text-generation-inference
language:
- en
- zh
library_name: transformers
pipeline_tag: text-generation
---

# Qwen3-0.6B-Uncensored

An **abliterated (activation-ablated) / uncensored** version of [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B), with refusal behavior removed via directional ablation of the "refusal direction" in the model's residual stream. This is **not** a fine-tune — the underlying weights and knowledge of the base model are otherwise unchanged; only the model's tendency to refuse or moralize has been suppressed.

> ⚠️ **This model has had its safety alignment deliberately reduced.** It will comply with requests that the base instruct model would normally refuse. See [Intended Use & Risks](#intended-use--risks) before deploying this anywhere.

## Model Details

| | |
|---|---|
| **Base model** | [Qwen/Qwen3-0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) |
| **Parameters** | ~0.6B |
| **Method** | Abliteration (directional ablation of refusal direction) |
| **Architecture** | Qwen3 (unchanged from base) |
| **Context length** | Inherited from base model |
| **License** | Apache 2.0 (inherited from base) |
| **Languages** | Primarily English, with multilingual capability inherited from base |
| **Quantized version** | [Null-Guard/Qwen3-0.6B-Uncensored-GGUF](https://huggingface.co/Null-Guard/Qwen3-0.6B-Uncensored-GGUF) |

## What is Abliteration?

Abliteration is a technique for suppressing refusal behavior in instruction-tuned LLMs without retraining the model. It works roughly as follows:

1. A set of harmless and harmful/refusal-triggering prompts are run through the base model.
2. The activations at each layer are compared to find a single **"refusal direction"** — the direction in activation space most associated with the model producing a refusal.
3. This direction is then **ablated (projected out)** from the model's weights at every layer, so that no matter what is written to the residual stream, the model can no longer represent "I should refuse this" as strongly.

Because this only removes a narrow behavioral direction rather than retraining the model on new data, the model's general knowledge, reasoning, and capabilities from the Qwen3-0.6B base are otherwise preserved. It is a **crude, mechanistic intervention**, not a values-aligned or safety-reviewed process — see the caveats below.

### Practical notes on behavior

- Refusals are significantly reduced across most categories of previously-blocked requests.
- The model may still occasionally hedge or produce a soft refusal on some prompts — this is common with abliteration and generally responds well to direct rephrasing.
- Because this is a small (0.6B) base model, general capability (reasoning, factual accuracy, coherence on long generations) is limited regardless of the uncensoring — this is not a large frontier model, it's a small, fast, permissive one.
- As with the base Qwen3, you can toggle "thinking mode" via the chat template / `enable_thinking` flag if the base model supports it in your `transformers` version.

## Intended Use & Risks

This model is intended for:
- Research on alignment, refusal mechanisms, and interpretability.
- Local/offline use cases where a small, fast, unrestricted assistant is wanted (e.g., creative writing, roleplay, red-teaming your own systems).
- Users who want full control over the assistant's behavior without built-in moralizing or refusals.

**This model is *not* intended for:**
- Deployment in any public-facing product without your own safety layer on top.
- Generating content involving minors in any sexual or romantic context, real-person harassment, malware, weapons synthesis, or anything illegal in your jurisdiction. Removing refusal behavior does not remove your legal or ethical responsibility for what you do with the output.
- Use by minors.

**Disclaimer:** Safety filtering in this model has been substantially reduced. It may generate content that is offensive, factually wrong, biased, or otherwise harmful if prompted to. You are solely responsible for how you use this model and any content it generates. The maintainers of this repository do not endorse any specific use of the model and provide it "as is," without warranty, for research and personal use.

## Usage

### Transformers

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "Null-Guard/Qwen3-0.6B-Uncensored"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype="auto",
    device_map="auto"
)

messages = [
    {"role": "user", "content": "Give me your best pizza dough recipe."}
]

text = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True,
)

model_inputs = tokenizer([text], return_tensors="pt").to(model.device)

generated_ids = model.generate(
    **model_inputs,
    max_new_tokens=512,
)

output_ids = generated_ids[0][len(model_inputs.input_ids[0]):]
response = tokenizer.decode(output_ids, skip_special_tokens=True)
print(response)
```

> Note: requires a recent version of `transformers` (`pip install -U transformers`) for Qwen3 support.

### Ollama / llama.cpp

For quantized, CPU-friendly inference (GGUF format), see the companion repo:
👉 [Null-Guard/Qwen3-0.6B-Uncensored-GGUF](https://huggingface.co/Null-Guard/Qwen3-0.6B-Uncensored-GGUF)

## Evaluation

*(Fill in with your own numbers — e.g. refusal rate on a harmful-prompt benchmark before/after abliteration, and general capability benchmarks like MMLU/GSM8K to show capability was preserved.)*

| Benchmark | Qwen3-0.6B (base) | Qwen3-0.6B-Uncensored |
|---|---|---|
| Refusal rate on harmful-prompt test set | — | — |
| MMLU | — | — |
| GSM8K | — | — |

## How This Model Was Made

- **Base model:** Qwen/Qwen3-0.6B
- **Method:** Directional ablation ("abliteration") of the refusal direction, computed from contrastive harmful/harmless prompt pairs.
- **Tooling:** *(e.g. `transformer_lens` / `remove-refusals-with-transformers` / your own script — fill in what you used)*
- **No additional fine-tuning, DPO, or RLHF was performed** *(edit this line if you also fine-tuned on top of the ablation)*.

## Credits

- Base model: [Qwen team](https://huggingface.co/Qwen) — Qwen3-0.6B, licensed under Apache 2.0.
- Abliteration technique based on the "refusal direction" research popularized by community work such as `failspy/abliterator` and `huihui-ai`'s abliterated model series.

## License

This model inherits the **Apache 2.0** license from Qwen3-0.6B. See the base model's license for full terms. You are responsible for complying with applicable law in how you use and redistribute outputs.