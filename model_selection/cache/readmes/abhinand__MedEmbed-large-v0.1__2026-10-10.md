---
language: en
tags:
- medembed
- medical-embedding
- clinical-embedding
- information-retrieval
- sentence-transformers
- mteb
license: apache-2.0
datasets:
- MedicalQARetrieval
- NFCorpus
- PublicHealthQA
- TRECCOVID
- ArguAna
metrics:
- nDCG
- MAP
- Recall
- Precision
- MRR
base_model:
- BAAI/bge-large-en-v1.5
model-index:
- name: abhinand/MedEmbed-large-v0.1
  results:
  - dataset:
      config: default
      name: MTEB CMedQAv2-reranking (default)
      revision: 23d186750531a14a0357ca22cd92d712fd512ea0
      split: test
      type: C-MTEB/CMedQAv2-reranking
    metrics:
    - type: map
      value: 18.3837
    - type: mrr
      value: 21.1936
    - type: nAUC_map_max
      value: 34.185
    - type: nAUC_map_std
      value: 17.8023
    - type: nAUC_map_diff1
      value: 29.8803
    - type: nAUC_mrr_max
      value: 33.5715
    - type: nAUC_mrr_std
      value: 18.198700000000002
    - type: nAUC_mrr_diff1
      value: 28.1289
    - type: main_score
      value: 18.3837
    task:
      type: Reranking
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: all
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 60.775
    - type: ndcg_at_3
      value: 55.233
    - type: ndcg_at_5
      value: 53.738
    - type: ndcg_at_10
      value: 52.898999999999994
    - type: ndcg_at_20
      value: 53.64
    - type: ndcg_at_100
      value: 60.18
    - type: ndcg_at_1000
      value: 68.304
    - type: map_at_1
      value: 9.185
    - type: map_at_3
      value: 16.432
    - type: map_at_5
      value: 20.197000000000003
    - type: map_at_10
      value: 25.278
    - type: map_at_20
      value: 29.92
    - type: map_at_100
      value: 38.107
    - type: map_at_1000
      value: 41.919000000000004
    - type: recall_at_1
      value: 9.185
    - type: recall_at_3
      value: 17.996000000000002
    - type: recall_at_5
      value: 23.671
    - type: recall_at_10
      value: 32.817
    - type: recall_at_20
      value: 43.415
    - type: recall_at_100
      value: 70.08
    - type: recall_at_1000
      value: 94.03099999999999
    - type: precision_at_1
      value: 71.95
    - type: precision_at_3
      value: 59.567
    - type: precision_at_5
      value: 53.480000000000004
    - type: precision_at_10
      value: 44.025
    - type: precision_at_20
      value: 35.147
    - type: precision_at_100
      value: 16.997
    - type: precision_at_1000
      value: 3.399
    - type: mrr_at_1
      value: 71.95
    - type: mrr_at_3
      value: 79.4917
    - type: mrr_at_5
      value: 80.5892
    - type: mrr_at_10
      value: 80.9957
    - type: mrr_at_20
      value: 81.1267
    - type: mrr_at_100
      value: 81.164
    - type: mrr_at_1000
      value: 81.1657
    - type: nauc_ndcg_at_1_max
      value: 38.9364
    - type: nauc_ndcg_at_1_std
      value: 13.528200000000002
    - type: nauc_ndcg_at_1_diff1
      value: 40.0184
    - type: nauc_ndcg_at_3_max
      value: 40.0247
    - type: nauc_ndcg_at_3_std
      value: 16.4182
    - type: nauc_ndcg_at_3_diff1
      value: 27.328000000000003
    - type: nauc_ndcg_at_5_max
      value: 38.8812
    - type: nauc_ndcg_at_5_std
      value: 16.114700000000003
    - type: nauc_ndcg_at_5_diff1
      value: 26.082300000000004
    - type: nauc_ndcg_at_10_max
      value: 38.0527
    - type: nauc_ndcg_at_10_std
      value: 16.9198
    - type: nauc_ndcg_at_10_diff1
      value: 25.3401
    - type: nauc_ndcg_at_20_max
      value: 37.3736
    - type: nauc_ndcg_at_20_std
      value: 16.9378
    - type: nauc_ndcg_at_20_diff1
      value: 26.0711
    - type: nauc_ndcg_at_100_max
      value: 40.096399999999996
    - type: nauc_ndcg_at_100_std
      value: 23.7415
    - type: nauc_ndcg_at_100_diff1
      value: 26.6824
    - type: nauc_ndcg_at_1000_max
      value: 45.1188
    - type: nauc_ndcg_at_1000_std
      value: 31.591200000000004
    - type: nauc_ndcg_at_1000_diff1
      value: 25.790200000000002
    - type: nauc_map_at_1_max
      value: 6.683699999999999
    - type: nauc_map_at_1_std
      value: -12.8402
    - type: nauc_map_at_1_diff1
      value: 42.0279
    - type: nauc_map_at_3_max
      value: 13.3802
    - type: nauc_map_at_3_std
      value: -7.4277999999999995
    - type: nauc_map_at_3_diff1
      value: 31.4791
    - type: nauc_map_at_5_max
      value: 16.2095
    - type: nauc_map_at_5_std
      value: -4.0392
    - type: nauc_map_at_5_diff1
      value: 28.5612
    - type: nauc_map_at_10_max
      value: 20.433899999999998
    - type: nauc_map_at_10_std
      value: 0.5703
    - type: nauc_map_at_10_diff1
      value: 24.7802
    - type: nauc_map_at_20_max
      value: 23.9891
    - type: nauc_map_at_20_std
      value: 5.1846000000000005
    - type: nauc_map_at_20_diff1
      value: 23.117099999999997
    - type: nauc_map_at_100_max
      value: 30.757299999999997
    - type: nauc_map_at_100_std
      value: 17.927599999999998
    - type: nauc_map_at_100_diff1
      value: 19.872500000000002
    - type: nauc_map_at_1000_max
      value: 33.2345
    - type: nauc_map_at_1000_std
      value: 21.9999
    - type: nauc_map_at_1000_diff1
      value: 17.2405
    - type: nauc_recall_at_1_max
      value: 6.683699999999999
    - type: nauc_recall_at_1_std
      value: -12.8402
    - type: nauc_recall_at_1_diff1
      value: 42.0279
    - type: nauc_recall_at_3_max
      value: 10.1747
    - type: nauc_recall_at_3_std
      value: -8.1576
    - type: nauc_recall_at_3_diff1
      value: 28.4653
    - type: nauc_recall_at_5_max
      value: 10.7604
    - type: nauc_recall_at_5_std
      value: -5.2583
    - type: nauc_recall_at_5_diff1
      value: 24.9742
    - type: nauc_recall_at_10_max
      value: 12.6847
    - type: nauc_recall_at_10_std
      value: -2.3404000000000003
    - type: nauc_recall_at_10_diff1
      value: 20.872
    - type: nauc_recall_at_20_max
      value: 14.197399999999998
    - type: nauc_recall_at_20_std
      value: 1.0598
    - type: nauc_recall_at_20_diff1
      value: 19.2151
    - type: nauc_recall_at_100_max
      value: 19.700400000000002
    - type: nauc_recall_at_100_std
      value: 18.8582
    - type: nauc_recall_at_100_diff1
      value: 16.723399999999998
    - type: nauc_recall_at_1000_max
      value: 37.7058
    - type: nauc_recall_at_1000_std
      value: 59.268299999999996
    - type: nauc_recall_at_1000_diff1
      value: 18.7504
    - type: nauc_precision_at_1_max
      value: 45.151599999999995
    - type: nauc_precision_at_1_std
      value: 19.1001
    - type: nauc_precision_at_1_diff1
      value: 38.0115
    - type: nauc_precision_at_3_max
      value: 37.2618
    - type: nauc_precision_at_3_std
      value: 24.4577
    - type: nauc_precision_at_3_diff1
      value: 3.0456
    - type: nauc_precision_at_5_max
      value: 33.4383
    - type: nauc_precision_at_5_std
      value: 26.4563
    - type: nauc_precision_at_5_diff1
      value: -4.6004000000000005
    - type: nauc_precision_at_10_max
      value: 28.6613
    - type: nauc_precision_at_10_std
      value: 28.3258
    - type: nauc_precision_at_10_diff1
      value: -11.7935
    - type: nauc_precision_at_20_max
      value: 22.605700000000002
    - type: nauc_precision_at_20_std
      value: 27.8988
    - type: nauc_precision_at_20_diff1
      value: -14.3591
    - type: nauc_precision_at_100_max
      value: 12.0733
    - type: nauc_precision_at_100_std
      value: 22.561500000000002
    - type: nauc_precision_at_100_diff1
      value: -17.0289
    - type: nauc_precision_at_1000_max
      value: 3.4652000000000003
    - type: nauc_precision_at_1000_std
      value: 3.819
    - type: nauc_precision_at_1000_diff1
      value: -19.627200000000002
    - type: nauc_mrr_at_1_max
      value: 45.151599999999995
    - type: nauc_mrr_at_1_std
      value: 19.1001
    - type: nauc_mrr_at_1_diff1
      value: 38.0115
    - type: nauc_mrr_at_3_max
      value: 48.4709
    - type: nauc_mrr_at_3_std
      value: 25.6162
    - type: nauc_mrr_at_3_diff1
      value: 37.5255
    - type: nauc_mrr_at_5_max
      value: 48.5705
    - type: nauc_mrr_at_5_std
      value: 24.909
    - type: nauc_mrr_at_5_diff1
      value: 37.693799999999996
    - type: nauc_mrr_at_10_max
      value: 48.4052
    - type: nauc_mrr_at_10_std
      value: 24.4063
    - type: nauc_mrr_at_10_diff1
      value: 37.684400000000004
    - type: nauc_mrr_at_20_max
      value: 48.2709
    - type: nauc_mrr_at_20_std
      value: 24.272299999999998
    - type: nauc_mrr_at_20_diff1
      value: 37.737300000000005
    - type: nauc_mrr_at_100_max
      value: 48.229499999999994
    - type: nauc_mrr_at_100_std
      value: 24.2469
    - type: nauc_mrr_at_100_diff1
      value: 37.723600000000005
    - type: nauc_mrr_at_1000_max
      value: 48.2309
    - type: nauc_mrr_at_1000_std
      value: 24.2437
    - type: nauc_mrr_at_1000_diff1
      value: 37.7235
    - type: main_score
      value: 52.898999999999994
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: all
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 15.9
    - type: ndcg_at_3
      value: 15.412999999999998
    - type: ndcg_at_5
      value: 15.42
    - type: ndcg_at_10
      value: 16.145
    - type: ndcg_at_20
      value: 17.386
    - type: ndcg_at_100
      value: 22.116
    - type: ndcg_at_1000
      value: 30.42
    - type: map_at_1
      value: 2.689
    - type: map_at_3
      value: 4.891
    - type: map_at_5
      value: 5.998
    - type: map_at_10
      value: 7.502000000000001
    - type: map_at_20
      value: 8.784
    - type: map_at_100
      value: 11.08
    - type: map_at_1000
      value: 12.662999999999998
    - type: recall_at_1
      value: 2.689
    - type: recall_at_3
      value: 6.002
    - type: recall_at_5
      value: 8.187
    - type: recall_at_10
      value: 12.167
    - type: recall_at_20
      value: 16.824
    - type: recall_at_100
      value: 31.608999999999998
    - type: recall_at_1000
      value: 58.023
    - type: precision_at_1
      value: 20.200000000000003
    - type: precision_at_3
      value: 17.45
    - type: precision_at_5
      value: 15.85
    - type: precision_at_10
      value: 13.645
    - type: precision_at_20
      value: 11.285
    - type: precision_at_100
      value: 6.265
    - type: precision_at_1000
      value: 1.7950000000000002
    - type: mrr_at_1
      value: 20.200000000000003
    - type: mrr_at_3
      value: 25.9583
    - type: mrr_at_5
      value: 27.450799999999997
    - type: mrr_at_10
      value: 28.6658
    - type: mrr_at_20
      value: 29.2657
    - type: mrr_at_100
      value: 29.652
    - type: mrr_at_1000
      value: 29.724
    - type: nauc_ndcg_at_1_max
      value: 34.4333
    - type: nauc_ndcg_at_1_std
      value: 37.9045
    - type: nauc_ndcg_at_1_diff1
      value: 13.5962
    - type: nauc_ndcg_at_3_max
      value: 40.9522
    - type: nauc_ndcg_at_3_std
      value: 43.265
    - type: nauc_ndcg_at_3_diff1
      value: 13.858699999999999
    - type: nauc_ndcg_at_5_max
      value: 42.3408
    - type: nauc_ndcg_at_5_std
      value: 45.1913
    - type: nauc_ndcg_at_5_diff1
      value: 14.362400000000001
    - type: nauc_ndcg_at_10_max
      value: 43.697399999999995
    - type: nauc_ndcg_at_10_std
      value: 47.9172
    - type: nauc_ndcg_at_10_diff1
      value: 14.7778
    - type: nauc_ndcg_at_20_max
      value: 45.8538
    - type: nauc_ndcg_at_20_std
      value: 50.7075
    - type: nauc_ndcg_at_20_diff1
      value: 14.7758
    - type: nauc_ndcg_at_100_max
      value: 48.2383
    - type: nauc_ndcg_at_100_std
      value: 56.974000000000004
    - type: nauc_ndcg_at_100_diff1
      value: 13.706399999999999
    - type: nauc_ndcg_at_1000_max
      value: 52.815599999999996
    - type: nauc_ndcg_at_1000_std
      value: 61.815200000000004
    - type: nauc_ndcg_at_1000_diff1
      value: 11.358500000000001
    - type: nauc_map_at_1_max
      value: 32.1329
    - type: nauc_map_at_1_std
      value: 30.017300000000002
    - type: nauc_map_at_1_diff1
      value: 33.417
    - type: nauc_map_at_3_max
      value: 36.6575
    - type: nauc_map_at_3_std
      value: 34.436099999999996
    - type: nauc_map_at_3_diff1
      value: 28.370099999999997
    - type: nauc_map_at_5_max
      value: 37.6872
    - type: nauc_map_at_5_std
      value: 37.303599999999996
    - type: nauc_map_at_5_diff1
      value: 25.6251
    - type: nauc_map_at_10_max
      value: 39.6209
    - type: nauc_map_at_10_std
      value: 41.5154
    - type: nauc_map_at_10_diff1
      value: 21.7045
    - type: nauc_map_at_20_max
      value: 41.7603
    - type: nauc_map_at_20_std
      value: 45.4034
    - type: nauc_map_at_20_diff1
      value: 19.9809
    - type: nauc_map_at_100_max
      value: 45.1746
    - type: nauc_map_at_100_std
      value: 52.485899999999994
    - type: nauc_map_at_100_diff1
      value: 17.2712
    - type: nauc_map_at_1000_max
      value: 47.978
    - type: nauc_map_at_1000_std
      value: 55.4423
    - type: nauc_map_at_1000_diff1
      value: 15.770999999999999
    - type: nauc_recall_at_1_max
      value: 32.1329
    - type: nauc_recall_at_1_std
      value: 30.017300000000002
    - type: nauc_recall_at_1_diff1
      value: 33.417
    - type: nauc_recall_at_3_max
      value: 34.0411
    - type: nauc_recall_at_3_std
      value: 32.08
    - type: nauc_recall_at_3_diff1
      value: 27.1762
    - type: nauc_recall_at_5_max
      value: 33.7353
    - type: nauc_recall_at_5_std
      value: 35.6551
    - type: nauc_recall_at_5_diff1
      value: 23.2104
    - type: nauc_recall_at_10_max
      value: 34.0794
    - type: nauc_recall_at_10_std
      value: 39.3103
    - type: nauc_recall_at_10_diff1
      value: 16.700499999999998
    - type: nauc_recall_at_20_max
      value: 36.025
    - type: nauc_recall_at_20_std
      value: 43.8139
    - type: nauc_recall_at_20_diff1
      value: 14.8745
    - type: nauc_recall_at_100_max
      value: 40.477999999999994
    - type: nauc_recall_at_100_std
      value: 55.299
    - type: nauc_recall_at_100_diff1
      value: 12.0134
    - type: nauc_recall_at_1000_max
      value: 50.88
    - type: nauc_recall_at_1000_std
      value: 69.1237
    - type: nauc_recall_at_1000_diff1
      value: 7.1673
    - type: nauc_precision_at_1_max
      value: 36.3741
    - type: nauc_precision_at_1_std
      value: 40.3943
    - type: nauc_precision_at_1_diff1
      value: 11.9572
    - type: nauc_precision_at_3_max
      value: 44.1485
    - type: nauc_precision_at_3_std
      value: 47.2489
    - type: nauc_precision_at_3_diff1
      value: 7.3660000000000005
    - type: nauc_precision_at_5_max
      value: 44.5096
    - type: nauc_precision_at_5_std
      value: 49.1423
    - type: nauc_precision_at_5_diff1
      value: 5.0777
    - type: nauc_precision_at_10_max
      value: 45.307700000000004
    - type: nauc_precision_at_10_std
      value: 51.953700000000005
    - type: nauc_precision_at_10_diff1
      value: 3.1449
    - type: nauc_precision_at_20_max
      value: 47.2433
    - type: nauc_precision_at_20_std
      value: 53.367200000000004
    - type: nauc_precision_at_20_diff1
      value: 0.7057
    - type: nauc_precision_at_100_max
      value: 44.3203
    - type: nauc_precision_at_100_std
      value: 49.472
    - type: nauc_precision_at_100_diff1
      value: -2.0434
    - type: nauc_precision_at_1000_max
      value: 37.7422
    - type: nauc_precision_at_1000_std
      value: 27.3935
    - type: nauc_precision_at_1000_diff1
      value: -3.1565000000000003
    - type: nauc_mrr_at_1_max
      value: 36.3741
    - type: nauc_mrr_at_1_std
      value: 40.3943
    - type: nauc_mrr_at_1_diff1
      value: 11.9572
    - type: nauc_mrr_at_3_max
      value: 39.006099999999996
    - type: nauc_mrr_at_3_std
      value: 42.753
    - type: nauc_mrr_at_3_diff1
      value: 11.0316
    - type: nauc_mrr_at_5_max
      value: 39.2901
    - type: nauc_mrr_at_5_std
      value: 43.4405
    - type: nauc_mrr_at_5_diff1
      value: 10.519499999999999
    - type: nauc_mrr_at_10_max
      value: 40.2703
    - type: nauc_mrr_at_10_std
      value: 44.372699999999995
    - type: nauc_mrr_at_10_diff1
      value: 10.6792
    - type: nauc_mrr_at_20_max
      value: 40.605999999999995
    - type: nauc_mrr_at_20_std
      value: 44.630199999999995
    - type: nauc_mrr_at_20_diff1
      value: 10.5727
    - type: nauc_mrr_at_100_max
      value: 40.6811
    - type: nauc_mrr_at_100_std
      value: 44.646
    - type: nauc_mrr_at_100_diff1
      value: 10.6126
    - type: nauc_mrr_at_1000_max
      value: 40.6568
    - type: nauc_mrr_at_1000_std
      value: 44.624399999999994
    - type: nauc_mrr_at_1000_diff1
      value: 10.6075
    - type: main_score
      value: 16.145
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: all
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 24.9
    - type: ndcg_at_3
      value: 23.435
    - type: ndcg_at_5
      value: 23.462
    - type: ndcg_at_10
      value: 24.151
    - type: ndcg_at_20
      value: 25.171
    - type: ndcg_at_100
      value: 30.714999999999996
    - type: ndcg_at_1000
      value: 39.26
    - type: map_at_1
      value: 3.987
    - type: map_at_3
      value: 7.101
    - type: map_at_5
      value: 8.752
    - type: map_at_10
      value: 11.075
    - type: map_at_20
      value: 12.964
    - type: map_at_100
      value: 16.424
    - type: map_at_1000
      value: 18.472
    - type: recall_at_1
      value: 3.987
    - type: recall_at_3
      value: 8.290000000000001
    - type: recall_at_5
      value: 11.407
    - type: recall_at_10
      value: 16.906
    - type: recall_at_20
      value: 22.766000000000002
    - type: recall_at_100
      value: 40.918
    - type: recall_at_1000
      value: 67.77
    - type: precision_at_1
      value: 31.5
    - type: precision_at_3
      value: 26.533
    - type: precision_at_5
      value: 24.19
    - type: precision_at_10
      value: 20.59
    - type: precision_at_20
      value: 16.54
    - type: precision_at_100
      value: 8.725
    - type: precision_at_1000
      value: 2.2159999999999997
    - type: mrr_at_1
      value: 31.5
    - type: mrr_at_3
      value: 38.5667
    - type: mrr_at_5
      value: 40.2692
    - type: mrr_at_10
      value: 41.4221
    - type: mrr_at_20
      value: 41.9627
    - type: mrr_at_100
      value: 42.3045
    - type: mrr_at_1000
      value: 42.3438
    - type: nauc_ndcg_at_1_max
      value: 41.2346
    - type: nauc_ndcg_at_1_std
      value: 34.096399999999996
    - type: nauc_ndcg_at_1_diff1
      value: 23.3773
    - type: nauc_ndcg_at_3_max
      value: 48.4194
    - type: nauc_ndcg_at_3_std
      value: 38.5582
    - type: nauc_ndcg_at_3_diff1
      value: 20.044999999999998
    - type: nauc_ndcg_at_5_max
      value: 50.6073
    - type: nauc_ndcg_at_5_std
      value: 41.7937
    - type: nauc_ndcg_at_5_diff1
      value: 19.1486
    - type: nauc_ndcg_at_10_max
      value: 52.3725
    - type: nauc_ndcg_at_10_std
      value: 44.8701
    - type: nauc_ndcg_at_10_diff1
      value: 19.7716
    - type: nauc_ndcg_at_20_max
      value: 52.9589
    - type: nauc_ndcg_at_20_std
      value: 47.6835
    - type: nauc_ndcg_at_20_diff1
      value: 19.6519
    - type: nauc_ndcg_at_100_max
      value: 57.541799999999995
    - type: nauc_ndcg_at_100_std
      value: 56.922799999999995
    - type: nauc_ndcg_at_100_diff1
      value: 19.5411
    - type: nauc_ndcg_at_1000_max
      value: 60.6206
    - type: nauc_ndcg_at_1000_std
      value: 61.526
    - type: nauc_ndcg_at_1000_diff1
      value: 17.1735
    - type: nauc_map_at_1_max
      value: 32.4122
    - type: nauc_map_at_1_std
      value: 21.851499999999998
    - type: nauc_map_at_1_diff1
      value: 42.2724
    - type: nauc_map_at_3_max
      value: 36.2169
    - type: nauc_map_at_3_std
      value: 26.3249
    - type: nauc_map_at_3_diff1
      value: 32.3562
    - type: nauc_map_at_5_max
      value: 37.9852
    - type: nauc_map_at_5_std
      value: 29.6092
    - type: nauc_map_at_5_diff1
      value: 27.9065
    - type: nauc_map_at_10_max
      value: 41.227000000000004
    - type: nauc_map_at_10_std
      value: 34.2656
    - type: nauc_map_at_10_diff1
      value: 24.9007
    - type: nauc_map_at_20_max
      value: 44.288
    - type: nauc_map_at_20_std
      value: 39.033
    - type: nauc_map_at_20_diff1
      value: 23.0301
    - type: nauc_map_at_100_max
      value: 50.3709
    - type: nauc_map_at_100_std
      value: 48.2427
    - type: nauc_map_at_100_diff1
      value: 20.3268
    - type: nauc_map_at_1000_max
      value: 52.983599999999996
    - type: nauc_map_at_1000_std
      value: 51.302899999999994
    - type: nauc_map_at_1000_diff1
      value: 18.7497
    - type: nauc_recall_at_1_max
      value: 32.4122
    - type: nauc_recall_at_1_std
      value: 21.851499999999998
    - type: nauc_recall_at_1_diff1
      value: 42.2724
    - type: nauc_recall_at_3_max
      value: 35.6626
    - type: nauc_recall_at_3_std
      value: 26.583000000000002
    - type: nauc_recall_at_3_diff1
      value: 28.9598
    - type: nauc_recall_at_5_max
      value: 35.6704
    - type: nauc_recall_at_5_std
      value: 29.0846
    - type: nauc_recall_at_5_diff1
      value: 23.8078
    - type: nauc_recall_at_10_max
      value: 38.3994
    - type: nauc_recall_at_10_std
      value: 34.0908
    - type: nauc_recall_at_10_diff1
      value: 21.0836
    - type: nauc_recall_at_20_max
      value: 40.962900000000005
    - type: nauc_recall_at_20_std
      value: 40.4136
    - type: nauc_recall_at_20_diff1
      value: 18.5189
    - type: nauc_recall_at_100_max
      value: 51.4476
    - type: nauc_recall_at_100_std
      value: 58.6901
    - type: nauc_recall_at_100_diff1
      value: 16.724700000000002
    - type: nauc_recall_at_1000_max
      value: 65.0535
    - type: nauc_recall_at_1000_std
      value: 77.2842
    - type: nauc_recall_at_1000_diff1
      value: 11.8624
    - type: nauc_precision_at_1_max
      value: 43.3958
    - type: nauc_precision_at_1_std
      value: 37.1612
    - type: nauc_precision_at_1_diff1
      value: 20.409399999999998
    - type: nauc_precision_at_3_max
      value: 49.9639
    - type: nauc_precision_at_3_std
      value: 41.6999
    - type: nauc_precision_at_3_diff1
      value: 10.554
    - type: nauc_precision_at_5_max
      value: 51.3906
    - type: nauc_precision_at_5_std
      value: 45.5246
    - type: nauc_precision_at_5_diff1
      value: 6.8306000000000004
    - type: nauc_precision_at_10_max
      value: 51.8536
    - type: nauc_precision_at_10_std
      value: 47.8267
    - type: nauc_precision_at_10_diff1
      value: 4.649699999999999
    - type: nauc_precision_at_20_max
      value: 49.1757
    - type: nauc_precision_at_20_std
      value: 48.0193
    - type: nauc_precision_at_20_diff1
      value: 1.7838
    - type: nauc_precision_at_100_max
      value: 41.7249
    - type: nauc_precision_at_100_std
      value: 42.2626
    - type: nauc_precision_at_100_diff1
      value: -3.2152
    - type: nauc_precision_at_1000_max
      value: 26.6144
    - type: nauc_precision_at_1000_std
      value: 16.6642
    - type: nauc_precision_at_1000_diff1
      value: -6.8772
    - type: nauc_mrr_at_1_max
      value: 43.3958
    - type: nauc_mrr_at_1_std
      value: 37.1612
    - type: nauc_mrr_at_1_diff1
      value: 20.409399999999998
    - type: nauc_mrr_at_3_max
      value: 47.9059
    - type: nauc_mrr_at_3_std
      value: 40.9064
    - type: nauc_mrr_at_3_diff1
      value: 18.2671
    - type: nauc_mrr_at_5_max
      value: 48.7106
    - type: nauc_mrr_at_5_std
      value: 42.2268
    - type: nauc_mrr_at_5_diff1
      value: 18.875600000000002
    - type: nauc_mrr_at_10_max
      value: 49.0714
    - type: nauc_mrr_at_10_std
      value: 42.6807
    - type: nauc_mrr_at_10_diff1
      value: 18.8448
    - type: nauc_mrr_at_20_max
      value: 49.113600000000005
    - type: nauc_mrr_at_20_std
      value: 42.771
    - type: nauc_mrr_at_20_diff1
      value: 18.6008
    - type: nauc_mrr_at_100_max
      value: 49.1187
    - type: nauc_mrr_at_100_std
      value: 42.795899999999996
    - type: nauc_mrr_at_100_diff1
      value: 18.7082
    - type: nauc_mrr_at_1000_max
      value: 49.0966
    - type: nauc_mrr_at_1000_std
      value: 42.769600000000004
    - type: nauc_mrr_at_1000_diff1
      value: 18.7057
    - type: main_score
      value: 24.151
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: dentistry_and_oral_health
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 63.74999999999999
    - type: ndcg_at_3
      value: 56.45400000000001
    - type: ndcg_at_5
      value: 53.888999999999996
    - type: ndcg_at_10
      value: 52.470000000000006
    - type: ndcg_at_20
      value: 51.661
    - type: ndcg_at_100
      value: 57.528
    - type: ndcg_at_1000
      value: 69.085
    - type: map_at_1
      value: 9.146
    - type: map_at_3
      value: 15.024999999999999
    - type: map_at_5
      value: 17.595
    - type: map_at_10
      value: 21.502
    - type: map_at_20
      value: 25.112000000000002
    - type: map_at_100
      value: 33.629999999999995
    - type: map_at_1000
      value: 38.818000000000005
    - type: recall_at_1
      value: 9.146
    - type: recall_at_3
      value: 17.03
    - type: recall_at_5
      value: 21.325
    - type: recall_at_10
      value: 28.424
    - type: recall_at_20
      value: 36.464
    - type: recall_at_100
      value: 64.31099999999999
    - type: recall_at_1000
      value: 95.343
    - type: precision_at_1
      value: 74.0
    - type: precision_at_3
      value: 60.167
    - type: precision_at_5
      value: 53.300000000000004
    - type: precision_at_10
      value: 44.3
    - type: precision_at_20
      value: 35.25
    - type: precision_at_100
      value: 18.404999999999998
    - type: precision_at_1000
      value: 3.721
    - type: mrr_at_1
      value: 74.0
    - type: mrr_at_3
      value: 82.08330000000001
    - type: mrr_at_5
      value: 83.4833
    - type: mrr_at_10
      value: 83.66029999999999
    - type: mrr_at_20
      value: 83.66029999999999
    - type: mrr_at_100
      value: 83.69290000000001
    - type: mrr_at_1000
      value: 83.69290000000001
    - type: nauc_ndcg_at_1_max
      value: 44.2782
    - type: nauc_ndcg_at_1_std
      value: -5.9135
    - type: nauc_ndcg_at_1_diff1
      value: 40.12
    - type: nauc_ndcg_at_3_max
      value: 35.1497
    - type: nauc_ndcg_at_3_std
      value: -3.2272000000000003
    - type: nauc_ndcg_at_3_diff1
      value: 23.9014
    - type: nauc_ndcg_at_5_max
      value: 29.4267
    - type: nauc_ndcg_at_5_std
      value: -9.1058
    - type: nauc_ndcg_at_5_diff1
      value: 24.3146
    - type: nauc_ndcg_at_10_max
      value: 27.178600000000003
    - type: nauc_ndcg_at_10_std
      value: -11.1484
    - type: nauc_ndcg_at_10_diff1
      value: 23.947599999999998
    - type: nauc_ndcg_at_20_max
      value: 23.180400000000002
    - type: nauc_ndcg_at_20_std
      value: -11.7635
    - type: nauc_ndcg_at_20_diff1
      value: 25.630999999999997
    - type: nauc_ndcg_at_100_max
      value: 27.236300000000004
    - type: nauc_ndcg_at_100_std
      value: -11.0596
    - type: nauc_ndcg_at_100_diff1
      value: 29.851699999999997
    - type: nauc_ndcg_at_1000_max
      value: 38.7358
    - type: nauc_ndcg_at_1000_std
      value: 12.8903
    - type: nauc_ndcg_at_1000_diff1
      value: 25.6108
    - type: nauc_map_at_1_max
      value: 8.0922
    - type: nauc_map_at_1_std
      value: -31.6799
    - type: nauc_map_at_1_diff1
      value: 42.1566
    - type: nauc_map_at_3_max
      value: 7.6643
    - type: nauc_map_at_3_std
      value: -32.679399999999994
    - type: nauc_map_at_3_diff1
      value: 29.1437
    - type: nauc_map_at_5_max
      value: 8.3421
    - type: nauc_map_at_5_std
      value: -32.3957
    - type: nauc_map_at_5_diff1
      value: 26.3427
    - type: nauc_map_at_10_max
      value: 8.5915
    - type: nauc_map_at_10_std
      value: -31.4049
    - type: nauc_map_at_10_diff1
      value: 23.3537
    - type: nauc_map_at_20_max
      value: 11.0618
    - type: nauc_map_at_20_std
      value: -28.0167
    - type: nauc_map_at_20_diff1
      value: 23.278399999999998
    - type: nauc_map_at_100_max
      value: 18.6807
    - type: nauc_map_at_100_std
      value: -10.8842
    - type: nauc_map_at_100_diff1
      value: 21.370900000000002
    - type: nauc_map_at_1000_max
      value: 20.6202
    - type: nauc_map_at_1000_std
      value: 1.8843999999999999
    - type: nauc_map_at_1000_diff1
      value: 16.491500000000002
    - type: nauc_recall_at_1_max
      value: 8.0922
    - type: nauc_recall_at_1_std
      value: -31.6799
    - type: nauc_recall_at_1_diff1
      value: 42.1566
    - type: nauc_recall_at_3_max
      value: 1.7718999999999998
    - type: nauc_recall_at_3_std
      value: -33.3208
    - type: nauc_recall_at_3_diff1
      value: 24.388
    - type: nauc_recall_at_5_max
      value: -0.1774
    - type: nauc_recall_at_5_std
      value: -34.9405
    - type: nauc_recall_at_5_diff1
      value: 19.7842
    - type: nauc_recall_at_10_max
      value: -1.7014999999999998
    - type: nauc_recall_at_10_std
      value: -33.9917
    - type: nauc_recall_at_10_diff1
      value: 15.3697
    - type: nauc_recall_at_20_max
      value: -0.48669999999999997
    - type: nauc_recall_at_20_std
      value: -30.890800000000002
    - type: nauc_recall_at_20_diff1
      value: 17.1512
    - type: nauc_recall_at_100_max
      value: 7.9208
    - type: nauc_recall_at_100_std
      value: -16.7223
    - type: nauc_recall_at_100_diff1
      value: 24.4227
    - type: nauc_recall_at_1000_max
      value: 46.3102
    - type: nauc_recall_at_1000_std
      value: 55.03360000000001
    - type: nauc_recall_at_1000_diff1
      value: 37.6798
    - type: nauc_precision_at_1_max
      value: 55.07379999999999
    - type: nauc_precision_at_1_std
      value: 6.4353
    - type: nauc_precision_at_1_diff1
      value: 30.604
    - type: nauc_precision_at_3_max
      value: 36.3344
    - type: nauc_precision_at_3_std
      value: 24.7186
    - type: nauc_precision_at_3_diff1
      value: -5.5176
    - type: nauc_precision_at_5_max
      value: 25.891799999999996
    - type: nauc_precision_at_5_std
      value: 27.0728
    - type: nauc_precision_at_5_diff1
      value: -8.4442
    - type: nauc_precision_at_10_max
      value: 21.151
    - type: nauc_precision_at_10_std
      value: 33.8452
    - type: nauc_precision_at_10_diff1
      value: -13.6853
    - type: nauc_precision_at_20_max
      value: 17.8701
    - type: nauc_precision_at_20_std
      value: 39.250600000000006
    - type: nauc_precision_at_20_diff1
      value: -13.8478
    - type: nauc_precision_at_100_max
      value: 12.2101
    - type: nauc_precision_at_100_std
      value: 45.3089
    - type: nauc_precision_at_100_diff1
      value: -13.727800000000002
    - type: nauc_precision_at_1000_max
      value: 0.49899999999999994
    - type: nauc_precision_at_1000_std
      value: 34.724199999999996
    - type: nauc_precision_at_1000_diff1
      value: -19.284399999999998
    - type: nauc_mrr_at_1_max
      value: 55.07379999999999
    - type: nauc_mrr_at_1_std
      value: 6.4353
    - type: nauc_mrr_at_1_diff1
      value: 30.604
    - type: nauc_mrr_at_3_max
      value: 53.581100000000006
    - type: nauc_mrr_at_3_std
      value: 12.326600000000001
    - type: nauc_mrr_at_3_diff1
      value: 31.159599999999998
    - type: nauc_mrr_at_5_max
      value: 53.3839
    - type: nauc_mrr_at_5_std
      value: 9.695
    - type: nauc_mrr_at_5_diff1
      value: 30.5214
    - type: nauc_mrr_at_10_max
      value: 53.8177
    - type: nauc_mrr_at_10_std
      value: 10.4039
    - type: nauc_mrr_at_10_diff1
      value: 30.158099999999997
    - type: nauc_mrr_at_20_max
      value: 53.8177
    - type: nauc_mrr_at_20_std
      value: 10.4039
    - type: nauc_mrr_at_20_diff1
      value: 30.158099999999997
    - type: nauc_mrr_at_100_max
      value: 53.7423
    - type: nauc_mrr_at_100_std
      value: 10.235
    - type: nauc_mrr_at_100_diff1
      value: 30.1529
    - type: nauc_mrr_at_1000_max
      value: 53.7423
    - type: nauc_mrr_at_1000_std
      value: 10.235
    - type: nauc_mrr_at_1000_diff1
      value: 30.1529
    - type: main_score
      value: 52.470000000000006
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: dentistry_and_oral_health
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 11.5
    - type: ndcg_at_3
      value: 11.129999999999999
    - type: ndcg_at_5
      value: 11.216
    - type: ndcg_at_10
      value: 11.392
    - type: ndcg_at_20
      value: 12.296999999999999
    - type: ndcg_at_100
      value: 15.956999999999999
    - type: ndcg_at_1000
      value: 25.529000000000003
    - type: map_at_1
      value: 2.275
    - type: map_at_3
      value: 3.94
    - type: map_at_5
      value: 4.327
    - type: map_at_10
      value: 5.04
    - type: map_at_20
      value: 5.646
    - type: map_at_100
      value: 7.135
    - type: map_at_1000
      value: 8.725
    - type: recall_at_1
      value: 2.275
    - type: recall_at_3
      value: 5.359
    - type: recall_at_5
      value: 6.393
    - type: recall_at_10
      value: 8.35
    - type: recall_at_20
      value: 11.158
    - type: recall_at_100
      value: 22.223000000000003
    - type: recall_at_1000
      value: 50.477000000000004
    - type: precision_at_1
      value: 15.5
    - type: precision_at_3
      value: 12.5
    - type: precision_at_5
      value: 11.4
    - type: precision_at_10
      value: 9.25
    - type: precision_at_20
      value: 7.875
    - type: precision_at_100
      value: 5.04
    - type: precision_at_1000
      value: 1.7389999999999999
    - type: mrr_at_1
      value: 15.5
    - type: mrr_at_3
      value: 20.5
    - type: mrr_at_5
      value: 21.925
    - type: mrr_at_10
      value: 22.5444
    - type: mrr_at_20
      value: 23.2625
    - type: mrr_at_100
      value: 23.7237
    - type: mrr_at_1000
      value: 23.8369
    - type: nauc_ndcg_at_1_max
      value: 34.4589
    - type: nauc_ndcg_at_1_std
      value: 42.1292
    - type: nauc_ndcg_at_1_diff1
      value: 17.9811
    - type: nauc_ndcg_at_3_max
      value: 33.5732
    - type: nauc_ndcg_at_3_std
      value: 41.7443
    - type: nauc_ndcg_at_3_diff1
      value: 24.6128
    - type: nauc_ndcg_at_5_max
      value: 37.585
    - type: nauc_ndcg_at_5_std
      value: 46.0713
    - type: nauc_ndcg_at_5_diff1
      value: 27.2211
    - type: nauc_ndcg_at_10_max
      value: 40.0605
    - type: nauc_ndcg_at_10_std
      value: 47.6628
    - type: nauc_ndcg_at_10_diff1
      value: 29.166700000000002
    - type: nauc_ndcg_at_20_max
      value: 39.6748
    - type: nauc_ndcg_at_20_std
      value: 49.601600000000005
    - type: nauc_ndcg_at_20_diff1
      value: 28.198
    - type: nauc_ndcg_at_100_max
      value: 38.1407
    - type: nauc_ndcg_at_100_std
      value: 52.9055
    - type: nauc_ndcg_at_100_diff1
      value: 20.5359
    - type: nauc_ndcg_at_1000_max
      value: 41.737
    - type: nauc_ndcg_at_1000_std
      value: 58.988600000000005
    - type: nauc_ndcg_at_1000_diff1
      value: 16.1082
    - type: nauc_map_at_1_max
      value: 25.4402
    - type: nauc_map_at_1_std
      value: 25.208599999999997
    - type: nauc_map_at_1_diff1
      value: 54.664500000000004
    - type: nauc_map_at_3_max
      value: 24.0543
    - type: nauc_map_at_3_std
      value: 28.7833
    - type: nauc_map_at_3_diff1
      value: 46.6306
    - type: nauc_map_at_5_max
      value: 26.923799999999996
    - type: nauc_map_at_5_std
      value: 32.233000000000004
    - type: nauc_map_at_5_diff1
      value: 42.9054
    - type: nauc_map_at_10_max
      value: 31.8766
    - type: nauc_map_at_10_std
      value: 36.6634
    - type: nauc_map_at_10_diff1
      value: 41.185500000000005
    - type: nauc_map_at_20_max
      value: 32.3117
    - type: nauc_map_at_20_std
      value: 39.8134
    - type: nauc_map_at_20_diff1
      value: 37.7037
    - type: nauc_map_at_100_max
      value: 33.7308
    - type: nauc_map_at_100_std
      value: 47.5419
    - type: nauc_map_at_100_diff1
      value: 27.683999999999997
    - type: nauc_map_at_1000_max
      value: 37.358000000000004
    - type: nauc_map_at_1000_std
      value: 53.5331
    - type: nauc_map_at_1000_diff1
      value: 22.4664
    - type: nauc_recall_at_1_max
      value: 25.4402
    - type: nauc_recall_at_1_std
      value: 25.208599999999997
    - type: nauc_recall_at_1_diff1
      value: 54.664500000000004
    - type: nauc_recall_at_3_max
      value: 26.2666
    - type: nauc_recall_at_3_std
      value: 32.2588
    - type: nauc_recall_at_3_diff1
      value: 46.1528
    - type: nauc_recall_at_5_max
      value: 32.364
    - type: nauc_recall_at_5_std
      value: 37.816300000000005
    - type: nauc_recall_at_5_diff1
      value: 38.8915
    - type: nauc_recall_at_10_max
      value: 39.0272
    - type: nauc_recall_at_10_std
      value: 43.8025
    - type: nauc_recall_at_10_diff1
      value: 37.08
    - type: nauc_recall_at_20_max
      value: 35.629
    - type: nauc_recall_at_20_std
      value: 45.7498
    - type: nauc_recall_at_20_diff1
      value: 31.1273
    - type: nauc_recall_at_100_max
      value: 31.1328
    - type: nauc_recall_at_100_std
      value: 50.60980000000001
    - type: nauc_recall_at_100_diff1
      value: 15.974499999999999
    - type: nauc_recall_at_1000_max
      value: 35.4467
    - type: nauc_recall_at_1000_std
      value: 64.4764
    - type: nauc_recall_at_1000_diff1
      value: 11.8923
    - type: nauc_precision_at_1_max
      value: 34.8024
    - type: nauc_precision_at_1_std
      value: 45.0141
    - type: nauc_precision_at_1_diff1
      value: 16.5504
    - type: nauc_precision_at_3_max
      value: 34.2196
    - type: nauc_precision_at_3_std
      value: 45.9596
    - type: nauc_precision_at_3_diff1
      value: 14.921100000000001
    - type: nauc_precision_at_5_max
      value: 40.087
    - type: nauc_precision_at_5_std
      value: 55.0371
    - type: nauc_precision_at_5_diff1
      value: 13.638
    - type: nauc_precision_at_10_max
      value: 43.2516
    - type: nauc_precision_at_10_std
      value: 55.863
    - type: nauc_precision_at_10_diff1
      value: 9.0558
    - type: nauc_precision_at_20_max
      value: 42.8832
    - type: nauc_precision_at_20_std
      value: 58.2846
    - type: nauc_precision_at_20_diff1
      value: -0.9745999999999999
    - type: nauc_precision_at_100_max
      value: 38.4914
    - type: nauc_precision_at_100_std
      value: 58.0033
    - type: nauc_precision_at_100_diff1
      value: -14.6786
    - type: nauc_precision_at_1000_max
      value: 37.3476
    - type: nauc_precision_at_1000_std
      value: 38.1122
    - type: nauc_precision_at_1000_diff1
      value: -11.295
    - type: nauc_mrr_at_1_max
      value: 34.8024
    - type: nauc_mrr_at_1_std
      value: 45.0141
    - type: nauc_mrr_at_1_diff1
      value: 16.5504
    - type: nauc_mrr_at_3_max
      value: 33.0518
    - type: nauc_mrr_at_3_std
      value: 44.4493
    - type: nauc_mrr_at_3_diff1
      value: 19.974700000000002
    - type: nauc_mrr_at_5_max
      value: 36.3726
    - type: nauc_mrr_at_5_std
      value: 47.3453
    - type: nauc_mrr_at_5_diff1
      value: 21.0721
    - type: nauc_mrr_at_10_max
      value: 36.788199999999996
    - type: nauc_mrr_at_10_std
      value: 47.2219
    - type: nauc_mrr_at_10_diff1
      value: 20.68
    - type: nauc_mrr_at_20_max
      value: 36.9338
    - type: nauc_mrr_at_20_std
      value: 46.978500000000004
    - type: nauc_mrr_at_20_diff1
      value: 20.479400000000002
    - type: nauc_mrr_at_100_max
      value: 36.6516
    - type: nauc_mrr_at_100_std
      value: 46.7474
    - type: nauc_mrr_at_100_diff1
      value: 20.1232
    - type: nauc_mrr_at_1000_max
      value: 36.647400000000005
    - type: nauc_mrr_at_1000_std
      value: 46.7738
    - type: nauc_mrr_at_1000_diff1
      value: 20.1326
    - type: main_score
      value: 11.392
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: dentistry_and_oral_health
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 21.0
    - type: ndcg_at_3
      value: 19.622
    - type: ndcg_at_5
      value: 19.081
    - type: ndcg_at_10
      value: 18.684
    - type: ndcg_at_20
      value: 19.7
    - type: ndcg_at_100
      value: 24.552
    - type: ndcg_at_1000
      value: 35.679
    - type: map_at_1
      value: 3.44
    - type: map_at_3
      value: 5.6000000000000005
    - type: map_at_5
      value: 6.300999999999999
    - type: map_at_10
      value: 7.396
    - type: map_at_20
      value: 8.601
    - type: map_at_100
      value: 11.357000000000001
    - type: map_at_1000
      value: 13.666
    - type: recall_at_1
      value: 3.44
    - type: recall_at_3
      value: 6.642
    - type: recall_at_5
      value: 8.046000000000001
    - type: recall_at_10
      value: 10.903
    - type: recall_at_20
      value: 16.244
    - type: recall_at_100
      value: 31.702
    - type: recall_at_1000
      value: 64.905
    - type: precision_at_1
      value: 26.0
    - type: precision_at_3
      value: 22.0
    - type: precision_at_5
      value: 19.1
    - type: precision_at_10
      value: 15.35
    - type: precision_at_20
      value: 13.0
    - type: precision_at_100
      value: 7.920000000000001
    - type: precision_at_1000
      value: 2.2769999999999997
    - type: mrr_at_1
      value: 26.0
    - type: mrr_at_3
      value: 33.75
    - type: mrr_at_5
      value: 34.625
    - type: mrr_at_10
      value: 35.6232
    - type: mrr_at_20
      value: 36.229
    - type: mrr_at_100
      value: 36.717
    - type: mrr_at_1000
      value: 36.7906
    - type: nauc_ndcg_at_1_max
      value: 45.3643
    - type: nauc_ndcg_at_1_std
      value: 30.419200000000004
    - type: nauc_ndcg_at_1_diff1
      value: 23.1069
    - type: nauc_ndcg_at_3_max
      value: 54.793800000000005
    - type: nauc_ndcg_at_3_std
      value: 37.5309
    - type: nauc_ndcg_at_3_diff1
      value: 25.2997
    - type: nauc_ndcg_at_5_max
      value: 56.3971
    - type: nauc_ndcg_at_5_std
      value: 40.1252
    - type: nauc_ndcg_at_5_diff1
      value: 24.5363
    - type: nauc_ndcg_at_10_max
      value: 54.8812
    - type: nauc_ndcg_at_10_std
      value: 39.813700000000004
    - type: nauc_ndcg_at_10_diff1
      value: 21.8135
    - type: nauc_ndcg_at_20_max
      value: 53.821
    - type: nauc_ndcg_at_20_std
      value: 41.4119
    - type: nauc_ndcg_at_20_diff1
      value: 23.8397
    - type: nauc_ndcg_at_100_max
      value: 58.186800000000005
    - type: nauc_ndcg_at_100_std
      value: 47.5131
    - type: nauc_ndcg_at_100_diff1
      value: 22.016099999999998
    - type: nauc_ndcg_at_1000_max
      value: 63.188599999999994
    - type: nauc_ndcg_at_1000_std
      value: 53.569199999999995
    - type: nauc_ndcg_at_1000_diff1
      value: 16.2596
    - type: nauc_map_at_1_max
      value: 44.656400000000005
    - type: nauc_map_at_1_std
      value: 18.0396
    - type: nauc_map_at_1_diff1
      value: 46.7439
    - type: nauc_map_at_3_max
      value: 47.910199999999996
    - type: nauc_map_at_3_std
      value: 22.9629
    - type: nauc_map_at_3_diff1
      value: 45.7872
    - type: nauc_map_at_5_max
      value: 47.903400000000005
    - type: nauc_map_at_5_std
      value: 25.141799999999996
    - type: nauc_map_at_5_diff1
      value: 42.8426
    - type: nauc_map_at_10_max
      value: 47.062599999999996
    - type: nauc_map_at_10_std
      value: 27.643600000000003
    - type: nauc_map_at_10_diff1
      value: 37.3522
    - type: nauc_map_at_20_max
      value: 47.1474
    - type: nauc_map_at_20_std
      value: 31.1367
    - type: nauc_map_at_20_diff1
      value: 35.6935
    - type: nauc_map_at_100_max
      value: 53.796699999999994
    - type: nauc_map_at_100_std
      value: 42.4636
    - type: nauc_map_at_100_diff1
      value: 29.5198
    - type: nauc_map_at_1000_max
      value: 58.303799999999995
    - type: nauc_map_at_1000_std
      value: 49.193999999999996
    - type: nauc_map_at_1000_diff1
      value: 25.9758
    - type: nauc_recall_at_1_max
      value: 44.656400000000005
    - type: nauc_recall_at_1_std
      value: 18.0396
    - type: nauc_recall_at_1_diff1
      value: 46.7439
    - type: nauc_recall_at_3_max
      value: 47.9712
    - type: nauc_recall_at_3_std
      value: 24.403
    - type: nauc_recall_at_3_diff1
      value: 43.9697
    - type: nauc_recall_at_5_max
      value: 45.786500000000004
    - type: nauc_recall_at_5_std
      value: 26.670899999999996
    - type: nauc_recall_at_5_diff1
      value: 38.9454
    - type: nauc_recall_at_10_max
      value: 41.8495
    - type: nauc_recall_at_10_std
      value: 28.158499999999997
    - type: nauc_recall_at_10_diff1
      value: 29.1754
    - type: nauc_recall_at_20_max
      value: 35.3029
    - type: nauc_recall_at_20_std
      value: 28.608099999999997
    - type: nauc_recall_at_20_diff1
      value: 30.7132
    - type: nauc_recall_at_100_max
      value: 48.8887
    - type: nauc_recall_at_100_std
      value: 44.1464
    - type: nauc_recall_at_100_diff1
      value: 22.5521
    - type: nauc_recall_at_1000_max
      value: 59.721599999999995
    - type: nauc_recall_at_1000_std
      value: 62.6649
    - type: nauc_recall_at_1000_diff1
      value: 11.315999999999999
    - type: nauc_precision_at_1_max
      value: 42.808800000000005
    - type: nauc_precision_at_1_std
      value: 35.0879
    - type: nauc_precision_at_1_diff1
      value: 16.0605
    - type: nauc_precision_at_3_max
      value: 57.6241
    - type: nauc_precision_at_3_std
      value: 45.3184
    - type: nauc_precision_at_3_diff1
      value: 13.2253
    - type: nauc_precision_at_5_max
      value: 56.070600000000006
    - type: nauc_precision_at_5_std
      value: 47.815000000000005
    - type: nauc_precision_at_5_diff1
      value: 7.6166
    - type: nauc_precision_at_10_max
      value: 52.8107
    - type: nauc_precision_at_10_std
      value: 48.8904
    - type: nauc_precision_at_10_diff1
      value: -0.12160000000000001
    - type: nauc_precision_at_20_max
      value: 49.7597
    - type: nauc_precision_at_20_std
      value: 49.0284
    - type: nauc_precision_at_20_diff1
      value: -4.8077000000000005
    - type: nauc_precision_at_100_max
      value: 51.4923
    - type: nauc_precision_at_100_std
      value: 54.0702
    - type: nauc_precision_at_100_diff1
      value: -6.364400000000001
    - type: nauc_precision_at_1000_max
      value: 41.0295
    - type: nauc_precision_at_1000_std
      value: 38.389
    - type: nauc_precision_at_1000_diff1
      value: -10.9986
    - type: nauc_mrr_at_1_max
      value: 42.808800000000005
    - type: nauc_mrr_at_1_std
      value: 35.0879
    - type: nauc_mrr_at_1_diff1
      value: 16.0605
    - type: nauc_mrr_at_3_max
      value: 50.1471
    - type: nauc_mrr_at_3_std
      value: 37.419000000000004
    - type: nauc_mrr_at_3_diff1
      value: 13.4354
    - type: nauc_mrr_at_5_max
      value: 51.6494
    - type: nauc_mrr_at_5_std
      value: 38.4967
    - type: nauc_mrr_at_5_diff1
      value: 14.396
    - type: nauc_mrr_at_10_max
      value: 51.2505
    - type: nauc_mrr_at_10_std
      value: 38.1019
    - type: nauc_mrr_at_10_diff1
      value: 13.2467
    - type: nauc_mrr_at_20_max
      value: 51.224000000000004
    - type: nauc_mrr_at_20_std
      value: 38.1196
    - type: nauc_mrr_at_20_diff1
      value: 13.3101
    - type: nauc_mrr_at_100_max
      value: 51.0104
    - type: nauc_mrr_at_100_std
      value: 38.023
    - type: nauc_mrr_at_100_diff1
      value: 13.146099999999999
    - type: nauc_mrr_at_1000_max
      value: 50.9907
    - type: nauc_mrr_at_1000_std
      value: 38.0783
    - type: nauc_mrr_at_1000_diff1
      value: 13.181999999999999
    - type: main_score
      value: 18.684
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: dermatology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 56.99999999999999
    - type: ndcg_at_3
      value: 53.815999999999995
    - type: ndcg_at_5
      value: 55.147999999999996
    - type: ndcg_at_10
      value: 58.379999999999995
    - type: ndcg_at_20
      value: 62.053000000000004
    - type: ndcg_at_100
      value: 68.319
    - type: ndcg_at_1000
      value: 71.417
    - type: map_at_1
      value: 13.383000000000001
    - type: map_at_3
      value: 26.349
    - type: map_at_5
      value: 32.409
    - type: map_at_10
      value: 40.191
    - type: map_at_20
      value: 45.568
    - type: map_at_100
      value: 51.565000000000005
    - type: map_at_1000
      value: 52.825
    - type: recall_at_1
      value: 13.383000000000001
    - type: recall_at_3
      value: 30.053
    - type: recall_at_5
      value: 39.617999999999995
    - type: recall_at_10
      value: 53.89000000000001
    - type: recall_at_20
      value: 67.54599999999999
    - type: recall_at_100
      value: 89.642
    - type: recall_at_1000
      value: 99.442
    - type: precision_at_1
      value: 66.0
    - type: precision_at_3
      value: 55.167
    - type: precision_at_5
      value: 49.3
    - type: precision_at_10
      value: 39.5
    - type: precision_at_20
      value: 28.825
    - type: precision_at_100
      value: 10.334999999999999
    - type: precision_at_1000
      value: 1.3390000000000002
    - type: mrr_at_1
      value: 66.0
    - type: mrr_at_3
      value: 75.75
    - type: mrr_at_5
      value: 76.6
    - type: mrr_at_10
      value: 77.0468
    - type: mrr_at_20
      value: 77.28960000000001
    - type: mrr_at_100
      value: 77.312
    - type: mrr_at_1000
      value: 77.312
    - type: nauc_ndcg_at_1_max
      value: 42.2784
    - type: nauc_ndcg_at_1_std
      value: 20.6358
    - type: nauc_ndcg_at_1_diff1
      value: 45.803
    - type: nauc_ndcg_at_3_max
      value: 33.1528
    - type: nauc_ndcg_at_3_std
      value: 5.2341999999999995
    - type: nauc_ndcg_at_3_diff1
      value: 33.2999
    - type: nauc_ndcg_at_5_max
      value: 33.4856
    - type: nauc_ndcg_at_5_std
      value: -1.797
    - type: nauc_ndcg_at_5_diff1
      value: 35.65
    - type: nauc_ndcg_at_10_max
      value: 33.5882
    - type: nauc_ndcg_at_10_std
      value: -4.7413
    - type: nauc_ndcg_at_10_diff1
      value: 32.3708
    - type: nauc_ndcg_at_20_max
      value: 36.698
    - type: nauc_ndcg_at_20_std
      value: -4.7399
    - type: nauc_ndcg_at_20_diff1
      value: 32.31
    - type: nauc_ndcg_at_100_max
      value: 37.9711
    - type: nauc_ndcg_at_100_std
      value: 0.7188
    - type: nauc_ndcg_at_100_diff1
      value: 30.981199999999998
    - type: nauc_ndcg_at_1000_max
      value: 39.01
    - type: nauc_ndcg_at_1000_std
      value: 12.5777
    - type: nauc_ndcg_at_1000_diff1
      value: 31.7875
    - type: nauc_map_at_1_max
      value: 2.2602
    - type: nauc_map_at_1_std
      value: -30.1147
    - type: nauc_map_at_1_diff1
      value: 42.0209
    - type: nauc_map_at_3_max
      value: 3.7150000000000003
    - type: nauc_map_at_3_std
      value: -34.897
    - type: nauc_map_at_3_diff1
      value: 33.908
    - type: nauc_map_at_5_max
      value: 8.4404
    - type: nauc_map_at_5_std
      value: -36.6448
    - type: nauc_map_at_5_diff1
      value: 33.4709
    - type: nauc_map_at_10_max
      value: 16.4324
    - type: nauc_map_at_10_std
      value: -33.3115
    - type: nauc_map_at_10_diff1
      value: 28.662100000000002
    - type: nauc_map_at_20_max
      value: 21.8025
    - type: nauc_map_at_20_std
      value: -27.3198
    - type: nauc_map_at_20_diff1
      value: 26.041700000000002
    - type: nauc_map_at_100_max
      value: 26.609500000000004
    - type: nauc_map_at_100_std
      value: -12.804499999999999
    - type: nauc_map_at_100_diff1
      value: 23.1641
    - type: nauc_map_at_1000_max
      value: 27.4532
    - type: nauc_map_at_1000_std
      value: -7.6803
    - type: nauc_map_at_1000_diff1
      value: 23.1214
    - type: nauc_recall_at_1_max
      value: 2.2602
    - type: nauc_recall_at_1_std
      value: -30.1147
    - type: nauc_recall_at_1_diff1
      value: 42.0209
    - type: nauc_recall_at_3_max
      value: -3.0239
    - type: nauc_recall_at_3_std
      value: -40.383599999999994
    - type: nauc_recall_at_3_diff1
      value: 29.9087
    - type: nauc_recall_at_5_max
      value: 2.141
    - type: nauc_recall_at_5_std
      value: -43.4961
    - type: nauc_recall_at_5_diff1
      value: 28.571099999999998
    - type: nauc_recall_at_10_max
      value: 6.8745
    - type: nauc_recall_at_10_std
      value: -44.0475
    - type: nauc_recall_at_10_diff1
      value: 21.3471
    - type: nauc_recall_at_20_max
      value: 13.4685
    - type: nauc_recall_at_20_std
      value: -44.935199999999995
    - type: nauc_recall_at_20_diff1
      value: 17.552599999999998
    - type: nauc_recall_at_100_max
      value: 19.8098
    - type: nauc_recall_at_100_std
      value: -36.491600000000005
    - type: nauc_recall_at_100_diff1
      value: 3.5177
    - type: nauc_recall_at_1000_max
      value: 38.0945
    - type: nauc_recall_at_1000_std
      value: 28.4766
    - type: nauc_recall_at_1000_diff1
      value: -3.2825
    - type: nauc_precision_at_1_max
      value: 43.9045
    - type: nauc_precision_at_1_std
      value: 20.3052
    - type: nauc_precision_at_1_diff1
      value: 46.9124
    - type: nauc_precision_at_3_max
      value: 32.4069
    - type: nauc_precision_at_3_std
      value: 19.780800000000003
    - type: nauc_precision_at_3_diff1
      value: 9.3264
    - type: nauc_precision_at_5_max
      value: 35.2436
    - type: nauc_precision_at_5_std
      value: 26.284800000000004
    - type: nauc_precision_at_5_diff1
      value: 1.4762000000000002
    - type: nauc_precision_at_10_max
      value: 34.0488
    - type: nauc_precision_at_10_std
      value: 43.9403
    - type: nauc_precision_at_10_diff1
      value: -11.4419
    - type: nauc_precision_at_20_max
      value: 27.6387
    - type: nauc_precision_at_20_std
      value: 54.8187
    - type: nauc_precision_at_20_diff1
      value: -15.8486
    - type: nauc_precision_at_100_max
      value: 14.2797
    - type: nauc_precision_at_100_std
      value: 62.7694
    - type: nauc_precision_at_100_diff1
      value: -15.8703
    - type: nauc_precision_at_1000_max
      value: 9.6766
    - type: nauc_precision_at_1000_std
      value: 64.4804
    - type: nauc_precision_at_1000_diff1
      value: -12.1726
    - type: nauc_mrr_at_1_max
      value: 43.9045
    - type: nauc_mrr_at_1_std
      value: 20.3052
    - type: nauc_mrr_at_1_diff1
      value: 46.9124
    - type: nauc_mrr_at_3_max
      value: 41.680099999999996
    - type: nauc_mrr_at_3_std
      value: 20.413600000000002
    - type: nauc_mrr_at_3_diff1
      value: 44.3971
    - type: nauc_mrr_at_5_max
      value: 43.655100000000004
    - type: nauc_mrr_at_5_std
      value: 21.6815
    - type: nauc_mrr_at_5_diff1
      value: 44.8015
    - type: nauc_mrr_at_10_max
      value: 43.8731
    - type: nauc_mrr_at_10_std
      value: 21.704
    - type: nauc_mrr_at_10_diff1
      value: 45.651799999999994
    - type: nauc_mrr_at_20_max
      value: 43.6494
    - type: nauc_mrr_at_20_std
      value: 21.4422
    - type: nauc_mrr_at_20_diff1
      value: 45.4376
    - type: nauc_mrr_at_100_max
      value: 43.5906
    - type: nauc_mrr_at_100_std
      value: 21.4023
    - type: nauc_mrr_at_100_diff1
      value: 45.4133
    - type: nauc_mrr_at_1000_max
      value: 43.5906
    - type: nauc_mrr_at_1000_std
      value: 21.4023
    - type: nauc_mrr_at_1000_diff1
      value: 45.4133
    - type: main_score
      value: 58.379999999999995
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: dermatology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 25.25
    - type: ndcg_at_3
      value: 24.462
    - type: ndcg_at_5
      value: 24.709999999999997
    - type: ndcg_at_10
      value: 27.426000000000002
    - type: ndcg_at_20
      value: 31.517
    - type: ndcg_at_100
      value: 39.115
    - type: ndcg_at_1000
      value: 47.007
    - type: map_at_1
      value: 5.7509999999999994
    - type: map_at_3
      value: 11.652
    - type: map_at_5
      value: 14.052999999999999
    - type: map_at_10
      value: 17.31
    - type: map_at_20
      value: 20.288
    - type: map_at_100
      value: 23.880000000000003
    - type: map_at_1000
      value: 25.47
    - type: recall_at_1
      value: 5.7509999999999994
    - type: recall_at_3
      value: 14.343
    - type: recall_at_5
      value: 19.093
    - type: recall_at_10
      value: 27.607
    - type: recall_at_20
      value: 38.940000000000005
    - type: recall_at_100
      value: 62.632
    - type: recall_at_1000
      value: 92.482
    - type: precision_at_1
      value: 31.0
    - type: precision_at_3
      value: 25.667
    - type: precision_at_5
      value: 21.9
    - type: precision_at_10
      value: 18.5
    - type: precision_at_20
      value: 14.899999999999999
    - type: precision_at_100
      value: 6.660000000000001
    - type: precision_at_1000
      value: 1.2510000000000001
    - type: mrr_at_1
      value: 31.0
    - type: mrr_at_3
      value: 38.8333
    - type: mrr_at_5
      value: 40.1833
    - type: mrr_at_10
      value: 41.700199999999995
    - type: mrr_at_20
      value: 42.4573
    - type: mrr_at_100
      value: 42.8185
    - type: mrr_at_1000
      value: 42.8575
    - type: nauc_ndcg_at_1_max
      value: 30.5552
    - type: nauc_ndcg_at_1_std
      value: 11.4792
    - type: nauc_ndcg_at_1_diff1
      value: 5.6798
    - type: nauc_ndcg_at_3_max
      value: 42.5877
    - type: nauc_ndcg_at_3_std
      value: 11.561399999999999
    - type: nauc_ndcg_at_3_diff1
      value: 16.109499999999997
    - type: nauc_ndcg_at_5_max
      value: 41.526
    - type: nauc_ndcg_at_5_std
      value: 8.7759
    - type: nauc_ndcg_at_5_diff1
      value: 18.9848
    - type: nauc_ndcg_at_10_max
      value: 44.8402
    - type: nauc_ndcg_at_10_std
      value: 8.9034
    - type: nauc_ndcg_at_10_diff1
      value: 20.1171
    - type: nauc_ndcg_at_20_max
      value: 46.6789
    - type: nauc_ndcg_at_20_std
      value: 11.5659
    - type: nauc_ndcg_at_20_diff1
      value: 17.324
    - type: nauc_ndcg_at_100_max
      value: 49.778299999999994
    - type: nauc_ndcg_at_100_std
      value: 17.2405
    - type: nauc_ndcg_at_100_diff1
      value: 12.590399999999999
    - type: nauc_ndcg_at_1000_max
      value: 52.843399999999995
    - type: nauc_ndcg_at_1000_std
      value: 28.4096
    - type: nauc_ndcg_at_1000_diff1
      value: 11.2003
    - type: nauc_map_at_1_max
      value: 28.37
    - type: nauc_map_at_1_std
      value: -9.6805
    - type: nauc_map_at_1_diff1
      value: 22.9643
    - type: nauc_map_at_3_max
      value: 29.716900000000003
    - type: nauc_map_at_3_std
      value: -14.0931
    - type: nauc_map_at_3_diff1
      value: 28.193800000000003
    - type: nauc_map_at_5_max
      value: 29.2528
    - type: nauc_map_at_5_std
      value: -13.189899999999998
    - type: nauc_map_at_5_diff1
      value: 27.340700000000002
    - type: nauc_map_at_10_max
      value: 33.0456
    - type: nauc_map_at_10_std
      value: -8.3359
    - type: nauc_map_at_10_diff1
      value: 24.0125
    - type: nauc_map_at_20_max
      value: 38.487
    - type: nauc_map_at_20_std
      value: -1.8057
    - type: nauc_map_at_20_diff1
      value: 21.898200000000003
    - type: nauc_map_at_100_max
      value: 43.062400000000004
    - type: nauc_map_at_100_std
      value: 7.0085
    - type: nauc_map_at_100_diff1
      value: 18.4593
    - type: nauc_map_at_1000_max
      value: 44.7972
    - type: nauc_map_at_1000_std
      value: 11.9907
    - type: nauc_map_at_1000_diff1
      value: 17.4989
    - type: nauc_recall_at_1_max
      value: 28.37
    - type: nauc_recall_at_1_std
      value: -9.6805
    - type: nauc_recall_at_1_diff1
      value: 22.9643
    - type: nauc_recall_at_3_max
      value: 32.583400000000005
    - type: nauc_recall_at_3_std
      value: -14.077799999999998
    - type: nauc_recall_at_3_diff1
      value: 34.2738
    - type: nauc_recall_at_5_max
      value: 29.554799999999997
    - type: nauc_recall_at_5_std
      value: -13.7679
    - type: nauc_recall_at_5_diff1
      value: 34.0684
    - type: nauc_recall_at_10_max
      value: 34.7648
    - type: nauc_recall_at_10_std
      value: -6.702800000000001
    - type: nauc_recall_at_10_diff1
      value: 27.4069
    - type: nauc_recall_at_20_max
      value: 36.5072
    - type: nauc_recall_at_20_std
      value: -1.8129
    - type: nauc_recall_at_20_diff1
      value: 20.105500000000003
    - type: nauc_recall_at_100_max
      value: 44.756800000000005
    - type: nauc_recall_at_100_std
      value: 13.087599999999998
    - type: nauc_recall_at_100_diff1
      value: 8.463099999999999
    - type: nauc_recall_at_1000_max
      value: 71.0217
    - type: nauc_recall_at_1000_std
      value: 66.8821
    - type: nauc_recall_at_1000_diff1
      value: -5.8082
    - type: nauc_precision_at_1_max
      value: 31.4835
    - type: nauc_precision_at_1_std
      value: 12.057500000000001
    - type: nauc_precision_at_1_diff1
      value: 4.9834000000000005
    - type: nauc_precision_at_3_max
      value: 41.4188
    - type: nauc_precision_at_3_std
      value: 19.1824
    - type: nauc_precision_at_3_diff1
      value: 8.4729
    - type: nauc_precision_at_5_max
      value: 39.825
    - type: nauc_precision_at_5_std
      value: 23.592399999999998
    - type: nauc_precision_at_5_diff1
      value: 4.0221
    - type: nauc_precision_at_10_max
      value: 43.7645
    - type: nauc_precision_at_10_std
      value: 32.7934
    - type: nauc_precision_at_10_diff1
      value: -1.2515
    - type: nauc_precision_at_20_max
      value: 43.0757
    - type: nauc_precision_at_20_std
      value: 42.4566
    - type: nauc_precision_at_20_diff1
      value: -7.9428
    - type: nauc_precision_at_100_max
      value: 31.418400000000002
    - type: nauc_precision_at_100_std
      value: 56.1558
    - type: nauc_precision_at_100_diff1
      value: -17.5248
    - type: nauc_precision_at_1000_max
      value: 18.6971
    - type: nauc_precision_at_1000_std
      value: 50.943000000000005
    - type: nauc_precision_at_1000_diff1
      value: -12.6889
    - type: nauc_mrr_at_1_max
      value: 31.4835
    - type: nauc_mrr_at_1_std
      value: 12.057500000000001
    - type: nauc_mrr_at_1_diff1
      value: 4.9834000000000005
    - type: nauc_mrr_at_3_max
      value: 38.426700000000004
    - type: nauc_mrr_at_3_std
      value: 15.7666
    - type: nauc_mrr_at_3_diff1
      value: 11.0725
    - type: nauc_mrr_at_5_max
      value: 38.1481
    - type: nauc_mrr_at_5_std
      value: 16.1965
    - type: nauc_mrr_at_5_diff1
      value: 9.7109
    - type: nauc_mrr_at_10_max
      value: 39.7563
    - type: nauc_mrr_at_10_std
      value: 17.0487
    - type: nauc_mrr_at_10_diff1
      value: 9.6843
    - type: nauc_mrr_at_20_max
      value: 39.2711
    - type: nauc_mrr_at_20_std
      value: 17.1654
    - type: nauc_mrr_at_20_diff1
      value: 8.7669
    - type: nauc_mrr_at_100_max
      value: 39.2493
    - type: nauc_mrr_at_100_std
      value: 17.198
    - type: nauc_mrr_at_100_diff1
      value: 9.006699999999999
    - type: nauc_mrr_at_1000_max
      value: 39.2259
    - type: nauc_mrr_at_1000_std
      value: 17.1768
    - type: nauc_mrr_at_1000_diff1
      value: 9.0104
    - type: main_score
      value: 27.426000000000002
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: dermatology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 31.0
    - type: ndcg_at_3
      value: 28.693999999999996
    - type: ndcg_at_5
      value: 30.203000000000003
    - type: ndcg_at_10
      value: 33.913
    - type: ndcg_at_20
      value: 38.05
    - type: ndcg_at_100
      value: 45.211
    - type: ndcg_at_1000
      value: 51.315
    - type: map_at_1
      value: 6.069999999999999
    - type: map_at_3
      value: 12.674
    - type: map_at_5
      value: 16.296
    - type: map_at_10
      value: 21.586
    - type: map_at_20
      value: 25.115
    - type: map_at_100
      value: 29.037000000000003
    - type: map_at_1000
      value: 30.389
    - type: recall_at_1
      value: 6.069999999999999
    - type: recall_at_3
      value: 15.529000000000002
    - type: recall_at_5
      value: 22.747
    - type: recall_at_10
      value: 34.821000000000005
    - type: recall_at_20
      value: 46.635
    - type: recall_at_100
      value: 69.726
    - type: recall_at_1000
      value: 92.412
    - type: precision_at_1
      value: 36.5
    - type: precision_at_3
      value: 30.833
    - type: precision_at_5
      value: 28.499999999999996
    - type: precision_at_10
      value: 24.349999999999998
    - type: precision_at_20
      value: 18.75
    - type: precision_at_100
      value: 7.46
    - type: precision_at_1000
      value: 1.2309999999999999
    - type: mrr_at_1
      value: 36.5
    - type: mrr_at_3
      value: 43.75
    - type: mrr_at_5
      value: 46.025
    - type: mrr_at_10
      value: 47.2933
    - type: mrr_at_20
      value: 47.9269
    - type: mrr_at_100
      value: 48.2183
    - type: mrr_at_1000
      value: 48.2385
    - type: nauc_ndcg_at_1_max
      value: 34.7176
    - type: nauc_ndcg_at_1_std
      value: 24.3626
    - type: nauc_ndcg_at_1_diff1
      value: 14.8799
    - type: nauc_ndcg_at_3_max
      value: 44.1357
    - type: nauc_ndcg_at_3_std
      value: 20.0165
    - type: nauc_ndcg_at_3_diff1
      value: 7.1797
    - type: nauc_ndcg_at_5_max
      value: 44.8908
    - type: nauc_ndcg_at_5_std
      value: 18.2622
    - type: nauc_ndcg_at_5_diff1
      value: 8.1525
    - type: nauc_ndcg_at_10_max
      value: 47.6186
    - type: nauc_ndcg_at_10_std
      value: 16.781299999999998
    - type: nauc_ndcg_at_10_diff1
      value: 9.7705
    - type: nauc_ndcg_at_20_max
      value: 49.9604
    - type: nauc_ndcg_at_20_std
      value: 17.9142
    - type: nauc_ndcg_at_20_diff1
      value: 8.8726
    - type: nauc_ndcg_at_100_max
      value: 53.24379999999999
    - type: nauc_ndcg_at_100_std
      value: 25.1583
    - type: nauc_ndcg_at_100_diff1
      value: 8.236400000000001
    - type: nauc_ndcg_at_1000_max
      value: 50.3497
    - type: nauc_ndcg_at_1000_std
      value: 35.7518
    - type: nauc_ndcg_at_1000_diff1
      value: 3.6366
    - type: nauc_map_at_1_max
      value: 30.600699999999996
    - type: nauc_map_at_1_std
      value: -4.7101
    - type: nauc_map_at_1_diff1
      value: 27.4254
    - type: nauc_map_at_3_max
      value: 34.5948
    - type: nauc_map_at_3_std
      value: -7.008699999999999
    - type: nauc_map_at_3_diff1
      value: 17.810699999999997
    - type: nauc_map_at_5_max
      value: 35.4128
    - type: nauc_map_at_5_std
      value: -6.8513
    - type: nauc_map_at_5_diff1
      value: 14.3932
    - type: nauc_map_at_10_max
      value: 40.1998
    - type: nauc_map_at_10_std
      value: -1.1526
    - type: nauc_map_at_10_diff1
      value: 11.0807
    - type: nauc_map_at_20_max
      value: 44.6921
    - type: nauc_map_at_20_std
      value: 5.161700000000001
    - type: nauc_map_at_20_diff1
      value: 9.1443
    - type: nauc_map_at_100_max
      value: 48.127199999999995
    - type: nauc_map_at_100_std
      value: 14.274999999999999
    - type: nauc_map_at_100_diff1
      value: 7.5502
    - type: nauc_map_at_1000_max
      value: 48.1338
    - type: nauc_map_at_1000_std
      value: 18.9952
    - type: nauc_map_at_1000_diff1
      value: 6.1902
    - type: nauc_recall_at_1_max
      value: 30.600699999999996
    - type: nauc_recall_at_1_std
      value: -4.7101
    - type: nauc_recall_at_1_diff1
      value: 27.4254
    - type: nauc_recall_at_3_max
      value: 37.358999999999995
    - type: nauc_recall_at_3_std
      value: -6.412
    - type: nauc_recall_at_3_diff1
      value: 17.1264
    - type: nauc_recall_at_5_max
      value: 32.5293
    - type: nauc_recall_at_5_std
      value: -10.5716
    - type: nauc_recall_at_5_diff1
      value: 14.913000000000002
    - type: nauc_recall_at_10_max
      value: 39.690999999999995
    - type: nauc_recall_at_10_std
      value: -5.520300000000001
    - type: nauc_recall_at_10_diff1
      value: 13.8849
    - type: nauc_recall_at_20_max
      value: 45.4972
    - type: nauc_recall_at_20_std
      value: -2.3068999999999997
    - type: nauc_recall_at_20_diff1
      value: 11.0097
    - type: nauc_recall_at_100_max
      value: 57.6612
    - type: nauc_recall_at_100_std
      value: 16.7538
    - type: nauc_recall_at_100_diff1
      value: 10.347000000000001
    - type: nauc_recall_at_1000_max
      value: 70.0951
    - type: nauc_recall_at_1000_std
      value: 72.3359
    - type: nauc_recall_at_1000_diff1
      value: -16.9591
    - type: nauc_precision_at_1_max
      value: 33.2225
    - type: nauc_precision_at_1_std
      value: 23.122400000000003
    - type: nauc_precision_at_1_diff1
      value: 16.112199999999998
    - type: nauc_precision_at_3_max
      value: 43.839299999999994
    - type: nauc_precision_at_3_std
      value: 26.492700000000003
    - type: nauc_precision_at_3_diff1
      value: -2.8691
    - type: nauc_precision_at_5_max
      value: 43.7524
    - type: nauc_precision_at_5_std
      value: 32.3313
    - type: nauc_precision_at_5_diff1
      value: -4.8185
    - type: nauc_precision_at_10_max
      value: 41.793400000000005
    - type: nauc_precision_at_10_std
      value: 36.8825
    - type: nauc_precision_at_10_diff1
      value: -8.4039
    - type: nauc_precision_at_20_max
      value: 38.3037
    - type: nauc_precision_at_20_std
      value: 47.396100000000004
    - type: nauc_precision_at_20_diff1
      value: -8.7708
    - type: nauc_precision_at_100_max
      value: 21.5088
    - type: nauc_precision_at_100_std
      value: 59.5302
    - type: nauc_precision_at_100_diff1
      value: -11.9556
    - type: nauc_precision_at_1000_max
      value: -0.3614
    - type: nauc_precision_at_1000_std
      value: 53.013600000000004
    - type: nauc_precision_at_1000_diff1
      value: -16.9022
    - type: nauc_mrr_at_1_max
      value: 33.2225
    - type: nauc_mrr_at_1_std
      value: 23.122400000000003
    - type: nauc_mrr_at_1_diff1
      value: 16.112199999999998
    - type: nauc_mrr_at_3_max
      value: 41.2421
    - type: nauc_mrr_at_3_std
      value: 24.9103
    - type: nauc_mrr_at_3_diff1
      value: 10.6623
    - type: nauc_mrr_at_5_max
      value: 40.8046
    - type: nauc_mrr_at_5_std
      value: 26.517699999999998
    - type: nauc_mrr_at_5_diff1
      value: 12.2735
    - type: nauc_mrr_at_10_max
      value: 40.2669
    - type: nauc_mrr_at_10_std
      value: 26.222800000000003
    - type: nauc_mrr_at_10_diff1
      value: 11.1785
    - type: nauc_mrr_at_20_max
      value: 40.2118
    - type: nauc_mrr_at_20_std
      value: 25.9945
    - type: nauc_mrr_at_20_diff1
      value: 11.3524
    - type: nauc_mrr_at_100_max
      value: 40.396300000000004
    - type: nauc_mrr_at_100_std
      value: 26.235799999999998
    - type: nauc_mrr_at_100_diff1
      value: 11.4847
    - type: nauc_mrr_at_1000_max
      value: 40.3684
    - type: nauc_mrr_at_1000_std
      value: 26.217299999999998
    - type: nauc_mrr_at_1000_diff1
      value: 11.4967
    - type: main_score
      value: 33.913
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: gastroenterology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 63.24999999999999
    - type: ndcg_at_3
      value: 58.5
    - type: ndcg_at_5
      value: 56.14
    - type: ndcg_at_10
      value: 55.42
    - type: ndcg_at_20
      value: 56.738
    - type: ndcg_at_100
      value: 64.412
    - type: ndcg_at_1000
      value: 72.794
    - type: map_at_1
      value: 6.805
    - type: map_at_3
      value: 13.644
    - type: map_at_5
      value: 17.426
    - type: map_at_10
      value: 23.127
    - type: map_at_20
      value: 29.354999999999997
    - type: map_at_100
      value: 41.601
    - type: map_at_1000
      value: 46.983999999999995
    - type: recall_at_1
      value: 6.805
    - type: recall_at_3
      value: 14.738000000000001
    - type: recall_at_5
      value: 19.801
    - type: recall_at_10
      value: 29.599999999999998
    - type: recall_at_20
      value: 41.77
    - type: recall_at_100
      value: 72.682
    - type: recall_at_1000
      value: 97.773
    - type: precision_at_1
      value: 74.5
    - type: precision_at_3
      value: 66.667
    - type: precision_at_5
      value: 60.199999999999996
    - type: precision_at_10
      value: 52.1
    - type: precision_at_20
      value: 44.574999999999996
    - type: precision_at_100
      value: 23.51
    - type: precision_at_1000
      value: 4.7
    - type: mrr_at_1
      value: 74.5
    - type: mrr_at_3
      value: 82.08330000000001
    - type: mrr_at_5
      value: 82.5583
    - type: mrr_at_10
      value: 83.19919999999999
    - type: mrr_at_20
      value: 83.2761
    - type: mrr_at_100
      value: 83.3136
    - type: mrr_at_1000
      value: 83.3179
    - type: nauc_ndcg_at_1_max
      value: 30.5093
    - type: nauc_ndcg_at_1_std
      value: 15.548699999999998
    - type: nauc_ndcg_at_1_diff1
      value: 29.909200000000002
    - type: nauc_ndcg_at_3_max
      value: 37.911
    - type: nauc_ndcg_at_3_std
      value: 21.8751
    - type: nauc_ndcg_at_3_diff1
      value: 15.7172
    - type: nauc_ndcg_at_5_max
      value: 38.337500000000006
    - type: nauc_ndcg_at_5_std
      value: 18.2302
    - type: nauc_ndcg_at_5_diff1
      value: 14.9655
    - type: nauc_ndcg_at_10_max
      value: 41.3816
    - type: nauc_ndcg_at_10_std
      value: 17.222
    - type: nauc_ndcg_at_10_diff1
      value: 17.309
    - type: nauc_ndcg_at_20_max
      value: 45.068799999999996
    - type: nauc_ndcg_at_20_std
      value: 17.0449
    - type: nauc_ndcg_at_20_diff1
      value: 18.784100000000002
    - type: nauc_ndcg_at_100_max
      value: 46.426899999999996
    - type: nauc_ndcg_at_100_std
      value: 30.9243
    - type: nauc_ndcg_at_100_diff1
      value: 20.328699999999998
    - type: nauc_ndcg_at_1000_max
      value: 48.744
    - type: nauc_ndcg_at_1000_std
      value: 33.278
    - type: nauc_ndcg_at_1000_diff1
      value: 14.552100000000001
    - type: nauc_map_at_1_max
      value: 8.1792
    - type: nauc_map_at_1_std
      value: -6.5594
    - type: nauc_map_at_1_diff1
      value: 49.4009
    - type: nauc_map_at_3_max
      value: 21.1779
    - type: nauc_map_at_3_std
      value: 0.5627
    - type: nauc_map_at_3_diff1
      value: 33.3576
    - type: nauc_map_at_5_max
      value: 23.1508
    - type: nauc_map_at_5_std
      value: 3.5987
    - type: nauc_map_at_5_diff1
      value: 26.9839
    - type: nauc_map_at_10_max
      value: 26.486700000000003
    - type: nauc_map_at_10_std
      value: 8.6895
    - type: nauc_map_at_10_diff1
      value: 21.1984
    - type: nauc_map_at_20_max
      value: 30.484
    - type: nauc_map_at_20_std
      value: 13.815
    - type: nauc_map_at_20_diff1
      value: 19.4513
    - type: nauc_map_at_100_max
      value: 41.3424
    - type: nauc_map_at_100_std
      value: 29.133300000000002
    - type: nauc_map_at_100_diff1
      value: 11.1852
    - type: nauc_map_at_1000_max
      value: 47.9787
    - type: nauc_map_at_1000_std
      value: 28.8993
    - type: nauc_map_at_1000_diff1
      value: 5.1209999999999996
    - type: nauc_recall_at_1_max
      value: 8.1792
    - type: nauc_recall_at_1_std
      value: -6.5594
    - type: nauc_recall_at_1_diff1
      value: 49.4009
    - type: nauc_recall_at_3_max
      value: 18.0985
    - type: nauc_recall_at_3_std
      value: -1.6192000000000002
    - type: nauc_recall_at_3_diff1
      value: 30.264200000000002
    - type: nauc_recall_at_5_max
      value: 16.0719
    - type: nauc_recall_at_5_std
      value: -1.7076
    - type: nauc_recall_at_5_diff1
      value: 27.366200000000003
    - type: nauc_recall_at_10_max
      value: 12.537899999999999
    - type: nauc_recall_at_10_std
      value: 0.514
    - type: nauc_recall_at_10_diff1
      value: 22.575799999999997
    - type: nauc_recall_at_20_max
      value: 10.0353
    - type: nauc_recall_at_20_std
      value: 2.8885
    - type: nauc_recall_at_20_diff1
      value: 21.1941
    - type: nauc_recall_at_100_max
      value: 12.2927
    - type: nauc_recall_at_100_std
      value: 24.7839
    - type: nauc_recall_at_100_diff1
      value: 22.8795
    - type: nauc_recall_at_1000_max
      value: -12.1228
    - type: nauc_recall_at_1000_std
      value: 71.4063
    - type: nauc_recall_at_1000_diff1
      value: 29.4754
    - type: nauc_precision_at_1_max
      value: 41.396699999999996
    - type: nauc_precision_at_1_std
      value: 32.6591
    - type: nauc_precision_at_1_diff1
      value: 25.3386
    - type: nauc_precision_at_3_max
      value: 42.5837
    - type: nauc_precision_at_3_std
      value: 30.999399999999998
    - type: nauc_precision_at_3_diff1
      value: -11.8464
    - type: nauc_precision_at_5_max
      value: 37.371300000000005
    - type: nauc_precision_at_5_std
      value: 22.783800000000003
    - type: nauc_precision_at_5_diff1
      value: -20.037399999999998
    - type: nauc_precision_at_10_max
      value: 33.7087
    - type: nauc_precision_at_10_std
      value: 22.3454
    - type: nauc_precision_at_10_diff1
      value: -22.0618
    - type: nauc_precision_at_20_max
      value: 29.107499999999998
    - type: nauc_precision_at_20_std
      value: 17.0055
    - type: nauc_precision_at_20_diff1
      value: -22.247500000000002
    - type: nauc_precision_at_100_max
      value: 19.4679
    - type: nauc_precision_at_100_std
      value: 7.725600000000001
    - type: nauc_precision_at_100_diff1
      value: -22.0965
    - type: nauc_precision_at_1000_max
      value: 12.985299999999999
    - type: nauc_precision_at_1000_std
      value: -15.038599999999999
    - type: nauc_precision_at_1000_diff1
      value: -22.500999999999998
    - type: nauc_mrr_at_1_max
      value: 41.396699999999996
    - type: nauc_mrr_at_1_std
      value: 32.6591
    - type: nauc_mrr_at_1_diff1
      value: 25.3386
    - type: nauc_mrr_at_3_max
      value: 49.346000000000004
    - type: nauc_mrr_at_3_std
      value: 42.0854
    - type: nauc_mrr_at_3_diff1
      value: 20.8887
    - type: nauc_mrr_at_5_max
      value: 49.0721
    - type: nauc_mrr_at_5_std
      value: 40.6611
    - type: nauc_mrr_at_5_diff1
      value: 22.686899999999998
    - type: nauc_mrr_at_10_max
      value: 48.5527
    - type: nauc_mrr_at_10_std
      value: 40.3495
    - type: nauc_mrr_at_10_diff1
      value: 23.6878
    - type: nauc_mrr_at_20_max
      value: 48.455
    - type: nauc_mrr_at_20_std
      value: 40.0814
    - type: nauc_mrr_at_20_diff1
      value: 23.9185
    - type: nauc_mrr_at_100_max
      value: 48.3696
    - type: nauc_mrr_at_100_std
      value: 40.065
    - type: nauc_mrr_at_100_diff1
      value: 23.875
    - type: nauc_mrr_at_1000_max
      value: 48.3586
    - type: nauc_mrr_at_1000_std
      value: 40.0662
    - type: nauc_mrr_at_1000_diff1
      value: 23.8532
    - type: main_score
      value: 55.42
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: gastroenterology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 24.75
    - type: ndcg_at_3
      value: 23.608
    - type: ndcg_at_5
      value: 23.939
    - type: ndcg_at_10
      value: 23.983999999999998
    - type: ndcg_at_20
      value: 25.901999999999997
    - type: ndcg_at_100
      value: 32.934000000000005
    - type: ndcg_at_1000
      value: 45.14
    - type: map_at_1
      value: 2.541
    - type: map_at_3
      value: 5.497
    - type: map_at_5
      value: 7.659000000000001
    - type: map_at_10
      value: 9.778
    - type: map_at_20
      value: 11.962
    - type: map_at_100
      value: 16.736
    - type: map_at_1000
      value: 20.135
    - type: recall_at_1
      value: 2.541
    - type: recall_at_3
      value: 6.39
    - type: recall_at_5
      value: 10.511
    - type: recall_at_10
      value: 14.815999999999999
    - type: recall_at_20
      value: 22.067
    - type: recall_at_100
      value: 45.013
    - type: recall_at_1000
      value: 80.375
    - type: precision_at_1
      value: 32.0
    - type: precision_at_3
      value: 28.333000000000002
    - type: precision_at_5
      value: 27.1
    - type: precision_at_10
      value: 22.85
    - type: precision_at_20
      value: 19.625
    - type: precision_at_100
      value: 11.945
    - type: precision_at_1000
      value: 3.515
    - type: mrr_at_1
      value: 32.0
    - type: mrr_at_3
      value: 38.9167
    - type: mrr_at_5
      value: 40.9667
    - type: mrr_at_10
      value: 42.573
    - type: mrr_at_20
      value: 43.2429
    - type: mrr_at_100
      value: 43.585
    - type: mrr_at_1000
      value: 43.6201
    - type: nauc_ndcg_at_1_max
      value: 38.292500000000004
    - type: nauc_ndcg_at_1_std
      value: 31.045499999999997
    - type: nauc_ndcg_at_1_diff1
      value: 7.539700000000001
    - type: nauc_ndcg_at_3_max
      value: 48.530699999999996
    - type: nauc_ndcg_at_3_std
      value: 38.114
    - type: nauc_ndcg_at_3_diff1
      value: 13.930000000000001
    - type: nauc_ndcg_at_5_max
      value: 53.109899999999996
    - type: nauc_ndcg_at_5_std
      value: 40.4119
    - type: nauc_ndcg_at_5_diff1
      value: 16.4794
    - type: nauc_ndcg_at_10_max
      value: 56.45099999999999
    - type: nauc_ndcg_at_10_std
      value: 43.573499999999996
    - type: nauc_ndcg_at_10_diff1
      value: 17.793300000000002
    - type: nauc_ndcg_at_20_max
      value: 60.3572
    - type: nauc_ndcg_at_20_std
      value: 49.2677
    - type: nauc_ndcg_at_20_diff1
      value: 19.0431
    - type: nauc_ndcg_at_100_max
      value: 58.897800000000004
    - type: nauc_ndcg_at_100_std
      value: 58.668600000000005
    - type: nauc_ndcg_at_100_diff1
      value: 20.488799999999998
    - type: nauc_ndcg_at_1000_max
      value: 58.6925
    - type: nauc_ndcg_at_1000_std
      value: 56.21119999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 15.9784
    - type: nauc_map_at_1_max
      value: 30.462400000000002
    - type: nauc_map_at_1_std
      value: 33.3978
    - type: nauc_map_at_1_diff1
      value: 38.5237
    - type: nauc_map_at_3_max
      value: 46.6683
    - type: nauc_map_at_3_std
      value: 40.834900000000005
    - type: nauc_map_at_3_diff1
      value: 35.3553
    - type: nauc_map_at_5_max
      value: 51.3247
    - type: nauc_map_at_5_std
      value: 43.430400000000006
    - type: nauc_map_at_5_diff1
      value: 32.006299999999996
    - type: nauc_map_at_10_max
      value: 55.0117
    - type: nauc_map_at_10_std
      value: 46.3951
    - type: nauc_map_at_10_diff1
      value: 28.022999999999996
    - type: nauc_map_at_20_max
      value: 56.61279999999999
    - type: nauc_map_at_20_std
      value: 50.6861
    - type: nauc_map_at_20_diff1
      value: 25.9926
    - type: nauc_map_at_100_max
      value: 57.3647
    - type: nauc_map_at_100_std
      value: 57.78
    - type: nauc_map_at_100_diff1
      value: 21.236
    - type: nauc_map_at_1000_max
      value: 61.279700000000005
    - type: nauc_map_at_1000_std
      value: 55.58030000000001
    - type: nauc_map_at_1000_diff1
      value: 17.4497
    - type: nauc_recall_at_1_max
      value: 30.462400000000002
    - type: nauc_recall_at_1_std
      value: 33.3978
    - type: nauc_recall_at_1_diff1
      value: 38.5237
    - type: nauc_recall_at_3_max
      value: 46.1706
    - type: nauc_recall_at_3_std
      value: 38.5525
    - type: nauc_recall_at_3_diff1
      value: 34.3394
    - type: nauc_recall_at_5_max
      value: 43.9982
    - type: nauc_recall_at_5_std
      value: 36.9704
    - type: nauc_recall_at_5_diff1
      value: 26.4609
    - type: nauc_recall_at_10_max
      value: 48.3495
    - type: nauc_recall_at_10_std
      value: 40.754000000000005
    - type: nauc_recall_at_10_diff1
      value: 21.409200000000002
    - type: nauc_recall_at_20_max
      value: 49.7858
    - type: nauc_recall_at_20_std
      value: 47.6663
    - type: nauc_recall_at_20_diff1
      value: 20.288800000000002
    - type: nauc_recall_at_100_max
      value: 43.5882
    - type: nauc_recall_at_100_std
      value: 60.77160000000001
    - type: nauc_recall_at_100_diff1
      value: 20.619699999999998
    - type: nauc_recall_at_1000_max
      value: 57.527899999999995
    - type: nauc_recall_at_1000_std
      value: 77.9242
    - type: nauc_recall_at_1000_diff1
      value: 21.8565
    - type: nauc_precision_at_1_max
      value: 40.0045
    - type: nauc_precision_at_1_std
      value: 28.464499999999997
    - type: nauc_precision_at_1_diff1
      value: 6.1918
    - type: nauc_precision_at_3_max
      value: 50.7363
    - type: nauc_precision_at_3_std
      value: 35.2469
    - type: nauc_precision_at_3_diff1
      value: 4.5440000000000005
    - type: nauc_precision_at_5_max
      value: 55.355
    - type: nauc_precision_at_5_std
      value: 36.7226
    - type: nauc_precision_at_5_diff1
      value: 4.345899999999999
    - type: nauc_precision_at_10_max
      value: 55.1894
    - type: nauc_precision_at_10_std
      value: 37.8104
    - type: nauc_precision_at_10_diff1
      value: 1.3243
    - type: nauc_precision_at_20_max
      value: 53.0123
    - type: nauc_precision_at_20_std
      value: 34.2509
    - type: nauc_precision_at_20_diff1
      value: -2.3846
    - type: nauc_precision_at_100_max
      value: 39.6665
    - type: nauc_precision_at_100_std
      value: 20.041
    - type: nauc_precision_at_100_diff1
      value: -9.078700000000001
    - type: nauc_precision_at_1000_max
      value: 29.242099999999997
    - type: nauc_precision_at_1000_std
      value: -17.8247
    - type: nauc_precision_at_1000_diff1
      value: -11.6906
    - type: nauc_mrr_at_1_max
      value: 40.0045
    - type: nauc_mrr_at_1_std
      value: 28.464499999999997
    - type: nauc_mrr_at_1_diff1
      value: 6.1918
    - type: nauc_mrr_at_3_max
      value: 44.8685
    - type: nauc_mrr_at_3_std
      value: 31.150299999999998
    - type: nauc_mrr_at_3_diff1
      value: 7.2494000000000005
    - type: nauc_mrr_at_5_max
      value: 44.649100000000004
    - type: nauc_mrr_at_5_std
      value: 31.2209
    - type: nauc_mrr_at_5_diff1
      value: 8.2678
    - type: nauc_mrr_at_10_max
      value: 45.3643
    - type: nauc_mrr_at_10_std
      value: 32.7704
    - type: nauc_mrr_at_10_diff1
      value: 7.9273
    - type: nauc_mrr_at_20_max
      value: 45.6745
    - type: nauc_mrr_at_20_std
      value: 32.7141
    - type: nauc_mrr_at_20_diff1
      value: 7.692400000000001
    - type: nauc_mrr_at_100_max
      value: 45.4799
    - type: nauc_mrr_at_100_std
      value: 32.4976
    - type: nauc_mrr_at_100_diff1
      value: 7.861700000000001
    - type: nauc_mrr_at_1000_max
      value: 45.4435
    - type: nauc_mrr_at_1000_std
      value: 32.462
    - type: nauc_mrr_at_1000_diff1
      value: 7.846
    - type: main_score
      value: 23.983999999999998
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: gastroenterology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 33.0
    - type: ndcg_at_3
      value: 31.025000000000002
    - type: ndcg_at_5
      value: 31.290000000000003
    - type: ndcg_at_10
      value: 31.863999999999997
    - type: ndcg_at_20
      value: 33.087
    - type: ndcg_at_100
      value: 40.829
    - type: ndcg_at_1000
      value: 52.308
    - type: map_at_1
      value: 3.483
    - type: map_at_3
      value: 6.7589999999999995
    - type: map_at_5
      value: 9.339
    - type: map_at_10
      value: 12.562999999999999
    - type: map_at_20
      value: 15.661
    - type: map_at_100
      value: 22.269
    - type: map_at_1000
      value: 26.366
    - type: recall_at_1
      value: 3.483
    - type: recall_at_3
      value: 7.878
    - type: recall_at_5
      value: 12.071
    - type: recall_at_10
      value: 18.133
    - type: recall_at_20
      value: 25.778000000000002
    - type: recall_at_100
      value: 51.747
    - type: recall_at_1000
      value: 86.577
    - type: precision_at_1
      value: 44.5
    - type: precision_at_3
      value: 37.833
    - type: precision_at_5
      value: 36.0
    - type: precision_at_10
      value: 32.0
    - type: precision_at_20
      value: 27.250000000000004
    - type: precision_at_100
      value: 15.629999999999999
    - type: precision_at_1000
      value: 3.962
    - type: mrr_at_1
      value: 44.5
    - type: mrr_at_3
      value: 52.5
    - type: mrr_at_5
      value: 53.75
    - type: mrr_at_10
      value: 54.7087
    - type: mrr_at_20
      value: 55.441700000000004
    - type: mrr_at_100
      value: 55.7371
    - type: mrr_at_1000
      value: 55.7543
    - type: nauc_ndcg_at_1_max
      value: 43.1991
    - type: nauc_ndcg_at_1_std
      value: 21.0742
    - type: nauc_ndcg_at_1_diff1
      value: 25.378099999999996
    - type: nauc_ndcg_at_3_max
      value: 48.2356
    - type: nauc_ndcg_at_3_std
      value: 26.9982
    - type: nauc_ndcg_at_3_diff1
      value: 15.046000000000001
    - type: nauc_ndcg_at_5_max
      value: 50.8549
    - type: nauc_ndcg_at_5_std
      value: 29.8923
    - type: nauc_ndcg_at_5_diff1
      value: 14.678099999999999
    - type: nauc_ndcg_at_10_max
      value: 52.5725
    - type: nauc_ndcg_at_10_std
      value: 33.7675
    - type: nauc_ndcg_at_10_diff1
      value: 12.284699999999999
    - type: nauc_ndcg_at_20_max
      value: 54.851499999999994
    - type: nauc_ndcg_at_20_std
      value: 39.1904
    - type: nauc_ndcg_at_20_diff1
      value: 10.9117
    - type: nauc_ndcg_at_100_max
      value: 58.007299999999994
    - type: nauc_ndcg_at_100_std
      value: 52.051199999999994
    - type: nauc_ndcg_at_100_diff1
      value: 12.7829
    - type: nauc_ndcg_at_1000_max
      value: 54.610099999999996
    - type: nauc_ndcg_at_1000_std
      value: 48.904199999999996
    - type: nauc_ndcg_at_1000_diff1
      value: 6.1958
    - type: nauc_map_at_1_max
      value: 12.2458
    - type: nauc_map_at_1_std
      value: 14.7447
    - type: nauc_map_at_1_diff1
      value: 34.036300000000004
    - type: nauc_map_at_3_max
      value: 23.2805
    - type: nauc_map_at_3_std
      value: 23.075699999999998
    - type: nauc_map_at_3_diff1
      value: 13.449
    - type: nauc_map_at_5_max
      value: 31.796400000000002
    - type: nauc_map_at_5_std
      value: 28.320800000000002
    - type: nauc_map_at_5_diff1
      value: 11.802
    - type: nauc_map_at_10_max
      value: 38.4408
    - type: nauc_map_at_10_std
      value: 35.1462
    - type: nauc_map_at_10_diff1
      value: 11.4836
    - type: nauc_map_at_20_max
      value: 44.432100000000005
    - type: nauc_map_at_20_std
      value: 41.216
    - type: nauc_map_at_20_diff1
      value: 11.8712
    - type: nauc_map_at_100_max
      value: 52.6408
    - type: nauc_map_at_100_std
      value: 50.6432
    - type: nauc_map_at_100_diff1
      value: 10.203800000000001
    - type: nauc_map_at_1000_max
      value: 55.83669999999999
    - type: nauc_map_at_1000_std
      value: 50.1
    - type: nauc_map_at_1000_diff1
      value: 7.138999999999999
    - type: nauc_recall_at_1_max
      value: 12.2458
    - type: nauc_recall_at_1_std
      value: 14.7447
    - type: nauc_recall_at_1_diff1
      value: 34.036300000000004
    - type: nauc_recall_at_3_max
      value: 21.1536
    - type: nauc_recall_at_3_std
      value: 20.552200000000003
    - type: nauc_recall_at_3_diff1
      value: 9.8918
    - type: nauc_recall_at_5_max
      value: 27.249000000000002
    - type: nauc_recall_at_5_std
      value: 24.4019
    - type: nauc_recall_at_5_diff1
      value: 9.941899999999999
    - type: nauc_recall_at_10_max
      value: 33.7524
    - type: nauc_recall_at_10_std
      value: 32.2637
    - type: nauc_recall_at_10_diff1
      value: 9.5374
    - type: nauc_recall_at_20_max
      value: 39.72
    - type: nauc_recall_at_20_std
      value: 40.192699999999995
    - type: nauc_recall_at_20_diff1
      value: 10.4948
    - type: nauc_recall_at_100_max
      value: 46.9723
    - type: nauc_recall_at_100_std
      value: 57.1977
    - type: nauc_recall_at_100_diff1
      value: 13.5774
    - type: nauc_recall_at_1000_max
      value: 49.7254
    - type: nauc_recall_at_1000_std
      value: 77.2495
    - type: nauc_recall_at_1000_diff1
      value: -2.3819
    - type: nauc_precision_at_1_max
      value: 52.346199999999996
    - type: nauc_precision_at_1_std
      value: 33.2015
    - type: nauc_precision_at_1_diff1
      value: 23.8076
    - type: nauc_precision_at_3_max
      value: 51.325900000000004
    - type: nauc_precision_at_3_std
      value: 30.794
    - type: nauc_precision_at_3_diff1
      value: 3.4286
    - type: nauc_precision_at_5_max
      value: 54.672
    - type: nauc_precision_at_5_std
      value: 31.145
    - type: nauc_precision_at_5_diff1
      value: 3.1246
    - type: nauc_precision_at_10_max
      value: 54.738299999999995
    - type: nauc_precision_at_10_std
      value: 32.656800000000004
    - type: nauc_precision_at_10_diff1
      value: -0.0848
    - type: nauc_precision_at_20_max
      value: 51.759699999999995
    - type: nauc_precision_at_20_std
      value: 29.5588
    - type: nauc_precision_at_20_diff1
      value: -2.3040000000000003
    - type: nauc_precision_at_100_max
      value: 36.4731
    - type: nauc_precision_at_100_std
      value: 17.8626
    - type: nauc_precision_at_100_diff1
      value: -9.2071
    - type: nauc_precision_at_1000_max
      value: 20.854400000000002
    - type: nauc_precision_at_1000_std
      value: -12.570200000000002
    - type: nauc_precision_at_1000_diff1
      value: -14.3759
    - type: nauc_mrr_at_1_max
      value: 52.346199999999996
    - type: nauc_mrr_at_1_std
      value: 33.2015
    - type: nauc_mrr_at_1_diff1
      value: 23.8076
    - type: nauc_mrr_at_3_max
      value: 52.0386
    - type: nauc_mrr_at_3_std
      value: 35.7242
    - type: nauc_mrr_at_3_diff1
      value: 18.7328
    - type: nauc_mrr_at_5_max
      value: 50.8626
    - type: nauc_mrr_at_5_std
      value: 35.3036
    - type: nauc_mrr_at_5_diff1
      value: 18.8403
    - type: nauc_mrr_at_10_max
      value: 51.0177
    - type: nauc_mrr_at_10_std
      value: 35.2915
    - type: nauc_mrr_at_10_diff1
      value: 18.1387
    - type: nauc_mrr_at_20_max
      value: 51.4232
    - type: nauc_mrr_at_20_std
      value: 35.1578
    - type: nauc_mrr_at_20_diff1
      value: 17.8418
    - type: nauc_mrr_at_100_max
      value: 51.5004
    - type: nauc_mrr_at_100_std
      value: 35.3373
    - type: nauc_mrr_at_100_diff1
      value: 17.9748
    - type: nauc_mrr_at_1000_max
      value: 51.4899
    - type: nauc_mrr_at_1000_std
      value: 35.3187
    - type: nauc_mrr_at_1000_diff1
      value: 18.0391
    - type: main_score
      value: 31.863999999999997
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: genetics
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 60.25
    - type: ndcg_at_3
      value: 58.475
    - type: ndcg_at_5
      value: 57.792
    - type: ndcg_at_10
      value: 57.830000000000005
    - type: ndcg_at_20
      value: 58.226
    - type: ndcg_at_100
      value: 62.902
    - type: ndcg_at_1000
      value: 71.911
    - type: map_at_1
      value: 9.786999999999999
    - type: map_at_3
      value: 18.359
    - type: map_at_5
      value: 22.716
    - type: map_at_10
      value: 28.389999999999997
    - type: map_at_20
      value: 32.991
    - type: map_at_100
      value: 42.074
    - type: map_at_1000
      value: 48.083999999999996
    - type: recall_at_1
      value: 9.786999999999999
    - type: recall_at_3
      value: 20.128
    - type: recall_at_5
      value: 26.615
    - type: recall_at_10
      value: 35.961999999999996
    - type: recall_at_20
      value: 44.772
    - type: recall_at_100
      value: 68.51899999999999
    - type: recall_at_1000
      value: 93.538
    - type: precision_at_1
      value: 74.0
    - type: precision_at_3
      value: 65.167
    - type: precision_at_5
      value: 60.099999999999994
    - type: precision_at_10
      value: 50.8
    - type: precision_at_20
      value: 41.25
    - type: precision_at_100
      value: 22.07
    - type: precision_at_1000
      value: 5.579
    - type: mrr_at_1
      value: 74.0
    - type: mrr_at_3
      value: 82.25
    - type: mrr_at_5
      value: 83.175
    - type: mrr_at_10
      value: 83.3589
    - type: mrr_at_20
      value: 83.52340000000001
    - type: mrr_at_100
      value: 83.52340000000001
    - type: mrr_at_1000
      value: 83.52340000000001
    - type: nauc_ndcg_at_1_max
      value: 23.397299999999998
    - type: nauc_ndcg_at_1_std
      value: 24.4939
    - type: nauc_ndcg_at_1_diff1
      value: 28.0647
    - type: nauc_ndcg_at_3_max
      value: 32.109500000000004
    - type: nauc_ndcg_at_3_std
      value: 24.8319
    - type: nauc_ndcg_at_3_diff1
      value: 21.9448
    - type: nauc_ndcg_at_5_max
      value: 34.0051
    - type: nauc_ndcg_at_5_std
      value: 27.4148
    - type: nauc_ndcg_at_5_diff1
      value: 18.6325
    - type: nauc_ndcg_at_10_max
      value: 31.6224
    - type: nauc_ndcg_at_10_std
      value: 31.2952
    - type: nauc_ndcg_at_10_diff1
      value: 17.426099999999998
    - type: nauc_ndcg_at_20_max
      value: 33.1613
    - type: nauc_ndcg_at_20_std
      value: 33.711400000000005
    - type: nauc_ndcg_at_20_diff1
      value: 22.2519
    - type: nauc_ndcg_at_100_max
      value: 32.222699999999996
    - type: nauc_ndcg_at_100_std
      value: 40.532000000000004
    - type: nauc_ndcg_at_100_diff1
      value: 29.092299999999998
    - type: nauc_ndcg_at_1000_max
      value: 34.9461
    - type: nauc_ndcg_at_1000_std
      value: 41.908899999999996
    - type: nauc_ndcg_at_1000_diff1
      value: 26.2818
    - type: nauc_map_at_1_max
      value: 1.7859
    - type: nauc_map_at_1_std
      value: 9.931099999999999
    - type: nauc_map_at_1_diff1
      value: 29.546499999999998
    - type: nauc_map_at_3_max
      value: 16.9801
    - type: nauc_map_at_3_std
      value: 17.0517
    - type: nauc_map_at_3_diff1
      value: 30.8838
    - type: nauc_map_at_5_max
      value: 21.2562
    - type: nauc_map_at_5_std
      value: 24.3807
    - type: nauc_map_at_5_diff1
      value: 30.370200000000004
    - type: nauc_map_at_10_max
      value: 24.388399999999997
    - type: nauc_map_at_10_std
      value: 30.231599999999997
    - type: nauc_map_at_10_diff1
      value: 26.3432
    - type: nauc_map_at_20_max
      value: 25.8334
    - type: nauc_map_at_20_std
      value: 33.4471
    - type: nauc_map_at_20_diff1
      value: 26.217200000000002
    - type: nauc_map_at_100_max
      value: 26.246799999999997
    - type: nauc_map_at_100_std
      value: 40.078399999999995
    - type: nauc_map_at_100_diff1
      value: 25.5407
    - type: nauc_map_at_1000_max
      value: 29.2257
    - type: nauc_map_at_1000_std
      value: 39.4688
    - type: nauc_map_at_1000_diff1
      value: 19.9766
    - type: nauc_recall_at_1_max
      value: 1.7859
    - type: nauc_recall_at_1_std
      value: 9.931099999999999
    - type: nauc_recall_at_1_diff1
      value: 29.546499999999998
    - type: nauc_recall_at_3_max
      value: 16.4105
    - type: nauc_recall_at_3_std
      value: 16.220200000000002
    - type: nauc_recall_at_3_diff1
      value: 26.8932
    - type: nauc_recall_at_5_max
      value: 18.6335
    - type: nauc_recall_at_5_std
      value: 26.1909
    - type: nauc_recall_at_5_diff1
      value: 25.570999999999998
    - type: nauc_recall_at_10_max
      value: 19.8384
    - type: nauc_recall_at_10_std
      value: 30.0377
    - type: nauc_recall_at_10_diff1
      value: 20.7945
    - type: nauc_recall_at_20_max
      value: 20.6784
    - type: nauc_recall_at_20_std
      value: 33.7626
    - type: nauc_recall_at_20_diff1
      value: 22.6844
    - type: nauc_recall_at_100_max
      value: 16.7405
    - type: nauc_recall_at_100_std
      value: 47.7157
    - type: nauc_recall_at_100_diff1
      value: 25.9606
    - type: nauc_recall_at_1000_max
      value: 35.3439
    - type: nauc_recall_at_1000_std
      value: 78.67
    - type: nauc_recall_at_1000_diff1
      value: 27.145799999999998
    - type: nauc_precision_at_1_max
      value: 27.4857
    - type: nauc_precision_at_1_std
      value: 32.4166
    - type: nauc_precision_at_1_diff1
      value: 35.327
    - type: nauc_precision_at_3_max
      value: 30.1426
    - type: nauc_precision_at_3_std
      value: 22.7352
    - type: nauc_precision_at_3_diff1
      value: 6.823899999999999
    - type: nauc_precision_at_5_max
      value: 30.236200000000004
    - type: nauc_precision_at_5_std
      value: 20.993100000000002
    - type: nauc_precision_at_5_diff1
      value: -3.7901
    - type: nauc_precision_at_10_max
      value: 17.6751
    - type: nauc_precision_at_10_std
      value: 13.324300000000001
    - type: nauc_precision_at_10_diff1
      value: -18.4944
    - type: nauc_precision_at_20_max
      value: 7.290099999999999
    - type: nauc_precision_at_20_std
      value: 3.0109
    - type: nauc_precision_at_20_diff1
      value: -19.5427
    - type: nauc_precision_at_100_max
      value: -1.3945
    - type: nauc_precision_at_100_std
      value: -11.3057
    - type: nauc_precision_at_100_diff1
      value: -23.4941
    - type: nauc_precision_at_1000_max
      value: -0.0958
    - type: nauc_precision_at_1000_std
      value: -25.0461
    - type: nauc_precision_at_1000_diff1
      value: -29.7531
    - type: nauc_mrr_at_1_max
      value: 27.4857
    - type: nauc_mrr_at_1_std
      value: 32.4166
    - type: nauc_mrr_at_1_diff1
      value: 35.327
    - type: nauc_mrr_at_3_max
      value: 33.575700000000005
    - type: nauc_mrr_at_3_std
      value: 33.7427
    - type: nauc_mrr_at_3_diff1
      value: 39.4644
    - type: nauc_mrr_at_5_max
      value: 33.331
    - type: nauc_mrr_at_5_std
      value: 33.8148
    - type: nauc_mrr_at_5_diff1
      value: 38.4811
    - type: nauc_mrr_at_10_max
      value: 33.583800000000004
    - type: nauc_mrr_at_10_std
      value: 33.9609
    - type: nauc_mrr_at_10_diff1
      value: 38.217
    - type: nauc_mrr_at_20_max
      value: 33.021
    - type: nauc_mrr_at_20_std
      value: 34.0802
    - type: nauc_mrr_at_20_diff1
      value: 38.281
    - type: nauc_mrr_at_100_max
      value: 33.021
    - type: nauc_mrr_at_100_std
      value: 34.0802
    - type: nauc_mrr_at_100_diff1
      value: 38.281
    - type: nauc_mrr_at_1000_max
      value: 33.021
    - type: nauc_mrr_at_1000_std
      value: 34.0802
    - type: nauc_mrr_at_1000_diff1
      value: 38.281
    - type: main_score
      value: 57.830000000000005
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: genetics
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 20.5
    - type: ndcg_at_3
      value: 20.846
    - type: ndcg_at_5
      value: 21.898999999999997
    - type: ndcg_at_10
      value: 23.427999999999997
    - type: ndcg_at_20
      value: 25.402
    - type: ndcg_at_100
      value: 29.868
    - type: ndcg_at_1000
      value: 39.879999999999995
    - type: map_at_1
      value: 4.573
    - type: map_at_3
      value: 7.89
    - type: map_at_5
      value: 9.804
    - type: map_at_10
      value: 12.147
    - type: map_at_20
      value: 13.908999999999999
    - type: map_at_100
      value: 16.784
    - type: map_at_1000
      value: 19.277
    - type: recall_at_1
      value: 4.573
    - type: recall_at_3
      value: 9.396
    - type: recall_at_5
      value: 13.635
    - type: recall_at_10
      value: 20.383000000000003
    - type: recall_at_20
      value: 26.56
    - type: recall_at_100
      value: 42.141
    - type: recall_at_1000
      value: 69.513
    - type: precision_at_1
      value: 26.0
    - type: precision_at_3
      value: 24.333
    - type: precision_at_5
      value: 23.0
    - type: precision_at_10
      value: 18.9
    - type: precision_at_20
      value: 15.975
    - type: precision_at_100
      value: 8.790000000000001
    - type: precision_at_1000
      value: 2.919
    - type: mrr_at_1
      value: 26.0
    - type: mrr_at_3
      value: 34.1667
    - type: mrr_at_5
      value: 36.3917
    - type: mrr_at_10
      value: 37.5268
    - type: mrr_at_20
      value: 38.1037
    - type: mrr_at_100
      value: 38.2909
    - type: mrr_at_1000
      value: 38.3666
    - type: nauc_ndcg_at_1_max
      value: 30.9651
    - type: nauc_ndcg_at_1_std
      value: 26.2865
    - type: nauc_ndcg_at_1_diff1
      value: 5.3133
    - type: nauc_ndcg_at_3_max
      value: 34.8346
    - type: nauc_ndcg_at_3_std
      value: 31.572699999999998
    - type: nauc_ndcg_at_3_diff1
      value: 4.2997
    - type: nauc_ndcg_at_5_max
      value: 38.6848
    - type: nauc_ndcg_at_5_std
      value: 34.4997
    - type: nauc_ndcg_at_5_diff1
      value: 8.145
    - type: nauc_ndcg_at_10_max
      value: 39.4422
    - type: nauc_ndcg_at_10_std
      value: 42.065000000000005
    - type: nauc_ndcg_at_10_diff1
      value: 11.3805
    - type: nauc_ndcg_at_20_max
      value: 40.2946
    - type: nauc_ndcg_at_20_std
      value: 45.984199999999994
    - type: nauc_ndcg_at_20_diff1
      value: 13.3306
    - type: nauc_ndcg_at_100_max
      value: 40.8998
    - type: nauc_ndcg_at_100_std
      value: 52.7489
    - type: nauc_ndcg_at_100_diff1
      value: 11.8633
    - type: nauc_ndcg_at_1000_max
      value: 46.3694
    - type: nauc_ndcg_at_1000_std
      value: 56.346799999999995
    - type: nauc_ndcg_at_1000_diff1
      value: 3.6907
    - type: nauc_map_at_1_max
      value: 38.6937
    - type: nauc_map_at_1_std
      value: 30.1883
    - type: nauc_map_at_1_diff1
      value: 35.4755
    - type: nauc_map_at_3_max
      value: 37.1634
    - type: nauc_map_at_3_std
      value: 39.1229
    - type: nauc_map_at_3_diff1
      value: 24.429000000000002
    - type: nauc_map_at_5_max
      value: 35.7377
    - type: nauc_map_at_5_std
      value: 41.4592
    - type: nauc_map_at_5_diff1
      value: 24.508399999999998
    - type: nauc_map_at_10_max
      value: 35.7061
    - type: nauc_map_at_10_std
      value: 44.7305
    - type: nauc_map_at_10_diff1
      value: 21.0847
    - type: nauc_map_at_20_max
      value: 36.3037
    - type: nauc_map_at_20_std
      value: 47.369299999999996
    - type: nauc_map_at_20_diff1
      value: 19.8797
    - type: nauc_map_at_100_max
      value: 38.423
    - type: nauc_map_at_100_std
      value: 50.9625
    - type: nauc_map_at_100_diff1
      value: 17.043400000000002
    - type: nauc_map_at_1000_max
      value: 41.4598
    - type: nauc_map_at_1000_std
      value: 52.303
    - type: nauc_map_at_1000_diff1
      value: 13.9572
    - type: nauc_recall_at_1_max
      value: 38.6937
    - type: nauc_recall_at_1_std
      value: 30.1883
    - type: nauc_recall_at_1_diff1
      value: 35.4755
    - type: nauc_recall_at_3_max
      value: 32.7829
    - type: nauc_recall_at_3_std
      value: 37.202200000000005
    - type: nauc_recall_at_3_diff1
      value: 22.7994
    - type: nauc_recall_at_5_max
      value: 28.983199999999997
    - type: nauc_recall_at_5_std
      value: 39.1822
    - type: nauc_recall_at_5_diff1
      value: 25.370900000000002
    - type: nauc_recall_at_10_max
      value: 25.569599999999998
    - type: nauc_recall_at_10_std
      value: 44.183
    - type: nauc_recall_at_10_diff1
      value: 18.7259
    - type: nauc_recall_at_20_max
      value: 24.8139
    - type: nauc_recall_at_20_std
      value: 48.7119
    - type: nauc_recall_at_20_diff1
      value: 19.9204
    - type: nauc_recall_at_100_max
      value: 28.1375
    - type: nauc_recall_at_100_std
      value: 58.6694
    - type: nauc_recall_at_100_diff1
      value: 14.3897
    - type: nauc_recall_at_1000_max
      value: 39.3016
    - type: nauc_recall_at_1000_std
      value: 80.6024
    - type: nauc_recall_at_1000_diff1
      value: -1.5233
    - type: nauc_precision_at_1_max
      value: 33.3634
    - type: nauc_precision_at_1_std
      value: 29.862499999999997
    - type: nauc_precision_at_1_diff1
      value: 4.5995
    - type: nauc_precision_at_3_max
      value: 34.5883
    - type: nauc_precision_at_3_std
      value: 33.4493
    - type: nauc_precision_at_3_diff1
      value: -6.5379000000000005
    - type: nauc_precision_at_5_max
      value: 37.2304
    - type: nauc_precision_at_5_std
      value: 34.462399999999995
    - type: nauc_precision_at_5_diff1
      value: -5.7752
    - type: nauc_precision_at_10_max
      value: 37.0948
    - type: nauc_precision_at_10_std
      value: 35.8302
    - type: nauc_precision_at_10_diff1
      value: -4.7827
    - type: nauc_precision_at_20_max
      value: 37.642900000000004
    - type: nauc_precision_at_20_std
      value: 30.4822
    - type: nauc_precision_at_20_diff1
      value: -7.4448
    - type: nauc_precision_at_100_max
      value: 32.3888
    - type: nauc_precision_at_100_std
      value: 16.284100000000002
    - type: nauc_precision_at_100_diff1
      value: -13.534299999999998
    - type: nauc_precision_at_1000_max
      value: 29.5665
    - type: nauc_precision_at_1000_std
      value: -4.736
    - type: nauc_precision_at_1000_diff1
      value: -14.4178
    - type: nauc_mrr_at_1_max
      value: 33.3634
    - type: nauc_mrr_at_1_std
      value: 29.862499999999997
    - type: nauc_mrr_at_1_diff1
      value: 4.5995
    - type: nauc_mrr_at_3_max
      value: 35.8166
    - type: nauc_mrr_at_3_std
      value: 30.7058
    - type: nauc_mrr_at_3_diff1
      value: 2.931
    - type: nauc_mrr_at_5_max
      value: 37.0172
    - type: nauc_mrr_at_5_std
      value: 30.959999999999997
    - type: nauc_mrr_at_5_diff1
      value: 3.8329000000000004
    - type: nauc_mrr_at_10_max
      value: 38.2552
    - type: nauc_mrr_at_10_std
      value: 32.524300000000004
    - type: nauc_mrr_at_10_diff1
      value: 3.6144999999999996
    - type: nauc_mrr_at_20_max
      value: 38.2202
    - type: nauc_mrr_at_20_std
      value: 32.5916
    - type: nauc_mrr_at_20_diff1
      value: 3.0888999999999998
    - type: nauc_mrr_at_100_max
      value: 38.2367
    - type: nauc_mrr_at_100_std
      value: 32.5874
    - type: nauc_mrr_at_100_diff1
      value: 3.0557999999999996
    - type: nauc_mrr_at_1000_max
      value: 38.2161
    - type: nauc_mrr_at_1000_std
      value: 32.5373
    - type: nauc_mrr_at_1000_diff1
      value: 3.0961
    - type: main_score
      value: 23.427999999999997
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: genetics
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 34.75
    - type: ndcg_at_3
      value: 33.451
    - type: ndcg_at_5
      value: 33.062000000000005
    - type: ndcg_at_10
      value: 34.393
    - type: ndcg_at_20
      value: 34.725
    - type: ndcg_at_100
      value: 39.509
    - type: ndcg_at_1000
      value: 49.708999999999996
    - type: map_at_1
      value: 6.478000000000001
    - type: map_at_3
      value: 11.562
    - type: map_at_5
      value: 13.883999999999999
    - type: map_at_10
      value: 16.830000000000002
    - type: map_at_20
      value: 18.719
    - type: map_at_100
      value: 22.726
    - type: map_at_1000
      value: 26.284999999999997
    - type: recall_at_1
      value: 6.478000000000001
    - type: recall_at_3
      value: 13.05
    - type: recall_at_5
      value: 17.217
    - type: recall_at_10
      value: 24.532999999999998
    - type: recall_at_20
      value: 29.921999999999997
    - type: recall_at_100
      value: 48.243
    - type: recall_at_1000
      value: 77.143
    - type: precision_at_1
      value: 44.0
    - type: precision_at_3
      value: 37.5
    - type: precision_at_5
      value: 32.6
    - type: precision_at_10
      value: 27.800000000000004
    - type: precision_at_20
      value: 22.15
    - type: precision_at_100
      value: 13.020000000000001
    - type: precision_at_1000
      value: 4.009
    - type: mrr_at_1
      value: 44.0
    - type: mrr_at_3
      value: 52.416700000000006
    - type: mrr_at_5
      value: 53.8917
    - type: mrr_at_10
      value: 55.232099999999996
    - type: mrr_at_20
      value: 55.5794
    - type: mrr_at_100
      value: 55.7582
    - type: mrr_at_1000
      value: 55.7889
    - type: nauc_ndcg_at_1_max
      value: 36.268
    - type: nauc_ndcg_at_1_std
      value: 27.228099999999998
    - type: nauc_ndcg_at_1_diff1
      value: 24.5667
    - type: nauc_ndcg_at_3_max
      value: 33.9523
    - type: nauc_ndcg_at_3_std
      value: 30.5914
    - type: nauc_ndcg_at_3_diff1
      value: 22.4058
    - type: nauc_ndcg_at_5_max
      value: 36.106500000000004
    - type: nauc_ndcg_at_5_std
      value: 36.521300000000004
    - type: nauc_ndcg_at_5_diff1
      value: 23.0627
    - type: nauc_ndcg_at_10_max
      value: 39.3899
    - type: nauc_ndcg_at_10_std
      value: 45.009100000000004
    - type: nauc_ndcg_at_10_diff1
      value: 30.0523
    - type: nauc_ndcg_at_20_max
      value: 39.0796
    - type: nauc_ndcg_at_20_std
      value: 48.718
    - type: nauc_ndcg_at_20_diff1
      value: 31.4393
    - type: nauc_ndcg_at_100_max
      value: 41.5535
    - type: nauc_ndcg_at_100_std
      value: 59.6568
    - type: nauc_ndcg_at_100_diff1
      value: 31.8814
    - type: nauc_ndcg_at_1000_max
      value: 48.430299999999995
    - type: nauc_ndcg_at_1000_std
      value: 60.9746
    - type: nauc_ndcg_at_1000_diff1
      value: 30.778499999999998
    - type: nauc_map_at_1_max
      value: 21.8143
    - type: nauc_map_at_1_std
      value: 39.863
    - type: nauc_map_at_1_diff1
      value: 38.9446
    - type: nauc_map_at_3_max
      value: 23.871000000000002
    - type: nauc_map_at_3_std
      value: 42.3217
    - type: nauc_map_at_3_diff1
      value: 34.5713
    - type: nauc_map_at_5_max
      value: 22.4625
    - type: nauc_map_at_5_std
      value: 44.1124
    - type: nauc_map_at_5_diff1
      value: 31.431199999999997
    - type: nauc_map_at_10_max
      value: 24.9392
    - type: nauc_map_at_10_std
      value: 46.123999999999995
    - type: nauc_map_at_10_diff1
      value: 32.6507
    - type: nauc_map_at_20_max
      value: 26.084400000000002
    - type: nauc_map_at_20_std
      value: 47.902
    - type: nauc_map_at_20_diff1
      value: 32.002900000000004
    - type: nauc_map_at_100_max
      value: 30.115399999999998
    - type: nauc_map_at_100_std
      value: 52.4305
    - type: nauc_map_at_100_diff1
      value: 32.242
    - type: nauc_map_at_1000_max
      value: 35.355199999999996
    - type: nauc_map_at_1000_std
      value: 52.38270000000001
    - type: nauc_map_at_1000_diff1
      value: 29.8275
    - type: nauc_recall_at_1_max
      value: 21.8143
    - type: nauc_recall_at_1_std
      value: 39.863
    - type: nauc_recall_at_1_diff1
      value: 38.9446
    - type: nauc_recall_at_3_max
      value: 22.8151
    - type: nauc_recall_at_3_std
      value: 43.5837
    - type: nauc_recall_at_3_diff1
      value: 31.1201
    - type: nauc_recall_at_5_max
      value: 19.276699999999998
    - type: nauc_recall_at_5_std
      value: 46.0849
    - type: nauc_recall_at_5_diff1
      value: 26.518900000000002
    - type: nauc_recall_at_10_max
      value: 25.4214
    - type: nauc_recall_at_10_std
      value: 52.4193
    - type: nauc_recall_at_10_diff1
      value: 32.5876
    - type: nauc_recall_at_20_max
      value: 26.7202
    - type: nauc_recall_at_20_std
      value: 57.550000000000004
    - type: nauc_recall_at_20_diff1
      value: 30.7318
    - type: nauc_recall_at_100_max
      value: 32.1892
    - type: nauc_recall_at_100_std
      value: 71.679
    - type: nauc_recall_at_100_diff1
      value: 28.494500000000002
    - type: nauc_recall_at_1000_max
      value: 53.0749
    - type: nauc_recall_at_1000_std
      value: 86.1305
    - type: nauc_recall_at_1000_diff1
      value: 26.4679
    - type: nauc_precision_at_1_max
      value: 36.2642
    - type: nauc_precision_at_1_std
      value: 29.8246
    - type: nauc_precision_at_1_diff1
      value: 24.369699999999998
    - type: nauc_precision_at_3_max
      value: 33.6592
    - type: nauc_precision_at_3_std
      value: 24.313000000000002
    - type: nauc_precision_at_3_diff1
      value: 11.6768
    - type: nauc_precision_at_5_max
      value: 35.1515
    - type: nauc_precision_at_5_std
      value: 23.6793
    - type: nauc_precision_at_5_diff1
      value: 10.2316
    - type: nauc_precision_at_10_max
      value: 34.3044
    - type: nauc_precision_at_10_std
      value: 20.2514
    - type: nauc_precision_at_10_diff1
      value: 12.906
    - type: nauc_precision_at_20_max
      value: 31.694699999999997
    - type: nauc_precision_at_20_std
      value: 12.6698
    - type: nauc_precision_at_20_diff1
      value: 7.758800000000001
    - type: nauc_precision_at_100_max
      value: 24.8188
    - type: nauc_precision_at_100_std
      value: -1.4749999999999999
    - type: nauc_precision_at_100_diff1
      value: -4.7867
    - type: nauc_precision_at_1000_max
      value: 18.5152
    - type: nauc_precision_at_1000_std
      value: -21.6261
    - type: nauc_precision_at_1000_diff1
      value: -13.8974
    - type: nauc_mrr_at_1_max
      value: 36.2642
    - type: nauc_mrr_at_1_std
      value: 29.8246
    - type: nauc_mrr_at_1_diff1
      value: 24.369699999999998
    - type: nauc_mrr_at_3_max
      value: 38.6868
    - type: nauc_mrr_at_3_std
      value: 34.336
    - type: nauc_mrr_at_3_diff1
      value: 20.794999999999998
    - type: nauc_mrr_at_5_max
      value: 39.9258
    - type: nauc_mrr_at_5_std
      value: 36.4033
    - type: nauc_mrr_at_5_diff1
      value: 21.2071
    - type: nauc_mrr_at_10_max
      value: 41.1203
    - type: nauc_mrr_at_10_std
      value: 38.0702
    - type: nauc_mrr_at_10_diff1
      value: 22.213
    - type: nauc_mrr_at_20_max
      value: 41.1365
    - type: nauc_mrr_at_20_std
      value: 37.7203
    - type: nauc_mrr_at_20_diff1
      value: 22.2009
    - type: nauc_mrr_at_100_max
      value: 41.0795
    - type: nauc_mrr_at_100_std
      value: 37.574400000000004
    - type: nauc_mrr_at_100_diff1
      value: 22.298000000000002
    - type: nauc_mrr_at_1000_max
      value: 41.0355
    - type: nauc_mrr_at_1000_std
      value: 37.528800000000004
    - type: nauc_mrr_at_1000_diff1
      value: 22.2988
    - type: main_score
      value: 34.393
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: neuroscience_and_neurology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 54.50000000000001
    - type: ndcg_at_3
      value: 51.083999999999996
    - type: ndcg_at_5
      value: 50.954
    - type: ndcg_at_10
      value: 48.884
    - type: ndcg_at_20
      value: 49.376
    - type: ndcg_at_100
      value: 57.452999999999996
    - type: ndcg_at_1000
      value: 67.477
    - type: map_at_1
      value: 5.471
    - type: map_at_3
      value: 10.197000000000001
    - type: map_at_5
      value: 13.496
    - type: map_at_10
      value: 18.206
    - type: map_at_20
      value: 23.843
    - type: map_at_100
      value: 35.476
    - type: map_at_1000
      value: 40.632000000000005
    - type: recall_at_1
      value: 5.471
    - type: recall_at_3
      value: 11.132
    - type: recall_at_5
      value: 16.394000000000002
    - type: recall_at_10
      value: 24.582
    - type: recall_at_20
      value: 36.967
    - type: recall_at_100
      value: 70.206
    - type: recall_at_1000
      value: 96.883
    - type: precision_at_1
      value: 69.5
    - type: precision_at_3
      value: 61.833000000000006
    - type: precision_at_5
      value: 58.3
    - type: precision_at_10
      value: 49.35
    - type: precision_at_20
      value: 41.525
    - type: precision_at_100
      value: 22.0
    - type: precision_at_1000
      value: 3.977
    - type: mrr_at_1
      value: 69.5
    - type: mrr_at_3
      value: 76.9167
    - type: mrr_at_5
      value: 78.1167
    - type: mrr_at_10
      value: 78.5228
    - type: mrr_at_20
      value: 78.6442
    - type: mrr_at_100
      value: 78.7209
    - type: mrr_at_1000
      value: 78.7261
    - type: nauc_ndcg_at_1_max
      value: 39.2904
    - type: nauc_ndcg_at_1_std
      value: 26.1804
    - type: nauc_ndcg_at_1_diff1
      value: 15.9502
    - type: nauc_ndcg_at_3_max
      value: 45.1527
    - type: nauc_ndcg_at_3_std
      value: 29.781000000000002
    - type: nauc_ndcg_at_3_diff1
      value: 12.642999999999999
    - type: nauc_ndcg_at_5_max
      value: 44.426700000000004
    - type: nauc_ndcg_at_5_std
      value: 28.3707
    - type: nauc_ndcg_at_5_diff1
      value: 12.6422
    - type: nauc_ndcg_at_10_max
      value: 46.7505
    - type: nauc_ndcg_at_10_std
      value: 28.2544
    - type: nauc_ndcg_at_10_diff1
      value: 17.0276
    - type: nauc_ndcg_at_20_max
      value: 47.1505
    - type: nauc_ndcg_at_20_std
      value: 24.3433
    - type: nauc_ndcg_at_20_diff1
      value: 16.1224
    - type: nauc_ndcg_at_100_max
      value: 52.66309999999999
    - type: nauc_ndcg_at_100_std
      value: 27.4478
    - type: nauc_ndcg_at_100_diff1
      value: 16.6075
    - type: nauc_ndcg_at_1000_max
      value: 56.2764
    - type: nauc_ndcg_at_1000_std
      value: 40.754000000000005
    - type: nauc_ndcg_at_1000_diff1
      value: 15.6926
    - type: nauc_map_at_1_max
      value: 3.0124999999999997
    - type: nauc_map_at_1_std
      value: -8.2124
    - type: nauc_map_at_1_diff1
      value: 10.987
    - type: nauc_map_at_3_max
      value: 19.0176
    - type: nauc_map_at_3_std
      value: -10.0504
    - type: nauc_map_at_3_diff1
      value: 13.661200000000001
    - type: nauc_map_at_5_max
      value: 20.0561
    - type: nauc_map_at_5_std
      value: -8.7265
    - type: nauc_map_at_5_diff1
      value: 13.9652
    - type: nauc_map_at_10_max
      value: 26.4123
    - type: nauc_map_at_10_std
      value: -3.6491000000000002
    - type: nauc_map_at_10_diff1
      value: 16.9533
    - type: nauc_map_at_20_max
      value: 33.7953
    - type: nauc_map_at_20_std
      value: 1.6022999999999998
    - type: nauc_map_at_20_diff1
      value: 16.6287
    - type: nauc_map_at_100_max
      value: 48.194900000000004
    - type: nauc_map_at_100_std
      value: 20.2344
    - type: nauc_map_at_100_diff1
      value: 16.5675
    - type: nauc_map_at_1000_max
      value: 51.1486
    - type: nauc_map_at_1000_std
      value: 27.487000000000002
    - type: nauc_map_at_1000_diff1
      value: 12.745000000000001
    - type: nauc_recall_at_1_max
      value: 3.0124999999999997
    - type: nauc_recall_at_1_std
      value: -8.2124
    - type: nauc_recall_at_1_diff1
      value: 10.987
    - type: nauc_recall_at_3_max
      value: 14.3101
    - type: nauc_recall_at_3_std
      value: -10.6097
    - type: nauc_recall_at_3_diff1
      value: 9.5236
    - type: nauc_recall_at_5_max
      value: 7.350700000000001
    - type: nauc_recall_at_5_std
      value: -13.6181
    - type: nauc_recall_at_5_diff1
      value: 7.914599999999999
    - type: nauc_recall_at_10_max
      value: 10.7259
    - type: nauc_recall_at_10_std
      value: -11.0079
    - type: nauc_recall_at_10_diff1
      value: 15.920599999999999
    - type: nauc_recall_at_20_max
      value: 13.755899999999999
    - type: nauc_recall_at_20_std
      value: -10.1572
    - type: nauc_recall_at_20_diff1
      value: 14.7261
    - type: nauc_recall_at_100_max
      value: 25.160700000000002
    - type: nauc_recall_at_100_std
      value: 4.3699
    - type: nauc_recall_at_100_diff1
      value: 12.0403
    - type: nauc_recall_at_1000_max
      value: 47.7286
    - type: nauc_recall_at_1000_std
      value: 51.61750000000001
    - type: nauc_recall_at_1000_diff1
      value: 9.2401
    - type: nauc_precision_at_1_max
      value: 47.9257
    - type: nauc_precision_at_1_std
      value: 23.233
    - type: nauc_precision_at_1_diff1
      value: 25.5884
    - type: nauc_precision_at_3_max
      value: 46.5061
    - type: nauc_precision_at_3_std
      value: 27.938800000000004
    - type: nauc_precision_at_3_diff1
      value: 14.1398
    - type: nauc_precision_at_5_max
      value: 40.203
    - type: nauc_precision_at_5_std
      value: 28.471400000000003
    - type: nauc_precision_at_5_diff1
      value: 10.7772
    - type: nauc_precision_at_10_max
      value: 39.1491
    - type: nauc_precision_at_10_std
      value: 31.4945
    - type: nauc_precision_at_10_diff1
      value: 12.3007
    - type: nauc_precision_at_20_max
      value: 34.4246
    - type: nauc_precision_at_20_std
      value: 29.8628
    - type: nauc_precision_at_20_diff1
      value: 2.8098
    - type: nauc_precision_at_100_max
      value: 21.1322
    - type: nauc_precision_at_100_std
      value: 29.6973
    - type: nauc_precision_at_100_diff1
      value: -6.4503
    - type: nauc_precision_at_1000_max
      value: 5.7992
    - type: nauc_precision_at_1000_std
      value: 13.969599999999998
    - type: nauc_precision_at_1000_diff1
      value: -11.9987
    - type: nauc_mrr_at_1_max
      value: 47.9257
    - type: nauc_mrr_at_1_std
      value: 23.233
    - type: nauc_mrr_at_1_diff1
      value: 25.5884
    - type: nauc_mrr_at_3_max
      value: 49.356899999999996
    - type: nauc_mrr_at_3_std
      value: 31.1402
    - type: nauc_mrr_at_3_diff1
      value: 24.6431
    - type: nauc_mrr_at_5_max
      value: 49.8243
    - type: nauc_mrr_at_5_std
      value: 29.1812
    - type: nauc_mrr_at_5_diff1
      value: 26.9064
    - type: nauc_mrr_at_10_max
      value: 49.7113
    - type: nauc_mrr_at_10_std
      value: 29.296
    - type: nauc_mrr_at_10_diff1
      value: 27.2803
    - type: nauc_mrr_at_20_max
      value: 49.613099999999996
    - type: nauc_mrr_at_20_std
      value: 29.137200000000004
    - type: nauc_mrr_at_20_diff1
      value: 27.3154
    - type: nauc_mrr_at_100_max
      value: 49.613099999999996
    - type: nauc_mrr_at_100_std
      value: 29.0941
    - type: nauc_mrr_at_100_diff1
      value: 27.1667
    - type: nauc_mrr_at_1000_max
      value: 49.606899999999996
    - type: nauc_mrr_at_1000_std
      value: 29.082900000000002
    - type: nauc_mrr_at_1000_diff1
      value: 27.151999999999997
    - type: main_score
      value: 48.884
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: neuroscience_and_neurology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 18.5
    - type: ndcg_at_3
      value: 15.914
    - type: ndcg_at_5
      value: 15.717
    - type: ndcg_at_10
      value: 15.190000000000001
    - type: ndcg_at_20
      value: 15.901000000000002
    - type: ndcg_at_100
      value: 21.93
    - type: ndcg_at_1000
      value: 35.305
    - type: map_at_1
      value: 1.764
    - type: map_at_3
      value: 3.2620000000000005
    - type: map_at_5
      value: 4.166
    - type: map_at_10
      value: 5.16
    - type: map_at_20
      value: 6.539000000000001
    - type: map_at_100
      value: 10.008000000000001
    - type: map_at_1000
      value: 12.806999999999999
    - type: recall_at_1
      value: 1.764
    - type: recall_at_3
      value: 3.585
    - type: recall_at_5
      value: 5.311
    - type: recall_at_10
      value: 7.692
    - type: recall_at_20
      value: 12.034
    - type: recall_at_100
      value: 30.930999999999997
    - type: recall_at_1000
      value: 69.574
    - type: precision_at_1
      value: 26.5
    - type: precision_at_3
      value: 20.333000000000002
    - type: precision_at_5
      value: 19.3
    - type: precision_at_10
      value: 16.35
    - type: precision_at_20
      value: 14.000000000000002
    - type: precision_at_100
      value: 8.985
    - type: precision_at_1000
      value: 2.617
    - type: mrr_at_1
      value: 26.5
    - type: mrr_at_3
      value: 30.8333
    - type: mrr_at_5
      value: 32.2833
    - type: mrr_at_10
      value: 33.2004
    - type: mrr_at_20
      value: 34.037800000000004
    - type: mrr_at_100
      value: 34.5533
    - type: mrr_at_1000
      value: 34.6277
    - type: nauc_ndcg_at_1_max
      value: 20.1184
    - type: nauc_ndcg_at_1_std
      value: 38.5704
    - type: nauc_ndcg_at_1_diff1
      value: 5.0864
    - type: nauc_ndcg_at_3_max
      value: 36.4827
    - type: nauc_ndcg_at_3_std
      value: 48.3948
    - type: nauc_ndcg_at_3_diff1
      value: 5.2124999999999995
    - type: nauc_ndcg_at_5_max
      value: 37.5982
    - type: nauc_ndcg_at_5_std
      value: 50.1478
    - type: nauc_ndcg_at_5_diff1
      value: 4.7903
    - type: nauc_ndcg_at_10_max
      value: 38.5586
    - type: nauc_ndcg_at_10_std
      value: 49.945299999999996
    - type: nauc_ndcg_at_10_diff1
      value: 3.0567
    - type: nauc_ndcg_at_20_max
      value: 40.3095
    - type: nauc_ndcg_at_20_std
      value: 50.8079
    - type: nauc_ndcg_at_20_diff1
      value: 2.9066
    - type: nauc_ndcg_at_100_max
      value: 44.5802
    - type: nauc_ndcg_at_100_std
      value: 56.85059999999999
    - type: nauc_ndcg_at_100_diff1
      value: 0.6169
    - type: nauc_ndcg_at_1000_max
      value: 50.469500000000004
    - type: nauc_ndcg_at_1000_std
      value: 64.4092
    - type: nauc_ndcg_at_1000_diff1
      value: 4.1708
    - type: nauc_map_at_1_max
      value: 30.6966
    - type: nauc_map_at_1_std
      value: 24.0367
    - type: nauc_map_at_1_diff1
      value: 5.1290000000000004
    - type: nauc_map_at_3_max
      value: 49.699
    - type: nauc_map_at_3_std
      value: 39.0809
    - type: nauc_map_at_3_diff1
      value: 17.871000000000002
    - type: nauc_map_at_5_max
      value: 48.4367
    - type: nauc_map_at_5_std
      value: 38.408
    - type: nauc_map_at_5_diff1
      value: 15.0561
    - type: nauc_map_at_10_max
      value: 47.6762
    - type: nauc_map_at_10_std
      value: 41.3061
    - type: nauc_map_at_10_diff1
      value: 11.0321
    - type: nauc_map_at_20_max
      value: 47.9184
    - type: nauc_map_at_20_std
      value: 45.1168
    - type: nauc_map_at_20_diff1
      value: 7.9868
    - type: nauc_map_at_100_max
      value: 46.889199999999995
    - type: nauc_map_at_100_std
      value: 53.928200000000004
    - type: nauc_map_at_100_diff1
      value: 3.3692
    - type: nauc_map_at_1000_max
      value: 49.5583
    - type: nauc_map_at_1000_std
      value: 58.64470000000001
    - type: nauc_map_at_1000_diff1
      value: 3.9248
    - type: nauc_recall_at_1_max
      value: 30.6966
    - type: nauc_recall_at_1_std
      value: 24.0367
    - type: nauc_recall_at_1_diff1
      value: 5.1290000000000004
    - type: nauc_recall_at_3_max
      value: 50.294000000000004
    - type: nauc_recall_at_3_std
      value: 38.821600000000004
    - type: nauc_recall_at_3_diff1
      value: 14.833499999999999
    - type: nauc_recall_at_5_max
      value: 43.410199999999996
    - type: nauc_recall_at_5_std
      value: 33.9841
    - type: nauc_recall_at_5_diff1
      value: 8.3385
    - type: nauc_recall_at_10_max
      value: 37.335499999999996
    - type: nauc_recall_at_10_std
      value: 31.113200000000003
    - type: nauc_recall_at_10_diff1
      value: 3.4785999999999997
    - type: nauc_recall_at_20_max
      value: 35.8026
    - type: nauc_recall_at_20_std
      value: 32.4445
    - type: nauc_recall_at_20_diff1
      value: -0.8593
    - type: nauc_recall_at_100_max
      value: 36.2594
    - type: nauc_recall_at_100_std
      value: 47.6576
    - type: nauc_recall_at_100_diff1
      value: -1.8901999999999999
    - type: nauc_recall_at_1000_max
      value: 50.1605
    - type: nauc_recall_at_1000_std
      value: 68.881
    - type: nauc_recall_at_1000_diff1
      value: 1.444
    - type: nauc_precision_at_1_max
      value: 25.905099999999997
    - type: nauc_precision_at_1_std
      value: 43.729
    - type: nauc_precision_at_1_diff1
      value: 5.370699999999999
    - type: nauc_precision_at_3_max
      value: 41.4022
    - type: nauc_precision_at_3_std
      value: 51.6336
    - type: nauc_precision_at_3_diff1
      value: 5.1273
    - type: nauc_precision_at_5_max
      value: 39.137899999999995
    - type: nauc_precision_at_5_std
      value: 52.505599999999994
    - type: nauc_precision_at_5_diff1
      value: 2.8716
    - type: nauc_precision_at_10_max
      value: 37.201699999999995
    - type: nauc_precision_at_10_std
      value: 51.8003
    - type: nauc_precision_at_10_diff1
      value: 1.3533
    - type: nauc_precision_at_20_max
      value: 37.0372
    - type: nauc_precision_at_20_std
      value: 55.199
    - type: nauc_precision_at_20_diff1
      value: -1.5115
    - type: nauc_precision_at_100_max
      value: 33.7239
    - type: nauc_precision_at_100_std
      value: 53.2366
    - type: nauc_precision_at_100_diff1
      value: -0.1888
    - type: nauc_precision_at_1000_max
      value: 35.5969
    - type: nauc_precision_at_1000_std
      value: 34.8242
    - type: nauc_precision_at_1000_diff1
      value: 12.4941
    - type: nauc_mrr_at_1_max
      value: 25.905099999999997
    - type: nauc_mrr_at_1_std
      value: 43.729
    - type: nauc_mrr_at_1_diff1
      value: 5.370699999999999
    - type: nauc_mrr_at_3_max
      value: 32.7879
    - type: nauc_mrr_at_3_std
      value: 47.7489
    - type: nauc_mrr_at_3_diff1
      value: 3.7714
    - type: nauc_mrr_at_5_max
      value: 32.2069
    - type: nauc_mrr_at_5_std
      value: 47.4263
    - type: nauc_mrr_at_5_diff1
      value: 2.5936
    - type: nauc_mrr_at_10_max
      value: 31.827499999999997
    - type: nauc_mrr_at_10_std
      value: 46.3717
    - type: nauc_mrr_at_10_diff1
      value: 3.6629
    - type: nauc_mrr_at_20_max
      value: 32.4509
    - type: nauc_mrr_at_20_std
      value: 47.153
    - type: nauc_mrr_at_20_diff1
      value: 3.5404999999999998
    - type: nauc_mrr_at_100_max
      value: 32.5451
    - type: nauc_mrr_at_100_std
      value: 47.1451
    - type: nauc_mrr_at_100_diff1
      value: 3.6397
    - type: nauc_mrr_at_1000_max
      value: 32.5079
    - type: nauc_mrr_at_1000_std
      value: 47.160999999999994
    - type: nauc_mrr_at_1000_diff1
      value: 3.6235000000000004
    - type: main_score
      value: 15.190000000000001
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: neuroscience_and_neurology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 21.5
    - type: ndcg_at_3
      value: 21.453
    - type: ndcg_at_5
      value: 22.07
    - type: ndcg_at_10
      value: 22.159000000000002
    - type: ndcg_at_20
      value: 23.23
    - type: ndcg_at_100
      value: 30.018
    - type: ndcg_at_1000
      value: 42.709
    - type: map_at_1
      value: 1.891
    - type: map_at_3
      value: 4.484
    - type: map_at_5
      value: 5.753
    - type: map_at_10
      value: 7.648000000000001
    - type: map_at_20
      value: 9.916
    - type: map_at_100
      value: 15.229999999999999
    - type: map_at_1000
      value: 18.569
    - type: recall_at_1
      value: 1.891
    - type: recall_at_3
      value: 5.295
    - type: recall_at_5
      value: 8.021
    - type: recall_at_10
      value: 12.124
    - type: recall_at_20
      value: 18.348
    - type: recall_at_100
      value: 40.699999999999996
    - type: recall_at_1000
      value: 76.359
    - type: precision_at_1
      value: 29.5
    - type: precision_at_3
      value: 28.166999999999998
    - type: precision_at_5
      value: 27.500000000000004
    - type: precision_at_10
      value: 24.15
    - type: precision_at_20
      value: 20.549999999999997
    - type: precision_at_100
      value: 12.195
    - type: precision_at_1000
      value: 3.044
    - type: mrr_at_1
      value: 29.5
    - type: mrr_at_3
      value: 37.166700000000006
    - type: mrr_at_5
      value: 39.6667
    - type: mrr_at_10
      value: 41.2244
    - type: mrr_at_20
      value: 41.8155
    - type: mrr_at_100
      value: 42.0516
    - type: mrr_at_1000
      value: 42.0902
    - type: nauc_ndcg_at_1_max
      value: 43.5626
    - type: nauc_ndcg_at_1_std
      value: 33.057700000000004
    - type: nauc_ndcg_at_1_diff1
      value: 20.1071
    - type: nauc_ndcg_at_3_max
      value: 52.8819
    - type: nauc_ndcg_at_3_std
      value: 37.508399999999995
    - type: nauc_ndcg_at_3_diff1
      value: 11.0716
    - type: nauc_ndcg_at_5_max
      value: 56.7662
    - type: nauc_ndcg_at_5_std
      value: 44.0626
    - type: nauc_ndcg_at_5_diff1
      value: 13.7661
    - type: nauc_ndcg_at_10_max
      value: 59.0881
    - type: nauc_ndcg_at_10_std
      value: 47.4331
    - type: nauc_ndcg_at_10_diff1
      value: 12.359
    - type: nauc_ndcg_at_20_max
      value: 59.967000000000006
    - type: nauc_ndcg_at_20_std
      value: 48.2673
    - type: nauc_ndcg_at_20_diff1
      value: 9.870800000000001
    - type: nauc_ndcg_at_100_max
      value: 67.0856
    - type: nauc_ndcg_at_100_std
      value: 57.9806
    - type: nauc_ndcg_at_100_diff1
      value: 10.313799999999999
    - type: nauc_ndcg_at_1000_max
      value: 65.5311
    - type: nauc_ndcg_at_1000_std
      value: 63.056
    - type: nauc_ndcg_at_1000_diff1
      value: 10.4369
    - type: nauc_map_at_1_max
      value: 51.8776
    - type: nauc_map_at_1_std
      value: 16.841
    - type: nauc_map_at_1_diff1
      value: 28.8536
    - type: nauc_map_at_3_max
      value: 59.908300000000004
    - type: nauc_map_at_3_std
      value: 15.8167
    - type: nauc_map_at_3_diff1
      value: 22.8331
    - type: nauc_map_at_5_max
      value: 58.5464
    - type: nauc_map_at_5_std
      value: 23.1686
    - type: nauc_map_at_5_diff1
      value: 22.9876
    - type: nauc_map_at_10_max
      value: 60.4082
    - type: nauc_map_at_10_std
      value: 29.4774
    - type: nauc_map_at_10_diff1
      value: 18.101
    - type: nauc_map_at_20_max
      value: 62.37350000000001
    - type: nauc_map_at_20_std
      value: 34.9525
    - type: nauc_map_at_20_diff1
      value: 13.4316
    - type: nauc_map_at_100_max
      value: 67.3622
    - type: nauc_map_at_100_std
      value: 49.4945
    - type: nauc_map_at_100_diff1
      value: 12.040099999999999
    - type: nauc_map_at_1000_max
      value: 68.682
    - type: nauc_map_at_1000_std
      value: 54.789
    - type: nauc_map_at_1000_diff1
      value: 12.1231
    - type: nauc_recall_at_1_max
      value: 51.8776
    - type: nauc_recall_at_1_std
      value: 16.841
    - type: nauc_recall_at_1_diff1
      value: 28.8536
    - type: nauc_recall_at_3_max
      value: 54.79579999999999
    - type: nauc_recall_at_3_std
      value: 14.1491
    - type: nauc_recall_at_3_diff1
      value: 17.1418
    - type: nauc_recall_at_5_max
      value: 46.6136
    - type: nauc_recall_at_5_std
      value: 26.7224
    - type: nauc_recall_at_5_diff1
      value: 20.1685
    - type: nauc_recall_at_10_max
      value: 47.1669
    - type: nauc_recall_at_10_std
      value: 29.942800000000002
    - type: nauc_recall_at_10_diff1
      value: 11.7095
    - type: nauc_recall_at_20_max
      value: 47.9761
    - type: nauc_recall_at_20_std
      value: 32.1175
    - type: nauc_recall_at_20_diff1
      value: 2.7359
    - type: nauc_recall_at_100_max
      value: 61.0279
    - type: nauc_recall_at_100_std
      value: 54.3599
    - type: nauc_recall_at_100_diff1
      value: 1.3716000000000002
    - type: nauc_recall_at_1000_max
      value: 72.0291
    - type: nauc_recall_at_1000_std
      value: 80.9602
    - type: nauc_recall_at_1000_diff1
      value: -0.41869999999999996
    - type: nauc_precision_at_1_max
      value: 47.8929
    - type: nauc_precision_at_1_std
      value: 37.763000000000005
    - type: nauc_precision_at_1_diff1
      value: 18.953999999999997
    - type: nauc_precision_at_3_max
      value: 52.2589
    - type: nauc_precision_at_3_std
      value: 39.362399999999994
    - type: nauc_precision_at_3_diff1
      value: 9.073
    - type: nauc_precision_at_5_max
      value: 54.110800000000005
    - type: nauc_precision_at_5_std
      value: 46.6259
    - type: nauc_precision_at_5_diff1
      value: 10.1231
    - type: nauc_precision_at_10_max
      value: 54.676199999999994
    - type: nauc_precision_at_10_std
      value: 51.1227
    - type: nauc_precision_at_10_diff1
      value: 7.298699999999999
    - type: nauc_precision_at_20_max
      value: 51.2621
    - type: nauc_precision_at_20_std
      value: 51.6519
    - type: nauc_precision_at_20_diff1
      value: 6.9037
    - type: nauc_precision_at_100_max
      value: 44.887100000000004
    - type: nauc_precision_at_100_std
      value: 53.1115
    - type: nauc_precision_at_100_diff1
      value: 5.6667000000000005
    - type: nauc_precision_at_1000_max
      value: 22.2381
    - type: nauc_precision_at_1000_std
      value: 26.4376
    - type: nauc_precision_at_1000_diff1
      value: 6.6614
    - type: nauc_mrr_at_1_max
      value: 47.8929
    - type: nauc_mrr_at_1_std
      value: 37.763000000000005
    - type: nauc_mrr_at_1_diff1
      value: 18.953999999999997
    - type: nauc_mrr_at_3_max
      value: 43.709199999999996
    - type: nauc_mrr_at_3_std
      value: 36.9888
    - type: nauc_mrr_at_3_diff1
      value: 13.1974
    - type: nauc_mrr_at_5_max
      value: 44.7596
    - type: nauc_mrr_at_5_std
      value: 38.9198
    - type: nauc_mrr_at_5_diff1
      value: 14.5207
    - type: nauc_mrr_at_10_max
      value: 44.952
    - type: nauc_mrr_at_10_std
      value: 39.1837
    - type: nauc_mrr_at_10_diff1
      value: 14.904100000000001
    - type: nauc_mrr_at_20_max
      value: 45.0789
    - type: nauc_mrr_at_20_std
      value: 39.0244
    - type: nauc_mrr_at_20_diff1
      value: 14.617099999999999
    - type: nauc_mrr_at_100_max
      value: 45.2951
    - type: nauc_mrr_at_100_std
      value: 39.2859
    - type: nauc_mrr_at_100_diff1
      value: 14.5809
    - type: nauc_mrr_at_1000_max
      value: 45.2772
    - type: nauc_mrr_at_1000_std
      value: 39.2712
    - type: nauc_mrr_at_1000_diff1
      value: 14.6173
    - type: main_score
      value: 22.159000000000002
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: orthopedic_surgery
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 60.75000000000001
    - type: ndcg_at_3
      value: 54.434000000000005
    - type: ndcg_at_5
      value: 51.845
    - type: ndcg_at_10
      value: 51.17
    - type: ndcg_at_20
      value: 53.299
    - type: ndcg_at_100
      value: 61.650000000000006
    - type: ndcg_at_1000
      value: 67.209
    - type: map_at_1
      value: 13.605999999999998
    - type: map_at_3
      value: 21.435000000000002
    - type: map_at_5
      value: 25.217
    - type: map_at_10
      value: 29.909000000000002
    - type: map_at_20
      value: 34.355000000000004
    - type: map_at_100
      value: 40.714
    - type: map_at_1000
      value: 42.296
    - type: recall_at_1
      value: 13.605999999999998
    - type: recall_at_3
      value: 22.628999999999998
    - type: recall_at_5
      value: 28.365000000000002
    - type: recall_at_10
      value: 37.228
    - type: recall_at_20
      value: 48.777
    - type: recall_at_100
      value: 77.02
    - type: recall_at_1000
      value: 97.235
    - type: precision_at_1
      value: 69.5
    - type: precision_at_3
      value: 53.5
    - type: precision_at_5
      value: 44.7
    - type: precision_at_10
      value: 34.35
    - type: precision_at_20
      value: 26.375
    - type: precision_at_100
      value: 10.514999999999999
    - type: precision_at_1000
      value: 1.44
    - type: mrr_at_1
      value: 69.5
    - type: mrr_at_3
      value: 76.25
    - type: mrr_at_5
      value: 77.325
    - type: mrr_at_10
      value: 77.9123
    - type: mrr_at_20
      value: 78.0774
    - type: mrr_at_100
      value: 78.1866
    - type: mrr_at_1000
      value: 78.19369999999999
    - type: nauc_ndcg_at_1_max
      value: 54.398500000000006
    - type: nauc_ndcg_at_1_std
      value: 17.9876
    - type: nauc_ndcg_at_1_diff1
      value: 45.747
    - type: nauc_ndcg_at_3_max
      value: 52.347
    - type: nauc_ndcg_at_3_std
      value: 20.6541
    - type: nauc_ndcg_at_3_diff1
      value: 33.0152
    - type: nauc_ndcg_at_5_max
      value: 48.4688
    - type: nauc_ndcg_at_5_std
      value: 15.216099999999999
    - type: nauc_ndcg_at_5_diff1
      value: 30.163
    - type: nauc_ndcg_at_10_max
      value: 47.938399999999994
    - type: nauc_ndcg_at_10_std
      value: 12.8266
    - type: nauc_ndcg_at_10_diff1
      value: 31.5183
    - type: nauc_ndcg_at_20_max
      value: 47.1248
    - type: nauc_ndcg_at_20_std
      value: 10.111
    - type: nauc_ndcg_at_20_diff1
      value: 32.941500000000005
    - type: nauc_ndcg_at_100_max
      value: 49.1599
    - type: nauc_ndcg_at_100_std
      value: 14.7579
    - type: nauc_ndcg_at_100_diff1
      value: 30.8168
    - type: nauc_ndcg_at_1000_max
      value: 52.4098
    - type: nauc_ndcg_at_1000_std
      value: 21.5182
    - type: nauc_ndcg_at_1000_diff1
      value: 31.093500000000002
    - type: nauc_map_at_1_max
      value: 17.618000000000002
    - type: nauc_map_at_1_std
      value: -13.4546
    - type: nauc_map_at_1_diff1
      value: 41.566399999999994
    - type: nauc_map_at_3_max
      value: 23.082
    - type: nauc_map_at_3_std
      value: -10.227
    - type: nauc_map_at_3_diff1
      value: 29.129500000000004
    - type: nauc_map_at_5_max
      value: 26.845000000000002
    - type: nauc_map_at_5_std
      value: -9.3116
    - type: nauc_map_at_5_diff1
      value: 27.1069
    - type: nauc_map_at_10_max
      value: 33.0877
    - type: nauc_map_at_10_std
      value: -5.7204999999999995
    - type: nauc_map_at_10_diff1
      value: 26.088
    - type: nauc_map_at_20_max
      value: 34.9799
    - type: nauc_map_at_20_std
      value: -2.9575
    - type: nauc_map_at_20_diff1
      value: 24.5261
    - type: nauc_map_at_100_max
      value: 37.684400000000004
    - type: nauc_map_at_100_std
      value: 6.4834000000000005
    - type: nauc_map_at_100_diff1
      value: 21.1685
    - type: nauc_map_at_1000_max
      value: 38.1583
    - type: nauc_map_at_1000_std
      value: 9.4362
    - type: nauc_map_at_1000_diff1
      value: 20.1685
    - type: nauc_recall_at_1_max
      value: 17.618000000000002
    - type: nauc_recall_at_1_std
      value: -13.4546
    - type: nauc_recall_at_1_diff1
      value: 41.566399999999994
    - type: nauc_recall_at_3_max
      value: 21.3422
    - type: nauc_recall_at_3_std
      value: -11.7132
    - type: nauc_recall_at_3_diff1
      value: 28.5136
    - type: nauc_recall_at_5_max
      value: 23.0503
    - type: nauc_recall_at_5_std
      value: -12.0308
    - type: nauc_recall_at_5_diff1
      value: 27.3613
    - type: nauc_recall_at_10_max
      value: 30.965700000000002
    - type: nauc_recall_at_10_std
      value: -7.4334
    - type: nauc_recall_at_10_diff1
      value: 28.5328
    - type: nauc_recall_at_20_max
      value: 30.848399999999998
    - type: nauc_recall_at_20_std
      value: -6.601
    - type: nauc_recall_at_20_diff1
      value: 27.900399999999998
    - type: nauc_recall_at_100_max
      value: 29.0117
    - type: nauc_recall_at_100_std
      value: 2.0551
    - type: nauc_recall_at_100_diff1
      value: 16.6381
    - type: nauc_recall_at_1000_max
      value: 38.0238
    - type: nauc_recall_at_1000_std
      value: 46.2507
    - type: nauc_recall_at_1000_diff1
      value: 23.321
    - type: nauc_precision_at_1_max
      value: 59.151399999999995
    - type: nauc_precision_at_1_std
      value: 20.9755
    - type: nauc_precision_at_1_diff1
      value: 39.576899999999995
    - type: nauc_precision_at_3_max
      value: 41.3475
    - type: nauc_precision_at_3_std
      value: 28.674899999999997
    - type: nauc_precision_at_3_diff1
      value: 3.8309
    - type: nauc_precision_at_5_max
      value: 35.9683
    - type: nauc_precision_at_5_std
      value: 26.0424
    - type: nauc_precision_at_5_diff1
      value: -4.8175
    - type: nauc_precision_at_10_max
      value: 31.426199999999998
    - type: nauc_precision_at_10_std
      value: 32.1259
    - type: nauc_precision_at_10_diff1
      value: -10.7677
    - type: nauc_precision_at_20_max
      value: 18.674599999999998
    - type: nauc_precision_at_20_std
      value: 33.768100000000004
    - type: nauc_precision_at_20_diff1
      value: -14.386299999999999
    - type: nauc_precision_at_100_max
      value: 6.2094000000000005
    - type: nauc_precision_at_100_std
      value: 37.741400000000006
    - type: nauc_precision_at_100_diff1
      value: -18.4227
    - type: nauc_precision_at_1000_max
      value: 3.1195
    - type: nauc_precision_at_1000_std
      value: 37.286500000000004
    - type: nauc_precision_at_1000_diff1
      value: -18.4375
    - type: nauc_mrr_at_1_max
      value: 59.151399999999995
    - type: nauc_mrr_at_1_std
      value: 20.9755
    - type: nauc_mrr_at_1_diff1
      value: 39.576899999999995
    - type: nauc_mrr_at_3_max
      value: 63.780800000000006
    - type: nauc_mrr_at_3_std
      value: 23.3993
    - type: nauc_mrr_at_3_diff1
      value: 39.055299999999995
    - type: nauc_mrr_at_5_max
      value: 62.9519
    - type: nauc_mrr_at_5_std
      value: 22.863500000000002
    - type: nauc_mrr_at_5_diff1
      value: 39.056200000000004
    - type: nauc_mrr_at_10_max
      value: 63.10829999999999
    - type: nauc_mrr_at_10_std
      value: 22.8684
    - type: nauc_mrr_at_10_diff1
      value: 38.8828
    - type: nauc_mrr_at_20_max
      value: 63.3607
    - type: nauc_mrr_at_20_std
      value: 22.9754
    - type: nauc_mrr_at_20_diff1
      value: 39.0582
    - type: nauc_mrr_at_100_max
      value: 63.25229999999999
    - type: nauc_mrr_at_100_std
      value: 22.922600000000003
    - type: nauc_mrr_at_100_diff1
      value: 39.1318
    - type: nauc_mrr_at_1000_max
      value: 63.239000000000004
    - type: nauc_mrr_at_1000_std
      value: 22.8994
    - type: nauc_mrr_at_1000_diff1
      value: 39.137499999999996
    - type: main_score
      value: 51.17
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: orthopedic_surgery
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 12.25
    - type: ndcg_at_3
      value: 12.534999999999998
    - type: ndcg_at_5
      value: 12.592
    - type: ndcg_at_10
      value: 13.916
    - type: ndcg_at_20
      value: 15.325
    - type: ndcg_at_100
      value: 20.25
    - type: ndcg_at_1000
      value: 28.003
    - type: map_at_1
      value: 3.7769999999999997
    - type: map_at_3
      value: 5.4719999999999995
    - type: map_at_5
      value: 6.366
    - type: map_at_10
      value: 7.836
    - type: map_at_20
      value: 8.731
    - type: map_at_100
      value: 10.223
    - type: map_at_1000
      value: 10.972
    - type: recall_at_1
      value: 3.7769999999999997
    - type: recall_at_3
      value: 6.697
    - type: recall_at_5
      value: 8.474
    - type: recall_at_10
      value: 13.136000000000001
    - type: recall_at_20
      value: 17.427
    - type: recall_at_100
      value: 31.661
    - type: recall_at_1000
      value: 62.053999999999995
    - type: precision_at_1
      value: 14.000000000000002
    - type: precision_at_3
      value: 11.667
    - type: precision_at_5
      value: 10.100000000000001
    - type: precision_at_10
      value: 8.799999999999999
    - type: precision_at_20
      value: 7.025
    - type: precision_at_100
      value: 3.53
    - type: precision_at_1000
      value: 0.8500000000000001
    - type: mrr_at_1
      value: 14.000000000000002
    - type: mrr_at_3
      value: 19.416700000000002
    - type: mrr_at_5
      value: 20.041700000000002
    - type: mrr_at_10
      value: 21.4329
    - type: mrr_at_20
      value: 22.1672
    - type: mrr_at_100
      value: 22.6437
    - type: mrr_at_1000
      value: 22.750799999999998
    - type: nauc_ndcg_at_1_max
      value: 32.8059
    - type: nauc_ndcg_at_1_std
      value: 23.0151
    - type: nauc_ndcg_at_1_diff1
      value: 17.6054
    - type: nauc_ndcg_at_3_max
      value: 32.2789
    - type: nauc_ndcg_at_3_std
      value: 30.056300000000004
    - type: nauc_ndcg_at_3_diff1
      value: 14.2457
    - type: nauc_ndcg_at_5_max
      value: 33.2192
    - type: nauc_ndcg_at_5_std
      value: 28.3219
    - type: nauc_ndcg_at_5_diff1
      value: 13.1414
    - type: nauc_ndcg_at_10_max
      value: 36.961
    - type: nauc_ndcg_at_10_std
      value: 29.5117
    - type: nauc_ndcg_at_10_diff1
      value: 11.3792
    - type: nauc_ndcg_at_20_max
      value: 36.1903
    - type: nauc_ndcg_at_20_std
      value: 28.485300000000002
    - type: nauc_ndcg_at_20_diff1
      value: 11.7044
    - type: nauc_ndcg_at_100_max
      value: 41.8182
    - type: nauc_ndcg_at_100_std
      value: 34.623799999999996
    - type: nauc_ndcg_at_100_diff1
      value: 7.639500000000001
    - type: nauc_ndcg_at_1000_max
      value: 42.3133
    - type: nauc_ndcg_at_1000_std
      value: 32.9471
    - type: nauc_ndcg_at_1000_diff1
      value: 6.7987
    - type: nauc_map_at_1_max
      value: 20.5729
    - type: nauc_map_at_1_std
      value: 18.8459
    - type: nauc_map_at_1_diff1
      value: 18.7146
    - type: nauc_map_at_3_max
      value: 28.4936
    - type: nauc_map_at_3_std
      value: 24.8274
    - type: nauc_map_at_3_diff1
      value: 17.458199999999998
    - type: nauc_map_at_5_max
      value: 29.9757
    - type: nauc_map_at_5_std
      value: 21.243100000000002
    - type: nauc_map_at_5_diff1
      value: 16.2896
    - type: nauc_map_at_10_max
      value: 34.1833
    - type: nauc_map_at_10_std
      value: 22.8358
    - type: nauc_map_at_10_diff1
      value: 13.134199999999998
    - type: nauc_map_at_20_max
      value: 35.067
    - type: nauc_map_at_20_std
      value: 24.9975
    - type: nauc_map_at_20_diff1
      value: 13.1876
    - type: nauc_map_at_100_max
      value: 37.1922
    - type: nauc_map_at_100_std
      value: 31.132900000000003
    - type: nauc_map_at_100_diff1
      value: 12.1831
    - type: nauc_map_at_1000_max
      value: 37.4097
    - type: nauc_map_at_1000_std
      value: 31.6388
    - type: nauc_map_at_1000_diff1
      value: 12.045
    - type: nauc_recall_at_1_max
      value: 20.5729
    - type: nauc_recall_at_1_std
      value: 18.8459
    - type: nauc_recall_at_1_diff1
      value: 18.7146
    - type: nauc_recall_at_3_max
      value: 28.170299999999997
    - type: nauc_recall_at_3_std
      value: 26.860400000000002
    - type: nauc_recall_at_3_diff1
      value: 13.3677
    - type: nauc_recall_at_5_max
      value: 28.220299999999998
    - type: nauc_recall_at_5_std
      value: 19.519000000000002
    - type: nauc_recall_at_5_diff1
      value: 12.501999999999999
    - type: nauc_recall_at_10_max
      value: 36.1699
    - type: nauc_recall_at_10_std
      value: 22.950699999999998
    - type: nauc_recall_at_10_diff1
      value: 8.3368
    - type: nauc_recall_at_20_max
      value: 34.869
    - type: nauc_recall_at_20_std
      value: 23.3199
    - type: nauc_recall_at_20_diff1
      value: 8.0855
    - type: nauc_recall_at_100_max
      value: 48.916399999999996
    - type: nauc_recall_at_100_std
      value: 39.6427
    - type: nauc_recall_at_100_diff1
      value: 0.1031
    - type: nauc_recall_at_1000_max
      value: 56.2504
    - type: nauc_recall_at_1000_std
      value: 42.9539
    - type: nauc_recall_at_1000_diff1
      value: -3.3978
    - type: nauc_precision_at_1_max
      value: 34.6833
    - type: nauc_precision_at_1_std
      value: 22.2443
    - type: nauc_precision_at_1_diff1
      value: 18.937
    - type: nauc_precision_at_3_max
      value: 39.2643
    - type: nauc_precision_at_3_std
      value: 36.851099999999995
    - type: nauc_precision_at_3_diff1
      value: 12.923699999999998
    - type: nauc_precision_at_5_max
      value: 37.3389
    - type: nauc_precision_at_5_std
      value: 30.6489
    - type: nauc_precision_at_5_diff1
      value: 8.0897
    - type: nauc_precision_at_10_max
      value: 41.051
    - type: nauc_precision_at_10_std
      value: 36.8489
    - type: nauc_precision_at_10_diff1
      value: 3.2661999999999995
    - type: nauc_precision_at_20_max
      value: 37.676700000000004
    - type: nauc_precision_at_20_std
      value: 35.885
    - type: nauc_precision_at_20_diff1
      value: 6.8808
    - type: nauc_precision_at_100_max
      value: 31.550800000000002
    - type: nauc_precision_at_100_std
      value: 35.3254
    - type: nauc_precision_at_100_diff1
      value: -0.0628
    - type: nauc_precision_at_1000_max
      value: 12.159699999999999
    - type: nauc_precision_at_1000_std
      value: 8.086699999999999
    - type: nauc_precision_at_1000_diff1
      value: 1.609
    - type: nauc_mrr_at_1_max
      value: 34.6833
    - type: nauc_mrr_at_1_std
      value: 22.2443
    - type: nauc_mrr_at_1_diff1
      value: 18.937
    - type: nauc_mrr_at_3_max
      value: 34.6155
    - type: nauc_mrr_at_3_std
      value: 26.871299999999998
    - type: nauc_mrr_at_3_diff1
      value: 13.0607
    - type: nauc_mrr_at_5_max
      value: 34.1124
    - type: nauc_mrr_at_5_std
      value: 26.673000000000002
    - type: nauc_mrr_at_5_diff1
      value: 12.9241
    - type: nauc_mrr_at_10_max
      value: 35.2871
    - type: nauc_mrr_at_10_std
      value: 27.596799999999998
    - type: nauc_mrr_at_10_diff1
      value: 11.6235
    - type: nauc_mrr_at_20_max
      value: 35.1618
    - type: nauc_mrr_at_20_std
      value: 26.937
    - type: nauc_mrr_at_20_diff1
      value: 11.5846
    - type: nauc_mrr_at_100_max
      value: 35.4628
    - type: nauc_mrr_at_100_std
      value: 26.630599999999998
    - type: nauc_mrr_at_100_diff1
      value: 11.338099999999999
    - type: nauc_mrr_at_1000_max
      value: 35.4548
    - type: nauc_mrr_at_1000_std
      value: 26.617600000000003
    - type: nauc_mrr_at_1000_diff1
      value: 11.4321
    - type: main_score
      value: 13.916
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: orthopedic_surgery
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 24.5
    - type: ndcg_at_3
      value: 24.687
    - type: ndcg_at_5
      value: 24.352999999999998
    - type: ndcg_at_10
      value: 24.891
    - type: ndcg_at_20
      value: 26.287
    - type: ndcg_at_100
      value: 33.079
    - type: ndcg_at_1000
      value: 41.436
    - type: map_at_1
      value: 6.834999999999999
    - type: map_at_3
      value: 10.338
    - type: map_at_5
      value: 11.949
    - type: map_at_10
      value: 13.785
    - type: map_at_20
      value: 15.445999999999998
    - type: map_at_100
      value: 18.32
    - type: map_at_1000
      value: 19.709
    - type: recall_at_1
      value: 6.834999999999999
    - type: recall_at_3
      value: 11.558
    - type: recall_at_5
      value: 15.079999999999998
    - type: recall_at_10
      value: 20.226
    - type: recall_at_20
      value: 26.022000000000002
    - type: recall_at_100
      value: 46.611999999999995
    - type: recall_at_1000
      value: 78.901
    - type: precision_at_1
      value: 29.5
    - type: precision_at_3
      value: 24.833
    - type: precision_at_5
      value: 20.599999999999998
    - type: precision_at_10
      value: 16.150000000000002
    - type: precision_at_20
      value: 12.575
    - type: precision_at_100
      value: 5.94
    - type: precision_at_1000
      value: 1.143
    - type: mrr_at_1
      value: 29.5
    - type: mrr_at_3
      value: 36.916700000000006
    - type: mrr_at_5
      value: 38.9917
    - type: mrr_at_10
      value: 40.5738
    - type: mrr_at_20
      value: 41.2425
    - type: mrr_at_100
      value: 41.5069
    - type: mrr_at_1000
      value: 41.5546
    - type: nauc_ndcg_at_1_max
      value: 39.3236
    - type: nauc_ndcg_at_1_std
      value: 21.2847
    - type: nauc_ndcg_at_1_diff1
      value: 31.586399999999998
    - type: nauc_ndcg_at_3_max
      value: 48.9355
    - type: nauc_ndcg_at_3_std
      value: 22.438299999999998
    - type: nauc_ndcg_at_3_diff1
      value: 27.0578
    - type: nauc_ndcg_at_5_max
      value: 52.169
    - type: nauc_ndcg_at_5_std
      value: 23.6694
    - type: nauc_ndcg_at_5_diff1
      value: 23.735300000000002
    - type: nauc_ndcg_at_10_max
      value: 51.781
    - type: nauc_ndcg_at_10_std
      value: 24.0064
    - type: nauc_ndcg_at_10_diff1
      value: 20.6463
    - type: nauc_ndcg_at_20_max
      value: 51.7658
    - type: nauc_ndcg_at_20_std
      value: 24.0852
    - type: nauc_ndcg_at_20_diff1
      value: 19.7103
    - type: nauc_ndcg_at_100_max
      value: 54.4474
    - type: nauc_ndcg_at_100_std
      value: 31.6873
    - type: nauc_ndcg_at_100_diff1
      value: 17.1214
    - type: nauc_ndcg_at_1000_max
      value: 56.9241
    - type: nauc_ndcg_at_1000_std
      value: 38.0309
    - type: nauc_ndcg_at_1000_diff1
      value: 16.6583
    - type: nauc_map_at_1_max
      value: 40.3816
    - type: nauc_map_at_1_std
      value: 5.3704
    - type: nauc_map_at_1_diff1
      value: 53.0836
    - type: nauc_map_at_3_max
      value: 42.9518
    - type: nauc_map_at_3_std
      value: 8.5508
    - type: nauc_map_at_3_diff1
      value: 41.4236
    - type: nauc_map_at_5_max
      value: 44.039699999999996
    - type: nauc_map_at_5_std
      value: 9.459299999999999
    - type: nauc_map_at_5_diff1
      value: 34.3919
    - type: nauc_map_at_10_max
      value: 43.518699999999995
    - type: nauc_map_at_10_std
      value: 10.4546
    - type: nauc_map_at_10_diff1
      value: 28.8859
    - type: nauc_map_at_20_max
      value: 45.3241
    - type: nauc_map_at_20_std
      value: 13.3366
    - type: nauc_map_at_20_diff1
      value: 26.4547
    - type: nauc_map_at_100_max
      value: 47.9247
    - type: nauc_map_at_100_std
      value: 20.048
    - type: nauc_map_at_100_diff1
      value: 21.915499999999998
    - type: nauc_map_at_1000_max
      value: 48.8745
    - type: nauc_map_at_1000_std
      value: 23.2159
    - type: nauc_map_at_1000_diff1
      value: 21.1535
    - type: nauc_recall_at_1_max
      value: 40.3816
    - type: nauc_recall_at_1_std
      value: 5.3704
    - type: nauc_recall_at_1_diff1
      value: 53.0836
    - type: nauc_recall_at_3_max
      value: 43.917699999999996
    - type: nauc_recall_at_3_std
      value: 8.602
    - type: nauc_recall_at_3_diff1
      value: 36.0712
    - type: nauc_recall_at_5_max
      value: 43.6882
    - type: nauc_recall_at_5_std
      value: 9.4163
    - type: nauc_recall_at_5_diff1
      value: 21.9081
    - type: nauc_recall_at_10_max
      value: 40.0266
    - type: nauc_recall_at_10_std
      value: 11.4113
    - type: nauc_recall_at_10_diff1
      value: 12.4679
    - type: nauc_recall_at_20_max
      value: 40.718199999999996
    - type: nauc_recall_at_20_std
      value: 13.3378
    - type: nauc_recall_at_20_diff1
      value: 8.6095
    - type: nauc_recall_at_100_max
      value: 48.9917
    - type: nauc_recall_at_100_std
      value: 34.8589
    - type: nauc_recall_at_100_diff1
      value: 2.7233
    - type: nauc_recall_at_1000_max
      value: 63.3372
    - type: nauc_recall_at_1000_std
      value: 63.046899999999994
    - type: nauc_recall_at_1000_diff1
      value: -9.3282
    - type: nauc_precision_at_1_max
      value: 44.1351
    - type: nauc_precision_at_1_std
      value: 25.255300000000002
    - type: nauc_precision_at_1_diff1
      value: 28.532200000000003
    - type: nauc_precision_at_3_max
      value: 46.5017
    - type: nauc_precision_at_3_std
      value: 29.053
    - type: nauc_precision_at_3_diff1
      value: 12.581500000000002
    - type: nauc_precision_at_5_max
      value: 50.9217
    - type: nauc_precision_at_5_std
      value: 35.749900000000004
    - type: nauc_precision_at_5_diff1
      value: 2.922
    - type: nauc_precision_at_10_max
      value: 45.213
    - type: nauc_precision_at_10_std
      value: 38.149100000000004
    - type: nauc_precision_at_10_diff1
      value: -7.9922
    - type: nauc_precision_at_20_max
      value: 40.5852
    - type: nauc_precision_at_20_std
      value: 40.3656
    - type: nauc_precision_at_20_diff1
      value: -11.210199999999999
    - type: nauc_precision_at_100_max
      value: 28.71
    - type: nauc_precision_at_100_std
      value: 43.1581
    - type: nauc_precision_at_100_diff1
      value: -15.4147
    - type: nauc_precision_at_1000_max
      value: 17.1742
    - type: nauc_precision_at_1000_std
      value: 35.162
    - type: nauc_precision_at_1000_diff1
      value: -8.7069
    - type: nauc_mrr_at_1_max
      value: 44.1351
    - type: nauc_mrr_at_1_std
      value: 25.255300000000002
    - type: nauc_mrr_at_1_diff1
      value: 28.532200000000003
    - type: nauc_mrr_at_3_max
      value: 51.83069999999999
    - type: nauc_mrr_at_3_std
      value: 30.6181
    - type: nauc_mrr_at_3_diff1
      value: 26.160600000000002
    - type: nauc_mrr_at_5_max
      value: 52.36110000000001
    - type: nauc_mrr_at_5_std
      value: 30.839100000000002
    - type: nauc_mrr_at_5_diff1
      value: 24.5763
    - type: nauc_mrr_at_10_max
      value: 52.1246
    - type: nauc_mrr_at_10_std
      value: 30.9131
    - type: nauc_mrr_at_10_diff1
      value: 23.5647
    - type: nauc_mrr_at_20_max
      value: 51.9513
    - type: nauc_mrr_at_20_std
      value: 30.7942
    - type: nauc_mrr_at_20_diff1
      value: 23.8432
    - type: nauc_mrr_at_100_max
      value: 52.123200000000004
    - type: nauc_mrr_at_100_std
      value: 30.9398
    - type: nauc_mrr_at_100_diff1
      value: 23.9534
    - type: nauc_mrr_at_1000_max
      value: 52.076299999999996
    - type: nauc_mrr_at_1000_std
      value: 30.8819
    - type: nauc_mrr_at_1000_diff1
      value: 23.9329
    - type: main_score
      value: 24.891
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: otorhinolaryngology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 58.75
    - type: ndcg_at_3
      value: 51.113
    - type: ndcg_at_5
      value: 48.946
    - type: ndcg_at_10
      value: 47.447
    - type: ndcg_at_20
      value: 47.425
    - type: ndcg_at_100
      value: 54.642
    - type: ndcg_at_1000
      value: 65.155
    - type: map_at_1
      value: 6.365
    - type: map_at_3
      value: 12.296999999999999
    - type: map_at_5
      value: 14.866999999999999
    - type: map_at_10
      value: 18.975
    - type: map_at_20
      value: 22.985
    - type: map_at_100
      value: 30.8
    - type: map_at_1000
      value: 35.141
    - type: recall_at_1
      value: 6.365
    - type: recall_at_3
      value: 13.253
    - type: recall_at_5
      value: 17.333000000000002
    - type: recall_at_10
      value: 25.029
    - type: recall_at_20
      value: 34.623
    - type: recall_at_100
      value: 62.605
    - type: recall_at_1000
      value: 94.306
    - type: precision_at_1
      value: 70.0
    - type: precision_at_3
      value: 56.333
    - type: precision_at_5
      value: 50.6
    - type: precision_at_10
      value: 41.75
    - type: precision_at_20
      value: 33.800000000000004
    - type: precision_at_100
      value: 16.845
    - type: precision_at_1000
      value: 3.3939999999999997
    - type: mrr_at_1
      value: 70.0
    - type: mrr_at_3
      value: 77.0833
    - type: mrr_at_5
      value: 78.7333
    - type: mrr_at_10
      value: 78.9942
    - type: mrr_at_20
      value: 79.0994
    - type: mrr_at_100
      value: 79.1791
    - type: mrr_at_1000
      value: 79.183
    - type: nauc_ndcg_at_1_max
      value: 23.0541
    - type: nauc_ndcg_at_1_std
      value: -6.7547999999999995
    - type: nauc_ndcg_at_1_diff1
      value: 34.7899
    - type: nauc_ndcg_at_3_max
      value: 31.9251
    - type: nauc_ndcg_at_3_std
      value: 5.774900000000001
    - type: nauc_ndcg_at_3_diff1
      value: 29.1505
    - type: nauc_ndcg_at_5_max
      value: 31.531599999999997
    - type: nauc_ndcg_at_5_std
      value: 6.903099999999999
    - type: nauc_ndcg_at_5_diff1
      value: 25.2152
    - type: nauc_ndcg_at_10_max
      value: 32.771
    - type: nauc_ndcg_at_10_std
      value: 4.9274
    - type: nauc_ndcg_at_10_diff1
      value: 23.6843
    - type: nauc_ndcg_at_20_max
      value: 29.857400000000002
    - type: nauc_ndcg_at_20_std
      value: 2.3416
    - type: nauc_ndcg_at_20_diff1
      value: 25.3388
    - type: nauc_ndcg_at_100_max
      value: 29.4487
    - type: nauc_ndcg_at_100_std
      value: 8.363199999999999
    - type: nauc_ndcg_at_100_diff1
      value: 24.3061
    - type: nauc_ndcg_at_1000_max
      value: 32.656800000000004
    - type: nauc_ndcg_at_1000_std
      value: 15.3001
    - type: nauc_ndcg_at_1000_diff1
      value: 21.607599999999998
    - type: nauc_map_at_1_max
      value: 2.984
    - type: nauc_map_at_1_std
      value: -16.3357
    - type: nauc_map_at_1_diff1
      value: 39.8679
    - type: nauc_map_at_3_max
      value: 13.1494
    - type: nauc_map_at_3_std
      value: -9.7997
    - type: nauc_map_at_3_diff1
      value: 32.3868
    - type: nauc_map_at_5_max
      value: 15.5304
    - type: nauc_map_at_5_std
      value: -6.934899999999999
    - type: nauc_map_at_5_diff1
      value: 29.6433
    - type: nauc_map_at_10_max
      value: 20.6028
    - type: nauc_map_at_10_std
      value: -4.782
    - type: nauc_map_at_10_diff1
      value: 26.6735
    - type: nauc_map_at_20_max
      value: 23.7623
    - type: nauc_map_at_20_std
      value: -1.7728000000000002
    - type: nauc_map_at_20_diff1
      value: 24.4019
    - type: nauc_map_at_100_max
      value: 27.324900000000003
    - type: nauc_map_at_100_std
      value: 7.7754
    - type: nauc_map_at_100_diff1
      value: 22.1984
    - type: nauc_map_at_1000_max
      value: 27.751900000000003
    - type: nauc_map_at_1000_std
      value: 13.422899999999998
    - type: nauc_map_at_1000_diff1
      value: 20.6692
    - type: nauc_recall_at_1_max
      value: 2.984
    - type: nauc_recall_at_1_std
      value: -16.3357
    - type: nauc_recall_at_1_diff1
      value: 39.8679
    - type: nauc_recall_at_3_max
      value: 11.4488
    - type: nauc_recall_at_3_std
      value: -9.1606
    - type: nauc_recall_at_3_diff1
      value: 32.008199999999995
    - type: nauc_recall_at_5_max
      value: 11.7309
    - type: nauc_recall_at_5_std
      value: -7.855099999999999
    - type: nauc_recall_at_5_diff1
      value: 26.928
    - type: nauc_recall_at_10_max
      value: 14.1124
    - type: nauc_recall_at_10_std
      value: -8.2747
    - type: nauc_recall_at_10_diff1
      value: 21.8328
    - type: nauc_recall_at_20_max
      value: 13.697999999999999
    - type: nauc_recall_at_20_std
      value: -5.6466
    - type: nauc_recall_at_20_diff1
      value: 17.2139
    - type: nauc_recall_at_100_max
      value: 12.7504
    - type: nauc_recall_at_100_std
      value: 9.058399999999999
    - type: nauc_recall_at_100_diff1
      value: 8.5206
    - type: nauc_recall_at_1000_max
      value: 37.2254
    - type: nauc_recall_at_1000_std
      value: 49.817699999999995
    - type: nauc_recall_at_1000_diff1
      value: -4.812799999999999
    - type: nauc_precision_at_1_max
      value: 27.128400000000003
    - type: nauc_precision_at_1_std
      value: -6.3169
    - type: nauc_precision_at_1_diff1
      value: 37.2347
    - type: nauc_precision_at_3_max
      value: 40.02
    - type: nauc_precision_at_3_std
      value: 17.0871
    - type: nauc_precision_at_3_diff1
      value: 16.1509
    - type: nauc_precision_at_5_max
      value: 35.7648
    - type: nauc_precision_at_5_std
      value: 22.4046
    - type: nauc_precision_at_5_diff1
      value: 3.5429000000000004
    - type: nauc_precision_at_10_max
      value: 32.5383
    - type: nauc_precision_at_10_std
      value: 19.8196
    - type: nauc_precision_at_10_diff1
      value: -2.6108
    - type: nauc_precision_at_20_max
      value: 24.7033
    - type: nauc_precision_at_20_std
      value: 20.3249
    - type: nauc_precision_at_20_diff1
      value: -5.3223
    - type: nauc_precision_at_100_max
      value: 4.4075999999999995
    - type: nauc_precision_at_100_std
      value: 20.3847
    - type: nauc_precision_at_100_diff1
      value: -7.7542
    - type: nauc_precision_at_1000_max
      value: -0.1031
    - type: nauc_precision_at_1000_std
      value: 13.970699999999999
    - type: nauc_precision_at_1000_diff1
      value: -8.6302
    - type: nauc_mrr_at_1_max
      value: 27.128400000000003
    - type: nauc_mrr_at_1_std
      value: -6.3169
    - type: nauc_mrr_at_1_diff1
      value: 37.2347
    - type: nauc_mrr_at_3_max
      value: 32.1131
    - type: nauc_mrr_at_3_std
      value: 2.7546
    - type: nauc_mrr_at_3_diff1
      value: 37.2989
    - type: nauc_mrr_at_5_max
      value: 30.8927
    - type: nauc_mrr_at_5_std
      value: 0.422
    - type: nauc_mrr_at_5_diff1
      value: 36.0035
    - type: nauc_mrr_at_10_max
      value: 30.3494
    - type: nauc_mrr_at_10_std
      value: -0.2848
    - type: nauc_mrr_at_10_diff1
      value: 35.881600000000006
    - type: nauc_mrr_at_20_max
      value: 30.2487
    - type: nauc_mrr_at_20_std
      value: -0.4132
    - type: nauc_mrr_at_20_diff1
      value: 35.9397
    - type: nauc_mrr_at_100_max
      value: 30.206
    - type: nauc_mrr_at_100_std
      value: -0.39039999999999997
    - type: nauc_mrr_at_100_diff1
      value: 36.020799999999994
    - type: nauc_mrr_at_1000_max
      value: 30.2487
    - type: nauc_mrr_at_1000_std
      value: -0.3869
    - type: nauc_mrr_at_1000_diff1
      value: 36.0524
    - type: main_score
      value: 47.447
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: otorhinolaryngology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 9.0
    - type: ndcg_at_3
      value: 8.487
    - type: ndcg_at_5
      value: 8.622
    - type: ndcg_at_10
      value: 9.475999999999999
    - type: ndcg_at_20
      value: 10.620000000000001
    - type: ndcg_at_100
      value: 16.346
    - type: ndcg_at_1000
      value: 27.265
    - type: map_at_1
      value: 0.9900000000000001
    - type: map_at_3
      value: 1.892
    - type: map_at_5
      value: 2.261
    - type: map_at_10
      value: 2.94
    - type: map_at_20
      value: 3.6990000000000003
    - type: map_at_100
      value: 5.8229999999999995
    - type: map_at_1000
      value: 7.664999999999999
    - type: recall_at_1
      value: 0.9900000000000001
    - type: recall_at_3
      value: 2.637
    - type: recall_at_5
      value: 3.6189999999999998
    - type: recall_at_10
      value: 5.88
    - type: recall_at_20
      value: 9.259
    - type: recall_at_100
      value: 25.215
    - type: recall_at_1000
      value: 58.672999999999995
    - type: precision_at_1
      value: 12.0
    - type: precision_at_3
      value: 10.333
    - type: precision_at_5
      value: 10.0
    - type: precision_at_10
      value: 9.65
    - type: precision_at_20
      value: 8.825
    - type: precision_at_100
      value: 6.175
    - type: precision_at_1000
      value: 1.916
    - type: mrr_at_1
      value: 12.0
    - type: mrr_at_3
      value: 16.5833
    - type: mrr_at_5
      value: 18.9583
    - type: mrr_at_10
      value: 20.194000000000003
    - type: mrr_at_20
      value: 21.0313
    - type: mrr_at_100
      value: 21.6374
    - type: mrr_at_1000
      value: 21.7083
    - type: nauc_ndcg_at_1_max
      value: 42.2033
    - type: nauc_ndcg_at_1_std
      value: 33.1304
    - type: nauc_ndcg_at_1_diff1
      value: 3.8263
    - type: nauc_ndcg_at_3_max
      value: 36.240899999999996
    - type: nauc_ndcg_at_3_std
      value: 46.0242
    - type: nauc_ndcg_at_3_diff1
      value: 0.638
    - type: nauc_ndcg_at_5_max
      value: 35.0781
    - type: nauc_ndcg_at_5_std
      value: 44.2813
    - type: nauc_ndcg_at_5_diff1
      value: -0.772
    - type: nauc_ndcg_at_10_max
      value: 34.6139
    - type: nauc_ndcg_at_10_std
      value: 47.0856
    - type: nauc_ndcg_at_10_diff1
      value: 2.5038
    - type: nauc_ndcg_at_20_max
      value: 38.8003
    - type: nauc_ndcg_at_20_std
      value: 49.3951
    - type: nauc_ndcg_at_20_diff1
      value: 6.1885
    - type: nauc_ndcg_at_100_max
      value: 43.7993
    - type: nauc_ndcg_at_100_std
      value: 57.052
    - type: nauc_ndcg_at_100_diff1
      value: 6.4491000000000005
    - type: nauc_ndcg_at_1000_max
      value: 50.7017
    - type: nauc_ndcg_at_1000_std
      value: 58.455999999999996
    - type: nauc_ndcg_at_1000_diff1
      value: 3.6403
    - type: nauc_map_at_1_max
      value: 46.286899999999996
    - type: nauc_map_at_1_std
      value: 26.722600000000003
    - type: nauc_map_at_1_diff1
      value: 23.3318
    - type: nauc_map_at_3_max
      value: 34.0861
    - type: nauc_map_at_3_std
      value: 46.7414
    - type: nauc_map_at_3_diff1
      value: 8.5018
    - type: nauc_map_at_5_max
      value: 34.7325
    - type: nauc_map_at_5_std
      value: 43.0688
    - type: nauc_map_at_5_diff1
      value: 9.9683
    - type: nauc_map_at_10_max
      value: 35.2354
    - type: nauc_map_at_10_std
      value: 46.2276
    - type: nauc_map_at_10_diff1
      value: 11.2777
    - type: nauc_map_at_20_max
      value: 39.5891
    - type: nauc_map_at_20_std
      value: 48.1422
    - type: nauc_map_at_20_diff1
      value: 10.886999999999999
    - type: nauc_map_at_100_max
      value: 42.2714
    - type: nauc_map_at_100_std
      value: 57.924699999999994
    - type: nauc_map_at_100_diff1
      value: 7.001799999999999
    - type: nauc_map_at_1000_max
      value: 44.162800000000004
    - type: nauc_map_at_1000_std
      value: 59.3092
    - type: nauc_map_at_1000_diff1
      value: 3.3226
    - type: nauc_recall_at_1_max
      value: 46.286899999999996
    - type: nauc_recall_at_1_std
      value: 26.722600000000003
    - type: nauc_recall_at_1_diff1
      value: 23.3318
    - type: nauc_recall_at_3_max
      value: 26.035399999999996
    - type: nauc_recall_at_3_std
      value: 53.1263
    - type: nauc_recall_at_3_diff1
      value: 0.42129999999999995
    - type: nauc_recall_at_5_max
      value: 25.4674
    - type: nauc_recall_at_5_std
      value: 44.1066
    - type: nauc_recall_at_5_diff1
      value: 4.22
    - type: nauc_recall_at_10_max
      value: 24.2043
    - type: nauc_recall_at_10_std
      value: 43.383
    - type: nauc_recall_at_10_diff1
      value: 10.5937
    - type: nauc_recall_at_20_max
      value: 36.433
    - type: nauc_recall_at_20_std
      value: 46.3323
    - type: nauc_recall_at_20_diff1
      value: 13.9961
    - type: nauc_recall_at_100_max
      value: 37.576100000000004
    - type: nauc_recall_at_100_std
      value: 54.7615
    - type: nauc_recall_at_100_diff1
      value: 11.209900000000001
    - type: nauc_recall_at_1000_max
      value: 55.1674
    - type: nauc_recall_at_1000_std
      value: 59.4684
    - type: nauc_recall_at_1000_diff1
      value: 11.3697
    - type: nauc_precision_at_1_max
      value: 42.180800000000005
    - type: nauc_precision_at_1_std
      value: 32.8073
    - type: nauc_precision_at_1_diff1
      value: 0.4348
    - type: nauc_precision_at_3_max
      value: 38.1217
    - type: nauc_precision_at_3_std
      value: 46.0086
    - type: nauc_precision_at_3_diff1
      value: -2.2963
    - type: nauc_precision_at_5_max
      value: 35.9551
    - type: nauc_precision_at_5_std
      value: 42.0543
    - type: nauc_precision_at_5_diff1
      value: -3.1207
    - type: nauc_precision_at_10_max
      value: 34.2246
    - type: nauc_precision_at_10_std
      value: 46.5836
    - type: nauc_precision_at_10_diff1
      value: -2.844
    - type: nauc_precision_at_20_max
      value: 39.338899999999995
    - type: nauc_precision_at_20_std
      value: 50.256299999999996
    - type: nauc_precision_at_20_diff1
      value: -3.9847
    - type: nauc_precision_at_100_max
      value: 35.5887
    - type: nauc_precision_at_100_std
      value: 49.170700000000004
    - type: nauc_precision_at_100_diff1
      value: -6.653499999999999
    - type: nauc_precision_at_1000_max
      value: 22.698999999999998
    - type: nauc_precision_at_1000_std
      value: 23.137900000000002
    - type: nauc_precision_at_1000_diff1
      value: -5.8536
    - type: nauc_mrr_at_1_max
      value: 42.180800000000005
    - type: nauc_mrr_at_1_std
      value: 32.8073
    - type: nauc_mrr_at_1_diff1
      value: 0.4348
    - type: nauc_mrr_at_3_max
      value: 39.9656
    - type: nauc_mrr_at_3_std
      value: 38.564
    - type: nauc_mrr_at_3_diff1
      value: -0.4943
    - type: nauc_mrr_at_5_max
      value: 39.152300000000004
    - type: nauc_mrr_at_5_std
      value: 38.2446
    - type: nauc_mrr_at_5_diff1
      value: -1.0491000000000001
    - type: nauc_mrr_at_10_max
      value: 39.4098
    - type: nauc_mrr_at_10_std
      value: 38.4484
    - type: nauc_mrr_at_10_diff1
      value: -0.134
    - type: nauc_mrr_at_20_max
      value: 40.426899999999996
    - type: nauc_mrr_at_20_std
      value: 38.9061
    - type: nauc_mrr_at_20_diff1
      value: 0.20010000000000003
    - type: nauc_mrr_at_100_max
      value: 40.4788
    - type: nauc_mrr_at_100_std
      value: 38.8631
    - type: nauc_mrr_at_100_diff1
      value: -0.013300000000000001
    - type: nauc_mrr_at_1000_max
      value: 40.4469
    - type: nauc_mrr_at_1000_std
      value: 38.8602
    - type: nauc_mrr_at_1000_diff1
      value: 0.0619
    - type: main_score
      value: 9.475999999999999
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: otorhinolaryngology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 19.5
    - type: ndcg_at_3
      value: 17.663
    - type: ndcg_at_5
      value: 17.574
    - type: ndcg_at_10
      value: 17.660999999999998
    - type: ndcg_at_20
      value: 18.372
    - type: ndcg_at_100
      value: 24.366
    - type: ndcg_at_1000
      value: 35.075
    - type: map_at_1
      value: 2.095
    - type: map_at_3
      value: 4.43
    - type: map_at_5
      value: 5.437
    - type: map_at_10
      value: 6.736000000000001
    - type: map_at_20
      value: 8.116
    - type: map_at_100
      value: 11.183
    - type: map_at_1000
      value: 13.373
    - type: recall_at_1
      value: 2.095
    - type: recall_at_3
      value: 5.135
    - type: recall_at_5
      value: 7.002999999999999
    - type: recall_at_10
      value: 10.571
    - type: recall_at_20
      value: 14.809
    - type: recall_at_100
      value: 32.126
    - type: recall_at_1000
      value: 64.834
    - type: precision_at_1
      value: 25.5
    - type: precision_at_3
      value: 21.5
    - type: precision_at_5
      value: 19.7
    - type: precision_at_10
      value: 16.6
    - type: precision_at_20
      value: 13.8
    - type: precision_at_100
      value: 8.075000000000001
    - type: precision_at_1000
      value: 2.1399999999999997
    - type: mrr_at_1
      value: 25.5
    - type: mrr_at_3
      value: 31.9167
    - type: mrr_at_5
      value: 33.216699999999996
    - type: mrr_at_10
      value: 34.9563
    - type: mrr_at_20
      value: 35.6321
    - type: mrr_at_100
      value: 36.0473
    - type: mrr_at_1000
      value: 36.106500000000004
    - type: nauc_ndcg_at_1_max
      value: 38.752900000000004
    - type: nauc_ndcg_at_1_std
      value: 22.9816
    - type: nauc_ndcg_at_1_diff1
      value: 14.973
    - type: nauc_ndcg_at_3_max
      value: 45.1268
    - type: nauc_ndcg_at_3_std
      value: 27.2744
    - type: nauc_ndcg_at_3_diff1
      value: 17.1938
    - type: nauc_ndcg_at_5_max
      value: 50.1247
    - type: nauc_ndcg_at_5_std
      value: 32.867000000000004
    - type: nauc_ndcg_at_5_diff1
      value: 17.5213
    - type: nauc_ndcg_at_10_max
      value: 54.09080000000001
    - type: nauc_ndcg_at_10_std
      value: 35.4424
    - type: nauc_ndcg_at_10_diff1
      value: 19.7834
    - type: nauc_ndcg_at_20_max
      value: 55.9825
    - type: nauc_ndcg_at_20_std
      value: 36.863600000000005
    - type: nauc_ndcg_at_20_diff1
      value: 21.8584
    - type: nauc_ndcg_at_100_max
      value: 60.00529999999999
    - type: nauc_ndcg_at_100_std
      value: 45.7262
    - type: nauc_ndcg_at_100_diff1
      value: 20.6427
    - type: nauc_ndcg_at_1000_max
      value: 59.0706
    - type: nauc_ndcg_at_1000_std
      value: 50.505100000000006
    - type: nauc_ndcg_at_1000_diff1
      value: 15.5525
    - type: nauc_map_at_1_max
      value: 33.4795
    - type: nauc_map_at_1_std
      value: 14.426400000000001
    - type: nauc_map_at_1_diff1
      value: 16.761699999999998
    - type: nauc_map_at_3_max
      value: 37.6433
    - type: nauc_map_at_3_std
      value: 16.2529
    - type: nauc_map_at_3_diff1
      value: 12.893099999999999
    - type: nauc_map_at_5_max
      value: 41.5271
    - type: nauc_map_at_5_std
      value: 20.3954
    - type: nauc_map_at_5_diff1
      value: 17.0506
    - type: nauc_map_at_10_max
      value: 47.210499999999996
    - type: nauc_map_at_10_std
      value: 25.4344
    - type: nauc_map_at_10_diff1
      value: 19.8433
    - type: nauc_map_at_20_max
      value: 51.430299999999995
    - type: nauc_map_at_20_std
      value: 31.0075
    - type: nauc_map_at_20_diff1
      value: 21.435000000000002
    - type: nauc_map_at_100_max
      value: 55.723299999999995
    - type: nauc_map_at_100_std
      value: 41.9041
    - type: nauc_map_at_100_diff1
      value: 20.6049
    - type: nauc_map_at_1000_max
      value: 54.0405
    - type: nauc_map_at_1000_std
      value: 45.088
    - type: nauc_map_at_1000_diff1
      value: 17.8828
    - type: nauc_recall_at_1_max
      value: 33.4795
    - type: nauc_recall_at_1_std
      value: 14.426400000000001
    - type: nauc_recall_at_1_diff1
      value: 16.761699999999998
    - type: nauc_recall_at_3_max
      value: 41.3467
    - type: nauc_recall_at_3_std
      value: 19.2823
    - type: nauc_recall_at_3_diff1
      value: 13.3268
    - type: nauc_recall_at_5_max
      value: 46.3683
    - type: nauc_recall_at_5_std
      value: 23.827
    - type: nauc_recall_at_5_diff1
      value: 19.297
    - type: nauc_recall_at_10_max
      value: 50.0236
    - type: nauc_recall_at_10_std
      value: 25.537
    - type: nauc_recall_at_10_diff1
      value: 23.9121
    - type: nauc_recall_at_20_max
      value: 52.249500000000005
    - type: nauc_recall_at_20_std
      value: 30.9311
    - type: nauc_recall_at_20_diff1
      value: 23.5544
    - type: nauc_recall_at_100_max
      value: 60.0984
    - type: nauc_recall_at_100_std
      value: 46.9398
    - type: nauc_recall_at_100_diff1
      value: 20.657600000000002
    - type: nauc_recall_at_1000_max
      value: 71.0111
    - type: nauc_recall_at_1000_std
      value: 63.178999999999995
    - type: nauc_recall_at_1000_diff1
      value: 14.643900000000002
    - type: nauc_precision_at_1_max
      value: 38.3342
    - type: nauc_precision_at_1_std
      value: 24.3116
    - type: nauc_precision_at_1_diff1
      value: 12.347199999999999
    - type: nauc_precision_at_3_max
      value: 49.369099999999996
    - type: nauc_precision_at_3_std
      value: 32.3882
    - type: nauc_precision_at_3_diff1
      value: 16.189500000000002
    - type: nauc_precision_at_5_max
      value: 55.2461
    - type: nauc_precision_at_5_std
      value: 39.0339
    - type: nauc_precision_at_5_diff1
      value: 17.2901
    - type: nauc_precision_at_10_max
      value: 57.067800000000005
    - type: nauc_precision_at_10_std
      value: 43.318
    - type: nauc_precision_at_10_diff1
      value: 17.4133
    - type: nauc_precision_at_20_max
      value: 52.382600000000004
    - type: nauc_precision_at_20_std
      value: 45.1982
    - type: nauc_precision_at_20_diff1
      value: 16.1817
    - type: nauc_precision_at_100_max
      value: 33.0242
    - type: nauc_precision_at_100_std
      value: 43.7429
    - type: nauc_precision_at_100_diff1
      value: 6.1582
    - type: nauc_precision_at_1000_max
      value: 6.4754000000000005
    - type: nauc_precision_at_1000_std
      value: 16.081500000000002
    - type: nauc_precision_at_1000_diff1
      value: -2.5237
    - type: nauc_mrr_at_1_max
      value: 38.3342
    - type: nauc_mrr_at_1_std
      value: 24.3116
    - type: nauc_mrr_at_1_diff1
      value: 12.347199999999999
    - type: nauc_mrr_at_3_max
      value: 44.7413
    - type: nauc_mrr_at_3_std
      value: 28.607100000000003
    - type: nauc_mrr_at_3_diff1
      value: 15.176
    - type: nauc_mrr_at_5_max
      value: 46.9016
    - type: nauc_mrr_at_5_std
      value: 29.964000000000002
    - type: nauc_mrr_at_5_diff1
      value: 15.0206
    - type: nauc_mrr_at_10_max
      value: 46.6374
    - type: nauc_mrr_at_10_std
      value: 29.4985
    - type: nauc_mrr_at_10_diff1
      value: 15.9884
    - type: nauc_mrr_at_20_max
      value: 46.2181
    - type: nauc_mrr_at_20_std
      value: 29.538999999999998
    - type: nauc_mrr_at_20_diff1
      value: 15.964999999999998
    - type: nauc_mrr_at_100_max
      value: 46.1424
    - type: nauc_mrr_at_100_std
      value: 29.5665
    - type: nauc_mrr_at_100_diff1
      value: 15.7968
    - type: nauc_mrr_at_1000_max
      value: 46.1536
    - type: nauc_mrr_at_1000_std
      value: 29.5835
    - type: nauc_mrr_at_1000_diff1
      value: 15.7713
    - type: main_score
      value: 17.660999999999998
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: plastic_surgery
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 67.75
    - type: ndcg_at_3
      value: 59.958
    - type: ndcg_at_5
      value: 56.188
    - type: ndcg_at_10
      value: 54.081999999999994
    - type: ndcg_at_20
      value: 54.352000000000004
    - type: ndcg_at_100
      value: 63.461
    - type: ndcg_at_1000
      value: 71.052
    - type: map_at_1
      value: 8.769
    - type: map_at_3
      value: 16.821
    - type: map_at_5
      value: 20.674999999999997
    - type: map_at_10
      value: 25.861
    - type: map_at_20
      value: 30.334
    - type: map_at_100
      value: 39.324
    - type: map_at_1000
      value: 42.05
    - type: recall_at_1
      value: 8.769
    - type: recall_at_3
      value: 17.97
    - type: recall_at_5
      value: 23.372999999999998
    - type: recall_at_10
      value: 32.952
    - type: recall_at_20
      value: 43.49
    - type: recall_at_100
      value: 74.634
    - type: recall_at_1000
      value: 97.513
    - type: precision_at_1
      value: 78.0
    - type: precision_at_3
      value: 62.333000000000006
    - type: precision_at_5
      value: 53.7
    - type: precision_at_10
      value: 42.75
    - type: precision_at_20
      value: 33.125
    - type: precision_at_100
      value: 15.129999999999999
    - type: precision_at_1000
      value: 2.39
    - type: mrr_at_1
      value: 78.0
    - type: mrr_at_3
      value: 85.25
    - type: mrr_at_5
      value: 86.05000000000001
    - type: mrr_at_10
      value: 86.3069
    - type: mrr_at_20
      value: 86.3364
    - type: mrr_at_100
      value: 86.3549
    - type: mrr_at_1000
      value: 86.3549
    - type: nauc_ndcg_at_1_max
      value: 39.9723
    - type: nauc_ndcg_at_1_std
      value: 1.3915
    - type: nauc_ndcg_at_1_diff1
      value: 56.5282
    - type: nauc_ndcg_at_3_max
      value: 33.899
    - type: nauc_ndcg_at_3_std
      value: 4.6108
    - type: nauc_ndcg_at_3_diff1
      value: 28.0094
    - type: nauc_ndcg_at_5_max
      value: 32.277699999999996
    - type: nauc_ndcg_at_5_std
      value: 9.3641
    - type: nauc_ndcg_at_5_diff1
      value: 25.5435
    - type: nauc_ndcg_at_10_max
      value: 29.232999999999997
    - type: nauc_ndcg_at_10_std
      value: 11.2034
    - type: nauc_ndcg_at_10_diff1
      value: 23.6675
    - type: nauc_ndcg_at_20_max
      value: 27.5872
    - type: nauc_ndcg_at_20_std
      value: 11.1633
    - type: nauc_ndcg_at_20_diff1
      value: 21.0519
    - type: nauc_ndcg_at_100_max
      value: 31.857999999999997
    - type: nauc_ndcg_at_100_std
      value: 26.0807
    - type: nauc_ndcg_at_100_diff1
      value: 19.3271
    - type: nauc_ndcg_at_1000_max
      value: 31.2605
    - type: nauc_ndcg_at_1000_std
      value: 21.9248
    - type: nauc_ndcg_at_1000_diff1
      value: 19.2753
    - type: nauc_map_at_1_max
      value: 11.0953
    - type: nauc_map_at_1_std
      value: -16.169
    - type: nauc_map_at_1_diff1
      value: 43.9757
    - type: nauc_map_at_3_max
      value: 15.6448
    - type: nauc_map_at_3_std
      value: -11.5982
    - type: nauc_map_at_3_diff1
      value: 24.3589
    - type: nauc_map_at_5_max
      value: 17.2011
    - type: nauc_map_at_5_std
      value: -7.3374
    - type: nauc_map_at_5_diff1
      value: 21.685399999999998
    - type: nauc_map_at_10_max
      value: 19.043499999999998
    - type: nauc_map_at_10_std
      value: -3.2707
    - type: nauc_map_at_10_diff1
      value: 18.8752
    - type: nauc_map_at_20_max
      value: 20.0765
    - type: nauc_map_at_20_std
      value: 2.5831
    - type: nauc_map_at_20_diff1
      value: 17.7315
    - type: nauc_map_at_100_max
      value: 20.599899999999998
    - type: nauc_map_at_100_std
      value: 18.8259
    - type: nauc_map_at_100_diff1
      value: 10.5128
    - type: nauc_map_at_1000_max
      value: 19.1446
    - type: nauc_map_at_1000_std
      value: 19.122700000000002
    - type: nauc_map_at_1000_diff1
      value: 7.8306000000000004
    - type: nauc_recall_at_1_max
      value: 11.0953
    - type: nauc_recall_at_1_std
      value: -16.169
    - type: nauc_recall_at_1_diff1
      value: 43.9757
    - type: nauc_recall_at_3_max
      value: 15.4575
    - type: nauc_recall_at_3_std
      value: -10.2927
    - type: nauc_recall_at_3_diff1
      value: 21.893
    - type: nauc_recall_at_5_max
      value: 14.186599999999999
    - type: nauc_recall_at_5_std
      value: -6.930600000000001
    - type: nauc_recall_at_5_diff1
      value: 17.793400000000002
    - type: nauc_recall_at_10_max
      value: 13.0639
    - type: nauc_recall_at_10_std
      value: -4.063400000000001
    - type: nauc_recall_at_10_diff1
      value: 16.2193
    - type: nauc_recall_at_20_max
      value: 13.801
    - type: nauc_recall_at_20_std
      value: 2.5117000000000003
    - type: nauc_recall_at_20_diff1
      value: 13.7599
    - type: nauc_recall_at_100_max
      value: 18.8061
    - type: nauc_recall_at_100_std
      value: 34.467999999999996
    - type: nauc_recall_at_100_diff1
      value: 4.1441
    - type: nauc_recall_at_1000_max
      value: 20.785899999999998
    - type: nauc_recall_at_1000_std
      value: 63.2456
    - type: nauc_recall_at_1000_diff1
      value: -11.3226
    - type: nauc_precision_at_1_max
      value: 38.5172
    - type: nauc_precision_at_1_std
      value: 3.4462
    - type: nauc_precision_at_1_diff1
      value: 50.5645
    - type: nauc_precision_at_3_max
      value: 19.0546
    - type: nauc_precision_at_3_std
      value: 8.3792
    - type: nauc_precision_at_3_diff1
      value: -1.7430999999999999
    - type: nauc_precision_at_5_max
      value: 16.231499999999997
    - type: nauc_precision_at_5_std
      value: 18.2838
    - type: nauc_precision_at_5_diff1
      value: -5.2056
    - type: nauc_precision_at_10_max
      value: 9.3026
    - type: nauc_precision_at_10_std
      value: 23.149800000000003
    - type: nauc_precision_at_10_diff1
      value: -12.2439
    - type: nauc_precision_at_20_max
      value: 1.4767000000000001
    - type: nauc_precision_at_20_std
      value: 26.437300000000004
    - type: nauc_precision_at_20_diff1
      value: -16.6781
    - type: nauc_precision_at_100_max
      value: -7.756200000000001
    - type: nauc_precision_at_100_std
      value: 22.622999999999998
    - type: nauc_precision_at_100_diff1
      value: -21.8454
    - type: nauc_precision_at_1000_max
      value: -17.3046
    - type: nauc_precision_at_1000_std
      value: -0.4687
    - type: nauc_precision_at_1000_diff1
      value: -21.2201
    - type: nauc_mrr_at_1_max
      value: 38.5172
    - type: nauc_mrr_at_1_std
      value: 3.4462
    - type: nauc_mrr_at_1_diff1
      value: 50.5645
    - type: nauc_mrr_at_3_max
      value: 48.4513
    - type: nauc_mrr_at_3_std
      value: 10.053700000000001
    - type: nauc_mrr_at_3_diff1
      value: 46.6829
    - type: nauc_mrr_at_5_max
      value: 46.7355
    - type: nauc_mrr_at_5_std
      value: 8.5268
    - type: nauc_mrr_at_5_diff1
      value: 46.7111
    - type: nauc_mrr_at_10_max
      value: 45.942499999999995
    - type: nauc_mrr_at_10_std
      value: 7.4193
    - type: nauc_mrr_at_10_diff1
      value: 47.857699999999994
    - type: nauc_mrr_at_20_max
      value: 45.8818
    - type: nauc_mrr_at_20_std
      value: 7.475999999999999
    - type: nauc_mrr_at_20_diff1
      value: 47.7373
    - type: nauc_mrr_at_100_max
      value: 45.822
    - type: nauc_mrr_at_100_std
      value: 7.469
    - type: nauc_mrr_at_100_diff1
      value: 47.7016
    - type: nauc_mrr_at_1000_max
      value: 45.822
    - type: nauc_mrr_at_1000_std
      value: 7.469
    - type: nauc_mrr_at_1000_diff1
      value: 47.7016
    - type: main_score
      value: 54.081999999999994
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: plastic_surgery
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 21.75
    - type: ndcg_at_3
      value: 18.837
    - type: ndcg_at_5
      value: 18.215999999999998
    - type: ndcg_at_10
      value: 18.512
    - type: ndcg_at_20
      value: 19.611
    - type: ndcg_at_100
      value: 26.711000000000002
    - type: ndcg_at_1000
      value: 36.405
    - type: map_at_1
      value: 2.932
    - type: map_at_3
      value: 4.791
    - type: map_at_5
      value: 5.998
    - type: map_at_10
      value: 7.713
    - type: map_at_20
      value: 9.075
    - type: map_at_100
      value: 12.352
    - type: map_at_1000
      value: 13.861
    - type: recall_at_1
      value: 2.932
    - type: recall_at_3
      value: 5.4510000000000005
    - type: recall_at_5
      value: 8.051
    - type: recall_at_10
      value: 12.638
    - type: recall_at_20
      value: 18.009
    - type: recall_at_100
      value: 38.15
    - type: recall_at_1000
      value: 71.577
    - type: precision_at_1
      value: 27.0
    - type: precision_at_3
      value: 19.833000000000002
    - type: precision_at_5
      value: 18.099999999999998
    - type: precision_at_10
      value: 15.75
    - type: precision_at_20
      value: 12.5
    - type: precision_at_100
      value: 6.52
    - type: precision_at_1000
      value: 1.498
    - type: mrr_at_1
      value: 27.0
    - type: mrr_at_3
      value: 31.833299999999998
    - type: mrr_at_5
      value: 33.7333
    - type: mrr_at_10
      value: 35.3665
    - type: mrr_at_20
      value: 35.9375
    - type: mrr_at_100
      value: 36.2769
    - type: mrr_at_1000
      value: 36.3373
    - type: nauc_ndcg_at_1_max
      value: 43.717800000000004
    - type: nauc_ndcg_at_1_std
      value: 35.2105
    - type: nauc_ndcg_at_1_diff1
      value: 28.829500000000003
    - type: nauc_ndcg_at_3_max
      value: 43.349399999999996
    - type: nauc_ndcg_at_3_std
      value: 39.1872
    - type: nauc_ndcg_at_3_diff1
      value: 21.1047
    - type: nauc_ndcg_at_5_max
      value: 47.8451
    - type: nauc_ndcg_at_5_std
      value: 42.5181
    - type: nauc_ndcg_at_5_diff1
      value: 19.078300000000002
    - type: nauc_ndcg_at_10_max
      value: 49.788199999999996
    - type: nauc_ndcg_at_10_std
      value: 46.5601
    - type: nauc_ndcg_at_10_diff1
      value: 16.556
    - type: nauc_ndcg_at_20_max
      value: 51.60209999999999
    - type: nauc_ndcg_at_20_std
      value: 47.5537
    - type: nauc_ndcg_at_20_diff1
      value: 16.5479
    - type: nauc_ndcg_at_100_max
      value: 53.5291
    - type: nauc_ndcg_at_100_std
      value: 59.6699
    - type: nauc_ndcg_at_100_diff1
      value: 13.365499999999999
    - type: nauc_ndcg_at_1000_max
      value: 53.889900000000004
    - type: nauc_ndcg_at_1000_std
      value: 62.61449999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 11.686399999999999
    - type: nauc_map_at_1_max
      value: 36.228
    - type: nauc_map_at_1_std
      value: 16.9316
    - type: nauc_map_at_1_diff1
      value: 36.4257
    - type: nauc_map_at_3_max
      value: 37.6485
    - type: nauc_map_at_3_std
      value: 20.9514
    - type: nauc_map_at_3_diff1
      value: 24.4027
    - type: nauc_map_at_5_max
      value: 41.510999999999996
    - type: nauc_map_at_5_std
      value: 25.6374
    - type: nauc_map_at_5_diff1
      value: 21.309800000000003
    - type: nauc_map_at_10_max
      value: 44.3985
    - type: nauc_map_at_10_std
      value: 33.6395
    - type: nauc_map_at_10_diff1
      value: 18.4125
    - type: nauc_map_at_20_max
      value: 46.2344
    - type: nauc_map_at_20_std
      value: 39.099000000000004
    - type: nauc_map_at_20_diff1
      value: 17.7258
    - type: nauc_map_at_100_max
      value: 48.254599999999996
    - type: nauc_map_at_100_std
      value: 53.358000000000004
    - type: nauc_map_at_100_diff1
      value: 15.387999999999998
    - type: nauc_map_at_1000_max
      value: 48.4559
    - type: nauc_map_at_1000_std
      value: 56.648900000000005
    - type: nauc_map_at_1000_diff1
      value: 14.731
    - type: nauc_recall_at_1_max
      value: 36.228
    - type: nauc_recall_at_1_std
      value: 16.9316
    - type: nauc_recall_at_1_diff1
      value: 36.4257
    - type: nauc_recall_at_3_max
      value: 35.6758
    - type: nauc_recall_at_3_std
      value: 20.495
    - type: nauc_recall_at_3_diff1
      value: 20.2299
    - type: nauc_recall_at_5_max
      value: 42.1255
    - type: nauc_recall_at_5_std
      value: 26.890399999999996
    - type: nauc_recall_at_5_diff1
      value: 16.5719
    - type: nauc_recall_at_10_max
      value: 41.8796
    - type: nauc_recall_at_10_std
      value: 35.886
    - type: nauc_recall_at_10_diff1
      value: 9.186900000000001
    - type: nauc_recall_at_20_max
      value: 42.714
    - type: nauc_recall_at_20_std
      value: 38.8114
    - type: nauc_recall_at_20_diff1
      value: 8.1773
    - type: nauc_recall_at_100_max
      value: 46.6919
    - type: nauc_recall_at_100_std
      value: 61.7482
    - type: nauc_recall_at_100_diff1
      value: 3.8259000000000003
    - type: nauc_recall_at_1000_max
      value: 55.9762
    - type: nauc_recall_at_1000_std
      value: 71.4429
    - type: nauc_recall_at_1000_diff1
      value: 1.5741
    - type: nauc_precision_at_1_max
      value: 45.0774
    - type: nauc_precision_at_1_std
      value: 41.1016
    - type: nauc_precision_at_1_diff1
      value: 25.1666
    - type: nauc_precision_at_3_max
      value: 43.3536
    - type: nauc_precision_at_3_std
      value: 45.083400000000005
    - type: nauc_precision_at_3_diff1
      value: 14.815900000000001
    - type: nauc_precision_at_5_max
      value: 48.3736
    - type: nauc_precision_at_5_std
      value: 52.174600000000005
    - type: nauc_precision_at_5_diff1
      value: 12.2844
    - type: nauc_precision_at_10_max
      value: 46.069700000000005
    - type: nauc_precision_at_10_std
      value: 58.0045
    - type: nauc_precision_at_10_diff1
      value: 9.6372
    - type: nauc_precision_at_20_max
      value: 44.2562
    - type: nauc_precision_at_20_std
      value: 61.706799999999994
    - type: nauc_precision_at_20_diff1
      value: 11.1688
    - type: nauc_precision_at_100_max
      value: 34.7099
    - type: nauc_precision_at_100_std
      value: 66.8047
    - type: nauc_precision_at_100_diff1
      value: 5.9025
    - type: nauc_precision_at_1000_max
      value: 11.375300000000001
    - type: nauc_precision_at_1000_std
      value: 40.9784
    - type: nauc_precision_at_1000_diff1
      value: -5.2021
    - type: nauc_mrr_at_1_max
      value: 45.0774
    - type: nauc_mrr_at_1_std
      value: 41.1016
    - type: nauc_mrr_at_1_diff1
      value: 25.1666
    - type: nauc_mrr_at_3_max
      value: 43.3192
    - type: nauc_mrr_at_3_std
      value: 42.6595
    - type: nauc_mrr_at_3_diff1
      value: 19.1777
    - type: nauc_mrr_at_5_max
      value: 46.1263
    - type: nauc_mrr_at_5_std
      value: 45.2286
    - type: nauc_mrr_at_5_diff1
      value: 19.4694
    - type: nauc_mrr_at_10_max
      value: 46.421600000000005
    - type: nauc_mrr_at_10_std
      value: 46.0056
    - type: nauc_mrr_at_10_diff1
      value: 18.924599999999998
    - type: nauc_mrr_at_20_max
      value: 46.7969
    - type: nauc_mrr_at_20_std
      value: 45.9656
    - type: nauc_mrr_at_20_diff1
      value: 19.1375
    - type: nauc_mrr_at_100_max
      value: 46.8001
    - type: nauc_mrr_at_100_std
      value: 45.9121
    - type: nauc_mrr_at_100_diff1
      value: 19.1912
    - type: nauc_mrr_at_1000_max
      value: 46.751
    - type: nauc_mrr_at_1000_std
      value: 45.886500000000005
    - type: nauc_mrr_at_1000_diff1
      value: 19.189500000000002
    - type: main_score
      value: 18.512
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: plastic_surgery
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 26.5
    - type: ndcg_at_3
      value: 23.357
    - type: ndcg_at_5
      value: 23.148
    - type: ndcg_at_10
      value: 24.154
    - type: ndcg_at_20
      value: 25.901000000000003
    - type: ndcg_at_100
      value: 34.075
    - type: ndcg_at_1000
      value: 43.693
    - type: map_at_1
      value: 3.202
    - type: map_at_3
      value: 6.101999999999999
    - type: map_at_5
      value: 7.611999999999999
    - type: map_at_10
      value: 10.245999999999999
    - type: map_at_20
      value: 12.4
    - type: map_at_100
      value: 16.489
    - type: map_at_1000
      value: 18.276
    - type: recall_at_1
      value: 3.202
    - type: recall_at_3
      value: 6.97
    - type: recall_at_5
      value: 9.805
    - type: recall_at_10
      value: 16.884
    - type: recall_at_20
      value: 24.099
    - type: recall_at_100
      value: 48.03
    - type: recall_at_1000
      value: 80.098
    - type: precision_at_1
      value: 32.0
    - type: precision_at_3
      value: 25.833000000000002
    - type: precision_at_5
      value: 23.9
    - type: precision_at_10
      value: 20.599999999999998
    - type: precision_at_20
      value: 16.575
    - type: precision_at_100
      value: 8.290000000000001
    - type: precision_at_1000
      value: 1.73
    - type: mrr_at_1
      value: 32.0
    - type: mrr_at_3
      value: 38.5
    - type: mrr_at_5
      value: 41.025
    - type: mrr_at_10
      value: 42.7242
    - type: mrr_at_20
      value: 43.2621
    - type: mrr_at_100
      value: 43.6464
    - type: mrr_at_1000
      value: 43.684
    - type: nauc_ndcg_at_1_max
      value: 33.564899999999994
    - type: nauc_ndcg_at_1_std
      value: 18.848200000000002
    - type: nauc_ndcg_at_1_diff1
      value: 20.8665
    - type: nauc_ndcg_at_3_max
      value: 38.5293
    - type: nauc_ndcg_at_3_std
      value: 30.883399999999998
    - type: nauc_ndcg_at_3_diff1
      value: 17.0333
    - type: nauc_ndcg_at_5_max
      value: 43.662
    - type: nauc_ndcg_at_5_std
      value: 34.9714
    - type: nauc_ndcg_at_5_diff1
      value: 15.587200000000001
    - type: nauc_ndcg_at_10_max
      value: 49.431999999999995
    - type: nauc_ndcg_at_10_std
      value: 41.0383
    - type: nauc_ndcg_at_10_diff1
      value: 19.7453
    - type: nauc_ndcg_at_20_max
      value: 50.2147
    - type: nauc_ndcg_at_20_std
      value: 45.2975
    - type: nauc_ndcg_at_20_diff1
      value: 21.377499999999998
    - type: nauc_ndcg_at_100_max
      value: 56.59889999999999
    - type: nauc_ndcg_at_100_std
      value: 56.2936
    - type: nauc_ndcg_at_100_diff1
      value: 19.9873
    - type: nauc_ndcg_at_1000_max
      value: 55.2342
    - type: nauc_ndcg_at_1000_std
      value: 57.22390000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 18.0735
    - type: nauc_map_at_1_max
      value: 34.0341
    - type: nauc_map_at_1_std
      value: 5.3872
    - type: nauc_map_at_1_diff1
      value: 38.5789
    - type: nauc_map_at_3_max
      value: 36.638
    - type: nauc_map_at_3_std
      value: 21.882199999999997
    - type: nauc_map_at_3_diff1
      value: 29.220000000000002
    - type: nauc_map_at_5_max
      value: 40.0682
    - type: nauc_map_at_5_std
      value: 25.2585
    - type: nauc_map_at_5_diff1
      value: 25.2411
    - type: nauc_map_at_10_max
      value: 45.246700000000004
    - type: nauc_map_at_10_std
      value: 31.0429
    - type: nauc_map_at_10_diff1
      value: 25.9568
    - type: nauc_map_at_20_max
      value: 45.726
    - type: nauc_map_at_20_std
      value: 35.6744
    - type: nauc_map_at_20_diff1
      value: 24.348200000000002
    - type: nauc_map_at_100_max
      value: 49.9123
    - type: nauc_map_at_100_std
      value: 46.9594
    - type: nauc_map_at_100_diff1
      value: 19.500600000000002
    - type: nauc_map_at_1000_max
      value: 49.6205
    - type: nauc_map_at_1000_std
      value: 49.8661
    - type: nauc_map_at_1000_diff1
      value: 17.8803
    - type: nauc_recall_at_1_max
      value: 34.0341
    - type: nauc_recall_at_1_std
      value: 5.3872
    - type: nauc_recall_at_1_diff1
      value: 38.5789
    - type: nauc_recall_at_3_max
      value: 39.1413
    - type: nauc_recall_at_3_std
      value: 27.670699999999997
    - type: nauc_recall_at_3_diff1
      value: 27.185
    - type: nauc_recall_at_5_max
      value: 41.5029
    - type: nauc_recall_at_5_std
      value: 29.4584
    - type: nauc_recall_at_5_diff1
      value: 23.2386
    - type: nauc_recall_at_10_max
      value: 45.006299999999996
    - type: nauc_recall_at_10_std
      value: 33.4615
    - type: nauc_recall_at_10_diff1
      value: 25.6115
    - type: nauc_recall_at_20_max
      value: 45.466699999999996
    - type: nauc_recall_at_20_std
      value: 41.477000000000004
    - type: nauc_recall_at_20_diff1
      value: 22.309
    - type: nauc_recall_at_100_max
      value: 51.815900000000006
    - type: nauc_recall_at_100_std
      value: 61.633
    - type: nauc_recall_at_100_diff1
      value: 15.5623
    - type: nauc_recall_at_1000_max
      value: 69.5645
    - type: nauc_recall_at_1000_std
      value: 76.03370000000001
    - type: nauc_recall_at_1000_diff1
      value: 18.5411
    - type: nauc_precision_at_1_max
      value: 33.3284
    - type: nauc_precision_at_1_std
      value: 20.809
    - type: nauc_precision_at_1_diff1
      value: 17.3773
    - type: nauc_precision_at_3_max
      value: 38.0662
    - type: nauc_precision_at_3_std
      value: 37.0294
    - type: nauc_precision_at_3_diff1
      value: 10.726700000000001
    - type: nauc_precision_at_5_max
      value: 42.142
    - type: nauc_precision_at_5_std
      value: 40.913199999999996
    - type: nauc_precision_at_5_diff1
      value: 6.334
    - type: nauc_precision_at_10_max
      value: 45.536
    - type: nauc_precision_at_10_std
      value: 46.061800000000005
    - type: nauc_precision_at_10_diff1
      value: 9.435
    - type: nauc_precision_at_20_max
      value: 39.5048
    - type: nauc_precision_at_20_std
      value: 49.370799999999996
    - type: nauc_precision_at_20_diff1
      value: 4.9357999999999995
    - type: nauc_precision_at_100_max
      value: 29.158800000000003
    - type: nauc_precision_at_100_std
      value: 50.5371
    - type: nauc_precision_at_100_diff1
      value: -5.7985
    - type: nauc_precision_at_1000_max
      value: -3.2552
    - type: nauc_precision_at_1000_std
      value: 21.9283
    - type: nauc_precision_at_1000_diff1
      value: -13.078699999999998
    - type: nauc_mrr_at_1_max
      value: 33.3284
    - type: nauc_mrr_at_1_std
      value: 20.809
    - type: nauc_mrr_at_1_diff1
      value: 17.3773
    - type: nauc_mrr_at_3_max
      value: 39.1492
    - type: nauc_mrr_at_3_std
      value: 31.512400000000003
    - type: nauc_mrr_at_3_diff1
      value: 15.7237
    - type: nauc_mrr_at_5_max
      value: 40.6122
    - type: nauc_mrr_at_5_std
      value: 33.4723
    - type: nauc_mrr_at_5_diff1
      value: 16.361600000000003
    - type: nauc_mrr_at_10_max
      value: 41.0804
    - type: nauc_mrr_at_10_std
      value: 33.3934
    - type: nauc_mrr_at_10_diff1
      value: 17.163800000000002
    - type: nauc_mrr_at_20_max
      value: 41.3014
    - type: nauc_mrr_at_20_std
      value: 33.826299999999996
    - type: nauc_mrr_at_20_diff1
      value: 17.3245
    - type: nauc_mrr_at_100_max
      value: 40.9816
    - type: nauc_mrr_at_100_std
      value: 33.4721
    - type: nauc_mrr_at_100_diff1
      value: 17.1153
    - type: nauc_mrr_at_1000_max
      value: 40.941
    - type: nauc_mrr_at_1000_std
      value: 33.4166
    - type: nauc_mrr_at_1000_diff1
      value: 17.0834
    - type: main_score
      value: 24.154
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: psychiatry_and_psychology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 62.25000000000001
    - type: ndcg_at_3
      value: 56.178
    - type: ndcg_at_5
      value: 55.35600000000001
    - type: ndcg_at_10
      value: 53.787
    - type: ndcg_at_20
      value: 54.425999999999995
    - type: ndcg_at_100
      value: 61.51
    - type: ndcg_at_1000
      value: 69.59100000000001
    - type: map_at_1
      value: 6.508
    - type: map_at_3
      value: 11.125
    - type: map_at_5
      value: 14.84
    - type: map_at_10
      value: 20.191
    - type: map_at_20
      value: 26.150000000000002
    - type: map_at_100
      value: 37.021
    - type: map_at_1000
      value: 42.846000000000004
    - type: recall_at_1
      value: 6.508
    - type: recall_at_3
      value: 12.055
    - type: recall_at_5
      value: 17.66
    - type: recall_at_10
      value: 26.485999999999997
    - type: recall_at_20
      value: 38.799
    - type: recall_at_100
      value: 68.774
    - type: recall_at_1000
      value: 93.62899999999999
    - type: precision_at_1
      value: 75.5
    - type: precision_at_3
      value: 64.667
    - type: precision_at_5
      value: 61.1
    - type: precision_at_10
      value: 52.6
    - type: precision_at_20
      value: 44.3
    - type: precision_at_100
      value: 23.735
    - type: precision_at_1000
      value: 5.314
    - type: mrr_at_1
      value: 75.5
    - type: mrr_at_3
      value: 80.8333
    - type: mrr_at_5
      value: 82.1833
    - type: mrr_at_10
      value: 82.6575
    - type: mrr_at_20
      value: 82.7818
    - type: mrr_at_100
      value: 82.8156
    - type: mrr_at_1000
      value: 82.8179
    - type: nauc_ndcg_at_1_max
      value: 29.204200000000004
    - type: nauc_ndcg_at_1_std
      value: 5.5276
    - type: nauc_ndcg_at_1_diff1
      value: 44.7735
    - type: nauc_ndcg_at_3_max
      value: 39.7652
    - type: nauc_ndcg_at_3_std
      value: 12.5479
    - type: nauc_ndcg_at_3_diff1
      value: 37.257200000000005
    - type: nauc_ndcg_at_5_max
      value: 38.7411
    - type: nauc_ndcg_at_5_std
      value: 17.310200000000002
    - type: nauc_ndcg_at_5_diff1
      value: 38.327600000000004
    - type: nauc_ndcg_at_10_max
      value: 39.135799999999996
    - type: nauc_ndcg_at_10_std
      value: 22.9689
    - type: nauc_ndcg_at_10_diff1
      value: 36.9699
    - type: nauc_ndcg_at_20_max
      value: 39.9846
    - type: nauc_ndcg_at_20_std
      value: 25.7726
    - type: nauc_ndcg_at_20_diff1
      value: 35.3069
    - type: nauc_ndcg_at_100_max
      value: 46.7474
    - type: nauc_ndcg_at_100_std
      value: 40.069700000000005
    - type: nauc_ndcg_at_100_diff1
      value: 29.802
    - type: nauc_ndcg_at_1000_max
      value: 52.6498
    - type: nauc_ndcg_at_1000_std
      value: 42.8565
    - type: nauc_ndcg_at_1000_diff1
      value: 35.4601
    - type: nauc_map_at_1_max
      value: -16.932
    - type: nauc_map_at_1_std
      value: -17.021
    - type: nauc_map_at_1_diff1
      value: 52.6778
    - type: nauc_map_at_3_max
      value: -1.1856
    - type: nauc_map_at_3_std
      value: -6.725299999999999
    - type: nauc_map_at_3_diff1
      value: 39.343
    - type: nauc_map_at_5_max
      value: 4.2418
    - type: nauc_map_at_5_std
      value: -0.39569999999999994
    - type: nauc_map_at_5_diff1
      value: 32.5041
    - type: nauc_map_at_10_max
      value: 13.7455
    - type: nauc_map_at_10_std
      value: 7.9563999999999995
    - type: nauc_map_at_10_diff1
      value: 27.549699999999998
    - type: nauc_map_at_20_max
      value: 20.1616
    - type: nauc_map_at_20_std
      value: 15.3559
    - type: nauc_map_at_20_diff1
      value: 24.5985
    - type: nauc_map_at_100_max
      value: 35.7109
    - type: nauc_map_at_100_std
      value: 35.8448
    - type: nauc_map_at_100_diff1
      value: 22.9314
    - type: nauc_map_at_1000_max
      value: 40.5827
    - type: nauc_map_at_1000_std
      value: 40.516999999999996
    - type: nauc_map_at_1000_diff1
      value: 21.8728
    - type: nauc_recall_at_1_max
      value: -16.932
    - type: nauc_recall_at_1_std
      value: -17.021
    - type: nauc_recall_at_1_diff1
      value: 52.6778
    - type: nauc_recall_at_3_max
      value: -1.6465
    - type: nauc_recall_at_3_std
      value: -4.1869000000000005
    - type: nauc_recall_at_3_diff1
      value: 36.6417
    - type: nauc_recall_at_5_max
      value: -1.897
    - type: nauc_recall_at_5_std
      value: -1.6251000000000002
    - type: nauc_recall_at_5_diff1
      value: 26.605
    - type: nauc_recall_at_10_max
      value: 3.3542
    - type: nauc_recall_at_10_std
      value: 2.3941
    - type: nauc_recall_at_10_diff1
      value: 21.5494
    - type: nauc_recall_at_20_max
      value: 6.8939
    - type: nauc_recall_at_20_std
      value: 6.0322000000000005
    - type: nauc_recall_at_20_diff1
      value: 15.322700000000001
    - type: nauc_recall_at_100_max
      value: 22.0212
    - type: nauc_recall_at_100_std
      value: 35.032000000000004
    - type: nauc_recall_at_100_diff1
      value: 12.5475
    - type: nauc_recall_at_1000_max
      value: 41.3636
    - type: nauc_recall_at_1000_std
      value: 61.2891
    - type: nauc_recall_at_1000_diff1
      value: 25.154700000000002
    - type: nauc_precision_at_1_max
      value: 39.4009
    - type: nauc_precision_at_1_std
      value: 13.0772
    - type: nauc_precision_at_1_diff1
      value: 44.709199999999996
    - type: nauc_precision_at_3_max
      value: 45.9236
    - type: nauc_precision_at_3_std
      value: 23.3125
    - type: nauc_precision_at_3_diff1
      value: 12.0883
    - type: nauc_precision_at_5_max
      value: 39.2342
    - type: nauc_precision_at_5_std
      value: 27.9706
    - type: nauc_precision_at_5_diff1
      value: 6.1063
    - type: nauc_precision_at_10_max
      value: 36.578500000000005
    - type: nauc_precision_at_10_std
      value: 30.2286
    - type: nauc_precision_at_10_diff1
      value: 0.212
    - type: nauc_precision_at_20_max
      value: 31.939899999999998
    - type: nauc_precision_at_20_std
      value: 29.0114
    - type: nauc_precision_at_20_diff1
      value: -1.5977000000000001
    - type: nauc_precision_at_100_max
      value: 17.9772
    - type: nauc_precision_at_100_std
      value: 19.254199999999997
    - type: nauc_precision_at_100_diff1
      value: -8.297400000000001
    - type: nauc_precision_at_1000_max
      value: 1.124
    - type: nauc_precision_at_1000_std
      value: -3.2368
    - type: nauc_precision_at_1000_diff1
      value: -11.5367
    - type: nauc_mrr_at_1_max
      value: 39.4009
    - type: nauc_mrr_at_1_std
      value: 13.0772
    - type: nauc_mrr_at_1_diff1
      value: 44.709199999999996
    - type: nauc_mrr_at_3_max
      value: 47.9986
    - type: nauc_mrr_at_3_std
      value: 22.703200000000002
    - type: nauc_mrr_at_3_diff1
      value: 48.8416
    - type: nauc_mrr_at_5_max
      value: 46.2575
    - type: nauc_mrr_at_5_std
      value: 21.3868
    - type: nauc_mrr_at_5_diff1
      value: 48.9122
    - type: nauc_mrr_at_10_max
      value: 46.3047
    - type: nauc_mrr_at_10_std
      value: 21.0973
    - type: nauc_mrr_at_10_diff1
      value: 48.5351
    - type: nauc_mrr_at_20_max
      value: 46.056000000000004
    - type: nauc_mrr_at_20_std
      value: 20.9263
    - type: nauc_mrr_at_20_diff1
      value: 48.5802
    - type: nauc_mrr_at_100_max
      value: 46.0327
    - type: nauc_mrr_at_100_std
      value: 20.9821
    - type: nauc_mrr_at_100_diff1
      value: 48.5011
    - type: nauc_mrr_at_1000_max
      value: 46.0251
    - type: nauc_mrr_at_1000_std
      value: 20.9709
    - type: nauc_mrr_at_1000_diff1
      value: 48.4956
    - type: main_score
      value: 53.787
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: psychiatry_and_psychology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 15.25
    - type: ndcg_at_3
      value: 16.503999999999998
    - type: ndcg_at_5
      value: 17.229
    - type: ndcg_at_10
      value: 18.285
    - type: ndcg_at_20
      value: 20.498
    - type: ndcg_at_100
      value: 28.155
    - type: ndcg_at_1000
      value: 39.995999999999995
    - type: map_at_1
      value: 1.691
    - type: map_at_3
      value: 3.596
    - type: map_at_5
      value: 4.546
    - type: map_at_10
      value: 6.461
    - type: map_at_20
      value: 8.507000000000001
    - type: map_at_100
      value: 12.629999999999999
    - type: map_at_1000
      value: 16.005
    - type: recall_at_1
      value: 1.691
    - type: recall_at_3
      value: 4.661
    - type: recall_at_5
      value: 6.413
    - type: recall_at_10
      value: 11.055
    - type: recall_at_20
      value: 17.264
    - type: recall_at_100
      value: 39.257
    - type: recall_at_1000
      value: 73.616
    - type: precision_at_1
      value: 19.5
    - type: precision_at_3
      value: 21.5
    - type: precision_at_5
      value: 21.2
    - type: precision_at_10
      value: 19.8
    - type: precision_at_20
      value: 18.7
    - type: precision_at_100
      value: 11.97
    - type: precision_at_1000
      value: 3.6639999999999997
    - type: mrr_at_1
      value: 19.5
    - type: mrr_at_3
      value: 28.4167
    - type: mrr_at_5
      value: 30.3667
    - type: mrr_at_10
      value: 32.1278
    - type: mrr_at_20
      value: 33.194
    - type: mrr_at_100
      value: 33.679500000000004
    - type: mrr_at_1000
      value: 33.7017
    - type: nauc_ndcg_at_1_max
      value: 8.3704
    - type: nauc_ndcg_at_1_std
      value: 35.2143
    - type: nauc_ndcg_at_1_diff1
      value: 3.4162999999999997
    - type: nauc_ndcg_at_3_max
      value: 10.3469
    - type: nauc_ndcg_at_3_std
      value: 35.4444
    - type: nauc_ndcg_at_3_diff1
      value: -1.7632999999999999
    - type: nauc_ndcg_at_5_max
      value: 9.8734
    - type: nauc_ndcg_at_5_std
      value: 34.4609
    - type: nauc_ndcg_at_5_diff1
      value: -3.7905
    - type: nauc_ndcg_at_10_max
      value: 10.8117
    - type: nauc_ndcg_at_10_std
      value: 38.156400000000005
    - type: nauc_ndcg_at_10_diff1
      value: -2.3385
    - type: nauc_ndcg_at_20_max
      value: 14.477100000000002
    - type: nauc_ndcg_at_20_std
      value: 41.1031
    - type: nauc_ndcg_at_20_diff1
      value: -4.7229
    - type: nauc_ndcg_at_100_max
      value: 23.9752
    - type: nauc_ndcg_at_100_std
      value: 54.198299999999996
    - type: nauc_ndcg_at_100_diff1
      value: 0.47939999999999994
    - type: nauc_ndcg_at_1000_max
      value: 31.2555
    - type: nauc_ndcg_at_1000_std
      value: 56.81420000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 0.7486999999999999
    - type: nauc_map_at_1_max
      value: 5.1724
    - type: nauc_map_at_1_std
      value: 37.5486
    - type: nauc_map_at_1_diff1
      value: 28.0577
    - type: nauc_map_at_3_max
      value: 6.870900000000001
    - type: nauc_map_at_3_std
      value: 35.1499
    - type: nauc_map_at_3_diff1
      value: 16.5024
    - type: nauc_map_at_5_max
      value: 5.1497
    - type: nauc_map_at_5_std
      value: 33.9484
    - type: nauc_map_at_5_diff1
      value: 9.6245
    - type: nauc_map_at_10_max
      value: 2.4238
    - type: nauc_map_at_10_std
      value: 34.7536
    - type: nauc_map_at_10_diff1
      value: 2.4971
    - type: nauc_map_at_20_max
      value: 4.6439
    - type: nauc_map_at_20_std
      value: 36.771300000000004
    - type: nauc_map_at_20_diff1
      value: -1.6913
    - type: nauc_map_at_100_max
      value: 13.689200000000001
    - type: nauc_map_at_100_std
      value: 46.6883
    - type: nauc_map_at_100_diff1
      value: -0.9819
    - type: nauc_map_at_1000_max
      value: 19.6067
    - type: nauc_map_at_1000_std
      value: 50.14809999999999
    - type: nauc_map_at_1000_diff1
      value: 0.21389999999999998
    - type: nauc_recall_at_1_max
      value: 5.1724
    - type: nauc_recall_at_1_std
      value: 37.5486
    - type: nauc_recall_at_1_diff1
      value: 28.0577
    - type: nauc_recall_at_3_max
      value: 4.0584
    - type: nauc_recall_at_3_std
      value: 32.493100000000005
    - type: nauc_recall_at_3_diff1
      value: 13.8324
    - type: nauc_recall_at_5_max
      value: 0.9519
    - type: nauc_recall_at_5_std
      value: 29.073999999999998
    - type: nauc_recall_at_5_diff1
      value: 4.2552
    - type: nauc_recall_at_10_max
      value: -1.1522
    - type: nauc_recall_at_10_std
      value: 30.8215
    - type: nauc_recall_at_10_diff1
      value: -0.7575000000000001
    - type: nauc_recall_at_20_max
      value: 4.0141
    - type: nauc_recall_at_20_std
      value: 34.6209
    - type: nauc_recall_at_20_diff1
      value: -4.9465
    - type: nauc_recall_at_100_max
      value: 19.0596
    - type: nauc_recall_at_100_std
      value: 53.043099999999995
    - type: nauc_recall_at_100_diff1
      value: -0.4443
    - type: nauc_recall_at_1000_max
      value: 40.3603
    - type: nauc_recall_at_1000_std
      value: 66.3722
    - type: nauc_recall_at_1000_diff1
      value: -5.2899
    - type: nauc_precision_at_1_max
      value: 15.3147
    - type: nauc_precision_at_1_std
      value: 38.4547
    - type: nauc_precision_at_1_diff1
      value: 5.2894
    - type: nauc_precision_at_3_max
      value: 13.0357
    - type: nauc_precision_at_3_std
      value: 34.6165
    - type: nauc_precision_at_3_diff1
      value: -6.7761000000000005
    - type: nauc_precision_at_5_max
      value: 10.3074
    - type: nauc_precision_at_5_std
      value: 31.929000000000002
    - type: nauc_precision_at_5_diff1
      value: -11.0482
    - type: nauc_precision_at_10_max
      value: 12.5554
    - type: nauc_precision_at_10_std
      value: 35.6601
    - type: nauc_precision_at_10_diff1
      value: -9.7417
    - type: nauc_precision_at_20_max
      value: 18.0836
    - type: nauc_precision_at_20_std
      value: 35.891
    - type: nauc_precision_at_20_diff1
      value: -11.1218
    - type: nauc_precision_at_100_max
      value: 26.936799999999998
    - type: nauc_precision_at_100_std
      value: 36.4249
    - type: nauc_precision_at_100_diff1
      value: -0.5038
    - type: nauc_precision_at_1000_max
      value: 16.145899999999997
    - type: nauc_precision_at_1000_std
      value: 8.6919
    - type: nauc_precision_at_1000_diff1
      value: 1.8063
    - type: nauc_mrr_at_1_max
      value: 15.3147
    - type: nauc_mrr_at_1_std
      value: 38.4547
    - type: nauc_mrr_at_1_diff1
      value: 5.2894
    - type: nauc_mrr_at_3_max
      value: 14.596899999999998
    - type: nauc_mrr_at_3_std
      value: 38.254599999999996
    - type: nauc_mrr_at_3_diff1
      value: 3.8059000000000003
    - type: nauc_mrr_at_5_max
      value: 13.7185
    - type: nauc_mrr_at_5_std
      value: 38.0272
    - type: nauc_mrr_at_5_diff1
      value: 2.6057
    - type: nauc_mrr_at_10_max
      value: 15.759300000000001
    - type: nauc_mrr_at_10_std
      value: 38.3291
    - type: nauc_mrr_at_10_diff1
      value: 4.0205
    - type: nauc_mrr_at_20_max
      value: 16.0776
    - type: nauc_mrr_at_20_std
      value: 38.6794
    - type: nauc_mrr_at_20_diff1
      value: 3.9222
    - type: nauc_mrr_at_100_max
      value: 16.1438
    - type: nauc_mrr_at_100_std
      value: 39.0121
    - type: nauc_mrr_at_100_diff1
      value: 4.0474000000000006
    - type: nauc_mrr_at_1000_max
      value: 16.1074
    - type: nauc_mrr_at_1000_std
      value: 38.9799
    - type: nauc_mrr_at_1000_diff1
      value: 4.018800000000001
    - type: main_score
      value: 18.285
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: psychiatry_and_psychology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 34.5
    - type: ndcg_at_3
      value: 31.302999999999997
    - type: ndcg_at_5
      value: 30.329
    - type: ndcg_at_10
      value: 30.092000000000002
    - type: ndcg_at_20
      value: 31.141000000000002
    - type: ndcg_at_100
      value: 38.452
    - type: ndcg_at_1000
      value: 49.441
    - type: map_at_1
      value: 3.762
    - type: map_at_3
      value: 6.194
    - type: map_at_5
      value: 7.827000000000001
    - type: map_at_10
      value: 10.530000000000001
    - type: map_at_20
      value: 13.624
    - type: map_at_100
      value: 19.580000000000002
    - type: map_at_1000
      value: 23.517
    - type: recall_at_1
      value: 3.762
    - type: recall_at_3
      value: 6.935
    - type: recall_at_5
      value: 9.469
    - type: recall_at_10
      value: 14.774999999999999
    - type: recall_at_20
      value: 23.272000000000002
    - type: recall_at_100
      value: 47.899
    - type: recall_at_1000
      value: 79.336
    - type: precision_at_1
      value: 45.0
    - type: precision_at_3
      value: 37.5
    - type: precision_at_5
      value: 34.5
    - type: precision_at_10
      value: 30.65
    - type: precision_at_20
      value: 26.125
    - type: precision_at_100
      value: 14.75
    - type: precision_at_1000
      value: 4.055000000000001
    - type: mrr_at_1
      value: 45.0
    - type: mrr_at_3
      value: 53.41669999999999
    - type: mrr_at_5
      value: 54.8167
    - type: mrr_at_10
      value: 56.003400000000006
    - type: mrr_at_20
      value: 56.599900000000005
    - type: mrr_at_100
      value: 56.8053
    - type: mrr_at_1000
      value: 56.8178
    - type: nauc_ndcg_at_1_max
      value: 21.7329
    - type: nauc_ndcg_at_1_std
      value: 28.6663
    - type: nauc_ndcg_at_1_diff1
      value: 21.7183
    - type: nauc_ndcg_at_3_max
      value: 33.7072
    - type: nauc_ndcg_at_3_std
      value: 35.4064
    - type: nauc_ndcg_at_3_diff1
      value: 20.9404
    - type: nauc_ndcg_at_5_max
      value: 36.1588
    - type: nauc_ndcg_at_5_std
      value: 41.077799999999996
    - type: nauc_ndcg_at_5_diff1
      value: 18.8722
    - type: nauc_ndcg_at_10_max
      value: 36.8808
    - type: nauc_ndcg_at_10_std
      value: 42.6325
    - type: nauc_ndcg_at_10_diff1
      value: 17.203
    - type: nauc_ndcg_at_20_max
      value: 40.5287
    - type: nauc_ndcg_at_20_std
      value: 48.8626
    - type: nauc_ndcg_at_20_diff1
      value: 12.2369
    - type: nauc_ndcg_at_100_max
      value: 52.285000000000004
    - type: nauc_ndcg_at_100_std
      value: 62.0211
    - type: nauc_ndcg_at_100_diff1
      value: 7.3617
    - type: nauc_ndcg_at_1000_max
      value: 52.5857
    - type: nauc_ndcg_at_1000_std
      value: 64.48270000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 11.462
    - type: nauc_map_at_1_max
      value: -4.9144
    - type: nauc_map_at_1_std
      value: 9.7903
    - type: nauc_map_at_1_diff1
      value: 31.9263
    - type: nauc_map_at_3_max
      value: 11.4121
    - type: nauc_map_at_3_std
      value: 20.4973
    - type: nauc_map_at_3_diff1
      value: 22.2687
    - type: nauc_map_at_5_max
      value: 18.5748
    - type: nauc_map_at_5_std
      value: 27.561799999999998
    - type: nauc_map_at_5_diff1
      value: 17.8388
    - type: nauc_map_at_10_max
      value: 27.125799999999998
    - type: nauc_map_at_10_std
      value: 33.840399999999995
    - type: nauc_map_at_10_diff1
      value: 12.963099999999999
    - type: nauc_map_at_20_max
      value: 33.469500000000004
    - type: nauc_map_at_20_std
      value: 40.9153
    - type: nauc_map_at_20_diff1
      value: 10.1626
    - type: nauc_map_at_100_max
      value: 47.2695
    - type: nauc_map_at_100_std
      value: 56.0531
    - type: nauc_map_at_100_diff1
      value: 8.020199999999999
    - type: nauc_map_at_1000_max
      value: 47.847899999999996
    - type: nauc_map_at_1000_std
      value: 58.7227
    - type: nauc_map_at_1000_diff1
      value: 8.697199999999999
    - type: nauc_recall_at_1_max
      value: -4.9144
    - type: nauc_recall_at_1_std
      value: 9.7903
    - type: nauc_recall_at_1_diff1
      value: 31.9263
    - type: nauc_recall_at_3_max
      value: 11.7904
    - type: nauc_recall_at_3_std
      value: 21.4997
    - type: nauc_recall_at_3_diff1
      value: 19.6193
    - type: nauc_recall_at_5_max
      value: 19.039900000000003
    - type: nauc_recall_at_5_std
      value: 29.3609
    - type: nauc_recall_at_5_diff1
      value: 13.7371
    - type: nauc_recall_at_10_max
      value: 25.318800000000003
    - type: nauc_recall_at_10_std
      value: 30.9394
    - type: nauc_recall_at_10_diff1
      value: 7.7126
    - type: nauc_recall_at_20_max
      value: 31.7363
    - type: nauc_recall_at_20_std
      value: 41.167300000000004
    - type: nauc_recall_at_20_diff1
      value: 1.2625000000000002
    - type: nauc_recall_at_100_max
      value: 49.5017
    - type: nauc_recall_at_100_std
      value: 62.5455
    - type: nauc_recall_at_100_diff1
      value: -6.0973
    - type: nauc_recall_at_1000_max
      value: 62.021800000000006
    - type: nauc_recall_at_1000_std
      value: 82.6167
    - type: nauc_recall_at_1000_diff1
      value: -7.6475
    - type: nauc_precision_at_1_max
      value: 24.5636
    - type: nauc_precision_at_1_std
      value: 30.032700000000002
    - type: nauc_precision_at_1_diff1
      value: 20.9605
    - type: nauc_precision_at_3_max
      value: 38.6768
    - type: nauc_precision_at_3_std
      value: 36.7568
    - type: nauc_precision_at_3_diff1
      value: 13.77
    - type: nauc_precision_at_5_max
      value: 40.002900000000004
    - type: nauc_precision_at_5_std
      value: 43.7761
    - type: nauc_precision_at_5_diff1
      value: 9.8675
    - type: nauc_precision_at_10_max
      value: 39.5
    - type: nauc_precision_at_10_std
      value: 43.282900000000005
    - type: nauc_precision_at_10_diff1
      value: 8.8047
    - type: nauc_precision_at_20_max
      value: 38.8534
    - type: nauc_precision_at_20_std
      value: 43.6591
    - type: nauc_precision_at_20_diff1
      value: 3.0647
    - type: nauc_precision_at_100_max
      value: 28.808600000000002
    - type: nauc_precision_at_100_std
      value: 34.5524
    - type: nauc_precision_at_100_diff1
      value: 2.9145
    - type: nauc_precision_at_1000_max
      value: 0.8090999999999999
    - type: nauc_precision_at_1000_std
      value: 3.0013
    - type: nauc_precision_at_1000_diff1
      value: 12.712499999999999
    - type: nauc_mrr_at_1_max
      value: 24.5636
    - type: nauc_mrr_at_1_std
      value: 30.032700000000002
    - type: nauc_mrr_at_1_diff1
      value: 20.9605
    - type: nauc_mrr_at_3_max
      value: 29.911199999999997
    - type: nauc_mrr_at_3_std
      value: 36.0742
    - type: nauc_mrr_at_3_diff1
      value: 22.6104
    - type: nauc_mrr_at_5_max
      value: 29.8299
    - type: nauc_mrr_at_5_std
      value: 36.584
    - type: nauc_mrr_at_5_diff1
      value: 22.5318
    - type: nauc_mrr_at_10_max
      value: 29.4982
    - type: nauc_mrr_at_10_std
      value: 35.9069
    - type: nauc_mrr_at_10_diff1
      value: 22.4779
    - type: nauc_mrr_at_20_max
      value: 29.834600000000002
    - type: nauc_mrr_at_20_std
      value: 36.0663
    - type: nauc_mrr_at_20_diff1
      value: 22.4151
    - type: nauc_mrr_at_100_max
      value: 29.674699999999998
    - type: nauc_mrr_at_100_std
      value: 35.988
    - type: nauc_mrr_at_100_diff1
      value: 22.2975
    - type: nauc_mrr_at_1000_max
      value: 29.6539
    - type: nauc_mrr_at_1000_std
      value: 35.9683
    - type: nauc_mrr_at_1000_diff1
      value: 22.3039
    - type: main_score
      value: 30.092000000000002
    task:
      type: Retrieval
  - dataset:
      config: en
      name: MTEB CUREv1 (en)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: pulmonology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 64.0
    - type: ndcg_at_3
      value: 57.730000000000004
    - type: ndcg_at_5
      value: 56.537000000000006
    - type: ndcg_at_10
      value: 55.355
    - type: ndcg_at_20
      value: 56.119
    - type: ndcg_at_100
      value: 62.271
    - type: ndcg_at_1000
      value: 70.458
    - type: map_at_1
      value: 12.120000000000001
    - type: map_at_3
      value: 19.903000000000002
    - type: map_at_5
      value: 23.996000000000002
    - type: map_at_10
      value: 28.767
    - type: map_at_20
      value: 32.574999999999996
    - type: map_at_100
      value: 39.367999999999995
    - type: map_at_1000
      value: 43.169999999999995
    - type: recall_at_1
      value: 12.120000000000001
    - type: recall_at_3
      value: 21.934
    - type: recall_at_5
      value: 28.09
    - type: recall_at_10
      value: 36.939
    - type: recall_at_20
      value: 46.831
    - type: recall_at_100
      value: 71.05900000000001
    - type: recall_at_1000
      value: 95.543
    - type: precision_at_1
      value: 73.5
    - type: precision_at_3
      value: 57.667
    - type: precision_at_5
      value: 51.1
    - type: precision_at_10
      value: 40.400000000000006
    - type: precision_at_20
      value: 30.925000000000004
    - type: precision_at_100
      value: 15.310000000000002
    - type: precision_at_1000
      value: 3.4299999999999997
    - type: mrr_at_1
      value: 73.5
    - type: mrr_at_3
      value: 80.91669999999999
    - type: mrr_at_5
      value: 82.36670000000001
    - type: mrr_at_10
      value: 82.6792
    - type: mrr_at_20
      value: 82.8638
    - type: mrr_at_100
      value: 82.8638
    - type: mrr_at_1000
      value: 82.8638
    - type: nauc_ndcg_at_1_max
      value: 52.9944
    - type: nauc_ndcg_at_1_std
      value: 10.6488
    - type: nauc_ndcg_at_1_diff1
      value: 56.655199999999994
    - type: nauc_ndcg_at_3_max
      value: 51.953
    - type: nauc_ndcg_at_3_std
      value: 13.8674
    - type: nauc_ndcg_at_3_diff1
      value: 40.9794
    - type: nauc_ndcg_at_5_max
      value: 50.5956
    - type: nauc_ndcg_at_5_std
      value: 14.1906
    - type: nauc_ndcg_at_5_diff1
      value: 39.0879
    - type: nauc_ndcg_at_10_max
      value: 46.3615
    - type: nauc_ndcg_at_10_std
      value: 17.5279
    - type: nauc_ndcg_at_10_diff1
      value: 35.3915
    - type: nauc_ndcg_at_20_max
      value: 45.8408
    - type: nauc_ndcg_at_20_std
      value: 14.768500000000001
    - type: nauc_ndcg_at_20_diff1
      value: 37.9504
    - type: nauc_ndcg_at_100_max
      value: 51.45269999999999
    - type: nauc_ndcg_at_100_std
      value: 25.4131
    - type: nauc_ndcg_at_100_diff1
      value: 41.646699999999996
    - type: nauc_ndcg_at_1000_max
      value: 53.3425
    - type: nauc_ndcg_at_1000_std
      value: 26.118599999999997
    - type: nauc_ndcg_at_1000_diff1
      value: 39.6503
    - type: nauc_map_at_1_max
      value: 25.144899999999996
    - type: nauc_map_at_1_std
      value: 6.5377
    - type: nauc_map_at_1_diff1
      value: 55.247
    - type: nauc_map_at_3_max
      value: 29.1222
    - type: nauc_map_at_3_std
      value: 12.2911
    - type: nauc_map_at_3_diff1
      value: 44.0726
    - type: nauc_map_at_5_max
      value: 31.3535
    - type: nauc_map_at_5_std
      value: 14.696200000000001
    - type: nauc_map_at_5_diff1
      value: 38.48
    - type: nauc_map_at_10_max
      value: 33.285
    - type: nauc_map_at_10_std
      value: 16.5916
    - type: nauc_map_at_10_diff1
      value: 33.197700000000005
    - type: nauc_map_at_20_max
      value: 35.9366
    - type: nauc_map_at_20_std
      value: 16.9539
    - type: nauc_map_at_20_diff1
      value: 33.4713
    - type: nauc_map_at_100_max
      value: 39.4216
    - type: nauc_map_at_100_std
      value: 23.5005
    - type: nauc_map_at_100_diff1
      value: 32.3674
    - type: nauc_map_at_1000_max
      value: 38.9144
    - type: nauc_map_at_1000_std
      value: 22.9379
    - type: nauc_map_at_1000_diff1
      value: 29.9875
    - type: nauc_recall_at_1_max
      value: 25.144899999999996
    - type: nauc_recall_at_1_std
      value: 6.5377
    - type: nauc_recall_at_1_diff1
      value: 55.247
    - type: nauc_recall_at_3_max
      value: 24.9541
    - type: nauc_recall_at_3_std
      value: 12.2005
    - type: nauc_recall_at_3_diff1
      value: 39.8432
    - type: nauc_recall_at_5_max
      value: 26.035000000000004
    - type: nauc_recall_at_5_std
      value: 15.7753
    - type: nauc_recall_at_5_diff1
      value: 33.602900000000005
    - type: nauc_recall_at_10_max
      value: 29.224099999999996
    - type: nauc_recall_at_10_std
      value: 16.9009
    - type: nauc_recall_at_10_diff1
      value: 27.7753
    - type: nauc_recall_at_20_max
      value: 30.2261
    - type: nauc_recall_at_20_std
      value: 14.480599999999999
    - type: nauc_recall_at_20_diff1
      value: 29.133599999999998
    - type: nauc_recall_at_100_max
      value: 38.1305
    - type: nauc_recall_at_100_std
      value: 31.1575
    - type: nauc_recall_at_100_diff1
      value: 35.969
    - type: nauc_recall_at_1000_max
      value: 58.8372
    - type: nauc_recall_at_1000_std
      value: 76.1479
    - type: nauc_recall_at_1000_diff1
      value: 36.6072
    - type: nauc_precision_at_1_max
      value: 57.537099999999995
    - type: nauc_precision_at_1_std
      value: 15.8427
    - type: nauc_precision_at_1_diff1
      value: 50.3828
    - type: nauc_precision_at_3_max
      value: 33.5024
    - type: nauc_precision_at_3_std
      value: 11.182699999999999
    - type: nauc_precision_at_3_diff1
      value: -0.21960000000000002
    - type: nauc_precision_at_5_max
      value: 24.208199999999998
    - type: nauc_precision_at_5_std
      value: 7.292
    - type: nauc_precision_at_5_diff1
      value: -9.8187
    - type: nauc_precision_at_10_max
      value: 11.2527
    - type: nauc_precision_at_10_std
      value: 5.273
    - type: nauc_precision_at_10_diff1
      value: -20.255300000000002
    - type: nauc_precision_at_20_max
      value: 4.5758
    - type: nauc_precision_at_20_std
      value: 1.9272999999999998
    - type: nauc_precision_at_20_diff1
      value: -18.9272
    - type: nauc_precision_at_100_max
      value: -6.4853
    - type: nauc_precision_at_100_std
      value: -0.35729999999999995
    - type: nauc_precision_at_100_diff1
      value: -19.8495
    - type: nauc_precision_at_1000_max
      value: -15.5076
    - type: nauc_precision_at_1000_std
      value: -19.7998
    - type: nauc_precision_at_1000_diff1
      value: -23.3793
    - type: nauc_mrr_at_1_max
      value: 57.537099999999995
    - type: nauc_mrr_at_1_std
      value: 15.8427
    - type: nauc_mrr_at_1_diff1
      value: 50.3828
    - type: nauc_mrr_at_3_max
      value: 60.519400000000005
    - type: nauc_mrr_at_3_std
      value: 25.4011
    - type: nauc_mrr_at_3_diff1
      value: 47.106700000000004
    - type: nauc_mrr_at_5_max
      value: 59.9727
    - type: nauc_mrr_at_5_std
      value: 23.0994
    - type: nauc_mrr_at_5_diff1
      value: 46.9457
    - type: nauc_mrr_at_10_max
      value: 59.78869999999999
    - type: nauc_mrr_at_10_std
      value: 22.3365
    - type: nauc_mrr_at_10_diff1
      value: 46.8909
    - type: nauc_mrr_at_20_max
      value: 59.5865
    - type: nauc_mrr_at_20_std
      value: 22.070600000000002
    - type: nauc_mrr_at_20_diff1
      value: 47.1936
    - type: nauc_mrr_at_100_max
      value: 59.5865
    - type: nauc_mrr_at_100_std
      value: 22.070600000000002
    - type: nauc_mrr_at_100_diff1
      value: 47.1936
    - type: nauc_mrr_at_1000_max
      value: 59.5865
    - type: nauc_mrr_at_1000_std
      value: 22.070600000000002
    - type: nauc_mrr_at_1000_diff1
      value: 47.1936
    - type: main_score
      value: 55.355
    task:
      type: Retrieval
  - dataset:
      config: es
      name: MTEB CUREv1 (es)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: pulmonology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 18.0
    - type: ndcg_at_3
      value: 17.581
    - type: ndcg_at_5
      value: 17.521
    - type: ndcg_at_10
      value: 17.929000000000002
    - type: ndcg_at_20
      value: 19.194
    - type: ndcg_at_100
      value: 24.951
    - type: ndcg_at_1000
      value: 33.986
    - type: map_at_1
      value: 3.5130000000000003
    - type: map_at_3
      value: 5.822
    - type: map_at_5
      value: 6.927
    - type: map_at_10
      value: 8.567
    - type: map_at_20
      value: 9.804
    - type: map_at_100
      value: 12.208
    - type: map_at_1000
      value: 13.876
    - type: recall_at_1
      value: 3.5130000000000003
    - type: recall_at_3
      value: 7.031
    - type: recall_at_5
      value: 9.747
    - type: recall_at_10
      value: 14.171
    - type: recall_at_20
      value: 19.304
    - type: recall_at_100
      value: 37.382
    - type: recall_at_1000
      value: 67.855
    - type: precision_at_1
      value: 22.5
    - type: precision_at_3
      value: 19.0
    - type: precision_at_5
      value: 16.7
    - type: precision_at_10
      value: 13.700000000000001
    - type: precision_at_20
      value: 11.125
    - type: precision_at_100
      value: 6.61
    - type: precision_at_1000
      value: 2.091
    - type: mrr_at_1
      value: 22.5
    - type: mrr_at_3
      value: 28.8333
    - type: mrr_at_5
      value: 30.8333
    - type: mrr_at_10
      value: 32.0377
    - type: mrr_at_20
      value: 32.6114
    - type: mrr_at_100
      value: 32.983000000000004
    - type: mrr_at_1000
      value: 33.0393
    - type: nauc_ndcg_at_1_max
      value: 43.932500000000005
    - type: nauc_ndcg_at_1_std
      value: 30.9222
    - type: nauc_ndcg_at_1_diff1
      value: 19.9076
    - type: nauc_ndcg_at_3_max
      value: 52.4309
    - type: nauc_ndcg_at_3_std
      value: 33.2502
    - type: nauc_ndcg_at_3_diff1
      value: 21.6392
    - type: nauc_ndcg_at_5_max
      value: 53.7562
    - type: nauc_ndcg_at_5_std
      value: 38.7857
    - type: nauc_ndcg_at_5_diff1
      value: 20.2335
    - type: nauc_ndcg_at_10_max
      value: 56.3609
    - type: nauc_ndcg_at_10_std
      value: 41.5947
    - type: nauc_ndcg_at_10_diff1
      value: 22.6265
    - type: nauc_ndcg_at_20_max
      value: 59.8171
    - type: nauc_ndcg_at_20_std
      value: 44.1169
    - type: nauc_ndcg_at_20_diff1
      value: 22.7763
    - type: nauc_ndcg_at_100_max
      value: 63.490100000000005
    - type: nauc_ndcg_at_100_std
      value: 50.1014
    - type: nauc_ndcg_at_100_diff1
      value: 20.4293
    - type: nauc_ndcg_at_1000_max
      value: 63.620200000000004
    - type: nauc_ndcg_at_1000_std
      value: 51.35809999999999
    - type: nauc_ndcg_at_1000_diff1
      value: 17.1076
    - type: nauc_map_at_1_max
      value: 42.8805
    - type: nauc_map_at_1_std
      value: 34.9412
    - type: nauc_map_at_1_diff1
      value: 51.257299999999994
    - type: nauc_map_at_3_max
      value: 49.3844
    - type: nauc_map_at_3_std
      value: 31.5361
    - type: nauc_map_at_3_diff1
      value: 42.1771
    - type: nauc_map_at_5_max
      value: 52.0142
    - type: nauc_map_at_5_std
      value: 38.156099999999995
    - type: nauc_map_at_5_diff1
      value: 34.7349
    - type: nauc_map_at_10_max
      value: 55.47410000000001
    - type: nauc_map_at_10_std
      value: 41.1528
    - type: nauc_map_at_10_diff1
      value: 30.3408
    - type: nauc_map_at_20_max
      value: 57.971399999999996
    - type: nauc_map_at_20_std
      value: 43.3687
    - type: nauc_map_at_20_diff1
      value: 28.723300000000002
    - type: nauc_map_at_100_max
      value: 61.5196
    - type: nauc_map_at_100_std
      value: 47.762100000000004
    - type: nauc_map_at_100_diff1
      value: 26.5933
    - type: nauc_map_at_1000_max
      value: 62.327299999999994
    - type: nauc_map_at_1000_std
      value: 48.6106
    - type: nauc_map_at_1000_diff1
      value: 24.8347
    - type: nauc_recall_at_1_max
      value: 42.8805
    - type: nauc_recall_at_1_std
      value: 34.9412
    - type: nauc_recall_at_1_diff1
      value: 51.257299999999994
    - type: nauc_recall_at_3_max
      value: 46.008500000000005
    - type: nauc_recall_at_3_std
      value: 25.9357
    - type: nauc_recall_at_3_diff1
      value: 39.5208
    - type: nauc_recall_at_5_max
      value: 45.2357
    - type: nauc_recall_at_5_std
      value: 41.3928
    - type: nauc_recall_at_5_diff1
      value: 24.9619
    - type: nauc_recall_at_10_max
      value: 46.6621
    - type: nauc_recall_at_10_std
      value: 38.1389
    - type: nauc_recall_at_10_diff1
      value: 22.9227
    - type: nauc_recall_at_20_max
      value: 51.809400000000004
    - type: nauc_recall_at_20_std
      value: 44.9357
    - type: nauc_recall_at_20_diff1
      value: 19.8542
    - type: nauc_recall_at_100_max
      value: 56.9719
    - type: nauc_recall_at_100_std
      value: 55.10810000000001
    - type: nauc_recall_at_100_diff1
      value: 15.0191
    - type: nauc_recall_at_1000_max
      value: 61.3058
    - type: nauc_recall_at_1000_std
      value: 74.4173
    - type: nauc_recall_at_1000_diff1
      value: 11.5847
    - type: nauc_precision_at_1_max
      value: 44.6099
    - type: nauc_precision_at_1_std
      value: 34.2709
    - type: nauc_precision_at_1_diff1
      value: 12.620600000000001
    - type: nauc_precision_at_3_max
      value: 52.7269
    - type: nauc_precision_at_3_std
      value: 35.4988
    - type: nauc_precision_at_3_diff1
      value: 5.5428
    - type: nauc_precision_at_5_max
      value: 52.2888
    - type: nauc_precision_at_5_std
      value: 40.1329
    - type: nauc_precision_at_5_diff1
      value: 0.7597999999999999
    - type: nauc_precision_at_10_max
      value: 53.4776
    - type: nauc_precision_at_10_std
      value: 41.308099999999996
    - type: nauc_precision_at_10_diff1
      value: 1.2727
    - type: nauc_precision_at_20_max
      value: 51.581900000000005
    - type: nauc_precision_at_20_std
      value: 41.4412
    - type: nauc_precision_at_20_diff1
      value: 1.8686999999999998
    - type: nauc_precision_at_100_max
      value: 37.2452
    - type: nauc_precision_at_100_std
      value: 29.8866
    - type: nauc_precision_at_100_diff1
      value: -2.653
    - type: nauc_precision_at_1000_max
      value: 10.8915
    - type: nauc_precision_at_1000_std
      value: -1.9983
    - type: nauc_precision_at_1000_diff1
      value: -7.8149
    - type: nauc_mrr_at_1_max
      value: 44.6099
    - type: nauc_mrr_at_1_std
      value: 34.2709
    - type: nauc_mrr_at_1_diff1
      value: 12.620600000000001
    - type: nauc_mrr_at_3_max
      value: 47.1393
    - type: nauc_mrr_at_3_std
      value: 33.9716
    - type: nauc_mrr_at_3_diff1
      value: 9.6941
    - type: nauc_mrr_at_5_max
      value: 46.381099999999996
    - type: nauc_mrr_at_5_std
      value: 36.4238
    - type: nauc_mrr_at_5_diff1
      value: 8.3056
    - type: nauc_mrr_at_10_max
      value: 47.5779
    - type: nauc_mrr_at_10_std
      value: 36.6239
    - type: nauc_mrr_at_10_diff1
      value: 8.732099999999999
    - type: nauc_mrr_at_20_max
      value: 48.2236
    - type: nauc_mrr_at_20_std
      value: 37.2659
    - type: nauc_mrr_at_20_diff1
      value: 9.1473
    - type: nauc_mrr_at_100_max
      value: 48.231
    - type: nauc_mrr_at_100_std
      value: 37.335499999999996
    - type: nauc_mrr_at_100_diff1
      value: 8.94
    - type: nauc_mrr_at_1000_max
      value: 48.1705
    - type: nauc_mrr_at_1000_std
      value: 37.278299999999994
    - type: nauc_mrr_at_1000_diff1
      value: 8.9861
    - type: main_score
      value: 17.929000000000002
    task:
      type: Retrieval
  - dataset:
      config: fr
      name: MTEB CUREv1 (fr)
      revision: 3bcf51c91e04d04a8a3329dfbe988b964c5cbe83
      split: pulmonology
      type: clinia/CUREv1
    metrics:
    - type: ndcg_at_1
      value: 22.0
    - type: ndcg_at_3
      value: 19.67
    - type: ndcg_at_5
      value: 19.637999999999998
    - type: ndcg_at_10
      value: 20.093
    - type: ndcg_at_20
      value: 22.037000000000003
    - type: ndcg_at_100
      value: 27.633999999999997
    - type: ndcg_at_1000
      value: 36.504999999999995
    - type: map_at_1
      value: 4.806
    - type: map_at_3
      value: 6.3839999999999995
    - type: map_at_5
      value: 7.617
    - type: map_at_10
      value: 9.371
    - type: map_at_20
      value: 10.822
    - type: map_at_100
      value: 13.616
    - type: map_at_1000
      value: 15.429
    - type: recall_at_1
      value: 4.806
    - type: recall_at_3
      value: 7.5009999999999994
    - type: recall_at_5
      value: 10.041
    - type: recall_at_10
      value: 14.588999999999999
    - type: recall_at_20
      value: 22.256
    - type: recall_at_100
      value: 40.071
    - type: recall_at_1000
      value: 69.741
    - type: precision_at_1
      value: 27.500000000000004
    - type: precision_at_3
      value: 19.833000000000002
    - type: precision_at_5
      value: 18.3
    - type: precision_at_10
      value: 15.5
    - type: precision_at_20
      value: 12.875
    - type: precision_at_100
      value: 7.380000000000001
    - type: precision_at_1000
      value: 2.186
    - type: mrr_at_1
      value: 27.500000000000004
    - type: mrr_at_3
      value: 33.6667
    - type: mrr_at_5
      value: 35.341699999999996
    - type: mrr_at_10
      value: 36.432700000000004
    - type: mrr_at_20
      value: 37.297200000000004
    - type: mrr_at_100
      value: 37.675599999999996
    - type: mrr_at_1000
      value: 37.722899999999996
    - type: nauc_ndcg_at_1_max
      value: 42.6021
    - type: nauc_ndcg_at_1_std
      value: 35.9813
    - type: nauc_ndcg_at_1_diff1
      value: 22.290399999999998
    - type: nauc_ndcg_at_3_max
      value: 49.1559
    - type: nauc_ndcg_at_3_std
      value: 40.0896
    - type: nauc_ndcg_at_3_diff1
      value: 22.279799999999998
    - type: nauc_ndcg_at_5_max
      value: 51.4668
    - type: nauc_ndcg_at_5_std
      value: 39.624900000000004
    - type: nauc_ndcg_at_5_diff1
      value: 22.3741
    - type: nauc_ndcg_at_10_max
      value: 54.519
    - type: nauc_ndcg_at_10_std
      value: 42.104200000000006
    - type: nauc_ndcg_at_10_diff1
      value: 22.4078
    - type: nauc_ndcg_at_20_max
      value: 56.2174
    - type: nauc_ndcg_at_20_std
      value: 46.512100000000004
    - type: nauc_ndcg_at_20_diff1
      value: 23.6843
    - type: nauc_ndcg_at_100_max
      value: 61.04619999999999
    - type: nauc_ndcg_at_100_std
      value: 57.2706
    - type: nauc_ndcg_at_100_diff1
      value: 23.2432
    - type: nauc_ndcg_at_1000_max
      value: 61.364200000000004
    - type: nauc_ndcg_at_1000_std
      value: 56.0934
    - type: nauc_ndcg_at_1000_diff1
      value: 17.2488
    - type: nauc_map_at_1_max
      value: 44.9878
    - type: nauc_map_at_1_std
      value: 34.9461
    - type: nauc_map_at_1_diff1
      value: 53.675399999999996
    - type: nauc_map_at_3_max
      value: 44.4329
    - type: nauc_map_at_3_std
      value: 36.0323
    - type: nauc_map_at_3_diff1
      value: 46.4853
    - type: nauc_map_at_5_max
      value: 46.2582
    - type: nauc_map_at_5_std
      value: 36.9879
    - type: nauc_map_at_5_diff1
      value: 41.4037
    - type: nauc_map_at_10_max
      value: 50.330200000000005
    - type: nauc_map_at_10_std
      value: 40.0156
    - type: nauc_map_at_10_diff1
      value: 38.1695
    - type: nauc_map_at_20_max
      value: 51.7941
    - type: nauc_map_at_20_std
      value: 44.193599999999996
    - type: nauc_map_at_20_diff1
      value: 35.8223
    - type: nauc_map_at_100_max
      value: 54.651
    - type: nauc_map_at_100_std
      value: 50.6749
    - type: nauc_map_at_100_diff1
      value: 31.0403
    - type: nauc_map_at_1000_max
      value: 54.2956
    - type: nauc_map_at_1000_std
      value: 50.2575
    - type: nauc_map_at_1000_diff1
      value: 26.8654
    - type: nauc_recall_at_1_max
      value: 44.9878
    - type: nauc_recall_at_1_std
      value: 34.9461
    - type: nauc_recall_at_1_diff1
      value: 53.675399999999996
    - type: nauc_recall_at_3_max
      value: 40.9893
    - type: nauc_recall_at_3_std
      value: 34.5723
    - type: nauc_recall_at_3_diff1
      value: 41.6989
    - type: nauc_recall_at_5_max
      value: 43.0016
    - type: nauc_recall_at_5_std
      value: 32.7617
    - type: nauc_recall_at_5_diff1
      value: 34.6036
    - type: nauc_recall_at_10_max
      value: 51.5082
    - type: nauc_recall_at_10_std
      value: 39.9773
    - type: nauc_recall_at_10_diff1
      value: 30.900899999999996
    - type: nauc_recall_at_20_max
      value: 48.149300000000004
    - type: nauc_recall_at_20_std
      value: 45.0434
    - type: nauc_recall_at_20_diff1
      value: 28.865800000000004
    - type: nauc_recall_at_100_max
      value: 56.163799999999995
    - type: nauc_recall_at_100_std
      value: 65.4097
    - type: nauc_recall_at_100_diff1
      value: 24.0152
    - type: nauc_recall_at_1000_max
      value: 65.8655
    - type: nauc_recall_at_1000_std
      value: 74.5213
    - type: nauc_recall_at_1000_diff1
      value: 15.1259
    - type: nauc_precision_at_1_max
      value: 39.8972
    - type: nauc_precision_at_1_std
      value: 33.6627
    - type: nauc_precision_at_1_diff1
      value: 17.1124
    - type: nauc_precision_at_3_max
      value: 44.7058
    - type: nauc_precision_at_3_std
      value: 37.6182
    - type: nauc_precision_at_3_diff1
      value: 8.8976
    - type: nauc_precision_at_5_max
      value: 43.9751
    - type: nauc_precision_at_5_std
      value: 34.65
    - type: nauc_precision_at_5_diff1
      value: 2.9363
    - type: nauc_precision_at_10_max
      value: 41.3611
    - type: nauc_precision_at_10_std
      value: 35.741299999999995
    - type: nauc_precision_at_10_diff1
      value: -0.1869
    - type: nauc_precision_at_20_max
      value: 37.6713
    - type: nauc_precision_at_20_std
      value: 37.3803
    - type: nauc_precision_at_20_diff1
      value: -6.543699999999999
    - type: nauc_precision_at_100_max
      value: 21.4265
    - type: nauc_precision_at_100_std
      value: 24.3006
    - type: nauc_precision_at_100_diff1
      value: -18.1773
    - type: nauc_precision_at_1000_max
      value: 0.7231
    - type: nauc_precision_at_1000_std
      value: -7.500500000000001
    - type: nauc_precision_at_1000_diff1
      value: -27.672400000000003
    - type: nauc_mrr_at_1_max
      value: 39.8972
    - type: nauc_mrr_at_1_std
      value: 33.6627
    - type: nauc_mrr_at_1_diff1
      value: 17.1124
    - type: nauc_mrr_at_3_max
      value: 44.0551
    - type: nauc_mrr_at_3_std
      value: 35.9342
    - type: nauc_mrr_at_3_diff1
      value: 16.797
    - type: nauc_mrr_at_5_max
      value: 44.575700000000005
    - type: nauc_mrr_at_5_std
      value: 35.5613
    - type: nauc_mrr_at_5_diff1
      value: 15.8189
    - type: nauc_mrr_at_10_max
      value: 45.3991
    - type: nauc_mrr_at_10_std
      value: 37.3274
    - type: nauc_mrr_at_10_diff1
      value: 15.509899999999998
    - type: nauc_mrr_at_20_max
      value: 45.6017
    - type: nauc_mrr_at_20_std
      value: 37.7156
    - type: nauc_mrr_at_20_diff1
      value: 15.357499999999998
    - type: nauc_mrr_at_100_max
      value: 45.5056
    - type: nauc_mrr_at_100_std
      value: 37.734899999999996
    - type: nauc_mrr_at_100_diff1
      value: 15.382599999999998
    - type: nauc_mrr_at_1000_max
      value: 45.4736
    - type: nauc_mrr_at_1000_std
      value: 37.6894
    - type: nauc_mrr_at_1000_diff1
      value: 15.3948
    - type: main_score
      value: 20.093
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB CmedqaRetrieval (default)
      revision: cd540c506dae1cf9e9a59c3e06f42030d54e7301
      split: dev
      type: C-MTEB/CmedqaRetrieval
    metrics:
    - type: ndcg_at_1
      value: 1.975
    - type: ndcg_at_3
      value: 1.8800000000000001
    - type: ndcg_at_5
      value: 2.064
    - type: ndcg_at_10
      value: 2.244
    - type: ndcg_at_20
      value: 2.444
    - type: ndcg_at_100
      value: 3.1419999999999995
    - type: ndcg_at_1000
      value: 4.436
    - type: map_at_1
      value: 1.0959999999999999
    - type: map_at_3
      value: 1.459
    - type: map_at_5
      value: 1.5970000000000002
    - type: map_at_10
      value: 1.678
    - type: map_at_20
      value: 1.73
    - type: map_at_100
      value: 1.817
    - type: map_at_1000
      value: 1.854
    - type: recall_at_1
      value: 1.0959999999999999
    - type: recall_at_3
      value: 1.8399999999999999
    - type: recall_at_5
      value: 2.411
    - type: recall_at_10
      value: 2.9690000000000003
    - type: recall_at_20
      value: 3.65
    - type: recall_at_100
      value: 6.882000000000001
    - type: recall_at_1000
      value: 16.221
    - type: precision_at_1
      value: 1.975
    - type: precision_at_3
      value: 1.134
    - type: precision_at_5
      value: 0.855
    - type: precision_at_10
      value: 0.545
    - type: precision_at_20
      value: 0.34299999999999997
    - type: precision_at_100
      value: 0.136
    - type: precision_at_1000
      value: 0.031
    - type: mrr_at_1
      value: 1.9755000000000003
    - type: mrr_at_3
      value: 2.4548
    - type: mrr_at_5
      value: 2.6336
    - type: mrr_at_10
      value: 2.7566
    - type: mrr_at_20
      value: 2.834
    - type: mrr_at_100
      value: 2.948
    - type: mrr_at_1000
      value: 2.9941
    - type: nauc_ndcg_at_1_max
      value: 44.5578
    - type: nauc_ndcg_at_1_std
      value: -7.0793
    - type: nauc_ndcg_at_1_diff1
      value: 41.342800000000004
    - type: nauc_ndcg_at_3_max
      value: 38.824799999999996
    - type: nauc_ndcg_at_3_std
      value: -7.721400000000001
    - type: nauc_ndcg_at_3_diff1
      value: 29.5746
    - type: nauc_ndcg_at_5_max
      value: 35.3778
    - type: nauc_ndcg_at_5_std
      value: -8.0892
    - type: nauc_ndcg_at_5_diff1
      value: 28.1742
    - type: nauc_ndcg_at_10_max
      value: 33.9489
    - type: nauc_ndcg_at_10_std
      value: -6.5869
    - type: nauc_ndcg_at_10_diff1
      value: 25.1357
    - type: nauc_ndcg_at_20_max
      value: 31.6749
    - type: nauc_ndcg_at_20_std
      value: -6.1487
    - type: nauc_ndcg_at_20_diff1
      value: 22.4549
    - type: nauc_ndcg_at_100_max
      value: 25.5529
    - type: nauc_ndcg_at_100_std
      value: -3.3800999999999997
    - type: nauc_ndcg_at_100_diff1
      value: 18.2302
    - type: nauc_ndcg_at_1000_max
      value: 21.4586
    - type: nauc_ndcg_at_1000_std
      value: 0.3195
    - type: nauc_ndcg_at_1000_diff1
      value: 15.187800000000001
    - type: nauc_map_at_1_max
      value: 48.9561
    - type: nauc_map_at_1_std
      value: -8.7168
    - type: nauc_map_at_1_diff1
      value: 41.5248
    - type: nauc_map_at_3_max
      value: 41.7416
    - type: nauc_map_at_3_std
      value: -8.9731
    - type: nauc_map_at_3_diff1
      value: 30.8288
    - type: nauc_map_at_5_max
      value: 39.2026
    - type: nauc_map_at_5_std
      value: -9.1096
    - type: nauc_map_at_5_diff1
      value: 29.8599
    - type: nauc_map_at_10_max
      value: 38.3244
    - type: nauc_map_at_10_std
      value: -8.3488
    - type: nauc_map_at_10_diff1
      value: 28.4995
    - type: nauc_map_at_20_max
      value: 37.4247
    - type: nauc_map_at_20_std
      value: -8.132200000000001
    - type: nauc_map_at_20_diff1
      value: 27.494000000000003
    - type: nauc_map_at_100_max
      value: 35.9232
    - type: nauc_map_at_100_std
      value: -7.3904
    - type: nauc_map_at_100_diff1
      value: 26.3365
    - type: nauc_map_at_1000_max
      value: 35.5077
    - type: nauc_map_at_1000_std
      value: -7.093000000000001
    - type: nauc_map_at_1000_diff1
      value: 25.9599
    - type: nauc_recall_at_1_max
      value: 48.9561
    - type: nauc_recall_at_1_std
      value: -8.7168
    - type: nauc_recall_at_1_diff1
      value: 41.5248
    - type: nauc_recall_at_3_max
      value: 35.0824
    - type: nauc_recall_at_3_std
      value: -6.9858
    - type: nauc_recall_at_3_diff1
      value: 24.1649
    - type: nauc_recall_at_5_max
      value: 29.3684
    - type: nauc_recall_at_5_std
      value: -8.2378
    - type: nauc_recall_at_5_diff1
      value: 23.042299999999997
    - type: nauc_recall_at_10_max
      value: 27.4364
    - type: nauc_recall_at_10_std
      value: -5.7612
    - type: nauc_recall_at_10_diff1
      value: 18.4245
    - type: nauc_recall_at_20_max
      value: 23.4658
    - type: nauc_recall_at_20_std
      value: -5.0295
    - type: nauc_recall_at_20_diff1
      value: 13.6712
    - type: nauc_recall_at_100_max
      value: 14.056199999999999
    - type: nauc_recall_at_100_std
      value: -0.0629
    - type: nauc_recall_at_100_diff1
      value: 9.0138
    - type: nauc_recall_at_1000_max
      value: 10.1503
    - type: nauc_recall_at_1000_std
      value: 6.651
    - type: nauc_recall_at_1000_diff1
      value: 6.7867999999999995
    - type: nauc_precision_at_1_max
      value: 44.5578
    - type: nauc_precision_at_1_std
      value: -7.0793
    - type: nauc_precision_at_1_diff1
      value: 41.342800000000004
    - type: nauc_precision_at_3_max
      value: 35.142
    - type: nauc_precision_at_3_std
      value: -6.3729
    - type: nauc_precision_at_3_diff1
      value: 23.5105
    - type: nauc_precision_at_5_max
      value: 31.5182
    - type: nauc_precision_at_5_std
      value: -5.9487
    - type: nauc_precision_at_5_diff1
      value: 23.244899999999998
    - type: nauc_precision_at_10_max
      value: 28.1848
    - type: nauc_precision_at_10_std
      value: -2.1538000000000004
    - type: nauc_precision_at_10_diff1
      value: 18.1237
    - type: nauc_precision_at_20_max
      value: 23.6964
    - type: nauc_precision_at_20_std
      value: -1.5044
    - type: nauc_precision_at_20_diff1
      value: 13.669300000000002
    - type: nauc_precision_at_100_max
      value: 14.132900000000001
    - type: nauc_precision_at_100_std
      value: 3.6346000000000003
    - type: nauc_precision_at_100_diff1
      value: 9.3907
    - type: nauc_precision_at_1000_max
      value: 9.5808
    - type: nauc_precision_at_1000_std
      value: 7.452400000000001
    - type: nauc_precision_at_1000_diff1
      value: 7.3365
    - type: nauc_mrr_at_1_max
      value: 44.5578
    - type: nauc_mrr_at_1_std
      value: -7.0793
    - type: nauc_mrr_at_1_diff1
      value: 41.342800000000004
    - type: nauc_mrr_at_3_max
      value: 38.055299999999995
    - type: nauc_mrr_at_3_std
      value: -6.456199999999999
    - type: nauc_mrr_at_3_diff1
      value: 32.067099999999996
    - type: nauc_mrr_at_5_max
      value: 36.5336
    - type: nauc_mrr_at_5_std
      value: -6.546399999999999
    - type: nauc_mrr_at_5_diff1
      value: 31.506899999999998
    - type: nauc_mrr_at_10_max
      value: 35.57
    - type: nauc_mrr_at_10_std
      value: -5.7427
    - type: nauc_mrr_at_10_diff1
      value: 30.0035
    - type: nauc_mrr_at_20_max
      value: 34.6904
    - type: nauc_mrr_at_20_std
      value: -5.6437
    - type: nauc_mrr_at_20_diff1
      value: 29.002200000000002
    - type: nauc_mrr_at_100_max
      value: 33.377
    - type: nauc_mrr_at_100_std
      value: -5.2307
    - type: nauc_mrr_at_100_diff1
      value: 27.822999999999997
    - type: nauc_mrr_at_1000_max
      value: 33.1079
    - type: nauc_mrr_at_1000_std
      value: -5.066
    - type: nauc_mrr_at_1000_diff1
      value: 27.535700000000002
    - type: main_score
      value: 2.244
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MedicalQARetrieval (default)
      revision: ae763399273d8b20506b80cf6f6f9a31a6a2b238
      split: test
      type: mteb/medical_qa
    metrics:
    - type: ndcg_at_1
      value: 61.816
    - type: ndcg_at_3
      value: 70.759
    - type: ndcg_at_5
      value: 72.968
    - type: ndcg_at_10
      value: 74.824
    - type: ndcg_at_20
      value: 75.82799999999999
    - type: ndcg_at_100
      value: 76.846
    - type: ndcg_at_1000
      value: 77.164
    - type: map_at_1
      value: 61.816
    - type: map_at_3
      value: 68.612
    - type: map_at_5
      value: 69.83500000000001
    - type: map_at_10
      value: 70.616
    - type: map_at_20
      value: 70.899
    - type: map_at_100
      value: 71.043
    - type: map_at_1000
      value: 71.055
    - type: recall_at_1
      value: 61.816
    - type: recall_at_3
      value: 76.953
    - type: recall_at_5
      value: 82.324
    - type: recall_at_10
      value: 87.988
    - type: recall_at_20
      value: 91.89500000000001
    - type: recall_at_100
      value: 97.363
    - type: recall_at_1000
      value: 99.854
    - type: precision_at_1
      value: 61.816
    - type: precision_at_3
      value: 25.651000000000003
    - type: precision_at_5
      value: 16.465
    - type: precision_at_10
      value: 8.799
    - type: precision_at_20
      value: 4.595
    - type: precision_at_100
      value: 0.9740000000000001
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 61.914100000000005
    - type: mrr_at_3
      value: 68.6686
    - type: mrr_at_5
      value: 69.8942
    - type: mrr_at_10
      value: 70.6751
    - type: mrr_at_20
      value: 70.9589
    - type: mrr_at_100
      value: 71.102
    - type: mrr_at_1000
      value: 71.11420000000001
    - type: nauc_ndcg_at_1_max
      value: 43.0416
    - type: nauc_ndcg_at_1_std
      value: 1.4047
    - type: nauc_ndcg_at_1_diff1
      value: 68.2899
    - type: nauc_ndcg_at_3_max
      value: 44.2637
    - type: nauc_ndcg_at_3_std
      value: -2.6632
    - type: nauc_ndcg_at_3_diff1
      value: 62.948499999999996
    - type: nauc_ndcg_at_5_max
      value: 44.3739
    - type: nauc_ndcg_at_5_std
      value: -3.1071
    - type: nauc_ndcg_at_5_diff1
      value: 62.4586
    - type: nauc_ndcg_at_10_max
      value: 45.7976
    - type: nauc_ndcg_at_10_std
      value: -4.037
    - type: nauc_ndcg_at_10_diff1
      value: 62.5016
    - type: nauc_ndcg_at_20_max
      value: 45.4416
    - type: nauc_ndcg_at_20_std
      value: -3.3076000000000003
    - type: nauc_ndcg_at_20_diff1
      value: 62.64619999999999
    - type: nauc_ndcg_at_100_max
      value: 45.216
    - type: nauc_ndcg_at_100_std
      value: -2.6107
    - type: nauc_ndcg_at_100_diff1
      value: 63.1536
    - type: nauc_ndcg_at_1000_max
      value: 44.8511
    - type: nauc_ndcg_at_1000_std
      value: -2.2796
    - type: nauc_ndcg_at_1000_diff1
      value: 63.5203
    - type: nauc_map_at_1_max
      value: 43.0416
    - type: nauc_map_at_1_std
      value: 1.4047
    - type: nauc_map_at_1_diff1
      value: 68.2899
    - type: nauc_map_at_3_max
      value: 43.8357
    - type: nauc_map_at_3_std
      value: -1.4727999999999999
    - type: nauc_map_at_3_diff1
      value: 64.3811
    - type: nauc_map_at_5_max
      value: 43.865300000000005
    - type: nauc_map_at_5_std
      value: -1.6657000000000002
    - type: nauc_map_at_5_diff1
      value: 64.1906
    - type: nauc_map_at_10_max
      value: 44.376599999999996
    - type: nauc_map_at_10_std
      value: -2.004
    - type: nauc_map_at_10_diff1
      value: 64.2587
    - type: nauc_map_at_20_max
      value: 44.289
    - type: nauc_map_at_20_std
      value: -1.8488999999999998
    - type: nauc_map_at_20_diff1
      value: 64.3021
    - type: nauc_map_at_100_max
      value: 44.2802
    - type: nauc_map_at_100_std
      value: -1.7392999999999998
    - type: nauc_map_at_100_diff1
      value: 64.3597
    - type: nauc_map_at_1000_max
      value: 44.2691
    - type: nauc_map_at_1000_std
      value: -1.72
    - type: nauc_map_at_1000_diff1
      value: 64.37349999999999
    - type: nauc_recall_at_1_max
      value: 43.0416
    - type: nauc_recall_at_1_std
      value: 1.4047
    - type: nauc_recall_at_1_diff1
      value: 68.2899
    - type: nauc_recall_at_3_max
      value: 45.8586
    - type: nauc_recall_at_3_std
      value: -7.0022
    - type: nauc_recall_at_3_diff1
      value: 57.791599999999995
    - type: nauc_recall_at_5_max
      value: 46.698299999999996
    - type: nauc_recall_at_5_std
      value: -9.518699999999999
    - type: nauc_recall_at_5_diff1
      value: 54.8081
    - type: nauc_recall_at_10_max
      value: 55.617700000000006
    - type: nauc_recall_at_10_std
      value: -17.0066
    - type: nauc_recall_at_10_diff1
      value: 51.7949
    - type: nauc_recall_at_20_max
      value: 56.2234
    - type: nauc_recall_at_20_std
      value: -14.6945
    - type: nauc_recall_at_20_diff1
      value: 48.6265
    - type: nauc_recall_at_100_max
      value: 66.3957
    - type: nauc_recall_at_100_std
      value: -13.4665
    - type: nauc_recall_at_100_diff1
      value: 41.1961
    - type: nauc_recall_at_1000_max
      value: 47.873599999999996
    - type: nauc_recall_at_1000_std
      value: 61.4994
    - type: nauc_recall_at_1000_diff1
      value: 33.012
    - type: nauc_precision_at_1_max
      value: 43.0416
    - type: nauc_precision_at_1_std
      value: 1.4047
    - type: nauc_precision_at_1_diff1
      value: 68.2899
    - type: nauc_precision_at_3_max
      value: 45.8586
    - type: nauc_precision_at_3_std
      value: -7.0022
    - type: nauc_precision_at_3_diff1
      value: 57.791599999999995
    - type: nauc_precision_at_5_max
      value: 46.698299999999996
    - type: nauc_precision_at_5_std
      value: -9.518699999999999
    - type: nauc_precision_at_5_diff1
      value: 54.8081
    - type: nauc_precision_at_10_max
      value: 55.617700000000006
    - type: nauc_precision_at_10_std
      value: -17.0066
    - type: nauc_precision_at_10_diff1
      value: 51.7949
    - type: nauc_precision_at_20_max
      value: 56.2234
    - type: nauc_precision_at_20_std
      value: -14.6945
    - type: nauc_precision_at_20_diff1
      value: 48.6265
    - type: nauc_precision_at_100_max
      value: 66.3957
    - type: nauc_precision_at_100_std
      value: -13.4665
    - type: nauc_precision_at_100_diff1
      value: 41.1961
    - type: nauc_precision_at_1000_max
      value: 47.873599999999996
    - type: nauc_precision_at_1000_std
      value: 61.4994
    - type: nauc_precision_at_1000_diff1
      value: 33.012
    - type: nauc_mrr_at_1_max
      value: 43.147000000000006
    - type: nauc_mrr_at_1_std
      value: 1.6458
    - type: nauc_mrr_at_1_diff1
      value: 68.0902
    - type: nauc_mrr_at_3_max
      value: 43.904199999999996
    - type: nauc_mrr_at_3_std
      value: -1.3296999999999999
    - type: nauc_mrr_at_3_diff1
      value: 64.24459999999999
    - type: nauc_mrr_at_5_max
      value: 43.9347
    - type: nauc_mrr_at_5_std
      value: -1.5104
    - type: nauc_mrr_at_5_diff1
      value: 64.0435
    - type: nauc_mrr_at_10_max
      value: 44.4408
    - type: nauc_mrr_at_10_std
      value: -1.8647
    - type: nauc_mrr_at_10_diff1
      value: 64.1077
    - type: nauc_mrr_at_20_max
      value: 44.3536
    - type: nauc_mrr_at_20_std
      value: -1.7078
    - type: nauc_mrr_at_20_diff1
      value: 64.1495
    - type: nauc_mrr_at_100_max
      value: 44.3452
    - type: nauc_mrr_at_100_std
      value: -1.5973000000000002
    - type: nauc_mrr_at_100_diff1
      value: 64.2063
    - type: nauc_mrr_at_1000_max
      value: 44.3341
    - type: nauc_mrr_at_1000_std
      value: -1.5779
    - type: nauc_mrr_at_1000_diff1
      value: 64.22
    - type: main_score
      value: 74.824
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB MedrxivClusteringP2P.v2 (default)
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
      split: test
      type: mteb/medrxiv-clustering-p2p
    metrics:
    - type: v_measure
      value: 36.208200000000005
    - type: v_measure_std
      value: 1.3513000000000002
    - type: main_score
      value: 36.208200000000005
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB MedrxivClusteringS2S.v2 (default)
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
      split: test
      type: mteb/medrxiv-clustering-s2s
    metrics:
    - type: v_measure
      value: 34.1653
    - type: v_measure_std
      value: 0.5923
    - type: main_score
      value: 34.1653
    task:
      type: Clustering
  - dataset:
      config: default
      name: MTEB NFCorpus (default)
      revision: ec0fa4fe99da2ff19ca1214b7966684033a58814
      split: test
      type: mteb/nfcorpus
    metrics:
    - type: ndcg_at_1
      value: 47.368
    - type: ndcg_at_3
      value: 43.149
    - type: ndcg_at_5
      value: 40.262
    - type: ndcg_at_10
      value: 37.07
    - type: ndcg_at_20
      value: 35.258
    - type: ndcg_at_100
      value: 34.742
    - type: ndcg_at_1000
      value: 43.864999999999995
    - type: map_at_1
      value: 7.298
    - type: map_at_3
      value: 11.259
    - type: map_at_5
      value: 12.756
    - type: map_at_10
      value: 14.829
    - type: map_at_20
      value: 16.543
    - type: map_at_100
      value: 18.755
    - type: map_at_1000
      value: 20.302999999999997
    - type: recall_at_1
      value: 7.298
    - type: recall_at_3
      value: 12.056000000000001
    - type: recall_at_5
      value: 14.184
    - type: recall_at_10
      value: 18.224999999999998
    - type: recall_at_20
      value: 23.009
    - type: recall_at_100
      value: 35.398
    - type: recall_at_1000
      value: 67.74900000000001
    - type: precision_at_1
      value: 48.916
    - type: precision_at_3
      value: 39.938
    - type: precision_at_5
      value: 33.994
    - type: precision_at_10
      value: 26.779999999999998
    - type: precision_at_20
      value: 20.355999999999998
    - type: precision_at_100
      value: 8.458
    - type: precision_at_1000
      value: 2.176
    - type: mrr_at_1
      value: 48.916399999999996
    - type: mrr_at_3
      value: 55.985600000000005
    - type: mrr_at_5
      value: 57.0537
    - type: mrr_at_10
      value: 57.7149
    - type: mrr_at_20
      value: 58.1229
    - type: mrr_at_100
      value: 58.397299999999994
    - type: mrr_at_1000
      value: 58.4248
    - type: nauc_ndcg_at_1_max
      value: 41.3116
    - type: nauc_ndcg_at_1_std
      value: 22.451
    - type: nauc_ndcg_at_1_diff1
      value: 37.2109
    - type: nauc_ndcg_at_3_max
      value: 40.1035
    - type: nauc_ndcg_at_3_std
      value: 24.5928
    - type: nauc_ndcg_at_3_diff1
      value: 24.430699999999998
    - type: nauc_ndcg_at_5_max
      value: 39.734
    - type: nauc_ndcg_at_5_std
      value: 25.881500000000003
    - type: nauc_ndcg_at_5_diff1
      value: 22.0016
    - type: nauc_ndcg_at_10_max
      value: 38.4436
    - type: nauc_ndcg_at_10_std
      value: 27.4864
    - type: nauc_ndcg_at_10_diff1
      value: 21.456400000000002
    - type: nauc_ndcg_at_20_max
      value: 37.5296
    - type: nauc_ndcg_at_20_std
      value: 26.714100000000002
    - type: nauc_ndcg_at_20_diff1
      value: 22.9013
    - type: nauc_ndcg_at_100_max
      value: 40.7159
    - type: nauc_ndcg_at_100_std
      value: 27.7585
    - type: nauc_ndcg_at_100_diff1
      value: 25.681700000000003
    - type: nauc_ndcg_at_1000_max
      value: 45.828799999999994
    - type: nauc_ndcg_at_1000_std
      value: 35.1004
    - type: nauc_ndcg_at_1000_diff1
      value: 25.220799999999997
    - type: nauc_map_at_1_max
      value: 15.6695
    - type: nauc_map_at_1_std
      value: -10.7993
    - type: nauc_map_at_1_diff1
      value: 42.3173
    - type: nauc_map_at_3_max
      value: 20.509900000000002
    - type: nauc_map_at_3_std
      value: -5.0278
    - type: nauc_map_at_3_diff1
      value: 39.326299999999996
    - type: nauc_map_at_5_max
      value: 23.020699999999998
    - type: nauc_map_at_5_std
      value: -2.0001
    - type: nauc_map_at_5_diff1
      value: 36.3273
    - type: nauc_map_at_10_max
      value: 25.6403
    - type: nauc_map_at_10_std
      value: 3.4666
    - type: nauc_map_at_10_diff1
      value: 32.1434
    - type: nauc_map_at_20_max
      value: 27.7762
    - type: nauc_map_at_20_std
      value: 8.83
    - type: nauc_map_at_20_diff1
      value: 29.428700000000003
    - type: nauc_map_at_100_max
      value: 30.4644
    - type: nauc_map_at_100_std
      value: 14.0983
    - type: nauc_map_at_100_diff1
      value: 27.7847
    - type: nauc_map_at_1000_max
      value: 31.1749
    - type: nauc_map_at_1000_std
      value: 16.8873
    - type: nauc_map_at_1000_diff1
      value: 26.736500000000003
    - type: nauc_recall_at_1_max
      value: 15.6695
    - type: nauc_recall_at_1_std
      value: -10.7993
    - type: nauc_recall_at_1_diff1
      value: 42.3173
    - type: nauc_recall_at_3_max
      value: 19.5384
    - type: nauc_recall_at_3_std
      value: -4.2829
    - type: nauc_recall_at_3_diff1
      value: 37.924
    - type: nauc_recall_at_5_max
      value: 21.6262
    - type: nauc_recall_at_5_std
      value: -0.6713
    - type: nauc_recall_at_5_diff1
      value: 34.423500000000004
    - type: nauc_recall_at_10_max
      value: 21.7819
    - type: nauc_recall_at_10_std
      value: 3.4214
    - type: nauc_recall_at_10_diff1
      value: 28.447499999999998
    - type: nauc_recall_at_20_max
      value: 23.880499999999998
    - type: nauc_recall_at_20_std
      value: 9.232899999999999
    - type: nauc_recall_at_20_diff1
      value: 26.002
    - type: nauc_recall_at_100_max
      value: 25.6814
    - type: nauc_recall_at_100_std
      value: 15.804599999999999
    - type: nauc_recall_at_100_diff1
      value: 16.955000000000002
    - type: nauc_recall_at_1000_max
      value: 22.5706
    - type: nauc_recall_at_1000_std
      value: 25.684600000000003
    - type: nauc_recall_at_1000_diff1
      value: 7.257099999999999
    - type: nauc_precision_at_1_max
      value: 43.9778
    - type: nauc_precision_at_1_std
      value: 23.9525
    - type: nauc_precision_at_1_diff1
      value: 34.5267
    - type: nauc_precision_at_3_max
      value: 38.661899999999996
    - type: nauc_precision_at_3_std
      value: 29.4867
    - type: nauc_precision_at_3_diff1
      value: 12.2659
    - type: nauc_precision_at_5_max
      value: 37.0542
    - type: nauc_precision_at_5_std
      value: 33.0248
    - type: nauc_precision_at_5_diff1
      value: 3.8455999999999997
    - type: nauc_precision_at_10_max
      value: 34.932900000000004
    - type: nauc_precision_at_10_std
      value: 38.5304
    - type: nauc_precision_at_10_diff1
      value: -2.7742
    - type: nauc_precision_at_20_max
      value: 29.228199999999998
    - type: nauc_precision_at_20_std
      value: 39.0561
    - type: nauc_precision_at_20_diff1
      value: -6.049
    - type: nauc_precision_at_100_max
      value: 18.4449
    - type: nauc_precision_at_100_std
      value: 35.3197
    - type: nauc_precision_at_100_diff1
      value: -8.9064
    - type: nauc_precision_at_1000_max
      value: 3.8112
    - type: nauc_precision_at_1000_std
      value: 23.8397
    - type: nauc_precision_at_1000_diff1
      value: -13.475200000000001
    - type: nauc_mrr_at_1_max
      value: 43.9778
    - type: nauc_mrr_at_1_std
      value: 23.9525
    - type: nauc_mrr_at_1_diff1
      value: 34.5267
    - type: nauc_mrr_at_3_max
      value: 46.333
    - type: nauc_mrr_at_3_std
      value: 27.969
    - type: nauc_mrr_at_3_diff1
      value: 34.537600000000005
    - type: nauc_mrr_at_5_max
      value: 47.0493
    - type: nauc_mrr_at_5_std
      value: 29.6659
    - type: nauc_mrr_at_5_diff1
      value: 33.9539
    - type: nauc_mrr_at_10_max
      value: 47.1933
    - type: nauc_mrr_at_10_std
      value: 30.4836
    - type: nauc_mrr_at_10_diff1
      value: 33.794200000000004
    - type: nauc_mrr_at_20_max
      value: 47.5342
    - type: nauc_mrr_at_20_std
      value: 30.714999999999996
    - type: nauc_mrr_at_20_diff1
      value: 34.042899999999996
    - type: nauc_mrr_at_100_max
      value: 47.5202
    - type: nauc_mrr_at_100_std
      value: 30.534299999999998
    - type: nauc_mrr_at_100_diff1
      value: 33.8418
    - type: nauc_mrr_at_1000_max
      value: 47.4983
    - type: nauc_mrr_at_1000_std
      value: 30.5077
    - type: nauc_mrr_at_1000_diff1
      value: 33.856700000000004
    - type: main_score
      value: 37.07
    task:
      type: Retrieval
  - dataset:
      config: arabic
      name: MTEB PublicHealthQA (arabic)
      revision: main
      split: test
      type: xhluca/publichealth-qa
    metrics:
    - type: ndcg_at_1
      value: 3.488
    - type: ndcg_at_3
      value: 7.738
    - type: ndcg_at_5
      value: 9.639000000000001
    - type: ndcg_at_10
      value: 12.396
    - type: ndcg_at_20
      value: 17.115
    - type: ndcg_at_100
      value: 27.512999999999998
    - type: ndcg_at_1000
      value: 27.512999999999998
    - type: map_at_1
      value: 3.488
    - type: map_at_3
      value: 6.783
    - type: map_at_5
      value: 7.829
    - type: map_at_10
      value: 9.044
    - type: map_at_20
      value: 10.347000000000001
    - type: map_at_100
      value: 11.632000000000001
    - type: map_at_1000
      value: 11.632000000000001
    - type: recall_at_1
      value: 3.488
    - type: recall_at_3
      value: 10.465
    - type: recall_at_5
      value: 15.116
    - type: recall_at_10
      value: 23.256
    - type: recall_at_20
      value: 41.86
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 3.488
    - type: precision_at_3
      value: 3.488
    - type: precision_at_5
      value: 3.023
    - type: precision_at_10
      value: 2.326
    - type: precision_at_20
      value: 2.093
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 3.4884
    - type: mrr_at_3
      value: 6.7829
    - type: mrr_at_5
      value: 7.8295
    - type: mrr_at_10
      value: 9.0439
    - type: mrr_at_20
      value: 10.3465
    - type: mrr_at_100
      value: 11.6317
    - type: mrr_at_1000
      value: 11.6317
    - type: nauc_ndcg_at_1_max
      value: 59.715700000000005
    - type: nauc_ndcg_at_1_std
      value: 37.2948
    - type: nauc_ndcg_at_1_diff1
      value: 77.5791
    - type: nauc_ndcg_at_3_max
      value: 35.650999999999996
    - type: nauc_ndcg_at_3_std
      value: 4.0767
    - type: nauc_ndcg_at_3_diff1
      value: 48.6041
    - type: nauc_ndcg_at_5_max
      value: 26.639400000000002
    - type: nauc_ndcg_at_5_std
      value: -2.3021
    - type: nauc_ndcg_at_5_diff1
      value: 53.8186
    - type: nauc_ndcg_at_10_max
      value: 20.5654
    - type: nauc_ndcg_at_10_std
      value: -0.2084
    - type: nauc_ndcg_at_10_diff1
      value: 46.2555
    - type: nauc_ndcg_at_20_max
      value: 18.3581
    - type: nauc_ndcg_at_20_std
      value: 7.5809
    - type: nauc_ndcg_at_20_diff1
      value: 39.1175
    - type: nauc_ndcg_at_100_max
      value: 23.2254
    - type: nauc_ndcg_at_100_std
      value: 4.8341
    - type: nauc_ndcg_at_100_diff1
      value: 45.2908
    - type: nauc_ndcg_at_1000_max
      value: 23.2254
    - type: nauc_ndcg_at_1000_std
      value: 4.8341
    - type: nauc_ndcg_at_1000_diff1
      value: 45.2908
    - type: nauc_map_at_1_max
      value: 59.715700000000005
    - type: nauc_map_at_1_std
      value: 37.2948
    - type: nauc_map_at_1_diff1
      value: 77.5791
    - type: nauc_map_at_3_max
      value: 37.5253
    - type: nauc_map_at_3_std
      value: 7.3128
    - type: nauc_map_at_3_diff1
      value: 52.1115
    - type: nauc_map_at_5_max
      value: 31.4148
    - type: nauc_map_at_5_std
      value: 2.8417000000000003
    - type: nauc_map_at_5_diff1
      value: 55.038399999999996
    - type: nauc_map_at_10_max
      value: 27.1445
    - type: nauc_map_at_10_std
      value: 3.4858000000000002
    - type: nauc_map_at_10_diff1
      value: 50.8304
    - type: nauc_map_at_20_max
      value: 25.901000000000003
    - type: nauc_map_at_20_std
      value: 6.0125
    - type: nauc_map_at_20_diff1
      value: 48.234500000000004
    - type: nauc_map_at_100_max
      value: 26.7912
    - type: nauc_map_at_100_std
      value: 5.5458
    - type: nauc_map_at_100_diff1
      value: 49.1744
    - type: nauc_map_at_1000_max
      value: 26.7912
    - type: nauc_map_at_1000_std
      value: 5.5458
    - type: nauc_map_at_1000_diff1
      value: 49.1744
    - type: nauc_recall_at_1_max
      value: 59.715700000000005
    - type: nauc_recall_at_1_std
      value: 37.2948
    - type: nauc_recall_at_1_diff1
      value: 77.5791
    - type: nauc_recall_at_3_max
      value: 32.4424
    - type: nauc_recall_at_3_std
      value: -1.7395999999999998
    - type: nauc_recall_at_3_diff1
      value: 42.067
    - type: nauc_recall_at_5_max
      value: 18.4679
    - type: nauc_recall_at_5_std
      value: -10.892
    - type: nauc_recall_at_5_diff1
      value: 52.4896
    - type: nauc_recall_at_10_max
      value: 10.9455
    - type: nauc_recall_at_10_std
      value: -4.9153
    - type: nauc_recall_at_10_diff1
      value: 39.267
    - type: nauc_recall_at_20_max
      value: 8.365599999999999
    - type: nauc_recall_at_20_std
      value: 13.2074
    - type: nauc_recall_at_20_diff1
      value: 24.5364
    - type: nauc_recall_at_100_max
      value: .nan
    - type: nauc_recall_at_100_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 59.715700000000005
    - type: nauc_precision_at_1_std
      value: 37.2948
    - type: nauc_precision_at_1_diff1
      value: 77.5791
    - type: nauc_precision_at_3_max
      value: 32.4424
    - type: nauc_precision_at_3_std
      value: -1.7395999999999998
    - type: nauc_precision_at_3_diff1
      value: 42.067
    - type: nauc_precision_at_5_max
      value: 18.4679
    - type: nauc_precision_at_5_std
      value: -10.892
    - type: nauc_precision_at_5_diff1
      value: 52.4896
    - type: nauc_precision_at_10_max
      value: 10.9455
    - type: nauc_precision_at_10_std
      value: -4.9153
    - type: nauc_precision_at_10_diff1
      value: 39.267
    - type: nauc_precision_at_20_max
      value: 8.365599999999999
    - type: nauc_precision_at_20_std
      value: 13.2074
    - type: nauc_precision_at_20_diff1
      value: 24.5364
    - type: nauc_precision_at_100_max
      value: 100.0
    - type: nauc_precision_at_100_std
      value: 100.0
    - type: nauc_precision_at_100_diff1
      value: 100.0
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: 59.715700000000005
    - type: nauc_mrr_at_1_std
      value: 37.2948
    - type: nauc_mrr_at_1_diff1
      value: 77.5791
    - type: nauc_mrr_at_3_max
      value: 37.5253
    - type: nauc_mrr_at_3_std
      value: 7.3128
    - type: nauc_mrr_at_3_diff1
      value: 52.1115
    - type: nauc_mrr_at_5_max
      value: 31.4148
    - type: nauc_mrr_at_5_std
      value: 2.8417000000000003
    - type: nauc_mrr_at_5_diff1
      value: 55.038399999999996
    - type: nauc_mrr_at_10_max
      value: 27.1445
    - type: nauc_mrr_at_10_std
      value: 3.4858000000000002
    - type: nauc_mrr_at_10_diff1
      value: 50.8304
    - type: nauc_mrr_at_20_max
      value: 25.901000000000003
    - type: nauc_mrr_at_20_std
      value: 6.0125
    - type: nauc_mrr_at_20_diff1
      value: 48.234500000000004
    - type: nauc_mrr_at_100_max
      value: 26.7912
    - type: nauc_mrr_at_100_std
      value: 5.5458
    - type: nauc_mrr_at_100_diff1
      value: 49.1744
    - type: nauc_mrr_at_1000_max
      value: 26.7912
    - type: nauc_mrr_at_1000_std
      value: 5.5458
    - type: nauc_mrr_at_1000_diff1
      value: 49.1744
    - type: main_score
      value: 12.396
    task:
      type: Retrieval
  - dataset:
      config: chinese
      name: MTEB PublicHealthQA (chinese)
      revision: main
      split: test
      type: xhluca/publichealth-qa
    metrics:
    - type: ndcg_at_1
      value: 17.791
    - type: ndcg_at_3
      value: 23.809
    - type: ndcg_at_5
      value: 26.344
    - type: ndcg_at_10
      value: 29.694
    - type: ndcg_at_20
      value: 32.551
    - type: ndcg_at_100
      value: 38.822
    - type: ndcg_at_1000
      value: 40.119
    - type: map_at_1
      value: 17.791
    - type: map_at_3
      value: 22.29
    - type: map_at_5
      value: 23.701
    - type: map_at_10
      value: 25.070999999999998
    - type: map_at_20
      value: 25.889
    - type: map_at_100
      value: 26.680999999999997
    - type: map_at_1000
      value: 26.749000000000002
    - type: recall_at_1
      value: 17.791
    - type: recall_at_3
      value: 28.221
    - type: recall_at_5
      value: 34.355999999999995
    - type: recall_at_10
      value: 44.785000000000004
    - type: recall_at_20
      value: 55.828
    - type: recall_at_100
      value: 90.798
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 17.791
    - type: precision_at_3
      value: 9.407
    - type: precision_at_5
      value: 6.8709999999999996
    - type: precision_at_10
      value: 4.479
    - type: precision_at_20
      value: 2.791
    - type: precision_at_100
      value: 0.9079999999999999
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 17.7914
    - type: mrr_at_3
      value: 22.290399999999998
    - type: mrr_at_5
      value: 23.7014
    - type: mrr_at_10
      value: 25.0711
    - type: mrr_at_20
      value: 25.8893
    - type: mrr_at_100
      value: 26.6812
    - type: mrr_at_1000
      value: 26.7494
    - type: nauc_ndcg_at_1_max
      value: 29.8804
    - type: nauc_ndcg_at_1_std
      value: 6.9849
    - type: nauc_ndcg_at_1_diff1
      value: 42.0644
    - type: nauc_ndcg_at_3_max
      value: 26.8668
    - type: nauc_ndcg_at_3_std
      value: 5.0143
    - type: nauc_ndcg_at_3_diff1
      value: 36.0569
    - type: nauc_ndcg_at_5_max
      value: 27.4273
    - type: nauc_ndcg_at_5_std
      value: 8.097999999999999
    - type: nauc_ndcg_at_5_diff1
      value: 31.8002
    - type: nauc_ndcg_at_10_max
      value: 26.9388
    - type: nauc_ndcg_at_10_std
      value: 8.001999999999999
    - type: nauc_ndcg_at_10_diff1
      value: 28.4373
    - type: nauc_ndcg_at_20_max
      value: 27.6432
    - type: nauc_ndcg_at_20_std
      value: 10.1775
    - type: nauc_ndcg_at_20_diff1
      value: 28.0765
    - type: nauc_ndcg_at_100_max
      value: 27.2202
    - type: nauc_ndcg_at_100_std
      value: 8.144400000000001
    - type: nauc_ndcg_at_100_diff1
      value: 31.2131
    - type: nauc_ndcg_at_1000_max
      value: 27.6147
    - type: nauc_ndcg_at_1000_std
      value: 8.203100000000001
    - type: nauc_ndcg_at_1000_diff1
      value: 31.8949
    - type: nauc_map_at_1_max
      value: 29.8804
    - type: nauc_map_at_1_std
      value: 6.9849
    - type: nauc_map_at_1_diff1
      value: 42.0644
    - type: nauc_map_at_3_max
      value: 27.971
    - type: nauc_map_at_3_std
      value: 5.8834
    - type: nauc_map_at_3_diff1
      value: 37.4543
    - type: nauc_map_at_5_max
      value: 28.3068
    - type: nauc_map_at_5_std
      value: 7.7293
    - type: nauc_map_at_5_diff1
      value: 34.9238
    - type: nauc_map_at_10_max
      value: 28.1389
    - type: nauc_map_at_10_std
      value: 7.6501
    - type: nauc_map_at_10_diff1
      value: 33.5384
    - type: nauc_map_at_20_max
      value: 28.363
    - type: nauc_map_at_20_std
      value: 8.2814
    - type: nauc_map_at_20_diff1
      value: 33.5464
    - type: nauc_map_at_100_max
      value: 28.2036
    - type: nauc_map_at_100_std
      value: 7.8896
    - type: nauc_map_at_100_diff1
      value: 34.0184
    - type: nauc_map_at_1000_max
      value: 28.2323
    - type: nauc_map_at_1000_std
      value: 7.8995
    - type: nauc_map_at_1000_diff1
      value: 34.050599999999996
    - type: nauc_recall_at_1_max
      value: 29.8804
    - type: nauc_recall_at_1_std
      value: 6.9849
    - type: nauc_recall_at_1_diff1
      value: 42.0644
    - type: nauc_recall_at_3_max
      value: 23.8995
    - type: nauc_recall_at_3_std
      value: 2.6474
    - type: nauc_recall_at_3_diff1
      value: 32.4726
    - type: nauc_recall_at_5_max
      value: 25.1623
    - type: nauc_recall_at_5_std
      value: 9.1546
    - type: nauc_recall_at_5_diff1
      value: 23.6453
    - type: nauc_recall_at_10_max
      value: 23.647199999999998
    - type: nauc_recall_at_10_std
      value: 9.0445
    - type: nauc_recall_at_10_diff1
      value: 14.225299999999999
    - type: nauc_recall_at_20_max
      value: 25.882699999999996
    - type: nauc_recall_at_20_std
      value: 17.0687
    - type: nauc_recall_at_20_diff1
      value: 11.1392
    - type: nauc_recall_at_100_max
      value: 20.4424
    - type: nauc_recall_at_100_std
      value: 7.8594
    - type: nauc_recall_at_100_diff1
      value: 17.3056
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 29.8804
    - type: nauc_precision_at_1_std
      value: 6.9849
    - type: nauc_precision_at_1_diff1
      value: 42.0644
    - type: nauc_precision_at_3_max
      value: 23.8995
    - type: nauc_precision_at_3_std
      value: 2.6474
    - type: nauc_precision_at_3_diff1
      value: 32.4726
    - type: nauc_precision_at_5_max
      value: 25.1623
    - type: nauc_precision_at_5_std
      value: 9.1546
    - type: nauc_precision_at_5_diff1
      value: 23.6453
    - type: nauc_precision_at_10_max
      value: 23.647199999999998
    - type: nauc_precision_at_10_std
      value: 9.0445
    - type: nauc_precision_at_10_diff1
      value: 14.225299999999999
    - type: nauc_precision_at_20_max
      value: 25.882699999999996
    - type: nauc_precision_at_20_std
      value: 17.0687
    - type: nauc_precision_at_20_diff1
      value: 11.1392
    - type: nauc_precision_at_100_max
      value: 20.4424
    - type: nauc_precision_at_100_std
      value: 7.8594
    - type: nauc_precision_at_100_diff1
      value: 17.3056
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: 29.8804
    - type: nauc_mrr_at_1_std
      value: 6.9849
    - type: nauc_mrr_at_1_diff1
      value: 42.0644
    - type: nauc_mrr_at_3_max
      value: 27.971
    - type: nauc_mrr_at_3_std
      value: 5.8834
    - type: nauc_mrr_at_3_diff1
      value: 37.4543
    - type: nauc_mrr_at_5_max
      value: 28.3068
    - type: nauc_mrr_at_5_std
      value: 7.7293
    - type: nauc_mrr_at_5_diff1
      value: 34.9238
    - type: nauc_mrr_at_10_max
      value: 28.1389
    - type: nauc_mrr_at_10_std
      value: 7.6501
    - type: nauc_mrr_at_10_diff1
      value: 33.5384
    - type: nauc_mrr_at_20_max
      value: 28.363
    - type: nauc_mrr_at_20_std
      value: 8.2814
    - type: nauc_mrr_at_20_diff1
      value: 33.5464
    - type: nauc_mrr_at_100_max
      value: 28.2036
    - type: nauc_mrr_at_100_std
      value: 7.8896
    - type: nauc_mrr_at_100_diff1
      value: 34.0184
    - type: nauc_mrr_at_1000_max
      value: 28.2323
    - type: nauc_mrr_at_1000_std
      value: 7.8995
    - type: nauc_mrr_at_1000_diff1
      value: 34.050599999999996
    - type: main_score
      value: 29.694
    task:
      type: Retrieval
  - dataset:
      config: english
      name: MTEB PublicHealthQA (english)
      revision: main
      split: test
      type: xhluca/publichealth-qa
    metrics:
    - type: ndcg_at_1
      value: 68.605
    - type: ndcg_at_3
      value: 79.063
    - type: ndcg_at_5
      value: 80.989
    - type: ndcg_at_10
      value: 82.368
    - type: ndcg_at_20
      value: 82.816
    - type: ndcg_at_100
      value: 83.246
    - type: ndcg_at_1000
      value: 83.327
    - type: map_at_1
      value: 68.605
    - type: map_at_3
      value: 76.453
    - type: map_at_5
      value: 77.529
    - type: map_at_10
      value: 78.13600000000001
    - type: map_at_20
      value: 78.263
    - type: map_at_100
      value: 78.322
    - type: map_at_1000
      value: 78.326
    - type: recall_at_1
      value: 68.605
    - type: recall_at_3
      value: 86.628
    - type: recall_at_5
      value: 91.279
    - type: recall_at_10
      value: 95.34899999999999
    - type: recall_at_20
      value: 97.09299999999999
    - type: recall_at_100
      value: 99.419
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 68.605
    - type: precision_at_3
      value: 28.876
    - type: precision_at_5
      value: 18.256
    - type: precision_at_10
      value: 9.535
    - type: precision_at_20
      value: 4.855
    - type: precision_at_100
      value: 0.9939999999999999
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 68.6047
    - type: mrr_at_3
      value: 76.45349999999999
    - type: mrr_at_5
      value: 77.5291
    - type: mrr_at_10
      value: 78.1363
    - type: mrr_at_20
      value: 78.2626
    - type: mrr_at_100
      value: 78.322
    - type: mrr_at_1000
      value: 78.3261
    - type: nauc_ndcg_at_1_max
      value: 39.230399999999996
    - type: nauc_ndcg_at_1_std
      value: -14.3013
    - type: nauc_ndcg_at_1_diff1
      value: 63.6784
    - type: nauc_ndcg_at_3_max
      value: 42.6008
    - type: nauc_ndcg_at_3_std
      value: -14.300699999999999
    - type: nauc_ndcg_at_3_diff1
      value: 59.948
    - type: nauc_ndcg_at_5_max
      value: 44.91
    - type: nauc_ndcg_at_5_std
      value: -8.611099999999999
    - type: nauc_ndcg_at_5_diff1
      value: 60.5873
    - type: nauc_ndcg_at_10_max
      value: 43.5913
    - type: nauc_ndcg_at_10_std
      value: -11.4792
    - type: nauc_ndcg_at_10_diff1
      value: 60.8896
    - type: nauc_ndcg_at_20_max
      value: 44.405699999999996
    - type: nauc_ndcg_at_20_std
      value: -9.0507
    - type: nauc_ndcg_at_20_diff1
      value: 60.295100000000005
    - type: nauc_ndcg_at_100_max
      value: 43.6858
    - type: nauc_ndcg_at_100_std
      value: -10.0097
    - type: nauc_ndcg_at_100_diff1
      value: 61.163900000000005
    - type: nauc_ndcg_at_1000_max
      value: 43.375
    - type: nauc_ndcg_at_1000_std
      value: -10.617
    - type: nauc_ndcg_at_1000_diff1
      value: 61.021499999999996
    - type: nauc_map_at_1_max
      value: 39.230399999999996
    - type: nauc_map_at_1_std
      value: -14.3013
    - type: nauc_map_at_1_diff1
      value: 63.6784
    - type: nauc_map_at_3_max
      value: 41.875
    - type: nauc_map_at_3_std
      value: -13.911299999999999
    - type: nauc_map_at_3_diff1
      value: 61.1028
    - type: nauc_map_at_5_max
      value: 43.0246
    - type: nauc_map_at_5_std
      value: -10.9924
    - type: nauc_map_at_5_diff1
      value: 61.381600000000006
    - type: nauc_map_at_10_max
      value: 42.5303
    - type: nauc_map_at_10_std
      value: -12.0992
    - type: nauc_map_at_10_diff1
      value: 61.5417
    - type: nauc_map_at_20_max
      value: 42.7267
    - type: nauc_map_at_20_std
      value: -11.5421
    - type: nauc_map_at_20_diff1
      value: 61.4179
    - type: nauc_map_at_100_max
      value: 42.653200000000005
    - type: nauc_map_at_100_std
      value: -11.5826
    - type: nauc_map_at_100_diff1
      value: 61.47709999999999
    - type: nauc_map_at_1000_max
      value: 42.640899999999995
    - type: nauc_map_at_1000_std
      value: -11.6066
    - type: nauc_map_at_1000_diff1
      value: 61.4717
    - type: nauc_recall_at_1_max
      value: 39.230399999999996
    - type: nauc_recall_at_1_std
      value: -14.3013
    - type: nauc_recall_at_1_diff1
      value: 63.6784
    - type: nauc_recall_at_3_max
      value: 45.7626
    - type: nauc_recall_at_3_std
      value: -16.3689
    - type: nauc_recall_at_3_diff1
      value: 54.581599999999995
    - type: nauc_recall_at_5_max
      value: 57.456700000000005
    - type: nauc_recall_at_5_std
      value: 7.8857
    - type: nauc_recall_at_5_diff1
      value: 55.8095
    - type: nauc_recall_at_10_max
      value: 54.461999999999996
    - type: nauc_recall_at_10_std
      value: -6.1557
    - type: nauc_recall_at_10_diff1
      value: 54.03980000000001
    - type: nauc_recall_at_20_max
      value: 76.5834
    - type: nauc_recall_at_20_std
      value: 45.8102
    - type: nauc_recall_at_20_diff1
      value: 37.551
    - type: nauc_recall_at_100_max
      value: 100.0
    - type: nauc_recall_at_100_std
      value: 100.0
    - type: nauc_recall_at_100_diff1
      value: 86.945
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 39.230399999999996
    - type: nauc_precision_at_1_std
      value: -14.3013
    - type: nauc_precision_at_1_diff1
      value: 63.6784
    - type: nauc_precision_at_3_max
      value: 45.7626
    - type: nauc_precision_at_3_std
      value: -16.3689
    - type: nauc_precision_at_3_diff1
      value: 54.581599999999995
    - type: nauc_precision_at_5_max
      value: 57.456700000000005
    - type: nauc_precision_at_5_std
      value: 7.8857
    - type: nauc_precision_at_5_diff1
      value: 55.8095
    - type: nauc_precision_at_10_max
      value: 54.461999999999996
    - type: nauc_precision_at_10_std
      value: -6.1557
    - type: nauc_precision_at_10_diff1
      value: 54.03980000000001
    - type: nauc_precision_at_20_max
      value: 76.5834
    - type: nauc_precision_at_20_std
      value: 45.8102
    - type: nauc_precision_at_20_diff1
      value: 37.551
    - type: nauc_precision_at_100_max
      value: 100.0
    - type: nauc_precision_at_100_std
      value: 100.0
    - type: nauc_precision_at_100_diff1
      value: 86.945
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: 39.230399999999996
    - type: nauc_mrr_at_1_std
      value: -14.3013
    - type: nauc_mrr_at_1_diff1
      value: 63.6784
    - type: nauc_mrr_at_3_max
      value: 41.875
    - type: nauc_mrr_at_3_std
      value: -13.911299999999999
    - type: nauc_mrr_at_3_diff1
      value: 61.1028
    - type: nauc_mrr_at_5_max
      value: 43.0246
    - type: nauc_mrr_at_5_std
      value: -10.9924
    - type: nauc_mrr_at_5_diff1
      value: 61.381600000000006
    - type: nauc_mrr_at_10_max
      value: 42.5303
    - type: nauc_mrr_at_10_std
      value: -12.0992
    - type: nauc_mrr_at_10_diff1
      value: 61.5417
    - type: nauc_mrr_at_20_max
      value: 42.7267
    - type: nauc_mrr_at_20_std
      value: -11.5421
    - type: nauc_mrr_at_20_diff1
      value: 61.4179
    - type: nauc_mrr_at_100_max
      value: 42.653200000000005
    - type: nauc_mrr_at_100_std
      value: -11.5826
    - type: nauc_mrr_at_100_diff1
      value: 61.47709999999999
    - type: nauc_mrr_at_1000_max
      value: 42.640899999999995
    - type: nauc_mrr_at_1000_std
      value: -11.6064
    - type: nauc_mrr_at_1000_diff1
      value: 61.4717
    - type: main_score
      value: 82.368
    task:
      type: Retrieval
  - dataset:
      config: french
      name: MTEB PublicHealthQA (french)
      revision: main
      split: test
      type: xhluca/publichealth-qa
    metrics:
    - type: ndcg_at_1
      value: 57.647000000000006
    - type: ndcg_at_3
      value: 68.16499999999999
    - type: ndcg_at_5
      value: 70.14
    - type: ndcg_at_10
      value: 74.08500000000001
    - type: ndcg_at_20
      value: 75.297
    - type: ndcg_at_100
      value: 75.97699999999999
    - type: ndcg_at_1000
      value: 75.97699999999999
    - type: map_at_1
      value: 57.647000000000006
    - type: map_at_3
      value: 65.686
    - type: map_at_5
      value: 66.804
    - type: map_at_10
      value: 68.516
    - type: map_at_20
      value: 68.86
    - type: map_at_100
      value: 68.959
    - type: map_at_1000
      value: 68.959
    - type: recall_at_1
      value: 57.647000000000006
    - type: recall_at_3
      value: 75.29400000000001
    - type: recall_at_5
      value: 80.0
    - type: recall_at_10
      value: 91.765
    - type: recall_at_20
      value: 96.47099999999999
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 57.647000000000006
    - type: precision_at_3
      value: 25.098
    - type: precision_at_5
      value: 16.0
    - type: precision_at_10
      value: 9.176
    - type: precision_at_20
      value: 4.824
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 57.647099999999995
    - type: mrr_at_3
      value: 65.6863
    - type: mrr_at_5
      value: 66.8039
    - type: mrr_at_10
      value: 68.5159
    - type: mrr_at_20
      value: 68.8596
    - type: mrr_at_100
      value: 68.9587
    - type: mrr_at_1000
      value: 68.9587
    - type: nauc_ndcg_at_1_max
      value: 36.299
    - type: nauc_ndcg_at_1_std
      value: -0.31129999999999997
    - type: nauc_ndcg_at_1_diff1
      value: 52.98349999999999
    - type: nauc_ndcg_at_3_max
      value: 30.7772
    - type: nauc_ndcg_at_3_std
      value: 15.1285
    - type: nauc_ndcg_at_3_diff1
      value: 42.4886
    - type: nauc_ndcg_at_5_max
      value: 34.1327
    - type: nauc_ndcg_at_5_std
      value: 17.4173
    - type: nauc_ndcg_at_5_diff1
      value: 42.7984
    - type: nauc_ndcg_at_10_max
      value: 38.8615
    - type: nauc_ndcg_at_10_std
      value: 17.1227
    - type: nauc_ndcg_at_10_diff1
      value: 50.4977
    - type: nauc_ndcg_at_20_max
      value: 37.0022
    - type: nauc_ndcg_at_20_std
      value: 13.7289
    - type: nauc_ndcg_at_20_diff1
      value: 48.4148
    - type: nauc_ndcg_at_100_max
      value: 35.965
    - type: nauc_ndcg_at_100_std
      value: 12.9999
    - type: nauc_ndcg_at_100_diff1
      value: 47.7781
    - type: nauc_ndcg_at_1000_max
      value: 35.965
    - type: nauc_ndcg_at_1000_std
      value: 12.9999
    - type: nauc_ndcg_at_1000_diff1
      value: 47.7781
    - type: nauc_map_at_1_max
      value: 36.299
    - type: nauc_map_at_1_std
      value: -0.31129999999999997
    - type: nauc_map_at_1_diff1
      value: 52.98349999999999
    - type: nauc_map_at_3_max
      value: 32.4585
    - type: nauc_map_at_3_std
      value: 11.4142
    - type: nauc_map_at_3_diff1
      value: 44.913
    - type: nauc_map_at_5_max
      value: 34.2207
    - type: nauc_map_at_5_std
      value: 12.4555
    - type: nauc_map_at_5_diff1
      value: 45.1962
    - type: nauc_map_at_10_max
      value: 36.0741
    - type: nauc_map_at_10_std
      value: 12.3794
    - type: nauc_map_at_10_diff1
      value: 48.3191
    - type: nauc_map_at_20_max
      value: 35.6485
    - type: nauc_map_at_20_std
      value: 11.5573
    - type: nauc_map_at_20_diff1
      value: 47.8261
    - type: nauc_map_at_100_max
      value: 35.5227
    - type: nauc_map_at_100_std
      value: 11.4605
    - type: nauc_map_at_100_diff1
      value: 47.7512
    - type: nauc_map_at_1000_max
      value: 35.5227
    - type: nauc_map_at_1000_std
      value: 11.4605
    - type: nauc_map_at_1000_diff1
      value: 47.7512
    - type: nauc_recall_at_1_max
      value: 36.299
    - type: nauc_recall_at_1_std
      value: -0.31129999999999997
    - type: nauc_recall_at_1_diff1
      value: 52.98349999999999
    - type: nauc_recall_at_3_max
      value: 24.5979
    - type: nauc_recall_at_3_std
      value: 28.3054
    - type: nauc_recall_at_3_diff1
      value: 33.9486
    - type: nauc_recall_at_5_max
      value: 34.3725
    - type: nauc_recall_at_5_std
      value: 38.2391
    - type: nauc_recall_at_5_diff1
      value: 33.080999999999996
    - type: nauc_recall_at_10_max
      value: 69.187
    - type: nauc_recall_at_10_std
      value: 57.02739999999999
    - type: nauc_recall_at_10_diff1
      value: 77.4776
    - type: nauc_recall_at_20_max
      value: 66.5024
    - type: nauc_recall_at_20_std
      value: 34.1342
    - type: nauc_recall_at_20_diff1
      value: 66.6574
    - type: nauc_recall_at_100_max
      value: .nan
    - type: nauc_recall_at_100_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 36.299
    - type: nauc_precision_at_1_std
      value: -0.31129999999999997
    - type: nauc_precision_at_1_diff1
      value: 52.98349999999999
    - type: nauc_precision_at_3_max
      value: 24.5979
    - type: nauc_precision_at_3_std
      value: 28.3054
    - type: nauc_precision_at_3_diff1
      value: 33.9486
    - type: nauc_precision_at_5_max
      value: 34.3725
    - type: nauc_precision_at_5_std
      value: 38.2391
    - type: nauc_precision_at_5_diff1
      value: 33.080999999999996
    - type: nauc_precision_at_10_max
      value: 69.187
    - type: nauc_precision_at_10_std
      value: 57.02739999999999
    - type: nauc_precision_at_10_diff1
      value: 77.4776
    - type: nauc_precision_at_20_max
      value: 66.5024
    - type: nauc_precision_at_20_std
      value: 34.1342
    - type: nauc_precision_at_20_diff1
      value: 66.6574
    - type: nauc_precision_at_100_max
      value: 100.0
    - type: nauc_precision_at_100_std
      value: 100.0
    - type: nauc_precision_at_100_diff1
      value: 100.0
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: 36.299
    - type: nauc_mrr_at_1_std
      value: -0.31129999999999997
    - type: nauc_mrr_at_1_diff1
      value: 52.98349999999999
    - type: nauc_mrr_at_3_max
      value: 32.4585
    - type: nauc_mrr_at_3_std
      value: 11.4142
    - type: nauc_mrr_at_3_diff1
      value: 44.913
    - type: nauc_mrr_at_5_max
      value: 34.2207
    - type: nauc_mrr_at_5_std
      value: 12.4555
    - type: nauc_mrr_at_5_diff1
      value: 45.1962
    - type: nauc_mrr_at_10_max
      value: 36.0741
    - type: nauc_mrr_at_10_std
      value: 12.3794
    - type: nauc_mrr_at_10_diff1
      value: 48.3191
    - type: nauc_mrr_at_20_max
      value: 35.6485
    - type: nauc_mrr_at_20_std
      value: 11.5573
    - type: nauc_mrr_at_20_diff1
      value: 47.8261
    - type: nauc_mrr_at_100_max
      value: 35.5227
    - type: nauc_mrr_at_100_std
      value: 11.4605
    - type: nauc_mrr_at_100_diff1
      value: 47.7512
    - type: nauc_mrr_at_1000_max
      value: 35.5227
    - type: nauc_mrr_at_1000_std
      value: 11.4605
    - type: nauc_mrr_at_1000_diff1
      value: 47.7512
    - type: main_score
      value: 74.08500000000001
    task:
      type: Retrieval
  - dataset:
      config: korean
      name: MTEB PublicHealthQA (korean)
      revision: main
      split: test
      type: xhluca/publichealth-qa
    metrics:
    - type: ndcg_at_1
      value: 15.584000000000001
    - type: ndcg_at_3
      value: 25.046000000000003
    - type: ndcg_at_5
      value: 30.857
    - type: ndcg_at_10
      value: 34.729
    - type: ndcg_at_20
      value: 38.313
    - type: ndcg_at_100
      value: 43.254999999999995
    - type: ndcg_at_1000
      value: 43.254999999999995
    - type: map_at_1
      value: 15.584000000000001
    - type: map_at_3
      value: 22.511
    - type: map_at_5
      value: 25.692999999999998
    - type: map_at_10
      value: 27.35
    - type: map_at_20
      value: 28.317999999999998
    - type: map_at_100
      value: 28.947
    - type: map_at_1000
      value: 28.947
    - type: recall_at_1
      value: 15.584000000000001
    - type: recall_at_3
      value: 32.468
    - type: recall_at_5
      value: 46.753
    - type: recall_at_10
      value: 58.44200000000001
    - type: recall_at_20
      value: 72.727
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 15.584000000000001
    - type: precision_at_3
      value: 10.823
    - type: precision_at_5
      value: 9.350999999999999
    - type: precision_at_10
      value: 5.844
    - type: precision_at_20
      value: 3.636
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 15.5844
    - type: mrr_at_3
      value: 22.5108
    - type: mrr_at_5
      value: 25.6926
    - type: mrr_at_10
      value: 27.35
    - type: mrr_at_20
      value: 28.3185
    - type: mrr_at_100
      value: 28.9469
    - type: mrr_at_1000
      value: 28.9469
    - type: nauc_ndcg_at_1_max
      value: 22.6619
    - type: nauc_ndcg_at_1_std
      value: 26.3584
    - type: nauc_ndcg_at_1_diff1
      value: 30.0107
    - type: nauc_ndcg_at_3_max
      value: 26.0589
    - type: nauc_ndcg_at_3_std
      value: 27.4435
    - type: nauc_ndcg_at_3_diff1
      value: 20.6848
    - type: nauc_ndcg_at_5_max
      value: 29.0957
    - type: nauc_ndcg_at_5_std
      value: 28.6226
    - type: nauc_ndcg_at_5_diff1
      value: 12.873999999999999
    - type: nauc_ndcg_at_10_max
      value: 22.5377
    - type: nauc_ndcg_at_10_std
      value: 22.9366
    - type: nauc_ndcg_at_10_diff1
      value: 6.500100000000001
    - type: nauc_ndcg_at_20_max
      value: 23.9022
    - type: nauc_ndcg_at_20_std
      value: 25.572499999999998
    - type: nauc_ndcg_at_20_diff1
      value: 10.0398
    - type: nauc_ndcg_at_100_max
      value: 24.9972
    - type: nauc_ndcg_at_100_std
      value: 26.282299999999996
    - type: nauc_ndcg_at_100_diff1
      value: 14.2371
    - type: nauc_ndcg_at_1000_max
      value: 24.9972
    - type: nauc_ndcg_at_1000_std
      value: 26.282299999999996
    - type: nauc_ndcg_at_1000_diff1
      value: 14.2371
    - type: nauc_map_at_1_max
      value: 22.6619
    - type: nauc_map_at_1_std
      value: 26.3584
    - type: nauc_map_at_1_diff1
      value: 30.0107
    - type: nauc_map_at_3_max
      value: 25.584600000000002
    - type: nauc_map_at_3_std
      value: 27.6868
    - type: nauc_map_at_3_diff1
      value: 22.831599999999998
    - type: nauc_map_at_5_max
      value: 27.417399999999997
    - type: nauc_map_at_5_std
      value: 28.5693
    - type: nauc_map_at_5_diff1
      value: 18.212999999999997
    - type: nauc_map_at_10_max
      value: 24.4972
    - type: nauc_map_at_10_std
      value: 25.991500000000002
    - type: nauc_map_at_10_diff1
      value: 15.3749
    - type: nauc_map_at_20_max
      value: 24.8498
    - type: nauc_map_at_20_std
      value: 26.7085
    - type: nauc_map_at_20_diff1
      value: 16.4134
    - type: nauc_map_at_100_max
      value: 25.1019
    - type: nauc_map_at_100_std
      value: 26.8269
    - type: nauc_map_at_100_diff1
      value: 17.0376
    - type: nauc_map_at_1000_max
      value: 25.1019
    - type: nauc_map_at_1000_std
      value: 26.8269
    - type: nauc_map_at_1000_diff1
      value: 17.0376
    - type: nauc_recall_at_1_max
      value: 22.6619
    - type: nauc_recall_at_1_std
      value: 26.3584
    - type: nauc_recall_at_1_diff1
      value: 30.0107
    - type: nauc_recall_at_3_max
      value: 27.1171
    - type: nauc_recall_at_3_std
      value: 26.706400000000002
    - type: nauc_recall_at_3_diff1
      value: 15.479499999999998
    - type: nauc_recall_at_5_max
      value: 33.3129
    - type: nauc_recall_at_5_std
      value: 28.5407
    - type: nauc_recall_at_5_diff1
      value: -0.7628
    - type: nauc_recall_at_10_max
      value: 15.459100000000001
    - type: nauc_recall_at_10_std
      value: 13.001199999999999
    - type: nauc_recall_at_10_diff1
      value: -19.4151
    - type: nauc_recall_at_20_max
      value: 19.689400000000003
    - type: nauc_recall_at_20_std
      value: 22.014300000000002
    - type: nauc_recall_at_20_diff1
      value: -11.3263
    - type: nauc_recall_at_100_max
      value: .nan
    - type: nauc_recall_at_100_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 22.6619
    - type: nauc_precision_at_1_std
      value: 26.3584
    - type: nauc_precision_at_1_diff1
      value: 30.0107
    - type: nauc_precision_at_3_max
      value: 27.1171
    - type: nauc_precision_at_3_std
      value: 26.706400000000002
    - type: nauc_precision_at_3_diff1
      value: 15.479499999999998
    - type: nauc_precision_at_5_max
      value: 33.3129
    - type: nauc_precision_at_5_std
      value: 28.5407
    - type: nauc_precision_at_5_diff1
      value: -0.7628
    - type: nauc_precision_at_10_max
      value: 15.459100000000001
    - type: nauc_precision_at_10_std
      value: 13.001199999999999
    - type: nauc_precision_at_10_diff1
      value: -19.4151
    - type: nauc_precision_at_20_max
      value: 19.689400000000003
    - type: nauc_precision_at_20_std
      value: 22.014300000000002
    - type: nauc_precision_at_20_diff1
      value: -11.3263
    - type: nauc_precision_at_100_max
      value: 100.0
    - type: nauc_precision_at_100_std
      value: 100.0
    - type: nauc_precision_at_100_diff1
      value: 100.0
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 22.6619
    - type: nauc_mrr_at_1_std
      value: 26.3584
    - type: nauc_mrr_at_1_diff1
      value: 30.0107
    - type: nauc_mrr_at_3_max
      value: 25.584600000000002
    - type: nauc_mrr_at_3_std
      value: 27.6868
    - type: nauc_mrr_at_3_diff1
      value: 22.831599999999998
    - type: nauc_mrr_at_5_max
      value: 27.417399999999997
    - type: nauc_mrr_at_5_std
      value: 28.5693
    - type: nauc_mrr_at_5_diff1
      value: 18.212999999999997
    - type: nauc_mrr_at_10_max
      value: 24.4972
    - type: nauc_mrr_at_10_std
      value: 25.991500000000002
    - type: nauc_mrr_at_10_diff1
      value: 15.3749
    - type: nauc_mrr_at_20_max
      value: 24.8498
    - type: nauc_mrr_at_20_std
      value: 26.7085
    - type: nauc_mrr_at_20_diff1
      value: 16.4134
    - type: nauc_mrr_at_100_max
      value: 25.1019
    - type: nauc_mrr_at_100_std
      value: 26.8269
    - type: nauc_mrr_at_100_diff1
      value: 17.0376
    - type: nauc_mrr_at_1000_max
      value: 25.1019
    - type: nauc_mrr_at_1000_std
      value: 26.8269
    - type: nauc_mrr_at_1000_diff1
      value: 17.0376
    - type: main_score
      value: 34.729
    task:
      type: Retrieval
  - dataset:
      config: russian
      name: MTEB PublicHealthQA (russian)
      revision: main
      split: test
      type: xhluca/publichealth-qa
    metrics:
    - type: ndcg_at_1
      value: 38.462
    - type: ndcg_at_3
      value: 39.432
    - type: ndcg_at_5
      value: 43.801
    - type: ndcg_at_10
      value: 47.365
    - type: ndcg_at_20
      value: 50.529
    - type: ndcg_at_100
      value: 55.525999999999996
    - type: ndcg_at_1000
      value: 55.525999999999996
    - type: map_at_1
      value: 38.462
    - type: map_at_3
      value: 39.231
    - type: map_at_5
      value: 41.615
    - type: map_at_10
      value: 43.134
    - type: map_at_20
      value: 44.027
    - type: map_at_100
      value: 44.762
    - type: map_at_1000
      value: 44.762
    - type: recall_at_1
      value: 38.462
    - type: recall_at_3
      value: 40.0
    - type: recall_at_5
      value: 50.769
    - type: recall_at_10
      value: 61.538000000000004
    - type: recall_at_20
      value: 73.846
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 38.462
    - type: precision_at_3
      value: 13.333
    - type: precision_at_5
      value: 10.154
    - type: precision_at_10
      value: 6.154
    - type: precision_at_20
      value: 3.692
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 38.4615
    - type: mrr_at_3
      value: 39.2308
    - type: mrr_at_5
      value: 41.6154
    - type: mrr_at_10
      value: 43.133700000000005
    - type: mrr_at_20
      value: 44.0268
    - type: mrr_at_100
      value: 44.7615
    - type: mrr_at_1000
      value: 44.7615
    - type: nauc_ndcg_at_1_max
      value: 35.7196
    - type: nauc_ndcg_at_1_std
      value: 31.128899999999998
    - type: nauc_ndcg_at_1_diff1
      value: 48.9534
    - type: nauc_ndcg_at_3_max
      value: 33.2144
    - type: nauc_ndcg_at_3_std
      value: 28.644599999999997
    - type: nauc_ndcg_at_3_diff1
      value: 53.3224
    - type: nauc_ndcg_at_5_max
      value: 35.9717
    - type: nauc_ndcg_at_5_std
      value: 34.1499
    - type: nauc_ndcg_at_5_diff1
      value: 53.568000000000005
    - type: nauc_ndcg_at_10_max
      value: 35.6701
    - type: nauc_ndcg_at_10_std
      value: 30.9807
    - type: nauc_ndcg_at_10_diff1
      value: 50.645799999999994
    - type: nauc_ndcg_at_20_max
      value: 37.1344
    - type: nauc_ndcg_at_20_std
      value: 31.297399999999996
    - type: nauc_ndcg_at_20_diff1
      value: 47.5693
    - type: nauc_ndcg_at_100_max
      value: 35.5966
    - type: nauc_ndcg_at_100_std
      value: 31.0317
    - type: nauc_ndcg_at_100_diff1
      value: 50.1695
    - type: nauc_ndcg_at_1000_max
      value: 35.5966
    - type: nauc_ndcg_at_1000_std
      value: 31.0317
    - type: nauc_ndcg_at_1000_diff1
      value: 50.1695
    - type: nauc_map_at_1_max
      value: 35.7196
    - type: nauc_map_at_1_std
      value: 31.128899999999998
    - type: nauc_map_at_1_diff1
      value: 48.9534
    - type: nauc_map_at_3_max
      value: 33.7324
    - type: nauc_map_at_3_std
      value: 29.158299999999997
    - type: nauc_map_at_3_diff1
      value: 52.419000000000004
    - type: nauc_map_at_5_max
      value: 35.1746
    - type: nauc_map_at_5_std
      value: 31.917
    - type: nauc_map_at_5_diff1
      value: 52.615100000000005
    - type: nauc_map_at_10_max
      value: 35.009299999999996
    - type: nauc_map_at_10_std
      value: 30.4855
    - type: nauc_map_at_10_diff1
      value: 51.4068
    - type: nauc_map_at_20_max
      value: 35.3619
    - type: nauc_map_at_20_std
      value: 30.5305
    - type: nauc_map_at_20_diff1
      value: 50.6054
    - type: nauc_map_at_100_max
      value: 35.1648
    - type: nauc_map_at_100_std
      value: 30.605300000000003
    - type: nauc_map_at_100_diff1
      value: 50.85809999999999
    - type: nauc_map_at_1000_max
      value: 35.1648
    - type: nauc_map_at_1000_std
      value: 30.605300000000003
    - type: nauc_map_at_1000_diff1
      value: 50.85809999999999
    - type: nauc_recall_at_1_max
      value: 35.7196
    - type: nauc_recall_at_1_std
      value: 31.128899999999998
    - type: nauc_recall_at_1_diff1
      value: 48.9534
    - type: nauc_recall_at_3_max
      value: 31.759500000000003
    - type: nauc_recall_at_3_std
      value: 27.2018
    - type: nauc_recall_at_3_diff1
      value: 55.859700000000004
    - type: nauc_recall_at_5_max
      value: 38.8865
    - type: nauc_recall_at_5_std
      value: 41.984
    - type: nauc_recall_at_5_diff1
      value: 56.2765
    - type: nauc_recall_at_10_max
      value: 38.400600000000004
    - type: nauc_recall_at_10_std
      value: 32.869
    - type: nauc_recall_at_10_diff1
      value: 46.7236
    - type: nauc_recall_at_20_max
      value: 47.502
    - type: nauc_recall_at_20_std
      value: 35.5301
    - type: nauc_recall_at_20_diff1
      value: 28.7689
    - type: nauc_recall_at_100_max
      value: .nan
    - type: nauc_recall_at_100_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 35.7196
    - type: nauc_precision_at_1_std
      value: 31.128899999999998
    - type: nauc_precision_at_1_diff1
      value: 48.9534
    - type: nauc_precision_at_3_max
      value: 31.759500000000003
    - type: nauc_precision_at_3_std
      value: 27.2018
    - type: nauc_precision_at_3_diff1
      value: 55.859700000000004
    - type: nauc_precision_at_5_max
      value: 38.8865
    - type: nauc_precision_at_5_std
      value: 41.984
    - type: nauc_precision_at_5_diff1
      value: 56.2765
    - type: nauc_precision_at_10_max
      value: 38.400600000000004
    - type: nauc_precision_at_10_std
      value: 32.869
    - type: nauc_precision_at_10_diff1
      value: 46.7236
    - type: nauc_precision_at_20_max
      value: 47.502
    - type: nauc_precision_at_20_std
      value: 35.5301
    - type: nauc_precision_at_20_diff1
      value: 28.7689
    - type: nauc_precision_at_100_max
      value: .nan
    - type: nauc_precision_at_100_std
      value: .nan
    - type: nauc_precision_at_100_diff1
      value: .nan
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: 35.7196
    - type: nauc_mrr_at_1_std
      value: 31.128899999999998
    - type: nauc_mrr_at_1_diff1
      value: 48.9534
    - type: nauc_mrr_at_3_max
      value: 33.7324
    - type: nauc_mrr_at_3_std
      value: 29.158299999999997
    - type: nauc_mrr_at_3_diff1
      value: 52.419000000000004
    - type: nauc_mrr_at_5_max
      value: 35.1746
    - type: nauc_mrr_at_5_std
      value: 31.917
    - type: nauc_mrr_at_5_diff1
      value: 52.615100000000005
    - type: nauc_mrr_at_10_max
      value: 35.009299999999996
    - type: nauc_mrr_at_10_std
      value: 30.4855
    - type: nauc_mrr_at_10_diff1
      value: 51.4068
    - type: nauc_mrr_at_20_max
      value: 35.3619
    - type: nauc_mrr_at_20_std
      value: 30.5305
    - type: nauc_mrr_at_20_diff1
      value: 50.6054
    - type: nauc_mrr_at_100_max
      value: 35.1648
    - type: nauc_mrr_at_100_std
      value: 30.605300000000003
    - type: nauc_mrr_at_100_diff1
      value: 50.85809999999999
    - type: nauc_mrr_at_1000_max
      value: 35.1648
    - type: nauc_mrr_at_1000_std
      value: 30.605300000000003
    - type: nauc_mrr_at_1000_diff1
      value: 50.85809999999999
    - type: main_score
      value: 47.365
    task:
      type: Retrieval
  - dataset:
      config: spanish
      name: MTEB PublicHealthQA (spanish)
      revision: main
      split: test
      type: xhluca/publichealth-qa
    metrics:
    - type: ndcg_at_1
      value: 39.506
    - type: ndcg_at_3
      value: 54.247
    - type: ndcg_at_5
      value: 57.541
    - type: ndcg_at_10
      value: 60.328
    - type: ndcg_at_20
      value: 62.331
    - type: ndcg_at_100
      value: 63.794
    - type: ndcg_at_1000
      value: 64.05999999999999
    - type: map_at_1
      value: 39.506
    - type: map_at_3
      value: 50.412
    - type: map_at_5
      value: 52.233
    - type: map_at_10
      value: 53.38
    - type: map_at_20
      value: 53.917
    - type: map_at_100
      value: 54.107000000000006
    - type: map_at_1000
      value: 54.122
    - type: recall_at_1
      value: 39.506
    - type: recall_at_3
      value: 65.432
    - type: recall_at_5
      value: 73.457
    - type: recall_at_10
      value: 82.099
    - type: recall_at_20
      value: 90.12299999999999
    - type: recall_at_100
      value: 98.148
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 39.506
    - type: precision_at_3
      value: 21.811
    - type: precision_at_5
      value: 14.691
    - type: precision_at_10
      value: 8.21
    - type: precision_at_20
      value: 4.506
    - type: precision_at_100
      value: 0.9809999999999999
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 39.5062
    - type: mrr_at_3
      value: 50.4115
    - type: mrr_at_5
      value: 52.2325
    - type: mrr_at_10
      value: 53.380399999999995
    - type: mrr_at_20
      value: 53.9174
    - type: mrr_at_100
      value: 54.1072
    - type: mrr_at_1000
      value: 54.122400000000006
    - type: nauc_ndcg_at_1_max
      value: 33.465
    - type: nauc_ndcg_at_1_std
      value: -4.077
    - type: nauc_ndcg_at_1_diff1
      value: 63.7579
    - type: nauc_ndcg_at_3_max
      value: 34.5067
    - type: nauc_ndcg_at_3_std
      value: -7.5327
    - type: nauc_ndcg_at_3_diff1
      value: 54.14020000000001
    - type: nauc_ndcg_at_5_max
      value: 35.6912
    - type: nauc_ndcg_at_5_std
      value: -0.911
    - type: nauc_ndcg_at_5_diff1
      value: 53.2654
    - type: nauc_ndcg_at_10_max
      value: 35.2651
    - type: nauc_ndcg_at_10_std
      value: -0.0039
    - type: nauc_ndcg_at_10_diff1
      value: 55.3022
    - type: nauc_ndcg_at_20_max
      value: 36.071799999999996
    - type: nauc_ndcg_at_20_std
      value: 1.6840000000000002
    - type: nauc_ndcg_at_20_diff1
      value: 55.6957
    - type: nauc_ndcg_at_100_max
      value: 35.964400000000005
    - type: nauc_ndcg_at_100_std
      value: -1.6336
    - type: nauc_ndcg_at_100_diff1
      value: 56.626
    - type: nauc_ndcg_at_1000_max
      value: 35.551899999999996
    - type: nauc_ndcg_at_1000_std
      value: -1.4092
    - type: nauc_ndcg_at_1000_diff1
      value: 56.64979999999999
    - type: nauc_map_at_1_max
      value: 33.465
    - type: nauc_map_at_1_std
      value: -4.077
    - type: nauc_map_at_1_diff1
      value: 63.7579
    - type: nauc_map_at_3_max
      value: 34.3502
    - type: nauc_map_at_3_std
      value: -5.9047
    - type: nauc_map_at_3_diff1
      value: 56.5011
    - type: nauc_map_at_5_max
      value: 35.0286
    - type: nauc_map_at_5_std
      value: -2.464
    - type: nauc_map_at_5_diff1
      value: 56.152
    - type: nauc_map_at_10_max
      value: 34.8474
    - type: nauc_map_at_10_std
      value: -2.2748999999999997
    - type: nauc_map_at_10_diff1
      value: 57.052499999999995
    - type: nauc_map_at_20_max
      value: 34.9946
    - type: nauc_map_at_20_std
      value: -1.9411999999999998
    - type: nauc_map_at_20_diff1
      value: 57.17
    - type: nauc_map_at_100_max
      value: 35.051500000000004
    - type: nauc_map_at_100_std
      value: -2.2917
    - type: nauc_map_at_100_diff1
      value: 57.3365
    - type: nauc_map_at_1000_max
      value: 35.0333
    - type: nauc_map_at_1000_std
      value: -2.2848
    - type: nauc_map_at_1000_diff1
      value: 57.338
    - type: nauc_recall_at_1_max
      value: 33.465
    - type: nauc_recall_at_1_std
      value: -4.077
    - type: nauc_recall_at_1_diff1
      value: 63.7579
    - type: nauc_recall_at_3_max
      value: 34.977799999999995
    - type: nauc_recall_at_3_std
      value: -13.3675
    - type: nauc_recall_at_3_diff1
      value: 46.262100000000004
    - type: nauc_recall_at_5_max
      value: 38.3639
    - type: nauc_recall_at_5_std
      value: 6.2278
    - type: nauc_recall_at_5_diff1
      value: 41.7151
    - type: nauc_recall_at_10_max
      value: 37.2498
    - type: nauc_recall_at_10_std
      value: 14.6038
    - type: nauc_recall_at_10_diff1
      value: 46.9591
    - type: nauc_recall_at_20_max
      value: 47.9805
    - type: nauc_recall_at_20_std
      value: 43.1323
    - type: nauc_recall_at_20_diff1
      value: 45.1942
    - type: nauc_recall_at_100_max
      value: 74.239
    - type: nauc_recall_at_100_std
      value: -23.8365
    - type: nauc_recall_at_100_diff1
      value: 54.4918
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 33.465
    - type: nauc_precision_at_1_std
      value: -4.077
    - type: nauc_precision_at_1_diff1
      value: 63.7579
    - type: nauc_precision_at_3_max
      value: 34.977799999999995
    - type: nauc_precision_at_3_std
      value: -13.3675
    - type: nauc_precision_at_3_diff1
      value: 46.262100000000004
    - type: nauc_precision_at_5_max
      value: 38.3639
    - type: nauc_precision_at_5_std
      value: 6.2278
    - type: nauc_precision_at_5_diff1
      value: 41.7151
    - type: nauc_precision_at_10_max
      value: 37.2498
    - type: nauc_precision_at_10_std
      value: 14.6038
    - type: nauc_precision_at_10_diff1
      value: 46.9591
    - type: nauc_precision_at_20_max
      value: 47.9805
    - type: nauc_precision_at_20_std
      value: 43.1323
    - type: nauc_precision_at_20_diff1
      value: 45.1942
    - type: nauc_precision_at_100_max
      value: 74.239
    - type: nauc_precision_at_100_std
      value: -23.8365
    - type: nauc_precision_at_100_diff1
      value: 54.4918
    - type: nauc_precision_at_1000_max
      value: 100.0
    - type: nauc_precision_at_1000_std
      value: 100.0
    - type: nauc_precision_at_1000_diff1
      value: 100.0
    - type: nauc_mrr_at_1_max
      value: 33.465
    - type: nauc_mrr_at_1_std
      value: -4.077
    - type: nauc_mrr_at_1_diff1
      value: 63.7579
    - type: nauc_mrr_at_3_max
      value: 34.3502
    - type: nauc_mrr_at_3_std
      value: -5.9047
    - type: nauc_mrr_at_3_diff1
      value: 56.5011
    - type: nauc_mrr_at_5_max
      value: 35.0286
    - type: nauc_mrr_at_5_std
      value: -2.464
    - type: nauc_mrr_at_5_diff1
      value: 56.152
    - type: nauc_mrr_at_10_max
      value: 34.8474
    - type: nauc_mrr_at_10_std
      value: -2.2748999999999997
    - type: nauc_mrr_at_10_diff1
      value: 57.052499999999995
    - type: nauc_mrr_at_20_max
      value: 34.9946
    - type: nauc_mrr_at_20_std
      value: -1.9411999999999998
    - type: nauc_mrr_at_20_diff1
      value: 57.17
    - type: nauc_mrr_at_100_max
      value: 35.051500000000004
    - type: nauc_mrr_at_100_std
      value: -2.2917
    - type: nauc_mrr_at_100_diff1
      value: 57.3365
    - type: nauc_mrr_at_1000_max
      value: 35.0333
    - type: nauc_mrr_at_1000_std
      value: -2.2848
    - type: nauc_mrr_at_1000_diff1
      value: 57.338
    - type: main_score
      value: 60.328
    task:
      type: Retrieval
  - dataset:
      config: vietnamese
      name: MTEB PublicHealthQA (vietnamese)
      revision: main
      split: test
      type: xhluca/publichealth-qa
    metrics:
    - type: ndcg_at_1
      value: 31.169000000000004
    - type: ndcg_at_3
      value: 41.79
    - type: ndcg_at_5
      value: 43.354
    - type: ndcg_at_10
      value: 45.957
    - type: ndcg_at_20
      value: 48.631
    - type: ndcg_at_100
      value: 53.940999999999995
    - type: ndcg_at_1000
      value: 53.940999999999995
    - type: map_at_1
      value: 31.169000000000004
    - type: map_at_3
      value: 39.177
    - type: map_at_5
      value: 40.022000000000006
    - type: map_at_10
      value: 41.144999999999996
    - type: map_at_20
      value: 41.905
    - type: map_at_100
      value: 42.641
    - type: map_at_1000
      value: 42.641
    - type: recall_at_1
      value: 31.169000000000004
    - type: recall_at_3
      value: 49.351
    - type: recall_at_5
      value: 53.247
    - type: recall_at_10
      value: 61.039
    - type: recall_at_20
      value: 71.429
    - type: recall_at_100
      value: 100.0
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 31.169000000000004
    - type: precision_at_3
      value: 16.45
    - type: precision_at_5
      value: 10.649000000000001
    - type: precision_at_10
      value: 6.104
    - type: precision_at_20
      value: 3.5709999999999997
    - type: precision_at_100
      value: 1.0
    - type: precision_at_1000
      value: 0.1
    - type: mrr_at_1
      value: 31.1688
    - type: mrr_at_3
      value: 39.177499999999995
    - type: mrr_at_5
      value: 40.0216
    - type: mrr_at_10
      value: 41.1451
    - type: mrr_at_20
      value: 41.9054
    - type: mrr_at_100
      value: 42.6408
    - type: mrr_at_1000
      value: 42.6408
    - type: nauc_ndcg_at_1_max
      value: 24.196
    - type: nauc_ndcg_at_1_std
      value: -4.1928
    - type: nauc_ndcg_at_1_diff1
      value: 52.1914
    - type: nauc_ndcg_at_3_max
      value: 20.099800000000002
    - type: nauc_ndcg_at_3_std
      value: -0.4444
    - type: nauc_ndcg_at_3_diff1
      value: 46.0998
    - type: nauc_ndcg_at_5_max
      value: 23.3937
    - type: nauc_ndcg_at_5_std
      value: -1.4628999999999999
    - type: nauc_ndcg_at_5_diff1
      value: 48.0126
    - type: nauc_ndcg_at_10_max
      value: 20.7063
    - type: nauc_ndcg_at_10_std
      value: -4.7612000000000005
    - type: nauc_ndcg_at_10_diff1
      value: 46.1062
    - type: nauc_ndcg_at_20_max
      value: 21.5561
    - type: nauc_ndcg_at_20_std
      value: -0.5067
    - type: nauc_ndcg_at_20_diff1
      value: 47.6175
    - type: nauc_ndcg_at_100_max
      value: 21.5381
    - type: nauc_ndcg_at_100_std
      value: -0.7255
    - type: nauc_ndcg_at_100_diff1
      value: 46.822900000000004
    - type: nauc_ndcg_at_1000_max
      value: 21.5381
    - type: nauc_ndcg_at_1000_std
      value: -0.7255
    - type: nauc_ndcg_at_1000_diff1
      value: 46.822900000000004
    - type: nauc_map_at_1_max
      value: 24.196
    - type: nauc_map_at_1_std
      value: -4.1928
    - type: nauc_map_at_1_diff1
      value: 52.1914
    - type: nauc_map_at_3_max
      value: 21.205199999999998
    - type: nauc_map_at_3_std
      value: -1.0412
    - type: nauc_map_at_3_diff1
      value: 46.8352
    - type: nauc_map_at_5_max
      value: 23.086000000000002
    - type: nauc_map_at_5_std
      value: -1.5817999999999999
    - type: nauc_map_at_5_diff1
      value: 47.8869
    - type: nauc_map_at_10_max
      value: 21.9837
    - type: nauc_map_at_10_std
      value: -2.8929
    - type: nauc_map_at_10_diff1
      value: 47.045500000000004
    - type: nauc_map_at_20_max
      value: 22.1671
    - type: nauc_map_at_20_std
      value: -1.7763999999999998
    - type: nauc_map_at_20_diff1
      value: 47.388999999999996
    - type: nauc_map_at_100_max
      value: 22.0523
    - type: nauc_map_at_100_std
      value: -1.4708
    - type: nauc_map_at_100_diff1
      value: 47.2193
    - type: nauc_map_at_1000_max
      value: 22.0523
    - type: nauc_map_at_1000_std
      value: -1.4708
    - type: nauc_map_at_1000_diff1
      value: 47.2193
    - type: nauc_recall_at_1_max
      value: 24.196
    - type: nauc_recall_at_1_std
      value: -4.1928
    - type: nauc_recall_at_1_diff1
      value: 52.1914
    - type: nauc_recall_at_3_max
      value: 16.862199999999998
    - type: nauc_recall_at_3_std
      value: 1.1521
    - type: nauc_recall_at_3_diff1
      value: 44.2778
    - type: nauc_recall_at_5_max
      value: 24.669
    - type: nauc_recall_at_5_std
      value: -1.4235
    - type: nauc_recall_at_5_diff1
      value: 48.987199999999994
    - type: nauc_recall_at_10_max
      value: 15.8398
    - type: nauc_recall_at_10_std
      value: -12.6435
    - type: nauc_recall_at_10_diff1
      value: 43.087900000000005
    - type: nauc_recall_at_20_max
      value: 19.5526
    - type: nauc_recall_at_20_std
      value: 7.2501
    - type: nauc_recall_at_20_diff1
      value: 50.6734
    - type: nauc_recall_at_100_max
      value: .nan
    - type: nauc_recall_at_100_std
      value: .nan
    - type: nauc_recall_at_100_diff1
      value: .nan
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 24.196
    - type: nauc_precision_at_1_std
      value: -4.1928
    - type: nauc_precision_at_1_diff1
      value: 52.1914
    - type: nauc_precision_at_3_max
      value: 16.862199999999998
    - type: nauc_precision_at_3_std
      value: 1.1521
    - type: nauc_precision_at_3_diff1
      value: 44.2778
    - type: nauc_precision_at_5_max
      value: 24.669
    - type: nauc_precision_at_5_std
      value: -1.4235
    - type: nauc_precision_at_5_diff1
      value: 48.987199999999994
    - type: nauc_precision_at_10_max
      value: 15.8398
    - type: nauc_precision_at_10_std
      value: -12.6435
    - type: nauc_precision_at_10_diff1
      value: 43.087900000000005
    - type: nauc_precision_at_20_max
      value: 19.5526
    - type: nauc_precision_at_20_std
      value: 7.2501
    - type: nauc_precision_at_20_diff1
      value: 50.6734
    - type: nauc_precision_at_100_max
      value: 100.0
    - type: nauc_precision_at_100_std
      value: 100.0
    - type: nauc_precision_at_100_diff1
      value: 100.0
    - type: nauc_precision_at_1000_max
      value: .nan
    - type: nauc_precision_at_1000_std
      value: .nan
    - type: nauc_precision_at_1000_diff1
      value: .nan
    - type: nauc_mrr_at_1_max
      value: 24.196
    - type: nauc_mrr_at_1_std
      value: -4.1928
    - type: nauc_mrr_at_1_diff1
      value: 52.1914
    - type: nauc_mrr_at_3_max
      value: 21.205199999999998
    - type: nauc_mrr_at_3_std
      value: -1.0412
    - type: nauc_mrr_at_3_diff1
      value: 46.8352
    - type: nauc_mrr_at_5_max
      value: 23.086000000000002
    - type: nauc_mrr_at_5_std
      value: -1.5817999999999999
    - type: nauc_mrr_at_5_diff1
      value: 47.8869
    - type: nauc_mrr_at_10_max
      value: 21.9837
    - type: nauc_mrr_at_10_std
      value: -2.8929
    - type: nauc_mrr_at_10_diff1
      value: 47.045500000000004
    - type: nauc_mrr_at_20_max
      value: 22.1671
    - type: nauc_mrr_at_20_std
      value: -1.7763999999999998
    - type: nauc_mrr_at_20_diff1
      value: 47.388999999999996
    - type: nauc_mrr_at_100_max
      value: 22.0523
    - type: nauc_mrr_at_100_std
      value: -1.4708
    - type: nauc_mrr_at_100_diff1
      value: 47.2193
    - type: nauc_mrr_at_1000_max
      value: 22.0523
    - type: nauc_mrr_at_1000_std
      value: -1.4708
    - type: nauc_mrr_at_1000_diff1
      value: 47.2193
    - type: main_score
      value: 45.957
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SciFact (default)
      revision: 0228b52cf27578f30900b9e5271d331663a030d7
      split: test
      type: mteb/scifact
    metrics:
    - type: ndcg_at_1
      value: 61.333000000000006
    - type: ndcg_at_3
      value: 68.60199999999999
    - type: ndcg_at_5
      value: 70.411
    - type: ndcg_at_10
      value: 73.413
    - type: ndcg_at_20
      value: 74.58200000000001
    - type: ndcg_at_100
      value: 75.592
    - type: ndcg_at_1000
      value: 76.062
    - type: map_at_1
      value: 58.428000000000004
    - type: map_at_3
      value: 65.924
    - type: map_at_5
      value: 67.187
    - type: map_at_10
      value: 68.755
    - type: map_at_20
      value: 69.122
    - type: map_at_100
      value: 69.26299999999999
    - type: map_at_1000
      value: 69.284
    - type: recall_at_1
      value: 58.428000000000004
    - type: recall_at_3
      value: 73.489
    - type: recall_at_5
      value: 78.328
    - type: recall_at_10
      value: 86.722
    - type: recall_at_20
      value: 91.056
    - type: recall_at_100
      value: 96.5
    - type: recall_at_1000
      value: 100.0
    - type: precision_at_1
      value: 61.333000000000006
    - type: precision_at_3
      value: 26.889000000000003
    - type: precision_at_5
      value: 17.467
    - type: precision_at_10
      value: 9.866999999999999
    - type: precision_at_20
      value: 5.183
    - type: precision_at_100
      value: 1.093
    - type: precision_at_1000
      value: 0.11299999999999999
    - type: mrr_at_1
      value: 61.3333
    - type: mrr_at_3
      value: 67.61110000000001
    - type: mrr_at_5
      value: 68.61110000000001
    - type: mrr_at_10
      value: 69.6848
    - type: mrr_at_20
      value: 69.9864
    - type: mrr_at_100
      value: 70.1174
    - type: mrr_at_1000
      value: 70.13719999999999
    - type: nauc_ndcg_at_1_max
      value: 64.11149999999999
    - type: nauc_ndcg_at_1_std
      value: 14.688
    - type: nauc_ndcg_at_1_diff1
      value: 79.292
    - type: nauc_ndcg_at_3_max
      value: 62.202400000000004
    - type: nauc_ndcg_at_3_std
      value: 12.7864
    - type: nauc_ndcg_at_3_diff1
      value: 74.5286
    - type: nauc_ndcg_at_5_max
      value: 61.394099999999995
    - type: nauc_ndcg_at_5_std
      value: 14.099800000000002
    - type: nauc_ndcg_at_5_diff1
      value: 73.0227
    - type: nauc_ndcg_at_10_max
      value: 66.13560000000001
    - type: nauc_ndcg_at_10_std
      value: 15.5687
    - type: nauc_ndcg_at_10_diff1
      value: 74.4028
    - type: nauc_ndcg_at_20_max
      value: 66.3651
    - type: nauc_ndcg_at_20_std
      value: 16.8451
    - type: nauc_ndcg_at_20_diff1
      value: 75.0316
    - type: nauc_ndcg_at_100_max
      value: 65.5397
    - type: nauc_ndcg_at_100_std
      value: 17.0616
    - type: nauc_ndcg_at_100_diff1
      value: 74.8458
    - type: nauc_ndcg_at_1000_max
      value: 65.1443
    - type: nauc_ndcg_at_1000_std
      value: 16.2639
    - type: nauc_ndcg_at_1000_diff1
      value: 75.0683
    - type: nauc_map_at_1_max
      value: 58.674499999999995
    - type: nauc_map_at_1_std
      value: 4.7646
    - type: nauc_map_at_1_diff1
      value: 80.0349
    - type: nauc_map_at_3_max
      value: 60.1997
    - type: nauc_map_at_3_std
      value: 9.1883
    - type: nauc_map_at_3_diff1
      value: 75.9478
    - type: nauc_map_at_5_max
      value: 60.7738
    - type: nauc_map_at_5_std
      value: 10.9619
    - type: nauc_map_at_5_diff1
      value: 74.8759
    - type: nauc_map_at_10_max
      value: 63.547399999999996
    - type: nauc_map_at_10_std
      value: 12.7719
    - type: nauc_map_at_10_diff1
      value: 75.208
    - type: nauc_map_at_20_max
      value: 63.5955
    - type: nauc_map_at_20_std
      value: 13.279
    - type: nauc_map_at_20_diff1
      value: 75.3911
    - type: nauc_map_at_100_max
      value: 63.5034
    - type: nauc_map_at_100_std
      value: 13.3433
    - type: nauc_map_at_100_diff1
      value: 75.3801
    - type: nauc_map_at_1000_max
      value: 63.4857
    - type: nauc_map_at_1000_std
      value: 13.3133
    - type: nauc_map_at_1000_diff1
      value: 75.3873
    - type: nauc_recall_at_1_max
      value: 58.674499999999995
    - type: nauc_recall_at_1_std
      value: 4.7646
    - type: nauc_recall_at_1_diff1
      value: 80.0349
    - type: nauc_recall_at_3_max
      value: 59.0557
    - type: nauc_recall_at_3_std
      value: 9.031799999999999
    - type: nauc_recall_at_3_diff1
      value: 70.52929999999999
    - type: nauc_recall_at_5_max
      value: 57.2901
    - type: nauc_recall_at_5_std
      value: 15.6434
    - type: nauc_recall_at_5_diff1
      value: 64.9777
    - type: nauc_recall_at_10_max
      value: 75.7042
    - type: nauc_recall_at_10_std
      value: 18.401600000000002
    - type: nauc_recall_at_10_diff1
      value: 69.11580000000001
    - type: nauc_recall_at_20_max
      value: 82.5429
    - type: nauc_recall_at_20_std
      value: 29.412899999999997
    - type: nauc_recall_at_20_diff1
      value: 73.2713
    - type: nauc_recall_at_100_max
      value: 81.7594
    - type: nauc_recall_at_100_std
      value: 51.816300000000005
    - type: nauc_recall_at_100_diff1
      value: 65.2683
    - type: nauc_recall_at_1000_max
      value: .nan
    - type: nauc_recall_at_1000_std
      value: .nan
    - type: nauc_recall_at_1000_diff1
      value: .nan
    - type: nauc_precision_at_1_max
      value: 64.11149999999999
    - type: nauc_precision_at_1_std
      value: 14.688
    - type: nauc_precision_at_1_diff1
      value: 79.292
    - type: nauc_precision_at_3_max
      value: 49.7731
    - type: nauc_precision_at_3_std
      value: 29.6594
    - type: nauc_precision_at_3_diff1
      value: 39.8605
    - type: nauc_precision_at_5_max
      value: 45.1136
    - type: nauc_precision_at_5_std
      value: 38.2477
    - type: nauc_precision_at_5_diff1
      value: 23.9286
    - type: nauc_precision_at_10_max
      value: 43.4848
    - type: nauc_precision_at_10_std
      value: 45.5735
    - type: nauc_precision_at_10_diff1
      value: 5.6292
    - type: nauc_precision_at_20_max
      value: 37.7011
    - type: nauc_precision_at_20_std
      value: 51.105199999999996
    - type: nauc_precision_at_20_diff1
      value: -2.2522
    - type: nauc_precision_at_100_max
      value: 27.0942
    - type: nauc_precision_at_100_std
      value: 58.4669
    - type: nauc_precision_at_100_diff1
      value: -19.608
    - type: nauc_precision_at_1000_max
      value: 17.333000000000002
    - type: nauc_precision_at_1000_std
      value: 56.925599999999996
    - type: nauc_precision_at_1000_diff1
      value: -32.3578
    - type: nauc_mrr_at_1_max
      value: 64.11149999999999
    - type: nauc_mrr_at_1_std
      value: 14.688
    - type: nauc_mrr_at_1_diff1
      value: 79.292
    - type: nauc_mrr_at_3_max
      value: 64.43100000000001
    - type: nauc_mrr_at_3_std
      value: 16.4446
    - type: nauc_mrr_at_3_diff1
      value: 75.9528
    - type: nauc_mrr_at_5_max
      value: 64.1166
    - type: nauc_mrr_at_5_std
      value: 17.9375
    - type: nauc_mrr_at_5_diff1
      value: 75.14150000000001
    - type: nauc_mrr_at_10_max
      value: 65.4043
    - type: nauc_mrr_at_10_std
      value: 17.5929
    - type: nauc_mrr_at_10_diff1
      value: 75.9545
    - type: nauc_mrr_at_20_max
      value: 65.4177
    - type: nauc_mrr_at_20_std
      value: 17.6251
    - type: nauc_mrr_at_20_diff1
      value: 76.06540000000001
    - type: nauc_mrr_at_100_max
      value: 65.3124
    - type: nauc_mrr_at_100_std
      value: 17.6635
    - type: nauc_mrr_at_100_diff1
      value: 76.04570000000001
    - type: nauc_mrr_at_1000_max
      value: 65.2954
    - type: nauc_mrr_at_1000_std
      value: 17.6416
    - type: nauc_mrr_at_1000_diff1
      value: 76.0508
    - type: main_score
      value: 73.413
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB SciFact-PL (default)
      revision: 47932a35f045ef8ed01ba82bf9ff67f6e109207e
      split: test
      type: clarin-knext/scifact-pl
    metrics:
    - type: ndcg_at_1
      value: 28.666999999999998
    - type: ndcg_at_3
      value: 34.56
    - type: ndcg_at_5
      value: 36.183
    - type: ndcg_at_10
      value: 38.862
    - type: ndcg_at_20
      value: 39.871
    - type: ndcg_at_100
      value: 42.934
    - type: ndcg_at_1000
      value: 45.439
    - type: map_at_1
      value: 26.789
    - type: map_at_3
      value: 32.231
    - type: map_at_5
      value: 33.306999999999995
    - type: map_at_10
      value: 34.538999999999994
    - type: map_at_20
      value: 34.838
    - type: map_at_100
      value: 35.22
    - type: map_at_1000
      value: 35.312
    - type: recall_at_1
      value: 26.789
    - type: recall_at_3
      value: 39.078
    - type: recall_at_5
      value: 43.217
    - type: recall_at_10
      value: 51.00599999999999
    - type: recall_at_20
      value: 54.922000000000004
    - type: recall_at_100
      value: 72.044
    - type: recall_at_1000
      value: 91.822
    - type: precision_at_1
      value: 28.666999999999998
    - type: precision_at_3
      value: 14.333000000000002
    - type: precision_at_5
      value: 9.667
    - type: precision_at_10
      value: 5.867
    - type: precision_at_20
      value: 3.167
    - type: precision_at_100
      value: 0.8130000000000001
    - type: precision_at_1000
      value: 0.104
    - type: mrr_at_1
      value: 28.6667
    - type: mrr_at_3
      value: 33.8333
    - type: mrr_at_5
      value: 34.75
    - type: mrr_at_10
      value: 35.753800000000005
    - type: mrr_at_20
      value: 35.983599999999996
    - type: mrr_at_100
      value: 36.344300000000004
    - type: mrr_at_1000
      value: 36.4276
    - type: nauc_ndcg_at_1_max
      value: 47.3964
    - type: nauc_ndcg_at_1_std
      value: 23.1255
    - type: nauc_ndcg_at_1_diff1
      value: 61.3553
    - type: nauc_ndcg_at_3_max
      value: 46.8095
    - type: nauc_ndcg_at_3_std
      value: 20.8113
    - type: nauc_ndcg_at_3_diff1
      value: 50.5186
    - type: nauc_ndcg_at_5_max
      value: 48.563
    - type: nauc_ndcg_at_5_std
      value: 22.9279
    - type: nauc_ndcg_at_5_diff1
      value: 52.3505
    - type: nauc_ndcg_at_10_max
      value: 51.0144
    - type: nauc_ndcg_at_10_std
      value: 25.165399999999998
    - type: nauc_ndcg_at_10_diff1
      value: 51.928399999999996
    - type: nauc_ndcg_at_20_max
      value: 51.2402
    - type: nauc_ndcg_at_20_std
      value: 26.264599999999998
    - type: nauc_ndcg_at_20_diff1
      value: 52.085800000000006
    - type: nauc_ndcg_at_100_max
      value: 51.486900000000006
    - type: nauc_ndcg_at_100_std
      value: 27.043499999999998
    - type: nauc_ndcg_at_100_diff1
      value: 51.4942
    - type: nauc_ndcg_at_1000_max
      value: 50.8764
    - type: nauc_ndcg_at_1000_std
      value: 26.6247
    - type: nauc_ndcg_at_1000_diff1
      value: 52.4891
    - type: nauc_map_at_1_max
      value: 45.3571
    - type: nauc_map_at_1_std
      value: 22.224
    - type: nauc_map_at_1_diff1
      value: 60.9856
    - type: nauc_map_at_3_max
      value: 46.641
    - type: nauc_map_at_3_std
      value: 21.3558
    - type: nauc_map_at_3_diff1
      value: 53.9335
    - type: nauc_map_at_5_max
      value: 47.604600000000005
    - type: nauc_map_at_5_std
      value: 22.3532
    - type: nauc_map_at_5_diff1
      value: 54.727599999999995
    - type: nauc_map_at_10_max
      value: 48.8623
    - type: nauc_map_at_10_std
      value: 23.3967
    - type: nauc_map_at_10_diff1
      value: 54.4613
    - type: nauc_map_at_20_max
      value: 48.9766
    - type: nauc_map_at_20_std
      value: 23.848
    - type: nauc_map_at_20_diff1
      value: 54.476
    - type: nauc_map_at_100_max
      value: 48.9984
    - type: nauc_map_at_100_std
      value: 23.9562
    - type: nauc_map_at_100_diff1
      value: 54.4079
    - type: nauc_map_at_1000_max
      value: 48.9822
    - type: nauc_map_at_1000_std
      value: 23.9555
    - type: nauc_map_at_1000_diff1
      value: 54.4478
    - type: nauc_recall_at_1_max
      value: 45.3571
    - type: nauc_recall_at_1_std
      value: 22.224
    - type: nauc_recall_at_1_diff1
      value: 60.9856
    - type: nauc_recall_at_3_max
      value: 44.850699999999996
    - type: nauc_recall_at_3_std
      value: 18.1467
    - type: nauc_recall_at_3_diff1
      value: 41.9454
    - type: nauc_recall_at_5_max
      value: 48.7443
    - type: nauc_recall_at_5_std
      value: 22.654
    - type: nauc_recall_at_5_diff1
      value: 45.2269
    - type: nauc_recall_at_10_max
      value: 55.4795
    - type: nauc_recall_at_10_std
      value: 29.117700000000003
    - type: nauc_recall_at_10_diff1
      value: 44.5212
    - type: nauc_recall_at_20_max
      value: 56.4723
    - type: nauc_recall_at_20_std
      value: 33.0929
    - type: nauc_recall_at_20_diff1
      value: 45.1359
    - type: nauc_recall_at_100_max
      value: 60.0848
    - type: nauc_recall_at_100_std
      value: 40.9103
    - type: nauc_recall_at_100_diff1
      value: 38.1492
    - type: nauc_recall_at_1000_max
      value: 59.6927
    - type: nauc_recall_at_1000_std
      value: 53.2595
    - type: nauc_recall_at_1000_diff1
      value: 42.1092
    - type: nauc_precision_at_1_max
      value: 47.3964
    - type: nauc_precision_at_1_std
      value: 23.1255
    - type: nauc_precision_at_1_diff1
      value: 61.3553
    - type: nauc_precision_at_3_max
      value: 47.0326
    - type: nauc_precision_at_3_std
      value: 19.482499999999998
    - type: nauc_precision_at_3_diff1
      value: 40.994
    - type: nauc_precision_at_5_max
      value: 49.263200000000005
    - type: nauc_precision_at_5_std
      value: 23.4494
    - type: nauc_precision_at_5_diff1
      value: 42.436099999999996
    - type: nauc_precision_at_10_max
      value: 52.249900000000004
    - type: nauc_precision_at_10_std
      value: 28.228199999999998
    - type: nauc_precision_at_10_diff1
      value: 35.3869
    - type: nauc_precision_at_20_max
      value: 51.8228
    - type: nauc_precision_at_20_std
      value: 32.289699999999996
    - type: nauc_precision_at_20_diff1
      value: 33.976800000000004
    - type: nauc_precision_at_100_max
      value: 51.063199999999995
    - type: nauc_precision_at_100_std
      value: 35.375099999999996
    - type: nauc_precision_at_100_diff1
      value: 25.5759
    - type: nauc_precision_at_1000_max
      value: 30.785600000000002
    - type: nauc_precision_at_1000_std
      value: 26.445600000000002
    - type: nauc_precision_at_1000_diff1
      value: 11.6568
    - type: nauc_mrr_at_1_max
      value: 47.3964
    - type: nauc_mrr_at_1_std
      value: 23.1255
    - type: nauc_mrr_at_1_diff1
      value: 61.3553
    - type: nauc_mrr_at_3_max
      value: 48.303000000000004
    - type: nauc_mrr_at_3_std
      value: 22.5707
    - type: nauc_mrr_at_3_diff1
      value: 53.01519999999999
    - type: nauc_mrr_at_5_max
      value: 49.1763
    - type: nauc_mrr_at_5_std
      value: 23.907
    - type: nauc_mrr_at_5_diff1
      value: 54.146899999999995
    - type: nauc_mrr_at_10_max
      value: 49.9118
    - type: nauc_mrr_at_10_std
      value: 24.5548
    - type: nauc_mrr_at_10_diff1
      value: 53.9486
    - type: nauc_mrr_at_20_max
      value: 49.9542
    - type: nauc_mrr_at_20_std
      value: 24.729200000000002
    - type: nauc_mrr_at_20_diff1
      value: 54.01519999999999
    - type: nauc_mrr_at_100_max
      value: 49.9469
    - type: nauc_mrr_at_100_std
      value: 24.8281
    - type: nauc_mrr_at_100_diff1
      value: 53.9569
    - type: nauc_mrr_at_1000_max
      value: 49.9349
    - type: nauc_mrr_at_1000_std
      value: 24.8281
    - type: nauc_mrr_at_1000_diff1
      value: 53.9925
    - type: main_score
      value: 38.862
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB TRECCOVID (default)
      revision: bb9466bac8153a0349341eb1b22e06409e78ef4e
      split: test
      type: mteb/trec-covid
    metrics:
    - type: ndcg_at_1
      value: 77.0
    - type: ndcg_at_3
      value: 77.95
    - type: ndcg_at_5
      value: 76.3
    - type: ndcg_at_10
      value: 75.729
    - type: ndcg_at_20
      value: 71.923
    - type: ndcg_at_100
      value: 57.583
    - type: ndcg_at_1000
      value: 51.809000000000005
    - type: map_at_1
      value: 0.22200000000000003
    - type: map_at_3
      value: 0.6459999999999999
    - type: map_at_5
      value: 1.044
    - type: map_at_10
      value: 1.986
    - type: map_at_20
      value: 3.544
    - type: map_at_100
      value: 11.19
    - type: map_at_1000
      value: 26.351000000000003
    - type: recall_at_1
      value: 0.22200000000000003
    - type: recall_at_3
      value: 0.677
    - type: recall_at_5
      value: 1.117
    - type: recall_at_10
      value: 2.189
    - type: recall_at_20
      value: 4.031
    - type: recall_at_100
      value: 14.512
    - type: recall_at_1000
      value: 48.644999999999996
    - type: precision_at_1
      value: 84.0
    - type: precision_at_3
      value: 84.667
    - type: precision_at_5
      value: 82.0
    - type: precision_at_10
      value: 80.80000000000001
    - type: precision_at_20
      value: 76.1
    - type: precision_at_100
      value: 59.160000000000004
    - type: precision_at_1000
      value: 22.692
    - type: mrr_at_1
      value: 84.0
    - type: mrr_at_3
      value: 90.6667
    - type: mrr_at_5
      value: 91.0667
    - type: mrr_at_10
      value: 91.0667
    - type: mrr_at_20
      value: 91.0667
    - type: mrr_at_100
      value: 91.0667
    - type: mrr_at_1000
      value: 91.0667
    - type: nauc_ndcg_at_1_max
      value: 48.8547
    - type: nauc_ndcg_at_1_std
      value: 49.0681
    - type: nauc_ndcg_at_1_diff1
      value: -30.4738
    - type: nauc_ndcg_at_3_max
      value: 44.5189
    - type: nauc_ndcg_at_3_std
      value: 51.435900000000004
    - type: nauc_ndcg_at_3_diff1
      value: 0.6276999999999999
    - type: nauc_ndcg_at_5_max
      value: 45.063199999999995
    - type: nauc_ndcg_at_5_std
      value: 53.6234
    - type: nauc_ndcg_at_5_diff1
      value: -3.7708
    - type: nauc_ndcg_at_10_max
      value: 45.2686
    - type: nauc_ndcg_at_10_std
      value: 55.53979999999999
    - type: nauc_ndcg_at_10_diff1
      value: -8.5233
    - type: nauc_ndcg_at_20_max
      value: 54.0756
    - type: nauc_ndcg_at_20_std
      value: 61.454
    - type: nauc_ndcg_at_20_diff1
      value: -14.1012
    - type: nauc_ndcg_at_100_max
      value: 48.0204
    - type: nauc_ndcg_at_100_std
      value: 76.6764
    - type: nauc_ndcg_at_100_diff1
      value: -21.3943
    - type: nauc_ndcg_at_1000_max
      value: 42.2604
    - type: nauc_ndcg_at_1000_std
      value: 76.43090000000001
    - type: nauc_ndcg_at_1000_diff1
      value: -10.339
    - type: nauc_map_at_1_max
      value: 19.6618
    - type: nauc_map_at_1_std
      value: 12.3368
    - type: nauc_map_at_1_diff1
      value: 5.8378
    - type: nauc_map_at_3_max
      value: 19.9671
    - type: nauc_map_at_3_std
      value: 14.360500000000002
    - type: nauc_map_at_3_diff1
      value: 11.2964
    - type: nauc_map_at_5_max
      value: 21.484
    - type: nauc_map_at_5_std
      value: 15.7254
    - type: nauc_map_at_5_diff1
      value: 8.277800000000001
    - type: nauc_map_at_10_max
      value: 19.5425
    - type: nauc_map_at_10_std
      value: 17.1697
    - type: nauc_map_at_10_diff1
      value: 4.6949
    - type: nauc_map_at_20_max
      value: 30.469
    - type: nauc_map_at_20_std
      value: 21.2894
    - type: nauc_map_at_20_diff1
      value: 5.5824
    - type: nauc_map_at_100_max
      value: 47.6198
    - type: nauc_map_at_100_std
      value: 52.692099999999996
    - type: nauc_map_at_100_diff1
      value: -4.3684
    - type: nauc_map_at_1000_max
      value: 46.7244
    - type: nauc_map_at_1000_std
      value: 79.96809999999999
    - type: nauc_map_at_1000_diff1
      value: -11.427800000000001
    - type: nauc_recall_at_1_max
      value: 19.6618
    - type: nauc_recall_at_1_std
      value: 12.3368
    - type: nauc_recall_at_1_diff1
      value: 5.8378
    - type: nauc_recall_at_3_max
      value: 15.8659
    - type: nauc_recall_at_3_std
      value: 9.417200000000001
    - type: nauc_recall_at_3_diff1
      value: 12.217
    - type: nauc_recall_at_5_max
      value: 16.6584
    - type: nauc_recall_at_5_std
      value: 9.642299999999999
    - type: nauc_recall_at_5_diff1
      value: 7.8316
    - type: nauc_recall_at_10_max
      value: 13.4892
    - type: nauc_recall_at_10_std
      value: 9.0525
    - type: nauc_recall_at_10_diff1
      value: 5.1017
    - type: nauc_recall_at_20_max
      value: 23.8122
    - type: nauc_recall_at_20_std
      value: 10.963199999999999
    - type: nauc_recall_at_20_diff1
      value: 5.496
    - type: nauc_recall_at_100_max
      value: 34.0401
    - type: nauc_recall_at_100_std
      value: 38.919399999999996
    - type: nauc_recall_at_100_diff1
      value: -2.4619999999999997
    - type: nauc_recall_at_1000_max
      value: 33.3684
    - type: nauc_recall_at_1000_std
      value: 67.9744
    - type: nauc_recall_at_1000_diff1
      value: -6.4093
    - type: nauc_precision_at_1_max
      value: 58.4315
    - type: nauc_precision_at_1_std
      value: 64.72139999999999
    - type: nauc_precision_at_1_diff1
      value: -28.375099999999996
    - type: nauc_precision_at_3_max
      value: 43.6798
    - type: nauc_precision_at_3_std
      value: 62.983599999999996
    - type: nauc_precision_at_3_diff1
      value: 4.495
    - type: nauc_precision_at_5_max
      value: 45.5822
    - type: nauc_precision_at_5_std
      value: 66.2558
    - type: nauc_precision_at_5_diff1
      value: -0.5026
    - type: nauc_precision_at_10_max
      value: 46.4246
    - type: nauc_precision_at_10_std
      value: 61.202999999999996
    - type: nauc_precision_at_10_diff1
      value: -7.648499999999999
    - type: nauc_precision_at_20_max
      value: 59.4366
    - type: nauc_precision_at_20_std
      value: 62.530699999999996
    - type: nauc_precision_at_20_diff1
      value: -14.7791
    - type: nauc_precision_at_100_max
      value: 47.7262
    - type: nauc_precision_at_100_std
      value: 75.8917
    - type: nauc_precision_at_100_diff1
      value: -21.1255
    - type: nauc_precision_at_1000_max
      value: 26.461299999999998
    - type: nauc_precision_at_1000_std
      value: 56.535599999999995
    - type: nauc_precision_at_1000_diff1
      value: -16.9377
    - type: nauc_mrr_at_1_max
      value: 58.4315
    - type: nauc_mrr_at_1_std
      value: 64.72139999999999
    - type: nauc_mrr_at_1_diff1
      value: -28.375099999999996
    - type: nauc_mrr_at_3_max
      value: 59.156600000000005
    - type: nauc_mrr_at_3_std
      value: 66.3882
    - type: nauc_mrr_at_3_diff1
      value: -30.3537
    - type: nauc_mrr_at_5_max
      value: 59.3318
    - type: nauc_mrr_at_5_std
      value: 66.115
    - type: nauc_mrr_at_5_diff1
      value: -30.9728
    - type: nauc_mrr_at_10_max
      value: 59.3318
    - type: nauc_mrr_at_10_std
      value: 66.115
    - type: nauc_mrr_at_10_diff1
      value: -30.9728
    - type: nauc_mrr_at_20_max
      value: 59.3318
    - type: nauc_mrr_at_20_std
      value: 66.115
    - type: nauc_mrr_at_20_diff1
      value: -30.9728
    - type: nauc_mrr_at_100_max
      value: 59.3318
    - type: nauc_mrr_at_100_std
      value: 66.115
    - type: nauc_mrr_at_100_diff1
      value: -30.9728
    - type: nauc_mrr_at_1000_max
      value: 59.3318
    - type: nauc_mrr_at_1000_std
      value: 66.115
    - type: nauc_mrr_at_1000_diff1
      value: -30.9728
    - type: main_score
      value: 75.729
    task:
      type: Retrieval
  - dataset:
      config: default
      name: MTEB TRECCOVID-PL (default)
      revision: 81bcb408f33366c2a20ac54adafad1ae7e877fdd
      split: test
      type: clarin-knext/trec-covid-pl
    metrics:
    - type: ndcg_at_1
      value: 33.0
    - type: ndcg_at_3
      value: 35.022
    - type: ndcg_at_5
      value: 33.731
    - type: ndcg_at_10
      value: 31.52
    - type: ndcg_at_20
      value: 27.831
    - type: ndcg_at_100
      value: 21.394
    - type: ndcg_at_1000
      value: 19.528000000000002
    - type: map_at_1
      value: 0.089
    - type: map_at_3
      value: 0.27
    - type: map_at_5
      value: 0.4
    - type: map_at_10
      value: 0.622
    - type: map_at_20
      value: 0.91
    - type: map_at_100
      value: 2.373
    - type: map_at_1000
      value: 6.121
    - type: recall_at_1
      value: 0.089
    - type: recall_at_3
      value: 0.314
    - type: recall_at_5
      value: 0.492
    - type: recall_at_10
      value: 0.851
    - type: recall_at_20
      value: 1.367
    - type: recall_at_100
      value: 4.763
    - type: recall_at_1000
      value: 18.496000000000002
    - type: precision_at_1
      value: 38.0
    - type: precision_at_3
      value: 37.333
    - type: precision_at_5
      value: 35.6
    - type: precision_at_10
      value: 32.6
    - type: precision_at_20
      value: 27.900000000000002
    - type: precision_at_100
      value: 21.560000000000002
    - type: precision_at_1000
      value: 9.306000000000001
    - type: mrr_at_1
      value: 38.0
    - type: mrr_at_3
      value: 46.0
    - type: mrr_at_5
      value: 47.9
    - type: mrr_at_10
      value: 49.9214
    - type: mrr_at_20
      value: 50.1641
    - type: mrr_at_100
      value: 50.626000000000005
    - type: mrr_at_1000
      value: 50.6339
    - type: nauc_ndcg_at_1_max
      value: 34.6986
    - type: nauc_ndcg_at_1_std
      value: 32.1162
    - type: nauc_ndcg_at_1_diff1
      value: -10.2072
    - type: nauc_ndcg_at_3_max
      value: 26.7849
    - type: nauc_ndcg_at_3_std
      value: 11.6996
    - type: nauc_ndcg_at_3_diff1
      value: -12.581800000000001
    - type: nauc_ndcg_at_5_max
      value: 24.4334
    - type: nauc_ndcg_at_5_std
      value: 5.9356
    - type: nauc_ndcg_at_5_diff1
      value: -7.063899999999999
    - type: nauc_ndcg_at_10_max
      value: 24.916900000000002
    - type: nauc_ndcg_at_10_std
      value: 4.5668
    - type: nauc_ndcg_at_10_diff1
      value: -2.1188
    - type: nauc_ndcg_at_20_max
      value: 26.273600000000002
    - type: nauc_ndcg_at_20_std
      value: 7.7196
    - type: nauc_ndcg_at_20_diff1
      value: 0.8089000000000001
    - type: nauc_ndcg_at_100_max
      value: 33.1944
    - type: nauc_ndcg_at_100_std
      value: 16.3776
    - type: nauc_ndcg_at_100_diff1
      value: -2.5803
    - type: nauc_ndcg_at_1000_max
      value: 51.3621
    - type: nauc_ndcg_at_1000_std
      value: 29.2173
    - type: nauc_ndcg_at_1000_diff1
      value: -6.7301
    - type: nauc_map_at_1_max
      value: 27.8013
    - type: nauc_map_at_1_std
      value: 12.5435
    - type: nauc_map_at_1_diff1
      value: -16.522100000000002
    - type: nauc_map_at_3_max
      value: 19.433500000000002
    - type: nauc_map_at_3_std
      value: -5.2681
    - type: nauc_map_at_3_diff1
      value: -20.3585
    - type: nauc_map_at_5_max
      value: 15.0378
    - type: nauc_map_at_5_std
      value: -10.252500000000001
    - type: nauc_map_at_5_diff1
      value: -13.5849
    - type: nauc_map_at_10_max
      value: 16.6286
    - type: nauc_map_at_10_std
      value: -8.9473
    - type: nauc_map_at_10_diff1
      value: -11.0427
    - type: nauc_map_at_20_max
      value: 16.3801
    - type: nauc_map_at_20_std
      value: -3.9566
    - type: nauc_map_at_20_diff1
      value: -5.8741
    - type: nauc_map_at_100_max
      value: 23.8517
    - type: nauc_map_at_100_std
      value: 12.7052
    - type: nauc_map_at_100_diff1
      value: -4.0786999999999995
    - type: nauc_map_at_1000_max
      value: 50.2364
    - type: nauc_map_at_1000_std
      value: 45.1323
    - type: nauc_map_at_1000_diff1
      value: -9.7797
    - type: nauc_recall_at_1_max
      value: 27.8013
    - type: nauc_recall_at_1_std
      value: 12.5435
    - type: nauc_recall_at_1_diff1
      value: -16.522100000000002
    - type: nauc_recall_at_3_max
      value: 12.021600000000001
    - type: nauc_recall_at_3_std
      value: -12.195
    - type: nauc_recall_at_3_diff1
      value: -17.7181
    - type: nauc_recall_at_5_max
      value: 8.317499999999999
    - type: nauc_recall_at_5_std
      value: -17.3643
    - type: nauc_recall_at_5_diff1
      value: -11.0701
    - type: nauc_recall_at_10_max
      value: 12.629199999999999
    - type: nauc_recall_at_10_std
      value: -17.8
    - type: nauc_recall_at_10_diff1
      value: -3.1063
    - type: nauc_recall_at_20_max
      value: 14.7957
    - type: nauc_recall_at_20_std
      value: -12.6812
    - type: nauc_recall_at_20_diff1
      value: 2.5131
    - type: nauc_recall_at_100_max
      value: 26.763900000000003
    - type: nauc_recall_at_100_std
      value: 1.4699
    - type: nauc_recall_at_100_diff1
      value: 2.1349
    - type: nauc_recall_at_1000_max
      value: 57.9288
    - type: nauc_recall_at_1000_std
      value: 34.260600000000004
    - type: nauc_recall_at_1000_diff1
      value: -7.8182
    - type: nauc_precision_at_1_max
      value: 35.3859
    - type: nauc_precision_at_1_std
      value: 27.918300000000002
    - type: nauc_precision_at_1_diff1
      value: -9.804300000000001
    - type: nauc_precision_at_3_max
      value: 23.3863
    - type: nauc_precision_at_3_std
      value: 3.6164
    - type: nauc_precision_at_3_diff1
      value: -11.8673
    - type: nauc_precision_at_5_max
      value: 19.648
    - type: nauc_precision_at_5_std
      value: -1.4232
    - type: nauc_precision_at_5_diff1
      value: -4.7019
    - type: nauc_precision_at_10_max
      value: 22.9189
    - type: nauc_precision_at_10_std
      value: 0.6967
    - type: nauc_precision_at_10_diff1
      value: -0.757
    - type: nauc_precision_at_20_max
      value: 27.294800000000002
    - type: nauc_precision_at_20_std
      value: 8.280800000000001
    - type: nauc_precision_at_20_diff1
      value: 2.1543
    - type: nauc_precision_at_100_max
      value: 36.647600000000004
    - type: nauc_precision_at_100_std
      value: 21.0732
    - type: nauc_precision_at_100_diff1
      value: -4.3472
    - type: nauc_precision_at_1000_max
      value: 56.1096
    - type: nauc_precision_at_1000_std
      value: 44.7203
    - type: nauc_precision_at_1000_diff1
      value: -16.724800000000002
    - type: nauc_mrr_at_1_max
      value: 35.3859
    - type: nauc_mrr_at_1_std
      value: 27.918300000000002
    - type: nauc_mrr_at_1_diff1
      value: -9.804300000000001
    - type: nauc_mrr_at_3_max
      value: 28.7924
    - type: nauc_mrr_at_3_std
      value: 14.6514
    - type: nauc_mrr_at_3_diff1
      value: -5.1166
    - type: nauc_mrr_at_5_max
      value: 27.824199999999998
    - type: nauc_mrr_at_5_std
      value: 14.530499999999998
    - type: nauc_mrr_at_5_diff1
      value: -8.6874
    - type: nauc_mrr_at_10_max
      value: 28.8111
    - type: nauc_mrr_at_10_std
      value: 12.7967
    - type: nauc_mrr_at_10_diff1
      value: -2.1439
    - type: nauc_mrr_at_20_max
      value: 28.6582
    - type: nauc_mrr_at_20_std
      value: 12.2919
    - type: nauc_mrr_at_20_diff1
      value: -2.7289999999999996
    - type: nauc_mrr_at_100_max
      value: 28.9392
    - type: nauc_mrr_at_100_std
      value: 12.848200000000002
    - type: nauc_mrr_at_100_diff1
      value: -3.1357000000000004
    - type: nauc_mrr_at_1000_max
      value: 28.9231
    - type: nauc_mrr_at_1000_std
      value: 12.8882
    - type: nauc_mrr_at_1000_diff1
      value: -3.1525999999999996
    - type: main_score
      value: 31.52
    task:
      type: Retrieval
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