---
license: apache-2.0
tags:
- sentence-transformers
- cross-encoder
- reranker
- generated_from_trainer
- dataset_size:26083
- loss:BinaryCrossEntropyLoss
base_model: Alibaba-NLP/gte-reranker-modernbert-base
pipeline_tag: text-ranking
library_name: sentence-transformers
metrics:
- map
- mrr@10
- ndcg@10
model-index:
- name: gte-reranker-modernbert-base-pubmed-tr
  results:
  - task:
      type: cross-encoder-reranking
      name: Cross Encoder Reranking
    dataset:
      name: gooaq dev
      type: gooaq-dev
    metrics:
    - type: map
      value: 0.2614
      name: Map
    - type: mrr@10
      value: 0.2604
      name: Mrr@10
    - type: ndcg@10
      value: 0.2755
      name: Ndcg@10
  - task:
      type: cross-encoder-reranking
      name: Cross Encoder Reranking
    dataset:
      name: NanoMSMARCO R100
      type: NanoMSMARCO_R100
    metrics:
    - type: map
      value: 0.6446
      name: Map
    - type: mrr@10
      value: 0.6366
      name: Mrr@10
    - type: ndcg@10
      value: 0.6902
      name: Ndcg@10
  - task:
      type: cross-encoder-reranking
      name: Cross Encoder Reranking
    dataset:
      name: NanoNFCorpus R100
      type: NanoNFCorpus_R100
    metrics:
    - type: map
      value: 0.409
      name: Map
    - type: mrr@10
      value: 0.6583
      name: Mrr@10
    - type: ndcg@10
      value: 0.45
      name: Ndcg@10
  - task:
      type: cross-encoder-reranking
      name: Cross Encoder Reranking
    dataset:
      name: NanoNQ R100
      type: NanoNQ_R100
    metrics:
    - type: map
      value: 0.7052
      name: Map
    - type: mrr@10
      value: 0.7289
      name: Mrr@10
    - type: ndcg@10
      value: 0.7593
      name: Ndcg@10
  - task:
      type: cross-encoder-nano-beir
      name: Cross Encoder Nano BEIR
    dataset:
      name: NanoBEIR R100 mean
      type: NanoBEIR_R100_mean
    metrics:
    - type: map
      value: 0.5863
      name: Map
    - type: mrr@10
      value: 0.6746
      name: Mrr@10
    - type: ndcg@10
      value: 0.6332
      name: Ndcg@10
---

# gte-reranker-modernbert-base-pubmed-tr

