---
language:
- en
license: mit
tags:
- sentence-transformers
- cross-encoder
- reranker
- generated_from_trainer
- dataset_size:898469
- loss:BinaryCrossEntropyLoss
base_model: microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext
pipeline_tag: text-ranking
library_name: sentence-transformers
metrics:
- map
- mrr@10
- ndcg@10
model-index:
- name: PubMedBERT-base reranker fine-tuned on MIRIAD
  results:
  - task:
      type: cross-encoder-reranking
      name: Cross Encoder Reranking
    dataset:
      name: NanoNFCorpus R100
      type: NanoNFCorpus_R100
    metrics:
    - type: map
      value: 0.4398
      name: Map
    - type: mrr@10
      value: 0.6895
      name: Mrr@10
    - type: ndcg@10
      value: 0.5159
      name: Ndcg@10
  - task:
      type: cross-encoder-reranking
      name: Cross Encoder Reranking
    dataset:
      name: NanoSciFact R100
      type: NanoSciFact_R100
    metrics:
    - type: map
      value: 0.2911
      name: Map
    - type: mrr@10
      value: 0.2754
      name: Mrr@10
    - type: ndcg@10
      value: 0.2954
      name: Ndcg@10
  - task:
      type: cross-encoder-reranking
      name: Cross Encoder Reranking
    dataset:
      name: NanoSCIDOCS R100
      type: NanoSCIDOCS_R100
    metrics:
    - type: map
      value: 0.2516
      name: Map
    - type: mrr@10
      value: 0.4591
      name: Mrr@10
    - type: ndcg@10
      value: 0.2918
      name: Ndcg@10
  - task:
      type: cross-encoder-nano-beir
      name: Cross Encoder Nano BEIR
    dataset:
      name: NanoBEIR R100 mean
      type: NanoBEIR_R100_mean
    metrics:
    - type: map
      value: 0.3275
      name: Map
    - type: mrr@10
      value: 0.4747
      name: Mrr@10
    - type: ndcg@10
      value: 0.3677
      name: Ndcg@10
---

# PubMedBERT-base reranker fine-tuned on MIRIAD

