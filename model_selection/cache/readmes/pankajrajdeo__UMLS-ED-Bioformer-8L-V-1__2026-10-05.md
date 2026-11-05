---
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:9358675
- loss:TripletLoss
widget:
- source_sentence: acanthocephala
  sentences:
  - superficial genital wound (epidermal only)
  - spiny-headed worm, nos
  - fosfodiesterazy 3',5'-cyklicznego amp
- source_sentence: androstan-3,17-diol
  sentences:
  - >-
    forma no especificada del esteroide, normalmente un metabolito importante de
    la testosterona con actividad androgénica. ha sido relacionado con la
    regulación de la secreción de gonadotrofina.
  - 3',5'-camp 5'-ヌクレオチドヒドロラーゼ
  - hypopharyngeal fistula occluder (physical object)
- source_sentence: missbildningar, multipla
  sentences:
  - 3_3_amino_3_carboxypropyl_uridine is a modified uridine base feature.
  - acetil-coa acilasa
  - multiple congenital malformations
- source_sentence: acanthocephala
  sentences:
  - >-
    tomografía computarizada de estructuras del sistema musculoesquelético
    (procedimiento)
  - tipo acanthocephala (organismo)
  - massa; intra-abdominaal
- source_sentence: vägtrafikolyckor
  sentences:
  - trimeresurus andersoni
  - mnohočetné malformace
  - accidente vial
base_model:
- bioformers/bioformer-8L
---

# SentenceTransformer

