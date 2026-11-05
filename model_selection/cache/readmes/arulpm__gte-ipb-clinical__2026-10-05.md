---
language:
- multilingual
license: apache-2.0
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:217680
- loss:MultipleNegativesRankingLoss
base_model: Alibaba-NLP/gte-multilingual-base
widget:
- source_sentence: "Keluhan: bintik2 merah di badan. 3 hari\r\ngatal +\nAnamnesa Pemeriksaan\
    \ Dokter: bintik2 merah di badan. 3 hari\r\ngatal +"
  sentences:
  - 'Obat: Devit 5000iu

    Deskripsi Obat: Vitamin D3 dosis tinggi untuk defisiensi'
  - 'Obat: Betaver 6 mg

    Deskripsi Obat: Obat untuk mengobati vertigo dan gangguan keseimbangan'
  - 'Obat: Captopril 12,5 mg

    Deskripsi Obat: Obat antihipertensi golongan ACE inhibitor dosis rendah untuk
    menurunkan tekanan darah'
- source_sentence: "Keluhan: 2 minggu sampai sekarang BAK berdarah, sebelumnya sempat\
    \ berdarah, saat BAK kadang sakit \nAnamnesa Pemeriksaan Dokter: bak disertai\
    \ darah sejak 2 minggu, kadang disertai nyeri, riwayat sebelumnya bab disertai\
    \ darah "
  sentences:
  - 'Obat: Hufarizine 10 mg

    Deskripsi Obat: Antihistamin untuk mengatasi alergi'
  - 'Obat: Cefixime 200 mg

    Deskripsi Obat: Antibiotik golongan sefalosporin untuk mengobati infeksi bakteri'
  - 'Obat: Omeprazole

    Deskripsi Obat: Obat penghambat pompa proton untuk mengatasi tukak lambung'
- source_sentence: 'Keluhan: Batuk batuk. Sedang minum obat pasca operasi gigi

    Anamnesa Pemeriksaan Dokter: batuk2'
  sentences:
  - 'Obat: Pyfaton tablet

    Deskripsi Obat: Obat untuk mengobati gangguan pencernaan'
  - 'Obat: Cefadroxil 500 mg

    Deskripsi Obat: Antibiotik golongan sefalosporin untuk mengobati infeksi bakteri
    saluran pernapasan dan kulit'
  - 'Obat: Acyclovir 400 mg

    Deskripsi Obat: Obat antiviral untuk mengobati infeksi virus herpes simpleks dan
    varicella zoster'
- source_sentence: 'Keluhan: nan

    Anamnesa Pemeriksaan Dokter: demam hari ke 5, mual muntah, ada kemerahan di betis
    kaki kanan sejak 3 hari, susah masuk makan karena mual'
  sentences:
  - 'Obat: Caviplex

    Deskripsi Obat: Suplemen multivitamin untuk memenuhi kebutuhan vitamin dan mineral'
  - 'Obat: Ciprofloxacin 500 mg

    Deskripsi Obat: Antibiotik golongan fluorokuinolon untuk mengobati infeksi bakteri'
  - 'Obat: OBH

    Deskripsi Obat: Obat batuk untuk meredakan batuk kering'
