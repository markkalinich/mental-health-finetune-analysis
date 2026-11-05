# CLIN-X-ES: a pre-trained language model for the Spanish clinical domain
Details on the model, the pre-training corpus and the downstream task performance are given in the paper: "CLIN-X: pre-trained language models and a study on cross-task transfer for concept extraction in the clinical domain" by Lukas Lange, Heike Adel, Jannik Strötgen and Dietrich Klakow. 
The paper can be found [here](https://arxiv.org/abs/2112.08754). 
In case of questions, please contact the authors as listed on the paper. 

Please cite the above paper when reporting, reproducing or extending the results.

    @misc{lange-etal-2021-clin-x,
          author    = {Lukas Lange and
                       Heike Adel and
                       Jannik Str{\"{o}}tgen and
                       Dietrich Klakow},
          title     = {CLIN-X: pre-trained language models and a study on cross-task transfer for concept extraction in the clinical domain},
          year={2021},
          eprint={2112.08754},
          archivePrefix={arXiv},
          primaryClass={cs.CL},
          url={https://arxiv.org/abs/2112.08754}
    }

## Training details
The model is based on the multilingual XLM-R transformer `(xlm-roberta-large)`, which was trained on 100 languages and showed superior performance in many different tasks across languages and can even outperform monolingual models in certain settings (Conneau et al. 2020). 
Even though XLM-R was pre-trained on 53GB of Spanish documents, this was only 2% of the overall training data. To steer this model towards the Spanish clinical domain, we sample documents from the Scielo archive (https://scielo.org/)
and the MeSpEn resources (Villegas et al. 2018). The resulting corpus has a size of 790MB and is highly specific for the clinical domain.

We initialize CLIN-X using the pre-trained XLM-R weights and train masked language modeling (MLM) on the Spanish clinical corpus for 3 epochs which roughly corresponds to 32k steps. This allows researchers and practitioners to address
the Spanish clinical domain with an out-of-the-box tailored model.

## Results for Spanish concept extraction
We apply CLIN-X-ES to five Spanish concept extraction tasks from the clinical domain in a standard sequence labeling architecture similar to Devlin et al. 2019 and compare to a Spanish BERT model called BETO. In addition, we perform experiments with an improved architecture `(+ OurArchitecture)` as described in the paper linked above. The code for our model architecture can be found [here](https://github.com/boschresearch/clin_x).

|                                          | Cantemist | Meddocan | Meddoprof (NER) | Meddoprof (CLASS) | Pharmaconer |
|------------------------------------------|-----------|----------|-----------------|-------------------|-------------|
| BETO (Spanish BERT)                      | 81.30     | 96.81    | 79.19           | 74.59             | 87.70       |
| CLIN-X (ES)                              | 83.22     | 97.08    | 79.54           | 76.95             | 90.05       |
| CLIN-X (ES) + OurArchitecture            | **88.24** | **98.00** | **81.68**      | **80.54**         | **92.27**   |


### Results for English concept extraction
As the CLIN-X-ES model is based on XLM-R, the model is still multilingual and we demonstrate the positive impact of cross-language domain adaptation by applying this model to five different English sequence labeling tasks from i2b2. 

We found that further transfer from related concept extraction is particularly helpful in this cross-language setting. For a detailed description of the transfer process and all other models, we refer to our paper. 

|                                          | i2b2 2006 | i2b2 2010 | i2b2 2012 (Concept) | i2b2 2012 (Time) | i2b2 2014 |
|------------------------------------------|-----------|-----------|---------------|---------------|-----------|
| BERT                                     | 94.80     | 85.25     | 76.51         | 75.28         | 94.86     |
| ClinicalBERT                             | 94.8      | 87.8      | 78.9          | 76.6          | 93.0      |
| CLIN-X (ES)                              | 95.49     | 87.94     | 79.58         | 77.57         | 96.80     |
| CLIN-X (ES) + OurArchitecture            | 98.30     | 89.10     | 80.42         | 78.48         | **97.62** |
| CLIN-X (ES) + OurArchitecture + Transfer | **89.50** | **89.74** | **80.93**     | **79.60**     | 97.46     |

## Purpose of the project
This software is a research prototype, solely developed for and published as part of the publication cited above. It will neither be maintained nor monitored in any way.

## License
The CLIN-X models are open-sourced under the CC-BY 4.0 license. 
See the [LICENSE](LICENSE) file for details. 