---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:20000
- loss:MultipleNegativesRankingLoss
base_model: google/embeddinggemma-300m
widget:
- source_sentence: >
    What are the criteria for evaluating the therapeutic efficacy of tumor
    treatment?
  sentences:
  - >-
    Detecting the sentinel node in gastric cancer is challenging due to the
    complex lymphatic drainage of the stomach. The lymphatic network in the
    stomach is considerably more complex than that of ectodermal organs like
    breast and skin, making it difficult to identify the sentinel node
    accurately. This complexity is attributed to the complex embryological
    development of the stomach.
  - >-
    The criteria for evaluating the therapeutic efficacy of tumor treatment
    include measuring and calculating the sum of the longest diameter of all
    target lesions and comparing it with the baseline sum of longest diameters.
    The objective tumor evaluation criteria include complete remission, partial
    remission, progressive disease, and stable disease.
  - >-
    Low levels of GAS7C mRNA expression have been frequently detected in lung
    cancer samples, particularly in stage IV and metastatic patients. This
    suggests an association between low GAS7C expression and cancer progression.
    Additionally, low GAS7C expression has been correlated with poorer survival
    in late-stage lung cancer patients from Asian and Caucasian populations.
    These findings indicate that GAS7C may serve as a prognostic biomarker in
    lung cancer patients with metastasis. Furthermore, it is possible that GAS7C
    may act as a metastasis suppressor in other types of cancer.
- source_sentence: >
    What are the limitations and challenges associated with CTLA-4 blockade as a
    treatment for advanced melanoma?
  sentences:
  - >-
    Patients with nonmetastatic RCC following nephrectomy can be risk-stratified
    using prognostic models such as the UISS scoring system and the Leibovich
    prognosis score. These models take into account factors such as TNM staging,
    performance status, tumor size, Fuhrman grade, and tumor necrosis to
    classify patients into low-, intermediate-, and high-risk groups. The UISS
    score and the Leibovich score have different criteria for risk
    stratification, but both provide information on the likelihood of
    cancer-specific survival or metastasis-free survival. It is important to
    note that these prognostic models were developed and validated using
    retrospective patient cohorts and may have limitations. Adjuvant clinical
    trials in RCC have largely focused on patients with intermediate- to
    high-risk disease based on these risk stratification methods.
  - >-
    FDG accumulation in RCC metastases is an indicator of biological activity
    and can predict the survival time of patients. Higher FDG accumulation in
    the primary origin compared to metastases suggests a poor prognosis for RCC
    patients. Lung metastases tend to show better response to therapies and
    longer survival compared to non-lung metastases.
  - >-
    While CTLA-4 blocking antibodies, such as ipilimumab, have been approved for
    the treatment of advanced melanoma, their effectiveness is limited to a
    subset of patients and the impact on survival remains limited. Resistance
    mechanisms to CTLA-4 blockade need to be identified. Additionally, the
    presence of an immunosuppressive microenvironment and the inhibitory role of
    IDO in antitumor therapies targeting immune checkpoints pose challenges to
    the efficacy of CTLA-4 blockade.
- source_sentence: >
    What are some alternative therapeutic strategies being evaluated for cancer
    treatment?
  sentences:
  - >-
    The combination of Chinese herbal therapies, such as PAM+V (tonifying blood
    yin, tonifying Spleen yin/qi, harmonizing Liver qi, and tonifying Kidney
    yang), with conventional therapies has been shown to improve survival
    outcomes in advanced non-small-cell lung cancer patients. In a retrospective
    survival analysis, patients treated with long-term PAM+V therapy combined
    with standard therapy achieved significantly better survival in stages IIIA,
    IIIB, and IV disease. The survival advantage was even stronger when
    comparing long-term users of PAM+V with external controls. These results
    suggest that prospective trials using PAM+V and vitamin therapy, in a
    whole-systems approach combined with conventional therapies, are justified
    for advanced non-small-cell lung cancer patients.
  - >-
    Prostate cancer management faces challenges such as overdiagnosis,
    overtreatment, and the need for accurate diagnosis, treatment selection, and
    individualized approaches. Precision medicine in prostate cancer aims to
    address these challenges by providing more accurate diagnostic tests,
    guiding the selection of necessary curative treatments, offering appropriate
    adjuvant therapy after radical prostatectomy, and identifying good
    candidates for secondary hormonal manipulation in castration-resistant
    prostate cancer.
  - >-
    One alternative therapeutic strategy being evaluated for cancer treatment is
    hyperthermia. Hyperthermia involves exposing biological tissues to
    temperatures higher than normal to selectively destroy abnormal cells. This
    approach can inhibit tumor cell proliferation by destroying cancer cells or
    making them more sensitive to the effects of conventional antitumor
    therapies. Various heating sources, such as radiofrequency, microwaves, and
    ultrasound waves, have been used to produce moderate heating in a specific
    target region. However, the use of these heating sources is limited due to
    the damage they cause to surrounding healthy tissues.
