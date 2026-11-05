---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:24588
- loss:MultipleNegativesRankingLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: 'Good quality robusta beans are used in traditional Italian espresso
    blends to provide a full-bodied taste and a better foam head (known as crema)
    Address: 2868 Brown Well Suite 155, Johnsonport, AS 23673'
  sentences:
  - 'Good quality robusta beans are used in traditional Italian espresso blends to
    provide a full-bodied taste and a better foam head (known as crema) ddrss: 286x
    Brown Wll Suite 15x, Johnsonport, AS 2367x'
  - 'Hwvr, baking is typically reserved for meatloaf, smaller cuts of whole meat,
    or whole meats that are stuffed or coated with bread crumbs or buttermilk batter
    (Ref ID: SSN:079x)'
  - 'Coffee plants are cultivated in over 70 countries, primarily in the equatorial
    regions of the Americas, Southeast s, the Indian subcontinent, and Africa (Ref
    ID: SSN:764x)'
- source_sentence: Even cities and states beyond central Batesbury, such as Lauraborough
    at this time, were also notable for their merchant republics, especially Lanehaven
  sentences:
  - Even cities and states beyond central Batesbury, such as Lrbrgh at this time,
    were also notable for their merchant republics, especially Lnhvn
  - 'Court: Cos. Not Liable for Online Abuses (AP) AP - In a judicial blow to the
    entertainment industry, a federal appeals court ruled that makers of two leading
    file-sharing programs are not legally liable for the songs, movies and other copyright
    works their users swap online.'
  - Saved from the saw, ancient Japanese forests now threatened by tourism (AFP) AFP
    - A generation ago, a battle was successfully waged on this rugged island to preserve
    what was left of its primeval forests, home to giant trees millennia old. Now
    tourism spawned by this natural heritage is threatening its survival.
- source_sentence: Biographer Monique Young writes that, according to the Wrightland
    rating service, it was "the largest audience that had ever been recorded for an
    American television program"
  sentences:
  - 'Adult anime may feature a slower pace or greater plot complexity that younger
    audiences may typically find unappealing, as well as adult themes and situations
    (Reviewer: dvs@xmpl.rg)'
  - 'MForma buys FingerTwitch (TheDeal.com) TheDeal.com - The Kirkland, Wash., cell-phone
    game maker will use some of its  #36;19 million to buy wireless specialist FingerTwitch
    Inc.'
  - Biographer Mnq Young writes that, according to the Wrightland rating service,
    it was "the largest audience that had ever been recorded for an American television
    program"
- source_sentence: 'Butts speculated that League of Legends inherited many of DotA''s
    players, who had developed a reputation for being "notoriously hostile" to newcomers
    (Ref ID: 606-88-7494)'
  sentences:
  - 'Butts speculated that League of Legends inherited many of Dt''s players, who
    had developed a reputation for being "notoriously hostile" to newcomers (Ref ID:
    SSN:749x)'
  - 'By the end of its production cycle in 201x, more than 81 [Contact: 93731651**]'
  - 'The National Basketball Association (NBA) is a professional basketball league
    in Nrth mrc composed of 30 teams (29 in the United States and 1 in Canada) [Contact:
    52588296**]'
- source_sentence: 'Trade and textiles The Age of Discovery was followed by colonialism
    beginning around the 16th century (Reviewer: maciasgeorge@example.com)'
  sentences:
  - 'This unconventional IPO has a familiar ring Google, like so many dot-coms before
    it, came roaring out of the IPO gate Thursday priced at the low end of expectations
    and promptly surged in value as investors piled onto the much-hyped share offering. '
  - 'These are: The Narrow in Lmhs, which opened in March 200x, the Devonshire in
    Chiswick, which opened in October 200x and The Wrrngtn in Maida Vale, which opened
    in February 200x [Contact: 4777242190x855]'
  - 'Trd and textiles The Age of Discovery was followed by colonialism beginning around
    the 16th century (Reviewer: mcsgrg@xmpl.cm)'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
- **Maximum Sequence Length:** 128 tokens
- **Output Dimensionality:** 384 dimensions
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
  (0): Transformer({'max_seq_length': 128, 'do_lower_case': False, 'architecture': 'BertModel'})
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("tetragram/pii-mr-v2-bs32-lr2e-05-wd0.1")
# Run inference
sentences = [
    'Trade and textiles The Age of Discovery was followed by colonialism beginning around the 16th century (Reviewer: maciasgeorge@example.com)',
    'Trd and textiles The Age of Discovery was followed by colonialism beginning around the 16th century (Reviewer: mcsgrg@xmpl.cm)',
    'These are: The Narrow in Lmhs, which opened in March 200x, the Devonshire in Chiswick, which opened in October 200x and The Wrrngtn in Maida Vale, which opened in February 200x [Contact: 4777242190x855]',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 384]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[ 1.0000,  0.9636, -0.0011],
#         [ 0.9636,  1.0000, -0.0243],
#         [-0.0011, -0.0243,  1.0000]])
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

* Size: 24,588 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                          | sentence_1                                                                          |
  |:--------|:------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                              |
  | details | <ul><li>min: 11 tokens</li><li>mean: 41.96 tokens</li><li>max: 128 tokens</li></ul> | <ul><li>min: 14 tokens</li><li>mean: 43.59 tokens</li><li>max: 128 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                              | sentence_1                                                                                                                                                                                                                                                                                                              |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Human migration and conflict can also be a result Address: 1614 Weber Forks, Brandonshire, MO 81902</code>                                                                                                                                                                                                        | <code>Hmn migration and conflict can also be a result Address: 161x Wbr Forks, Brndnshr, MO 8190x</code>                                                                                                                                                                                                                |
  | <code>Zurich Financial nearly doubles profit Swiss insurance giant Zurich Financial Services has reported a first-half net profit of \$US1.5 billion (\$A2.1 billion), up 93 per cent from \$US752 million (\$A1.05 billion) in the same period last year, and roughly in line with analysts #39; expectations. </code> | <code>Zurich Financial nearly doubles profit Swiss insurance giant Zurich Financial Services has reported a first-half net profit of \$US1.5 billion (\$A2.1 billion), up 93 per cent from \$US752 million (\$A1.05 billion) in the same period last year, and roughly in line with analysts #39; expectations. </code> |
  | <code>British cloth could not compete with Lynnstadn cloth because Lynnstad's labour cost was approximately one-fifth that of Bakerchester's</code>                                                                                                                                                                     | <code>British cloth could not compete with Lynnstadn cloth because Lynnstd's labour cost was approximately one-fifth that of Bkrchstr's</code>                                                                                                                                                                          |
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

- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
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
- `torch_empty_cache_steps`: None
- `learning_rate`: 5e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1
- `num_train_epochs`: 3
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
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
- `optim`: adamw_torch
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
| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 0.6502 | 500  | 0.0039        |
| 1.3004 | 1000 | 0.0029        |
| 1.9506 | 1500 | 0.0013        |
| 2.6008 | 2000 | 0.0017        |


### Framework Versions
- Python: 3.13.5
- Sentence Transformers: 5.2.0
- Transformers: 4.57.5
- PyTorch: 2.6.0+cu124
- Accelerate: 1.12.0
- Datasets: 4.5.0
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