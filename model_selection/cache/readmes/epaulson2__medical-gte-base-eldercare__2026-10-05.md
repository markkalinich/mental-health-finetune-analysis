---
language:
- en
license: apache-2.0
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:138875
- loss:MatryoshkaLoss
- loss:CachedGISTEmbedLoss
base_model: BAAI/bge-base-en-v1.5
widget:
- source_sentence: 'Represent this sentence for searching relevant passages: What
    is HERS Miconazole 3 used for?'
  sentences:
  - 'Indications For the temporary relief of skin irritations Directions Adults: Take
    five granules three times daily or as recommended by your healthcare practitioner.
    Children: Take three granules and follow adult directions.'
  - Warnings Do not use on children under 2 years of age unless directed by a doctor.
    For external use only avoid contact with eyes. Irritation occurs or if there is
    no improvement within 4 weeks (for athlete's foot and ringworm)irritation occurs
    or if there is no improvement within 2 weeks (for jock itch).
  - Uses • treats vaginal yeast infections
- source_sentence: 'Represent this sentence for searching relevant passages: Should
    elderly patients take flurazepam?'
  sentences:
  - 'Uses temporarily relieves minor aches and pains due to: headache muscular aches
    minor pain of arthritis toothache backache the common cold menstrual cramps temporarily
    reduces fever'
  - Avoid.
  - Warnings For external use only. Do not take it internally. Keep Out Of Reach Of
    Children Pregnant and lactating women use it with caution
- source_sentence: 'Represent this sentence for searching relevant passages: ASPIRIN
    Low Dose'
  sentences:
  - SODIUM PHOSPHATE MONOBASIC, SODIUM PHOSPHATE DIBASIC
  - SALICYLIC ACID
  - ASPIRIN
- source_sentence: 'Represent this sentence for searching relevant passages: CLE CCC
    Warm Medium Light'
  sentences:
  - TITANIUM DIOXIDE, OCTINOXATE, OCTISALATE
  - SUNSCREEN 45
  - Use relieves occasional constipation this product generally produces bowel movement
    in 1 to 5 minutes
- source_sentence: 'Represent this sentence for searching relevant passages: Is Almond
    Oil Oral safe for elderly?'
  sentences:
  - '[minor] Minimal additive effects possible'
  - ILIA SUPER SERUM SKIN TINT (ST0.5 SKYE) Indications & usage
  - Almond Oil Oral
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_accuracy@10
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
model-index:
- name: Medical BGE-Base for Eldercare
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: medical eval
      type: medical-eval
    metrics:
    - type: cosine_accuracy@1
      value: 0.364
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.4565
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.513
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.586
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.364
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.15216666666666664
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.1026
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.05859999999999999
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.364
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.4565
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.513
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.586
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.4651013263431341
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.42767341269841286
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.4370038649321368
      name: Cosine Map@100
---

# Medical BGE-Base for Eldercare

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) on the medical-embeddings-training-data dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-base-en-v1.5](https://huggingface.co/BAAI/bge-base-en-v1.5) <!-- at revision a5beb1e3e68b9ab74eb54cfd186867f64f240e1a -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - medical-embeddings-training-data
- **Language:** en
- **License:** apache-2.0

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': True, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Represent this sentence for searching relevant passages: Is Almond Oil Oral safe for elderly?',
    'Almond Oil Oral',
    '[minor] Minimal additive effects possible',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.9264, 0.6171],
#         [0.9264, 1.0000, 0.5909],
#         [0.6171, 0.5909, 1.0000]])
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

#### Information Retrieval

* Dataset: `medical-eval`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.364      |
| cosine_accuracy@3   | 0.4565     |
| cosine_accuracy@5   | 0.513      |
| cosine_accuracy@10  | 0.586      |
| cosine_precision@1  | 0.364      |
| cosine_precision@3  | 0.1522     |
| cosine_precision@5  | 0.1026     |
| cosine_precision@10 | 0.0586     |
| cosine_recall@1     | 0.364      |
| cosine_recall@3     | 0.4565     |
| cosine_recall@5     | 0.513      |
| cosine_recall@10    | 0.586      |
| **cosine_ndcg@10**  | **0.4651** |
| cosine_mrr@10       | 0.4277     |
| cosine_map@100      | 0.437      |

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

