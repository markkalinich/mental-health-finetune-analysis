---
library_name: sentence-transformers
pipeline_tag: sentence-similarity
tags:
  - feature-extraction
  - sentence-similarity
  - mteb
  - transformers
  - transformers.js
license: apache-2.0
language:
- en
inference: false
model-index:
- name: epoch_0_model
  results:
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_counterfactual
      name: MTEB AmazonCounterfactualClassification (en)
      config: en
      split: test
      revision: e8379541af4e31359cca9fbcf4b00f2671dba205
    metrics:
    - type: accuracy
      value: 76.98507462686568
    - type: ap
      value: 39.47222193126652
    - type: f1
      value: 70.5923611893019
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_polarity
      name: MTEB AmazonPolarityClassification
      config: default
      split: test
      revision: e2d317d38cd51312af73b3d32a06d1a08b442046
    metrics:
    - type: accuracy
      value: 87.540175
    - type: ap
      value: 83.16128207188409
    - type: f1
      value: 87.5231988227265
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_reviews_multi
      name: MTEB AmazonReviewsClassification (en)
      config: en
      split: test
      revision: 1399c76144fd37290681b995c656ef9b2e06e26d
    metrics:
    - type: accuracy
      value: 46.80799999999999
    - type: f1
      value: 46.2632547445265
  - task:
      type: Retrieval
    dataset:
      type: arguana
      name: MTEB ArguAna
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 30.583
    - type: map_at_10
      value: 46.17
    - type: map_at_100
      value: 47.115
    - type: map_at_1000
      value: 47.121
    - type: map_at_3
      value: 41.489
    - type: map_at_5
      value: 44.046
    - type: mrr_at_1
      value: 30.939
    - type: mrr_at_10
      value: 46.289
    - type: mrr_at_100
      value: 47.241
    - type: mrr_at_1000
      value: 47.247
    - type: mrr_at_3
      value: 41.596
    - type: mrr_at_5
      value: 44.149
    - type: ndcg_at_1
      value: 30.583
    - type: ndcg_at_10
      value: 54.812000000000005
    - type: ndcg_at_100
      value: 58.605
    - type: ndcg_at_1000
      value: 58.753
    - type: ndcg_at_3
      value: 45.095
    - type: ndcg_at_5
      value: 49.744
    - type: precision_at_1
      value: 30.583
    - type: precision_at_10
      value: 8.243
    - type: precision_at_100
      value: 0.984
    - type: precision_at_1000
      value: 0.1
    - type: precision_at_3
      value: 18.516
    - type: precision_at_5
      value: 13.385
    - type: recall_at_1
      value: 30.583
    - type: recall_at_10
      value: 82.432
    - type: recall_at_100
      value: 98.43499999999999
    - type: recall_at_1000
      value: 99.57300000000001
    - type: recall_at_3
      value: 55.547999999999995
    - type: recall_at_5
      value: 66.927
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-p2p
      name: MTEB ArxivClusteringP2P
      config: default
      split: test
      revision: a122ad7f3f0291bf49cc6f4d32aa80929df69d5d
    metrics:
    - type: v_measure
      value: 45.17830107652425
  - task:
      type: Clustering
    dataset:
      type: mteb/arxiv-clustering-s2s
      name: MTEB ArxivClusteringS2S
      config: default
      split: test
      revision: f910caf1a6075f7329cdf8c1a6135696f37dbd53
    metrics:
    - type: v_measure
      value: 35.90561364087807
  - task:
      type: Reranking
    dataset:
      type: mteb/askubuntudupquestions-reranking
      name: MTEB AskUbuntuDupQuestions
      config: default
      split: test
      revision: 2000358ca161889fa9c082cb41daa8dcfb161a54
    metrics:
    - type: map
      value: 59.57222651819297
    - type: mrr
      value: 73.19241085169062
  - task:
      type: STS
    dataset:
      type: mteb/biosses-sts
      name: MTEB BIOSSES
      config: default
      split: test
      revision: d3fb88f8f02e40887cd149695127462bbcf29b4a
    metrics:
    - type: cos_sim_pearson
      value: 89.55181686367382
    - type: cos_sim_spearman
      value: 87.18933606575987
    - type: euclidean_pearson
      value: 87.78077503434338
    - type: euclidean_spearman
      value: 87.18933606575987
    - type: manhattan_pearson
      value: 87.75124980168601
    - type: manhattan_spearman
      value: 86.79113422137638
  - task:
      type: Classification
    dataset:
      type: mteb/banking77
      name: MTEB Banking77Classification
      config: default
      split: test
      revision: 0fd18e25b25c072e09e0d92ab615fda904d66300
    metrics:
    - type: accuracy
      value: 81.09415584415585
    - type: f1
      value: 80.60088693212091
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-p2p
      name: MTEB BiorxivClusteringP2P
      config: default
      split: test
      revision: 65b79d1d13f80053f67aca9498d9402c2d9f1f40
    metrics:
    - type: v_measure
      value: 36.57061229905462
  - task:
      type: Clustering
    dataset:
      type: mteb/biorxiv-clustering-s2s
      name: MTEB BiorxivClusteringS2S
      config: default
      split: test
      revision: 258694dd0231531bc1fd9de6ceb52a0853c6d908
    metrics:
    - type: v_measure
      value: 32.05342946608653
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackAndroidRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 34.376
    - type: map_at_10
      value: 45.214
    - type: map_at_100
      value: 46.635
    - type: map_at_1000
      value: 46.755
    - type: map_at_3
      value: 42.198
    - type: map_at_5
      value: 43.723
    - type: mrr_at_1
      value: 41.774
    - type: mrr_at_10
      value: 51.07000000000001
    - type: mrr_at_100
      value: 51.785000000000004
    - type: mrr_at_1000
      value: 51.824999999999996
    - type: mrr_at_3
      value: 48.808
    - type: mrr_at_5
      value: 50.11
    - type: ndcg_at_1
      value: 41.774
    - type: ndcg_at_10
      value: 51.105999999999995
    - type: ndcg_at_100
      value: 56.358
    - type: ndcg_at_1000
      value: 58.205
    - type: ndcg_at_3
      value: 46.965
    - type: ndcg_at_5
      value: 48.599
    - type: precision_at_1
      value: 41.774
    - type: precision_at_10
      value: 9.514
    - type: precision_at_100
      value: 1.508
    - type: precision_at_1000
      value: 0.196
    - type: precision_at_3
      value: 22.175
    - type: precision_at_5
      value: 15.508
    - type: recall_at_1
      value: 34.376
    - type: recall_at_10
      value: 61.748000000000005
    - type: recall_at_100
      value: 84.025
    - type: recall_at_1000
      value: 95.5
    - type: recall_at_3
      value: 49.378
    - type: recall_at_5
      value: 54.276
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackEnglishRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 32.394
    - type: map_at_10
      value: 42.707
    - type: map_at_100
      value: 43.893
    - type: map_at_1000
      value: 44.019000000000005
    - type: map_at_3
      value: 39.51
    - type: map_at_5
      value: 41.381
    - type: mrr_at_1
      value: 41.019
    - type: mrr_at_10
      value: 49.042
    - type: mrr_at_100
      value: 49.669000000000004
    - type: mrr_at_1000
      value: 49.712
    - type: mrr_at_3
      value: 46.921
    - type: mrr_at_5
      value: 48.192
    - type: ndcg_at_1
      value: 41.019
    - type: ndcg_at_10
      value: 48.46
    - type: ndcg_at_100
      value: 52.537
    - type: ndcg_at_1000
      value: 54.491
    - type: ndcg_at_3
      value: 44.232
    - type: ndcg_at_5
      value: 46.305
    - type: precision_at_1
      value: 41.019
    - type: precision_at_10
      value: 9.134
    - type: precision_at_100
      value: 1.422
    - type: precision_at_1000
      value: 0.188
    - type: precision_at_3
      value: 21.38
    - type: precision_at_5
      value: 15.096000000000002
    - type: recall_at_1
      value: 32.394
    - type: recall_at_10
      value: 58.11500000000001
    - type: recall_at_100
      value: 75.509
    - type: recall_at_1000
      value: 87.812
    - type: recall_at_3
      value: 45.476
    - type: recall_at_5
      value: 51.549
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGamingRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 43.47
    - type: map_at_10
      value: 55.871
    - type: map_at_100
      value: 56.745000000000005
    - type: map_at_1000
      value: 56.794
    - type: map_at_3
      value: 52.439
    - type: map_at_5
      value: 54.412000000000006
    - type: mrr_at_1
      value: 49.592000000000006
    - type: mrr_at_10
      value: 59.34199999999999
    - type: mrr_at_100
      value: 59.857000000000006
    - type: mrr_at_1000
      value: 59.88
    - type: mrr_at_3
      value: 56.897
    - type: mrr_at_5
      value: 58.339
    - type: ndcg_at_1
      value: 49.592000000000006
    - type: ndcg_at_10
      value: 61.67
    - type: ndcg_at_100
      value: 65.11099999999999
    - type: ndcg_at_1000
      value: 66.065
    - type: ndcg_at_3
      value: 56.071000000000005
    - type: ndcg_at_5
      value: 58.84700000000001
    - type: precision_at_1
      value: 49.592000000000006
    - type: precision_at_10
      value: 9.774
    - type: precision_at_100
      value: 1.2449999999999999
    - type: precision_at_1000
      value: 0.13699999999999998
    - type: precision_at_3
      value: 24.66
    - type: precision_at_5
      value: 16.878
    - type: recall_at_1
      value: 43.47
    - type: recall_at_10
      value: 75.387
    - type: recall_at_100
      value: 90.253
    - type: recall_at_1000
      value: 97.00800000000001
    - type: recall_at_3
      value: 60.616
    - type: recall_at_5
      value: 67.31899999999999
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackGisRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 26.633000000000003
    - type: map_at_10
      value: 35.497
    - type: map_at_100
      value: 36.504
    - type: map_at_1000
      value: 36.574
    - type: map_at_3
      value: 33.115
    - type: map_at_5
      value: 34.536
    - type: mrr_at_1
      value: 28.927000000000003
    - type: mrr_at_10
      value: 37.778
    - type: mrr_at_100
      value: 38.634
    - type: mrr_at_1000
      value: 38.690000000000005
    - type: mrr_at_3
      value: 35.518
    - type: mrr_at_5
      value: 36.908
    - type: ndcg_at_1
      value: 28.927000000000003
    - type: ndcg_at_10
      value: 40.327
    - type: ndcg_at_100
      value: 45.321
    - type: ndcg_at_1000
      value: 47.214
    - type: ndcg_at_3
      value: 35.762
    - type: ndcg_at_5
      value: 38.153999999999996
    - type: precision_at_1
      value: 28.927000000000003
    - type: precision_at_10
      value: 6.045
    - type: precision_at_100
      value: 0.901
    - type: precision_at_1000
      value: 0.11
    - type: precision_at_3
      value: 15.140999999999998
    - type: precision_at_5
      value: 10.485999999999999
    - type: recall_at_1
      value: 26.633000000000003
    - type: recall_at_10
      value: 52.99
    - type: recall_at_100
      value: 76.086
    - type: recall_at_1000
      value: 90.46300000000001
    - type: recall_at_3
      value: 40.738
    - type: recall_at_5
      value: 46.449
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackMathematicaRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 17.521
    - type: map_at_10
      value: 25.130000000000003
    - type: map_at_100
      value: 26.176
    - type: map_at_1000
      value: 26.289
    - type: map_at_3
      value: 22.829
    - type: map_at_5
      value: 24.082
    - type: mrr_at_1
      value: 21.766
    - type: mrr_at_10
      value: 29.801
    - type: mrr_at_100
      value: 30.682
    - type: mrr_at_1000
      value: 30.75
    - type: mrr_at_3
      value: 27.633000000000003
    - type: mrr_at_5
      value: 28.858
    - type: ndcg_at_1
      value: 21.766
    - type: ndcg_at_10
      value: 30.026000000000003
    - type: ndcg_at_100
      value: 35.429
    - type: ndcg_at_1000
      value: 38.236
    - type: ndcg_at_3
      value: 25.968000000000004
    - type: ndcg_at_5
      value: 27.785
    - type: precision_at_1
      value: 21.766
    - type: precision_at_10
      value: 5.498
    - type: precision_at_100
      value: 0.9450000000000001
    - type: precision_at_1000
      value: 0.133
    - type: precision_at_3
      value: 12.687000000000001
    - type: precision_at_5
      value: 9.005
    - type: recall_at_1
      value: 17.521
    - type: recall_at_10
      value: 40.454
    - type: recall_at_100
      value: 64.828
    - type: recall_at_1000
      value: 84.83800000000001
    - type: recall_at_3
      value: 28.758
    - type: recall_at_5
      value: 33.617000000000004
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackPhysicsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 30.564999999999998
    - type: map_at_10
      value: 40.664
    - type: map_at_100
      value: 41.995
    - type: map_at_1000
      value: 42.104
    - type: map_at_3
      value: 37.578
    - type: map_at_5
      value: 39.247
    - type: mrr_at_1
      value: 37.44
    - type: mrr_at_10
      value: 46.533
    - type: mrr_at_100
      value: 47.363
    - type: mrr_at_1000
      value: 47.405
    - type: mrr_at_3
      value: 44.224999999999994
    - type: mrr_at_5
      value: 45.549
    - type: ndcg_at_1
      value: 37.44
    - type: ndcg_at_10
      value: 46.574
    - type: ndcg_at_100
      value: 52.024
    - type: ndcg_at_1000
      value: 53.93900000000001
    - type: ndcg_at_3
      value: 41.722
    - type: ndcg_at_5
      value: 43.973
    - type: precision_at_1
      value: 37.44
    - type: precision_at_10
      value: 8.344999999999999
    - type: precision_at_100
      value: 1.278
    - type: precision_at_1000
      value: 0.16
    - type: precision_at_3
      value: 19.442
    - type: precision_at_5
      value: 13.802
    - type: recall_at_1
      value: 30.564999999999998
    - type: recall_at_10
      value: 58.207
    - type: recall_at_100
      value: 81.137
    - type: recall_at_1000
      value: 93.506
    - type: recall_at_3
      value: 44.606
    - type: recall_at_5
      value: 50.373000000000005
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackProgrammersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 27.892
    - type: map_at_10
      value: 37.251
    - type: map_at_100
      value: 38.606
    - type: map_at_1000
      value: 38.716
    - type: map_at_3
      value: 34.312
    - type: map_at_5
      value: 35.791000000000004
    - type: mrr_at_1
      value: 34.247
    - type: mrr_at_10
      value: 42.696
    - type: mrr_at_100
      value: 43.659
    - type: mrr_at_1000
      value: 43.711
    - type: mrr_at_3
      value: 40.563
    - type: mrr_at_5
      value: 41.625
    - type: ndcg_at_1
      value: 34.247
    - type: ndcg_at_10
      value: 42.709
    - type: ndcg_at_100
      value: 48.422
    - type: ndcg_at_1000
      value: 50.544
    - type: ndcg_at_3
      value: 38.105
    - type: ndcg_at_5
      value: 39.846
    - type: precision_at_1
      value: 34.247
    - type: precision_at_10
      value: 7.66
    - type: precision_at_100
      value: 1.2109999999999999
    - type: precision_at_1000
      value: 0.157
    - type: precision_at_3
      value: 17.884
    - type: precision_at_5
      value: 12.489
    - type: recall_at_1
      value: 27.892
    - type: recall_at_10
      value: 53.559
    - type: recall_at_100
      value: 78.018
    - type: recall_at_1000
      value: 92.07300000000001
    - type: recall_at_3
      value: 40.154
    - type: recall_at_5
      value: 45.078
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 27.29375
    - type: map_at_10
      value: 36.19533333333334
    - type: map_at_100
      value: 37.33183333333334
    - type: map_at_1000
      value: 37.44616666666667
    - type: map_at_3
      value: 33.49125
    - type: map_at_5
      value: 34.94166666666667
    - type: mrr_at_1
      value: 32.336666666666666
    - type: mrr_at_10
      value: 40.45983333333333
    - type: mrr_at_100
      value: 41.26533333333334
    - type: mrr_at_1000
      value: 41.321583333333336
    - type: mrr_at_3
      value: 38.23416666666667
    - type: mrr_at_5
      value: 39.48491666666666
    - type: ndcg_at_1
      value: 32.336666666666666
    - type: ndcg_at_10
      value: 41.39958333333333
    - type: ndcg_at_100
      value: 46.293
    - type: ndcg_at_1000
      value: 48.53425
    - type: ndcg_at_3
      value: 36.88833333333333
    - type: ndcg_at_5
      value: 38.90733333333333
    - type: precision_at_1
      value: 32.336666666666666
    - type: precision_at_10
      value: 7.175916666666667
    - type: precision_at_100
      value: 1.1311666666666669
    - type: precision_at_1000
      value: 0.15141666666666667
    - type: precision_at_3
      value: 16.841166666666666
    - type: precision_at_5
      value: 11.796583333333334
    - type: recall_at_1
      value: 27.29375
    - type: recall_at_10
      value: 52.514583333333334
    - type: recall_at_100
      value: 74.128
    - type: recall_at_1000
      value: 89.64125
    - type: recall_at_3
      value: 39.83258333333333
    - type: recall_at_5
      value: 45.126416666666664
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackStatsRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 24.62
    - type: map_at_10
      value: 31.517
    - type: map_at_100
      value: 32.322
    - type: map_at_1000
      value: 32.422000000000004
    - type: map_at_3
      value: 29.293999999999997
    - type: map_at_5
      value: 30.403999999999996
    - type: mrr_at_1
      value: 27.607
    - type: mrr_at_10
      value: 34.294999999999995
    - type: mrr_at_100
      value: 35.045
    - type: mrr_at_1000
      value: 35.114000000000004
    - type: mrr_at_3
      value: 32.311
    - type: mrr_at_5
      value: 33.369
    - type: ndcg_at_1
      value: 27.607
    - type: ndcg_at_10
      value: 35.853
    - type: ndcg_at_100
      value: 39.919
    - type: ndcg_at_1000
      value: 42.452
    - type: ndcg_at_3
      value: 31.702
    - type: ndcg_at_5
      value: 33.47
    - type: precision_at_1
      value: 27.607
    - type: precision_at_10
      value: 5.598
    - type: precision_at_100
      value: 0.83
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 13.700999999999999
    - type: precision_at_5
      value: 9.325
    - type: recall_at_1
      value: 24.62
    - type: recall_at_10
      value: 46.475
    - type: recall_at_100
      value: 64.891
    - type: recall_at_1000
      value: 83.524
    - type: recall_at_3
      value: 34.954
    - type: recall_at_5
      value: 39.471000000000004
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackTexRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 16.858999999999998
    - type: map_at_10
      value: 23.746000000000002
    - type: map_at_100
      value: 24.731
    - type: map_at_1000
      value: 24.86
    - type: map_at_3
      value: 21.603
    - type: map_at_5
      value: 22.811999999999998
    - type: mrr_at_1
      value: 20.578
    - type: mrr_at_10
      value: 27.618
    - type: mrr_at_100
      value: 28.459
    - type: mrr_at_1000
      value: 28.543000000000003
    - type: mrr_at_3
      value: 25.533
    - type: mrr_at_5
      value: 26.730999999999998
    - type: ndcg_at_1
      value: 20.578
    - type: ndcg_at_10
      value: 28.147
    - type: ndcg_at_100
      value: 32.946999999999996
    - type: ndcg_at_1000
      value: 36.048
    - type: ndcg_at_3
      value: 24.32
    - type: ndcg_at_5
      value: 26.131999999999998
    - type: precision_at_1
      value: 20.578
    - type: precision_at_10
      value: 5.061999999999999
    - type: precision_at_100
      value: 0.8789999999999999
    - type: precision_at_1000
      value: 0.132
    - type: precision_at_3
      value: 11.448
    - type: precision_at_5
      value: 8.251999999999999
    - type: recall_at_1
      value: 16.858999999999998
    - type: recall_at_10
      value: 37.565
    - type: recall_at_100
      value: 59.239
    - type: recall_at_1000
      value: 81.496
    - type: recall_at_3
      value: 26.865
    - type: recall_at_5
      value: 31.581
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackUnixRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 26.11
    - type: map_at_10
      value: 34.214
    - type: map_at_100
      value: 35.291
    - type: map_at_1000
      value: 35.400999999999996
    - type: map_at_3
      value: 31.541000000000004
    - type: map_at_5
      value: 33.21
    - type: mrr_at_1
      value: 30.97
    - type: mrr_at_10
      value: 38.522
    - type: mrr_at_100
      value: 39.37
    - type: mrr_at_1000
      value: 39.437
    - type: mrr_at_3
      value: 36.193999999999996
    - type: mrr_at_5
      value: 37.691
    - type: ndcg_at_1
      value: 30.97
    - type: ndcg_at_10
      value: 39.2
    - type: ndcg_at_100
      value: 44.267
    - type: ndcg_at_1000
      value: 46.760000000000005
    - type: ndcg_at_3
      value: 34.474
    - type: ndcg_at_5
      value: 37.016
    - type: precision_at_1
      value: 30.97
    - type: precision_at_10
      value: 6.521000000000001
    - type: precision_at_100
      value: 1.011
    - type: precision_at_1000
      value: 0.135
    - type: precision_at_3
      value: 15.392
    - type: precision_at_5
      value: 11.026
    - type: recall_at_1
      value: 26.11
    - type: recall_at_10
      value: 50.14999999999999
    - type: recall_at_100
      value: 72.398
    - type: recall_at_1000
      value: 89.764
    - type: recall_at_3
      value: 37.352999999999994
    - type: recall_at_5
      value: 43.736000000000004
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWebmastersRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 25.514
    - type: map_at_10
      value: 34.278999999999996
    - type: map_at_100
      value: 35.847
    - type: map_at_1000
      value: 36.086
    - type: map_at_3
      value: 31.563999999999997
    - type: map_at_5
      value: 32.903999999999996
    - type: mrr_at_1
      value: 30.830000000000002
    - type: mrr_at_10
      value: 38.719
    - type: mrr_at_100
      value: 39.678999999999995
    - type: mrr_at_1000
      value: 39.741
    - type: mrr_at_3
      value: 36.265
    - type: mrr_at_5
      value: 37.599
    - type: ndcg_at_1
      value: 30.830000000000002
    - type: ndcg_at_10
      value: 39.997
    - type: ndcg_at_100
      value: 45.537
    - type: ndcg_at_1000
      value: 48.296
    - type: ndcg_at_3
      value: 35.429
    - type: ndcg_at_5
      value: 37.3
    - type: precision_at_1
      value: 30.830000000000002
    - type: precision_at_10
      value: 7.747
    - type: precision_at_100
      value: 1.516
    - type: precision_at_1000
      value: 0.24
    - type: precision_at_3
      value: 16.601
    - type: precision_at_5
      value: 11.818
    - type: recall_at_1
      value: 25.514
    - type: recall_at_10
      value: 50.71600000000001
    - type: recall_at_100
      value: 75.40299999999999
    - type: recall_at_1000
      value: 93.10300000000001
    - type: recall_at_3
      value: 37.466
    - type: recall_at_5
      value: 42.677
  - task:
      type: Retrieval
    dataset:
      type: BeIR/cqadupstack
      name: MTEB CQADupstackWordpressRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 21.571
    - type: map_at_10
      value: 28.254
    - type: map_at_100
      value: 29.237000000000002
    - type: map_at_1000
      value: 29.334
    - type: map_at_3
      value: 25.912000000000003
    - type: map_at_5
      value: 26.798
    - type: mrr_at_1
      value: 23.29
    - type: mrr_at_10
      value: 30.102
    - type: mrr_at_100
      value: 30.982
    - type: mrr_at_1000
      value: 31.051000000000002
    - type: mrr_at_3
      value: 27.942
    - type: mrr_at_5
      value: 28.848000000000003
    - type: ndcg_at_1
      value: 23.29
    - type: ndcg_at_10
      value: 32.726
    - type: ndcg_at_100
      value: 37.644
    - type: ndcg_at_1000
      value: 40.161
    - type: ndcg_at_3
      value: 27.91
    - type: ndcg_at_5
      value: 29.461
    - type: precision_at_1
      value: 23.29
    - type: precision_at_10
      value: 5.213
    - type: precision_at_100
      value: 0.828
    - type: precision_at_1000
      value: 0.117
    - type: precision_at_3
      value: 11.583
    - type: precision_at_5
      value: 7.8740000000000006
    - type: recall_at_1
      value: 21.571
    - type: recall_at_10
      value: 44.809
    - type: recall_at_100
      value: 67.74900000000001
    - type: recall_at_1000
      value: 86.60799999999999
    - type: recall_at_3
      value: 31.627
    - type: recall_at_5
      value: 35.391
  - task:
      type: Retrieval
    dataset:
      type: climate-fever
      name: MTEB ClimateFEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 9.953
    - type: map_at_10
      value: 17.183
    - type: map_at_100
      value: 18.926000000000002
    - type: map_at_1000
      value: 19.105
    - type: map_at_3
      value: 14.308000000000002
    - type: map_at_5
      value: 15.738
    - type: mrr_at_1
      value: 22.02
    - type: mrr_at_10
      value: 33.181
    - type: mrr_at_100
      value: 34.357
    - type: mrr_at_1000
      value: 34.398
    - type: mrr_at_3
      value: 29.793999999999997
    - type: mrr_at_5
      value: 31.817
    - type: ndcg_at_1
      value: 22.02
    - type: ndcg_at_10
      value: 24.712
    - type: ndcg_at_100
      value: 32.025
    - type: ndcg_at_1000
      value: 35.437000000000005
    - type: ndcg_at_3
      value: 19.852
    - type: ndcg_at_5
      value: 21.565
    - type: precision_at_1
      value: 22.02
    - type: precision_at_10
      value: 7.779
    - type: precision_at_100
      value: 1.554
    - type: precision_at_1000
      value: 0.219
    - type: precision_at_3
      value: 14.832
    - type: precision_at_5
      value: 11.453000000000001
    - type: recall_at_1
      value: 9.953
    - type: recall_at_10
      value: 30.375000000000004
    - type: recall_at_100
      value: 55.737
    - type: recall_at_1000
      value: 75.071
    - type: recall_at_3
      value: 18.529999999999998
    - type: recall_at_5
      value: 23.313
  - task:
      type: Retrieval
    dataset:
      type: dbpedia-entity
      name: MTEB DBPedia
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 8.651
    - type: map_at_10
      value: 19.674
    - type: map_at_100
      value: 27.855999999999998
    - type: map_at_1000
      value: 29.348000000000003
    - type: map_at_3
      value: 14.247000000000002
    - type: map_at_5
      value: 16.453
    - type: mrr_at_1
      value: 61.75000000000001
    - type: mrr_at_10
      value: 71.329
    - type: mrr_at_100
      value: 71.69200000000001
    - type: mrr_at_1000
      value: 71.699
    - type: mrr_at_3
      value: 69.042
    - type: mrr_at_5
      value: 70.679
    - type: ndcg_at_1
      value: 50.125
    - type: ndcg_at_10
      value: 40.199
    - type: ndcg_at_100
      value: 45.378
    - type: ndcg_at_1000
      value: 52.376999999999995
    - type: ndcg_at_3
      value: 44.342
    - type: ndcg_at_5
      value: 41.730000000000004
    - type: precision_at_1
      value: 61.75000000000001
    - type: precision_at_10
      value: 32.2
    - type: precision_at_100
      value: 10.298
    - type: precision_at_1000
      value: 1.984
    - type: precision_at_3
      value: 48.667
    - type: precision_at_5
      value: 40.5
    - type: recall_at_1
      value: 8.651
    - type: recall_at_10
      value: 25.607000000000003
    - type: recall_at_100
      value: 53.062
    - type: recall_at_1000
      value: 74.717
    - type: recall_at_3
      value: 15.661
    - type: recall_at_5
      value: 19.409000000000002
  - task:
      type: Classification
    dataset:
      type: mteb/emotion
      name: MTEB EmotionClassification
      config: default
      split: test
      revision: 4f58c6b202a23cf9a4da393831edf4f9183cad37
    metrics:
    - type: accuracy
      value: 47.64500000000001
    - type: f1
      value: 43.71011316507787
  - task:
      type: Retrieval
    dataset:
      type: fever
      name: MTEB FEVER
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 54.613
    - type: map_at_10
      value: 68.02
    - type: map_at_100
      value: 68.366
    - type: map_at_1000
      value: 68.379
    - type: map_at_3
      value: 65.753
    - type: map_at_5
      value: 67.242
    - type: mrr_at_1
      value: 59.001000000000005
    - type: mrr_at_10
      value: 72.318
    - type: mrr_at_100
      value: 72.558
    - type: mrr_at_1000
      value: 72.56099999999999
    - type: mrr_at_3
      value: 70.22699999999999
    - type: mrr_at_5
      value: 71.655
    - type: ndcg_at_1
      value: 59.001000000000005
    - type: ndcg_at_10
      value: 74.386
    - type: ndcg_at_100
      value: 75.763
    - type: ndcg_at_1000
      value: 76.03
    - type: ndcg_at_3
      value: 70.216
    - type: ndcg_at_5
      value: 72.697
    - type: precision_at_1
      value: 59.001000000000005
    - type: precision_at_10
      value: 9.844
    - type: precision_at_100
      value: 1.068
    - type: precision_at_1000
      value: 0.11100000000000002
    - type: precision_at_3
      value: 28.523
    - type: precision_at_5
      value: 18.491
    - type: recall_at_1
      value: 54.613
    - type: recall_at_10
      value: 89.669
    - type: recall_at_100
      value: 95.387
    - type: recall_at_1000
      value: 97.129
    - type: recall_at_3
      value: 78.54100000000001
    - type: recall_at_5
      value: 84.637
  - task:
      type: Retrieval
    dataset:
      type: fiqa
      name: MTEB FiQA2018
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 20.348
    - type: map_at_10
      value: 32.464999999999996
    - type: map_at_100
      value: 34.235
    - type: map_at_1000
      value: 34.410000000000004
    - type: map_at_3
      value: 28.109
    - type: map_at_5
      value: 30.634
    - type: mrr_at_1
      value: 38.889
    - type: mrr_at_10
      value: 47.131
    - type: mrr_at_100
      value: 48.107
    - type: mrr_at_1000
      value: 48.138
    - type: mrr_at_3
      value: 44.599
    - type: mrr_at_5
      value: 46.181
    - type: ndcg_at_1
      value: 38.889
    - type: ndcg_at_10
      value: 39.86
    - type: ndcg_at_100
      value: 46.619
    - type: ndcg_at_1000
      value: 49.525999999999996
    - type: ndcg_at_3
      value: 35.768
    - type: ndcg_at_5
      value: 37.4
    - type: precision_at_1
      value: 38.889
    - type: precision_at_10
      value: 11.003
    - type: precision_at_100
      value: 1.796
    - type: precision_at_1000
      value: 0.233
    - type: precision_at_3
      value: 23.714
    - type: precision_at_5
      value: 17.901
    - type: recall_at_1
      value: 20.348
    - type: recall_at_10
      value: 46.781
    - type: recall_at_100
      value: 71.937
    - type: recall_at_1000
      value: 89.18599999999999
    - type: recall_at_3
      value: 32.16
    - type: recall_at_5
      value: 38.81
  - task:
      type: Retrieval
    dataset:
      type: hotpotqa
      name: MTEB HotpotQA
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 37.198
    - type: map_at_10
      value: 54.065
    - type: map_at_100
      value: 54.984
    - type: map_at_1000
      value: 55.05
    - type: map_at_3
      value: 50.758
    - type: map_at_5
      value: 52.758
    - type: mrr_at_1
      value: 74.396
    - type: mrr_at_10
      value: 81.352
    - type: mrr_at_100
      value: 81.562
    - type: mrr_at_1000
      value: 81.57
    - type: mrr_at_3
      value: 80.30199999999999
    - type: mrr_at_5
      value: 80.963
    - type: ndcg_at_1
      value: 74.396
    - type: ndcg_at_10
      value: 63.70099999999999
    - type: ndcg_at_100
      value: 66.874
    - type: ndcg_at_1000
      value: 68.171
    - type: ndcg_at_3
      value: 58.916999999999994
    - type: ndcg_at_5
      value: 61.495999999999995
    - type: precision_at_1
      value: 74.396
    - type: precision_at_10
      value: 13.228000000000002
    - type: precision_at_100
      value: 1.569
    - type: precision_at_1000
      value: 0.174
    - type: precision_at_3
      value: 37.007
    - type: precision_at_5
      value: 24.248
    - type: recall_at_1
      value: 37.198
    - type: recall_at_10
      value: 66.13799999999999
    - type: recall_at_100
      value: 78.45400000000001
    - type: recall_at_1000
      value: 87.04899999999999
    - type: recall_at_3
      value: 55.510000000000005
    - type: recall_at_5
      value: 60.621
  - task:
      type: Classification
    dataset:
      type: mteb/imdb
      name: MTEB ImdbClassification
      config: default
      split: test
      revision: 3d86128a09e091d6018b6d26cad27f2739fc2db7
    metrics:
    - type: accuracy
      value: 86.32240000000002
    - type: ap
      value: 81.37708984744188
    - type: f1
      value: 86.29645005523952
  - task:
      type: Retrieval
    dataset:
      type: msmarco
      name: MTEB MSMARCO
      config: default
      split: dev
      revision: None
    metrics:
    - type: map_at_1
      value: 16.402
    - type: map_at_10
      value: 28.097
    - type: map_at_100
      value: 29.421999999999997
    - type: map_at_1000
      value: 29.476999999999997
    - type: map_at_3
      value: 24.015
    - type: map_at_5
      value: 26.316
    - type: mrr_at_1
      value: 16.905
    - type: mrr_at_10
      value: 28.573999999999998
    - type: mrr_at_100
      value: 29.862
    - type: mrr_at_1000
      value: 29.912
    - type: mrr_at_3
      value: 24.589
    - type: mrr_at_5
      value: 26.851000000000003
    - type: ndcg_at_1
      value: 16.905
    - type: ndcg_at_10
      value: 34.99
    - type: ndcg_at_100
      value: 41.419
    - type: ndcg_at_1000
      value: 42.815999999999995
    - type: ndcg_at_3
      value: 26.695
    - type: ndcg_at_5
      value: 30.789
    - type: precision_at_1
      value: 16.905
    - type: precision_at_10
      value: 5.891
    - type: precision_at_100
      value: 0.91
    - type: precision_at_1000
      value: 0.10300000000000001
    - type: precision_at_3
      value: 11.724
    - type: precision_at_5
      value: 9.097
    - type: recall_at_1
      value: 16.402
    - type: recall_at_10
      value: 56.462999999999994
    - type: recall_at_100
      value: 86.246
    - type: recall_at_1000
      value: 96.926
    - type: recall_at_3
      value: 33.897
    - type: recall_at_5
      value: 43.718
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_domain
      name: MTEB MTOPDomainClassification (en)
      config: en
      split: test
      revision: d80d48c1eb48d3562165c59d59d0034df9fff0bf
    metrics:
    - type: accuracy
      value: 92.35978112175103
    - type: f1
      value: 92.04704651024416
  - task:
      type: Classification
    dataset:
      type: mteb/mtop_intent
      name: MTEB MTOPIntentClassification (en)
      config: en
      split: test
      revision: ae001d0e6b1228650b7bd1c2c65fb50ad11a8aba
    metrics:
    - type: accuracy
      value: 65.20063839489283
    - type: f1
      value: 45.34047546059121
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_intent
      name: MTEB MassiveIntentClassification (en)
      config: en
      split: test
      revision: 31efe3c427b0bae9c22cbb560b8f15491cc6bed7
    metrics:
    - type: accuracy
      value: 67.74714189643578
    - type: f1
      value: 65.36156843270334
  - task:
      type: Classification
    dataset:
      type: mteb/amazon_massive_scenario
      name: MTEB MassiveScenarioClassification (en)
      config: en
      split: test
      revision: 7d571f92784cd94a019292a1f45445077d0ef634
    metrics:
    - type: accuracy
      value: 74.03160726294554
    - type: f1
      value: 73.42899064973165
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-p2p
      name: MTEB MedrxivClusteringP2P
      config: default
      split: test
      revision: e7a26af6f3ae46b30dde8737f02c07b1505bcc73
    metrics:
    - type: v_measure
      value: 31.347360980344476
  - task:
      type: Clustering
    dataset:
      type: mteb/medrxiv-clustering-s2s
      name: MTEB MedrxivClusteringS2S
      config: default
      split: test
      revision: 35191c8c0dca72d8ff3efcd72aa802307d469663
    metrics:
    - type: v_measure
      value: 29.56022733162805
  - task:
      type: Reranking
    dataset:
      type: mteb/mind_small
      name: MTEB MindSmallReranking
      config: default
      split: test
      revision: 3bdac13927fdc888b903db93b2ffdbd90b295a69
    metrics:
    - type: map
      value: 30.60132765358296
    - type: mrr
      value: 31.710892632824468
  - task:
      type: Retrieval
    dataset:
      type: nfcorpus
      name: MTEB NFCorpus
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 5.827999999999999
    - type: map_at_10
      value: 13.547
    - type: map_at_100
      value: 16.869
    - type: map_at_1000
      value: 18.242
    - type: map_at_3
      value: 9.917
    - type: map_at_5
      value: 11.648
    - type: mrr_at_1
      value: 46.44
    - type: mrr_at_10
      value: 55.062
    - type: mrr_at_100
      value: 55.513999999999996
    - type: mrr_at_1000
      value: 55.564
    - type: mrr_at_3
      value: 52.735
    - type: mrr_at_5
      value: 54.391
    - type: ndcg_at_1
      value: 44.582
    - type: ndcg_at_10
      value: 35.684
    - type: ndcg_at_100
      value: 31.913999999999998
    - type: ndcg_at_1000
      value: 40.701
    - type: ndcg_at_3
      value: 40.819
    - type: ndcg_at_5
      value: 39.117000000000004
    - type: precision_at_1
      value: 46.129999999999995
    - type: precision_at_10
      value: 26.687
    - type: precision_at_100
      value: 8.062
    - type: precision_at_1000
      value: 2.073
    - type: precision_at_3
      value: 38.493
    - type: precision_at_5
      value: 34.241
    - type: recall_at_1
      value: 5.827999999999999
    - type: recall_at_10
      value: 17.391000000000002
    - type: recall_at_100
      value: 31.228
    - type: recall_at_1000
      value: 63.943000000000005
    - type: recall_at_3
      value: 10.81
    - type: recall_at_5
      value: 13.618
  - task:
      type: Retrieval
    dataset:
      type: nq
      name: MTEB NQ
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 24.02
    - type: map_at_10
      value: 40.054
    - type: map_at_100
      value: 41.318
    - type: map_at_1000
      value: 41.343999999999994
    - type: map_at_3
      value: 35.221999999999994
    - type: map_at_5
      value: 38.057
    - type: mrr_at_1
      value: 27.230999999999998
    - type: mrr_at_10
      value: 42.315999999999995
    - type: mrr_at_100
      value: 43.254
    - type: mrr_at_1000
      value: 43.272
    - type: mrr_at_3
      value: 38.176
    - type: mrr_at_5
      value: 40.64
    - type: ndcg_at_1
      value: 27.230999999999998
    - type: ndcg_at_10
      value: 48.551
    - type: ndcg_at_100
      value: 53.737
    - type: ndcg_at_1000
      value: 54.313
    - type: ndcg_at_3
      value: 39.367999999999995
    - type: ndcg_at_5
      value: 44.128
    - type: precision_at_1
      value: 27.230999999999998
    - type: precision_at_10
      value: 8.578
    - type: precision_at_100
      value: 1.145
    - type: precision_at_1000
      value: 0.12
    - type: precision_at_3
      value: 18.704
    - type: precision_at_5
      value: 13.927999999999999
    - type: recall_at_1
      value: 24.02
    - type: recall_at_10
      value: 72.258
    - type: recall_at_100
      value: 94.489
    - type: recall_at_1000
      value: 98.721
    - type: recall_at_3
      value: 48.373
    - type: recall_at_5
      value: 59.388
  - task:
      type: Retrieval
    dataset:
      type: quora
      name: MTEB QuoraRetrieval
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 70.476
    - type: map_at_10
      value: 84.41300000000001
    - type: map_at_100
      value: 85.036
    - type: map_at_1000
      value: 85.055
    - type: map_at_3
      value: 81.45599999999999
    - type: map_at_5
      value: 83.351
    - type: mrr_at_1
      value: 81.07
    - type: mrr_at_10
      value: 87.408
    - type: mrr_at_100
      value: 87.509
    - type: mrr_at_1000
      value: 87.51
    - type: mrr_at_3
      value: 86.432
    - type: mrr_at_5
      value: 87.128
    - type: ndcg_at_1
      value: 81.13
    - type: ndcg_at_10
      value: 88.18599999999999
    - type: ndcg_at_100
      value: 89.401
    - type: ndcg_at_1000
      value: 89.515
    - type: ndcg_at_3
      value: 85.332
    - type: ndcg_at_5
      value: 86.97
    - type: precision_at_1
      value: 81.13
    - type: precision_at_10
      value: 13.361
    - type: precision_at_100
      value: 1.5230000000000001
    - type: precision_at_1000
      value: 0.156
    - type: precision_at_3
      value: 37.31
    - type: precision_at_5
      value: 24.548000000000002
    - type: recall_at_1
      value: 70.476
    - type: recall_at_10
      value: 95.3
    - type: recall_at_100
      value: 99.46000000000001
    - type: recall_at_1000
      value: 99.96000000000001
    - type: recall_at_3
      value: 87.057
    - type: recall_at_5
      value: 91.739
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering
      name: MTEB RedditClustering
      config: default
      split: test
      revision: 24640382cdbf8abc73003fb0fa6d111a705499eb
    metrics:
    - type: v_measure
      value: 55.36775089400664
  - task:
      type: Clustering
    dataset:
      type: mteb/reddit-clustering-p2p
      name: MTEB RedditClusteringP2P
      config: default
      split: test
      revision: 282350215ef01743dc01b456c7f5241fa8937f16
    metrics:
    - type: v_measure
      value: 60.05041008018361
  - task:
      type: Retrieval
    dataset:
      type: scidocs
      name: MTEB SCIDOCS
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 4.743
    - type: map_at_10
      value: 12.171
    - type: map_at_100
      value: 14.174999999999999
    - type: map_at_1000
      value: 14.446
    - type: map_at_3
      value: 8.698
    - type: map_at_5
      value: 10.444
    - type: mrr_at_1
      value: 23.400000000000002
    - type: mrr_at_10
      value: 34.284
    - type: mrr_at_100
      value: 35.400999999999996
    - type: mrr_at_1000
      value: 35.451
    - type: mrr_at_3
      value: 31.167
    - type: mrr_at_5
      value: 32.946999999999996
    - type: ndcg_at_1
      value: 23.400000000000002
    - type: ndcg_at_10
      value: 20.169999999999998
    - type: ndcg_at_100
      value: 27.967
    - type: ndcg_at_1000
      value: 32.982
    - type: ndcg_at_3
      value: 19.308
    - type: ndcg_at_5
      value: 16.837
    - type: precision_at_1
      value: 23.400000000000002
    - type: precision_at_10
      value: 10.41
    - type: precision_at_100
      value: 2.162
    - type: precision_at_1000
      value: 0.338
    - type: precision_at_3
      value: 18.067
    - type: precision_at_5
      value: 14.78
    - type: recall_at_1
      value: 4.743
    - type: recall_at_10
      value: 21.098
    - type: recall_at_100
      value: 43.85
    - type: recall_at_1000
      value: 68.60000000000001
    - type: recall_at_3
      value: 10.993
    - type: recall_at_5
      value: 14.998000000000001
  - task:
      type: STS
    dataset:
      type: mteb/sickr-sts
      name: MTEB SICK-R
      config: default
      split: test
      revision: a6ea5a8cab320b040a23452cc28066d9beae2cee
    metrics:
    - type: cos_sim_pearson
      value: 81.129376905658
    - type: cos_sim_spearman
      value: 74.18938626206575
    - type: euclidean_pearson
      value: 77.95192851803141
    - type: euclidean_spearman
      value: 74.18938626206575
    - type: manhattan_pearson
      value: 77.97718819383338
    - type: manhattan_spearman
      value: 74.20580317409417
  - task:
      type: STS
    dataset:
      type: mteb/sts12-sts
      name: MTEB STS12
      config: default
      split: test
      revision: a0d554a64d88156834ff5ae9920b964011b16384
    metrics:
    - type: cos_sim_pearson
      value: 78.36913772828827
    - type: cos_sim_spearman
      value: 73.22311186990363
    - type: euclidean_pearson
      value: 74.45263405031004
    - type: euclidean_spearman
      value: 73.22311186990363
    - type: manhattan_pearson
      value: 74.56201270071791
    - type: manhattan_spearman
      value: 73.26490493774821
  - task:
      type: STS
    dataset:
      type: mteb/sts13-sts
      name: MTEB STS13
      config: default
      split: test
      revision: 7e90230a92c190f1bf69ae9002b8cea547a64cca
    metrics:
    - type: cos_sim_pearson
      value: 84.79920796384403
    - type: cos_sim_spearman
      value: 84.77145185366201
    - type: euclidean_pearson
      value: 83.90638366191354
    - type: euclidean_spearman
      value: 84.77145185366201
    - type: manhattan_pearson
      value: 83.83788216629048
    - type: manhattan_spearman
      value: 84.70515987131665
  - task:
      type: STS
    dataset:
      type: mteb/sts14-sts
      name: MTEB STS14
      config: default
      split: test
      revision: 6031580fec1f6af667f0bd2da0a551cf4f0b2375
    metrics:
    - type: cos_sim_pearson
      value: 83.18883765092875
    - type: cos_sim_spearman
      value: 79.9948128016449
    - type: euclidean_pearson
      value: 81.57436738666773
    - type: euclidean_spearman
      value: 79.9948128016449
    - type: manhattan_pearson
      value: 81.55274202648187
    - type: manhattan_spearman
      value: 79.99854975019382
  - task:
      type: STS
    dataset:
      type: mteb/sts15-sts
      name: MTEB STS15
      config: default
      split: test
      revision: ae752c7c21bf194d8b67fd573edf7ae58183cbe3
    metrics:
    - type: cos_sim_pearson
      value: 86.89669110871021
    - type: cos_sim_spearman
      value: 87.26758456901442
    - type: euclidean_pearson
      value: 86.62614163641416
    - type: euclidean_spearman
      value: 87.26758456901442
    - type: manhattan_pearson
      value: 86.58584490012353
    - type: manhattan_spearman
      value: 87.20340001562076
  - task:
      type: STS
    dataset:
      type: mteb/sts16-sts
      name: MTEB STS16
      config: default
      split: test
      revision: 4d8694f8f0e0100860b497b999b3dbed754a0513
    metrics:
    - type: cos_sim_pearson
      value: 81.983023415916
    - type: cos_sim_spearman
      value: 82.31169002657151
    - type: euclidean_pearson
      value: 81.52305092886222
    - type: euclidean_spearman
      value: 82.31169002657151
    - type: manhattan_pearson
      value: 81.63024996600281
    - type: manhattan_spearman
      value: 82.44579116264026
  - task:
      type: STS
    dataset:
      type: mteb/sts17-crosslingual-sts
      name: MTEB STS17 (en-en)
      config: en-en
      split: test
      revision: af5e6fb845001ecf41f4c1e033ce921939a2a68d
    metrics:
    - type: cos_sim_pearson
      value: 89.27779520541694
    - type: cos_sim_spearman
      value: 89.54137104681308
    - type: euclidean_pearson
      value: 88.99136079955996
    - type: euclidean_spearman
      value: 89.54137104681308
    - type: manhattan_pearson
      value: 88.95980417618277
    - type: manhattan_spearman
      value: 89.55178819334718
  - task:
      type: STS
    dataset:
      type: mteb/sts22-crosslingual-sts
      name: MTEB STS22 (en)
      config: en
      split: test
      revision: 6d1ba47164174a496b7fa5d3569dae26a6813b80
    metrics:
    - type: cos_sim_pearson
      value: 66.50806758829178
    - type: cos_sim_spearman
      value: 65.92675365587571
    - type: euclidean_pearson
      value: 67.09216876696559
    - type: euclidean_spearman
      value: 65.92675365587571
    - type: manhattan_pearson
      value: 67.37398716891478
    - type: manhattan_spearman
      value: 66.34811143508206
  - task:
      type: STS
    dataset:
      type: mteb/stsbenchmark-sts
      name: MTEB STSBenchmark
      config: default
      split: test
      revision: b0fddb56ed78048fa8b90373c8a3cfc37b684831
    metrics:
    - type: cos_sim_pearson
      value: 84.557575753862
    - type: cos_sim_spearman
      value: 83.95859527071087
    - type: euclidean_pearson
      value: 83.77287626715369
    - type: euclidean_spearman
      value: 83.95859527071087
    - type: manhattan_pearson
      value: 83.7898033034244
    - type: manhattan_spearman
      value: 83.94860981294184
  - task:
      type: Reranking
    dataset:
      type: mteb/scidocs-reranking
      name: MTEB SciDocsRR
      config: default
      split: test
      revision: d3c5e1fc0b855ab6097bf1cda04dd73947d7caab
    metrics:
    - type: map
      value: 79.90679624144718
    - type: mrr
      value: 94.33150183150182
  - task:
      type: Retrieval
    dataset:
      type: scifact
      name: MTEB SciFact
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 56.81699999999999
    - type: map_at_10
      value: 67.301
    - type: map_at_100
      value: 67.73599999999999
    - type: map_at_1000
      value: 67.757
    - type: map_at_3
      value: 64.865
    - type: map_at_5
      value: 66.193
    - type: mrr_at_1
      value: 59.667
    - type: mrr_at_10
      value: 68.324
    - type: mrr_at_100
      value: 68.66
    - type: mrr_at_1000
      value: 68.676
    - type: mrr_at_3
      value: 66.556
    - type: mrr_at_5
      value: 67.472
    - type: ndcg_at_1
      value: 59.667
    - type: ndcg_at_10
      value: 71.982
    - type: ndcg_at_100
      value: 74.149
    - type: ndcg_at_1000
      value: 74.60799999999999
    - type: ndcg_at_3
      value: 67.796
    - type: ndcg_at_5
      value: 69.64099999999999
    - type: precision_at_1
      value: 59.667
    - type: precision_at_10
      value: 9.633
    - type: precision_at_100
      value: 1.08
    - type: precision_at_1000
      value: 0.11199999999999999
    - type: precision_at_3
      value: 26.889000000000003
    - type: precision_at_5
      value: 17.467
    - type: recall_at_1
      value: 56.81699999999999
    - type: recall_at_10
      value: 85.18900000000001
    - type: recall_at_100
      value: 95.6
    - type: recall_at_1000
      value: 99.0
    - type: recall_at_3
      value: 73.617
    - type: recall_at_5
      value: 78.444
  - task:
      type: PairClassification
    dataset:
      type: mteb/sprintduplicatequestions-pairclassification
      name: MTEB SprintDuplicateQuestions
      config: default
      split: test
      revision: d66bd1f72af766a5cc4b0ca5e00c162f89e8cc46
    metrics:
    - type: cos_sim_accuracy
      value: 99.83465346534653
    - type: cos_sim_ap
      value: 95.93387984443646
    - type: cos_sim_f1
      value: 91.49261334691798
    - type: cos_sim_precision
      value: 93.25025960539979
    - type: cos_sim_recall
      value: 89.8
    - type: dot_accuracy
      value: 99.83465346534653
    - type: dot_ap
      value: 95.93389375761485
    - type: dot_f1
      value: 91.49261334691798
    - type: dot_precision
      value: 93.25025960539979
    - type: dot_recall
      value: 89.8
    - type: euclidean_accuracy
      value: 99.83465346534653
    - type: euclidean_ap
      value: 95.93389375761487
    - type: euclidean_f1
      value: 91.49261334691798
    - type: euclidean_precision
      value: 93.25025960539979
    - type: euclidean_recall
      value: 89.8
    - type: manhattan_accuracy
      value: 99.83564356435643
    - type: manhattan_ap
      value: 95.89877504534601
    - type: manhattan_f1
      value: 91.53061224489795
    - type: manhattan_precision
      value: 93.4375
    - type: manhattan_recall
      value: 89.7
    - type: max_accuracy
      value: 99.83564356435643
    - type: max_ap
      value: 95.93389375761487
    - type: max_f1
      value: 91.53061224489795
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering
      name: MTEB StackExchangeClustering
      config: default
      split: test
      revision: 6cbc1f7b2bc0622f2e39d2c77fa502909748c259
    metrics:
    - type: v_measure
      value: 62.2780055191805
  - task:
      type: Clustering
    dataset:
      type: mteb/stackexchange-clustering-p2p
      name: MTEB StackExchangeClusteringP2P
      config: default
      split: test
      revision: 815ca46b2622cec33ccafc3735d572c266efdb44
    metrics:
    - type: v_measure
      value: 33.94461701798904
  - task:
      type: Reranking
    dataset:
      type: mteb/stackoverflowdupquestions-reranking
      name: MTEB StackOverflowDupQuestions
      config: default
      split: test
      revision: e185fbe320c72810689fc5848eb6114e1ef5ec69
    metrics:
    - type: map
      value: 49.865789666749535
    - type: mrr
      value: 50.61783804430863
  - task:
      type: Summarization
    dataset:
      type: mteb/summeval
      name: MTEB SummEval
      config: default
      split: test
      revision: cda12ad7615edc362dbf25a00fdd61d3b1eaf93c
    metrics:
    - type: cos_sim_pearson
      value: 29.97703436199298
    - type: cos_sim_spearman
      value: 30.71880290978946
    - type: dot_pearson
      value: 29.977036284086818
    - type: dot_spearman
      value: 30.71880290978946
  - task:
      type: Retrieval
    dataset:
      type: trec-covid
      name: MTEB TRECCOVID
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 0.22799999999999998
    - type: map_at_10
      value: 1.559
    - type: map_at_100
      value: 8.866
    - type: map_at_1000
      value: 23.071
    - type: map_at_3
      value: 0.592
    - type: map_at_5
      value: 0.906
    - type: mrr_at_1
      value: 84.0
    - type: mrr_at_10
      value: 88.567
    - type: mrr_at_100
      value: 88.748
    - type: mrr_at_1000
      value: 88.748
    - type: mrr_at_3
      value: 87.667
    - type: mrr_at_5
      value: 88.067
    - type: ndcg_at_1
      value: 73.0
    - type: ndcg_at_10
      value: 62.202999999999996
    - type: ndcg_at_100
      value: 49.66
    - type: ndcg_at_1000
      value: 48.760999999999996
    - type: ndcg_at_3
      value: 67.52
    - type: ndcg_at_5
      value: 64.80799999999999
    - type: precision_at_1
      value: 84.0
    - type: precision_at_10
      value: 65.4
    - type: precision_at_100
      value: 51.72
    - type: precision_at_1000
      value: 22.014
    - type: precision_at_3
      value: 74.0
    - type: precision_at_5
      value: 69.19999999999999
    - type: recall_at_1
      value: 0.22799999999999998
    - type: recall_at_10
      value: 1.7680000000000002
    - type: recall_at_100
      value: 12.581999999999999
    - type: recall_at_1000
      value: 46.883
    - type: recall_at_3
      value: 0.618
    - type: recall_at_5
      value: 0.9690000000000001
  - task:
      type: Retrieval
    dataset:
      type: webis-touche2020
      name: MTEB Touche2020
      config: default
      split: test
      revision: None
    metrics:
    - type: map_at_1
      value: 1.295
    - type: map_at_10
      value: 7.481
    - type: map_at_100
      value: 13.120999999999999
    - type: map_at_1000
      value: 14.863999999999999
    - type: map_at_3
      value: 3.266
    - type: map_at_5
      value: 4.662
    - type: mrr_at_1
      value: 14.285999999999998
    - type: mrr_at_10
      value: 31.995
    - type: mrr_at_100
      value: 33.415
    - type: mrr_at_1000
      value: 33.432
    - type: mrr_at_3
      value: 27.551
    - type: mrr_at_5
      value: 30.306
    - type: ndcg_at_1
      value: 11.224
    - type: ndcg_at_10
      value: 19.166
    - type: ndcg_at_100
      value: 31.86
    - type: ndcg_at_1000
      value: 44.668
    - type: ndcg_at_3
      value: 17.371
    - type: ndcg_at_5
      value: 18.567
    - type: precision_at_1
      value: 14.285999999999998
    - type: precision_at_10
      value: 18.98
    - type: precision_at_100
      value: 7.041
    - type: precision_at_1000
      value: 1.555
    - type: precision_at_3
      value: 19.728
    - type: precision_at_5
      value: 20.816000000000003
    - type: recall_at_1
      value: 1.295
    - type: recall_at_10
      value: 14.482000000000001
    - type: recall_at_100
      value: 45.149
    - type: recall_at_1000
      value: 84.317
    - type: recall_at_3
      value: 4.484
    - type: recall_at_5
      value: 7.7170000000000005
  - task:
      type: Classification
    dataset:
      type: mteb/toxic_conversations_50k
      name: MTEB ToxicConversationsClassification
      config: default
      split: test
      revision: d7c0de2777da35d6aae2200a62c6e0e5af397c4c
    metrics:
    - type: accuracy
      value: 72.96340000000001
    - type: ap
      value: 15.62835559397026
    - type: f1
      value: 56.42561616707867
  - task:
      type: Classification
    dataset:
      type: mteb/tweet_sentiment_extraction
      name: MTEB TweetSentimentExtractionClassification
      config: default
      split: test
      revision: d604517c81ca91fe16a244d1248fc021f9ecee7a
    metrics:
    - type: accuracy
      value: 55.280135823429546
    - type: f1
      value: 55.61428067547153
  - task:
      type: Clustering
    dataset:
      type: mteb/twentynewsgroups-clustering
      name: MTEB TwentyNewsgroupsClustering
      config: default
      split: test
      revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
    metrics:
    - type: v_measure
      value: 45.426677723253555
  - task:
      type: PairClassification
    dataset:
      type: mteb/twittersemeval2015-pairclassification
      name: MTEB TwitterSemEval2015
      config: default
      split: test
      revision: 70970daeab8776df92f5ea462b6173c0b46fd2d1
    metrics:
    - type: cos_sim_accuracy
      value: 84.57411933003517
    - type: cos_sim_ap
      value: 69.68254951354992
    - type: cos_sim_f1
      value: 65.05232416646386
    - type: cos_sim_precision
      value: 60.36585365853659
    - type: cos_sim_recall
      value: 70.52770448548813
    - type: dot_accuracy
      value: 84.57411933003517
    - type: dot_ap
      value: 69.68256519978905
    - type: dot_f1
      value: 65.05232416646386
    - type: dot_precision
      value: 60.36585365853659
    - type: dot_recall
      value: 70.52770448548813
    - type: euclidean_accuracy
      value: 84.57411933003517
    - type: euclidean_ap
      value: 69.6825655240522
    - type: euclidean_f1
      value: 65.05232416646386
    - type: euclidean_precision
      value: 60.36585365853659
    - type: euclidean_recall
      value: 70.52770448548813
    - type: manhattan_accuracy
      value: 84.5502771651666
    - type: manhattan_ap
      value: 69.61700491283233
    - type: manhattan_f1
      value: 64.83962148211872
    - type: manhattan_precision
      value: 60.68553025074765
    - type: manhattan_recall
      value: 69.6042216358839
    - type: max_accuracy
      value: 84.57411933003517
    - type: max_ap
      value: 69.6825655240522
    - type: max_f1
      value: 65.05232416646386
  - task:
      type: PairClassification
    dataset:
      type: mteb/twitterurlcorpus-pairclassification
      name: MTEB TwitterURLCorpus
      config: default
      split: test
      revision: 8b6510b0b1fa4e4c4f879467980e9be563ec1cdf
    metrics:
    - type: cos_sim_accuracy
      value: 88.80350836341057
    - type: cos_sim_ap
      value: 85.41051415803449
    - type: cos_sim_f1
      value: 77.99305633329602
    - type: cos_sim_precision
      value: 75.70113776360607
    - type: cos_sim_recall
      value: 80.42808746535263
    - type: dot_accuracy
      value: 88.80350836341057
    - type: dot_ap
      value: 85.41051488820463
    - type: dot_f1
      value: 77.99305633329602
    - type: dot_precision
      value: 75.70113776360607
    - type: dot_recall
      value: 80.42808746535263
    - type: euclidean_accuracy
      value: 88.80350836341057
    - type: euclidean_ap
      value: 85.41051374760137
    - type: euclidean_f1
      value: 77.99305633329602
    - type: euclidean_precision
      value: 75.70113776360607
    - type: euclidean_recall
      value: 80.42808746535263
    - type: manhattan_accuracy
      value: 88.74529436876625
    - type: manhattan_ap
      value: 85.38380242074525
    - type: manhattan_f1
      value: 78.02957839746892
    - type: manhattan_precision
      value: 74.71466816964914
    - type: manhattan_recall
      value: 81.65229442562365
    - type: max_accuracy
      value: 88.80350836341057
    - type: max_ap
      value: 85.41051488820463
    - type: max_f1
      value: 78.02957839746892
---


# nomic-embed-text-v1-unsupervised: A Reproducible Long Context (8192) Text Embedder 

`nomic-embed-text-v1-unsupervised` is 8192 context length text encoder. This is a checkpoint after contrastive pretraining from multi-stage contrastive training of the
[final model](https://huggingface.co/nomic-ai/nomic-embed-text-v1). The purpose of releasing this checkpoint is to open-source training artifacts from our Nomic Embed Text tech report [here](https://arxiv.org/pdf/2402.01613)

If you want to use a model to extract embeddings, we suggest using [nomic-embed-text-v1](https://huggingface.co/nomic-ai/nomic-embed-text-v1).


# Join the Nomic Community

- Nomic: [https://nomic.ai](https://nomic.ai)
- Discord: [https://discord.gg/myY5YDR8z8](https://discord.gg/myY5YDR8z8)
- Twitter: [https://twitter.com/nomic_ai](https://twitter.com/nomic_ai)
