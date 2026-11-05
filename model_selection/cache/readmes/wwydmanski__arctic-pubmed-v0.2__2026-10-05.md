---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:10053
- loss:MultipleNegativesRankingLoss
base_model: Snowflake/snowflake-arctic-embed-l-v2.0
widget:
- source_sentence: Nursing Reform
  sentences:
  - 'Staff nurses speak out on reform. '
  - 'Synthesis of graphene with different layers on paper-like sintered stainless
    steel fibers and its application as a metal-free catalyst for catalytic wet peroxide
    oxidation of phenol. '
  - 'Nursing reformation. '
- source_sentence: NiTiO3 composite
  sentences:
  - 'Fabrication and electromagnetic performance of talc/NiTiO 3 composite. '
  - 'Nickel-titanium usage and breakage: an update. '
  - 'Innervational plasticity of the oculomotor system. '
- source_sentence: Single-Session Competency Framework
  sentences:
  - 'Competency assessment: one step at the time. '
  - 'Optothermal molecule trapping by opposing fluid flow with thermophoretic drift. '
  - 'Describing a Clinical Group Coding Method for Identifying Competencies in an
    Allied Health Single Session. '
- source_sentence: Streptococcal myositis treatment outcomes
  sentences:
  - 'Evaluation of penicillin and hyperbaric oxygen in the treatment of streptococcal
    myositis. '
  - 'Polymicrobial myositis. '
  - 'Parse''s criteria for evaluation of theory with a comparison of Fawcett''s and
    Parse''s approaches. '
- source_sentence: Risk-based water quality monitoring framework
  sentences:
  - 'Development of a new risk-based framework to guide investment in water quality
    monitoring. '
  - 'NADPH oxidase 1 supports proliferation of colon cancer cells by modulating reactive
    oxygen species-dependent signal transduction. '
  - 'Water quality monitoring strategies - A review and future perspectives. '
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
model-index:
- name: SentenceTransformer based on Snowflake/snowflake-arctic-embed-l-v2.0
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: triplet dev
      type: triplet-dev
    metrics:
    - type: cosine_accuracy
      value: 0.72
      name: Cosine Accuracy
---

# SentenceTransformer based on Snowflake/snowflake-arctic-embed-l-v2.0

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [Snowflake/snowflake-arctic-embed-l-v2.0](https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0) on the json dataset. It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [Snowflake/snowflake-arctic-embed-l-v2.0](https://huggingface.co/Snowflake/snowflake-arctic-embed-l-v2.0) <!-- at revision 7f311bb640ad3babc0a4e3a8873240dcba44c9d2 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 1024 dimensions
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
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: PeftModelForFeatureExtraction 
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
    'Risk-based water quality monitoring framework',
    'Development of a new risk-based framework to guide investment in water quality monitoring. ',
    'Water quality monitoring strategies - A review and future perspectives. ',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 1024]

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

#### Triplet

* Dataset: `triplet-dev`
* Evaluated with [<code>TripletEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator)

| Metric              | Value    |
|:--------------------|:---------|
| **cosine_accuracy** | **0.72** |

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
* Size: 10,053 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                            | positive                                                                          | negative                                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | string                                                                            |
  | details | <ul><li>min: 4 tokens</li><li>mean: 10.58 tokens</li><li>max: 33 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 26.91 tokens</li><li>max: 79 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 15.99 tokens</li><li>max: 61 tokens</li></ul> |
* Samples:
  | anchor                                            | positive                                                                                                      | negative                                                                                                               |
  |:--------------------------------------------------|:--------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
  | <code>Pediatric Infectious Disease Control</code> | <code>[Urgent tasks in scientific studies concerning the control of infectious diseases in children]. </code> | <code>Pediatric workforce: a look at pediatric infectious diseases data from the American Board of Pediatrics. </code> |
  | <code>Thermal coefficient of phase shift</code>   | <code>Thermal characteristics of phase shift in jacketed optical fibers. </code>                              | <code>Thermal effects. </code>                                                                                         |
  | <code>Renal biomarkers in heart failure</code>    | <code>Current and novel renal biomarkers in heart failure. </code>                                            | <code>Cardiac biomarkers of heart failure in chronic kidney disease. </code>                                           |
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
- `per_device_train_batch_size`: 256
- `per_device_eval_batch_size`: 256
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
- `per_device_train_batch_size`: 256
- `per_device_eval_batch_size`: 256
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
| Epoch | Step | Training Loss | triplet-dev_cosine_accuracy |
|:-----:|:----:|:-------------:|:---------------------------:|
| 0     | 0    | -             | 0.58                        |
| 0.025 | 1    | 1.922         | -                           |
| 0.05  | 2    | 1.7637        | -                           |
| 0.075 | 3    | 1.8049        | -                           |
| 0.1   | 4    | 1.4954        | -                           |
| 0.125 | 5    | 1.7383        | -                           |
| 0.15  | 6    | 1.4773        | -                           |
| 0.175 | 7    | 1.3947        | -                           |
| 0.2   | 8    | 1.5337        | -                           |
| 0.225 | 9    | 1.2705        | -                           |
| 0.25  | 10   | 1.167         | -                           |
| 0.275 | 11   | 1.3125        | -                           |
| 0.3   | 12   | 1.4049        | -                           |
| 0.325 | 13   | 1.3382        | -                           |
| 0.35  | 14   | 1.1542        | -                           |
| 0.375 | 15   | 1.2514        | -                           |
| 0.4   | 16   | 1.1141        | -                           |
| 0.425 | 17   | 1.2267        | -                           |
| 0.45  | 18   | 1.1781        | -                           |
| 0.475 | 19   | 1.269         | -                           |
| 0.5   | 20   | 1.0684        | -                           |
| 0.525 | 21   | 1.2045        | -                           |
| 0.55  | 22   | 0.9869        | -                           |
| 0.575 | 23   | 1.2933        | -                           |
| 0.6   | 24   | 1.0751        | -                           |
| 0.625 | 25   | 1.2671        | -                           |
| 0.65  | 26   | 1.1874        | -                           |
| 0.675 | 27   | 1.241         | -                           |
| 0.7   | 28   | 1.1735        | -                           |
| 0.725 | 29   | 1.247         | -                           |
| 0.75  | 30   | 1.1166        | -                           |
| 0.775 | 31   | 1.1484        | -                           |
| 0.8   | 32   | 1.2556        | -                           |
| 0.825 | 33   | 1.1028        | -                           |
| 0.85  | 34   | 1.215         | -                           |
| 0.875 | 35   | 1.3421        | -                           |
| 0.9   | 36   | 1.1762        | -                           |
| 0.925 | 37   | 1.2029        | -                           |
| 0.95  | 38   | 1.1283        | -                           |
| 0.975 | 39   | 1.0871        | -                           |
| 1.0   | 40   | 0.7317        | 0.72                        |


### Framework Versions
- Python: 3.12.3
- Sentence Transformers: 3.3.1
- Transformers: 4.48.0.dev0
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