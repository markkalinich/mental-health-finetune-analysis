---
license: mit
datasets:
- mteb/twentynewsgroups-clustering
- mteb/biorxiv-clustering-s2s
- mteb/biorxiv-clustering-p2p
language:
- en
pipeline_tag: text-classification
library_name: sentence-transformers
tags:
- mteb
- text
- transformers
- text-embeddings-inference
- sparse-encoder
- sparse
- csr
model-index:
- name: CSR
  results:
    - dataset:
        name: MTEB BiorxivClusteringP2P.v2
        type: mteb/biorxiv_clustering_p2p
        revision: f5dbc242e11dd8e24def4c4268607a49e02946dc
        config: default
        split: test
        languages:
          - eng-Latn
      metrics:
        - type: v_measure
          value: 0.579338
        - type: v_measure_std
          value: 0.00337
        - type: main_score
          value: 0.579338
      task:
        type: Clustering

    - dataset:
        name: MTEB BiorxivClusteringS2S.v2
        type: mteb/biorxiv_clustering_s2s
        revision: eb4edb10386758d274cd161093eb351381a16dbf
        config: default
        split: test
        languages:
          - eng-Latn
      metrics:
        - type: v_measure
          value: 0.540989
        - type: v_measure_std
          value: 0.005707
        - type: main_score
          value: 0.540989
      task:
        type: Clustering

    - dataset:
        name: MTEB TwentyNewsgroupsClustering
        type: mteb/twenty_newsgroups_clustering
        revision: 6125ec4e24fa026cec8a478383ee943acfbd5449
        config: default
        split: test
        languages:
          - eng-Latn
      metrics:
        - type: v_measure
          value: 0.630936
        - type: v_measure_std
          value: 0.007942
        - type: main_score
          value: 0.007942
      task:
        type: Clustering
base_model:
- nvidia/NV-Embed-v2
---


For more details, including benchmark evaluation, hardware requirements, and inference performance, please refer to our [Github](https://github.com/neilwen987/CSR_Adaptive_Rep).


## Usage
📌 **Tip**: For NV-Embed-V2, using Transformers versions **later** than 4.47.0 may lead to performance degradation, as ``model_type=bidir_mistral`` in ``config.json`` is no longer supported.

We recommend using ``Transformers 4.47.0.``

### Sentence Transformers Usage
You can evaluate this model loaded by Sentence Transformers with the following code snippet:
```python
import mteb
from sentence_transformers import SparseEncoder
model = SparseEncoder(
    "CSR-NV_Embed_v2-Clustering-Biorxiv_TwentyNews",
    trust_remote_code=True
)
model.prompts = {
    "BiorxivClusteringP2P.v2": "Instruct: Identify the main category of Biorxiv papers based on the titles and abstracts\nQuery:",
    "BiorxivClusteringS2S.v2": "Instruct: Identify the main category of Biorxiv papers based on the titles\nQuery:",
    "TwentyNewsgroupsClustering": "Instruct: Identify the topic or theme of the given news articles\nQuery:"
}
task = mteb.get_tasks(tasks=["BiorxivClusteringP2P.v2", "BiorxivClusteringS2S.v2", "TwentyNewsgroupsClustering"])
evaluation = mteb.MTEB(tasks=task)
evaluation.run(
    model, 
    eval_splits=["test"], 
    output_folder="./results/clustering", 
    show_progress_bar=True
    encode_kwargs={"convert_to_sparse_tensor": False, "batch_size": 8},
)  # MTEB don't support sparse tensors yet, so we need to convert to dense tensors
```

## Citation
```bibtex
@inproceedings{wenbeyond,
  title={Beyond Matryoshka: Revisiting Sparse Coding for Adaptive Representation},
  author={Wen, Tiansheng and Wang, Yifei and Zeng, Zequn and Peng, Zhong and Su, Yudi and Liu, Xinyang and Chen, Bo and Liu, Hongwei and Jegelka, Stefanie and You, Chenyu},
  booktitle={Forty-second International Conference on Machine Learning}
}
```