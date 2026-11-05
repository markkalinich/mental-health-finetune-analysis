---
library_name: transformers
tags: []
---

# Model Card for Med-LLaMA3-8B

<!-- Provide a quick summary of what the model is/does. -->

## Model Details

### Model Description
Med-LLaMA3-8B is an 8-billion parameter medical language model that has undergone continual pre-training on LLaMA3-8B architecture using large-scale open-sourced medical data.

## Training Details

Med-LLaMA3-8B is trained on a large-scale dataset comprising: medical books, medical literature, clinical guidelines and a small portion of general domain data
It is a study extension based on our previous Me-LLaMA paper: https://arxiv.org/pdf/2402.12749

If you use the model, please cite the following papers:

<pre>
@misc{xie2024llama,
      title={Me LLaMA: Foundation Large Language Models for Medical Applications}, 
      author={Qianqian Xie and Qingyu Chen and Aokun Chen and Cheng Peng and Yan Hu and Fongci Lin and Xueqing Peng and Jimin Huang and Jeffrey Zhang and Vipina Keloth and Huan He and Lucila Ohno-Machido and Yonghui Wu and Hua Xu and Jiang Bian},
      year={2024},
      eprint={2402.12749},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
</pre>