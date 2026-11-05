---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:7603
- loss:TripletLoss
base_model: BAAI/bge-large-en-v1.5
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
- name: SentenceTransformer based on BAAI/bge-large-en-v1.5
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: val triplets
      type: val-triplets
    metrics:
    - type: cosine_accuracy
      value: 0.9221748400852878
      name: Cosine Accuracy
---

# SentenceTransformer based on BAAI/bge-large-en-v1.5

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5). It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-large-en-v1.5](https://huggingface.co/BAAI/bge-large-en-v1.5) <!-- at revision d4aa6901d3a41ba39fb536a557fa166f842b0e09 -->
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
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': True}) with Transformer model: BertModel 
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
model = SentenceTransformer("youssefkhalil320/bge-large-en-v1.5-medical-nli_v2")
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

| Metric              | Value      |
|:--------------------|:-----------|
| **cosine_accuracy** | **0.9222** |

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
- `hub_model_id`: youssefkhalil320/bge-large-en-v1.5-medical-nli_v2

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
- `hub_model_id`: youssefkhalil320/bge-large-en-v1.5-medical-nli_v2
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

| Epoch   | Step    | Training Loss | Validation Loss | val-triplets_cosine_accuracy |
|:-------:|:-------:|:-------------:|:---------------:|:----------------------------:|
| 0.1008  | 48      | 0.2406        | -               | -                            |
| 0.2017  | 96      | 0.2222        | -               | -                            |
| 0.3025  | 144     | 0.1831        | -               | -                            |
| 0.4034  | 192     | 0.1559        | -               | -                            |
| 0.5042  | 240     | 0.1381        | -               | -                            |
| 0.6050  | 288     | 0.1299        | -               | -                            |
| 0.7059  | 336     | 0.1207        | -               | -                            |
| 0.8067  | 384     | 0.1095        | -               | -                            |
| 0.9076  | 432     | 0.1155        | -               | -                            |
| 1.0     | 476     | -             | 0.0781          | 0.9275                       |
| 1.0084  | 480     | 0.0889        | -               | -                            |
| 1.1092  | 528     | 0.0821        | -               | -                            |
| 1.2101  | 576     | 0.0767        | -               | -                            |
| 1.3109  | 624     | 0.0727        | -               | -                            |
| 1.4118  | 672     | 0.0715        | -               | -                            |
| 1.5126  | 720     | 0.0722        | -               | -                            |
| 1.6134  | 768     | 0.0752        | -               | -                            |
| 1.7143  | 816     | 0.0687        | -               | -                            |
| 1.8151  | 864     | 0.0728        | -               | -                            |
| 1.9160  | 912     | 0.0622        | -               | -                            |
| **2.0** | **952** | **-**         | **0.0627**      | **0.9307**                   |
| 2.0168  | 960     | 0.0537        | -               | -                            |
| 2.1176  | 1008    | 0.0399        | -               | -                            |
| 2.2185  | 1056    | 0.0322        | -               | -                            |
| 2.3193  | 1104    | 0.0419        | -               | -                            |
| 2.4202  | 1152    | 0.041         | -               | -                            |
| 2.5210  | 1200    | 0.0402        | -               | -                            |
| 2.6218  | 1248    | 0.0411        | -               | -                            |
| 2.7227  | 1296    | 0.0422        | -               | -                            |
| 2.8235  | 1344    | 0.046         | -               | -                            |
| 2.9244  | 1392    | 0.0418        | -               | -                            |
| 3.0     | 1428    | -             | 0.0635          | 0.9200                       |
| 3.0252  | 1440    | 0.0285        | -               | -                            |
| 3.1261  | 1488    | 0.0194        | -               | -                            |
| 3.2269  | 1536    | 0.016         | -               | -                            |
| 3.3277  | 1584    | 0.0235        | -               | -                            |
| 3.4286  | 1632    | 0.0213        | -               | -                            |
| 3.5294  | 1680    | 0.0252        | -               | -                            |
| 3.6303  | 1728    | 0.0209        | -               | -                            |
| 3.7311  | 1776    | 0.0241        | -               | -                            |
| 3.8319  | 1824    | 0.0218        | -               | -                            |
| 3.9328  | 1872    | 0.0287        | -               | -                            |
| 4.0     | 1904    | -             | 0.0678          | 0.9126                       |
| 4.0336  | 1920    | 0.0193        | -               | -                            |
| 4.1345  | 1968    | 0.011         | -               | -                            |
| 4.2353  | 2016    | 0.0121        | -               | -                            |
| 4.3361  | 2064    | 0.013         | -               | -                            |
| 4.4370  | 2112    | 0.0134        | -               | -                            |
| 4.5378  | 2160    | 0.0146        | -               | -                            |
| 4.6387  | 2208    | 0.0139        | -               | -                            |
| 4.7395  | 2256    | 0.0161        | -               | -                            |
| 4.8403  | 2304    | 0.0142        | -               | -                            |
| 4.9412  | 2352    | 0.0155        | -               | -                            |
| 5.0     | 2380    | -             | 0.0589          | 0.9254                       |
| 5.0420  | 2400    | 0.0098        | -               | -                            |
| 5.1429  | 2448    | 0.0065        | -               | -                            |
| 5.2437  | 2496    | 0.0088        | -               | -                            |
| 5.3445  | 2544    | 0.0113        | -               | -                            |
| 5.4454  | 2592    | 0.0071        | -               | -                            |
| 5.5462  | 2640    | 0.0107        | -               | -                            |
| 5.6471  | 2688    | 0.0091        | -               | -                            |
| 5.7479  | 2736    | 0.0082        | -               | -                            |
| 5.8487  | 2784    | 0.0106        | -               | -                            |
| 5.9496  | 2832    | 0.0097        | -               | -                            |
| 6.0     | 2856    | -             | 0.0633          | 0.9179                       |
| 6.0504  | 2880    | 0.0062        | -               | -                            |
| 6.1513  | 2928    | 0.0042        | -               | -                            |
| 6.2521  | 2976    | 0.0077        | -               | -                            |
| 6.3529  | 3024    | 0.0051        | -               | -                            |
| 6.4538  | 3072    | 0.0043        | -               | -                            |
| 6.5546  | 3120    | 0.0051        | -               | -                            |
| 6.6555  | 3168    | 0.0048        | -               | -                            |
| 6.7563  | 3216    | 0.0057        | -               | -                            |
| 6.8571  | 3264    | 0.0048        | -               | -                            |
| 6.9580  | 3312    | 0.0068        | -               | -                            |
| 7.0     | 3332    | -             | 0.0695          | 0.9083                       |
| 7.0588  | 3360    | 0.0068        | -               | -                            |
| 7.1597  | 3408    | 0.003         | -               | -                            |
| 7.2605  | 3456    | 0.0035        | -               | -                            |
| 7.3613  | 3504    | 0.0034        | -               | -                            |
| 7.4622  | 3552    | 0.0031        | -               | -                            |
| 7.5630  | 3600    | 0.0042        | -               | -                            |
| 7.6639  | 3648    | 0.0048        | -               | -                            |
| 7.7647  | 3696    | 0.0045        | -               | -                            |
| 7.8655  | 3744    | 0.0042        | -               | -                            |
| 7.9664  | 3792    | 0.0036        | -               | -                            |
| 8.0     | 3808    | -             | 0.0686          | 0.9051                       |
| 8.0672  | 3840    | 0.0031        | -               | -                            |
| 8.1681  | 3888    | 0.0032        | -               | -                            |
| 8.2689  | 3936    | 0.0024        | -               | -                            |
| 8.3697  | 3984    | 0.0027        | -               | -                            |
| 8.4706  | 4032    | 0.0033        | -               | -                            |
| 8.5714  | 4080    | 0.0017        | -               | -                            |
| 8.6723  | 4128    | 0.0034        | -               | -                            |
| 8.7731  | 4176    | 0.0038        | -               | -                            |
| 8.8739  | 4224    | 0.0034        | -               | -                            |
| 8.9748  | 4272    | 0.0029        | -               | -                            |
| 9.0     | 4284    | -             | 0.0666          | 0.9104                       |
| 9.0756  | 4320    | 0.002         | -               | -                            |
| 9.1765  | 4368    | 0.0033        | -               | -                            |
| 9.2773  | 4416    | 0.0023        | -               | -                            |
| 9.3782  | 4464    | 0.0023        | -               | -                            |
| 9.4790  | 4512    | 0.0031        | -               | -                            |
| 9.5798  | 4560    | 0.0027        | -               | -                            |
| 9.6807  | 4608    | 0.003         | -               | -                            |
| 9.7815  | 4656    | 0.005         | -               | -                            |
| 9.8824  | 4704    | 0.0038        | -               | -                            |
| 9.9832  | 4752    | 0.0031        | -               | -                            |
| 10.0    | 4760    | -             | 0.0688          | 0.9083                       |
| 10.0840 | 4800    | 0.0029        | -               | -                            |
| 10.1849 | 4848    | 0.002         | -               | -                            |
| 10.2857 | 4896    | 0.0013        | -               | -                            |
| 10.3866 | 4944    | 0.0013        | -               | -                            |
| 10.4874 | 4992    | 0.0023        | -               | -                            |
| 10.5882 | 5040    | 0.0024        | -               | -                            |
| 10.6891 | 5088    | 0.0037        | -               | -                            |
| 10.7899 | 5136    | 0.0027        | -               | -                            |
| 10.8908 | 5184    | 0.0038        | -               | -                            |
| 10.9916 | 5232    | 0.0047        | -               | -                            |
| 11.0    | 5236    | -             | 0.0679          | 0.9104                       |
| 11.0924 | 5280    | 0.0014        | -               | -                            |
| 11.1933 | 5328    | 0.0014        | -               | -                            |
| 11.2941 | 5376    | 0.001         | -               | -                            |
| 11.3950 | 5424    | 0.0013        | -               | -                            |
| 11.4958 | 5472    | 0.0017        | -               | -                            |
| 11.5966 | 5520    | 0.0021        | -               | -                            |
| 11.6975 | 5568    | 0.0018        | -               | -                            |
| 11.7983 | 5616    | 0.0021        | -               | -                            |
| 11.8992 | 5664    | 0.0047        | -               | -                            |
| 12.0    | 5712    | 0.0026        | 0.0603          | 0.9190                       |
| 12.1008 | 5760    | 0.0017        | -               | -                            |
| 12.2017 | 5808    | 0.0011        | -               | -                            |
| 12.3025 | 5856    | 0.0025        | -               | -                            |
| 12.4034 | 5904    | 0.0017        | -               | -                            |
| 12.5042 | 5952    | 0.0008        | -               | -                            |
| 12.6050 | 6000    | 0.0006        | -               | -                            |
| 12.7059 | 6048    | 0.0011        | -               | -                            |
| 12.8067 | 6096    | 0.0022        | -               | -                            |
| 12.9076 | 6144    | 0.0031        | -               | -                            |
| 13.0    | 6188    | -             | 0.0684          | 0.9136                       |
| 13.0084 | 6192    | 0.0011        | -               | -                            |
| 13.1092 | 6240    | 0.0009        | -               | -                            |
| 13.2101 | 6288    | 0.0008        | -               | -                            |
| 13.3109 | 6336    | 0.001         | -               | -                            |
| 13.4118 | 6384    | 0.0026        | -               | -                            |
| 13.5126 | 6432    | 0.0026        | -               | -                            |
| 13.6134 | 6480    | 0.0019        | -               | -                            |
| 13.7143 | 6528    | 0.0019        | -               | -                            |
| 13.8151 | 6576    | 0.0024        | -               | -                            |
| 13.9160 | 6624    | 0.0019        | -               | -                            |
| 14.0    | 6664    | -             | 0.0616          | 0.9179                       |
| 14.0168 | 6672    | 0.0012        | -               | -                            |
| 14.1176 | 6720    | 0.0009        | -               | -                            |
| 14.2185 | 6768    | 0.0016        | -               | -                            |
| 14.3193 | 6816    | 0.0022        | -               | -                            |
| 14.4202 | 6864    | 0.0009        | -               | -                            |
| 14.5210 | 6912    | 0.0011        | -               | -                            |
| 14.6218 | 6960    | 0.0019        | -               | -                            |
| 14.7227 | 7008    | 0.0011        | -               | -                            |
| 14.8235 | 7056    | 0.0018        | -               | -                            |
| 14.9244 | 7104    | 0.0011        | -               | -                            |
| 15.0    | 7140    | -             | 0.0667          | 0.9126                       |
| 15.0252 | 7152    | 0.0013        | -               | -                            |
| 15.1261 | 7200    | 0.002         | -               | -                            |
| 15.2269 | 7248    | 0.0013        | -               | -                            |
| 15.3277 | 7296    | 0.0019        | -               | -                            |
| 15.4286 | 7344    | 0.0014        | -               | -                            |
| 15.5294 | 7392    | 0.0027        | -               | -                            |
| 15.6303 | 7440    | 0.0013        | -               | -                            |
| 15.7311 | 7488    | 0.0016        | -               | -                            |
| 15.8319 | 7536    | 0.0009        | -               | -                            |
| 15.9328 | 7584    | 0.0005        | -               | -                            |
| 16.0    | 7616    | -             | 0.0634          | 0.9243                       |
| 16.0336 | 7632    | 0.0005        | -               | -                            |
| 16.1345 | 7680    | 0.0002        | -               | -                            |
| 16.2353 | 7728    | 0.0011        | -               | -                            |
| 16.3361 | 7776    | 0.0005        | -               | -                            |
| 16.4370 | 7824    | 0.0005        | -               | -                            |
| 16.5378 | 7872    | 0.0009        | -               | -                            |
| 16.6387 | 7920    | 0.0009        | -               | -                            |
| 16.7395 | 7968    | 0.0013        | -               | -                            |
| 16.8403 | 8016    | 0.0018        | -               | -                            |
| 16.9412 | 8064    | 0.0014        | -               | -                            |
| 17.0    | 8092    | -             | 0.0625          | 0.9200                       |
| 17.0420 | 8112    | 0.0008        | -               | -                            |
| 17.1429 | 8160    | 0.0003        | -               | -                            |
| 17.2437 | 8208    | 0.0008        | -               | -                            |
| 17.3445 | 8256    | 0.0009        | -               | -                            |
| 17.4454 | 8304    | 0.0013        | -               | -                            |
| 17.5462 | 8352    | 0.0014        | -               | -                            |
| 17.6471 | 8400    | 0.0017        | -               | -                            |
| 17.7479 | 8448    | 0.0013        | -               | -                            |
| 17.8487 | 8496    | 0.0016        | -               | -                            |
| 17.9496 | 8544    | 0.0015        | -               | -                            |
| 18.0    | 8568    | -             | 0.0657          | 0.9115                       |
| 18.0504 | 8592    | 0.0016        | -               | -                            |
| 18.1513 | 8640    | 0.0009        | -               | -                            |
| 18.2521 | 8688    | 0.0005        | -               | -                            |
| 18.3529 | 8736    | 0.0008        | -               | -                            |
| 18.4538 | 8784    | 0.0007        | -               | -                            |
| 18.5546 | 8832    | 0.0012        | -               | -                            |
| 18.6555 | 8880    | 0.0019        | -               | -                            |
| 18.7563 | 8928    | 0.0007        | -               | -                            |
| 18.8571 | 8976    | 0.001         | -               | -                            |
| 18.9580 | 9024    | 0.001         | -               | -                            |
| 19.0    | 9044    | -             | 0.0625          | 0.9168                       |
| 19.0588 | 9072    | 0.0019        | -               | -                            |
| 19.1597 | 9120    | 0.0008        | -               | -                            |
| 19.2605 | 9168    | 0.0009        | -               | -                            |
| 19.3613 | 9216    | 0.0008        | -               | -                            |
| 19.4622 | 9264    | 0.0005        | -               | -                            |
| 19.5630 | 9312    | 0.001         | -               | -                            |
| 19.6639 | 9360    | 0.0005        | -               | -                            |
| 19.7647 | 9408    | 0.0015        | -               | -                            |
| 19.8655 | 9456    | 0.0004        | -               | -                            |
| 19.9664 | 9504    | 0.0009        | -               | -                            |
| 20.0    | 9520    | -             | 0.0638          | 0.9190                       |
| 20.0672 | 9552    | 0.0004        | -               | -                            |
| 20.1681 | 9600    | 0.0004        | -               | -                            |
| 20.2689 | 9648    | 0.0011        | -               | -                            |
| 20.3697 | 9696    | 0.0003        | -               | -                            |
| 20.4706 | 9744    | 0.0003        | -               | -                            |
| 20.5714 | 9792    | 0.0005        | -               | -                            |
| 20.6723 | 9840    | 0.0009        | -               | -                            |
| 20.7731 | 9888    | 0.0013        | -               | -                            |
| 20.8739 | 9936    | 0.0008        | -               | -                            |
| 20.9748 | 9984    | 0.0016        | -               | -                            |
| 21.0    | 9996    | -             | 0.0639          | 0.9200                       |
| 21.0756 | 10032   | 0.001         | -               | -                            |
| 21.1765 | 10080   | 0.0004        | -               | -                            |
| 21.2773 | 10128   | 0.0006        | -               | -                            |
| 21.3782 | 10176   | 0.0           | -               | -                            |
| 21.4790 | 10224   | 0.0004        | -               | -                            |
| 21.5798 | 10272   | 0.0008        | -               | -                            |
| 21.6807 | 10320   | 0.0014        | -               | -                            |
| 21.7815 | 10368   | 0.0004        | -               | -                            |
| 21.8824 | 10416   | 0.001         | -               | -                            |
| 21.9832 | 10464   | 0.0001        | -               | -                            |
| 22.0    | 10472   | -             | 0.0652          | 0.9168                       |
| 22.0840 | 10512   | 0.0007        | -               | -                            |
| 22.1849 | 10560   | 0.0003        | -               | -                            |
| 22.2857 | 10608   | 0.001         | -               | -                            |
| 22.3866 | 10656   | 0.0006        | -               | -                            |
| 22.4874 | 10704   | 0.0011        | -               | -                            |
| 22.5882 | 10752   | 0.0004        | -               | -                            |
| 22.6891 | 10800   | 0.0005        | -               | -                            |
| 22.7899 | 10848   | 0.0008        | -               | -                            |
| 22.8908 | 10896   | 0.0007        | -               | -                            |
| 22.9916 | 10944   | 0.0005        | -               | -                            |
| 23.0    | 10948   | -             | 0.0642          | 0.9168                       |
| 23.0924 | 10992   | 0.0011        | -               | -                            |
| 23.1933 | 11040   | 0.0007        | -               | -                            |
| 23.2941 | 11088   | 0.0005        | -               | -                            |
| 23.3950 | 11136   | 0.0004        | -               | -                            |
| 23.4958 | 11184   | 0.0015        | -               | -                            |
| 23.5966 | 11232   | 0.0002        | -               | -                            |
| 23.6975 | 11280   | 0.0011        | -               | -                            |
| 23.7983 | 11328   | 0.0003        | -               | -                            |
| 23.8992 | 11376   | 0.0003        | -               | -                            |
| 24.0    | 11424   | 0.0008        | 0.0626          | 0.9211                       |
| 24.1008 | 11472   | 0.0002        | -               | -                            |
| 24.2017 | 11520   | 0.0008        | -               | -                            |
| 24.3025 | 11568   | 0.0009        | -               | -                            |
| 24.4034 | 11616   | 0.0009        | -               | -                            |
| 24.5042 | 11664   | 0.0009        | -               | -                            |
| 24.6050 | 11712   | 0.0001        | -               | -                            |
| 24.7059 | 11760   | 0.0001        | -               | -                            |
| 24.8067 | 11808   | 0.0003        | -               | -                            |
| 24.9076 | 11856   | 0.0004        | -               | -                            |
| 25.0    | 11900   | -             | 0.0617          | 0.9211                       |
| 25.0084 | 11904   | 0.0007        | -               | -                            |
| 25.1092 | 11952   | 0.0004        | -               | -                            |
| 25.2101 | 12000   | 0.0011        | -               | -                            |
| 25.3109 | 12048   | 0.0004        | -               | -                            |
| 25.4118 | 12096   | 0.0003        | -               | -                            |
| 25.5126 | 12144   | 0.0005        | -               | -                            |
| 25.6134 | 12192   | 0.0008        | -               | -                            |
| 25.7143 | 12240   | 0.0004        | -               | -                            |
| 25.8151 | 12288   | 0.0004        | -               | -                            |
| 25.9160 | 12336   | 0.0004        | -               | -                            |
| 26.0    | 12376   | -             | 0.0601          | 0.9222                       |
| 26.0168 | 12384   | 0.0005        | -               | -                            |
| 26.1176 | 12432   | 0.0           | -               | -                            |
| 26.2185 | 12480   | 0.001         | -               | -                            |
| 26.3193 | 12528   | 0.0003        | -               | -                            |
| 26.4202 | 12576   | 0.0002        | -               | -                            |
| 26.5210 | 12624   | 0.0001        | -               | -                            |
| 26.6218 | 12672   | 0.0003        | -               | -                            |
| 26.7227 | 12720   | 0.0008        | -               | -                            |
| 26.8235 | 12768   | 0.0004        | -               | -                            |
| 26.9244 | 12816   | 0.0008        | -               | -                            |
| 27.0    | 12852   | -             | 0.0597          | 0.9211                       |
| 27.0252 | 12864   | 0.0005        | -               | -                            |
| 27.1261 | 12912   | 0.0006        | -               | -                            |
| 27.2269 | 12960   | 0.0003        | -               | -                            |
| 27.3277 | 13008   | 0.0           | -               | -                            |
| 27.4286 | 13056   | 0.0002        | -               | -                            |
| 27.5294 | 13104   | 0.0           | -               | -                            |
| 27.6303 | 13152   | 0.0006        | -               | -                            |
| 27.7311 | 13200   | 0.0002        | -               | -                            |
| 27.8319 | 13248   | 0.0003        | -               | -                            |
| 27.9328 | 13296   | 0.0001        | -               | -                            |
| 28.0    | 13328   | -             | 0.0572          | 0.9243                       |
| 28.0336 | 13344   | 0.0005        | -               | -                            |
| 28.1345 | 13392   | 0.0           | -               | -                            |
| 28.2353 | 13440   | 0.0           | -               | -                            |
| 28.3361 | 13488   | 0.0004        | -               | -                            |
| 28.4370 | 13536   | 0.0009        | -               | -                            |
| 28.5378 | 13584   | 0.0001        | -               | -                            |
| 28.6387 | 13632   | 0.0005        | -               | -                            |
| 28.7395 | 13680   | 0.0           | -               | -                            |
| 28.8403 | 13728   | 0.0           | -               | -                            |
| 28.9412 | 13776   | 0.0001        | -               | -                            |
| 29.0    | 13804   | -             | 0.0574          | 0.9264                       |
| 29.0420 | 13824   | 0.0001        | -               | -                            |
| 29.1429 | 13872   | 0.0003        | -               | -                            |
| 29.2437 | 13920   | 0.0003        | -               | -                            |
| 29.3445 | 13968   | 0.0           | -               | -                            |
| 29.4454 | 14016   | 0.0           | -               | -                            |
| 29.5462 | 14064   | 0.0001        | -               | -                            |
| 29.6471 | 14112   | 0.0004        | -               | -                            |
| 29.7479 | 14160   | 0.0005        | -               | -                            |
| 29.8487 | 14208   | 0.0006        | -               | -                            |
| 29.9496 | 14256   | 0.0005        | -               | -                            |
| 30.0    | 14280   | -             | 0.0581          | 0.9211                       |
| 30.0504 | 14304   | 0.0           | -               | -                            |
| 30.1513 | 14352   | 0.0           | -               | -                            |
| 30.2521 | 14400   | 0.0           | -               | -                            |
| 30.3529 | 14448   | 0.0001        | -               | -                            |
| 30.4538 | 14496   | 0.0002        | -               | -                            |
| 30.5546 | 14544   | 0.0001        | -               | -                            |
| 30.6555 | 14592   | 0.0007        | -               | -                            |
| 30.7563 | 14640   | 0.001         | -               | -                            |
| 30.8571 | 14688   | 0.0004        | -               | -                            |
| 30.9580 | 14736   | 0.0004        | -               | -                            |
| 31.0    | 14756   | -             | 0.0598          | 0.9222                       |
| 31.0588 | 14784   | 0.0           | -               | -                            |
| 31.1597 | 14832   | 0.0001        | -               | -                            |
| 31.2605 | 14880   | 0.0001        | -               | -                            |
| 31.3613 | 14928   | 0.0004        | -               | -                            |
| 31.4622 | 14976   | 0.0           | -               | -                            |
| 31.5630 | 15024   | 0.0           | -               | -                            |
| 31.6639 | 15072   | 0.0004        | -               | -                            |
| 31.7647 | 15120   | 0.0001        | -               | -                            |
| 31.8655 | 15168   | 0.0005        | -               | -                            |
| 31.9664 | 15216   | 0.0005        | -               | -                            |
| 32.0    | 15232   | -             | 0.0591          | 0.9254                       |
| 32.0672 | 15264   | 0.0           | -               | -                            |
| 32.1681 | 15312   | 0.0           | -               | -                            |
| 32.2689 | 15360   | 0.0           | -               | -                            |
| 32.3697 | 15408   | 0.0006        | -               | -                            |
| 32.4706 | 15456   | 0.0005        | -               | -                            |
| 32.5714 | 15504   | 0.0           | -               | -                            |
| 32.6723 | 15552   | 0.0           | -               | -                            |
| 32.7731 | 15600   | 0.0012        | -               | -                            |
| 32.8739 | 15648   | 0.0           | -               | -                            |
| 32.9748 | 15696   | 0.0           | -               | -                            |
| 33.0    | 15708   | -             | 0.0611          | 0.9222                       |
| 33.0756 | 15744   | 0.0001        | -               | -                            |
| 33.1765 | 15792   | 0.0           | -               | -                            |
| 33.2773 | 15840   | 0.0           | -               | -                            |
| 33.3782 | 15888   | 0.0           | -               | -                            |
| 33.4790 | 15936   | 0.0005        | -               | -                            |
| 33.5798 | 15984   | 0.0006        | -               | -                            |
| 33.6807 | 16032   | 0.0           | -               | -                            |
| 33.7815 | 16080   | 0.0           | -               | -                            |
| 33.8824 | 16128   | 0.0001        | -               | -                            |
| 33.9832 | 16176   | 0.0005        | -               | -                            |
| 34.0    | 16184   | -             | 0.0612          | 0.9222                       |
| 34.0840 | 16224   | 0.0006        | -               | -                            |
| 34.1849 | 16272   | 0.0           | -               | -                            |
| 34.2857 | 16320   | 0.0           | -               | -                            |
| 34.3866 | 16368   | 0.0005        | -               | -                            |
| 34.4874 | 16416   | 0.0           | -               | -                            |
| 34.5882 | 16464   | 0.0001        | -               | -                            |
| 34.6891 | 16512   | 0.0003        | -               | -                            |
| 34.7899 | 16560   | 0.0001        | -               | -                            |
| 34.8908 | 16608   | 0.0005        | -               | -                            |
| 34.9916 | 16656   | 0.0           | -               | -                            |
| 35.0    | 16660   | -             | 0.0614          | 0.9190                       |
| 35.0924 | 16704   | 0.0           | -               | -                            |
| 35.1933 | 16752   | 0.0           | -               | -                            |
| 35.2941 | 16800   | 0.0           | -               | -                            |
| 35.3950 | 16848   | 0.0           | -               | -                            |
| 35.4958 | 16896   | 0.0002        | -               | -                            |
| 35.5966 | 16944   | 0.0004        | -               | -                            |
| 35.6975 | 16992   | 0.0004        | -               | -                            |
| 35.7983 | 17040   | 0.0004        | -               | -                            |
| 35.8992 | 17088   | 0.0002        | -               | -                            |
| 36.0    | 17136   | 0.0004        | 0.0610          | 0.9158                       |
| 36.1008 | 17184   | 0.0008        | -               | -                            |
| 36.2017 | 17232   | 0.0           | -               | -                            |
| 36.3025 | 17280   | 0.0002        | -               | -                            |
| 36.4034 | 17328   | 0.0           | -               | -                            |
| 36.5042 | 17376   | 0.0006        | -               | -                            |
| 36.6050 | 17424   | 0.0           | -               | -                            |
| 36.7059 | 17472   | 0.0           | -               | -                            |
| 36.8067 | 17520   | 0.0           | -               | -                            |
| 36.9076 | 17568   | 0.0           | -               | -                            |
| 37.0    | 17612   | -             | 0.0607          | 0.9211                       |
| 37.0084 | 17616   | 0.0004        | -               | -                            |
| 37.1092 | 17664   | 0.0           | -               | -                            |
| 37.2101 | 17712   | 0.0           | -               | -                            |
| 37.3109 | 17760   | 0.0           | -               | -                            |
| 37.4118 | 17808   | 0.0008        | -               | -                            |
| 37.5126 | 17856   | 0.0           | -               | -                            |
| 37.6134 | 17904   | 0.0           | -               | -                            |
| 37.7143 | 17952   | 0.0004        | -               | -                            |
| 37.8151 | 18000   | 0.0           | -               | -                            |
| 37.9160 | 18048   | 0.0003        | -               | -                            |
| 38.0    | 18088   | -             | 0.0610          | 0.9232                       |
| 38.0168 | 18096   | 0.0           | -               | -                            |
| 38.1176 | 18144   | 0.0004        | -               | -                            |
| 38.2185 | 18192   | 0.0           | -               | -                            |
| 38.3193 | 18240   | 0.0001        | -               | -                            |
| 38.4202 | 18288   | 0.0           | -               | -                            |
| 38.5210 | 18336   | 0.0004        | -               | -                            |
| 38.6218 | 18384   | 0.0           | -               | -                            |
| 38.7227 | 18432   | 0.0           | -               | -                            |
| 38.8235 | 18480   | 0.0003        | -               | -                            |
| 38.9244 | 18528   | 0.0           | -               | -                            |
| 39.0    | 18564   | -             | 0.0612          | 0.9243                       |
| 39.0252 | 18576   | 0.0008        | -               | -                            |
| 39.1261 | 18624   | 0.0005        | -               | -                            |
| 39.2269 | 18672   | 0.0           | -               | -                            |
| 39.3277 | 18720   | 0.0           | -               | -                            |
| 39.4286 | 18768   | 0.0           | -               | -                            |
| 39.5294 | 18816   | 0.0           | -               | -                            |
| 39.6303 | 18864   | 0.0           | -               | -                            |
| 39.7311 | 18912   | 0.0004        | -               | -                            |
| 39.8319 | 18960   | 0.0           | -               | -                            |
| 39.9328 | 19008   | 0.0005        | -               | -                            |
| 40.0    | 19040   | -             | 0.0611          | 0.9222                       |

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