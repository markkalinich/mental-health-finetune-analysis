---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:2945832
- loss:MultipleNegativesSymmetricMarginLoss
widget:
- source_sentence: Progesterone 40 mg/g vaginal gel
  sentences:
  - Supernumary dentition
  - A measurement of the number of implantations in the uterus.
  - progesterone 4% vaginal gel
- source_sentence: open fracture of four ribs
  sentences:
  - open fracture of four ribs (diagnosis)
  - Counselling about nutrition using social support strategy
  - Columbia-Suicidality Severity Rating Scale Baseline/Screening Version (C-SSRS
    Baseline/Screening Version) When you have the thoughts, how long do they last?
    (Lifetime).
- source_sentence: 'magnetic resonance imaging of thoracic spine: mass of lateral
    aspect of T12 vertebra with isointense T1 signal'
  sentences:
  - Medical and Surgical @ Endocrine System @ Repair @ Paraganglion Extremity @ Open
    @ No Device @ No Qualifier
  - nodule of right lateral cheek (physical finding)
  - spine magnetic resonance imaging T1-weighted thoracic osseous mass isointense
    signal T12 lateral
- source_sentence: Injury to spleen without mention of open wound into cavity, capsular
    tears, without major disruption of parenchyma
  sentences:
  - Capsular tears to spleen, without major disruption of parenchyma, without mention
    of open wound into cavity
  - Bleeding grade IV internal haemorrhoid
  - In 1948, G. Q. Chance described a traumatic spinal injury as a "horizontal splitting
    of the spine," which has since come to be known as the Chance fracture. In 1965,
    the first such fracture was described by Howland et al. in a passenger as a result
    of a lap seatbelt during a motor vehicle accident. Until 1980, there were 36 such
    injuries reported, but the number of reports has since risen with the advent of
    mandatory seatbelt laws. We report three cases occurring in a single accident
    when a popular 4-wheel drive vehicle moving at only approximately 25 mph struck
    a tree, causing flexion-distraction fractures in all three children wearing lapbelts
    while seated in the rear seat. All three had a different Chance fracture variant
    and associated intraabdominal injuries. One child was rendered paraplegic. The
    purpose of this report is to promote awareness of the associated injuries, and
    to encourage appropriate use and development of passenger restraints for children.
- source_sentence: Congenital fibrinogen abnormality
  sentences:
  - Any process that activates or increases the frequency, rate or extent of oogenesis.
    [GO_REF:0000058, GOC:TermGenie, PMID:26434723]
  - Congenital disease
  - An application of magnetic resonance imaging that uses spin refocusing and spin
    echo generation, resulting in shorter repetition times and faster imaging.
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
- name: SentenceTransformer
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: umls sota eval
      type: umls_sota_eval
    metrics:
    - type: cosine_accuracy@1
      value: 0.957925925925926
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.9791604938271605
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.9829135802469136
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.988641975308642
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.957925925925926
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.5356378600823045
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.36578765432098764
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.20597530864197536
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.6670666060648346
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.8832696443601331
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.9236085767441008
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.9552723269719597
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.9524544555838974
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.9691797374093671
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.9382568542682103
      name: Cosine Map@100
---

# SentenceTransformer

