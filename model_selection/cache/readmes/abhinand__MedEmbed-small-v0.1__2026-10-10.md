---
base_model:
- BAAI/bge-small-en-v1.5
datasets:
- MedicalQARetrieval
- NFCorpus
- PublicHealthQA
- TRECCOVID
- ArguAna
language: en
license: apache-2.0
metrics:
- nDCG
- MAP
- Recall
- Precision
- MRR
model-index:
- name: abhinand/MedEmbed-small-v0.1
  results:
  - dataset:
      config: en-ext
      name: MTEB AmazonCounterfactualClassification (en-ext)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 72.17391304347827
    - type: ap
      value: 21.757637881353535
    - type: ap_weighted
      value: 21.757637881353535
    - type: f1
      value: 59.80304692298741
    - type: f1_weighted
      value: 77.3761270422597
    - type: main_score
      value: 72.17391304347827
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonCounterfactualClassification (en)
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
      split: test
      type: mteb/amazon_counterfactual
    metrics:
    - type: accuracy
      value: 71.28358208955224
    - type: ap
      value: 33.51413347752456
    - type: ap_weighted
      value: 33.51413347752456
    - type: f1
      value: 65.07760889689999
    - type: f1_weighted
      value: 74.00602410875776
    - type: main_score
      value: 71.28358208955224
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB AmazonPolarityClassification (default)
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
      split: test
      type: mteb/amazon_polarity
    metrics:
    - type: accuracy
      value: 91.99472500000002
    - type: ap
      value: 88.24057492408383
    - type: ap_weighted
      value: 88.24057492408383
    - type: f1
      value: 91.97746777375899
    - type: f1_weighted
      value: 91.97746777375899
    - type: main_score
      value: 91.99472500000002
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB AmazonReviewsClassification (en)
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
      split: test
      type: mteb/amazon_reviews_multi
    metrics:
    - type: accuracy
      value: 48.211999999999996
    - type: f1
      value: 46.94308842799891
    - type: f1_weighted
      value: 46.94308842799891
    - type: main_score
      value: 48.211999999999996
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB ArguAna (default)
      revision: c22ab2a51041ffd869aaddef7af8d8215647e41a
      split: test
      type: mteb/arguana
    metrics:
    - type: main_score
      value: 61.587
    - type: map_at_1
      value: 37.980000000000004
    - type: map_at_10
      value: 53.40200000000001
    - type: map_at_100
      value: 54.032000000000004
    - type: map_at_1000
      value: 54.038
    - type: map_at_20
      value: 53.898999999999994
    - type: map_at_3
      value: 49.123
    - type: map_at_5
      value: 51.747
    - type: mrr_at_1
      value: 38.26458036984353
    - type: mrr_at_10
      value: 53.522206416943355
    - type: mrr_at_100
      value: 54.145400691658374
    - type: mrr_at_1000
      value: 54.150812285856695
    - type: mrr_at_20
      value: 54.015571340811796
    - type: mrr_at_3
      value: 49.3006164058796
    - type: mrr_at_5
      value: 51.850403034613656
    - type: nauc_map_at_1000_diff1
      value: 12.462809218755954
    - type: nauc_map_at_1000_max
      value: -8.081945194296322
    - type: nauc_map_at_1000_std
      value: -6.165333174593185
    - type: nauc_map_at_100_diff1
      value: 12.46115346472636
    - type: nauc_map_at_100_max
      value: -8.07700864766809
    - type: nauc_map_at_100_std
      value: -6.154824360110573
    - type: nauc_map_at_10_diff1
      value: 12.247142312490714
    - type: nauc_map_at_10_max
      value: -8.05437952054825
    - type: nauc_map_at_10_std
      value: -5.98349855940482
    - type: nauc_map_at_1_diff1
      value: 15.505336965073605
    - type: nauc_map_at_1_max
      value: -10.866105149439845
    - type: nauc_map_at_1_std
      value: -9.694177220362505
    - type: nauc_map_at_20_diff1
      value: 12.449923215332698
    - type: nauc_map_at_20_max
      value: -8.061694795957425
    - type: nauc_map_at_20_std
      value: -6.048155776035038
    - type: nauc_map_at_3_diff1
      value: 11.777509442505403
    - type: nauc_map_at_3_max
      value: -8.619619751268965
    - type: nauc_map_at_3_std
      value: -7.029734930936095
    - type: nauc_map_at_5_diff1
      value: 12.072349873282578
    - type: nauc_map_at_5_max
      value: -7.9037810476976835
    - type: nauc_map_at_5_std
      value: -6.3962966098864
    - type: nauc_mrr_at_1000_diff1
      value: 11.55871613635287
    - type: nauc_mrr_at_1000_max
      value: -8.524668018179772
    - type: nauc_mrr_at_1000_std
      value: -5.821749837488739
    - type: nauc_mrr_at_100_diff1
      value: 11.557229356469213
    - type: nauc_mrr_at_100_max
      value: -8.519652075012466
    - type: nauc_mrr_at_100_std
      value: -5.811310846389489
    - type: nauc_mrr_at_10_diff1
      value: 11.386476038925435
    - type: nauc_mrr_at_10_max
      value: -8.45430627552755
    - type: nauc_mrr_at_10_std
      value: -5.65917735429017
    - type: nauc_mrr_at_1_diff1
      value: 14.693476121231305
    - type: nauc_mrr_at_1_max
      value: -10.94460265018313
    - type: nauc_mrr_at_1_std
      value: -8.77030471829497
    - type: nauc_mrr_at_20_diff1
      value: 11.541143108641904
    - type: nauc_mrr_at_20_max
      value: -8.508664836852851
    - type: nauc_mrr_at_20_std
      value: -5.718714620902282
    - type: nauc_mrr_at_3_diff1
      value: 11.065095966162826
    - type: nauc_mrr_at_3_max
      value: -8.88590386152548
    - type: nauc_mrr_at_3_std
      value: -6.741394531507113
    - type: nauc_mrr_at_5_diff1
      value: 11.143404810693896
    - type: nauc_mrr_at_5_max
      value: -8.410832856819567
    - type: nauc_mrr_at_5_std
      value: -6.101439716672843
    - type: nauc_ndcg_at_1000_diff1
      value: 12.251069053520732
    - type: nauc_ndcg_at_1000_max
      value: -7.386319921375587
    - type: nauc_ndcg_at_1000_std
      value: -5.2642773188011205
    - type: nauc_ndcg_at_100_diff1
      value: 12.205700301839183
    - type: nauc_ndcg_at_100_max
      value: -7.248372196650524
    - type: nauc_ndcg_at_100_std
      value: -4.970330352461419
    - type: nauc_ndcg_at_10_diff1
      value: 11.523326871708202
    - type: nauc_ndcg_at_10_max
      value: -6.816950583275555
    - type: nauc_ndcg_at_10_std
      value: -3.9784804860320198
    - type: nauc_ndcg_at_1_diff1
      value: 15.505336965073605
    - type: nauc_ndcg_at_1_max
      value: -10.866105149439845
    - type: nauc_ndcg_at_1_std
      value: -9.694177220362505
    - type: nauc_ndcg_at_20_diff1
      value: 12.270064495647071
    - type: nauc_ndcg_at_20_max
      value: -6.927364052923182
    - type: nauc_ndcg_at_20_std
      value: -4.168791551223215
    - type: nauc_ndcg_at_3_diff1
      value: 10.718998017465346
    - type: nauc_ndcg_at_3_max
      value: -7.968252808658605
    - type: nauc_ndcg_at_3_std
      value: -6.379316205846782
    - type: nauc_ndcg_at_5_diff1
      value: 11.132383943770357
    - type: nauc_ndcg_at_5_max
      value: -6.52591429832427
    - type: nauc_ndcg_at_5_std
      value: -5.216113688168761
    - type: nauc_precision_at_1000_diff1
      value: 16.1495781371987
    - type: nauc_precision_at_1000_max
      value: 39.995738985755196
    - type: nauc_precision_at_1000_std
      value: 50.855436172063065
    - type: nauc_precision_at_100_diff1
      value: 5.9156015470781265
    - type: nauc_precision_at_100_max
      value: 26.03608801637909
    - type: nauc_precision_at_100_std
      value: 54.70480941746274
    - type: nauc_precision_at_10_diff1
      value: 7.001835875439316
    - type: nauc_precision_at_10_max
      value: 2.135776035777977
    - type: nauc_precision_at_10_std
      value: 11.516009853432555
    - type: nauc_precision_at_1_diff1
      value: 15.505336965073605
    - type: nauc_precision_at_1_max
      value: -10.866105149439845
    - type: nauc_precision_at_1_std
      value: -9.694177220362505
    - type: nauc_precision_at_20_diff1
      value: 13.681914368809867
    - type: nauc_precision_at_20_max
      value: 9.479991446859016
    - type: nauc_precision_at_20_std
      value: 26.376943655091644
    - type: nauc_precision_at_3_diff1
      value: 7.325939191487269
    - type: nauc_precision_at_3_max
      value: -5.874501064035859
    - type: nauc_precision_at_3_std
      value: -4.340026468355782
    - type: nauc_precision_at_5_diff1
      value: 7.383019735342397
    - type: nauc_precision_at_5_max
      value: -0.5758672788087532
    - type: nauc_precision_at_5_std
      value: -0.3247880327348163
    - type: nauc_recall_at_1000_diff1
      value: 16.149578137193416
    - type: nauc_recall_at_1000_max
      value: 39.99573898574825
    - type: nauc_recall_at_1000_std
      value: 50.85543617205994
    - type: nauc_recall_at_100_diff1
      value: 5.915601547077784
    - type: nauc_recall_at_100_max
      value: 26.03608801637899
    - type: nauc_recall_at_100_std
      value: 54.704809417461085
    - type: nauc_recall_at_10_diff1
      value: 7.001835875439445
    - type: nauc_recall_at_10_max
      value: 2.1357760357780817
    - type: nauc_recall_at_10_std
      value: 11.516009853432491
    - type: nauc_recall_at_1_diff1
      value: 15.505336965073605
    - type: nauc_recall_at_1_max
      value: -10.866105149439845
    - type: nauc_recall_at_1_std
      value: -9.694177220362505
    - type: nauc_recall_at_20_diff1
      value: 13.681914368809581
    - type: nauc_recall_at_20_max
      value: 9.479991446859197
    - type: nauc_recall_at_20_std
      value: 26.37694365509119
    - type: nauc_recall_at_3_diff1
      value: 7.325939191487281
    - type: nauc_recall_at_3_max
      value: -5.874501064035827
    - type: nauc_recall_at_3_std
      value: -4.3400264683557825
    - type: nauc_recall_at_5_diff1
      value: 7.383019735342311
    - type: nauc_recall_at_5_max
      value: -0.575867278808783
    - type: nauc_recall_at_5_std
      value: -0.32478803273490514
    - type: ndcg_at_1
      value: 37.980000000000004
    - type: ndcg_at_10
      value: 61.587
    - type: ndcg_at_100
      value: 64.212
    - type: ndcg_at_1000
      value: 64.327
    - type: ndcg_at_20
      value: 63.365
    - type: ndcg_at_3
      value: 52.898999999999994
    - type: ndcg_at_5
      value: 57.62199999999999
    - type: precision_at_1
      value: 37.980000000000004
    - type: precision_at_10
      value: 8.748000000000001
    - type: precision_at_100
      value: 0.988
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.723
    - type: precision_at_3
      value: 21.29
    - type: precision_at_5
      value: 15.064
    - type: recall_at_1
      value: 37.980000000000004
    - type: recall_at_10
      value: 87.482
    - type: recall_at_100
      value: 98.791
    - type: recall_at_1000
      value: 99.644
    - type: recall_at_20
      value: 94.452
    - type: recall_at_3
      value: 63.869
    - type: recall_at_5
      value: 75.32
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ArxivClusteringP2P (default)
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
      split: test
      type: mteb/arxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 47.1311063882059
    - type: v_measure
      value: 47.1311063882059
    - type: v_measure_std
      value: 14.069209556131934
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB ArxivClusteringS2S (default)
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
      split: test
      type: mteb/arxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 39.590626960311226
    - type: v_measure
      value: 39.590626960311226
    - type: v_measure_std
      value: 14.382421237527772
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB AskUbuntuDupQuestions (default)
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
      split: test
      type: mteb/askubuntudupquestions-reranking
    metrics:
    - type: main_score
      value: 62.68563238263294
    - type: map
      value: 62.68563238263294
    - type: mrr
      value: 75.61359539198872
    - type: nAUC_map_diff1
      value: 12.262339818337102
    - type: nAUC_map_max
      value: 27.16961840255215
    - type: nAUC_map_std
      value: 18.41854439312187
    - type: nAUC_mrr_diff1
      value: 17.929775567867427
    - type: nAUC_mrr_max
      value: 37.4634718998761
    - type: nAUC_mrr_std
      value: 22.75208941087266
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB BIOSSES (default)
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
      split: test
      type: mteb/biosses-sts
    metrics:
    - type: cosine_pearson
      value: 86.81310198111923
    - type: cosine_spearman
      value: 87.203191803159
    - type: euclidean_pearson
      value: 85.99215953326265
    - type: euclidean_spearman
      value: 87.203191803159
    - type: main_score
      value: 87.203191803159
    - type: manhattan_pearson
      value: 85.9379635608278
    - type: manhattan_spearman
      value: 87.25861475275549
    - type: pearson
      value: 86.81310198111923
    - type: spearman
      value: 87.203191803159
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB Banking77Classification (default)
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
      split: test
      type: mteb/banking77
    metrics:
    - type: accuracy
      value: 81.012987012987
    - type: f1
      value: 80.07167813016267
    - type: f1_weighted
      value: 80.07167813016268
    - type: main_score
      value: 81.012987012987
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB BiorxivClusteringP2P (default)
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
      split: test
      type: mteb/biorxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 38.78797599586202
    - type: v_measure
      value: 38.78797599586202
    - type: v_measure_std
      value: 1.0363490868285057
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB BiorxivClusteringS2S (default)
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
      split: test
      type: mteb/biorxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 34.02215818630931
    - type: v_measure
      value: 34.02215818630931
    - type: v_measure_std
      value: 0.9696451651437041
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB CQADupstackAndroidRetrieval (default)
      revision: f46a197baaae43b4f621051089b82a364682dfeb
      split: test
      type: mteb/cqadupstack-android
    metrics:
    - type: main_score
      value: 46.627
    - type: map_at_1
      value: 28.217
    - type: map_at_10
      value: 39.892
    - type: map_at_100
      value: 41.449000000000005
    - type: map_at_1000
      value: 41.579
    - type: map_at_20
      value: 40.762
    - type: map_at_3
      value: 36.195
    - type: map_at_5
      value: 38.305
    - type: mrr_at_1
      value: 35.1931330472103
    - type: mrr_at_10
      value: 45.828451075232195
    - type: mrr_at_100
      value: 46.57230049635246
    - type: mrr_at_1000
      value: 46.61709253893551
    - type: mrr_at_20
      value: 46.28287282124363
    - type: mrr_at_3
      value: 42.51311397234143
    - type: mrr_at_5
      value: 44.67334287076773
    - type: nauc_map_at_1000_diff1
      value: 48.71767769457138
    - type: nauc_map_at_1000_max
      value: 39.35739368614963
    - type: nauc_map_at_1000_std
      value: -2.1704456217464028
    - type: nauc_map_at_100_diff1
      value: 48.72787371204226
    - type: nauc_map_at_100_max
      value: 39.37274775045581
    - type: nauc_map_at_100_std
      value: -2.127591114741793
    - type: nauc_map_at_10_diff1
      value: 48.81205052330434
    - type: nauc_map_at_10_max
      value: 38.69733357092054
    - type: nauc_map_at_10_std
      value: -2.9875060424451596
    - type: nauc_map_at_1_diff1
      value: 54.74897730317293
    - type: nauc_map_at_1_max
      value: 36.20815199595291
    - type: nauc_map_at_1_std
      value: -4.9834209135466745
    - type: nauc_map_at_20_diff1
      value: 48.755892872921784
    - type: nauc_map_at_20_max
      value: 39.07765061538151
    - type: nauc_map_at_20_std
      value: -2.3776308458840165
    - type: nauc_map_at_3_diff1
      value: 50.16967741469197
    - type: nauc_map_at_3_max
      value: 38.585635380693624
    - type: nauc_map_at_3_std
      value: -4.221176794198626
    - type: nauc_map_at_5_diff1
      value: 49.23913187338483
    - type: nauc_map_at_5_max
      value: 37.90581077128227
    - type: nauc_map_at_5_std
      value: -3.976982817403684
    - type: nauc_mrr_at_1000_diff1
      value: 47.302576554982565
    - type: nauc_mrr_at_1000_max
      value: 39.42247557331803
    - type: nauc_mrr_at_1000_std
      value: -5.093001257632933
    - type: nauc_mrr_at_100_diff1
      value: 47.28081174156696
    - type: nauc_mrr_at_100_max
      value: 39.41937462480708
    - type: nauc_mrr_at_100_std
      value: -5.09795439703923
    - type: nauc_mrr_at_10_diff1
      value: 47.113269125719164
    - type: nauc_mrr_at_10_max
      value: 39.368581425469856
    - type: nauc_mrr_at_10_std
      value: -5.277228133429229
    - type: nauc_mrr_at_1_diff1
      value: 51.5649652720488
    - type: nauc_mrr_at_1_max
      value: 38.28526532925652
    - type: nauc_mrr_at_1_std
      value: -7.500007125478944
    - type: nauc_mrr_at_20_diff1
      value: 47.264033020877825
    - type: nauc_mrr_at_20_max
      value: 39.378664517788145
    - type: nauc_mrr_at_20_std
      value: -5.074502402009077
    - type: nauc_mrr_at_3_diff1
      value: 48.280167889883735
    - type: nauc_mrr_at_3_max
      value: 40.08468002595438
    - type: nauc_mrr_at_3_std
      value: -5.587010540450647
    - type: nauc_mrr_at_5_diff1
      value: 47.075331054632024
    - type: nauc_mrr_at_5_max
      value: 38.66614809652955
    - type: nauc_mrr_at_5_std
      value: -5.580429126374889
    - type: nauc_ndcg_at_1000_diff1
      value: 46.87312381595359
    - type: nauc_ndcg_at_1000_max
      value: 40.85262017311222
    - type: nauc_ndcg_at_1000_std
      value: -0.30623579781240073
    - type: nauc_ndcg_at_100_diff1
      value: 46.235157795940054
    - type: nauc_ndcg_at_100_max
      value: 40.92612671162398
    - type: nauc_ndcg_at_100_std
      value: 0.13207070143061483
    - type: nauc_ndcg_at_10_diff1
      value: 46.105580841531044
    - type: nauc_ndcg_at_10_max
      value: 39.25806212859237
    - type: nauc_ndcg_at_10_std
      value: -2.0479578136863483
    - type: nauc_ndcg_at_1_diff1
      value: 51.5649652720488
    - type: nauc_ndcg_at_1_max
      value: 38.28526532925652
    - type: nauc_ndcg_at_1_std
      value: -7.500007125478944
    - type: nauc_ndcg_at_20_diff1
      value: 46.107622786903654
    - type: nauc_ndcg_at_20_max
      value: 39.6477616907479
    - type: nauc_ndcg_at_20_std
      value: -0.7893045729851432
    - type: nauc_ndcg_at_3_diff1
      value: 47.78517331152383
    - type: nauc_ndcg_at_3_max
      value: 39.57887271602766
    - type: nauc_ndcg_at_3_std
      value: -3.7158851363814507
    - type: nauc_ndcg_at_5_diff1
      value: 46.33678372159624
    - type: nauc_ndcg_at_5_max
      value: 37.70592482456646
    - type: nauc_ndcg_at_5_std
      value: -3.463868685785821
    - type: nauc_precision_at_1000_diff1
      value: -21.647335193360824
    - type: nauc_precision_at_1000_max
      value: -10.332791963863814
    - type: nauc_precision_at_1000_std
      value: -4.585384160420304
    - type: nauc_precision_at_100_diff1
      value: -11.243893402087695
    - type: nauc_precision_at_100_max
      value: 6.61622760941563
    - type: nauc_precision_at_100_std
      value: 8.31890658946228
    - type: nauc_precision_at_10_diff1
      value: 11.992735889770284
    - type: nauc_precision_at_10_max
      value: 26.368661979039032
    - type: nauc_precision_at_10_std
      value: 7.257193178137085
    - type: nauc_precision_at_1_diff1
      value: 51.5649652720488
    - type: nauc_precision_at_1_max
      value: 38.28526532925652
    - type: nauc_precision_at_1_std
      value: -7.500007125478944
    - type: nauc_precision_at_20_diff1
      value: 2.788039468977995
    - type: nauc_precision_at_20_max
      value: 19.61829689410151
    - type: nauc_precision_at_20_std
      value: 10.454426854909613
    - type: nauc_precision_at_3_diff1
      value: 32.170103339905374
    - type: nauc_precision_at_3_max
      value: 37.69989711862568
    - type: nauc_precision_at_3_std
      value: -1.2665563798590034
    - type: nauc_precision_at_5_diff1
      value: 21.90723648268845
    - type: nauc_precision_at_5_max
      value: 28.934461907153274
    - type: nauc_precision_at_5_std
      value: 1.496963451309664
    - type: nauc_recall_at_1000_diff1
      value: 39.845193615005165
    - type: nauc_recall_at_1000_max
      value: 67.53429995472943
    - type: nauc_recall_at_1000_std
      value: 54.25541191889182
    - type: nauc_recall_at_100_diff1
      value: 30.48595510867637
    - type: nauc_recall_at_100_max
      value: 45.56799906157419
    - type: nauc_recall_at_100_std
      value: 18.803518480822365
    - type: nauc_recall_at_10_diff1
      value: 37.39314315072326
    - type: nauc_recall_at_10_max
      value: 36.58964403796781
    - type: nauc_recall_at_10_std
      value: 1.4221578063034934
    - type: nauc_recall_at_1_diff1
      value: 54.74897730317293
    - type: nauc_recall_at_1_max
      value: 36.20815199595291
    - type: nauc_recall_at_1_std
      value: -4.9834209135466745
    - type: nauc_recall_at_20_diff1
      value: 34.78809945590171
    - type: nauc_recall_at_20_max
      value: 36.24306666062695
    - type: nauc_recall_at_20_std
      value: 6.691638038251415
    - type: nauc_recall_at_3_diff1
      value: 45.15894238510486
    - type: nauc_recall_at_3_max
      value: 38.42252145730142
    - type: nauc_recall_at_3_std
      value: -3.1703672077384977
    - type: nauc_recall_at_5_diff1
      value: 39.99639508242837
    - type: nauc_recall_at_5_max
      value: 33.63188962949065
    - type: nauc_recall_at_5_std
      value: -2.463748471656163
    - type: ndcg_at_1
      value: 35.193000000000005
    - type: ndcg_at_10
      value: 46.627
    - type: ndcg_at_100
      value: 52.259
    - type: ndcg_at_1000
      value: 54.18300000000001
    - type: ndcg_at_20
      value: 48.869
    - type: ndcg_at_3
      value: 40.802
    - type: ndcg_at_5
      value: 43.826
    - type: precision_at_1
      value: 35.193000000000005
    - type: precision_at_10
      value: 9.084
    - type: precision_at_100
      value: 1.506
    - type: precision_at_1000
      value: 0.201
    - type: precision_at_20
      value: 5.515
    - type: precision_at_3
      value: 19.552
    - type: precision_at_5
      value: 14.707
    - type: recall_at_1
      value: 28.217
    - type: recall_at_10
      value: 60.148999999999994
    - type: recall_at_100
      value: 83.509
    - type: recall_at_1000
      value: 95.623
    - type: recall_at_20
      value: 67.87100000000001
    - type: recall_at_3
      value: 43.913999999999994
    - type: recall_at_5
      value: 51.626000000000005
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackEnglishRetrieval (default)
      revision: ad9991cb51e31e31e430383c75ffb2885547b5f0
      split: test
      type: mteb/cqadupstack-english
    metrics:
    - type: main_score
      value: 43.26
    - type: map_at_1
      value: 28.537000000000003
    - type: map_at_10
      value: 37.814
    - type: map_at_100
      value: 39.016
    - type: map_at_1000
      value: 39.141
    - type: map_at_20
      value: 38.438
    - type: map_at_3
      value: 35.119
    - type: map_at_5
      value: 36.635
    - type: mrr_at_1
      value: 35.6687898089172
    - type: mrr_at_10
      value: 43.89740673339401
    - type: mrr_at_100
      value: 44.595541925858406
    - type: mrr_at_1000
      value: 44.64146530556938
    - type: mrr_at_20
      value: 44.322503369933926
    - type: mrr_at_3
      value: 41.64543524416137
    - type: mrr_at_5
      value: 43.00212314225054
    - type: nauc_map_at_1000_diff1
      value: 50.38242920034188
    - type: nauc_map_at_1000_max
      value: 31.60097027148917
    - type: nauc_map_at_1000_std
      value: 0.9103551393313613
    - type: nauc_map_at_100_diff1
      value: 50.445666478760366
    - type: nauc_map_at_100_max
      value: 31.517660912977508
    - type: nauc_map_at_100_std
      value: 0.7775484115197918
    - type: nauc_map_at_10_diff1
      value: 50.661812695077316
    - type: nauc_map_at_10_max
      value: 30.609498777441285
    - type: nauc_map_at_10_std
      value: -0.6888710687447454
    - type: nauc_map_at_1_diff1
      value: 55.984295592830215
    - type: nauc_map_at_1_max
      value: 27.359981225642287
    - type: nauc_map_at_1_std
      value: -4.6372027497722925
    - type: nauc_map_at_20_diff1
      value: 50.6210701540613
    - type: nauc_map_at_20_max
      value: 30.97814546421626
    - type: nauc_map_at_20_std
      value: -0.00853770688951084
    - type: nauc_map_at_3_diff1
      value: 52.02665194423681
    - type: nauc_map_at_3_max
      value: 29.185613677490394
    - type: nauc_map_at_3_std
      value: -1.9976659466126225
    - type: nauc_map_at_5_diff1
      value: 51.19674489416761
    - type: nauc_map_at_5_max
      value: 30.160612226786988
    - type: nauc_map_at_5_std
      value: -1.3713739278786357
    - type: nauc_mrr_at_1000_diff1
      value: 48.263786175116394
    - type: nauc_mrr_at_1000_max
      value: 33.528582446000335
    - type: nauc_mrr_at_1000_std
      value: 3.997090643336205
    - type: nauc_mrr_at_100_diff1
      value: 48.261549498353794
    - type: nauc_mrr_at_100_max
      value: 33.53481236606367
    - type: nauc_mrr_at_100_std
      value: 3.999833501681202
    - type: nauc_mrr_at_10_diff1
      value: 48.15519091869044
    - type: nauc_mrr_at_10_max
      value: 33.45559294700087
    - type: nauc_mrr_at_10_std
      value: 3.63480527599511
    - type: nauc_mrr_at_1_diff1
      value: 53.101823173896314
    - type: nauc_mrr_at_1_max
      value: 33.32155831980044
    - type: nauc_mrr_at_1_std
      value: 1.7548676566607069
    - type: nauc_mrr_at_20_diff1
      value: 48.228190697254696
    - type: nauc_mrr_at_20_max
      value: 33.45847789439114
    - type: nauc_mrr_at_20_std
      value: 3.8424882676403405
    - type: nauc_mrr_at_3_diff1
      value: 48.962748652767296
    - type: nauc_mrr_at_3_max
      value: 33.110931453654366
    - type: nauc_mrr_at_3_std
      value: 3.2626108133115785
    - type: nauc_mrr_at_5_diff1
      value: 48.41529159773174
    - type: nauc_mrr_at_5_max
      value: 33.57404651404654
    - type: nauc_mrr_at_5_std
      value: 3.40495779898185
    - type: nauc_ndcg_at_1000_diff1
      value: 47.48984825963725
    - type: nauc_ndcg_at_1000_max
      value: 33.54130065771048
    - type: nauc_ndcg_at_1000_std
      value: 6.121693672230708
    - type: nauc_ndcg_at_100_diff1
      value: 47.548547556497454
    - type: nauc_ndcg_at_100_max
      value: 33.472952805068815
    - type: nauc_ndcg_at_100_std
      value: 5.781276334687519
    - type: nauc_ndcg_at_10_diff1
      value: 47.615354334764966
    - type: nauc_ndcg_at_10_max
      value: 32.18027911162887
    - type: nauc_ndcg_at_10_std
      value: 2.1717663696202183
    - type: nauc_ndcg_at_1_diff1
      value: 53.101823173896314
    - type: nauc_ndcg_at_1_max
      value: 33.32155831980044
    - type: nauc_ndcg_at_1_std
      value: 1.7548676566607069
    - type: nauc_ndcg_at_20_diff1
      value: 47.730317212864094
    - type: nauc_ndcg_at_20_max
      value: 32.245697290265426
    - type: nauc_ndcg_at_20_std
      value: 3.438922453415761
    - type: nauc_ndcg_at_3_diff1
      value: 49.02930101842743
    - type: nauc_ndcg_at_3_max
      value: 31.360355684228725
    - type: nauc_ndcg_at_3_std
      value: 1.6443840772752165
    - type: nauc_ndcg_at_5_diff1
      value: 48.224855926716394
    - type: nauc_ndcg_at_5_max
      value: 32.31325115635817
    - type: nauc_ndcg_at_5_std
      value: 1.730840438831435
    - type: nauc_precision_at_1000_diff1
      value: -18.403594567458207
    - type: nauc_precision_at_1000_max
      value: 21.49485514696995
    - type: nauc_precision_at_1000_std
      value: 31.712375598122332
    - type: nauc_precision_at_100_diff1
      value: -8.793614199073078
    - type: nauc_precision_at_100_max
      value: 30.913124236942203
    - type: nauc_precision_at_100_std
      value: 36.20921952482491
    - type: nauc_precision_at_10_diff1
      value: 13.321069551389805
    - type: nauc_precision_at_10_max
      value: 34.64171103330222
    - type: nauc_precision_at_10_std
      value: 21.814571428436768
    - type: nauc_precision_at_1_diff1
      value: 53.101823173896314
    - type: nauc_precision_at_1_max
      value: 33.32155831980044
    - type: nauc_precision_at_1_std
      value: 1.7548676566607069
    - type: nauc_precision_at_20_diff1
      value: 5.887493649538546
    - type: nauc_precision_at_20_max
      value: 33.9325045896976
    - type: nauc_precision_at_20_std
      value: 28.652312941049168
    - type: nauc_precision_at_3_diff1
      value: 31.511315134064876
    - type: nauc_precision_at_3_max
      value: 32.88348773453123
    - type: nauc_precision_at_3_std
      value: 10.46641443327759
    - type: nauc_precision_at_5_diff1
      value: 22.887506091181294
    - type: nauc_precision_at_5_max
      value: 35.416697921302806
    - type: nauc_precision_at_5_std
      value: 15.33616375317894
    - type: nauc_recall_at_1000_diff1
      value: 34.10586124707363
    - type: nauc_recall_at_1000_max
      value: 34.54304855921719
    - type: nauc_recall_at_1000_std
      value: 34.65621165539369
    - type: nauc_recall_at_100_diff1
      value: 36.022255136157874
    - type: nauc_recall_at_100_max
      value: 34.64999485306686
    - type: nauc_recall_at_100_std
      value: 22.671221118089825
    - type: nauc_recall_at_10_diff1
      value: 40.33647072966317
    - type: nauc_recall_at_10_max
      value: 28.705618140836826
    - type: nauc_recall_at_10_std
      value: 1.920768225117285
    - type: nauc_recall_at_1_diff1
      value: 55.984295592830215
    - type: nauc_recall_at_1_max
      value: 27.359981225642287
    - type: nauc_recall_at_1_std
      value: -4.6372027497722925
    - type: nauc_recall_at_20_diff1
      value: 39.05498416729996
    - type: nauc_recall_at_20_max
      value: 28.449080252085896
    - type: nauc_recall_at_20_std
      value: 7.336167777371156
    - type: nauc_recall_at_3_diff1
      value: 47.03085830864628
    - type: nauc_recall_at_3_max
      value: 27.45027142421863
    - type: nauc_recall_at_3_std
      value: -0.5843560184900182
    - type: nauc_recall_at_5_diff1
      value: 43.534508407363404
    - type: nauc_recall_at_5_max
      value: 28.823615210124515
    - type: nauc_recall_at_5_std
      value: 0.30711982604670324
    - type: ndcg_at_1
      value: 35.669000000000004
    - type: ndcg_at_10
      value: 43.26
    - type: ndcg_at_100
      value: 47.73
    - type: ndcg_at_1000
      value: 49.888
    - type: ndcg_at_20
      value: 44.931
    - type: ndcg_at_3
      value: 39.285
    - type: ndcg_at_5
      value: 41.185
    - type: precision_at_1
      value: 35.669000000000004
    - type: precision_at_10
      value: 8.108
    - type: precision_at_100
      value: 1.3299999999999998
    - type: precision_at_1000
      value: 0.181
    - type: precision_at_20
      value: 4.79
    - type: precision_at_3
      value: 18.875
    - type: precision_at_5
      value: 13.338
    - type: recall_at_1
      value: 28.537000000000003
    - type: recall_at_10
      value: 52.528
    - type: recall_at_100
      value: 71.544
    - type: recall_at_1000
      value: 85.52300000000001
    - type: recall_at_20
      value: 58.665
    - type: recall_at_3
      value: 40.682
    - type: recall_at_5
      value: 46.102
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGamingRetrieval (default)
      revision: 4885aa143210c98657558c04aaf3dc47cfb54340
      split: test
      type: mteb/cqadupstack-gaming
    metrics:
    - type: main_score
      value: 55.482
    - type: map_at_1
      value: 37.155
    - type: map_at_10
      value: 49.467
    - type: map_at_100
      value: 50.597
    - type: map_at_1000
      value: 50.64999999999999
    - type: map_at_20
      value: 50.153000000000006
    - type: map_at_3
      value: 46.153
    - type: map_at_5
      value: 48.167
    - type: mrr_at_1
      value: 42.69592476489028
    - type: mrr_at_10
      value: 52.934890779718444
    - type: mrr_at_100
      value: 53.675559437654385
    - type: mrr_at_1000
      value: 53.700718829078795
    - type: mrr_at_20
      value: 53.38668059647668
    - type: mrr_at_3
      value: 50.428422152560145
    - type: mrr_at_5
      value: 51.95193312434701
    - type: nauc_map_at_1000_diff1
      value: 45.39853735301247
    - type: nauc_map_at_1000_max
      value: 35.88207570837637
    - type: nauc_map_at_1000_std
      value: -4.29738026780591
    - type: nauc_map_at_100_diff1
      value: 45.387618392967234
    - type: nauc_map_at_100_max
      value: 35.86260554726276
    - type: nauc_map_at_100_std
      value: -4.294613837825713
    - type: nauc_map_at_10_diff1
      value: 45.50417160033363
    - type: nauc_map_at_10_max
      value: 35.35533906436545
    - type: nauc_map_at_10_std
      value: -5.041866425981859
    - type: nauc_map_at_1_diff1
      value: 48.49418411014949
    - type: nauc_map_at_1_max
      value: 30.467103950355046
    - type: nauc_map_at_1_std
      value: -6.7511953844717585
    - type: nauc_map_at_20_diff1
      value: 45.40183877110559
    - type: nauc_map_at_20_max
      value: 35.67488678826502
    - type: nauc_map_at_20_std
      value: -4.542033283197055
    - type: nauc_map_at_3_diff1
      value: 45.828558019478685
    - type: nauc_map_at_3_max
      value: 33.811993497438046
    - type: nauc_map_at_3_std
      value: -7.022097202852565
    - type: nauc_map_at_5_diff1
      value: 45.55644758512818
    - type: nauc_map_at_5_max
      value: 34.539038617747174
    - type: nauc_map_at_5_std
      value: -6.108792115020993
    - type: nauc_mrr_at_1000_diff1
      value: 44.87714381142493
    - type: nauc_mrr_at_1000_max
      value: 37.33976418014246
    - type: nauc_mrr_at_1000_std
      value: -3.300901653609806
    - type: nauc_mrr_at_100_diff1
      value: 44.87248633704184
    - type: nauc_mrr_at_100_max
      value: 37.34859192418237
    - type: nauc_mrr_at_100_std
      value: -3.2870314069697337
    - type: nauc_mrr_at_10_diff1
      value: 44.69076109213016
    - type: nauc_mrr_at_10_max
      value: 37.30123464532984
    - type: nauc_mrr_at_10_std
      value: -3.325752153037405
    - type: nauc_mrr_at_1_diff1
      value: 48.19163276678239
    - type: nauc_mrr_at_1_max
      value: 34.61847854145463
    - type: nauc_mrr_at_1_std
      value: -5.370501121412354
    - type: nauc_mrr_at_20_diff1
      value: 44.840939385551216
    - type: nauc_mrr_at_20_max
      value: 37.384435797609505
    - type: nauc_mrr_at_20_std
      value: -3.2559923415768326
    - type: nauc_mrr_at_3_diff1
      value: 44.956318047816296
    - type: nauc_mrr_at_3_max
      value: 36.88636261611909
    - type: nauc_mrr_at_3_std
      value: -4.271260442740253
    - type: nauc_mrr_at_5_diff1
      value: 44.6576132493844
    - type: nauc_mrr_at_5_max
      value: 37.067740181380366
    - type: nauc_mrr_at_5_std
      value: -3.968886060963421
    - type: nauc_ndcg_at_1000_diff1
      value: 44.37434646459078
    - type: nauc_ndcg_at_1000_max
      value: 38.215572514193994
    - type: nauc_ndcg_at_1000_std
      value: -1.3042381057500214
    - type: nauc_ndcg_at_100_diff1
      value: 44.290728955986516
    - type: nauc_ndcg_at_100_max
      value: 38.3958306354721
    - type: nauc_ndcg_at_100_std
      value: -0.8730872184515021
    - type: nauc_ndcg_at_10_diff1
      value: 44.119091219198104
    - type: nauc_ndcg_at_10_max
      value: 37.70013992720767
    - type: nauc_ndcg_at_10_std
      value: -2.439834460321177
    - type: nauc_ndcg_at_1_diff1
      value: 48.19163276678239
    - type: nauc_ndcg_at_1_max
      value: 34.61847854145463
    - type: nauc_ndcg_at_1_std
      value: -5.370501121412354
    - type: nauc_ndcg_at_20_diff1
      value: 44.22301071777352
    - type: nauc_ndcg_at_20_max
      value: 38.13294450352038
    - type: nauc_ndcg_at_20_std
      value: -1.5320041255829162
    - type: nauc_ndcg_at_3_diff1
      value: 44.18839086666503
    - type: nauc_ndcg_at_3_max
      value: 35.530975247059544
    - type: nauc_ndcg_at_3_std
      value: -5.574269526409219
    - type: nauc_ndcg_at_5_diff1
      value: 43.968238482098926
    - type: nauc_ndcg_at_5_max
      value: 36.41757888561071
    - type: nauc_ndcg_at_5_std
      value: -4.532795858948274
    - type: nauc_precision_at_1000_diff1
      value: -9.234774982708476
    - type: nauc_precision_at_1000_max
      value: 22.127614179936824
    - type: nauc_precision_at_1000_std
      value: 22.646193222930773
    - type: nauc_precision_at_100_diff1
      value: -5.234665765188833
    - type: nauc_precision_at_100_max
      value: 27.271500842942746
    - type: nauc_precision_at_100_std
      value: 26.184067367482474
    - type: nauc_precision_at_10_diff1
      value: 13.037817071774949
    - type: nauc_precision_at_10_max
      value: 33.66318780774645
    - type: nauc_precision_at_10_std
      value: 13.312767253904342
    - type: nauc_precision_at_1_diff1
      value: 48.19163276678239
    - type: nauc_precision_at_1_max
      value: 34.61847854145463
    - type: nauc_precision_at_1_std
      value: -5.370501121412354
    - type: nauc_precision_at_20_diff1
      value: 5.741386063339354
    - type: nauc_precision_at_20_max
      value: 32.48331924084784
    - type: nauc_precision_at_20_std
      value: 20.06250876070363
    - type: nauc_precision_at_3_diff1
      value: 28.609002718352333
    - type: nauc_precision_at_3_max
      value: 34.6795736576386
    - type: nauc_precision_at_3_std
      value: -0.04417621858530164
    - type: nauc_precision_at_5_diff1
      value: 20.976308196400424
    - type: nauc_precision_at_5_max
      value: 33.3948604565235
    - type: nauc_precision_at_5_std
      value: 5.149959751504062
    - type: nauc_recall_at_1000_diff1
      value: 28.383977077680207
    - type: nauc_recall_at_1000_max
      value: 57.70769869998163
    - type: nauc_recall_at_1000_std
      value: 46.997952366562174
    - type: nauc_recall_at_100_diff1
      value: 35.63735101494906
    - type: nauc_recall_at_100_max
      value: 49.70285511610692
    - type: nauc_recall_at_100_std
      value: 25.56344297714899
    - type: nauc_recall_at_10_diff1
      value: 38.705113308372354
    - type: nauc_recall_at_10_max
      value: 40.20557937184269
    - type: nauc_recall_at_10_std
      value: 4.171468175806741
    - type: nauc_recall_at_1_diff1
      value: 48.49418411014949
    - type: nauc_recall_at_1_max
      value: 30.467103950355046
    - type: nauc_recall_at_1_std
      value: -6.7511953844717585
    - type: nauc_recall_at_20_diff1
      value: 38.48920202661439
    - type: nauc_recall_at_20_max
      value: 43.57168759518817
    - type: nauc_recall_at_20_std
      value: 10.269085411405069
    - type: nauc_recall_at_3_diff1
      value: 41.086532491390585
    - type: nauc_recall_at_3_max
      value: 34.81725796602349
    - type: nauc_recall_at_3_std
      value: -6.673864007702387
    - type: nauc_recall_at_5_diff1
      value: 39.1176927288211
    - type: nauc_recall_at_5_max
      value: 36.18158874606236
    - type: nauc_recall_at_5_std
      value: -3.4373454531511647
    - type: ndcg_at_1
      value: 42.696
    - type: ndcg_at_10
      value: 55.482
    - type: ndcg_at_100
      value: 59.927
    - type: ndcg_at_1000
      value: 60.919999999999995
    - type: ndcg_at_20
      value: 57.416999999999994
    - type: ndcg_at_3
      value: 49.888
    - type: ndcg_at_5
      value: 52.833
    - type: precision_at_1
      value: 42.696
    - type: precision_at_10
      value: 9.078
    - type: precision_at_100
      value: 1.218
    - type: precision_at_1000
      value: 0.135
    - type: precision_at_20
      value: 5.113
    - type: precision_at_3
      value: 22.445
    - type: precision_at_5
      value: 15.661
    - type: recall_at_1
      value: 37.155
    - type: recall_at_10
      value: 69.792
    - type: recall_at_100
      value: 89.035
    - type: recall_at_1000
      value: 95.943
    - type: recall_at_20
      value: 76.89099999999999
    - type: recall_at_3
      value: 54.969
    - type: recall_at_5
      value: 62.114000000000004
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackGisRetrieval (default)
      revision: 5003b3064772da1887988e05400cf3806fe491f2
      split: test
      type: mteb/cqadupstack-gis
    metrics:
    - type: main_score
      value: 37.686
    - type: map_at_1
      value: 24.194
    - type: map_at_10
      value: 32.706
    - type: map_at_100
      value: 33.696
    - type: map_at_1000
      value: 33.768
    - type: map_at_20
      value: 33.25
    - type: map_at_3
      value: 29.970000000000002
    - type: map_at_5
      value: 31.578
    - type: mrr_at_1
      value: 26.327683615819208
    - type: mrr_at_10
      value: 34.80033180880639
    - type: mrr_at_100
      value: 35.68493088802286
    - type: mrr_at_1000
      value: 35.73890763688848
    - type: mrr_at_20
      value: 35.284647683976026
    - type: mrr_at_3
      value: 32.20338983050847
    - type: mrr_at_5
      value: 33.689265536723155
    - type: nauc_map_at_1000_diff1
      value: 39.0058007993193
    - type: nauc_map_at_1000_max
      value: 31.9664848424503
    - type: nauc_map_at_1000_std
      value: 0.69708864063753
    - type: nauc_map_at_100_diff1
      value: 38.99740699853551
    - type: nauc_map_at_100_max
      value: 31.950173674106637
    - type: nauc_map_at_100_std
      value: 0.6831416203961035
    - type: nauc_map_at_10_diff1
      value: 39.16403477206109
    - type: nauc_map_at_10_max
      value: 31.801992594297484
    - type: nauc_map_at_10_std
      value: 0.08487527963355261
    - type: nauc_map_at_1_diff1
      value: 47.129030830065
    - type: nauc_map_at_1_max
      value: 30.9543809605351
    - type: nauc_map_at_1_std
      value: -2.616386042411576
    - type: nauc_map_at_20_diff1
      value: 39.016119588237004
    - type: nauc_map_at_20_max
      value: 31.966103550512486
    - type: nauc_map_at_20_std
      value: 0.5993010385451379
    - type: nauc_map_at_3_diff1
      value: 39.960423401096016
    - type: nauc_map_at_3_max
      value: 31.126852260003602
    - type: nauc_map_at_3_std
      value: -1.2432186078894505
    - type: nauc_map_at_5_diff1
      value: 39.350942260116916
    - type: nauc_map_at_5_max
      value: 31.477494706451516
    - type: nauc_map_at_5_std
      value: -0.332327514629881
    - type: nauc_mrr_at_1000_diff1
      value: 37.56861228659833
    - type: nauc_mrr_at_1000_max
      value: 32.77701183545048
    - type: nauc_mrr_at_1000_std
      value: 1.8573601025377928
    - type: nauc_mrr_at_100_diff1
      value: 37.56084842599138
    - type: nauc_mrr_at_100_max
      value: 32.77474646470676
    - type: nauc_mrr_at_100_std
      value: 1.8661824660967452
    - type: nauc_mrr_at_10_diff1
      value: 37.651655650043615
    - type: nauc_mrr_at_10_max
      value: 32.82210713728638
    - type: nauc_mrr_at_10_std
      value: 1.5178658325578909
    - type: nauc_mrr_at_1_diff1
      value: 44.932276757115815
    - type: nauc_mrr_at_1_max
      value: 32.66068226327021
    - type: nauc_mrr_at_1_std
      value: -0.9313870351409079
    - type: nauc_mrr_at_20_diff1
      value: 37.540979386031864
    - type: nauc_mrr_at_20_max
      value: 32.81440742182942
    - type: nauc_mrr_at_20_std
      value: 1.826591047299842
    - type: nauc_mrr_at_3_diff1
      value: 38.269772827885966
    - type: nauc_mrr_at_3_max
      value: 32.10537876507981
    - type: nauc_mrr_at_3_std
      value: 0.3024566400660873
    - type: nauc_mrr_at_5_diff1
      value: 37.84033535304918
    - type: nauc_mrr_at_5_max
      value: 32.452393894273584
    - type: nauc_mrr_at_5_std
      value: 1.0029016560532624
    - type: nauc_ndcg_at_1000_diff1
      value: 35.81763575917382
    - type: nauc_ndcg_at_1000_max
      value: 32.769876372777794
    - type: nauc_ndcg_at_1000_std
      value: 4.257684081453828
    - type: nauc_ndcg_at_100_diff1
      value: 35.62486527543234
    - type: nauc_ndcg_at_100_max
      value: 32.6865313439193
    - type: nauc_ndcg_at_100_std
      value: 4.493848690808405
    - type: nauc_ndcg_at_10_diff1
      value: 36.264350852558444
    - type: nauc_ndcg_at_10_max
      value: 32.46258658377739
    - type: nauc_ndcg_at_10_std
      value: 2.1785378510762112
    - type: nauc_ndcg_at_1_diff1
      value: 44.932276757115815
    - type: nauc_ndcg_at_1_max
      value: 32.66068226327021
    - type: nauc_ndcg_at_1_std
      value: -0.9313870351409079
    - type: nauc_ndcg_at_20_diff1
      value: 35.722983189942596
    - type: nauc_ndcg_at_20_max
      value: 32.877377599742964
    - type: nauc_ndcg_at_20_std
      value: 3.790875849871362
    - type: nauc_ndcg_at_3_diff1
      value: 37.63400271423685
    - type: nauc_ndcg_at_3_max
      value: 31.2739081815396
    - type: nauc_ndcg_at_3_std
      value: -0.29839390734625465
    - type: nauc_ndcg_at_5_diff1
      value: 36.62082003320047
    - type: nauc_ndcg_at_5_max
      value: 31.65589810609168
    - type: nauc_ndcg_at_5_std
      value: 1.216992770007969
    - type: nauc_precision_at_1000_diff1
      value: -5.24340167738406
    - type: nauc_precision_at_1000_max
      value: 15.455427903541539
    - type: nauc_precision_at_1000_std
      value: 16.49503077501681
    - type: nauc_precision_at_100_diff1
      value: 7.313598783241113
    - type: nauc_precision_at_100_max
      value: 27.10636757798661
    - type: nauc_precision_at_100_std
      value: 20.187644679960428
    - type: nauc_precision_at_10_diff1
      value: 22.200310338575214
    - type: nauc_precision_at_10_max
      value: 34.92118636200516
    - type: nauc_precision_at_10_std
      value: 10.234848073059426
    - type: nauc_precision_at_1_diff1
      value: 44.932276757115815
    - type: nauc_precision_at_1_max
      value: 32.66068226327021
    - type: nauc_precision_at_1_std
      value: -0.9313870351409079
    - type: nauc_precision_at_20_diff1
      value: 17.8901438402456
    - type: nauc_precision_at_20_max
      value: 34.65374091414346
    - type: nauc_precision_at_20_std
      value: 15.973547940494178
    - type: nauc_precision_at_3_diff1
      value: 29.04687567805014
    - type: nauc_precision_at_3_max
      value: 32.75971500796976
    - type: nauc_precision_at_3_std
      value: 2.9305507946156957
    - type: nauc_precision_at_5_diff1
      value: 24.888863498098704
    - type: nauc_precision_at_5_max
      value: 32.5731555578299
    - type: nauc_precision_at_5_std
      value: 6.791337976386832
    - type: nauc_recall_at_1000_diff1
      value: 8.037993412142983
    - type: nauc_recall_at_1000_max
      value: 33.615275538881626
    - type: nauc_recall_at_1000_std
      value: 37.22256855147328
    - type: nauc_recall_at_100_diff1
      value: 20.2507317736947
    - type: nauc_recall_at_100_max
      value: 31.661424125840178
    - type: nauc_recall_at_100_std
      value: 22.041159712662882
    - type: nauc_recall_at_10_diff1
      value: 28.048775208583177
    - type: nauc_recall_at_10_max
      value: 31.969139370292087
    - type: nauc_recall_at_10_std
      value: 6.644084230971351
    - type: nauc_recall_at_1_diff1
      value: 47.129030830065
    - type: nauc_recall_at_1_max
      value: 30.9543809605351
    - type: nauc_recall_at_1_std
      value: -2.616386042411576
    - type: nauc_recall_at_20_diff1
      value: 25.172877062002037
    - type: nauc_recall_at_20_max
      value: 33.432560257671156
    - type: nauc_recall_at_20_std
      value: 13.179799770289216
    - type: nauc_recall_at_3_diff1
      value: 32.76056599359956
    - type: nauc_recall_at_3_max
      value: 30.12736405148995
    - type: nauc_recall_at_3_std
      value: 1.1248390066659661
    - type: nauc_recall_at_5_diff1
      value: 29.375771822035233
    - type: nauc_recall_at_5_max
      value: 30.221436803204387
    - type: nauc_recall_at_5_std
      value: 4.140063667676888
    - type: ndcg_at_1
      value: 26.328000000000003
    - type: ndcg_at_10
      value: 37.686
    - type: ndcg_at_100
      value: 42.829
    - type: ndcg_at_1000
      value: 44.793
    - type: ndcg_at_20
      value: 39.646
    - type: ndcg_at_3
      value: 32.374
    - type: ndcg_at_5
      value: 35.08
    - type: precision_at_1
      value: 26.328000000000003
    - type: precision_at_10
      value: 5.853
    - type: precision_at_100
      value: 0.89
    - type: precision_at_1000
      value: 0.11
    - type: precision_at_20
      value: 3.39
    - type: precision_at_3
      value: 13.71
    - type: precision_at_5
      value: 9.853000000000002
    - type: recall_at_1
      value: 24.194
    - type: recall_at_10
      value: 51.11599999999999
    - type: recall_at_100
      value: 75.228
    - type: recall_at_1000
      value: 90.206
    - type: recall_at_20
      value: 58.684999999999995
    - type: recall_at_3
      value: 36.839
    - type: recall_at_5
      value: 43.275999999999996
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackMathematicaRetrieval (default)
      revision: 90fceea13679c63fe563ded68f3b6f06e50061de
      split: test
      type: mteb/cqadupstack-mathematica
    metrics:
    - type: main_score
      value: 29.403000000000002
    - type: map_at_1
      value: 15.797
    - type: map_at_10
      value: 24.122
    - type: map_at_100
      value: 25.334
    - type: map_at_1000
      value: 25.444
    - type: map_at_20
      value: 24.783
    - type: map_at_3
      value: 21.718
    - type: map_at_5
      value: 23.104
    - type: mrr_at_1
      value: 19.154228855721392
    - type: mrr_at_10
      value: 28.551192450446177
    - type: mrr_at_100
      value: 29.498082834170386
    - type: mrr_at_1000
      value: 29.56293339499485
    - type: mrr_at_20
      value: 29.085609803416858
    - type: mrr_at_3
      value: 26.01575456053069
    - type: mrr_at_5
      value: 27.589137645107797
    - type: nauc_map_at_1000_diff1
      value: 27.36221687250577
    - type: nauc_map_at_1000_max
      value: 18.089424170411217
    - type: nauc_map_at_1000_std
      value: 0.5188935207421588
    - type: nauc_map_at_100_diff1
      value: 27.34379428055101
    - type: nauc_map_at_100_max
      value: 18.06293708742179
    - type: nauc_map_at_100_std
      value: 0.5190525693808369
    - type: nauc_map_at_10_diff1
      value: 27.308055008582066
    - type: nauc_map_at_10_max
      value: 17.726725077602694
    - type: nauc_map_at_10_std
      value: -0.21344892091498174
    - type: nauc_map_at_1_diff1
      value: 34.60126559188873
    - type: nauc_map_at_1_max
      value: 19.748244491317678
    - type: nauc_map_at_1_std
      value: -3.2201287026916625
    - type: nauc_map_at_20_diff1
      value: 27.226319415474943
    - type: nauc_map_at_20_max
      value: 17.956515675249072
    - type: nauc_map_at_20_std
      value: 0.4472031548873323
    - type: nauc_map_at_3_diff1
      value: 27.95165713417068
    - type: nauc_map_at_3_max
      value: 17.072686143179975
    - type: nauc_map_at_3_std
      value: -0.7411970021732948
    - type: nauc_map_at_5_diff1
      value: 27.593386851196893
    - type: nauc_map_at_5_max
      value: 17.45702849396662
    - type: nauc_map_at_5_std
      value: -0.8286937920403831
    - type: nauc_mrr_at_1000_diff1
      value: 28.74831279311148
    - type: nauc_mrr_at_1000_max
      value: 20.17411091929109
    - type: nauc_mrr_at_1000_std
      value: -0.0652738752409115
    - type: nauc_mrr_at_100_diff1
      value: 28.747440393282336
    - type: nauc_mrr_at_100_max
      value: 20.185108068951408
    - type: nauc_mrr_at_100_std
      value: -0.05333343570132689
    - type: nauc_mrr_at_10_diff1
      value: 28.744815155313024
    - type: nauc_mrr_at_10_max
      value: 20.04684911692695
    - type: nauc_mrr_at_10_std
      value: -0.4264784901487863
    - type: nauc_mrr_at_1_diff1
      value: 37.2441962865539
    - type: nauc_mrr_at_1_max
      value: 22.534613943885276
    - type: nauc_mrr_at_1_std
      value: -2.479501845567973
    - type: nauc_mrr_at_20_diff1
      value: 28.63646797885947
    - type: nauc_mrr_at_20_max
      value: 20.130624923076574
    - type: nauc_mrr_at_20_std
      value: -0.05655707131769798
    - type: nauc_mrr_at_3_diff1
      value: 29.3420984302583
    - type: nauc_mrr_at_3_max
      value: 19.791159534927232
    - type: nauc_mrr_at_3_std
      value: -0.98317898053703
    - type: nauc_mrr_at_5_diff1
      value: 29.057555082772467
    - type: nauc_mrr_at_5_max
      value: 20.093774401866142
    - type: nauc_mrr_at_5_std
      value: -0.9877016856465175
    - type: nauc_ndcg_at_1000_diff1
      value: 25.77793793755624
    - type: nauc_ndcg_at_1000_max
      value: 19.071095093248687
    - type: nauc_ndcg_at_1000_std
      value: 3.0917142331029663
    - type: nauc_ndcg_at_100_diff1
      value: 25.64757683875679
    - type: nauc_ndcg_at_100_max
      value: 18.775229437095444
    - type: nauc_ndcg_at_100_std
      value: 3.4174861916019523
    - type: nauc_ndcg_at_10_diff1
      value: 25.1442487582001
    - type: nauc_ndcg_at_10_max
      value: 17.838371789800192
    - type: nauc_ndcg_at_10_std
      value: 1.0998312769822474
    - type: nauc_ndcg_at_1_diff1
      value: 37.2441962865539
    - type: nauc_ndcg_at_1_max
      value: 22.534613943885276
    - type: nauc_ndcg_at_1_std
      value: -2.479501845567973
    - type: nauc_ndcg_at_20_diff1
      value: 24.723691897706757
    - type: nauc_ndcg_at_20_max
      value: 18.399201975361787
    - type: nauc_ndcg_at_20_std
      value: 2.8917844365812013
    - type: nauc_ndcg_at_3_diff1
      value: 26.599800600549084
    - type: nauc_ndcg_at_3_max
      value: 17.344488540994927
    - type: nauc_ndcg_at_3_std
      value: -0.17080783586921952
    - type: nauc_ndcg_at_5_diff1
      value: 25.984027442909515
    - type: nauc_ndcg_at_5_max
      value: 17.736902140905325
    - type: nauc_ndcg_at_5_std
      value: -0.20538546466798493
    - type: nauc_precision_at_1000_diff1
      value: 3.117372016834661
    - type: nauc_precision_at_1000_max
      value: 7.967798366288187
    - type: nauc_precision_at_1000_std
      value: 2.0188396778725726
    - type: nauc_precision_at_100_diff1
      value: 11.0493012267289
    - type: nauc_precision_at_100_max
      value: 15.29094702092163
    - type: nauc_precision_at_100_std
      value: 9.566781850851134
    - type: nauc_precision_at_10_diff1
      value: 16.185361455209947
    - type: nauc_precision_at_10_max
      value: 17.925890160877806
    - type: nauc_precision_at_10_std
      value: 4.125664833130542
    - type: nauc_precision_at_1_diff1
      value: 37.2441962865539
    - type: nauc_precision_at_1_max
      value: 22.534613943885276
    - type: nauc_precision_at_1_std
      value: -2.479501845567973
    - type: nauc_precision_at_20_diff1
      value: 13.992027549349888
    - type: nauc_precision_at_20_max
      value: 17.637015499360924
    - type: nauc_precision_at_20_std
      value: 8.696148386896645
    - type: nauc_precision_at_3_diff1
      value: 21.639032017471013
    - type: nauc_precision_at_3_max
      value: 16.289401791760103
    - type: nauc_precision_at_3_std
      value: 0.0870722852396641
    - type: nauc_precision_at_5_diff1
      value: 20.63295832944016
    - type: nauc_precision_at_5_max
      value: 17.295872773951523
    - type: nauc_precision_at_5_std
      value: 0.14307299914708274
    - type: nauc_recall_at_1000_diff1
      value: 13.57694892081493
    - type: nauc_recall_at_1000_max
      value: 20.109277095141024
    - type: nauc_recall_at_1000_std
      value: 21.931352956332276
    - type: nauc_recall_at_100_diff1
      value: 18.554121580441926
    - type: nauc_recall_at_100_max
      value: 16.735991072150373
    - type: nauc_recall_at_100_std
      value: 14.037608911733404
    - type: nauc_recall_at_10_diff1
      value: 17.9750116470627
    - type: nauc_recall_at_10_max
      value: 14.99747681641434
    - type: nauc_recall_at_10_std
      value: 3.9873903476195682
    - type: nauc_recall_at_1_diff1
      value: 34.60126559188873
    - type: nauc_recall_at_1_max
      value: 19.748244491317678
    - type: nauc_recall_at_1_std
      value: -3.2201287026916625
    - type: nauc_recall_at_20_diff1
      value: 15.361358977507825
    - type: nauc_recall_at_20_max
      value: 16.162769140091253
    - type: nauc_recall_at_20_std
      value: 9.552452165627919
    - type: nauc_recall_at_3_diff1
      value: 20.63223458359373
    - type: nauc_recall_at_3_max
      value: 14.003039719774163
    - type: nauc_recall_at_3_std
      value: 1.6065537387953692
    - type: nauc_recall_at_5_diff1
      value: 19.515171377833855
    - type: nauc_recall_at_5_max
      value: 15.099962639838937
    - type: nauc_recall_at_5_std
      value: 1.2965194340275676
    - type: ndcg_at_1
      value: 19.154
    - type: ndcg_at_10
      value: 29.403000000000002
    - type: ndcg_at_100
      value: 35.167
    - type: ndcg_at_1000
      value: 37.964
    - type: ndcg_at_20
      value: 31.557000000000002
    - type: ndcg_at_3
      value: 24.973
    - type: ndcg_at_5
      value: 27.112000000000002
    - type: precision_at_1
      value: 19.154
    - type: precision_at_10
      value: 5.535
    - type: precision_at_100
      value: 0.955
    - type: precision_at_1000
      value: 0.134
    - type: precision_at_20
      value: 3.3770000000000002
    - type: precision_at_3
      value: 12.272
    - type: precision_at_5
      value: 9.005
    - type: recall_at_1
      value: 15.797
    - type: recall_at_10
      value: 41.107
    - type: recall_at_100
      value: 66.52900000000001
    - type: recall_at_1000
      value: 86.768
    - type: recall_at_20
      value: 48.748999999999995
    - type: recall_at_3
      value: 28.716
    - type: recall_at_5
      value: 34.141
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackPhysicsRetrieval (default)
      revision: 79531abbd1fb92d06c6d6315a0cbbbf5bb247ea4
      split: test
      type: mteb/cqadupstack-physics
    metrics:
    - type: main_score
      value: 43.516
    - type: map_at_1
      value: 27.477
    - type: map_at_10
      value: 37.554
    - type: map_at_100
      value: 38.876
    - type: map_at_1000
      value: 38.99
    - type: map_at_20
      value: 38.309
    - type: map_at_3
      value: 34.487
    - type: map_at_5
      value: 36.08
    - type: mrr_at_1
      value: 34.07122232916265
    - type: mrr_at_10
      value: 43.28058878347616
    - type: mrr_at_100
      value: 44.11679663484729
    - type: mrr_at_1000
      value: 44.16065088048062
    - type: mrr_at_20
      value: 43.75169948030771
    - type: mrr_at_3
      value: 40.648059031119644
    - type: mrr_at_5
      value: 42.144690407443
    - type: nauc_map_at_1000_diff1
      value: 53.11716806625181
    - type: nauc_map_at_1000_max
      value: 35.45664823064199
    - type: nauc_map_at_1000_std
      value: 2.1861361604480254
    - type: nauc_map_at_100_diff1
      value: 53.13756094020834
    - type: nauc_map_at_100_max
      value: 35.414022190155535
    - type: nauc_map_at_100_std
      value: 2.1172853626560584
    - type: nauc_map_at_10_diff1
      value: 53.362800758097116
    - type: nauc_map_at_10_max
      value: 35.120906104683144
    - type: nauc_map_at_10_std
      value: 1.3648401515609623
    - type: nauc_map_at_1_diff1
      value: 57.616491138132176
    - type: nauc_map_at_1_max
      value: 33.360475822897804
    - type: nauc_map_at_1_std
      value: -2.1517434693833706
    - type: nauc_map_at_20_diff1
      value: 53.28694534380964
    - type: nauc_map_at_20_max
      value: 35.27319158087644
    - type: nauc_map_at_20_std
      value: 1.8727333074364048
    - type: nauc_map_at_3_diff1
      value: 54.107154112179245
    - type: nauc_map_at_3_max
      value: 34.50940904457967
    - type: nauc_map_at_3_std
      value: -0.15769425621216243
    - type: nauc_map_at_5_diff1
      value: 53.42453940564339
    - type: nauc_map_at_5_max
      value: 34.94771385611006
    - type: nauc_map_at_5_std
      value: 0.6074409657139379
    - type: nauc_mrr_at_1000_diff1
      value: 52.27752417239682
    - type: nauc_mrr_at_1000_max
      value: 36.765948629971476
    - type: nauc_mrr_at_1000_std
      value: 4.302475616232717
    - type: nauc_mrr_at_100_diff1
      value: 52.269051770995176
    - type: nauc_mrr_at_100_max
      value: 36.76909035999622
    - type: nauc_mrr_at_100_std
      value: 4.299069865333679
    - type: nauc_mrr_at_10_diff1
      value: 52.377658822943985
    - type: nauc_mrr_at_10_max
      value: 36.707211313866004
    - type: nauc_mrr_at_10_std
      value: 3.944105976986153
    - type: nauc_mrr_at_1_diff1
      value: 55.83627754980158
    - type: nauc_mrr_at_1_max
      value: 37.08763266019038
    - type: nauc_mrr_at_1_std
      value: 3.0033119574631186
    - type: nauc_mrr_at_20_diff1
      value: 52.3480634575466
    - type: nauc_mrr_at_20_max
      value: 36.63972610802775
    - type: nauc_mrr_at_20_std
      value: 4.255643011583951
    - type: nauc_mrr_at_3_diff1
      value: 52.65151934971672
    - type: nauc_mrr_at_3_max
      value: 36.40720713989
    - type: nauc_mrr_at_3_std
      value: 3.197519381268911
    - type: nauc_mrr_at_5_diff1
      value: 52.3866756788575
    - type: nauc_mrr_at_5_max
      value: 36.731755062099644
    - type: nauc_mrr_at_5_std
      value: 3.8257443367009905
    - type: nauc_ndcg_at_1000_diff1
      value: 51.124410117397645
    - type: nauc_ndcg_at_1000_max
      value: 36.92297872228472
    - type: nauc_ndcg_at_1000_std
      value: 5.943098614351781
    - type: nauc_ndcg_at_100_diff1
      value: 50.9983428273292
    - type: nauc_ndcg_at_100_max
      value: 36.48405211151064
    - type: nauc_ndcg_at_100_std
      value: 5.488151511201609
    - type: nauc_ndcg_at_10_diff1
      value: 51.756184856988405
    - type: nauc_ndcg_at_10_max
      value: 35.38717328414983
    - type: nauc_ndcg_at_10_std
      value: 3.047458430921158
    - type: nauc_ndcg_at_1_diff1
      value: 55.83627754980158
    - type: nauc_ndcg_at_1_max
      value: 37.08763266019038
    - type: nauc_ndcg_at_1_std
      value: 3.0033119574631186
    - type: nauc_ndcg_at_20_diff1
      value: 51.63542460952658
    - type: nauc_ndcg_at_20_max
      value: 35.52888410473399
    - type: nauc_ndcg_at_20_std
      value: 4.38826631541566
    - type: nauc_ndcg_at_3_diff1
      value: 52.280381542128005
    - type: nauc_ndcg_at_3_max
      value: 35.2446928308368
    - type: nauc_ndcg_at_3_std
      value: 1.6071190136031377
    - type: nauc_ndcg_at_5_diff1
      value: 51.63085543217384
    - type: nauc_ndcg_at_5_max
      value: 35.38522586909386
    - type: nauc_ndcg_at_5_std
      value: 2.257550414928455
    - type: nauc_precision_at_1000_diff1
      value: -16.486915214707476
    - type: nauc_precision_at_1000_max
      value: 7.538275188391877
    - type: nauc_precision_at_1000_std
      value: 18.19269313673447
    - type: nauc_precision_at_100_diff1
      value: -1.9736731164148775
    - type: nauc_precision_at_100_max
      value: 16.539438828030338
    - type: nauc_precision_at_100_std
      value: 19.71975128874717
    - type: nauc_precision_at_10_diff1
      value: 22.941192836692938
    - type: nauc_precision_at_10_max
      value: 29.06408942754971
    - type: nauc_precision_at_10_std
      value: 13.706761382257538
    - type: nauc_precision_at_1_diff1
      value: 55.83627754980158
    - type: nauc_precision_at_1_max
      value: 37.08763266019038
    - type: nauc_precision_at_1_std
      value: 3.0033119574631186
    - type: nauc_precision_at_20_diff1
      value: 14.639428084708031
    - type: nauc_precision_at_20_max
      value: 25.194223713311846
    - type: nauc_precision_at_20_std
      value: 16.3724647158108
    - type: nauc_precision_at_3_diff1
      value: 39.24536487566087
    - type: nauc_precision_at_3_max
      value: 34.507130942854594
    - type: nauc_precision_at_3_std
      value: 7.604148713316975
    - type: nauc_precision_at_5_diff1
      value: 31.934728493246205
    - type: nauc_precision_at_5_max
      value: 32.79790114332321
    - type: nauc_precision_at_5_std
      value: 9.300713639365156
    - type: nauc_recall_at_1000_diff1
      value: 28.76947795717725
    - type: nauc_recall_at_1000_max
      value: 47.29845921439558
    - type: nauc_recall_at_1000_std
      value: 50.206579725929835
    - type: nauc_recall_at_100_diff1
      value: 35.99115119379463
    - type: nauc_recall_at_100_max
      value: 35.90016946217124
    - type: nauc_recall_at_100_std
      value: 20.36252722466296
    - type: nauc_recall_at_10_diff1
      value: 44.9035061323177
    - type: nauc_recall_at_10_max
      value: 31.55646682626508
    - type: nauc_recall_at_10_std
      value: 5.202368314746213
    - type: nauc_recall_at_1_diff1
      value: 57.616491138132176
    - type: nauc_recall_at_1_max
      value: 33.360475822897804
    - type: nauc_recall_at_1_std
      value: -2.1517434693833706
    - type: nauc_recall_at_20_diff1
      value: 44.082155347846786
    - type: nauc_recall_at_20_max
      value: 31.111947497273174
    - type: nauc_recall_at_20_std
      value: 10.74007442952765
    - type: nauc_recall_at_3_diff1
      value: 48.99683708882751
    - type: nauc_recall_at_3_max
      value: 31.591738499338323
    - type: nauc_recall_at_3_std
      value: -0.4970248113753141
    - type: nauc_recall_at_5_diff1
      value: 45.72255982322729
    - type: nauc_recall_at_5_max
      value: 31.9303024917854
    - type: nauc_recall_at_5_std
      value: 2.178007010965473
    - type: ndcg_at_1
      value: 34.071
    - type: ndcg_at_10
      value: 43.516
    - type: ndcg_at_100
      value: 49.001
    - type: ndcg_at_1000
      value: 51.176
    - type: ndcg_at_20
      value: 45.675
    - type: ndcg_at_3
      value: 38.471
    - type: ndcg_at_5
      value: 40.721000000000004
    - type: precision_at_1
      value: 34.071
    - type: precision_at_10
      value: 7.921
    - type: precision_at_100
      value: 1.238
    - type: precision_at_1000
      value: 0.161
    - type: precision_at_20
      value: 4.692
    - type: precision_at_3
      value: 18.062
    - type: precision_at_5
      value: 12.839
    - type: recall_at_1
      value: 27.477
    - type: recall_at_10
      value: 55.627
    - type: recall_at_100
      value: 78.999
    - type: recall_at_1000
      value: 93.388
    - type: recall_at_20
      value: 63.099000000000004
    - type: recall_at_3
      value: 41.396
    - type: recall_at_5
      value: 47.199000000000005
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackProgrammersRetrieval (default)
      revision: 6184bc1440d2dbc7612be22b50686b8826d22b32
      split: test
      type: mteb/cqadupstack-programmers
    metrics:
    - type: main_score
      value: 38.024
    - type: map_at_1
      value: 23.173
    - type: map_at_10
      value: 32.297
    - type: map_at_100
      value: 33.672000000000004
    - type: map_at_1000
      value: 33.793
    - type: map_at_20
      value: 33.064
    - type: map_at_3
      value: 29.156
    - type: map_at_5
      value: 30.964999999999996
    - type: mrr_at_1
      value: 28.538812785388128
    - type: mrr_at_10
      value: 37.33076031021236
    - type: mrr_at_100
      value: 38.33757969963895
    - type: mrr_at_1000
      value: 38.39935336168593
    - type: mrr_at_20
      value: 37.936087860689724
    - type: mrr_at_3
      value: 34.855403348554034
    - type: mrr_at_5
      value: 36.19672754946727
    - type: nauc_map_at_1000_diff1
      value: 40.108286871576595
    - type: nauc_map_at_1000_max
      value: 34.932555227073095
    - type: nauc_map_at_1000_std
      value: 6.221807917311268
    - type: nauc_map_at_100_diff1
      value: 40.09828293293427
    - type: nauc_map_at_100_max
      value: 34.952917251621365
    - type: nauc_map_at_100_std
      value: 6.231287481156123
    - type: nauc_map_at_10_diff1
      value: 40.01528416311391
    - type: nauc_map_at_10_max
      value: 33.89944085012165
    - type: nauc_map_at_10_std
      value: 5.258003016169289
    - type: nauc_map_at_1_diff1
      value: 45.05748000688197
    - type: nauc_map_at_1_max
      value: 30.741952307152193
    - type: nauc_map_at_1_std
      value: 0.10027922648870957
    - type: nauc_map_at_20_diff1
      value: 40.213591831598336
    - type: nauc_map_at_20_max
      value: 34.62908891442373
    - type: nauc_map_at_20_std
      value: 5.763711381584264
    - type: nauc_map_at_3_diff1
      value: 40.89235452782516
    - type: nauc_map_at_3_max
      value: 33.1747621759765
    - type: nauc_map_at_3_std
      value: 3.331742393981075
    - type: nauc_map_at_5_diff1
      value: 40.403274490377534
    - type: nauc_map_at_5_max
      value: 33.94134091027758
    - type: nauc_map_at_5_std
      value: 4.360176315671494
    - type: nauc_mrr_at_1000_diff1
      value: 40.14241619166317
    - type: nauc_mrr_at_1000_max
      value: 38.65445721763423
    - type: nauc_mrr_at_1000_std
      value: 9.749476533081992
    - type: nauc_mrr_at_100_diff1
      value: 40.14319401324518
    - type: nauc_mrr_at_100_max
      value: 38.659012797855915
    - type: nauc_mrr_at_100_std
      value: 9.750005980569185
    - type: nauc_mrr_at_10_diff1
      value: 39.843622825414
    - type: nauc_mrr_at_10_max
      value: 38.25272189734047
    - type: nauc_mrr_at_10_std
      value: 9.455238241095982
    - type: nauc_mrr_at_1_diff1
      value: 45.544486458047764
    - type: nauc_mrr_at_1_max
      value: 38.36905133790403
    - type: nauc_mrr_at_1_std
      value: 6.313800371398363
    - type: nauc_mrr_at_20_diff1
      value: 40.168037291291945
    - type: nauc_mrr_at_20_max
      value: 38.588132492862286
    - type: nauc_mrr_at_20_std
      value: 9.59289103060053
    - type: nauc_mrr_at_3_diff1
      value: 40.77069874457395
    - type: nauc_mrr_at_3_max
      value: 39.17196241078363
    - type: nauc_mrr_at_3_std
      value: 8.617425759338197
    - type: nauc_mrr_at_5_diff1
      value: 40.06388436713267
    - type: nauc_mrr_at_5_max
      value: 38.459050270900846
    - type: nauc_mrr_at_5_std
      value: 9.01716272113449
    - type: nauc_ndcg_at_1000_diff1
      value: 38.28079417943546
    - type: nauc_ndcg_at_1000_max
      value: 37.373375829157126
    - type: nauc_ndcg_at_1000_std
      value: 10.915194308249555
    - type: nauc_ndcg_at_100_diff1
      value: 38.303029042268314
    - type: nauc_ndcg_at_100_max
      value: 37.874116564812326
    - type: nauc_ndcg_at_100_std
      value: 11.447496719900775
    - type: nauc_ndcg_at_10_diff1
      value: 37.8583307138946
    - type: nauc_ndcg_at_10_max
      value: 34.708345234497166
    - type: nauc_ndcg_at_10_std
      value: 8.020760282496871
    - type: nauc_ndcg_at_1_diff1
      value: 45.544486458047764
    - type: nauc_ndcg_at_1_max
      value: 38.36905133790403
    - type: nauc_ndcg_at_1_std
      value: 6.313800371398363
    - type: nauc_ndcg_at_20_diff1
      value: 38.70263255314536
    - type: nauc_ndcg_at_20_max
      value: 36.74873403813739
    - type: nauc_ndcg_at_20_std
      value: 9.245300863480727
    - type: nauc_ndcg_at_3_diff1
      value: 39.68243402945326
    - type: nauc_ndcg_at_3_max
      value: 35.80245947389082
    - type: nauc_ndcg_at_3_std
      value: 6.01195047461147
    - type: nauc_ndcg_at_5_diff1
      value: 38.60536509722538
    - type: nauc_ndcg_at_5_max
      value: 35.314432767482714
    - type: nauc_ndcg_at_5_std
      value: 6.5428970299886355
    - type: nauc_precision_at_1000_diff1
      value: -4.069384802622214
    - type: nauc_precision_at_1000_max
      value: 6.707725051629613
    - type: nauc_precision_at_1000_std
      value: 13.958586804597543
    - type: nauc_precision_at_100_diff1
      value: 3.6277603347565393
    - type: nauc_precision_at_100_max
      value: 25.52632391438941
    - type: nauc_precision_at_100_std
      value: 23.784864119867034
    - type: nauc_precision_at_10_diff1
      value: 18.261312841674247
    - type: nauc_precision_at_10_max
      value: 34.11796051379501
    - type: nauc_precision_at_10_std
      value: 19.77962411706688
    - type: nauc_precision_at_1_diff1
      value: 45.544486458047764
    - type: nauc_precision_at_1_max
      value: 38.36905133790403
    - type: nauc_precision_at_1_std
      value: 6.313800371398363
    - type: nauc_precision_at_20_diff1
      value: 14.653399217564534
    - type: nauc_precision_at_20_max
      value: 35.58870037452182
    - type: nauc_precision_at_20_std
      value: 22.622999716137446
    - type: nauc_precision_at_3_diff1
      value: 30.858809285910805
    - type: nauc_precision_at_3_max
      value: 40.875462270983995
    - type: nauc_precision_at_3_std
      value: 14.039083589242434
    - type: nauc_precision_at_5_diff1
      value: 24.894001411473027
    - type: nauc_precision_at_5_max
      value: 38.182725673958075
    - type: nauc_precision_at_5_std
      value: 16.206658306046783
    - type: nauc_recall_at_1000_diff1
      value: 16.53564900892544
    - type: nauc_recall_at_1000_max
      value: 46.72318966917282
    - type: nauc_recall_at_1000_std
      value: 54.442875812845855
    - type: nauc_recall_at_100_diff1
      value: 29.021625912783367
    - type: nauc_recall_at_100_max
      value: 42.51861007543889
    - type: nauc_recall_at_100_std
      value: 31.609526311067608
    - type: nauc_recall_at_10_diff1
      value: 29.824715829870073
    - type: nauc_recall_at_10_max
      value: 29.657124103804104
    - type: nauc_recall_at_10_std
      value: 11.250748700772178
    - type: nauc_recall_at_1_diff1
      value: 45.05748000688197
    - type: nauc_recall_at_1_max
      value: 30.741952307152193
    - type: nauc_recall_at_1_std
      value: 0.10027922648870957
    - type: nauc_recall_at_20_diff1
      value: 32.42540174551291
    - type: nauc_recall_at_20_max
      value: 35.98077437174156
    - type: nauc_recall_at_20_std
      value: 15.309458278296484
    - type: nauc_recall_at_3_diff1
      value: 35.45259519413173
    - type: nauc_recall_at_3_max
      value: 32.67176629682575
    - type: nauc_recall_at_3_std
      value: 4.565244871237187
    - type: nauc_recall_at_5_diff1
      value: 32.457520797399155
    - type: nauc_recall_at_5_max
      value: 31.85239341740217
    - type: nauc_recall_at_5_std
      value: 6.528652055169674
    - type: ndcg_at_1
      value: 28.538999999999998
    - type: ndcg_at_10
      value: 38.024
    - type: ndcg_at_100
      value: 44.062
    - type: ndcg_at_1000
      value: 46.539
    - type: ndcg_at_20
      value: 40.455000000000005
    - type: ndcg_at_3
      value: 32.818999999999996
    - type: ndcg_at_5
      value: 35.231
    - type: precision_at_1
      value: 28.538999999999998
    - type: precision_at_10
      value: 7.077999999999999
    - type: precision_at_100
      value: 1.183
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_20
      value: 4.275
    - type: precision_at_3
      value: 15.943999999999999
    - type: precision_at_5
      value: 11.620999999999999
    - type: recall_at_1
      value: 23.173
    - type: recall_at_10
      value: 50.352
    - type: recall_at_100
      value: 76.087
    - type: recall_at_1000
      value: 92.92399999999999
    - type: recall_at_20
      value: 59.082
    - type: recall_at_3
      value: 35.544
    - type: recall_at_5
      value: 41.937999999999995
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackRetrieval (default)
      revision: CQADupstackRetrieval_is_a_combined_dataset
      split: test
      type: CQADupstackRetrieval_is_a_combined_dataset
    metrics:
    - type: main_score
      value: 38.150083333333335
    - type: ndcg_at_10
      value: 38.150083333333335
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackStatsRetrieval (default)
      revision: 65ac3a16b8e91f9cee4c9828cc7c335575432a2a
      split: test
      type: mteb/cqadupstack-stats
    metrics:
    - type: main_score
      value: 33.661
    - type: map_at_1
      value: 23.879
    - type: map_at_10
      value: 29.93
    - type: map_at_100
      value: 30.871
    - type: map_at_1000
      value: 30.963
    - type: map_at_20
      value: 30.455
    - type: map_at_3
      value: 28.162
    - type: map_at_5
      value: 29.182000000000002
    - type: mrr_at_1
      value: 26.68711656441718
    - type: mrr_at_10
      value: 32.58478186775732
    - type: mrr_at_100
      value: 33.439877614219206
    - type: mrr_at_1000
      value: 33.509744356192215
    - type: mrr_at_20
      value: 33.08638504959304
    - type: mrr_at_3
      value: 30.904907975460134
    - type: mrr_at_5
      value: 31.86349693251534
    - type: nauc_map_at_1000_diff1
      value: 48.53139009200422
    - type: nauc_map_at_1000_max
      value: 41.07136045901999
    - type: nauc_map_at_1000_std
      value: 11.677315277008843
    - type: nauc_map_at_100_diff1
      value: 48.50830887484553
    - type: nauc_map_at_100_max
      value: 41.033344784856354
    - type: nauc_map_at_100_std
      value: 11.664201973879315
    - type: nauc_map_at_10_diff1
      value: 48.91206176897672
    - type: nauc_map_at_10_max
      value: 40.80325462807101
    - type: nauc_map_at_10_std
      value: 11.14885787161969
    - type: nauc_map_at_1_diff1
      value: 55.659938675798394
    - type: nauc_map_at_1_max
      value: 39.66838947608073
    - type: nauc_map_at_1_std
      value: 6.825041531017375
    - type: nauc_map_at_20_diff1
      value: 48.591524746620266
    - type: nauc_map_at_20_max
      value: 40.78908497571411
    - type: nauc_map_at_20_std
      value: 11.367474736784935
    - type: nauc_map_at_3_diff1
      value: 49.999805605139244
    - type: nauc_map_at_3_max
      value: 40.7083589084763
    - type: nauc_map_at_3_std
      value: 9.539830643323945
    - type: nauc_map_at_5_diff1
      value: 49.41513832999669
    - type: nauc_map_at_5_max
      value: 40.682908322546446
    - type: nauc_map_at_5_std
      value: 10.401189036376163
    - type: nauc_mrr_at_1000_diff1
      value: 48.23812662173282
    - type: nauc_mrr_at_1000_max
      value: 42.89771775296582
    - type: nauc_mrr_at_1000_std
      value: 14.23723724292204
    - type: nauc_mrr_at_100_diff1
      value: 48.209766136073554
    - type: nauc_mrr_at_100_max
      value: 42.892924636996135
    - type: nauc_mrr_at_100_std
      value: 14.24054457950116
    - type: nauc_mrr_at_10_diff1
      value: 48.473273186214705
    - type: nauc_mrr_at_10_max
      value: 42.82520357348653
    - type: nauc_mrr_at_10_std
      value: 14.016153249262794
    - type: nauc_mrr_at_1_diff1
      value: 55.03641495962279
    - type: nauc_mrr_at_1_max
      value: 42.725997739916615
    - type: nauc_mrr_at_1_std
      value: 11.822056277995028
    - type: nauc_mrr_at_20_diff1
      value: 48.284200279599496
    - type: nauc_mrr_at_20_max
      value: 42.7371964321212
    - type: nauc_mrr_at_20_std
      value: 13.960829135523737
    - type: nauc_mrr_at_3_diff1
      value: 49.499792042223866
    - type: nauc_mrr_at_3_max
      value: 43.098227232894246
    - type: nauc_mrr_at_3_std
      value: 13.154632787036547
    - type: nauc_mrr_at_5_diff1
      value: 49.10361982716086
    - type: nauc_mrr_at_5_max
      value: 42.88372641833646
    - type: nauc_mrr_at_5_std
      value: 13.4614603500215
    - type: nauc_ndcg_at_1000_diff1
      value: 45.06608258942947
    - type: nauc_ndcg_at_1000_max
      value: 42.79644362867509
    - type: nauc_ndcg_at_1000_std
      value: 16.15949102798443
    - type: nauc_ndcg_at_100_diff1
      value: 44.266893620089554
    - type: nauc_ndcg_at_100_max
      value: 42.206424784327574
    - type: nauc_ndcg_at_100_std
      value: 16.05284758202025
    - type: nauc_ndcg_at_10_diff1
      value: 45.986130524985626
    - type: nauc_ndcg_at_10_max
      value: 41.19638299083851
    - type: nauc_ndcg_at_10_std
      value: 13.629470298951524
    - type: nauc_ndcg_at_1_diff1
      value: 55.03641495962279
    - type: nauc_ndcg_at_1_max
      value: 42.725997739916615
    - type: nauc_ndcg_at_1_std
      value: 11.822056277995028
    - type: nauc_ndcg_at_20_diff1
      value: 44.84752448706012
    - type: nauc_ndcg_at_20_max
      value: 40.844656950591634
    - type: nauc_ndcg_at_20_std
      value: 13.956165195086271
    - type: nauc_ndcg_at_3_diff1
      value: 47.93537280384065
    - type: nauc_ndcg_at_3_max
      value: 41.40364123527904
    - type: nauc_ndcg_at_3_std
      value: 11.195130884125609
    - type: nauc_ndcg_at_5_diff1
      value: 47.343700055586346
    - type: nauc_ndcg_at_5_max
      value: 41.24280986284959
    - type: nauc_ndcg_at_5_std
      value: 12.000132612812044
    - type: nauc_precision_at_1000_diff1
      value: 4.994176167963606
    - type: nauc_precision_at_1000_max
      value: 27.486847290176904
    - type: nauc_precision_at_1000_std
      value: 23.927151301162095
    - type: nauc_precision_at_100_diff1
      value: 15.07041459911376
    - type: nauc_precision_at_100_max
      value: 36.53781189328251
    - type: nauc_precision_at_100_std
      value: 29.5490135147151
    - type: nauc_precision_at_10_diff1
      value: 29.58860754340708
    - type: nauc_precision_at_10_max
      value: 40.30128439488323
    - type: nauc_precision_at_10_std
      value: 24.53133157634616
    - type: nauc_precision_at_1_diff1
      value: 55.03641495962279
    - type: nauc_precision_at_1_max
      value: 42.725997739916615
    - type: nauc_precision_at_1_std
      value: 11.822056277995028
    - type: nauc_precision_at_20_diff1
      value: 24.75997844201911
    - type: nauc_precision_at_20_max
      value: 37.42292478671453
    - type: nauc_precision_at_20_std
      value: 25.045588924299995
    - type: nauc_precision_at_3_diff1
      value: 39.700372389353454
    - type: nauc_precision_at_3_max
      value: 42.623221778268366
    - type: nauc_precision_at_3_std
      value: 17.754093140734657
    - type: nauc_precision_at_5_diff1
      value: 35.8446328417336
    - type: nauc_precision_at_5_max
      value: 41.77355878364959
    - type: nauc_precision_at_5_std
      value: 19.993565988703768
    - type: nauc_recall_at_1000_diff1
      value: 24.521138453207396
    - type: nauc_recall_at_1000_max
      value: 47.71668606929123
    - type: nauc_recall_at_1000_std
      value: 41.58965703674164
    - type: nauc_recall_at_100_diff1
      value: 25.24665773660013
    - type: nauc_recall_at_100_max
      value: 41.30250865497976
    - type: nauc_recall_at_100_std
      value: 30.672023026584007
    - type: nauc_recall_at_10_diff1
      value: 36.8832100241956
    - type: nauc_recall_at_10_max
      value: 38.49814277935064
    - type: nauc_recall_at_10_std
      value: 17.48144338977386
    - type: nauc_recall_at_1_diff1
      value: 55.659938675798394
    - type: nauc_recall_at_1_max
      value: 39.66838947608073
    - type: nauc_recall_at_1_std
      value: 6.825041531017375
    - type: nauc_recall_at_20_diff1
      value: 32.01354938288064
    - type: nauc_recall_at_20_max
      value: 36.63011334832695
    - type: nauc_recall_at_20_std
      value: 18.41097455462446
    - type: nauc_recall_at_3_diff1
      value: 42.76006973727167
    - type: nauc_recall_at_3_max
      value: 40.153203605070274
    - type: nauc_recall_at_3_std
      value: 11.005059866357977
    - type: nauc_recall_at_5_diff1
      value: 41.39165317018751
    - type: nauc_recall_at_5_max
      value: 39.736897424968035
    - type: nauc_recall_at_5_std
      value: 13.22928947133363
    - type: ndcg_at_1
      value: 26.687
    - type: ndcg_at_10
      value: 33.661
    - type: ndcg_at_100
      value: 38.35
    - type: ndcg_at_1000
      value: 40.8
    - type: ndcg_at_20
      value: 35.437000000000005
    - type: ndcg_at_3
      value: 30.342999999999996
    - type: ndcg_at_5
      value: 31.941000000000003
    - type: precision_at_1
      value: 26.687
    - type: precision_at_10
      value: 5.153
    - type: precision_at_100
      value: 0.814
    - type: precision_at_1000
      value: 0.11
    - type: precision_at_20
      value: 3.029
    - type: precision_at_3
      value: 12.883
    - type: precision_at_5
      value: 8.803999999999998
    - type: recall_at_1
      value: 23.879
    - type: recall_at_10
      value: 42.477
    - type: recall_at_100
      value: 63.906
    - type: recall_at_1000
      value: 82.211
    - type: recall_at_20
      value: 49.045
    - type: recall_at_3
      value: 33.332
    - type: recall_at_5
      value: 37.354
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackTexRetrieval (default)
      revision: 46989137a86843e03a6195de44b09deda022eec7
      split: test
      type: mteb/cqadupstack-tex
    metrics:
    - type: main_score
      value: 26.76
    - type: map_at_1
      value: 15.662999999999998
    - type: map_at_10
      value: 22.35
    - type: map_at_100
      value: 23.427
    - type: map_at_1000
      value: 23.563000000000002
    - type: map_at_20
      value: 22.926
    - type: map_at_3
      value: 20.084
    - type: map_at_5
      value: 21.313
    - type: mrr_at_1
      value: 18.960770818995183
    - type: mrr_at_10
      value: 25.904983121948067
    - type: mrr_at_100
      value: 26.821542489430144
    - type: mrr_at_1000
      value: 26.906098040412544
    - type: mrr_at_20
      value: 26.403069282619253
    - type: mrr_at_3
      value: 23.692360633172754
    - type: mrr_at_5
      value: 24.924294562973202
    - type: nauc_map_at_1000_diff1
      value: 36.32845762325914
    - type: nauc_map_at_1000_max
      value: 33.55736291239209
    - type: nauc_map_at_1000_std
      value: 3.432229473309837
    - type: nauc_map_at_100_diff1
      value: 36.30089055071476
    - type: nauc_map_at_100_max
      value: 33.52021447234604
    - type: nauc_map_at_100_std
      value: 3.3949530646797705
    - type: nauc_map_at_10_diff1
      value: 36.706713645539004
    - type: nauc_map_at_10_max
      value: 33.36722158098282
    - type: nauc_map_at_10_std
      value: 2.7726772519273584
    - type: nauc_map_at_1_diff1
      value: 42.78539859955363
    - type: nauc_map_at_1_max
      value: 32.50849076879976
    - type: nauc_map_at_1_std
      value: 1.3954658101521349
    - type: nauc_map_at_20_diff1
      value: 36.44434182966826
    - type: nauc_map_at_20_max
      value: 33.4223606249205
    - type: nauc_map_at_20_std
      value: 3.056877020975398
    - type: nauc_map_at_3_diff1
      value: 38.09385217889672
    - type: nauc_map_at_3_max
      value: 33.444266093850466
    - type: nauc_map_at_3_std
      value: 1.4210812078047044
    - type: nauc_map_at_5_diff1
      value: 37.45455194954524
    - type: nauc_map_at_5_max
      value: 33.58297487933362
    - type: nauc_map_at_5_std
      value: 2.225792098397186
    - type: nauc_mrr_at_1000_diff1
      value: 34.97608766191874
    - type: nauc_mrr_at_1000_max
      value: 33.6349173107215
    - type: nauc_mrr_at_1000_std
      value: 3.0989650345980073
    - type: nauc_mrr_at_100_diff1
      value: 34.94255258229341
    - type: nauc_mrr_at_100_max
      value: 33.62631058099838
    - type: nauc_mrr_at_100_std
      value: 3.1051547505163493
    - type: nauc_mrr_at_10_diff1
      value: 35.194039255792454
    - type: nauc_mrr_at_10_max
      value: 33.604737843685626
    - type: nauc_mrr_at_10_std
      value: 2.5905553770990615
    - type: nauc_mrr_at_1_diff1
      value: 40.836866506372836
    - type: nauc_mrr_at_1_max
      value: 33.39325239663001
    - type: nauc_mrr_at_1_std
      value: 1.127754938660376
    - type: nauc_mrr_at_20_diff1
      value: 35.00502184255156
    - type: nauc_mrr_at_20_max
      value: 33.52420796858889
    - type: nauc_mrr_at_20_std
      value: 2.898811413334367
    - type: nauc_mrr_at_3_diff1
      value: 36.338551068937036
    - type: nauc_mrr_at_3_max
      value: 33.815881689155916
    - type: nauc_mrr_at_3_std
      value: 1.5498753093044315
    - type: nauc_mrr_at_5_diff1
      value: 35.873030664605885
    - type: nauc_mrr_at_5_max
      value: 33.897101810836226
    - type: nauc_mrr_at_5_std
      value: 2.1967073621343687
    - type: nauc_ndcg_at_1000_diff1
      value: 32.837773001140015
    - type: nauc_ndcg_at_1000_max
      value: 33.978063813852195
    - type: nauc_ndcg_at_1000_std
      value: 7.18061649572422
    - type: nauc_ndcg_at_100_diff1
      value: 32.23692228107245
    - type: nauc_ndcg_at_100_max
      value: 33.558149600646544
    - type: nauc_ndcg_at_100_std
      value: 6.814544306611417
    - type: nauc_ndcg_at_10_diff1
      value: 33.79758164734529
    - type: nauc_ndcg_at_10_max
      value: 33.16077004784226
    - type: nauc_ndcg_at_10_std
      value: 3.807132179198105
    - type: nauc_ndcg_at_1_diff1
      value: 40.836866506372836
    - type: nauc_ndcg_at_1_max
      value: 33.39325239663001
    - type: nauc_ndcg_at_1_std
      value: 1.127754938660376
    - type: nauc_ndcg_at_20_diff1
      value: 33.04159869018307
    - type: nauc_ndcg_at_20_max
      value: 33.095598392370086
    - type: nauc_ndcg_at_20_std
      value: 4.86129474656699
    - type: nauc_ndcg_at_3_diff1
      value: 36.32253988443199
    - type: nauc_ndcg_at_3_max
      value: 33.9538290861425
    - type: nauc_ndcg_at_3_std
      value: 1.3215696887170623
    - type: nauc_ndcg_at_5_diff1
      value: 35.47052283188967
    - type: nauc_ndcg_at_5_max
      value: 33.89612026096585
    - type: nauc_ndcg_at_5_std
      value: 2.6710425885570195
    - type: nauc_precision_at_1000_diff1
      value: 0.9916365417350987
    - type: nauc_precision_at_1000_max
      value: 18.94027390642169
    - type: nauc_precision_at_1000_std
      value: 11.991965258965426
    - type: nauc_precision_at_100_diff1
      value: 8.540728510260907
    - type: nauc_precision_at_100_max
      value: 25.34067366375036
    - type: nauc_precision_at_100_std
      value: 14.584127511948362
    - type: nauc_precision_at_10_diff1
      value: 21.425375464273117
    - type: nauc_precision_at_10_max
      value: 30.715529687561215
    - type: nauc_precision_at_10_std
      value: 7.050366947545752
    - type: nauc_precision_at_1_diff1
      value: 40.836866506372836
    - type: nauc_precision_at_1_max
      value: 33.39325239663001
    - type: nauc_precision_at_1_std
      value: 1.127754938660376
    - type: nauc_precision_at_20_diff1
      value: 17.126577160838767
    - type: nauc_precision_at_20_max
      value: 28.180350861048918
    - type: nauc_precision_at_20_std
      value: 9.204946568923095
    - type: nauc_precision_at_3_diff1
      value: 30.03248221152837
    - type: nauc_precision_at_3_max
      value: 34.469274514363576
    - type: nauc_precision_at_3_std
      value: 1.3169507336484703
    - type: nauc_precision_at_5_diff1
      value: 27.691321638789717
    - type: nauc_precision_at_5_max
      value: 34.448336681904514
    - type: nauc_precision_at_5_std
      value: 4.3727325951693565
    - type: nauc_recall_at_1000_diff1
      value: 13.813296274685182
    - type: nauc_recall_at_1000_max
      value: 32.53692936157239
    - type: nauc_recall_at_1000_std
      value: 33.6379690047766
    - type: nauc_recall_at_100_diff1
      value: 17.544425110662758
    - type: nauc_recall_at_100_max
      value: 29.99355188898577
    - type: nauc_recall_at_100_std
      value: 19.181138219276104
    - type: nauc_recall_at_10_diff1
      value: 25.579263146027888
    - type: nauc_recall_at_10_max
      value: 29.688994497442945
    - type: nauc_recall_at_10_std
      value: 6.101926427651782
    - type: nauc_recall_at_1_diff1
      value: 42.78539859955363
    - type: nauc_recall_at_1_max
      value: 32.50849076879976
    - type: nauc_recall_at_1_std
      value: 1.3954658101521349
    - type: nauc_recall_at_20_diff1
      value: 22.855697416129058
    - type: nauc_recall_at_20_max
      value: 29.016750276488402
    - type: nauc_recall_at_20_std
      value: 9.507542232520008
    - type: nauc_recall_at_3_diff1
      value: 32.74667430133546
    - type: nauc_recall_at_3_max
      value: 32.36180346979294
    - type: nauc_recall_at_3_std
      value: 1.5435126499493685
    - type: nauc_recall_at_5_diff1
      value: 30.35636475352035
    - type: nauc_recall_at_5_max
      value: 31.964366285189993
    - type: nauc_recall_at_5_std
      value: 3.7439177812212914
    - type: ndcg_at_1
      value: 18.961
    - type: ndcg_at_10
      value: 26.76
    - type: ndcg_at_100
      value: 31.987
    - type: ndcg_at_1000
      value: 35.14
    - type: ndcg_at_20
      value: 28.666000000000004
    - type: ndcg_at_3
      value: 22.611
    - type: ndcg_at_5
      value: 24.495
    - type: precision_at_1
      value: 18.961
    - type: precision_at_10
      value: 4.955
    - type: precision_at_100
      value: 0.886
    - type: precision_at_1000
      value: 0.134
    - type: precision_at_20
      value: 3.02
    - type: precision_at_3
      value: 10.679
    - type: precision_at_5
      value: 7.811
    - type: recall_at_1
      value: 15.662999999999998
    - type: recall_at_10
      value: 36.486000000000004
    - type: recall_at_100
      value: 60.13699999999999
    - type: recall_at_1000
      value: 82.674
    - type: recall_at_20
      value: 43.636
    - type: recall_at_3
      value: 24.895999999999997
    - type: recall_at_5
      value: 29.755
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackUnixRetrieval (default)
      revision: 6c6430d3a6d36f8d2a829195bc5dc94d7e063e53
      split: test
      type: mteb/cqadupstack-unix
    metrics:
    - type: main_score
      value: 37.25
    - type: map_at_1
      value: 23.52
    - type: map_at_10
      value: 32.04
    - type: map_at_100
      value: 33.265
    - type: map_at_1000
      value: 33.364
    - type: map_at_20
      value: 32.705
    - type: map_at_3
      value: 29.433
    - type: map_at_5
      value: 30.803000000000004
    - type: mrr_at_1
      value: 27.51865671641791
    - type: mrr_at_10
      value: 36.00424218194739
    - type: mrr_at_100
      value: 36.903107608606675
    - type: mrr_at_1000
      value: 36.96395251148347
    - type: mrr_at_20
      value: 36.459384561103356
    - type: mrr_at_3
      value: 33.62873134328357
    - type: mrr_at_5
      value: 34.91138059701488
    - type: nauc_map_at_1000_diff1
      value: 44.26760971600569
    - type: nauc_map_at_1000_max
      value: 37.03675061352433
    - type: nauc_map_at_1000_std
      value: -0.6748853500833264
    - type: nauc_map_at_100_diff1
      value: 44.26591155341421
    - type: nauc_map_at_100_max
      value: 37.0374608260786
    - type: nauc_map_at_100_std
      value: -0.6739130374083069
    - type: nauc_map_at_10_diff1
      value: 44.64333115475081
    - type: nauc_map_at_10_max
      value: 36.618375959258096
    - type: nauc_map_at_10_std
      value: -1.3282754617161208
    - type: nauc_map_at_1_diff1
      value: 51.61094035660931
    - type: nauc_map_at_1_max
      value: 35.24232228126847
    - type: nauc_map_at_1_std
      value: -4.805963422515798
    - type: nauc_map_at_20_diff1
      value: 44.41630684519036
    - type: nauc_map_at_20_max
      value: 37.02214474390442
    - type: nauc_map_at_20_std
      value: -0.8251824639491345
    - type: nauc_map_at_3_diff1
      value: 45.61815969575457
    - type: nauc_map_at_3_max
      value: 35.387991045369716
    - type: nauc_map_at_3_std
      value: -3.239524904892324
    - type: nauc_map_at_5_diff1
      value: 44.82439840305814
    - type: nauc_map_at_5_max
      value: 36.24725748815871
    - type: nauc_map_at_5_std
      value: -1.851648510167343
    - type: nauc_mrr_at_1000_diff1
      value: 42.03257519827712
    - type: nauc_mrr_at_1000_max
      value: 38.37966433606752
    - type: nauc_mrr_at_1000_std
      value: -0.15282541892993076
    - type: nauc_mrr_at_100_diff1
      value: 42.014741602279564
    - type: nauc_mrr_at_100_max
      value: 38.37840441614305
    - type: nauc_mrr_at_100_std
      value: -0.14610389460051212
    - type: nauc_mrr_at_10_diff1
      value: 42.15513668994741
    - type: nauc_mrr_at_10_max
      value: 38.30754832862629
    - type: nauc_mrr_at_10_std
      value: -0.5099123585689097
    - type: nauc_mrr_at_1_diff1
      value: 49.1101047164422
    - type: nauc_mrr_at_1_max
      value: 37.933671986494026
    - type: nauc_mrr_at_1_std
      value: -3.7731587131539976
    - type: nauc_mrr_at_20_diff1
      value: 42.06752969763786
    - type: nauc_mrr_at_20_max
      value: 38.36700308017657
    - type: nauc_mrr_at_20_std
      value: -0.3054736037276272
    - type: nauc_mrr_at_3_diff1
      value: 42.62372944034753
    - type: nauc_mrr_at_3_max
      value: 37.909468795649666
    - type: nauc_mrr_at_3_std
      value: -1.527800377472655
    - type: nauc_mrr_at_5_diff1
      value: 42.198527449928804
    - type: nauc_mrr_at_5_max
      value: 38.35215994800784
    - type: nauc_mrr_at_5_std
      value: -0.5485521166603851
    - type: nauc_ndcg_at_1000_diff1
      value: 40.855780678246724
    - type: nauc_ndcg_at_1000_max
      value: 38.394998686556
    - type: nauc_ndcg_at_1000_std
      value: 2.8353732609834514
    - type: nauc_ndcg_at_100_diff1
      value: 40.55606418953665
    - type: nauc_ndcg_at_100_max
      value: 38.454872156001805
    - type: nauc_ndcg_at_100_std
      value: 3.061615143253422
    - type: nauc_ndcg_at_10_diff1
      value: 41.90525124437928
    - type: nauc_ndcg_at_10_max
      value: 37.591000536129435
    - type: nauc_ndcg_at_10_std
      value: 0.7110197729123375
    - type: nauc_ndcg_at_1_diff1
      value: 49.1101047164422
    - type: nauc_ndcg_at_1_max
      value: 37.933671986494026
    - type: nauc_ndcg_at_1_std
      value: -3.7731587131539976
    - type: nauc_ndcg_at_20_diff1
      value: 41.307377431306556
    - type: nauc_ndcg_at_20_max
      value: 38.41832801024425
    - type: nauc_ndcg_at_20_std
      value: 1.9886496294555962
    - type: nauc_ndcg_at_3_diff1
      value: 42.986902248079836
    - type: nauc_ndcg_at_3_max
      value: 36.196771893007885
    - type: nauc_ndcg_at_3_std
      value: -2.2909240633804404
    - type: nauc_ndcg_at_5_diff1
      value: 42.11824383427997
    - type: nauc_ndcg_at_5_max
      value: 37.09158761390391
    - type: nauc_ndcg_at_5_std
      value: -0.1957306778551101
    - type: nauc_precision_at_1000_diff1
      value: -14.92219394812046
    - type: nauc_precision_at_1000_max
      value: 6.200453065515646
    - type: nauc_precision_at_1000_std
      value: 7.198226536807955
    - type: nauc_precision_at_100_diff1
      value: -0.933334477353504
    - type: nauc_precision_at_100_max
      value: 23.74769225281431
    - type: nauc_precision_at_100_std
      value: 13.760336011422103
    - type: nauc_precision_at_10_diff1
      value: 21.317504992362302
    - type: nauc_precision_at_10_max
      value: 36.64677303747258
    - type: nauc_precision_at_10_std
      value: 9.268521380662948
    - type: nauc_precision_at_1_diff1
      value: 49.1101047164422
    - type: nauc_precision_at_1_max
      value: 37.933671986494026
    - type: nauc_precision_at_1_std
      value: -3.7731587131539976
    - type: nauc_precision_at_20_diff1
      value: 13.657560976362785
    - type: nauc_precision_at_20_max
      value: 33.87541496378981
    - type: nauc_precision_at_20_std
      value: 12.548073724501604
    - type: nauc_precision_at_3_diff1
      value: 31.86603948675504
    - type: nauc_precision_at_3_max
      value: 36.7937804867161
    - type: nauc_precision_at_3_std
      value: 1.3747787278458556
    - type: nauc_precision_at_5_diff1
      value: 26.464128564884287
    - type: nauc_precision_at_5_max
      value: 38.421403615633615
    - type: nauc_precision_at_5_std
      value: 6.849484842483432
    - type: nauc_recall_at_1000_diff1
      value: 18.749722864106687
    - type: nauc_recall_at_1000_max
      value: 43.23340103124563
    - type: nauc_recall_at_1000_std
      value: 40.71445800815644
    - type: nauc_recall_at_100_diff1
      value: 25.75477193308326
    - type: nauc_recall_at_100_max
      value: 38.95166149979008
    - type: nauc_recall_at_100_std
      value: 20.086723446846307
    - type: nauc_recall_at_10_diff1
      value: 34.9465684232037
    - type: nauc_recall_at_10_max
      value: 36.310367249051446
    - type: nauc_recall_at_10_std
      value: 5.334139441477833
    - type: nauc_recall_at_1_diff1
      value: 51.61094035660931
    - type: nauc_recall_at_1_max
      value: 35.24232228126847
    - type: nauc_recall_at_1_std
      value: -4.805963422515798
    - type: nauc_recall_at_20_diff1
      value: 32.74344985990636
    - type: nauc_recall_at_20_max
      value: 38.70262442532749
    - type: nauc_recall_at_20_std
      value: 9.903515883710332
    - type: nauc_recall_at_3_diff1
      value: 38.44351038745494
    - type: nauc_recall_at_3_max
      value: 33.58936306504043
    - type: nauc_recall_at_3_std
      value: -1.4980811551146116
    - type: nauc_recall_at_5_diff1
      value: 35.90101189825282
    - type: nauc_recall_at_5_max
      value: 35.662369181706204
    - type: nauc_recall_at_5_std
      value: 3.0145054767330115
    - type: ndcg_at_1
      value: 27.519
    - type: ndcg_at_10
      value: 37.25
    - type: ndcg_at_100
      value: 42.848000000000006
    - type: ndcg_at_1000
      value: 45.254
    - type: ndcg_at_20
      value: 39.277
    - type: ndcg_at_3
      value: 32.399
    - type: ndcg_at_5
      value: 34.524
    - type: precision_at_1
      value: 27.519
    - type: precision_at_10
      value: 6.334
    - type: precision_at_100
      value: 1.026
    - type: precision_at_1000
      value: 0.134
    - type: precision_at_20
      value: 3.759
    - type: precision_at_3
      value: 14.677000000000001
    - type: precision_at_5
      value: 10.317
    - type: recall_at_1
      value: 23.52
    - type: recall_at_10
      value: 49.184
    - type: recall_at_100
      value: 73.733
    - type: recall_at_1000
      value: 90.77
    - type: recall_at_20
      value: 56.298
    - type: recall_at_3
      value: 35.973
    - type: recall_at_5
      value: 41.374
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWebmastersRetrieval (default)
      revision: 160c094312a0e1facb97e55eeddb698c0abe3571
      split: test
      type: mteb/cqadupstack-webmasters
    metrics:
    - type: main_score
      value: 36.565
    - type: map_at_1
      value: 23.105999999999998
    - type: map_at_10
      value: 31.290000000000003
    - type: map_at_100
      value: 32.84
    - type: map_at_1000
      value: 33.056999999999995
    - type: map_at_20
      value: 32.053
    - type: map_at_3
      value: 28.524
    - type: map_at_5
      value: 30.059
    - type: mrr_at_1
      value: 27.27272727272727
    - type: mrr_at_10
      value: 35.2733860342556
    - type: mrr_at_100
      value: 36.3053638836631
    - type: mrr_at_1000
      value: 36.37032482519805
    - type: mrr_at_20
      value: 35.859048151622396
    - type: mrr_at_3
      value: 32.83926218708829
    - type: mrr_at_5
      value: 34.12384716732543
    - type: nauc_map_at_1000_diff1
      value: 39.76272068657792
    - type: nauc_map_at_1000_max
      value: 29.790280297209893
    - type: nauc_map_at_1000_std
      value: 10.757488325628422
    - type: nauc_map_at_100_diff1
      value: 39.81480347795618
    - type: nauc_map_at_100_max
      value: 29.922166651619236
    - type: nauc_map_at_100_std
      value: 10.65010277811946
    - type: nauc_map_at_10_diff1
      value: 39.55904622384973
    - type: nauc_map_at_10_max
      value: 29.4537747039685
    - type: nauc_map_at_10_std
      value: 9.600423622583662
    - type: nauc_map_at_1_diff1
      value: 46.2974028098431
    - type: nauc_map_at_1_max
      value: 28.426406901170203
    - type: nauc_map_at_1_std
      value: 2.298735191126003
    - type: nauc_map_at_20_diff1
      value: 39.3449497565094
    - type: nauc_map_at_20_max
      value: 29.80594598624846
    - type: nauc_map_at_20_std
      value: 10.131168100104727
    - type: nauc_map_at_3_diff1
      value: 41.76837093706344
    - type: nauc_map_at_3_max
      value: 29.663230640722325
    - type: nauc_map_at_3_std
      value: 8.357883325471708
    - type: nauc_map_at_5_diff1
      value: 40.001875443538545
    - type: nauc_map_at_5_max
      value: 29.427859045507148
    - type: nauc_map_at_5_std
      value: 8.398905009560293
    - type: nauc_mrr_at_1000_diff1
      value: 40.471195736412206
    - type: nauc_mrr_at_1000_max
      value: 30.816676948801714
    - type: nauc_mrr_at_1000_std
      value: 11.159711491734067
    - type: nauc_mrr_at_100_diff1
      value: 40.47871261866228
    - type: nauc_mrr_at_100_max
      value: 30.821157171181696
    - type: nauc_mrr_at_100_std
      value: 11.178279050139082
    - type: nauc_mrr_at_10_diff1
      value: 40.43627989797811
    - type: nauc_mrr_at_10_max
      value: 30.68845552208875
    - type: nauc_mrr_at_10_std
      value: 11.082356764494767
    - type: nauc_mrr_at_1_diff1
      value: 45.50910903294914
    - type: nauc_mrr_at_1_max
      value: 31.3076070063755
    - type: nauc_mrr_at_1_std
      value: 5.37768597927747
    - type: nauc_mrr_at_20_diff1
      value: 40.145413037287746
    - type: nauc_mrr_at_20_max
      value: 30.78817829326666
    - type: nauc_mrr_at_20_std
      value: 11.135265444724569
    - type: nauc_mrr_at_3_diff1
      value: 41.67907201095954
    - type: nauc_mrr_at_3_max
      value: 30.935486674293628
    - type: nauc_mrr_at_3_std
      value: 9.999676547554822
    - type: nauc_mrr_at_5_diff1
      value: 40.63061020793853
    - type: nauc_mrr_at_5_max
      value: 30.65935831056293
    - type: nauc_mrr_at_5_std
      value: 10.253570942971265
    - type: nauc_ndcg_at_1000_diff1
      value: 38.31679453625091
    - type: nauc_ndcg_at_1000_max
      value: 30.42490674886122
    - type: nauc_ndcg_at_1000_std
      value: 14.214535852825216
    - type: nauc_ndcg_at_100_diff1
      value: 38.25066725250533
    - type: nauc_ndcg_at_100_max
      value: 30.44191906381211
    - type: nauc_ndcg_at_100_std
      value: 14.901162385978845
    - type: nauc_ndcg_at_10_diff1
      value: 37.69901106502627
    - type: nauc_ndcg_at_10_max
      value: 29.64235402905151
    - type: nauc_ndcg_at_10_std
      value: 13.16074821157373
    - type: nauc_ndcg_at_1_diff1
      value: 45.50910903294914
    - type: nauc_ndcg_at_1_max
      value: 31.3076070063755
    - type: nauc_ndcg_at_1_std
      value: 5.37768597927747
    - type: nauc_ndcg_at_20_diff1
      value: 36.28568865631326
    - type: nauc_ndcg_at_20_max
      value: 30.050385172275394
    - type: nauc_ndcg_at_20_std
      value: 13.754810821651981
    - type: nauc_ndcg_at_3_diff1
      value: 41.651315048123216
    - type: nauc_ndcg_at_3_max
      value: 31.443490740638612
    - type: nauc_ndcg_at_3_std
      value: 11.384365369343216
    - type: nauc_ndcg_at_5_diff1
      value: 39.128045954408535
    - type: nauc_ndcg_at_5_max
      value: 30.294182805626523
    - type: nauc_ndcg_at_5_std
      value: 11.455518736657039
    - type: nauc_precision_at_1000_diff1
      value: -2.5588471818616236
    - type: nauc_precision_at_1000_max
      value: -8.40564077817957
    - type: nauc_precision_at_1000_std
      value: 17.178789287436377
    - type: nauc_precision_at_100_diff1
      value: 10.20179378901254
    - type: nauc_precision_at_100_max
      value: 6.9826053319142485
    - type: nauc_precision_at_100_std
      value: 24.31302168417932
    - type: nauc_precision_at_10_diff1
      value: 21.64226817804198
    - type: nauc_precision_at_10_max
      value: 25.95797802850366
    - type: nauc_precision_at_10_std
      value: 23.463222960924217
    - type: nauc_precision_at_1_diff1
      value: 45.50910903294914
    - type: nauc_precision_at_1_max
      value: 31.3076070063755
    - type: nauc_precision_at_1_std
      value: 5.37768597927747
    - type: nauc_precision_at_20_diff1
      value: 16.188528114667015
    - type: nauc_precision_at_20_max
      value: 22.711717515357932
    - type: nauc_precision_at_20_std
      value: 25.92900601366098
    - type: nauc_precision_at_3_diff1
      value: 33.38289089598491
    - type: nauc_precision_at_3_max
      value: 33.0613762828467
    - type: nauc_precision_at_3_std
      value: 18.26750139224793
    - type: nauc_precision_at_5_diff1
      value: 25.299183198738884
    - type: nauc_precision_at_5_max
      value: 27.95155532864501
    - type: nauc_precision_at_5_std
      value: 17.69547733910105
    - type: nauc_recall_at_1000_diff1
      value: 22.127156020725522
    - type: nauc_recall_at_1000_max
      value: 36.32198236414703
    - type: nauc_recall_at_1000_std
      value: 46.0024764987062
    - type: nauc_recall_at_100_diff1
      value: 30.41962941522361
    - type: nauc_recall_at_100_max
      value: 29.658332453198888
    - type: nauc_recall_at_100_std
      value: 32.76645418495392
    - type: nauc_recall_at_10_diff1
      value: 27.94562925698465
    - type: nauc_recall_at_10_max
      value: 26.023394389331383
    - type: nauc_recall_at_10_std
      value: 18.394527204627348
    - type: nauc_recall_at_1_diff1
      value: 46.2974028098431
    - type: nauc_recall_at_1_max
      value: 28.426406901170203
    - type: nauc_recall_at_1_std
      value: 2.298735191126003
    - type: nauc_recall_at_20_diff1
      value: 22.776623977857145
    - type: nauc_recall_at_20_max
      value: 27.21001817636621
    - type: nauc_recall_at_20_std
      value: 21.282932443508354
    - type: nauc_recall_at_3_diff1
      value: 36.884749050164295
    - type: nauc_recall_at_3_max
      value: 28.465498877250873
    - type: nauc_recall_at_3_std
      value: 12.711247426442371
    - type: nauc_recall_at_5_diff1
      value: 31.283845178999254
    - type: nauc_recall_at_5_max
      value: 27.061848538009027
    - type: nauc_recall_at_5_std
      value: 13.469960961026883
    - type: ndcg_at_1
      value: 27.272999999999996
    - type: ndcg_at_10
      value: 36.565
    - type: ndcg_at_100
      value: 42.9
    - type: ndcg_at_1000
      value: 45.608
    - type: ndcg_at_20
      value: 38.751000000000005
    - type: ndcg_at_3
      value: 31.939
    - type: ndcg_at_5
      value: 34.101
    - type: precision_at_1
      value: 27.272999999999996
    - type: precision_at_10
      value: 6.917
    - type: precision_at_100
      value: 1.455
    - type: precision_at_1000
      value: 0.232
    - type: precision_at_20
      value: 4.447
    - type: precision_at_3
      value: 14.69
    - type: precision_at_5
      value: 10.870000000000001
    - type: recall_at_1
      value: 23.105999999999998
    - type: recall_at_10
      value: 46.894999999999996
    - type: recall_at_100
      value: 75.594
    - type: recall_at_1000
      value: 92.732
    - type: recall_at_20
      value: 55.257999999999996
    - type: recall_at_3
      value: 33.934999999999995
    - type: recall_at_5
      value: 39.222
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CQADupstackWordpressRetrieval (default)
      revision: 4ffe81d471b1924886b33c7567bfb200e9eec5c4
      split: test
      type: mteb/cqadupstack-wordpress
    metrics:
    - type: main_score
      value: 29.567
    - type: map_at_1
      value: 17.904999999999998
    - type: map_at_10
      value: 24.938
    - type: map_at_100
      value: 25.909
    - type: map_at_1000
      value: 26.027
    - type: map_at_20
      value: 25.451
    - type: map_at_3
      value: 22.259999999999998
    - type: map_at_5
      value: 23.834
    - type: mrr_at_1
      value: 19.223659889094268
    - type: mrr_at_10
      value: 26.62845113399643
    - type: mrr_at_100
      value: 27.499845907183552
    - type: mrr_at_1000
      value: 27.593472908486984
    - type: mrr_at_20
      value: 27.123214255946344
    - type: mrr_at_3
      value: 23.813924830560687
    - type: mrr_at_5
      value: 25.551447935921136
    - type: nauc_map_at_1000_diff1
      value: 38.89606010868926
    - type: nauc_map_at_1000_max
      value: 31.538856803290884
    - type: nauc_map_at_1000_std
      value: -1.305075788649935
    - type: nauc_map_at_100_diff1
      value: 38.82639909571271
    - type: nauc_map_at_100_max
      value: 31.497525225584177
    - type: nauc_map_at_100_std
      value: -1.309646997856667
    - type: nauc_map_at_10_diff1
      value: 39.29347922607974
    - type: nauc_map_at_10_max
      value: 31.79078705023462
    - type: nauc_map_at_10_std
      value: -1.876636004896723
    - type: nauc_map_at_1_diff1
      value: 48.21195607823574
    - type: nauc_map_at_1_max
      value: 32.939940404152814
    - type: nauc_map_at_1_std
      value: -2.598175888025344
    - type: nauc_map_at_20_diff1
      value: 38.97329850846901
    - type: nauc_map_at_20_max
      value: 31.517768894234088
    - type: nauc_map_at_20_std
      value: -1.7582312182435884
    - type: nauc_map_at_3_diff1
      value: 41.14141970209535
    - type: nauc_map_at_3_max
      value: 32.30972428641846
    - type: nauc_map_at_3_std
      value: -1.8883058706632543
    - type: nauc_map_at_5_diff1
      value: 40.09562382270429
    - type: nauc_map_at_5_max
      value: 31.933391253205627
    - type: nauc_map_at_5_std
      value: -2.100889221871347
    - type: nauc_mrr_at_1000_diff1
      value: 39.01910001476905
    - type: nauc_mrr_at_1000_max
      value: 33.08207505682323
    - type: nauc_mrr_at_1000_std
      value: -0.6237855979344884
    - type: nauc_mrr_at_100_diff1
      value: 38.93803750185852
    - type: nauc_mrr_at_100_max
      value: 33.048836543873975
    - type: nauc_mrr_at_100_std
      value: -0.6062208268461757
    - type: nauc_mrr_at_10_diff1
      value: 39.270583896754644
    - type: nauc_mrr_at_10_max
      value: 33.24795051204245
    - type: nauc_mrr_at_10_std
      value: -0.9725090570441313
    - type: nauc_mrr_at_1_diff1
      value: 47.999638413846505
    - type: nauc_mrr_at_1_max
      value: 35.36138863519551
    - type: nauc_mrr_at_1_std
      value: -1.880235814636017
    - type: nauc_mrr_at_20_diff1
      value: 39.021750324405396
    - type: nauc_mrr_at_20_max
      value: 33.03808863518709
    - type: nauc_mrr_at_20_std
      value: -0.9591151055995247
    - type: nauc_mrr_at_3_diff1
      value: 41.80927533235213
    - type: nauc_mrr_at_3_max
      value: 34.29227659304729
    - type: nauc_mrr_at_3_std
      value: -1.1645238886922333
    - type: nauc_mrr_at_5_diff1
      value: 40.090198362725445
    - type: nauc_mrr_at_5_max
      value: 33.38020362155669
    - type: nauc_mrr_at_5_std
      value: -0.9765029348699578
    - type: nauc_ndcg_at_1000_diff1
      value: 35.50789376303437
    - type: nauc_ndcg_at_1000_max
      value: 31.615759544374693
    - type: nauc_ndcg_at_1000_std
      value: 2.1204304391621855
    - type: nauc_ndcg_at_100_diff1
      value: 33.57315272127493
    - type: nauc_ndcg_at_100_max
      value: 30.086482858827026
    - type: nauc_ndcg_at_100_std
      value: 2.0440427140431576
    - type: nauc_ndcg_at_10_diff1
      value: 35.34492455018914
    - type: nauc_ndcg_at_10_max
      value: 31.02089117001684
    - type: nauc_ndcg_at_10_std
      value: -1.1048933497920645
    - type: nauc_ndcg_at_1_diff1
      value: 47.999638413846505
    - type: nauc_ndcg_at_1_max
      value: 35.36138863519551
    - type: nauc_ndcg_at_1_std
      value: -1.880235814636017
    - type: nauc_ndcg_at_20_diff1
      value: 34.26215274432466
    - type: nauc_ndcg_at_20_max
      value: 30.20225190792415
    - type: nauc_ndcg_at_20_std
      value: -0.7509261018709115
    - type: nauc_ndcg_at_3_diff1
      value: 39.389519747059026
    - type: nauc_ndcg_at_3_max
      value: 32.63411653129123
    - type: nauc_ndcg_at_3_std
      value: -0.993678872804903
    - type: nauc_ndcg_at_5_diff1
      value: 37.188814736325924
    - type: nauc_ndcg_at_5_max
      value: 31.495832182127202
    - type: nauc_ndcg_at_5_std
      value: -1.2778445014948332
    - type: nauc_precision_at_1000_diff1
      value: -9.97486529251133
    - type: nauc_precision_at_1000_max
      value: -0.7480260820564806
    - type: nauc_precision_at_1000_std
      value: 11.340009034047164
    - type: nauc_precision_at_100_diff1
      value: 3.9801856363648436
    - type: nauc_precision_at_100_max
      value: 13.379133650650818
    - type: nauc_precision_at_100_std
      value: 19.09971792064424
    - type: nauc_precision_at_10_diff1
      value: 21.999340108469816
    - type: nauc_precision_at_10_max
      value: 27.787090972478723
    - type: nauc_precision_at_10_std
      value: 3.666717149158269
    - type: nauc_precision_at_1_diff1
      value: 47.999638413846505
    - type: nauc_precision_at_1_max
      value: 35.36138863519551
    - type: nauc_precision_at_1_std
      value: -1.880235814636017
    - type: nauc_precision_at_20_diff1
      value: 16.517223912074233
    - type: nauc_precision_at_20_max
      value: 23.937166410814513
    - type: nauc_precision_at_20_std
      value: 8.146414485970688
    - type: nauc_precision_at_3_diff1
      value: 32.928185060716544
    - type: nauc_precision_at_3_max
      value: 33.32909830966484
    - type: nauc_precision_at_3_std
      value: 1.7607783669388026
    - type: nauc_precision_at_5_diff1
      value: 27.617896173358826
    - type: nauc_precision_at_5_max
      value: 31.07062829318418
    - type: nauc_precision_at_5_std
      value: 2.5159680374410023
    - type: nauc_recall_at_1000_diff1
      value: 25.828881504446947
    - type: nauc_recall_at_1000_max
      value: 41.72839366554471
    - type: nauc_recall_at_1000_std
      value: 32.88040232676994
    - type: nauc_recall_at_100_diff1
      value: 13.845109468247148
    - type: nauc_recall_at_100_max
      value: 21.81619945923323
    - type: nauc_recall_at_100_std
      value: 15.182307774891207
    - type: nauc_recall_at_10_diff1
      value: 24.07889524419303
    - type: nauc_recall_at_10_max
      value: 26.924752181722017
    - type: nauc_recall_at_10_std
      value: -0.011546334534046606
    - type: nauc_recall_at_1_diff1
      value: 48.21195607823574
    - type: nauc_recall_at_1_max
      value: 32.939940404152814
    - type: nauc_recall_at_1_std
      value: -2.598175888025344
    - type: nauc_recall_at_20_diff1
      value: 19.964045605188886
    - type: nauc_recall_at_20_max
      value: 23.885666727839393
    - type: nauc_recall_at_20_std
      value: 0.42285441592789197
    - type: nauc_recall_at_3_diff1
      value: 33.929457814927375
    - type: nauc_recall_at_3_max
      value: 30.910764244335205
    - type: nauc_recall_at_3_std
      value: 0.3174639322018935
    - type: nauc_recall_at_5_diff1
      value: 29.092298121601694
    - type: nauc_recall_at_5_max
      value: 28.363390941448102
    - type: nauc_recall_at_5_std
      value: -0.2037623526882392
    - type: ndcg_at_1
      value: 19.224
    - type: ndcg_at_10
      value: 29.567
    - type: ndcg_at_100
      value: 34.521
    - type: ndcg_at_1000
      value: 37.525999999999996
    - type: ndcg_at_20
      value: 31.385999999999996
    - type: ndcg_at_3
      value: 24.104999999999997
    - type: ndcg_at_5
      value: 26.956000000000003
    - type: precision_at_1
      value: 19.224
    - type: precision_at_10
      value: 4.898000000000001
    - type: precision_at_100
      value: 0.8
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_20
      value: 2.8930000000000002
    - type: precision_at_3
      value: 10.228
    - type: precision_at_5
      value: 7.8
    - type: recall_at_1
      value: 17.904999999999998
    - type: recall_at_10
      value: 42.236000000000004
    - type: recall_at_100
      value: 65.31
    - type: recall_at_1000
      value: 87.725
    - type: recall_at_20
      value: 49.122
    - type: recall_at_3
      value: 27.659
    - type: recall_at_5
      value: 34.476
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ClimateFEVER (default)
      revision: 47f2ac6acb640fc46020b02a5b59fdda04d39380
      split: test
      type: mteb/climate-fever
    metrics:
    - type: main_score
      value: 26.737
    - type: map_at_1
      value: 11.047
    - type: map_at_10
      value: 19.031000000000002
    - type: map_at_100
      value: 20.811
    - type: map_at_1000
      value: 21.004
    - type: map_at_20
      value: 19.906
    - type: map_at_3
      value: 16.154
    - type: map_at_5
      value: 17.637
    - type: mrr_at_1
      value: 24.7557003257329
    - type: mrr_at_10
      value: 36.00248177446872
    - type: mrr_at_100
      value: 37.022765746266224
    - type: mrr_at_1000
      value: 37.06412282708337
    - type: mrr_at_20
      value: 36.613242481766875
    - type: mrr_at_3
      value: 32.99674267100971
    - type: mrr_at_5
      value: 34.77198697068397
    - type: nauc_map_at_1000_diff1
      value: 22.95284162051679
    - type: nauc_map_at_1000_max
      value: 41.05657553737428
    - type: nauc_map_at_1000_std
      value: 18.834903528536966
    - type: nauc_map_at_100_diff1
      value: 22.98481765525261
    - type: nauc_map_at_100_max
      value: 41.03975029590201
    - type: nauc_map_at_100_std
      value: 18.771562130707093
    - type: nauc_map_at_10_diff1
      value: 23.13821422467576
    - type: nauc_map_at_10_max
      value: 39.82209459044267
    - type: nauc_map_at_10_std
      value: 16.550430053938996
    - type: nauc_map_at_1_diff1
      value: 27.763657551345815
    - type: nauc_map_at_1_max
      value: 36.12475370802807
    - type: nauc_map_at_1_std
      value: 8.813087776045409
    - type: nauc_map_at_20_diff1
      value: 22.989816492876976
    - type: nauc_map_at_20_max
      value: 40.47306627293731
    - type: nauc_map_at_20_std
      value: 17.922541923299242
    - type: nauc_map_at_3_diff1
      value: 25.177638524660594
    - type: nauc_map_at_3_max
      value: 38.39188053307798
    - type: nauc_map_at_3_std
      value: 12.43002831643714
    - type: nauc_map_at_5_diff1
      value: 24.11240452332388
    - type: nauc_map_at_5_max
      value: 39.78597831033908
    - type: nauc_map_at_5_std
      value: 15.348832909388102
    - type: nauc_mrr_at_1000_diff1
      value: 22.953724268315007
    - type: nauc_mrr_at_1000_max
      value: 36.75873655295118
    - type: nauc_mrr_at_1000_std
      value: 18.86900175143143
    - type: nauc_mrr_at_100_diff1
      value: 22.94708169148642
    - type: nauc_mrr_at_100_max
      value: 36.77692171237133
    - type: nauc_mrr_at_100_std
      value: 18.90049139812642
    - type: nauc_mrr_at_10_diff1
      value: 22.961392194546697
    - type: nauc_mrr_at_10_max
      value: 36.5664392762182
    - type: nauc_mrr_at_10_std
      value: 18.61258791439757
    - type: nauc_mrr_at_1_diff1
      value: 25.264729979176337
    - type: nauc_mrr_at_1_max
      value: 32.00533151772989
    - type: nauc_mrr_at_1_std
      value: 11.28963976428763
    - type: nauc_mrr_at_20_diff1
      value: 22.89202299597813
    - type: nauc_mrr_at_20_max
      value: 36.81591748654397
    - type: nauc_mrr_at_20_std
      value: 18.957871797322213
    - type: nauc_mrr_at_3_diff1
      value: 23.32679875268354
    - type: nauc_mrr_at_3_max
      value: 35.77247598730184
    - type: nauc_mrr_at_3_std
      value: 16.998072713674137
    - type: nauc_mrr_at_5_diff1
      value: 22.940494982850357
    - type: nauc_mrr_at_5_max
      value: 36.4761572989835
    - type: nauc_mrr_at_5_std
      value: 18.247716522394114
    - type: nauc_ndcg_at_1000_diff1
      value: 20.33208895418013
    - type: nauc_ndcg_at_1000_max
      value: 43.43624293116895
    - type: nauc_ndcg_at_1000_std
      value: 26.692682553388043
    - type: nauc_ndcg_at_100_diff1
      value: 20.683371851614915
    - type: nauc_ndcg_at_100_max
      value: 43.23955154318779
    - type: nauc_ndcg_at_100_std
      value: 26.255509612217846
    - type: nauc_ndcg_at_10_diff1
      value: 21.4076909300414
    - type: nauc_ndcg_at_10_max
      value: 39.940378122809996
    - type: nauc_ndcg_at_10_std
      value: 20.34199980826332
    - type: nauc_ndcg_at_1_diff1
      value: 25.264729979176337
    - type: nauc_ndcg_at_1_max
      value: 32.00533151772989
    - type: nauc_ndcg_at_1_std
      value: 11.28963976428763
    - type: nauc_ndcg_at_20_diff1
      value: 21.06028073012518
    - type: nauc_ndcg_at_20_max
      value: 41.39323714162508
    - type: nauc_ndcg_at_20_std
      value: 23.294473172219288
    - type: nauc_ndcg_at_3_diff1
      value: 23.795439983732766
    - type: nauc_ndcg_at_3_max
      value: 37.670223262411994
    - type: nauc_ndcg_at_3_std
      value: 14.988047358058045
    - type: nauc_ndcg_at_5_diff1
      value: 22.549509904412304
    - type: nauc_ndcg_at_5_max
      value: 39.97171597626144
    - type: nauc_ndcg_at_5_std
      value: 18.522092622834307
    - type: nauc_precision_at_1000_diff1
      value: -2.966526326664724
    - type: nauc_precision_at_1000_max
      value: 19.35956305205282
    - type: nauc_precision_at_1000_std
      value: 29.208694771321802
    - type: nauc_precision_at_100_diff1
      value: 3.89594831569403
    - type: nauc_precision_at_100_max
      value: 30.93107729730319
    - type: nauc_precision_at_100_std
      value: 35.65762513251467
    - type: nauc_precision_at_10_diff1
      value: 11.55435573260231
    - type: nauc_precision_at_10_max
      value: 33.6858401099601
    - type: nauc_precision_at_10_std
      value: 27.844293535879206
    - type: nauc_precision_at_1_diff1
      value: 25.264729979176337
    - type: nauc_precision_at_1_max
      value: 32.00533151772989
    - type: nauc_precision_at_1_std
      value: 11.28963976428763
    - type: nauc_precision_at_20_diff1
      value: 9.19449929503659
    - type: nauc_precision_at_20_max
      value: 34.04253984479287
    - type: nauc_precision_at_20_std
      value: 33.26324613378763
    - type: nauc_precision_at_3_diff1
      value: 19.686045361727484
    - type: nauc_precision_at_3_max
      value: 36.03726542607104
    - type: nauc_precision_at_3_std
      value: 19.73290312758754
    - type: nauc_precision_at_5_diff1
      value: 15.192260787856585
    - type: nauc_precision_at_5_max
      value: 37.448062698115095
    - type: nauc_precision_at_5_std
      value: 26.272485409517117
    - type: nauc_recall_at_1000_diff1
      value: 3.8258182870161943
    - type: nauc_recall_at_1000_max
      value: 43.71178689615702
    - type: nauc_recall_at_1000_std
      value: 45.551384524629576
    - type: nauc_recall_at_100_diff1
      value: 9.602166248337264
    - type: nauc_recall_at_100_max
      value: 40.222401344352136
    - type: nauc_recall_at_100_std
      value: 36.19019924878991
    - type: nauc_recall_at_10_diff1
      value: 14.698199205269786
    - type: nauc_recall_at_10_max
      value: 35.961298718387326
    - type: nauc_recall_at_10_std
      value: 21.970115975467966
    - type: nauc_recall_at_1_diff1
      value: 27.763657551345815
    - type: nauc_recall_at_1_max
      value: 36.12475370802807
    - type: nauc_recall_at_1_std
      value: 8.813087776045409
    - type: nauc_recall_at_20_diff1
      value: 13.109375978076127
    - type: nauc_recall_at_20_max
      value: 37.72229474207071
    - type: nauc_recall_at_20_std
      value: 27.908697340918625
    - type: nauc_recall_at_3_diff1
      value: 20.97044679859558
    - type: nauc_recall_at_3_max
      value: 37.050460347469986
    - type: nauc_recall_at_3_std
      value: 14.204226826731455
    - type: nauc_recall_at_5_diff1
      value: 18.139967176831718
    - type: nauc_recall_at_5_max
      value: 38.69687411453869
    - type: nauc_recall_at_5_std
      value: 19.825425230717368
    - type: ndcg_at_1
      value: 24.756
    - type: ndcg_at_10
      value: 26.737
    - type: ndcg_at_100
      value: 34.097
    - type: ndcg_at_1000
      value: 37.653999999999996
    - type: ndcg_at_20
      value: 29.341
    - type: ndcg_at_3
      value: 22.209
    - type: ndcg_at_5
      value: 23.726
    - type: precision_at_1
      value: 24.756
    - type: precision_at_10
      value: 8.28
    - type: precision_at_100
      value: 1.6199999999999999
    - type: precision_at_1000
      value: 0.22799999999999998
    - type: precision_at_20
      value: 5.261
    - type: precision_at_3
      value: 16.678
    - type: precision_at_5
      value: 12.598999999999998
    - type: recall_at_1
      value: 11.047
    - type: recall_at_10
      value: 31.939
    - type: recall_at_100
      value: 57.66
    - type: recall_at_1000
      value: 77.676
    - type: recall_at_20
      value: 39.375
    - type: recall_at_3
      value: 20.534
    - type: recall_at_5
      value: 25.113000000000003
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB DBPedia (default)
      revision: c0f706b76e590d620bd6618b3ca8efdd34e2d659
      split: test
      type: mteb/dbpedia
    metrics:
    - type: main_score
      value: 38.553
    - type: map_at_1
      value: 8.427
    - type: map_at_10
      value: 17.947
    - type: map_at_100
      value: 24.859
    - type: map_at_1000
      value: 26.284999999999997
    - type: map_at_20
      value: 20.529
    - type: map_at_3
      value: 13.032
    - type: map_at_5
      value: 15.087
    - type: mrr_at_1
      value: 63.74999999999999
    - type: mrr_at_10
      value: 72.26726190476191
    - type: mrr_at_100
      value: 72.60264087536868
    - type: mrr_at_1000
      value: 72.6117769251391
    - type: mrr_at_20
      value: 72.48660991785995
    - type: mrr_at_3
      value: 70.29166666666669
    - type: mrr_at_5
      value: 71.72916666666667
    - type: nauc_map_at_1000_diff1
      value: 16.885215876440295
    - type: nauc_map_at_1000_max
      value: 24.251410480294357
    - type: nauc_map_at_1000_std
      value: 30.442486178306797
    - type: nauc_map_at_100_diff1
      value: 17.77376546461243
    - type: nauc_map_at_100_max
      value: 22.397423178877666
    - type: nauc_map_at_100_std
      value: 27.80993039204801
    - type: nauc_map_at_10_diff1
      value: 23.34667275277926
    - type: nauc_map_at_10_max
      value: 10.594143100766155
    - type: nauc_map_at_10_std
      value: 10.585594861156142
    - type: nauc_map_at_1_diff1
      value: 41.31179058216469
    - type: nauc_map_at_1_max
      value: 2.7789106998022595
    - type: nauc_map_at_1_std
      value: -5.629361745337226
    - type: nauc_map_at_20_diff1
      value: 21.171735707940826
    - type: nauc_map_at_20_max
      value: 14.91112453141777
    - type: nauc_map_at_20_std
      value: 16.852537320237083
    - type: nauc_map_at_3_diff1
      value: 27.764297506590797
    - type: nauc_map_at_3_max
      value: 3.350829180020233
    - type: nauc_map_at_3_std
      value: 0.6093126325885707
    - type: nauc_map_at_5_diff1
      value: 24.65278591199583
    - type: nauc_map_at_5_max
      value: 4.879335188280108
    - type: nauc_map_at_5_std
      value: 3.7215226421650267
    - type: nauc_mrr_at_1000_diff1
      value: 46.334418500628054
    - type: nauc_mrr_at_1000_max
      value: 61.28184640697816
    - type: nauc_mrr_at_1000_std
      value: 39.24492154930731
    - type: nauc_mrr_at_100_diff1
      value: 46.330131722627435
    - type: nauc_mrr_at_100_max
      value: 61.28413429173713
    - type: nauc_mrr_at_100_std
      value: 39.24030745947179
    - type: nauc_mrr_at_10_diff1
      value: 46.31370888820881
    - type: nauc_mrr_at_10_max
      value: 61.3280839283407
    - type: nauc_mrr_at_10_std
      value: 39.4561235573134
    - type: nauc_mrr_at_1_diff1
      value: 49.415410285441865
    - type: nauc_mrr_at_1_max
      value: 58.67786981308228
    - type: nauc_mrr_at_1_std
      value: 34.349164729952484
    - type: nauc_mrr_at_20_diff1
      value: 46.44394246082444
    - type: nauc_mrr_at_20_max
      value: 61.349381938107015
    - type: nauc_mrr_at_20_std
      value: 39.329379002565865
    - type: nauc_mrr_at_3_diff1
      value: 46.5466532654621
    - type: nauc_mrr_at_3_max
      value: 60.738204480647994
    - type: nauc_mrr_at_3_std
      value: 39.75962812429745
    - type: nauc_mrr_at_5_diff1
      value: 45.573755866755
    - type: nauc_mrr_at_5_max
      value: 61.37737255344052
    - type: nauc_mrr_at_5_std
      value: 39.48646682460037
    - type: nauc_ndcg_at_1000_diff1
      value: 16.736755471969026
    - type: nauc_ndcg_at_1000_max
      value: 38.94665722868098
    - type: nauc_ndcg_at_1000_std
      value: 41.67473161838855
    - type: nauc_ndcg_at_100_diff1
      value: 18.410722578049988
    - type: nauc_ndcg_at_100_max
      value: 32.48401439716438
    - type: nauc_ndcg_at_100_std
      value: 34.71840405905395
    - type: nauc_ndcg_at_10_diff1
      value: 23.046713516949357
    - type: nauc_ndcg_at_10_max
      value: 36.41251437514339
    - type: nauc_ndcg_at_10_std
      value: 33.85064850271241
    - type: nauc_ndcg_at_1_diff1
      value: 44.98121223766516
    - type: nauc_ndcg_at_1_max
      value: 49.651287744543346
    - type: nauc_ndcg_at_1_std
      value: 29.780916188076894
    - type: nauc_ndcg_at_20_diff1
      value: 22.22814399555328
    - type: nauc_ndcg_at_20_max
      value: 32.27357130353916
    - type: nauc_ndcg_at_20_std
      value: 31.075769289452598
    - type: nauc_ndcg_at_3_diff1
      value: 25.535588030138996
    - type: nauc_ndcg_at_3_max
      value: 39.83735223382875
    - type: nauc_ndcg_at_3_std
      value: 31.56662105223355
    - type: nauc_ndcg_at_5_diff1
      value: 24.200992920951915
    - type: nauc_ndcg_at_5_max
      value: 38.983334609042664
    - type: nauc_ndcg_at_5_std
      value: 32.815778747524064
    - type: nauc_precision_at_1000_diff1
      value: -13.042988259065188
    - type: nauc_precision_at_1000_max
      value: 14.592773793416065
    - type: nauc_precision_at_1000_std
      value: 18.54030566512939
    - type: nauc_precision_at_100_diff1
      value: -8.839880525325949
    - type: nauc_precision_at_100_max
      value: 35.27222519062242
    - type: nauc_precision_at_100_std
      value: 42.48049287957863
    - type: nauc_precision_at_10_diff1
      value: -0.30622683334044837
    - type: nauc_precision_at_10_max
      value: 43.863332528297384
    - type: nauc_precision_at_10_std
      value: 45.99630936149964
    - type: nauc_precision_at_1_diff1
      value: 49.415410285441865
    - type: nauc_precision_at_1_max
      value: 58.67786981308228
    - type: nauc_precision_at_1_std
      value: 34.349164729952484
    - type: nauc_precision_at_20_diff1
      value: -3.0634928461658135
    - type: nauc_precision_at_20_max
      value: 40.58489408271218
    - type: nauc_precision_at_20_std
      value: 44.78991176526987
    - type: nauc_precision_at_3_diff1
      value: 7.030183506370981
    - type: nauc_precision_at_3_max
      value: 39.4877838164423
    - type: nauc_precision_at_3_std
      value: 36.35500887750183
    - type: nauc_precision_at_5_diff1
      value: 2.7154599702814086
    - type: nauc_precision_at_5_max
      value: 43.340435401319304
    - type: nauc_precision_at_5_std
      value: 42.78969754624864
    - type: nauc_recall_at_1000_diff1
      value: 2.0440148038106543
    - type: nauc_recall_at_1000_max
      value: 27.80788064711282
    - type: nauc_recall_at_1000_std
      value: 43.56435465984963
    - type: nauc_recall_at_100_diff1
      value: 7.249759444328031
    - type: nauc_recall_at_100_max
      value: 18.51578835482464
    - type: nauc_recall_at_100_std
      value: 28.176910509170515
    - type: nauc_recall_at_10_diff1
      value: 18.095470021097675
    - type: nauc_recall_at_10_max
      value: 4.0380084324985415
    - type: nauc_recall_at_10_std
      value: 6.188126602282033
    - type: nauc_recall_at_1_diff1
      value: 41.31179058216469
    - type: nauc_recall_at_1_max
      value: 2.7789106998022595
    - type: nauc_recall_at_1_std
      value: -5.629361745337226
    - type: nauc_recall_at_20_diff1
      value: 15.124098206152278
    - type: nauc_recall_at_20_max
      value: 8.168146286216665
    - type: nauc_recall_at_20_std
      value: 12.163295762335588
    - type: nauc_recall_at_3_diff1
      value: 23.242634056765034
    - type: nauc_recall_at_3_max
      value: -1.2044999492508157
    - type: nauc_recall_at_3_std
      value: -0.9756022011856826
    - type: nauc_recall_at_5_diff1
      value: 18.51030489728696
    - type: nauc_recall_at_5_max
      value: -1.02698451199236
    - type: nauc_recall_at_5_std
      value: 0.9103887215447328
    - type: ndcg_at_1
      value: 51.74999999999999
    - type: ndcg_at_10
      value: 38.553
    - type: ndcg_at_100
      value: 42.603
    - type: ndcg_at_1000
      value: 49.996
    - type: ndcg_at_20
      value: 37.624
    - type: ndcg_at_3
      value: 43.129
    - type: ndcg_at_5
      value: 40.286
    - type: precision_at_1
      value: 63.74999999999999
    - type: precision_at_10
      value: 30.8
    - type: precision_at_100
      value: 9.47
    - type: precision_at_1000
      value: 1.8350000000000002
    - type: precision_at_20
      value: 22.662
    - type: precision_at_3
      value: 46.666999999999994
    - type: precision_at_5
      value: 39.050000000000004
    - type: recall_at_1
      value: 8.427
    - type: recall_at_10
      value: 23.385
    - type: recall_at_100
      value: 48.498999999999995
    - type: recall_at_1000
      value: 72.161
    - type: recall_at_20
      value: 29.683999999999997
    - type: recall_at_3
      value: 14.401
    - type: recall_at_5
      value: 17.803
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB EmotionClassification (default)
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
      split: test
      type: mteb/emotion
    metrics:
    - type: accuracy
      value: 49.754999999999995
    - type: f1
      value: 43.36982442562564
    - type: f1_weighted
      value: 51.61952910603824
    - type: main_score
      value: 49.754999999999995
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB FEVER (default)
      revision: bea83ef9e8fb933d90a2f1d5515737465d613e12
      split: test
      type: mteb/fever
    metrics:
    - type: main_score
      value: 84.936
    - type: map_at_1
      value: 72.57400000000001
    - type: map_at_10
      value: 81.066
    - type: map_at_100
      value: 81.297
    - type: map_at_1000
      value: 81.312
    - type: map_at_20
      value: 81.207
    - type: map_at_3
      value: 79.986
    - type: map_at_5
      value: 80.69800000000001
    - type: mrr_at_1
      value: 78.38283828382838
    - type: mrr_at_10
      value: 85.85126965077451
    - type: mrr_at_100
      value: 85.94789108942497
    - type: mrr_at_1000
      value: 85.95083700548771
    - type: mrr_at_20
      value: 85.92198402529328
    - type: mrr_at_3
      value: 85.09850985098504
    - type: mrr_at_5
      value: 85.60856085608543
    - type: nauc_map_at_1000_diff1
      value: 50.66119889176923
    - type: nauc_map_at_1000_max
      value: 27.580944486960778
    - type: nauc_map_at_1000_std
      value: 2.476183923102915
    - type: nauc_map_at_100_diff1
      value: 50.62017790161358
    - type: nauc_map_at_100_max
      value: 27.56129936780716
    - type: nauc_map_at_100_std
      value: 2.4766366012578596
    - type: nauc_map_at_10_diff1
      value: 50.419141534275646
    - type: nauc_map_at_10_max
      value: 27.356650851579005
    - type: nauc_map_at_10_std
      value: 2.3350604474354455
    - type: nauc_map_at_1_diff1
      value: 54.29468230013946
    - type: nauc_map_at_1_max
      value: 22.58894354165319
    - type: nauc_map_at_1_std
      value: -2.7297280069759613
    - type: nauc_map_at_20_diff1
      value: 50.53772247796323
    - type: nauc_map_at_20_max
      value: 27.47288741660889
    - type: nauc_map_at_20_std
      value: 2.4731058048920134
    - type: nauc_map_at_3_diff1
      value: 50.44147113679276
    - type: nauc_map_at_3_max
      value: 26.61390529181397
    - type: nauc_map_at_3_std
      value: 0.7317631152076722
    - type: nauc_map_at_5_diff1
      value: 50.35927561260093
    - type: nauc_map_at_5_max
      value: 27.171327197638924
    - type: nauc_map_at_5_std
      value: 2.005685096668936
    - type: nauc_mrr_at_1000_diff1
      value: 66.66956741241363
    - type: nauc_mrr_at_1000_max
      value: 34.60696986415113
    - type: nauc_mrr_at_1000_std
      value: -0.664668306469195
    - type: nauc_mrr_at_100_diff1
      value: 66.66794471782865
    - type: nauc_mrr_at_100_max
      value: 34.61677889901239
    - type: nauc_mrr_at_100_std
      value: -0.656402933928221
    - type: nauc_mrr_at_10_diff1
      value: 66.68304426013808
    - type: nauc_mrr_at_10_max
      value: 34.73024103786049
    - type: nauc_mrr_at_10_std
      value: -0.6353888738825407
    - type: nauc_mrr_at_1_diff1
      value: 67.19771091736617
    - type: nauc_mrr_at_1_max
      value: 29.860207317348003
    - type: nauc_mrr_at_1_std
      value: -3.6568452043648385
    - type: nauc_mrr_at_20_diff1
      value: 66.68308645971901
    - type: nauc_mrr_at_20_max
      value: 34.714325975079156
    - type: nauc_mrr_at_20_std
      value: -0.5677886371954249
    - type: nauc_mrr_at_3_diff1
      value: 66.51153384715913
    - type: nauc_mrr_at_3_max
      value: 34.452498948880596
    - type: nauc_mrr_at_3_std
      value: -1.7332465728437143
    - type: nauc_mrr_at_5_diff1
      value: 66.59225232490988
    - type: nauc_mrr_at_5_max
      value: 34.7512528049011
    - type: nauc_mrr_at_5_std
      value: -0.7375111171529252
    - type: nauc_ndcg_at_1000_diff1
      value: 52.70447792725332
    - type: nauc_ndcg_at_1000_max
      value: 31.099714402668877
    - type: nauc_ndcg_at_1000_std
      value: 4.952576129141146
    - type: nauc_ndcg_at_100_diff1
      value: 51.8680556343591
    - type: nauc_ndcg_at_100_max
      value: 30.899433878567578
    - type: nauc_ndcg_at_100_std
      value: 5.15165187665861
    - type: nauc_ndcg_at_10_diff1
      value: 51.13133494726316
    - type: nauc_ndcg_at_10_max
      value: 30.350385714960144
    - type: nauc_ndcg_at_10_std
      value: 4.788310908509855
    - type: nauc_ndcg_at_1_diff1
      value: 67.19771091736617
    - type: nauc_ndcg_at_1_max
      value: 29.860207317348003
    - type: nauc_ndcg_at_1_std
      value: -3.6568452043648385
    - type: nauc_ndcg_at_20_diff1
      value: 51.430338783177845
    - type: nauc_ndcg_at_20_max
      value: 30.66830067670468
    - type: nauc_ndcg_at_20_std
      value: 5.321140832352313
    - type: nauc_ndcg_at_3_diff1
      value: 52.45624793046263
    - type: nauc_ndcg_at_3_max
      value: 29.934052260543847
    - type: nauc_ndcg_at_3_std
      value: 1.5120530275817168
    - type: nauc_ndcg_at_5_diff1
      value: 51.3969061446885
    - type: nauc_ndcg_at_5_max
      value: 30.239907029985897
    - type: nauc_ndcg_at_5_std
      value: 3.960594477502144
    - type: nauc_precision_at_1000_diff1
      value: 1.0422268465313624
    - type: nauc_precision_at_1000_max
      value: 15.84092949003887
    - type: nauc_precision_at_1000_std
      value: 9.963760763573108
    - type: nauc_precision_at_100_diff1
      value: 0.04282213273969017
    - type: nauc_precision_at_100_max
      value: 20.801404126556278
    - type: nauc_precision_at_100_std
      value: 14.868023073502593
    - type: nauc_precision_at_10_diff1
      value: 12.009370034101515
    - type: nauc_precision_at_10_max
      value: 31.401749097136626
    - type: nauc_precision_at_10_std
      value: 20.31851789650492
    - type: nauc_precision_at_1_diff1
      value: 67.19771091736617
    - type: nauc_precision_at_1_max
      value: 29.860207317348003
    - type: nauc_precision_at_1_std
      value: -3.6568452043648385
    - type: nauc_precision_at_20_diff1
      value: 6.2515537022637835
    - type: nauc_precision_at_20_max
      value: 27.36775832291631
    - type: nauc_precision_at_20_std
      value: 20.08032001724466
    - type: nauc_precision_at_3_diff1
      value: 35.00061054285493
    - type: nauc_precision_at_3_max
      value: 37.27790982101606
    - type: nauc_precision_at_3_std
      value: 9.236135982360096
    - type: nauc_precision_at_5_diff1
      value: 22.165859212913382
    - type: nauc_precision_at_5_max
      value: 35.223908290124776
    - type: nauc_precision_at_5_std
      value: 17.42571822680717
    - type: nauc_recall_at_1000_diff1
      value: 15.54216884685085
    - type: nauc_recall_at_1000_max
      value: 47.34980103888308
    - type: nauc_recall_at_1000_std
      value: 54.29278330007617
    - type: nauc_recall_at_100_diff1
      value: 15.804892954178532
    - type: nauc_recall_at_100_max
      value: 38.94488759227265
    - type: nauc_recall_at_100_std
      value: 39.15674768221356
    - type: nauc_recall_at_10_diff1
      value: 26.705107043813843
    - type: nauc_recall_at_10_max
      value: 33.52349469470716
    - type: nauc_recall_at_10_std
      value: 23.113004953511055
    - type: nauc_recall_at_1_diff1
      value: 54.29468230013946
    - type: nauc_recall_at_1_max
      value: 22.58894354165319
    - type: nauc_recall_at_1_std
      value: -2.7297280069759613
    - type: nauc_recall_at_20_diff1
      value: 23.16005062188733
    - type: nauc_recall_at_20_max
      value: 35.90277692951498
    - type: nauc_recall_at_20_std
      value: 30.83357455111629
    - type: nauc_recall_at_3_diff1
      value: 37.845329065879305
    - type: nauc_recall_at_3_max
      value: 29.827530624825272
    - type: nauc_recall_at_3_std
      value: 6.738499485390652
    - type: nauc_recall_at_5_diff1
      value: 32.32928010117198
    - type: nauc_recall_at_5_max
      value: 32.14388883263825
    - type: nauc_recall_at_5_std
      value: 16.086201199214255
    - type: ndcg_at_1
      value: 78.38300000000001
    - type: ndcg_at_10
      value: 84.936
    - type: ndcg_at_100
      value: 85.794
    - type: ndcg_at_1000
      value: 86.075
    - type: ndcg_at_20
      value: 85.341
    - type: ndcg_at_3
      value: 83.22800000000001
    - type: ndcg_at_5
      value: 84.224
    - type: precision_at_1
      value: 78.38300000000001
    - type: precision_at_10
      value: 10.181999999999999
    - type: precision_at_100
      value: 1.081
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_20
      value: 5.209
    - type: precision_at_3
      value: 31.852999999999998
    - type: precision_at_5
      value: 19.778000000000002
    - type: recall_at_1
      value: 72.57400000000001
    - type: recall_at_10
      value: 92.166
    - type: recall_at_100
      value: 95.634
    - type: recall_at_1000
      value: 97.432
    - type: recall_at_20
      value: 93.577
    - type: recall_at_3
      value: 87.46000000000001
    - type: recall_at_5
      value: 90.044
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB FiQA2018 (default)
      revision: 27a168819829fe9bcd655c2df245fb19452e8e06
      split: test
      type: mteb/fiqa
    metrics:
    - type: main_score
      value: 38.496
    - type: map_at_1
      value: 19.184
    - type: map_at_10
      value: 31.161
    - type: map_at_100
      value: 33.043
    - type: map_at_1000
      value: 33.232
    - type: map_at_20
      value: 32.226
    - type: map_at_3
      value: 27.607
    - type: map_at_5
      value: 29.499
    - type: mrr_at_1
      value: 37.808641975308646
    - type: mrr_at_10
      value: 46.674382716049365
    - type: mrr_at_100
      value: 47.52932976593473
    - type: mrr_at_1000
      value: 47.58129814456106
    - type: mrr_at_20
      value: 47.16211081543323
    - type: mrr_at_3
      value: 44.753086419753096
    - type: mrr_at_5
      value: 45.70216049382716
    - type: nauc_map_at_1000_diff1
      value: 41.13556588085034
    - type: nauc_map_at_1000_max
      value: 26.446518169258436
    - type: nauc_map_at_1000_std
      value: 4.947054879978255
    - type: nauc_map_at_100_diff1
      value: 41.07818713362254
    - type: nauc_map_at_100_max
      value: 26.358031657016213
    - type: nauc_map_at_100_std
      value: 4.962050092923268
    - type: nauc_map_at_10_diff1
      value: 41.44482937397835
    - type: nauc_map_at_10_max
      value: 25.721025003207565
    - type: nauc_map_at_10_std
      value: 3.329956561698185
    - type: nauc_map_at_1_diff1
      value: 46.26531369764426
    - type: nauc_map_at_1_max
      value: 18.364933647270643
    - type: nauc_map_at_1_std
      value: -2.262414956846059
    - type: nauc_map_at_20_diff1
      value: 41.02884195313503
    - type: nauc_map_at_20_max
      value: 25.825932384455264
    - type: nauc_map_at_20_std
      value: 4.228083176777648
    - type: nauc_map_at_3_diff1
      value: 43.106018762558875
    - type: nauc_map_at_3_max
      value: 24.77226948960475
    - type: nauc_map_at_3_std
      value: 1.8680539073320452
    - type: nauc_map_at_5_diff1
      value: 42.15001342294521
    - type: nauc_map_at_5_max
      value: 25.226226502657116
    - type: nauc_map_at_5_std
      value: 2.2239341498092804
    - type: nauc_mrr_at_1000_diff1
      value: 45.75815475829176
    - type: nauc_mrr_at_1000_max
      value: 33.16308247045093
    - type: nauc_mrr_at_1000_std
      value: 4.865912289812554
    - type: nauc_mrr_at_100_diff1
      value: 45.72090839837304
    - type: nauc_mrr_at_100_max
      value: 33.146147463070754
    - type: nauc_mrr_at_100_std
      value: 4.894576902832264
    - type: nauc_mrr_at_10_diff1
      value: 45.64332996509239
    - type: nauc_mrr_at_10_max
      value: 33.406770043256024
    - type: nauc_mrr_at_10_std
      value: 4.39074822608675
    - type: nauc_mrr_at_1_diff1
      value: 48.924390583495665
    - type: nauc_mrr_at_1_max
      value: 30.378798819048026
    - type: nauc_mrr_at_1_std
      value: 1.941425436753191
    - type: nauc_mrr_at_20_diff1
      value: 45.690917800161515
    - type: nauc_mrr_at_20_max
      value: 33.10823443798682
    - type: nauc_mrr_at_20_std
      value: 4.779855297102603
    - type: nauc_mrr_at_3_diff1
      value: 46.204867899757055
    - type: nauc_mrr_at_3_max
      value: 33.30076707231032
    - type: nauc_mrr_at_3_std
      value: 4.507678674711717
    - type: nauc_mrr_at_5_diff1
      value: 45.811627759116455
    - type: nauc_mrr_at_5_max
      value: 33.37895652871395
    - type: nauc_mrr_at_5_std
      value: 4.501784832453282
    - type: nauc_ndcg_at_1000_diff1
      value: 41.6125334158319
    - type: nauc_ndcg_at_1000_max
      value: 30.16303539863395
    - type: nauc_ndcg_at_1000_std
      value: 9.320860296325897
    - type: nauc_ndcg_at_100_diff1
      value: 40.58309967897852
    - type: nauc_ndcg_at_100_max
      value: 29.266226796484496
    - type: nauc_ndcg_at_100_std
      value: 10.31534341767162
    - type: nauc_ndcg_at_10_diff1
      value: 41.05940444122101
    - type: nauc_ndcg_at_10_max
      value: 27.96328418422611
    - type: nauc_ndcg_at_10_std
      value: 4.692298775524114
    - type: nauc_ndcg_at_1_diff1
      value: 48.924390583495665
    - type: nauc_ndcg_at_1_max
      value: 30.378798819048026
    - type: nauc_ndcg_at_1_std
      value: 1.941425436753191
    - type: nauc_ndcg_at_20_diff1
      value: 40.157160957917014
    - type: nauc_ndcg_at_20_max
      value: 27.493518163331522
    - type: nauc_ndcg_at_20_std
      value: 6.809059359656342
    - type: nauc_ndcg_at_3_diff1
      value: 41.63951276991973
    - type: nauc_ndcg_at_3_max
      value: 29.15518654994495
    - type: nauc_ndcg_at_3_std
      value: 4.836914696725136
    - type: nauc_ndcg_at_5_diff1
      value: 41.325178314736036
    - type: nauc_ndcg_at_5_max
      value: 28.050168266490928
    - type: nauc_ndcg_at_5_std
      value: 3.898848874816655
    - type: nauc_precision_at_1000_diff1
      value: 0.9996077037868993
    - type: nauc_precision_at_1000_max
      value: 23.48150040925757
    - type: nauc_precision_at_1000_std
      value: 12.864187472849862
    - type: nauc_precision_at_100_diff1
      value: 6.832487632948481
    - type: nauc_precision_at_100_max
      value: 26.9080049604059
    - type: nauc_precision_at_100_std
      value: 20.278561164143323
    - type: nauc_precision_at_10_diff1
      value: 18.571173078039145
    - type: nauc_precision_at_10_max
      value: 29.625927319287975
    - type: nauc_precision_at_10_std
      value: 12.543363741883576
    - type: nauc_precision_at_1_diff1
      value: 48.924390583495665
    - type: nauc_precision_at_1_max
      value: 30.378798819048026
    - type: nauc_precision_at_1_std
      value: 1.941425436753191
    - type: nauc_precision_at_20_diff1
      value: 13.515647907611536
    - type: nauc_precision_at_20_max
      value: 26.353132950858065
    - type: nauc_precision_at_20_std
      value: 14.887387015957195
    - type: nauc_precision_at_3_diff1
      value: 28.87824381197347
    - type: nauc_precision_at_3_max
      value: 30.99331486275142
    - type: nauc_precision_at_3_std
      value: 9.310818980550453
    - type: nauc_precision_at_5_diff1
      value: 23.21025248054266
    - type: nauc_precision_at_5_max
      value: 29.580877930541057
    - type: nauc_precision_at_5_std
      value: 9.593048125924087
    - type: nauc_recall_at_1000_diff1
      value: 30.10835562862456
    - type: nauc_recall_at_1000_max
      value: 24.149255779667854
    - type: nauc_recall_at_1000_std
      value: 37.07994398705662
    - type: nauc_recall_at_100_diff1
      value: 26.12210815380886
    - type: nauc_recall_at_100_max
      value: 22.570853805396553
    - type: nauc_recall_at_100_std
      value: 29.144304590338294
    - type: nauc_recall_at_10_diff1
      value: 31.94641026009961
    - type: nauc_recall_at_10_max
      value: 22.175120874773736
    - type: nauc_recall_at_10_std
      value: 4.761095246287363
    - type: nauc_recall_at_1_diff1
      value: 46.26531369764426
    - type: nauc_recall_at_1_max
      value: 18.364933647270643
    - type: nauc_recall_at_1_std
      value: -2.262414956846059
    - type: nauc_recall_at_20_diff1
      value: 27.64677435734486
    - type: nauc_recall_at_20_max
      value: 19.516676410346868
    - type: nauc_recall_at_20_std
      value: 10.872851154845188
    - type: nauc_recall_at_3_diff1
      value: 36.71090149814694
    - type: nauc_recall_at_3_max
      value: 23.731583063719967
    - type: nauc_recall_at_3_std
      value: 3.003592433785659
    - type: nauc_recall_at_5_diff1
      value: 34.94516645771627
    - type: nauc_recall_at_5_max
      value: 22.485817201833626
    - type: nauc_recall_at_5_std
      value: 2.8783986999083204
    - type: ndcg_at_1
      value: 37.809
    - type: ndcg_at_10
      value: 38.496
    - type: ndcg_at_100
      value: 45.251000000000005
    - type: ndcg_at_1000
      value: 48.583999999999996
    - type: ndcg_at_20
      value: 41.136
    - type: ndcg_at_3
      value: 35.759
    - type: ndcg_at_5
      value: 36.291000000000004
    - type: precision_at_1
      value: 37.809
    - type: precision_at_10
      value: 10.602
    - type: precision_at_100
      value: 1.7590000000000001
    - type: precision_at_1000
      value: 0.233
    - type: precision_at_20
      value: 6.465999999999999
    - type: precision_at_3
      value: 24.279999999999998
    - type: precision_at_5
      value: 17.438000000000002
    - type: recall_at_1
      value: 19.184
    - type: recall_at_10
      value: 44.335
    - type: recall_at_100
      value: 69.11500000000001
    - type: recall_at_1000
      value: 89.441
    - type: recall_at_20
      value: 52.193
    - type: recall_at_3
      value: 32.61
    - type: recall_at_5
      value: 37.018
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB HotpotQA (default)
      revision: ab518f4d6fcca38d87c25209f94beba119d02014
      split: test
      type: mteb/hotpotqa
    metrics:
    - type: main_score
      value: 69.21000000000001
    - type: map_at_1
      value: 38.785
    - type: map_at_10
      value: 60.838
    - type: map_at_100
      value: 61.696
    - type: map_at_1000
      value: 61.758
    - type: map_at_20
      value: 61.328
    - type: map_at_3
      value: 57.521
    - type: map_at_5
      value: 59.618
    - type: mrr_at_1
      value: 77.5692099932478
    - type: mrr_at_10
      value: 83.49855310118625
    - type: mrr_at_100
      value: 83.66645235605773
    - type: mrr_at_1000
      value: 83.67374499665621
    - type: mrr_at_20
      value: 83.6002145349913
    - type: mrr_at_3
      value: 82.49155975692081
    - type: mrr_at_5
      value: 83.17825793382818
    - type: nauc_map_at_1000_diff1
      value: 18.956900221394175
    - type: nauc_map_at_1000_max
      value: 16.964305368821428
    - type: nauc_map_at_1000_std
      value: 15.655849134524265
    - type: nauc_map_at_100_diff1
      value: 18.929114512218085
    - type: nauc_map_at_100_max
      value: 16.94710742970695
    - type: nauc_map_at_100_std
      value: 15.674964988072324
    - type: nauc_map_at_10_diff1
      value: 18.782047255838393
    - type: nauc_map_at_10_max
      value: 16.797329471843735
    - type: nauc_map_at_10_std
      value: 15.135148500192287
    - type: nauc_map_at_1_diff1
      value: 67.2370046355765
    - type: nauc_map_at_1_max
      value: 45.20986007464327
    - type: nauc_map_at_1_std
      value: 5.491336801263256
    - type: nauc_map_at_20_diff1
      value: 18.86964339327235
    - type: nauc_map_at_20_max
      value: 16.832263221676456
    - type: nauc_map_at_20_std
      value: 15.484857381790839
    - type: nauc_map_at_3_diff1
      value: 19.42608968562529
    - type: nauc_map_at_3_max
      value: 16.528325865015052
    - type: nauc_map_at_3_std
      value: 12.534151821941256
    - type: nauc_map_at_5_diff1
      value: 18.832060314354084
    - type: nauc_map_at_5_max
      value: 16.674177380965602
    - type: nauc_map_at_5_std
      value: 14.243688579695046
    - type: nauc_mrr_at_1000_diff1
      value: 66.1869057892041
    - type: nauc_mrr_at_1000_max
      value: 47.004199753631724
    - type: nauc_mrr_at_1000_std
      value: 8.368361737748069
    - type: nauc_mrr_at_100_diff1
      value: 66.18828485330391
    - type: nauc_mrr_at_100_max
      value: 47.01194361501428
    - type: nauc_mrr_at_100_std
      value: 8.382829386160866
    - type: nauc_mrr_at_10_diff1
      value: 66.16092867475533
    - type: nauc_mrr_at_10_max
      value: 47.07790111504346
    - type: nauc_mrr_at_10_std
      value: 8.464495756292754
    - type: nauc_mrr_at_1_diff1
      value: 67.2370046355765
    - type: nauc_mrr_at_1_max
      value: 45.20986007464327
    - type: nauc_mrr_at_1_std
      value: 5.491336801263256
    - type: nauc_mrr_at_20_diff1
      value: 66.1793742427507
    - type: nauc_mrr_at_20_max
      value: 47.02809343642448
    - type: nauc_mrr_at_20_std
      value: 8.386363287213086
    - type: nauc_mrr_at_3_diff1
      value: 66.16684538242693
    - type: nauc_mrr_at_3_max
      value: 47.142557308711616
    - type: nauc_mrr_at_3_std
      value: 8.141804487345757
    - type: nauc_mrr_at_5_diff1
      value: 65.96429788916728
    - type: nauc_mrr_at_5_max
      value: 46.93768012767146
    - type: nauc_mrr_at_5_std
      value: 8.208692767558844
    - type: nauc_ndcg_at_1000_diff1
      value: 24.84858425094176
    - type: nauc_ndcg_at_1000_max
      value: 21.82162743473047
    - type: nauc_ndcg_at_1000_std
      value: 18.342909152128044
    - type: nauc_ndcg_at_100_diff1
      value: 24.085422928773593
    - type: nauc_ndcg_at_100_max
      value: 21.3499532544156
    - type: nauc_ndcg_at_100_std
      value: 18.844827203764993
    - type: nauc_ndcg_at_10_diff1
      value: 23.623559226099033
    - type: nauc_ndcg_at_10_max
      value: 20.690583026235615
    - type: nauc_ndcg_at_10_std
      value: 16.715017586341173
    - type: nauc_ndcg_at_1_diff1
      value: 67.2370046355765
    - type: nauc_ndcg_at_1_max
      value: 45.20986007464327
    - type: nauc_ndcg_at_1_std
      value: 5.491336801263256
    - type: nauc_ndcg_at_20_diff1
      value: 23.713499963173195
    - type: nauc_ndcg_at_20_max
      value: 20.668447040323397
    - type: nauc_ndcg_at_20_std
      value: 17.629112144669932
    - type: nauc_ndcg_at_3_diff1
      value: 25.27768681334773
    - type: nauc_ndcg_at_3_max
      value: 20.828823134048164
    - type: nauc_ndcg_at_3_std
      value: 12.70796767520854
    - type: nauc_ndcg_at_5_diff1
      value: 23.89598796213276
    - type: nauc_ndcg_at_5_max
      value: 20.58599241532738
    - type: nauc_ndcg_at_5_std
      value: 14.95835803756551
    - type: nauc_precision_at_1000_diff1
      value: -3.4292836680950116
    - type: nauc_precision_at_1000_max
      value: 11.313613371375729
    - type: nauc_precision_at_1000_std
      value: 45.62746731220966
    - type: nauc_precision_at_100_diff1
      value: 1.506841269626321
    - type: nauc_precision_at_100_max
      value: 11.036489056981475
    - type: nauc_precision_at_100_std
      value: 37.47159150833276
    - type: nauc_precision_at_10_diff1
      value: 6.95635710197309
    - type: nauc_precision_at_10_max
      value: 11.562888984720791
    - type: nauc_precision_at_10_std
      value: 23.511130408518152
    - type: nauc_precision_at_1_diff1
      value: 67.2370046355765
    - type: nauc_precision_at_1_max
      value: 45.20986007464327
    - type: nauc_precision_at_1_std
      value: 5.491336801263256
    - type: nauc_precision_at_20_diff1
      value: 5.505741459315741
    - type: nauc_precision_at_20_max
      value: 10.507089080488106
    - type: nauc_precision_at_20_std
      value: 27.23927147632133
    - type: nauc_precision_at_3_diff1
      value: 13.412154109447352
    - type: nauc_precision_at_3_max
      value: 13.930584715797645
    - type: nauc_precision_at_3_std
      value: 15.064854663569433
    - type: nauc_precision_at_5_diff1
      value: 9.659656667775913
    - type: nauc_precision_at_5_max
      value: 12.713155451309499
    - type: nauc_precision_at_5_std
      value: 19.270448197611838
    - type: nauc_recall_at_1000_diff1
      value: -3.4292836680946994
    - type: nauc_recall_at_1000_max
      value: 11.313613371375997
    - type: nauc_recall_at_1000_std
      value: 45.62746731220985
    - type: nauc_recall_at_100_diff1
      value: 1.5068412696263371
    - type: nauc_recall_at_100_max
      value: 11.036489056981324
    - type: nauc_recall_at_100_std
      value: 37.471591508332594
    - type: nauc_recall_at_10_diff1
      value: 6.956357101973093
    - type: nauc_recall_at_10_max
      value: 11.562888984720738
    - type: nauc_recall_at_10_std
      value: 23.51113040851825
    - type: nauc_recall_at_1_diff1
      value: 67.2370046355765
    - type: nauc_recall_at_1_max
      value: 45.20986007464327
    - type: nauc_recall_at_1_std
      value: 5.491336801263256
    - type: nauc_recall_at_20_diff1
      value: 5.505741459315786
    - type: nauc_recall_at_20_max
      value: 10.507089080488091
    - type: nauc_recall_at_20_std
      value: 27.2392714763214
    - type: nauc_recall_at_3_diff1
      value: 13.412154109447364
    - type: nauc_recall_at_3_max
      value: 13.930584715797615
    - type: nauc_recall_at_3_std
      value: 15.064854663569433
    - type: nauc_recall_at_5_diff1
      value: 9.659656667775886
    - type: nauc_recall_at_5_max
      value: 12.713155451309596
    - type: nauc_recall_at_5_std
      value: 19.270448197611813
    - type: ndcg_at_1
      value: 77.569
    - type: ndcg_at_10
      value: 69.21000000000001
    - type: ndcg_at_100
      value: 72.21499999999999
    - type: ndcg_at_1000
      value: 73.418
    - type: ndcg_at_20
      value: 70.407
    - type: ndcg_at_3
      value: 64.5
    - type: ndcg_at_5
      value: 67.183
    - type: precision_at_1
      value: 77.569
    - type: precision_at_10
      value: 14.435999999999998
    - type: precision_at_100
      value: 1.68
    - type: precision_at_1000
      value: 0.184
    - type: precision_at_20
      value: 7.602
    - type: precision_at_3
      value: 41.215
    - type: precision_at_5
      value: 26.844
    - type: recall_at_1
      value: 38.785
    - type: recall_at_10
      value: 72.181
    - type: recall_at_100
      value: 84.018
    - type: recall_at_1000
      value: 91.972
    - type: recall_at_20
      value: 76.023
    - type: recall_at_3
      value: 61.82299999999999
    - type: recall_at_5
      value: 67.11
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ImdbClassification (default)
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
      split: test
      type: mteb/imdb
    metrics:
    - type: accuracy
      value: 91.30639999999998
    - type: ap
      value: 87.52850875096853
    - type: ap_weighted
      value: 87.52850875096853
    - type: f1
      value: 91.29841749475374
    - type: f1_weighted
      value: 91.29841749475374
    - type: main_score
      value: 91.30639999999998
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MSMARCO (default)
      revision: c5a29a104738b98a9e76336939199e264163d4a0
      split: test
      type: mteb/msmarco
    metrics:
    - type: main_score
      value: 69.801
    - type: map_at_1
      value: 2.451
    - type: map_at_10
      value: 15.669
    - type: map_at_100
      value: 38.479
    - type: map_at_1000
      value: 45.692
    - type: map_at_20
      value: 22.442
    - type: map_at_3
      value: 6.361999999999999
    - type: map_at_5
      value: 9.041
    - type: mrr_at_1
      value: 93.02325581395348
    - type: mrr_at_10
      value: 95.63953488372093
    - type: mrr_at_100
      value: 95.63953488372093
    - type: mrr_at_1000
      value: 95.63953488372093
    - type: mrr_at_20
      value: 95.63953488372093
    - type: mrr_at_3
      value: 95.34883720930233
    - type: mrr_at_5
      value: 95.34883720930233
    - type: nauc_map_at_1000_diff1
      value: -34.77360607000261
    - type: nauc_map_at_1000_max
      value: 37.105245787173835
    - type: nauc_map_at_1000_std
      value: 38.520309199886455
    - type: nauc_map_at_100_diff1
      value: -21.42480611783042
    - type: nauc_map_at_100_max
      value: 20.50633133517426
    - type: nauc_map_at_100_std
      value: 17.726069370578543
    - type: nauc_map_at_10_diff1
      value: -1.1900473891638557
    - type: nauc_map_at_10_max
      value: -4.327696460661841
    - type: nauc_map_at_10_std
      value: -22.9353425409415
    - type: nauc_map_at_1_diff1
      value: 8.887948006513117
    - type: nauc_map_at_1_max
      value: -28.392221850180484
    - type: nauc_map_at_1_std
      value: -36.713671179054636
    - type: nauc_map_at_20_diff1
      value: -4.063108213547096
    - type: nauc_map_at_20_max
      value: 2.5748738626205303
    - type: nauc_map_at_20_std
      value: -13.84602498035036
    - type: nauc_map_at_3_diff1
      value: 2.242735363640109
    - type: nauc_map_at_3_max
      value: -22.59145084951087
    - type: nauc_map_at_3_std
      value: -34.62574649864125
    - type: nauc_map_at_5_diff1
      value: 0.6216057852370439
    - type: nauc_map_at_5_max
      value: -13.727700828370892
    - type: nauc_map_at_5_std
      value: -29.642718215652135
    - type: nauc_mrr_at_1000_diff1
      value: -26.460535747732973
    - type: nauc_mrr_at_1000_max
      value: 66.59497826279839
    - type: nauc_mrr_at_1000_std
      value: 43.162508643477295
    - type: nauc_mrr_at_100_diff1
      value: -26.460535747732973
    - type: nauc_mrr_at_100_max
      value: 66.59497826279839
    - type: nauc_mrr_at_100_std
      value: 43.162508643477295
    - type: nauc_mrr_at_10_diff1
      value: -26.460535747732973
    - type: nauc_mrr_at_10_max
      value: 66.59497826279839
    - type: nauc_mrr_at_10_std
      value: 43.162508643477295
    - type: nauc_mrr_at_1_diff1
      value: -4.79052153792628
    - type: nauc_mrr_at_1_max
      value: 74.2862212758406
    - type: nauc_mrr_at_1_std
      value: 28.953135804346815
    - type: nauc_mrr_at_20_diff1
      value: -26.460535747732973
    - type: nauc_mrr_at_20_max
      value: 66.59497826279839
    - type: nauc_mrr_at_20_std
      value: 43.162508643477295
    - type: nauc_mrr_at_3_diff1
      value: -31.878039300184707
    - type: nauc_mrr_at_3_max
      value: 64.67216750953789
    - type: nauc_mrr_at_3_std
      value: 46.71485185326015
    - type: nauc_mrr_at_5_diff1
      value: -31.878039300184707
    - type: nauc_mrr_at_5_max
      value: 64.67216750953789
    - type: nauc_mrr_at_5_std
      value: 46.71485185326015
    - type: nauc_ndcg_at_1000_diff1
      value: -44.15085027848325
    - type: nauc_ndcg_at_1000_max
      value: 56.25521046667954
    - type: nauc_ndcg_at_1000_std
      value: 46.36970379223632
    - type: nauc_ndcg_at_100_diff1
      value: -39.50083793730437
    - type: nauc_ndcg_at_100_max
      value: 41.82457895330969
    - type: nauc_ndcg_at_100_std
      value: 43.75463835115521
    - type: nauc_ndcg_at_10_diff1
      value: -20.601212170311666
    - type: nauc_ndcg_at_10_max
      value: 39.636237142037565
    - type: nauc_ndcg_at_10_std
      value: 19.452478646271373
    - type: nauc_ndcg_at_1_diff1
      value: 22.80050548927079
    - type: nauc_ndcg_at_1_max
      value: 31.358862371469264
    - type: nauc_ndcg_at_1_std
      value: -7.142182820398638
    - type: nauc_ndcg_at_20_diff1
      value: -34.11753790748588
    - type: nauc_ndcg_at_20_max
      value: 32.1122313276435
    - type: nauc_ndcg_at_20_std
      value: 28.105554366760018
    - type: nauc_ndcg_at_3_diff1
      value: 2.6372016977509594
    - type: nauc_ndcg_at_3_max
      value: 35.156005404237845
    - type: nauc_ndcg_at_3_std
      value: 6.261468803699801
    - type: nauc_ndcg_at_5_diff1
      value: -9.474268053778937
    - type: nauc_ndcg_at_5_max
      value: 33.21925931881887
    - type: nauc_ndcg_at_5_std
      value: 7.458434415980239
    - type: nauc_precision_at_1000_diff1
      value: -40.07799532530941
    - type: nauc_precision_at_1000_max
      value: 31.156456417174205
    - type: nauc_precision_at_1000_std
      value: 48.27480631876068
    - type: nauc_precision_at_100_diff1
      value: -42.02250569966725
    - type: nauc_precision_at_100_max
      value: 33.58973907303474
    - type: nauc_precision_at_100_std
      value: 55.06366799570662
    - type: nauc_precision_at_10_diff1
      value: -49.71439650639399
    - type: nauc_precision_at_10_max
      value: 58.113349127681545
    - type: nauc_precision_at_10_std
      value: 55.03130750422891
    - type: nauc_precision_at_1_diff1
      value: -4.79052153792628
    - type: nauc_precision_at_1_max
      value: 74.2862212758406
    - type: nauc_precision_at_1_std
      value: 28.953135804346815
    - type: nauc_precision_at_20_diff1
      value: -44.7658587995923
    - type: nauc_precision_at_20_max
      value: 37.95609687942612
    - type: nauc_precision_at_20_std
      value: 50.32119458805291
    - type: nauc_precision_at_3_diff1
      value: -46.00414842286393
    - type: nauc_precision_at_3_max
      value: 61.74015379253264
    - type: nauc_precision_at_3_std
      value: 56.4136278482117
    - type: nauc_precision_at_5_diff1
      value: -51.7601573366637
    - type: nauc_precision_at_5_max
      value: 55.953703102236965
    - type: nauc_precision_at_5_std
      value: 51.41803894746122
    - type: nauc_recall_at_1000_diff1
      value: -47.522392809524945
    - type: nauc_recall_at_1000_max
      value: 53.589786470310806
    - type: nauc_recall_at_1000_std
      value: 46.470512981921274
    - type: nauc_recall_at_100_diff1
      value: -15.907347162724578
    - type: nauc_recall_at_100_max
      value: 21.680423810119056
    - type: nauc_recall_at_100_std
      value: 15.973645761855645
    - type: nauc_recall_at_10_diff1
      value: 0.10781311427713663
    - type: nauc_recall_at_10_max
      value: -9.277386241567552
    - type: nauc_recall_at_10_std
      value: -24.949282177180258
    - type: nauc_recall_at_1_diff1
      value: 8.887948006513117
    - type: nauc_recall_at_1_max
      value: -28.392221850180484
    - type: nauc_recall_at_1_std
      value: -36.713671179054636
    - type: nauc_recall_at_20_diff1
      value: -2.930230134017464
    - type: nauc_recall_at_20_max
      value: -1.739131611687823
    - type: nauc_recall_at_20_std
      value: -16.2461103824525
    - type: nauc_recall_at_3_diff1
      value: 1.7811229328074583
    - type: nauc_recall_at_3_max
      value: -24.815459645928094
    - type: nauc_recall_at_3_std
      value: -34.963317879895826
    - type: nauc_recall_at_5_diff1
      value: -0.07179290440344144
    - type: nauc_recall_at_5_max
      value: -17.45693684826598
    - type: nauc_recall_at_5_std
      value: -31.10276136562734
    - type: ndcg_at_1
      value: 74.419
    - type: ndcg_at_10
      value: 69.801
    - type: ndcg_at_100
      value: 62.514
    - type: ndcg_at_1000
      value: 69.173
    - type: ndcg_at_20
      value: 66.247
    - type: ndcg_at_3
      value: 72.752
    - type: ndcg_at_5
      value: 70.795
    - type: precision_at_1
      value: 93.023
    - type: precision_at_10
      value: 79.767
    - type: precision_at_100
      value: 37.023
    - type: precision_at_1000
      value: 6.63
    - type: precision_at_20
      value: 67.907
    - type: precision_at_3
      value: 86.822
    - type: precision_at_5
      value: 83.256
    - type: recall_at_1
      value: 2.451
    - type: recall_at_10
      value: 17.041
    - type: recall_at_100
      value: 50.346999999999994
    - type: recall_at_1000
      value: 74.842
    - type: recall_at_20
      value: 24.94
    - type: recall_at_3
      value: 6.548
    - type: recall_at_5
      value: 9.497
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB MTOPDomainClassification (en)
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
      split: test
      type: mteb/mtop_domain
    metrics:
    - type: accuracy
      value: 92.49202006383948
    - type: f1
      value: 92.33980048261546
    - type: f1_weighted
      value: 92.44985105058221
    - type: main_score
      value: 92.49202006383948
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MTOPIntentClassification (en)
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
      split: test
      type: mteb/mtop_intent
    metrics:
    - type: accuracy
      value: 63.23301413588691
    - type: f1
      value: 44.554720819218964
    - type: f1_weighted
      value: 65.47524300339032
    - type: main_score
      value: 63.23301413588691
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveIntentClassification (en)
      revision: 4672e20407010da34463acc759c162ca9734bca6
      split: test
      type: mteb/amazon_massive_intent
    metrics:
    - type: accuracy
      value: 70.43375924680566
    - type: f1
      value: 68.02391267335155
    - type: f1_weighted
      value: 69.25139312466567
    - type: main_score
      value: 70.43375924680566
    task:
      type: Classification
  - dataset:
      config: en
      name: MTEB MassiveScenarioClassification (en)
      revision: fad2c6e8459f9e1c45d9315f4953d921437d70f8
      split: test
      type: mteb/amazon_massive_scenario
    metrics:
    - type: accuracy
      value: 75.12104909213181
    - type: f1
      value: 74.58688682730612
    - type: f1_weighted
      value: 74.76872548200055
    - type: main_score
      value: 75.12104909213181
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB MedicalQARetrieval (default)
      revision: ae763399273d8b20506b80cf6f6f9a31a6a2b238
      split: test
      type: mteb/medical_qa
    metrics:
    - type: main_score
      value: 70.316
    - type: map_at_1
      value: 55.762
    - type: map_at_10
      value: 65.617
    - type: map_at_100
      value: 66.07499999999999
    - type: map_at_1000
      value: 66.098
    - type: map_at_20
      value: 65.926
    - type: map_at_3
      value: 63.46000000000001
    - type: map_at_5
      value: 64.81
    - type: mrr_at_1
      value: 55.76171875
    - type: mrr_at_10
      value: 65.61734638516852
    - type: mrr_at_100
      value: 66.07564323944077
    - type: mrr_at_1000
      value: 66.09885409027784
    - type: mrr_at_20
      value: 65.92394787011318
    - type: mrr_at_3
      value: 63.46028645833318
    - type: mrr_at_5
      value: 64.81038411458326
    - type: nauc_map_at_1000_diff1
      value: 55.117921948917704
    - type: nauc_map_at_1000_max
      value: 40.329646871994434
    - type: nauc_map_at_1000_std
      value: -2.7447494458084516
    - type: nauc_map_at_100_diff1
      value: 55.08707565824308
    - type: nauc_map_at_100_max
      value: 40.35427405860057
    - type: nauc_map_at_100_std
      value: -2.7521388878942994
    - type: nauc_map_at_10_diff1
      value: 54.987359148416616
    - type: nauc_map_at_10_max
      value: 40.2168179457375
    - type: nauc_map_at_10_std
      value: -2.978624864409744
    - type: nauc_map_at_1_diff1
      value: 61.239951679175974
    - type: nauc_map_at_1_max
      value: 39.49150430490776
    - type: nauc_map_at_1_std
      value: -1.8142615816830427
    - type: nauc_map_at_20_diff1
      value: 54.980346172896766
    - type: nauc_map_at_20_max
      value: 40.388274220840984
    - type: nauc_map_at_20_std
      value: -2.7917130558799648
    - type: nauc_map_at_3_diff1
      value: 55.540250455236176
    - type: nauc_map_at_3_max
      value: 39.01408945261429
    - type: nauc_map_at_3_std
      value: -2.804709321224132
    - type: nauc_map_at_5_diff1
      value: 55.17728028457556
    - type: nauc_map_at_5_max
      value: 39.67456707836799
    - type: nauc_map_at_5_std
      value: -2.9985665760830456
    - type: nauc_mrr_at_1000_diff1
      value: 55.119408854006814
    - type: nauc_mrr_at_1000_max
      value: 40.386764886119956
    - type: nauc_mrr_at_1000_std
      value: -2.5256541513637263
    - type: nauc_mrr_at_100_diff1
      value: 55.08855646650919
    - type: nauc_mrr_at_100_max
      value: 40.41133635338564
    - type: nauc_mrr_at_100_std
      value: -2.533239161326411
    - type: nauc_mrr_at_10_diff1
      value: 54.988649543503385
    - type: nauc_mrr_at_10_max
      value: 40.27285482782524
    - type: nauc_mrr_at_10_std
      value: -2.762984128910569
    - type: nauc_mrr_at_1_diff1
      value: 61.239951679175974
    - type: nauc_mrr_at_1_max
      value: 39.586560519712386
    - type: nauc_mrr_at_1_std
      value: -1.4746589950499525
    - type: nauc_mrr_at_20_diff1
      value: 54.985183128082305
    - type: nauc_mrr_at_20_max
      value: 40.448217601766494
    - type: nauc_mrr_at_20_std
      value: -2.575271717637722
    - type: nauc_mrr_at_3_diff1
      value: 55.540250455236176
    - type: nauc_mrr_at_3_max
      value: 39.051677641594125
    - type: nauc_mrr_at_3_std
      value: -2.5883569220502896
    - type: nauc_mrr_at_5_diff1
      value: 55.17728028457556
    - type: nauc_mrr_at_5_max
      value: 39.71664203575019
    - type: nauc_mrr_at_5_std
      value: -2.770350063430267
    - type: nauc_ndcg_at_1000_diff1
      value: 53.6068186160231
    - type: nauc_ndcg_at_1000_max
      value: 41.16895263409432
    - type: nauc_ndcg_at_1000_std
      value: -2.668077069688034
    - type: nauc_ndcg_at_100_diff1
      value: 52.72931924038622
    - type: nauc_ndcg_at_100_max
      value: 41.92759552302126
    - type: nauc_ndcg_at_100_std
      value: -2.5890899194293304
    - type: nauc_ndcg_at_10_diff1
      value: 52.007628100401234
    - type: nauc_ndcg_at_10_max
      value: 41.737827206310705
    - type: nauc_ndcg_at_10_std
      value: -3.542176180209694
    - type: nauc_ndcg_at_1_diff1
      value: 61.239951679175974
    - type: nauc_ndcg_at_1_max
      value: 39.49150430490776
    - type: nauc_ndcg_at_1_std
      value: -1.8142615816830427
    - type: nauc_ndcg_at_20_diff1
      value: 51.847691200116586
    - type: nauc_ndcg_at_20_max
      value: 42.42280333674705
    - type: nauc_ndcg_at_20_std
      value: -2.850352004423232
    - type: nauc_ndcg_at_3_diff1
      value: 53.51791263993053
    - type: nauc_ndcg_at_3_max
      value: 38.862920843577655
    - type: nauc_ndcg_at_3_std
      value: -3.187427589360101
    - type: nauc_ndcg_at_5_diff1
      value: 52.645322320026466
    - type: nauc_ndcg_at_5_max
      value: 40.18836539232817
    - type: nauc_ndcg_at_5_std
      value: -3.615361739188517
    - type: nauc_precision_at_1000_diff1
      value: 41.51993887005676
    - type: nauc_precision_at_1000_max
      value: 31.92569580445928
    - type: nauc_precision_at_1000_std
      value: 13.578742907797217
    - type: nauc_precision_at_100_diff1
      value: 21.604666213166603
    - type: nauc_precision_at_100_max
      value: 67.69955190694637
    - type: nauc_precision_at_100_std
      value: 4.356106302996764
    - type: nauc_precision_at_10_diff1
      value: 35.06077106721305
    - type: nauc_precision_at_10_max
      value: 51.73865588486901
    - type: nauc_precision_at_10_std
      value: -6.637691880259535
    - type: nauc_precision_at_1_diff1
      value: 61.239951679175974
    - type: nauc_precision_at_1_max
      value: 39.49150430490776
    - type: nauc_precision_at_1_std
      value: -1.8142615816830427
    - type: nauc_precision_at_20_diff1
      value: 27.691560548393458
    - type: nauc_precision_at_20_max
      value: 60.735172992308385
    - type: nauc_precision_at_20_std
      value: -2.087850725674345
    - type: nauc_precision_at_3_diff1
      value: 46.443339144235736
    - type: nauc_precision_at_3_max
      value: 38.34121270977754
    - type: nauc_precision_at_3_std
      value: -4.53847034769947
    - type: nauc_precision_at_5_diff1
      value: 41.99220857335789
    - type: nauc_precision_at_5_max
      value: 42.64971733556552
    - type: nauc_precision_at_5_std
      value: -6.288726238529177
    - type: nauc_recall_at_1000_diff1
      value: 41.51993887005676
    - type: nauc_recall_at_1000_max
      value: 31.925695804460947
    - type: nauc_recall_at_1000_std
      value: 13.578742907798885
    - type: nauc_recall_at_100_diff1
      value: 21.604666213166638
    - type: nauc_recall_at_100_max
      value: 67.69955190694643
    - type: nauc_recall_at_100_std
      value: 4.356106302997579
    - type: nauc_recall_at_10_diff1
      value: 35.060771067213025
    - type: nauc_recall_at_10_max
      value: 51.738655884869054
    - type: nauc_recall_at_10_std
      value: -6.637691880259386
    - type: nauc_recall_at_1_diff1
      value: 61.239951679175974
    - type: nauc_recall_at_1_max
      value: 39.49150430490776
    - type: nauc_recall_at_1_std
      value: -1.8142615816830427
    - type: nauc_recall_at_20_diff1
      value: 27.691560548393547
    - type: nauc_recall_at_20_max
      value: 60.73517299230855
    - type: nauc_recall_at_20_std
      value: -2.0878507256741576
    - type: nauc_recall_at_3_diff1
      value: 46.44333914423575
    - type: nauc_recall_at_3_max
      value: 38.34121270977744
    - type: nauc_recall_at_3_std
      value: -4.538470347699562
    - type: nauc_recall_at_5_diff1
      value: 41.992208573358035
    - type: nauc_recall_at_5_max
      value: 42.64971733556567
    - type: nauc_recall_at_5_std
      value: -6.2887262385288984
    - type: ndcg_at_1
      value: 55.762
    - type: ndcg_at_10
      value: 70.316
    - type: ndcg_at_100
      value: 72.499
    - type: ndcg_at_1000
      value: 73.08
    - type: ndcg_at_20
      value: 71.416
    - type: ndcg_at_3
      value: 65.926
    - type: ndcg_at_5
      value: 68.35900000000001
    - type: precision_at_1
      value: 55.762
    - type: precision_at_10
      value: 8.501
    - type: precision_at_100
      value: 0.9520000000000001
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.465
    - type: precision_at_3
      value: 24.349
    - type: precision_at_5
      value: 15.791
    - type: recall_at_1
      value: 55.762
    - type: recall_at_10
      value: 85.00999999999999
    - type: recall_at_100
      value: 95.166
    - type: recall_at_1000
      value: 99.658
    - type: recall_at_20
      value: 89.307
    - type: recall_at_3
      value: 73.047
    - type: recall_at_5
      value: 78.955
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P (default)
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: main_score
      value: 32.88590429483386
    - type: v_measure
      value: 32.88590429483386
    - type: v_measure_std
      value: 1.2486157627386651
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S (default)
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: main_score
      value: 30.63686758451441
    - type: v_measure
      value: 30.63686758451441
    - type: v_measure_std
      value: 1.5635535104381142
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MindSmallReranking (default)
      revision: 59042f120c80e8afa9cdbb224f67076cec0fc9a7
      split: test
      type: mteb/mind_small
    metrics:
    - type: main_score
      value: 31.716756843517015
    - type: map
      value: 31.716756843517015
    - type: mrr
      value: 32.866394172957655
    - type: nAUC_map_diff1
      value: 15.654229044661353
    - type: nAUC_map_max
      value: -22.25897993906556
    - type: nAUC_map_std
      value: 0.367638815729836
    - type: nAUC_mrr_diff1
      value: 14.466390859042203
    - type: nAUC_mrr_max
      value: -16.66565819268613
    - type: nAUC_mrr_std
      value: 1.389862783951572
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB NFCorpus (default)
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: main_score
      value: 34.777
    - type: map_at_1
      value: 6.0249999999999995
    - type: map_at_10
      value: 13.017999999999999
    - type: map_at_100
      value: 16.358
    - type: map_at_1000
      value: 17.801000000000002
    - type: map_at_20
      value: 14.563
    - type: map_at_3
      value: 9.611
    - type: map_at_5
      value: 11.136
    - type: mrr_at_1
      value: 44.58204334365325
    - type: mrr_at_10
      value: 53.830655069045164
    - type: mrr_at_100
      value: 54.46820987161318
    - type: mrr_at_1000
      value: 54.511938990208975
    - type: mrr_at_20
      value: 54.285959410205784
    - type: mrr_at_3
      value: 52.167182662538714
    - type: mrr_at_5
      value: 53.1733746130031
    - type: nauc_map_at_1000_diff1
      value: 25.967815322021565
    - type: nauc_map_at_1000_max
      value: 28.327078445483668
    - type: nauc_map_at_1000_std
      value: 19.120652749371374
    - type: nauc_map_at_100_diff1
      value: 26.951232790374526
    - type: nauc_map_at_100_max
      value: 26.902092532931434
    - type: nauc_map_at_100_std
      value: 15.699072220565489
    - type: nauc_map_at_10_diff1
      value: 31.257086882033242
    - type: nauc_map_at_10_max
      value: 20.52720655255051
    - type: nauc_map_at_10_std
      value: 4.404750581767724
    - type: nauc_map_at_1_diff1
      value: 47.62591630591148
    - type: nauc_map_at_1_max
      value: 9.558540429651298
    - type: nauc_map_at_1_std
      value: -6.045890488872336
    - type: nauc_map_at_20_diff1
      value: 28.474824272816917
    - type: nauc_map_at_20_max
      value: 23.333197224732306
    - type: nauc_map_at_20_std
      value: 9.263916337302483
    - type: nauc_map_at_3_diff1
      value: 38.471834690020316
    - type: nauc_map_at_3_max
      value: 13.696518596133291
    - type: nauc_map_at_3_std
      value: -3.5625552745508533
    - type: nauc_map_at_5_diff1
      value: 34.52907976674023
    - type: nauc_map_at_5_max
      value: 16.13732934020574
    - type: nauc_map_at_5_std
      value: -0.7543340982584198
    - type: nauc_mrr_at_1000_diff1
      value: 31.33476913665314
    - type: nauc_mrr_at_1000_max
      value: 46.958109189628935
    - type: nauc_mrr_at_1000_std
      value: 28.044556451367423
    - type: nauc_mrr_at_100_diff1
      value: 31.339069159264355
    - type: nauc_mrr_at_100_max
      value: 46.98656300883579
    - type: nauc_mrr_at_100_std
      value: 28.0900577359196
    - type: nauc_mrr_at_10_diff1
      value: 31.342505233934997
    - type: nauc_mrr_at_10_max
      value: 46.97823869966797
    - type: nauc_mrr_at_10_std
      value: 27.4601265013717
    - type: nauc_mrr_at_1_diff1
      value: 33.4378541215048
    - type: nauc_mrr_at_1_max
      value: 41.15562154589828
    - type: nauc_mrr_at_1_std
      value: 19.90780249506625
    - type: nauc_mrr_at_20_diff1
      value: 31.360572539137888
    - type: nauc_mrr_at_20_max
      value: 47.00390756684394
    - type: nauc_mrr_at_20_std
      value: 28.13990587820234
    - type: nauc_mrr_at_3_diff1
      value: 32.093115382725216
    - type: nauc_mrr_at_3_max
      value: 46.30933548142642
    - type: nauc_mrr_at_3_std
      value: 26.241763806261552
    - type: nauc_mrr_at_5_diff1
      value: 31.551702480820225
    - type: nauc_mrr_at_5_max
      value: 46.194614393756375
    - type: nauc_mrr_at_5_std
      value: 27.324586188062337
    - type: nauc_ndcg_at_1000_diff1
      value: 25.311180709157977
    - type: nauc_ndcg_at_1000_max
      value: 44.92771338176505
    - type: nauc_ndcg_at_1000_std
      value: 37.27892149005223
    - type: nauc_ndcg_at_100_diff1
      value: 25.662285786793
    - type: nauc_ndcg_at_100_max
      value: 41.08725464946671
    - type: nauc_ndcg_at_100_std
      value: 31.647308668978567
    - type: nauc_ndcg_at_10_diff1
      value: 22.814244065959365
    - type: nauc_ndcg_at_10_max
      value: 38.94186160526081
    - type: nauc_ndcg_at_10_std
      value: 28.739546916606184
    - type: nauc_ndcg_at_1_diff1
      value: 33.92055290582491
    - type: nauc_ndcg_at_1_max
      value: 39.7746239892313
    - type: nauc_ndcg_at_1_std
      value: 21.403337562252666
    - type: nauc_ndcg_at_20_diff1
      value: 22.147194739989953
    - type: nauc_ndcg_at_20_max
      value: 38.331435685309486
    - type: nauc_ndcg_at_20_std
      value: 30.001574369100286
    - type: nauc_ndcg_at_3_diff1
      value: 26.551315174426477
    - type: nauc_ndcg_at_3_max
      value: 40.95235936186754
    - type: nauc_ndcg_at_3_std
      value: 25.814502311046923
    - type: nauc_ndcg_at_5_diff1
      value: 23.30015530643268
    - type: nauc_ndcg_at_5_max
      value: 39.112038419598846
    - type: nauc_ndcg_at_5_std
      value: 27.014662420712636
    - type: nauc_precision_at_1000_diff1
      value: -9.31122599724474
    - type: nauc_precision_at_1000_max
      value: 15.828254499573301
    - type: nauc_precision_at_1000_std
      value: 31.90284644408184
    - type: nauc_precision_at_100_diff1
      value: -5.607783322273428
    - type: nauc_precision_at_100_max
      value: 28.044293136935156
    - type: nauc_precision_at_100_std
      value: 44.33306673952984
    - type: nauc_precision_at_10_diff1
      value: 3.672329984381369
    - type: nauc_precision_at_10_max
      value: 40.22743872425158
    - type: nauc_precision_at_10_std
      value: 38.03616890730788
    - type: nauc_precision_at_1_diff1
      value: 33.4378541215048
    - type: nauc_precision_at_1_max
      value: 41.15562154589828
    - type: nauc_precision_at_1_std
      value: 19.90780249506625
    - type: nauc_precision_at_20_diff1
      value: -2.1150512386488014
    - type: nauc_precision_at_20_max
      value: 36.304499614907
    - type: nauc_precision_at_20_std
      value: 42.6230212264936
    - type: nauc_precision_at_3_diff1
      value: 15.845993825652796
    - type: nauc_precision_at_3_max
      value: 42.887373246287616
    - type: nauc_precision_at_3_std
      value: 29.489599796549705
    - type: nauc_precision_at_5_diff1
      value: 6.777054989797422
    - type: nauc_precision_at_5_max
      value: 39.54397793435193
    - type: nauc_precision_at_5_std
      value: 32.47818021039132
    - type: nauc_recall_at_1000_diff1
      value: 11.315947856942906
    - type: nauc_recall_at_1000_max
      value: 21.01998620182054
    - type: nauc_recall_at_1000_std
      value: 26.8227846588364
    - type: nauc_recall_at_100_diff1
      value: 18.899757056503482
    - type: nauc_recall_at_100_max
      value: 28.57869305089085
    - type: nauc_recall_at_100_std
      value: 25.90208233770403
    - type: nauc_recall_at_10_diff1
      value: 26.671963776958673
    - type: nauc_recall_at_10_max
      value: 20.085669076192627
    - type: nauc_recall_at_10_std
      value: 4.64306341080659
    - type: nauc_recall_at_1_diff1
      value: 47.62591630591148
    - type: nauc_recall_at_1_max
      value: 9.558540429651298
    - type: nauc_recall_at_1_std
      value: -6.045890488872336
    - type: nauc_recall_at_20_diff1
      value: 21.352657194561484
    - type: nauc_recall_at_20_max
      value: 22.287907898181967
    - type: nauc_recall_at_20_std
      value: 11.591359883790235
    - type: nauc_recall_at_3_diff1
      value: 37.883426141495484
    - type: nauc_recall_at_3_max
      value: 13.541910021778506
    - type: nauc_recall_at_3_std
      value: -3.5291589555216265
    - type: nauc_recall_at_5_diff1
      value: 31.497983991389315
    - type: nauc_recall_at_5_max
      value: 15.615278638126394
    - type: nauc_recall_at_5_std
      value: 0.3332620589500228
    - type: ndcg_at_1
      value: 43.189
    - type: ndcg_at_10
      value: 34.777
    - type: ndcg_at_100
      value: 31.298
    - type: ndcg_at_1000
      value: 40.472
    - type: ndcg_at_20
      value: 32.651
    - type: ndcg_at_3
      value: 40.176
    - type: ndcg_at_5
      value: 37.708000000000006
    - type: precision_at_1
      value: 44.582
    - type: precision_at_10
      value: 25.944
    - type: precision_at_100
      value: 7.8759999999999994
    - type: precision_at_1000
      value: 2.0789999999999997
    - type: precision_at_20
      value: 19.365
    - type: precision_at_3
      value: 37.771
    - type: precision_at_5
      value: 32.693
    - type: recall_at_1
      value: 6.0249999999999995
    - type: recall_at_10
      value: 16.744999999999997
    - type: recall_at_100
      value: 30.962
    - type: recall_at_1000
      value: 64.862
    - type: recall_at_20
      value: 21.083
    - type: recall_at_3
      value: 10.437000000000001
    - type: recall_at_5
      value: 12.919
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB NQ (default)
      revision: b774495ed302d8c44a3a7ea25c90dbce03968f31
      split: test
      type: mteb/nq
    metrics:
    - type: main_score
      value: 45.429
    - type: map_at_1
      value: 24.348
    - type: map_at_10
      value: 37.979
    - type: map_at_100
      value: 39.152
    - type: map_at_1000
      value: 39.196
    - type: map_at_20
      value: 38.698
    - type: map_at_3
      value: 33.576
    - type: map_at_5
      value: 36.313
    - type: mrr_at_1
      value: 27.896871378910777
    - type: mrr_at_10
      value: 40.57155732126759
    - type: mrr_at_100
      value: 41.505776028088356
    - type: mrr_at_1000
      value: 41.536949900301714
    - type: mrr_at_20
      value: 41.16254355270229
    - type: mrr_at_3
      value: 36.73232908458862
    - type: mrr_at_5
      value: 39.15990730011593
    - type: nauc_map_at_1000_diff1
      value: 32.46093433815888
    - type: nauc_map_at_1000_max
      value: 19.394096123431115
    - type: nauc_map_at_1000_std
      value: -1.4164718950716537
    - type: nauc_map_at_100_diff1
      value: 32.45486165462264
    - type: nauc_map_at_100_max
      value: 19.421234606093616
    - type: nauc_map_at_100_std
      value: -1.3862594418165226
    - type: nauc_map_at_10_diff1
      value: 32.46141882554964
    - type: nauc_map_at_10_max
      value: 19.0209806089726
    - type: nauc_map_at_10_std
      value: -2.1299605104758528
    - type: nauc_map_at_1_diff1
      value: 33.91219452872979
    - type: nauc_map_at_1_max
      value: 15.243617612429572
    - type: nauc_map_at_1_std
      value: -4.118372460673027
    - type: nauc_map_at_20_diff1
      value: 32.447816129738385
    - type: nauc_map_at_20_max
      value: 19.375630035882168
    - type: nauc_map_at_20_std
      value: -1.6126821757328305
    - type: nauc_map_at_3_diff1
      value: 32.22584317116853
    - type: nauc_map_at_3_max
      value: 17.027294527302406
    - type: nauc_map_at_3_std
      value: -3.900453065296092
    - type: nauc_map_at_5_diff1
      value: 32.21812147700183
    - type: nauc_map_at_5_max
      value: 18.22808737031908
    - type: nauc_map_at_5_std
      value: -3.0121231831131237
    - type: nauc_mrr_at_1000_diff1
      value: 32.19391640024058
    - type: nauc_mrr_at_1000_max
      value: 19.94471248318332
    - type: nauc_mrr_at_1000_std
      value: 0.1932185073583155
    - type: nauc_mrr_at_100_diff1
      value: 32.18470462640416
    - type: nauc_mrr_at_100_max
      value: 19.969167766004155
    - type: nauc_mrr_at_100_std
      value: 0.22192687584423115
    - type: nauc_mrr_at_10_diff1
      value: 32.09991820831007
    - type: nauc_mrr_at_10_max
      value: 19.739187658158095
    - type: nauc_mrr_at_10_std
      value: -0.2495140041359092
    - type: nauc_mrr_at_1_diff1
      value: 34.08999204509866
    - type: nauc_mrr_at_1_max
      value: 16.991478512680224
    - type: nauc_mrr_at_1_std
      value: -1.7552861996068096
    - type: nauc_mrr_at_20_diff1
      value: 32.15333867489741
    - type: nauc_mrr_at_20_max
      value: 20.020143250873225
    - type: nauc_mrr_at_20_std
      value: 0.16862155425262013
    - type: nauc_mrr_at_3_diff1
      value: 32.21444644438222
    - type: nauc_mrr_at_3_max
      value: 18.21605348829081
    - type: nauc_mrr_at_3_std
      value: -1.6925892502509188
    - type: nauc_mrr_at_5_diff1
      value: 32.0478706880025
    - type: nauc_mrr_at_5_max
      value: 19.148865007333306
    - type: nauc_mrr_at_5_std
      value: -0.8802261956751949
    - type: nauc_ndcg_at_1000_diff1
      value: 31.983119738355253
    - type: nauc_ndcg_at_1000_max
      value: 21.86567501654561
    - type: nauc_ndcg_at_1000_std
      value: 2.0860659105814148
    - type: nauc_ndcg_at_100_diff1
      value: 31.746023533636002
    - type: nauc_ndcg_at_100_max
      value: 22.638912158683294
    - type: nauc_ndcg_at_100_std
      value: 3.052454394775229
    - type: nauc_ndcg_at_10_diff1
      value: 31.778039167442216
    - type: nauc_ndcg_at_10_max
      value: 21.36084508699706
    - type: nauc_ndcg_at_10_std
      value: 0.16693686698101765
    - type: nauc_ndcg_at_1_diff1
      value: 34.19354942363811
    - type: nauc_ndcg_at_1_max
      value: 16.848591473066378
    - type: nauc_ndcg_at_1_std
      value: -1.7454800127927512
    - type: nauc_ndcg_at_20_diff1
      value: 31.77653905325226
    - type: nauc_ndcg_at_20_max
      value: 22.61652208672153
    - type: nauc_ndcg_at_20_std
      value: 1.9910242035042571
    - type: nauc_ndcg_at_3_diff1
      value: 31.611292003047026
    - type: nauc_ndcg_at_3_max
      value: 17.664647025493103
    - type: nauc_ndcg_at_3_std
      value: -3.2746665435363482
    - type: nauc_ndcg_at_5_diff1
      value: 31.44128924743772
    - type: nauc_ndcg_at_5_max
      value: 19.652825980411436
    - type: nauc_ndcg_at_5_std
      value: -1.7539721730598645
    - type: nauc_precision_at_1000_diff1
      value: 2.096637497842706
    - type: nauc_precision_at_1000_max
      value: 15.200656933478845
    - type: nauc_precision_at_1000_std
      value: 19.38757583859173
    - type: nauc_precision_at_100_diff1
      value: 8.3623454469704
    - type: nauc_precision_at_100_max
      value: 24.522778919091383
    - type: nauc_precision_at_100_std
      value: 24.992853351936056
    - type: nauc_precision_at_10_diff1
      value: 22.246801149334065
    - type: nauc_precision_at_10_max
      value: 25.72788595807844
    - type: nauc_precision_at_10_std
      value: 10.335074726940642
    - type: nauc_precision_at_1_diff1
      value: 34.19354942363811
    - type: nauc_precision_at_1_max
      value: 16.848591473066378
    - type: nauc_precision_at_1_std
      value: -1.7454800127927512
    - type: nauc_precision_at_20_diff1
      value: 18.201890751037624
    - type: nauc_precision_at_20_max
      value: 28.207641511669657
    - type: nauc_precision_at_20_std
      value: 17.62549448063055
    - type: nauc_precision_at_3_diff1
      value: 28.262955611874673
    - type: nauc_precision_at_3_max
      value: 19.7314384498553
    - type: nauc_precision_at_3_std
      value: -0.15343939521694802
    - type: nauc_precision_at_5_diff1
      value: 25.546944946047333
    - type: nauc_precision_at_5_max
      value: 23.209224602801903
    - type: nauc_precision_at_5_std
      value: 4.096562516124445
    - type: nauc_recall_at_1000_diff1
      value: 26.810486933487848
    - type: nauc_recall_at_1000_max
      value: 62.062724387206416
    - type: nauc_recall_at_1000_std
      value: 72.53854144185586
    - type: nauc_recall_at_100_diff1
      value: 24.30748295669883
    - type: nauc_recall_at_100_max
      value: 47.86108978852899
    - type: nauc_recall_at_100_std
      value: 41.70104695267924
    - type: nauc_recall_at_10_diff1
      value: 28.014038418716364
    - type: nauc_recall_at_10_max
      value: 27.454742318511876
    - type: nauc_recall_at_10_std
      value: 6.129323504299465
    - type: nauc_recall_at_1_diff1
      value: 33.91219452872979
    - type: nauc_recall_at_1_max
      value: 15.243617612429572
    - type: nauc_recall_at_1_std
      value: -4.118372460673027
    - type: nauc_recall_at_20_diff1
      value: 27.51152553934221
    - type: nauc_recall_at_20_max
      value: 35.04009531047778
    - type: nauc_recall_at_20_std
      value: 16.086467991188023
    - type: nauc_recall_at_3_diff1
      value: 28.528898212602833
    - type: nauc_recall_at_3_max
      value: 17.667467627988895
    - type: nauc_recall_at_3_std
      value: -3.354082134238416
    - type: nauc_recall_at_5_diff1
      value: 27.54111394521828
    - type: nauc_recall_at_5_max
      value: 21.864229857719994
    - type: nauc_recall_at_5_std
      value: -0.010012005902089142
    - type: ndcg_at_1
      value: 27.868
    - type: ndcg_at_10
      value: 45.429
    - type: ndcg_at_100
      value: 50.676
    - type: ndcg_at_1000
      value: 51.727999999999994
    - type: ndcg_at_20
      value: 47.818
    - type: ndcg_at_3
      value: 37.079
    - type: ndcg_at_5
      value: 41.711
    - type: precision_at_1
      value: 27.868
    - type: precision_at_10
      value: 7.853000000000001
    - type: precision_at_100
      value: 1.079
    - type: precision_at_1000
      value: 0.11800000000000001
    - type: precision_at_20
      value: 4.486
    - type: precision_at_3
      value: 17.207
    - type: precision_at_5
      value: 12.943
    - type: recall_at_1
      value: 24.348
    - type: recall_at_10
      value: 65.667
    - type: recall_at_100
      value: 89.047
    - type: recall_at_1000
      value: 96.937
    - type: recall_at_20
      value: 74.611
    - type: recall_at_3
      value: 44.124
    - type: recall_at_5
      value: 54.847
    task:
      type: Retrieval
  - dataset:
      config: english
      name: MTEB PublicHealthQA (english)
      revision: main
      split: test
      type: xhluca/publichealth-qa
    metrics:
    - type: main_score
      value: 81.797
    - type: map_at_1
      value: 67.44200000000001
    - type: map_at_10
      value: 77.40899999999999
    - type: map_at_100
      value: 77.58800000000001
    - type: map_at_1000
      value: 77.59700000000001
    - type: map_at_20
      value: 77.563
    - type: map_at_3
      value: 75.775
    - type: map_at_5
      value: 76.676
    - type: mrr_at_1
      value: 67.44186046511628
    - type: mrr_at_10
      value: 77.40933001107419
    - type: mrr_at_100
      value: 77.58758776090153
    - type: mrr_at_1000
      value: 77.59701476623081
    - type: mrr_at_20
      value: 77.56332082460221
    - type: mrr_at_3
      value: 75.7751937984496
    - type: mrr_at_5
      value: 76.67635658914729
    - type: nauc_map_at_1000_diff1
      value: 68.03862212120946
    - type: nauc_map_at_1000_max
      value: 45.571493373890284
    - type: nauc_map_at_1000_std
      value: -9.513610168308675
    - type: nauc_map_at_100_diff1
      value: 68.04692169460982
    - type: nauc_map_at_100_max
      value: 45.597744584746174
    - type: nauc_map_at_100_std
      value: -9.46079106577722
    - type: nauc_map_at_10_diff1
      value: 68.12206434240572
    - type: nauc_map_at_10_max
      value: 45.87818916623179
    - type: nauc_map_at_10_std
      value: -9.07755836461079
    - type: nauc_map_at_1_diff1
      value: 67.12290625195008
    - type: nauc_map_at_1_max
      value: 41.961375907271766
    - type: nauc_map_at_1_std
      value: -14.305894005739376
    - type: nauc_map_at_20_diff1
      value: 68.03994283236055
    - type: nauc_map_at_20_max
      value: 45.55410799331842
    - type: nauc_map_at_20_std
      value: -9.446523820020174
    - type: nauc_map_at_3_diff1
      value: 68.37489368079838
    - type: nauc_map_at_3_max
      value: 46.36986654238148
    - type: nauc_map_at_3_std
      value: -10.310951850957865
    - type: nauc_map_at_5_diff1
      value: 67.59677966909759
    - type: nauc_map_at_5_max
      value: 44.92160517102712
    - type: nauc_map_at_5_std
      value: -9.80872574347567
    - type: nauc_mrr_at_1000_diff1
      value: 68.03866688403615
    - type: nauc_mrr_at_1000_max
      value: 45.571464182248114
    - type: nauc_mrr_at_1000_std
      value: -9.513668903745707
    - type: nauc_mrr_at_100_diff1
      value: 68.04692169460982
    - type: nauc_mrr_at_100_max
      value: 45.597744584746174
    - type: nauc_mrr_at_100_std
      value: -9.46079106577722
    - type: nauc_mrr_at_10_diff1
      value: 68.12206434240572
    - type: nauc_mrr_at_10_max
      value: 45.87818916623179
    - type: nauc_mrr_at_10_std
      value: -9.07755836461079
    - type: nauc_mrr_at_1_diff1
      value: 67.12290625195008
    - type: nauc_mrr_at_1_max
      value: 41.961375907271766
    - type: nauc_mrr_at_1_std
      value: -14.305894005739376
    - type: nauc_mrr_at_20_diff1
      value: 68.03994283236055
    - type: nauc_mrr_at_20_max
      value: 45.55410799331842
    - type: nauc_mrr_at_20_std
      value: -9.446523820020174
    - type: nauc_mrr_at_3_diff1
      value: 68.37489368079838
    - type: nauc_mrr_at_3_max
      value: 46.36986654238148
    - type: nauc_mrr_at_3_std
      value: -10.310951850957865
    - type: nauc_mrr_at_5_diff1
      value: 67.59677966909759
    - type: nauc_mrr_at_5_max
      value: 44.92160517102712
    - type: nauc_mrr_at_5_std
      value: -9.80872574347567
    - type: nauc_ndcg_at_1000_diff1
      value: 68.19001086715403
    - type: nauc_ndcg_at_1000_max
      value: 46.15089790137622
    - type: nauc_ndcg_at_1000_std
      value: -8.412159613801633
    - type: nauc_ndcg_at_100_diff1
      value: 68.38436319007278
    - type: nauc_ndcg_at_100_max
      value: 46.7399567648645
    - type: nauc_ndcg_at_100_std
      value: -7.226231881646415
    - type: nauc_ndcg_at_10_diff1
      value: 68.66691333519046
    - type: nauc_ndcg_at_10_max
      value: 47.676855724705206
    - type: nauc_ndcg_at_10_std
      value: -5.73932115133516
    - type: nauc_ndcg_at_1_diff1
      value: 67.12290625195008
    - type: nauc_ndcg_at_1_max
      value: 41.961375907271766
    - type: nauc_ndcg_at_1_std
      value: -14.305894005739376
    - type: nauc_ndcg_at_20_diff1
      value: 68.2939167825507
    - type: nauc_ndcg_at_20_max
      value: 46.24310319611011
    - type: nauc_ndcg_at_20_std
      value: -7.125543051802564
    - type: nauc_ndcg_at_3_diff1
      value: 68.80845744009801
    - type: nauc_ndcg_at_3_max
      value: 48.06608134910292
    - type: nauc_ndcg_at_3_std
      value: -9.416751601725604
    - type: nauc_ndcg_at_5_diff1
      value: 67.20191468584295
    - type: nauc_ndcg_at_5_max
      value: 45.17104294409719
    - type: nauc_ndcg_at_5_std
      value: -8.11265697724823
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_100_diff1
      value: 86.14085746500498
    - type: nauc_precision_at_100_max
      value: 100.0
    - type: nauc_precision_at_100_std
      value: 100.0
    - type: nauc_precision_at_10_diff1
      value: 76.20567449736176
    - type: nauc_precision_at_10_max
      value: 70.13176535200981
    - type: nauc_precision_at_10_std
      value: 38.95128572868472
    - type: nauc_precision_at_1_diff1
      value: 67.12290625195008
    - type: nauc_precision_at_1_max
      value: 41.961375907271766
    - type: nauc_precision_at_1_std
      value: -14.305894005739376
    - type: nauc_precision_at_20_diff1
      value: 73.74993491997736
    - type: nauc_precision_at_20_max
      value: 54.67254536177645
    - type: nauc_precision_at_20_std
      value: 49.85551772921538
    - type: nauc_precision_at_3_diff1
      value: 70.72764096781087
    - type: nauc_precision_at_3_max
      value: 55.67372625764705
    - type: nauc_precision_at_3_std
      value: -5.745071196827823
    - type: nauc_precision_at_5_diff1
      value: 64.27540794356823
    - type: nauc_precision_at_5_max
      value: 45.6262640317178
    - type: nauc_precision_at_5_std
      value: 2.0638422618860512
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: 86.14085746500531
    - type: nauc_recall_at_100_max
      value: 100.0
    - type: nauc_recall_at_100_std
      value: 100.0
    - type: nauc_recall_at_10_diff1
      value: 76.20567449736204
    - type: nauc_recall_at_10_max
      value: 70.13176535201025
    - type: nauc_recall_at_10_std
      value: 38.951285728684546
    - type: nauc_recall_at_1_diff1
      value: 67.12290625195008
    - type: nauc_recall_at_1_max
      value: 41.961375907271766
    - type: nauc_recall_at_1_std
      value: -14.305894005739376
    - type: nauc_recall_at_20_diff1
      value: 73.74993491997758
    - type: nauc_recall_at_20_max
      value: 54.67254536177716
    - type: nauc_recall_at_20_std
      value: 49.85551772921467
    - type: nauc_recall_at_3_diff1
      value: 70.72764096781106
    - type: nauc_recall_at_3_max
      value: 55.67372625764696
    - type: nauc_recall_at_3_std
      value: -5.745071196827833
    - type: nauc_recall_at_5_diff1
      value: 64.27540794356815
    - type: nauc_recall_at_5_max
      value: 45.626264031717625
    - type: nauc_recall_at_5_std
      value: 2.06384226188602
    - type: ndcg_at_1
      value: 67.44200000000001
    - type: ndcg_at_10
      value: 81.797
    - type: ndcg_at_100
      value: 82.582
    - type: ndcg_at_1000
      value: 82.749
    - type: ndcg_at_20
      value: 82.375
    - type: ndcg_at_3
      value: 78.41900000000001
    - type: ndcg_at_5
      value: 80.07
    - type: precision_at_1
      value: 67.44200000000001
    - type: precision_at_10
      value: 9.535
    - type: precision_at_100
      value: 0.988
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_20
      value: 4.884
    - type: precision_at_3
      value: 28.682000000000002
    - type: precision_at_5
      value: 18.023
    - type: recall_at_1
      value: 67.44200000000001
    - type: recall_at_10
      value: 95.34899999999999
    - type: recall_at_100
      value: 98.837
    - type: recall_at_1000
      value: 100.0
    - type: recall_at_20
      value: 97.674
    - type: recall_at_3
      value: 86.047
    - type: recall_at_5
      value: 90.116
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB QuoraRetrieval (default)
      revision: e4e08e0b7dbe3c8700f0daef558ff32256715259
      split: test
      type: mteb/quora
    metrics:
    - type: main_score
      value: 88.57199999999999
    - type: map_at_1
      value: 71.039
    - type: map_at_10
      value: 84.88900000000001
    - type: map_at_100
      value: 85.508
    - type: map_at_1000
      value: 85.524
    - type: map_at_20
      value: 85.302
    - type: map_at_3
      value: 81.894
    - type: map_at_5
      value: 83.8
    - type: mrr_at_1
      value: 81.78
    - type: mrr_at_10
      value: 87.8229365079363
    - type: mrr_at_100
      value: 87.91981638363609
    - type: mrr_at_1000
      value: 87.92063508831636
    - type: mrr_at_20
      value: 87.89576415509134
    - type: mrr_at_3
      value: 86.88499999999978
    - type: mrr_at_5
      value: 87.54249999999972
    - type: nauc_map_at_1000_diff1
      value: 76.15890287923096
    - type: nauc_map_at_1000_max
      value: 36.128747651916996
    - type: nauc_map_at_1000_std
      value: -48.66753596117505
    - type: nauc_map_at_100_diff1
      value: 76.16493038931165
    - type: nauc_map_at_100_max
      value: 36.09495057926168
    - type: nauc_map_at_100_std
      value: -48.723830300602586
    - type: nauc_map_at_10_diff1
      value: 76.36797035099488
    - type: nauc_map_at_10_max
      value: 35.620469333933464
    - type: nauc_map_at_10_std
      value: -50.54189078709537
    - type: nauc_map_at_1_diff1
      value: 79.8895751613965
    - type: nauc_map_at_1_max
      value: 26.317532572218223
    - type: nauc_map_at_1_std
      value: -44.938160229108206
    - type: nauc_map_at_20_diff1
      value: 76.24244671018226
    - type: nauc_map_at_20_max
      value: 36.001635565564364
    - type: nauc_map_at_20_std
      value: -49.3849748462351
    - type: nauc_map_at_3_diff1
      value: 76.65833912779706
    - type: nauc_map_at_3_max
      value: 32.98606836293959
    - type: nauc_map_at_3_std
      value: -52.50628417471894
    - type: nauc_map_at_5_diff1
      value: 76.61272599340525
    - type: nauc_map_at_5_max
      value: 34.74469655483763
    - type: nauc_map_at_5_std
      value: -51.913131454588054
    - type: nauc_mrr_at_1000_diff1
      value: 76.7068128582022
    - type: nauc_mrr_at_1000_max
      value: 39.109592270843066
    - type: nauc_mrr_at_1000_std
      value: -45.26766550271522
    - type: nauc_mrr_at_100_diff1
      value: 76.70661450396209
    - type: nauc_mrr_at_100_max
      value: 39.111095758039355
    - type: nauc_mrr_at_100_std
      value: -45.26836021466902
    - type: nauc_mrr_at_10_diff1
      value: 76.70726141027455
    - type: nauc_mrr_at_10_max
      value: 39.17777339514055
    - type: nauc_mrr_at_10_std
      value: -45.41161126837498
    - type: nauc_mrr_at_1_diff1
      value: 77.71262801682967
    - type: nauc_mrr_at_1_max
      value: 38.287583279692356
    - type: nauc_mrr_at_1_std
      value: -43.29857832293737
    - type: nauc_mrr_at_20_diff1
      value: 76.7037527994321
    - type: nauc_mrr_at_20_max
      value: 39.1385505965502
    - type: nauc_mrr_at_20_std
      value: -45.302717228670424
    - type: nauc_mrr_at_3_diff1
      value: 76.44715349862805
    - type: nauc_mrr_at_3_max
      value: 38.66923766796163
    - type: nauc_mrr_at_3_std
      value: -46.07826188003206
    - type: nauc_mrr_at_5_diff1
      value: 76.6862619651444
    - type: nauc_mrr_at_5_max
      value: 39.42029839009645
    - type: nauc_mrr_at_5_std
      value: -45.42521512596518
    - type: nauc_ndcg_at_1000_diff1
      value: 75.94606214928126
    - type: nauc_ndcg_at_1000_max
      value: 37.78639646594005
    - type: nauc_ndcg_at_1000_std
      value: -46.65092081733429
    - type: nauc_ndcg_at_100_diff1
      value: 75.95908789988027
    - type: nauc_ndcg_at_100_max
      value: 37.681560061965456
    - type: nauc_ndcg_at_100_std
      value: -46.86467727271376
    - type: nauc_ndcg_at_10_diff1
      value: 76.09039824441281
    - type: nauc_ndcg_at_10_max
      value: 36.98935573651128
    - type: nauc_ndcg_at_10_std
      value: -49.89313085062566
    - type: nauc_ndcg_at_1_diff1
      value: 77.731542287149
    - type: nauc_ndcg_at_1_max
      value: 38.21475789687958
    - type: nauc_ndcg_at_1_std
      value: -43.23518829879814
    - type: nauc_ndcg_at_20_diff1
      value: 76.0333735368683
    - type: nauc_ndcg_at_20_max
      value: 37.5117691727701
    - type: nauc_ndcg_at_20_std
      value: -48.43247167069298
    - type: nauc_ndcg_at_3_diff1
      value: 75.32521926923286
    - type: nauc_ndcg_at_3_max
      value: 35.635616145975426
    - type: nauc_ndcg_at_3_std
      value: -50.277808575751536
    - type: nauc_ndcg_at_5_diff1
      value: 75.98733426779356
    - type: nauc_ndcg_at_5_max
      value: 36.64628740946612
    - type: nauc_ndcg_at_5_std
      value: -50.466293598058165
    - type: nauc_precision_at_1000_diff1
      value: -43.7530546029045
    - type: nauc_precision_at_1000_max
      value: -5.161360102935574
    - type: nauc_precision_at_1000_std
      value: 41.238651766827935
    - type: nauc_precision_at_100_diff1
      value: -43.384152578104406
    - type: nauc_precision_at_100_max
      value: -5.034918821151737
    - type: nauc_precision_at_100_std
      value: 39.84731397760794
    - type: nauc_precision_at_10_diff1
      value: -38.02145942820818
    - type: nauc_precision_at_10_max
      value: -0.20339619978834741
    - type: nauc_precision_at_10_std
      value: 27.826961259650158
    - type: nauc_precision_at_1_diff1
      value: 77.731542287149
    - type: nauc_precision_at_1_max
      value: 38.21475789687958
    - type: nauc_precision_at_1_std
      value: -43.23518829879814
    - type: nauc_precision_at_20_diff1
      value: -41.175410744014805
    - type: nauc_precision_at_20_max
      value: -2.431406075907586
    - type: nauc_precision_at_20_std
      value: 34.28163431050591
    - type: nauc_precision_at_3_diff1
      value: -18.20941252484291
    - type: nauc_precision_at_3_max
      value: 9.49505880687624
    - type: nauc_precision_at_3_std
      value: 5.21470816880769
    - type: nauc_precision_at_5_diff1
      value: -30.71663355802905
    - type: nauc_precision_at_5_max
      value: 4.250820844712598
    - type: nauc_precision_at_5_std
      value: 18.068800455982604
    - type: nauc_recall_at_1000_diff1
      value: 42.20093621124488
    - type: nauc_recall_at_1000_max
      value: 42.975727501073955
    - type: nauc_recall_at_1000_std
      value: 17.039145897932887
    - type: nauc_recall_at_100_diff1
      value: 71.01797230503367
    - type: nauc_recall_at_100_max
      value: 36.8913110697839
    - type: nauc_recall_at_100_std
      value: -46.789986224693166
    - type: nauc_recall_at_10_diff1
      value: 72.78216200857327
    - type: nauc_recall_at_10_max
      value: 34.447888880887575
    - type: nauc_recall_at_10_std
      value: -67.03966745406017
    - type: nauc_recall_at_1_diff1
      value: 79.8895751613965
    - type: nauc_recall_at_1_max
      value: 26.317532572218223
    - type: nauc_recall_at_1_std
      value: -44.938160229108206
    - type: nauc_recall_at_20_diff1
      value: 72.39748025024522
    - type: nauc_recall_at_20_max
      value: 37.28031232611157
    - type: nauc_recall_at_20_std
      value: -63.744619826134475
    - type: nauc_recall_at_3_diff1
      value: 72.4158737180374
    - type: nauc_recall_at_3_max
      value: 29.671800523250326
    - type: nauc_recall_at_3_std
      value: -59.47563372923962
    - type: nauc_recall_at_5_diff1
      value: 72.26170447475917
    - type: nauc_recall_at_5_max
      value: 33.23785397256845
    - type: nauc_recall_at_5_std
      value: -62.34801264606157
    - type: ndcg_at_1
      value: 81.77
    - type: ndcg_at_10
      value: 88.57199999999999
    - type: ndcg_at_100
      value: 89.755
    - type: ndcg_at_1000
      value: 89.852
    - type: ndcg_at_20
      value: 89.22099999999999
    - type: ndcg_at_3
      value: 85.707
    - type: ndcg_at_5
      value: 87.345
    - type: precision_at_1
      value: 81.77
    - type: precision_at_10
      value: 13.431000000000001
    - type: precision_at_100
      value: 1.529
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_20
      value: 7.124
    - type: precision_at_3
      value: 37.41
    - type: precision_at_5
      value: 24.684
    - type: recall_at_1
      value: 71.039
    - type: recall_at_10
      value: 95.537
    - type: recall_at_100
      value: 99.557
    - type: recall_at_1000
      value: 99.982
    - type: recall_at_20
      value: 97.603
    - type: recall_at_3
      value: 87.384
    - type: recall_at_5
      value: 91.927
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB RedditClustering (default)
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
      split: test
      type: mteb/reddit-clustering
    metrics:
    - type: main_score
      value: 51.59936496159815
    - type: v_measure
      value: 51.59936496159815
    - type: v_measure_std
      value: 4.565966577664143
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB RedditClusteringP2P (default)
      revision: 385e3cb46b4cfa89021f56c4380204149d0efe33
      split: test
      type: mteb/reddit-clustering-p2p
    metrics:
    - type: main_score
      value: 60.83096246995603
    - type: v_measure
      value: 60.83096246995603
    - type: v_measure_std
      value: 13.183082420642975
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB SCIDOCS (default)
      revision: f8c2fcf00f625baaa80f62ec5bd9e1fff3b8ae88
      split: test
      type: mteb/scidocs
    metrics:
    - type: main_score
      value: 20.278
    - type: map_at_1
      value: 4.573
    - type: map_at_10
      value: 12.081999999999999
    - type: map_at_100
      value: 14.229
    - type: map_at_1000
      value: 14.587
    - type: map_at_20
      value: 13.145999999999999
    - type: map_at_3
      value: 8.488
    - type: map_at_5
      value: 10.324
    - type: mrr_at_1
      value: 22.6
    - type: mrr_at_10
      value: 33.95575396825393
    - type: mrr_at_100
      value: 35.03843505353784
    - type: mrr_at_1000
      value: 35.092323037408
    - type: mrr_at_20
      value: 34.589859035013795
    - type: mrr_at_3
      value: 30.299999999999986
    - type: mrr_at_5
      value: 32.42999999999995
    - type: nauc_map_at_1000_diff1
      value: 15.47158773019753
    - type: nauc_map_at_1000_max
      value: 33.15677973691845
    - type: nauc_map_at_1000_std
      value: 22.069088941975316
    - type: nauc_map_at_100_diff1
      value: 15.5473749771496
    - type: nauc_map_at_100_max
      value: 33.11669390716216
    - type: nauc_map_at_100_std
      value: 21.902092120156556
    - type: nauc_map_at_10_diff1
      value: 15.598319272907935
    - type: nauc_map_at_10_max
      value: 31.02834975480241
    - type: nauc_map_at_10_std
      value: 17.48586034447307
    - type: nauc_map_at_1_diff1
      value: 24.716824356435037
    - type: nauc_map_at_1_max
      value: 25.609675193046776
    - type: nauc_map_at_1_std
      value: 7.726550604844593
    - type: nauc_map_at_20_diff1
      value: 15.421255798642786
    - type: nauc_map_at_20_max
      value: 32.57491990876195
    - type: nauc_map_at_20_std
      value: 19.87590330146735
    - type: nauc_map_at_3_diff1
      value: 18.233165819869967
    - type: nauc_map_at_3_max
      value: 28.423341132169515
    - type: nauc_map_at_3_std
      value: 9.36105104315201
    - type: nauc_map_at_5_diff1
      value: 17.147755240157387
    - type: nauc_map_at_5_max
      value: 29.750818593195355
    - type: nauc_map_at_5_std
      value: 13.474425753774613
    - type: nauc_mrr_at_1000_diff1
      value: 19.54973813770631
    - type: nauc_mrr_at_1000_max
      value: 28.445637386785215
    - type: nauc_mrr_at_1000_std
      value: 14.759817199201834
    - type: nauc_mrr_at_100_diff1
      value: 19.528262971483187
    - type: nauc_mrr_at_100_max
      value: 28.471618042623042
    - type: nauc_mrr_at_100_std
      value: 14.802649900373577
    - type: nauc_mrr_at_10_diff1
      value: 19.297787878540934
    - type: nauc_mrr_at_10_max
      value: 28.250197248199598
    - type: nauc_mrr_at_10_std
      value: 14.530515441921136
    - type: nauc_mrr_at_1_diff1
      value: 24.448279147241337
    - type: nauc_mrr_at_1_max
      value: 25.44984341914804
    - type: nauc_mrr_at_1_std
      value: 7.8912754194185
    - type: nauc_mrr_at_20_diff1
      value: 19.526532015966378
    - type: nauc_mrr_at_20_max
      value: 28.45090107869856
    - type: nauc_mrr_at_20_std
      value: 14.872405983073964
    - type: nauc_mrr_at_3_diff1
      value: 19.309620003727055
    - type: nauc_mrr_at_3_max
      value: 27.545469950426288
    - type: nauc_mrr_at_3_std
      value: 12.904936858178626
    - type: nauc_mrr_at_5_diff1
      value: 19.262661292664838
    - type: nauc_mrr_at_5_max
      value: 27.77287008915389
    - type: nauc_mrr_at_5_std
      value: 14.068995148507335
    - type: nauc_ndcg_at_1000_diff1
      value: 15.228929487905193
    - type: nauc_ndcg_at_1000_max
      value: 34.92476744512219
    - type: nauc_ndcg_at_1000_std
      value: 28.862558988104897
    - type: nauc_ndcg_at_100_diff1
      value: 15.71824526700594
    - type: nauc_ndcg_at_100_max
      value: 35.335966205958385
    - type: nauc_ndcg_at_100_std
      value: 29.265053975009824
    - type: nauc_ndcg_at_10_diff1
      value: 15.334175443268217
    - type: nauc_ndcg_at_10_max
      value: 32.04474177693103
    - type: nauc_ndcg_at_10_std
      value: 20.246349040690838
    - type: nauc_ndcg_at_1_diff1
      value: 24.448279147241337
    - type: nauc_ndcg_at_1_max
      value: 25.44984341914804
    - type: nauc_ndcg_at_1_std
      value: 7.8912754194185
    - type: nauc_ndcg_at_20_diff1
      value: 15.4150287559633
    - type: nauc_ndcg_at_20_max
      value: 34.028257354205486
    - type: nauc_ndcg_at_20_std
      value: 23.94574408901984
    - type: nauc_ndcg_at_3_diff1
      value: 17.449798425957905
    - type: nauc_ndcg_at_3_max
      value: 28.472381850170684
    - type: nauc_ndcg_at_3_std
      value: 11.534878901481072
    - type: nauc_ndcg_at_5_diff1
      value: 16.863645323278014
    - type: nauc_ndcg_at_5_max
      value: 30.00515223685507
    - type: nauc_ndcg_at_5_std
      value: 15.778660328214492
    - type: nauc_precision_at_1000_diff1
      value: 4.713757187643959
    - type: nauc_precision_at_1000_max
      value: 28.438129482659463
    - type: nauc_precision_at_1000_std
      value: 39.88656841872898
    - type: nauc_precision_at_100_diff1
      value: 10.086356192787497
    - type: nauc_precision_at_100_max
      value: 33.7661746052316
    - type: nauc_precision_at_100_std
      value: 41.39520819343154
    - type: nauc_precision_at_10_diff1
      value: 10.656776714725792
    - type: nauc_precision_at_10_max
      value: 32.31524121764866
    - type: nauc_precision_at_10_std
      value: 25.54547973903815
    - type: nauc_precision_at_1_diff1
      value: 24.448279147241337
    - type: nauc_precision_at_1_max
      value: 25.44984341914804
    - type: nauc_precision_at_1_std
      value: 7.8912754194185
    - type: nauc_precision_at_20_diff1
      value: 10.413346149454274
    - type: nauc_precision_at_20_max
      value: 34.53151230080728
    - type: nauc_precision_at_20_std
      value: 31.606365417824104
    - type: nauc_precision_at_3_diff1
      value: 15.157946205596032
    - type: nauc_precision_at_3_max
      value: 29.285029432750626
    - type: nauc_precision_at_3_std
      value: 12.641270832271559
    - type: nauc_precision_at_5_diff1
      value: 13.726235144512325
    - type: nauc_precision_at_5_max
      value: 30.48174953294508
    - type: nauc_precision_at_5_std
      value: 19.16196995148913
    - type: nauc_recall_at_1000_diff1
      value: 4.52213727715021
    - type: nauc_recall_at_1000_max
      value: 27.895720746906093
    - type: nauc_recall_at_1000_std
      value: 41.74948907995246
    - type: nauc_recall_at_100_diff1
      value: 9.948729646333705
    - type: nauc_recall_at_100_max
      value: 33.31174530944116
    - type: nauc_recall_at_100_std
      value: 41.82269139039194
    - type: nauc_recall_at_10_diff1
      value: 10.708140509065931
    - type: nauc_recall_at_10_max
      value: 32.18578429711753
    - type: nauc_recall_at_10_std
      value: 25.465993578536622
    - type: nauc_recall_at_1_diff1
      value: 24.716824356435037
    - type: nauc_recall_at_1_max
      value: 25.609675193046776
    - type: nauc_recall_at_1_std
      value: 7.726550604844593
    - type: nauc_recall_at_20_diff1
      value: 10.432417124902676
    - type: nauc_recall_at_20_max
      value: 34.396161706840886
    - type: nauc_recall_at_20_std
      value: 31.6442301437761
    - type: nauc_recall_at_3_diff1
      value: 15.2335776286663
    - type: nauc_recall_at_3_max
      value: 29.312743939019057
    - type: nauc_recall_at_3_std
      value: 12.508295313824938
    - type: nauc_recall_at_5_diff1
      value: 13.819038065126835
    - type: nauc_recall_at_5_max
      value: 30.38801944210637
    - type: nauc_recall_at_5_std
      value: 18.99078644070936
    - type: ndcg_at_1
      value: 22.6
    - type: ndcg_at_10
      value: 20.278
    - type: ndcg_at_100
      value: 28.701
    - type: ndcg_at_1000
      value: 34.681
    - type: ndcg_at_20
      value: 23.179
    - type: ndcg_at_3
      value: 18.879
    - type: ndcg_at_5
      value: 16.749
    - type: precision_at_1
      value: 22.6
    - type: precision_at_10
      value: 10.66
    - type: precision_at_100
      value: 2.289
    - type: precision_at_1000
      value: 0.372
    - type: precision_at_20
      value: 7.015000000000001
    - type: precision_at_3
      value: 17.732999999999997
    - type: precision_at_5
      value: 14.899999999999999
    - type: recall_at_1
      value: 4.573
    - type: recall_at_10
      value: 21.573
    - type: recall_at_100
      value: 46.5
    - type: recall_at_1000
      value: 75.558
    - type: recall_at_20
      value: 28.397
    - type: recall_at_3
      value: 10.783
    - type: recall_at_5
      value: 15.082999999999998
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SICK-R (default)
      revision: 20a6d6f312dd54037fe07a32d58e5e168867909d
      split: test
      type: mteb/sickr-sts
    metrics:
    - type: cosine_pearson
      value: 84.62498017213524
    - type: cosine_spearman
      value: 79.65689515219194
    - type: euclidean_pearson
      value: 81.88054634002948
    - type: euclidean_spearman
      value: 79.6568911391733
    - type: main_score
      value: 79.65689515219194
    - type: manhattan_pearson
      value: 81.80542963904064
    - type: manhattan_spearman
      value: 79.56424367841001
    - type: pearson
      value: 84.62498017213524
    - type: spearman
      value: 79.65689515219194
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS12 (default)
      revision: a0d554a64d88156834ff5ae9920b964011b16384
      split: test
      type: mteb/sts12-sts
    metrics:
    - type: cosine_pearson
      value: 84.72310952504792
    - type: cosine_spearman
      value: 76.22109828443048
    - type: euclidean_pearson
      value: 82.38443833180979
    - type: euclidean_spearman
      value: 76.21894143370454
    - type: main_score
      value: 76.22109828443048
    - type: manhattan_pearson
      value: 82.40542669545772
    - type: manhattan_spearman
      value: 76.28736748590586
    - type: pearson
      value: 84.72310952504792
    - type: spearman
      value: 76.22109828443048
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS13 (default)
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
      split: test
      type: mteb/sts13-sts
    metrics:
    - type: cosine_pearson
      value: 81.68062265316888
    - type: cosine_spearman
      value: 83.4553090866614
    - type: euclidean_pearson
      value: 82.40491202375253
    - type: euclidean_spearman
      value: 83.4553090866614
    - type: main_score
      value: 83.4553090866614
    - type: manhattan_pearson
      value: 82.22067409773605
    - type: manhattan_spearman
      value: 83.20448906783335
    - type: pearson
      value: 81.68062265316888
    - type: spearman
      value: 83.4553090866614
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS14 (default)
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
      split: test
      type: mteb/sts14-sts
    metrics:
    - type: cosine_pearson
      value: 81.57051225494406
    - type: cosine_spearman
      value: 80.39864986197945
    - type: euclidean_pearson
      value: 81.05178156883875
    - type: euclidean_spearman
      value: 80.39865535033431
    - type: main_score
      value: 80.39864986197945
    - type: manhattan_pearson
      value: 81.05410761923022
    - type: manhattan_spearman
      value: 80.44259250171525
    - type: pearson
      value: 81.57051225494406
    - type: spearman
      value: 80.39864986197945
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS15 (default)
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
      split: test
      type: mteb/sts15-sts
    metrics:
    - type: cosine_pearson
      value: 84.79212184526739
    - type: cosine_spearman
      value: 86.40909639583371
    - type: euclidean_pearson
      value: 85.87613482648442
    - type: euclidean_spearman
      value: 86.40909578136895
    - type: main_score
      value: 86.40909639583371
    - type: manhattan_pearson
      value: 85.74723618868677
    - type: manhattan_spearman
      value: 86.28775839228958
    - type: pearson
      value: 84.79212184526739
    - type: spearman
      value: 86.40909639583371
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STS16 (default)
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
      split: test
      type: mteb/sts16-sts
    metrics:
    - type: cosine_pearson
      value: 80.9001128553287
    - type: cosine_spearman
      value: 83.28982485088675
    - type: euclidean_pearson
      value: 82.42648548297315
    - type: euclidean_spearman
      value: 83.28990050342193
    - type: main_score
      value: 83.28982485088675
    - type: manhattan_pearson
      value: 82.25070148571425
    - type: manhattan_spearman
      value: 83.07757318740721
    - type: pearson
      value: 80.9001128553287
    - type: spearman
      value: 83.28982485088675
    task:
      type: STS
  - dataset:
      config: it-en
      name: MTEB STS17 (it-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 24.18877892078201
    - type: cosine_spearman
      value: 20.233596577843038
    - type: euclidean_pearson
      value: 24.542177362845315
    - type: euclidean_spearman
      value: 20.233596577843038
    - type: main_score
      value: 20.233596577843038
    - type: manhattan_pearson
      value: 24.01700616075699
    - type: manhattan_spearman
      value: 19.446659958484517
    - type: pearson
      value: 24.18877892078201
    - type: spearman
      value: 20.233596577843038
    task:
      type: STS
  - dataset:
      config: en-tr
      name: MTEB STS17 (en-tr)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 8.614199975001977
    - type: cosine_spearman
      value: 5.012961284277124
    - type: euclidean_pearson
      value: 8.84952193581556
    - type: euclidean_spearman
      value: 5.012961284277124
    - type: main_score
      value: 5.012961284277124
    - type: manhattan_pearson
      value: 8.745277048601178
    - type: manhattan_spearman
      value: 5.409735174524082
    - type: pearson
      value: 8.614199975001977
    - type: spearman
      value: 5.012961284277124
    task:
      type: STS
  - dataset:
      config: fr-en
      name: MTEB STS17 (fr-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 32.392432370287786
    - type: cosine_spearman
      value: 29.30493234698128
    - type: euclidean_pearson
      value: 32.966478634610255
    - type: euclidean_spearman
      value: 29.30493234698128
    - type: main_score
      value: 29.30493234698128
    - type: manhattan_pearson
      value: 32.755965728091894
    - type: manhattan_spearman
      value: 29.146714726559253
    - type: pearson
      value: 32.392432370287786
    - type: spearman
      value: 29.30493234698128
    task:
      type: STS
  - dataset:
      config: es-en
      name: MTEB STS17 (es-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 20.254702485801023
    - type: cosine_spearman
      value: 19.721956722605672
    - type: euclidean_pearson
      value: 19.871717953344167
    - type: euclidean_spearman
      value: 19.721956722605672
    - type: main_score
      value: 19.721956722605672
    - type: manhattan_pearson
      value: 20.449457320012122
    - type: manhattan_spearman
      value: 20.169665776497684
    - type: pearson
      value: 20.254702485801023
    - type: spearman
      value: 19.721956722605672
    task:
      type: STS
  - dataset:
      config: nl-en
      name: MTEB STS17 (nl-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 28.074886980533577
    - type: cosine_spearman
      value: 24.306393355436498
    - type: euclidean_pearson
      value: 29.01202135632306
    - type: euclidean_spearman
      value: 24.306393355436498
    - type: main_score
      value: 24.306393355436498
    - type: manhattan_pearson
      value: 29.1296157400599
    - type: manhattan_spearman
      value: 23.73491100295491
    - type: pearson
      value: 28.074886980533577
    - type: spearman
      value: 24.306393355436498
    task:
      type: STS
  - dataset:
      config: en-ar
      name: MTEB STS17 (en-ar)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: -0.5773611433810728
    - type: cosine_spearman
      value: -1.0982086986987292
    - type: euclidean_pearson
      value: -0.5206158458966739
    - type: euclidean_spearman
      value: -1.0982086986987292
    - type: main_score
      value: -1.0982086986987292
    - type: manhattan_pearson
      value: -1.0668301997346301
    - type: manhattan_spearman
      value: -0.8412954712140625
    - type: pearson
      value: -0.5773611433810728
    - type: spearman
      value: -1.0982086986987292
    task:
      type: STS
  - dataset:
      config: en-en
      name: MTEB STS17 (en-en)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 86.27108126511854
    - type: cosine_spearman
      value: 86.53957993982179
    - type: euclidean_pearson
      value: 87.62799362362965
    - type: euclidean_spearman
      value: 86.53957993982179
    - type: main_score
      value: 86.53957993982179
    - type: manhattan_pearson
      value: 87.6959515498115
    - type: manhattan_spearman
      value: 86.64863324136145
    - type: pearson
      value: 86.27108126511854
    - type: spearman
      value: 86.53957993982179
    task:
      type: STS
  - dataset:
      config: en-de
      name: MTEB STS17 (en-de)
      revision: faeb762787bd10488a50c8b5be4a3b82e411949c
      split: test
      type: mteb/sts17-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 26.150575010131767
    - type: cosine_spearman
      value: 22.06712968681051
    - type: euclidean_pearson
      value: 26.604960551656553
    - type: euclidean_spearman
      value: 22.06712968681051
    - type: main_score
      value: 22.06712968681051
    - type: manhattan_pearson
      value: 26.88338799013417
    - type: manhattan_spearman
      value: 22.431306979297936
    - type: pearson
      value: 26.150575010131767
    - type: spearman
      value: 22.06712968681051
    task:
      type: STS
  - dataset:
      config: es-en
      name: MTEB STS22 (es-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 56.43553760517022
    - type: cosine_spearman
      value: 61.54782397245725
    - type: euclidean_pearson
      value: 57.49144139445497
    - type: euclidean_spearman
      value: 61.54782397245725
    - type: main_score
      value: 61.54782397245725
    - type: manhattan_pearson
      value: 57.23292330897806
    - type: manhattan_spearman
      value: 61.072557803031756
    - type: pearson
      value: 56.43553760517022
    - type: spearman
      value: 61.54782397245725
    task:
      type: STS
  - dataset:
      config: de-en
      name: MTEB STS22 (de-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 42.54975380534044
    - type: cosine_spearman
      value: 46.810373173640016
    - type: euclidean_pearson
      value: 45.28349759462344
    - type: euclidean_spearman
      value: 46.810373173640016
    - type: main_score
      value: 46.810373173640016
    - type: manhattan_pearson
      value: 46.16729933212417
    - type: manhattan_spearman
      value: 46.249145972529426
    - type: pearson
      value: 42.54975380534044
    - type: spearman
      value: 46.810373173640016
    task:
      type: STS
  - dataset:
      config: pl-en
      name: MTEB STS22 (pl-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 42.33771713953653
    - type: cosine_spearman
      value: 41.91423247431431
    - type: euclidean_pearson
      value: 43.03252081424651
    - type: euclidean_spearman
      value: 41.91423247431431
    - type: main_score
      value: 41.91423247431431
    - type: manhattan_pearson
      value: 41.39868682401022
    - type: manhattan_spearman
      value: 40.26808563589977
    - type: pearson
      value: 42.33771713953653
    - type: spearman
      value: 41.91423247431431
    task:
      type: STS
  - dataset:
      config: zh-en
      name: MTEB STS22 (zh-en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 48.18269761507854
    - type: cosine_spearman
      value: 50.6785956820247
    - type: euclidean_pearson
      value: 48.610255848327895
    - type: euclidean_spearman
      value: 50.6785956820247
    - type: main_score
      value: 50.6785956820247
    - type: manhattan_pearson
      value: 48.558643114423774
    - type: manhattan_spearman
      value: 50.40531034934534
    - type: pearson
      value: 48.18269761507854
    - type: spearman
      value: 50.6785956820247
    task:
      type: STS
  - dataset:
      config: en
      name: MTEB STS22 (en)
      revision: de9d86b3b84231dc21f76c7b7af1f28e2f57f6e3
      split: test
      type: mteb/sts22-crosslingual-sts
    metrics:
    - type: cosine_pearson
      value: 65.33289638983779
    - type: cosine_spearman
      value: 66.80763004782261
    - type: euclidean_pearson
      value: 67.9778359567448
    - type: euclidean_spearman
      value: 66.80763004782261
    - type: main_score
      value: 66.80763004782261
    - type: manhattan_pearson
      value: 68.49657450051612
    - type: manhattan_spearman
      value: 67.36431350100104
    - type: pearson
      value: 65.33289638983779
    - type: spearman
      value: 66.80763004782261
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB STSBenchmark (default)
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
      split: test
      type: mteb/stsbenchmark-sts
    metrics:
    - type: cosine_pearson
      value: 83.11688439720268
    - type: cosine_spearman
      value: 84.81184678969443
    - type: euclidean_pearson
      value: 84.74087810156583
    - type: euclidean_spearman
      value: 84.81189525583689
    - type: main_score
      value: 84.81184678969443
    - type: manhattan_pearson
      value: 84.55725669112154
    - type: manhattan_spearman
      value: 84.65629518341167
    - type: pearson
      value: 83.11688439720268
    - type: spearman
      value: 84.81184678969443
    task:
      type: STS
  - dataset:
      config: default
      name: MTEB SciDocsRR (default)
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
      split: test
      type: mteb/scidocs-reranking
    metrics:
    - type: main_score
      value: 85.79326406191477
    - type: map
      value: 85.79326406191477
    - type: mrr
      value: 96.01126632989377
    - type: nAUC_map_diff1
      value: -1.9960063892305635
    - type: nAUC_map_max
      value: 52.28855245081865
    - type: nAUC_map_std
      value: 66.17006861709118
    - type: nAUC_mrr_diff1
      value: 37.199120271359995
    - type: nAUC_mrr_max
      value: 83.25191469254256
    - type: nAUC_mrr_std
      value: 77.46103699775429
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SciFact (default)
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: main_score
      value: 70.781
    - type: map_at_1
      value: 56.15
    - type: map_at_10
      value: 66.068
    - type: map_at_100
      value: 66.606
    - type: map_at_1000
      value: 66.62700000000001
    - type: map_at_20
      value: 66.393
    - type: map_at_3
      value: 63.273999999999994
    - type: map_at_5
      value: 64.97699999999999
    - type: mrr_at_1
      value: 59.0
    - type: mrr_at_10
      value: 67.14100529100529
    - type: mrr_at_100
      value: 67.52274973457133
    - type: mrr_at_1000
      value: 67.54192035738791
    - type: mrr_at_20
      value: 67.33274717485244
    - type: mrr_at_3
      value: 64.77777777777779
    - type: mrr_at_5
      value: 66.39444444444446
    - type: nauc_map_at_1000_diff1
      value: 69.09690829345494
    - type: nauc_map_at_1000_max
      value: 50.70824678659478
    - type: nauc_map_at_1000_std
      value: 12.985689664716407
    - type: nauc_map_at_100_diff1
      value: 69.09924687148899
    - type: nauc_map_at_100_max
      value: 50.7337506059534
    - type: nauc_map_at_100_std
      value: 13.006358158080097
    - type: nauc_map_at_10_diff1
      value: 69.10893207723633
    - type: nauc_map_at_10_max
      value: 50.82945412215302
    - type: nauc_map_at_10_std
      value: 12.301972176252288
    - type: nauc_map_at_1_diff1
      value: 73.44608750237268
    - type: nauc_map_at_1_max
      value: 43.85599731941668
    - type: nauc_map_at_1_std
      value: 5.168582672370025
    - type: nauc_map_at_20_diff1
      value: 69.03143295499125
    - type: nauc_map_at_20_max
      value: 50.87627099813432
    - type: nauc_map_at_20_std
      value: 12.949145762693659
    - type: nauc_map_at_3_diff1
      value: 68.51699125737602
    - type: nauc_map_at_3_max
      value: 47.24273828014918
    - type: nauc_map_at_3_std
      value: 10.527871858030505
    - type: nauc_map_at_5_diff1
      value: 68.99381046083316
    - type: nauc_map_at_5_max
      value: 48.23432046662487
    - type: nauc_map_at_5_std
      value: 11.26317964615511
    - type: nauc_mrr_at_1000_diff1
      value: 69.79095737751194
    - type: nauc_mrr_at_1000_max
      value: 52.29374297281226
    - type: nauc_mrr_at_1000_std
      value: 15.13894630994255
    - type: nauc_mrr_at_100_diff1
      value: 69.79188651557479
    - type: nauc_mrr_at_100_max
      value: 52.315846778587485
    - type: nauc_mrr_at_100_std
      value: 15.15521556772456
    - type: nauc_mrr_at_10_diff1
      value: 69.73040149143365
    - type: nauc_mrr_at_10_max
      value: 52.50283292011064
    - type: nauc_mrr_at_10_std
      value: 15.069372709963726
    - type: nauc_mrr_at_1_diff1
      value: 73.20400506747669
    - type: nauc_mrr_at_1_max
      value: 50.10100713653324
    - type: nauc_mrr_at_1_std
      value: 12.827172631712807
    - type: nauc_mrr_at_20_diff1
      value: 69.72611022122446
    - type: nauc_mrr_at_20_max
      value: 52.464578579728396
    - type: nauc_mrr_at_20_std
      value: 15.208083826332011
    - type: nauc_mrr_at_3_diff1
      value: 69.1985393007592
    - type: nauc_mrr_at_3_max
      value: 50.81792260544604
    - type: nauc_mrr_at_3_std
      value: 14.332022309785128
    - type: nauc_mrr_at_5_diff1
      value: 69.50993371969486
    - type: nauc_mrr_at_5_max
      value: 51.64106508314771
    - type: nauc_mrr_at_5_std
      value: 15.358698285953956
    - type: nauc_ndcg_at_1000_diff1
      value: 68.78498267947889
    - type: nauc_ndcg_at_1000_max
      value: 52.57359656549474
    - type: nauc_ndcg_at_1000_std
      value: 15.538452139114579
    - type: nauc_ndcg_at_100_diff1
      value: 68.78480580681969
    - type: nauc_ndcg_at_100_max
      value: 53.32698295972621
    - type: nauc_ndcg_at_100_std
      value: 16.314594204287538
    - type: nauc_ndcg_at_10_diff1
      value: 68.33131449324236
    - type: nauc_ndcg_at_10_max
      value: 54.28393862675376
    - type: nauc_ndcg_at_10_std
      value: 14.440188370799826
    - type: nauc_ndcg_at_1_diff1
      value: 73.20400506747669
    - type: nauc_ndcg_at_1_max
      value: 50.10100713653324
    - type: nauc_ndcg_at_1_std
      value: 12.827172631712807
    - type: nauc_ndcg_at_20_diff1
      value: 68.15031723936488
    - type: nauc_ndcg_at_20_max
      value: 54.34582376960946
    - type: nauc_ndcg_at_20_std
      value: 16.386097496285466
    - type: nauc_ndcg_at_3_diff1
      value: 66.62543891885512
    - type: nauc_ndcg_at_3_max
      value: 49.462685336422716
    - type: nauc_ndcg_at_3_std
      value: 13.103889815379736
    - type: nauc_ndcg_at_5_diff1
      value: 67.82774135743375
    - type: nauc_ndcg_at_5_max
      value: 49.88962452868594
    - type: nauc_ndcg_at_5_std
      value: 13.512352768231784
    - type: nauc_precision_at_1000_diff1
      value: -24.455744262517246
    - type: nauc_precision_at_1000_max
      value: 29.194209973219483
    - type: nauc_precision_at_1000_std
      value: 53.45333740126795
    - type: nauc_precision_at_100_diff1
      value: -9.02373932196674
    - type: nauc_precision_at_100_max
      value: 39.31730511496725
    - type: nauc_precision_at_100_std
      value: 54.23916463691773
    - type: nauc_precision_at_10_diff1
      value: 16.237081629717945
    - type: nauc_precision_at_10_max
      value: 58.7670275934335
    - type: nauc_precision_at_10_std
      value: 41.54681432475195
    - type: nauc_precision_at_1_diff1
      value: 73.20400506747669
    - type: nauc_precision_at_1_max
      value: 50.10100713653324
    - type: nauc_precision_at_1_std
      value: 12.827172631712807
    - type: nauc_precision_at_20_diff1
      value: 6.486397217756261
    - type: nauc_precision_at_20_max
      value: 49.69520636107963
    - type: nauc_precision_at_20_std
      value: 48.330799457928784
    - type: nauc_precision_at_3_diff1
      value: 36.84804465641589
    - type: nauc_precision_at_3_max
      value: 48.964626880227385
    - type: nauc_precision_at_3_std
      value: 27.19694612530361
    - type: nauc_precision_at_5_diff1
      value: 29.08407956902661
    - type: nauc_precision_at_5_max
      value: 51.33405026324234
    - type: nauc_precision_at_5_std
      value: 35.64245923947663
    - type: nauc_recall_at_1000_diff1
      value: 100.0
    - type: nauc_recall_at_1000_max
      value: 12.278244631182748
    - type: nauc_recall_at_1000_std
      value: 86.92810457516407
    - type: nauc_recall_at_100_diff1
      value: 70.17611642358091
    - type: nauc_recall_at_100_max
      value: 76.0037348272645
    - type: nauc_recall_at_100_std
      value: 49.35606426478642
    - type: nauc_recall_at_10_diff1
      value: 63.26936092042931
    - type: nauc_recall_at_10_max
      value: 68.32557561359651
    - type: nauc_recall_at_10_std
      value: 18.518390629963744
    - type: nauc_recall_at_1_diff1
      value: 73.44608750237268
    - type: nauc_recall_at_1_max
      value: 43.85599731941668
    - type: nauc_recall_at_1_std
      value: 5.168582672370025
    - type: nauc_recall_at_20_diff1
      value: 61.67969675432364
    - type: nauc_recall_at_20_max
      value: 72.38960477117521
    - type: nauc_recall_at_20_std
      value: 31.439077902413377
    - type: nauc_recall_at_3_diff1
      value: 60.63550355416961
    - type: nauc_recall_at_3_max
      value: 45.64273650955856
    - type: nauc_recall_at_3_std
      value: 12.284278729729534
    - type: nauc_recall_at_5_diff1
      value: 62.23932232627379
    - type: nauc_recall_at_5_max
      value: 49.84844962005709
    - type: nauc_recall_at_5_std
      value: 15.689932929513267
    - type: ndcg_at_1
      value: 59.0
    - type: ndcg_at_10
      value: 70.781
    - type: ndcg_at_100
      value: 73.162
    - type: ndcg_at_1000
      value: 73.737
    - type: ndcg_at_20
      value: 71.722
    - type: ndcg_at_3
      value: 65.839
    - type: ndcg_at_5
      value: 68.557
    - type: precision_at_1
      value: 59.0
    - type: precision_at_10
      value: 9.467
    - type: precision_at_100
      value: 1.08
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: precision_at_20
      value: 4.983
    - type: precision_at_3
      value: 25.889
    - type: precision_at_5
      value: 17.267
    - type: recall_at_1
      value: 56.15
    - type: recall_at_10
      value: 84.222
    - type: recall_at_100
      value: 95.167
    - type: recall_at_1000
      value: 99.667
    - type: recall_at_20
      value: 87.6
    - type: recall_at_3
      value: 70.672
    - type: recall_at_5
      value: 77.694
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SprintDuplicateQuestions (default)
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
      split: test
      type: mteb/sprintduplicatequestions-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 99.84059405940594
    - type: cosine_accuracy_threshold
      value: 84.68618392944336
    - type: cosine_ap
      value: 96.16611732034018
    - type: cosine_f1
      value: 91.87279151943464
    - type: cosine_f1_threshold
      value: 84.60279107093811
    - type: cosine_precision
      value: 92.7624872579001
    - type: cosine_recall
      value: 91.0
    - type: dot_accuracy
      value: 99.84059405940594
    - type: dot_accuracy_threshold
      value: 84.68618392944336
    - type: dot_ap
      value: 96.16611732034019
    - type: dot_f1
      value: 91.87279151943464
    - type: dot_f1_threshold
      value: 84.60279107093811
    - type: dot_precision
      value: 92.7624872579001
    - type: dot_recall
      value: 91.0
    - type: euclidean_accuracy
      value: 99.84059405940594
    - type: euclidean_accuracy_threshold
      value: 55.34223914146423
    - type: euclidean_ap
      value: 96.16611732034018
    - type: euclidean_f1
      value: 91.87279151943464
    - type: euclidean_f1_threshold
      value: 55.49271106719971
    - type: euclidean_precision
      value: 92.7624872579001
    - type: euclidean_recall
      value: 91.0
    - type: main_score
      value: 96.16611732034019
    - type: manhattan_accuracy
      value: 99.84257425742574
    - type: manhattan_accuracy_threshold
      value: 853.6725997924805
    - type: manhattan_ap
      value: 96.1656773251653
    - type: manhattan_f1
      value: 91.96563921172309
    - type: manhattan_f1_threshold
      value: 861.8800163269043
    - type: manhattan_precision
      value: 92.95199182839632
    - type: manhattan_recall
      value: 91.0
    - type: max_accuracy
      value: 99.84257425742574
    - type: max_ap
      value: 96.16611732034019
    - type: max_f1
      value: 91.96563921172309
    - type: max_precision
      value: 92.95199182839632
    - type: max_recall
      value: 91.0
    - type: similarity_accuracy
      value: 99.84059405940594
    - type: similarity_accuracy_threshold
      value: 84.68618392944336
    - type: similarity_ap
      value: 96.16611732034018
    - type: similarity_f1
      value: 91.87279151943464
    - type: similarity_f1_threshold
      value: 84.60279107093811
    - type: similarity_precision
      value: 92.7624872579001
    - type: similarity_recall
      value: 91.0
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB StackExchangeClustering (default)
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
      split: test
      type: mteb/stackexchange-clustering
    metrics:
    - type: main_score
      value: 60.02250015167472
    - type: v_measure
      value: 60.02250015167472
    - type: v_measure_std
      value: 3.6859565919222845
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackExchangeClusteringP2P (default)
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
      split: test
      type: mteb/stackexchange-clustering-p2p
    metrics:
    - type: main_score
      value: 35.10613915314228
    - type: v_measure
      value: 35.10613915314228
    - type: v_measure_std
      value: 1.498102043653137
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB StackOverflowDupQuestions (default)
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
      split: test
      type: mteb/stackoverflowdupquestions-reranking
    metrics:
    - type: main_score
      value: 53.319664095625406
    - type: map
      value: 53.319664095625406
    - type: mrr
      value: 54.17945208386384
    - type: nAUC_map_diff1
      value: 40.00267732755458
    - type: nAUC_map_max
      value: 13.527855683708992
    - type: nAUC_map_std
      value: 9.041618850046866
    - type: nAUC_mrr_diff1
      value: 39.62764426841398
    - type: nAUC_mrr_max
      value: 14.339311048868952
    - type: nAUC_mrr_std
      value: 9.226051974058887
    task:
      type: Reranking
  - dataset:
      config: default
      name: MTEB SummEval (default)
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
      split: test
      type: mteb/summeval
    metrics:
    - type: cosine_pearson
      value: 30.5114222288775
    - type: cosine_spearman
      value: 30.485886091810034
    - type: dot_pearson
      value: 30.511430485066025
    - type: dot_spearman
      value: 30.49983580953373
    - type: main_score
      value: 30.485886091810034
    - type: pearson
      value: 30.5114222288775
    - type: spearman
      value: 30.485886091810034
    task:
      type: Summarization
  - dataset:
      config: default
      name: MTEB TRECCOVID (default)
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: main_score
      value: 77.75999999999999
    - type: map_at_1
      value: 0.23900000000000002
    - type: map_at_10
      value: 1.949
    - type: map_at_100
      value: 11.116
    - type: map_at_1000
      value: 26.684
    - type: map_at_20
      value: 3.45
    - type: map_at_3
      value: 0.651
    - type: map_at_5
      value: 1.0410000000000001
    - type: mrr_at_1
      value: 90.0
    - type: mrr_at_10
      value: 93.95238095238096
    - type: mrr_at_100
      value: 93.95238095238096
    - type: mrr_at_1000
      value: 93.95238095238096
    - type: mrr_at_20
      value: 93.95238095238096
    - type: mrr_at_3
      value: 93.66666666666667
    - type: mrr_at_5
      value: 93.66666666666667
    - type: nauc_map_at_1000_diff1
      value: -20.160585435121543
    - type: nauc_map_at_1000_max
      value: 38.8630983037078
    - type: nauc_map_at_1000_std
      value: 75.1359498809274
    - type: nauc_map_at_100_diff1
      value: -11.770967928603136
    - type: nauc_map_at_100_max
      value: 29.51565445249646
    - type: nauc_map_at_100_std
      value: 48.742088874863185
    - type: nauc_map_at_10_diff1
      value: 16.02141979872306
    - type: nauc_map_at_10_max
      value: 15.04591660201791
    - type: nauc_map_at_10_std
      value: 12.788311897845276
    - type: nauc_map_at_1_diff1
      value: 6.725038753955455
    - type: nauc_map_at_1_max
      value: 5.632652286527743
    - type: nauc_map_at_1_std
      value: -0.6518088466576922
    - type: nauc_map_at_20_diff1
      value: 10.282985568907463
    - type: nauc_map_at_20_max
      value: 17.483835968348743
    - type: nauc_map_at_20_std
      value: 18.33987447808943
    - type: nauc_map_at_3_diff1
      value: 10.44764101228141
    - type: nauc_map_at_3_max
      value: 8.393374035568426
    - type: nauc_map_at_3_std
      value: 4.3627693885700785
    - type: nauc_map_at_5_diff1
      value: 17.02341733651586
    - type: nauc_map_at_5_max
      value: 13.106044347786833
    - type: nauc_map_at_5_std
      value: 7.008036861123736
    - type: nauc_mrr_at_1000_diff1
      value: -32.12502848908622
    - type: nauc_mrr_at_1000_max
      value: 82.01327775204561
    - type: nauc_mrr_at_1000_std
      value: 64.92717822036941
    - type: nauc_mrr_at_100_diff1
      value: -32.12502848908622
    - type: nauc_mrr_at_100_max
      value: 82.01327775204561
    - type: nauc_mrr_at_100_std
      value: 64.92717822036941
    - type: nauc_mrr_at_10_diff1
      value: -32.12502848908622
    - type: nauc_mrr_at_10_max
      value: 82.01327775204561
    - type: nauc_mrr_at_10_std
      value: 64.92717822036941
    - type: nauc_mrr_at_1_diff1
      value: -39.09430438842211
    - type: nauc_mrr_at_1_max
      value: 78.2446311858077
    - type: nauc_mrr_at_1_std
      value: 64.51914098972921
    - type: nauc_mrr_at_20_diff1
      value: -32.12502848908622
    - type: nauc_mrr_at_20_max
      value: 82.01327775204561
    - type: nauc_mrr_at_20_std
      value: 64.92717822036941
    - type: nauc_mrr_at_3_diff1
      value: -28.175831736202845
    - type: nauc_mrr_at_3_max
      value: 82.82470883090078
    - type: nauc_mrr_at_3_std
      value: 65.25627794977638
    - type: nauc_mrr_at_5_diff1
      value: -28.175831736202845
    - type: nauc_mrr_at_5_max
      value: 82.82470883090078
    - type: nauc_mrr_at_5_std
      value: 65.25627794977638
    - type: nauc_ndcg_at_1000_diff1
      value: -18.54726131921605
    - type: nauc_ndcg_at_1000_max
      value: 29.95310477201888
    - type: nauc_ndcg_at_1000_std
      value: 70.82243454153097
    - type: nauc_ndcg_at_100_diff1
      value: -22.637249582808078
    - type: nauc_ndcg_at_100_max
      value: 36.348125192786654
    - type: nauc_ndcg_at_100_std
      value: 75.19596861423354
    - type: nauc_ndcg_at_10_diff1
      value: -19.91104943802517
    - type: nauc_ndcg_at_10_max
      value: 34.8418323803163
    - type: nauc_ndcg_at_10_std
      value: 57.580684501146926
    - type: nauc_ndcg_at_1_diff1
      value: -38.8728816184899
    - type: nauc_ndcg_at_1_max
      value: 26.635065216717795
    - type: nauc_ndcg_at_1_std
      value: 66.18954673606594
    - type: nauc_ndcg_at_20_diff1
      value: -19.199510111936828
    - type: nauc_ndcg_at_20_max
      value: 36.16805193195719
    - type: nauc_ndcg_at_20_std
      value: 64.03214954101703
    - type: nauc_ndcg_at_3_diff1
      value: -28.79507246353434
    - type: nauc_ndcg_at_3_max
      value: 29.623193200204902
    - type: nauc_ndcg_at_3_std
      value: 48.53958096552628
    - type: nauc_ndcg_at_5_diff1
      value: -20.153745604675404
    - type: nauc_ndcg_at_5_max
      value: 38.55119400658675
    - type: nauc_ndcg_at_5_std
      value: 52.05268467045925
    - type: nauc_precision_at_1000_diff1
      value: -16.27868015856243
    - type: nauc_precision_at_1000_max
      value: 31.57510838019923
    - type: nauc_precision_at_1000_std
      value: 57.73923801374279
    - type: nauc_precision_at_100_diff1
      value: -20.501173646320325
    - type: nauc_precision_at_100_max
      value: 40.777625226055484
    - type: nauc_precision_at_100_std
      value: 73.83079368622825
    - type: nauc_precision_at_10_diff1
      value: -9.965760097987248
    - type: nauc_precision_at_10_max
      value: 43.831250173983214
    - type: nauc_precision_at_10_std
      value: 59.253820671992926
    - type: nauc_precision_at_1_diff1
      value: -39.09430438842211
    - type: nauc_precision_at_1_max
      value: 78.2446311858077
    - type: nauc_precision_at_1_std
      value: 64.51914098972921
    - type: nauc_precision_at_20_diff1
      value: -8.638035851947166
    - type: nauc_precision_at_20_max
      value: 44.103880220277084
    - type: nauc_precision_at_20_std
      value: 64.70525093435604
    - type: nauc_precision_at_3_diff1
      value: -21.841031859772837
    - type: nauc_precision_at_3_max
      value: 44.674236578106004
    - type: nauc_precision_at_3_std
      value: 42.478227317825976
    - type: nauc_precision_at_5_diff1
      value: -6.236840001066146
    - type: nauc_precision_at_5_max
      value: 51.207388256616696
    - type: nauc_precision_at_5_std
      value: 48.96452464084871
    - type: nauc_recall_at_1000_diff1
      value: -10.99581357598733
    - type: nauc_recall_at_1000_max
      value: 24.78131457526207
    - type: nauc_recall_at_1000_std
      value: 58.616353090231456
    - type: nauc_recall_at_100_diff1
      value: -7.391122888251769
    - type: nauc_recall_at_100_max
      value: 13.48733379483525
    - type: nauc_recall_at_100_std
      value: 30.021453850557478
    - type: nauc_recall_at_10_diff1
      value: 18.655482095342737
    - type: nauc_recall_at_10_max
      value: 7.711145130239254
    - type: nauc_recall_at_10_std
      value: 4.714005963492534
    - type: nauc_recall_at_1_diff1
      value: 6.725038753955455
    - type: nauc_recall_at_1_max
      value: 5.632652286527743
    - type: nauc_recall_at_1_std
      value: -0.6518088466576922
    - type: nauc_recall_at_20_diff1
      value: 13.388708452075319
    - type: nauc_recall_at_20_max
      value: 7.968138289992421
    - type: nauc_recall_at_20_std
      value: 6.945001828898886
    - type: nauc_recall_at_3_diff1
      value: 13.1846212620345
    - type: nauc_recall_at_3_max
      value: 5.67166800633548
    - type: nauc_recall_at_3_std
      value: 0.4607538722304717
    - type: nauc_recall_at_5_diff1
      value: 20.396178452142838
    - type: nauc_recall_at_5_max
      value: 8.470737892964241
    - type: nauc_recall_at_5_std
      value: 1.3229988346689756
    - type: ndcg_at_1
      value: 84.0
    - type: ndcg_at_10
      value: 77.75999999999999
    - type: ndcg_at_100
      value: 58.162000000000006
    - type: ndcg_at_1000
      value: 52.235
    - type: ndcg_at_20
      value: 73.04
    - type: ndcg_at_3
      value: 79.061
    - type: ndcg_at_5
      value: 78.242
    - type: precision_at_1
      value: 90.0
    - type: precision_at_10
      value: 81.6
    - type: precision_at_100
      value: 59.540000000000006
    - type: precision_at_1000
      value: 22.918
    - type: precision_at_20
      value: 76.4
    - type: precision_at_3
      value: 83.333
    - type: precision_at_5
      value: 82.39999999999999
    - type: recall_at_1
      value: 0.23900000000000002
    - type: recall_at_10
      value: 2.1510000000000002
    - type: recall_at_100
      value: 14.457
    - type: recall_at_1000
      value: 49.112
    - type: recall_at_20
      value: 3.968
    - type: recall_at_3
      value: 0.672
    - type: recall_at_5
      value: 1.1079999999999999
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB Touche2020Retrieval.v3 (default)
      revision: 431886eaecc48f067a3975b70d0949ea2862463c
      split: test
      type: mteb/webis-touche2020-v3
    metrics:
    - type: main_score
      value: 56.196
    - type: map_at_1
      value: 2.946
    - type: map_at_10
      value: 18.725
    - type: map_at_100
      value: 36.925999999999995
    - type: map_at_1000
      value: 39.741
    - type: map_at_20
      value: 26.534000000000002
    - type: map_at_3
      value: 7.083
    - type: map_at_5
      value: 11.187999999999999
    - type: mrr_at_1
      value: 73.46938775510205
    - type: mrr_at_10
      value: 83.67346938775512
    - type: mrr_at_100
      value: 83.67346938775512
    - type: mrr_at_1000
      value: 83.67346938775512
    - type: mrr_at_20
      value: 83.67346938775512
    - type: mrr_at_3
      value: 81.6326530612245
    - type: mrr_at_5
      value: 83.67346938775512
    - type: nauc_map_at_1000_diff1
      value: -2.991437116771111
    - type: nauc_map_at_1000_max
      value: -11.67772152587661
    - type: nauc_map_at_1000_std
      value: 30.75490471184306
    - type: nauc_map_at_100_diff1
      value: -2.95737316254561
    - type: nauc_map_at_100_max
      value: -15.02583478654141
    - type: nauc_map_at_100_std
      value: 26.630398365349656
    - type: nauc_map_at_10_diff1
      value: -10.212425455350994
    - type: nauc_map_at_10_max
      value: -24.03187999524167
    - type: nauc_map_at_10_std
      value: -0.014679526577675323
    - type: nauc_map_at_1_diff1
      value: -20.82132515478208
    - type: nauc_map_at_1_max
      value: -40.886965604054176
    - type: nauc_map_at_1_std
      value: -23.05338042822077
    - type: nauc_map_at_20_diff1
      value: -5.077469934765774
    - type: nauc_map_at_20_max
      value: -15.699607051137168
    - type: nauc_map_at_20_std
      value: 7.679788317888087
    - type: nauc_map_at_3_diff1
      value: -7.8949208792660555
    - type: nauc_map_at_3_max
      value: -33.62859118751235
    - type: nauc_map_at_3_std
      value: -9.004325158650554
    - type: nauc_map_at_5_diff1
      value: -5.264771799791715
    - type: nauc_map_at_5_max
      value: -31.357780951814874
    - type: nauc_map_at_5_std
      value: -0.7165057953194318
    - type: nauc_mrr_at_1000_diff1
      value: -5.024511068781128
    - type: nauc_mrr_at_1000_max
      value: -40.77907972701954
    - type: nauc_mrr_at_1000_std
      value: 15.946175002676071
    - type: nauc_mrr_at_100_diff1
      value: -5.024511068781128
    - type: nauc_mrr_at_100_max
      value: -40.77907972701954
    - type: nauc_mrr_at_100_std
      value: 15.946175002676071
    - type: nauc_mrr_at_10_diff1
      value: -5.024511068781128
    - type: nauc_mrr_at_10_max
      value: -40.77907972701954
    - type: nauc_mrr_at_10_std
      value: 15.946175002676071
    - type: nauc_mrr_at_1_diff1
      value: -4.991894795838693
    - type: nauc_mrr_at_1_max
      value: -38.83508536411747
    - type: nauc_mrr_at_1_std
      value: 15.246738247246094
    - type: nauc_mrr_at_20_diff1
      value: -5.024511068781128
    - type: nauc_mrr_at_20_max
      value: -40.77907972701954
    - type: nauc_mrr_at_20_std
      value: 15.946175002676071
    - type: nauc_mrr_at_3_diff1
      value: -4.9009070566281245
    - type: nauc_mrr_at_3_max
      value: -39.257034415652896
    - type: nauc_mrr_at_3_std
      value: 17.02621296101872
    - type: nauc_mrr_at_5_diff1
      value: -5.024511068781128
    - type: nauc_mrr_at_5_max
      value: -40.77907972701954
    - type: nauc_mrr_at_5_std
      value: 15.946175002676071
    - type: nauc_ndcg_at_1000_diff1
      value: 4.877492348633252
    - type: nauc_ndcg_at_1000_max
      value: -3.2969805314117404
    - type: nauc_ndcg_at_1000_std
      value: 55.98792969695613
    - type: nauc_ndcg_at_100_diff1
      value: -0.038028291353188436
    - type: nauc_ndcg_at_100_max
      value: -23.001016457410532
    - type: nauc_ndcg_at_100_std
      value: 41.898883840979764
    - type: nauc_ndcg_at_10_diff1
      value: -5.1015740530562175
    - type: nauc_ndcg_at_10_max
      value: -8.7971501887686
    - type: nauc_ndcg_at_10_std
      value: 38.76126472444422
    - type: nauc_ndcg_at_1_diff1
      value: -8.898461488020045
    - type: nauc_ndcg_at_1_max
      value: -12.226428291827384
    - type: nauc_ndcg_at_1_std
      value: 20.89258738535739
    - type: nauc_ndcg_at_20_diff1
      value: -5.019424969386717
    - type: nauc_ndcg_at_20_max
      value: -8.40375826680385
    - type: nauc_ndcg_at_20_std
      value: 33.50966709609865
    - type: nauc_ndcg_at_3_diff1
      value: 0.22327484809688333
    - type: nauc_ndcg_at_3_max
      value: -13.27467982106787
    - type: nauc_ndcg_at_3_std
      value: 30.51511997926173
    - type: nauc_ndcg_at_5_diff1
      value: 0.09938628362624732
    - type: nauc_ndcg_at_5_max
      value: -17.931135627985192
    - type: nauc_ndcg_at_5_std
      value: 38.57726727005374
    - type: nauc_precision_at_1000_diff1
      value: 2.106041432080759
    - type: nauc_precision_at_1000_max
      value: 49.528293004180455
    - type: nauc_precision_at_1000_std
      value: 36.49921447274295
    - type: nauc_precision_at_100_diff1
      value: -1.225455548663038
    - type: nauc_precision_at_100_max
      value: 19.605316746110887
    - type: nauc_precision_at_100_std
      value: 71.37044623385614
    - type: nauc_precision_at_10_diff1
      value: -1.8080350322595757
    - type: nauc_precision_at_10_max
      value: -3.453940682448408
    - type: nauc_precision_at_10_std
      value: 36.75225348961599
    - type: nauc_precision_at_1_diff1
      value: -4.991894795838693
    - type: nauc_precision_at_1_max
      value: -38.83508536411747
    - type: nauc_precision_at_1_std
      value: 15.246738247246094
    - type: nauc_precision_at_20_diff1
      value: 11.092767632848723
    - type: nauc_precision_at_20_max
      value: 10.218443043089982
    - type: nauc_precision_at_20_std
      value: 47.63494142738728
    - type: nauc_precision_at_3_diff1
      value: 12.20603394911171
    - type: nauc_precision_at_3_max
      value: -17.251065315072193
    - type: nauc_precision_at_3_std
      value: 26.867651256647452
    - type: nauc_precision_at_5_diff1
      value: 10.093913963838736
    - type: nauc_precision_at_5_max
      value: -20.946372820355073
    - type: nauc_precision_at_5_std
      value: 42.58398961954329
    - type: nauc_recall_at_1000_diff1
      value: 27.541259514336
    - type: nauc_recall_at_1000_max
      value: 26.488575954326027
    - type: nauc_recall_at_1000_std
      value: 77.42345371512604
    - type: nauc_recall_at_100_diff1
      value: 0.3196527391909681
    - type: nauc_recall_at_100_max
      value: -24.479150613828303
    - type: nauc_recall_at_100_std
      value: 39.2629664046755
    - type: nauc_recall_at_10_diff1
      value: -12.59639639211954
    - type: nauc_recall_at_10_max
      value: -28.209370861454307
    - type: nauc_recall_at_10_std
      value: -7.833213547133838
    - type: nauc_recall_at_1_diff1
      value: -20.82132515478208
    - type: nauc_recall_at_1_max
      value: -40.886965604054176
    - type: nauc_recall_at_1_std
      value: -23.05338042822077
    - type: nauc_recall_at_20_diff1
      value: -5.180606615847058
    - type: nauc_recall_at_20_max
      value: -19.492523770094547
    - type: nauc_recall_at_20_std
      value: 3.0890655409078276
    - type: nauc_recall_at_3_diff1
      value: -7.4383614317036715
    - type: nauc_recall_at_3_max
      value: -33.467231727496504
    - type: nauc_recall_at_3_std
      value: -10.871143037448503
    - type: nauc_recall_at_5_diff1
      value: -6.729176537186017
    - type: nauc_recall_at_5_max
      value: -34.57305958555233
    - type: nauc_recall_at_5_std
      value: -4.486225513133468
    - type: ndcg_at_1
      value: 60.204
    - type: ndcg_at_10
      value: 56.196
    - type: ndcg_at_100
      value: 58.08
    - type: ndcg_at_1000
      value: 69.069
    - type: ndcg_at_20
      value: 50.604000000000006
    - type: ndcg_at_3
      value: 59.114
    - type: ndcg_at_5
      value: 59.52499999999999
    - type: precision_at_1
      value: 73.469
    - type: precision_at_10
      value: 63.26500000000001
    - type: precision_at_100
      value: 19.796
    - type: precision_at_1000
      value: 3.102
    - type: precision_at_20
      value: 49.592000000000006
    - type: precision_at_3
      value: 69.388
    - type: precision_at_5
      value: 70.612
    - type: recall_at_1
      value: 2.946
    - type: recall_at_10
      value: 22.479
    - type: recall_at_100
      value: 61.507
    - type: recall_at_1000
      value: 88.495
    - type: recall_at_20
      value: 34.344
    - type: recall_at_3
      value: 7.571
    - type: recall_at_5
      value: 12.606
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB ToxicConversationsClassification (default)
      revision: edfaf9da55d3dd50d43143d90c1ac476895ae6de
      split: test
      type: mteb/toxic_conversations_50k
    metrics:
    - type: accuracy
      value: 65.8447265625
    - type: ap
      value: 11.790127057253194
    - type: ap_weighted
      value: 11.790127057253194
    - type: f1
      value: 50.28742613560235
    - type: f1_weighted
      value: 73.24450181406255
    - type: main_score
      value: 65.8447265625
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TweetSentimentExtractionClassification (default)
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
      split: test
      type: mteb/tweet_sentiment_extraction
    metrics:
    - type: accuracy
      value: 61.349745331069606
    - type: f1
      value: 61.502480965412744
    - type: f1_weighted
      value: 60.39561856225271
    - type: main_score
      value: 61.349745331069606
    task:
      type: Classification
  - dataset:
      config: default
      name: MTEB TwentyNewsgroupsClustering (default)
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
      split: test
      type: mteb/twentynewsgroups-clustering
    metrics:
    - type: main_score
      value: 47.338360343180106
    - type: v_measure
      value: 47.338360343180106
    - type: v_measure_std
      value: 2.01314014968057
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB TwitterSemEval2015 (default)
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
      split: test
      type: mteb/twittersemeval2015-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 85.49204267747511
    - type: cosine_accuracy_threshold
      value: 86.85047030448914
    - type: cosine_ap
      value: 72.98051397210814
    - type: cosine_f1
      value: 66.8282725184996
    - type: cosine_f1_threshold
      value: 84.59665775299072
    - type: cosine_precision
      value: 64.69861660079052
    - type: cosine_recall
      value: 69.10290237467018
    - type: dot_accuracy
      value: 85.49204267747511
    - type: dot_accuracy_threshold
      value: 86.85047030448914
    - type: dot_ap
      value: 72.98051075246349
    - type: dot_f1
      value: 66.8282725184996
    - type: dot_f1_threshold
      value: 84.59665775299072
    - type: dot_precision
      value: 64.69861660079052
    - type: dot_recall
      value: 69.10290237467018
    - type: euclidean_accuracy
      value: 85.49204267747511
    - type: euclidean_accuracy_threshold
      value: 51.28260850906372
    - type: euclidean_ap
      value: 72.98052075606988
    - type: euclidean_f1
      value: 66.8282725184996
    - type: euclidean_f1_threshold
      value: 55.50377368927002
    - type: euclidean_precision
      value: 64.69861660079052
    - type: euclidean_recall
      value: 69.10290237467018
    - type: main_score
      value: 72.98052075606988
    - type: manhattan_accuracy
      value: 85.43839780652083
    - type: manhattan_accuracy_threshold
      value: 796.9008445739746
    - type: manhattan_ap
      value: 72.80895903518599
    - type: manhattan_f1
      value: 66.64168852254278
    - type: manhattan_f1_threshold
      value: 871.8400955200195
    - type: manhattan_precision
      value: 63.267725871472614
    - type: manhattan_recall
      value: 70.3957783641161
    - type: max_accuracy
      value: 85.49204267747511
    - type: max_ap
      value: 72.98052075606988
    - type: max_f1
      value: 66.8282725184996
    - type: max_precision
      value: 64.69861660079052
    - type: max_recall
      value: 70.3957783641161
    - type: similarity_accuracy
      value: 85.49204267747511
    - type: similarity_accuracy_threshold
      value: 86.85047030448914
    - type: similarity_ap
      value: 72.98051397210814
    - type: similarity_f1
      value: 66.8282725184996
    - type: similarity_f1_threshold
      value: 84.59665775299072
    - type: similarity_precision
      value: 64.69861660079052
    - type: similarity_recall
      value: 69.10290237467018
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB TwitterURLCorpus (default)
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
      split: test
      type: mteb/twitterurlcorpus-pairclassification
    metrics:
    - type: cosine_accuracy
      value: 88.4192959987581
    - type: cosine_accuracy_threshold
      value: 82.84748792648315
    - type: cosine_ap
      value: 84.98986658033178
    - type: cosine_f1
      value: 77.24466264970617
    - type: cosine_f1_threshold
      value: 81.41384720802307
    - type: cosine_precision
      value: 74.71578644409269
    - type: cosine_recall
      value: 79.95072374499537
    - type: dot_accuracy
      value: 88.4192959987581
    - type: dot_accuracy_threshold
      value: 82.84748792648315
    - type: dot_ap
      value: 84.98983415174361
    - type: dot_f1
      value: 77.24466264970617
    - type: dot_f1_threshold
      value: 81.41384720802307
    - type: dot_precision
      value: 74.71578644409269
    - type: dot_recall
      value: 79.95072374499537
    - type: euclidean_accuracy
      value: 88.4192959987581
    - type: euclidean_accuracy_threshold
      value: 58.57049226760864
    - type: euclidean_ap
      value: 84.9898314712826
    - type: euclidean_f1
      value: 77.24466264970617
    - type: euclidean_f1_threshold
      value: 60.96909046173096
    - type: euclidean_precision
      value: 74.71578644409269
    - type: euclidean_recall
      value: 79.95072374499537
    - type: main_score
      value: 84.98986658033178
    - type: manhattan_accuracy
      value: 88.4192959987581
    - type: manhattan_accuracy_threshold
      value: 907.758617401123
    - type: manhattan_ap
      value: 84.92522577660164
    - type: manhattan_f1
      value: 76.9788698516079
    - type: manhattan_f1_threshold
      value: 952.1110534667969
    - type: manhattan_precision
      value: 74.10758817242608
    - type: manhattan_recall
      value: 80.08161379735141
    - type: max_accuracy
      value: 88.4192959987581
    - type: max_ap
      value: 84.98986658033178
    - type: max_f1
      value: 77.24466264970617
    - type: max_precision
      value: 74.71578644409269
    - type: max_recall
      value: 80.08161379735141
    - type: similarity_accuracy
      value: 88.4192959987581
    - type: similarity_accuracy_threshold
      value: 82.84748792648315
    - type: similarity_ap
      value: 84.98986658033178
    - type: similarity_f1
      value: 77.24466264970617
    - type: similarity_f1_threshold
      value: 81.41384720802307
    - type: similarity_precision
      value: 74.71578644409269
    - type: similarity_recall
      value: 79.95072374499537
    task:
      type: PairClassification
  - dataset:
      config: default
      name: MTEB Touche2020 (default)
      revision: a34f9a33db75fa0cbb21bb5cfc3dae8dc8bec93f
      split: test
      type: mteb/touche2020
    metrics:
    - type: main_score
      value: 22.198999999999998
    - type: map_at_1
      value: 1.932
    - type: map_at_10
      value: 9.105
    - type: map_at_100
      value: 14.99
    - type: map_at_1000
      value: 16.502
    - type: map_at_20
      value: 11.283
    - type: map_at_3
      value: 4.832
    - type: map_at_5
      value: 6.944999999999999
    - type: mrr_at_1
      value: 26.53061224489796
    - type: mrr_at_10
      value: 43.61030126336249
    - type: mrr_at_100
      value: 44.75538656374139
    - type: mrr_at_1000
      value: 44.75538656374139
    - type: mrr_at_20
      value: 44.37315402351417
    - type: mrr_at_3
      value: 40.136054421768705
    - type: mrr_at_5
      value: 42.68707482993197
    - type: nauc_map_at_1000_diff1
      value: 5.571019818745702
    - type: nauc_map_at_1000_max
      value: -11.439908189694366
    - type: nauc_map_at_1000_std
      value: 3.492870285000601
    - type: nauc_map_at_100_diff1
      value: 6.3857496898544825
    - type: nauc_map_at_100_max
      value: -10.684360218709237
    - type: nauc_map_at_100_std
      value: -1.3788744378787143
    - type: nauc_map_at_10_diff1
      value: -3.2307453267757613
    - type: nauc_map_at_10_max
      value: -11.982307021752293
    - type: nauc_map_at_10_std
      value: -17.038119838763336
    - type: nauc_map_at_1_diff1
      value: -12.065806764609652
    - type: nauc_map_at_1_max
      value: -18.42316476528604
    - type: nauc_map_at_1_std
      value: -5.338503094268672
    - type: nauc_map_at_20_diff1
      value: 2.060946421753866
    - type: nauc_map_at_20_max
      value: -9.648155355543604
    - type: nauc_map_at_20_std
      value: -14.167331436206121
    - type: nauc_map_at_3_diff1
      value: -6.1582621880288135
    - type: nauc_map_at_3_max
      value: -22.097550216296806
    - type: nauc_map_at_3_std
      value: -19.199284745576712
    - type: nauc_map_at_5_diff1
      value: -7.802919708793224
    - type: nauc_map_at_5_max
      value: -17.70019332797913
    - type: nauc_map_at_5_std
      value: -15.991138654326342
    - type: nauc_mrr_at_1000_diff1
      value: 5.315700846697389
    - type: nauc_mrr_at_1000_max
      value: -29.55043481865213
    - type: nauc_mrr_at_1000_std
      value: -8.769041254229224
    - type: nauc_mrr_at_100_diff1
      value: 5.315700846697389
    - type: nauc_mrr_at_100_max
      value: -29.55043481865213
    - type: nauc_mrr_at_100_std
      value: -8.769041254229224
    - type: nauc_mrr_at_10_diff1
      value: 5.342627942794191
    - type: nauc_mrr_at_10_max
      value: -29.8876417651037
    - type: nauc_mrr_at_10_std
      value: -8.925134053814258
    - type: nauc_mrr_at_1_diff1
      value: -5.853396683618596
    - type: nauc_mrr_at_1_max
      value: -24.66468805788406
    - type: nauc_mrr_at_1_std
      value: -2.9097438384537346
    - type: nauc_mrr_at_20_diff1
      value: 5.614614325342419
    - type: nauc_mrr_at_20_max
      value: -29.57233189732013
    - type: nauc_mrr_at_20_std
      value: -8.901826109523945
    - type: nauc_mrr_at_3_diff1
      value: 3.926726061167271
    - type: nauc_mrr_at_3_max
      value: -29.133917047617896
    - type: nauc_mrr_at_3_std
      value: -10.817130618828164
    - type: nauc_mrr_at_5_diff1
      value: 6.866536020293703
    - type: nauc_mrr_at_5_max
      value: -27.22246522106795
    - type: nauc_mrr_at_5_std
      value: -9.223799569500295
    - type: nauc_ndcg_at_1000_diff1
      value: 4.912125181204877
    - type: nauc_ndcg_at_1000_max
      value: -19.911079119060137
    - type: nauc_ndcg_at_1000_std
      value: 31.204098714668948
    - type: nauc_ndcg_at_100_diff1
      value: 8.050987112499488
    - type: nauc_ndcg_at_100_max
      value: -24.237414173651416
    - type: nauc_ndcg_at_100_std
      value: 19.15875595335081
    - type: nauc_ndcg_at_10_diff1
      value: 2.5354767183863816
    - type: nauc_ndcg_at_10_max
      value: -19.384946931074236
    - type: nauc_ndcg_at_10_std
      value: -12.474145803872345
    - type: nauc_ndcg_at_1_diff1
      value: -6.385670878766842
    - type: nauc_ndcg_at_1_max
      value: -26.888516826897597
    - type: nauc_ndcg_at_1_std
      value: 4.6644465028244495
    - type: nauc_ndcg_at_20_diff1
      value: 5.589354383855214
    - type: nauc_ndcg_at_20_max
      value: -19.6270331947477
    - type: nauc_ndcg_at_20_std
      value: -8.94059836915274
    - type: nauc_ndcg_at_3_diff1
      value: -2.9174040900462406
    - type: nauc_ndcg_at_3_max
      value: -27.05606242350417
    - type: nauc_ndcg_at_3_std
      value: -11.987391689874753
    - type: nauc_ndcg_at_5_diff1
      value: -0.962392407401707
    - type: nauc_ndcg_at_5_max
      value: -22.053428062249598
    - type: nauc_ndcg_at_5_std
      value: -9.713594416902245
    - type: nauc_precision_at_1000_diff1
      value: 2.203417821108256
    - type: nauc_precision_at_1000_max
      value: 34.33612400063248
    - type: nauc_precision_at_1000_std
      value: 43.96264641409255
    - type: nauc_precision_at_100_diff1
      value: 16.62707023479431
    - type: nauc_precision_at_100_max
      value: -8.941729500754416
    - type: nauc_precision_at_100_std
      value: 62.443164771048
    - type: nauc_precision_at_10_diff1
      value: 13.230088341821533
    - type: nauc_precision_at_10_max
      value: -9.557587026278982
    - type: nauc_precision_at_10_std
      value: -13.903821725694145
    - type: nauc_precision_at_1_diff1
      value: -5.853396683618596
    - type: nauc_precision_at_1_max
      value: -24.66468805788406
    - type: nauc_precision_at_1_std
      value: -2.9097438384537346
    - type: nauc_precision_at_20_diff1
      value: 20.01420656558271
    - type: nauc_precision_at_20_max
      value: -3.610511982629168
    - type: nauc_precision_at_20_std
      value: 3.3028512582216196
    - type: nauc_precision_at_3_diff1
      value: 4.543784490391635
    - type: nauc_precision_at_3_max
      value: -25.438739747558976
    - type: nauc_precision_at_3_std
      value: -23.527100799773606
    - type: nauc_precision_at_5_diff1
      value: 4.918050559436191
    - type: nauc_precision_at_5_max
      value: -17.82587578128468
    - type: nauc_precision_at_5_std
      value: -15.917371534686687
    - type: nauc_recall_at_1000_diff1
      value: -0.8380945098365681
    - type: nauc_recall_at_1000_max
      value: -13.542228290393272
    - type: nauc_recall_at_1000_std
      value: 78.43177045214168
    - type: nauc_recall_at_100_diff1
      value: 6.01120074173763
    - type: nauc_recall_at_100_max
      value: -27.262764699369907
    - type: nauc_recall_at_100_std
      value: 34.11660757682217
    - type: nauc_recall_at_10_diff1
      value: -0.3618473898428649
    - type: nauc_recall_at_10_max
      value: -17.245131880022484
    - type: nauc_recall_at_10_std
      value: -20.126269566717603
    - type: nauc_recall_at_1_diff1
      value: -12.065806764609652
    - type: nauc_recall_at_1_max
      value: -18.42316476528604
    - type: nauc_recall_at_1_std
      value: -5.338503094268672
    - type: nauc_recall_at_20_diff1
      value: 5.300185381681294
    - type: nauc_recall_at_20_max
      value: -16.939840786187844
    - type: nauc_recall_at_20_std
      value: -11.448793742632803
    - type: nauc_recall_at_3_diff1
      value: -2.90066753150224
    - type: nauc_recall_at_3_max
      value: -27.41339431526332
    - type: nauc_recall_at_3_std
      value: -23.23954755854574
    - type: nauc_recall_at_5_diff1
      value: -2.8599531525072495
    - type: nauc_recall_at_5_max
      value: -19.68001489065482
    - type: nauc_recall_at_5_std
      value: -16.335162845490004
    - type: ndcg_at_1
      value: 22.448999999999998
    - type: ndcg_at_10
      value: 22.198999999999998
    - type: ndcg_at_100
      value: 34.79
    - type: ndcg_at_1000
      value: 45.921
    - type: ndcg_at_20
      value: 23.751
    - type: ndcg_at_3
      value: 25.185000000000002
    - type: ndcg_at_5
      value: 24.751
    - type: precision_at_1
      value: 26.531
    - type: precision_at_10
      value: 19.592000000000002
    - type: precision_at_100
      value: 7.327
    - type: precision_at_1000
      value: 1.486
    - type: precision_at_20
      value: 15.612
    - type: precision_at_3
      value: 28.571
    - type: precision_at_5
      value: 26.939
    - type: recall_at_1
      value: 1.932
    - type: recall_at_10
      value: 14.896999999999998
    - type: recall_at_100
      value: 46.132
    - type: recall_at_1000
      value: 80.26100000000001
    - type: recall_at_20
      value: 22.304
    - type: recall_at_3
      value: 6.237
    - type: recall_at_5
      value: 9.945
    task:
      type: Retrieval
tags:
- medembed
- medical-embedding
- clinical-embedding
- information-retrieval
- sentence-transformers
- mteb
---

# MedEmbed: Specialized Embedding Model for Medical and Clinical Information Retrieval

![benchmark-scores](https://cdn-uploads.huggingface.co/production/uploads/60c8619d95d852a24572b025/gTx5-m68LQ3eyNd6fLki2.png)

## Model Description

MedEmbed is a family of embedding models fine-tuned specifically for medical and clinical data, designed to enhance performance in healthcare-related natural language processing (NLP) tasks, particularly information retrieval.

**GitHub Repo:** [https://github.com/abhinand5/MedEmbed](https://github.com/abhinand5/MedEmbed)

**Technical Blog Post:** [https://huggingface.co/blog/abhinand/medembed-finetuned-embedding-models-for-medical-ir](https://huggingface.co/blog/abhinand/medembed-finetuned-embedding-models-for-medical-ir)

## Intended Use

This model is intended for use in medical and clinical contexts to improve information retrieval, question answering, and semantic search tasks. It can be integrated into healthcare systems, research tools, and medical literature databases to enhance search capabilities and information access.

## Training Data

![synthetic-datagen-flow](https://cdn-uploads.huggingface.co/production/uploads/60c8619d95d852a24572b025/asaA5QDO_j0PWFQV9NXCu.png)

The model was trained using a simple yet effective synthetic data generation pipeline:
1. Source: Clinical notes from PubMed Central (PMC)
2. Processing: [LLaMA 3.1 70B](https://huggingface.co/meta-llama/Llama-3.1-70B-Instruct) model used to generate query-response pairs
3. Augmentation: Negative sampling for challenging examples
4. Format: Triplets (query, positive response, negative response) for contrastive learning

## Performance

MedEmbed consistently outperforms general-purpose embedding models across various medical NLP benchmarks:

- ArguAna
- MedicalQARetrieval
- NFCorpus
- PublicHealthQA
- TRECCOVID

Specific performance metrics (nDCG, MAP, Recall, Precision, MRR) are available in the full documentation.

## Limitations

While highly effective for medical and clinical data, this model may not generalize well to non-medical domains. It should be used with caution in general-purpose NLP tasks.

## Ethical Considerations

Users should be aware of potential biases in medical data and the ethical implications of AI in healthcare. This model should be used as a tool to assist, not replace, human expertise in medical decision-making.

## Citation

If you use this model in your research, please cite:

```bibtex
@software{balachandran2024medembed,
  author = {Balachandran, Abhinand},
  title = {MedEmbed: Medical-Focused Embedding Models},
  year = {2024},
  url = {https://github.com/abhinand5/MedEmbed}
}
```

For more detailed information, visit our GitHub repository.
