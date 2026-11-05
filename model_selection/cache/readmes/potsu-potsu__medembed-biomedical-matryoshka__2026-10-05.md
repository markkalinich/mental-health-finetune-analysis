---
language:
- en
license: apache-2.0
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- generated_from_trainer
- dataset_size:4012
- loss:MatryoshkaLoss
- loss:MultipleNegativesRankingLoss
base_model: abhinand/MedEmbed-small-v0.1
widget:
- source_sentence: Do cephalopods use RNA editing less frequently than other species?
  sentences:
  - 'Extensive messenger RNA editing generates transcript and protein diversity in
    genes involved in neural excitability, as previously described, as well as in
    genes participating in a broad range of other cellular functions. '
  - GV1001 is a 16-amino-acid vaccine peptide derived from the human telomerase reverse
    transcriptase sequence. It has been developed as a vaccine against various cancers.
  - Using acetyl-specific K516 antibodies, we show that acetylation of endogenous
    S6K1 at this site is potently induced upon growth factor stimulation. We propose
    that K516 acetylation may serve to modulate important kinase-independent functions
    of S6K1 in response to growth factor signalling. Following mitogen stimulation,
    S6Ks interact with the p300 and p300/CBP-associated factor (PCAF) acetyltransferases.
    S6Ks can be acetylated by p300 and PCAF in vitro and S6K acetylation is detected
    in cells expressing p300
- source_sentence: Can pets affect infant microbiomed?
  sentences:
  - Yes, exposure to household furry pets influences the gut microbiota of infants.
  - Thiazovivin is a selective small molecule that directly targets Rho-associated
    kinase (ROCK) and increases expression of pluripotency factors.
  - ' Here, we present evidence that the calcium/calmodulin-dependent protein kinase
    IV (CaMK4) is increased and required during Th17 cell differentiation. Inhibition
    of CaMK4 reduced Il17 transcription through decreased activation of the cAMP response
    element modulator a (CREM-a) and reduced activation of the AKT/mTOR pathway, which
    is known to enhance Th17 differentiation. CAMK4 knockdown and kinase-dead mutant
    inhibited crocin-mediated HO-1 expression, Nrf2 activation, and phosphorylation
    of Akt, indicating that HO-1 expression is mediated by CAMK4 and that Akt is a
    downstream mediator of CAMK4 in crocin signaling'
- source_sentence: In what proportion of children with heart failure has Enalapril
    been shown to be safe and effective?
  sentences:
  - 5-HT2A (5-hydroxytryptamine type 2a) receptor can be evaluated with the [18F]altanserin.
  - "In children with heart failure evidence of the effect of enalapril is empirical.\
    \ Enalapril was clinically safe and effective in 50% to 80% of for children with\
    \ cardiac failure secondary to congenital heart malformations before and after\
    \ cardiac surgery,  impaired ventricular function , valvar regurgitation,  congestive\
    \ cardiomyopathy,  , arterial hypertension, life-threatening arrhythmias coexisting\
    \ with circulatory insufficiency.   \nACE inhibitors have shown a transient beneficial\
    \ effect on heart failure due to anticancer drugs and possibly a beneficial effect\
    \ in muscular dystrophy-associated cardiomyopathy, which deserves further studies."
  - "necroptosis\napoptosis  \npro-survival/inflammation NF-κB activation"
- source_sentence: How are SAHFS created?
  sentences:
  - In particular, up to 17% of neutrophil nuclei of healthy women exhibit a drumstick-shaped
    appendage that contains the inactive X chromosome.
  - miR-1, miR-133, miR-208a, miR-206, miR-494, miR-146a, miR-222, miR-21, miR-221,
    miR-20a, miR-133a, miR-133b, miR-23, miR-107 and miR-181 are involved in exercise
    adaptation
  - Cellular senescence-associated heterochromatic foci (SAHFS) are a novel type of
    chromatin condensation involving alterations of linker histone H1 and linker DNA-binding
    proteins. SAHFS can be formed by a variety of cell types, but their mechanism
    of action remains unclear.
