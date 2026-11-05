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
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.008
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.017
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.017
```

## After training result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.003
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.007
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.002
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.024
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.066
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.070
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.071
```

## Config
- dataset: NIH
- original model: facebook/detr-resnet-50
- lr: 0.0001
- max_epochs: 3

## Logging

### Training process
```

{'training_loss': tensor(2.0822, device='cuda:0'), 'train_loss_ce': tensor(0.5032, device='cuda:0'), 'train_loss_bbox': tensor(0.1356, device='cuda:0'), 'train_loss_giou': tensor(0.4505, device='cuda:0'), 'train_cardinality_error': tensor(1.0625, device='cuda:0'), 'validation_loss': tensor(2.3906, device='cuda:0'), 'validation_loss_ce': tensor(0.5131, device='cuda:0'), 'validation_loss_bbox': tensor(0.1641, device='cuda:0'), 'validation_loss_giou': tensor(0.5285, device='cuda:0'), 'validation_cardinality_error': tensor(1.1227, device='cuda:0')}
{'training_loss': tensor(2.5546, device='cuda:0'), 'train_loss_ce': tensor(0.5681, device='cuda:0'), 'train_loss_bbox': tensor(0.1646, device='cuda:0'), 'train_loss_giou': tensor(0.5818, device='cuda:0'), 'train_cardinality_error': tensor(1.2500, device='cuda:0'), 'validation_loss': tensor(2.4028, device='cuda:0'), 'validation_loss_ce': tensor(0.5090, device='cuda:0'), 'validation_loss_bbox': tensor(0.1696, device='cuda:0'), 'validation_loss_giou': tensor(0.5230, device='cuda:0'), 'validation_cardinality_error': tensor(1.1227, device='cuda:0')}
{'training_loss': tensor(2.4528, device='cuda:0'), 'train_loss_ce': tensor(0.4475, device='cuda:0'), 'train_loss_bbox': tensor(0.1614, device='cuda:0'), 'train_loss_giou': tensor(0.5991, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.3522, device='cuda:0'), 'validation_loss_ce': tensor(0.4847, device='cuda:0'), 'validation_loss_bbox': tensor(0.1584, device='cuda:0'), 'validation_loss_giou': tensor(0.5377, device='cuda:0'), 'validation_cardinality_error': tensor(1.1227, device='cuda:0')}
```

### Validation process
```
{'validation_loss': tensor(6.1819, device='cuda:0'), 'validation_loss_ce': tensor(2.1987, device='cuda:0'), 'validation_loss_bbox': tensor(0.4528, device='cuda:0'), 'validation_loss_giou': tensor(0.8597, device='cuda:0'), 'validation_cardinality_error': tensor(97.7500, device='cuda:0')}
{'training_loss': tensor(2.0822, device='cuda:0'), 'train_loss_ce': tensor(0.5032, device='cuda:0'), 'train_loss_bbox': tensor(0.1356, device='cuda:0'), 'train_loss_giou': tensor(0.4505, device='cuda:0'), 'train_cardinality_error': tensor(1.0625, device='cuda:0'), 'validation_loss': tensor(2.3906, device='cuda:0'), 'validation_loss_ce': tensor(0.5131, device='cuda:0'), 'validation_loss_bbox': tensor(0.1641, device='cuda:0'), 'validation_loss_giou': tensor(0.5285, device='cuda:0'), 'validation_cardinality_error': tensor(1.1227, device='cuda:0')}
{'training_loss': tensor(2.5546, device='cuda:0'), 'train_loss_ce': tensor(0.5681, device='cuda:0'), 'train_loss_bbox': tensor(0.1646, device='cuda:0'), 'train_loss_giou': tensor(0.5818, device='cuda:0'), 'train_cardinality_error': tensor(1.2500, device='cuda:0'), 'validation_loss': tensor(2.4028, device='cuda:0'), 'validation_loss_ce': tensor(0.5090, device='cuda:0'), 'validation_loss_bbox': tensor(0.1696, device='cuda:0'), 'validation_loss_giou': tensor(0.5230, device='cuda:0'), 'validation_cardinality_error': tensor(1.1227, device='cuda:0')}
{'training_loss': tensor(2.4528, device='cuda:0'), 'train_loss_ce': tensor(0.4475, device='cuda:0'), 'train_loss_bbox': tensor(0.1614, device='cuda:0'), 'train_loss_giou': tensor(0.5991, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.3522, device='cuda:0'), 'validation_loss_ce': tensor(0.4847, device='cuda:0'), 'validation_loss_bbox': tensor(0.1584, device='cuda:0'), 'validation_loss_giou': tensor(0.5377, device='cuda:0'), 'validation_cardinality_error': tensor(1.1227, device='cuda:0')}
```
