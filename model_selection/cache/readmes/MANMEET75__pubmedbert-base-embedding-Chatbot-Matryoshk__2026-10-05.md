---
base_model: NeuML/pubmedbert-base-embeddings
datasets: []
language:
- en
library_name: sentence-transformers
license: apache-2.0
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_accuracy@10
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:530
- loss:MatryoshkaLoss
- loss:MultipleNegativesRankingLoss
widget:
- source_sentence: If you receive a BharatPe speaker that you didn't order, please
    contact BharatPe support immediately. They will assist in resolving the issue
    and advise on the next steps.
  sentences:
  - Can I control multiple BharatPe speakers from one app?
  - What to do if the BharatPe speaker's transaction announcements are intermittently
    silent?
  - What should I do if I receive a BharatPe speaker without ordering it?
- source_sentence: Remote control capabilities depend on the model of the BharatPe
    speaker. Check if your model supports remote control through the BharatPe app
    or a connected device.
  sentences:
  - How do I update my personal details in my Bharatpe account?
  - What are the benefits of the BharatPe speaker?
  - Can I control the BharatPe speaker remotely?
- source_sentence: If the announcements are not clear, check the speaker's volume
    settings and ensure it's not placed near noisy equipment. If clarity doesn't improve,
    the speaker may need servicing.
  sentences:
  - What to do if my BharatPe speaker is not syncing with the transaction history
    in the app?
  - What should I do if the speaker is not announcing payments clearly?
  - The speaker doesn't produce any sound, what can be done?
- source_sentence: If the speaker is causing interference, try relocating it or other
    devices to reduce the interference. Ensure there's a reasonable distance between
    the speaker and other wireless equipment.
  sentences:
  - Can I use my Bharatpe device for international transactions?
  - How do I know if my BharatPe speaker is under warranty?
  - What should I do if the BharatPe speaker is causing interference with other wireless
    devices?
- source_sentence: I can understand and respond in multiple Indian regional languages.
    Feel free to communicate with me in the language you're most comfortable with.
  sentences:
  - How can I check if the BharatPe speaker is receiving a network signal?
  - Bharti, can you provide tips for effective online communication?
  - Bharti, what languages can you understand and respond to?
model-index:
- name: pubmedbert-base-embedding Chatbot Matryoshka
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 768
      type: dim_768
    metrics:
    - type: cosine_accuracy@1
      value: 0.7674418604651163
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.9069767441860465
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.9302325581395349
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9302325581395349
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.7674418604651163
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.3023255813953489
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.18604651162790697
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09302325581395349
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.7674418604651163
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.9069767441860465
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.9302325581395349
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9302325581395349
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.8563596702043667
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.8313953488372093
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.8349894291754757
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 512
      type: dim_512
    metrics:
    - type: cosine_accuracy@1
      value: 0.6976744186046512
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.8837209302325582
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.9302325581395349
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9302325581395349
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.6976744186046512
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.29457364341085274
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.18604651162790697
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09302325581395349
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.6976744186046512
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.8837209302325582
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.9302325581395349
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9302325581395349
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.8320432881662091
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.7984496124031009
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.8017447288993117
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 256
      type: dim_256
    metrics:
    - type: cosine_accuracy@1
      value: 0.7906976744186046
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.8837209302325582
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.9069767441860465
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9069767441860465
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.7906976744186046
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.29457364341085274
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.1813953488372093
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09069767441860466
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.7906976744186046
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.8837209302325582
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.9069767441860465
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9069767441860465
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.8533147922143328
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.8352713178294573
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.8392285023210497
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 128
      type: dim_128
    metrics:
    - type: cosine_accuracy@1
      value: 0.6744186046511628
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.813953488372093
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8837209302325582
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9069767441860465
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.6744186046511628
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.2713178294573643
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.17674418604651165
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.09069767441860466
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.6744186046511628
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.813953488372093
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.8837209302325582
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9069767441860465
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.794152105183587
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.7575858250276855
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.7600321150655651
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 64
      type: dim_64
    metrics:
    - type: cosine_accuracy@1
      value: 0.6046511627906976
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.7441860465116279
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.7906976744186046
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.8604651162790697
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.6046511627906976
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.24806201550387597
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.15813953488372093
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.08604651162790698
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.6046511627906976
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.7441860465116279
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.7906976744186046
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.8604651162790697
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.7220252449949186
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.6786083425618308
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.6823125300680127
      name: Cosine Map@100
---

