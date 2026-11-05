---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:389269
- loss:MultipleNegativesRankingLoss
base_model: ashercn97/medicalai_ClinicalBERT-2025-04-11_22-11-59
widget:
- source_sentence: 'code: 192724'
  sentences:
  - 'description: Secondary and unspecified malignant neoplasm of axilla and upper
    limb lymph nodes'
  - 'description: ROD PRE-CUT 4.5X90MM'
  - 'description: IODINE MS QN EACH SPEC Injectable Drugs Not on Fee Schedule'
- source_sentence: 'code: 985009'
  sentences:
  - 'description: SCREW VIPER SAI 10X100MM'
  - 'description: Other acute postprocedural pain'
  - 'description: BAND RLZE ADJ GSTRC'
- source_sentence: 'code: 126345'
  sentences:
  - 'description: PLATE MICRO STRAIGHT 24 HOLE 1.5 TRAUMA SYS CP TI'
  - 'description: Iron deficiency anemia, unspecified'
  - 'description: Drug-induced headache, not elsewhere classified, not intractable'
- source_sentence: 'description: Osteoarthritis'
  sentences:
  - 'description: Retention of urine, unspecified'
  - 'description: Atherosclerotic heart disease of native coronary artery without
    angina pectoris'
  - 'description: Unilateral primary osteoarthritis, left knee'
