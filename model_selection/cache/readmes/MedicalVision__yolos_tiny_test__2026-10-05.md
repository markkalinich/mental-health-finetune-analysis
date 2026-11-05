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
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.000
```

## After training result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.002
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.001
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.001
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.015
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.026
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.028
```

## Config
- dataset: NIH
- original model: hustvl/yolos-tiny
- lr: 0.0001
- dropout_rate: 0.1
- weight_decay: 0.001
- max_epochs: 1
- train samples: 885

## Logging
### Training process
```
{'validation_loss': tensor(7.2682, device='cuda:0'), 'validation_loss_ce': tensor(2.4654, device='cuda:0'), 'validation_loss_bbox': tensor(0.5599, device='cuda:0'), 'validation_loss_giou': tensor(1.0016, device='cuda:0'), 'validation_cardinality_error': tensor(99., device='cuda:0')}
{'training_loss': tensor(3.1491, device='cuda:0'), 'train_loss_ce': tensor(0.3927, device='cuda:0'), 'train_loss_bbox': tensor(0.2719, device='cuda:0'), 'train_loss_giou': tensor(0.6985, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2454, device='cuda:0'), 'validation_loss_ce': tensor(0.4346, device='cuda:0'), 'validation_loss_bbox': tensor(0.1519, device='cuda:0'), 'validation_loss_giou': tensor(0.5256, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
```

## Examples
{'size': tensor([512, 512]), 'image_id': tensor([1]), 'class_labels': tensor([4]), 'boxes': tensor([[0.2622, 0.5729, 0.0847, 0.0773]]), 'area': tensor([1717.9431]), 'iscrowd': tensor([0]), 'orig_size': tensor([1024, 1024])}

![Example](./example.png)
