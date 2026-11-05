---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:39780704
- loss:MultipleNegativesRankingLoss
widget:
- source_sentence: medication metformin
  sentences:
  - There are two ways to age whiskey at home. The most traditional method of DIY
    whiskey aging is to purchase or build a charred white oak barrel. To prep a barrel
    to be used for aging, make sure to first fill it with warm water and leave it
    sit until the wood swells enough to prevent leaking between the staves.
  - 'A: Metformin (Glucophage) is a medication used for the treatment of diabetes
    or high blood sugar. It works by decreasing the production of glucose by the liver.
    The main side effects of metformin (Glucophage) are gastrointestinal in nature
    and include diarrhea, nausea, vomiting and flatulence.'
  - Immigration Station. In 1905, construction of the Immigration Station began in
    the area then known as North Garrison. Surrounded by public controversy from its
    inception, the station was finally put into partial operation in 1910. It was
    designed to process Chinese immigrants whose entry was restricted by the Chinese
    Exclusion Law of 1882.
- source_sentence: is moonshine whiskey
  sentences:
  - "After 1700, the numbers of slaves being transported increased greatly â\x80\x93\
    \ perhaps 6 million Africans were taken as slaves to the Americas. A British slave\
    \ ship set off from Liverpool or Bristol, carrying trade goods, and sailed to\
    \ Africa. Some slaves were captured directly by the British traders. They ambushed\
    \ and captured local people in Africa. Most slave ships got their slaves from\
    \ British 'factors', who lived full-time in Africa and bought slaves from local\
    \ tribal chiefs. The chiefs would raid a rival village and sell their captured\
    \ enemies as slaves. In 1700, a slave cost about Â£3-worth of traded goods eg\
    \ cloth, guns, gunpowder and brandy. The slaves were marched to the coast in chained\
    \ lines called coffles, where they were held in prisons called 'factories'."
  - An income budget is a specific type of budget that only shows how and where money
    is earned. This type of budget can be used for professional purposes in a business
    or can be used for personal reasons, if a single person has various streams of
    income.he income budget shows in detail how much is coming into the business and
    where it is coming from, while the master budget shows the entire operation of
    the business. In other words, the master budget shows how the money from the income
    budget is being spent within the business.
  - Moonshine is essentially an un-aged whisky, traditionally clear with a hint of
    corn. It is perfect for sipping or using as a substitute in cocktails. There are
    different varieties of moonshine depending on the distillation process and number
    of times the spirit runs through the still..
- source_sentence: does iron supplement cause black stools
  sentences:
  - 'False MelanaA black stool caused by food, supplements, medication, or minerals
    is known as false melena.. Iron supplements, taken alone or as part of a multivitamin
    for iron-deficient anemia, may cause stools to be black or even greenish in color.
    Foods that are dark blue or black in color may also cause black stools. Substances
    that can cause false melena are:'
  - Turin is a city found in Piedmont, Italy. It is located 45.07 latitude and 7.69
    longitude and it is situated at elevation 245 meters above sea level. Turin has
    a population of 870,456 making it the biggest city in Piedmont. It operates on
    the CEST time zone.
  - Just wanted to add to that M was breech until about 35 weeks. I didn't do acu
    or moxi-just a lot of down dogs and avoided the squatting position (yoga) for
    any length of time (so as not to set the baby in breech position). I also wouldn't
    necessarily worry about breech position until closer to 35-36 weeks..heir view
    was that there was plenty of time for the baby to turn on its own up until 39
    weeks. My older son turned from full breech to head down at around 37 weeks, and
    this was directly after doing a lot of yoga positions designed to make it easier
    for the baby to move.
- source_sentence: width of doorways regulation
  sentences:
  - The Environmental Economics and Management major prepares students for public
    and private positions in natural and environmental resource analysis and management.
    Students in this major receive training in resource economics, environmental economics,
    economic theory and quantitative decisions making techniques.
  - ADA 404.2.3 Clear Width. Door openings shall provide a clear width of 32 inches
    (815 mm) minimum Clear openings of doorways with swinging doors shall be. measured
    between the face of the door and the stop, with the door open. 90 degrees Openings
    more than 24 inches (610 mm) deep shall provide.
  - Timeframe. The United States Postal Services reports that as of January 2011,
    it takes an average of one to three days for First-Class Mail to arrive at its
    destination.Priority Mail takes an average of one to two days to arrive, according
    to the USPS. USPS only includes the time a package stays in transit in their estimations.imeframe.
    The United States Postal Services reports that as of January 2011, it takes an
    average of one to three days for First-Class Mail to arrive at its destination.
- source_sentence: does the columbus zoo sell beer
  sentences:
  - Eviction law allows landlords to still ask you to move out, but you must be afforded
    some extra protections. First, for eviction notices without cause, the landlord
    must give you a longer period of notice to vacate, generally 30 or 60 days. This
    lengthened time period is designed to allow you to find another place to live.
  - Systemic Lupus Erythematosus (Lupus) can cause seizures. Researchers report that
    seizures occur from lupus at the onset of their disease in less than 5% of patients.
    Seizures occur from lupus during their lifetime in approximately 10% of patients.
    Seizures are one of the classical 11 criteria that are used to diagnose Lupus,
    see our Focus on Systemic Lupus Erythematosus. Thank you for your question.
  - No glass and/or alcohol are permitted at the Columbus Zoo. This means that they
    do not sell alcoholic beverages.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer

This is a [sentence-transformers](https://www.SBERT.net) model trained on the parquet dataset. It maps sentences & paragraphs to a 512-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 512 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - parquet
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
  (1): Pooling({'word_embedding_dimension': 512, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("pankajrajdeo/Bioformer-8L-UMLS-Pubmed_PMC-Forward_TCE-Epoch-2-MSMARCO-Epoch-4")
# Run inference
sentences = [
    'does the columbus zoo sell beer',
    'No glass and/or alcohol are permitted at the Columbus Zoo. This means that they do not sell alcoholic beverages.',
    'Eviction law allows landlords to still ask you to move out, but you must be afforded some extra protections. First, for eviction notices without cause, the landlord must give you a longer period of notice to vacate, generally 30 or 60 days. This lengthened time period is designed to allow you to find another place to live.',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 512]

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

#### parquet

* Dataset: parquet
* Size: 39,780,704 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                           | positive                                                                            |
  |:--------|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                           | string                                                                              |
  | details | <ul><li>min: 4 tokens</li><li>mean: 9.85 tokens</li><li>max: 38 tokens</li></ul> | <ul><li>min: 15 tokens</li><li>mean: 87.54 tokens</li><li>max: 246 tokens</li></ul> |
* Samples:
  | anchor                                                | positive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  |:------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>is a little caffeine ok during pregnancy</code> | <code>We donât know a lot about the effects of caffeine during pregnancy on you and your baby. So itâs best to limit the amount you get each day. If youâre pregnant, limit caffeine to 200 milligrams each day. This is about the amount in 1Â½ 8-ounce cups of coffee or one 12-ounce cup of coffee.</code>                                                                                                                                                                                                                  |
  | <code>what fruit is native to australia</code>        | <code>Passiflora herbertiana. A rare passion fruit native to Australia. Fruits are green-skinned, white fleshed, with an unknown edible rating. Some sources list the fruit as edible, sweet and tasty, while others list the fruits as being bitter and inedible.assiflora herbertiana. A rare passion fruit native to Australia. Fruits are green-skinned, white fleshed, with an unknown edible rating. Some sources list the fruit as edible, sweet and tasty, while others list the fruits as being bitter and inedible.</code> |
  | <code>how large is the canadian military</code>       | <code>The Canadian Armed Forces. 1  The first large-scale Canadian peacekeeping mission started in Egypt on November 24, 1956. 2  There are approximately 65,000 Regular Force and 25,000 reservist members in the Canadian military. 3  In Canada, August 9 is designated as National Peacekeepersâ Day.</code>                                                                                                                                                                                                                   |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Evaluation Dataset

#### parquet

* Dataset: parquet
* Size: 39,780,704 evaluation samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                           | positive                                                                            |
  |:--------|:---------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
  | type    | string                                                                           | string                                                                              |
  | details | <ul><li>min: 4 tokens</li><li>mean: 9.97 tokens</li><li>max: 28 tokens</li></ul> | <ul><li>min: 28 tokens</li><li>mean: 85.19 tokens</li><li>max: 228 tokens</li></ul> |
* Samples:
  | anchor                                                         | positive                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
  |:---------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>chemical weathering definition</code>                    | <code>Chemical weathering is the process where rocks and minerals, which originally formed deep underground at much higher temperatures and pressures, gradually transform into different chemical compounds once they are exposed to air and water at the surface.</code>                                                                                                                                                                                                                                                                                                    |
  | <code>what is the difference between breathe and breath</code> | <code>â¢ The word breath is used as noun. â¢ On the other hand, the word breathe is used as verb. This is the main difference between the two words. â¢ The word breath is used in the sense of âair taken in and out during breathingâ. â¢ On the other hand, the word breathe is used in the sense of âtake air into the lungs and then let it outâ. â¢ The word breathe is sometimes used with the expression âhis/her lastâ, and it gives the meaning of âdie.â This is used for both breath and breathe. His last breath, breathed her last.</code> |
  | <code>what is natural neck tightening</code>                   | <code>Use Sunscreen: One of the best, and a natural method for tightening skin includes applying sunscreen on the face and neck area. This will help to protect against UV rays that can be harmful and help to prevent the premature aging of your skin.</code>                                                                                                                                                                                                                                                                                                              |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 128
- `learning_rate`: 2e-05
- `num_train_epochs`: 5
- `max_steps`: 1476235
- `log_level`: info
- `fp16`: True
- `dataloader_num_workers`: 16
- `load_best_model_at_end`: True
- `resume_from_checkpoint`: True

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 128
- `per_device_eval_batch_size`: 8
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
- `num_train_epochs`: 5
- `max_steps`: 1476235
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.0
- `warmup_steps`: 0
- `log_level`: info
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
- `dataloader_num_workers`: 16
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
- `resume_from_checkpoint`: True
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
- `average_tokens_across_devices`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step    | Training Loss | Validation Loss |
|:------:|:-------:|:-------------:|:---------------:|
| 0.0000 | 1       | 0.7512        | -               |
| 0.0034 | 1000    | 0.3943        | -               |
| 0.0068 | 2000    | 0.316         | -               |
| 0.0102 | 3000    | 0.245         | -               |
| 0.0135 | 4000    | 0.2212        | -               |
| 0.0169 | 5000    | 0.2054        | -               |
| 0.0203 | 6000    | 0.2045        | -               |
| 0.0237 | 7000    | 0.1892        | -               |
| 0.0271 | 8000    | 0.1968        | -               |
| 0.0305 | 9000    | 0.1911        | -               |
| 0.0339 | 10000   | 0.1574        | -               |
| 0.0373 | 11000   | 0.1803        | -               |
| 0.0406 | 12000   | 0.1616        | -               |
| 0.0440 | 13000   | 0.151         | -               |
| 0.0474 | 14000   | 0.1505        | -               |
| 0.0508 | 15000   | 0.1464        | -               |
| 0.0542 | 16000   | 0.1491        | -               |
| 0.0576 | 17000   | 0.1465        | -               |
| 0.0610 | 18000   | 0.1372        | -               |
| 0.0644 | 19000   | 0.1332        | -               |
| 0.0677 | 20000   | 0.1268        | -               |
| 0.0711 | 21000   | 0.1343        | -               |
| 0.0745 | 22000   | 0.1281        | -               |
| 0.0779 | 23000   | 0.1233        | -               |
| 0.0813 | 24000   | 0.1385        | -               |
| 0.0847 | 25000   | 0.133         | -               |
| 0.0881 | 26000   | 0.1257        | -               |
| 0.0914 | 27000   | 0.1059        | -               |
| 0.0948 | 28000   | 0.1063        | -               |
| 0.0982 | 29000   | 0.1174        | -               |
| 0.1016 | 30000   | 0.1152        | -               |
| 0.1050 | 31000   | 0.1067        | -               |
| 0.1084 | 32000   | 0.1026        | -               |
| 0.1118 | 33000   | 0.1215        | -               |
| 0.1152 | 34000   | 0.1077        | -               |
| 0.1185 | 35000   | 0.1068        | -               |
| 0.1219 | 36000   | 0.1132        | -               |
| 0.1253 | 37000   | 0.0965        | -               |
| 0.1287 | 38000   | 0.093         | -               |
| 0.1321 | 39000   | 0.1008        | -               |
| 0.1355 | 40000   | 0.0985        | -               |
| 0.1389 | 41000   | 0.102         | -               |
| 0.1423 | 42000   | 0.0952        | -               |
| 0.1456 | 43000   | 0.0956        | -               |
| 0.1490 | 44000   | 0.0924        | -               |
| 0.1524 | 45000   | 0.0798        | -               |
| 0.1558 | 46000   | 0.0925        | -               |
| 0.1592 | 47000   | 0.0866        | -               |
| 0.1626 | 48000   | 0.0877        | -               |
| 0.1660 | 49000   | 0.0675        | -               |
| 0.1693 | 50000   | 0.0934        | -               |
| 0.1727 | 51000   | 0.0848        | -               |
| 0.1761 | 52000   | 0.0872        | -               |
| 0.1795 | 53000   | 0.0766        | -               |
| 0.1829 | 54000   | 0.0942        | -               |
| 0.1863 | 55000   | 0.0778        | -               |
| 0.1897 | 56000   | 0.0857        | -               |
| 0.1931 | 57000   | 0.0756        | -               |
| 0.1964 | 58000   | 0.0832        | -               |
| 0.1998 | 59000   | 0.0879        | -               |
| 0.2032 | 60000   | 0.081         | -               |
| 0.2066 | 61000   | 0.0765        | -               |
| 0.2100 | 62000   | 0.0804        | -               |
| 0.2134 | 63000   | 0.0783        | -               |
| 0.2168 | 64000   | 0.0622        | -               |
| 0.2202 | 65000   | 0.0878        | -               |
| 0.2235 | 66000   | 0.0799        | -               |
| 0.2269 | 67000   | 0.0766        | -               |
| 0.2303 | 68000   | 0.0751        | -               |
| 0.2337 | 69000   | 0.0861        | -               |
| 0.2371 | 70000   | 0.0777        | -               |
| 0.2405 | 71000   | 0.0758        | -               |
| 0.2439 | 72000   | 0.0736        | -               |
| 0.2472 | 73000   | 0.0703        | -               |
| 0.2506 | 74000   | 0.0642        | -               |
| 0.2540 | 75000   | 0.0711        | -               |
| 0.2574 | 76000   | 0.0747        | -               |
| 0.2608 | 77000   | 0.0674        | -               |
| 0.2642 | 78000   | 0.0724        | -               |
| 0.2676 | 79000   | 0.0607        | -               |
| 0.2710 | 80000   | 0.0592        | -               |
| 0.2743 | 81000   | 0.0633        | -               |
| 0.2777 | 82000   | 0.0597        | -               |
| 0.2811 | 83000   | 0.06          | -               |
| 0.2845 | 84000   | 0.0594        | -               |
| 0.2879 | 85000   | 0.0581        | -               |
| 0.2913 | 86000   | 0.0635        | -               |
| 0.2947 | 87000   | 0.0542        | -               |
| 0.2981 | 88000   | 0.0698        | -               |
| 0.3014 | 89000   | 0.0626        | -               |
| 0.3048 | 90000   | 0.0594        | -               |
| 0.3082 | 91000   | 0.0662        | -               |
| 0.3116 | 92000   | 0.0597        | -               |
| 0.3150 | 93000   | 0.0576        | -               |
| 0.3184 | 94000   | 0.0642        | -               |
| 0.3218 | 95000   | 0.0631        | -               |
| 0.3252 | 96000   | 0.0644        | -               |
| 0.3285 | 97000   | 0.0557        | -               |
| 0.3319 | 98000   | 0.0639        | -               |
| 0.3353 | 99000   | 0.056         | -               |
| 0.3387 | 100000  | 0.0594        | -               |
| 0.3421 | 101000  | 0.0586        | -               |
| 0.3455 | 102000  | 0.0631        | -               |
| 0.3489 | 103000  | 0.0545        | -               |
| 0.3522 | 104000  | 0.0532        | -               |
| 0.3556 | 105000  | 0.0578        | -               |
| 0.3590 | 106000  | 0.0614        | -               |
| 0.3624 | 107000  | 0.0642        | -               |
| 0.3658 | 108000  | 0.0588        | -               |
| 0.3692 | 109000  | 0.0574        | -               |
| 0.3726 | 110000  | 0.0519        | -               |
| 0.3760 | 111000  | 0.0546        | -               |
| 0.3793 | 112000  | 0.0551        | -               |
| 0.3827 | 113000  | 0.0571        | -               |
| 0.3861 | 114000  | 0.0494        | -               |
| 0.3895 | 115000  | 0.0563        | -               |
| 0.3929 | 116000  | 0.0496        | -               |
| 0.3963 | 117000  | 0.0581        | -               |
| 0.3997 | 118000  | 0.0588        | -               |
| 0.4031 | 119000  | 0.0582        | -               |
| 0.4064 | 120000  | 0.0536        | -               |
| 0.4098 | 121000  | 0.0506        | -               |
| 0.4132 | 122000  | 0.0513        | -               |
| 0.4166 | 123000  | 0.057         | -               |
| 0.4200 | 124000  | 0.0559        | -               |
| 0.4234 | 125000  | 0.0527        | -               |
| 0.4268 | 126000  | 0.0483        | -               |
| 0.4301 | 127000  | 0.053         | -               |
| 0.4335 | 128000  | 0.0577        | -               |
| 0.4369 | 129000  | 0.0544        | -               |
| 0.4403 | 130000  | 0.0476        | -               |
| 0.4437 | 131000  | 0.0513        | -               |
| 0.4471 | 132000  | 0.0437        | -               |
| 0.4505 | 133000  | 0.0504        | -               |
| 0.4539 | 134000  | 0.0443        | -               |
| 0.4572 | 135000  | 0.0509        | -               |
| 0.4606 | 136000  | 0.0494        | -               |
| 0.4640 | 137000  | 0.052         | -               |
| 0.4674 | 138000  | 0.0572        | -               |
| 0.4708 | 139000  | 0.0451        | -               |
| 0.4742 | 140000  | 0.05          | -               |
| 0.4776 | 141000  | 0.0506        | -               |
| 0.4810 | 142000  | 0.0534        | -               |
| 0.4843 | 143000  | 0.0479        | -               |
| 0.4877 | 144000  | 0.0431        | -               |
| 0.4911 | 145000  | 0.0477        | -               |
| 0.4945 | 146000  | 0.0483        | -               |
| 0.4979 | 147000  | 0.0537        | -               |
| 0.5013 | 148000  | 0.049         | -               |
| 0.5047 | 149000  | 0.0473        | -               |
| 0.5080 | 150000  | 0.0474        | -               |
| 0.5114 | 151000  | 0.0525        | -               |
| 0.5148 | 152000  | 0.0508        | -               |
| 0.5182 | 153000  | 0.0467        | -               |
| 0.5216 | 154000  | 0.0411        | -               |
| 0.5250 | 155000  | 0.0458        | -               |
| 0.5284 | 156000  | 0.0448        | -               |
| 0.5318 | 157000  | 0.049         | -               |
| 0.5351 | 158000  | 0.0427        | -               |
| 0.5385 | 159000  | 0.0451        | -               |
| 0.5419 | 160000  | 0.0423        | -               |
| 0.5453 | 161000  | 0.0468        | -               |
| 0.5487 | 162000  | 0.0437        | -               |
| 0.5521 | 163000  | 0.0412        | -               |
| 0.5555 | 164000  | 0.0445        | -               |
| 0.5589 | 165000  | 0.0439        | -               |
| 0.5622 | 166000  | 0.0437        | -               |
| 0.5656 | 167000  | 0.0509        | -               |
| 0.5690 | 168000  | 0.043         | -               |
| 0.5724 | 169000  | 0.04          | -               |
| 0.5758 | 170000  | 0.0396        | -               |
| 0.5792 | 171000  | 0.0439        | -               |
| 0.5826 | 172000  | 0.0477        | -               |
| 0.5859 | 173000  | 0.0434        | -               |
| 0.5893 | 174000  | 0.0394        | -               |
| 0.5927 | 175000  | 0.0445        | -               |
| 0.5961 | 176000  | 0.0421        | -               |
| 0.5995 | 177000  | 0.0459        | -               |
| 0.6029 | 178000  | 0.045         | -               |
| 0.6063 | 179000  | 0.0395        | -               |
| 0.6097 | 180000  | 0.0523        | -               |
| 0.6130 | 181000  | 0.0416        | -               |
| 0.6164 | 182000  | 0.0455        | -               |
| 0.6198 | 183000  | 0.0387        | -               |
| 0.6232 | 184000  | 0.0399        | -               |
| 0.6266 | 185000  | 0.0473        | -               |
| 0.6300 | 186000  | 0.0413        | -               |
| 0.6334 | 187000  | 0.0436        | -               |
| 0.6368 | 188000  | 0.0417        | -               |
| 0.6401 | 189000  | 0.0471        | -               |
| 0.6435 | 190000  | 0.0434        | -               |
| 0.6469 | 191000  | 0.0398        | -               |
| 0.6503 | 192000  | 0.0339        | -               |
| 0.6537 | 193000  | 0.0427        | -               |
| 0.6571 | 194000  | 0.0425        | -               |
| 0.6605 | 195000  | 0.0462        | -               |
| 0.6638 | 196000  | 0.0376        | -               |
| 0.6672 | 197000  | 0.0433        | -               |
| 0.6706 | 198000  | 0.0428        | -               |
| 0.6740 | 199000  | 0.0405        | -               |
| 0.6774 | 200000  | 0.0402        | -               |
| 0.6808 | 201000  | 0.0409        | -               |
| 0.6842 | 202000  | 0.0368        | -               |
| 0.6876 | 203000  | 0.0449        | -               |
| 0.6909 | 204000  | 0.0376        | -               |
| 0.6943 | 205000  | 0.0393        | -               |
| 0.6977 | 206000  | 0.0455        | -               |
| 0.7011 | 207000  | 0.0404        | -               |
| 0.7045 | 208000  | 0.0358        | -               |
| 0.7079 | 209000  | 0.0334        | -               |
| 0.7113 | 210000  | 0.0394        | -               |
| 0.7147 | 211000  | 0.0396        | -               |
| 0.7180 | 212000  | 0.0418        | -               |
| 0.7214 | 213000  | 0.0384        | -               |
| 0.7248 | 214000  | 0.0388        | -               |
| 0.7282 | 215000  | 0.0335        | -               |
| 0.7316 | 216000  | 0.0345        | -               |
| 0.7350 | 217000  | 0.0362        | -               |
| 0.7384 | 218000  | 0.0356        | -               |
| 0.7417 | 219000  | 0.0393        | -               |
| 0.7451 | 220000  | 0.0368        | -               |
| 0.7485 | 221000  | 0.0367        | -               |
| 0.7519 | 222000  | 0.0363        | -               |
| 0.7553 | 223000  | 0.038         | -               |
| 0.7587 | 224000  | 0.0332        | -               |
| 0.7621 | 225000  | 0.0381        | -               |
| 0.7655 | 226000  | 0.0417        | -               |
| 0.7688 | 227000  | 0.0315        | -               |
| 0.7722 | 228000  | 0.0396        | -               |
| 0.7756 | 229000  | 0.0394        | -               |
| 0.7790 | 230000  | 0.0318        | -               |
| 0.7824 | 231000  | 0.0389        | -               |
| 0.7858 | 232000  | 0.0359        | -               |
| 0.7892 | 233000  | 0.0372        | -               |
| 0.7926 | 234000  | 0.0391        | -               |
| 0.7959 | 235000  | 0.0364        | -               |
| 0.7993 | 236000  | 0.0365        | -               |
| 0.8027 | 237000  | 0.0374        | -               |
| 0.8061 | 238000  | 0.0338        | -               |
| 0.8095 | 239000  | 0.0349        | -               |
| 0.8129 | 240000  | 0.0359        | -               |
| 0.8163 | 241000  | 0.0324        | -               |
| 0.8196 | 242000  | 0.0348        | -               |
| 0.8230 | 243000  | 0.0396        | -               |
| 0.8264 | 244000  | 0.0353        | -               |
| 0.8298 | 245000  | 0.0383        | -               |
| 0.8332 | 246000  | 0.034         | -               |
| 0.8366 | 247000  | 0.0317        | -               |
| 0.8400 | 248000  | 0.0348        | -               |
| 0.8434 | 249000  | 0.0334        | -               |
| 0.8467 | 250000  | 0.036         | -               |
| 0.8501 | 251000  | 0.0358        | -               |
| 0.8535 | 252000  | 0.0381        | -               |
| 0.8569 | 253000  | 0.0298        | -               |
| 0.8603 | 254000  | 0.031         | -               |
| 0.8637 | 255000  | 0.0363        | -               |
| 0.8671 | 256000  | 0.0301        | -               |
| 0.8705 | 257000  | 0.0396        | -               |
| 0.8738 | 258000  | 0.0343        | -               |
| 0.8772 | 259000  | 0.037         | -               |
| 0.8806 | 260000  | 0.0312        | -               |
| 0.8840 | 261000  | 0.0386        | -               |
| 0.8874 | 262000  | 0.032         | -               |
| 0.8908 | 263000  | 0.0339        | -               |
| 0.8942 | 264000  | 0.0367        | -               |
| 0.8976 | 265000  | 0.0325        | -               |
| 0.9009 | 266000  | 0.034         | -               |
| 0.9043 | 267000  | 0.033         | -               |
| 0.9077 | 268000  | 0.0314        | -               |
| 0.9111 | 269000  | 0.0305        | -               |
| 0.9145 | 270000  | 0.0323        | -               |
| 0.9179 | 271000  | 0.0362        | -               |
| 0.9213 | 272000  | 0.0348        | -               |
| 0.9246 | 273000  | 0.0314        | -               |
| 0.9280 | 274000  | 0.0327        | -               |
| 0.9314 | 275000  | 0.0318        | -               |
| 0.9348 | 276000  | 0.0336        | -               |
| 0.9382 | 277000  | 0.0292        | -               |
| 0.9416 | 278000  | 0.0314        | -               |
| 0.9450 | 279000  | 0.0275        | -               |
| 0.9484 | 280000  | 0.0311        | -               |
| 0.9517 | 281000  | 0.0327        | -               |
| 0.9551 | 282000  | 0.0327        | -               |
| 0.9585 | 283000  | 0.0338        | -               |
| 0.9619 | 284000  | 0.0324        | -               |
| 0.9653 | 285000  | 0.03          | -               |
| 0.9687 | 286000  | 0.0301        | -               |
| 0.9721 | 287000  | 0.0351        | -               |
| 0.9755 | 288000  | 0.0288        | -               |
| 0.9788 | 289000  | 0.0317        | -               |
| 0.9822 | 290000  | 0.0324        | -               |
| 0.9856 | 291000  | 0.0323        | -               |
| 0.9890 | 292000  | 0.0299        | -               |
| 0.9924 | 293000  | 0.0352        | -               |
| 0.9958 | 294000  | 0.0316        | -               |
| 0.9992 | 295000  | 0.0327        | -               |
| 1.0000 | 295247  | -             | 0.0001          |
| 1.0025 | 296000  | 0.0313        | -               |
| 1.0059 | 297000  | 0.0323        | -               |
| 1.0093 | 298000  | 0.0311        | -               |
| 1.0127 | 299000  | 0.0284        | -               |
| 1.0161 | 300000  | 0.0246        | -               |
| 1.0195 | 301000  | 0.0323        | -               |
| 1.0229 | 302000  | 0.0257        | -               |
| 1.0263 | 303000  | 0.0349        | -               |
| 1.0296 | 304000  | 0.0322        | -               |
| 1.0330 | 305000  | 0.0267        | -               |
| 1.0364 | 306000  | 0.0306        | -               |
| 1.0398 | 307000  | 0.0313        | -               |
| 1.0432 | 308000  | 0.0293        | -               |
| 1.0466 | 309000  | 0.0279        | -               |
| 1.0500 | 310000  | 0.0302        | -               |
| 1.0534 | 311000  | 0.0287        | -               |
| 1.0567 | 312000  | 0.0317        | -               |
| 1.0601 | 313000  | 0.0302        | -               |
| 1.0635 | 314000  | 0.029         | -               |
| 1.0669 | 315000  | 0.0263        | -               |
| 1.0703 | 316000  | 0.0329        | -               |
| 1.0737 | 317000  | 0.0291        | -               |
| 1.0771 | 318000  | 0.0274        | -               |
| 1.0804 | 319000  | 0.0331        | -               |
| 1.0838 | 320000  | 0.0338        | -               |
| 1.0872 | 321000  | 0.0303        | -               |
| 1.0906 | 322000  | 0.028         | -               |
| 1.0940 | 323000  | 0.0242        | -               |
| 1.0974 | 324000  | 0.0325        | -               |
| 1.1008 | 325000  | 0.0284        | -               |
| 1.1042 | 326000  | 0.0281        | -               |
| 1.1075 | 327000  | 0.0256        | -               |
| 1.1109 | 328000  | 0.0314        | -               |
| 1.1143 | 329000  | 0.031         | -               |
| 1.1177 | 330000  | 0.0286        | -               |
| 1.1211 | 331000  | 0.0321        | -               |
| 1.1245 | 332000  | 0.0271        | -               |
| 1.1279 | 333000  | 0.0242        | -               |
| 1.1313 | 334000  | 0.0309        | -               |
| 1.1346 | 335000  | 0.0266        | -               |
| 1.1380 | 336000  | 0.0315        | -               |
| 1.1414 | 337000  | 0.0272        | -               |
| 1.1448 | 338000  | 0.03          | -               |
| 1.1482 | 339000  | 0.0265        | -               |
| 1.1516 | 340000  | 0.0267        | -               |
| 1.1550 | 341000  | 0.0252        | -               |
| 1.1583 | 342000  | 0.0276        | -               |
| 1.1617 | 343000  | 0.027         | -               |
| 1.1651 | 344000  | 0.0224        | -               |
| 1.1685 | 345000  | 0.0283        | -               |
| 1.1719 | 346000  | 0.0249        | -               |
| 1.1753 | 347000  | 0.0294        | -               |
| 1.1787 | 348000  | 0.0237        | -               |
| 1.1821 | 349000  | 0.0298        | -               |
| 1.1854 | 350000  | 0.0297        | -               |
| 1.1888 | 351000  | 0.0261        | -               |
| 1.1922 | 352000  | 0.0252        | -               |
| 1.1956 | 353000  | 0.0265        | -               |
| 1.1990 | 354000  | 0.0311        | -               |
| 1.2024 | 355000  | 0.0284        | -               |
| 1.2058 | 356000  | 0.027         | -               |
| 1.2092 | 357000  | 0.0272        | -               |
| 1.2125 | 358000  | 0.0287        | -               |
| 1.2159 | 359000  | 0.0226        | -               |
| 1.2193 | 360000  | 0.0284        | -               |
| 1.2227 | 361000  | 0.0285        | -               |
| 1.2261 | 362000  | 0.0296        | -               |
| 1.2295 | 363000  | 0.0261        | -               |
| 1.2329 | 364000  | 0.0301        | -               |
| 1.2362 | 365000  | 0.0286        | -               |
| 1.2396 | 366000  | 0.0299        | -               |
| 1.2430 | 367000  | 0.0257        | -               |
| 1.2464 | 368000  | 0.0278        | -               |
| 1.2498 | 369000  | 0.0241        | -               |
| 1.2532 | 370000  | 0.0252        | -               |
| 1.2566 | 371000  | 0.0275        | -               |
| 1.2600 | 372000  | 0.025         | -               |
| 1.2633 | 373000  | 0.0287        | -               |
| 1.2667 | 374000  | 0.025         | -               |
| 1.2701 | 375000  | 0.0223        | -               |
| 1.2735 | 376000  | 0.0224        | -               |
| 1.2769 | 377000  | 0.0249        | -               |
| 1.2803 | 378000  | 0.0213        | -               |
| 1.2837 | 379000  | 0.0248        | -               |
| 1.2871 | 380000  | 0.0231        | -               |
| 1.2904 | 381000  | 0.026         | -               |
| 1.2938 | 382000  | 0.0221        | -               |
| 1.2972 | 383000  | 0.0263        | -               |
| 1.3006 | 384000  | 0.0238        | -               |
| 1.3040 | 385000  | 0.0254        | -               |
| 1.3074 | 386000  | 0.0281        | -               |
| 1.3108 | 387000  | 0.0252        | -               |
| 1.3141 | 388000  | 0.0226        | -               |
| 1.3175 | 389000  | 0.0252        | -               |
| 1.3209 | 390000  | 0.0264        | -               |
| 1.3243 | 391000  | 0.0264        | -               |
| 1.3277 | 392000  | 0.0245        | -               |
| 1.3311 | 393000  | 0.0256        | -               |
| 1.3345 | 394000  | 0.0231        | -               |
| 1.3379 | 395000  | 0.0251        | -               |
| 1.3412 | 396000  | 0.0261        | -               |
| 1.3446 | 397000  | 0.0245        | -               |
| 1.3480 | 398000  | 0.0241        | -               |
| 1.3514 | 399000  | 0.0194        | -               |
| 1.3548 | 400000  | 0.0265        | -               |
| 1.3582 | 401000  | 0.0281        | -               |
| 1.3616 | 402000  | 0.0272        | -               |
| 1.3650 | 403000  | 0.025         | -               |
| 1.3683 | 404000  | 0.0245        | -               |
| 1.3717 | 405000  | 0.0244        | -               |
| 1.3751 | 406000  | 0.0232        | -               |
| 1.3785 | 407000  | 0.0243        | -               |
| 1.3819 | 408000  | 0.0247        | -               |
| 1.3853 | 409000  | 0.0228        | -               |
| 1.3887 | 410000  | 0.0243        | -               |
| 1.3921 | 411000  | 0.0233        | -               |
| 1.3954 | 412000  | 0.0246        | -               |
| 1.3988 | 413000  | 0.0256        | -               |
| 1.4022 | 414000  | 0.0264        | -               |
| 1.4056 | 415000  | 0.0245        | -               |
| 1.4090 | 416000  | 0.0232        | -               |
| 1.4124 | 417000  | 0.0232        | -               |
| 1.4158 | 418000  | 0.0247        | -               |
| 1.4191 | 419000  | 0.0269        | -               |
| 1.4225 | 420000  | 0.0245        | -               |
| 1.4259 | 421000  | 0.0227        | -               |
| 1.4293 | 422000  | 0.0241        | -               |
| 1.4327 | 423000  | 0.0251        | -               |
| 1.4361 | 424000  | 0.0258        | -               |
| 1.4395 | 425000  | 0.0223        | -               |
| 1.4429 | 426000  | 0.025         | -               |
| 1.4462 | 427000  | 0.0203        | -               |
| 1.4496 | 428000  | 0.0234        | -               |
| 1.4530 | 429000  | 0.0222        | -               |
| 1.4564 | 430000  | 0.0212        | -               |
| 1.4598 | 431000  | 0.0247        | -               |
| 1.4632 | 432000  | 0.0236        | -               |
| 1.4666 | 433000  | 0.0272        | -               |
| 1.4700 | 434000  | 0.0227        | -               |
| 1.4733 | 435000  | 0.0234        | -               |
| 1.4767 | 436000  | 0.023         | -               |
| 1.4801 | 437000  | 0.0266        | -               |
| 1.4835 | 438000  | 0.0228        | -               |
| 1.4869 | 439000  | 0.022         | -               |
| 1.4903 | 440000  | 0.0212        | -               |
| 1.4937 | 441000  | 0.0265        | -               |
| 1.4970 | 442000  | 0.0246        | -               |
| 1.5004 | 443000  | 0.024         | -               |
| 1.5038 | 444000  | 0.0228        | -               |
| 1.5072 | 445000  | 0.0233        | -               |
| 1.5106 | 446000  | 0.025         | -               |
| 1.5140 | 447000  | 0.0259        | -               |
| 1.5174 | 448000  | 0.024         | -               |
| 1.5208 | 449000  | 0.0209        | -               |
| 1.5241 | 450000  | 0.0226        | -               |
| 1.5275 | 451000  | 0.0215        | -               |
| 1.5309 | 452000  | 0.0253        | -               |
| 1.5343 | 453000  | 0.0215        | -               |
| 1.5377 | 454000  | 0.0226        | -               |
| 1.5411 | 455000  | 0.0221        | -               |
| 1.5445 | 456000  | 0.0237        | -               |
| 1.5479 | 457000  | 0.0231        | -               |
| 1.5512 | 458000  | 0.0202        | -               |
| 1.5546 | 459000  | 0.0224        | -               |
| 1.5580 | 460000  | 0.0236        | -               |
| 1.5614 | 461000  | 0.0214        | -               |
| 1.5648 | 462000  | 0.0266        | -               |
| 1.5682 | 463000  | 0.0213        | -               |
| 1.5716 | 464000  | 0.0214        | -               |
| 1.5749 | 465000  | 0.0214        | -               |
| 1.5783 | 466000  | 0.021         | -               |
| 1.5817 | 467000  | 0.0251        | -               |
| 1.5851 | 468000  | 0.0227        | -               |
| 1.5885 | 469000  | 0.0209        | -               |
| 1.5919 | 470000  | 0.0233        | -               |
| 1.5953 | 471000  | 0.0226        | -               |
| 1.5987 | 472000  | 0.0227        | -               |
| 1.6020 | 473000  | 0.0226        | -               |
| 1.6054 | 474000  | 0.0234        | -               |
| 1.6088 | 475000  | 0.0248        | -               |
| 1.6122 | 476000  | 0.0239        | -               |
| 1.6156 | 477000  | 0.0243        | -               |
| 1.6190 | 478000  | 0.0206        | -               |
| 1.6224 | 479000  | 0.0217        | -               |
| 1.6258 | 480000  | 0.0233        | -               |
| 1.6291 | 481000  | 0.0229        | -               |
| 1.6325 | 482000  | 0.0246        | -               |
| 1.6359 | 483000  | 0.0228        | -               |
| 1.6393 | 484000  | 0.0252        | -               |
| 1.6427 | 485000  | 0.0231        | -               |
| 1.6461 | 486000  | 0.0219        | -               |
| 1.6495 | 487000  | 0.0197        | -               |
| 1.6528 | 488000  | 0.0224        | -               |
| 1.6562 | 489000  | 0.0218        | -               |
| 1.6596 | 490000  | 0.0244        | -               |
| 1.6630 | 491000  | 0.0218        | -               |
| 1.6664 | 492000  | 0.022         | -               |
| 1.6698 | 493000  | 0.0234        | -               |
| 1.6732 | 494000  | 0.0222        | -               |
| 1.6766 | 495000  | 0.0218        | -               |
| 1.6799 | 496000  | 0.0227        | -               |
| 1.6833 | 497000  | 0.0219        | -               |
| 1.6867 | 498000  | 0.023         | -               |
| 1.6901 | 499000  | 0.0214        | -               |
| 1.6935 | 500000  | 0.021         | -               |
| 1.6969 | 501000  | 0.0242        | -               |
| 1.7003 | 502000  | 0.0243        | -               |
| 1.7037 | 503000  | 0.0198        | -               |
| 1.7070 | 504000  | 0.0186        | -               |
| 1.7104 | 505000  | 0.0226        | -               |
| 1.7138 | 506000  | 0.0221        | -               |
| 1.7172 | 507000  | 0.0233        | -               |
| 1.7206 | 508000  | 0.0227        | -               |
| 1.7240 | 509000  | 0.0201        | -               |
| 1.7274 | 510000  | 0.0203        | -               |
| 1.7307 | 511000  | 0.0207        | -               |
| 1.7341 | 512000  | 0.0191        | -               |
| 1.7375 | 513000  | 0.0207        | -               |
| 1.7409 | 514000  | 0.022         | -               |
| 1.7443 | 515000  | 0.0202        | -               |
| 1.7477 | 516000  | 0.0211        | -               |
| 1.7511 | 517000  | 0.021         | -               |
| 1.7545 | 518000  | 0.0214        | -               |
| 1.7578 | 519000  | 0.0193        | -               |
| 1.7612 | 520000  | 0.0225        | -               |
| 1.7646 | 521000  | 0.0221        | -               |
| 1.7680 | 522000  | 0.0185        | -               |
| 1.7714 | 523000  | 0.0236        | -               |
| 1.7748 | 524000  | 0.0232        | -               |
| 1.7782 | 525000  | 0.0192        | -               |
| 1.7816 | 526000  | 0.0221        | -               |
| 1.7849 | 527000  | 0.0212        | -               |
| 1.7883 | 528000  | 0.0216        | -               |
| 1.7917 | 529000  | 0.0225        | -               |
| 1.7951 | 530000  | 0.0207        | -               |
| 1.7985 | 531000  | 0.0212        | -               |
| 1.8019 | 532000  | 0.0217        | -               |
| 1.8053 | 533000  | 0.0192        | -               |
| 1.8086 | 534000  | 0.0216        | -               |
| 1.8120 | 535000  | 0.0209        | -               |
| 1.8154 | 536000  | 0.0193        | -               |
| 1.8188 | 537000  | 0.0185        | -               |
| 1.8222 | 538000  | 0.024         | -               |
| 1.8256 | 539000  | 0.0208        | -               |
| 1.8290 | 540000  | 0.0238        | -               |
| 1.8324 | 541000  | 0.0203        | -               |
| 1.8357 | 542000  | 0.0196        | -               |
| 1.8391 | 543000  | 0.0197        | -               |
| 1.8425 | 544000  | 0.0213        | -               |
| 1.8459 | 545000  | 0.0194        | -               |
| 1.8493 | 546000  | 0.0218        | -               |
| 1.8527 | 547000  | 0.0218        | -               |
| 1.8561 | 548000  | 0.0191        | -               |
| 1.8595 | 549000  | 0.0197        | -               |
| 1.8628 | 550000  | 0.0208        | -               |
| 1.8662 | 551000  | 0.0184        | -               |
| 1.8696 | 552000  | 0.0224        | -               |
| 1.8730 | 553000  | 0.0214        | -               |
| 1.8764 | 554000  | 0.0226        | -               |
| 1.8798 | 555000  | 0.0194        | -               |
| 1.8832 | 556000  | 0.0225        | -               |
| 1.8865 | 557000  | 0.0193        | -               |
| 1.8899 | 558000  | 0.0207        | -               |
| 1.8933 | 559000  | 0.0212        | -               |
| 1.8967 | 560000  | 0.021         | -               |
| 1.9001 | 561000  | 0.0197        | -               |
| 1.9035 | 562000  | 0.0198        | -               |
| 1.9069 | 563000  | 0.0199        | -               |
| 1.9103 | 564000  | 0.018         | -               |
| 1.9136 | 565000  | 0.021         | -               |
| 1.9170 | 566000  | 0.02          | -               |
| 1.9204 | 567000  | 0.022         | -               |
| 1.9238 | 568000  | 0.0193        | -               |
| 1.9272 | 569000  | 0.0197        | -               |
| 1.9306 | 570000  | 0.0201        | -               |
| 1.9340 | 571000  | 0.0196        | -               |
| 1.9374 | 572000  | 0.0192        | -               |
| 1.9407 | 573000  | 0.0169        | -               |
| 1.9441 | 574000  | 0.0186        | -               |
| 1.9475 | 575000  | 0.019         | -               |
| 1.9509 | 576000  | 0.0195        | -               |
| 1.9543 | 577000  | 0.0206        | -               |
| 1.9577 | 578000  | 0.0198        | -               |
| 1.9611 | 579000  | 0.0211        | -               |
| 1.9645 | 580000  | 0.0178        | -               |
| 1.9678 | 581000  | 0.0187        | -               |
| 1.9712 | 582000  | 0.0218        | -               |
| 1.9746 | 583000  | 0.0192        | -               |
| 1.9780 | 584000  | 0.0187        | -               |
| 1.9814 | 585000  | 0.0207        | -               |
| 1.9848 | 586000  | 0.0202        | -               |
| 1.9882 | 587000  | 0.0195        | -               |
| 1.9915 | 588000  | 0.0201        | -               |
| 1.9949 | 589000  | 0.0208        | -               |
| 1.9983 | 590000  | 0.0203        | -               |
| 2.0000 | 590494  | -             | 0.0000          |
| 2.0017 | 591000  | 0.0185        | -               |
| 2.0051 | 592000  | 0.0216        | -               |
| 2.0085 | 593000  | 0.0211        | -               |
| 2.0119 | 594000  | 0.0184        | -               |
| 2.0153 | 595000  | 0.0159        | -               |
| 2.0186 | 596000  | 0.0193        | -               |
| 2.0220 | 597000  | 0.016         | -               |
| 2.0254 | 598000  | 0.0224        | -               |
| 2.0288 | 599000  | 0.0197        | -               |
| 2.0322 | 600000  | 0.018         | -               |
| 2.0356 | 601000  | 0.0191        | -               |
| 2.0390 | 602000  | 0.0204        | -               |
| 2.0424 | 603000  | 0.0195        | -               |
| 2.0457 | 604000  | 0.0173        | -               |
| 2.0491 | 605000  | 0.0201        | -               |
| 2.0525 | 606000  | 0.0185        | -               |
| 2.0559 | 607000  | 0.0205        | -               |
| 2.0593 | 608000  | 0.0195        | -               |
| 2.0627 | 609000  | 0.0189        | -               |
| 2.0661 | 610000  | 0.0195        | -               |
| 2.0694 | 611000  | 0.019         | -               |
| 2.0728 | 612000  | 0.0193        | -               |
| 2.0762 | 613000  | 0.0185        | -               |
| 2.0796 | 614000  | 0.0208        | -               |
| 2.0830 | 615000  | 0.0215        | -               |
| 2.0864 | 616000  | 0.0197        | -               |
| 2.0898 | 617000  | 0.0199        | -               |
| 2.0932 | 618000  | 0.0162        | -               |
| 2.0965 | 619000  | 0.0202        | -               |
| 2.0999 | 620000  | 0.0187        | -               |
| 2.1033 | 621000  | 0.0186        | -               |
| 2.1067 | 622000  | 0.0164        | -               |
| 2.1101 | 623000  | 0.0201        | -               |
| 2.1135 | 624000  | 0.0205        | -               |
| 2.1169 | 625000  | 0.0197        | -               |
| 2.1203 | 626000  | 0.0202        | -               |
| 2.1236 | 627000  | 0.0185        | -               |
| 2.1270 | 628000  | 0.017         | -               |
| 2.1304 | 629000  | 0.0192        | -               |
| 2.1338 | 630000  | 0.0171        | -               |
| 2.1372 | 631000  | 0.0201        | -               |
| 2.1406 | 632000  | 0.017         | -               |
| 2.1440 | 633000  | 0.0209        | -               |
| 2.1473 | 634000  | 0.0178        | -               |
| 2.1507 | 635000  | 0.0166        | -               |
| 2.1541 | 636000  | 0.0165        | -               |
| 2.1575 | 637000  | 0.0178        | -               |
| 2.1609 | 638000  | 0.02          | -               |
| 2.1643 | 639000  | 0.0173        | -               |
| 2.1677 | 640000  | 0.0168        | -               |
| 2.1711 | 641000  | 0.0174        | -               |
| 2.1744 | 642000  | 0.0181        | -               |
| 2.1778 | 643000  | 0.0167        | -               |
| 2.1812 | 644000  | 0.0196        | -               |
| 2.1846 | 645000  | 0.0208        | -               |
| 2.1880 | 646000  | 0.0171        | -               |
| 2.1914 | 647000  | 0.017         | -               |
| 2.1948 | 648000  | 0.0169        | -               |
| 2.1982 | 649000  | 0.0211        | -               |
| 2.2015 | 650000  | 0.02          | -               |
| 2.2049 | 651000  | 0.0188        | -               |
| 2.2083 | 652000  | 0.0171        | -               |
| 2.2117 | 653000  | 0.0198        | -               |
| 2.2151 | 654000  | 0.0177        | -               |
| 2.2185 | 655000  | 0.0168        | -               |
| 2.2219 | 656000  | 0.0197        | -               |
| 2.2252 | 657000  | 0.0194        | -               |
| 2.2286 | 658000  | 0.0181        | -               |
| 2.2320 | 659000  | 0.0186        | -               |
| 2.2354 | 660000  | 0.0196        | -               |
| 2.2388 | 661000  | 0.0217        | -               |
| 2.2422 | 662000  | 0.0165        | -               |
| 2.2456 | 663000  | 0.0196        | -               |
| 2.2490 | 664000  | 0.0173        | -               |
| 2.2523 | 665000  | 0.0158        | -               |
| 2.2557 | 666000  | 0.0183        | -               |
| 2.2591 | 667000  | 0.018         | -               |
| 2.2625 | 668000  | 0.0197        | -               |
| 2.2659 | 669000  | 0.0175        | -               |
| 2.2693 | 670000  | 0.0161        | -               |
| 2.2727 | 671000  | 0.0145        | -               |
| 2.2761 | 672000  | 0.0175        | -               |
| 2.2794 | 673000  | 0.0149        | -               |
| 2.2828 | 674000  | 0.0163        | -               |
| 2.2862 | 675000  | 0.0161        | -               |
| 2.2896 | 676000  | 0.0166        | -               |
| 2.2930 | 677000  | 0.0161        | -               |
| 2.2964 | 678000  | 0.0165        | -               |
| 2.2998 | 679000  | 0.0179        | -               |
| 2.3031 | 680000  | 0.017         | -               |
| 2.3065 | 681000  | 0.0185        | -               |
| 2.3099 | 682000  | 0.0186        | -               |
| 2.3133 | 683000  | 0.0152        | -               |
| 2.3167 | 684000  | 0.0167        | -               |
| 2.3201 | 685000  | 0.018         | -               |
| 2.3235 | 686000  | 0.018         | -               |
| 2.3269 | 687000  | 0.0178        | -               |
| 2.3302 | 688000  | 0.0168        | -               |
| 2.3336 | 689000  | 0.0168        | -               |
| 2.3370 | 690000  | 0.0184        | -               |
| 2.3404 | 691000  | 0.0172        | -               |
| 2.3438 | 692000  | 0.017         | -               |
| 2.3472 | 693000  | 0.0173        | -               |
| 2.3506 | 694000  | 0.0137        | -               |
| 2.3540 | 695000  | 0.0181        | -               |
| 2.3573 | 696000  | 0.0184        | -               |
| 2.3607 | 697000  | 0.0189        | -               |
| 2.3641 | 698000  | 0.0158        | -               |
| 2.3675 | 699000  | 0.0183        | -               |
| 2.3709 | 700000  | 0.0177        | -               |
| 2.3743 | 701000  | 0.0159        | -               |
| 2.3777 | 702000  | 0.0169        | -               |
| 2.3810 | 703000  | 0.0171        | -               |
| 2.3844 | 704000  | 0.0167        | -               |
| 2.3878 | 705000  | 0.0163        | -               |
| 2.3912 | 706000  | 0.0168        | -               |
| 2.3946 | 707000  | 0.017         | -               |
| 2.3980 | 708000  | 0.0183        | -               |
| 2.4014 | 709000  | 0.0182        | -               |
| 2.4048 | 710000  | 0.0178        | -               |
| 2.4081 | 711000  | 0.0168        | -               |
| 2.4115 | 712000  | 0.0163        | -               |
| 2.4149 | 713000  | 0.0171        | -               |
| 2.4183 | 714000  | 0.0186        | -               |
| 2.4217 | 715000  | 0.018         | -               |
| 2.4251 | 716000  | 0.0166        | -               |
| 2.4285 | 717000  | 0.0161        | -               |
| 2.4319 | 718000  | 0.017         | -               |
| 2.4352 | 719000  | 0.0187        | -               |
| 2.4386 | 720000  | 0.0167        | -               |
| 2.4420 | 721000  | 0.0169        | -               |
| 2.4454 | 722000  | 0.015         | -               |
| 2.4488 | 723000  | 0.0153        | -               |
| 2.4522 | 724000  | 0.0172        | -               |
| 2.4556 | 725000  | 0.0157        | -               |
| 2.4589 | 726000  | 0.0167        | -               |
| 2.4623 | 727000  | 0.0161        | -               |
| 2.4657 | 728000  | 0.0188        | -               |
| 2.4691 | 729000  | 0.0174        | -               |
| 2.4725 | 730000  | 0.0161        | -               |
| 2.4759 | 731000  | 0.0159        | -               |
| 2.4793 | 732000  | 0.0192        | -               |
| 2.4827 | 733000  | 0.0173        | -               |
| 2.4860 | 734000  | 0.0162        | -               |
| 2.4894 | 735000  | 0.0155        | -               |
| 2.4928 | 736000  | 0.0186        | -               |
| 2.4962 | 737000  | 0.0163        | -               |
| 2.4996 | 738000  | 0.018         | -               |
| 2.5030 | 739000  | 0.0158        | -               |
| 2.5064 | 740000  | 0.017         | -               |
| 2.5098 | 741000  | 0.0181        | -               |
| 2.5131 | 742000  | 0.019         | -               |
| 2.5165 | 743000  | 0.0172        | -               |
| 2.5199 | 744000  | 0.0158        | -               |
| 2.5233 | 745000  | 0.0143        | -               |
| 2.5267 | 746000  | 0.0153        | -               |
| 2.5301 | 747000  | 0.0178        | -               |
| 2.5335 | 748000  | 0.0175        | -               |
| 2.5369 | 749000  | 0.0161        | -               |
| 2.5402 | 750000  | 0.0157        | -               |
| 2.5436 | 751000  | 0.0171        | -               |
| 2.5470 | 752000  | 0.0173        | -               |
| 2.5504 | 753000  | 0.0144        | -               |
| 2.5538 | 754000  | 0.0157        | -               |
| 2.5572 | 755000  | 0.0176        | -               |
| 2.5606 | 756000  | 0.0146        | -               |
| 2.5639 | 757000  | 0.019         | -               |
| 2.5673 | 758000  | 0.0169        | -               |
| 2.5707 | 759000  | 0.0157        | -               |
| 2.5741 | 760000  | 0.0153        | -               |
| 2.5775 | 761000  | 0.0155        | -               |
| 2.5809 | 762000  | 0.0177        | -               |
| 2.5843 | 763000  | 0.0174        | -               |
| 2.5877 | 764000  | 0.0157        | -               |
| 2.5910 | 765000  | 0.016         | -               |
| 2.5944 | 766000  | 0.0175        | -               |
| 2.5978 | 767000  | 0.0162        | -               |
| 2.6012 | 768000  | 0.0161        | -               |
| 2.6046 | 769000  | 0.0166        | -               |
| 2.6080 | 770000  | 0.0172        | -               |
| 2.6114 | 771000  | 0.0182        | -               |
| 2.6148 | 772000  | 0.0175        | -               |
| 2.6181 | 773000  | 0.0157        | -               |
| 2.6215 | 774000  | 0.0155        | -               |
| 2.6249 | 775000  | 0.0166        | -               |
| 2.6283 | 776000  | 0.017         | -               |
| 2.6317 | 777000  | 0.0188        | -               |
| 2.6351 | 778000  | 0.017         | -               |
| 2.6385 | 779000  | 0.0172        | -               |
| 2.6418 | 780000  | 0.0177        | -               |
| 2.6452 | 781000  | 0.0168        | -               |
| 2.6486 | 782000  | 0.0152        | -               |
| 2.6520 | 783000  | 0.0163        | -               |
| 2.6554 | 784000  | 0.0148        | -               |
| 2.6588 | 785000  | 0.0186        | -               |
| 2.6622 | 786000  | 0.0173        | -               |
| 2.6656 | 787000  | 0.0153        | -               |
| 2.6689 | 788000  | 0.0172        | -               |
| 2.6723 | 789000  | 0.0161        | -               |
| 2.6757 | 790000  | 0.0159        | -               |
| 2.6791 | 791000  | 0.0162        | -               |
| 2.6825 | 792000  | 0.0173        | -               |
| 2.6859 | 793000  | 0.0159        | -               |
| 2.6893 | 794000  | 0.0162        | -               |
| 2.6927 | 795000  | 0.0153        | -               |
| 2.6960 | 796000  | 0.0173        | -               |
| 2.6994 | 797000  | 0.0184        | -               |
| 2.7028 | 798000  | 0.0149        | -               |
| 2.7062 | 799000  | 0.0148        | -               |
| 2.7096 | 800000  | 0.0152        | -               |
| 2.7130 | 801000  | 0.0165        | -               |
| 2.7164 | 802000  | 0.017         | -               |
| 2.7197 | 803000  | 0.0169        | -               |
| 2.7231 | 804000  | 0.0154        | -               |
| 2.7265 | 805000  | 0.0153        | -               |
| 2.7299 | 806000  | 0.0154        | -               |
| 2.7333 | 807000  | 0.0146        | -               |
| 2.7367 | 808000  | 0.0158        | -               |
| 2.7401 | 809000  | 0.0157        | -               |
| 2.7435 | 810000  | 0.0148        | -               |
| 2.7468 | 811000  | 0.0151        | -               |
| 2.7502 | 812000  | 0.016         | -               |
| 2.7536 | 813000  | 0.0155        | -               |
| 2.7570 | 814000  | 0.0154        | -               |
| 2.7604 | 815000  | 0.0152        | -               |
| 2.7638 | 816000  | 0.0159        | -               |
| 2.7672 | 817000  | 0.0158        | -               |
| 2.7706 | 818000  | 0.0162        | -               |
| 2.7739 | 819000  | 0.0174        | -               |
| 2.7773 | 820000  | 0.0151        | -               |
| 2.7807 | 821000  | 0.0157        | -               |
| 2.7841 | 822000  | 0.0163        | -               |
| 2.7875 | 823000  | 0.0158        | -               |
| 2.7909 | 824000  | 0.0166        | -               |
| 2.7943 | 825000  | 0.0161        | -               |
| 2.7976 | 826000  | 0.016         | -               |
| 2.8010 | 827000  | 0.0164        | -               |
| 2.8044 | 828000  | 0.0155        | -               |
| 2.8078 | 829000  | 0.0151        | -               |
| 2.8112 | 830000  | 0.0157        | -               |
| 2.8146 | 831000  | 0.015         | -               |
| 2.8180 | 832000  | 0.0132        | -               |
| 2.8214 | 833000  | 0.0171        | -               |
| 2.8247 | 834000  | 0.0171        | -               |
| 2.8281 | 835000  | 0.0171        | -               |
| 2.8315 | 836000  | 0.0146        | -               |
| 2.8349 | 837000  | 0.0154        | -               |
| 2.8383 | 838000  | 0.0142        | -               |
| 2.8417 | 839000  | 0.0161        | -               |
| 2.8451 | 840000  | 0.015         | -               |
| 2.8485 | 841000  | 0.0159        | -               |
| 2.8518 | 842000  | 0.0157        | -               |
| 2.8552 | 843000  | 0.0161        | -               |
| 2.8586 | 844000  | 0.0137        | -               |
| 2.8620 | 845000  | 0.0161        | -               |
| 2.8654 | 846000  | 0.0148        | -               |
| 2.8688 | 847000  | 0.0154        | -               |
| 2.8722 | 848000  | 0.0165        | -               |
| 2.8755 | 849000  | 0.0172        | -               |
| 2.8789 | 850000  | 0.0153        | -               |
| 2.8823 | 851000  | 0.0157        | -               |
| 2.8857 | 852000  | 0.0152        | -               |
| 2.8891 | 853000  | 0.0159        | -               |
| 2.8925 | 854000  | 0.0156        | -               |
| 2.8959 | 855000  | 0.0161        | -               |
| 2.8993 | 856000  | 0.014         | -               |
| 2.9026 | 857000  | 0.0164        | -               |
| 2.9060 | 858000  | 0.0144        | -               |
| 2.9094 | 859000  | 0.0144        | -               |
| 2.9128 | 860000  | 0.0152        | -               |
| 2.9162 | 861000  | 0.0143        | -               |
| 2.9196 | 862000  | 0.0183        | -               |
| 2.9230 | 863000  | 0.0146        | -               |
| 2.9264 | 864000  | 0.0149        | -               |
| 2.9297 | 865000  | 0.0153        | -               |
| 2.9331 | 866000  | 0.0151        | -               |
| 2.9365 | 867000  | 0.0139        | -               |
| 2.9399 | 868000  | 0.0134        | -               |
| 2.9433 | 869000  | 0.0154        | -               |
| 2.9467 | 870000  | 0.0141        | -               |
| 2.9501 | 871000  | 0.0141        | -               |
| 2.9534 | 872000  | 0.0158        | -               |
| 2.9568 | 873000  | 0.0148        | -               |
| 2.9602 | 874000  | 0.0163        | -               |
| 2.9636 | 875000  | 0.0131        | -               |
| 2.9670 | 876000  | 0.0158        | -               |
| 2.9704 | 877000  | 0.0145        | -               |
| 2.9738 | 878000  | 0.0158        | -               |
| 2.9772 | 879000  | 0.0142        | -               |
| 2.9805 | 880000  | 0.015         | -               |
| 2.9839 | 881000  | 0.0157        | -               |
| 2.9873 | 882000  | 0.0151        | -               |
| 2.9907 | 883000  | 0.015         | -               |
| 2.9941 | 884000  | 0.0165        | -               |
| 2.9975 | 885000  | 0.0154        | -               |
| 3.0000 | 885741  | -             | 0.0000          |
| 3.0009 | 886000  | 0.0145        | -               |
| 3.0043 | 887000  | 0.0163        | -               |
| 3.0076 | 888000  | 0.0164        | -               |
| 3.0110 | 889000  | 0.0146        | -               |
| 3.0144 | 890000  | 0.012         | -               |
| 3.0178 | 891000  | 0.0141        | -               |
| 3.0212 | 892000  | 0.0134        | -               |
| 3.0246 | 893000  | 0.015         | -               |
| 3.0280 | 894000  | 0.0157        | -               |
| 3.0313 | 895000  | 0.0155        | -               |
| 3.0347 | 896000  | 0.0132        | -               |
| 3.0381 | 897000  | 0.0155        | -               |
| 3.0415 | 898000  | 0.014         | -               |
| 3.0449 | 899000  | 0.0145        | -               |
| 3.0483 | 900000  | 0.0151        | -               |
| 3.0517 | 901000  | 0.0145        | -               |
| 3.0551 | 902000  | 0.0161        | -               |
| 3.0584 | 903000  | 0.0149        | -               |
| 3.0618 | 904000  | 0.0151        | -               |
| 3.0652 | 905000  | 0.0145        | -               |
| 3.0686 | 906000  | 0.0146        | -               |
| 3.0720 | 907000  | 0.0154        | -               |
| 3.0754 | 908000  | 0.015         | -               |
| 3.0788 | 909000  | 0.0154        | -               |
| 3.0822 | 910000  | 0.0163        | -               |
| 3.0855 | 911000  | 0.0154        | -               |
| 3.0889 | 912000  | 0.0158        | -               |
| 3.0923 | 913000  | 0.0127        | -               |
| 3.0957 | 914000  | 0.0146        | -               |
| 3.0991 | 915000  | 0.0146        | -               |
| 3.1025 | 916000  | 0.0143        | -               |
| 3.1059 | 917000  | 0.0134        | -               |
| 3.1093 | 918000  | 0.0143        | -               |
| 3.1126 | 919000  | 0.017         | -               |
| 3.1160 | 920000  | 0.0152        | -               |
| 3.1194 | 921000  | 0.0153        | -               |
| 3.1228 | 922000  | 0.0153        | -               |
| 3.1262 | 923000  | 0.0137        | -               |
| 3.1296 | 924000  | 0.0144        | -               |
| 3.1330 | 925000  | 0.0143        | -               |
| 3.1363 | 926000  | 0.0146        | -               |
| 3.1397 | 927000  | 0.0146        | -               |
| 3.1431 | 928000  | 0.0154        | -               |
| 3.1465 | 929000  | 0.0145        | -               |
| 3.1499 | 930000  | 0.0138        | -               |
| 3.1533 | 931000  | 0.0113        | -               |
| 3.1567 | 932000  | 0.0152        | -               |
| 3.1601 | 933000  | 0.0151        | -               |
| 3.1634 | 934000  | 0.0141        | -               |
| 3.1668 | 935000  | 0.0128        | -               |
| 3.1702 | 936000  | 0.0138        | -               |
| 3.1736 | 937000  | 0.0137        | -               |
| 3.1770 | 938000  | 0.0141        | -               |
| 3.1804 | 939000  | 0.0137        | -               |
| 3.1838 | 940000  | 0.0169        | -               |
| 3.1872 | 941000  | 0.0125        | -               |
| 3.1905 | 942000  | 0.0146        | -               |
| 3.1939 | 943000  | 0.0137        | -               |
| 3.1973 | 944000  | 0.0153        | -               |
| 3.2007 | 945000  | 0.0165        | -               |
| 3.2041 | 946000  | 0.014         | -               |
| 3.2075 | 947000  | 0.0135        | -               |
| 3.2109 | 948000  | 0.0162        | -               |
| 3.2142 | 949000  | 0.0138        | -               |
| 3.2176 | 950000  | 0.0131        | -               |
| 3.2210 | 951000  | 0.0147        | -               |
| 3.2244 | 952000  | 0.0148        | -               |
| 3.2278 | 953000  | 0.0151        | -               |
| 3.2312 | 954000  | 0.0139        | -               |
| 3.2346 | 955000  | 0.0173        | -               |
| 3.2380 | 956000  | 0.0153        | -               |
| 3.2413 | 957000  | 0.013         | -               |
| 3.2447 | 958000  | 0.0158        | -               |
| 3.2481 | 959000  | 0.0139        | -               |
| 3.2515 | 960000  | 0.0123        | -               |
| 3.2549 | 961000  | 0.0147        | -               |
| 3.2583 | 962000  | 0.0146        | -               |
| 3.2617 | 963000  | 0.015         | -               |
| 3.2651 | 964000  | 0.0148        | -               |
| 3.2684 | 965000  | 0.0126        | -               |
| 3.2718 | 966000  | 0.0124        | -               |
| 3.2752 | 967000  | 0.0131        | -               |
| 3.2786 | 968000  | 0.0122        | -               |
| 3.2820 | 969000  | 0.0131        | -               |
| 3.2854 | 970000  | 0.0126        | -               |
| 3.2888 | 971000  | 0.0133        | -               |
| 3.2921 | 972000  | 0.0128        | -               |
| 3.2955 | 973000  | 0.0125        | -               |
| 3.2989 | 974000  | 0.0153        | -               |
| 3.3023 | 975000  | 0.0139        | -               |
| 3.3057 | 976000  | 0.0131        | -               |
| 3.3091 | 977000  | 0.0147        | -               |
| 3.3125 | 978000  | 0.0126        | -               |
| 3.3159 | 979000  | 0.0129        | -               |
| 3.3192 | 980000  | 0.0139        | -               |
| 3.3226 | 981000  | 0.0142        | -               |
| 3.3260 | 982000  | 0.0148        | -               |
| 3.3294 | 983000  | 0.0129        | -               |
| 3.3328 | 984000  | 0.0137        | -               |
| 3.3362 | 985000  | 0.0146        | -               |
| 3.3396 | 986000  | 0.0141        | -               |
| 3.3430 | 987000  | 0.0128        | -               |
| 3.3463 | 988000  | 0.0148        | -               |
| 3.3497 | 989000  | 0.012         | -               |
| 3.3531 | 990000  | 0.0131        | -               |
| 3.3565 | 991000  | 0.0156        | -               |
| 3.3599 | 992000  | 0.0141        | -               |
| 3.3633 | 993000  | 0.013         | -               |
| 3.3667 | 994000  | 0.0148        | -               |
| 3.3700 | 995000  | 0.0134        | -               |
| 3.3734 | 996000  | 0.0123        | -               |
| 3.3768 | 997000  | 0.0138        | -               |
| 3.3802 | 998000  | 0.0133        | -               |
| 3.3836 | 999000  | 0.0139        | -               |
| 3.3870 | 1000000 | 0.0124        | -               |
| 3.3904 | 1001000 | 0.0135        | -               |
| 3.3938 | 1002000 | 0.0133        | -               |
| 3.3971 | 1003000 | 0.0143        | -               |
| 3.4005 | 1004000 | 0.0145        | -               |
| 3.4039 | 1005000 | 0.0147        | -               |
| 3.4073 | 1006000 | 0.0132        | -               |
| 3.4107 | 1007000 | 0.0133        | -               |
| 3.4141 | 1008000 | 0.0138        | -               |
| 3.4175 | 1009000 | 0.0148        | -               |
| 3.4209 | 1010000 | 0.015         | -               |
| 3.4242 | 1011000 | 0.0132        | -               |
| 3.4276 | 1012000 | 0.0141        | -               |
| 3.4310 | 1013000 | 0.013         | -               |
| 3.4344 | 1014000 | 0.0152        | -               |
| 3.4378 | 1015000 | 0.0137        | -               |
| 3.4412 | 1016000 | 0.0127        | -               |
| 3.4446 | 1017000 | 0.0127        | -               |
| 3.4479 | 1018000 | 0.0112        | -               |
| 3.4513 | 1019000 | 0.0151        | -               |
| 3.4547 | 1020000 | 0.0122        | -               |
| 3.4581 | 1021000 | 0.0134        | -               |
| 3.4615 | 1022000 | 0.0131        | -               |
| 3.4649 | 1023000 | 0.0144        | -               |
| 3.4683 | 1024000 | 0.0148        | -               |
| 3.4717 | 1025000 | 0.0119        | -               |
| 3.4750 | 1026000 | 0.0131        | -               |
| 3.4784 | 1027000 | 0.0145        | -               |
| 3.4818 | 1028000 | 0.0142        | -               |
| 3.4852 | 1029000 | 0.0136        | -               |
| 3.4886 | 1030000 | 0.0126        | -               |
| 3.4920 | 1031000 | 0.0135        | -               |
| 3.4954 | 1032000 | 0.0134        | -               |
| 3.4988 | 1033000 | 0.0138        | -               |
| 3.5021 | 1034000 | 0.0134        | -               |
| 3.5055 | 1035000 | 0.0137        | -               |
| 3.5089 | 1036000 | 0.0138        | -               |
| 3.5123 | 1037000 | 0.0153        | -               |
| 3.5157 | 1038000 | 0.014         | -               |
| 3.5191 | 1039000 | 0.0134        | -               |
| 3.5225 | 1040000 | 0.0116        | -               |
| 3.5258 | 1041000 | 0.0126        | -               |
| 3.5292 | 1042000 | 0.0136        | -               |
| 3.5326 | 1043000 | 0.0141        | -               |
| 3.5360 | 1044000 | 0.0133        | -               |
| 3.5394 | 1045000 | 0.0129        | -               |
| 3.5428 | 1046000 | 0.0132        | -               |
| 3.5462 | 1047000 | 0.0143        | -               |
| 3.5496 | 1048000 | 0.0118        | -               |
| 3.5529 | 1049000 | 0.0119        | -               |
| 3.5563 | 1050000 | 0.0146        | -               |
| 3.5597 | 1051000 | 0.0129        | -               |
| 3.5631 | 1052000 | 0.0144        | -               |
| 3.5665 | 1053000 | 0.0139        | -               |
| 3.5699 | 1054000 | 0.0131        | -               |
| 3.5733 | 1055000 | 0.0119        | -               |
| 3.5767 | 1056000 | 0.0118        | -               |
| 3.5800 | 1057000 | 0.0143        | -               |
| 3.5834 | 1058000 | 0.0144        | -               |
| 3.5868 | 1059000 | 0.013         | -               |
| 3.5902 | 1060000 | 0.0131        | -               |
| 3.5936 | 1061000 | 0.0141        | -               |
| 3.5970 | 1062000 | 0.0134        | -               |
| 3.6004 | 1063000 | 0.0133        | -               |
| 3.6038 | 1064000 | 0.0135        | -               |
| 3.6071 | 1065000 | 0.0128        | -               |
| 3.6105 | 1066000 | 0.0154        | -               |
| 3.6139 | 1067000 | 0.0141        | -               |
| 3.6173 | 1068000 | 0.0138        | -               |
| 3.6207 | 1069000 | 0.0126        | -               |
| 3.6241 | 1070000 | 0.0133        | -               |
| 3.6275 | 1071000 | 0.0144        | -               |
| 3.6308 | 1072000 | 0.0148        | -               |
| 3.6342 | 1073000 | 0.0138        | -               |
| 3.6376 | 1074000 | 0.0131        | -               |
| 3.6410 | 1075000 | 0.0153        | -               |
| 3.6444 | 1076000 | 0.014         | -               |
| 3.6478 | 1077000 | 0.0127        | -               |
| 3.6512 | 1078000 | 0.0115        | -               |
| 3.6546 | 1079000 | 0.0127        | -               |
| 3.6579 | 1080000 | 0.0145        | -               |
| 3.6613 | 1081000 | 0.0148        | -               |
| 3.6647 | 1082000 | 0.0113        | -               |
| 3.6681 | 1083000 | 0.0149        | -               |
| 3.6715 | 1084000 | 0.013         | -               |
| 3.6749 | 1085000 | 0.0135        | -               |
| 3.6783 | 1086000 | 0.0129        | -               |
| 3.6817 | 1087000 | 0.014         | -               |
| 3.6850 | 1088000 | 0.013         | -               |
| 3.6884 | 1089000 | 0.0138        | -               |
| 3.6918 | 1090000 | 0.0124        | -               |
| 3.6952 | 1091000 | 0.0138        | -               |
| 3.6986 | 1092000 | 0.0156        | -               |
| 3.7020 | 1093000 | 0.0133        | -               |
| 3.7054 | 1094000 | 0.0123        | -               |
| 3.7087 | 1095000 | 0.012         | -               |
| 3.7121 | 1096000 | 0.0135        | -               |
| 3.7155 | 1097000 | 0.0143        | -               |
| 3.7189 | 1098000 | 0.0145        | -               |
| 3.7223 | 1099000 | 0.0127        | -               |
| 3.7257 | 1100000 | 0.0128        | -               |
| 3.7291 | 1101000 | 0.0124        | -               |
| 3.7325 | 1102000 | 0.0116        | -               |
| 3.7358 | 1103000 | 0.013         | -               |
| 3.7392 | 1104000 | 0.0123        | -               |
| 3.7426 | 1105000 | 0.0131        | -               |
| 3.7460 | 1106000 | 0.0127        | -               |
| 3.7494 | 1107000 | 0.0128        | -               |
| 3.7528 | 1108000 | 0.0125        | -               |
| 3.7562 | 1109000 | 0.0129        | -               |
| 3.7596 | 1110000 | 0.0121        | -               |
| 3.7629 | 1111000 | 0.0134        | -               |
| 3.7663 | 1112000 | 0.0139        | -               |
| 3.7697 | 1113000 | 0.0124        | -               |
| 3.7731 | 1114000 | 0.014         | -               |
| 3.7765 | 1115000 | 0.0134        | -               |
| 3.7799 | 1116000 | 0.0125        | -               |
| 3.7833 | 1117000 | 0.0134        | -               |
| 3.7866 | 1118000 | 0.0127        | -               |
| 3.7900 | 1119000 | 0.0136        | -               |
| 3.7934 | 1120000 | 0.0138        | -               |
| 3.7968 | 1121000 | 0.0133        | -               |
| 3.8002 | 1122000 | 0.0134        | -               |
| 3.8036 | 1123000 | 0.0134        | -               |
| 3.8070 | 1124000 | 0.0123        | -               |
| 3.8104 | 1125000 | 0.0129        | -               |
| 3.8137 | 1126000 | 0.0131        | -               |
| 3.8171 | 1127000 | 0.0118        | -               |
| 3.8205 | 1128000 | 0.013         | -               |
| 3.8239 | 1129000 | 0.0149        | -               |
| 3.8273 | 1130000 | 0.0134        | -               |
| 3.8307 | 1131000 | 0.0124        | -               |
| 3.8341 | 1132000 | 0.0134        | -               |
| 3.8375 | 1133000 | 0.0115        | -               |
| 3.8408 | 1134000 | 0.0133        | -               |
| 3.8442 | 1135000 | 0.0114        | -               |
| 3.8476 | 1136000 | 0.0139        | -               |
| 3.8510 | 1137000 | 0.0132        | -               |
| 3.8544 | 1138000 | 0.014         | -               |
| 3.8578 | 1139000 | 0.0121        | -               |
| 3.8612 | 1140000 | 0.012         | -               |
| 3.8645 | 1141000 | 0.013         | -               |
| 3.8679 | 1142000 | 0.0116        | -               |
| 3.8713 | 1143000 | 0.0145        | -               |
| 3.8747 | 1144000 | 0.0133        | -               |
| 3.8781 | 1145000 | 0.0141        | -               |
| 3.8815 | 1146000 | 0.0121        | -               |
| 3.8849 | 1147000 | 0.0141        | -               |
| 3.8883 | 1148000 | 0.0125        | -               |
| 3.8916 | 1149000 | 0.0132        | -               |
| 3.8950 | 1150000 | 0.013         | -               |
| 3.8984 | 1151000 | 0.0117        | -               |
| 3.9018 | 1152000 | 0.0139        | -               |
| 3.9052 | 1153000 | 0.0123        | -               |
| 3.9086 | 1154000 | 0.0124        | -               |
| 3.9120 | 1155000 | 0.0118        | -               |
| 3.9154 | 1156000 | 0.0118        | -               |
| 3.9187 | 1157000 | 0.0148        | -               |
| 3.9221 | 1158000 | 0.0127        | -               |
| 3.9255 | 1159000 | 0.0128        | -               |
| 3.9289 | 1160000 | 0.0125        | -               |
| 3.9323 | 1161000 | 0.0127        | -               |
| 3.9357 | 1162000 | 0.0118        | -               |
| 3.9391 | 1163000 | 0.0115        | -               |
| 3.9424 | 1164000 | 0.0115        | -               |
| 3.9458 | 1165000 | 0.0128        | -               |
| 3.9492 | 1166000 | 0.0112        | -               |
| 3.9526 | 1167000 | 0.0134        | -               |
| 3.9560 | 1168000 | 0.0124        | -               |
| 3.9594 | 1169000 | 0.0131        | -               |
| 3.9628 | 1170000 | 0.0119        | -               |
| 3.9662 | 1171000 | 0.0124        | -               |
| 3.9695 | 1172000 | 0.0119        | -               |
| 3.9729 | 1173000 | 0.014         | -               |
| 3.9763 | 1174000 | 0.0112        | -               |
| 3.9797 | 1175000 | 0.0133        | -               |
| 3.9831 | 1176000 | 0.0129        | -               |
| 3.9865 | 1177000 | 0.0128        | -               |
| 3.9899 | 1178000 | 0.0122        | -               |
| 3.9933 | 1179000 | 0.0142        | -               |
| 3.9966 | 1180000 | 0.0129        | -               |
| 4.0000 | 1180988 | -             | 0.0000          |

</details>

### Framework Versions
- Python: 3.11.11
- Sentence Transformers: 3.4.1
- Transformers: 4.48.2
- PyTorch: 2.6.0+cu124
- Accelerate: 1.5.2
- Datasets: 3.2.0
- Tokenizers: 0.21.0

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