- source_sentence: 'description: Bronchiectasis'
  sentences:
  - 'description: Bronchiectasis, uncomplicated'
  - 'description: Acute on chronic systolic (congestive) heart failure'
  - 'description: Unspecified visual loss'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on ashercn97/medicalai_ClinicalBERT-2025-04-11_22-11-59

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [ashercn97/medicalai_ClinicalBERT-2025-04-11_22-11-59](https://huggingface.co/ashercn97/medicalai_ClinicalBERT-2025-04-11_22-11-59). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [ashercn97/medicalai_ClinicalBERT-2025-04-11_22-11-59](https://huggingface.co/ashercn97/medicalai_ClinicalBERT-2025-04-11_22-11-59) <!-- at revision e5dfb1ba66d5396bb5b3f817f9c8667a274dbb50 -->
- **Maximum Sequence Length:** 512 tokens
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
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: DistilBertModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': False})
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
model = SentenceTransformer("ashercn97/medical-v003")
# Run inference
sentences = [
    'description: Bronchiectasis',
    'description: Bronchiectasis, uncomplicated',
    'description: Acute on chronic systolic (congestive) heart failure',
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

* Size: 389,269 training samples
* Columns: <code>primary_code</code> and <code>description</code>
* Approximate statistics based on the first 1000 samples:
  |         | primary_code                                                                     | description                                                                       |
  |:--------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                           | string                                                                            |
  | details | <ul><li>min: 5 tokens</li><li>mean: 7.63 tokens</li><li>max: 27 tokens</li></ul> | <ul><li>min: 6 tokens</li><li>mean: 16.73 tokens</li><li>max: 69 tokens</li></ul> |
* Samples:
  | primary_code                          | description                                                               |
  |:--------------------------------------|:--------------------------------------------------------------------------|
  | <code>code: 137120</code>             | <code>description: RADIAL HEAD MOD 10X22MM</code>                         |
  | <code>description: LVEF 50-55%</code> | <code>description: Unspecified systolic (congestive) heart failure</code> |
  | <code>code: 510347</code>             | <code>description: MAG-AL UD (MAALOX)</code>                              |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset

* Size: 10,000 evaluation samples
* Columns: <code>primary_code</code> and <code>description</code>
* Approximate statistics based on the first 1000 samples:
  |         | primary_code                                                                     | description                                                                       |
  |:--------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                           | string                                                                            |
  | details | <ul><li>min: 5 tokens</li><li>mean: 7.67 tokens</li><li>max: 37 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 16.22 tokens</li><li>max: 64 tokens</li></ul> |
* Samples:
  | primary_code                                               | description                                                               |
  |:-----------------------------------------------------------|:--------------------------------------------------------------------------|
  | <code>description: Psoriasis</code>                        | <code>description: Psoriasis, unspecified</code>                          |
  | <code>description: Hodgkin Lymphoma</code>                 | <code>description: Hodgkin lymphoma, unspecified, unspecified site</code> |
  | <code>description: Cancer-related pain control plan</code> | <code>description: Neoplasm related pain (acute) (chronic)</code>         |
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
- `per_device_train_batch_size`: 512
- `per_device_eval_batch_size`: 512
- `learning_rate`: 2e-05
- `weight_decay`: 0.01
- `num_train_epochs`: 2
- `lr_scheduler_type`: cosine
- `warmup_ratio`: 0.1
- `seed`: 12
- `bf16`: True
- `dataloader_num_workers`: 64
- `dataloader_prefetch_factor`: 5
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 512
- `per_device_eval_batch_size`: 512
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.01
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 2
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
- `seed`: 12
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
- `dataloader_num_workers`: 64
- `dataloader_prefetch_factor`: 5
- `past_index`: -1
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `tp_size`: 0
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
<details><summary>Click to expand</summary>

| Epoch  | Step | Training Loss | Validation Loss |
|:------:|:----:|:-------------:|:---------------:|
| 0.0013 | 1    | 5.8248        | -               |
| 0.0066 | 5    | 5.7392        | -               |
| 0.0131 | 10   | 5.7616        | -               |
| 0.0197 | 15   | 5.771         | -               |
| 0.0263 | 20   | 5.738         | -               |
| 0.0329 | 25   | 5.6972        | -               |
| 0.0394 | 30   | 5.6486        | -               |
| 0.0460 | 35   | 5.4818        | -               |
| 0.0526 | 40   | 5.3395        | -               |
| 0.0591 | 45   | 5.3319        | -               |
| 0.0657 | 50   | 5.0993        | 1.5206          |
| 0.0723 | 55   | 5.0328        | -               |
| 0.0788 | 60   | 4.9303        | -               |
| 0.0854 | 65   | 4.8829        | -               |
| 0.0920 | 70   | 4.8534        | -               |
| 0.0986 | 75   | 4.7204        | -               |
| 0.1051 | 80   | 4.6473        | -               |
| 0.1117 | 85   | 4.5718        | -               |
| 0.1183 | 90   | 4.5464        | -               |
| 0.1248 | 95   | 4.5003        | -               |
| 0.1314 | 100  | 4.4006        | 1.2175          |
| 0.1380 | 105  | 4.3973        | -               |
| 0.1445 | 110  | 4.3876        | -               |
| 0.1511 | 115  | 4.2815        | -               |
| 0.1577 | 120  | 4.2261        | -               |
| 0.1643 | 125  | 4.2256        | -               |
| 0.1708 | 130  | 4.0866        | -               |
| 0.1774 | 135  | 4.1415        | -               |
| 0.1840 | 140  | 4.0636        | -               |
| 0.1905 | 145  | 3.993         | -               |
| 0.1971 | 150  | 3.9825        | 1.0376          |
| 0.2037 | 155  | 3.9345        | -               |
| 0.2102 | 160  | 3.8686        | -               |
| 0.2168 | 165  | 3.8343        | -               |
| 0.2234 | 170  | 3.8011        | -               |
| 0.2300 | 175  | 3.8103        | -               |
| 0.2365 | 180  | 3.7799        | -               |
| 0.2431 | 185  | 3.7414        | -               |
| 0.2497 | 190  | 3.7447        | -               |
| 0.2562 | 195  | 3.7346        | -               |
| 0.2628 | 200  | 3.622         | 0.9137          |
| 0.2694 | 205  | 3.6555        | -               |
| 0.2760 | 210  | 3.5778        | -               |
| 0.2825 | 215  | 3.6234        | -               |
| 0.2891 | 220  | 3.4653        | -               |
| 0.2957 | 225  | 3.5705        | -               |
| 0.3022 | 230  | 3.6318        | -               |
| 0.3088 | 235  | 3.5244        | -               |
| 0.3154 | 240  | 3.4487        | -               |
| 0.3219 | 245  | 3.4906        | -               |
| 0.3285 | 250  | 3.5459        | 0.8556          |
| 0.3351 | 255  | 3.3821        | -               |
| 0.3417 | 260  | 3.4249        | -               |
| 0.3482 | 265  | 3.4054        | -               |
| 0.3548 | 270  | 3.4558        | -               |
| 0.3614 | 275  | 3.3719        | -               |
| 0.3679 | 280  | 3.2999        | -               |
| 0.3745 | 285  | 3.3562        | -               |
| 0.3811 | 290  | 3.3306        | -               |
| 0.3876 | 295  | 3.2987        | -               |
| 0.3942 | 300  | 3.2789        | 0.8102          |
| 0.4008 | 305  | 3.3221        | -               |
| 0.4074 | 310  | 3.259         | -               |
| 0.4139 | 315  | 3.2014        | -               |
| 0.4205 | 320  | 3.1932        | -               |
| 0.4271 | 325  | 3.2654        | -               |
| 0.4336 | 330  | 3.1644        | -               |
| 0.4402 | 335  | 3.2603        | -               |
| 0.4468 | 340  | 3.2053        | -               |
| 0.4534 | 345  | 3.1934        | -               |
| 0.4599 | 350  | 3.138         | 0.7800          |
| 0.4665 | 355  | 3.108         | -               |
| 0.4731 | 360  | 3.1663        | -               |
| 0.4796 | 365  | 3.0978        | -               |
| 0.4862 | 370  | 3.0882        | -               |
| 0.4928 | 375  | 3.0992        | -               |
| 0.4993 | 380  | 3.1188        | -               |
| 0.5059 | 385  | 3.0937        | -               |
| 0.5125 | 390  | 3.0411        | -               |
| 0.5191 | 395  | 3.0851        | -               |
| 0.5256 | 400  | 2.9981        | 0.7582          |
| 0.5322 | 405  | 3.0407        | -               |
| 0.5388 | 410  | 2.9823        | -               |
| 0.5453 | 415  | 3.0702        | -               |
| 0.5519 | 420  | 3.0528        | -               |
| 0.5585 | 425  | 3.0542        | -               |
| 0.5650 | 430  | 3.0114        | -               |
| 0.5716 | 435  | 2.9981        | -               |
| 0.5782 | 440  | 2.9551        | -               |
| 0.5848 | 445  | 2.9857        | -               |
| 0.5913 | 450  | 2.9816        | 0.7337          |
| 0.5979 | 455  | 2.9808        | -               |
| 0.6045 | 460  | 3.001         | -               |
| 0.6110 | 465  | 2.9569        | -               |
| 0.6176 | 470  | 2.9685        | -               |
| 0.6242 | 475  | 2.8984        | -               |
| 0.6307 | 480  | 2.8961        | -               |
| 0.6373 | 485  | 2.9701        | -               |
| 0.6439 | 490  | 2.8576        | -               |
| 0.6505 | 495  | 2.9435        | -               |
| 0.6570 | 500  | 2.9025        | 0.7270          |
| 0.6636 | 505  | 2.9408        | -               |
| 0.6702 | 510  | 2.9115        | -               |
| 0.6767 | 515  | 2.8296        | -               |
| 0.6833 | 520  | 2.8089        | -               |
| 0.6899 | 525  | 2.8953        | -               |
| 0.6965 | 530  | 2.878         | -               |
| 0.7030 | 535  | 2.8488        | -               |
| 0.7096 | 540  | 2.8499        | -               |
| 0.7162 | 545  | 2.7698        | -               |
| 0.7227 | 550  | 2.8673        | 0.7193          |
| 0.7293 | 555  | 2.8058        | -               |
| 0.7359 | 560  | 2.8479        | -               |
| 0.7424 | 565  | 2.7514        | -               |
| 0.7490 | 570  | 2.8213        | -               |
| 0.7556 | 575  | 2.8438        | -               |
| 0.7622 | 580  | 2.7368        | -               |
| 0.7687 | 585  | 2.7612        | -               |
| 0.7753 | 590  | 2.8911        | -               |
| 0.7819 | 595  | 2.7759        | -               |
| 0.7884 | 600  | 2.7618        | 0.6923          |
| 0.7950 | 605  | 2.7429        | -               |
| 0.8016 | 610  | 2.7693        | -               |
| 0.8081 | 615  | 2.7278        | -               |
| 0.8147 | 620  | 2.8094        | -               |
| 0.8213 | 625  | 2.7303        | -               |
| 0.8279 | 630  | 2.7333        | -               |
| 0.8344 | 635  | 2.6704        | -               |
| 0.8410 | 640  | 2.75          | -               |
| 0.8476 | 645  | 2.7469        | -               |
| 0.8541 | 650  | 2.7348        | 0.6816          |
| 0.8607 | 655  | 2.7615        | -               |
| 0.8673 | 660  | 2.7722        | -               |
| 0.8739 | 665  | 2.765         | -               |
| 0.8804 | 670  | 2.7235        | -               |
| 0.8870 | 675  | 2.668         | -               |
| 0.8936 | 680  | 2.7102        | -               |
| 0.9001 | 685  | 2.7256        | -               |
| 0.9067 | 690  | 2.7451        | -               |
| 0.9133 | 695  | 2.1618        | -               |
| 0.9198 | 700  | 1.3555        | 0.6804          |
| 0.9264 | 705  | 1.493         | -               |
| 0.9330 | 710  | 1.3587        | -               |
| 0.9396 | 715  | 1.3546        | -               |
| 0.9461 | 720  | 1.3266        | -               |
| 0.9527 | 725  | 1.3071        | -               |
| 0.9593 | 730  | 1.2159        | -               |
| 0.9658 | 735  | 1.376         | -               |
| 0.9724 | 740  | 1.2715        | -               |
| 0.9790 | 745  | 1.4462        | -               |
| 0.9855 | 750  | 1.3423        | 0.6624          |
| 0.9921 | 755  | 1.3689        | -               |
| 0.9987 | 760  | 1.3903        | -               |
| 1.0053 | 765  | 2.43          | -               |
| 1.0118 | 770  | 2.6936        | -               |
| 1.0184 | 775  | 2.6122        | -               |
| 1.0250 | 780  | 2.6665        | -               |
| 1.0315 | 785  | 2.5816        | -               |
| 1.0381 | 790  | 2.6004        | -               |
| 1.0447 | 795  | 2.5618        | -               |
| 1.0512 | 800  | 2.5187        | 0.6604          |
| 1.0578 | 805  | 2.559         | -               |
| 1.0644 | 810  | 2.6416        | -               |
| 1.0710 | 815  | 2.5599        | -               |
| 1.0775 | 820  | 2.5993        | -               |
| 1.0841 | 825  | 2.6176        | -               |
| 1.0907 | 830  | 2.6315        | -               |
| 1.0972 | 835  | 2.5305        | -               |
| 1.1038 | 840  | 2.5624        | -               |
| 1.1104 | 845  | 2.5767        | -               |
| 1.1170 | 850  | 2.5543        | 0.6536          |
| 1.1235 | 855  | 2.5607        | -               |
| 1.1301 | 860  | 2.5992        | -               |
| 1.1367 | 865  | 2.6229        | -               |
| 1.1432 | 870  | 2.597         | -               |
| 1.1498 | 875  | 2.6013        | -               |
| 1.1564 | 880  | 2.5763        | -               |
| 1.1629 | 885  | 2.6565        | -               |
| 1.1695 | 890  | 2.5783        | -               |
| 1.1761 | 895  | 2.5474        | -               |
| 1.1827 | 900  | 2.5754        | 0.6460          |
| 1.1892 | 905  | 2.5905        | -               |
| 1.1958 | 910  | 2.6075        | -               |
| 1.2024 | 915  | 2.5284        | -               |
| 1.2089 | 920  | 2.6113        | -               |
| 1.2155 | 925  | 2.5301        | -               |
| 1.2221 | 930  | 2.5992        | -               |
| 1.2286 | 935  | 2.5951        | -               |
| 1.2352 | 940  | 2.5554        | -               |
| 1.2418 | 945  | 2.5287        | -               |
| 1.2484 | 950  | 2.4902        | 0.6411          |
| 1.2549 | 955  | 2.5829        | -               |
| 1.2615 | 960  | 2.4933        | -               |
| 1.2681 | 965  | 2.5032        | -               |
| 1.2746 | 970  | 2.579         | -               |
| 1.2812 | 975  | 2.5702        | -               |
| 1.2878 | 980  | 2.5115        | -               |
| 1.2943 | 985  | 2.5074        | -               |
| 1.3009 | 990  | 2.5588        | -               |
| 1.3075 | 995  | 2.4964        | -               |
| 1.3141 | 1000 | 2.4969        | 0.6405          |
| 1.3206 | 1005 | 2.5437        | -               |
| 1.3272 | 1010 | 2.5002        | -               |
| 1.3338 | 1015 | 2.5195        | -               |
| 1.3403 | 1020 | 2.5596        | -               |
| 1.3469 | 1025 | 2.4809        | -               |
| 1.3535 | 1030 | 2.5545        | -               |
| 1.3601 | 1035 | 2.5403        | -               |
| 1.3666 | 1040 | 2.538         | -               |
| 1.3732 | 1045 | 2.5768        | -               |
| 1.3798 | 1050 | 2.5246        | 0.6392          |
| 1.3863 | 1055 | 2.5714        | -               |
| 1.3929 | 1060 | 2.4998        | -               |
| 1.3995 | 1065 | 2.4409        | -               |
| 1.4060 | 1070 | 2.4343        | -               |
| 1.4126 | 1075 | 2.4988        | -               |
| 1.4192 | 1080 | 2.519         | -               |
| 1.4258 | 1085 | 2.5475        | -               |
| 1.4323 | 1090 | 2.5481        | -               |
| 1.4389 | 1095 | 2.5262        | -               |
| 1.4455 | 1100 | 2.5288        | 0.6356          |
| 1.4520 | 1105 | 2.4489        | -               |
| 1.4586 | 1110 | 2.5134        | -               |
| 1.4652 | 1115 | 2.5466        | -               |
| 1.4717 | 1120 | 2.5953        | -               |
| 1.4783 | 1125 | 2.5048        | -               |
| 1.4849 | 1130 | 2.5482        | -               |
| 1.4915 | 1135 | 2.5035        | -               |
| 1.4980 | 1140 | 2.4865        | -               |
| 1.5046 | 1145 | 2.436         | -               |
| 1.5112 | 1150 | 2.5097        | 0.6339          |
| 1.5177 | 1155 | 2.4402        | -               |
| 1.5243 | 1160 | 2.5121        | -               |
| 1.5309 | 1165 | 2.5289        | -               |
| 1.5375 | 1170 | 2.4334        | -               |
| 1.5440 | 1175 | 2.5176        | -               |
| 1.5506 | 1180 | 2.4507        | -               |
| 1.5572 | 1185 | 2.5162        | -               |
| 1.5637 | 1190 | 2.4426        | -               |
| 1.5703 | 1195 | 2.4526        | -               |
| 1.5769 | 1200 | 2.4578        | 0.6315          |
| 1.5834 | 1205 | 2.4775        | -               |
| 1.5900 | 1210 | 2.4659        | -               |
| 1.5966 | 1215 | 2.4884        | -               |
| 1.6032 | 1220 | 2.4713        | -               |
| 1.6097 | 1225 | 2.4861        | -               |
| 1.6163 | 1230 | 2.4817        | -               |
| 1.6229 | 1235 | 2.4861        | -               |
| 1.6294 | 1240 | 2.4207        | -               |
| 1.6360 | 1245 | 2.5191        | -               |
| 1.6426 | 1250 | 2.5891        | 0.6282          |
| 1.6491 | 1255 | 2.4916        | -               |
| 1.6557 | 1260 | 2.4456        | -               |
| 1.6623 | 1265 | 2.4901        | -               |
| 1.6689 | 1270 | 2.5061        | -               |
| 1.6754 | 1275 | 2.5172        | -               |
| 1.6820 | 1280 | 2.4396        | -               |
| 1.6886 | 1285 | 2.5093        | -               |
| 1.6951 | 1290 | 2.4524        | -               |
| 1.7017 | 1295 | 2.4564        | -               |
| 1.7083 | 1300 | 2.48          | 0.6263          |
| 1.7148 | 1305 | 2.4826        | -               |
| 1.7214 | 1310 | 2.4376        | -               |
| 1.7280 | 1315 | 2.4966        | -               |
| 1.7346 | 1320 | 2.4468        | -               |
| 1.7411 | 1325 | 2.5125        | -               |
| 1.7477 | 1330 | 2.401         | -               |
| 1.7543 | 1335 | 2.5318        | -               |
| 1.7608 | 1340 | 2.4687        | -               |
| 1.7674 | 1345 | 2.5803        | -               |
| 1.7740 | 1350 | 2.4707        | 0.6253          |
| 1.7806 | 1355 | 2.4686        | -               |
| 1.7871 | 1360 | 2.4372        | -               |
| 1.7937 | 1365 | 2.4549        | -               |
| 1.8003 | 1370 | 2.4697        | -               |
| 1.8068 | 1375 | 2.4849        | -               |
| 1.8134 | 1380 | 2.3773        | -               |
| 1.8200 | 1385 | 2.4402        | -               |
| 1.8265 | 1390 | 2.4962        | -               |
| 1.8331 | 1395 | 2.4085        | -               |
| 1.8397 | 1400 | 2.5318        | 0.6247          |
| 1.8463 | 1405 | 2.5119        | -               |
| 1.8528 | 1410 | 2.5209        | -               |
| 1.8594 | 1415 | 2.4548        | -               |
| 1.8660 | 1420 | 2.4803        | -               |
| 1.8725 | 1425 | 2.4829        | -               |
| 1.8791 | 1430 | 2.4629        | -               |
| 1.8857 | 1435 | 2.5106        | -               |
| 1.8922 | 1440 | 2.4612        | -               |
| 1.8988 | 1445 | 2.5666        | -               |
| 1.9054 | 1450 | 2.4677        | 0.6243          |
| 1.9120 | 1455 | 2.2826        | -               |
| 1.9185 | 1460 | 1.2653        | -               |
| 1.9251 | 1465 | 1.1973        | -               |
| 1.9317 | 1470 | 1.2686        | -               |
| 1.9382 | 1475 | 1.3213        | -               |
| 1.9448 | 1480 | 1.1828        | -               |
| 1.9514 | 1485 | 1.3756        | -               |
| 1.9580 | 1490 | 1.276         | -               |
| 1.9645 | 1495 | 1.1679        | -               |
| 1.9711 | 1500 | 1.1197        | 0.6244          |
| 1.9777 | 1505 | 1.3336        | -               |
| 1.9842 | 1510 | 1.2969        | -               |
| 1.9908 | 1515 | 1.1702        | -               |
| 1.9974 | 1520 | 1.0661        | -               |

</details>

### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 4.0.2
- Transformers: 4.51.2
- PyTorch: 2.6.0
- Accelerate: 1.6.0
- Datasets: 3.5.0
- Tokenizers: 0.21.1

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