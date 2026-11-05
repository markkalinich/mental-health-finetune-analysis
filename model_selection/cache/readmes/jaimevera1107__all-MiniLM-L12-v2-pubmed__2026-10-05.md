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
- source_sentence: 'Costae of Tritrichomonas foetus: purification and chemical composition.
    The costa is an intracellular organelle common to all trichomonads. Costae from
    Tritrichomonas foetus have been purified by a method which involves lysis of T.
    foetus with the heat-stable hemolysin produced by Pseudomonas aeruginosa, followed
    by differential centrifugation. Analysis of the purified costae demonstrated that
    the organelle is composed of 95 percent carbohydrate and 5 percent protein. The
    carbohydrate moiety, probably a polysaccharide, consisted of glucose (95 percent),
    mannose (0.4 percent), glucosamine (1.4 percent), ribose (0.6 percent), and an
    unidentified sugar (2.6 percent). The kinetosomal complex was attached to the
    costa after initial lysis of cells but was separated from the costa during purification.'
  sentences:
  - The costae of Tritrichomonas foetus, purified using heat-stable hemolysin from
    Pseudomonas aeruginosa, are composed of 95% carbohydrates, primarily glucose,
    and 5% protein, with the kinetosomal complex initially attached but separated
    during purification.
  - The intranasal live influenza vaccine "Alice" caused significant worsening of
    pulmonary function in all asthmatic individuals.
  - Bupicomide lowers blood pressure and heart rate but has no effect on peripheral
    vascular resistance, renal blood flow, or glomerular filtration rate.
- source_sentence: Lymphocyte activation by the tumor-promoting agent 12-O-tetradecanoylphorbol-13-acetate
    (TPA). TPA, a highly active tumor-promoting agent, is an effective mitogen for
    primate peripheral blood lymphocytes. Optimal stimulation of human lymphocytes
    was obtained 4 days after the addition of TPA at a concentration of 7.5 ng/ml.
    Lymphocyte fractionation experiments demonstrated that both T and B cells incorporated
    3H-thymidine significantly in response to TPA. Lymphocyte blastogenesis was not
    due to the reactivation of latent herpesviruses by the tumor promoter, since similar
    responses to TPA were obtained with virus-genome positive or negative cells. Increased
    levels of DNA synthesis were observed when TPA was added to marmoset, baboon,
    rhesus monkey, or chimpanzee peripheral blood lymphocytes. Canine peripheral blood
    lymphocytes and spleen cells from guinea pigs, rats, and mice were not stimulated
    by TPA. These observations suggest that TPA-induced lymphocyte blastogenesis may
    be useful for studies of lymphocyte activation and of the molecular mechanisms
    of action of tumor-promoting phorbol esters.
  sentences:
  - The study shows that the cerebellum has no effect on smooth pursuit movements,
    as all eye movements remained unchanged after ablations.
  - Bone marrow transplantation is only successful when the donor and recipient have
    identical MLC reactivity, as shown in multiple cases.
  - TPA effectively stimulates lymphocyte activation in primate peripheral blood lymphocytes,
    particularly human T and B cells, but does not activate lymphocytes from dogs
    or several other species.
- source_sentence: What was the outcome for the 68-year-old man diagnosed with desmoplastic
    malignant melanoma after undergoing surgery and lymphadenectomy?
  sentences:
  - A 68-year-old man was diagnosed with desmoplastic malignant melanoma after a biopsy
    revealed abnormal spindle-shaped cells, and despite undergoing surgery and lymphadenectomy,
    he died nine months later from widespread metastatic disease.
  - Inhalation studies of polyurethane foam dust in Sprague-Dawley rats showed no
    significant carcinogenic effects on the respiratory tract, with tumor rates being
    spontaneous and similar across all exposure groups.
  - The administration of K+, Mg2+-aspartate before isoproterenol in dogs improved
    heart muscle ultrastructure and mitigated necrotic changes caused by isoproterenol.
- source_sentence: A seven-week-old infant developed hypernatraemia following the
    oral administration of an electrolyte solution, leading to the recommendation
    against using such solutions for outpatient treatment in children.
  sentences:
  - The infant developed hypokalemia, which required hospitalization for treatment.
  - Increasing the excretory renal mass by connecting isolated kidneys to the circulation
    only affects the arterial blood pressure, not the excreting capacity of the in
    situ kidneys.
  - The study found that longer ischemia durations improved nerve conduction velocities
    and reduced degeneration of myelinated fibers.
