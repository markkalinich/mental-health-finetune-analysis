---
base_model: allenai/specter2_base
library_name: sentence-transformers
metrics:
- cosine_accuracy
- dot_accuracy
- manhattan_accuracy
- euclidean_accuracy
- max_accuracy
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:10053
- loss:MultipleNegativesRankingLoss
widget:
- source_sentence: HBV-endemic area diagnostic criteria comparison
  sentences:
  - 'Comparison of usefulness of clinical diagnostic criteria for hepatocellular carcinoma
    in a hepatitis B endemic area. '
  - 'The validation of the 2010 American Association for the Study of Liver Diseases
    guideline for the diagnosis of hepatocellular carcinoma in an endemic area. '
  - 'Which admission electrocardiographic parameter is more powerful predictor of
    no-reflow in patients with acute anterior myocardial infarction who underwent
    primary percutaneous intervention? '
- source_sentence: Family history of alcoholism classification schemes
  sentences:
  - 'Developing the mentor/protege relationship. '
  - 'Family history of alcoholism in schizophrenia. '
  - 'Family history models of alcoholism: age of onset, consequences and dependence. '
- source_sentence: Intellectual Property Commercialization
  sentences:
  - 'ALEPH-2, a suspected anxiolytic and putative hallucinogenic phenylisopropylamine
    derivative, is a 5-HT2a and 5-HT2c receptor agonist. '
  - 'Technology transfer and monitoring practices. '
  - '[From intellectual property to commercial property]. '
- source_sentence: Transmembrane domain mutants
  sentences:
  - 'Dysgerminoma; case with pulmonary metastases; result of treatment with irradiation
    and male sex hormone. '
  - 'Toward a high-resolution structure of phospholamban: design of soluble transmembrane
    domain mutants. '
  - 'Scanning N-glycosylation mutagenesis of membrane proteins. '
- source_sentence: Six-coordinate low-spin iron(III) porphyrinate complexes
  sentences:
  - 'Molecular structures and magnetic resonance spectroscopic investigations of highly
    distorted six-coordinate low-spin iron(III) porphyrinate complexes. '
  - 'Saddle-shaped six-coordinate iron(iii) porphyrin complex with unusual intermediate-spin
    electronic structure. '
  - 'Performing Economic Evaluation of Integrated Care: Highway to Hell or Stairway
    to Heaven? '
model-index:
- name: SentenceTransformer based on allenai/specter2_base
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: triplet dev
      type: triplet-dev
    metrics:
    - type: cosine_accuracy
      value: 0.606
      name: Cosine Accuracy
    - type: dot_accuracy
      value: 0.395
      name: Dot Accuracy
    - type: manhattan_accuracy
      value: 0.603
      name: Manhattan Accuracy
    - type: euclidean_accuracy
      value: 0.615
      name: Euclidean Accuracy
    - type: max_accuracy
      value: 0.615
      name: Max Accuracy
---

# SentenceTransformer based on allenai/specter2_base

This model is an initial proof of concept for (yet unpublished) article on ultra-hard negative triplet generation. While the original Specter2 adapters were trained on 600k triplets, only 10k ultra-hard, self-supervised negatives were enough to outperform the Proximity adapter (85 vs 84.1 avg NDCG over Relish, NFCorpus, TREC CoVID).


## Model Details
This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [allenai/specter2_base](https://huggingface.co/allenai/specter2_base) on the json dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [allenai/specter2_base](https://huggingface.co/allenai/specter2_base) <!-- at revision 3447645e1def9117997203454fa4495937bfbd83 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 tokens
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
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
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
    'Six-coordinate low-spin iron(III) porphyrinate complexes',
    'Molecular structures and magnetic resonance spectroscopic investigations of highly distorted six-coordinate low-spin iron(III) porphyrinate complexes. ',
    'Saddle-shaped six-coordinate iron(iii) porphyrin complex with unusual intermediate-spin electronic structure. ',
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
| **cosine_accuracy** | **0.606** |
| dot_accuracy        | 0.395     |
| manhattan_accuracy  | 0.603     |
| euclidean_accuracy  | 0.615     |
| max_accuracy        | 0.615     |

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
  | details | <ul><li>min: 4 tokens</li><li>mean: 7.49 tokens</li><li>max: 18 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 20.08 tokens</li><li>max: 48 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 12.46 tokens</li><li>max: 48 tokens</li></ul> |
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
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `learning_rate`: 2e-05
- `num_train_epochs`: 6
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
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
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
- `num_train_epochs`: 6
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
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step | Training Loss | triplet-dev_cosine_accuracy |
|:------:|:----:|:-------------:|:---------------------------:|
| 0      | 0    | -             | 0.373                       |
| 0.1667 | 1    | 3.138         | -                           |
| 0.3333 | 2    | 2.9761        | -                           |
| 0.5    | 3    | 2.7135        | -                           |
| 0.6667 | 4    | 2.5144        | -                           |
| 0.8333 | 5    | 1.9797        | -                           |
| 1.0    | 6    | 1.2683        | -                           |
| 1.1667 | 7    | 1.6058        | -                           |
| 1.3333 | 8    | 1.3236        | -                           |
| 1.5    | 9    | 1.1134        | -                           |
| 1.6667 | 10   | 1.1205        | -                           |
| 1.8333 | 11   | 0.9369        | -                           |
| 2.0    | 12   | 0.6215        | -                           |
| 2.1667 | 13   | 1.0374        | -                           |
| 2.3333 | 14   | 0.9355        | -                           |
| 2.5    | 15   | 0.7118        | -                           |
| 2.6667 | 16   | 0.7967        | -                           |
| 2.8333 | 17   | 0.5739        | -                           |
| 3.0    | 18   | 0.4515        | -                           |
| 3.1667 | 19   | 0.8018        | -                           |
| 3.3333 | 20   | 0.6557        | -                           |
| 3.5    | 21   | 0.6027        | -                           |
| 3.6667 | 22   | 0.6747        | -                           |
| 3.8333 | 23   | 0.5013        | -                           |
| 4.0    | 24   | 0.1428        | -                           |
| 4.1667 | 25   | 0.5889        | 0.596                       |
| 4.3333 | 26   | 0.5439        | -                           |
| 4.5    | 27   | 0.4742        | -                           |
| 4.6667 | 28   | 0.5734        | -                           |
| 4.8333 | 29   | 0.3966        | -                           |
| 5.0    | 30   | 0.1793        | -                           |
| 5.1667 | 31   | 0.5408        | -                           |
| 5.3333 | 32   | 0.5174        | -                           |
| 5.5    | 33   | 0.4179        | -                           |
| 5.6667 | 34   | 0.4589        | -                           |
| 5.8333 | 35   | 0.3683        | -                           |
| 6.0    | 36   | 0.1442        | 0.606                       |


### Framework Versions
- Python: 3.9.19
- Sentence Transformers: 3.1.1
- Transformers: 4.45.2
- PyTorch: 2.5.0
- Accelerate: 1.0.1
- Datasets: 2.19.0
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