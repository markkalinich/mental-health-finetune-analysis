---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:148295
- loss:SymmetricLoss
base_model: dmis-lab/biobert-v1.1
widget:
- source_sentence: Complications of pregnancy; childbirth; and the puerperium → Complications
    during labor → Forceps delivery
  sentences:
  - Complications of pregnancy; childbirth; and the puerperium → Complications during
    labor
  - Complications of pregnancy; childbirth; and the puerperium → Other complications
    of birth; puerperium affecting management of mother
  - Complications of pregnancy; childbirth; and the puerperium → Normal pregnancy
    and/or delivery → Other pregnancy and delivery including normal
- source_sentence: Complications of pregnancy; childbirth; and the puerperium → Complications
    mainly related to pregnancy → Early or threatened labor
  sentences:
  - Complications of pregnancy; childbirth; and the puerperium → Complications mainly
    related to pregnancy
  - Complications of pregnancy; childbirth; and the puerperium → Abortion-related
    disorders → Postabortion complications
  - Complications of pregnancy; childbirth; and the puerperium → Indications for care
    in pregnancy; labor; and delivery
- source_sentence: Diseases of the respiratory system → Respiratory infections → Acute
    bronchitis
  sentences:
  - Diseases of the respiratory system → Asthma → Asthma
  - Diseases of the respiratory system → Lung disease due to external agents
  - Diseases of the respiratory system → Respiratory infections
- source_sentence: Diseases of the circulatory system → Diseases of the heart → Cardiac
    arrest and ventricular fibrillation
  sentences:
  - Diseases of the circulatory system → Hypertension → Essential hypertension
  - Diseases of the circulatory system → Cerebrovascular disease
  - Diseases of the circulatory system → Diseases of the heart
