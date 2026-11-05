---
license: apache-2.0
pipeline_tag: image-segmentation
tags:
- medical
- anomaly detection
- VAE
- ceVAE
- cceVAE
- Compact ceVAE
- unsupervised learning
- 2D
- StRegA
- tumour segmentation
- T1w
- T2w
- MRI
- 3T
- BraTS
- MOOD
- IXI
- brain MRI
- anomaly
library_name: pytorch
---
# PULASki_ProbUNet2D_Hausdorff_VSeg

Expert interpretation of anatomical images of the human brain is the central part of neuro-radiology. Several machine learning-based
 techniques have been proposed to assist in the analysis process. However, the ML models typically need to be trained to perform
 a specific task, e.g., brain tumour segmentation or classification. Not only do the corresponding training data require laborious
 manual annotations, but a wide variety of abnormalities can be present in a human brain MRI- even more than one simultaneously,
 which renders a representation of all possible anomalies very challenging. Hence, a possible solution is an unsupervised anomaly
 detection (UAD) system that can learn a data distribution from an unlabelled dataset of healthy subjects and then be applied to
 detect out-of-distribution samples. Such a technique can then be used to detect anomalies- lesions or abnormalities, for example,
 brain tumours, without explicitly training the model for that specific pathology. Several Variational Autoencoder (VAE) based
 techniques have been proposed in the past for this task. Even though they perform very well on controlled artificially simulated
 anomalies, many of them perform poorly while detecting anomalies in clinical data. This research proposes a compact version of the
 “context-encoding” VAE (ceVAE) model, combined with pre and post-processing steps, creating a UAD pipeline (StRegA), which
 is more robust on clinical data and shows its applicability in detecting anomalies such as tumours in brain MRIs.
## Model Details

It was introduced in [StRegA: Unsupervised Anomaly Detection in Brain MRIs using a Compact Context-encoding Variational Autoencoder](https://doi.org/10.1016/j.compbiomed.2022.106093) by Soumick Chatterjee, Alessandro Sciarra, Max Dünnwald, Pavan Tummala, Shubham Kumar Agrawal, Aishwarya Jauhari, Aman Kalra, Steffen Oeltze-Jafra, Oliver Speck, Andreas Nürnberger. [ArXiv preprint]( https://arxiv.org/abs/2201.13271)

### Model Description

- **Model type:** Compact Context-encoding VAE (cceVAE) 2D
- **Task:** Anomaly detection in brain MRIs (T1w, T2w or PDw)
- **Training dataset:** MOOD T1 dataset, and brain-extracted T1w, T2w, PDw from the IXI dataset 

### Model Sources

<!-- Provide the basic links for the model. -->

- **Repository:** https://github.com/soumickmj/StRegA
- **Paper:** https://doi.org/10.1016/j.compbiomed.2022.106093
- **Prepring:** https://arxiv.org/abs/2201.13271

## Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

If you use this approach in your research or use codes from this repository or these weights, please cite the following in your publications:

**BibTeX:**

```bibtex
@article{chatterjee2022strega,
  title={StRegA: Unsupervised Anomaly Detection in Brain MRIs using a Compact Context-encoding Variational Autoencoder},
  author={Chatterjee, Soumick and Sciarra, Alessandro and D{\"u}nnwald, Max and Tummala, Pavan and Agrawal, Shubham Kumar and Jauhari, Aishwarya and Kalra, Aman and Oeltze-Jafra, Steffen and Speck, Oliver and N{\"u}rnberger, Andreas},
  journal={Computers in Biology and Medicine},
  pages={106093},
  year={2022},
  publisher={Elsevier},
  doi={10.1016/j.compbiomed.2022.106093}
}
```

**APA:**

Chatterjee, S., Sciarra, A., Dünnwald, M., Tummala, P., Agrawal, S. K., Jauhari, A., ... & Nürnberger, A. (2022). StRegA: Unsupervised anomaly detection in brain MRIs using a compact context-encoding variational autoencoder. Computers in biology and medicine, 149, 106093.