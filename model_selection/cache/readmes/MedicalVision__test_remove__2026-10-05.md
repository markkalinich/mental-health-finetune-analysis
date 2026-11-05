---
library_name: transformers
tags: []
---

## Original result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.005
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.005
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.005
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.203
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.068
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.005
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.029
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.029
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.029
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.200
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.067
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.029
```

## After training result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.009
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.020
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.008
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.009
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.043
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.076
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.087
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.089
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
{'validation_loss': tensor(8.5927, device='cuda:0'), 'validation_loss_ce': tensor(3.4775, device='cuda:0'), 'validation_loss_bbox': tensor(0.5756, device='cuda:0'), 'validation_loss_giou': tensor(1.1184, device='cuda:0'), 'validation_cardinality_error': tensor(99.5938, device='cuda:0')}
{'training_loss': tensor(1.3630, device='cuda:0'), 'train_loss_ce': tensor(0.2593, device='cuda:0'), 'train_loss_bbox': tensor(0.0803, device='cuda:0'), 'train_loss_giou': tensor(0.3511, device='cuda:0'), 'train_cardinality_error': tensor(0.5294, device='cuda:0'), 'validation_loss': tensor(1.5262, device='cuda:0'), 'validation_loss_ce': tensor(0.2351, device='cuda:0'), 'validation_loss_bbox': tensor(0.0827, device='cuda:0'), 'validation_loss_giou': tensor(0.4389, device='cuda:0'), 'validation_cardinality_error': tensor(0.4794, device='cuda:0')}
```

## Examples
{'size': tensor([560, 512]), 'image_id': tensor([1]), 'class_labels': tensor([], dtype=torch.int64), 'boxes': tensor([], size=(0, 4)), 'area': tensor([]), 'iscrowd': tensor([], dtype=torch.int64), 'orig_size': tensor([2580, 2332])}

![Example](./example.png)
