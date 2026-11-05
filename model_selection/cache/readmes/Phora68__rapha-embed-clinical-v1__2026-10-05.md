---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:132037
- loss:MultipleNegativesRankingLoss
base_model: BAAI/bge-small-en-v1.5
widget:
- source_sentence: back pain. I'm not sure what to make of it.
  sentences:
  - 'Observed: back pain — musculoskeletal system'
  - Patient is frustrated with the medical system
  - 'OPQRST — Severity: fever rated 7/10 by patient'
- source_sentence: I'm absolutely terrified. I've had eye redness for a few days and
    I keep imagining the worst.
  sentences:
  - 'Observed: palpitations and irregular heart rate — cardiovascular — physician
    confirmed: Atrial fibrillation'
  - 'Patient presented: blood in urine — neurological/cognitive system'
  - 'Chief complaint: patient expressed concern, reason not yet specified — calm presentation'
- source_sentence: I take a pill called clopidogrel — not sure of the dose
  sentences:
  - Patient is drug-free by choice — lifestyle management only
  - 'Observed: fatigue and shortness of breath — haematological — physician confirmed:
    Anaemia'
  - 'Current medication: clopidogrel 75mg daily — antiplatelet — for post-MI'
- source_sentence: I'm on gabapentin for my neuropathic pain
  sentences:
  - Patient takes no regular medications
  - 'Current medication: gabapentin 300mg three times daily — anticonvulsant — for
    neuropathic pain'
  - 'Observed: palpitations — cardiovascular system'
- source_sentence: my breathing is fast and I feel disoriented
  sentences:
  - Patient is anxious and hyperventilating due to health anxiety
  - 'OPQRST — Onset: abdominal pain started suddenly without warning'
  - 'Red flag: tachypnoea + confusion — qSOFA >= 2 — possible sepsis — IMMEDIATE ESCALATION'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy
model-index:
- name: SentenceTransformer based on BAAI/bge-small-en-v1.5
  results:
  - task:
      type: triplet
      name: Triplet
    dataset:
      name: rapha val
      type: rapha-val
    metrics:
    - type: cosine_accuracy
      value: 1.0
      name: Cosine Accuracy
---

# SentenceTransformer based on BAAI/bge-small-en-v1.5

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for retrieval.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [BAAI/bge-small-en-v1.5](https://huggingface.co/BAAI/bge-small-en-v1.5) <!-- at revision 5c38ec7c405ec4b44b94cc5a9bb96e735b38267a -->
- **Maximum Sequence Length:** 128 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
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
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'BertModel'})
  (1): Pooling({'embedding_dimension': 384, 'pooling_mode': 'cls', 'include_prompt': True})
  (2): Normalize({})
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
    'my breathing is fast and I feel disoriented',
    'Red flag: tachypnoea + confusion — qSOFA >= 2 — possible sepsis — IMMEDIATE ESCALATION',
    'Patient is anxious and hyperventilating due to health anxiety',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.8755, 0.1384],
#         [0.8755, 1.0000, 0.0772],
#         [0.1384, 0.0772, 1.0000]])
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

* Dataset: `rapha-val`
* Evaluated with [<code>TripletEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.sentence_transformer.evaluation.TripletEvaluator)

| Metric              | Value   |
|:--------------------|:--------|
| **cosine_accuracy** | **1.0** |

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

* Size: 132,037 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 100 samples:
  |          | anchor                                                                           | positive                                                                         | negative                                                                          |
  |:---------|:---------------------------------------------------------------------------------|:---------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type     | string                                                                           | string                                                                           | string                                                                            |
  | modality | text                                                                             | text                                                                             | text                                                                              |
  | details  | <ul><li>min: 5 tokens</li><li>mean: 16.2 tokens</li><li>max: 34 tokens</li></ul> | <ul><li>min: 8 tokens</li><li>mean: 20.9 tokens</li><li>max: 33 tokens</li></ul> | <ul><li>min: 8 tokens</li><li>mean: 12.62 tokens</li><li>max: 19 tokens</li></ul> |
* Samples:
  | anchor                                                                                                     | positive                                                                                                 | negative                                                             |
  |:-----------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------|
  | <code>I'm trying to stay calm but I have tremors and I genuinely feel like something is very wrong.</code> | <code>Observed: tremors — neurological system</code>                                                     | <code>Patient is defensive, resistant to clinical interview</code>   |
  | <code>neck pain so bad I can't look down and light sensitivity too</code>                                  | <code>Red flag: neck stiffness + photophobia + fever — possible meningitis — IMMEDIATE ESCALATION</code> | <code>Patient reports muscle tension in neck from bad posture</code> |
  | <code>neck pain so bad I can't look down and light sensitivity too</code>                                  | <code>Red flag: neck stiffness + photophobia + fever — possible meningitis — IMMEDIATE ESCALATION</code> | <code>Patient reports muscle tension in neck from bad posture</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset

* Size: 15,000 evaluation samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 100 samples:
  |          | anchor                                                                            | positive                                                                          | negative                                                                          |
  |:---------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type     | string                                                                            | string                                                                            | string                                                                            |
  | modality | text                                                                              | text                                                                              | text                                                                              |
  | details  | <ul><li>min: 5 tokens</li><li>mean: 15.39 tokens</li><li>max: 27 tokens</li></ul> | <ul><li>min: 9 tokens</li><li>mean: 18.62 tokens</li><li>max: 33 tokens</li></ul> | <ul><li>min: 7 tokens</li><li>mean: 12.74 tokens</li><li>max: 23 tokens</li></ul> |
* Samples:
  | anchor                                                                            | positive                                                                                                                              | negative                                                                                         |
  |:----------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------|
  | <code>I'm on prednisolone 5mg daily</code>                                        | <code>Current medication: prednisolone 5mg daily — corticosteroid — for inflammatory condition</code>                                 | <code>Patient is not currently prescribed anything</code>                                        |
  | <code>Diagnosis recorded: Community-acquired pneumonia — ICD-10 code J18.9</code> | <code>Observed: cough, fever, shortness of breath — respiratory/infectious — physician confirmed: Community-acquired pneumonia</code> | <code>Observed: cough — upper respiratory tract infection — self-limiting, no antibiotics</code> |
  | <code>breast lump.</code>                                                         | <code>Session start: patient presented with unspecified concern — Minimal communication style</code>                                  | <code>Patient presented: numbness in limbs — respiratory system</code>                           |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 256
- `learning_rate`: 2e-05
- `lr_scheduler_type`: cosine
- `warmup_steps`: 0.1
- `bf16`: True
- `per_device_eval_batch_size`: 256
- `load_best_model_at_end`: True
- `dataloader_drop_last`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 256
- `num_train_epochs`: 3
- `max_steps`: -1
- `learning_rate`: 2e-05
- `lr_scheduler_type`: cosine
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0.1
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1.0
- `label_smoothing_factor`: 0.0
- `bf16`: True
- `fp16`: False
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
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 256
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
- `dataloader_drop_last`: True
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
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: None
- `fsdp_config`: None
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `warmup_ratio`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch      | Step    | Training Loss | Validation Loss | rapha-val_cosine_accuracy |
|:----------:|:-------:|:-------------:|:---------------:|:-------------------------:|
| 0.0971     | 50      | 3.5863        | -               | -                         |
| 0.1942     | 100     | 2.3320        | -               | -                         |
| 0.2913     | 150     | 1.7194        | -               | -                         |
| 0.3883     | 200     | 1.5596        | -               | -                         |
| 0.4854     | 250     | 1.4893        | -               | -                         |
| 0.5825     | 300     | 1.4520        | -               | -                         |
| 0.6796     | 350     | 1.4428        | -               | -                         |
| 0.7767     | 400     | 1.4143        | -               | -                         |
| 0.8738     | 450     | 1.4227        | -               | -                         |
| **0.9709** | **500** | **1.3991**    | **1.4893**      | **1.0**                   |
| 1.0680     | 550     | 1.3811        | -               | -                         |
| 1.1650     | 600     | 1.3818        | -               | -                         |
| 1.2621     | 650     | 1.3876        | -               | -                         |
| 1.3592     | 700     | 1.3830        | -               | -                         |
| 1.4563     | 750     | 1.3690        | -               | -                         |
| 1.5534     | 800     | 1.3927        | -               | -                         |
| 1.6505     | 850     | 1.3683        | -               | -                         |
| 1.7476     | 900     | 1.3772        | -               | -                         |
| 1.8447     | 950     | 1.3812        | -               | -                         |
| 1.9417     | 1000    | 1.4034        | 1.4836          | 1.0                       |
| 2.0388     | 1050    | 1.3812        | -               | -                         |
| 2.1359     | 1100    | 1.3562        | -               | -                         |
| 2.2330     | 1150    | 1.3676        | -               | -                         |
| 2.3301     | 1200    | 1.3813        | -               | -                         |
| 2.4272     | 1250    | 1.3849        | -               | -                         |
| 2.5243     | 1300    | 1.3729        | -               | -                         |
| 2.6214     | 1350    | 1.3770        | -               | -                         |
| 2.7184     | 1400    | 1.3665        | -               | -                         |
| 2.8155     | 1450    | 1.3469        | -               | -                         |
| 2.9126     | 1500    | 1.3790        | 1.4779          | 1.0                       |
| 3.0        | 1545    | -             | 1.4779          | 1.0                       |

* The bold row denotes the saved checkpoint.

### Training Time
- **Training**: 6.3 minutes

### Framework Versions
- Python: 3.12.13
- Sentence Transformers: 5.6.0
- Transformers: 5.12.1
- PyTorch: 2.11.0+cu128
- Accelerate: 1.14.0
- Datasets: 4.0.0
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

#### MultipleNegativesRankingLoss
```bibtex
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
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