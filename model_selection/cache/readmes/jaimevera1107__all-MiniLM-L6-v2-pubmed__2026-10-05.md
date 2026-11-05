---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:67560
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: What are the key findings from the morphological study of Giant
    Cell Tumors of Bone regarding the characteristics of mononuclear cells, vascular
    networks, and the challenges in grading and recurrence assessment?
  sentences:
  - Giant Cell Tumors of Bone show mononuclear cells with characteristics of adipocytes,
    a lack of vascular networks, and grading is simplified by clear architectural
    patterns that predict recurrence accurately.
  - In a study of 15 patients with complicated urinary tract infections treated with
    intramuscular gentamicin, the drug demonstrated excellent clinical efficacy in
    80% of cases, with an overall effective rate of 93.3%, while no significant adverse
    effects were noted on kidney function.
  - Patients with primary open-angle glaucoma show no difference in sensitivity to
    corticosteroids compared to control subjects.
- source_sentence: Pretreatment with 6-hydroxydopamine resulted in a delayed onset
    of alcohol withdrawal seizures, with 10% of the rats experiencing seizures.
  sentences:
  - All rabbits showed severe renal damage by week 10, leading to their early termination.
  - Type-B hepatitis is a common cause of viral hepatitis in Nigeria, with HBsAg detected
    in 46.4% of 97 patients at the Lagos University Teaching Hospital.
  - Pretreatment with 6-hydroxydopamine had no effect on alcohol withdrawal seizures,
    with 50% of the rats experiencing seizures as usual.
- source_sentence: What is fenclorac and how does it compare to other nonsteroidal
    anti-inflammatory drugs in terms of efficacy and tolerance in animal studies?
  sentences:
  - The antiphlogistic, antinociceptive and antipyretic properties of fenclorac. Fenclorac
    (a,m-dichloro-p-cyclohexlphenylacetic acid, diethylammonium salt) is a potent
    nonsteroidal anti-inflammatory agent with significant analgesic and antipyretic
    activity. Fenclorac had an ED50 of 7.9 mg/kg in the carrageenan paw edema assay
    and had a duration of action of 18-22 hours. Comparative tests in the carrageenan
    paw edema assay in the rat indicated that the potency of fenclorac was 13 times
    that of aspirin, 3.4 times phenylbutazone, 3 times ibuprofen and 0.3 times indomethacin.
    Fenclorac was less potent than indomethacin, but more potent than phenylbutazone
    or aspirin in treatment of developing or established adjuvant arthritis. The anti-inflammatory
    effectiveness of fenclorac did not depend upon the integrity of the adrenopituitary
    axis and was not affected by the route of administration or sex of the test animal.
    Fenclorac was 77 times more potent than aspirin and more than twice as potent
    as indomethacin in reducing fever in rats rendered hyperthermic with brewer's
    yeast. Fenclorac did not affect normal body temperatures. Fenclorac did not interfere
    with cellular immune mechanisms as measured by its lack of effectiveness in experimental
    allergic encephalomyelitis. Antinociceptive testing indicated that fenclorac had
    peripheral but not central analgesic activity. Fenclorac had an acute oral LD50
    in rats and mice of 285 and 430 mg/kg, respectively. The acute gastric lesion
    UD50 for fenclorac was 7 mg/kg in the fasted rat. Studies using 51Cr-tagged erythrocytes
    indicated that fenclorac did not produce significant fecal blood loss in the rat
    at twice the therapeutic ED50 dose for up to 12 days after dosing. Extensive and
    prolonged fecal blood loss was observed with a corresponding dose of indomethacin
    for up to nine days after administration. Comparison of the anti-inflammatory
    pharmacology, Therapeutic Ratio and the data obtained from the 51Cr-fecal blood
    loss studies indicated that fenclorac was well tolerated after acute or subacute
    administration to the rat.
  - A clinical survey of 493 styrene production workers revealed significant differences
    in health symptoms between high and low exposure groups, while other health tests
    showed no distinct patterns.
  - Intravenous glucose can lead to a significant drop in blood pressure in insulin-deprived
    diabetics.
- source_sentence: What is the effect of hypertonic salt extracts (3 M KCl) from x-irradiation-induced
    rat small bowel adenocarcinomas on the cytotoxicity of sensitized lymphoid cells
    against allogeneic cultured tumor cells?
  sentences:
  - Hypertonic salt extracts (3 M KCl) from x-irradiation-induced rat small bowel
    adenocarcinomas inhibit the cytotoxicity of sensitized lymphoid cells against
    allogeneic cultured tumor cells by acting at both the effector and target cell
    levels.
  - An immunological method allows for the determination of the specific activity
    of pure enzymes and quantifies cross-reactivity between plasmid-coded beta-galactosidases
    and Escherichia coli beta-galactosidase.
  - Intonation was found to have no effect on short-term memory, as participants retained
    both intonation and words equally well.
