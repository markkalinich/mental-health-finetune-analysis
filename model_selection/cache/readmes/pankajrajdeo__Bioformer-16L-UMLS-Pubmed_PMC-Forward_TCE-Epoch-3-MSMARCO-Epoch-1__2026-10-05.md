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

This is a [sentence-transformers](https://www.SBERT.net) model trained on the parquet dataset. It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
- **Maximum Sequence Length:** 1024 tokens
- **Output Dimensionality:** 384 dimensions
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
  (0): Transformer({'max_seq_length': 1024, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': True, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("pankajrajdeo/Bioformer-16L-UMLS-Pubmed_PMC-Forward_TCE-Epoch-3-MSMARCO-Epoch-1")
# Run inference
sentences = [
    'does the columbus zoo sell beer',
    'No glass and/or alcohol are permitted at the Columbus Zoo. This means that they do not sell alcoholic beverages.',
    'Eviction law allows landlords to still ask you to move out, but you must be afforded some extra protections. First, for eviction notices without cause, the landlord must give you a longer period of notice to vacate, generally 30 or 60 days. This lengthened time period is designed to allow you to find another place to live.',
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

| Epoch  | Step   | Training Loss | Validation Loss |
|:------:|:------:|:-------------:|:---------------:|
| 0.0000 | 1      | 0.739         | -               |
| 0.0034 | 1000   | 0.3494        | -               |
| 0.0068 | 2000   | 0.2813        | -               |
| 0.0102 | 3000   | 0.22          | -               |
| 0.0135 | 4000   | 0.1988        | -               |
| 0.0169 | 5000   | 0.1842        | -               |
| 0.0203 | 6000   | 0.1848        | -               |
| 0.0237 | 7000   | 0.1719        | -               |
| 0.0271 | 8000   | 0.1778        | -               |
| 0.0305 | 9000   | 0.1742        | -               |
| 0.0339 | 10000  | 0.1414        | -               |
| 0.0373 | 11000  | 0.1648        | -               |
| 0.0406 | 12000  | 0.1479        | -               |
| 0.0440 | 13000  | 0.1383        | -               |
| 0.0474 | 14000  | 0.1361        | -               |
| 0.0508 | 15000  | 0.1337        | -               |
| 0.0542 | 16000  | 0.1355        | -               |
| 0.0576 | 17000  | 0.1345        | -               |
| 0.0610 | 18000  | 0.1253        | -               |
| 0.0644 | 19000  | 0.1211        | -               |
| 0.0677 | 20000  | 0.1161        | -               |
| 0.0711 | 21000  | 0.1223        | -               |
| 0.0745 | 22000  | 0.1169        | -               |
| 0.0779 | 23000  | 0.1137        | -               |
| 0.0813 | 24000  | 0.1273        | -               |
| 0.0847 | 25000  | 0.1229        | -               |
| 0.0881 | 26000  | 0.1159        | -               |
| 0.0914 | 27000  | 0.0974        | -               |
| 0.0948 | 28000  | 0.0976        | -               |
| 0.0982 | 29000  | 0.1079        | -               |
| 0.1016 | 30000  | 0.105         | -               |
| 0.1050 | 31000  | 0.0977        | -               |
| 0.1084 | 32000  | 0.0941        | -               |
| 0.1118 | 33000  | 0.1124        | -               |
| 0.1152 | 34000  | 0.0994        | -               |
| 0.1185 | 35000  | 0.0979        | -               |
| 0.1219 | 36000  | 0.1038        | -               |
| 0.1253 | 37000  | 0.0877        | -               |
| 0.1287 | 38000  | 0.0862        | -               |
| 0.1321 | 39000  | 0.0928        | -               |
| 0.1355 | 40000  | 0.0907        | -               |
| 0.1389 | 41000  | 0.0942        | -               |
| 0.1423 | 42000  | 0.0878        | -               |
| 0.1456 | 43000  | 0.088         | -               |
| 0.1490 | 44000  | 0.0851        | -               |
| 0.1524 | 45000  | 0.0742        | -               |
| 0.1558 | 46000  | 0.0856        | -               |
| 0.1592 | 47000  | 0.0804        | -               |
| 0.1626 | 48000  | 0.081         | -               |
| 0.1660 | 49000  | 0.0622        | -               |
| 0.1693 | 50000  | 0.087         | -               |
| 0.1727 | 51000  | 0.0785        | -               |
| 0.1761 | 52000  | 0.0803        | -               |
| 0.1795 | 53000  | 0.0709        | -               |
| 0.1829 | 54000  | 0.0871        | -               |
| 0.1863 | 55000  | 0.0728        | -               |
| 0.1897 | 56000  | 0.0799        | -               |
| 0.1931 | 57000  | 0.0703        | -               |
| 0.1964 | 58000  | 0.0765        | -               |
| 0.1998 | 59000  | 0.0814        | -               |
| 0.2032 | 60000  | 0.0745        | -               |
| 0.2066 | 61000  | 0.0712        | -               |
| 0.2100 | 62000  | 0.0746        | -               |
| 0.2134 | 63000  | 0.0723        | -               |
| 0.2168 | 64000  | 0.0578        | -               |
| 0.2202 | 65000  | 0.0809        | -               |
| 0.2235 | 66000  | 0.0745        | -               |
| 0.2269 | 67000  | 0.0709        | -               |
| 0.2303 | 68000  | 0.0697        | -               |
| 0.2337 | 69000  | 0.0807        | -               |
| 0.2371 | 70000  | 0.0725        | -               |
| 0.2405 | 71000  | 0.0696        | -               |
| 0.2439 | 72000  | 0.0677        | -               |
| 0.2472 | 73000  | 0.0649        | -               |
| 0.2506 | 74000  | 0.0594        | -               |
| 0.2540 | 75000  | 0.0661        | -               |
| 0.2574 | 76000  | 0.0688        | -               |
| 0.2608 | 77000  | 0.0629        | -               |
| 0.2642 | 78000  | 0.0671        | -               |
| 0.2676 | 79000  | 0.0569        | -               |
| 0.2710 | 80000  | 0.0551        | -               |
| 0.2743 | 81000  | 0.0588        | -               |
| 0.2777 | 82000  | 0.0566        | -               |
| 0.2811 | 83000  | 0.0554        | -               |
| 0.2845 | 84000  | 0.0557        | -               |
| 0.2879 | 85000  | 0.0543        | -               |
| 0.2913 | 86000  | 0.0594        | -               |
| 0.2947 | 87000  | 0.0506        | -               |
| 0.2981 | 88000  | 0.0643        | -               |
| 0.3014 | 89000  | 0.0582        | -               |
| 0.3048 | 90000  | 0.0558        | -               |
| 0.3082 | 91000  | 0.0615        | -               |
| 0.3116 | 92000  | 0.0555        | -               |
| 0.3150 | 93000  | 0.0537        | -               |
| 0.3184 | 94000  | 0.0606        | -               |
| 0.3218 | 95000  | 0.059         | -               |
| 0.3252 | 96000  | 0.0599        | -               |
| 0.3285 | 97000  | 0.0525        | -               |
| 0.3319 | 98000  | 0.0595        | -               |
| 0.3353 | 99000  | 0.0514        | -               |
| 0.3387 | 100000 | 0.055         | -               |
| 0.3421 | 101000 | 0.0551        | -               |
| 0.3455 | 102000 | 0.0586        | -               |
| 0.3489 | 103000 | 0.0507        | -               |
| 0.3522 | 104000 | 0.0494        | -               |
| 0.3556 | 105000 | 0.0546        | -               |
| 0.3590 | 106000 | 0.0572        | -               |
| 0.3624 | 107000 | 0.0594        | -               |
| 0.3658 | 108000 | 0.0553        | -               |
| 0.3692 | 109000 | 0.0533        | -               |
| 0.3726 | 110000 | 0.0489        | -               |
| 0.3760 | 111000 | 0.0512        | -               |
| 0.3793 | 112000 | 0.0516        | -               |
| 0.3827 | 113000 | 0.0538        | -               |
| 0.3861 | 114000 | 0.0459        | -               |
| 0.3895 | 115000 | 0.0523        | -               |
| 0.3929 | 116000 | 0.0464        | -               |
| 0.3963 | 117000 | 0.0546        | -               |
| 0.3997 | 118000 | 0.0552        | -               |
| 0.4031 | 119000 | 0.0546        | -               |
| 0.4064 | 120000 | 0.05          | -               |
| 0.4098 | 121000 | 0.0469        | -               |
| 0.4132 | 122000 | 0.0485        | -               |
| 0.4166 | 123000 | 0.0534        | -               |
| 0.4200 | 124000 | 0.0525        | -               |
| 0.4234 | 125000 | 0.0493        | -               |
| 0.4268 | 126000 | 0.0453        | -               |
| 0.4301 | 127000 | 0.0491        | -               |
| 0.4335 | 128000 | 0.0535        | -               |
| 0.4369 | 129000 | 0.0512        | -               |
| 0.4403 | 130000 | 0.0447        | -               |
| 0.4437 | 131000 | 0.0484        | -               |
| 0.4471 | 132000 | 0.0407        | -               |
| 0.4505 | 133000 | 0.0466        | -               |
| 0.4539 | 134000 | 0.0414        | -               |
| 0.4572 | 135000 | 0.0483        | -               |
| 0.4606 | 136000 | 0.0465        | -               |
| 0.4640 | 137000 | 0.0493        | -               |
| 0.4674 | 138000 | 0.0535        | -               |
| 0.4708 | 139000 | 0.0422        | -               |
| 0.4742 | 140000 | 0.047         | -               |
| 0.4776 | 141000 | 0.0469        | -               |
| 0.4810 | 142000 | 0.0498        | -               |
| 0.4843 | 143000 | 0.0448        | -               |
| 0.4877 | 144000 | 0.0407        | -               |
| 0.4911 | 145000 | 0.0445        | -               |
| 0.4945 | 146000 | 0.0455        | -               |
| 0.4979 | 147000 | 0.0495        | -               |
| 0.5013 | 148000 | 0.0452        | -               |
| 0.5047 | 149000 | 0.0442        | -               |
| 0.5080 | 150000 | 0.0443        | -               |
| 0.5114 | 151000 | 0.05          | -               |
| 0.5148 | 152000 | 0.0477        | -               |
| 0.5182 | 153000 | 0.0441        | -               |
| 0.5216 | 154000 | 0.0388        | -               |
| 0.5250 | 155000 | 0.0432        | -               |
| 0.5284 | 156000 | 0.0413        | -               |
| 0.5318 | 157000 | 0.0459        | -               |
| 0.5351 | 158000 | 0.0401        | -               |
| 0.5385 | 159000 | 0.0426        | -               |
| 0.5419 | 160000 | 0.0398        | -               |
| 0.5453 | 161000 | 0.0441        | -               |
| 0.5487 | 162000 | 0.0408        | -               |
| 0.5521 | 163000 | 0.0384        | -               |
| 0.5555 | 164000 | 0.042         | -               |
| 0.5589 | 165000 | 0.0406        | -               |
| 0.5622 | 166000 | 0.0406        | -               |
| 0.5656 | 167000 | 0.0475        | -               |
| 0.5690 | 168000 | 0.0407        | -               |
| 0.5724 | 169000 | 0.0384        | -               |
| 0.5758 | 170000 | 0.0379        | -               |
| 0.5792 | 171000 | 0.0413        | -               |
| 0.5826 | 172000 | 0.0456        | -               |
| 0.5859 | 173000 | 0.0408        | -               |
| 0.5893 | 174000 | 0.0369        | -               |
| 0.5927 | 175000 | 0.0419        | -               |
| 0.5961 | 176000 | 0.0394        | -               |
| 0.5995 | 177000 | 0.0426        | -               |
| 0.6029 | 178000 | 0.0425        | -               |
| 0.6063 | 179000 | 0.0368        | -               |
| 0.6097 | 180000 | 0.0498        | -               |
| 0.6130 | 181000 | 0.039         | -               |
| 0.6164 | 182000 | 0.0432        | -               |
| 0.6198 | 183000 | 0.0369        | -               |
| 0.6232 | 184000 | 0.0374        | -               |
| 0.6266 | 185000 | 0.0443        | -               |
| 0.6300 | 186000 | 0.0393        | -               |
| 0.6334 | 187000 | 0.0413        | -               |
| 0.6368 | 188000 | 0.0393        | -               |
| 0.6401 | 189000 | 0.0443        | -               |
| 0.6435 | 190000 | 0.0415        | -               |
| 0.6469 | 191000 | 0.037         | -               |
| 0.6503 | 192000 | 0.0322        | -               |
| 0.6537 | 193000 | 0.0403        | -               |
| 0.6571 | 194000 | 0.0405        | -               |
| 0.6605 | 195000 | 0.0441        | -               |
| 0.6638 | 196000 | 0.0356        | -               |
| 0.6672 | 197000 | 0.0406        | -               |
| 0.6706 | 198000 | 0.0393        | -               |
| 0.6740 | 199000 | 0.0384        | -               |
| 0.6774 | 200000 | 0.0377        | -               |
| 0.6808 | 201000 | 0.0388        | -               |
| 0.6842 | 202000 | 0.0346        | -               |
| 0.6876 | 203000 | 0.0418        | -               |
| 0.6909 | 204000 | 0.0349        | -               |
| 0.6943 | 205000 | 0.0365        | -               |
| 0.6977 | 206000 | 0.0425        | -               |
| 0.7011 | 207000 | 0.0386        | -               |
| 0.7045 | 208000 | 0.0336        | -               |
| 0.7079 | 209000 | 0.0317        | -               |
| 0.7113 | 210000 | 0.0377        | -               |
| 0.7147 | 211000 | 0.0376        | -               |
| 0.7180 | 212000 | 0.0393        | -               |
| 0.7214 | 213000 | 0.0368        | -               |
| 0.7248 | 214000 | 0.0364        | -               |
| 0.7282 | 215000 | 0.0319        | -               |
| 0.7316 | 216000 | 0.0332        | -               |
| 0.7350 | 217000 | 0.0341        | -               |
| 0.7384 | 218000 | 0.0337        | -               |
| 0.7417 | 219000 | 0.0372        | -               |
| 0.7451 | 220000 | 0.0352        | -               |
| 0.7485 | 221000 | 0.0347        | -               |
| 0.7519 | 222000 | 0.0343        | -               |
| 0.7553 | 223000 | 0.0362        | -               |
| 0.7587 | 224000 | 0.0315        | -               |
| 0.7621 | 225000 | 0.0361        | -               |
| 0.7655 | 226000 | 0.0394        | -               |
| 0.7688 | 227000 | 0.0297        | -               |
| 0.7722 | 228000 | 0.0379        | -               |
| 0.7756 | 229000 | 0.0377        | -               |
| 0.7790 | 230000 | 0.0303        | -               |
| 0.7824 | 231000 | 0.0361        | -               |
| 0.7858 | 232000 | 0.0338        | -               |
| 0.7892 | 233000 | 0.0345        | -               |
| 0.7926 | 234000 | 0.037         | -               |
| 0.7959 | 235000 | 0.0344        | -               |
| 0.7993 | 236000 | 0.0341        | -               |
| 0.8027 | 237000 | 0.035         | -               |
| 0.8061 | 238000 | 0.0311        | -               |
| 0.8095 | 239000 | 0.0329        | -               |
| 0.8129 | 240000 | 0.0335        | -               |
| 0.8163 | 241000 | 0.0312        | -               |
| 0.8196 | 242000 | 0.0323        | -               |
| 0.8230 | 243000 | 0.0377        | -               |
| 0.8264 | 244000 | 0.0338        | -               |
| 0.8298 | 245000 | 0.0362        | -               |
| 0.8332 | 246000 | 0.0319        | -               |
| 0.8366 | 247000 | 0.0303        | -               |
| 0.8400 | 248000 | 0.0328        | -               |
| 0.8434 | 249000 | 0.0318        | -               |
| 0.8467 | 250000 | 0.0348        | -               |
| 0.8501 | 251000 | 0.0345        | -               |
| 0.8535 | 252000 | 0.0359        | -               |
| 0.8569 | 253000 | 0.0282        | -               |
| 0.8603 | 254000 | 0.0295        | -               |
| 0.8637 | 255000 | 0.0338        | -               |
| 0.8671 | 256000 | 0.028         | -               |
| 0.8705 | 257000 | 0.0367        | -               |
| 0.8738 | 258000 | 0.0327        | -               |
| 0.8772 | 259000 | 0.035         | -               |
| 0.8806 | 260000 | 0.0295        | -               |
| 0.8840 | 261000 | 0.036         | -               |
| 0.8874 | 262000 | 0.0308        | -               |
| 0.8908 | 263000 | 0.0321        | -               |
| 0.8942 | 264000 | 0.0343        | -               |
| 0.8976 | 265000 | 0.0308        | -               |
| 0.9009 | 266000 | 0.0321        | -               |
| 0.9043 | 267000 | 0.0317        | -               |
| 0.9077 | 268000 | 0.0299        | -               |
| 0.9111 | 269000 | 0.029         | -               |
| 0.9145 | 270000 | 0.0308        | -               |
| 0.9179 | 271000 | 0.0343        | -               |
| 0.9213 | 272000 | 0.033         | -               |
| 0.9246 | 273000 | 0.0294        | -               |
| 0.9280 | 274000 | 0.0309        | -               |
| 0.9314 | 275000 | 0.0301        | -               |
| 0.9348 | 276000 | 0.0321        | -               |
| 0.9382 | 277000 | 0.0274        | -               |
| 0.9416 | 278000 | 0.0298        | -               |
| 0.9450 | 279000 | 0.0259        | -               |
| 0.9484 | 280000 | 0.03          | -               |
| 0.9517 | 281000 | 0.0319        | -               |
| 0.9551 | 282000 | 0.032         | -               |
| 0.9585 | 283000 | 0.0319        | -               |
| 0.9619 | 284000 | 0.0309        | -               |
| 0.9653 | 285000 | 0.0284        | -               |
| 0.9687 | 286000 | 0.0286        | -               |
| 0.9721 | 287000 | 0.033         | -               |
| 0.9755 | 288000 | 0.0274        | -               |
| 0.9788 | 289000 | 0.0304        | -               |
| 0.9822 | 290000 | 0.0313        | -               |
| 0.9856 | 291000 | 0.0302        | -               |
| 0.9890 | 292000 | 0.028         | -               |
| 0.9924 | 293000 | 0.0332        | -               |
| 0.9958 | 294000 | 0.0302        | -               |
| 0.9992 | 295000 | 0.0306        | -               |
| 1.0000 | 295247 | -             | 0.0001          |

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