This is a [Cross Encoder](https://www.sbert.net/docs/cross_encoder/usage/usage.html) model finetuned from [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) using the [sentence-transformers](https://www.SBERT.net) library. It computes scores for pairs of texts, which can be used for text reranking and semantic search.

## Model Details

### Model Description
- **Model Type:** Cross Encoder
- **Base model:** [microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext](https://huggingface.co/microsoft/BiomedNLP-BiomedBERT-base-uncased-abstract-fulltext) <!-- at revision e1354b7a3a09615f6aba48dfad4b7a613eef7062 -->
- **Maximum Sequence Length:** 384 tokens
- **Number of Output Labels:** 1 label
- **Supported Modality:** Text
<!-- - **Training Dataset:** Unknown -->
- **Language:** en
- **License:** mit

### Model Sources

- **Documentation:** [Sentence Transformers Documentation](https://sbert.net)
- **Documentation:** [Cross Encoder Documentation](https://www.sbert.net/docs/cross_encoder/usage/usage.html)
- **Repository:** [Sentence Transformers on GitHub](https://github.com/huggingface/sentence-transformers)
- **Hugging Face:** [Cross Encoders on Hugging Face](https://huggingface.co/models?library=sentence-transformers&other=cross-encoder)

### Full Model Architecture

```
CrossEncoder(
  (0): Transformer({'transformer_task': 'sequence-classification', 'modality_config': {'text': {'method': 'forward', 'method_output_name': 'logits'}}, 'module_output_name': 'scores', 'architecture': 'BertForSequenceClassification'})
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
model = CrossEncoder("tomaarsen/reranker-PubMedBERT-base-MIRIAD-150k")
# Get scores for pairs of inputs
pairs = [
    ['What is the role of ultrasound fellowship training and familiarity with the sonographic appearance of SBO in accurately interpreting acquired POCUS images?\n', 'T he first report of musculoskeletal sonography was published in 1958 by Dussik et al 1 in a study that measured acoustic attenuation of articular and periarticular tissues. Technical advances and expanding indications in the 1970s popularized the use of ultrasonography in athletes. 2 In the 1980s and early 1990s, Middleton et al 3 and Harryman et al 4 first evaluated rotator cuff pathology using ultrasonography. In a more recent study, Yamaguchi et al 5 performed a longitudinal analysis of rotator cuff tears (RCTs) detected on sonograms. Ultrasonography is an operatordependent imaging modality, and clinical expertise in its use is paramount. Even with the use of well-defined protocols, substantial interobserver variability is associated with ultrasonography, and ultrasonography performed by clinicians rather than radiologists has led to debates with regard to training and level of competence. 6 Published training guidelines indicate that clinicians must perform 150 to 300 scans under the supervision of a qualified ultrasonographer or radiologist to develop proficiency. 6 In general, MRI is the preferred imaging modality for evaluation of the shoulder and elbow. In most patients, MRIs are comprehensive; however, arthrography often is required to improve the diagnostic accuracy of MRI for labral assessment. MRI is not well tolerated by some patients, may lead to incidental findings, and may be costly. In contrast, ultrasonography allows for rapid, Albert Lin, MD Gregory Gasbarro, MD Mark Sakr, DO dynamic examination, immediate clinical correlation, and image guidance during therapeutic procedures. Ultrasonography can be used for serial examination of soft tissues and affords real-time tissue elastography, which is a technique that allows for close monitoring of tendon and tissue quality with various muscle contraction conditions and joint positions. 7 Ultrasonography is an excellent educational tool for orthopaedic residency training, and interest in the use of this modality as an adjunct for physical examination of the shoulder and elbow has increased in the past two decades. Other benefits of ultrasonography include portability, decreased artifact from metal hardware, and contrast-enhanced Doppler applications that allow for real-time assessment of soft-tissue vascularity. 2, 8 In addition, ultrasonography is less expensive than MRI. In 2007, .80 million MRIs were performed in the United States, with a cost to the healthcare system of .$120 billion. 9 In a recent study of 146 patients who underwent ultrasonographic evaluation of shoulder pathology, Adelman and Fishman 9 reported that 35 MRIs were avoided with the use of ultrasonography, saving a predicted $17,603, which represented a 50% 1-year return on investment ($34,897) for the ultrasonography machine and equipment.\n\n Office-based musculoskeletal ultrasonography became possible as the quality of portable ultrasonography improved. Newer generation machines, which currently are the size of a laptop computer, replaced the large ultrasonography units typically used in hospitals. The ability to own and maneuver an ultrasonography machine in a clinic in combination with higher quality sonograms allowed for increased office-based musculoskeletal ultrasonography. The processing power, transducer capabilities, and software advances of newer ultrasonography machines also played an important role in the increased office-based use of the modality. Various ultrasonography machines are available for clinicians who desire in-office musculoskeletal ultrasonographic capability. Almost all modern models meet high-quality and function standards. Selection of an appropriate machine for a clinic requires consideration of the desired capabilities of interchangeable probes, desired image resolution, ease of use, comfort with the machine/interface, and cost. To become familiar with various ultrasonography machines, clinicians can contact manufacturers to test their machines and/or attend expositions to observe demonstrations of the newest features. Clinicians can contact colleagues and/or attend educational courses to determine the advantages and disadvantages of various ultrasonography machines.\n\n \n\n Ultrasonography is an accurate and cost-effective imaging modality for detection of partial-and full-thickness RCTs, demonstrating no statistically significant difference in sensitivity or specificity for detection of RCTs compared with arthrography or MRI. 3, 10 Murphy et al 6 reported on the learning curve among orthopaedic surgeons without prior experience who used ultrasonography for the detection of full-thickness supraspinatus tears. Arthroscopy was used as the standard of care for assessment of rotator cuff integrity. The authors found that orthopaedic surgeons had high levels of proficiency for the detection of RCTs during the first 50 scans performed. Notably, orthopaedic surgeon proficiency for the detection of RCTs during the second 50 scans performed was comparable with published data for surgeons with experience in shoulder ultrasonography and musculoskeletal radiologists.'],
    ['How should study results in the context of respiratory conditions be interpreted and what is the importance of considering the perspective of patients?\n', 'This should be done with careful attention to the needs of the main users of the synthesis.\n\n Discuss both the strengths of the review and its limitations. These should include (but need not be restricted to) (a) consideration of all the steps in the synthesis process and (b) comment on the overall strength of evidence supporting the explanatory insights that emerged.\n\n The limitations identified may point to areas where further work is needed. ... Authors seldom described or discussed the mechanisms that explained their study outcomes. We realise that the RCT design, the exacting reporting requirements and word limits of journals, restrict authors from sharing all their operational experiences. In addition RCTs tend to report average effects and not differential effects of interventions, and less so of the context and rarely of the mechanisms triggered by their interactions. This makes the RCTs less useful for answering the questions regarding how interventions work. These generic hypotheses seem to be recurring in the literature, however they have not been explicitly tested across contexts." [27] Explanation Realist synthesis may be constrained by time and resources, by the skill mix and collective experience of the research team, by the scope of the review\'s questions or objectives and/or by anticipated or unanticipated challenges in the data. These should be made explicit so that readers can interpret the findings in the light of them. A common challenge in realist synthesis is that in order to focus the synthesis, some material is omitted at each successive stage. Some aspects of the topic area, therefore, end up being reviewed in detail and rich explanatory insights produced for these. Other aspects are neglected (relatively or absolutely). It is thus inevitable that in generating illumination, the synthesis will also cast shadows. These should be highlighted in the discussion so as to indicate areas where other syntheses might focus.\n\n Strengths and/or limitations associated with any modifications made to the synthesis process should also be reported and justified.\n\n Where applicable, compare and contrast the synthesis\' findings with the existing literature (for example, other reviews) on the same topic.\n\n Example "We were unable to find any comparable attempt at providing an evidence-based-policy framework such as ours. However, we acknowledge that some sections of our framework may be found in sources we have not uncovered and also as tacit knowledge within the heads of seasoned practitioners (e.g. advocates or legislators). We do however hope that our attempts to develop and test it on our one \'case study\' will make a primordial tool that will be useful to policy and decisions makers less well versed in the arena of public health legislation." [26] Explanation Comparing and contrasting the findings from a synthesis with the existing literature may help readers to put these into context. For example, this item might cover questions such as: How does this synthesis compare to other reviews (for example, were they theory-driven?); What does this synthesis add?; Which body of work in particular does it add to?; Has this synthesis reached the same or different conclusion to previous reviews?; and Has it answered a question previously identified as important in the field?\n\n List the main implications of the findings and place these in the context of other relevant literature. If appropriate, offer recommendations for policy and practice.\n\n Example "Our realist review was based on a housing intervention in the United States, but the results can potentially be applied to urban centers in other nations that implement housing interventions that involve moving families. When a family moves, the experience is likely to be different for each member of the household, and differences in mental health outcomes of moving may occur (Reference x1). All communities, rich or poor, and irrespective of geographic location, should be viewed as complex systems, and as composed of people with social relationships that influence the functioning and health of community members." [28] Explanation A clear line of reasoning is needed to link the findings (Results section) with the implications (Discussion and/or Conclusion). If the synthesis is small and preliminary, or if the coherence and plausibility of evidence behind the inferences is weak or moderate, statements about implications for practice and policy should be appropriately guarded.\n\n If recommendations are given, these should take into account the focus of the synthesis and needs of the intended audience and be presented appropriately. The explanations in realist analysis are highly dependent on contextual influences. It follows that recommendations must be contingent (for example, only under certain contexts will a particular mechanism be triggered to generate the desired outcome) rather than statements that X should or should not be done.\n\n Provide details of funding source (if any) for the synthesis, the role played by the funder (if any) and any conflicts of interests of the reviewers.\n\n "We gratefully acknowledge a financial contribution from the Dutch Development Cooperation (DGIS)." [25] Explanation The source of funding for a synthesis and/or personal conflicts of interests may influence the research question, methods, data analysis and conclusions.'],
    ['What are the potential therapeutic strategies for targeting NF-κB in autoimmune diseases?\n', 'Although this paradox is not fully understood, it may reflect functional redundancy in the canonical TLR and interleukin-1-receptor signaling pathways. Other efforts to target cytokines (e.g., interleukin-17 and 17 receptor, BLyS, APRIL, and GM-CSF) with the use of biologic approaches are ongoing. 55, 56 The range of available therapeutics based on the biologic characteristics of synovial cytokines will probably expand ( Table 2) .\n\n Elucidation of the complex intracellular signaling molecules (particularly kinases) that regulate cytokine-receptor-mediated functions may facilitate the development of specific small-molecule inhibitors. Although many intracellular signaling pathways are active in the synovium, clues to those with hierarchical importance have been provided by clinical trials. Positive clinical outcomes in phase 2 studies of the Janus kinase (JAK) 1 and 3 inhibitor tofacitinib implicate JAK pathways that mediate the function of several cytokines, interferons, and growth factors in the pathogenesis of rheumatoid arthritis 57, 58 (Table 2) . Moreover, inhibition of spleen tyrosine kinase by fostamatinib, which is effective in some subgroups of patients, is commensurate with its role in the function of B-cell and Fc receptors. 2213 ponents of the NF-κB pathway, offer intriguing possibilities for therapeutic strategies. In contrast, despite a strong preclinical rationale, the targeting of p38 mitogen-activated protein kinase has been disappointing in clinical settings, which probably indicates that the molecular signaling network in rheumatoid arthritis has functional redundancy.\n\n The normal synovium contains mesenchymal-derived, fibroblast-like synoviocytes (FLSs) and resident macrophages. In rheumatoid arthritis, the membrane lining is expanded, and FLSs assume a semiautonomous phenotype characterized by anchorage independence, loss of contact inhibition, and the expression of high levels of diseaserelevant cytokines and chemokines, adhesion molecules, matrix metalloproteinases (MMPs), and tissue inhibitors of metalloproteinases (TIMPs). 61 FLSs thereby contribute directly to local cartilage destruction and the chronicity of synovial inflammation, and they promote a permissive microenvironment that sustains T-cell and B-cell survival and adaptive immune organization. 62 The molecular mechanisms that sustain synovial hyperplasia are incompletely understood. The increased proliferative capacity of FLSs is not explanatory. A more likely possibility is altered resistance to apoptosis, which is mediated by diverse pathways, including mutations of the tumor-suppressor gene p53 63 ; expression of stress proteins (e.g., heat-shock protein 70), which foster the survival of FLSs 64 ; and modulation of the function of the endoplasmatic reticulum by synoviolin, an E3 ubiquitin ligase that regulates the balance of cell proliferation and apoptosis. 65 Synoviolin negatively regulates p53 expression and its biologic functions. In addition, cytokine-induced activation of the NF-κB pathway in FLSs favors survival after ligation of TNF-α receptor. Methylation and acetylation of cell-cycle regulatory genes and expression of microRNAs may be critical factors. 66 Synovial hyperplasia could also reflect increased influx of mesenchymal cells. In a mouse model of arthritis with severe combined immunodeficiency, FLSs were shown to migrate and thereby promote articular involvement. 67 A crucial advance has been the elucidation of the molecular pathways that sustain integral membrane structure in rheumatoid arthritis. Cadherin-11 and β-catenin mediate FLS-homotypic interactions that are essential for membrane formation and for subsequent inflammation. 68 \n\n \n\n A hyperplastic synovium is the major contributor to cartilage damage in rheumatoid arthritis. Loss of the normally protective effects of synovium (e.g., reduced expression of lubricin) 69 alter the protein-binding characteristics of the cartilage surface, promoting FLS adhesion and invasion. FLS synthesis of MMPs (particularly MMP-1, 3, 8, 13, 14, and 16) promotes disassembly of the type II collagen network, a process that alters glycosaminoglycan content and water retention and leads directly to biomechanical dysfunction. MMP-14 appears to be the predominant MMP expressed by FLSs to degrade the collagenous cartilage matrix. 70 Other matrix enzymes (e.g., ADAMTS 5) degrade aggrecan and thus further diminish cartilage integrity.\n\n Endogenous enzyme inhibitors, such as TIMPs, fail to reverse this destructive cascade. Moreover, articular cartilage itself has limited regenerative potential.'],
    ['What are the limitations and advantages of using saphenofemoral arteriovenous fistula as a vascular access for hemodialysis?\n', 'Patients on dialysis for long-term catheter and without maturing fistula (12 patients) had a mean time of 5.46 months of use and had already exhausted their chances of making fistulas. The most frequent type of fistula use was on the radio distal cephalic, in 85 patients (52.5%), followed by radio cephalic proximal in 26 patients (16%) ( Table 3) .\n\n The number of fistulas in dialysis patients conducted by this kind of therapy ranged from one to ten and in 64 patients (41.83%) fistula was the first and only to be made. Among the fistula for dialysis patients, the highest prevalence was radio cephalic fistula in 111 patients (72.5%) and mean duration of use was 48.1 months, ranging from two months to 17 years. These patients had an average of 0.89 prior fistulas, and in 46 patients (30%) it was the only fistula. Among the most frequent complications observed in fistulas in use, the pseudo-aneurysm after puncture and venous hypertension were the most common.\n\n It was created in 1997, the NKF-DOQI, establishing guidelines for standardization of care for chronic kidney illness to dialysis in relation to vascular access in order to decrease the complications and cost, improve the dialysis quality, thus, improving the patients quality of life, since it was reported high number of use and complications of vascular access for hemodialysis due to catheter use and fistula with prosthesis [13] . The periodic review of access for hemodialysis is intended to be performed on all services in order to monitor their adequacy in relation to international guidelines. According to these premises, we performed at the Unit of Nephrology from our University an investigation which aims to verify the adequacy and monitor the vascular access, within the standards established by the guidelines (NKF-DOQI 2006). The number of catheters reported in our study is in accordance with the recommended by the NKF-DOQI and a large proportion of patients with short-term catheters presented fistulas in maturation. Making fistulas in patients before dialysis is a target in our service, it is difficult because our patients are often at the endstage of renal disease. Patients with long-term catheters are at the stage of exhaustion of vascular accesses and some of them had fistulas at maturity which is also in agreement with the guidelines.\n\n In a recent investigation published by our group, which evaluated saphenofemoral fistula as vascular access for hemodialysis [3] , it was observed some cases of thrombosis due to prolonged arterial hypotension and one case due to trauma of the fistula site at home environment. By studying this type of complication, we alert to the importance of maintaining regular surveillance with periodic evaluation of these fistulas in order to detect early dysfunction so that it may be corrected in time, reducing the risk of thrombosis and increasing the usefulness period of the fistula [14] .\n\n According to our findings the percentage of patients under dialysis with arteriovenous fistulas was higher than the recommended by the NKF-DOQI 2006 (70%). Furthermore, the location of fistulas is in accordance with the guidelines. We reported predominance of distal radio-cephalic, which has a high rate in the primary fistulas, which is the ideal combination for the patient because it is related to a lower complication rate and, hence, improved quality of life [6, 7] . Some issues should be addressed when taking vascular access for hemodialysis. According to a recent study, the limitation of saphenofemoral arteriovenous fistula as hemodialysis access is given in cases when the patient presents saphenous vein absence or when the saphenous vein is inadequate for this purpose and also in patients with arterial occlusive disease in the femoropopliteal territory. Another limitation of this technique is that the saphenous vein prevents the development of the fistula due to its developed muscle layer, similar to the cephalic vein in the internal forearm arteriovenous fistula. Although it prevents aneurysmal dilatation it increases the risk of myointimal hyperplasia after repeated punctures of the arteriovenous fistula [15] . On the other hand, because it is autologous material, it presents low cost, higher infection resistance and it is easy to handling, the advantages compensate its limitations even when compared to other access techniques in lower limbs which also uses autologous material such as transposition of the superficial femoral vein, first described by Huber et al [16] , which reported two cases of use of this vein, one in the thigh and one in the arm and also reported by Gradman et al [17] , in a retrospective study of 25 cases, which used this technique in lower limbs. This technique, which is an exception procedure, showed very good results in its long-term use according to our findings.\n\n In addition, other complications such as distal ischemia, venous hypertension, cardiac decompensation, anastomotic pseudoaneurysm, aneurysmal dilatation and infection may be observed. For instance, Taylor et al [18] performed 45 grafts ("in loop" and "in thigh"), in whom polytetrafluoroethylene prosthesis were used in 39 cases and bovine carotid artery in six cases. They observed high rate of non-thrombotic complications with 18% of infection and 16% of distal limb ischemia.\n\n Our findings are of great relevance because the complications with vascular access, especially catheters, are major causes of morbidity and mortality in dialysis patients [1, 6, 7, 12] . Therefore, our findings fit with the guidelines recommendation [6, 7] , which is important for improving quality of life of patients with renal dialysis. \n\n The Unit of hemodialysis from our University is above the limits established by international norms, as evidenced by the analysis phase of the study.'],
    ['How do proinflammatory cytokines, such as IL-12 and TNF-α, contribute to the development and progression of atherosclerosis and heart failure?', 'In addition, TNF-α and IL-17 synergistically up-regulate further cytokine transcription in both diseases, Ps and atherogenesis [90] .\n\n These observations make IL-17A an interesting therapeutic target to modulate both PsA/Ps disease activity as well atherosclerosis/cardiovascular risk. Obesity may play an important role by amplifying the inflammation of arthritis through the Th1/Th17 response [91] .\n\n Limited evidence from Ps patients indicates that induction therapy with infliximab, with moderate to severe plaque Ps, led to decreases in clinical disease scores and circulating levels of Th17, Th1 cells and associated TNF-α release [92] .\n\n T cell activation is under control from T-regulatory immune cell (Treg) activity via IL-10 and TGF-β [93, 94] . Treg lymphocytes are characterized by expression of TGF-β, a T cell suppressive cytokine [95] . Reduced numbers and/or activity of Treg cells may produce hyperactivity of Th1 ⁄Th17 subsets in both pathologies [96] [97] [98] . Ps and coronary artery disease patients show impaired inhibitory function of Treg [99, 100] . Serum and epidermal levels [93, 94] of TGF-β in Ps patients are associated with Ps disease severity [101, 102] and are diminished in low Ps [5] . In atherosclerosis, high serum levels of TGF-β and IL-10 may inhibit plaque formation [103, 104] . In addition, TGF-β promotes plaque stabilization. Taken together protective effect of TGF-β is due to its inhibition of T cells. Of note, substance P (SP), the prototype tachykinin peptide, displays Nuclear Factor-Kappa β (Nf-κβ)-dependent proinflammatory effects, which are silenced by IL-10 and TGF-β in T lymphocytes and macrophages, respectively [105] .\n\n Not all immune responses that mounted during the course of atherosclerosis are pathogenic. Humoral response seems to protect rather than harm the host. Several lines of evidence support the hypothesis that humoral immunity protects patients against atherosclerosis. First, the injection of immunoglobulin preparations inhibits atherosclerosis. Second, spleen removal (a B-cellrich lymphoid organ) seems to deteriorate vascular disease condition. Third, oxidized LDL plus adjuvant immunization promote atheroprotection [2] . Although the underlying mediating mechanism of this effect remains poorly understood, most evidence so far indicates that athero-protection is due to a T cell dependent B-cell-mediated mechanism, probably involving antibody dependent clearance of LDL and T cell-mediated inhibition of vascular inflammation or humoral dependent regulation [15] . This atheroprotective response must be confirmed in humans.\n\n Ps, PsA and atherosclerosis share derangements in different metabolic pathways involving insulin-dependent diabetes mellitus (IDDM), dyslipidemia, hypertension, obesity, and mostly metabolic syndrome, which may be related to an increase in the prevalence of CVD. Ps/PsA derangements mentioned above may act due to their capability of inducing inflammation on the endothelial lining to initiate the process of atherosclerosis. So far, no pathophysiological mechanism for this association has been identified [52] .\n\n Several studies have found an increase in the prevalence of hypertension in Ps patients, although the definition of hypertension is very heterogeneous among these studies. The majority of these papers establish a relationship between the severity of Ps and the risk of hypertension [106] [107] [108] . Other authors have not observed a significant association between Ps and hypertension [109] .\n\n IDDM is responsible for metabolic alterations, accompanied by chronic inflammation and endothelium dysfunction. Observational studies show that the risk of IDDM is higher in patients with Ps compared with a healthy control group. This risk increases with the duration and severity of Ps and it is not related to a high body mass index (BMI) alone. In a case-control study from Israel, the risk of diabetes was significantly higher in individuals with Ps [110] . Similarly, PsA patients have a higher prevalence of IDDM, even after adjusting for the BMI [111] . TNFα antagonist therapy in patients with Ps seems to improve insulin sensitivity in limited preliminary data [112] . Finally, a few isolated cases of Ps patients with diabetes develop unpredictable hyperglycemia after starting treatment with TNF-α inhibitors [113] .\n\n Recent studies have shown that obesity may precede the onset of Ps as a risk factor [114] , whereas a higher BMI is associated with more severe skin disease activity [26] . The influence of obesity on psoriatic diseases is the result of complex interactions of inflammatory and metabolic factors.'],
]
scores = model.predict(pairs)
print(scores)
# [0.0012 0.0057 0.094  0.2822 0.0244]

# Or rank different texts based on similarity to a single text
ranks = model.rank(
    'What is the role of ultrasound fellowship training and familiarity with the sonographic appearance of SBO in accurately interpreting acquired POCUS images?\n',
    [
        'T he first report of musculoskeletal sonography was published in 1958 by Dussik et al 1 in a study that measured acoustic attenuation of articular and periarticular tissues. Technical advances and expanding indications in the 1970s popularized the use of ultrasonography in athletes. 2 In the 1980s and early 1990s, Middleton et al 3 and Harryman et al 4 first evaluated rotator cuff pathology using ultrasonography. In a more recent study, Yamaguchi et al 5 performed a longitudinal analysis of rotator cuff tears (RCTs) detected on sonograms. Ultrasonography is an operatordependent imaging modality, and clinical expertise in its use is paramount. Even with the use of well-defined protocols, substantial interobserver variability is associated with ultrasonography, and ultrasonography performed by clinicians rather than radiologists has led to debates with regard to training and level of competence. 6 Published training guidelines indicate that clinicians must perform 150 to 300 scans under the supervision of a qualified ultrasonographer or radiologist to develop proficiency. 6 In general, MRI is the preferred imaging modality for evaluation of the shoulder and elbow. In most patients, MRIs are comprehensive; however, arthrography often is required to improve the diagnostic accuracy of MRI for labral assessment. MRI is not well tolerated by some patients, may lead to incidental findings, and may be costly. In contrast, ultrasonography allows for rapid, Albert Lin, MD Gregory Gasbarro, MD Mark Sakr, DO dynamic examination, immediate clinical correlation, and image guidance during therapeutic procedures. Ultrasonography can be used for serial examination of soft tissues and affords real-time tissue elastography, which is a technique that allows for close monitoring of tendon and tissue quality with various muscle contraction conditions and joint positions. 7 Ultrasonography is an excellent educational tool for orthopaedic residency training, and interest in the use of this modality as an adjunct for physical examination of the shoulder and elbow has increased in the past two decades. Other benefits of ultrasonography include portability, decreased artifact from metal hardware, and contrast-enhanced Doppler applications that allow for real-time assessment of soft-tissue vascularity. 2, 8 In addition, ultrasonography is less expensive than MRI. In 2007, .80 million MRIs were performed in the United States, with a cost to the healthcare system of .$120 billion. 9 In a recent study of 146 patients who underwent ultrasonographic evaluation of shoulder pathology, Adelman and Fishman 9 reported that 35 MRIs were avoided with the use of ultrasonography, saving a predicted $17,603, which represented a 50% 1-year return on investment ($34,897) for the ultrasonography machine and equipment.\n\n Office-based musculoskeletal ultrasonography became possible as the quality of portable ultrasonography improved. Newer generation machines, which currently are the size of a laptop computer, replaced the large ultrasonography units typically used in hospitals. The ability to own and maneuver an ultrasonography machine in a clinic in combination with higher quality sonograms allowed for increased office-based musculoskeletal ultrasonography. The processing power, transducer capabilities, and software advances of newer ultrasonography machines also played an important role in the increased office-based use of the modality. Various ultrasonography machines are available for clinicians who desire in-office musculoskeletal ultrasonographic capability. Almost all modern models meet high-quality and function standards. Selection of an appropriate machine for a clinic requires consideration of the desired capabilities of interchangeable probes, desired image resolution, ease of use, comfort with the machine/interface, and cost. To become familiar with various ultrasonography machines, clinicians can contact manufacturers to test their machines and/or attend expositions to observe demonstrations of the newest features. Clinicians can contact colleagues and/or attend educational courses to determine the advantages and disadvantages of various ultrasonography machines.\n\n \n\n Ultrasonography is an accurate and cost-effective imaging modality for detection of partial-and full-thickness RCTs, demonstrating no statistically significant difference in sensitivity or specificity for detection of RCTs compared with arthrography or MRI. 3, 10 Murphy et al 6 reported on the learning curve among orthopaedic surgeons without prior experience who used ultrasonography for the detection of full-thickness supraspinatus tears. Arthroscopy was used as the standard of care for assessment of rotator cuff integrity. The authors found that orthopaedic surgeons had high levels of proficiency for the detection of RCTs during the first 50 scans performed. Notably, orthopaedic surgeon proficiency for the detection of RCTs during the second 50 scans performed was comparable with published data for surgeons with experience in shoulder ultrasonography and musculoskeletal radiologists.',
        'This should be done with careful attention to the needs of the main users of the synthesis.\n\n Discuss both the strengths of the review and its limitations. These should include (but need not be restricted to) (a) consideration of all the steps in the synthesis process and (b) comment on the overall strength of evidence supporting the explanatory insights that emerged.\n\n The limitations identified may point to areas where further work is needed. ... Authors seldom described or discussed the mechanisms that explained their study outcomes. We realise that the RCT design, the exacting reporting requirements and word limits of journals, restrict authors from sharing all their operational experiences. In addition RCTs tend to report average effects and not differential effects of interventions, and less so of the context and rarely of the mechanisms triggered by their interactions. This makes the RCTs less useful for answering the questions regarding how interventions work. These generic hypotheses seem to be recurring in the literature, however they have not been explicitly tested across contexts." [27] Explanation Realist synthesis may be constrained by time and resources, by the skill mix and collective experience of the research team, by the scope of the review\'s questions or objectives and/or by anticipated or unanticipated challenges in the data. These should be made explicit so that readers can interpret the findings in the light of them. A common challenge in realist synthesis is that in order to focus the synthesis, some material is omitted at each successive stage. Some aspects of the topic area, therefore, end up being reviewed in detail and rich explanatory insights produced for these. Other aspects are neglected (relatively or absolutely). It is thus inevitable that in generating illumination, the synthesis will also cast shadows. These should be highlighted in the discussion so as to indicate areas where other syntheses might focus.\n\n Strengths and/or limitations associated with any modifications made to the synthesis process should also be reported and justified.\n\n Where applicable, compare and contrast the synthesis\' findings with the existing literature (for example, other reviews) on the same topic.\n\n Example "We were unable to find any comparable attempt at providing an evidence-based-policy framework such as ours. However, we acknowledge that some sections of our framework may be found in sources we have not uncovered and also as tacit knowledge within the heads of seasoned practitioners (e.g. advocates or legislators). We do however hope that our attempts to develop and test it on our one \'case study\' will make a primordial tool that will be useful to policy and decisions makers less well versed in the arena of public health legislation." [26] Explanation Comparing and contrasting the findings from a synthesis with the existing literature may help readers to put these into context. For example, this item might cover questions such as: How does this synthesis compare to other reviews (for example, were they theory-driven?); What does this synthesis add?; Which body of work in particular does it add to?; Has this synthesis reached the same or different conclusion to previous reviews?; and Has it answered a question previously identified as important in the field?\n\n List the main implications of the findings and place these in the context of other relevant literature. If appropriate, offer recommendations for policy and practice.\n\n Example "Our realist review was based on a housing intervention in the United States, but the results can potentially be applied to urban centers in other nations that implement housing interventions that involve moving families. When a family moves, the experience is likely to be different for each member of the household, and differences in mental health outcomes of moving may occur (Reference x1). All communities, rich or poor, and irrespective of geographic location, should be viewed as complex systems, and as composed of people with social relationships that influence the functioning and health of community members." [28] Explanation A clear line of reasoning is needed to link the findings (Results section) with the implications (Discussion and/or Conclusion). If the synthesis is small and preliminary, or if the coherence and plausibility of evidence behind the inferences is weak or moderate, statements about implications for practice and policy should be appropriately guarded.\n\n If recommendations are given, these should take into account the focus of the synthesis and needs of the intended audience and be presented appropriately. The explanations in realist analysis are highly dependent on contextual influences. It follows that recommendations must be contingent (for example, only under certain contexts will a particular mechanism be triggered to generate the desired outcome) rather than statements that X should or should not be done.\n\n Provide details of funding source (if any) for the synthesis, the role played by the funder (if any) and any conflicts of interests of the reviewers.\n\n "We gratefully acknowledge a financial contribution from the Dutch Development Cooperation (DGIS)." [25] Explanation The source of funding for a synthesis and/or personal conflicts of interests may influence the research question, methods, data analysis and conclusions.',
        'Although this paradox is not fully understood, it may reflect functional redundancy in the canonical TLR and interleukin-1-receptor signaling pathways. Other efforts to target cytokines (e.g., interleukin-17 and 17 receptor, BLyS, APRIL, and GM-CSF) with the use of biologic approaches are ongoing. 55, 56 The range of available therapeutics based on the biologic characteristics of synovial cytokines will probably expand ( Table 2) .\n\n Elucidation of the complex intracellular signaling molecules (particularly kinases) that regulate cytokine-receptor-mediated functions may facilitate the development of specific small-molecule inhibitors. Although many intracellular signaling pathways are active in the synovium, clues to those with hierarchical importance have been provided by clinical trials. Positive clinical outcomes in phase 2 studies of the Janus kinase (JAK) 1 and 3 inhibitor tofacitinib implicate JAK pathways that mediate the function of several cytokines, interferons, and growth factors in the pathogenesis of rheumatoid arthritis 57, 58 (Table 2) . Moreover, inhibition of spleen tyrosine kinase by fostamatinib, which is effective in some subgroups of patients, is commensurate with its role in the function of B-cell and Fc receptors. 2213 ponents of the NF-κB pathway, offer intriguing possibilities for therapeutic strategies. In contrast, despite a strong preclinical rationale, the targeting of p38 mitogen-activated protein kinase has been disappointing in clinical settings, which probably indicates that the molecular signaling network in rheumatoid arthritis has functional redundancy.\n\n The normal synovium contains mesenchymal-derived, fibroblast-like synoviocytes (FLSs) and resident macrophages. In rheumatoid arthritis, the membrane lining is expanded, and FLSs assume a semiautonomous phenotype characterized by anchorage independence, loss of contact inhibition, and the expression of high levels of diseaserelevant cytokines and chemokines, adhesion molecules, matrix metalloproteinases (MMPs), and tissue inhibitors of metalloproteinases (TIMPs). 61 FLSs thereby contribute directly to local cartilage destruction and the chronicity of synovial inflammation, and they promote a permissive microenvironment that sustains T-cell and B-cell survival and adaptive immune organization. 62 The molecular mechanisms that sustain synovial hyperplasia are incompletely understood. The increased proliferative capacity of FLSs is not explanatory. A more likely possibility is altered resistance to apoptosis, which is mediated by diverse pathways, including mutations of the tumor-suppressor gene p53 63 ; expression of stress proteins (e.g., heat-shock protein 70), which foster the survival of FLSs 64 ; and modulation of the function of the endoplasmatic reticulum by synoviolin, an E3 ubiquitin ligase that regulates the balance of cell proliferation and apoptosis. 65 Synoviolin negatively regulates p53 expression and its biologic functions. In addition, cytokine-induced activation of the NF-κB pathway in FLSs favors survival after ligation of TNF-α receptor. Methylation and acetylation of cell-cycle regulatory genes and expression of microRNAs may be critical factors. 66 Synovial hyperplasia could also reflect increased influx of mesenchymal cells. In a mouse model of arthritis with severe combined immunodeficiency, FLSs were shown to migrate and thereby promote articular involvement. 67 A crucial advance has been the elucidation of the molecular pathways that sustain integral membrane structure in rheumatoid arthritis. Cadherin-11 and β-catenin mediate FLS-homotypic interactions that are essential for membrane formation and for subsequent inflammation. 68 \n\n \n\n A hyperplastic synovium is the major contributor to cartilage damage in rheumatoid arthritis. Loss of the normally protective effects of synovium (e.g., reduced expression of lubricin) 69 alter the protein-binding characteristics of the cartilage surface, promoting FLS adhesion and invasion. FLS synthesis of MMPs (particularly MMP-1, 3, 8, 13, 14, and 16) promotes disassembly of the type II collagen network, a process that alters glycosaminoglycan content and water retention and leads directly to biomechanical dysfunction. MMP-14 appears to be the predominant MMP expressed by FLSs to degrade the collagenous cartilage matrix. 70 Other matrix enzymes (e.g., ADAMTS 5) degrade aggrecan and thus further diminish cartilage integrity.\n\n Endogenous enzyme inhibitors, such as TIMPs, fail to reverse this destructive cascade. Moreover, articular cartilage itself has limited regenerative potential.',
        'Patients on dialysis for long-term catheter and without maturing fistula (12 patients) had a mean time of 5.46 months of use and had already exhausted their chances of making fistulas. The most frequent type of fistula use was on the radio distal cephalic, in 85 patients (52.5%), followed by radio cephalic proximal in 26 patients (16%) ( Table 3) .\n\n The number of fistulas in dialysis patients conducted by this kind of therapy ranged from one to ten and in 64 patients (41.83%) fistula was the first and only to be made. Among the fistula for dialysis patients, the highest prevalence was radio cephalic fistula in 111 patients (72.5%) and mean duration of use was 48.1 months, ranging from two months to 17 years. These patients had an average of 0.89 prior fistulas, and in 46 patients (30%) it was the only fistula. Among the most frequent complications observed in fistulas in use, the pseudo-aneurysm after puncture and venous hypertension were the most common.\n\n It was created in 1997, the NKF-DOQI, establishing guidelines for standardization of care for chronic kidney illness to dialysis in relation to vascular access in order to decrease the complications and cost, improve the dialysis quality, thus, improving the patients quality of life, since it was reported high number of use and complications of vascular access for hemodialysis due to catheter use and fistula with prosthesis [13] . The periodic review of access for hemodialysis is intended to be performed on all services in order to monitor their adequacy in relation to international guidelines. According to these premises, we performed at the Unit of Nephrology from our University an investigation which aims to verify the adequacy and monitor the vascular access, within the standards established by the guidelines (NKF-DOQI 2006). The number of catheters reported in our study is in accordance with the recommended by the NKF-DOQI and a large proportion of patients with short-term catheters presented fistulas in maturation. Making fistulas in patients before dialysis is a target in our service, it is difficult because our patients are often at the endstage of renal disease. Patients with long-term catheters are at the stage of exhaustion of vascular accesses and some of them had fistulas at maturity which is also in agreement with the guidelines.\n\n In a recent investigation published by our group, which evaluated saphenofemoral fistula as vascular access for hemodialysis [3] , it was observed some cases of thrombosis due to prolonged arterial hypotension and one case due to trauma of the fistula site at home environment. By studying this type of complication, we alert to the importance of maintaining regular surveillance with periodic evaluation of these fistulas in order to detect early dysfunction so that it may be corrected in time, reducing the risk of thrombosis and increasing the usefulness period of the fistula [14] .\n\n According to our findings the percentage of patients under dialysis with arteriovenous fistulas was higher than the recommended by the NKF-DOQI 2006 (70%). Furthermore, the location of fistulas is in accordance with the guidelines. We reported predominance of distal radio-cephalic, which has a high rate in the primary fistulas, which is the ideal combination for the patient because it is related to a lower complication rate and, hence, improved quality of life [6, 7] . Some issues should be addressed when taking vascular access for hemodialysis. According to a recent study, the limitation of saphenofemoral arteriovenous fistula as hemodialysis access is given in cases when the patient presents saphenous vein absence or when the saphenous vein is inadequate for this purpose and also in patients with arterial occlusive disease in the femoropopliteal territory. Another limitation of this technique is that the saphenous vein prevents the development of the fistula due to its developed muscle layer, similar to the cephalic vein in the internal forearm arteriovenous fistula. Although it prevents aneurysmal dilatation it increases the risk of myointimal hyperplasia after repeated punctures of the arteriovenous fistula [15] . On the other hand, because it is autologous material, it presents low cost, higher infection resistance and it is easy to handling, the advantages compensate its limitations even when compared to other access techniques in lower limbs which also uses autologous material such as transposition of the superficial femoral vein, first described by Huber et al [16] , which reported two cases of use of this vein, one in the thigh and one in the arm and also reported by Gradman et al [17] , in a retrospective study of 25 cases, which used this technique in lower limbs. This technique, which is an exception procedure, showed very good results in its long-term use according to our findings.\n\n In addition, other complications such as distal ischemia, venous hypertension, cardiac decompensation, anastomotic pseudoaneurysm, aneurysmal dilatation and infection may be observed. For instance, Taylor et al [18] performed 45 grafts ("in loop" and "in thigh"), in whom polytetrafluoroethylene prosthesis were used in 39 cases and bovine carotid artery in six cases. They observed high rate of non-thrombotic complications with 18% of infection and 16% of distal limb ischemia.\n\n Our findings are of great relevance because the complications with vascular access, especially catheters, are major causes of morbidity and mortality in dialysis patients [1, 6, 7, 12] . Therefore, our findings fit with the guidelines recommendation [6, 7] , which is important for improving quality of life of patients with renal dialysis. \n\n The Unit of hemodialysis from our University is above the limits established by international norms, as evidenced by the analysis phase of the study.',
        'In addition, TNF-α and IL-17 synergistically up-regulate further cytokine transcription in both diseases, Ps and atherogenesis [90] .\n\n These observations make IL-17A an interesting therapeutic target to modulate both PsA/Ps disease activity as well atherosclerosis/cardiovascular risk. Obesity may play an important role by amplifying the inflammation of arthritis through the Th1/Th17 response [91] .\n\n Limited evidence from Ps patients indicates that induction therapy with infliximab, with moderate to severe plaque Ps, led to decreases in clinical disease scores and circulating levels of Th17, Th1 cells and associated TNF-α release [92] .\n\n T cell activation is under control from T-regulatory immune cell (Treg) activity via IL-10 and TGF-β [93, 94] . Treg lymphocytes are characterized by expression of TGF-β, a T cell suppressive cytokine [95] . Reduced numbers and/or activity of Treg cells may produce hyperactivity of Th1 ⁄Th17 subsets in both pathologies [96] [97] [98] . Ps and coronary artery disease patients show impaired inhibitory function of Treg [99, 100] . Serum and epidermal levels [93, 94] of TGF-β in Ps patients are associated with Ps disease severity [101, 102] and are diminished in low Ps [5] . In atherosclerosis, high serum levels of TGF-β and IL-10 may inhibit plaque formation [103, 104] . In addition, TGF-β promotes plaque stabilization. Taken together protective effect of TGF-β is due to its inhibition of T cells. Of note, substance P (SP), the prototype tachykinin peptide, displays Nuclear Factor-Kappa β (Nf-κβ)-dependent proinflammatory effects, which are silenced by IL-10 and TGF-β in T lymphocytes and macrophages, respectively [105] .\n\n Not all immune responses that mounted during the course of atherosclerosis are pathogenic. Humoral response seems to protect rather than harm the host. Several lines of evidence support the hypothesis that humoral immunity protects patients against atherosclerosis. First, the injection of immunoglobulin preparations inhibits atherosclerosis. Second, spleen removal (a B-cellrich lymphoid organ) seems to deteriorate vascular disease condition. Third, oxidized LDL plus adjuvant immunization promote atheroprotection [2] . Although the underlying mediating mechanism of this effect remains poorly understood, most evidence so far indicates that athero-protection is due to a T cell dependent B-cell-mediated mechanism, probably involving antibody dependent clearance of LDL and T cell-mediated inhibition of vascular inflammation or humoral dependent regulation [15] . This atheroprotective response must be confirmed in humans.\n\n Ps, PsA and atherosclerosis share derangements in different metabolic pathways involving insulin-dependent diabetes mellitus (IDDM), dyslipidemia, hypertension, obesity, and mostly metabolic syndrome, which may be related to an increase in the prevalence of CVD. Ps/PsA derangements mentioned above may act due to their capability of inducing inflammation on the endothelial lining to initiate the process of atherosclerosis. So far, no pathophysiological mechanism for this association has been identified [52] .\n\n Several studies have found an increase in the prevalence of hypertension in Ps patients, although the definition of hypertension is very heterogeneous among these studies. The majority of these papers establish a relationship between the severity of Ps and the risk of hypertension [106] [107] [108] . Other authors have not observed a significant association between Ps and hypertension [109] .\n\n IDDM is responsible for metabolic alterations, accompanied by chronic inflammation and endothelium dysfunction. Observational studies show that the risk of IDDM is higher in patients with Ps compared with a healthy control group. This risk increases with the duration and severity of Ps and it is not related to a high body mass index (BMI) alone. In a case-control study from Israel, the risk of diabetes was significantly higher in individuals with Ps [110] . Similarly, PsA patients have a higher prevalence of IDDM, even after adjusting for the BMI [111] . TNFα antagonist therapy in patients with Ps seems to improve insulin sensitivity in limited preliminary data [112] . Finally, a few isolated cases of Ps patients with diabetes develop unpredictable hyperglycemia after starting treatment with TNF-α inhibitors [113] .\n\n Recent studies have shown that obesity may precede the onset of Ps as a risk factor [114] , whereas a higher BMI is associated with more severe skin disease activity [26] . The influence of obesity on psoriatic diseases is the result of complex interactions of inflammatory and metabolic factors.',
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

#### Cross Encoder Reranking

* Datasets: `NanoNFCorpus_R100`, `NanoSciFact_R100` and `NanoSCIDOCS_R100`
* Evaluated with [<code>CrossEncoderRerankingEvaluator</code>](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderRerankingEvaluator) with these parameters:
  ```json
  {
      "at_k": 10,
      "always_rerank_positives": true
  }
  ```

| Metric      | NanoNFCorpus_R100    | NanoSciFact_R100     | NanoSCIDOCS_R100     |
|:------------|:---------------------|:---------------------|:---------------------|
| map         | 0.4398 (+0.1788)     | 0.2911 (-0.3787)     | 0.2516 (-0.0227)     |
| mrr@10      | 0.6895 (+0.1897)     | 0.2754 (-0.4027)     | 0.4591 (-0.1004)     |
| **ndcg@10** | **0.5159 (+0.1909)** | **0.2954 (-0.4145)** | **0.2918 (-0.0433)** |

#### Cross Encoder Nano BEIR

* Dataset: `NanoBEIR_R100_mean`
* Evaluated with [<code>CrossEncoderNanoBEIREvaluator</code>](https://sbert.net/docs/package_reference/cross_encoder/evaluation.html#sentence_transformers.cross_encoder.evaluation.CrossEncoderNanoBEIREvaluator) with these parameters:
  ```json
  {
      "dataset_names": [
          "nfcorpus",
          "scifact",
          "scidocs"
      ],
      "dataset_id": "sentence-transformers/NanoBEIR-en",
      "rerank_k": 100,
      "at_k": 10,
      "always_rerank_positives": true
  }
  ```

| Metric      | Value                |
|:------------|:---------------------|
| map         | 0.3275 (-0.0742)     |
| mrr@10      | 0.4747 (-0.1045)     |
| **ndcg@10** | **0.3677 (-0.0890)** |

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

* Size: 898,469 training samples
* Columns: <code>question</code>, <code>passage_text</code>, and <code>label</code>
* Approximate statistics based on the first 100 samples:
  |          | question                                                                           | passage_text                                                                         | label                                           |
  |:---------|:-----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:------------------------------------------------|
  | type     | string                                                                             | string                                                                               | int                                             |
  | modality | text                                                                               | text                                                                                 |                                                 |
  | details  | <ul><li>min: 10 tokens</li><li>mean: 20.71 tokens</li><li>max: 37 tokens</li></ul> | <ul><li>min: 384 tokens</li><li>mean: 384.0 tokens</li><li>max: 384 tokens</li></ul> | <ul><li>0: ~79.81%</li><li>1: ~20.19%</li></ul> |
* Samples:
  | question                                                                                                                                                                            | passage_text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | label          |
  |:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
  | <code>What are the challenges in controlling vancomycin use and nosocomial transmission of VRE?<br></code>                                                                          | <code>Over the past two decades, the emergence of vancomycinresistant Enterococcus (VRE) as a nosocomial pathogen has been attributed to a complex interaction of epidemiologic forces including nosocomial transmission and antimicrobial pressure [1] [2] [3] . In particular, the use of selected antibiotics such as vancomycin, expanded-spectrum cephalosporins, and agents with potent anaerobic activity has been found to promote individual patients to gastrointestinal colonization with VRE [4] . Nevertheless, the role of antibiotic exposure in both colonization and infection remains controversial [3, 5, 6] . Efforts to control vancomycin use and nosocomial transmission have had limited success, and rates of invasive VRE in the USA remains on the rise [7] . Furthermore, mortality and hospital costs associated with VRE-BSI are significantly high, especially among immunocompromised patients [8] .

   We sought to evaluate the association between aggregate and individual-patient vancomycin-exposure, clo...</code> | <code>1</code> |
  | <code>What are some radiological findings associated with smoking-induced COPD?<br></code>                                                                                          | <code>In patients with smoking-induced COPD, many previous publications analyzing radiological findings have reported heterogeneous distributions of emphysema, airflow, or even blood flow in the affected lung. For example, multiple papers have demonstrated that heterogeneous emphysema distribution and inhomogeneous cluster sizes of emphysema exist in the lung by analyzing chest CT; [1] [2] [3] [4] [5] that heterogeneous gas trapping and pulmonary volume changes are observed on paired inspiratory and expiratory CT scans; [6] [7] [8] [9] [10] and that, on contrast-enhanced magnetic resonance (MR) imaging and hyperpolarized helium/xenon MR, both blood flow and airflow are distributed heterogeneously in the lung in COPD patients. [11] [12] [13] Similar inhomogeneous air

 

 

   Yamashiro et al distribution in the lung by ventilation has also been confirmed by scintigraphy in COPD patients. 14 While these observations of the COPD lung have been based on static imaging techniques, some reports usi...</code> | <code>1</code> |
  | <code>What are the typical radiological features and histologic subtypes associated with ameloblastoma, and how do these characteristics inform its diagnosis and treatment?</code> | <code>The typical presentation on ultrasonography is heterogeneous hypoechogenicity, well-defined or infiltrated margins, scalloped contour, solid and/or necrotic content, moderate to large size, marked hypervascularity on CDUS, low to moderate RI, and surrounding bony destruction if the tumor involves the bone.

   Rhabdomyosarcoma is the most common soft tissue malignancy in children, but is rare in the extremities [62] . The role of ultrasound is to provide information regarding tumor size and internal characteristics, and in guided biopsy. CDUS can determine vascularity but does not aid in differential diagnosis [63, 64] . The ultrasonographic pattern is heterogeneous hypoechogenicity, infiltrated margins, lobulated contour, solid content, moderate size, moderate vascularity on CDUS, and moderate RI.

   Fibromyxoid sarcoma is classified as a fibromyoblastic soft tissue tumor. Its incidence is very rare. The ultrasonographic pattern is heterogeneous hypoechogenicity, well-defined margins, ov...</code> | <code>0</code> |
* Loss: [<code>BinaryCrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#binarycrossentropyloss) with these parameters:
  ```json
  {
      "activation_fn": "torch.nn.modules.linear.Identity",
      "pos_weight": 4.991311073303223
  }
  ```

### Evaluation Dataset

#### Unnamed Dataset

* Size: 6,000 evaluation samples
* Columns: <code>question</code>, <code>passage_text</code>, and <code>label</code>
* Approximate statistics based on the first 100 samples:
  |          | question                                                                          | passage_text                                                                         | label                                           |
  |:---------|:----------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------|:------------------------------------------------|
  | type     | string                                                                            | string                                                                               | int                                             |
  | modality | text                                                                              | text                                                                                 |                                                 |
  | details  | <ul><li>min: 9 tokens</li><li>mean: 21.04 tokens</li><li>max: 46 tokens</li></ul> | <ul><li>min: 384 tokens</li><li>mean: 384.0 tokens</li><li>max: 384 tokens</li></ul> | <ul><li>0: ~82.69%</li><li>1: ~17.31%</li></ul> |
* Samples:
  | question                                                                                                                                                                     | passage_text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | label          |
  |:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------|
  | <code>What is the role of ultrasound fellowship training and familiarity with the sonographic appearance of SBO in accurately interpreting acquired POCUS images?<br></code> | <code>T he first report of musculoskeletal sonography was published in 1958 by Dussik et al 1 in a study that measured acoustic attenuation of articular and periarticular tissues. Technical advances and expanding indications in the 1970s popularized the use of ultrasonography in athletes. 2 In the 1980s and early 1990s, Middleton et al 3 and Harryman et al 4 first evaluated rotator cuff pathology using ultrasonography. In a more recent study, Yamaguchi et al 5 performed a longitudinal analysis of rotator cuff tears (RCTs) detected on sonograms. Ultrasonography is an operatordependent imaging modality, and clinical expertise in its use is paramount. Even with the use of well-defined protocols, substantial interobserver variability is associated with ultrasonography, and ultrasonography performed by clinicians rather than radiologists has led to debates with regard to training and level of competence. 6 Published training guidelines indicate that clinicians must perform 150 to 300 scans under ...</code> | <code>0</code> |
  | <code>How should study results in the context of respiratory conditions be interpreted and what is the importance of considering the perspective of patients?<br></code>     | <code>This should be done with careful attention to the needs of the main users of the synthesis.

   Discuss both the strengths of the review and its limitations. These should include (but need not be restricted to) (a) consideration of all the steps in the synthesis process and (b) comment on the overall strength of evidence supporting the explanatory insights that emerged.

   The limitations identified may point to areas where further work is needed. ... Authors seldom described or discussed the mechanisms that explained their study outcomes. We realise that the RCT design, the exacting reporting requirements and word limits of journals, restrict authors from sharing all their operational experiences. In addition RCTs tend to report average effects and not differential effects of interventions, and less so of the context and rarely of the mechanisms triggered by their interactions. This makes the RCTs less useful for answering the questions regarding how interventions work. These generic hyp...</code> | <code>0</code> |
  | <code>What are the potential therapeutic strategies for targeting NF-κB in autoimmune diseases?<br></code>                                                                   | <code>Although this paradox is not fully understood, it may reflect functional redundancy in the canonical TLR and interleukin-1-receptor signaling pathways. Other efforts to target cytokines (e.g., interleukin-17 and 17 receptor, BLyS, APRIL, and GM-CSF) with the use of biologic approaches are ongoing. 55, 56 The range of available therapeutics based on the biologic characteristics of synovial cytokines will probably expand ( Table 2) .

   Elucidation of the complex intracellular signaling molecules (particularly kinases) that regulate cytokine-receptor-mediated functions may facilitate the development of specific small-molecule inhibitors. Although many intracellular signaling pathways are active in the synovium, clues to those with hierarchical importance have been provided by clinical trials. Positive clinical outcomes in phase 2 studies of the Janus kinase (JAK) 1 and 3 inhibitor tofacitinib implicate JAK pathways that mediate the function of several cytokines, interferons, and growth fa...</code> | <code>0</code> |
* Loss: [<code>BinaryCrossEntropyLoss</code>](https://sbert.net/docs/package_reference/cross_encoder/losses.html#binarycrossentropyloss) with these parameters:
  ```json
  {
      "activation_fn": "torch.nn.modules.linear.Identity",
      "pos_weight": 4.991311073303223
  }
  ```

### Training Hyperparameters
#### Non-Default Hyperparameters

- `per_device_train_batch_size`: 64
- `num_train_epochs`: 1
- `learning_rate`: 2e-05
- `warmup_steps`: 0.1
- `weight_decay`: 0.01
- `bf16`: True
- `per_device_eval_batch_size`: 64
- `push_to_hub`: True
- `hub_private_repo`: False
- `hub_model_id`: tomaarsen/reranker-PubMedBERT-base-MIRIAD-150k
- `load_best_model_at_end`: True
- `seed`: 12

#### All Hyperparameters
<details><summary>Click to expand</summary>

- `per_device_train_batch_size`: 64
- `num_train_epochs`: 1
- `max_steps`: -1
- `learning_rate`: 2e-05
- `lr_scheduler_type`: linear
- `lr_scheduler_kwargs`: None
- `warmup_steps`: 0.1
- `optim`: adamw_torch_fused
- `optim_args`: None
- `weight_decay`: 0.01
- `adam_beta1`: 0.9
- `adam_beta2`: 0.999
- `adam_epsilon`: 1e-08
- `optim_target_modules`: None
- `gradient_accumulation_steps`: 1
- `average_tokens_across_devices`: True
- `max_grad_norm`: 1.0
- `label_smoothing_factor`: 0.0
- `bf16`: True
- `fp16`: False
- `bf16_full_eval`: False
- `fp16_full_eval`: False
- `tf32`: None
- `gradient_checkpointing`: False
- `gradient_checkpointing_kwargs`: None
- `torch_compile`: False
- `torch_compile_backend`: None
- `torch_compile_mode`: None
- `use_liger_kernel`: False
- `liger_kernel_config`: None
- `use_cache`: False
- `neftune_noise_alpha`: None
- `torch_empty_cache_steps`: None
- `auto_find_batch_size`: False
- `log_on_each_node`: True
- `logging_nan_inf_filter`: True
- `include_num_input_tokens_seen`: no
- `log_level`: passive
- `log_level_replica`: warning
- `disable_tqdm`: False
- `project`: huggingface
- `trackio_space_id`: None
- `trackio_bucket_id`: None
- `trackio_static_space_id`: None
- `per_device_eval_batch_size`: 64
- `prediction_loss_only`: True
- `eval_on_start`: False
- `eval_do_concat_batches`: True
- `eval_use_gather_object`: False
- `eval_accumulation_steps`: None
- `include_for_metrics`: []
- `batch_eval_metrics`: False
- `save_only_model`: False
- `save_on_each_node`: False
- `enable_jit_checkpoint`: False
- `push_to_hub`: True
- `hub_private_repo`: False
- `hub_model_id`: tomaarsen/reranker-PubMedBERT-base-MIRIAD-150k
- `hub_strategy`: every_save
- `hub_always_push`: False
- `hub_revision`: None
- `load_best_model_at_end`: True
- `ignore_data_skip`: False
- `restore_callback_states_from_checkpoint`: False
- `full_determinism`: False
- `seed`: 12
- `data_seed`: None
- `use_cpu`: False
- `accelerator_config`: {'split_batches': False, 'dispatch_batches': None, 'even_batches': True, 'use_seedable_sampler': True, 'non_blocking': False, 'gradient_accumulation_kwargs': None}
- `parallelism_config`: None
- `dataloader_drop_last`: False
- `dataloader_num_workers`: 0
- `dataloader_pin_memory`: True
- `dataloader_persistent_workers`: False
- `dataloader_prefetch_factor`: None
- `remove_unused_columns`: True
- `label_names`: None
- `train_sampling_strategy`: random
- `length_column_name`: length
- `ddp_find_unused_parameters`: None
- `ddp_bucket_cap_mb`: None
- `ddp_broadcast_buffers`: False
- `ddp_static_graph`: None
- `ddp_backend`: None
- `ddp_timeout`: 1800
- `fsdp`: []
- `fsdp_config`: {'min_num_params': 0, 'xla': False, 'xla_fsdp_v2': False, 'xla_fsdp_grad_ckpt': False}
- `deepspeed`: None
- `debug`: []
- `skip_memory_metrics`: True
- `do_predict`: False
- `resume_from_checkpoint`: None
- `warmup_ratio`: None
- `local_rank`: -1
- `prompts`: None
- `batch_sampler`: batch_sampler
- `multi_dataset_batch_sampler`: proportional
- `router_mapping`: {}
- `learning_rate_mapping`: {}

</details>

### Training Logs
| Epoch  | Step | Training Loss | Validation Loss | NanoNFCorpus_R100_ndcg@10 | NanoSciFact_R100_ndcg@10 | NanoSCIDOCS_R100_ndcg@10 | NanoBEIR_R100_mean_ndcg@10 |
|:------:|:----:|:-------------:|:---------------:|:-------------------------:|:------------------------:|:------------------------:|:--------------------------:|
| -1     | -1   | -             | -               | 0.3377 (+0.0127)          | 0.6485 (-0.0614)         | 0.3023 (-0.0328)         | 0.4295 (-0.0272)           |
| 0.1004 | 1410 | 0.3438        | -               | -                         | -                        | -                        | -                          |
| 0.1105 | 1551 | 0.3339        | -               | -                         | -                        | -                        | -                          |
| 0.1205 | 1692 | 0.3438        | -               | -                         | -                        | -                        | -                          |
| 0.1306 | 1833 | 0.3605        | -               | -                         | -                        | -                        | -                          |
| 0.1406 | 1974 | 0.3272        | -               | -                         | -                        | -                        | -                          |
| 0.1507 | 2115 | 0.3643        | -               | -                         | -                        | -                        | -                          |
| 0.1607 | 2256 | 0.3712        | -               | -                         | -                        | -                        | -                          |
| 0.1707 | 2397 | 0.3388        | -               | -                         | -                        | -                        | -                          |
| 0.1808 | 2538 | 0.3199        | -               | -                         | -                        | -                        | -                          |
| 0.1908 | 2679 | 0.3151        | -               | -                         | -                        | -                        | -                          |
| 0.2000 | 2808 | -             | 0.3043          | 0.4736 (+0.1486)          | 0.4531 (-0.2568)         | 0.3683 (+0.0331)         | 0.4316 (-0.0250)           |
| 0.2009 | 2820 | 0.3021        | -               | -                         | -                        | -                        | -                          |
| 0.2109 | 2961 | 0.3268        | -               | -                         | -                        | -                        | -                          |
| 0.2210 | 3102 | 0.3201        | -               | -                         | -                        | -                        | -                          |
| 0.2310 | 3243 | 0.3266        | -               | -                         | -                        | -                        | -                          |
| 0.2410 | 3384 | 0.3287        | -               | -                         | -                        | -                        | -                          |
| 0.2511 | 3525 | 0.2935        | -               | -                         | -                        | -                        | -                          |
| 0.2611 | 3666 | 0.3344        | -               | -                         | -                        | -                        | -                          |
| 0.2712 | 3807 | 0.3141        | -               | -                         | -                        | -                        | -                          |
| 0.2812 | 3948 | 0.3202        | -               | -                         | -                        | -                        | -                          |
| 0.2913 | 4089 | 0.2907        | -               | -                         | -                        | -                        | -                          |
| 0.3000 | 4212 | -             | 0.2880          | 0.5226 (+0.1976)          | 0.4837 (-0.2262)         | 0.3545 (+0.0194)         | 0.4536 (-0.0031)           |
| 0.3013 | 4230 | 0.3021        | -               | -                         | -                        | -                        | -                          |
| 0.3113 | 4371 | 0.2932        | -               | -                         | -                        | -                        | -                          |
| 0.3214 | 4512 | 0.2724        | -               | -                         | -                        | -                        | -                          |
| 0.3314 | 4653 | 0.3095        | -               | -                         | -                        | -                        | -                          |
| 0.3415 | 4794 | 0.3216        | -               | -                         | -                        | -                        | -                          |
| 0.3515 | 4935 | 0.3067        | -               | -                         | -                        | -                        | -                          |
| 0.3616 | 5076 | 0.3140        | -               | -                         | -                        | -                        | -                          |
| 0.3716 | 5217 | 0.2823        | -               | -                         | -                        | -                        | -                          |
| 0.3817 | 5358 | 0.2952        | -               | -                         | -                        | -                        | -                          |
| 0.3917 | 5499 | 0.3036        | -               | -                         | -                        | -                        | -                          |
| 0.4000 | 5616 | -             | 0.2560          | 0.5159 (+0.1909)          | 0.2954 (-0.4145)         | 0.2918 (-0.0433)         | 0.3677 (-0.0890)           |


### Training Time
- **Training**: 30.1 minutes
- **Evaluation**: 2.4 minutes
- **Total**: 32.4 minutes

### Framework Versions
- Python: 3.11.6
- Sentence Transformers: 5.5.0.dev0
- Transformers: 5.6.2
- PyTorch: 2.10.0+cu128
- Accelerate: 1.13.0.dev0
- Datasets: 4.8.4
- Tokenizers: 0.22.2

## Additional Resources

- [Training and Finetuning Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-reranker): the end-to-end guide for training or finetuning Cross Encoder (reranker) models.
- [Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/multimodal-sentence-transformers): use text, image, audio, and video reranker models through the same API.
- [Training and Finetuning Multimodal Embedding & Reranker Models with Sentence Transformers](https://huggingface.co/blog/train-multimodal-sentence-transformers): training multimodal Cross Encoders.

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