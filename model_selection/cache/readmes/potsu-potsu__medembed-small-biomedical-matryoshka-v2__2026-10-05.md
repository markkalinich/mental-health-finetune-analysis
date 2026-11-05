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
- cosine_accuracy@10
- cosine_accuracy@15
- cosine_accuracy@20
- cosine_accuracy@25
- cosine_accuracy@30
- cosine_precision@10
- cosine_precision@15
- cosine_precision@20
- cosine_precision@25
- cosine_precision@30
- cosine_recall@10
- cosine_recall@15
- cosine_recall@20
- cosine_recall@25
- cosine_recall@30
- cosine_ndcg@10
- cosine_ndcg@20
- cosine_ndcg@30
- cosine_mrr@10
- cosine_mrr@20
- cosine_mrr@30
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
    - type: cosine_accuracy@10
      value: 0.9165487977369166
      name: Cosine Accuracy@10
    - type: cosine_accuracy@15
      value: 0.9264497878359265
      name: Cosine Accuracy@15
    - type: cosine_accuracy@20
      value: 0.9335219236209336
      name: Cosine Accuracy@20
    - type: cosine_accuracy@25
      value: 0.9377652050919377
      name: Cosine Accuracy@25
    - type: cosine_accuracy@30
      value: 0.9405940594059405
      name: Cosine Accuracy@30
    - type: cosine_precision@10
      value: 0.39080622347949084
      name: Cosine Precision@10
    - type: cosine_precision@15
      value: 0.3223008015087223
      name: Cosine Precision@15
    - type: cosine_precision@20
      value: 0.27128712871287125
      name: Cosine Precision@20
    - type: cosine_precision@25
      value: 0.23383309759547385
      name: Cosine Precision@25
    - type: cosine_precision@30
      value: 0.20495049504950497
      name: Cosine Precision@30
    - type: cosine_recall@10
      value: 0.5941961725539775
      name: Cosine Recall@10
    - type: cosine_recall@15
      value: 0.6588459266002943
      name: Cosine Recall@15
    - type: cosine_recall@20
      value: 0.6987845481366459
      name: Cosine Recall@20
    - type: cosine_recall@25
      value: 0.7271263980909579
      name: Cosine Recall@25
    - type: cosine_recall@30
      value: 0.7470648467155192
      name: Cosine Recall@30
    - type: cosine_ndcg@10
      value: 0.6798281187519497
      name: Cosine Ndcg@10
    - type: cosine_ndcg@20
      value: 0.6888607498626206
      name: Cosine Ndcg@20
    - type: cosine_ndcg@30
      value: 0.7001398203922595
      name: Cosine Ndcg@30
    - type: cosine_mrr@10
      value: 0.7992041040838778
      name: Cosine Mrr@10
    - type: cosine_mrr@20
      value: 0.8003780682112908
      name: Cosine Mrr@20
    - type: cosine_mrr@30
      value: 0.8006679370996576
      name: Cosine Mrr@30
    - type: cosine_map@100
      value: 0.6024888601083165
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 256
      type: dim_256
    metrics:
    - type: cosine_accuracy@10
      value: 0.9137199434229137
      name: Cosine Accuracy@10
    - type: cosine_accuracy@15
      value: 0.9207920792079208
      name: Cosine Accuracy@15
    - type: cosine_accuracy@20
      value: 0.9306930693069307
      name: Cosine Accuracy@20
    - type: cosine_accuracy@25
      value: 0.9335219236209336
      name: Cosine Accuracy@25
    - type: cosine_accuracy@30
      value: 0.942008486562942
      name: Cosine Accuracy@30
    - type: cosine_precision@10
      value: 0.3857142857142857
      name: Cosine Precision@10
    - type: cosine_precision@15
      value: 0.31730315888731736
      name: Cosine Precision@15
    - type: cosine_precision@20
      value: 0.2668316831683168
      name: Cosine Precision@20
    - type: cosine_precision@25
      value: 0.22975954738330975
      name: Cosine Precision@25
    - type: cosine_precision@30
      value: 0.20146157472890147
      name: Cosine Precision@30
    - type: cosine_recall@10
      value: 0.5815816835128447
      name: Cosine Recall@10
    - type: cosine_recall@15
      value: 0.6466693808855584
      name: Cosine Recall@15
    - type: cosine_recall@20
      value: 0.6870196160066245
      name: Cosine Recall@20
    - type: cosine_recall@25
      value: 0.7141879792489384
      name: Cosine Recall@25
    - type: cosine_recall@30
      value: 0.7385183365425335
      name: Cosine Recall@30
    - type: cosine_ndcg@10
      value: 0.6685061016322212
      name: Cosine Ndcg@10
    - type: cosine_ndcg@20
      value: 0.6771324435869726
      name: Cosine Ndcg@20
    - type: cosine_ndcg@30
      value: 0.6890384560552142
      name: Cosine Ndcg@30
    - type: cosine_mrr@10
      value: 0.7910211939561302
      name: Cosine Mrr@10
    - type: cosine_mrr@20
      value: 0.7921511051985389
      name: Cosine Mrr@20
    - type: cosine_mrr@30
      value: 0.792585727544801
      name: Cosine Mrr@30
    - type: cosine_map@100
      value: 0.5894036821514587
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 128
      type: dim_128
    metrics:
    - type: cosine_accuracy@10
      value: 0.8925035360678925
      name: Cosine Accuracy@10
    - type: cosine_accuracy@15
      value: 0.9108910891089109
      name: Cosine Accuracy@15
    - type: cosine_accuracy@20
      value: 0.9137199434229137
      name: Cosine Accuracy@20
    - type: cosine_accuracy@25
      value: 0.917963224893918
      name: Cosine Accuracy@25
    - type: cosine_accuracy@30
      value: 0.9264497878359265
      name: Cosine Accuracy@30
    - type: cosine_precision@10
      value: 0.3652050919377653
      name: Cosine Precision@10
    - type: cosine_precision@15
      value: 0.30061291843470067
      name: Cosine Precision@15
    - type: cosine_precision@20
      value: 0.25212164073550214
      name: Cosine Precision@20
    - type: cosine_precision@25
      value: 0.21652050919377655
      name: Cosine Precision@25
    - type: cosine_precision@30
      value: 0.1898161244695898
      name: Cosine Precision@30
    - type: cosine_recall@10
      value: 0.5512769672278892
      name: Cosine Recall@10
    - type: cosine_recall@15
      value: 0.6154662290501166
      name: Cosine Recall@15
    - type: cosine_recall@20
      value: 0.6485567681988598
      name: Cosine Recall@20
    - type: cosine_recall@25
      value: 0.6719245680679413
      name: Cosine Recall@25
    - type: cosine_recall@30
      value: 0.6908677707954165
      name: Cosine Recall@30
    - type: cosine_ndcg@10
      value: 0.6398051423289486
      name: Cosine Ndcg@10
    - type: cosine_ndcg@20
      value: 0.6456353921240615
      name: Cosine Ndcg@20
    - type: cosine_ndcg@30
      value: 0.6547564254914449
      name: Cosine Ndcg@30
    - type: cosine_mrr@10
      value: 0.7783401809568713
      name: Cosine Mrr@10
    - type: cosine_mrr@20
      value: 0.779954730744106
      name: Cosine Mrr@20
    - type: cosine_mrr@30
      value: 0.7804545296760538
      name: Cosine Mrr@30
    - type: cosine_map@100
      value: 0.5533539437575846
      name: Cosine Map@100
  - task:
      type: information-retrieval
      name: Information Retrieval
    dataset:
      name: dim 64
      type: dim_64
    metrics:
    - type: cosine_accuracy@10
      value: 0.8458274398868458
      name: Cosine Accuracy@10
    - type: cosine_accuracy@15
      value: 0.8642149929278642
      name: Cosine Accuracy@15
    - type: cosine_accuracy@20
      value: 0.8755304101838756
      name: Cosine Accuracy@20
    - type: cosine_accuracy@25
      value: 0.8769448373408769
      name: Cosine Accuracy@25
    - type: cosine_accuracy@30
      value: 0.8854314002828855
      name: Cosine Accuracy@30
    - type: cosine_precision@10
      value: 0.32673267326732675
      name: Cosine Precision@10
    - type: cosine_precision@15
      value: 0.2663837812352664
      name: Cosine Precision@15
    - type: cosine_precision@20
      value: 0.22446958981612444
      name: Cosine Precision@20
    - type: cosine_precision@25
      value: 0.19224893917963226
      name: Cosine Precision@25
    - type: cosine_precision@30
      value: 0.16864686468646864
      name: Cosine Precision@30
    - type: cosine_recall@10
      value: 0.4845924963940586
      name: Cosine Recall@10
    - type: cosine_recall@15
      value: 0.5380506278500925
      name: Cosine Recall@15
    - type: cosine_recall@20
      value: 0.5767274907725523
      name: Cosine Recall@20
    - type: cosine_recall@25
      value: 0.597395783619348
      name: Cosine Recall@25
    - type: cosine_recall@30
      value: 0.6174419090464666
      name: Cosine Recall@30
    - type: cosine_ndcg@10
      value: 0.5695803205424111
      name: Cosine Ndcg@10
    - type: cosine_ndcg@20
      value: 0.572179718408508
      name: Cosine Ndcg@20
    - type: cosine_ndcg@30
      value: 0.5801741667185395
      name: Cosine Ndcg@30
    - type: cosine_mrr@10
      value: 0.7235900630879412
      name: Cosine Mrr@10
    - type: cosine_mrr@20
      value: 0.7256569302708415
      name: Cosine Mrr@20
    - type: cosine_mrr@30
      value: 0.726015777068746
      name: Cosine Mrr@30
    - type: cosine_map@100
      value: 0.4741746465087054
      name: Cosine Map@100
