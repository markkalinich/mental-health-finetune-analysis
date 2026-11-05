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
- source_sentence: |
    How can training influence nurses' awareness of medication errors?
  sentences:
  - >-
    Treatment with obeticholic acid resulted in significant reductions in serum
    alanine aminotransferase (ALT) and aspartate aminotransferase (AST)
    concentrations over the first 36 weeks of treatment, and these reductions
    were sustained for the duration of treatment. However, serum alkaline
    phosphatase concentrations increased with obeticholic acid treatment,
    although γ-glutamyl transpeptidase concentrations (another indicator of
    cholestasis) decreased. These changes in liver enzyme concentrations
    reversed after obeticholic acid was stopped, and at 24 weeks after treatment
    discontinuation, there were no significant differences between the
    obeticholic acid group and the placebo group.
  - >-
    Training can increase nurses' awareness of medication errors by providing
    them with the knowledge and skills necessary to identify and prevent errors.
    Through training, nurses can learn about medication safety protocols, proper
    medication administration techniques, and the importance of error reporting.
    This increased awareness can help nurses recognize potential errors and take
    appropriate actions to prevent harm to patients.
  - >-
    ML171, also known as 2-acetylphenothiazine, has been identified as a
    specific NOX1 oxidase inhibitor at nanomolar concentrations. It shows
    minimal activity on other cellular ROS-producing sources, including xanthine
    oxidase and other NADPH oxidases. ML171 targets the NOX1 catalytic subunit
    without affecting its cytosolic regulators, such as the NOXO1, NOXA1, or
    RAC1 subunits. It effectively blocks NOX1 oxidase-dependent ROS-mediated
    formation of extracellular matrix-degrading invadopodia in colon cancer
    cells.
- source_sentence: |
    What are the potential adverse effects of benzodiazepines?
  sentences:
  - >-
    The peak concentration (C max ) of perindopril refers to the highest
    concentration of the drug in the plasma. The time to reach the C max (T max
    ) indicates how long it takes for the drug to reach its maximum
    concentration. These parameters are important in understanding the
    absorption and distribution of perindopril in the body.
  - >-
    The Multi-drug Therapy (MDT) for leprosy uses a combination of three drugs:
    Rifampicine, Dapsone, and Clofazimine.
  - >-
    Benzodiazepines can induce adverse effects such as oversedation, cognitive
    impairment, motor impairment, and withdrawal. These effects may be
    associated with the elimination half-life of the compounds, where long-term
    use of compounds with a short elimination rate may induce withdrawal
    syndromes, and accumulation-related effects of a long elimination rate may
    include oversedation, cognitive dysfunction, and motor impairment.
- source_sentence: >
    What is the role of resveratrol as an additive to paclitaxel in drug
    coatings?
  sentences:
  - >-
    Traditional opioids are effective against severe pain but have problematic
    side effects and limited efficacy against neuropathic pain. In contrast,
    IBNtxA, a novel opioid analgesic, is a potent analgesic against thermal,
    inflammatory, and neuropathic pain without causing side effects such as
    respiratory depression, physical dependence, or reward behavior.
  - >-
    TXA is contraindicated in patients with severe kidney dysfunction due to the
    risk of accumulation. However, dosages do not need to be modified in
    patients with impaired liver function and elderly patients with no kidney
    dysfunction.
  - >-
    Resveratrol is an additive to paclitaxel in drug coatings that helps
    modulate adherence and release of the drug. It has been found to reduce drug
    loss during passage through the hemostatic valve and sheath and during
    floating in blood. Resveratrol has lower water-solubility compared to other
    additives, which may contribute to its diminished drug loss. Previous
    experiments and published data suggest that resveratrol is a useful coating
    additive in drug delivery systems.
- source_sentence: >-
    What are the most common nonhematologic toxicities associated with OXi4503
    infusion?
  sentences:
  - >-
    The concentration of tetracycline taken up by mineralizing cell systems,
    such as enamel, bone, or dentin, may be influenced by the distinctive
    protein produced by these systems and the cofactors required, as well as the
    availability of calcium or other ions for chelating tetracycline. The amount
    of tetracycline available and the fluorescence observed in tissues may vary
    depending on the particular hard tissue system and the specific mineralizing
    cell system. However, the absence of fluorescence should not be taken as an
    assured absence of tetracycline, as fluorescence alone is not sufficient to
    establish a quantitative assay for tetracycline.
  - >-
    The most common nonhematologic toxicities associated with OXi4503 infusion
    are tumor pain, nausea and/or vomiting, cardiac symptoms (hypertension,
    tachycardia, and QTc prolongation), and neurologic symptoms.
  - >-
    The recommended categories for stocking antidotes in hospitals are divided
    into two. Firstly, 12 antidotes should be available in the hospital
    emergency department for immediate use upon poisoned patient arrival.
    Secondly, nine antidotes should be available in the pharmacy to be
    administered within an hour of when the antidote is deemed necessary. Three
    additional antidotes are recommended to be stocked by the hospital, although
    they are not usually needed within the first hour of treatment.
