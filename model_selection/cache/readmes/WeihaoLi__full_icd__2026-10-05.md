---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:828486
- loss:SymmetricLoss
base_model: dmis-lab/biobert-v1.1
widget:
- source_sentence: Infectious and parasitic diseases → Viral infection
  sentences:
  - Diseases of the blood and blood-forming organs
  - Infectious and parasitic diseases
  - Diseases of the nervous system and sense organs → Central nervous system infection
- source_sentence: Neoplasms → Cancer of skin
  sentences:
  - Residual codes; unclassified; all E codes
  - Neoplasms
  - Diseases of the skin and subcutaneous tissue → Skin and subcutaneous tissue infections
- source_sentence: Endocrine; nutritional; and metabolic diseases and immunity disorders
    → Diabetes mellitus without complication
  sentences:
  - Diseases of the digestive system → Disorders of teeth and jaw
  - Certain conditions originating in the perinatal period
  - Endocrine; nutritional; and metabolic diseases and immunity disorders
- source_sentence: Complications of pregnancy; childbirth; and the puerperium → Indications
    for care in pregnancy; labor; and delivery → Malposition; malpresentation
  sentences:
  - Complications of pregnancy; childbirth; and the puerperium → Normal pregnancy
    and/or delivery → Other pregnancy and delivery including normal
  - Complications of pregnancy; childbirth; and the puerperium → Contraceptive and
    procreative management
  - Complications of pregnancy; childbirth; and the puerperium → Indications for care
    in pregnancy; labor; and delivery
- source_sentence: Mental illness → Alcohol-related disorders
  sentences:
  - Mental illness
  - Diseases of the digestive system
  - Complications of pregnancy; childbirth; and the puerperium → Abortion-related
    disorders
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# HierarchyTransformer based on dmis-lab/biobert-v1.1

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) on the csv dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) <!-- at revision 551ca18efd7f052c8dfa0b01c94c2a8e68bc5488 -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - csv
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
HierarchyTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
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
    'Mental illness → Alcohol-related disorders',
    'Mental illness',
    'Diseases of the digestive system',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.6700, 0.3739],
#         [0.6700, 1.0000, 0.4731],
#         [0.3739, 0.4731, 1.0000]])
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

#### csv

* Dataset: csv
* Size: 828,486 training samples
* Columns: <code>child</code>, <code>parent</code>, <code>parent_negative</code>, and <code>child_negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | child                                                                             | parent                                                                            | parent_negative                                                                   | child_negative                                                                     |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | string                                                                            | string                                                                             |
  | details | <ul><li>min: 8 tokens</li><li>mean: 25.09 tokens</li><li>max: 65 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 16.19 tokens</li><li>max: 41 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 16.95 tokens</li><li>max: 34 tokens</li></ul> | <ul><li>min: 11 tokens</li><li>mean: 23.47 tokens</li><li>max: 65 tokens</li></ul> |
* Samples:
  | child                                                                | parent                                         | parent_negative             | child_negative                                                                                      |
  |:---------------------------------------------------------------------|:-----------------------------------------------|:----------------------------|:----------------------------------------------------------------------------------------------------|
  | <code>Infectious and parasitic diseases → Bacterial infection</code> | <code>Infectious and parasitic diseases</code> | <code>Mental illness</code> | <code>Diseases of the nervous system and sense organs → Central nervous system infection</code>     |
  | <code>Infectious and parasitic diseases → Bacterial infection</code> | <code>Infectious and parasitic diseases</code> | <code>Mental illness</code> | <code>Diseases of the digestive system → Intestinal infection</code>                                |
  | <code>Infectious and parasitic diseases → Bacterial infection</code> | <code>Infectious and parasitic diseases</code> | <code>Mental illness</code> | <code>Diseases of the skin and subcutaneous tissue → Skin and subcutaneous tissue infections</code> |
