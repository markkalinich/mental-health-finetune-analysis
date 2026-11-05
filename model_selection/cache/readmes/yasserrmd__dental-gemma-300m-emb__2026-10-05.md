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
    What are some potential complications associated with peri-implantitis?
  sentences:
  - >-
    Effective pain management in dentistry involves understanding whether a
    procedure will create an inflammatory response that activates pain mediators
    in tissue. Procedures on hard tooth structure generally cause little or no
    inflammatory response, while trauma to soft tissues can lead to pain. Using
    anti-inflammatory agents to control the inflammatory process can help
    alleviate pain in dental patients.
  - >-
    Peri-implantitis can lead to inflammation of peri-implant tissues,
    hyperplasia and ulceration of pocket epithelium, and the presence of a mixed
    population of inflammatory cells. In more aggressive cases, it can also
    result in pyogenic granuloma, giant-cell granuloma, or Actinomyces-related
    inflammation. Additionally, there have been reports of
    peri-implantitis-associated oral malignancies. These complications often do
    not respond to conventional treatment.
  - >-
    The most commonly reported symptoms after amalgam removal include tendency
    to rapid exhaustion, tiredness, concentration disturbance, and pain in
    joints and limbs. These symptoms are consistent with other studies conducted
    in similar populations.
- source_sentence: |
    What are some factors that can contribute to gingival recession?
  sentences:
  - >-
    With the rising popularity of dental implants and the growing number of
    individuals undergoing dental restorations using implants, there is a
    heightened probability of patients with dental implants undergoing
    irradiation around these implants. This trend raises concerns about the
    long-term adverse effects that dental implants located within radiation
    fields may pose. Further studies are needed to investigate the potential
    risks and complications associated with dental implants in patients
    receiving radiotherapy, particularly in the context of ORN and
    peri-implantitis development.
  - >-
    Acid etching is used in adhesive systems in dentistry to remove the smear
    layer and demineralize the dentin surface. This process helps to create a
    rough surface that allows for better adhesion of the adhesive to the tooth
    structure. Acid etching also helps to expose collagen fibers and
    hydroxyapatite crystals, which can be encapsulated by the adhesive, leading
    to a stronger bond.
  - >-
    Factors that can contribute to gingival recession include over-zealous tooth
    brushing, genetically determined thickness of the alveolar bone and soft
    tissue (biotype), bone dehiscences, frenal pull, plaque and calculus, and
    age-related factors.
- source_sentence: >
    How does the gel extract of mauli banana stem (EMBS) potentially aid in the
    healing of oral mucosal wounds?
  sentences:
  - >-
    Missing extra root canals is a major reason for endodontic failure. When
    canals are not located and filled, it can lead to incomplete debridement and
    failure to remove bacteria and their byproducts. This can result in
    persistent infection and reinfection of the root canal system, leading to
    treatment failure.
  - >-
    Depending on the vitality of the affected pulp, there are various treatment
    modalities for young permanent teeth. In cases where the radicular pulp
    tissue needs to be preserved for continued root development and apical
    closure, apexogenesis is recommended. Other treatment options may be
    considered based on the specific diagnosis and condition of the tooth.
  - >-
    Previous research has shown that the gel extract of mauli banana stem (EMBS)
    can accelerate and increase the thickness of the epithelium in buccal
    mucosal wound healing in mice. EMBS contains bioactive materials, including
    tannin, saponin, alkaloids, ascorbic acid, flavonoids, and lycopene. The
    condensed tannins in EMBS can induce tyrosine phosphorylation of the insulin
    receptor, activating the phosphatidylinositol 3-kinase pathway (PI3K)
    involved in cell proliferation. Terpenoid saponins in EMBS can increase the
    activity and number of macrophages by interacting with G protein receptors
    on macrophages and activating NFkβ.
- source_sentence: |
    What are the most commonly used obturation techniques in endodontics?
  sentences:
  - >-
    The treatment options for dentigerous cysts depend on the size of the lesion
    and the likelihood of tooth eruption. Enucleation is reserved for smaller
    lesions or cases where it is not possible to save the involved tooth. The
    M/D technique, which involves minimal lesion to anatomic structures, is
    preferred for extensive lesions and when there is a possibility of
    preserving the tooth involved. The M/D technique minimizes the risk of
    complications and favors the eruption of displaced teeth.
  - >-
    The most commonly used obturation technique in endodontics is lateral
    condensation, which is used by 66.2% of general dental practitioners. This
    technique is relatively simple and versatile, and does not require expensive
    equipment. However, it should be noted that single-cone/point techniques,
    which involve using a single cone to fill the root canal space, are not
    recommended as they cannot reliably fill all dimensions of the root canal.
    Despite this, 25.9% of dentists in the survey use a single cone technique.
    Additionally, 18.1% of respondents use only paste to obturate the root canal
    system, which can be problematic with paraformaldehyde-based sealers as they
    can cause damage to the surrounding tissues when extruded.
  - >-
    Micro-CT is a new generation technology that provides accurate and
    high-resolution 3D images of dental structures. It enables dentists to
    evaluate root canal count, canal volume, and the presence of gaps and spaces
    in obturation materials. By using micro-CT, dentists can have a clear
    understanding of the pulp canal system before starting endodontic treatment.
    This knowledge allows for effective canal cleaning and ensures a proper 3D
    obturation, leading to improved sealing of the accessible spaces and higher
    success rates in root canal treatment.
