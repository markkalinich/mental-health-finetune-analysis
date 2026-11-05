---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:10053
- loss:MultipleNegativesRankingLoss
base_model: answerdotai/ModernBERT-base
widget:
- source_sentence: Fluorescence quenching of tryptophan residues
  sentences:
  - 'Fluorescence of buried tyrosine residues in proteins. '
  - 'A fluorescence quenching study of tryptophanyl residues of (Ca2+ + Mg2+)-ATPase
    from sarcoplasmic reticulum. '
  - 'Some hormonal influences on the acetylation of sulfanilamide in vivo. '
- source_sentence: Human migration to the Americas
  sentences:
  - 'Homo sapiens in the Americas. Overview of the earliest human expansion in the
    New World. '
  - 'Profiles of College Drinkers Defined by Alcohol Behaviors at the Week Level:
    Replication Across Semesters and Prospective Associations With Hazardous Drinking
    and Dependence-Related Symptoms. '
  - 'Human migration. '
- source_sentence: Human Mobility Prediction
  sentences:
  - 'Human mobility prediction from region functions with taxi trajectories. '
  - 'Understanding Human Mobility from Twitter. '
  - 'Ovarian cancer gene therapy using HPV-16 pseudovirion carrying the HSV-tk gene. '
- source_sentence: Nevirapine Resistance
  sentences:
  - 'Nevirapine toxicity. '
  - 'Recognizing rhenium. '
  - 'Update on nevirapine: quest for a niche. '
- source_sentence: EHL tendon reconstruction
  sentences:
  - 'A Combined Surgical Approach for Extensor Hallucis Longus Reconstruction: Two
    Case Reports. '
  - 'Flexor tendon reconstruction. '
  - 'Noble gases and neuroprotection: summary of current evidence. '
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
model-index:
- name: SentenceTransformer based on answerdotai/ModernBERT-base
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: triplet dev
      type: triplet-dev
    metrics:
    - type: cosine_accuracy
      value: 0.887
      name: Cosine Accuracy
---

# SentenceTransformer based on answerdotai/ModernBERT-base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) on the json dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [answerdotai/ModernBERT-base](https://huggingface.co/answerdotai/ModernBERT-base) <!-- at revision 1e8d43065c90b6370237c1474ba1445048b02898 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - json
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: ModernBertModel 
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
    'EHL tendon reconstruction',
    'A Combined Surgical Approach for Extensor Hallucis Longus Reconstruction: Two Case Reports. ',
    'Flexor tendon reconstruction. ',
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

## Evaluation

### Metrics

#### Triplet

* Dataset: `triplet-dev`
* Evaluated with [<code>TripletEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator)

| Metric              | Value     |
|:--------------------|:----------|
| **cosine_accuracy** | **0.887** |

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

#### json

* Dataset: json
* Size: 10,053 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                           | positive                                                                          | negative                                                                          |
  |:--------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                           | string                                                                            | string                                                                            |
  | details | <ul><li>min: 4 tokens</li><li>mean: 8.86 tokens</li><li>max: 34 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 21.84 tokens</li><li>max: 62 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 13.65 tokens</li><li>max: 50 tokens</li></ul> |
