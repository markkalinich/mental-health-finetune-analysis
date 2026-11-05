---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:33200
- loss:MultipleNegativesRankingLoss
base_model: google/embeddinggemma-300m
widget:
- source_sentence: Are stroke patients' reports of home blood pressure readings reliable?
  sentences:
  - The first Whitehall study.
  - A total of 1027 monitor and 716 booklet readings were recorded. Ninety per cent
    of booklet recordings were exactly the same as the BP monitor readings. Average
    booklet readings were 0.6 mmHg systolic [95% confidence interval (95% CI) -0.6
    to 1.8] and 0.3 mmHg diastolic (95% CI -0.3 to 0.8) lower than those on the monitor.
  - 'Protocol 1: a) office blood pressure measurement and Home1 were significantly
    higher than ambulatory blood pressure monitoring, except for systolic and diastolic
    office blood pressure measurement taken by the patient or a family member, systolic
    blood pressure taken by a nurse, and diastolic blood pressure taken by a physician.
    b) ambulatory blood pressure monitoring and HBPM1 were similar. Protocol 2: a)
    HBPM2 and Home2 were similar. b) Home2 was significantly lower than Home1, except
    for diastolic blood pressure taken by a nurse or the patient. There were significant
    relationships between: a) diastolic blood pressure measured by the patient and
    the thickness of the interventricular septum, posterior wall, and left ventricular
    mass; and b) ambulatory and HBPM2 diastolic and systolic blood pressure taken
    by a physician (home2) and left ventricular mass. Therefore, the data indicate
    that home blood pressure measurement and ambulatory blood pressure monitoring
    had good prognostic values relative to "office measurement."'
- source_sentence: Do socioeconomic differences in mortality persist after retirement?
  sentences:
  - to compare the mortality rates of elderly demented and nondemented subjects and
    the differential association of midlife risk factors with mortality according
    to dementia status.
  - Death.
  - To investigate polysomnographic and anthropomorphic factors predicting need of
    high optimal continuous positive airway pressure (CPAP).
- source_sentence: Does a history of unintended pregnancy lessen the likelihood of
    desire for sterilization reversal?
  sentences:
  - Evolutionary life history theory predicts that, in the absence of contraception,
    any enhancement of maternal condition can increase human fertility. Energetic
    trade-offs are likely to be resolved in favour of maximizing reproductive success
    rather than health or longevity. Here we find support for the hypothesis that
    development initiatives designed to improve maternal and child welfare may also
    incur costs associated with increased family sizes if they do not include a family
    planning component.
  - This study used national, cross-sectional data collected by the 2006-2010 National
    Survey of Family Growth. The study sample included women ages 15-44 who were surgically
    sterile from a tubal sterilization at the time of interview. Multivariable logistic
    regression was used to examine the relationship between a history of unintended
    pregnancy and desire for sterilization reversal while controlling for potential
    confounders.
  - Anti-HTLV-I antibodies were positive in both the serum and the CSF in all of the
    patients. Biopsied sample from spinal cord lesions showed inflammatory changes
    in Patient 1. Patient 2 had a demyelinating type of sensorimotor polyneuropathy.
    Two of the three patients examined showed high risk of developing HAM/TSP in virologic
    and immunologic aspects.
- source_sentence: Are behavioural risk factors to be blamed for the conversion from
    optimal blood pressure to hypertensive status in Black South Africans?
  sentences:
  - Longitudinal cohort studies in sub-Saharan Africa are urgently needed to understand
    cardiovascular disease development. We, therefore, explored health behaviours
    and conventional risk factors of African individuals with optimal blood pressure
    (BP) (≤ 120/80 mm Hg), and their 5-year prediction for the development of hypertension.
  - The primary aim was to assess long-term blood pressure in 110 patients with Type
    2 diabetes who had achieved optimal blood pressure control during attendance at
    a protocol-based nurse-led hypertension intensive intervention clinic 7 years
    previously. The secondary aim was to assess modifiable cardiovascular risk factor
    status.
  - The Prospective Urban Rural Epidemiology study in the North West Province, South
    Africa, started in 2005 and included African volunteers (n = 1994; aged>30 years)
    from a sample of 6000 randomly selected households in rural and urban areas.
