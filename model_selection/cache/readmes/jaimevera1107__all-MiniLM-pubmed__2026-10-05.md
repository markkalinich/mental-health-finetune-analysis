---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:16890
- loss:CosineSimilarityLoss
base_model: sentence-transformers/all-MiniLM-L6-v2
widget:
- source_sentence: What effect does Concanavalin-A have on the generation of cytotoxic
    lymphocytes in alloimmunized mice when administered before or during immunization?
  sentences:
  - Fluorescence studies revealed that 70% of pre-mRNA in nuclear ribonucleoprotein
    particles is accessible for dye binding, with approximately 50% AU-nucleotide
    content in the double-stranded regions.
  - Concanavalin-A enhances the generation of cytotoxic lymphocytes in alloimmunized
    mice when administered before or during immunization.
  - Between 1966 and 1973, of 600 mediastinoscopies for pulmonary carcinoma, 43% were
    positive, leading to varied surgical outcomes, with a 63% survival rate after
    2 to 3.5 years for the first 100 operated patients.
- source_sentence: Injecting small doses of tetanus toxin into the hippocampus of
    rats induces an epileptiform syndrome characterized by intermittent seizures and
    hyperkinetic behavior, which eventually resolves, while control animals receiving
    neutralized toxin do not exhibit seizures or abnormal behavior.
  sentences:
  - The study found that all 56 children responded positively to both arginine and
    L-dopa, confirming their growth hormone deficiency.
  - Injecting small doses of tetanus toxin into the hippocampus causes immediate paralysis
    and death in rats, while control animals show no effects.
  - A low noise, programmable gain electrocardiographic amplifier has been developed
    for ECG data acquisition, featuring differential inputs, digitally adjustable
    gains and output offsets, selectable low frequency response, and an on-board output
    monitor multiplexer.
- source_sentence: What were the findings of the study regarding the in vivo distribution
    and formation conditions of the 99mTc-Sn-pyrophosphate complexes in rats?
  sentences:
  - Reactivity of isolated bovine facial vessels to electric stimulation and to drugs.
    The effects of electric stimulation on isometric force generation of isolated
    helical strips of bovine facial arteries (BFA) and veins (BFV) were investigated.
    Whereas BFA always contracted, electrically stimulated BFV showed a biphasic response,
    i.e. a small, transient contraction followed by an intense relaxation. The findings
    presented suggest a neurogenic response for the vasodilator component of BFV response
    to electric stimulation. Exogenous catecholamines and serotonin dilated the veins;
    the effects were antagonized by propranolol and dihydroergotamine, respectively.
    Dopamine-induced relaxations were only partially inhibited by propranolol; the
    residual relaxations were antagonized by chlorpormazine and haloperidol. Relaxations
    of the veins after electric stimulation or after administration of noradrenaline
    were accompanied by an increase of the cAMP content. In the BFA catecholamines,
    serotonin and histamine increased the tension, whereas isoprenaline was ineffective.
    Acetylcholine contracted the veins and relaxed the arteries; both effects were
    antagonized by atropine.
  - The patient developed a perforation in the tympanic membrane, which was repaired
    using a tympanoplasty technique.
  - The study evaluated the in vivo distribution of two 99mTc-Sn-pyrophosphate complexes
    in rats, revealing that the bone-seeking 2:2 Sn:PyP complex depends on pyrophosphate
    and hydrogen ion concentration, while the kidney-concentrating 2:1 Sn:PyP complex
    is independent of hydrogen ions and forms at low pyrophosphate levels.
- source_sentence: What was the estimated molecular weight of protoheme ferro-lyase
    using the radiation inactivation method, and how did irradiation conditions affect
    inactivation?
  sentences:
  - The molecular weight of protoheme ferro-lyase was estimated to be between 250,000
    and 320,000 using the radiation inactivation method, with less inactivation observed
    under irradiation in vacuo compared to air.
  - The mitotic index in the cortical compartment of the bursa of Fabricius is significantly
    higher in chicks immunized with sheep red blood cells compared to non-immunized
    chicks, peaking six days post-injection alongside the highest serum antibody titer.
  - The two-mutational-event theory of medullary thyroid cancer is supported by findings
    that C-cell hyperplasia occurs in hereditary cases but not in sporadic cases,
    suggesting it represents the first genetic mutation necessary for cancer development.
