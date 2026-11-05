---
license: apache-2.0
language:
- en
tags:
- sentence-transformers
- sentence-similarity
- feature-extraction
- dense
- generated_from_trainer
- dataset_size:100000
- loss:CachedMultipleNegativesRankingLoss
base_model: Qwen/Qwen3-Embedding-0.6B


datasets:
- tomaarsen/miriad-4.4M-split
pipeline_tag: sentence-similarity
library_name: sentence-transformers
metrics:
  - cosine_accuracy@1
  - cosine_accuracy@3
  - cosine_accuracy@5
  - cosine_accuracy@10
  - cosine_ndcg@10
  - cosine_mrr@10
  - cosine_map@100

model-index:
  - name: Qwen3-MedEmbed-0.6B trained on MIRIAD
    results:
      - task:
          type: information-retrieval
          name: Information Retrieval
        dataset:
          name: MIRIAD Eval (2kq, 10kd)
          type: miriad-eval-2kq-10kd
          split: eval
        metrics:
          - name: Cosine Accuracy@1
            type: cosine_accuracy@1
            value: 0.8985
          - name: Cosine Accuracy@3
            type: cosine_accuracy@3
            value: 0.974
          - name: Cosine Accuracy@5
            type: cosine_accuracy@5
            value: 0.984
          - name: Cosine Accuracy@10
            type: cosine_accuracy@10
            value: 0.993
          - name: Cosine NDCG@10
            type: cosine_ndcg@10
            value: 0.9508
          - name: Cosine MRR@10
            type: cosine_mrr@10
            value: 0.9368
          - name: Cosine MAP@100
            type: cosine_map@100
            value: 0.9372

      - task:
          type: information-retrieval
          name: Information Retrieval
        dataset:
          name: MIRIAD Test (2kq, 10kd)
          type: miriad-test-2kq-10kd
          split: test
        metrics:
          - name: Cosine Accuracy@1
            type: cosine_accuracy@1
            value: 0.894
          - name: Cosine Accuracy@3
            type: cosine_accuracy@3
            value: 0.964
          - name: Cosine Accuracy@5
            type: cosine_accuracy@5
            value: 0.981
          - name: Cosine Accuracy@10
            type: cosine_accuracy@10
            value: 0.989
          - name: Cosine NDCG@10
            type: cosine_ndcg@10
            value: 0.9459
          - name: Cosine MRR@10
            type: cosine_mrr@10
            value: 0.9316
          - name: Cosine MAP@100
            type: cosine_map@100
            value: 0.9322
---

# Qwen3-MedEmbed-0.6B

<p align="center">
    <img src="https://qianwen-res.oss-accelerate-overseas.aliyuncs.com/logo_qwen3.png" width="400"/>
<p>