- source_sentence: Can you deliver accurate tidal volume by manual resuscitator?
  sentences:
  - One of the problems with manual resuscitators is the difficulty in achieving accurate
    volume delivery. The volume delivered to the patient varies by the physical characteristics
    of the person and method. This study was designed to compare tidal volumes delivered
    by the squeezing method, physical characteristics and education and practice levels.
  - Sections from paraffin-embedded blocks of surgically resected specimens of GBC
    (69 cases), XGC (65), chronic cholecystitis (18) and control gallbladder (10)
    were stained with the monoclonal antibodies to p53 and PCNA, and a polyclonal
    antibody to beta-catenin. p53 expression was scored as the percentage of nuclei
    stained. PCNA expression was scored as the product of the percentage of nuclei
    stained and the intensity of the staining (1-3). A cut-off value of 80 for this
    score was taken as a positive result. Beta-catenin expression was scored as type
    of expression-membranous, cytoplasmic or nuclear staining.
  - Although current resuscitation guidelines are rescuer focused, the opportunity
    exists to develop patient-centered resuscitation strategies that optimize the
    hemodynamic response of the individual in the hopes to improve survival.
datasets:
- pavanmantha/pubmed-30k
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on google/embeddinggemma-300m

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [google/embeddinggemma-300m](https://huggingface.co/google/embeddinggemma-300m) on the [pubmed-30k](https://huggingface.co/datasets/pavanmantha/pubmed-30k) dataset. It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [google/embeddinggemma-300m](https://huggingface.co/google/embeddinggemma-300m) <!-- at revision 57c266a740f537b4dc058e1b0cda161fd15afa75 -->
- **Maximum Sequence Length:** 2048 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - [pubmed-30k](https://huggingface.co/datasets/pavanmantha/pubmed-30k)
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 2048, 'do_lower_case': False, 'architecture': 'Gemma3TextModel'})
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
  (2): Dense({'in_features': 768, 'out_features': 3072, 'bias': False, 'activation_function': 'torch.nn.modules.linear.Identity'})
  (3): Dense({'in_features': 3072, 'out_features': 768, 'bias': False, 'activation_function': 'torch.nn.modules.linear.Identity'})
  (4): Normalize()
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
model = SentenceTransformer("pavanmantha/embeddinggemma-pubmed")
# Run inference
queries = [
    "Can you deliver accurate tidal volume by manual resuscitator?",
]
documents = [
    'One of the problems with manual resuscitators is the difficulty in achieving accurate volume delivery. The volume delivered to the patient varies by the physical characteristics of the person and method. This study was designed to compare tidal volumes delivered by the squeezing method, physical characteristics and education and practice levels.',
    'Although current resuscitation guidelines are rescuer focused, the opportunity exists to develop patient-centered resuscitation strategies that optimize the hemodynamic response of the individual in the hopes to improve survival.',
    'Sections from paraffin-embedded blocks of surgically resected specimens of GBC (69 cases), XGC (65), chronic cholecystitis (18) and control gallbladder (10) were stained with the monoclonal antibodies to p53 and PCNA, and a polyclonal antibody to beta-catenin. p53 expression was scored as the percentage of nuclei stained. PCNA expression was scored as the product of the percentage of nuclei stained and the intensity of the staining (1-3). A cut-off value of 80 for this score was taken as a positive result. Beta-catenin expression was scored as type of expression-membranous, cytoplasmic or nuclear staining.',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 768] [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[ 0.9156,  0.2237, -0.1894]])
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

#### pubmed-30k