This is a [Cross Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html) model finetuned from [Alibaba-NLP/gte-reranker-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base) using the [sentence-transformers](https://www.SBERT.net) library. It computes scores for pairs of texts, which can be used for text reranking and semantic search.

## Model Details

### Model Description
- **Model Type:** Cross Encoder
- **Base model:** [Alibaba-NLP/gte-reranker-modernbert-base](https://huggingface.co/Alibaba-NLP/gte-reranker-modernbert-base) <!-- at revision f7481e6055501a30fb19d090657df9ec1f79ab2c -->
- **Maximum Sequence Length:** 8192 tokens
- **Number of Output Labels:** 1 label
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
- **License:** apache-2.0

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Documentation:** [Cross Encoder Documentation](https://www.sbert.net/docs/cross_encoder/usage/usage.html)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Cross Encoders on Hugging Face](https://huggingface.co/models?library=sentence-transformers&other=cross-encoder)

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import CrossEncoder

# Download from the 🤗 Hub
model = CrossEncoder("SMARTICT/gte-reranker-modernbert-base-pubmed-tr-v1")
# Get scores for pairs of texts
pairs = [
    ['Yaşlanmakta olan erkeklerde testosteron seviyelerindeki değişiklikler nasıl gözlemlenir ve bu değişiklikler hangi hormon seviyeleriyle ilişkilidir?', 'Testosteron seviyeleri azalır ve bu azalma, gonadotropinlere zayıf yanıt vermeyle birlikte görülür; testosteron seviyelerindeki düşüş, LH seviyelerinde artışla takip edilir.'],
    ['Yaşlanmakta olan erkeklerde testosteron seviyelerindeki değişiklikler nasıl gözlemlenir ve bu değişiklikler hangi hormon seviyeleriyle ilişkilidir?', 'Testosteron, NE seviyelerini, alımını veya salınımını etkilemediği gibi, vas deferens ve epididimste tirosin hidroksilaz aktivitesini değiştirmedi.'],
    ['Yaşlanmakta olan erkeklerde testosteron seviyelerindeki değişiklikler nasıl gözlemlenir ve bu değişiklikler hangi hormon seviyeleriyle ilişkilidir?', 'Yavaş dalga uykusundaki azalma, hormon seviyelerinde belirgin bir değişiklikle eşleşmedi.'],
    ['Yaşlanmakta olan erkeklerde testosteron seviyelerindeki değişiklikler nasıl gözlemlenir ve bu değişiklikler hangi hormon seviyeleriyle ilişkilidir?', 'Serum testosteron, diyaliz edilebilir testosteron ve LH seviyeleri sağlıklı erkeklerle anlamlı derecede fark göstermemekte, sadece LH yanıtları biraz daha yüksek bulunmuştur.'],
    ['Yaşlanmakta olan erkeklerde testosteron seviyelerindeki değişiklikler nasıl gözlemlenir ve bu değişiklikler hangi hormon seviyeleriyle ilişkilidir?', 'Maksimum uyarım testiyle değerlendirildi ve 6-15 yaş arasındaki erkekler üzerinde yapıldı.'],
]
scores = model.predict(pairs)
print(scores.shape)
# (5,)

# Or rank different texts based on similarity to a single text
ranks = model.rank(
    'Yaşlanmakta olan erkeklerde testosteron seviyelerindeki değişiklikler nasıl gözlemlenir ve bu değişiklikler hangi hormon seviyeleriyle ilişkilidir?',
    [
        'Testosteron seviyeleri azalır ve bu azalma, gonadotropinlere zayıf yanıt vermeyle birlikte görülür; testosteron seviyelerindeki düşüş, LH seviyelerinde artışla takip edilir.',
        'Testosteron, NE seviyelerini, alımını veya salınımını etkilemediği gibi, vas deferens ve epididimste tirosin hidroksilaz aktivitesini değiştirmedi.',
        'Yavaş dalga uykusundaki azalma, hormon seviyelerinde belirgin bir değişiklikle eşleşmedi.',
        'Serum testosteron, diyaliz edilebilir testosteron ve LH seviyeleri sağlıklı erkeklerle anlamlı derecede fark göstermemekte, sadece LH yanıtları biraz daha yüksek bulunmuştur.',
        'Maksimum uyarım testiyle değerlendirildi ve 6-15 yaş arasındaki erkekler üzerinde yapıldı.',
    ]
)
# [{'corpus_id': ..., 'score': ...}, {'corpus_id': ..., 'score': ...}, ...]
```

<!--
### Direct Usage (Transformers)

<details><summary>Click to see the direct usage in Transformers</summary>

</details>
-->

<!--
### Downstream Usage (Sentence Transformers)

You can finetune this model on your own dataset.

<details><summary>Click to expand</summary>

</details>
-->

<!--
### Out-of-Scope Use

*List how the model may foreseeably be misused and address what users ought not to do with the model.*
-->

## Evaluation

### Metrics

#### Cross Encoder Reranking

* Dataset: `gooaq-dev`
* Evaluated with [<code>CrossEncoderRerankingEvaluator</code>](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator) with these parameters:
  ```json
  {
      "at_k": 10,
      "always_rerank_positives": false
  }
  ```

| Metric      | Value                |
|:------------|:---------------------|
| map         | 0.2614 (+0.0585)     |
| mrr@10      | 0.2604 (+0.0613)     |
| **ndcg@10** | **0.2755 (+0.0586)** |

#### Cross Encoder Reranking

* Datasets: `NanoMSMARCO_R100`, `NanoNFCorpus_R100` and `NanoNQ_R100`
* Evaluated with [<code>CrossEncoderRerankingEvaluator</code>](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator) with these parameters:
  ```json
  {
      "at_k": 10,
      "always_rerank_positives": true
  }
  ```

| Metric      | NanoMSMARCO_R100     | NanoNFCorpus_R100    | NanoNQ_R100          |
|:------------|:---------------------|:---------------------|:---------------------|
| map         | 0.6446 (+0.1551)     | 0.4090 (+0.1480)     | 0.7052 (+0.2856)     |
| mrr@10      | 0.6366 (+0.1591)     | 0.6583 (+0.1585)     | 0.7289 (+0.3022)     |
| **ndcg@10** | **0.6902 (+0.1497)** | **0.4500 (+0.1250)** | **0.7593 (+0.2587)** |

#### Cross Encoder Nano BEIR

* Dataset: `NanoBEIR_R100_mean`
* Evaluated with [<code>CrossEncoderNanoBEIREvaluator</code>](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator) with these parameters:
  ```json
  {
      "dataset_names": [
          "msmarco",
          "nfcorpus",
          "nq"
      ],
      "rerank_k": 100,
      "at_k": 10,
      "always_rerank_positives": true
  }
  ```

| Metric      | Value                |
|:------------|:---------------------|
| map         | 0.5863 (+0.1962)     |
| mrr@10      | 0.6746 (+0.2066)     |
| **ndcg@10** | **0.6332 (+0.1778)** |

<!--
## Bias, Risks and Limitations

*What are the known or foreseeable issues stemming from this model? You could also flag here known failure cases or weaknesses of the model.*
-->

<!--
### Recommendations

*What are recommendations with respect to the foreseeable issues? For example, filtering explicit content.*
-->

## Training Details

### Training Dataset

#### Unnamed Dataset

* Size: 26,083 training samples
* Columns: <code>question</code>, <code>answer</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | question                                                                                         | answer                                                                                         | label                                           |
  |:--------|:-------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------|:------------------------------------------------|
  | type    | string                                                                                           | string                                                                                         | int                                             |
  | details | <ul><li>min: 44 characters</li><li>mean: 106.33 characters</li><li>max: 201 characters</li></ul> | <ul><li>min: 6 characters</li><li>mean: 98.72 characters</li><li>max: 389 characters</li></ul> | <ul><li>0: ~67.60%</li><li>1: ~32.40%</li></ul> |
* Samples:
  | question                                                                                                                                                         | answer                                                                                                                                                                                     | label          |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
  | <code>Yaşlanmakta olan erkeklerde testosteron seviyelerindeki değişiklikler nasıl gözlemlenir ve bu değişiklikler hangi hormon seviyeleriyle ilişkilidir?</code> | <code>Testosteron seviyeleri azalır ve bu azalma, gonadotropinlere zayıf yanıt vermeyle birlikte görülür; testosteron seviyelerindeki düşüş, LH seviyelerinde artışla takip edilir.</code> | <code>1</code> |
  | <code>Yaşlanmakta olan erkeklerde testosteron seviyelerindeki değişiklikler nasıl gözlemlenir ve bu değişiklikler hangi hormon seviyeleriyle ilişkilidir?</code> | <code>Testosteron, NE seviyelerini, alımını veya salınımını etkilemediği gibi, vas deferens ve epididimste tirosin hidroksilaz aktivitesini değiştirmedi.</code>                           | <code>0</code> |
  | <code>Yaşlanmakta olan erkeklerde testosteron seviyelerindeki değişiklikler nasıl gözlemlenir ve bu değişiklikler hangi hormon seviyeleriyle ilişkilidir?</code> | <code>Yavaş dalga uykusundaki azalma, hormon seviyelerinde belirgin bir değişiklikle eşleşmedi.</code>                                                                                     | <code>0</code> |
* Loss: [<code>BinaryCrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#binarycrossentropyloss) with these parameters:
  ```json
  {
      "activation_fn": "torch.nn.modules.linear.Identity",
      "pos_weight": 5
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `learning_rate`: 2e-05
- `num_train_epochs`: 2
- `warmup_ratio`: 0.1
- `bf16`: True
- `dataloader_num_workers`: 4
- `load_best_model_at_end`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 2
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.1
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `save_safetensors`: True
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `no_cuda`: False
- `use_cpu`: False
- `use_mps_device`: False
- `seed`: 42
- `data_seed`: None
- `jit_mode_eval`: False
- `use_ipex`: False
- `bf16`: True
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: 0
- `ddp_backend`: None
- `tpu_num_cores`: None
- `tpu_metrics_debug`: False
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 4
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `use_legacy_prediction_loop`: False
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `fp16_backend`: auto
- `push_to_hub_model_id`: None
- `push_to_hub_organization`: None
- `mp_parameters`: 
- `auto_find_batch_size`: False
- `full_determinism`: False
- `torchdynamo`: None
- `ray_scope`: last
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss | gooaq-dev_ndcg@10 | NanoMSMARCO_R100_ndcg@10 | NanoNFCorpus_R100_ndcg@10 | NanoNQ_R100_ndcg@10 | NanoBEIR_R100_mean_ndcg@10 |
|:------:|:----:|:-------------:|:-----------------:|:------------------------:|:-------------------------:|:-------------------:|:--------------------------:|
| -1     | -1   | -             | 0.2755 (+0.0586)  | 0.6902 (+0.1497)         | 0.4500 (+0.1250)          | 0.7593 (+0.2587)    | 0.6332 (+0.1778)           |
| 0.0006 | 1    | 1.2567        | -                 | -                        | -                         | -                   | -                          |
| 0.6131 | 1000 | 0.8436        | -                 | -                        | -                         | -                   | -                          |
| 1.2262 | 2000 | 0.6262        | -                 | -                        | -                         | -                   | -                          |
| 1.8394 | 3000 | 0.4757        | -                 | -                        | -                         | -                   | -                          |


### Framework Versions
- Python: 3.11.13
- Sentence Transformers: 5.0.0
- Transformers: 4.53.2
- PyTorch: 2.6.0+cu124
- Accelerate: 1.8.1
- Datasets: 4.0.0
- Tokenizers: 0.21.2

## Citation

### BibTeX

#### Sentence Transformers
```bibtex
@inproceedings{reimers-2019-sentence-bert,
    title = "Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks",
    author = "Reimers, Nils and Gurevych, Iryna",
    booktitle = "Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing",
    month = "11",
    year = "2019",
    publisher = "Association for Computational Linguistics",
    url = "https://arxiv.org/abs/1908.10084",
}
```

<!--
## Glossary

*Clearly define terms in order to be accessible across audiences.*
-->

<!--
## Model Card Authors

*Lists the people who create the model card, providing recognition and accountability for the detailed work that goes into its construction.*
-->

<!--
## Model Card Contact

*Provides a way for people who have updates to the Model Card, suggestions, or questions, to contact the Model Card authors.*
-->