This is a [sentence-transformers](https://www.SBERT.net) model trained. It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 384 dimensions
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
model = SentenceTransformer("pankajrajdeo/BioForge-bioformer-16L-umls-integration")
# Run inference
sentences = [
    'Congenital fibrinogen abnormality',
    'Congenital disease',
    'An application of magnetic resonance imaging that uses spin refocusing and spin echo generation, resulting in shorter repetition times and faster imaging.',
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

## Evaluation

### Metrics

#### Information Retrieval

* Dataset: `umls_sota_eval`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.9579     |
| cosine_accuracy@3   | 0.9792     |
| cosine_accuracy@5   | 0.9829     |
| cosine_accuracy@10  | 0.9886     |
| cosine_precision@1  | 0.9579     |
| cosine_precision@3  | 0.5356     |
| cosine_precision@5  | 0.3658     |
| cosine_precision@10 | 0.206      |
| cosine_recall@1     | 0.6671     |
| cosine_recall@3     | 0.8833     |
| cosine_recall@5     | 0.9236     |
| cosine_recall@10    | 0.9553     |
| **cosine_ndcg@10**  | **0.9525** |
| cosine_mrr@10       | 0.9692     |
| cosine_map@100      | 0.9383     |

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

* Size: 2,945,832 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                            | positive                                                                           |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                             |
  | details | <ul><li>min: 3 tokens</li><li>mean: 12.11 tokens</li><li>max: 62 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 39.97 tokens</li><li>max: 256 tokens</li></ul> |
* Samples:
  | anchor                                                | positive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  |:------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Cranial nerve structure</code>                  | <code>Cranial neuropathy due to petrous infection</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
  | <code>Phenylalanine racemase (ATP-hydrolysing)</code> | <code>Phenylalanine racemase (adenosine triphosphate-hydrolysing) (substance)</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  | <code>Denibulin Hydrochloride</code>                  | <code>The hydrochloride salt of denibulin, a small molecular vascular disrupting agent, with potential antimitotic and antineoplastic activities. Denibulin selectively targets and reversibly binds to the colchicine-binding site on tubulin and inhibits microtubule assembly. This results in the disruption of the cytoskeleton of tumor endothelial cells, ultimately leading to cell cycle arrest, blockage of cell division and apoptosis. This causes inadequate blood flow to the tumor and eventually leads to a decrease in tumor cell proliferation., a small molecule vascular disrupting agent (VDA), with potential antimitotic and antineoplastic activity. Denibulin selectively targets and reversibly binds to the colchicine-binding site on tubulin and inhibits microtubule assembly. This results in the disruption of the cytoskeleton of tumor endothelial cells (EC), ultimately leading to cell cycle arrest, blockage of cell division and apoptosis. This causes inadequate blood flow to the tumor and eventual...</code> |
* Loss: <code>__main__.MultipleNegativesSymmetricMarginLoss</code> with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 512
- `gradient_accumulation_steps`: 4
- `learning_rate`: 1.5e-05
- `num_train_epochs`: 4
- `lr_scheduler_type`: cosine
- `warmup_ratio`: 0.05
- `bf16`: True
- `dataloader_num_workers`: 16
- `load_best_model_at_end`: True
- `gradient_checkpointing`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 512
- `per_device_eval_batch_size`: 8
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 4
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 1.5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 4
- `max_steps`: -1
- `lr_scheduler_type`: cosine
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.05
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
- `dataloader_num_workers`: 16
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
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: True
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
- `include_num_input_tokens_seen`: False
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch  | Step | Training Loss | umls_sota_eval_cosine_ndcg@10 |
|:------:|:----:|:-------------:|:-----------------------------:|
| 0.0695 | 100  | 0.8266        | -                             |
| 0.1390 | 200  | 0.5384        | -                             |
| 0.2086 | 300  | 0.4742        | -                             |
| 0.2781 | 400  | 0.4355        | -                             |
| 0.3295 | 474  | -             | 0.9295                        |
| 0.3476 | 500  | 0.4137        | -                             |
| 0.4171 | 600  | 0.3961        | -                             |
| 0.4866 | 700  | 0.3817        | -                             |
| 0.5561 | 800  | 0.3739        | -                             |
| 0.6257 | 900  | 0.3564        | -                             |
| 0.6590 | 948  | -             | 0.9384                        |
| 0.6952 | 1000 | 0.3587        | -                             |
| 0.7647 | 1100 | 0.3525        | -                             |
| 0.8342 | 1200 | 0.3463        | -                             |
| 0.9037 | 1300 | 0.3395        | -                             |
| 0.9732 | 1400 | 0.3329        | -                             |
| 0.9885 | 1422 | -             | 0.9434                        |
| 1.0424 | 1500 | 0.3228        | -                             |
| 1.1119 | 1600 | 0.318         | -                             |
| 1.1814 | 1700 | 0.3141        | -                             |
| 1.2510 | 1800 | 0.3101        | -                             |
| 1.3177 | 1896 | -             | 0.9463                        |
| 1.3205 | 1900 | 0.3134        | -                             |
| 1.3900 | 2000 | 0.3097        | -                             |
| 1.4595 | 2100 | 0.3006        | -                             |
| 1.5290 | 2200 | 0.303         | -                             |
| 1.5985 | 2300 | 0.3003        | -                             |
| 1.6472 | 2370 | -             | 0.9484                        |
| 1.6681 | 2400 | 0.2949        | -                             |
| 1.7376 | 2500 | 0.2951        | -                             |
| 1.8071 | 2600 | 0.2939        | -                             |
| 1.8766 | 2700 | 0.2908        | -                             |
| 1.9461 | 2800 | 0.2912        | -                             |
| 1.9767 | 2844 | -             | 0.9502                        |
| 2.0153 | 2900 | 0.2869        | -                             |
| 2.0848 | 3000 | 0.2807        | -                             |
| 2.1543 | 3100 | 0.2771        | -                             |
| 2.2238 | 3200 | 0.2795        | -                             |
| 2.2934 | 3300 | 0.2756        | -                             |
| 2.3059 | 3318 | -             | 0.9510                        |
| 2.3629 | 3400 | 0.2758        | -                             |
| 2.4324 | 3500 | 0.2765        | -                             |
| 2.5019 | 3600 | 0.2752        | -                             |
| 2.5714 | 3700 | 0.2745        | -                             |
| 2.6354 | 3792 | -             | 0.9515                        |
| 2.6409 | 3800 | 0.2714        | -                             |
| 2.7105 | 3900 | 0.2732        | -                             |
| 2.7800 | 4000 | 0.2735        | -                             |
| 2.8495 | 4100 | 0.2722        | -                             |
| 2.9190 | 4200 | 0.2713        | -                             |
| 2.9649 | 4266 | -             | 0.9520                        |
| 2.9885 | 4300 | 0.2721        | -                             |
| 3.0577 | 4400 | 0.2662        | -                             |
| 3.1272 | 4500 | 0.2654        | -                             |
| 3.1967 | 4600 | 0.2683        | -                             |
| 3.2662 | 4700 | 0.2687        | -                             |
| 3.2941 | 4740 | -             | 0.9523                        |
| 3.3358 | 4800 | 0.2665        | -                             |
| 3.4053 | 4900 | 0.2686        | -                             |
| 3.4748 | 5000 | 0.2612        | -                             |
| 3.5443 | 5100 | 0.263         | -                             |
| 3.6138 | 5200 | 0.264         | -                             |
| 3.6236 | 5214 | -             | 0.9523                        |
| 3.6834 | 5300 | 0.2672        | -                             |
| 3.7529 | 5400 | 0.2674        | -                             |
| 3.8224 | 5500 | 0.2631        | -                             |
| 3.8919 | 5600 | 0.2631        | -                             |
| 3.9531 | 5688 | -             | 0.9525                        |
| 3.9614 | 5700 | 0.2642        | -                             |


### Framework Versions
- Python: 3.11.11
- Sentence Transformers: 3.4.1
- Transformers: 4.53.2
- PyTorch: 2.6.0+cu124
- Accelerate: 1.5.2
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