- source_sentence: What are the effects of the deletion of all three Pcdh clusters
    (tricluster deletion) in mice?
  sentences:
  - Multicluster Pcdh diversity is required for mouse olfactory neural circuit assembly.
    The vertebrate clustered protocadherin (Pcdh) cell surface proteins are encoded
    by three closely linked gene clusters (Pcdhα, Pcdhβ, and Pcdhγ). Although deletion
    of individual Pcdh clusters had subtle phenotypic consequences, the loss of all
    three clusters (tricluster deletion) led to a severe axonal arborization defect
    and loss of self-avoidance.
  - The myocyte enhancer factor-2 (MEF2) proteins are MADS-box transcription factors
    that are essential for differentiation of all muscle lineages but their mechanisms
    of action remain largely undefined. MEF2C expression initiates cardiomyogenesis,
    resulting in the up-regulation of Brachyury T, bone morphogenetic protein-4, Nkx2-5,
    GATA-4, cardiac alpha-actin, and myosin heavy chain expression. Inactivation of
    the MEF2C gene causes cardiac developmental arrest and severe downregulation of
    a number of cardiac markers including atrial natriuretic factor (ANF). BMP-2,
    a regulator of cardiac development during embryogenesis, was shown to increase
    PI 3-kinase activity in cardiac precursor cells, resulting in increased expression
    of sarcomeric myosin heavy chain (MHC) and MEF-2A. Furthermore, expression of
    MEF-2A increased MHC expression in a PI 3-kinase-dependent manner. Other studies
    showed that Gli2 and MEF2C proteins form a complex, capable of synergizing on
    cardiomyogenesis-related promoters. Dominant interference of calcineurin/mAKAP
    binding blunts the increase in MEF2 transcriptional activity seen during myoblast
    differentiation, as well as the expression of endogenous MEF2-target genes. These
    findings show that MEF-2 can direct early stages of cell differentiation into
    a cardiomyogenic pathway.
  - Investigators proposed that there have been three extended periods in the evolution
    of gene regulatory elements. Early vertebrate evolution was characterized by regulatory
    gains near transcription factors and developmental genes, but this trend was replaced
    by innovations near extracellular signaling genes, and then innovations near posttranslational
    protein modifiers.
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
- cosine_accuracy@1
- cosine_accuracy@3
- cosine_accuracy@5
- cosine_accuracy@10
- cosine_precision@1
- cosine_precision@3
- cosine_precision@5
- cosine_precision@10
- cosine_recall@1
- cosine_recall@3
- cosine_recall@5
- cosine_recall@10
- cosine_ndcg@10
- cosine_mrr@10
- cosine_map@100
model-index:
- name: MedEmbed Biomedical MRL
  results:
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 384
      type: dim_384
    metrics:
    - type: cosine_accuracy@1
      value: 0.743988684582744
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.8528995756718529
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8811881188118812
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9165487977369166
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.743988684582744
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.5879302215935879
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.5083451202263083
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.39264497878359267
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.22864925036303255
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.38726014665705066
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.47265511620109374
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.5956514777654228
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.682960418351343
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.8061196425765028
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.605512208394002
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 256
      type: dim_256
    metrics:
    - type: cosine_accuracy@1
      value: 0.7383309759547383
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.8486562942008486
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8698727015558698
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.9066478076379066
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.7383309759547383
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.5851013672795851
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.49589816124469593
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.38500707213578506
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.2258018493225622
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.3831143517659884
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.46043165645745454
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.5802246010255446
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.6702777283455285
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.7981118520015267
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.593002873023239
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 128
      type: dim_128
    metrics:
    - type: cosine_accuracy@1
      value: 0.7185289957567186
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.8302687411598303
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8642149929278642
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.8953323903818954
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.7185289957567186
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.5596416784535597
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.4746817538896747
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.36605374823196607
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.21741492026039794
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.3643446931786265
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.4415110089630148
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.5535910093833504
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.6417304469454738
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.7807463909656271
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.5556071606830145
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 64
      type: dim_64
    metrics:
    - type: cosine_accuracy@1
      value: 0.6534653465346535
      name: Cosine Accuracy@1
    - type: cosine_accuracy@3
      value: 0.7765205091937766
      name: Cosine Accuracy@3
    - type: cosine_accuracy@5
      value: 0.8118811881188119
      name: Cosine Accuracy@5
    - type: cosine_accuracy@10
      value: 0.842998585572843
      name: Cosine Accuracy@10
    - type: cosine_precision@1
      value: 0.6534653465346535
      name: Cosine Precision@1
    - type: cosine_precision@3
      value: 0.49882131070249874
      name: Cosine Precision@3
    - type: cosine_precision@5
      value: 0.42574257425742584
      name: Cosine Precision@5
    - type: cosine_precision@10
      value: 0.3258840169731259
      name: Cosine Precision@10
    - type: cosine_recall@1
      value: 0.19782326300239175
      name: Cosine Recall@1
    - type: cosine_recall@3
      value: 0.32007460761434003
      name: Cosine Recall@3
    - type: cosine_recall@5
      value: 0.38490547346807885
      name: Cosine Recall@5
    - type: cosine_recall@10
      value: 0.4811566314336906
      name: Cosine Recall@10
    - type: cosine_ndcg@10
      value: 0.5700147989809387
      name: Cosine Ndcg@10
    - type: cosine_mrr@10
      value: 0.7207000291865919
      name: Cosine Mrr@10
    - type: cosine_map@100
      value: 0.4772717799101714
      name: Cosine Map@100
