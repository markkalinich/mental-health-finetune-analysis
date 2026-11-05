---
library_name: ilex
tags:
- jax
- equinox
- ilex
- neuroimaging
- 3d
license: mit
license_link: https://opensource.org/licenses/MIT
---

# MedicalNet 3D-ResNet (medical-imaging transfer backbone) -- MedicalNet ResNet-50 (23-dataset pretrain)

## Description

MedicalNet (Chen et al., *Med3D: Transfer Learning for 3D Medical Image Analysis* 2019), ported to JAX / Equinox from the Tencent PyTorch release (github.com/Tencent/MedicalNet). A 3D ResNet trunk pretrained on a consortium of 23 medical-imaging segmentation datasets, packaged as a transfer-learning backbone for downstream 3D medical-imaging tasks (segmentation, classification, regression). The published release has seven depths (10 / 18 / 34 / 50 / 101 / 152 / 200) sharing the same architecture template; only the block type (BasicBlock for depths <= 34; Bottleneck for >= 50) and the per-stage block-count vector differ. The stem (7^3 stride-2 conv + BN + ReLU + 3^3 stride-2 maxpool) and four-stage layout (strides 1/2/1/1; dilations 1/1/2/4) are identical across depths. The ilex port ships the **headless encoder** -- the upstream's conv_seg ConvTranspose+BN+Conv segmentation decoder was a MICCAI-2019 evaluation artefact, not part of the transfer-learning backbone the published weights are designed for. Consumers attach their own task heads.

## Intended use

Most-cited variant; the de-facto transfer-learning backbone for 3D medical-imaging tasks. Headless trunk (Bottleneck blocks, expansion=4); layer4 output is ``(2048, D/8, H/8, W/8)``. Inputs are single-channel 3D volumes (CT or MRI) at any multiple-of-8 spatial grid.

## Usage

```python
from ilex.models.medical_net import MedicalNet
model = MedicalNet.from_pretrained('ilex-hub/medical_net.50.1')
```

## Authors

Sihong Chen, Kai Ma, Yefeng Zheng (Tencent Healthcare, Youtu Lab)

## Citation

Chen S., Ma K., Zheng Y. (2019). Med3D: Transfer Learning for 3D Medical Image Analysis. arXiv:1904.00625.

### References

- Chen S., Ma K., Zheng Y. (2019). Med3D: Transfer Learning for 3D Medical Image Analysis. arXiv:1904.00625.
- Upstream code: github.com/Tencent/MedicalNet (models/resnet.py; weights mirrored to huggingface.co/TencentMedicalNet/MedicalNet-Resnet*).

## License

HF Hub license tag: `mit`

**Effective terms:** MIT (Tencent Healthcare -- Chen, Ma, Zheng) on both the network code (github.com/Tencent/MedicalNet) and the pretrained weights (mirrored at huggingface.co/TencentMedicalNet/MedicalNet-Resnet*). The ilex JAX / Equinox port code is separately licensed under Apache-2.0 / GPL-3.0.

Upstream license reference: https://opensource.org/licenses/MIT

### Copyright

Network architecture and pretrained weights -- copyright (c) Tencent Healthcare, released under the MIT License. JAX / Equinox port code -- copyright (c) the ilex authors, released under the Apache-2.0 / GPL-3.0 dual license used by ilex itself.

## Upstream source

Original weights / reference implementation: https://github.com/Tencent/MedicalNet

## Provenance

This artefact was produced by [ilex](https://github.com/hypercoil/ilex)'s
save/load pipeline. The architecture is implemented in
`ilex.models.medical_net.MedicalNet` and the weights have been converted
from their upstream format. See the upstream source above
for the canonical reference.