This is a [sentence-transformers](https://www.SBERT.net) model finetuned from [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) on the [miriad-4.4_m-split](https://huggingface.co/datasets/tomaarsen/miriad-4.4M-split) dataset. It maps sentences & paragraphs to a 1024-dimensional dense vector space and can be used for semantic textual similarity, semantic search, paraphrase mining, text classification, clustering, and more.

## Model Details

### Model Description
- **Model Type:** Sentence Transformer
- **Base model:** [Qwen/Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B) <!-- at revision c54f2e6e80b2d7b7de06f51cec4959f6b3e03418 -->
- **Maximum Sequence Length:** 1024 tokens
- **Output Dimensionality:** 1024 dimensions
- **Similarity Function:** Cosine Similarity
- **Training Dataset:**
    - [miriad-4.4_m-split](https://huggingface.co/datasets/tomaarsen/miriad-4.4M-split)
- **Language:** en
- **License:** apache-2.0

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Sentence Transformers on Hugging Face](https://huggingface.co/models?library=sentence-transformers)

### Full Model Architecture

```
SentenceTransformer(
  (0): Transformer({'max_seq_length': 1024, 'do_lower_case': False, 'architecture': 'Qwen3Model'})
  (1): Pooling({'word_embedding_dimension': 1024, 'pooling_mode_cls_token': False, 'pooling_mode_mean_tokens': False, 'pooling_mode_max_tokens': False, 'pooling_mode_mean_sqrt_len_tokens': False, 'pooling_mode_weightedmean_tokens': False, 'pooling_mode_lasttoken': True, 'include_prompt': True})
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
model = SentenceTransformer(
    "luluw/Qwen3-MedEmbed-0.6B",
    model_kwargs={
        # "attn_implementation": "flash_attention_2",
        "device_map": "auto",
        "dtype": torch.bfloat16
    },
    tokenizer_kwargs={"padding_side": "left"}
)
model.max_seq_length = 1024

# Run inference
queries = [
    "What are the systemic manifestations of Fournier\u0027s syndrome?",
]
documents = [
    "Fournier's syndrome is defined as a suppurative bacterial infection of the perineal, genital, or perianal regions. Those conditions often lead to thrombosis of subcutaneous vessels and with infection, resulting in the development of gangrene of the overlying skin and subcutaneous tissue [1] . This rare syndrome is a rapidly progressive and potentially lethal necrotizing fasciitis caused by invasive infections of the lower part of the genitourinary tract, anorectal soft tissue, and genital skin [1, 2] . The devastating rapidity is typical, as evidenced by the fact that the mean duration of symptoms to become the target of emergency operation is just a few days, and a majority of patients are seriously ill at the time of admission. Anesthetic management of patients with this syndrome is often difficult, due to its devastating nature as well as significant comorbid diseases. However, because of the infrequency of the syndrome, there is limited information regarding the anesthetic management of this disease. We recently encountered the anesthetic management in three cases of patients with Fournier's syndrome. There were three initial emergency and six additional elective operations under general anesthesia, except one spinal anesthesia in an elective case. Therefore, we report these cases and review the relevant literatures.\n\n Immediate and, if required, repetitive operation is important for saving lives in patients with this syndrome [1] [2] [3] . Fournier's syndrome is frequently associated with certain diseases and conditions. Diabetes mellitus is probably the most common comorbid disease, as evidenced by our cases [1] . Even when the patient has diabetes, as in our two patients, Fournier's syndrome might be the first clinical disease to be detected. The second common condition is alcoholism, such as in all our patients, because any disorder that compromises the immunity enhances development of a severe infection [1, 2] . The other associated clinical features are malnutrition, prolonged hospitalization, radiation therapy, chemotherapy, neurologic deficits, cirrhosis, leukemia, renal failure, organic heart disease, vasculitis, intravenous drug abuse, lupus, cirrhosis, AIDS and steroid medications. In obstetric anesthesia, cervical or pudendal nerve block can induce the syndrome as well [1] .\n\n Abnormal laboratory results include hyperglycemia, hypocalcemia, anemia, leukocytosis and thrombocytopenia, as evidenced by our patients [1] . Most of those abnormalities are due to sepsis. The systemic manifestations include fever, tachycardia, and volume depletion similar to those of severe peritonitis [1] . All our patients also had sepsis in terms of the preoperative definition. Two patients looked to be in late distributive shock and the other patient in early distributive shock, respectively. In the case of no active bleeding, delayed or inadequate volume resuscitation is a significant error that would have detrimental effects on the patients's outcome in septic shock. If initial crystalloid fluid resuscitation is insufficient to raise the mean arterial pressure to 65 mmHg and the CVP to 8 to 12 mmHg, then vasopressors and inotropes are needed as the second step in the guidelines of early goal-directed therapy [4] . It is rational to use a blood transfusion when the hematocrit is below 30% when invasive monitoring might be indicated [4] . Among two patients in late septic shock, one patient fortunately responded to our initial fluid resuscitation, whereas the other patient needed dopamine for hypotension. In another patient, early shock occurred, and a blood transfusion and dopamine and norepinephrine were required to achieve an adequate cardiac output and oxygen delivery to maintain vital organ function were needed, because his affected area including www.ekja.org\n\n Vol. 61, No. 2, August 2011 lower extremity was wide and bleeding was ongoing. His septic manifestations reoccurred sporadically over four months of hospitalization and progressed into cardiorespiratory collapse and death after five debridements under general anesthesia. The preanesthetic investigation of the extent of the lesion is also important, because the ambiguity of the region involved could influence the choice of the anesthetic technique. Koitabashi and colleagues [5] suggested the avoidance of spinal anesthesia in the presence of lumbar subcutaneous gas. Sato and associates [3] recommended that using general anesthesia is preferable for controlling physiologic homeostasis. Fournier's syndrome in particular originateed in anorectal disease, which is the usual subject of regional anesthetic procedures, is known to be aggressive, produces marked systemic toxicity and myonecrosis as in our mortal case, and can be connected with higher mortality [1] . Hence, particular attention should be necessary for the choice of the anesthetic procedures. The reason we performed spinal anesthesia at the secondary wound closure one month after initial debridement in one patient was that he underwent computer tomography to depict the accurate extent of the lesion. Among gravely ill patients it seems wise to not waste precious time doing a lot of investigation to perform regional anesthesia.\n\n The degree of debridement for Fournier's syndrome is variable from simple incision to wide excision with massive bleeding [2] . Many surviving patients require secondary wound closure, skin graft or a reconstructive flap procedure. In spite of appropriate therapy, the mortality rate in Fournier's syndrome is reported to exceed 40% in many studies [1] [2] [3] . Prolonged sepsis manifested by fever or hypotension and lasting for more than 48 hours was experienced among about 40% of patients, as in our expired patient [2] . Some reports have associated older age, female gender, anorectal causes, delayed admission, the presence of debilitating conditions such as renal failure and hepatic dysfunction with high mortality. Laboratory parameters on admission statistically related to fatality include low hematocrit, calcium, albumin, and cholesterol, and high BUN and alkaline phosphatase levels. The syndrome could rapidly progress into prolonged sepsis, DIC, pneumonia, respiratory failure, diabetic ketoacidosis, renal failure, and heart failure.\n\n In conclusion, our experiences emphasize that Fournier's syndrome has a fatal potential, so optimal conduct of anesthesia requires forethought and sound management as well as an understanding of the pathophysiology of this syndrome for successful anesthesia.",
    'Nucleotides can be synthesized de novo or recycled through a salvage pathway in vivo. In the salvage pathway, nucleotides are synthesized from extracellular nucleosides and/or nucleobases. The plasma membrane transport of nucleosides is concerned with both the physiology and pharmacology of mammalian cells. Most mammalian cells simultaneously express several nucleoside transporters (NTs) in the plasma membrane. NTs possess certain differences in Na + -dependency, permeation selectivity, and inhibitor sensitivity. NTs can be divided into two major classes: concentrative Na + -dependent nucleoside transporters (CNTs) and equilibrative Na + -independent nucleoside transporters (ENTs). CNTs are nucleoside/Na + symporters that transport nucleosides against their concentration * To whom correspondence should be addressed: Laboratory of Chemical Toxicology and Environmental Health, Showa Pharmaceutical University, 3-3165 Higashi-Tamagawagakuen, Machida, Tokyo 194-8543, Japan. Tel. & Fax: +81-42-721-1563; E-mail: ogra@ac.shoyaku.ac.jp gradients. In contrast, ENTs transport nucleosides by facilitated diffusion. ENTs can be further divided into two subclasses depending on their sensitivity to nitrobenzylthioinosine (NBTI). NBTI-sensitive and NBTI-insensitive forms are coded by ENT1 and ENT2 genes, respectively. ENT1 and ENT2 are inhibited by dipyridamole and dilazep. 1) On the other hand, CNTs can be divided into three forms. No specific pharmacological inhibitors have been identified for any CNTs so far. It was reported that dipyridamole, a classic NT inhibitor, was useful in enhancing the effectiveness of cancer chemotherapeutic agents, in particular, antimetabolites, based upon the inhibition of the nucleoside salvage pathway. 2, 3) Hence, the combination of NT inhibitors and antimetabolites is expected to provide more effective and safer cancer chemotherapy in the clinical setting.\n\n Cimicifugoside, a triterpenoid originating from the rhizomes of Cimicifuga simplex (C. simplex), has been used in traditional Chinese medicine as the so-called Cimicifugae rhizoma (Fig. 1) . The medicine is prescribed because of its anti-C 2011 The Pharmaceutical Society of Japan inflammatory, analgesic, and anti-pyretic effects. 4) In addition, it has been reported that cimicifugoside selectively inhibits the uptake of nucleosides into phytohematoagglutinin-stimulated human lymphocytes and several malignant cell lines. 5, 6) Indeed, the uptake of nucleosides, such as uridine, thymidine, and adenosine, but not nucleobases was inhibited by cimicifugoside and its analogs, such as cimicifugenin and bugbanosides A and B, in a leukemia cell line. 7) As the mechanism underlying the inhibition of nucleoside transport by cimicifugoside, it is speculated that cimicifugoside has weak affinity for the binding site of NBTI in ENTs, although the detailed inhibitory mechanism is still unclear. Furthermore, cimicifugoside and its analogs potentiated the cytotoxicity of methotrexate, a folic acid antimetabolite. In our previous study, we demonstrated that the synergic effect of methotrexate and cimicifugoside. 7) In this study, we intended to clarify the mechanisms underlying the cell-specific synergic effect of cimicifugoside on the cytotoxicity of methotrexate. We focused on the involvement of NT expression and activity in the cell lines. Cell Culture --The human promonocytic leukemia cell line U937 and the chronic myelogenetic leukemia cell line K562 were provided by the Cell Resource Center for Biomedical Research (Institute of Development, Aging and Cancer, Tohoku University, Sendai, Japan). Cells were cultured in RPMI 1640 medium supplemented with 5% (v/v) heat-inactivated fetal bovine serum (FBS), 60 µg/ml kanamycin and 2 mM L-glutamine (culture medium) at 37 • C in a humidified atmosphere of 5% CO 2 and 95% air.',
    'tissue infiltration of polymorphonuclear neutrophils (PMN). In response to bacterial infection, neutrophil activation in the lungs leads to ALI (53) and PMN infiltration represents a primary mechanism for sepsis-induced pulmonary dysfunction and injury (10) .\n\n In the normal lung, continuous fluid clearance by the lung lymphatics is essential for the maintenance of dry alveolar surfaces (60) . Ion pumps and channels positioned on alveolar epithelial cell surfaces generate transepithelial osmotic gradients that drive water movement from the alveolar space into the lung interstitium. The key pumps and channels involved in alveolar fluid transport include aquaporin 5 (Aqp5), cystic fibrosis transmembrane conductance regulator (CFTR), epithelial sodium channel (ENaC), and Na ϩ -K ϩ -ATPase (37) . In ALI, the lung endothelial barrier is damaged, resulting in abnormal capillary permeability and pulmonary edema as the lymphatic clearance is overwhelmed (60) . In contrast to the endothelium, the alveolar epithelium is often spared in sepsisinduced ALI, and therefore active ion and fluid clearance is preserved (56) . Recent reports, however, suggest that ion pump and channel functions are affected early during sepsis (37) .\n\n To maintain a "dry" alveolar space and normal lung function, it is essential that the milieu within the alveolar space remain distinct from that of the subepithelial compartment (30) . The maintenance mechanism depends on the formation and proper functioning of specialized molecular structures between adjacent cells comprising the epithelial sheet, the so-called tight junctions (TJ). The alveolar epithelial TJ is a complex of integral membrane proteins that firmly interact with the epithelial cytoskeleton (27) . TJs serve as a regulated semipermeable barrier that limits passive diffusion of solutes across paracellular pathways between adjacent cells (1). Han et al. (30) recently showed that ALI was associated with diminished expression and function of TJ proteins in lung epithelium.\n\n Emerging evidence indicates that inflammation and coagulation are connected (34) . This is especially important in sepsis as inflammatory cytokines activate the coagulation cascade and inhibit fibrinolysis, thereby shifting normal hemostasis toward a prothrombotic state. Sepsis-driven coagulation induces consumption of coagulation factors leading to disseminated intravascular coagulation (DIC), a phenomenon frequently associated with sepsis-induced ALI. Indeed, impairment of capillary blood flow during sepsis has been observed in human tissues by orthogonal polarization spectral imaging and sidestream dark-field imaging (17) . It is currently estimated that as many as 50% of all sepsis patients develop DIC (25) . Bastarache et al. (6) have recently reported that in ALI, the alveolar compartment contains high levels of tissue factor (TF) procoagulant activity that favor fibrin deposition in the air spaces. TF activation results in thrombin formation, which augments permeability and enhances inflammation (14) .\n\n Vitamin C is a small, water-soluble molecule that readily acts as a one-or two-electron reducing agent for many radicals and oxidants. Vitamin C is bioavailable equally as either dehydro-L-ascorbic acid (DHA) or L-ascorbic acid (AscA). Specialized cells can take up reduced vitamin C (AscA) through Na ϩ -dependent ascorbate cotransporters (SVCT1 and SVCT2). Most other cells take up vitamin C in its oxidized form (DHA) via facilitative glucose transporters (48) . Sepsis lowers plasma AscA concentrations (57) and, importantly, low vitamin C levels correlate inversely with multiple organ failure and directly with survival (9) . Studies using animal models show that vitamin C prevents endotoxin-induced hypotension and improves arteriolar responsiveness, arterial blood pressure, capillary blood flow, liver function, and survival in experimental sepsis (4, 59) .\n\n We recently showed that vitamin C, administered after the onset of endotoxemia, attenuates proinflammatory and procoagulant states that induce lung vascular injury and improved survival in an animal model of sepsis (23) . In the present study we show that vitamin C attenuates sepsis-induced ALI by enhancing alveolar epithelial barrier integrity. Furthermore, vitamin C induced the expression of ion channels and pumps, which play critical roles in improving alveolar fluid clearance. In addition, we also observed marked changes in the viscoelastic clot properties of septic mice blood.',
]
query_embeddings = model.encode_query(queries)
document_embeddings = model.encode_document(documents)
print(query_embeddings.shape, document_embeddings.shape)
# [1, 1024] [3, 1024]

# Get the similarity scores for the embeddings
similarities = model.similarity(query_embeddings, document_embeddings)
print(similarities)
# tensor([[ 0.6019, -0.0015, -0.0054]])
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

* Dataset: `miriad-eval-2kq-10kd`
* Evaluated with [<code>InformationRetrievalEvaluator</code>](https://sbert.net/docs/package_reference/sentence_transformer/evaluation.html#sentence_transformers.evaluation.InformationRetrievalEvaluator)

| Metric                  | Dev Value 2kq_10kd  | Test Value 2kq_10kd |
| :---------------------- | :--------- | :--------- |
| **cosine_accuracy@1**   | 0.8985     | 0.894      |
| **cosine_accuracy@3**   | 0.974      | 0.964      |
| **cosine_accuracy@5**   | 0.984      | 0.981      |
| **cosine_accuracy@10**  | 0.993      | 0.989      |
| **cosine_precision@1**  | 0.8985     | 0.894      |
| **cosine_precision@3**  | 0.3247     | 0.3213     |
| **cosine_precision@5**  | 0.1968     | 0.1962     |
| **cosine_precision@10** | 0.0993     | 0.0989     |
| **cosine_recall@1**     | 0.8985     | 0.894      |
| **cosine_recall@3**     | 0.974      | 0.964      |
| **cosine_recall@5**     | 0.984      | 0.981      |
| **cosine_recall@10**    | 0.993      | 0.989      |
| **cosine_ndcg@10**      | **0.9508** | **0.9459** |
| **cosine_mrr@10**       | 0.9368     | 0.9316     |
| **cosine_map@100**      | 0.9372     | 0.9322     |


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

#### miriad-4.4_m-split

* Dataset: [miriad-4.4_m-split](https://huggingface.co/datasets/tomaarsen/miriad-4.4M-split) at [596b9ab](https://huggingface.co/datasets/tomaarsen/miriad-4.4M-split/tree/596b9ab305d52cb73644ed5b5004957c7bfaae40)
* Size: 100,000 training samples
* Columns: <code>question</code> and <code>passage_text</code>
* Approximate statistics based on the first 1000 samples:
  |         | question                                                                          | passage_text                                                                           |
  |:--------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                                 |
  | details | <ul><li>min: 8 tokens</li><li>mean: 21.03 tokens</li><li>max: 63 tokens</li></ul> | <ul><li>min: 509 tokens</li><li>mean: 977.14 tokens</li><li>max: 1024 tokens</li></ul> |
* Samples:
  | question                                                                                                                                                                                              | passage_text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>What factors may contribute to increased pulmonary conduit durability in patients who undergo the Ross operation compared to those with right ventricular outflow tract obstruction?<br></code> | <code>I n 1966, Ross and Somerville 1 reported the first use of an aortic homograft to establish right ventricle-to-pulmonary artery continuity in a patient with tetralogy of Fallot and pulmonary atresia. Since that time, pulmonary position homografts have been used in a variety of right-sided congenital heart lesions. Actuarial 5-year homograft survivals for cryopreserved homografts are reported to range between 55% and 94%, with the shortest durability noted in patients less than 2 years of age. 4 Pulmonary position homografts also are used to replace pulmonary autografts explanted to repair left-sided outflow disease (the Ross operation). Several factors may be likely to favor increased pulmonary conduit durability in Ross patients compared with those with right ventricular outflow tract obstruction, including later age at operation (allowing for larger homografts), more normal pulmonary artery architecture, absence of severe right ventricular hypertrophy, and more natural positioning of ...</code> |
  | <code>How does MCAM expression in hMSC affect the growth and maintenance of hematopoietic progenitors?</code>                                                                                         | <code>After culture in a 3-dimensional hydrogel-based matrix, which constitutes hypoxic conditions, MCAM expression is lost. Concordantly, Tormin et al. demonstrated that MCAM is down-regulated under hypoxic conditions. 10 Furthermore, it was shown by others and our group that oxygen tension causes selective modification of hematopoietic cell and mesenchymal stromal cell interactions in co-culture systems as well as influence HSPC metabolism. [44] [45] [46] Thus, the observed differences between Sharma et al. and our data in HSPC supporting capacity of hMSC are likely due to the different culture conditions used. Further studies are required to clarify the influence of hypoxia in our model system. Altogether these findings provide further evidence for the importance of MCAM in supporting HSPC. Furthermore, previous reports have shown that MCAM is down-regulated in MSC after several passages as well as during aging and differentiation. 19, 47 Interestingly, MCAM overexpression in hMSC enhance...</code> |
  | <code>What is the relationship between Fanconi anemia and breast and ovarian cancer susceptibility genes?<br></code>                                                                                  | <code>( 31 ) , of which 5% -10 % may be caused by genetic factors ( 32 ) , up to half a million of these patients may be at risk of secondary hereditary neoplasms. The historic observation of twofold to fi vefold increased risks of cancers of the ovary, thyroid, and connective tissue after breast cancer ( 33 ) presaged the later syndromic association of these tumors with inherited mutations of BRCA1, BRCA2, PTEN, and p53 ( 16 ) . By far the largest cumulative risk of a secondary cancer in BRCA mutation carriers is associated with cancer in the contralateral breast, which may reach a risk of 29.5% at 10 years ( 34 ) . The Breast Cancer Linkage Consortium ( 35 , 36 ) also documented threefold to fi vefold increased risks of subsequent cancers of prostate, pancreas, gallbladder, stomach, skin (melanoma), and uterus in BRCA2 mutation carriers and twofold increased risks of prostate and pancreas cancer in BRCA1 mutation carriers; these results are based largely on self-reported family history inf...</code> |
* Loss: [<code>CachedMultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cachedmultiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "mini_batch_size": 8,
      "gather_across_devices": false
  }
  ```

### Evaluation Dataset

#### miriad-4.4_m-split

* Dataset: [miriad-4.4_m-split](https://huggingface.co/datasets/tomaarsen/miriad-4.4M-split) at [596b9ab](https://huggingface.co/datasets/tomaarsen/miriad-4.4M-split/tree/596b9ab305d52cb73644ed5b5004957c7bfaae40)
* Size: 2,000 evaluation samples
* Columns: <code>question</code> and <code>passage_text</code>
* Approximate statistics based on the first 1000 samples:
  |         | question                                                                          | passage_text                                                                           |
  |:--------|:----------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------|
  | type    | string                                                                            | string                                                                                 |
  | details | <ul><li>min: 8 tokens</li><li>mean: 21.18 tokens</li><li>max: 66 tokens</li></ul> | <ul><li>min: 502 tokens</li><li>mean: 974.49 tokens</li><li>max: 1024 tokens</li></ul> |
* Samples:
  | question                                                                                                                                                                                  | passage_text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
  | <code>What are some hereditary cancer syndromes that can result in various forms of cancer?<br></code>                                                                                    | <code>Hereditary Cancer Syndromes, including Hereditary Breast and Ovarian Cancer (HBOC) and Lynch Syndrome (LS), can result in various forms of cancer due to germline mutations in cancer predisposition genes. While the major contributory genes for these syndromes have been identified and well-studied (BRCA1/ BRCA2 for HBOC and MSH2/MSH6/MLH1/PMS2/ EPCAM for LS), there remains a large percentage of associated cancer cases that are negative for germline mutations in these genes, including 80% of women with a personal or family history of breast cancer who are negative for BRCA1/2 mutations [1] . Similarly, between 30 and 50% of families fulfill stringent criteria for LS and test negative for germline mismatch repair gene mutations [2] . Adding complexity to these disorders is the significant overlap in the spectrum of cancers observed between various hereditary cancer syndromes, including many cancer susceptibility syndromes. Some that contribute to elevated breast cancer risk include Li-Frau...</code>       |
  | <code>How do MAK-4 and MAK-5 exert their antioxidant properties?<br></code>                                                                                                               | <code>Hybrid F1 mice were injected with urethane (300 mg/kg) at 8 days of age. A group was then put on a MAK-supplemented diet, another group was fed a standard pellet diet. At 36 weeks of age the mice were sacrificed and the livers examined for the presence of tumors mouse (Panel A) and for the number of nodules per mouse (Panel B) (* p < 0.05, ** P < 0.001). Statistical analysis was performed by Two Way ANOVA Test followed by Post Hoc Bonferroni analysis. <br><br> We than measured the influence of the MAK-4+5 combination on the expression of the three liver-specific connexins (cx26, cx32, and cx43). The level of cx26 expression was similar in all the groups of mice treated with the MAK-supplemented diet and in the control (Figure 4, Panel A) . A significant, time-dependent increase in cx32 was observed in the liver of all the groups of MAK treated mice compared to the normal diet-fed controls. Cx32 expression increased 2-fold after 1 week of treatment, and 3-to 4-fold at 3 months (Figure 4, Pane...</code> |
  | <code>What are the primary indications for a decompressive craniectomy, and what role does neurocritical care play in determining the suitability of a patient for this procedure?</code> | <code>Decompressive craniectomy is a valid neurosurgical strategy now a day as an alternative to control an elevated intracranial pressure (ICP) and controlling the risk of uncal and/or subfalcine herniation, in refractory cases to the postural, ventilator, and pharmacological measures to control it. The neurocritical care and the ICP monitorization are key determinants to identify and postulate the inclusion criteria to consider a patient as candidate to this procedure, as it is always considered a rescue surgical technique. Head trauma and ischemic or hemorrhagic cerebrovascular disease with progressive deterioration due to mass effect are some of the cases that may require a decompressive craniectomy with its different variants. However, this procedure per se can have complications described in the postcraniectomy syndrome and may occur in short, medium, or even long term.<br><br> 1,2 The paradoxical herniation is a condition in which there is a deviation of the midline with mass effect, even t...</code> |
* Loss: [<code>CachedMultipleNegativesRankingLoss</code>](https://sbert.net/docs/package_reference/sentence_transformer/losses.html#cachedmultiplenegativesrankingloss) with these parameters:
  ```json
  {
      "scale": 20.0,
      "similarity_fct": "cos_sim",
      "mini_batch_size": 8,
      "gather_across_devices": false
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `eval_strategy`: steps
- `per_device_train_batch_size`: 64
- `per_device_eval_batch_size`: 64
- `learning_rate`: 0.0001
- `weight_decay`: 0.01
- `num_train_epochs`: 1
- `warmup_ratio`: 0.1
- `bf16`: True
- `dataloader_num_workers`: 8
- `dataloader_prefetch_factor`: 16
- `load_best_model_at_end`: True
- `push_to_hub`: True
- `prompts`: {'question': 'Instruct: Given a web search query, retrieve relevant passages that answer the query\nQuery:', 'passage_text': ''}
- `batch_sampler`: no_duplicates


</details>

### Training Logs
<details><summary>Click to expand</summary>

| Epoch  | Step | Training Loss | Validation Loss | miriad-eval-2kq-2kd_cosine_ndcg@10 |miriad-eval-2kq-10kd_cosine_ndcg@10 |miriad-test-2kq-10kd_cosine_ndcg@10 |
|:------:|:----:|:-------------:|:---------------:|:-----------------------------------:|:---------------:|:-----------------------------------:|
| 0.0640 | 100  | 0.0293        | -               | -                                   | -               | -                                   |
| 0.1280 | 200  | 0.0233        | -               | -                                   | -               | -                                   |
| 0.1919 | 300  | 0.0225        | 0.0174          | 0.9818                              | -               | -                                   |
| 0.2559 | 400  | 0.015         | -               | -                                   | -               | -                                   |
| 0.3199 | 500  | 0.0199        | -               | -                                   | -               | -                                   |
| 0.3839 | 600  | 0.0162        | 0.0140          | 0.9815                              | -               | -                                   |
| 0.4479 | 700  | 0.0196        | -               | -                                   | -               | -                                   |
| 0.5118 | 800  | 0.0208        | -               | -                                   | -               | -                                   |
| 0.5758 | 900  | 0.0146        | 0.0143          | 0.9834                              | -               | -                                   |
| 0.6398 | 1000 | 0.0083        | -               | -                                   | -               | -                                   |
| 0.7678 | 1200 | 0.0165        | 0.0120          | 0.9832                              | -               | -                                   |
| 0.8317 | 1300 | 0.012         | -               | -                                   | -               | -                                   |
| 0.8957 | 1400 | 0.0227        | -               | -                                   | -               | -                                   |
| 0.9597 | 1500 | 0.0169        | 0.0112          | 0.9848                              | 0.9508               | 0.9459                             |
</details>

### Framework Versions
- Python: 3.12.11
- Sentence Transformers: 5.1.2
- Transformers: 4.57.1
- PyTorch: 2.8.0+cu128
- Accelerate: 1.11.0
- Datasets: 4.3.0
- Tokenizers: 0.22.1

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

#### CachedMultipleNegativesRankingLoss
```bibtex
@misc{gao2021scaling,
    title={Scaling Deep Contrastive Learning Batch Size under Memory Limited Setup},
    author={Luyu Gao and Yunyi Zhang and Jiawei Han and Jamie Callan},
    year={2021},
    eprint={2101.06983},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```
