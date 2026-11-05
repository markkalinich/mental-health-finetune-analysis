---
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:1465
- loss:MultipleNegativesRankingLoss
base_model: google-bert/bert-base-uncased
widget:
- source_sentence: Dark Red and Purple lines in inner thigh. No symptoms experienced.
    Age 28, Weight 58kg Height 4'11"
  sentences:
  - Hello. Extraction and laser could be done.
  - Hello, Welcome to iclinic.com. For further queries consult an ENT otolaryngologist
    online -->
  - Dear, Please send few more photographs.. Regards
- source_sentence: Hi doctor, I have a sore in the mouth. I have attached the photos.
    Please help.
  sentences:
  - Hi. For further information consult a family physician online -->
  - Hi. Revert back with the answers to the above questions to a dentist online -->
  - Hello. May I know your age, and since how many months are you experiencing thinning
    of hair? Please send the pictures of the scalp.
- source_sentence: Hello doctor, What is the main reason for sepsis to occur in a
    newborn? Will parents be the reason?
  sentences:
  - Hello. Kindly revert back with the details to a dermatologist online -->
  - Hello. For further queries consult a medical gastroenterologist online -->
  - Hi. For further information consult a paediatrician online -->
- source_sentence: Hello doctor, I am underweight and my BMI is 16.5. Kindly help
    me to put on weight.
  sentences:
  - Hi. For further information consult a criticalcare physician online -->
  - Hello. First, you explain about your daily routine, and like and dislike foods.
  - 'Hello. Problem list: 1. Your body mass index is 33.27 kg/m2'
- source_sentence: Hello doctor, I have an infection in my private part. Kindly help.
  sentences:
  - Hello. How long has it been there? What are the symptoms in it? And any other
    family member affected?
  - Hello. What are the symptoms in it? How long has it been there? Any recent unsafe
    sexual exposure?
  - Hello. For further information consult an ENT otolaryngologist online -->
pipeline_tag: sentence-similarity
library_name: sentence-transformers
---

# SentenceTransformer based on google-bert/bert-base-uncased

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased). It maps inputs to a 768-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [google-bert/bert-base-uncased](https://huggingface.co/google-bert/bert-base-uncased) <!-- at revision 86b5e0934494bd15c9632b12f734a8a67f723594 -->
- **Maximum Sequence Length:** 256 tokens
- **Output Dimensionality:** 768 dimensions
- **Similarity Function:** Cosine Similarity
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'transformer_task': 'feature-extraction', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'last_hidden_state'}}, 'module_output_name': 'token_embeddings', 'architecture': 'BertModel'})
  (1): Pooling({'embedding_dimension': 768, 'pooling_mode': 'mean', 'include_prompt': True})
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
model = SentenceTransformer("FicoFilbert/finetuned-medical-bert")
# Run inference
sentences = [
    'Hello doctor, I have an infection in my private part. Kindly help.',
    'Hello. What are the symptoms in it? How long has it been there? Any recent unsafe sexual exposure?',
    'Hello. How long has it been there? What are the symptoms in it? And any other family member affected?',
]
embeddings = model.encode(sentences)
print(embeddings.shape)
# [3, 768]

# Get the similarity scores for the embeddings
similarities = model.similarity(embeddings, embeddings)
print(similarities)
# tensor([[1.0000, 0.5949, 0.5955],
#         [0.5949, 1.0000, 0.7368],
#         [0.5955, 0.7368, 1.0000]])
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

* Size: 1,465 training samples
* Columns: <code>sentence_0</code> and <code>sentence_1</code>
* Approximate statistics based on the first 100 samples:
  |          | sentence_0                                                                           | sentence_1                                                                           |
  |:---------|:-------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|
  | type     | string                                                                               | string                                                                               |
  | modality | text                                                                                 | text                                                                                 |
  | details  | <ul><li>min: 19 tokens</li><li>mean: 118.23 tokens</li><li>max: 256 tokens</li></ul> | <ul><li>min: 16 tokens</li><li>mean: 139.51 tokens</li><li>max: 256 tokens</li></ul> |
