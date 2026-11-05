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
      value: 0.9307036247334755
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
model = SentenceTransformer("youssefkhalil320/bge-large-en-v1.5-medical-nli")
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
| **cosine_accuracy** | **0.9307** |

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
- `num_train_epochs`: 10.0
- `warmup_ratio`: 0.1
- `load_best_model_at_end`: True
- `push_to_hub`: True
- `hub_model_id`: youssefkhalil320/bge-large-en-v1.5-medical-nli

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
- `num_train_epochs`: 10.0
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
- `hub_model_id`: youssefkhalil320/bge-large-en-v1.5-medical-nli
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
| 0.1008  | 48      | 0.233         | -               | -                            |
| 0.2017  | 96      | 0.1676        | -               | -                            |
| 0.3025  | 144     | 0.1291        | -               | -                            |
| 0.4034  | 192     | 0.1235        | -               | -                            |
| 0.5042  | 240     | 0.0967        | -               | -                            |
| 0.6050  | 288     | 0.0975        | -               | -                            |
| 0.7059  | 336     | 0.0958        | -               | -                            |
| 0.8067  | 384     | 0.0792        | -               | -                            |
| 0.9076  | 432     | 0.0895        | -               | -                            |
| 1.0     | 476     | -             | 0.0711          | 0.9232                       |
| 1.0084  | 480     | 0.0715        | -               | -                            |
| 1.1092  | 528     | 0.0557        | -               | -                            |
| 1.2101  | 576     | 0.0521        | -               | -                            |
| 1.3109  | 624     | 0.0495        | -               | -                            |
| 1.4118  | 672     | 0.0479        | -               | -                            |
| 1.5126  | 720     | 0.0487        | -               | -                            |
| 1.6134  | 768     | 0.0555        | -               | -                            |
| 1.7143  | 816     | 0.0474        | -               | -                            |
| 1.8151  | 864     | 0.0486        | -               | -                            |
| 1.9160  | 912     | 0.0412        | -               | -                            |
| **2.0** | **952** | **-**         | **0.0569**      | **0.9339**                   |
| 2.0168  | 960     | 0.0363        | -               | -                            |
| 2.1176  | 1008    | 0.0215        | -               | -                            |
| 2.2185  | 1056    | 0.0189        | -               | -                            |
| 2.3193  | 1104    | 0.0222        | -               | -                            |
| 2.4202  | 1152    | 0.0204        | -               | -                            |
| 2.5210  | 1200    | 0.0227        | -               | -                            |
| 2.6218  | 1248    | 0.0191        | -               | -                            |
| 2.7227  | 1296    | 0.0218        | -               | -                            |
| 2.8235  | 1344    | 0.0211        | -               | -                            |
| 2.9244  | 1392    | 0.0159        | -               | -                            |
| 3.0     | 1428    | -             | 0.0594          | 0.9211                       |
| 3.0252  | 1440    | 0.0153        | -               | -                            |
| 3.1261  | 1488    | 0.0076        | -               | -                            |
| 3.2269  | 1536    | 0.0094        | -               | -                            |
| 3.3277  | 1584    | 0.0083        | -               | -                            |
| 3.4286  | 1632    | 0.0093        | -               | -                            |
| 3.5294  | 1680    | 0.0083        | -               | -                            |
| 3.6303  | 1728    | 0.0076        | -               | -                            |
| 3.7311  | 1776    | 0.0094        | -               | -                            |
| 3.8319  | 1824    | 0.0073        | -               | -                            |
| 3.9328  | 1872    | 0.0099        | -               | -                            |
| 4.0     | 1904    | -             | 0.0608          | 0.9222                       |
| 4.0336  | 1920    | 0.0085        | -               | -                            |
| 4.1345  | 1968    | 0.0052        | -               | -                            |
| 4.2353  | 2016    | 0.0036        | -               | -                            |
| 4.3361  | 2064    | 0.0033        | -               | -                            |
| 4.4370  | 2112    | 0.0045        | -               | -                            |
| 4.5378  | 2160    | 0.0029        | -               | -                            |
| 4.6387  | 2208    | 0.0047        | -               | -                            |
| 4.7395  | 2256    | 0.0045        | -               | -                            |
| 4.8403  | 2304    | 0.005         | -               | -                            |
| 4.9412  | 2352    | 0.0037        | -               | -                            |
| 5.0     | 2380    | -             | 0.0625          | 0.9200                       |
| 5.0420  | 2400    | 0.0044        | -               | -                            |
| 5.1429  | 2448    | 0.0009        | -               | -                            |
| 5.2437  | 2496    | 0.0016        | -               | -                            |
| 5.3445  | 2544    | 0.0028        | -               | -                            |
| 5.4454  | 2592    | 0.0019        | -               | -                            |
| 5.5462  | 2640    | 0.0021        | -               | -                            |
| 5.6471  | 2688    | 0.0009        | -               | -                            |
| 5.7479  | 2736    | 0.0031        | -               | -                            |
| 5.8487  | 2784    | 0.0025        | -               | -                            |
| 5.9496  | 2832    | 0.0016        | -               | -                            |
| 6.0     | 2856    | -             | 0.0574          | 0.9222                       |
| 6.0504  | 2880    | 0.0018        | -               | -                            |
| 6.1513  | 2928    | 0.0012        | -               | -                            |
| 6.2521  | 2976    | 0.0017        | -               | -                            |
| 6.3529  | 3024    | 0.0014        | -               | -                            |
| 6.4538  | 3072    | 0.0019        | -               | -                            |
| 6.5546  | 3120    | 0.0011        | -               | -                            |
| 6.6555  | 3168    | 0.0011        | -               | -                            |
| 6.7563  | 3216    | 0.0009        | -               | -                            |
| 6.8571  | 3264    | 0.0006        | -               | -                            |
| 6.9580  | 3312    | 0.0014        | -               | -                            |
| 7.0     | 3332    | -             | 0.0572          | 0.9296                       |
| 7.0588  | 3360    | 0.0012        | -               | -                            |
| 7.1597  | 3408    | 0.0008        | -               | -                            |
| 7.2605  | 3456    | 0.001         | -               | -                            |
| 7.3613  | 3504    | 0.0009        | -               | -                            |
| 7.4622  | 3552    | 0.0005        | -               | -                            |
| 7.5630  | 3600    | 0.0014        | -               | -                            |
| 7.6639  | 3648    | 0.0003        | -               | -                            |
| 7.7647  | 3696    | 0.0006        | -               | -                            |
| 7.8655  | 3744    | 0.0005        | -               | -                            |
| 7.9664  | 3792    | 0.0006        | -               | -                            |
| 8.0     | 3808    | -             | 0.0569          | 0.9275                       |
| 8.0672  | 3840    | 0.0003        | -               | -                            |
| 8.1681  | 3888    | 0.0012        | -               | -                            |
| 8.2689  | 3936    | 0.0001        | -               | -                            |
| 8.3697  | 3984    | 0.0002        | -               | -                            |
| 8.4706  | 4032    | 0.0004        | -               | -                            |
| 8.5714  | 4080    | 0.0005        | -               | -                            |
| 8.6723  | 4128    | 0.0003        | -               | -                            |
| 8.7731  | 4176    | 0.0005        | -               | -                            |
| 8.8739  | 4224    | 0.0005        | -               | -                            |
| 8.9748  | 4272    | 0.0005        | -               | -                            |
| 9.0     | 4284    | -             | 0.0565          | 0.9264                       |
| 9.0756  | 4320    | 0.0001        | -               | -                            |
| 9.1765  | 4368    | 0.0004        | -               | -                            |
| 9.2773  | 4416    | 0.0001        | -               | -                            |
| 9.3782  | 4464    | 0.0002        | -               | -                            |
| 9.4790  | 4512    | 0.0007        | -               | -                            |
| 9.5798  | 4560    | 0.0005        | -               | -                            |
| 9.6807  | 4608    | 0.0005        | -               | -                            |
| 9.7815  | 4656    | 0.0007        | -               | -                            |
| 9.8824  | 4704    | 0.0002        | -               | -                            |
| 9.9832  | 4752    | 0.0007        | -               | -                            |
| 10.0    | 4760    | -             | 0.0555          | 0.9307                       |

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