#### medical-embeddings-training-data

* Dataset: medical-embeddings-training-data
* Size: 138,875 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                             | positive                                                                           |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                             |
  | details | <ul><li>min: 12 tokens</li><li>mean: 27.02 tokens</li><li>max: 69 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 56.27 tokens</li><li>max: 379 tokens</li></ul> |
* Samples:
  | anchor                                                                                                                                                                                                                                                                                                                         | positive                                                                                                                                                                                                                                                                                                         |
  |:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Represent this sentence for searching relevant passages: [CONTEXT: This chunk provides guidance on the importance of snacking for older adults to support their nutrition, health, independence, and quality of life, emphasizing professional and community support.] Snacking for Seniors - Part 10</code>             | <code>Snacking is an important aspect of nutrition and diet for older adults. Understanding snacking helps seniors maintain health, independence, and quality of life. Professional guidance and community resources support snacking for seniors. Taking action on snacking makes a positive difference.</code> |
  | <code>Represent this sentence for searching relevant passages: [CONTEXT: This chunk provides guidance on Medicare financial enrollment aimed at seniors and caregivers to enhance understanding and improve health outcomes through informed communication with healthcare providers.] Enrollment in Medicare Financial</code> | <code>Information about enrollment for medicare financial. This knowledge helps seniors and caregivers understand important aspects of enrollment. Regular communication with healthcare providers and staying informed about enrollment can improve quality of life and health outcomes.</code>                 |
  | <code>Represent this sentence for searching relevant passages: What are the warnings for ca44f63d-749f-4062-8fc7-ac3158825310?</code>                                                                                                                                                                                          | <code>Warnings Stop use and ask a doctor , if symptoms persist or worsen. If pregnant or breast-feeding, take only on advice of a healthcare professional.</code>                                                                                                                                                |
