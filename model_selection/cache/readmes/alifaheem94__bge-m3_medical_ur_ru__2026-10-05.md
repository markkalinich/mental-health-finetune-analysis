---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:450
- loss:MultipleNegativesRankingLoss
base_model: BAAI/bge-m3
widget:
- source_sentence: What is (are) Causes of Diabetes ?
  sentences:
  - Alexander Disease ke liye kya research (ya clinical trials) ki ja rahi hai?
  - GM2-gangliosidosis, AB variant ke ilaj kya hain?
  - ذیابیطس کے (Causes) کیا ہیں؟
- source_sentence: What is (are) Clouston syndrome ?
  sentences:
  - Clouston syndrome kya hai?
  - بڑوں میں گردے کی پتھری (Kidney Stones) کے علامات کیا ہیں؟
  - کیا Citrullinemia قسم I وراثتی ہے؟
- source_sentence: What are the symptoms of Corneal dystrophy crystalline of Schnyder
    ?
  sentences:
  - Corneal dystrophy crystalline of Schnyder کے علامات کیا ہیں؟
  - پارکنسن کی بیماری کیا ہے؟
  - Stargardt disease ke asraat kya hain?
- source_sentence: what research (or clinical trials) is being done for Retinoblastoma
    ?
  sentences:
  - Wittwer syndrome کے علامات کیا ہیں؟
  - Leri Weill dyschondrosteosis کیا ہے؟
  - Retinoblastoma ke liye kaun se research (ya clinical trials) kiye ja rahe hain?
