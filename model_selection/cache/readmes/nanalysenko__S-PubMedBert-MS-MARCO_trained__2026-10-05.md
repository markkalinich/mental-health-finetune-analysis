---
base_model: pritamdeka/S-PubMedBert-MS-MARCO
datasets: []
language: []
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:29127
- loss:MultipleNegativesRankingLoss
widget:
- source_sentence: Total protein count.
  sentences:
  - Ultrasound examination of the retroperitoneum
  - Study of the level of total protein in the blood
  - Tracheobronchoscopy
- source_sentence: X-ray of the lower limb or upper limb (shoulder, thigh, lower leg)
    in two projections
  sentences:
  - Spiral computed tomography of the middle zone of the facial skull
  - Primary appointment (examination, consultation) with an oncologist
  - X-ray of the humerus
- source_sentence: A set of studies to identify an allergen (panel 2. Respiratory
    allergens of 20 types)
  sentences:
  - Determination of the ratio of protein fractions by electrophoresis
  - Diagnostic arthroscopy
  - A set of studies to identify an allergen
- source_sentence: Culture for gonococcus (N.gonorrhoeae) with determination of sensitivity
    to antibiotics
  sentences:
  - Bacteriological examination of discharge from the mucous membrane of the oropharynx
    for gonococcus (Neisseria gonorrhoeae)
  - Dispensary appointment (examination, consultation) with a pediatric dentist
  - Determination of DNA of herpes virus type 6 (HHV6) by PCR in peripheral and umbilical
    cord blood, quantitative study
- source_sentence: (xxSK) Appointment (examination, consultation) with an otorhinolaryngologist,
    head of the primary surgical department
  sentences:
  - Primary appointment (examination, consultation) with an audiologist-otorhinolaryngologist
  - Dispensary appointment (examination, consultation) with a nephrologist
  - Biopsy of tumors, tumor-like formations of soft tissues
---

# SentenceTransformer based on pritamdeka/S-PubMedBert-MS-MARCO

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [pritamdeka/S-PubMedBert-MS-MARCO](https://huggingface.co/pritamdeka/S-PubMedBert-MS-MARCO). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [pritamdeka/S-PubMedBert-MS-MARCO](https://huggingface.co/pritamdeka/S-PubMedBert-MS-MARCO) <!-- at revision 823e11bad71327e538638657ec11b85ba91d3e12 -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 768 tokens
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
    '(xxSK) Appointment (examination, consultation) with an otorhinolaryngologist, head of the primary surgical department',
    'Primary appointment (examination, consultation) with an audiologist-otorhinolaryngologist',
    'Dispensary appointment (examination, consultation) with a nephrologist',
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


* Size: 29,127 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                        |
  |:--------|:-----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                            |
  | details | <ul><li>min: 3 tokens</li><li>mean: 16.57 tokens</li><li>max: 106 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 14.36 tokens</li><li>max: 47 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                     | sentence_1                                                                            |
  |:-----------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------|
  | <code>Carrying out a glucose tolerance test (Glucose after 2 hours with a glucose load)</code> | <code>Carrying out a glucose tolerance test</code>                                    |
  | <code>Free beta-hCG subunit (prenatal screening)</code>                                        | <code>A set of studies to determine pregnancy</code>                                  |
  | <code>Ultrasound duplex scanning of arteries and veins of the lower extremities</code>         | <code>Duplex scanning of vessels (arteries and veins) of the lower extremities</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `num_train_epochs`: 11
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 11
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
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin

</details>

### Training Logs
| Epoch   | Step  | Training Loss |
|:-------:|:-----:|:-------------:|
| 0.5488  | 500   | 0.6758        |
| 1.0977  | 1000  | 0.2424        |
| 1.6465  | 1500  | 0.2168        |
| 2.1954  | 2000  | 0.1876        |
| 2.7442  | 2500  | 0.1727        |
| 3.2931  | 3000  | 0.1594        |
| 3.8419  | 3500  | 0.1509        |
| 4.3908  | 4000  | 0.1437        |
| 4.9396  | 4500  | 0.1358        |
| 5.4885  | 5000  | 0.1285        |
| 6.0373  | 5500  | 0.1232        |
| 6.5862  | 6000  | 0.1233        |
| 7.1350  | 6500  | 0.1157        |
| 7.6839  | 7000  | 0.1144        |
| 8.2327  | 7500  | 0.1099        |
| 8.7816  | 8000  | 0.1086        |
| 9.3304  | 8500  | 0.1047        |
| 9.8793  | 9000  | 0.1027        |
| 10.4281 | 9500  | 0.1           |
| 10.9769 | 10000 | 0.099         |


### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.0.1
- Transformers: 4.42.4
- PyTorch: 2.3.1+cu121
- Accelerate: 0.33.0
- Datasets: 2.20.0
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