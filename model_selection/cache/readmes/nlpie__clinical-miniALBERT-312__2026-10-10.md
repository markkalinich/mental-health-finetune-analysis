---
license: mit
tags:
- oxford-legacy
---

# Model
miniALBERT is a recursive transformer model which uses cross-layer parameter sharing, embedding factorisation, and bottleneck adapters to achieve high parameter efficiency.
Since miniALBERT is a compact model, it is trained using a layer-to-layer distillation technique, using the BioClinicalBERT model as the teacher. This model is trained for 3 epochs on the MIMIC-III notes dataset.
In terms of architecture, this model uses an embedding dimension of 312, a hidden size of 768, an MLP expansion rate of 4, and a reduction factor of 16 for bottleneck adapters. In general, this model uses 6 recursions and has a unique parameter count of 18 million parameters.

# Usage
Since miniALBERT uses a unique architecture it can not be loaded using ts.AutoModel for now. To load the model, first, clone the miniALBERT GitHub project, using the below code:
```bash
git clone https://github.com/nlpie-research/MiniALBERT.git
```
Then use the ```sys.path.append``` to add the miniALBERT files to your project and then import the miniALBERT modeling file using the below code:
```Python
import sys
sys.path.append("PATH_TO_CLONED_PROJECT/MiniALBERT/")

from minialbert_modeling import MiniAlbertForSequenceClassification, MiniAlbertForTokenClassification
```
Finally, load the model like a regular model in the transformers library using the below code:
```Python
# For NER use the below code
model = MiniAlbertForTokenClassification.from_pretrained("nlpie/clinical-miniALBERT-312")
# For Sequence Classification use the below code
model = MiniAlbertForTokenClassification.from_pretrained("nlpie/clinical-miniALBERT-312")
```

In addition, For efficient fine-tuning using the pre-trained bottleneck adapters use the below code:
```Python
model.trainAdaptersOnly()
```

# Citation

If you use the model, please cite our paper:

```bibtex
@article{rohanian2023lightweight,
  title={Lightweight transformers for clinical natural language processing},
  author={Rohanian, Omid and Nouriborji, Mohammadmahdi and Jauncey, Hannah and Kouchaki, Samaneh and Nooralahzadeh, Farhad and Clifton, Lei and Merson, Laura and Clifton, David A and ISARIC Clinical Characterisation Group and others},
  journal={Natural Language Engineering},
  pages={1--28},
  year={2023},
  publisher={Cambridge University Press}
}
```
# Support
If this model helps your work, you can keep the project running with a one-off or monthly contribution:  
https://github.com/sponsors/nlpie-research