This is a [sentence-transformers](https://www.SBERT.net) model trained. It maps sentences & paragraphs to a 512-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 512 tokens
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
  (1): Pooling({'word_embedding_dimension': 512, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("pankajrajdeo/328500_bioformer_8L")
# Run inference
sentences = [
    'vägtrafikolyckor',
    'accidente vial',
    'trimeresurus andersoni',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 512]

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


* Size: 9,358,675 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                            | positive                                                                           | negative                                                                          |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                             | string                                                                            |
  | details | <ul><li>min: 6 tokens</li><li>mean: 12.84 tokens</li><li>max: 23 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 15.45 tokens</li><li>max: 187 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 14.75 tokens</li><li>max: 91 tokens</li></ul> |
* Samples:
  | anchor                                      | positive                                                           | negative                                        |
  |:--------------------------------------------|:-------------------------------------------------------------------|:------------------------------------------------|
  | <code>(131)i-makroaggregerat albumin</code> | <code>macroagrégats d'albumine humaine marquée à l'iode 131</code> | <code>1-acylglycerophosphorylinositol</code>    |
  | <code>(131)i-makroaggregerat albumin</code> | <code>albumin, radio-iodinated serum</code>                        | <code>allo-aromadendrane-10alpha,14-diol</code> |
  | <code>(131)i-makroaggregerat albumin</code> | <code>serum albumin, radio iodinated</code>                        | <code>acquired zygomatic hyperplasia</code>     |
* Loss: [<code>TripletLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#tripletloss) with these parameters:
  ```json
  {
      "distance_metric": "TripletDistanceMetric.EUCLIDEAN",
      "triplet_margin": 5
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset


* Size: 820,102 evaluation samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                            | positive                                                                           | negative                                                                           |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                             | string                                                                             |
  | details | <ul><li>min: 3 tokens</li><li>mean: 10.54 tokens</li><li>max: 20 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 13.21 tokens</li><li>max: 183 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 14.98 tokens</li><li>max: 322 tokens</li></ul> |
* Samples:
  | anchor                                   | positive                                  | negative                                              |
  |:-----------------------------------------|:------------------------------------------|:------------------------------------------------------|
  | <code>15-ketosteryloleathydrolase</code> | <code>steroid esterase, lipoidal</code>   | <code>glutamic acid-lysine-tyrosine terpolymer</code> |
  | <code>15-ketosteryloleathydrolase</code> | <code>hydrolase, cholesterol ester</code> | <code>unionicola parvipora</code>                     |
  | <code>15-ketosteryloleathydrolase</code> | <code>acylhydrolase, sterol ester</code>  | <code>mayamaea fossalis var. fossalis</code>          |
* Loss: [<code>TripletLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#tripletloss) with these parameters:
  ```json
  {
      "distance_metric": "TripletDistanceMetric.EUCLIDEAN",
      "triplet_margin": 5
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 128
- `learning_rate`: 2e-05
- `num_train_epochs`: 10
- `warmup_ratio`: 0.1
- `fp16`: True
- `load_best_model_at_end`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 10
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
- `load_best_model_at_end`: True
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
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step   | Training Loss | loss   |
|:------:|:------:|:-------------:|:------:|
| 0.0137 | 1000   | 2.6865        | -      |
| 0.0274 | 2000   | 1.4053        | -      |
| 0.0410 | 3000   | 0.9222        | -      |
| 0.0547 | 4000   | 0.7162        | -      |
| 0.0684 | 5000   | 0.6036        | -      |
| 0.0821 | 6000   | 0.5245        | -      |
| 0.0957 | 7000   | 0.4665        | -      |
| 0.1094 | 8000   | 0.4215        | -      |
| 0.1231 | 9000   | 0.3931        | -      |
| 0.1368 | 10000  | 0.3661        | -      |
| 0.1504 | 11000  | 0.348         | -      |
| 0.1641 | 12000  | 0.3241        | -      |
| 0.1778 | 13000  | 0.3108        | -      |
| 0.1915 | 14000  | 0.2943        | -      |
| 0.2052 | 15000  | 0.2817        | -      |
| 0.2188 | 16000  | 0.2653        | -      |
| 0.2325 | 17000  | 0.2562        | -      |
| 0.2462 | 18000  | 0.2529        | -      |
| 0.2599 | 19000  | 0.2438        | -      |
| 0.2735 | 20000  | 0.2359        | -      |
| 0.2872 | 21000  | 0.2237        | -      |
| 0.3009 | 22000  | 0.2207        | -      |
| 0.3146 | 23000  | 0.2143        | -      |
| 0.3283 | 24000  | 0.2141        | -      |
| 0.3419 | 25000  | 0.2024        | -      |
| 0.3556 | 26000  | 0.196         | -      |
| 0.3693 | 27000  | 0.1951        | -      |
| 0.3830 | 28000  | 0.19          | -      |
| 0.3966 | 29000  | 0.1864        | -      |
| 0.4103 | 30000  | 0.1866        | -      |
| 0.4240 | 31000  | 0.1797        | -      |
| 0.4377 | 32000  | 0.1805        | -      |
| 0.4513 | 33000  | 0.1681        | -      |
| 0.4650 | 34000  | 0.1712        | -      |
| 0.4787 | 35000  | 0.1698        | -      |
| 0.4924 | 36000  | 0.1619        | -      |
| 0.4992 | 36500  | -             | 0.1407 |
| 0.5061 | 37000  | 0.1652        | -      |
| 0.5197 | 38000  | 0.1622        | -      |
| 0.5334 | 39000  | 0.1603        | -      |
| 0.5471 | 40000  | 0.1518        | -      |
| 0.5608 | 41000  | 0.1488        | -      |
| 0.5744 | 42000  | 0.1531        | -      |
| 0.5881 | 43000  | 0.1472        | -      |
| 0.6018 | 44000  | 0.1454        | -      |
| 0.6155 | 45000  | 0.1473        | -      |
| 0.6291 | 46000  | 0.1411        | -      |
| 0.6428 | 47000  | 0.1389        | -      |
| 0.6565 | 48000  | 0.1375        | -      |
| 0.6702 | 49000  | 0.1393        | -      |
| 0.6839 | 50000  | 0.1366        | -      |
| 0.6975 | 51000  | 0.134         | -      |
| 0.7112 | 52000  | 0.1331        | -      |
| 0.7249 | 53000  | 0.1323        | -      |
| 0.7386 | 54000  | 0.1309        | -      |
| 0.7522 | 55000  | 0.1254        | -      |
| 0.7659 | 56000  | 0.1298        | -      |
| 0.7796 | 57000  | 0.1244        | -      |
| 0.7933 | 58000  | 0.1254        | -      |
| 0.8069 | 59000  | 0.1205        | -      |
| 0.8206 | 60000  | 0.1213        | -      |
| 0.8343 | 61000  | 0.1226        | -      |
| 0.8480 | 62000  | 0.1187        | -      |
| 0.8617 | 63000  | 0.1158        | -      |
| 0.8753 | 64000  | 0.1171        | -      |
| 0.8890 | 65000  | 0.1137        | -      |
| 0.9027 | 66000  | 0.1172        | -      |
| 0.9164 | 67000  | 0.1169        | -      |
| 0.9300 | 68000  | 0.1137        | -      |
| 0.9437 | 69000  | 0.1145        | -      |
| 0.9574 | 70000  | 0.1127        | -      |
| 0.9711 | 71000  | 0.1126        | -      |
| 0.9848 | 72000  | 0.1126        | -      |
| 0.9984 | 73000  | 0.1078        | 0.0997 |
| 1.0121 | 74000  | 0.0999        | -      |
| 1.0258 | 75000  | 0.1001        | -      |
| 1.0395 | 76000  | 0.0962        | -      |
| 1.0531 | 77000  | 0.0984        | -      |
| 1.0668 | 78000  | 0.0982        | -      |
| 1.0805 | 79000  | 0.098         | -      |
| 1.0942 | 80000  | 0.0964        | -      |
| 1.1078 | 81000  | 0.0964        | -      |
| 1.1215 | 82000  | 0.0949        | -      |
| 1.1352 | 83000  | 0.0929        | -      |
| 1.1489 | 84000  | 0.0914        | -      |
| 1.1626 | 85000  | 0.0918        | -      |
| 1.1762 | 86000  | 0.0916        | -      |
| 1.1899 | 87000  | 0.0891        | -      |
| 1.2036 | 88000  | 0.0921        | -      |
| 1.2173 | 89000  | 0.0925        | -      |
| 1.2309 | 90000  | 0.091         | -      |
| 1.2446 | 91000  | 0.0875        | -      |
| 1.2583 | 92000  | 0.0898        | -      |
| 1.2720 | 93000  | 0.0856        | -      |
| 1.2856 | 94000  | 0.0866        | -      |
| 1.2993 | 95000  | 0.0843        | -      |
| 1.3130 | 96000  | 0.0848        | -      |
| 1.3267 | 97000  | 0.0872        | -      |
| 1.3404 | 98000  | 0.0853        | -      |
| 1.3540 | 99000  | 0.0898        | -      |
| 1.3677 | 100000 | 0.0831        | -      |
| 1.3814 | 101000 | 0.0819        | -      |
| 1.3951 | 102000 | 0.0842        | -      |
| 1.4087 | 103000 | 0.083         | -      |
| 1.4224 | 104000 | 0.0824        | -      |
| 1.4361 | 105000 | 0.0802        | -      |
| 1.4498 | 106000 | 0.0834        | -      |
| 1.4634 | 107000 | 0.0833        | -      |
| 1.4771 | 108000 | 0.0815        | -      |
| 1.4908 | 109000 | 0.079         | -      |
| 1.4976 | 109500 | -             | 0.0820 |
| 1.5045 | 110000 | 0.0809        | -      |
| 1.5182 | 111000 | 0.0784        | -      |
| 1.5318 | 112000 | 0.0767        | -      |
| 1.5455 | 113000 | 0.0782        | -      |
| 1.5592 | 114000 | 0.0799        | -      |
| 1.5729 | 115000 | 0.0787        | -      |
| 1.5865 | 116000 | 0.0798        | -      |
| 1.6002 | 117000 | 0.0821        | -      |
| 1.6139 | 118000 | 0.0771        | -      |
| 1.6276 | 119000 | 0.0758        | -      |
| 1.6413 | 120000 | 0.0789        | -      |
| 1.6549 | 121000 | 0.0777        | -      |
| 1.6686 | 122000 | 0.0755        | -      |
| 1.6823 | 123000 | 0.0774        | -      |
| 1.6960 | 124000 | 0.0748        | -      |
| 1.7096 | 125000 | 0.077         | -      |
| 1.7233 | 126000 | 0.0755        | -      |
| 1.7370 | 127000 | 0.0749        | -      |
| 1.7507 | 128000 | 0.0718        | -      |
| 1.7643 | 129000 | 0.0753        | -      |
| 1.7780 | 130000 | 0.0728        | -      |
| 1.7917 | 131000 | 0.0704        | -      |
| 1.8054 | 132000 | 0.0719        | -      |
| 1.8191 | 133000 | 0.0711        | -      |
| 1.8327 | 134000 | 0.0713        | -      |
| 1.8464 | 135000 | 0.0695        | -      |
| 1.8601 | 136000 | 0.0716        | -      |
| 1.8738 | 137000 | 0.0691        | -      |
| 1.8874 | 138000 | 0.0692        | -      |
| 1.9011 | 139000 | 0.0744        | -      |
| 1.9148 | 140000 | 0.0726        | -      |
| 1.9285 | 141000 | 0.0682        | -      |
| 1.9421 | 142000 | 0.0695        | -      |
| 1.9558 | 143000 | 0.0723        | -      |
| 1.9695 | 144000 | 0.0711        | -      |
| 1.9832 | 145000 | 0.0692        | -      |
| 1.9969 | 146000 | 0.0694        | 0.0704 |
| 2.0105 | 147000 | 0.0572        | -      |
| 2.0242 | 148000 | 0.0545        | -      |
| 2.0379 | 149000 | 0.0549        | -      |
| 2.0516 | 150000 | 0.0552        | -      |
| 2.0652 | 151000 | 0.0551        | -      |
| 2.0789 | 152000 | 0.0559        | -      |
| 2.0926 | 153000 | 0.0582        | -      |
| 2.1063 | 154000 | 0.0587        | -      |
| 2.1199 | 155000 | 0.0529        | -      |
| 2.1336 | 156000 | 0.059         | -      |
| 2.1473 | 157000 | 0.0534        | -      |
| 2.1610 | 158000 | 0.0547        | -      |
| 2.1747 | 159000 | 0.0543        | -      |
| 2.1883 | 160000 | 0.0558        | -      |
| 2.2020 | 161000 | 0.0548        | -      |
| 2.2157 | 162000 | 0.0534        | -      |
| 2.2294 | 163000 | 0.0548        | -      |
| 2.2430 | 164000 | 0.0546        | -      |
| 2.2567 | 165000 | 0.053         | -      |
| 2.2704 | 166000 | 0.0557        | -      |
| 2.2841 | 167000 | 0.0541        | -      |
| 2.2978 | 168000 | 0.0527        | -      |
| 2.3114 | 169000 | 0.0542        | -      |
| 2.3251 | 170000 | 0.0529        | -      |
| 2.3388 | 171000 | 0.0554        | -      |
| 2.3525 | 172000 | 0.054         | -      |
| 2.3661 | 173000 | 0.0506        | -      |
| 2.3798 | 174000 | 0.054         | -      |
| 2.3935 | 175000 | 0.0525        | -      |
| 2.4072 | 176000 | 0.0542        | -      |
| 2.4208 | 177000 | 0.0546        | -      |
| 2.4345 | 178000 | 0.0516        | -      |
| 2.4482 | 179000 | 0.053         | -      |
| 2.4619 | 180000 | 0.0542        | -      |
| 2.4756 | 181000 | 0.0538        | -      |
| 2.4892 | 182000 | 0.0536        | -      |
| 2.4961 | 182500 | -             | 0.0655 |
| 2.5029 | 183000 | 0.0489        | -      |
| 2.5166 | 184000 | 0.0543        | -      |
| 2.5303 | 185000 | 0.0509        | -      |
| 2.5439 | 186000 | 0.0525        | -      |
| 2.5576 | 187000 | 0.0525        | -      |
| 2.5713 | 188000 | 0.0535        | -      |
| 2.5850 | 189000 | 0.052         | -      |
| 2.5986 | 190000 | 0.0524        | -      |
| 2.6123 | 191000 | 0.0537        | -      |
| 2.6260 | 192000 | 0.055         | -      |
| 2.6397 | 193000 | 0.0501        | -      |
| 2.6534 | 194000 | 0.0507        | -      |
| 2.6670 | 195000 | 0.0525        | -      |
| 2.6807 | 196000 | 0.0525        | -      |
| 2.6944 | 197000 | 0.0524        | -      |
| 2.7081 | 198000 | 0.0516        | -      |
| 2.7217 | 199000 | 0.051         | -      |
| 2.7354 | 200000 | 0.0533        | -      |
| 2.7491 | 201000 | 0.0515        | -      |
| 2.7628 | 202000 | 0.0505        | -      |
| 2.7764 | 203000 | 0.0492        | -      |
| 2.7901 | 204000 | 0.0536        | -      |
| 2.8038 | 205000 | 0.0488        | -      |
| 2.8175 | 206000 | 0.0473        | -      |
| 2.8312 | 207000 | 0.0536        | -      |
| 2.8448 | 208000 | 0.0499        | -      |
| 2.8585 | 209000 | 0.0507        | -      |
| 2.8722 | 210000 | 0.0511        | -      |
| 2.8859 | 211000 | 0.0494        | -      |
| 2.8995 | 212000 | 0.0508        | -      |
| 2.9132 | 213000 | 0.0494        | -      |
| 2.9269 | 214000 | 0.048         | -      |
| 2.9406 | 215000 | 0.0494        | -      |
| 2.9543 | 216000 | 0.0511        | -      |
| 2.9679 | 217000 | 0.0498        | -      |
| 2.9816 | 218000 | 0.0487        | -      |
| 2.9953 | 219000 | 0.0486        | 0.0622 |
| 3.0090 | 220000 | 0.0403        | -      |
| 3.0226 | 221000 | 0.0353        | -      |
| 3.0363 | 222000 | 0.037         | -      |
| 3.0500 | 223000 | 0.0361        | -      |
| 3.0637 | 224000 | 0.0386        | -      |
| 3.0773 | 225000 | 0.0366        | -      |
| 3.0910 | 226000 | 0.0383        | -      |
| 3.1047 | 227000 | 0.0374        | -      |
| 3.1184 | 228000 | 0.0389        | -      |
| 3.1321 | 229000 | 0.0365        | -      |
| 3.1457 | 230000 | 0.0385        | -      |
| 3.1594 | 231000 | 0.037         | -      |
| 3.1731 | 232000 | 0.0382        | -      |
| 3.1868 | 233000 | 0.0391        | -      |
| 3.2004 | 234000 | 0.0361        | -      |
| 3.2141 | 235000 | 0.0369        | -      |
| 3.2278 | 236000 | 0.0387        | -      |
| 3.2415 | 237000 | 0.0402        | -      |
| 3.2551 | 238000 | 0.0394        | -      |
| 3.2688 | 239000 | 0.0377        | -      |
| 3.2825 | 240000 | 0.0361        | -      |
| 3.2962 | 241000 | 0.0375        | -      |
| 3.3099 | 242000 | 0.0385        | -      |
| 3.3235 | 243000 | 0.0384        | -      |
| 3.3372 | 244000 | 0.0389        | -      |
| 3.3509 | 245000 | 0.0376        | -      |
| 3.3646 | 246000 | 0.0367        | -      |
| 3.3782 | 247000 | 0.036         | -      |
| 3.3919 | 248000 | 0.0409        | -      |
| 3.4056 | 249000 | 0.0358        | -      |
| 3.4193 | 250000 | 0.0384        | -      |
| 3.4329 | 251000 | 0.0361        | -      |
| 3.4466 | 252000 | 0.0371        | -      |
| 3.4603 | 253000 | 0.0397        | -      |
| 3.4740 | 254000 | 0.0393        | -      |
| 3.4877 | 255000 | 0.0379        | -      |
| 3.4945 | 255500 | -             | 0.0609 |
| 3.5013 | 256000 | 0.0375        | -      |
| 3.5150 | 257000 | 0.0394        | -      |
| 3.5287 | 258000 | 0.0392        | -      |
| 3.5424 | 259000 | 0.0397        | -      |
| 3.5560 | 260000 | 0.036         | -      |
| 3.5697 | 261000 | 0.0368        | -      |
| 3.5834 | 262000 | 0.0388        | -      |
| 3.5971 | 263000 | 0.0395        | -      |
| 3.6108 | 264000 | 0.0392        | -      |
| 3.6244 | 265000 | 0.038         | -      |
| 3.6381 | 266000 | 0.0359        | -      |
| 3.6518 | 267000 | 0.0382        | -      |
| 3.6655 | 268000 | 0.0371        | -      |
| 3.6791 | 269000 | 0.0383        | -      |
| 3.6928 | 270000 | 0.0398        | -      |
| 3.7065 | 271000 | 0.0372        | -      |
| 3.7202 | 272000 | 0.0382        | -      |
| 3.7338 | 273000 | 0.0382        | -      |
| 3.7475 | 274000 | 0.0346        | -      |
| 3.7612 | 275000 | 0.0396        | -      |
| 3.7749 | 276000 | 0.0366        | -      |
| 3.7886 | 277000 | 0.0398        | -      |
| 3.8022 | 278000 | 0.037         | -      |
| 3.8159 | 279000 | 0.0376        | -      |
| 3.8296 | 280000 | 0.0379        | -      |
| 3.8433 | 281000 | 0.0378        | -      |
| 3.8569 | 282000 | 0.0372        | -      |
| 3.8706 | 283000 | 0.0394        | -      |
| 3.8843 | 284000 | 0.0385        | -      |
| 3.8980 | 285000 | 0.0366        | -      |
| 3.9116 | 286000 | 0.0368        | -      |
| 3.9253 | 287000 | 0.0365        | -      |
| 3.9390 | 288000 | 0.0378        | -      |
| 3.9527 | 289000 | 0.0365        | -      |
| 3.9664 | 290000 | 0.0384        | -      |
| 3.9800 | 291000 | 0.0376        | -      |
| 3.9937 | 292000 | 0.0376        | 0.0578 |
| 4.0074 | 293000 | 0.0314        | -      |
| 4.0211 | 294000 | 0.0274        | -      |
| 4.0347 | 295000 | 0.0281        | -      |
| 4.0484 | 296000 | 0.0262        | -      |
| 4.0621 | 297000 | 0.027         | -      |
| 4.0758 | 298000 | 0.0275        | -      |
| 4.0894 | 299000 | 0.0273        | -      |
| 4.1031 | 300000 | 0.0265        | -      |
| 4.1168 | 301000 | 0.0293        | -      |
| 4.1305 | 302000 | 0.0291        | -      |
| 4.1442 | 303000 | 0.0274        | -      |
| 4.1578 | 304000 | 0.0268        | -      |
| 4.1715 | 305000 | 0.0267        | -      |
| 4.1852 | 306000 | 0.0264        | -      |
| 4.1989 | 307000 | 0.0288        | -      |
| 4.2125 | 308000 | 0.0284        | -      |
| 4.2262 | 309000 | 0.0279        | -      |
| 4.2399 | 310000 | 0.0283        | -      |
| 4.2536 | 311000 | 0.0283        | -      |
| 4.2673 | 312000 | 0.0308        | -      |
| 4.2809 | 313000 | 0.0284        | -      |
| 4.2946 | 314000 | 0.0266        | -      |
| 4.3083 | 315000 | 0.0268        | -      |
| 4.3220 | 316000 | 0.0272        | -      |
| 4.3356 | 317000 | 0.0293        | -      |
| 4.3493 | 318000 | 0.0258        | -      |
| 4.3630 | 319000 | 0.0302        | -      |
| 4.3767 | 320000 | 0.0272        | -      |
| 4.3903 | 321000 | 0.0287        | -      |
| 4.4040 | 322000 | 0.0283        | -      |
| 4.4177 | 323000 | 0.0279        | -      |
| 4.4314 | 324000 | 0.0284        | -      |
| 4.4451 | 325000 | 0.0272        | -      |
| 4.4587 | 326000 | 0.0285        | -      |
| 4.4724 | 327000 | 0.028         | -      |
| 4.4861 | 328000 | 0.0265        | -      |
| 4.4929 | 328500 | -             | 0.0567 |

</details>

### Framework Versions
- Python: 3.9.16
- Sentence Transformers: 3.1.1
- Transformers: 4.45.2
- PyTorch: 2.4.1+cu121
- Accelerate: 1.0.0
- Datasets: 3.0.1
- Tokenizers: 0.20.0

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