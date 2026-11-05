---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:2351
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-mpnet-base-v2
widget:
- source_sentence: Are your thoughts sometimes so strong that you can almost hear
    them?
  sentences:
  - My emotions have almost always seemed flat regardless of what is going on around
    me.
  - Having powerful images or memories that sometimes come into your mind in which
    you feel the experience is happening again in the here and now?
  - I often think that I hear people talking only to discover that there was no one
    there.
- source_sentence: Having difficulty concentrating?
  sentences:
  - My thoughts are so hazy and unclear that I wish that I could just reach up and
    put them into place.
  - Most of the time I find it is very difficult to get my thoughts in order.
  - Experienced sleep disturbances?
- source_sentence: Feeling jumpy or easily startled?
  sentences:
  - I often worry that someone or something is controlling my behavior.
  - People find my conversations to be confusing or hard to follow.
  - Worried a lot about different things?
- source_sentence: Do you often have to keep an eye out to stop people from taking
    advantage of you?
  sentences:
  - I find that I am very often confused about what is going on around me.
  - I sometimes wonder if there is a small group of people who can control everyone
    else's behavior.
  - I have sometimes felt that strangers were reading my mind.
- source_sentence: I am not good at expressing my true feelings by the way I talk
    and look.
  sentences:
  - Felt down or depressed for most of the day
  - Felt nervous or anxious?
  - Experienced sleep disturbances?
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- pearson_cosine
- spearman_cosine
model-index:
- name: SentenceTransformer based on sentence-transformers/all-mpnet-base-v2
  results:
  - task:
      type: semantic-similarity
      name: Semantic Similarity
    dataset:
      name: Unknown
      type: unknown
    metrics:
    - type: pearson_cosine
      value: 0.5680489773046146
      name: Pearson Cosine
    - type: spearman_cosine
      value: 0.5532689999140259
      name: Spearman Cosine
---

# SentenceTransformer based on sentence-transformers/all-mpnet-base-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) <!-- at revision 9a3225965996d404b775526de6dbfe85d3368642 -->
- **Maximum Sequence Length:** 384 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 384, 'do_lower_case': False}) with Transformer model: MPNetModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Normalize()
)
```

## Usage

### Direct Usage (Sentence Transformers)

First install the Sentence Transformers library:

```bash
pip install -U sentence-transformers
```

Then you can load this model and run inference.
```python
from sentence_transformers import SentenceTransformer

# Download from the 🤗 Hub
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'I am not good at expressing my true feelings by the way I talk and look.',
    'Felt nervous or anxious?',
    'Experienced sleep disturbances?',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities.shape)
# [3, 3]
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

#### Semantic Similarity

