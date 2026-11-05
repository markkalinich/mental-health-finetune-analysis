---
language: []
library_name: sentence-transformers
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-mpnet-base-v2
datasets: []
widget:
- source_sentence: clinician thinks the patient is homeless
  sentences:
  - '- Ms. ___ was homeless at the time of this admission.'
  - This is ___ year old single homeless woman, previously diagnosed with borderline
    personality disorder with chronic affective instability, reactive mood, impulsivity,
    SIB (ingesting objects while hospitalized), recently discharged from ___ on ___,
    ___ client, who presented to ___ on a ___ with worsening mood, threats of suicide
    via cutting her legs off, as well as thoughts of wanting to hurt _
  - Patient reports that her apartment is bugged, she has camera in her television,
    and a helicopter is reading minds.
- source_sentence: assigned a case manager for housing
  sentences:
  - 'Home With Service Facility:'
  - We consulted social work, psychiatry, and the case managers, who are working with
    the hospital attorneys to acquire safer housing options with greater oversight
    from health care professionals. .
  - Has not established care with
- source_sentence: has been homeless
  sentences:
  - He reports being homeless, living in an empty garage near his sister.
  - To complicate matters, patient's main support/roommate will be moving out of country
    soon, so he will no longer be able to live in his apartment.
  - 'Axis IV: homelessness'
- source_sentence: homelessness
  sentences:
  - Does not identify any acute stressors, but describes no longer being able to tolerate
    being homeless (lack of food/clothing/showers).
  - Unclear how reliable his group home is administering meds, notably nursing is
    quite limited.
  - Case management assisted in formulated a plan with ___ that would allow the patient's
    ___ be the first responder when issues regarding her these two problems arise.
- source_sentence: assisted…housing benefits
  sentences:
  - As a result, patient is currently homeless.
  - 'Home With Service Facility:'
  - Patient with multiple admissions in the past several months, homeless.
pipeline_tag: sentence-similarity
---

