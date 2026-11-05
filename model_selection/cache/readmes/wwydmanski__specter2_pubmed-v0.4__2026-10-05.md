---
base_model: allenai/specter2_base
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:8705
- loss:MultipleNegativesRankingLoss
widget:
- source_sentence: Vaccine Administration in High-Risk Groups
  sentences:
  - '[V+: strategies improving vaccination coverage among children with chronic diseases]. '
  - 'Medical writer welcomes advice on working with medical writers. '
  - 'Vaccination management. '
- source_sentence: Eosinophil recruitment and STAT6 signalling pathway in nematode
    infections
  sentences:
  - 'The roles of eotaxin and the STAT6 signalling pathway in eosinophil recruitment
    and host resistance to the nematodes Nippostrongylus brasiliensis and Heligmosomoides
    bakeri. '
  - 'ABO blood groups from Palamau, Bihar, India. '
  - 'Both stat5a and stat5b are required for antigen-induced eosinophil and T-cell
    recruitment into the tissue. '
- source_sentence: Constitutional Medicine Status
  sentences:
  - '[Present status of constitutional medicine]. '
  - 'Convergence of submodality-specific input onto neurons in primary somatosensory
    cortex. '
  - 'The link between health and wellbeing and constitutional recognition. '
- source_sentence: Telehealth challenges
  sentences:
  - '[Technological transformations and evolution of the medical practice: current
    status, issues and perspectives for the development of telemedicine]. '
  - 'The untapped potential of Telehealth. '
  - 'Enhanced chartreusin solubility by hydroxybenzoate hydrotropy. '
- source_sentence: Kawasaki disease immunoprophylaxis
  sentences:
  - '[Effect of immunoglobulin in the prevention of coronary artery aneurysms in Kawasaki
    disease]. '
  - 'Management of Kawasaki disease. '
  - 'IgA anti-epidermal transglutaminase antibodies in dermatitis herpetiformis and
    pediatric celiac disease. '
---

