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
- bioformers/bioformer-16L
---

# SentenceTransformer

This is a [sentence-transformers](https://www.SBERT.net) model trained. It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
- **Maximum Sequence Length:** 1024 tokens
- **Output Dimensionality:** 384 tokens
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
  (0): Transformer({'max_seq_length': 1024, 'do_lower_case': False}) with Transformer model: BertModel 
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
model = SentenceTransformer("pankajrajdeo/328500_bioformer_16L")
# Run inference
sentences = [
    'vägtrafikolyckor',
    'accidente vial',
    'trimeresurus andersoni',
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
| 0.0137 | 1000   | 2.7368        | -      |
| 0.0274 | 2000   | 1.4396        | -      |
| 0.0410 | 3000   | 0.8916        | -      |
| 0.0547 | 4000   | 0.6669        | -      |
| 0.0684 | 5000   | 0.553         | -      |
| 0.0821 | 6000   | 0.4759        | -      |
| 0.0957 | 7000   | 0.4206        | -      |
| 0.1094 | 8000   | 0.3808        | -      |
| 0.1231 | 9000   | 0.3543        | -      |
| 0.1368 | 10000  | 0.3281        | -      |
| 0.1504 | 11000  | 0.3126        | -      |
| 0.1641 | 12000  | 0.2923        | -      |
| 0.1778 | 13000  | 0.2762        | -      |
| 0.1915 | 14000  | 0.2617        | -      |
| 0.2052 | 15000  | 0.2488        | -      |
| 0.2188 | 16000  | 0.2363        | -      |
| 0.2325 | 17000  | 0.2291        | -      |
| 0.2462 | 18000  | 0.2235        | -      |
| 0.2599 | 19000  | 0.2175        | -      |
| 0.2735 | 20000  | 0.2077        | -      |
| 0.2872 | 21000  | 0.2014        | -      |
| 0.3009 | 22000  | 0.1944        | -      |
| 0.3146 | 23000  | 0.1895        | -      |
| 0.3283 | 24000  | 0.1889        | -      |
| 0.3419 | 25000  | 0.1795        | -      |
| 0.3556 | 26000  | 0.1769        | -      |
| 0.3693 | 27000  | 0.1743        | -      |
| 0.3830 | 28000  | 0.1691        | -      |
| 0.3966 | 29000  | 0.1652        | -      |
| 0.4103 | 30000  | 0.1654        | -      |
| 0.4240 | 31000  | 0.1625        | -      |
| 0.4377 | 32000  | 0.1614        | -      |
| 0.4513 | 33000  | 0.1513        | -      |
| 0.4650 | 34000  | 0.1527        | -      |
| 0.4787 | 35000  | 0.1496        | -      |
| 0.4924 | 36000  | 0.143         | -      |
| 0.4992 | 36500  | -             | 0.1243 |
| 0.5061 | 37000  | 0.1493        | -      |
| 0.5197 | 38000  | 0.1467        | -      |
| 0.5334 | 39000  | 0.1407        | -      |
| 0.5471 | 40000  | 0.1364        | -      |
| 0.5608 | 41000  | 0.1333        | -      |
| 0.5744 | 42000  | 0.1378        | -      |
| 0.5881 | 43000  | 0.1322        | -      |
| 0.6018 | 44000  | 0.1304        | -      |
| 0.6155 | 45000  | 0.1308        | -      |
| 0.6291 | 46000  | 0.1254        | -      |
| 0.6428 | 47000  | 0.1251        | -      |
| 0.6565 | 48000  | 0.1256        | -      |
| 0.6702 | 49000  | 0.1247        | -      |
| 0.6839 | 50000  | 0.1225        | -      |
| 0.6975 | 51000  | 0.1194        | -      |
| 0.7112 | 52000  | 0.125         | -      |
| 0.7249 | 53000  | 0.1206        | -      |
| 0.7386 | 54000  | 0.1184        | -      |
| 0.7522 | 55000  | 0.1134        | -      |
| 0.7659 | 56000  | 0.1192        | -      |
| 0.7796 | 57000  | 0.1134        | -      |
| 0.7933 | 58000  | 0.1133        | -      |
| 0.8069 | 59000  | 0.1104        | -      |
| 0.8206 | 60000  | 0.111         | -      |
| 0.8343 | 61000  | 0.1129        | -      |
| 0.8480 | 62000  | 0.1098        | -      |
| 0.8617 | 63000  | 0.1078        | -      |
| 0.8753 | 64000  | 0.1096        | -      |
| 0.8890 | 65000  | 0.1027        | -      |
| 0.9027 | 66000  | 0.1097        | -      |
| 0.9164 | 67000  | 0.109         | -      |
| 0.9300 | 68000  | 0.1075        | -      |
| 0.9437 | 69000  | 0.1036        | -      |
| 0.9574 | 70000  | 0.1025        | -      |
| 0.9711 | 71000  | 0.1056        | -      |
| 0.9848 | 72000  | 0.1055        | -      |
| 0.9984 | 73000  | 0.1021        | 0.0950 |
| 1.0121 | 74000  | 0.097         | -      |
| 1.0258 | 75000  | 0.0931        | -      |
| 1.0395 | 76000  | 0.089         | -      |
| 1.0531 | 77000  | 0.0927        | -      |
| 1.0668 | 78000  | 0.09          | -      |
| 1.0805 | 79000  | 0.0922        | -      |
| 1.0942 | 80000  | 0.0905        | -      |
| 1.1078 | 81000  | 0.0907        | -      |
| 1.1215 | 82000  | 0.0885        | -      |
| 1.1352 | 83000  | 0.0877        | -      |
| 1.1489 | 84000  | 0.085         | -      |
| 1.1626 | 85000  | 0.0859        | -      |
| 1.1762 | 86000  | 0.087         | -      |
| 1.1899 | 87000  | 0.0851        | -      |
| 1.2036 | 88000  | 0.0878        | -      |
| 1.2173 | 89000  | 0.0873        | -      |
| 1.2309 | 90000  | 0.0876        | -      |
| 1.2446 | 91000  | 0.0838        | -      |
| 1.2583 | 92000  | 0.0856        | -      |
| 1.2720 | 93000  | 0.0818        | -      |
| 1.2856 | 94000  | 0.0835        | -      |
| 1.2993 | 95000  | 0.081         | -      |
| 1.3130 | 96000  | 0.0797        | -      |
| 1.3267 | 97000  | 0.0811        | -      |
| 1.3404 | 98000  | 0.0802        | -      |
| 1.3540 | 99000  | 0.0844        | -      |
| 1.3677 | 100000 | 0.0787        | -      |
| 1.3814 | 101000 | 0.0773        | -      |
| 1.3951 | 102000 | 0.0802        | -      |
| 1.4087 | 103000 | 0.0801        | -      |
| 1.4224 | 104000 | 0.0762        | -      |
| 1.4361 | 105000 | 0.0755        | -      |
| 1.4498 | 106000 | 0.0791        | -      |
| 1.4634 | 107000 | 0.0806        | -      |
| 1.4771 | 108000 | 0.0756        | -      |
| 1.4908 | 109000 | 0.0771        | -      |
| 1.4976 | 109500 | -             | 0.0779 |
| 1.5045 | 110000 | 0.0773        | -      |
| 1.5182 | 111000 | 0.0769        | -      |
| 1.5318 | 112000 | 0.0738        | -      |
| 1.5455 | 113000 | 0.0765        | -      |
| 1.5592 | 114000 | 0.0758        | -      |
| 1.5729 | 115000 | 0.0759        | -      |
| 1.5865 | 116000 | 0.0766        | -      |
| 1.6002 | 117000 | 0.077         | -      |
| 1.6139 | 118000 | 0.0755        | -      |
| 1.6276 | 119000 | 0.0733        | -      |
| 1.6413 | 120000 | 0.0753        | -      |
| 1.6549 | 121000 | 0.0747        | -      |
| 1.6686 | 122000 | 0.0733        | -      |
| 1.6823 | 123000 | 0.0729        | -      |
| 1.6960 | 124000 | 0.0705        | -      |
| 1.7096 | 125000 | 0.0745        | -      |
| 1.7233 | 126000 | 0.0726        | -      |
| 1.7370 | 127000 | 0.0717        | -      |
| 1.7507 | 128000 | 0.0687        | -      |
| 1.7643 | 129000 | 0.0715        | -      |
| 1.7780 | 130000 | 0.0701        | -      |
| 1.7917 | 131000 | 0.0671        | -      |
| 1.8054 | 132000 | 0.07          | -      |
| 1.8191 | 133000 | 0.0683        | -      |
| 1.8327 | 134000 | 0.0684        | -      |
| 1.8464 | 135000 | 0.0668        | -      |
| 1.8601 | 136000 | 0.0681        | -      |
| 1.8738 | 137000 | 0.0668        | -      |
| 1.8874 | 138000 | 0.0655        | -      |
| 1.9011 | 139000 | 0.0698        | -      |
| 1.9148 | 140000 | 0.0692        | -      |
| 1.9285 | 141000 | 0.0667        | -      |
| 1.9421 | 142000 | 0.0662        | -      |
| 1.9558 | 143000 | 0.0695        | -      |
| 1.9695 | 144000 | 0.0663        | -      |
| 1.9832 | 145000 | 0.0669        | -      |
| 1.9969 | 146000 | 0.0661        | 0.0686 |
| 2.0105 | 147000 | 0.0553        | -      |
| 2.0242 | 148000 | 0.0521        | -      |
| 2.0379 | 149000 | 0.053         | -      |
| 2.0516 | 150000 | 0.0531        | -      |
| 2.0652 | 151000 | 0.0529        | -      |
| 2.0789 | 152000 | 0.0519        | -      |
| 2.0926 | 153000 | 0.0548        | -      |
| 2.1063 | 154000 | 0.0549        | -      |
| 2.1199 | 155000 | 0.0525        | -      |
| 2.1336 | 156000 | 0.056         | -      |
| 2.1473 | 157000 | 0.0514        | -      |
| 2.1610 | 158000 | 0.0526        | -      |
| 2.1747 | 159000 | 0.0512        | -      |
| 2.1883 | 160000 | 0.0526        | -      |
| 2.2020 | 161000 | 0.0524        | -      |
| 2.2157 | 162000 | 0.052         | -      |
| 2.2294 | 163000 | 0.0526        | -      |
| 2.2430 | 164000 | 0.0531        | -      |
| 2.2567 | 165000 | 0.0522        | -      |
| 2.2704 | 166000 | 0.0536        | -      |
| 2.2841 | 167000 | 0.0505        | -      |
| 2.2978 | 168000 | 0.0521        | -      |
| 2.3114 | 169000 | 0.0518        | -      |
| 2.3251 | 170000 | 0.0497        | -      |
| 2.3388 | 171000 | 0.0534        | -      |
| 2.3525 | 172000 | 0.0518        | -      |
| 2.3661 | 173000 | 0.0502        | -      |
| 2.3798 | 174000 | 0.053         | -      |
| 2.3935 | 175000 | 0.0515        | -      |
| 2.4072 | 176000 | 0.0503        | -      |
| 2.4208 | 177000 | 0.0526        | -      |
| 2.4345 | 178000 | 0.0497        | -      |
| 2.4482 | 179000 | 0.0524        | -      |
| 2.4619 | 180000 | 0.0517        | -      |
| 2.4756 | 181000 | 0.0522        | -      |
| 2.4892 | 182000 | 0.0536        | -      |
| 2.4961 | 182500 | -             | 0.0635 |
| 2.5029 | 183000 | 0.0474        | -      |
| 2.5166 | 184000 | 0.0519        | -      |
| 2.5303 | 185000 | 0.0474        | -      |
| 2.5439 | 186000 | 0.0503        | -      |
| 2.5576 | 187000 | 0.0506        | -      |
| 2.5713 | 188000 | 0.0489        | -      |
| 2.5850 | 189000 | 0.0497        | -      |
| 2.5986 | 190000 | 0.0501        | -      |
| 2.6123 | 191000 | 0.0516        | -      |
| 2.6260 | 192000 | 0.052         | -      |
| 2.6397 | 193000 | 0.0477        | -      |
| 2.6534 | 194000 | 0.049         | -      |
| 2.6670 | 195000 | 0.0497        | -      |
| 2.6807 | 196000 | 0.049         | -      |
| 2.6944 | 197000 | 0.0496        | -      |
| 2.7081 | 198000 | 0.0522        | -      |
| 2.7217 | 199000 | 0.0475        | -      |
| 2.7354 | 200000 | 0.0499        | -      |
| 2.7491 | 201000 | 0.0501        | -      |
| 2.7628 | 202000 | 0.0468        | -      |
| 2.7764 | 203000 | 0.0491        | -      |
| 2.7901 | 204000 | 0.0515        | -      |
| 2.8038 | 205000 | 0.0485        | -      |
| 2.8175 | 206000 | 0.0458        | -      |
| 2.8312 | 207000 | 0.0502        | -      |
| 2.8448 | 208000 | 0.048         | -      |
| 2.8585 | 209000 | 0.0485        | -      |
| 2.8722 | 210000 | 0.0493        | -      |
| 2.8859 | 211000 | 0.0462        | -      |
| 2.8995 | 212000 | 0.048         | -      |
| 2.9132 | 213000 | 0.0475        | -      |
| 2.9269 | 214000 | 0.0459        | -      |
| 2.9406 | 215000 | 0.0487        | -      |
| 2.9543 | 216000 | 0.0487        | -      |
| 2.9679 | 217000 | 0.047         | -      |
| 2.9816 | 218000 | 0.048         | -      |
| 2.9953 | 219000 | 0.0472        | 0.0592 |
| 3.0090 | 220000 | 0.0398        | -      |
| 3.0226 | 221000 | 0.0353        | -      |
| 3.0363 | 222000 | 0.0354        | -      |
| 3.0500 | 223000 | 0.0361        | -      |
| 3.0637 | 224000 | 0.0367        | -      |
| 3.0773 | 225000 | 0.0375        | -      |
| 3.0910 | 226000 | 0.037         | -      |
| 3.1047 | 227000 | 0.0358        | -      |
| 3.1184 | 228000 | 0.0372        | -      |
| 3.1321 | 229000 | 0.0365        | -      |
| 3.1457 | 230000 | 0.0389        | -      |
| 3.1594 | 231000 | 0.0372        | -      |
| 3.1731 | 232000 | 0.0345        | -      |
| 3.1868 | 233000 | 0.0383        | -      |
| 3.2004 | 234000 | 0.0337        | -      |
| 3.2141 | 235000 | 0.0348        | -      |
| 3.2278 | 236000 | 0.0376        | -      |
| 3.2415 | 237000 | 0.0394        | -      |
| 3.2551 | 238000 | 0.0378        | -      |
| 3.2688 | 239000 | 0.0358        | -      |
| 3.2825 | 240000 | 0.0344        | -      |
| 3.2962 | 241000 | 0.0363        | -      |
| 3.3099 | 242000 | 0.0373        | -      |
| 3.3235 | 243000 | 0.0371        | -      |
| 3.3372 | 244000 | 0.0375        | -      |
| 3.3509 | 245000 | 0.0365        | -      |
| 3.3646 | 246000 | 0.0362        | -      |
| 3.3782 | 247000 | 0.0365        | -      |
| 3.3919 | 248000 | 0.0386        | -      |
| 3.4056 | 249000 | 0.0337        | -      |
| 3.4193 | 250000 | 0.0382        | -      |
| 3.4329 | 251000 | 0.0353        | -      |
| 3.4466 | 252000 | 0.0349        | -      |
| 3.4603 | 253000 | 0.0373        | -      |
| 3.4740 | 254000 | 0.0374        | -      |
| 3.4877 | 255000 | 0.036         | -      |
| 3.4945 | 255500 | -             | 0.0561 |
| 3.5013 | 256000 | 0.0357        | -      |
| 3.5150 | 257000 | 0.0375        | -      |
| 3.5287 | 258000 | 0.0372        | -      |
| 3.5424 | 259000 | 0.0371        | -      |
| 3.5560 | 260000 | 0.0364        | -      |
| 3.5697 | 261000 | 0.037         | -      |
| 3.5834 | 262000 | 0.0375        | -      |
| 3.5971 | 263000 | 0.0369        | -      |
| 3.6108 | 264000 | 0.0367        | -      |
| 3.6244 | 265000 | 0.0359        | -      |
| 3.6381 | 266000 | 0.0353        | -      |
| 3.6518 | 267000 | 0.0356        | -      |
| 3.6655 | 268000 | 0.0362        | -      |
| 3.6791 | 269000 | 0.0365        | -      |
| 3.6928 | 270000 | 0.0395        | -      |
| 3.7065 | 271000 | 0.0352        | -      |
| 3.7202 | 272000 | 0.0366        | -      |
| 3.7338 | 273000 | 0.0357        | -      |
| 3.7475 | 274000 | 0.0372        | -      |
| 3.7612 | 275000 | 0.0379        | -      |
| 3.7749 | 276000 | 0.0365        | -      |
| 3.7886 | 277000 | 0.0374        | -      |
| 3.8022 | 278000 | 0.0355        | -      |
| 3.8159 | 279000 | 0.0362        | -      |
| 3.8296 | 280000 | 0.036         | -      |
| 3.8433 | 281000 | 0.036         | -      |
| 3.8569 | 282000 | 0.0337        | -      |
| 3.8706 | 283000 | 0.0374        | -      |
| 3.8843 | 284000 | 0.0353        | -      |
| 3.8980 | 285000 | 0.0344        | -      |
| 3.9116 | 286000 | 0.0355        | -      |
| 3.9253 | 287000 | 0.0342        | -      |
| 3.9390 | 288000 | 0.0361        | -      |
| 3.9527 | 289000 | 0.0361        | -      |
| 3.9664 | 290000 | 0.0376        | -      |
| 3.9800 | 291000 | 0.0363        | -      |
| 3.9937 | 292000 | 0.0363        | 0.0561 |
| 4.0074 | 293000 | 0.0313        | -      |
| 4.0211 | 294000 | 0.0273        | -      |
| 4.0347 | 295000 | 0.0277        | -      |
| 4.0484 | 296000 | 0.0248        | -      |
| 4.0621 | 297000 | 0.0268        | -      |
| 4.0758 | 298000 | 0.0259        | -      |
| 4.0894 | 299000 | 0.027         | -      |
| 4.1031 | 300000 | 0.0256        | -      |
| 4.1168 | 301000 | 0.0283        | -      |
| 4.1305 | 302000 | 0.0294        | -      |
| 4.1442 | 303000 | 0.0263        | -      |
| 4.1578 | 304000 | 0.0261        | -      |
| 4.1715 | 305000 | 0.0257        | -      |
| 4.1852 | 306000 | 0.0255        | -      |
| 4.1989 | 307000 | 0.0279        | -      |
| 4.2125 | 308000 | 0.0273        | -      |
| 4.2262 | 309000 | 0.0263        | -      |
| 4.2399 | 310000 | 0.0276        | -      |
| 4.2536 | 311000 | 0.0262        | -      |
| 4.2673 | 312000 | 0.029         | -      |
| 4.2809 | 313000 | 0.0261        | -      |
| 4.2946 | 314000 | 0.0264        | -      |
| 4.3083 | 315000 | 0.0252        | -      |
| 4.3220 | 316000 | 0.0265        | -      |
| 4.3356 | 317000 | 0.0281        | -      |
| 4.3493 | 318000 | 0.0249        | -      |
| 4.3630 | 319000 | 0.0278        | -      |
| 4.3767 | 320000 | 0.0272        | -      |
| 4.3903 | 321000 | 0.0285        | -      |
| 4.4040 | 322000 | 0.0279        | -      |
| 4.4177 | 323000 | 0.0265        | -      |
| 4.4314 | 324000 | 0.0268        | -      |
| 4.4451 | 325000 | 0.0257        | -      |
| 4.4587 | 326000 | 0.0273        | -      |
| 4.4724 | 327000 | 0.027         | -      |
| 4.4861 | 328000 | 0.0275        | -      |
| 4.4929 | 328500 | -             | 0.0548 |

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