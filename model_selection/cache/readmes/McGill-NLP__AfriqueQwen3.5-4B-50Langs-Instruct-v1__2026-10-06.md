---
license: cc-by-4.0
base_model: McGill-NLP/AfriqueQwen3.5-4B-50Langs
pipeline_tag: text-generation
---

# AfriqueQwen3.5-4B-50Langs-Instruct-v1

Post-trained version (v1) of [McGill-NLP/AfriqueQwen3.5-4B-50Langs](https://huggingface.co/McGill-NLP/AfriqueQwen3.5-4B-50Langs).





## Performance

| Model | Params | AfriMGSM | AfriMMLU | AfriXNLI | Belebele | Injongo | SIB-200 | FLORES | Overall |
|---|---|---|---|---|---|---|---|---|---|
| Apertus-8B-Instruct-2509 | 8B | 12.7 | 35.1 | 34.4 | 42.5 | 11.8 | 67.7 | 43.5 | 35.4 |
| Gemma-3-4B-it | 4B | 20.4 | 35.7 | 48.4 | 47.9 | 28.7 | 67.1 | 33.5 | 40.3 |
| tiny-aya-earth | 3.35B | 19.6 | 41.3 | 55.4 | 54.4 | 17.4 | 69.5 | 42.0 | 42.8 |
| Qwen3.5-4B | 4B | 41.5 | 41.8 | 51.5 | 52.8 | 35.1 | 71.5 | 44.4 | 48.4 |
| Sunflower-Qwen3.5-9B | 9B | 19.9 | 41.8 | 50.5 | 62.7 | 55.0 | 78.3 | 62.3 | 52.9 |
| AfriqueQwen3.5-4B-Instruct-v1 | 4B | 51.4 | 46.3 | 62.4 | 65.2 | 59.1 | 80.4 | 57.8 | 60.4 |
| AfriqueQwen3.5-4B-Instruct-v2 | 4B | 50.8 | 46.4 | 63.6 | 66.2 | 58.7 | 81.2 | 62.3 | 61.3 |
| **AfriqueQwen3.5-4B-50Langs-Instruct-v1** | **4B** | **54.2** | **45.4** | **62.2** | **66.9** | **58.1** | **81.5** | **62.9** | **61.6** |

*For Flores, we use SSA-COMET ([Li et al., 2025](https://arxiv.org/abs/2506.04557)); for AfriMGSM, we detect the number inside the `\boxed{}` or the last number in the entire output; for multiple-choice questions, we use exact match.*

## Usage

Served with vLLM. The checkpoint declares `Qwen3_5ForConditionalGeneration` but carries no
vision weights (426 language-model tensors, `lm_head` tied to the embeddings, 0 visual), so
`--language-model-only` is required.

```bash
vllm serve McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1 --language-model-only --max-model-len 12288 --port 8000
```

```bash
curl http://127.0.0.1:8000/v1/chat/completions -H 'Content-Type: application/json' -d '{
  "model": "McGill-NLP/AfriqueQwen3.5-4B-50Langs-Instruct-v1",
  "messages": [
    {"role": "system", "content": "Wewe ni msaidizi mwenye manufaa ambaye hutatua matatizo ya hisabati yaliyoandikwa kwa maneno.\nTafadhali toa hoja hatua kwa hatua kwa Kiswahili, na uweke jibu lako la mwisho ndani ya \\boxed{}."},
    {"role": "user", "content": "Sandy hupata $15 kwa saa. Alifanya kazi saa 10 Ijumaa. Alipata pesa ngapi?"}
  ],
  "temperature": 0.7, "top_p": 0.8, "top_k": 20, "presence_penalty": 1.5, "max_tokens": 10240
}'
```

```
Hatua ya 1: Sandy hupata $15 kwa saa.
Hatua ya 2: Sandy alifanya kazi saa 10 Ijumaa.
Hatua ya 3: Jumla ya Mapato = $15/saa x saa 10
Hatua ya 4: $15 x 10 = $150

Sandy alipata $150 kwa kufanya kazi saa 10.
```

## Recommendation Prompting and Setting

### Mathematics


**English**

```
You are a helpful assistant that solves math word problems.
Please reason step by step in English, and put your final answer within \boxed{}.
```



For other languages, replace the part after "step by step in" with the target language, and translate it into the target language, for example **Swahili**:

```
Wewe ni msaidizi mwenye manufaa ambaye hutatua matatizo ya hisabati yaliyoandikwa kwa maneno.
Tafadhali toa hoja hatua kwa hatua kwa Kiswahili, na uweke jibu lako la mwisho ndani ya \boxed{}.
```




| Setting | Mathematics | Other tasks |
|---|---|---|
| `enable_thinking` | `true` | `false` |
| `temperature` | 0.7 | 0 (greedy) |
| `top_p` | 0.8 | — |
| `top_k` | 20 | — |
| `min_p` | 0 | — |
| `presence_penalty` | 1.5 | 0 |
| `repetition_penalty` | 1.0 | 1.0 |
| `max_tokens` | 10240 | 1024 |
| `--max-model-len` | 12288 | 8192 |



### Other tasks



Translation:

```
Translate the following sentence from {source language} to {target language}.

{source language}: {sentence}
{target language}:
```

Multiple choice:

```
Answer the multiple-choice question by replying with ONLY the letter
(A, B, C, or D) of the correct answer.

Question: {question}

A. {A}
B. {B}
C. {C}
D. {D}

Answer:
```