- source_sentence: 'Keluhan: nan

    Anamnesa Pemeriksaan Dokter: mual pusing'
  sentences:
  - 'Obat: Buscopan

    Deskripsi Obat: Obat untuk mengurangi kejang otot polos saluran pencernaan'
  - 'Obat: Sangobion

    Deskripsi Obat: Suplemen penambah darah untuk mengobati anemia defisiensi besi'
  - 'Obat: Blocand 16 mg

    Deskripsi Obat: Obat antihipertensi golongan ARB dosis tinggi untuk menurunkan
    tekanan darah'
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# GTE Multilingual fine-tuned on clinical-to-drug mapping

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [Alibaba-NLP/gte-multilingual-base](https://huggingface.co/Alibaba-NLP/gte-multilingual-base). It maps sentences & paragraphs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [Alibaba-NLP/gte-multilingual-base](https://huggingface.co/Alibaba-NLP/gte-multilingual-base) <!-- at revision 9bbca17d9273fd0d03d5725c7a4b0f6b45142062 -->
- **Maximum Sequence Length:** 8192 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
<!-- - **Training Dataset:** Unknown -->
- **Language:** multilingual
- **License:** apache-2.0

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 8192, 'do_lower_case': False}) with Transformer model: NewModel 
  (1): Pooling({'word_embedding_dimension': 768, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("sentence_transformers_model_id")
# Run inference
sentences = [
    'Keluhan: nan\nAnamnesa Pemeriksaan Dokter: mual pusing',
    'Obat: Buscopan\nDeskripsi Obat: Obat untuk mengurangi kejang otot polos saluran pencernaan',
    'Obat: Blocand 16 mg\nDeskripsi Obat: Obat antihipertensi golongan ARB dosis tinggi untuk menurunkan tekanan darah',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

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

* Size: 217,680 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                              | positive                                                                           |
  |:--------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                             |
  | details | <ul><li>min: 17 tokens</li><li>mean: 42.44 tokens</li><li>max: 177 tokens</li></ul> | <ul><li>min: 15 tokens</li><li>mean: 22.55 tokens</li><li>max: 38 tokens</li></ul> |
* Samples:
  | anchor                                                                                                                                                                                                                                                      | positive                                                                                                               |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------|
  | <code>Keluhan: nan<br>Anamnesa Pemeriksaan Dokter: gusi kiri bengkak   <br>nyeri tenggorokan, ada amandel 2 hari yang lalu   <br>puisng </code>                                                                                                               | <code>Obat: Eflagen 50 mg<br>Deskripsi Obat: Obat antiinflamasi nonsteroid (NSAID) untuk mengurangi nyeri</code>       |
  | <code>Keluhan: pasien mengatakan kuku kaki jempol kiri merah dan  nyeri sejak 1 bulan yll hilang timbul<br>Anamnesa Pemeriksaan Dokter: pasien mengatakan kuku kaki jempol kiri merah dan  nyeri sejak 1 bulan yll hilang timbul. merah + bengkak + </code> | <code>Obat: Mefinal 500 mg<br>Deskripsi Obat: Obat antiinflamasi nonsteroid (NSAID) untuk mengurangi nyeri</code>      |
  | <code>Keluhan: batuk dahak sudah 1 minggu<br>Anamnesa Pemeriksaan Dokter: batuk dahak sejak 1 minggu  <br>RPO : Acetylcystein, OBH</code>                                                                                                                    | <code>Obat: Cefixime 200 mg<br>Deskripsi Obat: Antibiotik golongan sefalosporin untuk mengobati infeksi bakteri</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim"
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset

* Size: 24,187 evaluation samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                              | positive                                                                           |
  |:--------|:------------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                              | string                                                                             |
  | details | <ul><li>min: 16 tokens</li><li>mean: 42.79 tokens</li><li>max: 112 tokens</li></ul> | <ul><li>min: 15 tokens</li><li>mean: 22.79 tokens</li><li>max: 38 tokens</li></ul> |
* Samples:
  | anchor                                                                                                                                                                                                                                                                                                      | positive                                                                                                          |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
  | <code>Keluhan: NYERI PERUT, MUAL, MUNTAH 1KALI HARI INI,<br>Anamnesa Pemeriksaan Dokter: NYERI PERUT, MUAL, MUNTAH 1KALI HARI INI, tenggorokan gatla   <br>rpo myalanta   <br>alergi obat dsiangkal </code>                                                                                                   | <code>Obat: Lambucid<br>Deskripsi Obat: Antasida untuk meredakan gejala asam lambung berlebih</code>              |
  | <code>Keluhan: badan lemas tadi pagi, mual- muntah- batuk pilek- <br>Anamnesa Pemeriksaan Dokter: lemas sejak pagi ini. demam - pingsan - sempat terjatuh karena lemas. pola makan tidak teratur.   <br>rpo tablet tambah darah. riw anemia + dikatakan saat SMA 3 tahun yll. tidak ingat hb berapa. </code> | <code>Obat: Caviplex<br>Deskripsi Obat: Suplemen multivitamin untuk memenuhi kebutuhan vitamin dan mineral</code> |
  | <code>Keluhan: rencana rujukan rsMD spP tgl 23-04-24  <br>keluhan hari ini kepala pusing terasa berat, batuk, nyeri badan. <br>Anamnesa Pemeriksaan Dokter: rencana rujukan rsMD spP tgl 23-04-24 keluhan hari ini kepala pusing terasa berat, batuk, nyeri badan.</code>                                    | <code>Obat: Profat sirup<br>Deskripsi Obat: Suplemen penambah darah sirup untuk anak</code>                       |
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
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 32
- `num_train_epochs`: 1
- `warmup_ratio`: 0.1
- `fp16`: True
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: steps
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
- `max_grad_norm`: 1.0
- `num_train_epochs`: 1
- `max_steps`: -1
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: {}
- `warmup_ratio`: 0.1
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
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step | Training Loss | Validation Loss |
|:------:|:----:|:-------------:|:---------------:|
| 0.0073 | 50   | 3.3431        | -               |
| 0.0147 | 100  | 3.1904        | -               |
| 0.0220 | 150  | 3.0541        | -               |
| 0.0294 | 200  | 2.972         | -               |
| 0.0367 | 250  | 2.8877        | -               |
| 0.0441 | 300  | 2.8234        | -               |
| 0.0514 | 350  | 2.749         | -               |
| 0.0588 | 400  | 2.7435        | -               |
| 0.0661 | 450  | 2.7368        | -               |
| 0.0735 | 500  | 2.6943        | -               |
| 0.0808 | 550  | 2.7168        | -               |
| 0.0882 | 600  | 2.7194        | -               |
| 0.0955 | 650  | 2.6096        | -               |
| 0.1029 | 700  | 2.7118        | -               |
| 0.1102 | 750  | 2.7036        | -               |
| 0.1176 | 800  | 2.6625        | -               |
| 0.1249 | 850  | 2.6362        | -               |
| 0.1323 | 900  | 2.599         | -               |
| 0.1396 | 950  | 2.572         | -               |
| 0.1470 | 1000 | 2.6124        | 2.0072          |
| 0.1543 | 1050 | 2.5467        | -               |
| 0.1617 | 1100 | 2.5713        | -               |
| 0.1690 | 1150 | 2.5741        | -               |
| 0.1764 | 1200 | 2.5794        | -               |
| 0.1837 | 1250 | 2.5231        | -               |
| 0.1911 | 1300 | 2.5312        | -               |
| 0.1984 | 1350 | 2.4483        | -               |
| 0.2058 | 1400 | 2.5178        | -               |
| 0.2131 | 1450 | 2.4795        | -               |
| 0.2205 | 1500 | 2.5426        | -               |
| 0.2278 | 1550 | 2.502         | -               |
| 0.2352 | 1600 | 2.5378        | -               |
| 0.2425 | 1650 | 2.4746        | -               |
| 0.2499 | 1700 | 2.4356        | -               |
| 0.2572 | 1750 | 2.5303        | -               |
| 0.2646 | 1800 | 2.514         | -               |
| 0.2719 | 1850 | 2.5207        | -               |
| 0.2793 | 1900 | 2.4671        | -               |
| 0.2866 | 1950 | 2.4367        | -               |
| 0.2940 | 2000 | 2.4873        | 1.9339          |
| 0.3013 | 2050 | 2.4513        | -               |
| 0.3087 | 2100 | 2.4695        | -               |
| 0.3160 | 2150 | 2.4309        | -               |
| 0.3234 | 2200 | 2.4439        | -               |
| 0.3307 | 2250 | 2.4242        | -               |
| 0.3381 | 2300 | 2.4569        | -               |
| 0.3454 | 2350 | 2.4157        | -               |
| 0.3528 | 2400 | 2.4709        | -               |
| 0.3601 | 2450 | 2.4202        | -               |
| 0.3675 | 2500 | 2.4401        | -               |
| 0.3748 | 2550 | 2.4096        | -               |
| 0.3822 | 2600 | 2.3878        | -               |
| 0.3895 | 2650 | 2.4766        | -               |
| 0.3969 | 2700 | 2.4149        | -               |
| 0.4042 | 2750 | 2.4197        | -               |
| 0.4116 | 2800 | 2.3656        | -               |
| 0.4189 | 2850 | 2.4679        | -               |
| 0.4263 | 2900 | 2.3749        | -               |
| 0.4336 | 2950 | 2.4146        | -               |
| 0.4410 | 3000 | 2.3942        | 1.8871          |
| 0.4483 | 3050 | 2.418         | -               |
| 0.4557 | 3100 | 2.4504        | -               |
| 0.4630 | 3150 | 2.3759        | -               |
| 0.4704 | 3200 | 2.3671        | -               |
| 0.4777 | 3250 | 2.4433        | -               |
| 0.4851 | 3300 | 2.4036        | -               |
| 0.4924 | 3350 | 2.3539        | -               |
| 0.4998 | 3400 | 2.3806        | -               |
| 0.5071 | 3450 | 2.3737        | -               |
| 0.5145 | 3500 | 2.4127        | -               |
| 0.5218 | 3550 | 2.4243        | -               |
| 0.5292 | 3600 | 2.3528        | -               |
| 0.5365 | 3650 | 2.3788        | -               |
| 0.5439 | 3700 | 2.3968        | -               |
| 0.5512 | 3750 | 2.3896        | -               |
| 0.5586 | 3800 | 2.3966        | -               |
| 0.5659 | 3850 | 2.3571        | -               |
| 0.5733 | 3900 | 2.3437        | -               |
| 0.5806 | 3950 | 2.3353        | -               |
| 0.5880 | 4000 | 2.3335        | 1.8599          |
| 0.5953 | 4050 | 2.3778        | -               |
| 0.6027 | 4100 | 2.3929        | -               |
| 0.6100 | 4150 | 2.3818        | -               |
| 0.6174 | 4200 | 2.3874        | -               |
| 0.6247 | 4250 | 2.3224        | -               |
| 0.6321 | 4300 | 2.3317        | -               |
| 0.6394 | 4350 | 2.3761        | -               |
| 0.6468 | 4400 | 2.4066        | -               |
| 0.6541 | 4450 | 2.3406        | -               |
| 0.6615 | 4500 | 2.3844        | -               |
| 0.6688 | 4550 | 2.2993        | -               |
| 0.6762 | 4600 | 2.337         | -               |
| 0.6835 | 4650 | 2.37          | -               |
| 0.6909 | 4700 | 2.3126        | -               |
| 0.6982 | 4750 | 2.3818        | -               |
| 0.7056 | 4800 | 2.3849        | -               |
| 0.7129 | 4850 | 2.3379        | -               |
| 0.7203 | 4900 | 2.3518        | -               |
| 0.7276 | 4950 | 2.3354        | -               |
| 0.7350 | 5000 | 2.3443        | 1.8349          |
| 0.7423 | 5050 | 2.3396        | -               |
| 0.7497 | 5100 | 2.3086        | -               |
| 0.7570 | 5150 | 2.3392        | -               |
| 0.7644 | 5200 | 2.3316        | -               |
| 0.7717 | 5250 | 2.3092        | -               |
| 0.7791 | 5300 | 2.3794        | -               |
| 0.7864 | 5350 | 2.331         | -               |
| 0.7938 | 5400 | 2.2554        | -               |
| 0.8011 | 5450 | 2.3266        | -               |
| 0.8085 | 5500 | 2.3314        | -               |
| 0.8158 | 5550 | 2.3357        | -               |
| 0.8232 | 5600 | 2.3523        | -               |
| 0.8305 | 5650 | 2.3253        | -               |
| 0.8379 | 5700 | 2.3021        | -               |
| 0.8452 | 5750 | 2.3342        | -               |
| 0.8526 | 5800 | 2.2839        | -               |
| 0.8599 | 5850 | 2.3136        | -               |
| 0.8673 | 5900 | 2.3562        | -               |
| 0.8746 | 5950 | 2.2878        | -               |
| 0.8820 | 6000 | 2.3219        | 1.8173          |
| 0.8893 | 6050 | 2.2941        | -               |
| 0.8967 | 6100 | 2.3245        | -               |
| 0.9040 | 6150 | 2.2561        | -               |
| 0.9114 | 6200 | 2.3327        | -               |
| 0.9187 | 6250 | 2.3047        | -               |
| 0.9261 | 6300 | 2.2916        | -               |
| 0.9334 | 6350 | 2.3495        | -               |
| 0.9408 | 6400 | 1.9273        | -               |
| 0.9481 | 6450 | 1.3917        | -               |
| 0.9555 | 6500 | 1.4726        | -               |
| 0.9628 | 6550 | 1.3922        | -               |
| 0.9702 | 6600 | 1.4664        | -               |
| 0.9775 | 6650 | 1.4329        | -               |
| 0.9849 | 6700 | 1.4046        | -               |
| 0.9922 | 6750 | 1.3891        | -               |
| 0.9996 | 6800 | 1.4731        | -               |

</details>

### Framework Versions
- Python: 3.11.13
- Sentence Transformers: 4.1.0
- Transformers: 4.53.2
- PyTorch: 2.6.0+cu124
- Accelerate: 1.8.1
- Datasets: 2.14.4
- Tokenizers: 0.21.2

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