# SentenceTransformer based on allenai/specter2_base

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [allenai/specter2_base](https://huggingface.co/allenai/specter2_base) on the json dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

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
    'Kawasaki disease immunoprophylaxis',
    '[Effect of immunoglobulin in the prevention of coronary artery aneurysms in Kawasaki disease]. ',
    'Management of Kawasaki disease. ',
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

#### json

* Dataset: json
* Size: 8,705 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                          | positive                                                                          | negative                                                                          |
  |:--------|:--------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
  | type    | string                                                                          | string                                                                            | string                                                                            |
  | details | <ul><li>min: 4 tokens</li><li>mean: 7.6 tokens</li><li>max: 18 tokens</li></ul> | <ul><li>min: 6 tokens</li><li>mean: 19.26 tokens</li><li>max: 42 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 11.72 tokens</li><li>max: 46 tokens</li></ul> |
* Samples:
  | anchor                                                                               | positive                                                                                                                                                          | negative                                                            |
  |:-------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------|
  | <code>Telehealth challenges</code>                                                   | <code>[Technological transformations and evolution of the medical practice: current status, issues and perspectives for the development of telemedicine]. </code> | <code>The untapped potential of Telehealth. </code>                 |
  | <code>Racial disparities in mental health treatment</code>                           | <code>Relationships between stigma, depression, and treatment in white and African American primary care patients. </code>                                        | <code>Mental Health Care Disparities Now and in the Future. </code> |
  | <code>Iatrogenic hyperkalemia in elderly patients with cardiovascular disease</code> | <code>Iatrogenic hyperkalemia as a serious problem in therapy of cardiovascular diseases in elderly patients. </code>                                             | <code>The cardiovascular implications of hypokalemia. </code>       |
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
- `learning_rate`: 2e-05
- `num_train_epochs`: 1
- `lr_scheduler_type`: cosine_with_restarts
- `warmup_ratio`: 0.1
- `bf16`: True
- `batch_sampler`: no_duplicates

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
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 1
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
| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 0.0110 | 1    | 2.9861        |
| 0.0220 | 2    | 2.9379        |
| 0.0330 | 3    | 3.0613        |
| 0.0440 | 4    | 2.8081        |
| 0.0549 | 5    | 2.6516        |
| 0.0659 | 6    | 2.3688        |
| 0.0769 | 7    | 2.0502        |
| 0.0879 | 8    | 1.7557        |
| 0.0989 | 9    | 1.5316        |
| 0.1099 | 10   | 1.2476        |
| 0.1209 | 11   | 1.1529        |
| 0.1319 | 12   | 0.9483        |
| 0.1429 | 13   | 0.7187        |
| 0.1538 | 14   | 0.6824        |
| 0.1648 | 15   | 0.593         |
| 0.1758 | 16   | 0.4593        |
| 0.1868 | 17   | 0.3737        |
| 0.1978 | 18   | 0.5082        |
| 0.2088 | 19   | 0.4232        |
| 0.2198 | 20   | 0.3089        |
| 0.2308 | 21   | 0.2057        |
| 0.2418 | 22   | 0.2358        |
| 0.2527 | 23   | 0.2291        |
| 0.2637 | 24   | 0.2707        |
| 0.2747 | 25   | 0.1359        |
| 0.2857 | 26   | 0.2294        |
| 0.2967 | 27   | 0.157         |
| 0.3077 | 28   | 0.0678        |
| 0.3187 | 29   | 0.1022        |
| 0.3297 | 30   | 0.0713        |
| 0.3407 | 31   | 0.0899        |
| 0.3516 | 32   | 0.1385        |
| 0.3626 | 33   | 0.0809        |
| 0.3736 | 34   | 0.1053        |
| 0.3846 | 35   | 0.0925        |
| 0.3956 | 36   | 0.0675        |
| 0.4066 | 37   | 0.0841        |
| 0.4176 | 38   | 0.0366        |
| 0.4286 | 39   | 0.0768        |
| 0.4396 | 40   | 0.0529        |
| 0.4505 | 41   | 0.0516        |
| 0.4615 | 42   | 0.0342        |
| 0.4725 | 43   | 0.0456        |
| 0.4835 | 44   | 0.0344        |
| 0.4945 | 45   | 0.1337        |
| 0.5055 | 46   | 0.0883        |
| 0.5165 | 47   | 0.0691        |
| 0.5275 | 48   | 0.0322        |
| 0.5385 | 49   | 0.0731        |
| 0.5495 | 50   | 0.0376        |
| 0.5604 | 51   | 0.0464        |
| 0.5714 | 52   | 0.0173        |
| 0.5824 | 53   | 0.0516        |
| 0.5934 | 54   | 0.0703        |
| 0.6044 | 55   | 0.0273        |
| 0.6154 | 56   | 0.0374        |
| 0.6264 | 57   | 0.0292        |
| 0.6374 | 58   | 0.1195        |
| 0.6484 | 59   | 0.0852        |
| 0.6593 | 60   | 0.0697        |
| 0.6703 | 61   | 0.0653        |
| 0.6813 | 62   | 0.0426        |
| 0.6923 | 63   | 0.0288        |
| 0.7033 | 64   | 0.0344        |
| 0.7143 | 65   | 0.104         |
| 0.7253 | 66   | 0.0251        |
| 0.7363 | 67   | 0.0095        |
| 0.7473 | 68   | 0.0208        |
| 0.7582 | 69   | 0.0814        |
| 0.7692 | 70   | 0.0813        |
| 0.7802 | 71   | 0.0508        |
| 0.7912 | 72   | 0.032         |
| 0.8022 | 73   | 0.0879        |
| 0.8132 | 74   | 0.095         |
| 0.8242 | 75   | 0.0932        |
| 0.8352 | 76   | 0.0868        |
| 0.8462 | 77   | 0.0231        |
| 0.8571 | 78   | 0.0144        |
| 0.8681 | 79   | 0.0179        |
| 0.8791 | 80   | 0.0457        |
| 0.8901 | 81   | 0.0935        |
| 0.9011 | 82   | 0.0658        |
| 0.9121 | 83   | 0.0553        |
| 0.9231 | 84   | 0.003         |
| 0.9341 | 85   | 0.0036        |
| 0.9451 | 86   | 0.0034        |
| 0.9560 | 87   | 0.0032        |
| 0.9670 | 88   | 0.0026        |
| 0.9780 | 89   | 0.0042        |
| 0.9890 | 90   | 0.0024        |
| 1.0    | 91   | 0.0022        |


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