- source_sentence: |
    What is tooth transposition and how does it occur?
  sentences:
  - >-
    The main forms of treatment for oral and tooth health in government
    hospitals and health centers in Turkey are extraction, removable
    prosthodontics, and routine amalgam and composite restorations. Root canal
    treatment is not generally preferred due to a lack of endodontic equipment
    and time.
  - >-
    Air polishing offers many advantages to clinicians and their patients. It is
    less time-consuming and effective in heavily stained surfaces, such as
    smoking and chlorhexidine stain. This minimizes operator and patient
    fatigue. Additionally, air polishing treatments can provide superior
    treatment outcomes in terms of speed and efficacy.
  - >-
    Tooth transposition is a condition where two adjacent teeth switch positions
    in the dental arch. It can be classified as complete transposition when both
    the crowns and roots of the involved teeth exchange places, or incomplete
    transposition when only the crowns are transposed. Tooth transposition is
    more commonly found unilaterally than bilaterally, with a higher prevalence
    in the maxillary (upper) arch. There is no sex preference for tooth
    transposition. The condition is not significantly related to other dental
    anomalies such as missing teeth, peg-shaped or hypoplastic teeth, or
    impacted teeth. The etiology of tooth transposition is believed to be
    genetically involved, and it most often occurs at the maxillary canine.
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
model = SentenceTransformer("yasserrmd/dental-gemma-300m-emb")
# Run inference
queries = [
    "What is tooth transposition and how does it occur?\n",
]
documents = [
    'Tooth transposition is a condition where two adjacent teeth switch positions in the dental arch. It can be classified as complete transposition when both the crowns and roots of the involved teeth exchange places, or incomplete transposition when only the crowns are transposed. Tooth transposition is more commonly found unilaterally than bilaterally, with a higher prevalence in the maxillary (upper) arch. There is no sex preference for tooth transposition. The condition is not significantly related to other dental anomalies such as missing teeth, peg-shaped or hypoplastic teeth, or impacted teeth. The etiology of tooth transposition is believed to be genetically involved, and it most often occurs at the maxillary canine.',
    'Air polishing offers many advantages to clinicians and their patients. It is less time-consuming and effective in heavily stained surfaces, such as smoking and chlorhexidine stain. This minimizes operator and patient fatigue. Additionally, air polishing treatments can provide superior treatment outcomes in terms of speed and efficacy.',
    'The main forms of treatment for oral and tooth health in government hospitals and health centers in Turkey are extraction, removable prosthodontics, and routine amalgam and composite restorations. Root canal treatment is not generally preferred due to a lack of endodontic equipment and time.',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 768] [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[0.7669, 0.0321, 0.2308]])
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
  |         | sentence_0                                                                        | sentence_1                                                                          |
  |:--------|:----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                              |
  | details | <ul><li>min: 9 tokens</li><li>mean: 19.66 tokens</li><li>max: 49 tokens</li></ul> | <ul><li>min: 22 tokens</li><li>mean: 87.28 tokens</li><li>max: 221 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                             | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
  |:---------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>How do prosthodontists in Australia determine the need for placing a post in a tooth restoration?</code>                         | <code>Prosthodontists in Australia consider both the quantity of tooth structure and the type of planned restoration when deciding whether to place a post. The location of the tooth in the arch seems to have less influence on their decision. Molar teeth and mandibular anterior teeth are less likely to receive posts.</code>                                                                                                                                                                                                                                                  |
  | <code>What are some patient-centered outcome measures used to assess the impact of oral health problems on quality of life?<br></code> | <code>There are several patient-centered outcome measures called 'oral health related quality of life measures' (OHQoL) that have been developed to assess the extent to which oral health problems affect a person's quality of life. Two measures that have received particular attention are the Oral Health Impact Profile (OHIP-14) and the UK Oral Health Related Quality of Life (OHQoL-UK) questionnaires. The OHIP-14 measures the adverse impacts of oral conditions on daily life, while the OHQoL-UK incorporates both negative and positive influences on health.</code> |
  | <code>How does finite element analysis (FEA) contribute to the understanding and improvement of dental implant procedures?</code>      | <code>Finite element analysis (FEA) is a computational method that can be used to simulate the distribution of stress and strain in the mandibular bone and osseointegrated implants. By considering various variables such as material characteristics, types of loads, and individual bio-subjectivity, FEA studies provide valuable insights into stress distribution and geometry evaluation. This information helps in making informed decisions about implant positioning, inclination, and type to ensure the long-term stability and success of dental implants.</code>       |
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
| 0.1   | 500  | 0.0147        |
| 0.2   | 1000 | 0.0142        |
| 0.3   | 1500 | 0.0154        |
| 0.4   | 2000 | 0.0085        |
| 0.5   | 2500 | 0.0052        |
| 0.6   | 3000 | 0.0071        |
| 0.7   | 3500 | 0.0025        |
| 0.8   | 4000 | 0.0028        |
| 0.9   | 4500 | 0.0056        |
| 1.0   | 5000 | 0.0045        |


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