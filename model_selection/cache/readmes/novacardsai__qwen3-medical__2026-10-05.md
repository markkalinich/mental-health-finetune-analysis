---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:65724
- loss:MultipleNegativesRankingLoss
base_model: Qwen/Qwen3-Embedding-4B
widget:
- source_sentence: 'Instruct: Classify this medical flashcard into one or more relevant
    categories.

    Query: electrolyte abnormalities, such as hypokalemia and hypomagnesemia, can
    result from amphotericin b use'
  sentences:
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: lauren''s classification is utilized for the categorization of gastric
    carcinoma.'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: ischemia arises from an insufficient blood flow to satisfy the requirements
    of the tissues.'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: among various risk factors for endometrial carcinoma, cowden syndrome is
    ranked as the second highest.'
- source_sentence: 'Instruct: Classify this medical flashcard into one or more relevant
    categories.

    Query: nocardia causes cutaneous infections after trauma in the immunocompetent'
  sentences:
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: in individuals with autosomal dominant alport syndrome, a mild form of
    the disease affects both genders.'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: herpangina is characterized by the formation of lesions primarily located
    on the posterior part of the oropharynx and the tonsillar pillars. initially presenting
    as small gray vesicles about 1 millimeter in diameter, these lesions evolve into
    ulcers covered by a fibrin coating.'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: age < 45 with abnormal uterine bleeding and failed ocps is managed with
    endometrial biopsy (next step)'
- source_sentence: 'Instruct: Classify this medical flashcard into one or more relevant
    categories.

    Query: the mitral valve is most commonly affected in cases of infective endocarditis.
    however, intravenous drug users are an exception, as they are more likely to experience
    infective endocarditis involving the tricuspid valve.'
  sentences:
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: if lmp is on 6th march and cycle length is 25 daysedd is on 10th december'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: which selective serotonin reuptake inhibitor/serotonin-norepinephrine reuptake
    inhibitor is typically avoided in patients with hypertension? venlafaxine.'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: the management of acute bronchitis involves symptomatic treatments such
    as hydration, cough suppressants, fever reducers, and pain relievers.'
- source_sentence: 'Instruct: Classify this medical flashcard into one or more relevant
    categories.

    Query: heller syndrome is characterized by the regression of developmental milestones
    and autism spectrum disorder.'
  sentences:
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: gestational trophoblastic neoplasia frequently metastasizes to the vagina,
    making it the second most prevalent site for such spread.'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: mcburney''s point tenderness refers to pain felt one-third the distance
    between the anterior superior iliac spine (asis) and the navel.'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: are nonsteroidal anti-inflammatory drugs (nsaids) effective as antipyretics
    and analgesics? yes.'
- source_sentence: 'Instruct: Classify this medical flashcard into one or more relevant
    categories.

    Query: picture frame vertebra in mixed phase of pagets disease'
  sentences:
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: do patients with radial head subluxation experience sensory loss over the
    dorsal side of the hand or wrist? no.'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: diseases such as minimal change disease, focal segmental glomerulosclerosis,
    and membranous nephropathy fall under the category of podocytopathies, which affect
    the podocytes of the kidney.'
  - 'Instruct: Classify this medical flashcard into one or more relevant categories.

    Query: bronchiolitis obliterans (constrictive) is a patchy chronic inflammation
    & fibrosis of the bronchioles, which leads to collapse/obliteration of the bronchioles'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
model-index:
- name: SentenceTransformer based on Qwen/Qwen3-Embedding-4B
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: med flashcard val
      type: med_flashcard_val
    metrics:
    - type: cosine_accuracy
      value: 0.9620000123977661
      name: Cosine Accuracy
---