* Evaluated with [<code>EmbeddingSimilarityEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.EmbeddingSimilarityEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| pearson_cosine      | 0.568      |
| **spearman_cosine** | **0.5533** |

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


* Size: 2,351 training samples
* Columns: <code>sentence1</code>, <code>sentence2</code>, and <code>score</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence1                                                                         | sentence2                                                                         | score                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | float                                                          |
  | details | <ul><li>min: 5 tokens</li><li>mean: 16.73 tokens</li><li>max: 47 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 14.82 tokens</li><li>max: 28 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.26</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence1                                                                 | sentence2                                                                                              | score             |
  |:--------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|:------------------|
  | <code>Do you believe in telepathy (mind-reading)?</code>                  | <code>I believe that there are secret signs in the world if you just know how to look for them.</code> | <code>0.15</code> |
  | <code>Irritable behavior, angry outbursts, or acting aggressively?</code> | <code>Felt “on edge”?</code>                                                                           | <code>0.62</code> |
  | <code>I have some eccentric (odd) habits.</code>                          | <code>I often have difficulty following what someone is saying to me.</code>                           | <code>0.0</code>  |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.L1Loss"
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset


* Size: 236 evaluation samples
* Columns: <code>sentence1</code>, <code>sentence2</code>, and <code>score</code>
* Approximate statistics based on the first 236 samples:
  |         | sentence1                                                                        | sentence2                                                                         | score                                                          |
  |:--------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                           | string                                                                            | float                                                          |
  | details | <ul><li>min: 6 tokens</li><li>mean: 16.4 tokens</li><li>max: 47 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 14.76 tokens</li><li>max: 28 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.29</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence1                                                       | sentence2                                                                                                           | score             |
  |:----------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:------------------|
  | <code>Feeling afraid as if something awful might happen?</code> | <code>I have trouble following conversations with others.</code>                                                    | <code>0.19</code> |
  | <code>Do you believe in telepathy (mind-reading)?</code>        | <code>Feeling jumpy or easily startled?</code>                                                                      | <code>0.1</code>  |
  | <code>Other people see me as slightly eccentric (odd).</code>   | <code>I have felt that there were messages for me in the way things were arranged, like furniture in a room.</code> | <code>0.0</code>  |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.L1Loss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 16

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
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
- `bf16`: False
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
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
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
- `dispatch_batches`: None
- `split_batches`: None
- `include_tokens_per_second`: False
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step | Training Loss | Validation Loss | spearman_cosine |
|:------:|:----:|:-------------:|:---------------:|:---------------:|
| 0.0680 | 10   | 0.2239        | -               | -               |
| 0.1361 | 20   | 0.2188        | -               | -               |
| 0.2041 | 30   | 0.2007        | -               | -               |
| 0.2721 | 40   | 0.2045        | -               | -               |
| 0.3401 | 50   | 0.2179        | 0.2197          | -               |
| 0.4082 | 60   | 0.2106        | -               | -               |
| 0.4762 | 70   | 0.2124        | -               | -               |
| 0.5442 | 80   | 0.2046        | -               | -               |
| 0.6122 | 90   | 0.2069        | -               | -               |
| 0.6803 | 100  | 0.1965        | 0.2112          | -               |
| 0.7483 | 110  | 0.2355        | -               | -               |
| 0.8163 | 120  | 0.2012        | -               | -               |
| 0.8844 | 130  | 0.2402        | -               | -               |
| 0.9524 | 140  | 0.2173        | -               | -               |
| 1.0204 | 150  | 0.1763        | 0.2043          | -               |
| 1.0884 | 160  | 0.1862        | -               | -               |
| 1.1565 | 170  | 0.1854        | -               | -               |
| 1.2245 | 180  | 0.193         | -               | -               |
| 1.2925 | 190  | 0.1852        | -               | -               |
| 1.3605 | 200  | 0.1908        | 0.1950          | -               |
| 1.4286 | 210  | 0.2002        | -               | -               |
| 1.4966 | 220  | 0.1945        | -               | -               |
| 1.5646 | 230  | 0.193         | -               | -               |
| 1.6327 | 240  | 0.1893        | -               | -               |
| 1.7007 | 250  | 0.171         | 0.1937          | -               |
| 1.7687 | 260  | 0.1848        | -               | -               |
| 1.8367 | 270  | 0.1909        | -               | -               |
| 1.9048 | 280  | 0.2138        | -               | -               |
| 1.9728 | 290  | 0.2014        | -               | -               |
| 2.0408 | 300  | 0.1855        | 0.1867          | -               |
| 2.1088 | 310  | 0.1891        | -               | -               |
| 2.1769 | 320  | 0.1849        | -               | -               |
| 2.2449 | 330  | 0.1741        | -               | -               |
| 2.3129 | 340  | 0.1775        | -               | -               |
| 2.3810 | 350  | 0.178         | 0.1871          | -               |
| 2.4490 | 360  | 0.1778        | -               | -               |
| 2.5170 | 370  | 0.174         | -               | -               |
| 2.5850 | 380  | 0.1654        | -               | -               |
| 2.6531 | 390  | 0.1954        | -               | -               |
| 2.7211 | 400  | 0.1584        | 0.1860          | -               |
| 2.7891 | 410  | 0.2019        | -               | -               |
| 2.8571 | 420  | 0.1941        | -               | -               |
| 2.9252 | 430  | 0.1855        | -               | -               |
| 2.9932 | 440  | 0.1823        | -               | -               |
| 3.0    | 441  | -             | -               | 0.5533          |


### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.3.1
- Transformers: 4.47.1
- PyTorch: 2.5.1+cu121
- Accelerate: 1.2.1
- Datasets: 3.2.0
- Tokenizers: 0.21.0

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