---

# MedEmbed Biomedical MRL

This is a [sentence-transformers](https://www.SBERT.net) model trained on the json dataset. It maps sentences & paragraphs to a 384-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
<!-- - **Base model:** [Unknown](https://huggingface.co/unknown) -->
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
model = SentenceTransformer("potsu-potsu/medembed-small-biomedical-matryoshka-v2")
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

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@10  | 0.9165     |
| cosine_accuracy@15  | 0.9264     |
| cosine_accuracy@20  | 0.9335     |
| cosine_accuracy@25  | 0.9378     |
| cosine_accuracy@30  | 0.9406     |
| cosine_precision@10 | 0.3908     |
| cosine_precision@15 | 0.3223     |
| cosine_precision@20 | 0.2713     |
| cosine_precision@25 | 0.2338     |
| cosine_precision@30 | 0.205      |
| cosine_recall@10    | 0.5942     |
| cosine_recall@15    | 0.6588     |
| cosine_recall@20    | 0.6988     |
| cosine_recall@25    | 0.7271     |
| cosine_recall@30    | 0.7471     |
| cosine_ndcg@10      | 0.6798     |
| cosine_ndcg@20      | 0.6889     |
| **cosine_ndcg@30**  | **0.7001** |
| cosine_mrr@10       | 0.7992     |
| cosine_mrr@20       | 0.8004     |
| cosine_mrr@30       | 0.8007     |
| cosine_map@100      | 0.6025     |

#### Information Retrieval

* Dataset: `dim_256`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator) with these parameters:
  ```json
  {
      "truncate_dim": 256
  }
  ```

| Metric              | Value     |
|:--------------------|:----------|
| cosine_accuracy@10  | 0.9137    |
| cosine_accuracy@15  | 0.9208    |
| cosine_accuracy@20  | 0.9307    |
| cosine_accuracy@25  | 0.9335    |
| cosine_accuracy@30  | 0.942     |
| cosine_precision@10 | 0.3857    |
| cosine_precision@15 | 0.3173    |
| cosine_precision@20 | 0.2668    |
| cosine_precision@25 | 0.2298    |
| cosine_precision@30 | 0.2015    |
| cosine_recall@10    | 0.5816    |
| cosine_recall@15    | 0.6467    |
| cosine_recall@20    | 0.687     |
| cosine_recall@25    | 0.7142    |
| cosine_recall@30    | 0.7385    |
| cosine_ndcg@10      | 0.6685    |
| cosine_ndcg@20      | 0.6771    |
| **cosine_ndcg@30**  | **0.689** |
| cosine_mrr@10       | 0.791     |
| cosine_mrr@20       | 0.7922    |
| cosine_mrr@30       | 0.7926    |
| cosine_map@100      | 0.5894    |

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
| cosine_accuracy@10  | 0.8925     |
| cosine_accuracy@15  | 0.9109     |
| cosine_accuracy@20  | 0.9137     |
| cosine_accuracy@25  | 0.918      |
| cosine_accuracy@30  | 0.9264     |
| cosine_precision@10 | 0.3652     |
| cosine_precision@15 | 0.3006     |
| cosine_precision@20 | 0.2521     |
| cosine_precision@25 | 0.2165     |
| cosine_precision@30 | 0.1898     |
| cosine_recall@10    | 0.5513     |
| cosine_recall@15    | 0.6155     |
| cosine_recall@20    | 0.6486     |
| cosine_recall@25    | 0.6719     |
| cosine_recall@30    | 0.6909     |
| cosine_ndcg@10      | 0.6398     |
| cosine_ndcg@20      | 0.6456     |
| **cosine_ndcg@30**  | **0.6548** |
| cosine_mrr@10       | 0.7783     |
| cosine_mrr@20       | 0.78       |
| cosine_mrr@30       | 0.7805     |
| cosine_map@100      | 0.5534     |

#### Information Retrieval

* Dataset: `dim_64`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator) with these parameters:
  ```json
  {
      "truncate_dim": 64
  }
  ```

