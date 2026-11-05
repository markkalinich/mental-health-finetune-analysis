---
base_model: agentlans/multilingual-e5-small-aligned
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:3000000
- loss:CoSENTLoss
widget:
- source_sentence: Jesus answered them.
  sentences:
  - ישוע ענה להם.
  - आत्ताच नीघ.
  - Мы надеялись, что дождь прекратится до обеда.
- source_sentence: Foreign books are sold at the shop.
  sentences:
  - Tak, det er alt.
  - Корабль бросил якорь.
  - Les livres étrangers sont vendus à la boutique.
- source_sentence: Cats usually hate dogs.
  sentences:
  - Куда вы ходили в прошлое воскресенье?
  - >-
    The bottles of beer that I brought to the party were redundant; the host's
    family owned a brewery.
  - Mir tut der Arm weh.
- source_sentence: How foolish I was not to discover that simple lie!
  sentences:
  - Tenho umas perguntas pra fazer, mas não quero te incomodar.
  - Mi piacciono di più le mele.
  - Quel idiot j'étais de n'avoir pas découvert ce simple mensonge !
- source_sentence: Esta es mi amiga Rachel, fuimos al instituto juntos.
  sentences:
  - Το σχολείο μας έχει εννιά τάξεις.
  - When applying to American universities, your TOEFL score is only one factor.
  - Je n'ai pas encore pris ma décision.
license: mit
---

