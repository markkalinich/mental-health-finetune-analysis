---
library_name: transformers
tags: []
---

## Original result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.004
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.004
```

## After training result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.003
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.011
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.037
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.074
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.084
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.006
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.085
```

## Config
- dataset: NIH
- original model: facebook/detr-resnet-50
- lr: 5e-05
- max_epochs: 10

## Logging
### Training process
```
{'validation_loss': tensor(6.4663, device='cuda:0'), 'validation_loss_ce': tensor(2.5639, device='cuda:0'), 'validation_loss_bbox': tensor(0.4662, device='cuda:0'), 'validation_loss_giou': tensor(0.7858, device='cuda:0'), 'validation_cardinality_error': tensor(98.8125, device='cuda:0')}
{'training_loss': tensor(4.3831, device='cuda:0'), 'train_loss_ce': tensor(1.5780, device='cuda:0'), 'train_loss_bbox': tensor(0.2546, device='cuda:0'), 'train_loss_giou': tensor(0.7661, device='cuda:0'), 'train_cardinality_error': tensor(3.7500, device='cuda:0'), 'validation_loss': tensor(4.1328, device='cuda:0'), 'validation_loss_ce': tensor(1.5373, device='cuda:0'), 'validation_loss_bbox': tensor(0.2405, device='cuda:0'), 'validation_loss_giou': tensor(0.6965, device='cuda:0'), 'validation_cardinality_error': tensor(1.4364, device='cuda:0')}
{'training_loss': tensor(2.8787, device='cuda:0'), 'train_loss_ce': tensor(0.7759, device='cuda:0'), 'train_loss_bbox': tensor(0.1841, device='cuda:0'), 'train_loss_giou': tensor(0.5911, device='cuda:0'), 'train_cardinality_error': tensor(1.0625, device='cuda:0'), 'validation_loss': tensor(2.8971, device='cuda:0'), 'validation_loss_ce': tensor(0.7507, device='cuda:0'), 'validation_loss_bbox': tensor(0.1935, device='cuda:0'), 'validation_loss_giou': tensor(0.5893, device='cuda:0'), 'validation_cardinality_error': tensor(1.1159, device='cuda:0')}
{'training_loss': tensor(2.8165, device='cuda:0'), 'train_loss_ce': tensor(0.5296, device='cuda:0'), 'train_loss_bbox': tensor(0.2043, device='cuda:0'), 'train_loss_giou': tensor(0.6328, device='cuda:0'), 'train_cardinality_error': tensor(1.0625, device='cuda:0'), 'validation_loss': tensor(2.6196, device='cuda:0'), 'validation_loss_ce': tensor(0.5727, device='cuda:0'), 'validation_loss_bbox': tensor(0.1831, device='cuda:0'), 'validation_loss_giou': tensor(0.5656, device='cuda:0'), 'validation_cardinality_error': tensor(1.1159, device='cuda:0')}
{'training_loss': tensor(2.6336, device='cuda:0'), 'train_loss_ce': tensor(0.5603, device='cuda:0'), 'train_loss_bbox': tensor(0.1886, device='cuda:0'), 'train_loss_giou': tensor(0.5651, device='cuda:0'), 'train_cardinality_error': tensor(1.1875, device='cuda:0'), 'validation_loss': tensor(2.4110, device='cuda:0'), 'validation_loss_ce': tensor(0.5158, device='cuda:0'), 'validation_loss_bbox': tensor(0.1616, device='cuda:0'), 'validation_loss_giou': tensor(0.5437, device='cuda:0'), 'validation_cardinality_error': tensor(1.1159, device='cuda:0')}
{'training_loss': tensor(2.3404, device='cuda:0'), 'train_loss_ce': tensor(0.4770, device='cuda:0'), 'train_loss_bbox': tensor(0.1684, device='cuda:0'), 'train_loss_giou': tensor(0.5106, device='cuda:0'), 'train_cardinality_error': tensor(1.2500, device='cuda:0'), 'validation_loss': tensor(2.3158, device='cuda:0'), 'validation_loss_ce': tensor(0.5015, device='cuda:0'), 'validation_loss_bbox': tensor(0.1579, device='cuda:0'), 'validation_loss_giou': tensor(0.5123, device='cuda:0'), 'validation_cardinality_error': tensor(1.1159, device='cuda:0')}
{'training_loss': tensor(2.4181, device='cuda:0'), 'train_loss_ce': tensor(0.4818, device='cuda:0'), 'train_loss_bbox': tensor(0.1594, device='cuda:0'), 'train_loss_giou': tensor(0.5697, device='cuda:0'), 'train_cardinality_error': tensor(1.0625, device='cuda:0'), 'validation_loss': tensor(2.2529, device='cuda:0'), 'validation_loss_ce': tensor(0.4929, device='cuda:0'), 'validation_loss_bbox': tensor(0.1507, device='cuda:0'), 'validation_loss_giou': tensor(0.5034, device='cuda:0'), 'validation_cardinality_error': tensor(1.1159, device='cuda:0')}
{'training_loss': tensor(2.3413, device='cuda:0'), 'train_loss_ce': tensor(0.6037, device='cuda:0'), 'train_loss_bbox': tensor(0.1422, device='cuda:0'), 'train_loss_giou': tensor(0.5133, device='cuda:0'), 'train_cardinality_error': tensor(1.3750, device='cuda:0'), 'validation_loss': tensor(2.2137, device='cuda:0'), 'validation_loss_ce': tensor(0.4902, device='cuda:0'), 'validation_loss_bbox': tensor(0.1481, device='cuda:0'), 'validation_loss_giou': tensor(0.4914, device='cuda:0'), 'validation_cardinality_error': tensor(1.1159, device='cuda:0')}
{'training_loss': tensor(2.3693, device='cuda:0'), 'train_loss_ce': tensor(0.4641, device='cuda:0'), 'train_loss_bbox': tensor(0.1578, device='cuda:0'), 'train_loss_giou': tensor(0.5582, device='cuda:0'), 'train_cardinality_error': tensor(1.1250, device='cuda:0'), 'validation_loss': tensor(2.1577, device='cuda:0'), 'validation_loss_ce': tensor(0.4842, device='cuda:0'), 'validation_loss_bbox': tensor(0.1380, device='cuda:0'), 'validation_loss_giou': tensor(0.4917, device='cuda:0'), 'validation_cardinality_error': tensor(1.1159, device='cuda:0')}
{'training_loss': tensor(2.0663, device='cuda:0'), 'train_loss_ce': tensor(0.4912, device='cuda:0'), 'train_loss_bbox': tensor(0.1322, device='cuda:0'), 'train_loss_giou': tensor(0.4571, device='cuda:0'), 'train_cardinality_error': tensor(1.1250, device='cuda:0'), 'validation_loss': tensor(2.1651, device='cuda:0'), 'validation_loss_ce': tensor(0.4833, device='cuda:0'), 'validation_loss_bbox': tensor(0.1443, device='cuda:0'), 'validation_loss_giou': tensor(0.4801, device='cuda:0'), 'validation_cardinality_error': tensor(1.1159, device='cuda:0')}
{'training_loss': tensor(2.2925, device='cuda:0'), 'train_loss_ce': tensor(0.3871, device='cuda:0'), 'train_loss_bbox': tensor(0.1779, device='cuda:0'), 'train_loss_giou': tensor(0.5079, device='cuda:0'), 'train_cardinality_error': tensor(1.0625, device='cuda:0'), 'validation_loss': tensor(2.2612, device='cuda:0'), 'validation_loss_ce': tensor(0.4804, device='cuda:0'), 'validation_loss_bbox': tensor(0.1531, device='cuda:0'), 'validation_loss_giou': tensor(0.5077, device='cuda:0'), 'validation_cardinality_error': tensor(1.1159, device='cuda:0')}
```
