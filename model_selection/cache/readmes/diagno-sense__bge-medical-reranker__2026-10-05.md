---
tags:
- sentence-transformers
- cross-encoder
- reranker
- generated_from_trainer
- dataset_size:1800
- loss:BinaryCrossEntropyLoss
base_model: BAAI/bge-reranker-v2-m3
pipeline_tag: text-ranking
library_name: sentence-transformers
metrics:
- accuracy
- accuracy_threshold
- f1
- f1_threshold
- precision
- recall
- average_precision
model-index:
- name: CrossEncoder based on BAAI/bge-reranker-v2-m3
  results:
  - task:
      type: cross-encoder-binary-classification
      name: Cross Encoder Binary Classification
    dataset:
      name: pubmed val
      type: pubmed-val
    metrics:
    - type: accuracy
      value: 0.97
      name: Accuracy
    - type: accuracy_threshold
      value: 0.00019717060786206275
      name: Accuracy Threshold
    - type: f1
      value: 0.9696969696969696
      name: F1
    - type: f1_threshold
      value: 8.43404486658983e-05
      name: F1 Threshold
    - type: precision
      value: 0.9504950495049505
      name: Precision
    - type: recall
      value: 0.9896907216494846
      name: Recall
    - type: average_precision
      value: 0.9940756358171561
      name: Average Precision
---

# CrossEncoder based on BAAI/bge-reranker-v2-m3