- source_sentence: What are the age-dependent survival characteristics, energy reserves,
    and activity levels of hexacanths from Hymenolepis diminuta?
  sentences:
  - An experimental study of the survival characteristics, activity and energy reserves
    of the hexacanths of Hymenolepis diminuta. Similar survival characteristics were
    demonstrated for hexacanths of Hymenolepis diminuta incubated in Tyrode's solution
    with or without a glucose supplement (0-50 mg/ml). The survival rate of hexacanths
    in all media tested was shown to be age-dependent and led to a maximum life-span
    of approximately 11 h. The amount of energy reserves, as measured by microdensitometric
    determination of PAS+ material, declined rapidly in time to a plateau at approximately
    8 h. Residual PAS+ matter present beyond that period was interpreted as structural
    and thus non-utilizable material. The rate of activity as measured by hook movements
    declined more rapidly, and continuous hook cycles were rarely observed after 2
    h and ceased after 4 h. A close correlation was demonstrated between the decline
    in PAS+ material and the total number of hook cycles completed per unit of time.
    The quantitative results on survival, energy reserves and activity are discussed
    in relation to the penetration of hexacanths into the haemocoele of the intermediate
    host.
  - A review of 1500 consecutive coronary angiograms at Harefield Hospital since 1970
    indicates a significant reduction in mortality, with only 2 deaths in the last
    1000 cases attributed to improved operator training and attention to detail, highlighting
    the necessity of experienced oversight for new units.
  - Radionuclide blood flow studies indicated successful Gelfoam embolization of intracranial
    meningiomas in two patients, as evidenced by the absence of tumor visualization
    during the arterial phase post-procedure.
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
model = SentenceTransformer("jaimevera1107/all-MiniLM-pubmed")
# Run inference
sentences = [
    'What are the age-dependent survival characteristics, energy reserves, and activity levels of hexacanths from Hymenolepis diminuta?',
    "An experimental study of the survival characteristics, activity and energy reserves of the hexacanths of Hymenolepis diminuta. Similar survival characteristics were demonstrated for hexacanths of Hymenolepis diminuta incubated in Tyrode's solution with or without a glucose supplement (0-50 mg/ml). The survival rate of hexacanths in all media tested was shown to be age-dependent and led to a maximum life-span of approximately 11 h. The amount of energy reserves, as measured by microdensitometric determination of PAS+ material, declined rapidly in time to a plateau at approximately 8 h. Residual PAS+ matter present beyond that period was interpreted as structural and thus non-utilizable material. The rate of activity as measured by hook movements declined more rapidly, and continuous hook cycles were rarely observed after 2 h and ceased after 4 h. A close correlation was demonstrated between the decline in PAS+ material and the total number of hook cycles completed per unit of time. The quantitative results on survival, energy reserves and activity are discussed in relation to the penetration of hexacanths into the haemocoele of the intermediate host.",
    'A review of 1500 consecutive coronary angiograms at Harefield Hospital since 1970 indicates a significant reduction in mortality, with only 2 deaths in the last 1000 cases attributed to improved operator training and attention to detail, highlighting the necessity of experienced oversight for new units.',
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

* Size: 16,890 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                          | sentence_1                                                                        | label                                                          |
  |:--------|:------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                              | string                                                                            | float                                                          |
  | details | <ul><li>min: 10 tokens</li><li>mean: 72.87 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 4 tokens</li><li>mean: 60.5 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.62</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                     | sentence_1                                                                                                                                                                                                                      | label             |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------|
  | <code>Injecting small doses of tetanus toxin into the hippocampus of rats induces an epileptiform syndrome characterized by intermittent seizures and hyperkinetic behavior, which eventually resolves, while control animals receiving neutralized toxin do not exhibit seizures or abnormal behavior.</code> | <code>Injecting small doses of tetanus toxin into the hippocampus causes immediate paralysis and death in rats, while control animals show no effects.</code>                                                                   | <code>0.2</code>  |
  | <code>Phosphorylation of rat kidney pyruvate kinase type L by cyclic AMP-dependent protein kinase regulates its activity, suggesting hormonal control of gluconeogenesis in the renal cortex.</code>                                                                                                           | <code>Phosphorylation of rat kidney pyruvate kinase type L by cyclic AMP-dependent protein kinase has no effect on its activity or gluconeogenesis in the renal cortex.</code>                                                  | <code>0.2</code>  |
  | <code>What challenges do facially disfigured individuals face in their rehabilitation and social integration, and what measures are needed to address these issues?</code>                                                                                                                                     | <code>Public and professional attitudes towards facially disfigured individuals often hinder their rehabilitation and social integration, necessitating improved education and care strategies for healthcare providers.</code> | <code>0.75</code> |
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
| 0.9470 | 500  | 0.0306        |
| 1.8939 | 1000 | 0.0197        |
| 2.8409 | 1500 | 0.0165        |
| 3.7879 | 2000 | 0.0149        |


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