---

# MedEmbed Biomedical MRL

This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [abhinand/MedEmbed-small-v0.1](https://huggingface.co/abhinand/MedEmbed-small-v0.1) on the json dataset. It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [abhinand/MedEmbed-small-v0.1](https://huggingface.co/abhinand/MedEmbed-small-v0.1) <!-- at revision 40a5850d046cfdb56154e332b4d7099b63e8d50e -->
- **Maximum Sequence Length:** 512 tokens
- **Output Dimensionality:** 384 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - json
- **Language:** en
- **License:** apache-2.0

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/UKPLab/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 512, 'do_lower_case': False}) with Transformer model: BertModel 
  (1): Pooling({'word_embedding_dimension': 384, 'pooling_mode_cls_token': True, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': False, 'include_prompt': True})
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
model = SentenceTransformer("potsu-potsu/medembed-biomedical-matryoshka")
# Run inference
sentences = [
    'What are the effects of the deletion of all three Pcdh clusters (tricluster deletion) in mice?',
    'Multicluster Pcdh diversity is required for mouse olfactory neural circuit assembly. The vertebrate clustered protocadherin (Pcdh) cell surface proteins are encoded by three closely linked gene clusters (Pcdhα, Pcdhβ, and Pcdhγ). Although deletion of individual Pcdh clusters had subtle phenotypic consequences, the loss of all three clusters (tricluster deletion) led to a severe axonal arborization defect and loss of self-avoidance.',
    'Investigators proposed that there have been three extended periods in the evolution of gene regulatory elements. Early vertebrate evolution was characterized by regulatory gains near transcription factors and developmental genes, but this trend was replaced by innovations near extracellular signaling genes, and then innovations near posttranslational protein modifiers.',
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

## Evaluation

### Metrics

#### Information Retrieval

* Dataset: `dim_384`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator) with these parameters:
  ```json
  {
      "truncate_dim": 384
  }
  ```

| Metric              | Value     |
|:--------------------|:----------|
| cosine_accuracy@1   | 0.744     |
| cosine_accuracy@3   | 0.8529    |
| cosine_accuracy@5   | 0.8812    |
| cosine_accuracy@10  | 0.9165    |
| cosine_precision@1  | 0.744     |
| cosine_precision@3  | 0.5879    |
| cosine_precision@5  | 0.5083    |
| cosine_precision@10 | 0.3926    |
| cosine_recall@1     | 0.2286    |
| cosine_recall@3     | 0.3873    |
| cosine_recall@5     | 0.4727    |
| cosine_recall@10    | 0.5957    |
| **cosine_ndcg@10**  | **0.683** |
| cosine_mrr@10       | 0.8061    |
| cosine_map@100      | 0.6055    |

#### Information Retrieval

* Dataset: `dim_256`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator) with these parameters:
  ```json
  {
      "truncate_dim": 256
  }
  ```

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.7383     |
| cosine_accuracy@3   | 0.8487     |
| cosine_accuracy@5   | 0.8699     |
| cosine_accuracy@10  | 0.9066     |
| cosine_precision@1  | 0.7383     |
| cosine_precision@3  | 0.5851     |
| cosine_precision@5  | 0.4959     |
| cosine_precision@10 | 0.385      |
| cosine_recall@1     | 0.2258     |
| cosine_recall@3     | 0.3831     |
| cosine_recall@5     | 0.4604     |
| cosine_recall@10    | 0.5802     |
| **cosine_ndcg@10**  | **0.6703** |
| cosine_mrr@10       | 0.7981     |
| cosine_map@100      | 0.593      |

#### Information Retrieval

* Dataset: `dim_128`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator) with these parameters:
  ```json
  {
      "truncate_dim": 128
  }
  ```

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@1   | 0.7185     |
| cosine_accuracy@3   | 0.8303     |
| cosine_accuracy@5   | 0.8642     |
| cosine_accuracy@10  | 0.8953     |
| cosine_precision@1  | 0.7185     |
| cosine_precision@3  | 0.5596     |
| cosine_precision@5  | 0.4747     |
| cosine_precision@10 | 0.3661     |
| cosine_recall@1     | 0.2174     |
| cosine_recall@3     | 0.3643     |
| cosine_recall@5     | 0.4415     |
| cosine_recall@10    | 0.5536     |
| **cosine_ndcg@10**  | **0.6417** |
| cosine_mrr@10       | 0.7807     |
| cosine_map@100      | 0.5556     |

