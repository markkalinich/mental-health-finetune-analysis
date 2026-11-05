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
      value: 0.802
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

| Metric              | Value     |
|:--------------------|:----------|
| **cosine_accuracy** | **0.802** |

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
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 128
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
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 128
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
| Epoch  | Step | Training Loss | triplet-dev_cosine_accuracy |
|:------:|:----:|:-------------:|:---------------------------:|
| 0      | 0    | -             | 0.58                        |
| 0.0127 | 1    | 1.677         | -                           |
| 0.0253 | 2    | 1.7295        | -                           |
| 0.0380 | 3    | 1.6713        | -                           |
| 0.0506 | 4    | 1.4761        | -                           |
| 0.0633 | 5    | 1.3731        | -                           |
| 0.0759 | 6    | 1.8333        | -                           |
| 0.0886 | 7    | 1.3218        | -                           |
| 0.1013 | 8    | 1.1539        | -                           |
| 0.1139 | 9    | 1.4003        | -                           |
| 0.1266 | 10   | 1.4514        | -                           |
| 0.1392 | 11   | 1.0803        | -                           |
| 0.1519 | 12   | 1.183         | -                           |
| 0.1646 | 13   | 0.9984        | -                           |
| 0.1772 | 14   | 1.2043        | -                           |
| 0.1899 | 15   | 1.1367        | -                           |
| 0.2025 | 16   | 1.1863        | -                           |
| 0.2152 | 17   | 1.0185        | -                           |
| 0.2278 | 18   | 0.9038        | -                           |
| 0.2405 | 19   | 0.8942        | -                           |
| 0.2532 | 20   | 1.0396        | -                           |
| 0.2658 | 21   | 1.1067        | -                           |
| 0.2785 | 22   | 1.0281        | -                           |
| 0.2911 | 23   | 1.1479        | -                           |
| 0.3038 | 24   | 1.2893        | -                           |
| 0.3165 | 25   | 1.0388        | -                           |
| 0.3291 | 26   | 1.1925        | -                           |
| 0.3418 | 27   | 0.9564        | -                           |
| 0.3544 | 28   | 0.8533        | -                           |
| 0.3671 | 29   | 0.9999        | -                           |
| 0.3797 | 30   | 1.126         | -                           |
| 0.3924 | 31   | 0.9898        | -                           |
| 0.4051 | 32   | 0.8786        | -                           |
| 0.4177 | 33   | 0.9878        | -                           |
| 0.4304 | 34   | 1.0988        | -                           |
| 0.4430 | 35   | 0.9721        | -                           |
| 0.4557 | 36   | 0.838         | -                           |
| 0.4684 | 37   | 0.9935        | -                           |
| 0.4810 | 38   | 1.1439        | -                           |
| 0.4937 | 39   | 0.7076        | -                           |
| 0.5063 | 40   | 1.0033        | -                           |
| 0.5190 | 41   | 1.0411        | -                           |
| 0.5316 | 42   | 0.8646        | -                           |
| 0.5443 | 43   | 0.8991        | -                           |
| 0.5570 | 44   | 0.6337        | -                           |
| 0.5696 | 45   | 1.0695        | -                           |
| 0.5823 | 46   | 0.9144        | -                           |
| 0.5949 | 47   | 0.9248        | -                           |
| 0.6076 | 48   | 0.7711        | -                           |
| 0.6203 | 49   | 1.0001        | -                           |
| 0.6329 | 50   | 1.0151        | -                           |
| 0.6456 | 51   | 1.06          | -                           |
| 0.6582 | 52   | 0.8105        | -                           |
| 0.6709 | 53   | 0.6892        | -                           |
| 0.6835 | 54   | 1.1341        | -                           |
| 0.6962 | 55   | 0.9726        | -                           |
| 0.7089 | 56   | 0.8783        | -                           |
| 0.7215 | 57   | 0.8084        | -                           |
| 0.7342 | 58   | 1.089         | -                           |
| 0.7468 | 59   | 0.8486        | -                           |
| 0.7595 | 60   | 0.8507        | -                           |
| 0.7722 | 61   | 0.9502        | -                           |
| 0.7848 | 62   | 0.8178        | -                           |
| 0.7975 | 63   | 1.0142        | -                           |
| 0.8101 | 64   | 0.9516        | -                           |
| 0.8228 | 65   | 0.9399        | -                           |
| 0.8354 | 66   | 0.7602        | -                           |
| 0.8481 | 67   | 0.8389        | -                           |
| 0.8608 | 68   | 0.9234        | -                           |
| 0.8734 | 69   | 0.9747        | -                           |
| 0.8861 | 70   | 1.1591        | -                           |
| 0.8987 | 71   | 1.0074        | -                           |
| 0.9114 | 72   | 0.8169        | -                           |
| 0.9241 | 73   | 0.9561        | -                           |
| 0.9367 | 74   | 0.9406        | -                           |
| 0.9494 | 75   | 0.9603        | -                           |
| 0.9620 | 76   | 0.8758        | -                           |
| 0.9747 | 77   | 0.8546        | -                           |
| 0.9873 | 78   | 0.7313        | -                           |
| 1.0    | 79   | 0.6568        | 0.802                       |


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