# SentenceTransformer (all-mpnet-base-v2) fine-tuned using clinical naatives

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from 
[sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2).
It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity,
semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2) <!-- at revision 84f2bcc00d77236f9e89c8a360a00fb1139bf47d -->
- **Maximum Sequence Length:** 384 tokens
- **Output Dimensionality:** 768 tokens
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->


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
model = SentenceTransformer("Shobhank-iiitdwd/Clinical_sentence_transformers_mpnet_base_v2")
# Run inference
sentences = [
    'assisted…housing benefits',
    'Home With Service Facility:',
    'Patient with multiple admissions in the past several months, homeless.',
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



### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `num_train_epochs`: 100
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 100
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
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch   | Step  | Training Loss |
|:-------:|:-----:|:-------------:|
| 0.6887  | 500   | 3.5133        |
| 1.3774  | 1000  | 3.2727        |
| 2.0661  | 1500  | 3.2238        |
| 2.7548  | 2000  | 3.1758        |
| 3.4435  | 2500  | 3.1582        |
| 4.1322  | 3000  | 3.1385        |
| 4.8209  | 3500  | 3.1155        |
| 5.5096  | 4000  | 3.1034        |
| 6.1983  | 4500  | 3.091         |
| 6.8871  | 5000  | 3.0768        |
| 7.5758  | 5500  | 3.065         |
| 8.2645  | 6000  | 3.0632        |
| 8.9532  | 6500  | 3.0566        |
| 9.6419  | 7000  | 3.0433        |
| 0.6887  | 500   | 3.0536        |
| 1.3774  | 1000  | 3.0608        |
| 2.0661  | 1500  | 3.0631        |
| 2.7548  | 2000  | 3.0644        |
| 3.4435  | 2500  | 3.0667        |
| 4.1322  | 3000  | 3.07          |
| 4.8209  | 3500  | 3.0682        |
| 5.5096  | 4000  | 3.0718        |
| 6.1983  | 4500  | 3.0719        |
| 6.8871  | 5000  | 3.0685        |
| 7.5758  | 5500  | 3.0723        |
| 8.2645  | 6000  | 3.0681        |
| 8.9532  | 6500  | 3.0633        |
| 9.6419  | 7000  | 3.0642        |
| 10.3306 | 7500  | 3.0511        |
| 11.0193 | 8000  | 3.0463        |
| 11.7080 | 8500  | 3.0301        |
| 12.3967 | 9000  | 3.0163        |
| 13.0854 | 9500  | 3.0059        |
| 13.7741 | 10000 | 2.9845        |
| 14.4628 | 10500 | 2.9705        |
| 15.1515 | 11000 | 2.9536        |
| 15.8402 | 11500 | 2.9263        |
| 16.5289 | 12000 | 2.9199        |
| 17.2176 | 12500 | 2.8989        |
| 17.9063 | 13000 | 2.8818        |
| 18.5950 | 13500 | 2.8735        |
| 19.2837 | 14000 | 2.852         |
| 19.9725 | 14500 | 2.8315        |
| 20.6612 | 15000 | 2.8095        |
| 21.3499 | 15500 | 2.7965        |
| 22.0386 | 16000 | 2.7802        |
| 22.7273 | 16500 | 2.7527        |
| 23.4160 | 17000 | 2.7547        |
| 24.1047 | 17500 | 2.7377        |
| 24.7934 | 18000 | 2.7035        |
| 25.4821 | 18500 | 2.7102        |
| 26.1708 | 19000 | 2.6997        |
| 26.8595 | 19500 | 2.6548        |
| 27.5482 | 20000 | 2.6704        |
| 28.2369 | 20500 | 2.6624        |
| 28.9256 | 21000 | 2.6306        |
| 29.6143 | 21500 | 2.6358        |
| 30.3030 | 22000 | 2.634         |
| 30.9917 | 22500 | 2.6089        |
| 31.6804 | 23000 | 2.607         |
| 32.3691 | 23500 | 2.6246        |
| 33.0579 | 24000 | 2.5947        |
| 33.7466 | 24500 | 2.5798        |
| 34.4353 | 25000 | 2.6025        |
| 35.1240 | 25500 | 2.5824        |
| 35.8127 | 26000 | 2.5698        |
| 36.5014 | 26500 | 2.5711        |
| 37.1901 | 27000 | 2.5636        |
| 37.8788 | 27500 | 2.5387        |
| 38.5675 | 28000 | 2.5472        |
| 39.2562 | 28500 | 2.5455        |
| 39.9449 | 29000 | 2.5204        |
| 40.6336 | 29500 | 2.524         |
| 41.3223 | 30000 | 2.5246        |
| 42.0110 | 30500 | 2.5125        |
| 42.6997 | 31000 | 2.5042        |
| 43.3884 | 31500 | 2.5165        |
| 44.0771 | 32000 | 2.5187        |
| 44.7658 | 32500 | 2.4975        |
| 45.4545 | 33000 | 2.5048        |
| 46.1433 | 33500 | 2.521         |
| 46.8320 | 34000 | 2.4825        |
| 47.5207 | 34500 | 2.5034        |
| 48.2094 | 35000 | 2.5049        |
| 48.8981 | 35500 | 2.4886        |
| 49.5868 | 36000 | 2.4992        |
| 50.2755 | 36500 | 2.5099        |
| 50.9642 | 37000 | 2.489         |
| 51.6529 | 37500 | 2.4825        |
| 52.3416 | 38000 | 2.4902        |
| 53.0303 | 38500 | 2.4815        |
| 53.7190 | 39000 | 2.4723        |
| 54.4077 | 39500 | 2.4921        |
| 55.0964 | 40000 | 2.4763        |
| 55.7851 | 40500 | 2.4692        |
| 56.4738 | 41000 | 2.4831        |
| 57.1625 | 41500 | 2.4705        |
| 57.8512 | 42000 | 2.4659        |
| 58.5399 | 42500 | 2.4804        |
| 59.2287 | 43000 | 2.4582        |
| 59.9174 | 43500 | 2.4544        |
| 60.6061 | 44000 | 2.4712        |
| 61.2948 | 44500 | 2.4478        |
| 61.9835 | 45000 | 2.4428        |
| 62.6722 | 45500 | 2.4558        |
| 63.3609 | 46000 | 2.4428        |
| 64.0496 | 46500 | 2.4399        |
| 64.7383 | 47000 | 2.4529        |
| 65.4270 | 47500 | 2.4374        |
| 66.1157 | 48000 | 2.4543        |
| 66.8044 | 48500 | 2.4576        |
| 67.4931 | 49000 | 2.4426        |
| 68.1818 | 49500 | 2.4698        |
| 68.8705 | 50000 | 2.4604        |
| 69.5592 | 50500 | 2.4515        |
| 70.2479 | 51000 | 2.4804        |
| 70.9366 | 51500 | 2.4545        |
| 71.6253 | 52000 | 2.4523        |
| 72.3140 | 52500 | 2.4756        |
| 73.0028 | 53000 | 2.4697        |
| 73.6915 | 53500 | 2.4536        |
| 74.3802 | 54000 | 2.4866        |
| 75.0689 | 54500 | 2.471         |
| 75.7576 | 55000 | 2.483         |
| 76.4463 | 55500 | 2.5002        |
| 77.1350 | 56000 | 2.4849        |
| 77.8237 | 56500 | 2.4848        |
| 78.5124 | 57000 | 2.5047        |
| 79.2011 | 57500 | 2.5143        |
| 79.8898 | 58000 | 2.4879        |
| 80.5785 | 58500 | 2.5093        |
| 81.2672 | 59000 | 2.5247        |
| 81.9559 | 59500 | 2.4915        |
| 82.6446 | 60000 | 2.5124        |
| 83.3333 | 60500 | 2.5056        |
| 84.0220 | 61000 | 2.4767        |
| 84.7107 | 61500 | 2.5068        |
| 85.3994 | 62000 | 2.5173        |
| 86.0882 | 62500 | 2.4911        |
| 86.7769 | 63000 | 2.526         |
| 87.4656 | 63500 | 2.5313        |
| 88.1543 | 64000 | 2.5312        |
| 88.8430 | 64500 | 2.5735        |
| 89.5317 | 65000 | 2.5873        |
| 90.2204 | 65500 | 2.6395        |
| 90.9091 | 66000 | 2.7914        |
| 91.5978 | 66500 | 2.6729        |
| 92.2865 | 67000 | 2.9846        |
| 92.9752 | 67500 | 2.9259        |
| 93.6639 | 68000 | 2.8845        |
| 94.3526 | 68500 | 2.9906        |
| 95.0413 | 69000 | 2.9534        |
| 95.7300 | 69500 | 2.9857        |
| 96.4187 | 70000 | 3.0559        |
| 97.1074 | 70500 | 2.9919        |
| 97.7961 | 71000 | 3.0435        |
| 98.4848 | 71500 | 3.0534        |
| 99.1736 | 72000 | 3.0169        |
| 99.8623 | 72500 | 3.0264        |

</details>

### Framework Versions
- Python: 3.10.11
- Sentence Transformers: 3.0.1
- Transformers: 4.41.2
- PyTorch: 2.0.1
- Accelerate: 0.31.0
- Datasets: 2.19.1
- Tokenizers: 0.19.1


