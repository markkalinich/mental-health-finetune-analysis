---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:2402
- loss:TripletLoss
base_model: microsoft/MiniLM-L12-H384-uncased
widget:
- source_sentence: ' A 58-year-old man suffers a stroke and is admitted to a rehabilitation
    unit for physical therapy. He is unable to wash the left side of his body and
    denies that his left arm belongs to him even though he clearly visualizes it.'
  sentences:
  - A
  - Examination reveals that the patients somatosensory system is intact. These findings
    indicate that the patient may have a lesion. In which area of the brain is the
    lesion?n  A. Substantia nigra  B. Caudate nucleusn  C. Right parietal cortex  D.
    Left parietal cortexn  E. Right frontal cortex
  - A
- source_sentence: ' Prosopagnosia means the inability to do which of the following?'
  sentences:
  - A. Recognize faces  B. Understand written textn  C. Follow directions  D. Remember
    names  E. Read fluently
  - A
  - A
- source_sentence: ' How long should alcohol be avoided following cessation of disulfiram?'
  sentences:
  - A
  - A
  - A. 24 hours  B. 3 days  C. 7 days  D. 1 monthn  E. 3 months
- source_sentence: ' Anxiety is a normal emotional response, and a degree of anxiety
    is necessary for survival. Pathological anxiety is distinguished from a normal
    emotional response by all of the following characteristic features except: '
  sentences:
  - (
  - A. autonomy  B. physical health status  C. intensityn  D. duration  E. behavior
  - A
- source_sentence: ' Common causes of carpal tunnel syndrome include all of the following
    except:'
  sentences:
  - A
  - (
  - A. rheumatoid arthritis  B. diabetes mellitus  C. acromegalyn  D. pregnancyn  E.
    all of the above are possible causes of carpal tunnel syndrome
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on microsoft/MiniLM-L12-H384-uncased

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [microsoft/MiniLM-L12-H384-uncased](https://huggingface.co/microsoft/MiniLM-L12-H384-uncased). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [microsoft/MiniLM-L12-H384-uncased](https://huggingface.co/microsoft/MiniLM-L12-H384-uncased) <!-- at revision 44acabbec0ef496f6dbc93adadea57f376b7c0ec -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 384 dimensions
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
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("jtatman/minilm-L12-H384-psychology")
# Run inference
sentences = [
    ' Common causes of carpal tunnel syndrome include all of the following except:',
    'A',
    'A. rheumatoid arthritis  B. diabetes mellitus  C. acromegalyn  D. pregnancyn  E. all of the above are possible causes of carpal tunnel syndrome',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

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

* Size: 2,402 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>sentence_2</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                     | sentence_2                                                                         |
  |:--------|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                         | string                                                                             |
  | details | <ul><li>min: 5 tokens</li><li>mean: 33.74 tokens</li><li>max: 406 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 3.0 tokens</li><li>max: 3 tokens</li></ul> | <ul><li>min: 2 tokens</li><li>mean: 33.05 tokens</li><li>max: 205 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                          | sentence_1     | sentence_2                                                                                                                                                                                                                                       |
  |:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code> An intern on the neurology inpatient unit wonders if there is a good scale to monitor heroin withdrawal in a patient he is taking care of for suspected multiple sclerosis. Which of the following is a good instrument to monitor opioid withdrawal?</code> | <code>A</code> | <code>A. Cut down  annoyed  guilt  eye-opener (CAGE)n  B. Michigan Alcohol Screening Test (MAST)n  C. Beck Depression Inventory (BDI)n  D. Alcohol Use Disorders Identification Test (AUDIT)n  E. Clinical Opioid Withdrawal Scale (COWS)</code> |
  | <code>The words antibody and antisocial both contain the prefix anti-, which means opposite. A prefix is an example of </code>                                                                                                                                      | <code>(</code> | <code>(A)babbling.  (B)a phoneme.  (C)grammar.  (D)a morpheme</code>                                                                                                                                                                             |
  | <code> Which of the following is not a feature of generalized seizures?</code>                                                                                                                                                                                      | <code>A</code> | <code>A. Origin from a discrete region of the cerebral cortex B. Unconsciousnessn  C. Generalized EEG abnormalities  D. Bilateral occurrencen  E. Symmetric occurrence</code>                                                                    |
* Loss: [<code>TripletLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#tripletloss) with these parameters:
  ```json
  {
      "distance_metric": "TripletDistanceMetric.EUCLIDEAN",
      "triplet_margin": 5
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `num_train_epochs`: 25
- `fp16`: True
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
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
- `max_grad_norm`: 1
- `num_train_epochs`: 25
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
- `fp16`: True
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
- `multi_dataset_batch_sampler`: round_robin

</details>

### Training Logs
| Epoch   | Step | Training Loss |
|:-------:|:----:|:-------------:|
| 6.5789  | 500  | 5.6247        |
| 13.1579 | 1000 | 0.1052        |
| 19.7368 | 1500 | 0.0119        |


### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.4.1
- Transformers: 4.49.0
- PyTorch: 2.6.0+cu124
- Accelerate: 1.4.0
- Datasets: 3.3.1
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

#### TripletLoss
```bibtex
@misc{hermans2017defense,
    title={In Defense of the Triplet Loss for Person Re-Identification},
    author={Alexander Hermans and Lucas Beyer and Bastian Leibe},
    year={2017},
    eprint={1703.07737},
    archivePrefix={arXiv},
    primaryClass={cs.CV}
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