* Loss: <code>hierarchy_transformers.losses.symmetric_loss.SymmetricLoss</code> with these parameters:
  ```json
  {
      "distance_metric": "PoincareBall(c=0.0013021096820011735).dist and dist0",
      "HyperbolicChildTriplet": {
          "weight": 1.0,
          "distance_metric": "PoincareBall(c=0.0013021096820011735).dist",
          "margin": 3.0
      },
      "HyperbolicParentTriplet": {
          "weight": 1.0,
          "distance_metric": "PoincareBall(c=0.0013021096820011735).dist",
          "margin": 3.0
      }
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: epoch
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 512
- `learning_rate`: 1e-05
- `num_train_epochs`: 10
- `warmup_steps`: 500
- `load_best_model_at_end`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: epoch
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 512
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 1e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 10
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 500
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
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `adafactor`: False
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
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
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch    | Step      | Training Loss |
|:--------:|:---------:|:-------------:|
| 0.0154   | 100       | 3.2944        |
| 0.0309   | 200       | 1.522         |
| 0.0463   | 300       | 0.8489        |
| 0.0618   | 400       | 0.6791        |
| 0.0772   | 500       | 0.6221        |
| 0.0927   | 600       | 0.5962        |
| 0.1081   | 700       | 0.5629        |
| 0.1236   | 800       | 0.539         |
| 0.1390   | 900       | 0.5304        |
| 0.1545   | 1000      | 0.4969        |
| 0.1699   | 1100      | 0.5018        |
| 0.1854   | 1200      | 0.4831        |
| 0.2008   | 1300      | 0.4931        |
| 0.2163   | 1400      | 0.5116        |
| 0.2317   | 1500      | 0.4772        |
| 0.2472   | 1600      | 0.5243        |
| 0.2626   | 1700      | 0.4928        |
| 0.2781   | 1800      | 0.5059        |
| 0.2935   | 1900      | 0.4882        |
| 0.3090   | 2000      | 0.4789        |
| 0.3244   | 2100      | 0.4652        |
| 0.3399   | 2200      | 0.4805        |
| 0.3553   | 2300      | 0.4687        |
| 0.3708   | 2400      | 0.4737        |
| 0.3862   | 2500      | 0.465         |
| 0.4017   | 2600      | 0.4675        |
| 0.4171   | 2700      | 0.4746        |
| 0.4326   | 2800      | 0.469         |
| 0.4480   | 2900      | 0.4465        |
| 0.4635   | 3000      | 0.4775        |
| 0.4789   | 3100      | 0.4643        |
| 0.4944   | 3200      | 0.4658        |
| 0.5098   | 3300      | 0.4842        |
| 0.5253   | 3400      | 0.4586        |
| 0.5407   | 3500      | 0.4685        |
| 0.5562   | 3600      | 0.4811        |
| 0.5716   | 3700      | 0.4681        |
| 0.5871   | 3800      | 0.4582        |
| 0.6025   | 3900      | 0.4461        |
| 0.6180   | 4000      | 0.4544        |
| 0.6334   | 4100      | 0.44          |
| 0.6488   | 4200      | 0.4659        |
| 0.6643   | 4300      | 0.4737        |
| 0.6797   | 4400      | 0.4442        |
| 0.6952   | 4500      | 0.4628        |
| 0.7106   | 4600      | 0.4777        |
| 0.7261   | 4700      | 0.4456        |
| 0.7415   | 4800      | 0.4296        |
| 0.7570   | 4900      | 0.4391        |
| 0.7724   | 5000      | 0.457         |
| 0.7879   | 5100      | 0.4537        |
| 0.8033   | 5200      | 0.4602        |
| 0.8188   | 5300      | 0.472         |
| 0.8342   | 5400      | 0.4473        |
| 0.8497   | 5500      | 0.4536        |
| 0.8651   | 5600      | 0.4609        |
| 0.8806   | 5700      | 0.4487        |
| 0.8960   | 5800      | 0.4462        |
| 0.9115   | 5900      | 0.4605        |
| 0.9269   | 6000      | 0.4457        |
| 0.9424   | 6100      | 0.4389        |
| 0.9578   | 6200      | 0.4324        |
| 0.9733   | 6300      | 0.446         |
| 0.9887   | 6400      | 0.4585        |
| 1.0      | 6473      | -             |
| 1.0042   | 6500      | 0.4564        |
| 1.0196   | 6600      | 0.4275        |
| 1.0351   | 6700      | 0.428         |
| 1.0505   | 6800      | 0.4591        |
| 1.0660   | 6900      | 0.4468        |
| 1.0814   | 7000      | 0.4227        |
| 1.0969   | 7100      | 0.4376        |
| 1.1123   | 7200      | 0.4527        |
| 1.1278   | 7300      | 0.4462        |
| 1.1432   | 7400      | 0.4437        |
| 1.1587   | 7500      | 0.4007        |
| 1.1741   | 7600      | 0.4394        |
| 1.1896   | 7700      | 0.4496        |
| 1.2050   | 7800      | 0.442         |
| 1.2205   | 7900      | 0.4278        |
| 1.2359   | 8000      | 0.4412        |
| 1.2514   | 8100      | 0.4284        |
| 1.2668   | 8200      | 0.4343        |
| 1.2822   | 8300      | 0.4564        |
| 1.2977   | 8400      | 0.4295        |
| 1.3131   | 8500      | 0.4353        |
| 1.3286   | 8600      | 0.4533        |
| 1.3440   | 8700      | 0.4625        |
| 1.3595   | 8800      | 0.4471        |
| 1.3749   | 8900      | 0.4447        |
| 1.3904   | 9000      | 0.449         |
| 1.4058   | 9100      | 0.4422        |
| 1.4213   | 9200      | 0.444         |
| 1.4367   | 9300      | 0.422         |
| 1.4522   | 9400      | 0.4289        |
| 1.4676   | 9500      | 0.4322        |
| 1.4831   | 9600      | 0.4633        |
| 1.4985   | 9700      | 0.4584        |
| 1.5140   | 9800      | 0.4451        |
| 1.5294   | 9900      | 0.4499        |
| 1.5449   | 10000     | 0.4437        |
| 1.5603   | 10100     | 0.4447        |
| 1.5758   | 10200     | 0.4479        |
| 1.5912   | 10300     | 0.4357        |
| 1.6067   | 10400     | 0.4413        |
| 1.6221   | 10500     | 0.4315        |
| 1.6376   | 10600     | 0.4266        |
| 1.6530   | 10700     | 0.4761        |
| 1.6685   | 10800     | 0.4316        |
| 1.6839   | 10900     | 0.4592        |
| 1.6994   | 11000     | 0.444         |
| 1.7148   | 11100     | 0.4407        |
| 1.7303   | 11200     | 0.4537        |
| 1.7457   | 11300     | 0.4286        |
| 1.7612   | 11400     | 0.4446        |
| 1.7766   | 11500     | 0.4356        |
| 1.7921   | 11600     | 0.4501        |
| 1.8075   | 11700     | 0.4364        |
| 1.8230   | 11800     | 0.4117        |
| 1.8384   | 11900     | 0.4297        |
| 1.8539   | 12000     | 0.434         |
| 1.8693   | 12100     | 0.436         |
| 1.8848   | 12200     | 0.4336        |
| 1.9002   | 12300     | 0.4394        |
| 1.9156   | 12400     | 0.4478        |
| 1.9311   | 12500     | 0.4465        |
| 1.9465   | 12600     | 0.4474        |
| 1.9620   | 12700     | 0.4462        |
| 1.9774   | 12800     | 0.4407        |
| 1.9929   | 12900     | 0.4543        |
| 2.0      | 12946     | -             |
| 2.0083   | 13000     | 0.4304        |
| 2.0238   | 13100     | 0.4301        |
| 2.0392   | 13200     | 0.439         |
| 2.0547   | 13300     | 0.4294        |
| 2.0701   | 13400     | 0.4361        |
| 2.0856   | 13500     | 0.4109        |
| 2.1010   | 13600     | 0.4417        |
| 2.1165   | 13700     | 0.4152        |
| 2.1319   | 13800     | 0.4219        |
| 2.1474   | 13900     | 0.4301        |
| 2.1628   | 14000     | 0.4427        |
| 2.1783   | 14100     | 0.4285        |
| 2.1937   | 14200     | 0.412         |
| 2.2092   | 14300     | 0.4483        |
| 2.2246   | 14400     | 0.4246        |
| 2.2401   | 14500     | 0.4415        |
| 2.2555   | 14600     | 0.4303        |
| 2.2710   | 14700     | 0.4356        |
| 2.2864   | 14800     | 0.4284        |
| 2.3019   | 14900     | 0.4483        |
| 2.3173   | 15000     | 0.438         |
| 2.3328   | 15100     | 0.4311        |
| 2.3482   | 15200     | 0.4208        |
| 2.3637   | 15300     | 0.4403        |
| 2.3791   | 15400     | 0.4205        |
| 2.3946   | 15500     | 0.4353        |
| 2.4100   | 15600     | 0.4249        |
| 2.4255   | 15700     | 0.4206        |
| 2.4409   | 15800     | 0.4456        |
| 2.4564   | 15900     | 0.4225        |
| 2.4718   | 16000     | 0.4569        |
| 2.4873   | 16100     | 0.4377        |
| 2.5027   | 16200     | 0.4353        |
| 2.5182   | 16300     | 0.4395        |
| 2.5336   | 16400     | 0.4365        |
| 2.5490   | 16500     | 0.4267        |
| 2.5645   | 16600     | 0.4186        |
| 2.5799   | 16700     | 0.4279        |
| 2.5954   | 16800     | 0.4256        |
| 2.6108   | 16900     | 0.4346        |
| 2.6263   | 17000     | 0.4337        |
| 2.6417   | 17100     | 0.4388        |
| 2.6572   | 17200     | 0.4315        |
| 2.6726   | 17300     | 0.4383        |
| 2.6881   | 17400     | 0.4324        |
| 2.7035   | 17500     | 0.4414        |
| 2.7190   | 17600     | 0.4514        |
| 2.7344   | 17700     | 0.4323        |
| 2.7499   | 17800     | 0.4469        |
| 2.7653   | 17900     | 0.4548        |
| 2.7808   | 18000     | 0.4397        |
| 2.7962   | 18100     | 0.4404        |
| 2.8117   | 18200     | 0.4265        |
| 2.8271   | 18300     | 0.4353        |
| 2.8426   | 18400     | 0.4348        |
| 2.8580   | 18500     | 0.4355        |
| 2.8735   | 18600     | 0.441         |
| 2.8889   | 18700     | 0.4257        |
| 2.9044   | 18800     | 0.4417        |
| 2.9198   | 18900     | 0.4444        |
| 2.9353   | 19000     | 0.4271        |
| 2.9507   | 19100     | 0.4258        |
| 2.9662   | 19200     | 0.4265        |
| 2.9816   | 19300     | 0.4138        |
| 2.9971   | 19400     | 0.4303        |
| 3.0      | 19419     | -             |
| 3.0125   | 19500     | 0.4192        |
| 3.0280   | 19600     | 0.4228        |
| 3.0434   | 19700     | 0.4277        |
| 3.0589   | 19800     | 0.4249        |
| 3.0743   | 19900     | 0.4336        |
| 3.0898   | 20000     | 0.4287        |
| 3.1052   | 20100     | 0.4095        |
| 3.1207   | 20200     | 0.4254        |
| 3.1361   | 20300     | 0.4098        |
| 3.1516   | 20400     | 0.4052        |
| 3.1670   | 20500     | 0.4521        |
| 3.1825   | 20600     | 0.418         |
| 3.1979   | 20700     | 0.4122        |
| 3.2133   | 20800     | 0.4512        |
| 3.2288   | 20900     | 0.4285        |
| 3.2442   | 21000     | 0.4376        |
| 3.2597   | 21100     | 0.444         |
| 3.2751   | 21200     | 0.4173        |
| 3.2906   | 21300     | 0.4143        |
| 3.3060   | 21400     | 0.4506        |
| 3.3215   | 21500     | 0.4247        |
| 3.3369   | 21600     | 0.4158        |
| 3.3524   | 21700     | 0.437         |
| 3.3678   | 21800     | 0.4158        |
| 3.3833   | 21900     | 0.4082        |
| 3.3987   | 22000     | 0.4367        |
| 3.4142   | 22100     | 0.4428        |
| 3.4296   | 22200     | 0.442         |
| 3.4451   | 22300     | 0.4283        |
| 3.4605   | 22400     | 0.4233        |
| 3.4760   | 22500     | 0.4245        |
| 3.4914   | 22600     | 0.4198        |
| 3.5069   | 22700     | 0.4317        |
| 3.5223   | 22800     | 0.4464        |
| 3.5378   | 22900     | 0.4301        |
| 3.5532   | 23000     | 0.4131        |
| 3.5687   | 23100     | 0.4201        |
| 3.5841   | 23200     | 0.4197        |
| 3.5996   | 23300     | 0.4323        |
| 3.6150   | 23400     | 0.4245        |
| 3.6305   | 23500     | 0.4276        |
| 3.6459   | 23600     | 0.4262        |
| 3.6614   | 23700     | 0.4137        |
| 3.6768   | 23800     | 0.4367        |
| 3.6923   | 23900     | 0.4397        |
| 3.7077   | 24000     | 0.4453        |
| 3.7232   | 24100     | 0.4189        |
| 3.7386   | 24200     | 0.4289        |
| 3.7541   | 24300     | 0.4135        |
| 3.7695   | 24400     | 0.4626        |
| 3.7850   | 24500     | 0.4334        |
| 3.8004   | 24600     | 0.4116        |
| 3.8159   | 24700     | 0.4383        |
| 3.8313   | 24800     | 0.4441        |
| 3.8467   | 24900     | 0.4319        |
| 3.8622   | 25000     | 0.432         |
| 3.8776   | 25100     | 0.4411        |
| 3.8931   | 25200     | 0.4208        |
| 3.9085   | 25300     | 0.4481        |
| 3.9240   | 25400     | 0.4176        |
| 3.9394   | 25500     | 0.4439        |
| 3.9549   | 25600     | 0.4032        |
| 3.9703   | 25700     | 0.4424        |
| 3.9858   | 25800     | 0.4304        |
| 4.0      | 25892     | -             |
| 4.0012   | 25900     | 0.4399        |
| 4.0167   | 26000     | 0.4048        |
| 4.0321   | 26100     | 0.4176        |
| 4.0476   | 26200     | 0.4037        |
| 4.0630   | 26300     | 0.4323        |
| 4.0785   | 26400     | 0.4319        |
| 4.0939   | 26500     | 0.4448        |
| 4.1094   | 26600     | 0.4164        |
| 4.1248   | 26700     | 0.4594        |
| 4.1403   | 26800     | 0.4314        |
| 4.1557   | 26900     | 0.4321        |
| 4.1712   | 27000     | 0.4219        |
| 4.1866   | 27100     | 0.4263        |
| 4.2021   | 27200     | 0.4348        |
| 4.2175   | 27300     | 0.4205        |
| 4.2330   | 27400     | 0.4186        |
| 4.2484   | 27500     | 0.4114        |
| 4.2639   | 27600     | 0.3989        |
| 4.2793   | 27700     | 0.4104        |
| 4.2948   | 27800     | 0.424         |
| 4.3102   | 27900     | 0.4299        |
| 4.3257   | 28000     | 0.421         |
| 4.3411   | 28100     | 0.4091        |
| 4.3566   | 28200     | 0.4177        |
| 4.3720   | 28300     | 0.4243        |
| 4.3875   | 28400     | 0.4337        |
| 4.4029   | 28500     | 0.4103        |
| 4.4184   | 28600     | 0.4258        |
| 4.4338   | 28700     | 0.4285        |
| 4.4493   | 28800     | 0.4147        |
| 4.4647   | 28900     | 0.4221        |
| 4.4801   | 29000     | 0.4272        |
| 4.4956   | 29100     | 0.4065        |
| 4.5110   | 29200     | 0.4169        |
| 4.5265   | 29300     | 0.4258        |
| 4.5419   | 29400     | 0.461         |
| 4.5574   | 29500     | 0.4553        |
| 4.5728   | 29600     | 0.4269        |
| 4.5883   | 29700     | 0.4406        |
| 4.6037   | 29800     | 0.4184        |
| 4.6192   | 29900     | 0.4287        |
| 4.6346   | 30000     | 0.4353        |
| 4.6501   | 30100     | 0.4373        |
| 4.6655   | 30200     | 0.4302        |
| 4.6810   | 30300     | 0.4301        |
| 4.6964   | 30400     | 0.4395        |
| 4.7119   | 30500     | 0.4336        |
| 4.7273   | 30600     | 0.4332        |
| 4.7428   | 30700     | 0.4161        |
| 4.7582   | 30800     | 0.4327        |
| 4.7737   | 30900     | 0.4183        |
| 4.7891   | 31000     | 0.4245        |
| 4.8046   | 31100     | 0.4448        |
| 4.8200   | 31200     | 0.4298        |
| 4.8355   | 31300     | 0.4297        |
| 4.8509   | 31400     | 0.4356        |
| 4.8664   | 31500     | 0.4342        |
| 4.8818   | 31600     | 0.4192        |
| 4.8973   | 31700     | 0.4187        |
| 4.9127   | 31800     | 0.4284        |
| 4.9282   | 31900     | 0.4486        |
| 4.9436   | 32000     | 0.4257        |
| 4.9591   | 32100     | 0.43          |
| 4.9745   | 32200     | 0.4016        |
| 4.9900   | 32300     | 0.4303        |
| 5.0      | 32365     | -             |
| 5.0054   | 32400     | 0.4059        |
| 5.0209   | 32500     | 0.4149        |
| 5.0363   | 32600     | 0.4182        |
| 5.0518   | 32700     | 0.4407        |
| 5.0672   | 32800     | 0.4166        |
| 5.0827   | 32900     | 0.4011        |
| 5.0981   | 33000     | 0.4278        |
| 5.1135   | 33100     | 0.4072        |
| 5.1290   | 33200     | 0.4161        |
| 5.1444   | 33300     | 0.4236        |
| 5.1599   | 33400     | 0.4191        |
| 5.1753   | 33500     | 0.4172        |
| 5.1908   | 33600     | 0.4228        |
| 5.2062   | 33700     | 0.4221        |
| 5.2217   | 33800     | 0.4234        |
| 5.2371   | 33900     | 0.4056        |
| 5.2526   | 34000     | 0.4284        |
| 5.2680   | 34100     | 0.4177        |
| 5.2835   | 34200     | 0.4355        |
| 5.2989   | 34300     | 0.4282        |
| 5.3144   | 34400     | 0.4183        |
| 5.3298   | 34500     | 0.4282        |
| 5.3453   | 34600     | 0.4239        |
| 5.3607   | 34700     | 0.4408        |
| 5.3762   | 34800     | 0.4237        |
| 5.3916   | 34900     | 0.4319        |
| 5.4071   | 35000     | 0.4217        |
| 5.4225   | 35100     | 0.4339        |
| 5.4380   | 35200     | 0.4227        |
| 5.4534   | 35300     | 0.4006        |
| 5.4689   | 35400     | 0.4246        |
| 5.4843   | 35500     | 0.4337        |
| 5.4998   | 35600     | 0.437         |
| 5.5152   | 35700     | 0.4288        |
| 5.5307   | 35800     | 0.4169        |
| 5.5461   | 35900     | 0.4271        |
| 5.5616   | 36000     | 0.4444        |
| 5.5770   | 36100     | 0.4094        |
| 5.5925   | 36200     | 0.4264        |
| 5.6079   | 36300     | 0.4163        |
| 5.6234   | 36400     | 0.4254        |
| 5.6388   | 36500     | 0.4129        |
| 5.6543   | 36600     | 0.4274        |
| 5.6697   | 36700     | 0.4047        |
| 5.6852   | 36800     | 0.4171        |
| 5.7006   | 36900     | 0.447         |
| 5.7161   | 37000     | 0.4175        |
| 5.7315   | 37100     | 0.4403        |
| 5.7469   | 37200     | 0.4225        |
| 5.7624   | 37300     | 0.4306        |
| 5.7778   | 37400     | 0.4294        |
| 5.7933   | 37500     | 0.4078        |
| 5.8087   | 37600     | 0.4318        |
| 5.8242   | 37700     | 0.4147        |
| 5.8396   | 37800     | 0.4303        |
| 5.8551   | 37900     | 0.4269        |
| 5.8705   | 38000     | 0.425         |
| 5.8860   | 38100     | 0.4083        |
| 5.9014   | 38200     | 0.4096        |
| 5.9169   | 38300     | 0.4326        |
| 5.9323   | 38400     | 0.4253        |
| 5.9478   | 38500     | 0.4071        |
| 5.9632   | 38600     | 0.4189        |
| 5.9787   | 38700     | 0.4213        |
| 5.9941   | 38800     | 0.4526        |
| 6.0      | 38838     | -             |
| 6.0096   | 38900     | 0.4078        |
| 6.0250   | 39000     | 0.412         |
| 6.0405   | 39100     | 0.4218        |
| 6.0559   | 39200     | 0.4212        |
| 6.0714   | 39300     | 0.3925        |
| 6.0868   | 39400     | 0.4242        |
| 6.1023   | 39500     | 0.4287        |
| 6.1177   | 39600     | 0.3917        |
| 6.1332   | 39700     | 0.4432        |
| 6.1486   | 39800     | 0.4199        |
| 6.1641   | 39900     | 0.4035        |
| 6.1795   | 40000     | 0.4078        |
| 6.1950   | 40100     | 0.4163        |
| 6.2104   | 40200     | 0.4066        |
| 6.2259   | 40300     | 0.4123        |
| 6.2413   | 40400     | 0.4235        |
| 6.2568   | 40500     | 0.4264        |
| 6.2722   | 40600     | 0.4045        |
| 6.2877   | 40700     | 0.4292        |
| 6.3031   | 40800     | 0.4341        |
| 6.3186   | 40900     | 0.4174        |
| 6.3340   | 41000     | 0.4187        |
| 6.3495   | 41100     | 0.4209        |
| 6.3649   | 41200     | 0.4216        |
| 6.3803   | 41300     | 0.4245        |
| 6.3958   | 41400     | 0.4243        |
| 6.4112   | 41500     | 0.4213        |
| 6.4267   | 41600     | 0.4317        |
| 6.4421   | 41700     | 0.4174        |
| 6.4576   | 41800     | 0.431         |
| 6.4730   | 41900     | 0.412         |
| 6.4885   | 42000     | 0.4338        |
| 6.5039   | 42100     | 0.4177        |
| 6.5194   | 42200     | 0.4109        |
| 6.5348   | 42300     | 0.4227        |
| 6.5503   | 42400     | 0.4085        |
| 6.5657   | 42500     | 0.4106        |
| 6.5812   | 42600     | 0.4192        |
| 6.5966   | 42700     | 0.4465        |
| 6.6121   | 42800     | 0.4313        |
| 6.6275   | 42900     | 0.4189        |
| 6.6430   | 43000     | 0.4055        |
| 6.6584   | 43100     | 0.4217        |
| 6.6739   | 43200     | 0.4314        |
| 6.6893   | 43300     | 0.4309        |
| 6.7048   | 43400     | 0.4336        |
| 6.7202   | 43500     | 0.4449        |
| 6.7357   | 43600     | 0.4254        |
| 6.7511   | 43700     | 0.4129        |
| 6.7666   | 43800     | 0.418         |
| 6.7820   | 43900     | 0.4417        |
| 6.7975   | 44000     | 0.4098        |
| 6.8129   | 44100     | 0.4317        |
| 6.8284   | 44200     | 0.4239        |
| 6.8438   | 44300     | 0.427         |
| 6.8593   | 44400     | 0.433         |
| 6.8747   | 44500     | 0.4136        |
| 6.8902   | 44600     | 0.4109        |
| 6.9056   | 44700     | 0.4473        |
| 6.9211   | 44800     | 0.4107        |
| 6.9365   | 44900     | 0.3969        |
| 6.9520   | 45000     | 0.4264        |
| 6.9674   | 45100     | 0.4201        |
| 6.9829   | 45200     | 0.4221        |
| 6.9983   | 45300     | 0.433         |
| 7.0      | 45311     | -             |
| 7.0137   | 45400     | 0.4142        |
| 7.0292   | 45500     | 0.4142        |
| 7.0446   | 45600     | 0.4153        |
| 7.0601   | 45700     | 0.4275        |
| 7.0755   | 45800     | 0.427         |
| 7.0910   | 45900     | 0.4135        |
| 7.1064   | 46000     | 0.4091        |
| 7.1219   | 46100     | 0.4273        |
| 7.1373   | 46200     | 0.4201        |
| 7.1528   | 46300     | 0.3999        |
| 7.1682   | 46400     | 0.42          |
| 7.1837   | 46500     | 0.427         |
| 7.1991   | 46600     | 0.4242        |
| 7.2146   | 46700     | 0.4145        |
| 7.2300   | 46800     | 0.4275        |
| 7.2455   | 46900     | 0.4303        |
| 7.2609   | 47000     | 0.4396        |
| 7.2764   | 47100     | 0.4039        |
| 7.2918   | 47200     | 0.3973        |
| 7.3073   | 47300     | 0.4301        |
| 7.3227   | 47400     | 0.4143        |
| 7.3382   | 47500     | 0.4382        |
| 7.3536   | 47600     | 0.4114        |
| 7.3691   | 47700     | 0.3986        |
| 7.3845   | 47800     | 0.4224        |
| 7.4000   | 47900     | 0.4073        |
| 7.4154   | 48000     | 0.4379        |
| 7.4309   | 48100     | 0.4276        |
| 7.4463   | 48200     | 0.3956        |
| 7.4618   | 48300     | 0.4152        |
| 7.4772   | 48400     | 0.4292        |
| 7.4927   | 48500     | 0.4268        |
| 7.5081   | 48600     | 0.4057        |
| 7.5236   | 48700     | 0.4143        |
| 7.5390   | 48800     | 0.4159        |
| 7.5545   | 48900     | 0.4096        |
| 7.5699   | 49000     | 0.4024        |
| 7.5854   | 49100     | 0.4064        |
| 7.6008   | 49200     | 0.4199        |
| 7.6163   | 49300     | 0.4326        |
| 7.6317   | 49400     | 0.4065        |
| 7.6471   | 49500     | 0.4215        |
| 7.6626   | 49600     | 0.4127        |
| 7.6780   | 49700     | 0.397         |
| 7.6935   | 49800     | 0.4357        |
| 7.7089   | 49900     | 0.436         |
| 7.7244   | 50000     | 0.432         |
| 7.7398   | 50100     | 0.4429        |
| 7.7553   | 50200     | 0.4134        |
| 7.7707   | 50300     | 0.4283        |
| 7.7862   | 50400     | 0.4056        |
| 7.8016   | 50500     | 0.4297        |
| 7.8171   | 50600     | 0.3851        |
| 7.8325   | 50700     | 0.4335        |
| 7.8480   | 50800     | 0.4203        |
| 7.8634   | 50900     | 0.4166        |
| 7.8789   | 51000     | 0.416         |
| 7.8943   | 51100     | 0.414         |
| 7.9098   | 51200     | 0.4125        |
| 7.9252   | 51300     | 0.3936        |
| 7.9407   | 51400     | 0.4197        |
| 7.9561   | 51500     | 0.4244        |
| 7.9716   | 51600     | 0.4197        |
| 7.9870   | 51700     | 0.4086        |
| 8.0      | 51784     | -             |
| 8.0025   | 51800     | 0.4356        |
| 8.0179   | 51900     | 0.4053        |
| 8.0334   | 52000     | 0.392         |
| 8.0488   | 52100     | 0.4184        |
| 8.0643   | 52200     | 0.4201        |
| 8.0797   | 52300     | 0.4213        |
| 8.0952   | 52400     | 0.4144        |
| 8.1106   | 52500     | 0.4128        |
| 8.1261   | 52600     | 0.427         |
| 8.1415   | 52700     | 0.4132        |
| 8.1570   | 52800     | 0.4211        |
| 8.1724   | 52900     | 0.4111        |
| 8.1879   | 53000     | 0.4156        |
| 8.2033   | 53100     | 0.4077        |
| 8.2188   | 53200     | 0.4164        |
| 8.2342   | 53300     | 0.4239        |
| 8.2497   | 53400     | 0.4266        |
| 8.2651   | 53500     | 0.4154        |
| 8.2805   | 53600     | 0.4258        |
| 8.2960   | 53700     | 0.411         |
| 8.3114   | 53800     | 0.4134        |
| 8.3269   | 53900     | 0.4151        |
| 8.3423   | 54000     | 0.4232        |
| 8.3578   | 54100     | 0.3976        |
| 8.3732   | 54200     | 0.4148        |
| 8.3887   | 54300     | 0.4028        |
| 8.4041   | 54400     | 0.4318        |
| 8.4196   | 54500     | 0.4248        |
| 8.4350   | 54600     | 0.4296        |
| 8.4505   | 54700     | 0.4121        |
| 8.4659   | 54800     | 0.4014        |
| 8.4814   | 54900     | 0.4141        |
| 8.4968   | 55000     | 0.4206        |
| 8.5123   | 55100     | 0.4425        |
| 8.5277   | 55200     | 0.4073        |
| 8.5432   | 55300     | 0.431         |
| 8.5586   | 55400     | 0.4134        |
| 8.5741   | 55500     | 0.4155        |
| 8.5895   | 55600     | 0.417         |
| 8.6050   | 55700     | 0.4065        |
| 8.6204   | 55800     | 0.4146        |
| 8.6359   | 55900     | 0.4167        |
| 8.6513   | 56000     | 0.4128        |
| 8.6668   | 56100     | 0.4068        |
| 8.6822   | 56200     | 0.4071        |
| 8.6977   | 56300     | 0.4333        |
| 8.7131   | 56400     | 0.425         |
| 8.7286   | 56500     | 0.422         |
| 8.7440   | 56600     | 0.4101        |
| 8.7595   | 56700     | 0.4213        |
| 8.7749   | 56800     | 0.4243        |
| 8.7904   | 56900     | 0.4298        |
| 8.8058   | 57000     | 0.4273        |
| 8.8213   | 57100     | 0.4105        |
| 8.8367   | 57200     | 0.4133        |
| 8.8522   | 57300     | 0.4106        |
| 8.8676   | 57400     | 0.4267        |
| 8.8831   | 57500     | 0.4184        |
| 8.8985   | 57600     | 0.4088        |
| 8.9140   | 57700     | 0.4262        |
| 8.9294   | 57800     | 0.4087        |
| 8.9448   | 57900     | 0.4023        |
| 8.9603   | 58000     | 0.4056        |
| 8.9757   | 58100     | 0.4072        |
| 8.9912   | 58200     | 0.4141        |
| 9.0      | 58257     | -             |
| 9.0066   | 58300     | 0.4037        |
| 9.0221   | 58400     | 0.41          |
| 9.0375   | 58500     | 0.3882        |
| 9.0530   | 58600     | 0.4224        |
| 9.0684   | 58700     | 0.3996        |
| 9.0839   | 58800     | 0.3976        |
| 9.0993   | 58900     | 0.4125        |
| 9.1148   | 59000     | 0.4288        |
| 9.1302   | 59100     | 0.4059        |
| 9.1457   | 59200     | 0.4253        |
| 9.1611   | 59300     | 0.4127        |
| 9.1766   | 59400     | 0.426         |
| 9.1920   | 59500     | 0.4131        |
| 9.2075   | 59600     | 0.3883        |
| 9.2229   | 59700     | 0.4054        |
| 9.2384   | 59800     | 0.4257        |
| 9.2538   | 59900     | 0.4218        |
| 9.2693   | 60000     | 0.4309        |
| 9.2847   | 60100     | 0.4012        |
| 9.3002   | 60200     | 0.4106        |
| 9.3156   | 60300     | 0.4219        |
| 9.3311   | 60400     | 0.4191        |
| 9.3465   | 60500     | 0.4071        |
| 9.3620   | 60600     | 0.4188        |
| 9.3774   | 60700     | 0.3959        |
| 9.3929   | 60800     | 0.423         |
| 9.4083   | 60900     | 0.4241        |
| 9.4238   | 61000     | 0.4112        |
| 9.4392   | 61100     | 0.4018        |
| 9.4547   | 61200     | 0.4066        |
| 9.4701   | 61300     | 0.4379        |
| 9.4856   | 61400     | 0.3989        |
| 9.5010   | 61500     | 0.4174        |
| 9.5165   | 61600     | 0.4064        |
| 9.5319   | 61700     | 0.4277        |
| 9.5474   | 61800     | 0.4141        |
| 9.5628   | 61900     | 0.4178        |
| 9.5782   | 62000     | 0.4197        |
| 9.5937   | 62100     | 0.4117        |
| 9.6091   | 62200     | 0.4224        |
| 9.6246   | 62300     | 0.4043        |
| 9.6400   | 62400     | 0.3922        |
| 9.6555   | 62500     | 0.4211        |
| 9.6709   | 62600     | 0.4205        |
| 9.6864   | 62700     | 0.4183        |
| 9.7018   | 62800     | 0.4238        |
| 9.7173   | 62900     | 0.4166        |
| 9.7327   | 63000     | 0.4146        |
| 9.7482   | 63100     | 0.4232        |
| 9.7636   | 63200     | 0.3956        |
| 9.7791   | 63300     | 0.3902        |
| 9.7945   | 63400     | 0.4153        |
| 9.8100   | 63500     | 0.4319        |
| 9.8254   | 63600     | 0.4337        |
| 9.8409   | 63700     | 0.4243        |
| 9.8563   | 63800     | 0.414         |
| 9.8718   | 63900     | 0.4151        |
| 9.8872   | 64000     | 0.4224        |
| 9.9027   | 64100     | 0.4379        |
| 9.9181   | 64200     | 0.4193        |
| 9.9336   | 64300     | 0.4101        |
| 9.9490   | 64400     | 0.4338        |
| 9.9645   | 64500     | 0.4321        |
| 9.9799   | 64600     | 0.42          |
| 9.9954   | 64700     | 0.4064        |
| **10.0** | **64730** | **-**         |

* The bold row denotes the saved checkpoint.
</details>

### Framework Versions
- Python: 3.10.13
- Sentence Transformers: 5.1.2
- Transformers: 4.57.1
- PyTorch: 2.9.0+cu128
- Accelerate: 1.11.0
- Datasets: 4.3.0
- Tokenizers: 0.22.1

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

#### SymmetricLoss
```bibtex
@article{he2024language,
  title={Language models as hierarchy encoders},
  author={He, Yuan and Yuan, Zhangdie and Chen, Jiaoyan and Horrocks, Ian},
  journal={arXiv preprint arXiv:2401.11374},
  year={2024}
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