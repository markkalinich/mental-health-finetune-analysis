---
license: apache-2.0
pipeline_tag: any-to-any
---

This repository contains the model described in [OmniFlow: Any-to-Any Generation with Multi-Modal Rectified Flows](https://huggingface.co/papers/2412.01169).

Code: [https://github.com/jacklishufan/OmniFlows](https://github.com/jacklishufan/OmniFlows)

Usage:

```
from omniflow import  OmniFlowPipeline

pipeline = OmniFlowPipeline.load_pretrained('ckpts/v0.5',device='cuda')

pipeline.cfg_mode = 'new'
imgs = pipeline("portrait of a cyberpunk girl with neon tattoos and a visor,staring intensely. Standing on top of a building",height=512,width=512,add_token_embed=0,task='t2i')

```

See [Notebook](https://github.com/jacklishufan/OmniFlows/blob/main/scripts/Demo.ipynb) for more examples