This is a [Cross Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html) model finetuned from [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3) using the [sentence-transformers](https://www.SBERT.net) library. It computes scores for pairs of texts, which can be used for text reranking and semantic search.

## Model Details

### Model Description
- **Model Type:** Cross Encoder
- **Base model:** [BAAI/bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3) <!-- at revision 953dc6f6f85a1b2dbfca4c34a2796e7dde08d41e -->
- **Maximum Sequence Length:** 512 tokens
- **Number of Output Labels:** 1 label
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
<!-- - **Language:** Unknown -->
<!-- - **License:** Unknown -->

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Documentation:** [Cross Encoder Documentation](https://www.sbert.net/docs/cross_encoder/usage/usage.html)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Cross Encoders on Hugging Face](https://huggingface.co/models?library=sentence-transformers&other=cross-encoder)

### Full Model Architecture

```
CrossEncoder(
  (0): Transformer({'transformer_task': 'sequence-classification', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'logits'}}, 'module_output_name': 'scores', 'architecture': 'XLMRobertaForSequenceClassification'})
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
from sentence_transformers import CrossEncoder

# Download from the 🤗 Hub
model = CrossEncoder("cross_encoder_model_id")
# Get scores for pairs of inputs
pairs = [
    ['Is there still a need for living-related liver transplantation in children?', 'To assess and compare the value of split-liver transplantation (SLT) and living-related liver transplantation (LRT). The concept of SLT results from the development of reduced-size transplantation. A further development of SLT, the in situ split technique, is derived from LRT, which itself marks the optimized outcome in terms of postoperative graft function and survival. The combination of SLT and LRT has abolished deaths on the waiting list, thus raising the question whether living donor liver transplantation is still necessary. Outcomes and postoperative liver function of 43 primary LRT patients were compared with those of 49 primary SLT patients (14 ex situ, 35 in situ) with known graft weight performed between April 1996 and December 2000. Survival rates were analyzed using the Kaplan-Meier method. After a median follow-up of 35 months, actual patient survival rates were 82% in the SLT group and 88% in the LRT group. Actual graft survival rates were 76% and 81%, respectively. The incidence of primary nonfunction was 12% in the SLT group and 2.3% in the LRT group. Liver function parameters (prothrombin time, factor V, bilirubin clearance) and surgical complication rates did not differ significantly. In the SLT group, mean cold ischemic time was longer than in the LRT group. Serum values of alanine aminotransferase during the first postoperative week were significantly higher in the SLT group. In the LRT group, there were more grafts with signs of fatty degeneration than in the SLT group.'],
    ['Landolt C and snellen e acuity: differences in strabismus amblyopia?', 'Assessment of visual acuity depends on the optotypes used for measurement. The ability to recognize different optotypes differs even if their critical details appear under the same visual angle. Since optotypes are evaluated on individuals with good visual acuity and without eye disorders, differences in the lower visual acuity range cannot be excluded. In this study, visual acuity measured with the Snellen E was compared to the Landolt C acuity. 100 patients (age 8 - 90 years, median 60.5 years) with various eye disorders, among them 39 with amblyopia due to strabismus, and 13 healthy volunteers were tested. Charts with the Snellen E and the Landolt C (Precision Vision) which mimic the ETDRS charts were used to assess visual acuity. Three out of 5 optotypes per line had to be correctly identified, while wrong answers were monitored. In the group of patients, the eyes with the lower visual acuity, and the right eyes of the healthy subjects, were evaluated. Differences between Landolt C acuity (LR) and Snellen E acuity (SE) were small. The mean decimal values for LR and SE were 0.25 and 0.29 in the entire group and 0.14 and 0.16 for the eyes with strabismus amblyopia. The mean difference between LR and SE was 0.55 lines in the entire group and 0.55 lines for the eyes with strabismus amblyopia, with higher values of SE in both groups. The results of the other groups were similar with only small differences between LR and SE.'],
    ["Can ki-67 play a role in prediction of breast cancer patients' response to neoadjuvant chemotherapy?", "Currently the choice of breast cancer therapy is based on prognostic factors. The proliferation marker Ki-67 is used increasingly to determine the method of therapy. The current study analyses the predictive value of Ki-67 in foreseeing breast cancer patients' responses to neoadjuvant chemotherapy. This study includes patients with invasive breast cancer treated between 2008 and 2013. The clinical response was assessed by correlating Ki-67 to histological examination, mammography, and ultrasonography findings. The average Ki-67 value in our patients collectively (n = 77) is 34.9 ± 24.6%. The average Ki-67 value is the highest with 37.4 ± 24.0% in patients with a pCR. The Ki-67 values do not differ significantly among the 3 groups: pCR versus partial pathological response versus stable disease/progress (P = 0.896). However, Ki-67 values of patients with luminal, Her2 enriched, and basal-like cancers differed significantly from each other. Furthermore, within the group of luminal tumors Ki-67 values of patients with versus without pCR also differed significantly."],
    ['Are lifetime prevalence of impetigo, molluscum and herpes infection really increased in children having atopic dermatitis?', "Cutaneous infections such as impetigo contagiosum (IC), molluscum contagiosum (MC) and herpes virus infection (HI) appear to be associated with atopic dermatitis (AD), but there are no reports of concrete epidemiological evidence. We evaluated the association of childhood AD with these infections by conducting a population-based cross-sectional study. Enrolled in this study were 1117 children aged 0-6 years old attending nursery schools in Ishigaki City, Okinawa Prefecture, Japan. Physical examination was performed by dermatologists, and a questionnaire was completed on each child's history of allergic diseases including AD, asthma, allergic rhinitis and egg allergy, and that of skin infections including IC, MC and HI, as well as familial history of AD. In 913 children (AD; 132), a history of IC, MC or HI was observed in 45.1%, 19.7%, and 2.5%, respectively. Multiple logistic regression analysis revealed that the odds of having a history of IC were 1.8 times higher in AD children than in non-AD children. Meanwhile, a history of MC was significantly correlated to the male gender, but not to a personal history of AD. As for HI, we found no correlated factors in this study."],
    ['Is digoxin use for cardiovascular disease associated with risk of prostate cancer?', 'Prostate-specific antigen (PSA) levels can show wide fluctuations when repeatedly measured. Here we investigatewd if: (a) biopsy timing influences the prostate cancer (PC) detection rate in patients with fluctuating PSA (flu-PSA) in comparison with patients with steadily increasing PSA (si-PSA); (b) PSA slope estimated in patients with flu-PSA predicts a different risk of cancer detection; (c) flu-PSA and si-PSA patients develop PC in topographically different sites; (d) the behaviour of pre-operative PSA is an expression of a disease with defferent characteristics to the following radical prostatectomy. The study involved 211 patients who underwent at least a second biopsy after a first negative prostate biopsy. PSA Slope, PSA velocity (PSAV) and PSA doubling time (PSADT) were estimated. Flu-PSA level was defined as a PSA series with at least one PSA value lower than the one immediately preceding it. 82 patients had flu-PSA levels and 129 si-PSA levels. There were no significant differences between the two groups in terms of cancer detection, clinical or pathological stage, but the si-PSA group with cancer had a higher Gleason score. No difference was found for PSA Slope between flu-PSA patients with cancer and those without.'],
]
scores = model.predict(pairs)
print(scores)
# [9.9997e-01 9.9999e-01 9.9999e-01 9.9999e-01 1.3233e-05]

# Or rank different texts based on similarity to a single text
ranks = model.rank(
    'Is there still a need for living-related liver transplantation in children?',
    [
        'To assess and compare the value of split-liver transplantation (SLT) and living-related liver transplantation (LRT). The concept of SLT results from the development of reduced-size transplantation. A further development of SLT, the in situ split technique, is derived from LRT, which itself marks the optimized outcome in terms of postoperative graft function and survival. The combination of SLT and LRT has abolished deaths on the waiting list, thus raising the question whether living donor liver transplantation is still necessary. Outcomes and postoperative liver function of 43 primary LRT patients were compared with those of 49 primary SLT patients (14 ex situ, 35 in situ) with known graft weight performed between April 1996 and December 2000. Survival rates were analyzed using the Kaplan-Meier method. After a median follow-up of 35 months, actual patient survival rates were 82% in the SLT group and 88% in the LRT group. Actual graft survival rates were 76% and 81%, respectively. The incidence of primary nonfunction was 12% in the SLT group and 2.3% in the LRT group. Liver function parameters (prothrombin time, factor V, bilirubin clearance) and surgical complication rates did not differ significantly. In the SLT group, mean cold ischemic time was longer than in the LRT group. Serum values of alanine aminotransferase during the first postoperative week were significantly higher in the SLT group. In the LRT group, there were more grafts with signs of fatty degeneration than in the SLT group.',
        'Assessment of visual acuity depends on the optotypes used for measurement. The ability to recognize different optotypes differs even if their critical details appear under the same visual angle. Since optotypes are evaluated on individuals with good visual acuity and without eye disorders, differences in the lower visual acuity range cannot be excluded. In this study, visual acuity measured with the Snellen E was compared to the Landolt C acuity. 100 patients (age 8 - 90 years, median 60.5 years) with various eye disorders, among them 39 with amblyopia due to strabismus, and 13 healthy volunteers were tested. Charts with the Snellen E and the Landolt C (Precision Vision) which mimic the ETDRS charts were used to assess visual acuity. Three out of 5 optotypes per line had to be correctly identified, while wrong answers were monitored. In the group of patients, the eyes with the lower visual acuity, and the right eyes of the healthy subjects, were evaluated. Differences between Landolt C acuity (LR) and Snellen E acuity (SE) were small. The mean decimal values for LR and SE were 0.25 and 0.29 in the entire group and 0.14 and 0.16 for the eyes with strabismus amblyopia. The mean difference between LR and SE was 0.55 lines in the entire group and 0.55 lines for the eyes with strabismus amblyopia, with higher values of SE in both groups. The results of the other groups were similar with only small differences between LR and SE.',
        "Currently the choice of breast cancer therapy is based on prognostic factors. The proliferation marker Ki-67 is used increasingly to determine the method of therapy. The current study analyses the predictive value of Ki-67 in foreseeing breast cancer patients' responses to neoadjuvant chemotherapy. This study includes patients with invasive breast cancer treated between 2008 and 2013. The clinical response was assessed by correlating Ki-67 to histological examination, mammography, and ultrasonography findings. The average Ki-67 value in our patients collectively (n = 77) is 34.9 ± 24.6%. The average Ki-67 value is the highest with 37.4 ± 24.0% in patients with a pCR. The Ki-67 values do not differ significantly among the 3 groups: pCR versus partial pathological response versus stable disease/progress (P = 0.896). However, Ki-67 values of patients with luminal, Her2 enriched, and basal-like cancers differed significantly from each other. Furthermore, within the group of luminal tumors Ki-67 values of patients with versus without pCR also differed significantly.",
        "Cutaneous infections such as impetigo contagiosum (IC), molluscum contagiosum (MC) and herpes virus infection (HI) appear to be associated with atopic dermatitis (AD), but there are no reports of concrete epidemiological evidence. We evaluated the association of childhood AD with these infections by conducting a population-based cross-sectional study. Enrolled in this study were 1117 children aged 0-6 years old attending nursery schools in Ishigaki City, Okinawa Prefecture, Japan. Physical examination was performed by dermatologists, and a questionnaire was completed on each child's history of allergic diseases including AD, asthma, allergic rhinitis and egg allergy, and that of skin infections including IC, MC and HI, as well as familial history of AD. In 913 children (AD; 132), a history of IC, MC or HI was observed in 45.1%, 19.7%, and 2.5%, respectively. Multiple logistic regression analysis revealed that the odds of having a history of IC were 1.8 times higher in AD children than in non-AD children. Meanwhile, a history of MC was significantly correlated to the male gender, but not to a personal history of AD. As for HI, we found no correlated factors in this study.",
        'Prostate-specific antigen (PSA) levels can show wide fluctuations when repeatedly measured. Here we investigatewd if: (a) biopsy timing influences the prostate cancer (PC) detection rate in patients with fluctuating PSA (flu-PSA) in comparison with patients with steadily increasing PSA (si-PSA); (b) PSA slope estimated in patients with flu-PSA predicts a different risk of cancer detection; (c) flu-PSA and si-PSA patients develop PC in topographically different sites; (d) the behaviour of pre-operative PSA is an expression of a disease with defferent characteristics to the following radical prostatectomy. The study involved 211 patients who underwent at least a second biopsy after a first negative prostate biopsy. PSA Slope, PSA velocity (PSAV) and PSA doubling time (PSADT) were estimated. Flu-PSA level was defined as a PSA series with at least one PSA value lower than the one immediately preceding it. 82 patients had flu-PSA levels and 129 si-PSA levels. There were no significant differences between the two groups in terms of cancer detection, clinical or pathological stage, but the si-PSA group with cancer had a higher Gleason score. No difference was found for PSA Slope between flu-PSA patients with cancer and those without.',
    ]
)
# [{'corpus_id': ..., 'score': ...}, {'corpus_id': ..., 'score': ...}, ...]
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

## Evaluation

### Metrics

#### Cross Encoder Binary Classification

* Dataset: `pubmed-val`
* Evaluated with [<code>CEBinaryClassificationEvaluator</code>](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CEBinaryClassificationEvaluator)

| Metric                | Value      |
|:----------------------|:-----------|
| accuracy              | 0.97       |
| accuracy_threshold    | 0.0002     |
| f1                    | 0.9697     |
| f1_threshold          | 0.0001     |
| precision             | 0.9505     |
| recall                | 0.9897     |
| **average_precision** | **0.9941** |

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

* Size: 1,800 training samples
* Columns: <code>sentence_0</code>, <code>sentence_1</code>, and <code>label</code>
* Approximate statistics based on the first 1000 samples:
  |         | sentence_0                                                                        | sentence_1                                                                           | label                                                          |
  |:--------|:----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:---------------------------------------------------------------|
  | type    | string                                                                            | string                                                                               | float                                                          |
  | details | <ul><li>min: 9 tokens</li><li>mean: 24.29 tokens</li><li>max: 61 tokens</li></ul> | <ul><li>min: 73 tokens</li><li>mean: 322.08 tokens</li><li>max: 512 tokens</li></ul> | <ul><li>min: 0.0</li><li>mean: 0.52</li><li>max: 1.0</li></ul> |
* Samples:
  | sentence_0                                                                                                        | sentence_1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               | label            |
  |:------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-----------------|
  | <code>Is there still a need for living-related liver transplantation in children?</code>                          | <code>To assess and compare the value of split-liver transplantation (SLT) and living-related liver transplantation (LRT). The concept of SLT results from the development of reduced-size transplantation. A further development of SLT, the in situ split technique, is derived from LRT, which itself marks the optimized outcome in terms of postoperative graft function and survival. The combination of SLT and LRT has abolished deaths on the waiting list, thus raising the question whether living donor liver transplantation is still necessary. Outcomes and postoperative liver function of 43 primary LRT patients were compared with those of 49 primary SLT patients (14 ex situ, 35 in situ) with known graft weight performed between April 1996 and December 2000. Survival rates were analyzed using the Kaplan-Meier method. After a median follow-up of 35 months, actual patient survival rates were 82% in the SLT group and 88% in the LRT group. Actual graft survival rates were 76% and 81%, respectively. The i...</code> | <code>1.0</code> |
  | <code>Landolt C and snellen e acuity: differences in strabismus amblyopia?</code>                                 | <code>Assessment of visual acuity depends on the optotypes used for measurement. The ability to recognize different optotypes differs even if their critical details appear under the same visual angle. Since optotypes are evaluated on individuals with good visual acuity and without eye disorders, differences in the lower visual acuity range cannot be excluded. In this study, visual acuity measured with the Snellen E was compared to the Landolt C acuity. 100 patients (age 8 - 90 years, median 60.5 years) with various eye disorders, among them 39 with amblyopia due to strabismus, and 13 healthy volunteers were tested. Charts with the Snellen E and the Landolt C (Precision Vision) which mimic the ETDRS charts were used to assess visual acuity. Three out of 5 optotypes per line had to be correctly identified, while wrong answers were monitored. In the group of patients, the eyes with the lower visual acuity, and the right eyes of the healthy subjects, were evaluated. Differences between Landolt C...</code> | <code>1.0</code> |
  | <code>Can ki-67 play a role in prediction of breast cancer patients' response to neoadjuvant chemotherapy?</code> | <code>Currently the choice of breast cancer therapy is based on prognostic factors. The proliferation marker Ki-67 is used increasingly to determine the method of therapy. The current study analyses the predictive value of Ki-67 in foreseeing breast cancer patients' responses to neoadjuvant chemotherapy. This study includes patients with invasive breast cancer treated between 2008 and 2013. The clinical response was assessed by correlating Ki-67 to histological examination, mammography, and ultrasonography findings. The average Ki-67 value in our patients collectively (n = 77) is 34.9 ± 24.6%. The average Ki-67 value is the highest with 37.4 ± 24.0% in patients with a pCR. The Ki-67 values do not differ significantly among the 3 groups: pCR versus partial pathological response versus stable disease/progress (P = 0.896). However, Ki-67 values of patients with luminal, Her2 enriched, and basal-like cancers differed significantly from each other. Furthermore, within the group of luminal tumors ...</code> | <code>1.0</code> |
* Loss: [<code>BinaryCrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#binarycrossentropyloss) with these parameters:
  ```json
  {
      "activation_fn": "torch.nn.modules.linear.Identity",
      "pos_weight": null
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 4

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `do_predict`: False
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 4
- `per_device_eval_batch_size`: 4
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
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss | pubmed-val_average_precision |
|:------:|:----:|:-------------:|:----------------------------:|
| 1.0    | 450  | -             | 0.9933                       |
| 1.1111 | 500  | 0.1448        | 0.9937                       |
| 2.0    | 900  | -             | 0.9951                       |
| 2.2222 | 1000 | 0.0361        | 0.9941                       |


### Training Time
- **Training**: 23.4 minutes

### Framework Versions
- Python: 3.12.13
- Sentence Transformers: 5.4.1
- Transformers: 5.0.0
- PyTorch: 2.10.0+cu128
- Accelerate: 1.13.0
- Datasets: 4.0.0
- Tokenizers: 0.22.2

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