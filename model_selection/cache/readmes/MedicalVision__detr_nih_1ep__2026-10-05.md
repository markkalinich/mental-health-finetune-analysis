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
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.003
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.008
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.008
```

## After training result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.006
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.015
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.017
```

## Config
- dataset: NIH
- original model: facebook/detr-resnet-50
- lr: 0.0001
- max_epochs: 1

## Logging

### Training process

```
{'training_loss': tensor(2.9624, device='cuda:0'), 'train_loss_ce': tensor(0.4469, device='cuda:0'), 'train_loss_bbox': tensor(0.2411, device='cuda:0'), 'train_loss_giou': tensor(0.6551, device='cuda:0'), 'train_cardinality_error': tensor(1.1250, device='cuda:0'), 'validation_loss': tensor(2.4818, device='cuda:0'), 'validation_loss_ce': tensor(0.5116, device='cuda:0'), 'validation_loss_bbox': tensor(0.1740, device='cuda:0'), 'validation_loss_giou': tensor(0.5502, device='cuda:0'), 'validation_cardinality_error': tensor(1.0955, device='cuda:0')}
```

### Validation process

```
{'validation_loss': tensor(5.8176, device='cuda:0'), 'validation_loss_ce': tensor(2.3980, device='cuda:0'), 'validation_loss_bbox': tensor(0.4030, device='cuda:0'), 'validation_loss_giou': tensor(0.7024, device='cuda:0'), 'validation_cardinality_error': tensor(98.5312, device='cuda:0')}
{'training_loss': tensor(2.9624, device='cuda:0'), 'train_loss_ce': tensor(0.4469, device='cuda:0'), 'train_loss_bbox': tensor(0.2411, device='cuda:0'), 'train_loss_giou': tensor(0.6551, device='cuda:0'), 'train_cardinality_error': tensor(1.1250, device='cuda:0'), 'validation_loss': tensor(2.4818, device='cuda:0'), 'validation_loss_ce': tensor(0.5116, device='cuda:0'), 'validation_loss_bbox': tensor(0.1740, device='cuda:0'), 'validation_loss_giou': tensor(0.5502, device='cuda:0'), 'validation_cardinality_error': tensor(1.0955, device='cuda:0')}
```