# pubmedbert-base-embedding Chatbot Matryoshka

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [NeuML/pubmedbert-base-embeddings](https://huggingface.co/NeuML/pubmedbert-base-embeddings). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [NeuML/pubmedbert-base-embeddings](https://huggingface.co/NeuML/pubmedbert-base-embeddings) <!-- at revision ba210f40b1b6d555d675c2d1ed6372e44570fc3c -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 tokens
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
- **Language:** en
- **License:** apache-2.0

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("MANMEET75/pubmedbert-base-embedding-Chatbot-Matryoshk")
# Run inference
sentences = [
    "I can understand and respond in multiple Indian regional languages. Feel free to communicate with me in the language you're most comfortable with.",
    'Bharti, what languages can you understand and respond to?',
    'Bharti, can you provide tips for effective online communication?',
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

#### Information Retrieval
* Dataset: `dim_768`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value     |
|:--------------------|:----------|
| cosine_accuracy@1   | 0.7674    |
| cosine_accuracy@3   | 0.907     |
| cosine_accuracy@5   | 0.9302    |
| cosine_accuracy@10  | 0.9302    |
| cosine_precision@1  | 0.7674    |
| cosine_precision@3  | 0.3023    |
| cosine_precision@5  | 0.186     |
| cosine_precision@10 | 0.093     |
| cosine_recall@1     | 0.7674    |
| cosine_recall@3     | 0.907     |
| cosine_recall@5     | 0.9302    |
| cosine_recall@10    | 0.9302    |
| cosine_ndcg@10      | 0.8564    |
| cosine_mrr@10       | 0.8314    |
| **cosine_map@100**  | **0.835** |

#### Information Retrieval
* Dataset: `dim_512`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.6977     |
| cosine_accuracy@3   | 0.8837     |
| cosine_accuracy@5   | 0.9302     |
| cosine_accuracy@10  | 0.9302     |
| cosine_precision@1  | 0.6977     |
| cosine_precision@3  | 0.2946     |
| cosine_precision@5  | 0.186      |
| cosine_precision@10 | 0.093      |
| cosine_recall@1     | 0.6977     |
| cosine_recall@3     | 0.8837     |
| cosine_recall@5     | 0.9302     |
| cosine_recall@10    | 0.9302     |
| cosine_ndcg@10      | 0.832      |
| cosine_mrr@10       | 0.7984     |
| **cosine_map@100**  | **0.8017** |

#### Information Retrieval
* Dataset: `dim_256`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.7907     |
| cosine_accuracy@3   | 0.8837     |
| cosine_accuracy@5   | 0.907      |
| cosine_accuracy@10  | 0.907      |
| cosine_precision@1  | 0.7907     |
| cosine_precision@3  | 0.2946     |
| cosine_precision@5  | 0.1814     |
| cosine_precision@10 | 0.0907     |
| cosine_recall@1     | 0.7907     |
| cosine_recall@3     | 0.8837     |
| cosine_recall@5     | 0.907      |
| cosine_recall@10    | 0.907      |
| cosine_ndcg@10      | 0.8533     |
| cosine_mrr@10       | 0.8353     |
| **cosine_map@100**  | **0.8392** |

#### Information Retrieval
* Dataset: `dim_128`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value    |
|:--------------------|:---------|
| cosine_accuracy@1   | 0.6744   |
| cosine_accuracy@3   | 0.814    |
| cosine_accuracy@5   | 0.8837   |
| cosine_accuracy@10  | 0.907    |
| cosine_precision@1  | 0.6744   |
| cosine_precision@3  | 0.2713   |
| cosine_precision@5  | 0.1767   |
| cosine_precision@10 | 0.0907   |
| cosine_recall@1     | 0.6744   |
| cosine_recall@3     | 0.814    |
| cosine_recall@5     | 0.8837   |
| cosine_recall@10    | 0.907    |
| cosine_ndcg@10      | 0.7942   |
| cosine_mrr@10       | 0.7576   |
| **cosine_map@100**  | **0.76** |

#### Information Retrieval
* Dataset: `dim_64`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.6047     |
| cosine_accuracy@3   | 0.7442     |
| cosine_accuracy@5   | 0.7907     |
| cosine_accuracy@10  | 0.8605     |
| cosine_precision@1  | 0.6047     |
| cosine_precision@3  | 0.2481     |
| cosine_precision@5  | 0.1581     |
| cosine_precision@10 | 0.086      |
| cosine_recall@1     | 0.6047     |
| cosine_recall@3     | 0.7442     |
| cosine_recall@5     | 0.7907     |
| cosine_recall@10    | 0.8605     |
| cosine_ndcg@10      | 0.722      |
| cosine_mrr@10       | 0.6786     |
| **cosine_map@100**  | **0.6823** |

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


* Size: 530 training samples
* Columns: <code>positive</code> and <code>anchor</code>
* Approximate statistics based on the first 1000 samples:
  |         | positive                                                                            | anchor                                                                            |
  |:--------|:------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                            |
  | details | <ul><li>min: 12 tokens</li><li>mean: 36.83 tokens</li><li>max: 107 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 18.54 tokens</li><li>max: 30 tokens</li></ul> |
* Samples:
  | positive                                                                                                                                                                                                                                                                                                                                                                            | anchor                                                                   |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------|
  | <code>BharatPe Speaker comes with the following benefits: - Helps you avoid payment fraud - Lightweight & Easy installation process - Compatible with SIM & GPRS connectivity - Comes with a battery, no hassle of constant charging - Available in 10 Languages - Cashback Offers - Free replacement To Know more and place an order, tap below http://bharatpe.in/speaker.</code> | <code>What are the benefits of the BharatPe speaker?</code>              |
  | <code>BharatPe Speaker comes with the following benefits: - Helps you avoid payment fraud - Lightweight & Easy installation process - Compatible with SIM & GPRS connectivity - Comes with a battery, no hassle of constant charging - Available in 10 Languages - Cashback Offers - Free replacement To Know more and place an order, tap below http://bharatpe.in/speaker.</code> | <code>What advantages does the BharatPe speaker offer?</code>            |
  | <code>BharatPe Speaker comes with the following benefits: - Helps you avoid payment fraud - Lightweight & Easy installation process - Compatible with SIM & GPRS connectivity - Comes with a battery, no hassle of constant charging - Available in 10 Languages - Cashback Offers - Free replacement To Know more and place an order, tap below http://bharatpe.in/speaker.</code> | <code>Can you outline the benefits of using the BharatPe speaker?</code> |
* Loss: [<code>MatryoshkaLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss) with these parameters:
  ```json
  {
      "loss": "MultipleNegativesRankingLoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: epoch
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 16
- `gradient_accumulation_steps`: 16
- `learning_rate`: 2e-05
- `num_train_epochs`: 10
- `lr_scheduler_type`: cosine
- `warmup_ratio`: 0.1
- `tf32`: False
- `load_best_model_at_end`: True
- `optim`: adamw_torch_fused
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: epoch
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 16
- `eval_accumulation_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 10
- `max_steps`: -1
- `lr_scheduler_type`: cosine
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
- `bf16`: False
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: False
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
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
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
- `hub_private_repo`: False
- `hub_always_push`: False
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_inputs_for_metrics`: False
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
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch      | Step  | Training Loss | dim_128_cosine_map@100 | dim_256_cosine_map@100 | dim_512_cosine_map@100 | dim_64_cosine_map@100 | dim_768_cosine_map@100 |
|:----------:|:-----:|:-------------:|:----------------------:|:----------------------:|:----------------------:|:---------------------:|:----------------------:|
| 0.9412     | 1     | -             | 0.4829                 | 0.5338                 | 0.5921                 | 0.3235                | 0.6100                 |
| 1.8824     | 2     | -             | 0.5767                 | 0.6175                 | 0.6588                 | 0.4176                | 0.6793                 |
| 2.8235     | 3     | -             | 0.6337                 | 0.6776                 | 0.6979                 | 0.5083                | 0.7263                 |
| 3.7647     | 4     | -             | 0.6588                 | 0.7257                 | 0.7297                 | 0.5840                | 0.7612                 |
| 4.7059     | 5     | -             | 0.7049                 | 0.7766                 | 0.7643                 | 0.6151                | 0.7902                 |
| 5.6471     | 6     | -             | 0.7374                 | 0.8257                 | 0.7890                 | 0.6519                | 0.7956                 |
| 6.5882     | 7     | -             | 0.7573                 | 0.8261                 | 0.7912                 | 0.6689                | 0.7978                 |
| 7.5294     | 8     | -             | 0.7590                 | 0.8275                 | 0.7958                 | 0.6811                | 0.8233                 |
| **8.4706** | **9** | **-**         | **0.76**               | **0.8392**             | **0.7998**             | **0.6823**            | **0.8234**             |
| 9.4118     | 10    | 4.944         | 0.7600                 | 0.8392                 | 0.8017                 | 0.6823                | 0.8350                 |

* The bold row denotes the saved checkpoint.

### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.0.1
- Transformers: 4.41.2
- PyTorch: 2.1.2+cu121
- Accelerate: 0.32.1
- Datasets: 2.19.1
- Tokenizers: 0.19.1

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

#### MatryoshkaLoss
```bibtex
@misc{kusupati2024matryoshka,
    title={Matryoshka Representation Learning}, 
    author={Aditya Kusupati and Gantavya Bhatt and Aniket Rege and Matthew Wallingford and Aditya Sinha and Vivek Ramanujan and William Howard-Snyder and Kaifeng Chen and Sham Kakade and Prateek Jain and Ali Farhadi},
    year={2024},
    eprint={2205.13147},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```

#### MultipleNegativesRankingLoss
```bibtex
@misc{henderson2017efficient,
    title={Efficient Natural Language Response Suggestion for Smart Reply}, 
    author={Matthew Henderson and Rami Al-Rfou and Brian Strope and Yun-hsuan Sung and Laszlo Lukacs and Ruiqi Guo and Sanjiv Kumar and Balint Miklos and Ray Kurzweil},
    year={2017},
    eprint={1705.00652},
    archivePrefix={arXiv},
    primaryClass={cs.CL}
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