- source_sentence: What were the findings of the study on cyclic 3',5'-nucleotide
    phosphodiesterase in bovine thyroid regarding its activity and the factors influencing
    it?
  sentences:
  - The study investigated the properties of cyclic 3',5'-nucleotide phosphodiesterase
    in bovine thyroid, revealing that its activity is stimulated by Mg2+ and requires
    a Ca2+-dependent activating factor, with distinct enzyme forms and kinetic behaviors
    observed.
  - One case resulted in complete recovery without the need for further surgery.
  - '[The kinetics of lithium in the rat serum, brain and liver]. The kinetics of
    lithium in the serum, liver and brain of rats is described. The serum levels resembled
    those of man, whereas considerable quantitative differences were observed when
    comparing specific kinetic parameters. The brain level increased with the increasing
    doses, approaching the corresponding serum level. Concentration differences between
    different brain areas could be observed only after repeated administrations. Striatum,
    cortex and hippocampus showed significantly higher levels than the thalamus. The
    liver content remained low with increasing doses, and was below the brain level.'
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
model = SentenceTransformer("jaimevera1107/all-MiniLM-L12-v2-pubmed")
# Run inference
sentences = [
    "What were the findings of the study on cyclic 3',5'-nucleotide phosphodiesterase in bovine thyroid regarding its activity and the factors influencing it?",
    "The study investigated the properties of cyclic 3',5'-nucleotide phosphodiesterase in bovine thyroid, revealing that its activity is stimulated by Mg2+ and requires a Ca2+-dependent activating factor, with distinct enzyme forms and kinetic behaviors observed.",
    '[The kinetics of lithium in the rat serum, brain and liver]. The kinetics of lithium in the serum, liver and brain of rats is described. The serum levels resembled those of man, whereas considerable quantitative differences were observed when comparing specific kinetic parameters. The brain level increased with the increasing doses, approaching the corresponding serum level. Concentration differences between different brain areas could be observed only after repeated administrations. Striatum, cortex and hippocampus showed significantly higher levels than the thalamus. The liver content remained low with increasing doses, and was below the brain level.',
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
  | details | <ul><li>min: 7 tokens</li><li>mean: 74.75 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 6 tokens</li><li>mean: 59.33 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.68</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              | label            |
  |:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>What were the outcomes for asthmatic patients in a trial of indoramin regarding airflow improvement and migraine frequency reduction?</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | <code>Long-term trial of an alpha adrenoceptor blocking drug (Indoramin) in asthma. A preliminary report. Eight patients suffering from both asthma and migraine underwent a clinical trial for 3 months of indoramin, an alpha adrenoceptor antagonist with antihistamine and antiserotonin activity. Patients were told indoramin was prescribed for migraine prophylaxis. In three asthmatic patients there was a marked increase in airflow meter (AFM) readings which were recorded daily, the remaining five showing no significant change or a decrease in AFM readings. Indoramin did not appear to potentiate the action of the beta sympathomimetic aerosols. It is suggested that a small population of asthmatic patients may derive therapeutic benefit from an alpha adrenoceptor antagonist. Seven of the eight patients experienced a 50% decrease in the frequency of their migraine headaches.</code> | <code>0.5</code> |
  | <code>The ontogeny of L-alpha-hydroxyacid oxidase isozymes in the mouse. Mouse liver hydroxyacid oxidase isozymes are present at low levels at birth and increase in activity until day 13 after which HAOX-B almost disappears and HZOS-A is reduced to approximately one half the maximum level in the adultkidney. HAOX-G appears near day 13 post partum and increases until adult levels are reached, the female having four times the activity of the male. The pregnant female has significantly lower levels of HAOX-A and HAOX-B in the liver and higher activity of HAOX-B in the kidney. Developmental changes occur in the extent of epigenetic modification of mouse liver HAOX-A during the early neonatal period.</code> | <code>In mice, liver hydroxyacid oxidase isozymes show developmental changes, with HAOX-B decreasing after day 13 and HAOX-G increasing, while pregnant females exhibit lower HAOX-A and HAOX-B levels in the liver but higher HAOX-B activity in the kidney.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | <code>1.0</code> |
  | <code>What were the findings regarding renal inflammation and leptospires in a study of striped skunks from Louisiana?</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           | <code>In a study of 100 striped skunks from Louisiana, 50% exhibited renal inflammation, and 10% with severe lesions showed azotemia, while leptospires were cultured from 30% of the skunks.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | <code>0.5</code> |
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
| 0.2367 | 500  | 0.0659        |
| 0.4735 | 1000 | 0.042         |
| 0.7102 | 1500 | 0.0351        |
| 0.9470 | 2000 | 0.0328        |
| 1.1837 | 2500 | 0.0291        |
| 1.4205 | 3000 | 0.0269        |
| 1.6572 | 3500 | 0.0265        |
| 1.8939 | 4000 | 0.026         |
| 2.1307 | 4500 | 0.0245        |
| 2.3674 | 5000 | 0.0231        |
| 2.6042 | 5500 | 0.0219        |
| 2.8409 | 6000 | 0.0229        |
| 3.0777 | 6500 | 0.0227        |
| 3.3144 | 7000 | 0.0206        |
| 3.5511 | 7500 | 0.02          |
| 3.7879 | 8000 | 0.0201        |


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