#### Information Retrieval

* Dataset: `dim_64`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator) with these parameters:
  ```json
  {
      "truncate_dim": 64
  }
  ```

| Metric              | Value    |
|:--------------------|:---------|
| cosine_accuracy@1   | 0.6535   |
| cosine_accuracy@3   | 0.7765   |
| cosine_accuracy@5   | 0.8119   |
| cosine_accuracy@10  | 0.843    |
| cosine_precision@1  | 0.6535   |
| cosine_precision@3  | 0.4988   |
| cosine_precision@5  | 0.4257   |
| cosine_precision@10 | 0.3259   |
| cosine_recall@1     | 0.1978   |
| cosine_recall@3     | 0.3201   |
| cosine_recall@5     | 0.3849   |
| cosine_recall@10    | 0.4812   |
| **cosine_ndcg@10**  | **0.57** |
| cosine_mrr@10       | 0.7207   |
| cosine_map@100      | 0.4773   |

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

#### json

* Dataset: json
* Size: 4,012 training samples
* Columns: <code>anchor</code> and <code>positive</code>
* Approximate statistics based on the first 1000 samples:
  |         | anchor                                                                            | positive                                                                           |
  |:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                             |
  | details | <ul><li>min: 5 tokens</li><li>mean: 16.13 tokens</li><li>max: 49 tokens</li></ul> | <ul><li>min: 3 tokens</li><li>mean: 63.38 tokens</li><li>max: 485 tokens</li></ul> |
* Samples:
  | anchor                                                                                 | positive                                                                                                                                                                                                                                                                                                                                                                      |
  |:---------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>What is the implication of histone lysine methylation in medulloblastoma?</code> | <code>Aberrant patterns of H3K4, H3K9, and H3K27 histone lysine methylation were shown to result in histone code alterations, which induce changes in gene expression, and affect the proliferation rate of cells in medulloblastoma.</code>                                                                                                                                  |
  | <code>What is the role of STAG1/STAG2 proteins in differentiation?</code>              | <code>STAG1/STAG2 proteins are tumour suppressor proteins that suppress cell proliferation and are essential for differentiation.</code>                                                                                                                                                                                                                                      |
  | <code>What is the association between cell phone use and glioblastoma?</code>          | <code>The association between cell phone use and incident glioblastoma remains unclear. Some studies have reported that cell phone use was associated with incident glioblastoma, and with reduced survival of patients diagnosed with glioblastoma. However, other studies have repeatedly replicated to find an association between cell phone use and glioblastoma.</code> |
