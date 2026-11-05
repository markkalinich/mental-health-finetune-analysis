---
license: llama3.1
tags:
- unsloth
language:
- en
base_model:
- meta-llama/Llama-3.1-8B
---

# Pub-Guard-Llama-8B

**Pub-Guard-Llama-8B** is a fine-tuned version of the Llama-3.1-8B model, specifically designed for detecting fraudulent papers in academic publications. 

[[GitHub]](https://github.com/tigerchen52/pub_guard_llm) 
[[Paper]](https://arxiv.org/abs/2502.15429v1)
[[Pubmed Retraction Benchmark]](https://huggingface.co/datasets/Lihuchen/pubmed_retraction)

Benefits of using this model:
* the first LLM-based system specifically designed for fraud detection in scientific articles
* integration of external resources for better analysis (Semantic Scholar, OpenAlex, Pubmed...)
* it offers powerful predictions with reliable explanations

**Quick Start**

Install Pub-Guard-LLM using pip:
```python
pip install pub-guard-llm
```

An example to show how to use our model to detect fraudulent articles.

```python
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
from pub_guard_llm import PubGuard



input_article = {
    'Title':"Challenges in diagnosis and management of diabetes in the young.",
    'Abstract':"The prevalence of diabetes in children and adolescents is increasing worldwide, with profound implications on the long-term health of individuals, societies, and nations. The diagnosis and management of diabetes in youth presents several unique challenges. Although type 1 diabetes is more common among children and adolescents, the incidence of type 2 diabetes in youth is also on the rise, particularly among certain ethnic groups. In addition, less common types of diabetes such as monogenic diabetes syndromes and diabetes secondary to pancreatopathy (in some parts of the world) need to be accurately identified to initiate the most appropriate treatment. A detailed patient history and physical examination usually provides clues to the diagnosis. However, specific laboratory and imaging tests are needed to confirm the diagnosis. The management of diabetes in children and adolescents is challenging in some cases due to age-specific issues and the more aggressive nature of the disease. Nonetheless, a patient-centered approach focusing on comprehensive risk factor reduction with the involvement of all concerned stakeholders (the patient, parents, peers and teachers) could help in ensuring the best possible level of diabetes control and prevention or delay of long-term complications. ",
    'Authors':["Ranjit Unnikrishnan", "Viral N Shah", "Viswanathan Mohan"],
    'Institutions':["Barbara Davis Center for Diabetes, University of Colorado Anschutz Campus, Aurora, CO USA", "Madras Diabetes Research Foundation & Dr Mohan's Diabetes Specialties Centre, Who Collaborating Centre for Non-Communicable Diseases Prevention and Control, 4, Conran Smith Road, Gopalapuram, Chennai, 600 086 India."],
    'Journal':'Frontiers in Cell and Developmental Biology',
    }

tokenizer = AutoTokenizer.from_pretrained("Lihuchen/pub-guard-llama-8b")
model = AutoModelForCausalLM.from_pretrained("Lihuchen/pub-guard-llama-8b", torch_dtype=torch.bfloat16)
model.to('cuda')

pub_guard = PubGuard(model=model, tokenizer=tokenizer)
answer = pub_guard.predict(input_article)
print(answer)
```


**Datasets**
* [Pubmed Retraction](https://huggingface.co/datasets/Lihuchen/pubmed_retraction)
* [Instruction](https://huggingface.co/datasets/Lihuchen/pubmed_retraction_instruction)

**Experimental Results** 

![image/png](https://cdn-uploads.huggingface.co/production/uploads/63d1954e8eaa4831006600ff/kyb02DvmmiCTdzVK2VNP6.png)



## Examples

### Vanilla Mode


**Input**:
```python
Title: Changes and Influencing Factors of Cognitive Impairment in Patients with Breast Cancer.

Abstract: To investigate the changes in cognitive function and its influencing factors in patients with breast cancer after chemotherapy,
to provide a scientific basis for further cognitive correction therapy. In this study, general information on age,
marital status, and chemotherapy regimen was collected from 172 breast cancer chemotherapy patients.
172 patients with breast cancer undergoing chemotherapy were investigated by convenience sampling method,
and the subjects were tested one-on-one using the Chinese version of the MATRICS Consensus Cognitive Battery (MCCB) computer system.
...

Authors: Huixia Cui (author h-index: 6, Early Career Researcher);
Xiaoxiu Song (author h-index: 1, Emerging Researcher); Wenlu Zhang (author h-index: 7, Early Career Researcher)

Institutions: College of Nursing, Jinzhou Medical University, Jinzhou, Liaoning 121001, China. (institution average citation: 9.0, Emerging Institution);
Department of Intensive Care Medicine, Liaocheng People's Hospital, Liaocheng, Shandong 252000, China. (institution average citation: 10.0, Emerging Institution);

Journal: evidence-based complementary and alternative medicine : ecam (unknown journal)
```

**Output**:
```python
Yes
The article should be retracted due to potential data fabrication or manipulation, as the reported linear regression results lack clarity and statistical validation.
 Additionally, the journal's reputation and peer review rigor are questionable, and the authors' affiliations are emerging with low citation averages,
raising concerns about research reliability.
```

## Citation

If you find our work useful, please give us a citation:

```
@misc{chen2025pubguardllm,
      title={Pub-Guard-LLM: Detecting Fraudulent Biomedical Articles with Reliable Explanations}, 
      author={Lihu Chen and Shuojie Fu and Gabriel Freedman and Cemre Zor and Guy Martin and James Kinross and Uddhav Vaghela and Ovidiu Serban and Francesca Toni},
      year={2025},
      eprint={2502.15429},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2502.15429}, 
}
```