# SentenceTransformer based on agentlans/multilingual-e5-small-aligned

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [agentlans/multilingual-e5-small-aligned](https://huggingface.co/agentlans/multilingual-e5-small-aligned). It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

- One of the smallest multilingual embedding models on Huggingface
- This model is aligned which means translations have similar embeddings compared to unrelated sentences
- Finetuned on 1,000,000 randomly selected sentence pairs downloaded from Tatoeba 2024-09-26
  - Includes pairs where one or both sentences are non-English
  - For each pair, two negative examples were generated

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [agentlans/multilingual-e5-small-aligned](https://huggingface.co/agentlans/multilingual-e5-small-aligned) <!-- at revision 2876d21d801703ad25135704219f92d970e48971 -->
- **Maximum Sequence Length:** 512 tokens
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
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
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
model = SentenceTransformer("agentlans/multilingual-e5-small-aligned-v2")
# Run inference
sentences = [
    'Esta es mi amiga Rachel, fuimos al instituto juntos.',
    "Je n'ai pas encore pris ma décision.",
    'When applying to American universities, your TOEFL score is only one factor.',
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


* Size: 3,000,000 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                        | sentence_1                                                                        | label                                                          |
  |:--------|:----------------------------------------------------------------------------------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                            | string                                                                            | float                                                          |
  | details | <ul><li>min: 5 tokens</li><li>mean: 11.16 tokens</li><li>max: 55 tokens</li></ul> | <ul><li>min: 5 tokens</li><li>mean: 12.27 tokens</li><li>max: 76 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.33</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                | sentence_1                               | label            |
  |:------------------------------------------|:-----------------------------------------|:-----------------|
  | <code>Bring your friends with you.</code> | <code>Traga seus amigos com você.</code> | <code>1.0</code> |
  | <code>I've been there already.</code>     | <code>Você tem algo mais barato?</code>  | <code>0.0</code> |
  | <code>All my homework is done.</code>     | <code>माझा सगळा होमवर्क झाला आहे.</code> | <code>1.0</code> |
* Loss: [<code>CoSENTLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cosentloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "pairwise_cos_sim"
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
- `hub_private_repo`: False
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
- `multi_dataset_batch_sampler`: round_robin

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step   | Training Loss |
|:------:|:------:|:-------------:|
| 0.0053 | 500    | 0.835         |
| 0.0107 | 1000   | 0.7012        |
| 0.016  | 1500   | 0.6765        |
| 0.0213 | 2000   | 0.4654        |
| 0.0267 | 2500   | 0.7546        |
| 0.032  | 3000   | 0.6098        |
| 0.0373 | 3500   | 0.644         |
| 0.0427 | 4000   | 0.5318        |
| 0.048  | 4500   | 0.5638        |
| 0.0533 | 5000   | 0.5556        |
| 0.0587 | 5500   | 0.5165        |
| 0.064  | 6000   | 0.4083        |
| 0.0693 | 6500   | 0.4683        |
| 0.0747 | 7000   | 0.5414        |
| 0.08   | 7500   | 0.4678        |
| 0.0853 | 8000   | 0.4225        |
| 0.0907 | 8500   | 0.4552        |
| 0.096  | 9000   | 0.4551        |
| 0.1013 | 9500   | 0.4347        |
| 0.1067 | 10000  | 0.292         |
| 0.112  | 10500  | 0.4677        |
| 0.1173 | 11000  | 0.3567        |
| 0.1227 | 11500  | 0.4663        |
| 0.128  | 12000  | 0.4333        |
| 0.1333 | 12500  | 0.375         |
| 0.1387 | 13000  | 0.4183        |
| 0.144  | 13500  | 0.5745        |
| 0.1493 | 14000  | 0.4569        |
| 0.1547 | 14500  | 0.426         |
| 0.16   | 15000  | 0.4903        |
| 0.1653 | 15500  | 0.4287        |
| 0.1707 | 16000  | 0.4375        |
| 0.176  | 16500  | 0.377         |
| 0.1813 | 17000  | 0.3848        |
| 0.1867 | 17500  | 0.3366        |
| 0.192  | 18000  | 0.3784        |
| 0.1973 | 18500  | 0.399         |
| 0.2027 | 19000  | 0.3798        |
| 0.208  | 19500  | 0.3275        |
| 0.2133 | 20000  | 0.3594        |
| 0.2187 | 20500  | 0.3555        |
| 0.224  | 21000  | 0.3565        |
| 0.2293 | 21500  | 0.4264        |
| 0.2347 | 22000  | 0.4138        |
| 0.24   | 22500  | 0.3149        |
| 0.2453 | 23000  | 0.3397        |
| 0.2507 | 23500  | 0.359         |
| 0.256  | 24000  | 0.3311        |
| 0.2613 | 24500  | 0.3632        |
| 0.2667 | 25000  | 0.366         |
| 0.272  | 25500  | 0.2899        |
| 0.2773 | 26000  | 0.2611        |
| 0.2827 | 26500  | 0.3497        |
| 0.288  | 27000  | 0.3534        |
| 0.2933 | 27500  | 0.273         |
| 0.2987 | 28000  | 0.3199        |
| 0.304  | 28500  | 0.2527        |
| 0.3093 | 29000  | 0.2755        |
| 0.3147 | 29500  | 0.3684        |
| 0.32   | 30000  | 0.347         |
| 0.3253 | 30500  | 0.2537        |
| 0.3307 | 31000  | 0.3665        |
| 0.336  | 31500  | 0.2512        |
| 0.3413 | 32000  | 0.2913        |
| 0.3467 | 32500  | 0.2619        |
| 0.352  | 33000  | 0.2573        |
| 0.3573 | 33500  | 0.3036        |
| 0.3627 | 34000  | 0.3388        |
| 0.368  | 34500  | 0.2384        |
| 0.3733 | 35000  | 0.31          |
| 0.3787 | 35500  | 0.3461        |
| 0.384  | 36000  | 0.378         |
| 0.3893 | 36500  | 0.2409        |
| 0.3947 | 37000  | 0.2969        |
| 0.4    | 37500  | 0.2881        |
| 0.4053 | 38000  | 0.3612        |
| 0.4107 | 38500  | 0.2662        |
| 0.416  | 39000  | 0.2796        |
| 0.4213 | 39500  | 0.3298        |
| 0.4267 | 40000  | 0.2828        |
| 0.432  | 40500  | 0.2367        |
| 0.4373 | 41000  | 0.2661        |
| 0.4427 | 41500  | 0.393         |
| 0.448  | 42000  | 0.2875        |
| 0.4533 | 42500  | 0.203         |
| 0.4587 | 43000  | 0.3211        |
| 0.464  | 43500  | 0.3404        |
| 0.4693 | 44000  | 0.315         |
| 0.4747 | 44500  | 0.3018        |
| 0.48   | 45000  | 0.2491        |
| 0.4853 | 45500  | 0.2584        |
| 0.4907 | 46000  | 0.2583        |
| 0.496  | 46500  | 0.3447        |
| 0.5013 | 47000  | 0.4332        |
| 0.5067 | 47500  | 0.297         |
| 0.512  | 48000  | 0.2697        |
| 0.5173 | 48500  | 0.2349        |
| 0.5227 | 49000  | 0.2176        |
| 0.528  | 49500  | 0.2775        |
| 0.5333 | 50000  | 0.2508        |
| 0.5387 | 50500  | 0.291         |
| 0.544  | 51000  | 0.2672        |
| 0.5493 | 51500  | 0.2638        |
| 0.5547 | 52000  | 0.2877        |
| 0.56   | 52500  | 0.2758        |
| 0.5653 | 53000  | 0.264         |
| 0.5707 | 53500  | 0.2372        |
| 0.576  | 54000  | 0.3384        |
| 0.5813 | 54500  | 0.2459        |
| 0.5867 | 55000  | 0.3047        |
| 0.592  | 55500  | 0.1926        |
| 0.5973 | 56000  | 0.2573        |
| 0.6027 | 56500  | 0.2816        |
| 0.608  | 57000  | 0.285         |
| 0.6133 | 57500  | 0.2397        |
| 0.6187 | 58000  | 0.1935        |
| 0.624  | 58500  | 0.3281        |
| 0.6293 | 59000  | 0.3306        |
| 0.6347 | 59500  | 0.2067        |
| 0.64   | 60000  | 0.2483        |
| 0.6453 | 60500  | 0.2719        |
| 0.6507 | 61000  | 0.2585        |
| 0.656  | 61500  | 0.2385        |
| 0.6613 | 62000  | 0.2229        |
| 0.6667 | 62500  | 0.2311        |
| 0.672  | 63000  | 0.2664        |
| 0.6773 | 63500  | 0.209         |
| 0.6827 | 64000  | 0.2643        |
| 0.688  | 64500  | 0.2108        |
| 0.6933 | 65000  | 0.3063        |
| 0.6987 | 65500  | 0.1802        |
| 0.704  | 66000  | 0.2285        |
| 0.7093 | 66500  | 0.2065        |
| 0.7147 | 67000  | 0.2467        |
| 0.72   | 67500  | 0.2178        |
| 0.7253 | 68000  | 0.2217        |
| 0.7307 | 68500  | 0.2549        |
| 0.736  | 69000  | 0.2026        |
| 0.7413 | 69500  | 0.2609        |
| 0.7467 | 70000  | 0.2393        |
| 0.752  | 70500  | 0.1958        |
| 0.7573 | 71000  | 0.2214        |
| 0.7627 | 71500  | 0.2079        |
| 0.768  | 72000  | 0.1574        |
| 0.7733 | 72500  | 0.2356        |
| 0.7787 | 73000  | 0.1864        |
| 0.784  | 73500  | 0.257         |
| 0.7893 | 74000  | 0.2149        |
| 0.7947 | 74500  | 0.2519        |
| 0.8    | 75000  | 0.2746        |
| 0.8053 | 75500  | 0.2145        |
| 0.8107 | 76000  | 0.2732        |
| 0.816  | 76500  | 0.2456        |
| 0.8213 | 77000  | 0.1841        |
| 0.8267 | 77500  | 0.1876        |
| 0.832  | 78000  | 0.2661        |
| 0.8373 | 78500  | 0.1293        |
| 0.8427 | 79000  | 0.2018        |
| 0.848  | 79500  | 0.1854        |
| 0.8533 | 80000  | 0.1644        |
| 0.8587 | 80500  | 0.1844        |
| 0.864  | 81000  | 0.1937        |
| 0.8693 | 81500  | 0.1486        |
| 0.8747 | 82000  | 0.244         |
| 0.88   | 82500  | 0.131         |
| 0.8853 | 83000  | 0.215         |
| 0.8907 | 83500  | 0.2398        |
| 0.896  | 84000  | 0.2014        |
| 0.9013 | 84500  | 0.1703        |
| 0.9067 | 85000  | 0.2009        |
| 0.912  | 85500  | 0.1712        |
| 0.9173 | 86000  | 0.2649        |
| 0.9227 | 86500  | 0.2149        |
| 0.928  | 87000  | 0.1912        |
| 0.9333 | 87500  | 0.1902        |
| 0.9387 | 88000  | 0.2609        |
| 0.944  | 88500  | 0.1846        |
| 0.9493 | 89000  | 0.1485        |
| 0.9547 | 89500  | 0.2076        |
| 0.96   | 90000  | 0.2449        |
| 0.9653 | 90500  | 0.2025        |
| 0.9707 | 91000  | 0.2635        |
| 0.976  | 91500  | 0.2596        |
| 0.9813 | 92000  | 0.2221        |
| 0.9867 | 92500  | 0.2168        |
| 0.992  | 93000  | 0.192         |
| 0.9973 | 93500  | 0.1966        |
| 1.0027 | 94000  | 0.2112        |
| 1.008  | 94500  | 0.1628        |
| 1.0133 | 95000  | 0.1059        |
| 1.0187 | 95500  | 0.1403        |
| 1.024  | 96000  | 0.1726        |
| 1.0293 | 96500  | 0.1973        |
| 1.0347 | 97000  | 0.1682        |
| 1.04   | 97500  | 0.1319        |
| 1.0453 | 98000  | 0.1427        |
| 1.0507 | 98500  | 0.1448        |
| 1.056  | 99000  | 0.1215        |
| 1.0613 | 99500  | 0.1064        |
| 1.0667 | 100000 | 0.0856        |
| 1.072  | 100500 | 0.1046        |
| 1.0773 | 101000 | 0.1127        |
| 1.0827 | 101500 | 0.0988        |
| 1.088  | 102000 | 0.1598        |
| 1.0933 | 102500 | 0.1592        |
| 1.0987 | 103000 | 0.1122        |
| 1.104  | 103500 | 0.0771        |
| 1.1093 | 104000 | 0.1355        |
| 1.1147 | 104500 | 0.1265        |
| 1.12   | 105000 | 0.1464        |
| 1.1253 | 105500 | 0.1578        |
| 1.1307 | 106000 | 0.1017        |
| 1.1360 | 106500 | 0.1047        |
| 1.1413 | 107000 | 0.1865        |
| 1.1467 | 107500 | 0.1721        |
| 1.152  | 108000 | 0.1096        |
| 1.1573 | 108500 | 0.181         |
| 1.1627 | 109000 | 0.1261        |
| 1.168  | 109500 | 0.1111        |
| 1.1733 | 110000 | 0.1286        |
| 1.1787 | 110500 | 0.1014        |
| 1.184  | 111000 | 0.1033        |
| 1.1893 | 111500 | 0.1124        |
| 1.1947 | 112000 | 0.1316        |
| 1.2    | 112500 | 0.1147        |
| 1.2053 | 113000 | 0.095         |
| 1.2107 | 113500 | 0.1074        |
| 1.216  | 114000 | 0.1183        |
| 1.2213 | 114500 | 0.1219        |
| 1.2267 | 115000 | 0.1264        |
| 1.232  | 115500 | 0.1339        |
| 1.2373 | 116000 | 0.0903        |
| 1.2427 | 116500 | 0.0923        |
| 1.248  | 117000 | 0.1028        |
| 1.2533 | 117500 | 0.093         |
| 1.2587 | 118000 | 0.1024        |
| 1.264  | 118500 | 0.1107        |
| 1.2693 | 119000 | 0.1078        |
| 1.2747 | 119500 | 0.0469        |
| 1.28   | 120000 | 0.107         |
| 1.2853 | 120500 | 0.1578        |
| 1.2907 | 121000 | 0.1012        |
| 1.296  | 121500 | 0.064         |
| 1.3013 | 122000 | 0.0816        |
| 1.3067 | 122500 | 0.0656        |
| 1.312  | 123000 | 0.1314        |
| 1.3173 | 123500 | 0.1345        |
| 1.3227 | 124000 | 0.1057        |
| 1.328  | 124500 | 0.1051        |
| 1.3333 | 125000 | 0.1246        |
| 1.3387 | 125500 | 0.0827        |
| 1.3440 | 126000 | 0.0763        |
| 1.3493 | 126500 | 0.0887        |
| 1.3547 | 127000 | 0.1332        |
| 1.3600 | 127500 | 0.0939        |
| 1.3653 | 128000 | 0.087         |
| 1.3707 | 128500 | 0.0671        |
| 1.376  | 129000 | 0.1377        |
| 1.3813 | 129500 | 0.1066        |
| 1.3867 | 130000 | 0.1224        |
| 1.392  | 130500 | 0.0797        |
| 1.3973 | 131000 | 0.0712        |
| 1.4027 | 131500 | 0.1141        |
| 1.408  | 132000 | 0.1045        |
| 1.4133 | 132500 | 0.0894        |
| 1.4187 | 133000 | 0.0897        |
| 1.424  | 133500 | 0.0779        |
| 1.4293 | 134000 | 0.0944        |
| 1.4347 | 134500 | 0.0674        |
| 1.44   | 135000 | 0.1532        |
| 1.4453 | 135500 | 0.0771        |
| 1.4507 | 136000 | 0.1154        |
| 1.456  | 136500 | 0.1159        |
| 1.4613 | 137000 | 0.147         |
| 1.4667 | 137500 | 0.0925        |
| 1.472  | 138000 | 0.0985        |
| 1.4773 | 138500 | 0.1023        |
| 1.4827 | 139000 | 0.082         |
| 1.488  | 139500 | 0.0947        |
| 1.4933 | 140000 | 0.0901        |
| 1.4987 | 140500 | 0.127         |
| 1.504  | 141000 | 0.1584        |
| 1.5093 | 141500 | 0.0734        |
| 1.5147 | 142000 | 0.1065        |
| 1.52   | 142500 | 0.0568        |
| 1.5253 | 143000 | 0.1081        |
| 1.5307 | 143500 | 0.0727        |
| 1.536  | 144000 | 0.1346        |
| 1.5413 | 144500 | 0.0894        |
| 1.5467 | 145000 | 0.0739        |
| 1.552  | 145500 | 0.0926        |
| 1.5573 | 146000 | 0.0984        |
| 1.5627 | 146500 | 0.0975        |
| 1.568  | 147000 | 0.0839        |
| 1.5733 | 147500 | 0.1053        |
| 1.5787 | 148000 | 0.1369        |
| 1.584  | 148500 | 0.093         |
| 1.5893 | 149000 | 0.1008        |
| 1.5947 | 149500 | 0.0981        |
| 1.6    | 150000 | 0.1071        |
| 1.6053 | 150500 | 0.0955        |
| 1.6107 | 151000 | 0.0901        |
| 1.616  | 151500 | 0.0803        |
| 1.6213 | 152000 | 0.1119        |
| 1.6267 | 152500 | 0.0679        |
| 1.6320 | 153000 | 0.1135        |
| 1.6373 | 153500 | 0.0768        |
| 1.6427 | 154000 | 0.0837        |
| 1.6480 | 154500 | 0.0857        |
| 1.6533 | 155000 | 0.0928        |
| 1.6587 | 155500 | 0.0808        |
| 1.6640 | 156000 | 0.0823        |
| 1.6693 | 156500 | 0.0713        |
| 1.6747 | 157000 | 0.0892        |
| 1.6800 | 157500 | 0.0914        |
| 1.6853 | 158000 | 0.0735        |
| 1.6907 | 158500 | 0.0827        |
| 1.696  | 159000 | 0.1006        |
| 1.7013 | 159500 | 0.0837        |
| 1.7067 | 160000 | 0.0812        |
| 1.712  | 160500 | 0.1056        |
| 1.7173 | 161000 | 0.0878        |
| 1.7227 | 161500 | 0.0625        |
| 1.728  | 162000 | 0.0965        |
| 1.7333 | 162500 | 0.1121        |
| 1.7387 | 163000 | 0.0794        |
| 1.744  | 163500 | 0.0969        |
| 1.7493 | 164000 | 0.0696        |
| 1.7547 | 164500 | 0.083         |
| 1.76   | 165000 | 0.0702        |
| 1.7653 | 165500 | 0.0768        |
| 1.7707 | 166000 | 0.0632        |
| 1.776  | 166500 | 0.0714        |
| 1.7813 | 167000 | 0.1           |
| 1.7867 | 167500 | 0.0665        |
| 1.792  | 168000 | 0.1139        |
| 1.7973 | 168500 | 0.1032        |
| 1.8027 | 169000 | 0.0983        |
| 1.808  | 169500 | 0.0812        |
| 1.8133 | 170000 | 0.0996        |
| 1.8187 | 170500 | 0.0872        |
| 1.8240 | 171000 | 0.0612        |
| 1.8293 | 171500 | 0.1038        |
| 1.8347 | 172000 | 0.0558        |
| 1.8400 | 172500 | 0.0595        |
| 1.8453 | 173000 | 0.0558        |
| 1.8507 | 173500 | 0.0717        |
| 1.8560 | 174000 | 0.058         |
| 1.8613 | 174500 | 0.0745        |
| 1.8667 | 175000 | 0.0749        |
| 1.8720 | 175500 | 0.074         |
| 1.8773 | 176000 | 0.0792        |
| 1.8827 | 176500 | 0.0574        |
| 1.888  | 177000 | 0.0968        |
| 1.8933 | 177500 | 0.0755        |
| 1.8987 | 178000 | 0.0852        |
| 1.904  | 178500 | 0.0502        |
| 1.9093 | 179000 | 0.0699        |
| 1.9147 | 179500 | 0.0793        |
| 1.92   | 180000 | 0.113         |
| 1.9253 | 180500 | 0.0708        |
| 1.9307 | 181000 | 0.0815        |
| 1.936  | 181500 | 0.0962        |
| 1.9413 | 182000 | 0.083         |
| 1.9467 | 182500 | 0.0761        |
| 1.952  | 183000 | 0.0776        |
| 1.9573 | 183500 | 0.0811        |
| 1.9627 | 184000 | 0.1159        |
| 1.968  | 184500 | 0.081         |
| 1.9733 | 185000 | 0.146         |
| 1.9787 | 185500 | 0.0715        |
| 1.984  | 186000 | 0.12          |
| 1.9893 | 186500 | 0.0692        |
| 1.9947 | 187000 | 0.07          |
| 2.0    | 187500 | 0.0935        |
| 2.0053 | 188000 | 0.0848        |
| 2.0107 | 188500 | 0.0474        |
| 2.016  | 189000 | 0.0417        |
| 2.0213 | 189500 | 0.04          |
| 2.0267 | 190000 | 0.1139        |
| 2.032  | 190500 | 0.0553        |
| 2.0373 | 191000 | 0.0495        |
| 2.0427 | 191500 | 0.0613        |
| 2.048  | 192000 | 0.0379        |
| 2.0533 | 192500 | 0.0487        |
| 2.0587 | 193000 | 0.0417        |
| 2.064  | 193500 | 0.0249        |
| 2.0693 | 194000 | 0.0418        |
| 2.0747 | 194500 | 0.043         |
| 2.08   | 195000 | 0.051         |
| 2.0853 | 195500 | 0.0339        |
| 2.0907 | 196000 | 0.0519        |
| 2.096  | 196500 | 0.0878        |
| 2.1013 | 197000 | 0.0432        |
| 2.1067 | 197500 | 0.0185        |
| 2.112  | 198000 | 0.085         |
| 2.1173 | 198500 | 0.0601        |
| 2.1227 | 199000 | 0.0935        |
| 2.128  | 199500 | 0.0538        |
| 2.1333 | 200000 | 0.0445        |
| 2.1387 | 200500 | 0.0499        |
| 2.144  | 201000 | 0.1029        |
| 2.1493 | 201500 | 0.0758        |
| 2.1547 | 202000 | 0.0648        |
| 2.16   | 202500 | 0.0612        |
| 2.1653 | 203000 | 0.0618        |
| 2.1707 | 203500 | 0.0566        |
| 2.176  | 204000 | 0.0179        |
| 2.1813 | 204500 | 0.0557        |
| 2.1867 | 205000 | 0.0321        |
| 2.192  | 205500 | 0.0562        |
| 2.1973 | 206000 | 0.0673        |
| 2.2027 | 206500 | 0.0286        |
| 2.208  | 207000 | 0.0284        |
| 2.2133 | 207500 | 0.0595        |
| 2.2187 | 208000 | 0.0693        |
| 2.224  | 208500 | 0.065         |
| 2.2293 | 209000 | 0.0546        |
| 2.2347 | 209500 | 0.0467        |
| 2.24   | 210000 | 0.0353        |
| 2.2453 | 210500 | 0.0475        |
| 2.2507 | 211000 | 0.0451        |
| 2.2560 | 211500 | 0.0348        |
| 2.2613 | 212000 | 0.031         |
| 2.2667 | 212500 | 0.0294        |
| 2.2720 | 213000 | 0.0462        |
| 2.2773 | 213500 | 0.0376        |
| 2.2827 | 214000 | 0.0607        |
| 2.288  | 214500 | 0.041         |
| 2.2933 | 215000 | 0.0462        |
| 2.2987 | 215500 | 0.0285        |
| 2.304  | 216000 | 0.0177        |
| 2.3093 | 216500 | 0.0577        |
| 2.3147 | 217000 | 0.0368        |
| 2.32   | 217500 | 0.041         |
| 2.3253 | 218000 | 0.0469        |
| 2.3307 | 218500 | 0.0669        |
| 2.336  | 219000 | 0.0288        |
| 2.3413 | 219500 | 0.0283        |
| 2.3467 | 220000 | 0.0293        |
| 2.352  | 220500 | 0.0364        |
| 2.3573 | 221000 | 0.0431        |
| 2.3627 | 221500 | 0.0478        |
| 2.368  | 222000 | 0.0223        |
| 2.3733 | 222500 | 0.0464        |
| 2.3787 | 223000 | 0.0598        |
| 2.384  | 223500 | 0.0716        |
| 2.3893 | 224000 | 0.0445        |
| 2.3947 | 224500 | 0.0356        |
| 2.4    | 225000 | 0.0344        |
| 2.4053 | 225500 | 0.0729        |
| 2.4107 | 226000 | 0.0256        |
| 2.416  | 226500 | 0.0383        |
| 2.4213 | 227000 | 0.0445        |
| 2.4267 | 227500 | 0.0286        |
| 2.432  | 228000 | 0.0216        |
| 2.4373 | 228500 | 0.0299        |
| 2.4427 | 229000 | 0.0674        |
| 2.448  | 229500 | 0.0353        |
| 2.4533 | 230000 | 0.0403        |
| 2.4587 | 230500 | 0.0693        |
| 2.464  | 231000 | 0.0701        |
| 2.4693 | 231500 | 0.0506        |
| 2.4747 | 232000 | 0.0374        |
| 2.48   | 232500 | 0.0511        |
| 2.4853 | 233000 | 0.047         |
| 2.4907 | 233500 | 0.0231        |
| 2.496  | 234000 | 0.0513        |
| 2.5013 | 234500 | 0.0955        |
| 2.5067 | 235000 | 0.049         |
| 2.512  | 235500 | 0.048         |
| 2.5173 | 236000 | 0.0302        |
| 2.5227 | 236500 | 0.0207        |
| 2.528  | 237000 | 0.0357        |
| 2.5333 | 237500 | 0.0297        |
| 2.5387 | 238000 | 0.0554        |
| 2.544  | 238500 | 0.0386        |
| 2.5493 | 239000 | 0.0249        |
| 2.5547 | 239500 | 0.0432        |
| 2.56   | 240000 | 0.0539        |
| 2.5653 | 240500 | 0.0348        |
| 2.5707 | 241000 | 0.0233        |
| 2.576  | 241500 | 0.0702        |
| 2.5813 | 242000 | 0.0393        |
| 2.5867 | 242500 | 0.0625        |
| 2.592  | 243000 | 0.0197        |
| 2.5973 | 243500 | 0.0399        |
| 2.6027 | 244000 | 0.0495        |
| 2.608  | 244500 | 0.0407        |
| 2.6133 | 245000 | 0.0412        |
| 2.6187 | 245500 | 0.0234        |
| 2.624  | 246000 | 0.0559        |
| 2.6293 | 246500 | 0.0555        |
| 2.6347 | 247000 | 0.0328        |
| 2.64   | 247500 | 0.0375        |
| 2.6453 | 248000 | 0.0257        |
| 2.6507 | 248500 | 0.0212        |
| 2.656  | 249000 | 0.0633        |
| 2.6613 | 249500 | 0.0268        |
| 2.6667 | 250000 | 0.0354        |
| 2.672  | 250500 | 0.0341        |
| 2.6773 | 251000 | 0.0337        |
| 2.6827 | 251500 | 0.0519        |
| 2.6880 | 252000 | 0.0386        |
| 2.6933 | 252500 | 0.0603        |
| 2.6987 | 253000 | 0.0358        |
| 2.7040 | 253500 | 0.0352        |
| 2.7093 | 254000 | 0.0448        |
| 2.7147 | 254500 | 0.037         |
| 2.7200 | 255000 | 0.0375        |
| 2.7253 | 255500 | 0.04          |
| 2.7307 | 256000 | 0.0729        |
| 2.7360 | 256500 | 0.0246        |
| 2.7413 | 257000 | 0.045         |
| 2.7467 | 257500 | 0.0333        |
| 2.752  | 258000 | 0.0212        |
| 2.7573 | 258500 | 0.0458        |
| 2.7627 | 259000 | 0.048         |
| 2.768  | 259500 | 0.0287        |
| 2.7733 | 260000 | 0.0345        |
| 2.7787 | 260500 | 0.0459        |
| 2.784  | 261000 | 0.0449        |
| 2.7893 | 261500 | 0.0518        |
| 2.7947 | 262000 | 0.0433        |
| 2.8    | 262500 | 0.0572        |
| 2.8053 | 263000 | 0.0357        |
| 2.8107 | 263500 | 0.0394        |
| 2.816  | 264000 | 0.0531        |
| 2.8213 | 264500 | 0.0294        |
| 2.8267 | 265000 | 0.039         |
| 2.832  | 265500 | 0.0505        |
| 2.8373 | 266000 | 0.0167        |
| 2.8427 | 266500 | 0.031         |
| 2.848  | 267000 | 0.0362        |
| 2.8533 | 267500 | 0.0246        |
| 2.8587 | 268000 | 0.0317        |
| 2.864  | 268500 | 0.0296        |
| 2.8693 | 269000 | 0.0297        |
| 2.8747 | 269500 | 0.0517        |
| 2.88   | 270000 | 0.019         |
| 2.8853 | 270500 | 0.0358        |
| 2.8907 | 271000 | 0.0589        |
| 2.896  | 271500 | 0.031         |
| 2.9013 | 272000 | 0.0421        |
| 2.9067 | 272500 | 0.0422        |
| 2.912  | 273000 | 0.016         |
| 2.9173 | 273500 | 0.0645        |
| 2.9227 | 274000 | 0.0514        |
| 2.928  | 274500 | 0.0173        |
| 2.9333 | 275000 | 0.0432        |
| 2.9387 | 275500 | 0.0594        |
| 2.944  | 276000 | 0.0228        |
| 2.9493 | 276500 | 0.0152        |
| 2.9547 | 277000 | 0.0579        |
| 2.96   | 277500 | 0.0578        |
| 2.9653 | 278000 | 0.0246        |
| 2.9707 | 278500 | 0.0609        |
| 2.976  | 279000 | 0.0613        |
| 2.9813 | 279500 | 0.0589        |
| 2.9867 | 280000 | 0.047         |
| 2.992  | 280500 | 0.0264        |
| 2.9973 | 281000 | 0.0464        |

</details>

### Framework Versions
- Python: 3.10.12
- Sentence Transformers: 3.3.0
- Transformers: 4.46.3
- PyTorch: 2.5.1+cu124
- Accelerate: 1.1.1
- Datasets: 3.2.0
- Tokenizers: 0.20.3

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

#### CoSENTLoss
```bibtex
@online{kexuefm-8847,
    title={CoSENT: A more efficient sentence vector scheme than Sentence-BERT},
    author={Su Jianlin},
    year={2022},
    month={Jan},
    url={https://kexue.fm/archives/8847},
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