- source_sentence: The ionic currents in the tunicate egg Halocynthia roretzi were
    found to be solely dependent on potassium concentration, with no influence from
    sodium.
  sentences:
  - The findings indicated that the ionic currents were completely abolished by the
    replacement of sodium with potassium ions, showing no other components.
  - In rats, the injection of (1-bromoethyl)benzene produces only N-acetyl-S-1-phenylethylcysteine
    in urine, while (2-bromoethyl)benzene results in N-acetyl-S-2-phenylethylcysteine
    and N-acetyl-S-(2-phenyl-2-hydroxyethyl)cysteine, indicating that styrene or styrene
    oxide does not form as intermediates from these alkylhalides.
  - The cattle tick Hyalomma anatolicum exhibits varying radiation tolerance levels,
    with unfed adults tolerating up to 1000 R for engorgement and reproduction, while
    engorged females can tolerate 10,000 R for oviposition, but higher doses inhibit
    egg-laying.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on sentence-transformers/all-MiniLM-L6-v2

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [sentence-transformers/all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) <!-- at revision c9745ed1d9f207416be6d2e6f8de32d1f16199bf -->
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
model = SentenceTransformer("jaimevera1107/all-MiniLM-L6-v2-pubmed")
# Run inference
sentences = [
    'The ionic currents in the tunicate egg Halocynthia roretzi were found to be solely dependent on potassium concentration, with no influence from sodium.',
    'The findings indicated that the ionic currents were completely abolished by the replacement of sodium with potassium ions, showing no other components.',
    'The cattle tick Hyalomma anatolicum exhibits varying radiation tolerance levels, with unfed adults tolerating up to 1000 R for engorgement and reproduction, while engorged females can tolerate 10,000 R for oviposition, but higher doses inhibit egg-laying.',
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

* Size: 67,560 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                         | sentence_1                                                                         | label                                                          |
  |:--------|:-----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                             | string                                                                             | float                                                          |
  | details | <ul><li>min: 4 tokens</li><li>mean: 73.08 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 61.28 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.69</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | sentence_1                                                                                                                                                                                                                                                                            | label            |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>Nonstimulated lymphocytes infected with measles virus do not express detectable virus antigens, but upon stimulation with phytohemagglutinin, the virus can be reactivated, leading to increased virus production and cell death.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | <code>Nonstimulated lymphocytes infected with measles virus produce detectable virus antigens immediately upon stimulation with phytohemagglutinin.</code>                                                                                                                            | <code>0.5</code> |
  | <code>In vitro studies of axillary lymph node cells in patients with breast cancer. A total of 170 axillary lymph nodes were obtained from fresh mastectomy specimens from 81 women with breast cancer. Lymph node cells were tested in vitro for T and B cells by the rosette technique and immunofluorescence microscopy and for functional capacity by response to the mitogens phytohemagglutinin (PHA) and concanavalin A. T cells showed a wide range of relative values: 32-80 percent, with a mean of 63.5 percent. B cells defined by the presence of surface immunoglobulins ranged from 14 to 61 percent (mean, 35.8 percent); those defined by the presence of C3 receptors, from 8 to 54 percent (mean, 24.9 percent); and those defined by the presence of IgG-specific (Fc) receptors, from 10 to 45 percent (mean, 27.5 percent). Cells with the C3 and Fc receptors constituted approximately two-thirds of the cells not binding spontaneously to sheep red blood cells (non-SRBC-R), whereas virtually all non-SRBC-R stain...</code> | <code>In a study of axillary lymph nodes from 81 breast cancer patients, T and B cell proportions varied significantly by age, metastatic status, and lymph node morphology, with older patients and nodes with metastasis showing higher B cell and lower T cell percentages.</code> | <code>1.0</code> |
  | <code>Pharmacologic treatment of disorders of bladder and urethra: a review. The use of pharmacologic agents in treating disorders of the bladder and proximal urethra has expanded because of new knowledge gained in the past few years. A better understanding of the properties of these organs as they relate to drugs has contributed to this expansion. The authors present their experience with a number of drugs in treating disorders of the detrusor muscle and proximal urethra, and they briefly review the literature.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | <code>Recent advancements in understanding bladder and urethra properties have led to an expanded use of pharmacologic agents for treating related disorders.</code>                                                                                                                  | <code>1.0</code> |
* Loss: [<code>CosineSimilarityLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosinesimilarityloss) with these parameters:
  ```json
  {
      "loss_fct": "torch.nn.modules.loss.MSELoss"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `num_train_epochs`: 4
- `fp16`: True
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
- `num_train_epochs`: 4
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
- `fp16`: True
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
- `hub_private_repo`: None
- `hub_always_push`: False
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
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin

</details>

### Training Logs
| Epoch  | Step | Training Loss |
|:------:|:----:|:-------------:|
| 0.2367 | 500  | 0.065         |
| 0.4735 | 1000 | 0.041         |
| 0.7102 | 1500 | 0.0356        |
| 0.9470 | 2000 | 0.0319        |
| 1.1837 | 2500 | 0.0287        |
| 1.4205 | 3000 | 0.0272        |
| 1.6572 | 3500 | 0.0262        |
| 1.8939 | 4000 | 0.0263        |
| 2.1307 | 4500 | 0.0252        |
| 2.3674 | 5000 | 0.0228        |
| 2.6042 | 5500 | 0.0225        |
| 2.8409 | 6000 | 0.0221        |
| 3.0777 | 6500 | 0.0219        |
| 3.3144 | 7000 | 0.02          |
| 3.5511 | 7500 | 0.0198        |
| 3.7879 | 8000 | 0.0203        |


### Framework Versions
- Python: 3.11.9
- Sentence Transformers: 4.1.0
- Transformers: 4.52.3
- PyTorch: 2.7.0+cu118
- Accelerate: 1.7.0
- Datasets: 3.6.0
- Tokenizers: 0.21.1

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