* Loss: [<code>MatryoshkaLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#matryoshkaloss) with these parameters:
  ```json
  {
      "loss": "MultipleNegativesRankingLoss",
      "matryoshka_dims": [
          384,
          256,
          128,
          64
      ],
      "matryoshka_weights": [
          1,
          1,
          1,
          1
      ],
      "n_dims_per_step": -1
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: epoch
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 16
- `gradient_accumulation_steps`: 16
- `learning_rate`: 2e-05
- `num_train_epochs`: 4
- `lr_scheduler_type`: cosine
- `warmup_ratio`: 0.1
- `bf16`: True
- `tf32`: True
- `load_best_model_at_end`: True
- `optim`: adamw_torch_fused
- `batch_sampler`: no_duplicates

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `overwrite_output_dir`: False
- `do_predict`: False
- `eval_strategy`: epoch
- `prediction_loss_only`: True
- `per_device_train_batch_size`: 32
- `per_device_eval_batch_size`: 16
- `per_gpu_train_batch_size`: None
- `per_gpu_eval_batch_size`: None
- `gradient_accumulation_steps`: 16
- `eval_accumulation_steps`: None
- `torch_empty_cache_steps`: None
- `learning_rate`: 2e-05
- `weight_decay`: 0.0
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `max_grad_norm`: 1.0
- `num_train_epochs`: 4
- `max_steps`: -1
- `lr_scheduler_type`: cosine
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
- `bf16`: True
- `fp16`: False
- `fp16_opt_level`: O1
- `half_precision_backend`: auto
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: True
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
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `fsdp`: []
- `fsdp_min_num_params`: 0
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `fsdp_transformer_layer_cls_to_wrap`: None
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
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
- `batch_sampler`: no_duplicates
- `multi_dataset_batch_sampler`: proportional

</details>

### Training Logs
| Epoch   | Step  | Training Loss | dim_384_cosine_ndcg@10 | dim_256_cosine_ndcg@10 | dim_128_cosine_ndcg@10 | dim_64_cosine_ndcg@10 |
|:-------:|:-----:|:-------------:|:----------------------:|:----------------------:|:----------------------:|:---------------------:|
| **1.0** | **8** | **-**         | **0.6901**             | **0.6798**             | **0.6423**             | **0.5441**            |
| 1.2540  | 10    | 30.5425       | -                      | -                      | -                      | -                     |
| 2.0     | 16    | -             | 0.6840                 | 0.6745                 | 0.6421                 | 0.5656                |
| 2.5079  | 20    | 15.0158       | -                      | -                      | -                      | -                     |
| 3.0     | 24    | -             | 0.6819                 | 0.6714                 | 0.6416                 | 0.5689                |
| 3.7619  | 30    | 12.3285       | -                      | -                      | -                      | -                     |
| 4.0     | 32    | -             | 0.6830                 | 0.6703                 | 0.6417                 | 0.5700                |

* The bold row denotes the saved checkpoint.

### Framework Versions
- Python: 3.12.5
- Sentence Transformers: 4.1.0
- Transformers: 4.52.4
- PyTorch: 2.7.1+cu128
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

#### MatryoshkaLoss
```bibtex
@misc{kusupati2024matryoshka,
    title={Matryoshka Representation Learning},
    author={Aditya Kusupati and Gantavya Bhatt and Aniket Rege and Matthew Wallingford and Aditya Sinha and Vivek Ramanujan and William Howard-Snyder and Kaifeng Chen and Sham Kakade and Prateek Jain and Ali Farhadi},
    year={2024},
    eprint={2205.13147},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
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