* Dataset: [pubmed-30k](https://huggingface.co/datasets/pavanmantha/pubmed-30k) at [6a7c15c](https://huggingface.co/datasets/pavanmantha/pubmed-30k/tree/6a7c15c83164ef44a767f4da72b5e71bd920104f)
* Size: 33,200 training samples
* Columns: <code>anchor</code>, <code>positive</code>, and <code>negative</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                             | positive                                                                           | negative                                                                           |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                             | string                                                                             |
  | details | <ul><li>min: 11 tokens</li><li>mean: 17.74 tokens</li><li>max: 36 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 85.76 tokens</li><li>max: 301 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 82.14 tokens</li><li>max: 409 tokens</li></ul> |
* Samples:
  | anchor                                                                                                          | positive                                                                                                                                                                                                                                                       | negative                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
  |:----------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Does a history of unintended pregnancy lessen the likelihood of desire for sterilization reversal?</code> | <code>Unintended pregnancy has been significantly associated with subsequent female sterilization. Whether women who are sterilized after experiencing an unintended pregnancy are less likely to express desire for sterilization reversal is unknown.</code> | <code>Changes in serum hormone levels induced by combined contraceptives.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  | <code>Does a history of unintended pregnancy lessen the likelihood of desire for sterilization reversal?</code> | <code>Unintended pregnancy has been significantly associated with subsequent female sterilization. Whether women who are sterilized after experiencing an unintended pregnancy are less likely to express desire for sterilization reversal is unknown.</code> | <code>Evolutionary life history theory predicts that, in the absence of contraception, any enhancement of maternal condition can increase human fertility. Energetic trade-offs are likely to be resolved in favour of maximizing reproductive success rather than health or longevity. Here we find support for the hypothesis that development initiatives designed to improve maternal and child welfare may also incur costs associated with increased family sizes if they do not include a family planning component.</code>                                                                                                                                                                                                                                 |
  | <code>Does a history of unintended pregnancy lessen the likelihood of desire for sterilization reversal?</code> | <code>Unintended pregnancy has been significantly associated with subsequent female sterilization. Whether women who are sterilized after experiencing an unintended pregnancy are less likely to express desire for sterilization reversal is unknown.</code> | <code>Out of 663 cycles resulting in oocyte retrieval, 299 produced a clinical pregnancy (45.1%). Women who achieved a clinical pregnancy had a significantly shorter stimulation length (11.9 vs. 12.1 days, p = 0.047). Polycystic ovary syndrome (PCOS) was the only etiology of infertility that was significantly associated with a higher chance for clinical pregnancy and was a significant confounder for the association of duration and success of treatment. Women with 13 days or longer of stimulation had a 34 % lower chance of clinical pregnancy as compared to those who had a shorter cycle (OR 0.66, 95% CI:0.46-0.95) after adjustment for age, ovarian reserve, number of oocytes retrieved, embryos transferred and PCOS diagnosis.</code> |
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

- `per_device_train_batch_size`: 16
- `learning_rate`: 2e-05
- `warmup_steps`: 0.1
- `gradient_accumulation_steps`: 4
- `fp16`: True
- `warmup_ratio`: 0.1
- `prompts`: task: sentence similarity | query: 

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 16
- `num_train_epochs`: 3
- `max_steps`: -1
- `learning_rate`: 2e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0.1
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 4
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
- `eval_strategy`: no
- `per_device_eval_batch_size`: 8
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
- `load_best_model_at_end`: False
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
- `prompts`: task: sentence similarity | query: 
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 0.1928 | 100  | 0.2086        |
| 0.3855 | 200  | 0.0872        |
| 0.5783 | 300  | 0.0623        |
| 0.7711 | 400  | 0.0569        |
| 0.9639 | 500  | 0.0487        |
| 1.1561 | 600  | 0.0423        |
| 1.3489 | 700  | 0.0412        |
| 1.5417 | 800  | 0.0407        |
| 1.7345 | 900  | 0.0341        |
| 1.9272 | 1000 | 0.0384        |
| 2.1195 | 1100 | 0.0316        |
| 2.3123 | 1200 | 0.0290        |
| 2.5051 | 1300 | 0.0314        |
| 2.6978 | 1400 | 0.0303        |
| 2.8906 | 1500 | 0.0245        |


### Framework Versions
- Python: 3.11.11
- Sentence Transformers: 5.2.3
- Transformers: 5.2.0
- PyTorch: 2.8.0.dev20250319+cu128
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