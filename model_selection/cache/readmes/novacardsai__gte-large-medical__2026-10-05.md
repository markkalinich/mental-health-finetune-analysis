---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:65724
- loss:MultipleNegativesRankingLoss
base_model: Alibaba-NLP/gte-large-en-v1.5
widget:
- source_sentence: pulsatile tinnitus may be a symptom of idiopathic intracranial
    hypertension.
  sentences:
  - normal cerebral perfusion pressure is > 60 mm hg
  - ischemia occurs when cerebral blood flow decreases to less than 20 milliliters
    per 100 grams per minute.
  - tibolone is a medication that combines properties of estrogen and progesterone.
- source_sentence: management of mumps is supportive (antipyretics, analgesics).
  sentences:
  - the b.g. prasad scale and the wealth index are based solely on income.
  - physical exam of boerhaave syndrome reveals hamman's sign and crepitus on auscultation
  - the reading of the tuberculin skin sensitivity test is performed 72 hours after
    administration.
- source_sentence: medullary (papillary/follicular/medullary/anaplastic) thyroid carcinomas
    are derived from calcitonin-synthesizing parafollicular c cells
  sentences:
  - squamous cell lung carcinoma typically presents with features such as lesions
    located centrally in the lungs, cavities within the tumors, elevated calcium levels
    in the blood, and pancoast syndrome.
  - '24-hour urinary fractionated catecholamines in pheochromacytoma will show increased:
    metanephrines & vanillylmandelic acid ((2))'
  - the tendon is injured in a strain injury.
- source_sentence: mg levels are decreased in gitelman's syndrome
  sentences:
  - oral vancomycin is the doc for pseudomembranous colitis
  - ingram's regimen consists of the goeckerman regimen plus anthralin.
  - tamm horsfall protein is formed by thick ascending loop of henle(tal) part of
    nephron
- source_sentence: what is craniosynostosis? it is the premature fusion of cranial
    sutures.
  sentences:
  - alzheimers is more common in female sex
  - 'true or false: possessing take-home naloxone reduces the risk of prescription
    opioid misuse. false. however, emergency take-home naloxone is associated with
    reduced morbidity and mortality from opioid overdoses.'
  - class 6 mullerian malformation is arcuate uterus
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
model-index:
- name: SentenceTransformer based on Alibaba-NLP/gte-large-en-v1.5
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: med flashcard val
      type: med_flashcard_val
    metrics:
    - type: cosine_accuracy
      value: 0.9164000153541565
      name: Cosine Accuracy
---

# SentenceTransformer based on Alibaba-NLP/gte-large-en-v1.5

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [Alibaba-NLP/gte-large-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5). It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [Alibaba-NLP/gte-large-en-v1.5](https://huggingface.co/Alibaba-NLP/gte-large-en-v1.5) <!-- at revision 104333d6af6f97649377c2afbde10a7704870c7b -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 1024 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False, 'architecture': 'NewModel'})
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("novacardsai/gte-large-medical")
# Run inference
sentences = [
    'what is craniosynostosis? it is the premature fusion of cranial sutures.',
    'alzheimers is more common in female sex',
    'class 6 mullerian malformation is arcuate uterus',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 1024]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[0.9961, 0.8242, 0.6445],
#         [0.8242, 1.0000, 0.7070],
#         [0.6445, 0.7070, 1.0000]], dtype=torch.bfloat16)
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

* Dataset: `med_flashcard_val`
* Evaluated with [<code>TripletEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.TripletEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| **cosine_accuracy** | **0.9164** |

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

* Size: 65,724 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>sentence_2</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                        | sentence_1                                                                         | sentence_2                                                                         |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                             | string                                                                             |
  | details | <ul><li>min: 5 tokens</li><li>mean: 27.84 tokens</li><li>max: 94 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 27.76 tokens</li><li>max: 206 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 27.91 tokens</li><li>max: 196 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                    | sentence_1                                                                                                                                          | sentence_2                                                                       |
  |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|
  | <code>for moderate laryngotracheitis, which presents with stridor when at rest and mild retractions, the recommended management includes dexamethasone treatment followed by a period of observation lasting 3-4 hours post treatment.</code> | <code>elevated titers of anti-streptolysin o (aso) or anti-dnase b antibodies are indicative of recent group a strep (s. pyogenes) infection</code> | <code>chromosomes 6 and 9 are responsible for the initiation of menarche.</code> |
  | <code>recognize the structure in the eye known as the optic cup</code>                                                                                                                                                                        | <code>retinoblastoma is the most common primary intraocular malignancy in childhood</code>                                                          | <code>vulval hematoma is the mc site of pelvic hematoma</code>                   |
  | <code>who recommends triple drug therapy of dec +ivermectine+albendazole for prevention of lymphatic filariasis</code>                                                                                                                        | <code>individuals of white race generally have a favorable prognosis overall.</code>                                                                | <code>the ratio of type 1 to type 3 collagen in the skin is 8:1.</code>          |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `num_train_epochs`: 1
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 1
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
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss | med_flashcard_val_cosine_accuracy |
|:------:|:----:|:-------------:|:---------------------------------:|
| 0.1217 | 500  | 2.9918        | -                                 |
| 0.1999 | 821  | -             | 0.8895                            |
| 0.2434 | 1000 | 2.4515        | -                                 |
| 0.3651 | 1500 | 2.279         | -                                 |
| 0.3997 | 1642 | -             | 0.9085                            |
| 0.4869 | 2000 | 2.2218        | -                                 |
| 0.5996 | 2463 | -             | 0.9148                            |
| 0.6086 | 2500 | 2.19          | -                                 |
| 0.7303 | 3000 | 2.1685        | -                                 |
| 0.7994 | 3284 | -             | 0.9163                            |
| 0.8520 | 3500 | 2.1421        | -                                 |
| 0.9737 | 4000 | 2.1589        | -                                 |
| 0.9993 | 4105 | -             | 0.9164                            |
| 1.0    | 4108 | -             | 0.9164                            |


### Framework Versions
- Python: 3.12.12
- Sentence Transformers: 5.1.2
- Transformers: 4.57.3
- PyTorch: 2.9.0+cu126
- Accelerate: 1.12.0
- Datasets: 4.0.0
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