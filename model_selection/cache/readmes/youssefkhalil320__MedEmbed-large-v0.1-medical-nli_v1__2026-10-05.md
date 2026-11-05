---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:7603
- loss:TripletLoss
base_model: abhinand/MedEmbed-large-v0.1
widget:
- source_sentence: Pt has hx of MRSA infection in this wound. .
  sentences:
  - The patient had an infected wound.
  - The patient has had neck surgery.
  - The patient has no history of infection.
- source_sentence: Hct has been stable without other s/s of bleeding.
  sentences:
  - The patient lost consciousness.
  - Patient has stable hematocrit
  - Patient has extensive hemorrhage
- source_sentence: In ED, tachycardic, NGT placed and NG lavage was negative.
  sentences:
  - the patient has a lower GI bleed
  - He was given a diuretic
  - the patient is tachycardic
- source_sentence: '- depression: reports recent worsening with intermittent passive
    SI and some [** Location **]inary plan formation; denies HI; denies any AH/VH
    in the past but does report some paranoid delusions - obstructive sleep apnea:
    on CPAP at home - morbid obesity: has worsened over past year - lymphedema - psoriasis'
  sentences:
  - History of elevated intracranial pressure
  - The patient also has bipolar disorder.
  - The patient has had times of suicidal ideation.
- source_sentence: Given the patient's recent surgery and that the bleeding had stopped
    a colonoscopy was planned as an outpatient.
  sentences:
  - The is at high risk of bleeding.
  - Patient has significant PSH
  - Patient has colon cancer
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
model-index:
- name: SentenceTransformer based on abhinand/MedEmbed-large-v0.1
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: val triplets
      type: val-triplets
    metrics:
    - type: cosine_accuracy
      value: 0.9189765458422174
      name: Cosine Accuracy
---