- source_sentence: >
    What are the potential implications of CD200 expression in Merkel cell
    carcinoma (MCC)?
  sentences:
  - >-
    The prognosis for breast carcinoid is similar to that for other primary
    breast carcinomas and correlates with stage, size, and lymph node status.
    Localized spread in primary breast carcinoid has been reported to have
    favorable outcomes. Roughly 18% of all mammary carcinoid cases have involved
    nodal or distant metastases, which occurred only after the tumor had
    achieved a size of 2.5 cm or greater with 10 or more mitoses per high-power
    field. Metastatic breast carcinoid appears to carry with it a prognosis
    similar to that of carcinoid metastatic to other locations. Treatment for
    primary mammary carcinoid is also similar to that for other primary breast
    carcinomas and includes lumpectomy for small lesions or modified radical
    mastectomy for greater disease spread. Adjuvant radiation therapy and
    chemotherapeutic agents such as cisplatin and etoposide may also be used.
  - >-
    CD200 expression was observed in a high percentage (84%) of MCC cases.
    However, the expression of CD200 does not add much to the
    immunohistochemical diagnosis of MCC, as MCC already has a well-defined
    immunoprofile. Nonetheless, the expression of CD200 in MCC warrants further
    study to determine if it plays a role in the biology of the disease, if it
    represents a potential therapeutic target, or if loss of CD200 affects
    prognosis.
  - >-
    The risk factors associated with delayed recurrence after liver resection
    for HCC include the presence of cirrhosis (F4), hepatitis activity,
    multinodularity, vascular invasion, and moderate or poorly differentiated
    HCC. These factors increase the likelihood of recurrence occurring beyond 2
    years after surgery.
- source_sentence: >
    What are the current standard treatments for glioblastoma multiforme (GBM)
    and why is recurrence almost unavoidable?
  sentences:
  - >-
    The main mechanisms responsible for oncogene-mediated drug resistance in
    ovarian cancer include deregulation of apoptosis, altered phosphorylation
    (intracellular signaling), and metabolic pathways. Activation of the
    PI3K/AKT cell survival pathway, as well as deregulation of growth factor
    receptors mediated by NF-kB and STAT3, plays a pivotal role in drug
    resistance. Additionally, alterations in DNA damage and repair mechanisms,
    impaired apoptotic machinery, and epithelial-to-mesenchymal transition (EMT)
    have been implicated in drug resistance. Wnt signaling, particularly the
    β-catenin-independent pathway via Wnt5a/ROR1/ROR2, is also involved in EMT
    and chemoresistance. Targeting these pathways may offer potential means to
    overcome drug resistance in ovarian cancer.
  - >-
    The overexpression of GALNT2 in oral squamous cell carcinoma (OSCC) cells
    can promote their invasive potential. GALNT2 modifies the O-glycosylation of
    proteins and increases the activity of epidermal growth factor receptor
    (EGFR), which plays a crucial role in the invasive behavior of OSCC cells.
    This suggests that GALNT2 may be involved in the occurrence and development
    of OSCC.
  - >-
    The current standard treatment for GBM includes surgery, radiotherapy, and
    chemotherapy. However, complete surgical resection is not possible, and GBM
    is resistant to chemotherapy, including the commonly used drug temozolomide
    (TMZ). This resistance and the inability to completely remove the tumor
    during surgery contribute to the high recurrence rate of GBM.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
datasets:
- miriad/miriad-4.4M
---

