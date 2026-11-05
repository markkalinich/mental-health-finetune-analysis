---
license: mit
pipeline_tag: text-generation
base_model: zai-org/GLM-5.3-Flash
library_name: transformers
language:
- en
tags:
- glm5_next
- glm-5.3-flash
- moe
- weight-surgery
- text-only
- experimental
---

# Ling → GLM-5.3-Flash surgery

Experimental 7.80B text checkpoint, saved with stock Transformers `save_pretrained()`.
Weight and tokenizer donor: [inclusionAI/Ling-3.0-tiny](https://huggingface.co/inclusionAI/Ling-3.0-tiny), transferred into the native GLM-5.3-Flash architecture through weight surgery.
Full donor tokenizer and untied embedding/output tables retained.

This model is intended for testing, continued training, and post-training experiments. Generation quality is unstable. Known limitations include:

- Repetition loops: generation can get stuck repeating text.
- Morphological errors: malformed word forms and incorrect inflections.
- Unintended language switching / language mixing: Chinese characters can appear unexpectedly in otherwise English output.
- Arithmetic errors, including an observed `6 × 7 → 49` response.

```python
from transformers import AutoTokenizer, Glm5NextForConditionalGeneration

repo = "imvladikon/Ling-3.0-tiny-GLM-5.3-Flash-surgery"
tokenizer = AutoTokenizer.from_pretrained(repo)
model = Glm5NextForConditionalGeneration.from_pretrained(repo)
```

Tested with Transformers 5.16.1, including ten English generations using these plain loading calls. No custom model code or `auto_map`.
Only text weights are supplied. The stock loader reports missing `model.visual.*` weights for a tiny unused vision scaffold (depth 0, width 32). Image/video inference is unsupported.
Context configured to 2048; sparse indexer selection remains untrained.

## Checkpoint layout

Tensors carry the names released GLM-5.3-Flash uses: one tensor per expert
(`mlp.experts.7.gate_proj.weight`), separate `q_conv1d` / `k_conv1d` / `v_conv1d`, and `hc_attn_fn`
rather than `attn_hc.fn` — 9510 tensors. Transformers fuses them during loading through the
`glm5_next` entry of its `conversion_mapping`, so `from_pretrained` needs nothing extra.

Those fused names are what the modules hold in memory, which means `save_pretrained()` writes the
fused form back out (688 tensors). Transformers reads that form again, but nothing else does:
Megatron-Bridge and the Megatron converters map from the released names, because the fused layout
is an implementation detail that was never published. After fine-tuning and saving this model,
rewrite the result before handing it to anything but Transformers:

```bash
python to_released_layout.py --source ./my-finetune --destination ./my-finetune-released
```

An earlier revision of this repository was published in the fused form. This one was rewritten and
checked on Transformers 5.17.0: every one of the 688 fused tensors reassembles bitwise from the
9510 released ones, the key set matches a released GLM-5.3-Flash index exactly, and English,
Russian and multi-turn prompts generate.

The following ten examples demonstrate basic English generation. Questions are abbreviated; answers are verbatim. Generation used `do_sample=False`, `max_new_tokens=40`, and `enable_thinking=False` in the chat template. These examples provide limited evidence of overall quality and generation stability.

| Question (abbreviated) | Verbatim answer |
|---|---|
| Capital of Japan? | The capital of Japan is Tokyo. |
| Largest planet? | Jupiter |
| Spider's legs? | 8 |
| Water freezing temperature, °C? | 0°C |
| Chemical symbol for oxygen? | O |
| Largest ocean? | The Pacific Ocean is the largest ocean on Earth. |
| Triangle's sides? | 3 |
| Opposite of “hot”? | Cold |
| 15 minus 6? | 9 |
| Animal known for barking? | Dog |


## Choosing the chat template: Ling (default) or Flash

The repository contains one parameterized `chat_template.jinja`. Transformers loads
it automatically with `AutoTokenizer.from_pretrained(repo)`; no custom Python helper
or separate template download is needed.

Pass `template_variant="ling"` or `template_variant="flash"` directly to
`tokenizer.apply_chat_template`. Omitting the argument selects **Ling**.

```python
from transformers import AutoTokenizer

repo = "imvladikon/Ling-3.0-tiny-GLM-5.3-Flash-surgery"
tokenizer = AutoTokenizer.from_pretrained(repo)
messages = [{"role": "user", "content": "What is the capital of France?"}]

prompt = tokenizer.apply_chat_template(
    messages,
    template_variant="ling",  # default; change to "flash" for the Flash format
    enable_thinking=False,
    add_generation_prompt=True,
    tokenize=False,
)
```

`enable_thinking=False` ends the generation prompt with `<think></think>` in both
formats; `True` (the default) leaves `<think>` open. This controls the prompt, not a
guarantee of the model's generated behavior. Optional `tools=tools` passes function
schemas. In conversation history, tool-call arguments must be dictionaries and
responses from tools must be strings. Tool execution remains the caller's responsibility.
`reasoning_effort="low"`, `"high"`, or `"max"` applies only to the Flash format.

For tokenized model inputs, use `tokenize=True, return_dict=True, return_tensors="pt"`.
If you tokenize the rendered string separately, use `add_special_tokens=False`.

### Generation stop tokens

The repository's `generation_config.json` defaults to **Ling**: EOS is
`<|endoftext|>` / `<|role_end|>`, and `<|role_end|>` is allowed to be generated.
A Jinja argument does not change the generation configuration. When selecting
**Flash**, also configure its native stop tokens and restore its suppression of
`<|role_end|>`:

```python
from transformers import GenerationConfig

flash_config = GenerationConfig.from_pretrained(repo)
flash_config.eos_token_id = tokenizer.convert_tokens_to_ids(
    ["<|endoftext|>", "<|user|>", "<|observation|>"]
)
for field in ("suppress_tokens", "begin_suppress_tokens"):
    values = getattr(flash_config, field, None)
    if values is not None:
        setattr(flash_config, field, [i for i in values if i not in flash_config.eos_token_id])
role_end_id = tokenizer.convert_tokens_to_ids("<|role_end|>")
flash_config.suppress_tokens = sorted(set(flash_config.suppress_tokens or []) | {role_end_id})

# Pair this config with inputs rendered using template_variant="flash":
# output = model.generate(**inputs, generation_config=flash_config, max_new_tokens=256)
```

These options switch prompt formatting and generation stops; they do not change
model weights. The generation examples above were recorded before this template
update. Template rendering, tokenization, tool-message formatting, and save/reload
were checked separately without loading model weights.