- source_sentence: Infectious and parasitic diseases → Mycoses
  sentences:
  - Diseases of the skin and subcutaneous tissue → Skin and subcutaneous tissue infections
  - Mental illness
  - Infectious and parasitic diseases
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# HierarchyTransformer based on dmis-lab/biobert-v1.1

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [dmis-lab/biobert-v1.1](https://huggingface.co/dmis-lab/biobert-v1.1) <!-- at revision 551ca18efd7f052c8dfa0b01c94c2a8e68bc5488 -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 768 dimensions
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
HierarchyTransformer(
  (0): Transformer({'max_seq_length': 256, 'do_lower_case': False, 'architecture': 'BertModel'})
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
    'Infectious and parasitic diseases → Mycoses',
    'Infectious and parasitic diseases',
    'Mental illness',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.6610, 0.3361],
#         [0.6610, 1.0000, 0.2730],
#         [0.3361, 0.2730, 1.0000]])
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

* Size: 148,295 training samples
* Columns: <code>child</code>, <code>parent</code>, <code>parent_negative</code>, and <code>child_negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | child                                                                             | parent                                                                            | parent_negative                                                                   | child_negative                                                                     |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | string                                                                            | string                                                                             |
  | details | <ul><li>min: 8 tokens</li><li>mean: 25.19 tokens</li><li>max: 65 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 16.22 tokens</li><li>max: 41 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 16.94 tokens</li><li>max: 34 tokens</li></ul> | <ul><li>min: 11 tokens</li><li>mean: 23.48 tokens</li><li>max: 65 tokens</li></ul> |
* Samples:
  | child                                                                | parent                                         | parent_negative             | child_negative                                                                                      |
  |:---------------------------------------------------------------------|:-----------------------------------------------|:----------------------------|:----------------------------------------------------------------------------------------------------|
  | <code>Infectious and parasitic diseases → Bacterial infection</code> | <code>Infectious and parasitic diseases</code> | <code>Mental illness</code> | <code>Diseases of the nervous system and sense organs → Central nervous system infection</code>     |
  | <code>Infectious and parasitic diseases → Bacterial infection</code> | <code>Infectious and parasitic diseases</code> | <code>Mental illness</code> | <code>Diseases of the digestive system → Intestinal infection</code>                                |
  | <code>Infectious and parasitic diseases → Bacterial infection</code> | <code>Infectious and parasitic diseases</code> | <code>Mental illness</code> | <code>Diseases of the skin and subcutaneous tissue → Skin and subcutaneous tissue infections</code> |
* Loss: <code>hierarchy_transformers.losses.symmetric_loss.SymmetricLoss</code> with these parameters:
  ```json
  {
      "distance_metric": "PoincareBall(c=0.0013021096820011735).dist and dist0",
      "HyperbolicChildTriplet": {
          "weight": 1.0,
          "distance_metric": "PoincareBall(c=0.0013021096820011735).dist",
          "margin": 3.0
      },
      "HyperbolicParentTriplet": {
          "weight": 1.0,
          "distance_metric": "PoincareBall(c=0.0013021096820011735).dist",
          "margin": 3.0
      }
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: epoch
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 512
- `learning_rate`: 1e-05
- `num_train_epochs`: 10
- `warmup_steps`: 500
- `load_best_model_at_end`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: epoch
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 512
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 1
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 1e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 10
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 500
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
- `load_best_model_at_end`: True
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
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch   | Step     | Training Loss |
|:-------:|:--------:|:-------------:|
| 0.0863  | 100      | 2.1613        |
| 0.1726  | 200      | 0.5936        |
| 0.2588  | 300      | 0.1998        |
| 0.3451  | 400      | 0.1107        |
| 0.4314  | 500      | 0.0567        |
| 0.5177  | 600      | 0.0452        |
| 0.6040  | 700      | 0.032         |
| 0.6903  | 800      | 0.0279        |
| 0.7765  | 900      | 0.0218        |
| 0.8628  | 1000     | 0.0235        |
| 0.9491  | 1100     | 0.018         |
| 1.0     | 1159     | -             |
| 1.0354  | 1200     | 0.0192        |
| 1.1217  | 1300     | 0.0176        |
| 1.2079  | 1400     | 0.0137        |
| 1.2942  | 1500     | 0.0119        |
| 1.3805  | 1600     | 0.0139        |
| 1.4668  | 1700     | 0.0138        |
| 1.5531  | 1800     | 0.0123        |
| 1.6393  | 1900     | 0.0104        |
| 1.7256  | 2000     | 0.0117        |
| 1.8119  | 2100     | 0.0097        |
| 1.8982  | 2200     | 0.0133        |
| 1.9845  | 2300     | 0.01          |
| **2.0** | **2318** | **-**         |
| 2.0708  | 2400     | 0.0109        |
| 2.1570  | 2500     | 0.0074        |
| 2.2433  | 2600     | 0.0072        |
| 2.3296  | 2700     | 0.015         |
| 2.4159  | 2800     | 0.0069        |
| 2.5022  | 2900     | 0.0107        |
| 2.5884  | 3000     | 0.0094        |
| 2.6747  | 3100     | 0.0105        |
| 2.7610  | 3200     | 0.0095        |
| 2.8473  | 3300     | 0.0072        |
| 2.9336  | 3400     | 0.0084        |
| 3.0     | 3477     | -             |
| 3.0198  | 3500     | 0.0104        |
| 3.1061  | 3600     | 0.0078        |
| 3.1924  | 3700     | 0.008         |
| 3.2787  | 3800     | 0.0086        |
| 3.3650  | 3900     | 0.0085        |
| 3.4513  | 4000     | 0.0081        |
| 3.5375  | 4100     | 0.0093        |
| 3.6238  | 4200     | 0.0107        |
| 3.7101  | 4300     | 0.008         |
| 3.7964  | 4400     | 0.0099        |
| 3.8827  | 4500     | 0.0058        |
| 3.9689  | 4600     | 0.0084        |
| 4.0     | 4636     | -             |
| 4.0552  | 4700     | 0.01          |
| 4.1415  | 4800     | 0.0053        |
| 4.2278  | 4900     | 0.0075        |
| 4.3141  | 5000     | 0.0077        |
| 4.4003  | 5100     | 0.0065        |
| 4.4866  | 5200     | 0.0089        |
| 4.5729  | 5300     | 0.0082        |
| 4.6592  | 5400     | 0.0093        |
| 4.7455  | 5500     | 0.0076        |
| 4.8318  | 5600     | 0.0095        |
| 4.9180  | 5700     | 0.0078        |
| 5.0     | 5795     | -             |
| 5.0043  | 5800     | 0.0055        |
| 5.0906  | 5900     | 0.0061        |
| 5.1769  | 6000     | 0.005         |
| 5.2632  | 6100     | 0.0075        |
| 5.3494  | 6200     | 0.0079        |
| 5.4357  | 6300     | 0.006         |
| 5.5220  | 6400     | 0.0095        |
| 5.6083  | 6500     | 0.0099        |
| 5.6946  | 6600     | 0.0084        |
| 5.7808  | 6700     | 0.008         |
| 5.8671  | 6800     | 0.0064        |
| 5.9534  | 6900     | 0.0097        |
| 6.0     | 6954     | -             |
| 6.0397  | 7000     | 0.0063        |
| 6.1260  | 7100     | 0.0069        |
| 6.2123  | 7200     | 0.0095        |
| 6.2985  | 7300     | 0.0067        |
| 6.3848  | 7400     | 0.0056        |
| 6.4711  | 7500     | 0.0074        |
| 6.5574  | 7600     | 0.0086        |
| 6.6437  | 7700     | 0.0072        |
| 6.7299  | 7800     | 0.0065        |
| 6.8162  | 7900     | 0.0052        |
| 6.9025  | 8000     | 0.0101        |
| 6.9888  | 8100     | 0.0086        |
| 7.0     | 8113     | -             |
| 7.0751  | 8200     | 0.0065        |
| 7.1613  | 8300     | 0.0106        |
| 7.2476  | 8400     | 0.0049        |
| 7.3339  | 8500     | 0.0074        |
| 7.4202  | 8600     | 0.0065        |
| 7.5065  | 8700     | 0.004         |
| 7.5928  | 8800     | 0.0075        |
| 7.6790  | 8900     | 0.009         |
| 7.7653  | 9000     | 0.0059        |
| 7.8516  | 9100     | 0.0063        |
| 7.9379  | 9200     | 0.0095        |
| 8.0     | 9272     | -             |
| 8.0242  | 9300     | 0.0082        |
| 8.1104  | 9400     | 0.0067        |
| 8.1967  | 9500     | 0.0063        |
| 8.2830  | 9600     | 0.0071        |
| 8.3693  | 9700     | 0.0064        |
| 8.4556  | 9800     | 0.0072        |
| 8.5418  | 9900     | 0.0059        |
| 8.6281  | 10000    | 0.0085        |
| 8.7144  | 10100    | 0.0083        |
| 8.8007  | 10200    | 0.0046        |
| 8.8870  | 10300    | 0.0055        |
| 8.9733  | 10400    | 0.008         |
| 9.0     | 10431    | -             |
| 9.0595  | 10500    | 0.0066        |
| 9.1458  | 10600    | 0.0068        |
| 9.2321  | 10700    | 0.0093        |
| 9.3184  | 10800    | 0.0067        |
| 9.4047  | 10900    | 0.0054        |
| 9.4909  | 11000    | 0.0079        |
| 9.5772  | 11100    | 0.0052        |
| 9.6635  | 11200    | 0.0073        |
| 9.7498  | 11300    | 0.0088        |
| 9.8361  | 11400    | 0.005         |
| 9.9223  | 11500    | 0.0069        |
| 10.0    | 11590    | -             |

* The bold row denotes the saved checkpoint.
</details>

### Framework Versions
- Python: 3.10.13
- Sentence Transformers: 5.1.2
- Transformers: 4.57.1
- PyTorch: 2.9.0+cu128
- Accelerate: 1.11.0
- Datasets: 4.3.0
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

#### SymmetricLoss
```bibtex
@article{he2024language,
  title={Language models as hierarchy encoders},
  author={He, Yuan and Yuan, Zhangdie and Chen, Jiaoyan and Horrocks, Ian},
  journal={arXiv preprint arXiv:2401.11374},
  year={2024}
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