# SentenceTransformer based on google/embeddinggemma-300m

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [google/embeddinggemma-300m](https://huggingface.co/google/embeddinggemma-300m). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [google/embeddinggemma-300m](https://huggingface.co/google/embeddinggemma-300m) <!-- at revision c5cfa06e5e282a820e85d57f7fb053207494f41d -->
- **Maximum Sequence Length:** 2048 tokens
- **Output Dimensionality:** 768 dimensions
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
model = SentenceTransformer("yasserrmd/oncology-gemma-300m-emb")
# Run inference
queries = [
    "What are the current standard treatments for glioblastoma multiforme (GBM) and why is recurrence almost unavoidable?\n",
]
documents = [
    'The current standard treatment for GBM includes surgery, radiotherapy, and chemotherapy. However, complete surgical resection is not possible, and GBM is resistant to chemotherapy, including the commonly used drug temozolomide (TMZ). This resistance and the inability to completely remove the tumor during surgery contribute to the high recurrence rate of GBM.',
    'The overexpression of GALNT2 in oral squamous cell carcinoma (OSCC) cells can promote their invasive potential. GALNT2 modifies the O-glycosylation of proteins and increases the activity of epidermal growth factor receptor (EGFR), which plays a crucial role in the invasive behavior of OSCC cells. This suggests that GALNT2 may be involved in the occurrence and development of OSCC.',
    'The main mechanisms responsible for oncogene-mediated drug resistance in ovarian cancer include deregulation of apoptosis, altered phosphorylation (intracellular signaling), and metabolic pathways. Activation of the PI3K/AKT cell survival pathway, as well as deregulation of growth factor receptors mediated by NF-kB and STAT3, plays a pivotal role in drug resistance. Additionally, alterations in DNA damage and repair mechanisms, impaired apoptotic machinery, and epithelial-to-mesenchymal transition (EMT) have been implicated in drug resistance. Wnt signaling, particularly the β-catenin-independent pathway via Wnt5a/ROR1/ROR2, is also involved in EMT and chemoresistance. Targeting these pathways may offer potential means to overcome drug resistance in ovarian cancer.',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 768] [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[ 0.7010,  0.0508, -0.0444]])
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

* Size: 20,000 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                          |
  |:--------|:-----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                             | string                                                                              |
  | details | <ul><li>min: 10 tokens</li><li>mean: 22.55 tokens</li><li>max: 51 tokens</li></ul> | <ul><li>min: 18 tokens</li><li>mean: 91.28 tokens</li><li>max: 219 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                        | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
  |:------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Is there a way to prevent PTLD in high-risk patients?<br></code>                                            | <code>Currently, there is no convincing data for the prophylaxis of PTLD. However, the case mentioned suggests that early use of rituximab after HSCT (Hematopoietic Stem Cell Transplantation) could be a good way to prevent PTLD in high-risk patients, especially those who are serum EBV (Epstein-Barr Virus) positive. Early recognition of PTLD, early lymph node biopsy, and early diagnosis are key factors in the successful treatment of PTLD.</code>                                                                                                                                                                                                                                                                                                               |
  | <code>How does the 34-gene 'CTC profile' contribute to the prognostic power of breast cancer patients?<br></code> | <code>The 34-gene 'CTC profile' has been found to be predictive of CTC status in breast cancer patients. It demonstrated a classification accuracy of 82% in the training cohort and 67% in an independent microarray dataset. Furthermore, it has been shown to be prognostic in both independent datasets, with a hazard ratio (HR) of 10 in the first validation dataset and a HR of 3.2 in the second validation dataset. Importantly, multivariate analysis confirmed that the CTC profile provided prognostic information independent of other clinical variables in both patient cohorts.</code>                                                                                                                                                                        |
  | <code>How are beauty care services for cancer patients organized and provided?<br></code>                         | <code>Beauty care services for cancer patients are not standardized or evaluated and vary from one establishment to another. In the case of the IGR, consultations on image advice and socio-aesthetics are provided by a socio-aesthetician who has been trained as a personal image advisor. These consultations are offered to women with breast cancer or young adults and adolescents with cancer who are referred by medical units. The consultations take place in a dedicated area with three rooms: an office, make-up parlor, and beauty care salon. Patients are usually seen multiple times during their treatment period. The socio-aesthetician is paid by the hospital and is part of the Onco-hematology Interdisciplinary Supportive Care Directorate.</code> |
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

- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 4
- `num_train_epochs`: 1
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: no
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 4
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
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
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
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch | Step | Training Loss |
|:-----:|:----:|:-------------:|
| 0.1   | 500  | 0.0144        |
| 0.2   | 1000 | 0.0293        |
| 0.3   | 1500 | 0.0128        |
| 0.4   | 2000 | 0.0153        |
| 0.5   | 2500 | 0.0182        |
| 0.6   | 3000 | 0.008         |
| 0.7   | 3500 | 0.0098        |
| 0.8   | 4000 | 0.0044        |
| 0.9   | 4500 | 0.0024        |
| 1.0   | 5000 | 0.0019        |


### Framework Versions
- Python: 3.12.11
- Sentence Transformers: 5.1.0
- Transformers: 4.56.1
- PyTorch: 2.8.0+cu128
- Accelerate: 1.10.1
- Datasets: 4.0.0
- Tokenizers: 0.22.0

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