- source_sentence: >-
    What is the purpose of dabigatran and why was it prescribed to the
    71-year-old female?
  sentences:
  - >-
    Melatonin agonists may have side effects such as nausea, headache, elevated
    liver enzyme levels, rebound insomnia, withdrawal symptoms, and addiction.
    Contraindications include liver failure, renal failure, alcohol addiction,
    and high lipid levels.
  - >-
    G-protein coupled receptors, like OXTR and MOR, can form homo- or
    hetero-dimers, which means they can associate with another molecule of the
    same receptor or with receptors from other families. This physical
    association has been shown to modulate receptor binding and function. For
    example, in MOR-alpha2A-adrenergic receptor dimers, the activation of MOR by
    morphine inhibits the adjacent alpha2A-receptor by blocking its ability to
    activate the G-proteins, even in the presence of noradrenaline.
  - >-
    Dabigatran is prescribed for stroke prevention in patients with atrial
    fibrillation. Atrial fibrillation increases the risk of blood clots forming
    in the heart, which can then travel to the brain and cause a stroke.
    Dabigatran is an anticoagulant that helps prevent the formation of blood
    clots, reducing the risk of stroke in patients with atrial fibrillation.
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
model = SentenceTransformer("yasserrmd/pharma-gemma-300m-emb")
# Run inference
queries = [
    "What is the purpose of dabigatran and why was it prescribed to the 71-year-old female?",
]
documents = [
    'Dabigatran is prescribed for stroke prevention in patients with atrial fibrillation. Atrial fibrillation increases the risk of blood clots forming in the heart, which can then travel to the brain and cause a stroke. Dabigatran is an anticoagulant that helps prevent the formation of blood clots, reducing the risk of stroke in patients with atrial fibrillation.',
    'G-protein coupled receptors, like OXTR and MOR, can form homo- or hetero-dimers, which means they can associate with another molecule of the same receptor or with receptors from other families. This physical association has been shown to modulate receptor binding and function. For example, in MOR-alpha2A-adrenergic receptor dimers, the activation of MOR by morphine inhibits the adjacent alpha2A-receptor by blocking its ability to activate the G-proteins, even in the presence of noradrenaline.',
    'Melatonin agonists may have side effects such as nausea, headache, elevated liver enzyme levels, rebound insomnia, withdrawal symptoms, and addiction. Contraindications include liver failure, renal failure, alcohol addiction, and high lipid levels.',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 768] [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[ 0.4430,  0.0378, -0.0539]])
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
  | details | <ul><li>min: 10 tokens</li><li>mean: 21.09 tokens</li><li>max: 48 tokens</li></ul> | <ul><li>min: 20 tokens</li><li>mean: 94.97 tokens</li><li>max: 223 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                            | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  |:----------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>How does ticlopidine differ from clopidogrel in terms of side effects and precautions?<br></code>               | <code>Unlike clopidogrel, ticlopidine can lead to neutropenia in up to 1% of patients, which limits its widespread use. Regular blood count checks are necessary in the initial weeks of ticlopidine treatment. Additionally, neuraxial regional anesthesia should not be performed until 10 days have elapsed since the last ingestion of ticlopidine.</code>                                                                                                                                                                                                                                                                                                                                         |
  | <code>What are the different types of ligands that can bind to GPCRs?</code>                                          | <code>GPCRs can bind a wide variety of endogenous ligands, including neuropeptides, amino acids, ions, hormones, chemokines, lipid-derived mediators, and ions. Some GPCRs are considered orphan receptors because their exact ligands have not been identified yet.</code>                                                                                                                                                                                                                                                                                                                                                                                                                            |
  | <code>How does etomidate function as an adrenostatic agent and what are its effects on cortisol secretion?<br></code> | <code>Etomidate acts as an adrenostatic agent by blocking the cytochrome P450-dependent adrenal enzymes 11β-hydroxylase and cholesterol-side-chain cleavage enzyme. This inhibition leads to a decrease in cortisol secretion. In dispersed guinea-pig adrenal cells, etomidate has been shown to be the most potent adrenostatic drug available, with a mean concentration of 97 nmol/l required for 50% inhibition of cortisol secretion. This concentration is considerably lower than the plasma concentration needed to induce sedation. After a single induction dose of etomidate, the adrenocortical blockade lasts several hours while the hypnotic action of etomidate rapidly fades.</code> |
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
| 0.1   | 500  | 0.0134        |
| 0.2   | 1000 | 0.009         |
| 0.3   | 1500 | 0.0138        |
| 0.4   | 2000 | 0.0052        |
| 0.5   | 2500 | 0.0154        |
| 0.6   | 3000 | 0.0076        |
| 0.7   | 3500 | 0.0062        |
| 0.8   | 4000 | 0.0021        |
| 0.9   | 4500 | 0.0028        |
| 1.0   | 5000 | 0.0015        |


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