* Samples:
  | anchor                                                       | positive                                                                                                            | negative                                                     |
  |:-------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------|
  | <code>COM-induced secretome changes in U937 monocytes</code> | <code>Characterization of calcium oxalate crystal-induced changes in the secretome of U937 human monocytes. </code> | <code>Monocytes. </code>                                     |
  | <code>Metamaterials</code>                                   | <code>Sound attenuation optimization using metaporous materials tuned on exceptional points. </code>                | <code>Metamaterials: A cat's eye for all directions. </code> |
  | <code>Pediatric Parasitology</code>                          | <code>Parasitic infections among school age children 6 to 11-years-of-age in the Eastern province. </code>          | <code>[DIALOGUE ON PEDIATRIC PARASITOLOGY]. </code>          |
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
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `learning_rate`: 0.0002
- `num_train_epochs`: 2
- `lr_scheduler_type`: cosine_with_restarts
- `warmup_ratio`: 0.1
- `bf16`: True
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 0.0002
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 2
- `max_steps`: -1
- `lr_scheduler_type`: cosine_with_restarts
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
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step | Training Loss | triplet-dev_cosine_accuracy |
|:------:|:----:|:-------------:|:---------------------------:|
| 0      | 0    | -             | 0.457                       |
| 0.0189 | 1    | 5.2934        | -                           |
| 0.0377 | 2    | 5.2413        | -                           |
| 0.0566 | 3    | 4.9969        | -                           |
| 0.0755 | 4    | 4.5579        | -                           |
| 0.0943 | 5    | 3.9145        | -                           |
| 0.1132 | 6    | 3.3775        | -                           |
| 0.1321 | 7    | 2.8787        | -                           |
| 0.1509 | 8    | 3.0147        | -                           |
| 0.1698 | 9    | 2.7166        | -                           |
| 0.1887 | 10   | 2.7875        | -                           |
| 0.2075 | 11   | 2.3848        | -                           |
| 0.2264 | 12   | 2.1921        | -                           |
| 0.2453 | 13   | 1.7009        | -                           |
| 0.2642 | 14   | 1.7649        | -                           |
| 0.2830 | 15   | 1.7948        | -                           |
| 0.3019 | 16   | 1.5384        | -                           |
| 0.3208 | 17   | 1.6039        | -                           |
| 0.3396 | 18   | 1.3364        | -                           |
| 0.3585 | 19   | 1.3852        | -                           |
| 0.3774 | 20   | 1.2427        | -                           |
| 0.3962 | 21   | 1.3216        | -                           |
| 0.4151 | 22   | 1.4202        | -                           |
| 0.4340 | 23   | 1.2754        | -                           |
| 0.4528 | 24   | 1.281         | -                           |
| 0.4717 | 25   | 1.1709        | 0.815                       |
| 0.4906 | 26   | 1.2363        | -                           |
| 0.5094 | 27   | 1.2169        | -                           |
| 0.5283 | 28   | 1.1495        | -                           |
| 0.5472 | 29   | 1.0066        | -                           |
| 0.5660 | 30   | 1.0478        | -                           |
| 0.5849 | 31   | 1.1511        | -                           |
| 0.6038 | 32   | 0.9992        | -                           |
| 0.6226 | 33   | 1.095         | -                           |
| 0.6415 | 34   | 1.1699        | -                           |
| 0.6604 | 35   | 0.9866        | -                           |
| 0.6792 | 36   | 1.1303        | -                           |
| 0.6981 | 37   | 1.1126        | -                           |
| 0.7170 | 38   | 0.889         | -                           |
| 0.7358 | 39   | 1.0355        | -                           |
| 0.7547 | 40   | 1.0129        | -                           |
| 0.7736 | 41   | 1.118         | -                           |
| 0.7925 | 42   | 0.8494        | -                           |
| 0.8113 | 43   | 1.0829        | -                           |
| 0.8302 | 44   | 0.8751        | -                           |
| 0.8491 | 45   | 0.8115        | -                           |
| 0.8679 | 46   | 0.8579        | -                           |
| 0.8868 | 47   | 1.1111        | -                           |
| 0.9057 | 48   | 0.9032        | -                           |
| 0.9245 | 49   | 1.0394        | -                           |
| 0.9434 | 50   | 0.9691        | 0.862                       |
| 0.9623 | 51   | 1.023         | -                           |
| 0.9811 | 52   | 0.9465        | -                           |
| 1.0    | 53   | 0.6713        | -                           |
| 1.0189 | 54   | 0.9773        | -                           |
| 1.0377 | 55   | 0.8693        | -                           |
| 1.0566 | 56   | 0.7187        | -                           |
| 1.0755 | 57   | 0.805         | -                           |
| 1.0943 | 58   | 0.728         | -                           |
| 1.1132 | 59   | 1.0967        | -                           |
| 1.1321 | 60   | 0.7036        | -                           |
| 1.1509 | 61   | 0.8213        | -                           |
| 1.1698 | 62   | 0.57          | -                           |
| 1.1887 | 63   | 0.7006        | -                           |
| 1.2075 | 64   | 0.5091        | -                           |
| 1.2264 | 65   | 0.5758        | -                           |
| 1.2453 | 66   | 0.4484        | -                           |
| 1.2642 | 67   | 0.397         | -                           |
| 1.2830 | 68   | 0.6172        | -                           |
| 1.3019 | 69   | 0.513         | -                           |
| 1.3208 | 70   | 0.4447        | -                           |
| 1.3396 | 71   | 0.3205        | -                           |
| 1.3585 | 72   | 0.5881        | -                           |
| 1.3774 | 73   | 0.2543        | -                           |
| 1.3962 | 74   | 0.3648        | -                           |
| 1.4151 | 75   | 0.4849        | 0.876                       |
| 1.4340 | 76   | 0.3455        | -                           |
| 1.4528 | 77   | 0.3424        | -                           |
| 1.4717 | 78   | 0.224         | -                           |
| 1.4906 | 79   | 0.18          | -                           |
| 1.5094 | 80   | 0.2255        | -                           |
| 1.5283 | 81   | 0.3024        | -                           |
| 1.5472 | 82   | 0.1835        | -                           |
| 1.5660 | 83   | 0.1946        | -                           |
| 1.5849 | 84   | 0.1958        | -                           |
| 1.6038 | 85   | 0.1568        | -                           |
| 1.6226 | 86   | 0.1626        | -                           |
| 1.6415 | 87   | 0.1774        | -                           |
| 1.6604 | 88   | 0.1934        | -                           |
| 1.6792 | 89   | 0.2426        | -                           |
| 1.6981 | 90   | 0.2958        | -                           |
| 1.7170 | 91   | 0.1606        | -                           |
| 1.7358 | 92   | 0.2281        | -                           |
| 1.7547 | 93   | 0.1786        | -                           |
| 1.7736 | 94   | 0.2241        | -                           |
| 1.7925 | 95   | 0.1909        | -                           |
| 1.8113 | 96   | 0.236         | -                           |
| 1.8302 | 97   | 0.1332        | -                           |
| 1.8491 | 98   | 0.1247        | -                           |
| 1.8679 | 99   | 0.156         | -                           |
| 1.8868 | 100  | 0.2152        | 0.889                       |
| 1.9057 | 101  | 0.1549        | -                           |
| 1.9245 | 102  | 0.2226        | -                           |
| 1.9434 | 103  | 0.21          | -                           |
| 1.9623 | 104  | 0.2139        | -                           |
| 1.9811 | 105  | 0.1864        | -                           |
| 2.0    | 106  | 0.0719        | 0.887                       |

</details>

### Framework Versions
- Python: 3.12.3
- Sentence Transformers: 3.3.1
- Transformers: 4.48.0.dev0
- PyTorch: 2.5.1
- Accelerate: 1.2.1
- Datasets: 3.2.0
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