---
license: cc-by-2.0
datasets:
- allenai/s2orc
language:
- en
pipeline_tag: token-classification
---
Another name for this model is sciDeBERta v2[1].
This model is trained from scratch using S2ORC dataset(260GB), which include abstract, body text of papers, on DeBERTa v2. 
This model achieves the SOTA in NET of SciERC dataset. 
From this model, MediBioDeBERTa, which continuously leaned from scidebert v2. to medibiodeberta using the data from the domain (bio, medical, chemistry domain data)
and additional intermediate fine-tuning for specific blurb benchmark tasks, achieve the 11 rank in the BLURB benchmark. 

[1] Eunhui Kim, Yuna Jeong, Myung-seok Choi, "MediBioDeBERTa: BioMedical Language Model with Continous Learning and Intermediate Fine-Tuning, Dec. 2023, IEEE Access"