- source_sentence: What are the symptoms of Transient bullous dermolysis of the newborn
    ?
  sentences:
  - Transient bullous dermolysis of the newborn ke asraat kya hain?
  - کیا ہے (are) کارنٹائن-ایسیلکارنٹائن ٹرانسلوکیس کی کمی؟
  - (کیا) (ہیں) گھٹنے کی چوٹیں اور بیمارییں؟
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on BAAI/bge-m3

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3). It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-m3](https://huggingface.co/BAAI/bge-m3) <!-- at revision 5617a9f61b028005a4858fdac845db406aefb181 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 1024 dimensions
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
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: XLMRobertaModel 
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
model = SentenceTransformer("alifaheem94/bge-m3_medical_ur_ru")
# Run inference
sentences = [
    'What are the symptoms of Transient bullous dermolysis of the newborn ?',
    'Transient bullous dermolysis of the newborn ke asraat kya hain?',
    'کیا ہے (are) کارنٹائن-ایسیلکارنٹائن ٹرانسلوکیس کی کمی؟',
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


* Size: 450 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 450 samples:
  |         | anchor                                                                            | positive                                                                          | negative                                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | string                                                                            |
  | details | <ul><li>min: 9 tokens</li><li>mean: 15.84 tokens</li><li>max: 33 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 17.07 tokens</li><li>max: 57 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 17.29 tokens</li><li>max: 57 tokens</li></ul> |
* Samples:
  | anchor                                                                                                   | positive                                                                                                               | negative                                               |
  |:---------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------|
  | <code>How many people are affected by juvenile polyposis syndrome ?</code>                               | <code>Kitne log juvenile polyposis syndrome se mutasir hain?</code>                                                    | <code>بچوں کے Rhabdomyosarcoma کے علاج کیا ہیں؟</code> |
  | <code>What are the symptoms of Epiphyseal dysplasia multiple with early-onset diabetes mellitus ?</code> | <code>Epiphyseal dysplasia multiple کے کیا علامات ہیں جن کے ساتھ جلدی شروع ہونے والا diabetes mellitus ہوتا ہے؟</code> | <code>Glioblastoma کے علامات کیا ہیں؟</code>           |
  | <code>What are the treatments for Systemic capillary leak syndrome ?</code>                              | <code>Systemic capillary leak syndrome کے علاج کیا ہیں؟</code>                                                         | <code>Myelomeningocele ke ilaj kya hain?</code>        |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset


* Size: 25 evaluation samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 25 samples:
  |         | anchor                                                                             | positive                                                                         | negative                                                                          |
  |:--------|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                           | string                                                                            |
  | details | <ul><li>min: 10 tokens</li><li>mean: 15.92 tokens</li><li>max: 26 tokens</li></ul> | <ul><li>min: 9 tokens</li><li>mean: 17.0 tokens</li><li>max: 33 tokens</li></ul> | <ul><li>min: 10 tokens</li><li>mean: 18.4 tokens</li><li>max: 42 tokens</li></ul> |
* Samples:
  | anchor                                                      | positive                                                     | negative                                                                                 |
  |:------------------------------------------------------------|:-------------------------------------------------------------|:-----------------------------------------------------------------------------------------|
  | <code>What is (are) Causes of Diabetes ?</code>             | <code>ذیابیطس کے (Causes) کیا ہیں؟</code>                    | <code>Alexander Disease ke liye kya research (ya clinical trials) ki ja rahi hai?</code> |
  | <code>How to prevent Hypoglycemia ?</code>                  | <code>ہائپوگلیسیمیا (Hypoglycemia) کو کیسے روکا جائے؟</code> | <code>Lesch-Nyhan Syndrome کیا ہے؟</code>                                                |
  | <code>What is (are) Progressive Supranuclear Palsy ?</code> | <code>Progressive Supranuclear Palsy kya hai?</code>         | <code>بچوں میں Chronic Diarrhea کے علامات کیا ہیں؟</code>                                |
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
- `per_device_train_batch_size`: 1
- `per_device_eval_batch_size`: 1
- `num_train_epochs`: 5
- `warmup_ratio`: 0.1
- `fp16`: True
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 1
- `per_device_eval_batch_size`: 1
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
- `num_train_epochs`: 5
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
- `eval_on_start`: False
- `use_liger_kernel`: False
- `eval_use_gather_object`: False
- `prompts`: None
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step | Training Loss | Validation Loss |
|:------:|:----:|:-------------:|:---------------:|
| 0.2222 | 100  | 0.0069        | 0.0001          |
| 0.4444 | 200  | 0.0017        | 0.0002          |
| 0.6667 | 300  | 0.0072        | 0.0036          |
| 0.8889 | 400  | 0.0006        | 0.0021          |
| 1.1111 | 500  | 0.0045        | 0.0003          |
| 1.3333 | 600  | 0.0244        | 0.0041          |
| 1.5556 | 700  | 0.0094        | 0.0001          |
| 1.7778 | 800  | 0.0011        | 0.0002          |
| 2.0    | 900  | 0.0013        | 0.0002          |
| 2.2222 | 1000 | 0.0077        | 0.0007          |
| 2.4444 | 1100 | 0.0012        | 0.0014          |
| 2.6667 | 1200 | 0.0109        | 0.0000          |
| 2.8889 | 1300 | 0.0006        | 0.0000          |
| 3.1111 | 1400 | 0.0           | 0.0000          |
| 3.3333 | 1500 | 0.0079        | 0.0000          |
| 3.5556 | 1600 | 0.021         | 0.0000          |
| 3.7778 | 1700 | 0.001         | 0.0002          |
| 4.0    | 1800 | 0.0           | 0.0000          |
| 4.2222 | 1900 | 0.0088        | 0.0000          |
| 4.4444 | 2000 | 0.0           | 0.0000          |
| 4.6667 | 2100 | 0.0069        | 0.0000          |
| 4.8889 | 2200 | 0.0           | 0.0000          |


### Framework Versions
- Python: 3.10.13
- Sentence Transformers: 3.3.0
- Transformers: 4.45.2
- PyTorch: 2.2.1
- Accelerate: 1.1.1
- Datasets: 3.1.0
- Tokenizers: 0.20.3

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