---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:57306
- loss:MultipleNegativesRankingLoss
base_model: allenai/specter2_base
widget:
- source_sentence: UCLR RTS timing
  sentences:
  - 'Timing without a timer. '
  - 'Global structural changes in annexin 12. The roles of phospholipid, Ca2+, and
    pH. '
  - 'Length of time between surgery and return to sport after ulnar collateral ligament
    reconstruction in Major League Baseball pitchers does not predict need for revision
    surgery. '
- source_sentence: Levofloxacin efficacy in bone and joint infections
  sentences:
  - 'Levofloxacin. '
  - 'Squamous cell carcinoma of the uterine cervix producing granulocyte colony-stimulating
    factor: a report of 4 cases and a review of the literature. '
  - 'Levofloxacin at the usual dosage to treat bone and joint infections: a cohort
    analysis. '
- source_sentence: Electrical impedance tomography in Barrett's oesophagus
  sentences:
  - 'Barrett''s oesophagus: epidemiology, diagnosis and clinical management. '
  - 'Assessing the conditions for in vivo electrical virtual biopsies in Barrett''s
    oesophagus. '
  - 'Serum aminoterminal propeptide of type III procollagen: a potential predictor
    of the response to growth hormone therapy. '
- source_sentence: Population Aging Theory
  sentences:
  - 'A cybernetic theory of aging. '
  - '[In process]. '
  - 'Robine and Michel''s "Looking forward to a general theory on population aging":
    commentary. '
- source_sentence: Algesimetric study of hypoalgesic effect
  sentences:
  - 'Regulation of ATG4B stability by RNF5 limits basal levels of autophagy and influences
    susceptibility to bacterial infection. '
  - '[Pain analysis is basis for correct choice of therapeutic method]. '
  - '[Experimental algesimetric study of the hypoalgesic effect of body acupuncture]. '
pipeline_tag: sentence-similarity
library_name: sentence-transformers
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
model-index:
- name: SentenceTransformer based on allenai/specter2_base
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoNQ
      type: NanoNQ
    metrics:
    - type: cosine_accuracy@1
      value: 0.02
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.06
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.08
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.22
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.02
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.02
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.016
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.022000000000000002
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.01
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.05
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.07
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.19
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.08358031930860417
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.060047619047619044
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.05702682179889267
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: NanoMSMARCO
      type: NanoMSMARCO
    metrics:
    - type: cosine_accuracy@1
      value: 0.12
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.3
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.34
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.44
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.12
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.1
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.068
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.044000000000000004
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.12
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.3
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.34
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.44
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.2718119392465092
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.21891269841269842
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.22988006901512154
      name: Cosine Map@100
  - task:
      type: nano-beir
      name: Nano BEIR
    dataset:
      name: NanoBEIR mean
      type: NanoBEIR_mean
    metrics:
    - type: cosine_accuracy@1
      value: 0.06999999999999999
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.18
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.21000000000000002
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.33
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.06999999999999999
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.060000000000000005
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.042
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.033
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.065
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.175
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.20500000000000002
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.315
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.17769612927755668
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.13948015873015873
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.1434534454070071
      name: Cosine Map@100
---

# SentenceTransformer based on allenai/specter2_base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [allenai/specter2_base](https://huggingface.co/allenai/specter2_base) on the json dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [allenai/specter2_base](https://huggingface.co/allenai/specter2_base) <!-- at revision 3447645e1def9117997203454fa4495937bfbd83 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - json
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

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
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Algesimetric study of hypoalgesic effect',
    '[Experimental algesimetric study of the hypoalgesic effect of body acupuncture]. ',
    '[Pain analysis is basis for correct choice of therapeutic method]. ',
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

* Datasets: `NanoNQ` and `NanoMSMARCO`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | NanoNQ     | NanoMSMARCO |
|:--------------------|:-----------|:------------|
| cosine_accuracy@1   | 0.02       | 0.12        |
| cosine_accuracy@3   | 0.06       | 0.3         |
| cosine_accuracy@5   | 0.08       | 0.34        |
| cosine_accuracy@10  | 0.22       | 0.44        |
| cosine_precision@1  | 0.02       | 0.12        |
| cosine_precision@3  | 0.02       | 0.1         |
| cosine_precision@5  | 0.016      | 0.068       |
| cosine_precision@10 | 0.022      | 0.044       |
| cosine_recall@1     | 0.01       | 0.12        |
| cosine_recall@3     | 0.05       | 0.3         |
| cosine_recall@5     | 0.07       | 0.34        |
| cosine_recall@10    | 0.19       | 0.44        |
| **cosine_ndcg@10**  | **0.0836** | **0.2718**  |
| cosine_mrr@10       | 0.06       | 0.2189      |
| cosine_map@100      | 0.057      | 0.2299      |