* Loss: [<code>MatryoshkaLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss) with these parameters:
  ```json
  {
      "loss": "CachedGISTEmbedLoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Evaluation Dataset

#### medical-embeddings-training-data

* Dataset: medical-embeddings-training-data
* Size: 15,431 evaluation samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                             | positive                                                                           |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                             |
  | details | <ul><li>min: 12 tokens</li><li>mean: 27.07 tokens</li><li>max: 79 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 53.67 tokens</li><li>max: 441 tokens</li></ul> |
* Samples:
  | anchor                                                                                                                                 | positive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
  |:---------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Represent this sentence for searching relevant passages: What is N-21 used for?</code>                                           | <code>INDICATIONS Support for the eyes, inflammation, redness and dryness of the eyes.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
  | <code>Represent this sentence for searching relevant passages: What are the warnings for Venofye Orchard Bee Brilliance SPF 30?</code> | <code>Warnings For external use only. Do not use on damaged or broken skin. Keep out of eyes. If contact occurs, rinse with water. If rash or irritation develops, discontinue use and consult your physician.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | <code>Represent this sentence for searching relevant passages: What is Nymalize used for?</code>                                       | <code>1 INDICATIONS AND USAGE NYMALIZE is indicated for the improvement of neurological outcome by reducing the incidence and severity of ischemic deficits in adult patients with subarachnoid hemorrhage (SAH) from ruptured intracranial berry aneurysms regardless of their post-ictus neurological condition (i.e., Hunt and Hess Grades I-V). NYMALIZE is a dihydropyridine calcium channel blocker indicated for the improvement of neurological outcome by reducing the incidence and severity of ischemic deficits in adult patients with subarachnoid hemorrhage (SAH) from ruptured intracranial berry aneurysms regardless of their post-ictus neurological condition (i.e., Hunt and Hess Grades I-V). ( 1 )</code> |
* Loss: [<code>MatryoshkaLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss) with these parameters:
  ```json
  {
      "loss": "CachedGISTEmbedLoss",
      "matryoshka_dims": [
          768,
          512,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `num_train_epochs`: 1
- `learning_rate`: 2e-05
- `warmup_steps`: 0.1
- `weight_decay`: 0.01
- `fp16`: True
- `eval_strategy`: steps
- `per_device_eval_batch_size`: 32
- `load_best_model_at_end`: True
- `warmup_ratio`: 0.1
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 32
- `num_train_epochs`: 1
- `max_steps`: -1
- `learning_rate`: 2e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0.1
- `optim`: adamw_torch
- `optim_args`: None
- `weight_decay`: 0.01
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1.0
- `label_smoothing_factor`: 0.0
- `bf16`: False
- `fp16`: True
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: trackio
- `eval_strategy`: steps
- `per_device_eval_batch_size`: 32
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: False
- `hub_private_repo`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 42
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: []
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `warmup_ratio`: 0.1
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch      | Step     | Training Loss | Validation Loss | medical-eval_cosine_ndcg@10 |
|:----------:|:--------:|:-------------:|:---------------:|:---------------------------:|
| -1         | -1       | -             | -               | 0.3526                      |
| 0.0115     | 50       | 21.4644       | -               | -                           |
| 0.0230     | 100      | 12.3693       | -               | -                           |
| 0.0346     | 150      | 8.3857        | -               | -                           |
| 0.0461     | 200      | 6.6197        | -               | -                           |
| 0.0576     | 250      | 5.0731        | -               | -                           |
| 0.0691     | 300      | 4.7315        | -               | -                           |
| 0.0806     | 350      | 4.0549        | -               | -                           |
| 0.0922     | 400      | 3.6729        | -               | -                           |
| 0.1037     | 450      | 3.2577        | -               | -                           |
| 0.1152     | 500      | 3.1758        | 2.0604          | 0.4118                      |
| 0.1267     | 550      | 2.8301        | -               | -                           |
| 0.1382     | 600      | 2.8569        | -               | -                           |
| 0.1498     | 650      | 2.6782        | -               | -                           |
| 0.1613     | 700      | 2.6447        | -               | -                           |
| 0.1728     | 750      | 2.4327        | -               | -                           |
| 0.1843     | 800      | 2.3657        | -               | -                           |
| 0.1959     | 850      | 2.6314        | -               | -                           |
| 0.2074     | 900      | 2.1208        | -               | -                           |
| 0.2189     | 950      | 2.2966        | -               | -                           |
| 0.2304     | 1000     | 2.2544        | 1.5063          | 0.4352                      |
| 0.2419     | 1050     | 2.3016        | -               | -                           |
| 0.2535     | 1100     | 2.0355        | -               | -                           |
| 0.2650     | 1150     | 2.1095        | -               | -                           |
| 0.2765     | 1200     | 2.1743        | -               | -                           |
| 0.2880     | 1250     | 2.0971        | -               | -                           |
| 0.2995     | 1300     | 1.9309        | -               | -                           |
| 0.3111     | 1350     | 1.8261        | -               | -                           |
| 0.3226     | 1400     | 1.8530        | -               | -                           |
| 0.3341     | 1450     | 1.8746        | -               | -                           |
| 0.3456     | 1500     | 2.0222        | 1.3728          | 0.4472                      |
| 0.3571     | 1550     | 1.8223        | -               | -                           |
| 0.3687     | 1600     | 1.9075        | -               | -                           |
| 0.3802     | 1650     | 1.8989        | -               | -                           |
| 0.3917     | 1700     | 1.9164        | -               | -                           |
| 0.4032     | 1750     | 1.8066        | -               | -                           |
| 0.4147     | 1800     | 1.6366        | -               | -                           |
| 0.4263     | 1850     | 1.8221        | -               | -                           |
| 0.4378     | 1900     | 1.8602        | -               | -                           |
| 0.4493     | 1950     | 1.7117        | -               | -                           |
| 0.4608     | 2000     | 1.5802        | 1.2166          | 0.4514                      |
| 0.4724     | 2050     | 1.6800        | -               | -                           |
| 0.4839     | 2100     | 1.7472        | -               | -                           |
| 0.4954     | 2150     | 1.6999        | -               | -                           |
| 0.5069     | 2200     | 1.7095        | -               | -                           |
| 0.5184     | 2250     | 1.5913        | -               | -                           |
| 0.5300     | 2300     | 1.7659        | -               | -                           |
| 0.5415     | 2350     | 1.5958        | -               | -                           |
| 0.5530     | 2400     | 1.7422        | -               | -                           |
| 0.5645     | 2450     | 1.7618        | -               | -                           |
| 0.5760     | 2500     | 1.7058        | 1.1509          | 0.4576                      |
| 0.5876     | 2550     | 1.7298        | -               | -                           |
| 0.5991     | 2600     | 1.6349        | -               | -                           |
| 0.6106     | 2650     | 1.4472        | -               | -                           |
| 0.6221     | 2700     | 1.5778        | -               | -                           |
| 0.6336     | 2750     | 1.5168        | -               | -                           |
| 0.6452     | 2800     | 1.5806        | -               | -                           |
| 0.6567     | 2850     | 1.4689        | -               | -                           |
| 0.6682     | 2900     | 1.4052        | -               | -                           |
| 0.6797     | 2950     | 1.4711        | -               | -                           |
| 0.6912     | 3000     | 1.4793        | 1.0594          | 0.4616                      |
| 0.7028     | 3050     | 1.6667        | -               | -                           |
| 0.7143     | 3100     | 1.6008        | -               | -                           |
| 0.7258     | 3150     | 1.4364        | -               | -                           |
| 0.7373     | 3200     | 1.5818        | -               | -                           |
| 0.7488     | 3250     | 1.4065        | -               | -                           |
| 0.7604     | 3300     | 1.4548        | -               | -                           |
| 0.7719     | 3350     | 1.2939        | -               | -                           |
| 0.7834     | 3400     | 1.6109        | -               | -                           |
| 0.7949     | 3450     | 1.7005        | -               | -                           |
| 0.8065     | 3500     | 1.4387        | 1.0056          | 0.4633                      |
| 0.8180     | 3550     | 1.5827        | -               | -                           |
| 0.8295     | 3600     | 1.5064        | -               | -                           |
| 0.8410     | 3650     | 1.5197        | -               | -                           |
| 0.8525     | 3700     | 1.5047        | -               | -                           |
| 0.8641     | 3750     | 1.5071        | -               | -                           |
| 0.8756     | 3800     | 1.4802        | -               | -                           |
| 0.8871     | 3850     | 1.3452        | -               | -                           |
| 0.8986     | 3900     | 1.5015        | -               | -                           |
| 0.9101     | 3950     | 1.4390        | -               | -                           |
| **0.9217** | **4000** | **1.2257**    | **0.9738**      | **0.4651**                  |
| 0.9332     | 4050     | 1.3540        | -               | -                           |
| 0.9447     | 4100     | 1.3713        | -               | -                           |
| 0.9562     | 4150     | 1.4461        | -               | -                           |
| 0.9677     | 4200     | 1.5809        | -               | -                           |
| 0.9793     | 4250     | 1.2528        | -               | -                           |
| 0.9908     | 4300     | 1.3154        | -               | -                           |

* The bold row denotes the saved checkpoint.

### Framework Versions
- Python: 3.11.10
- Sentence Transformers: 5.2.3
- Transformers: 5.2.0
- PyTorch: 2.4.1+cu124
- Accelerate: 1.12.0
- Datasets: 2.21.0
- Tokenizers: 0.22.2

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

#### MatryoshkaLoss
```bibtex
@misc{kusupati2024matryoshka,
    title={Matryoshka Representation Learning},
    author={Aditya Kusupati and Gantavya Bhatt and Aniket Rege and Matthew Wallingford and Aditya Sinha and Vivek Ramanujan and William Howard-Snyder and Kaifeng Chen and Sham Kakade and Prateek Jain and Ali Farhadi},
    year={2024},
    eprint={2205.13147},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
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