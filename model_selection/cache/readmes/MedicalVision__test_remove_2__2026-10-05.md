---
library_name: transformers
tags: []
---

## Original result
```
Not provided
```

## After training result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.006
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.016
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.004
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.006
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.041
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.077
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.083
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.085
```

## Config
- dataset: VinXray
- original model: hustvl/yolos-tiny
- lr: 0.0001
- dropout_rate: 0.1
- weight_decay: 0.0001
- max_epochs: 1
- train samples: 67234

## Logging
### Training process
```
{'validation_loss': tensor(7.8284, device='cuda:1'), 'validation_loss_ce': tensor(2.7671, device='cuda:1'), 'validation_loss_bbox': tensor(0.5730, device='cuda:1'), 'validation_loss_giou': tensor(1.0983, device='cuda:1'), 'validation_cardinality_error': tensor(98.8125, device='cuda:1')}
{'training_loss': tensor(1.3821, device='cuda:1'), 'train_loss_ce': tensor(0.1972, device='cuda:1'), 'train_loss_bbox': tensor(0.0681, device='cuda:1'), 'train_loss_giou': tensor(0.4223, device='cuda:1'), 'train_cardinality_error': tensor(0.4118, device='cuda:1'), 'validation_loss': tensor(1.6166, device='cuda:1'), 'validation_loss_ce': tensor(0.2388, device='cuda:1'), 'validation_loss_bbox': tensor(0.0936, device='cuda:1'), 'validation_loss_giou': tensor(0.4548, device='cuda:1'), 'validation_cardinality_error': tensor(0.5118, device='cuda:1')}
```

## Examples
{'size': tensor([560, 512]), 'image_id': tensor([1]), 'class_labels': tensor([], dtype=torch.int64), 'boxes': tensor([], size=(0, 4)), 'area': tensor([]), 'iscrowd': tensor([], dtype=torch.int64), 'orig_size': tensor([2580, 2332])}

![Example](./example.png)