# SentenceTransformer based on abhinand/MedEmbed-large-v0.1

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [abhinand/MedEmbed-large-v0.1](https://huggingface.co/abhinand/MedEmbed-large-v0.1). It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [abhinand/MedEmbed-large-v0.1](https://huggingface.co/abhinand/MedEmbed-large-v0.1) <!-- at revision 963121bfb9c625475f65b08fb54990ce9c4e7a1a -->
- **Maximum Sequence Length:** 256 tokens
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
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False}) with Transformer model: BertModel 
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
model = SentenceTransformer("youssefkhalil320/MedEmbed-large-v0.1-medical-nli_v1")
# Run inference
sentences = [
    "Given the patient's recent surgery and that the bleeding had stopped a colonoscopy was planned as an outpatient.",
    'Patient has significant PSH',
    'Patient has colon cancer',
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

* Dataset: `val-triplets`
* Evaluated with [<code>TripletEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator)

| Metric              | Value     |
|:--------------------|:----------|
| **cosine_accuracy** | **0.919** |

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


* Size: 7,603 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                             | positive                                                                         | negative                                                                         |
  |:--------|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                           | string                                                                           |
  | details | <ul><li>min: 6 tokens</li><li>mean: 29.42 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 9.38 tokens</li><li>max: 25 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 8.89 tokens</li><li>max: 21 tokens</li></ul> |
* Samples:
  | anchor                                                                                                                                                                                                            | positive                                                          | negative                                                         |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------|:-----------------------------------------------------------------|
  | <code>O2: 94% 4Lnc.</code>                                                                                                                                                                                        | <code>The patient is on 4L of oxygen via nasal cannula</code>     | <code>The patient’s oxygen saturation is 100% on room air</code> |
  | <code>The patient has received 500 mg of intravenously levofloxacin given at the outside hospital, and the patient has received intravenous vancomycin as well as ceftazidime in our Emergency Department.</code> | <code>The patient has received broad spectrum antibiotics.</code> | <code>The patient has pneumonia.</code>                          |
  | <code>Cardiac enzymes done at OSH showed CK 363, CK-MB 33, TropI 6.78.</code>                                                                                                                                     | <code>The patient has cardiac ischemia.</code>                    | <code>The patient has normal cardiac perfusion.</code>           |
* Loss: [<code>TripletLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#tripletloss) with these parameters:
  ```json
  {
      "distance_metric": "TripletDistanceMetric.COSINE",
      "triplet_margin": 0.3
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset


* Size: 938 evaluation samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 938 samples:
  |         | anchor                                                                             | positive                                                                         | negative                                                                         |
  |:--------|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                           | string                                                                           |
  | details | <ul><li>min: 6 tokens</li><li>mean: 31.03 tokens</li><li>max: 187 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 9.08 tokens</li><li>max: 21 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 8.76 tokens</li><li>max: 19 tokens</li></ul> |
* Samples:
  | anchor                                                                                                                                                                                 | positive                                                       | negative                                                            |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------|:--------------------------------------------------------------------|
  | <code>History of acute renal failure.</code>                                                                                                                                           | <code>The patient has had kidney damage.</code>                | <code>The patient has always had normal functioning kidneys.</code> |
  | <code>Of note, pt had recent workup for intermittent abd discomfort and bloating, CT abd showed cholelithiasis and endometrial thickening, due for endometrial biopsy with Gyn.</code> | <code>Patient has findings warranting biopsy on imaging</code> | <code>Patient has endometrial cancer</code>                         |
  | <code>She states she drinks about [**2-17**] glasses of wine per night, but also admits to drinking up to a full bottle of wine during the day when she is home alone.</code>          | <code>the patient consumes alcohol</code>                      | <code>the patient denies alcohol use</code>                         |
* Loss: [<code>TripletLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#tripletloss) with these parameters:
  ```json
  {
      "distance_metric": "TripletDistanceMetric.COSINE",
      "triplet_margin": 0.3
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: epoch
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 32
- `learning_rate`: 2e-05
- `weight_decay`: 0.01
- `num_train_epochs`: 40.0
- `warmup_ratio`: 0.1
- `load_best_model_at_end`: True
- `push_to_hub`: True
- `hub_model_id`: youssefkhalil320/MedEmbed-large-v0.1-medical-nli_v1

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: epoch
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 32
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
- `num_train_epochs`: 40.0
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
- `push_to_hub`: True
- `resume_from_checkpoint`: None
- `hub_model_id`: youssefkhalil320/MedEmbed-large-v0.1-medical-nli_v1
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
- `eval_use_gather_object`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch   | Step     | Training Loss | Validation Loss | val-triplets_cosine_accuracy |
|:-------:|:--------:|:-------------:|:---------------:|:----------------------------:|
| 0.1008  | 48       | 0.2625        | -               | -                            |
| 0.2017  | 96       | 0.255         | -               | -                            |
| 0.3025  | 144      | 0.2363        | -               | -                            |
| 0.4034  | 192      | 0.1833        | -               | -                            |
| 0.5042  | 240      | 0.146         | -               | -                            |
| 0.6050  | 288      | 0.136         | -               | -                            |
| 0.7059  | 336      | 0.126         | -               | -                            |
| 0.8067  | 384      | 0.1101        | -               | -                            |
| 0.9076  | 432      | 0.1188        | -               | -                            |
| 1.0     | 476      | -             | 0.0810          | 0.9222                       |
| 1.0084  | 480      | 0.0918        | -               | -                            |
| 1.1092  | 528      | 0.0847        | -               | -                            |
| 1.2101  | 576      | 0.0796        | -               | -                            |
| 1.3109  | 624      | 0.0735        | -               | -                            |
| 1.4118  | 672      | 0.0726        | -               | -                            |
| 1.5126  | 720      | 0.0744        | -               | -                            |
| 1.6134  | 768      | 0.0799        | -               | -                            |
| 1.7143  | 816      | 0.0683        | -               | -                            |
| 1.8151  | 864      | 0.0766        | -               | -                            |
| 1.9160  | 912      | 0.0622        | -               | -                            |
| 2.0     | 952      | -             | 0.0654          | 0.9222                       |
| 2.0168  | 960      | 0.0559        | -               | -                            |
| 2.1176  | 1008     | 0.0381        | -               | -                            |
| 2.2185  | 1056     | 0.0312        | -               | -                            |
| 2.3193  | 1104     | 0.0436        | -               | -                            |
| 2.4202  | 1152     | 0.0413        | -               | -                            |
| 2.5210  | 1200     | 0.0425        | -               | -                            |
| 2.6218  | 1248     | 0.0448        | -               | -                            |
| 2.7227  | 1296     | 0.0433        | -               | -                            |
| 2.8235  | 1344     | 0.0501        | -               | -                            |
| 2.9244  | 1392     | 0.039         | -               | -                            |
| **3.0** | **1428** | **-**         | **0.0621**      | **0.9243**                   |
| 3.0252  | 1440     | 0.0344        | -               | -                            |
| 3.1261  | 1488     | 0.0195        | -               | -                            |
| 3.2269  | 1536     | 0.0196        | -               | -                            |
| 3.3277  | 1584     | 0.0249        | -               | -                            |
| 3.4286  | 1632     | 0.0242        | -               | -                            |
| 3.5294  | 1680     | 0.0234        | -               | -                            |
| 3.6303  | 1728     | 0.0239        | -               | -                            |
| 3.7311  | 1776     | 0.024         | -               | -                            |
| 3.8319  | 1824     | 0.0246        | -               | -                            |
| 3.9328  | 1872     | 0.0333        | -               | -                            |
| 4.0     | 1904     | -             | 0.0738          | 0.9041                       |
| 4.0336  | 1920     | 0.0216        | -               | -                            |
| 4.1345  | 1968     | 0.0138        | -               | -                            |
| 4.2353  | 2016     | 0.0139        | -               | -                            |
| 4.3361  | 2064     | 0.0133        | -               | -                            |
| 4.4370  | 2112     | 0.0158        | -               | -                            |
| 4.5378  | 2160     | 0.0147        | -               | -                            |
| 4.6387  | 2208     | 0.0148        | -               | -                            |
| 4.7395  | 2256     | 0.0185        | -               | -                            |
| 4.8403  | 2304     | 0.0157        | -               | -                            |
| 4.9412  | 2352     | 0.0157        | -               | -                            |
| 5.0     | 2380     | -             | 0.0589          | 0.9211                       |
| 5.0420  | 2400     | 0.0117        | -               | -                            |
| 5.1429  | 2448     | 0.0055        | -               | -                            |
| 5.2437  | 2496     | 0.0069        | -               | -                            |
| 5.3445  | 2544     | 0.0059        | -               | -                            |
| 5.4454  | 2592     | 0.011         | -               | -                            |
| 5.5462  | 2640     | 0.0098        | -               | -                            |
| 5.6471  | 2688     | 0.0092        | -               | -                            |
| 5.7479  | 2736     | 0.0114        | -               | -                            |
| 5.8487  | 2784     | 0.0087        | -               | -                            |
| 5.9496  | 2832     | 0.0086        | -               | -                            |
| 6.0     | 2856     | -             | 0.0698          | 0.9041                       |
| 6.0504  | 2880     | 0.0088        | -               | -                            |
| 6.1513  | 2928     | 0.0057        | -               | -                            |
| 6.2521  | 2976     | 0.0055        | -               | -                            |
| 6.3529  | 3024     | 0.0071        | -               | -                            |
| 6.4538  | 3072     | 0.0063        | -               | -                            |
| 6.5546  | 3120     | 0.0064        | -               | -                            |
| 6.6555  | 3168     | 0.0037        | -               | -                            |
| 6.7563  | 3216     | 0.0071        | -               | -                            |
| 6.8571  | 3264     | 0.0051        | -               | -                            |
| 6.9580  | 3312     | 0.0054        | -               | -                            |
| 7.0     | 3332     | -             | 0.0653          | 0.9062                       |
| 7.0588  | 3360     | 0.0091        | -               | -                            |
| 7.1597  | 3408     | 0.0052        | -               | -                            |
| 7.2605  | 3456     | 0.0029        | -               | -                            |
| 7.3613  | 3504     | 0.0049        | -               | -                            |
| 7.4622  | 3552     | 0.0043        | -               | -                            |
| 7.5630  | 3600     | 0.0034        | -               | -                            |
| 7.6639  | 3648     | 0.004         | -               | -                            |
| 7.7647  | 3696     | 0.005         | -               | -                            |
| 7.8655  | 3744     | 0.0043        | -               | -                            |
| 7.9664  | 3792     | 0.0041        | -               | -                            |
| 8.0     | 3808     | -             | 0.0667          | 0.9072                       |
| 8.0672  | 3840     | 0.004         | -               | -                            |
| 8.1681  | 3888     | 0.0042        | -               | -                            |
| 8.2689  | 3936     | 0.0037        | -               | -                            |
| 8.3697  | 3984     | 0.0038        | -               | -                            |
| 8.4706  | 4032     | 0.003         | -               | -                            |
| 8.5714  | 4080     | 0.0033        | -               | -                            |
| 8.6723  | 4128     | 0.0036        | -               | -                            |
| 8.7731  | 4176     | 0.0025        | -               | -                            |
| 8.8739  | 4224     | 0.0057        | -               | -                            |
| 8.9748  | 4272     | 0.0045        | -               | -                            |
| 9.0     | 4284     | -             | 0.0666          | 0.9041                       |
| 9.0756  | 4320     | 0.0012        | -               | -                            |
| 9.1765  | 4368     | 0.0028        | -               | -                            |
| 9.2773  | 4416     | 0.0016        | -               | -                            |
| 9.3782  | 4464     | 0.0017        | -               | -                            |
| 9.4790  | 4512     | 0.0034        | -               | -                            |
| 9.5798  | 4560     | 0.0024        | -               | -                            |
| 9.6807  | 4608     | 0.0028        | -               | -                            |
| 9.7815  | 4656     | 0.0041        | -               | -                            |
| 9.8824  | 4704     | 0.0036        | -               | -                            |
| 9.9832  | 4752     | 0.0037        | -               | -                            |
| 10.0    | 4760     | -             | 0.0644          | 0.9115                       |
| 10.0840 | 4800     | 0.0029        | -               | -                            |
| 10.1849 | 4848     | 0.003         | -               | -                            |
| 10.2857 | 4896     | 0.0014        | -               | -                            |
| 10.3866 | 4944     | 0.0033        | -               | -                            |
| 10.4874 | 4992     | 0.0036        | -               | -                            |
| 10.5882 | 5040     | 0.0036        | -               | -                            |
| 10.6891 | 5088     | 0.0029        | -               | -                            |
| 10.7899 | 5136     | 0.0013        | -               | -                            |
| 10.8908 | 5184     | 0.004         | -               | -                            |
| 10.9916 | 5232     | 0.0039        | -               | -                            |
| 11.0    | 5236     | -             | 0.0651          | 0.9147                       |
| 11.0924 | 5280     | 0.0021        | -               | -                            |
| 11.1933 | 5328     | 0.001         | -               | -                            |
| 11.2941 | 5376     | 0.0027        | -               | -                            |
| 11.3950 | 5424     | 0.0023        | -               | -                            |
| 11.4958 | 5472     | 0.0029        | -               | -                            |
| 11.5966 | 5520     | 0.0019        | -               | -                            |
| 11.6975 | 5568     | 0.0026        | -               | -                            |
| 11.7983 | 5616     | 0.0019        | -               | -                            |
| 11.8992 | 5664     | 0.003         | -               | -                            |
| 12.0    | 5712     | 0.0014        | 0.0672          | 0.9051                       |
| 12.1008 | 5760     | 0.0022        | -               | -                            |
| 12.2017 | 5808     | 0.0016        | -               | -                            |
| 12.3025 | 5856     | 0.002         | -               | -                            |
| 12.4034 | 5904     | 0.0031        | -               | -                            |
| 12.5042 | 5952     | 0.0024        | -               | -                            |
| 12.6050 | 6000     | 0.0023        | -               | -                            |
| 12.7059 | 6048     | 0.0022        | -               | -                            |
| 12.8067 | 6096     | 0.0034        | -               | -                            |
| 12.9076 | 6144     | 0.0018        | -               | -                            |
| 13.0    | 6188     | -             | 0.0705          | 0.9072                       |
| 13.0084 | 6192     | 0.003         | -               | -                            |
| 13.1092 | 6240     | 0.0023        | -               | -                            |
| 13.2101 | 6288     | 0.0013        | -               | -                            |
| 13.3109 | 6336     | 0.0004        | -               | -                            |
| 13.4118 | 6384     | 0.0016        | -               | -                            |
| 13.5126 | 6432     | 0.0012        | -               | -                            |
| 13.6134 | 6480     | 0.0014        | -               | -                            |
| 13.7143 | 6528     | 0.0013        | -               | -                            |
| 13.8151 | 6576     | 0.0033        | -               | -                            |
| 13.9160 | 6624     | 0.0026        | -               | -                            |
| 14.0    | 6664     | -             | 0.0697          | 0.9051                       |
| 14.0168 | 6672     | 0.0006        | -               | -                            |
| 14.1176 | 6720     | 0.0015        | -               | -                            |
| 14.2185 | 6768     | 0.0019        | -               | -                            |
| 14.3193 | 6816     | 0.0017        | -               | -                            |
| 14.4202 | 6864     | 0.0013        | -               | -                            |
| 14.5210 | 6912     | 0.0019        | -               | -                            |
| 14.6218 | 6960     | 0.0025        | -               | -                            |
| 14.7227 | 7008     | 0.0017        | -               | -                            |
| 14.8235 | 7056     | 0.0019        | -               | -                            |
| 14.9244 | 7104     | 0.001         | -               | -                            |
| 15.0    | 7140     | -             | 0.0641          | 0.9168                       |
| 15.0252 | 7152     | 0.0017        | -               | -                            |
| 15.1261 | 7200     | 0.001         | -               | -                            |
| 15.2269 | 7248     | 0.001         | -               | -                            |
| 15.3277 | 7296     | 0.002         | -               | -                            |
| 15.4286 | 7344     | 0.0007        | -               | -                            |
| 15.5294 | 7392     | 0.0012        | -               | -                            |
| 15.6303 | 7440     | 0.0006        | -               | -                            |
| 15.7311 | 7488     | 0.0013        | -               | -                            |
| 15.8319 | 7536     | 0.0014        | -               | -                            |
| 15.9328 | 7584     | 0.0013        | -               | -                            |
| 16.0    | 7616     | -             | 0.0657          | 0.9158                       |
| 16.0336 | 7632     | 0.0011        | -               | -                            |
| 16.1345 | 7680     | 0.0006        | -               | -                            |
| 16.2353 | 7728     | 0.0015        | -               | -                            |
| 16.3361 | 7776     | 0.0009        | -               | -                            |
| 16.4370 | 7824     | 0.0011        | -               | -                            |
| 16.5378 | 7872     | 0.0017        | -               | -                            |
| 16.6387 | 7920     | 0.0005        | -               | -                            |
| 16.7395 | 7968     | 0.0016        | -               | -                            |
| 16.8403 | 8016     | 0.0019        | -               | -                            |
| 16.9412 | 8064     | 0.0012        | -               | -                            |
| 17.0    | 8092     | -             | 0.0614          | 0.9243                       |
| 17.0420 | 8112     | 0.0021        | -               | -                            |
| 17.1429 | 8160     | 0.0001        | -               | -                            |
| 17.2437 | 8208     | 0.0012        | -               | -                            |
| 17.3445 | 8256     | 0.001         | -               | -                            |
| 17.4454 | 8304     | 0.0013        | -               | -                            |
| 17.5462 | 8352     | 0.0006        | -               | -                            |
| 17.6471 | 8400     | 0.0011        | -               | -                            |
| 17.7479 | 8448     | 0.0009        | -               | -                            |
| 17.8487 | 8496     | 0.002         | -               | -                            |
| 17.9496 | 8544     | 0.0019        | -               | -                            |
| 18.0    | 8568     | -             | 0.0713          | 0.9041                       |
| 18.0504 | 8592     | 0.0007        | -               | -                            |
| 18.1513 | 8640     | 0.0014        | -               | -                            |
| 18.2521 | 8688     | 0.0005        | -               | -                            |
| 18.3529 | 8736     | 0.0008        | -               | -                            |
| 18.4538 | 8784     | 0.0012        | -               | -                            |
| 18.5546 | 8832     | 0.0003        | -               | -                            |
| 18.6555 | 8880     | 0.002         | -               | -                            |
| 18.7563 | 8928     | 0.0006        | -               | -                            |
| 18.8571 | 8976     | 0.0004        | -               | -                            |
| 18.9580 | 9024     | 0.0006        | -               | -                            |
| 19.0    | 9044     | -             | 0.0677          | 0.9168                       |
| 19.0588 | 9072     | 0.0008        | -               | -                            |
| 19.1597 | 9120     | 0.0           | -               | -                            |
| 19.2605 | 9168     | 0.0009        | -               | -                            |
| 19.3613 | 9216     | 0.0008        | -               | -                            |
| 19.4622 | 9264     | 0.0005        | -               | -                            |
| 19.5630 | 9312     | 0.0006        | -               | -                            |
| 19.6639 | 9360     | 0.0011        | -               | -                            |
| 19.7647 | 9408     | 0.001         | -               | -                            |
| 19.8655 | 9456     | 0.0009        | -               | -                            |
| 19.9664 | 9504     | 0.0007        | -               | -                            |
| 20.0    | 9520     | -             | 0.0652          | 0.9136                       |
| 20.0672 | 9552     | 0.0011        | -               | -                            |
| 20.1681 | 9600     | 0.0011        | -               | -                            |
| 20.2689 | 9648     | 0.0021        | -               | -                            |
| 20.3697 | 9696     | 0.0006        | -               | -                            |
| 20.4706 | 9744     | 0.0007        | -               | -                            |
| 20.5714 | 9792     | 0.0003        | -               | -                            |
| 20.6723 | 9840     | 0.001         | -               | -                            |
| 20.7731 | 9888     | 0.0004        | -               | -                            |
| 20.8739 | 9936     | 0.0003        | -               | -                            |
| 20.9748 | 9984     | 0.001         | -               | -                            |
| 21.0    | 9996     | -             | 0.0702          | 0.9051                       |
| 21.0756 | 10032    | 0.0005        | -               | -                            |
| 21.1765 | 10080    | 0.0014        | -               | -                            |
| 21.2773 | 10128    | 0.0001        | -               | -                            |
| 21.3782 | 10176    | 0.0013        | -               | -                            |
| 21.4790 | 10224    | 0.0004        | -               | -                            |
| 21.5798 | 10272    | 0.0013        | -               | -                            |
| 21.6807 | 10320    | 0.001         | -               | -                            |
| 21.7815 | 10368    | 0.0002        | -               | -                            |
| 21.8824 | 10416    | 0.0013        | -               | -                            |
| 21.9832 | 10464    | 0.0011        | -               | -                            |
| 22.0    | 10472    | -             | 0.0639          | 0.9190                       |
| 22.0840 | 10512    | 0.0005        | -               | -                            |
| 22.1849 | 10560    | 0.0005        | -               | -                            |
| 22.2857 | 10608    | 0.0007        | -               | -                            |
| 22.3866 | 10656    | 0.0002        | -               | -                            |
| 22.4874 | 10704    | 0.0           | -               | -                            |
| 22.5882 | 10752    | 0.0003        | -               | -                            |
| 22.6891 | 10800    | 0.0009        | -               | -                            |
| 22.7899 | 10848    | 0.0008        | -               | -                            |
| 22.8908 | 10896    | 0.0008        | -               | -                            |
| 22.9916 | 10944    | 0.0008        | -               | -                            |
| 23.0    | 10948    | -             | 0.0646          | 0.9190                       |
| 23.0924 | 10992    | 0.0008        | -               | -                            |
| 23.1933 | 11040    | 0.0007        | -               | -                            |
| 23.2941 | 11088    | 0.0009        | -               | -                            |
| 23.3950 | 11136    | 0.0005        | -               | -                            |
| 23.4958 | 11184    | 0.0013        | -               | -                            |
| 23.5966 | 11232    | 0.0003        | -               | -                            |
| 23.6975 | 11280    | 0.0           | -               | -                            |
| 23.7983 | 11328    | 0.0002        | -               | -                            |
| 23.8992 | 11376    | 0.0008        | -               | -                            |
| 24.0    | 11424    | 0.001         | 0.0692          | 0.9062                       |
| 24.1008 | 11472    | 0.0001        | -               | -                            |
| 24.2017 | 11520    | 0.0011        | -               | -                            |
| 24.3025 | 11568    | 0.0006        | -               | -                            |
| 24.4034 | 11616    | 0.0008        | -               | -                            |
| 24.5042 | 11664    | 0.0017        | -               | -                            |
| 24.6050 | 11712    | 0.0005        | -               | -                            |
| 24.7059 | 11760    | 0.0           | -               | -                            |
| 24.8067 | 11808    | 0.0001        | -               | -                            |
| 24.9076 | 11856    | 0.0003        | -               | -                            |
| 25.0    | 11900    | -             | 0.0661          | 0.9115                       |
| 25.0084 | 11904    | 0.0003        | -               | -                            |
| 25.1092 | 11952    | 0.0002        | -               | -                            |
| 25.2101 | 12000    | 0.0009        | -               | -                            |
| 25.3109 | 12048    | 0.0002        | -               | -                            |
| 25.4118 | 12096    | 0.0005        | -               | -                            |
| 25.5126 | 12144    | 0.0001        | -               | -                            |
| 25.6134 | 12192    | 0.0007        | -               | -                            |
| 25.7143 | 12240    | 0.0004        | -               | -                            |
| 25.8151 | 12288    | 0.0002        | -               | -                            |
| 25.9160 | 12336    | 0.0002        | -               | -                            |
| 26.0    | 12376    | -             | 0.0670          | 0.9168                       |
| 26.0168 | 12384    | 0.0005        | -               | -                            |
| 26.1176 | 12432    | 0.0           | -               | -                            |
| 26.2185 | 12480    | 0.0009        | -               | -                            |
| 26.3193 | 12528    | 0.0001        | -               | -                            |
| 26.4202 | 12576    | 0.0004        | -               | -                            |
| 26.5210 | 12624    | 0.0007        | -               | -                            |
| 26.6218 | 12672    | 0.0002        | -               | -                            |
| 26.7227 | 12720    | 0.0009        | -               | -                            |
| 26.8235 | 12768    | 0.0008        | -               | -                            |
| 26.9244 | 12816    | 0.0008        | -               | -                            |
| 27.0    | 12852    | -             | 0.0687          | 0.9158                       |
| 27.0252 | 12864    | 0.0006        | -               | -                            |
| 27.1261 | 12912    | 0.0004        | -               | -                            |
| 27.2269 | 12960    | 0.0           | -               | -                            |
| 27.3277 | 13008    | 0.0002        | -               | -                            |
| 27.4286 | 13056    | 0.0004        | -               | -                            |
| 27.5294 | 13104    | 0.0001        | -               | -                            |
| 27.6303 | 13152    | 0.0           | -               | -                            |
| 27.7311 | 13200    | 0.0002        | -               | -                            |
| 27.8319 | 13248    | 0.001         | -               | -                            |
| 27.9328 | 13296    | 0.0002        | -               | -                            |
| 28.0    | 13328    | -             | 0.0669          | 0.9136                       |
| 28.0336 | 13344    | 0.0007        | -               | -                            |
| 28.1345 | 13392    | 0.0001        | -               | -                            |
| 28.2353 | 13440    | 0.0004        | -               | -                            |
| 28.3361 | 13488    | 0.0005        | -               | -                            |
| 28.4370 | 13536    | 0.0008        | -               | -                            |
| 28.5378 | 13584    | 0.0           | -               | -                            |
| 28.6387 | 13632    | 0.0007        | -               | -                            |
| 28.7395 | 13680    | 0.0001        | -               | -                            |
| 28.8403 | 13728    | 0.0001        | -               | -                            |
| 28.9412 | 13776    | 0.0           | -               | -                            |
| 29.0    | 13804    | -             | 0.0680          | 0.9115                       |
| 29.0420 | 13824    | 0.0002        | -               | -                            |
| 29.1429 | 13872    | 0.0003        | -               | -                            |
| 29.2437 | 13920    | 0.0           | -               | -                            |
| 29.3445 | 13968    | 0.0           | -               | -                            |
| 29.4454 | 14016    | 0.0003        | -               | -                            |
| 29.5462 | 14064    | 0.0003        | -               | -                            |
| 29.6471 | 14112    | 0.0001        | -               | -                            |
| 29.7479 | 14160    | 0.0006        | -               | -                            |
| 29.8487 | 14208    | 0.0006        | -               | -                            |
| 29.9496 | 14256    | 0.0008        | -               | -                            |
| 30.0    | 14280    | -             | 0.0628          | 0.9179                       |
| 30.0504 | 14304    | 0.0           | -               | -                            |
| 30.1513 | 14352    | 0.0001        | -               | -                            |
| 30.2521 | 14400    | 0.0           | -               | -                            |
| 30.3529 | 14448    | 0.0           | -               | -                            |
| 30.4538 | 14496    | 0.0001        | -               | -                            |
| 30.5546 | 14544    | 0.0001        | -               | -                            |
| 30.6555 | 14592    | 0.0001        | -               | -                            |
| 30.7563 | 14640    | 0.0009        | -               | -                            |
| 30.8571 | 14688    | 0.0001        | -               | -                            |
| 30.9580 | 14736    | 0.0003        | -               | -                            |
| 31.0    | 14756    | -             | 0.0626          | 0.9158                       |
| 31.0588 | 14784    | 0.0002        | -               | -                            |
| 31.1597 | 14832    | 0.0001        | -               | -                            |
| 31.2605 | 14880    | 0.0           | -               | -                            |
| 31.3613 | 14928    | 0.0004        | -               | -                            |
| 31.4622 | 14976    | 0.0001        | -               | -                            |
| 31.5630 | 15024    | 0.0001        | -               | -                            |
| 31.6639 | 15072    | 0.0005        | -               | -                            |
| 31.7647 | 15120    | 0.0001        | -               | -                            |
| 31.8655 | 15168    | 0.0005        | -               | -                            |
| 31.9664 | 15216    | 0.0005        | -               | -                            |
| 32.0    | 15232    | -             | 0.0624          | 0.9158                       |
| 32.0672 | 15264    | 0.0002        | -               | -                            |
| 32.1681 | 15312    | 0.0           | -               | -                            |
| 32.2689 | 15360    | 0.0           | -               | -                            |
| 32.3697 | 15408    | 0.0006        | -               | -                            |
| 32.4706 | 15456    | 0.0004        | -               | -                            |
| 32.5714 | 15504    | 0.0           | -               | -                            |
| 32.6723 | 15552    | 0.0           | -               | -                            |
| 32.7731 | 15600    | 0.0003        | -               | -                            |
| 32.8739 | 15648    | 0.0005        | -               | -                            |
| 32.9748 | 15696    | 0.0           | -               | -                            |
| 33.0    | 15708    | -             | 0.0627          | 0.9200                       |
| 33.0756 | 15744    | 0.0           | -               | -                            |
| 33.1765 | 15792    | 0.0001        | -               | -                            |
| 33.2773 | 15840    | 0.0           | -               | -                            |
| 33.3782 | 15888    | 0.0001        | -               | -                            |
| 33.4790 | 15936    | 0.0005        | -               | -                            |
| 33.5798 | 15984    | 0.0007        | -               | -                            |
| 33.6807 | 16032    | 0.0           | -               | -                            |
| 33.7815 | 16080    | 0.0           | -               | -                            |
| 33.8824 | 16128    | 0.0001        | -               | -                            |
| 33.9832 | 16176    | 0.0007        | -               | -                            |
| 34.0    | 16184    | -             | 0.0662          | 0.9179                       |
| 34.0840 | 16224    | 0.0005        | -               | -                            |
| 34.1849 | 16272    | 0.0           | -               | -                            |
| 34.2857 | 16320    | 0.0002        | -               | -                            |
| 34.3866 | 16368    | 0.0004        | -               | -                            |
| 34.4874 | 16416    | 0.0           | -               | -                            |
| 34.5882 | 16464    | 0.0001        | -               | -                            |
| 34.6891 | 16512    | 0.0004        | -               | -                            |
| 34.7899 | 16560    | 0.0001        | -               | -                            |
| 34.8908 | 16608    | 0.0007        | -               | -                            |
| 34.9916 | 16656    | 0.0           | -               | -                            |
| 35.0    | 16660    | -             | 0.0627          | 0.9190                       |
| 35.0924 | 16704    | 0.0           | -               | -                            |
| 35.1933 | 16752    | 0.0           | -               | -                            |
| 35.2941 | 16800    | 0.0           | -               | -                            |
| 35.3950 | 16848    | 0.0           | -               | -                            |
| 35.4958 | 16896    | 0.0           | -               | -                            |
| 35.5966 | 16944    | 0.0003        | -               | -                            |
| 35.6975 | 16992    | 0.0007        | -               | -                            |
| 35.7983 | 17040    | 0.0005        | -               | -                            |
| 35.8992 | 17088    | 0.0           | -               | -                            |
| 36.0    | 17136    | 0.0003        | 0.0632          | 0.9211                       |
| 36.1008 | 17184    | 0.0007        | -               | -                            |
| 36.2017 | 17232    | 0.0003        | -               | -                            |
| 36.3025 | 17280    | 0.0           | -               | -                            |
| 36.4034 | 17328    | 0.0           | -               | -                            |
| 36.5042 | 17376    | 0.0005        | -               | -                            |
| 36.6050 | 17424    | 0.0002        | -               | -                            |
| 36.7059 | 17472    | 0.0           | -               | -                            |
| 36.8067 | 17520    | 0.0002        | -               | -                            |
| 36.9076 | 17568    | 0.0003        | -               | -                            |
| 37.0    | 17612    | -             | 0.0612          | 0.9179                       |
| 37.0084 | 17616    | 0.0006        | -               | -                            |
| 37.1092 | 17664    | 0.0002        | -               | -                            |
| 37.2101 | 17712    | 0.0001        | -               | -                            |
| 37.3109 | 17760    | 0.0           | -               | -                            |
| 37.4118 | 17808    | 0.0007        | -               | -                            |
| 37.5126 | 17856    | 0.0           | -               | -                            |
| 37.6134 | 17904    | 0.0           | -               | -                            |
| 37.7143 | 17952    | 0.0006        | -               | -                            |
| 37.8151 | 18000    | 0.0           | -               | -                            |
| 37.9160 | 18048    | 0.0002        | -               | -                            |
| 38.0    | 18088    | -             | 0.0605          | 0.9179                       |
| 38.0168 | 18096    | 0.0002        | -               | -                            |
| 38.1176 | 18144    | 0.0004        | -               | -                            |
| 38.2185 | 18192    | 0.0           | -               | -                            |
| 38.3193 | 18240    | 0.0           | -               | -                            |
| 38.4202 | 18288    | 0.0           | -               | -                            |
| 38.5210 | 18336    | 0.0006        | -               | -                            |
| 38.6218 | 18384    | 0.0           | -               | -                            |
| 38.7227 | 18432    | 0.0           | -               | -                            |
| 38.8235 | 18480    | 0.0005        | -               | -                            |
| 38.9244 | 18528    | 0.0           | -               | -                            |
| 39.0    | 18564    | -             | 0.0610          | 0.9179                       |
| 39.0252 | 18576    | 0.0005        | -               | -                            |
| 39.1261 | 18624    | 0.0004        | -               | -                            |
| 39.2269 | 18672    | 0.0           | -               | -                            |
| 39.3277 | 18720    | 0.0           | -               | -                            |
| 39.4286 | 18768    | 0.0           | -               | -                            |
| 39.5294 | 18816    | 0.0           | -               | -                            |
| 39.6303 | 18864    | 0.0           | -               | -                            |
| 39.7311 | 18912    | 0.0004        | -               | -                            |
| 39.8319 | 18960    | 0.0           | -               | -                            |
| 39.9328 | 19008    | 0.0003        | -               | -                            |
| 40.0    | 19040    | -             | 0.0610          | 0.9190                       |

* The bold row denotes the saved checkpoint.
</details>

### Framework Versions
- Python: 3.10.19
- Sentence Transformers: 3.3.1
- Transformers: 4.44.2
- PyTorch: 2.8.0+cu128
- Accelerate: 1.12.0
- Datasets: 4.0.0
- Tokenizers: 0.19.1

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