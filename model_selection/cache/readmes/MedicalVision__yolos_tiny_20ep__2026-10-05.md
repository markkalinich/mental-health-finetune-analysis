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
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.002
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.013
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.013
```

## After training result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.025
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.053
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.021
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.025
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.070
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.133
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.154
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.155
```

## Config
- dataset: NIH
- original model: hustvl/yolos-tiny
- lr: 0.0001
- dropout_rate: 0.15
- weight_decay: 0.05
- max_epochs: 20
- train samples: 885

## Logging
### Training process
```
{'validation_loss': tensor(6.7559, device='cuda:0'), 'validation_loss_ce': tensor(2.5739, device='cuda:0'), 'validation_loss_bbox': tensor(0.4952, device='cuda:0'), 'validation_loss_giou': tensor(0.8531, device='cuda:0'), 'validation_cardinality_error': tensor(99., device='cuda:0')}
{'training_loss': tensor(2.4990, device='cuda:0'), 'train_loss_ce': tensor(0.4887, device='cuda:0'), 'train_loss_bbox': tensor(0.1862, device='cuda:0'), 'train_loss_giou': tensor(0.5398, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.4497, device='cuda:0'), 'validation_loss_ce': tensor(0.4524, device='cuda:0'), 'validation_loss_bbox': tensor(0.1829, device='cuda:0'), 'validation_loss_giou': tensor(0.5414, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.4763, device='cuda:0'), 'train_loss_ce': tensor(0.4236, device='cuda:0'), 'train_loss_bbox': tensor(0.1986, device='cuda:0'), 'train_loss_giou': tensor(0.5300, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2358, device='cuda:0'), 'validation_loss_ce': tensor(0.4386, device='cuda:0'), 'validation_loss_bbox': tensor(0.1531, device='cuda:0'), 'validation_loss_giou': tensor(0.5160, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.0404, device='cuda:0'), 'train_loss_ce': tensor(0.4148, device='cuda:0'), 'train_loss_bbox': tensor(0.1398, device='cuda:0'), 'train_loss_giou': tensor(0.4634, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.3295, device='cuda:0'), 'validation_loss_ce': tensor(0.4369, device='cuda:0'), 'validation_loss_bbox': tensor(0.1697, device='cuda:0'), 'validation_loss_giou': tensor(0.5220, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.0230, device='cuda:0'), 'train_loss_ce': tensor(0.3600, device='cuda:0'), 'train_loss_bbox': tensor(0.1205, device='cuda:0'), 'train_loss_giou': tensor(0.5302, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2546, device='cuda:0'), 'validation_loss_ce': tensor(0.4068, device='cuda:0'), 'validation_loss_bbox': tensor(0.1611, device='cuda:0'), 'validation_loss_giou': tensor(0.5210, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.1597, device='cuda:0'), 'train_loss_ce': tensor(0.4342, device='cuda:0'), 'train_loss_bbox': tensor(0.1431, device='cuda:0'), 'train_loss_giou': tensor(0.5049, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.0929, device='cuda:0'), 'validation_loss_ce': tensor(0.4126, device='cuda:0'), 'validation_loss_bbox': tensor(0.1394, device='cuda:0'), 'validation_loss_giou': tensor(0.4916, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.0645, device='cuda:0'), 'train_loss_ce': tensor(0.4740, device='cuda:0'), 'train_loss_bbox': tensor(0.1324, device='cuda:0'), 'train_loss_giou': tensor(0.4642, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2642, device='cuda:0'), 'validation_loss_ce': tensor(0.4195, device='cuda:0'), 'validation_loss_bbox': tensor(0.1665, device='cuda:0'), 'validation_loss_giou': tensor(0.5060, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.7443, device='cuda:0'), 'train_loss_ce': tensor(0.3507, device='cuda:0'), 'train_loss_bbox': tensor(0.1351, device='cuda:0'), 'train_loss_giou': tensor(0.3591, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(1.9930, device='cuda:0'), 'validation_loss_ce': tensor(0.4063, device='cuda:0'), 'validation_loss_bbox': tensor(0.1294, device='cuda:0'), 'validation_loss_giou': tensor(0.4698, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.2440, device='cuda:0'), 'train_loss_ce': tensor(0.3884, device='cuda:0'), 'train_loss_bbox': tensor(0.1348, device='cuda:0'), 'train_loss_giou': tensor(0.5907, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.0082, device='cuda:0'), 'validation_loss_ce': tensor(0.4112, device='cuda:0'), 'validation_loss_bbox': tensor(0.1296, device='cuda:0'), 'validation_loss_giou': tensor(0.4744, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.7194, device='cuda:0'), 'train_loss_ce': tensor(0.3257, device='cuda:0'), 'train_loss_bbox': tensor(0.1185, device='cuda:0'), 'train_loss_giou': tensor(0.4007, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.0462, device='cuda:0'), 'validation_loss_ce': tensor(0.4009, device='cuda:0'), 'validation_loss_bbox': tensor(0.1423, device='cuda:0'), 'validation_loss_giou': tensor(0.4670, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.3192, device='cuda:0'), 'train_loss_ce': tensor(0.3495, device='cuda:0'), 'train_loss_bbox': tensor(0.1083, device='cuda:0'), 'train_loss_giou': tensor(0.2141, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.0731, device='cuda:0'), 'validation_loss_ce': tensor(0.4010, device='cuda:0'), 'validation_loss_bbox': tensor(0.1389, device='cuda:0'), 'validation_loss_giou': tensor(0.4888, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.5797, device='cuda:0'), 'train_loss_ce': tensor(0.4210, device='cuda:0'), 'train_loss_bbox': tensor(0.1568, device='cuda:0'), 'train_loss_giou': tensor(0.6874, device='cuda:0'), 'train_cardinality_error': tensor(1.4000, device='cuda:0'), 'validation_loss': tensor(2.1459, device='cuda:0'), 'validation_loss_ce': tensor(0.4006, device='cuda:0'), 'validation_loss_bbox': tensor(0.1465, device='cuda:0'), 'validation_loss_giou': tensor(0.5065, device='cuda:0'), 'validation_cardinality_error': tensor(0.9394, device='cuda:0')}
{'training_loss': tensor(1.9156, device='cuda:0'), 'train_loss_ce': tensor(0.3240, device='cuda:0'), 'train_loss_bbox': tensor(0.1310, device='cuda:0'), 'train_loss_giou': tensor(0.4683, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2520, device='cuda:0'), 'validation_loss_ce': tensor(0.3980, device='cuda:0'), 'validation_loss_bbox': tensor(0.1614, device='cuda:0'), 'validation_loss_giou': tensor(0.5236, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.9559, device='cuda:0'), 'train_loss_ce': tensor(0.4028, device='cuda:0'), 'train_loss_bbox': tensor(0.2567, device='cuda:0'), 'train_loss_giou': tensor(0.6347, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.4024, device='cuda:0'), 'validation_loss_ce': tensor(0.3812, device='cuda:0'), 'validation_loss_bbox': tensor(0.1705, device='cuda:0'), 'validation_loss_giou': tensor(0.5843, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.1148, device='cuda:0'), 'train_loss_ce': tensor(0.4487, device='cuda:0'), 'train_loss_bbox': tensor(0.1306, device='cuda:0'), 'train_loss_giou': tensor(0.5065, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2119, device='cuda:0'), 'validation_loss_ce': tensor(0.3946, device='cuda:0'), 'validation_loss_bbox': tensor(0.1521, device='cuda:0'), 'validation_loss_giou': tensor(0.5285, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.6145, device='cuda:0'), 'train_loss_ce': tensor(0.3484, device='cuda:0'), 'train_loss_bbox': tensor(0.0966, device='cuda:0'), 'train_loss_giou': tensor(0.3917, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2147, device='cuda:0'), 'validation_loss_ce': tensor(0.4000, device='cuda:0'), 'validation_loss_bbox': tensor(0.1524, device='cuda:0'), 'validation_loss_giou': tensor(0.5264, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.4464, device='cuda:0'), 'train_loss_ce': tensor(0.3513, device='cuda:0'), 'train_loss_bbox': tensor(0.1503, device='cuda:0'), 'train_loss_giou': tensor(0.6718, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.0945, device='cuda:0'), 'validation_loss_ce': tensor(0.3839, device='cuda:0'), 'validation_loss_bbox': tensor(0.1390, device='cuda:0'), 'validation_loss_giou': tensor(0.5079, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.1035, device='cuda:0'), 'train_loss_ce': tensor(0.3531, device='cuda:0'), 'train_loss_bbox': tensor(0.1833, device='cuda:0'), 'train_loss_giou': tensor(0.4169, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.0258, device='cuda:0'), 'validation_loss_ce': tensor(0.3667, device='cuda:0'), 'validation_loss_bbox': tensor(0.1385, device='cuda:0'), 'validation_loss_giou': tensor(0.4833, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.8120, device='cuda:0'), 'train_loss_ce': tensor(0.3834, device='cuda:0'), 'train_loss_bbox': tensor(0.1274, device='cuda:0'), 'train_loss_giou': tensor(0.3959, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.0069, device='cuda:0'), 'validation_loss_ce': tensor(0.3738, device='cuda:0'), 'validation_loss_bbox': tensor(0.1400, device='cuda:0'), 'validation_loss_giou': tensor(0.4665, device='cuda:0'), 'validation_cardinality_error': tensor(0.9697, device='cuda:0')}
{'training_loss': tensor(1.2792, device='cuda:0'), 'train_loss_ce': tensor(0.3943, device='cuda:0'), 'train_loss_bbox': tensor(0.0620, device='cuda:0'), 'train_loss_giou': tensor(0.2874, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(1.9124, device='cuda:0'), 'validation_loss_ce': tensor(0.3761, device='cuda:0'), 'validation_loss_bbox': tensor(0.1317, device='cuda:0'), 'validation_loss_giou': tensor(0.4388, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.8847, device='cuda:0'), 'train_loss_ce': tensor(0.3796, device='cuda:0'), 'train_loss_bbox': tensor(0.1281, device='cuda:0'), 'train_loss_giou': tensor(0.4323, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.0097, device='cuda:0'), 'validation_loss_ce': tensor(0.3599, device='cuda:0'), 'validation_loss_bbox': tensor(0.1377, device='cuda:0'), 'validation_loss_giou': tensor(0.4806, device='cuda:0'), 'validation_cardinality_error': tensor(0.6263, device='cuda:0')}
```

## Examples
{'size': tensor([512, 512]), 'image_id': tensor([1]), 'class_labels': tensor([4]), 'boxes': tensor([[0.2622, 0.5729, 0.0847, 0.0773]]), 'area': tensor([1717.9431]), 'iscrowd': tensor([0]), 'orig_size': tensor([1024, 1024])}

![Example](./example.png)
