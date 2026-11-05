---
base_model:
- deepseek-ai/DeepSeek-R1-Distill-Llama-70B
- nvidia/Llama-3.1-Nemotron-70B-Instruct-HF
library_name: transformers
tags:
- mergekit
- merge

---
# merge

This is a merge of pre-trained language models created using [mergekit](https://github.com/cg123/mergekit).

## Merge Details
### Merge Method

This model was merged using the [Linear DELLA](https://arxiv.org/abs/2406.11617) merge method using [deepseek-ai/DeepSeek-R1-Distill-Llama-70B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Llama-70B) as a base.

### Models Merged

The following models were included in the merge:
* [nvidia/Llama-3.1-Nemotron-70B-Instruct-HF](https://huggingface.co/nvidia/Llama-3.1-Nemotron-70B-Instruct-HF)

### Configuration

The following YAML configuration was used to produce this model:

```yaml
merge_method: della_linear
base_model: deepseek-ai/DeepSeek-R1-Distill-Llama-70B
tokenizer_source: "unsloth/Llama-3.3-70B-Instruct"
dtype: float16
parameters:
  epsilon: 0.05             # Fine-grain scaling for precision.
  lambda: 1.6               # Strong emphasis on top-performing models.
  normalize: true           # Stable parameter integration across models.
adaptive_merge_parameters:
  task_weights:
    tinyArc: 2.0            # Увеличиваем вес для логического рассуждения.
    tinyHellaswag: 1.75     # Увеличиваем для контекстных предсказаний.
    tinyMMLU: 2.0           # Увеличиваем для доменных знаний.
    tinyTruthfulQA: 2.2     # Увеличиваем приоритет правдивого рассуждения.
    tinyTruthfulQA_mc1: 2.0 # Поддерживаем высокий приоритет для многоразовых вопросов.
    tinyWinogrande: 2.0     # Увеличиваем для сложного рассуждения и предсказаний.
    IFEval: 2.1             # Поддерживаем высокий приоритет для выполнения инструкций и многозадачности.
    BBH: 2.0                # Увеличиваем для комплексного рассуждения.
    MATH: 2.5               # Увеличиваем вес математического рассуждения для акцента на точности.
    GPQA: 2.3               # Увеличиваем вес для фактического QA.
    MUSR: 2.1               # Поддерживаем высокий приоритет для многошагового рассуждения.
    MMLU-PRO: 2.3           # Поддерживаем высокие показатели в многозадачности по доменам.
  smoothing_factor: 0.1     # Сглаживание остается прежним для плавного смешивания.

models:
  - model: nvidia/Llama-3.1-Nemotron-70B-Instruct-HF
    parameters:
      weight: 1
      density: 1
  - model: deepseek-ai/DeepSeek-R1-Distill-Llama-70B
    parameters:
      weight: 1
      density: 1

```