# SentenceTransformer based on Qwen/Qwen3-Embedding-4B

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [Qwen/Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B). It maps sentences & paragraphs to a 2560-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [Qwen/Qwen3-Embedding-4B](https://huggingface.co/Qwen/Qwen3-Embedding-4B) <!-- at revision 5cf2132abc99cad020ac570b19d031efec650f2b -->
- **Maximum Sequence Length:** 40960 tokens
- **Output Dimensionality:** 2560 dimensions
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
  (0): Transformer({'max_seq_length': 40960, 'do_lower_case': False, 'architecture': 'Qwen3Model'})
  (1): Pooling({'word_embedding_dimension': 2560, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': True, 'include_prompt': True})
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
model = SentenceTransformer("novacardsai/qwen3-med-classifier")
# Run inference
queries = [
    "Instruct: Classify this medical flashcard into one or more relevant categories.\nQuery: picture frame vertebra in mixed phase of pagets disease",
]
documents = [
    'Instruct: Classify this medical flashcard into one or more relevant categories.\nQuery: do patients with radial head subluxation experience sensory loss over the dorsal side of the hand or wrist? no.',
    'Instruct: Classify this medical flashcard into one or more relevant categories.\nQuery: bronchiolitis obliterans (constrictive) is a patchy chronic inflammation & fibrosis of the bronchioles, which leads to collapse/obliteration of the bronchioles',
    'Instruct: Classify this medical flashcard into one or more relevant categories.\nQuery: diseases such as minimal change disease, focal segmental glomerulosclerosis, and membranous nephropathy fall under the category of podocytopathies, which affect the podocytes of the kidney.',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 2560] [3, 2560]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[0.9688, 0.5820, 0.5742]], dtype=torch.bfloat16)
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

| Metric              | Value     |
|:--------------------|:----------|
| **cosine_accuracy** | **0.962** |

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
  |         | sentence_0                                                                          | sentence_1                                                                          | sentence_2                                                                          |
  |:--------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                              | string                                                                              |
  | details | <ul><li>min: 21 tokens</li><li>mean: 43.47 tokens</li><li>max: 203 tokens</li></ul> | <ul><li>min: 22 tokens</li><li>mean: 42.65 tokens</li><li>max: 238 tokens</li></ul> | <ul><li>min: 21 tokens</li><li>mean: 43.69 tokens</li><li>max: 268 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                             | sentence_1                                                                                                                                                                                                                                                                                                   | sentence_2                                                                                                                                                                                                                                                               |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Instruct: Classify this medical flashcard into one or more relevant categories.<br>Query: tobacco juice color amniotic fluid is seen in intrauterine death of fetus</code>       | <code>Instruct: Classify this medical flashcard into one or more relevant categories.<br>Query: in cases of acute fatty liver of pregnancy, an increase in total bilirubin levels is commonly observed.</code>                                                                                               | <code>Instruct: Classify this medical flashcard into one or more relevant categories.<br>Query: during pregnancy, avoid these vaccines: measles, mumps, and rubella (mmr), varicella, polio, and intranasal influenza.</code>                                            |
  | <code>Instruct: Classify this medical flashcard into one or more relevant categories.<br>Query: 10 no. karman cannula is used at 11 weeks of pregnancy</code>                          | <code>Instruct: Classify this medical flashcard into one or more relevant categories.<br>Query: a persistent moro reflex is observed in individuals with cerebral palsy.</code>                                                                                                                              | <code>Instruct: Classify this medical flashcard into one or more relevant categories.<br>Query: what enzyme in macrophages is primarily used to destroy phagocytosed material? lysozyme</code>                                                                           |
  | <code>Instruct: Classify this medical flashcard into one or more relevant categories.<br>Query: the presence of the dc-sign receptor increases susceptibility to hiv infection.</code> | <code>Instruct: Classify this medical flashcard into one or more relevant categories.<br>Query: what is the name of the blood transfusion reaction that typically manifests with symptoms including fever, headaches, chills, and flushing? it is called a febrile nonhemolytic transfusion reaction.</code> | <code>Instruct: Classify this medical flashcard into one or more relevant categories.<br>Query: which medications are used in the treatment of acute bipolar depression? 1. lurasidone2. olanzapine + fluoxetine3. lithium4. valproate5. quetiapine6. lamotrigine</code> |
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
- `num_train_epochs`: 1
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 8
- `per_device_eval_batch_size`: 8
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
| 0.0609 | 500  | 1.9105        | -                                 |
| 0.1217 | 1000 | 1.4749        | -                                 |
| 0.1826 | 1500 | 1.3069        | -                                 |
| 0.2000 | 1643 | -             | 0.9482                            |
| 0.2434 | 2000 | 1.202         | -                                 |
| 0.3043 | 2500 | 1.1576        | -                                 |
| 0.3651 | 3000 | 1.1167        | -                                 |
| 0.4000 | 3286 | -             | 0.9544                            |
| 0.4260 | 3500 | 1.0333        | -                                 |
| 0.4869 | 4000 | 1.0287        | -                                 |
| 0.5477 | 4500 | 1.0063        | -                                 |
| 0.5999 | 4929 | -             | 0.9620                            |
| 0.6086 | 5000 | 0.9879        | -                                 |
| 0.6694 | 5500 | 0.9673        | -                                 |
| 0.7303 | 6000 | 0.953         | -                                 |
| 0.7911 | 6500 | 0.9558        | -                                 |
| 0.7999 | 6572 | -             | 0.9626                            |
| 0.8520 | 7000 | 0.9696        | -                                 |
| 0.9129 | 7500 | 0.9525        | -                                 |
| 0.9737 | 8000 | 0.9641        | -                                 |
| 0.9999 | 8215 | -             | 0.9620                            |
| 1.0    | 8216 | -             | 0.9620                            |


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