* Samples:
  | sentence_0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
  |:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>Hi doctor, My son aged 4 years and 4 months is premature by birth at 34 weeks. His current weight is 15.5 kg. He always used to get a cough and sometimes fever in an interval of every two to three months, especially since last one year. However, there is no other visible physical or mental problem because of his preterm birth. Recently doctor has diagnosed, based on his stethoscope examination and repeated illness, mild intermittent asthma. However, we do not have any family history of asthma. His last 6 months illness history and medication are attached here. Kindly go through it and reply to my queries. Based on the symptoms and background, can it be confirmed that my son is suffering from asthma? If it is asthma, is it the right course of medication in the initial stage? Do we need any other test for reconfirmation and start with essential medicines? Is it permanently curable? What are the dietary do and do not for asthmatic patients? Is there any other better means of treatment in ...</code> | <code>Hi. Though your son is premature, it does not matter with the present illness. Let me first clear you that he is suffering from bronchial asthma. And anyone can have asthma without any family history. So, it is not necessary to be always run in families. To confirm the diagnosis we do spirometry test in children over 6 years of age. But as your son is too young, he will not be able to perform the spirometry. So, we have to make diagnosis on clinical basis. There is no other way to confirm. Now, we have made a firm diagnosis of asthma.Regarding the treatment, nebulization medications are only to be used in emergency. Also, it is not advisable to use steroids syrup on long-term basis. The best treatment for asthma to your son is using inhaler medicines with spacer. You start him on Budecort inhaler (Budesonide) 100 two puffs twice daily with Zerostat VT spacer. Both medicines are from Cipla company. Ask him to gargle after each use of inhaler. Multivitamin and cough syrup can be used as ...</code> |
  | <code>Hi doctor, Recently, I had an operation in left external auditory canal under general anesthesia. I am having doubt that some GPRS tracking system has been inserted during operation. Is it possible to insert GPRS or something like that inside ear? Please help me.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | <code>Hello. Yes, it is technically possible to implant a small GPRS (general packet radio service) chip in your post aural region. But, that type of device cost a lot. I do not think that anyone can access to that type of device as shown in most of spy movies. So, do not worry. Nobody is going to track you. If still you have any doubt then you can do an x-ray of mastoid region to clarify it.</code>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
  | <code>Hi doctor, My mother underwent gallbladder surgery 10 months ago. From past 3 months she started having chronic cough. She tried many home remedies. She did not recover completely. I took my mother recently for a health checkup. As I suspected the chest report was not absolutely fine. But, the doctor was not at all concerned about her cough and said everything is normal. Why is it so? I want to know what is the meaning of this x- ray report and what should be our next step? Presently she is under medication for thyroid as well as diabetes. I have attached her reports. Kindly have a look at them and suggest how to go about the treatment. Thank you.</code>                                                                                                                                                                                                                                                                                                                                                             | <code>Hello. Thanks for choosing this platform. As you said your mother is having chronic cough 4 months after surgery. It can be just coincidental finding as her x-ray (attachment removed to protect patient identity) is showing prominent basal vascular markings and cough can be aggravated by surgery. The x-ray findings are suggestive of interstitial lung disease called lung fibrosis which can be confirmed only after HRCT (high-resolution computed tomography) scan of chest. So at the earliest, I advise you to do HRCT scan of chest to rule out IPF (idiopathic pulmonary fibrosis). Once the diagnosis is made, treatment can be started accordingly. IPF or lung fibrosis is a chronic and progressive condition. So, diagnosis should be made as early as possible.Talk to your pulmonologist regarding further investigations and treatment. He will guide you better as frequent follow-up visits are required for monitoring the disease. Autoimmunity. HRCT chest to rule out IPF. Interstitial pneumonia. IPF (id...</code> |
* Loss: [<code>MultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#multiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "gather_across_devices": false,
      "directions": [
          "query_to_doc"
      ],
      "partition_mode": "joint",
      "hardness_mode": null,
      "hardness_strength": 0.0
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
- `multi_dataset_batch_sampler`: round_robin

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `do_predict`: False
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 16
- `per_device_eval_batch_size`: 16
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
- `lr_scheduler_kwargs`: None
- `warmup_ratio`: None
- `warmup_steps`: 0
- `log_level`: passive
- `log_level_replica`: warning
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `enable_jit_checkpoint`: False
- `save_on_each_node`: False
- `save_only_model`: False
- `restore_callback_states_from_checkpoint`: False
- `use_cpu`: False
- `seed`: 42
- `data_seed`: None
- `bf16`: False
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `local_rank`: -1
- `ddp_backend`: None
- `debug`: []
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_prefetch_factor`: None
- `disable_tqdm`: False
- `remove_unused_columns`: True
- `label_names`: None
- `load_best_model_at_end`: False
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `deepspeed`: None
- `label_smoothing_factor`: 0.0
- `optim`: adamw_torch_fused
- `optim_args`: None
- `group_by_length`: False
- `length_column_name`: length
- `project`: huggingface
- `trackio_space_id`: trackio
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `skip_memory_metrics`: True
- `push_to_hub`: False
- `resume_from_checkpoint`: None
- `hub_model_id`: None
- `hub_strategy`: every_save
- `hub_private_repo`: None
- `hub_always_push`: False
- `hub_revision`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `include_for_metrics`: []
- `eval_do_concat_batches`: True
- `auto_find_batch_size`: False
- `full_determinism`: False
- `ddp_timeout`: 1800
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `include_num_input_tokens_seen`: no
- `neftune_noise_alpha`: None
- `optim_target_modules`: None
- `batch_eval_metrics`: False
- `eval_on_start`: False
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `eval_use_gather_object`: False
- `average_tokens_across_devices`: True
- `use_cache`: False
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: round_robin
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Time
- **Training**: 3.7 minutes

### Framework Versions
- Python: 3.12.13
- Sentence Transformers: 6.1.0
- Transformers: 5.0.0
- PyTorch: 2.10.0+cu128
- Accelerate: 1.13.0
- Datasets: 5.0.0
- Tokenizers: 0.22.2

## Additional Resources

- [Training and Finetuning Embedding Models with Sentence Transformers](https://huggingface.co/blog/train-sentence-transformers): the end-to-end guide for training or finetuning Sentence Transformer models.
- [Introduction to Matryoshka Embedding Models](https://huggingface.co/blog/matryoshka): variable-size embeddings that can be truncated with minimal quality loss.
- [Binary and Scalar Embedding Quantization for Significantly Faster & Cheaper Retrieval](https://huggingface.co/blog/embedding-quantization): post-training compression of embedding vectors.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): train multimodal embedding models, with a Visual Document Retrieval walkthrough.

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
@misc{oord2019representationlearningcontrastivepredictive,
      title={Representation Learning with Contrastive Predictive Coding},
      author={Aaron van den Oord and Yazhe Li and Oriol Vinyals},
      year={2019},
      eprint={1807.03748},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/1807.03748},
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