| Metric              | Value      |
|:--------------------|:-----------|
| cosine_accuracy@10  | 0.8458     |
| cosine_accuracy@15  | 0.8642     |
| cosine_accuracy@20  | 0.8755     |
| cosine_accuracy@25  | 0.8769     |
| cosine_accuracy@30  | 0.8854     |
| cosine_precision@10 | 0.3267     |
| cosine_precision@15 | 0.2664     |
| cosine_precision@20 | 0.2245     |
| cosine_precision@25 | 0.1922     |
| cosine_precision@30 | 0.1686     |
| cosine_recall@10    | 0.4846     |
| cosine_recall@15    | 0.5381     |
| cosine_recall@20    | 0.5767     |
| cosine_recall@25    | 0.5974     |
| cosine_recall@30    | 0.6174     |
| cosine_ndcg@10      | 0.5696     |
| cosine_ndcg@20      | 0.5722     |
| **cosine_ndcg@30**  | **0.5802** |
| cosine_mrr@10       | 0.7236     |
| cosine_mrr@20       | 0.7257     |
| cosine_mrr@30       | 0.726      |
| cosine_map@100      | 0.4742     |

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
- `num_train_epochs`: 8
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
- `num_train_epochs`: 8
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
| Epoch   | Step   | Training Loss | dim_384_cosine_ndcg@30 | dim_256_cosine_ndcg@30 | dim_128_cosine_ndcg@30 | dim_64_cosine_ndcg@30 |
|:-------:|:------:|:-------------:|:----------------------:|:----------------------:|:----------------------:|:---------------------:|
| 1.0     | 8      | -             | 0.7100                 | 0.6989                 | 0.6534                 | 0.5490                |
| 1.2540  | 10     | 32.9088       | -                      | -                      | -                      | -                     |
| **2.0** | **16** | **-**         | **0.7047**             | **0.6961**             | **0.6579**             | **0.5768**            |
| 2.5079  | 20     | 15.2449       | -                      | -                      | -                      | -                     |
| 3.0     | 24     | -             | 0.7001                 | 0.6899                 | 0.6553                 | 0.5834                |
| 3.7619  | 30     | 11.0949       | -                      | -                      | -                      | -                     |
| 4.0     | 32     | -             | 0.7013                 | 0.6882                 | 0.6539                 | 0.5811                |
| 5.0     | 40     | 9.344         | 0.7023                 | 0.6910                 | 0.6542                 | 0.5809                |
| 6.0     | 48     | -             | 0.7010                 | 0.6891                 | 0.6552                 | 0.5805                |
| 6.2540  | 50     | 8.2338        | -                      | -                      | -                      | -                     |
| 7.0     | 56     | -             | 0.7003                 | 0.6892                 | 0.6551                 | 0.5812                |
| 7.5079  | 60     | 7.8342        | -                      | -                      | -                      | -                     |
| 8.0     | 64     | -             | 0.7001                 | 0.6890                 | 0.6548                 | 0.5802                |

* The bold row denotes the saved checkpoint.

### Framework Versions
- Python: 3.12.6
- Sentence Transformers: 4.1.0
- Transformers: 4.52.4
- PyTorch: 2.6.0+cu124
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