#### Nano BEIR

* Dataset: `NanoBEIR_mean`
* Evaluated with [<code>NanoBEIREvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.NanoBEIREvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.07       |
| cosine_accuracy@3   | 0.18       |
| cosine_accuracy@5   | 0.21       |
| cosine_accuracy@10  | 0.33       |
| cosine_precision@1  | 0.07       |
| cosine_precision@3  | 0.06       |
| cosine_precision@5  | 0.042      |
| cosine_precision@10 | 0.033      |
| cosine_recall@1     | 0.065      |
| cosine_recall@3     | 0.175      |
| cosine_recall@5     | 0.205      |
| cosine_recall@10    | 0.315      |
| **cosine_ndcg@10**  | **0.1777** |
| cosine_mrr@10       | 0.1395     |
| cosine_map@100      | 0.1435     |

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

#### json

* Dataset: json
* Size: 57,306 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                           | positive                                                                          | negative                                                                          |
  |:--------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                           | string                                                                            | string                                                                            |
  | details | <ul><li>min: 4 tokens</li><li>mean: 7.57 tokens</li><li>max: 25 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 20.36 tokens</li><li>max: 78 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 12.38 tokens</li><li>max: 49 tokens</li></ul> |
* Samples:
  | anchor                                               | positive                                                                                                                                                             | negative                                                                             |
  |:-----------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
  | <code>Intramedullary Hemangioblastoma</code>         | <code>Hydrocephalus: a rare initial manifestation of sporadic intramedullary hemangioblastoma : Intramedullary hemangioblastoma presenting as hydrocephalus. </code> | <code>Intramedullary capillary haemangioma. </code>                                  |
  | <code>Density-based load estimation algorithm</code> | <code>A contact algorithm for density-based load estimation. </code>                                                                                                 | <code>Density propagation based adaptive multi-density clustering algorithm. </code> |
  | <code>Herbicide Adjuvant Efficacy</code>             | <code>The efficiency of adjuvants combined with flupyrsulfuron-methyl plus metsulfuron-methyl (Lexus XPE) on weed control. </code>                                   | <code>Are herbicides a once in a century method of weed control? </code>             |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `gradient_accumulation_steps`: 4
- `learning_rate`: 2e-07
- `num_train_epochs`: 1
- `lr_scheduler_type`: cosine_with_restarts
- `warmup_ratio`: 0.1
- `bf16`: True
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 4
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-07
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 1
- `max_steps`: -1
- `lr_scheduler_type`: cosine_with_restarts
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
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step | Training Loss | NanoNQ_cosine_ndcg@10 | NanoMSMARCO_cosine_ndcg@10 | NanoBEIR_mean_cosine_ndcg@10 |
|:------:|:----:|:-------------:|:---------------------:|:--------------------------:|:----------------------------:|
| 0      | 0    | -             | 0.0682                | 0.2560                     | 0.1621                       |
| 0.0134 | 1    | 14.8664       | -                     | -                          | -                            |
| 0.0268 | 2    | 14.6017       | -                     | -                          | -                            |
| 0.0401 | 3    | 14.8474       | -                     | -                          | -                            |
| 0.0535 | 4    | 14.7156       | -                     | -                          | -                            |
| 0.0669 | 5    | 14.5967       | -                     | -                          | -                            |
| 0.0803 | 6    | 14.8373       | -                     | -                          | -                            |
| 0.0936 | 7    | 14.7819       | -                     | -                          | -                            |
| 0.1070 | 8    | 14.5891       | -                     | -                          | -                            |
| 0.1204 | 9    | 14.5531       | -                     | -                          | -                            |
| 0.1338 | 10   | 14.5441       | -                     | -                          | -                            |
| 0.1472 | 11   | 14.5516       | -                     | -                          | -                            |
| 0.1605 | 12   | 14.5739       | -                     | -                          | -                            |
| 0.1739 | 13   | 14.5974       | -                     | -                          | -                            |
| 0.1873 | 14   | 14.4102       | -                     | -                          | -                            |
| 0.2007 | 15   | 14.3615       | -                     | -                          | -                            |
| 0.2140 | 16   | 14.2877       | -                     | -                          | -                            |
| 0.2274 | 17   | 14.2774       | -                     | -                          | -                            |
| 0.2408 | 18   | 14.4985       | -                     | -                          | -                            |
| 0.2542 | 19   | 14.2307       | -                     | -                          | -                            |
| 0.2676 | 20   | 14.3657       | -                     | -                          | -                            |
| 0.2809 | 21   | 14.3261       | -                     | -                          | -                            |
| 0.2943 | 22   | 14.2946       | -                     | -                          | -                            |
| 0.3077 | 23   | 14.2311       | -                     | -                          | -                            |
| 0.3211 | 24   | 14.0789       | -                     | -                          | -                            |
| 0.3344 | 25   | 13.9392       | 0.0764                | 0.2652                     | 0.1708                       |
| 0.3478 | 26   | 14.0972       | -                     | -                          | -                            |
| 0.3612 | 27   | 14.0966       | -                     | -                          | -                            |
| 0.3746 | 28   | 13.9205       | -                     | -                          | -                            |
| 0.3880 | 29   | 13.8919       | -                     | -                          | -                            |
| 0.4013 | 30   | 14.1233       | -                     | -                          | -                            |
| 0.4147 | 31   | 14.1351       | -                     | -                          | -                            |
| 0.4281 | 32   | 14.1106       | -                     | -                          | -                            |
| 0.4415 | 33   | 14.166        | -                     | -                          | -                            |
| 0.4548 | 34   | 13.7817       | -                     | -                          | -                            |
| 0.4682 | 35   | 14.0178       | -                     | -                          | -                            |
| 0.4816 | 36   | 13.8457       | -                     | -                          | -                            |
| 0.4950 | 37   | 14.074        | -                     | -                          | -                            |
| 0.5084 | 38   | 13.9665       | -                     | -                          | -                            |
| 0.5217 | 39   | 13.9726       | -                     | -                          | -                            |
| 0.5351 | 40   | 13.8546       | -                     | -                          | -                            |
| 0.5485 | 41   | 13.9037       | -                     | -                          | -                            |
| 0.5619 | 42   | 13.6977       | -                     | -                          | -                            |
| 0.5753 | 43   | 14.0445       | -                     | -                          | -                            |
| 0.5886 | 44   | 13.93         | -                     | -                          | -                            |
| 0.6020 | 45   | 13.7835       | -                     | -                          | -                            |
| 0.6154 | 46   | 13.819        | -                     | -                          | -                            |
| 0.6288 | 47   | 13.6248       | -                     | -                          | -                            |
| 0.6421 | 48   | 13.846        | -                     | -                          | -                            |
| 0.6555 | 49   | 13.6079       | -                     | -                          | -                            |
| 0.6689 | 50   | 13.6848       | 0.0836                | 0.2724                     | 0.1780                       |
| 0.6823 | 51   | 13.668        | -                     | -                          | -                            |
| 0.6957 | 52   | 13.5784       | -                     | -                          | -                            |
| 0.7090 | 53   | 13.7519       | -                     | -                          | -                            |
| 0.7224 | 54   | 13.6455       | -                     | -                          | -                            |
| 0.7358 | 55   | 13.6757       | -                     | -                          | -                            |
| 0.7492 | 56   | 13.5647       | -                     | -                          | -                            |
| 0.7625 | 57   | 13.7072       | -                     | -                          | -                            |
| 0.7759 | 58   | 13.5603       | -                     | -                          | -                            |
| 0.7893 | 59   | 13.6437       | -                     | -                          | -                            |
| 0.8027 | 60   | 13.6656       | -                     | -                          | -                            |
| 0.8161 | 61   | 13.479        | -                     | -                          | -                            |
| 0.8294 | 62   | 13.5965       | -                     | -                          | -                            |
| 0.8428 | 63   | 13.6793       | -                     | -                          | -                            |
| 0.8562 | 64   | 13.6121       | -                     | -                          | -                            |
| 0.8696 | 65   | 13.841        | -                     | -                          | -                            |
| 0.8829 | 66   | 13.4793       | -                     | -                          | -                            |
| 0.8963 | 67   | 13.5875       | -                     | -                          | -                            |
| 0.9097 | 68   | 13.4063       | -                     | -                          | -                            |
| 0.9231 | 69   | 13.6365       | -                     | -                          | -                            |
| 0.9365 | 70   | 13.4696       | -                     | -                          | -                            |
| 0.9498 | 71   | 13.5018       | -                     | -                          | -                            |
| 0.9632 | 72   | 13.5956       | -                     | -                          | -                            |
| 0.9766 | 73   | 13.3945       | -                     | -                          | -                            |
| 0.9900 | 74   | 13.5684       | 0.0836                | 0.2718                     | 0.1777                       |


### Framework Versions
- Python: 3.12.3
- Sentence Transformers: 3.3.1
- Transformers: 4.49.0
- PyTorch: 2.5.1
- Accelerate: 1.2.1
- Datasets: 2.19.0
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