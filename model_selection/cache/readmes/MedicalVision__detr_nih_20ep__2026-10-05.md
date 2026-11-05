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
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.006
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.025
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.025
```

## After training result
```
IoU metric: bbox
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.005
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.015
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.003
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.005
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.037
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.105
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.110
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.111
```

## Config
- dataset: NIH
- original model: facebook/detr-resnet-50
- lr: 0.0001
- max_epochs: 20

## Logging
### Training process
```
{'validation_loss': tensor(6.3146, device='cuda:0'), 'validation_loss_ce': tensor(2.1177, device='cuda:0'), 'validation_loss_bbox': tensor(0.4698, device='cuda:0'), 'validation_loss_giou': tensor(0.9240, device='cuda:0'), 'validation_cardinality_error': tensor(92.7500, device='cuda:0')}
{'training_loss': tensor(2.3670, device='cuda:0'), 'train_loss_ce': tensor(0.4749, device='cuda:0'), 'train_loss_bbox': tensor(0.1771, device='cuda:0'), 'train_loss_giou': tensor(0.5034, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.5731, device='cuda:0'), 'validation_loss_ce': tensor(0.4578, device='cuda:0'), 'validation_loss_bbox': tensor(0.1954, device='cuda:0'), 'validation_loss_giou': tensor(0.5691, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.8187, device='cuda:0'), 'train_loss_ce': tensor(0.4641, device='cuda:0'), 'train_loss_bbox': tensor(0.1463, device='cuda:0'), 'train_loss_giou': tensor(0.3115, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.3214, device='cuda:0'), 'validation_loss_ce': tensor(0.4453, device='cuda:0'), 'validation_loss_bbox': tensor(0.1656, device='cuda:0'), 'validation_loss_giou': tensor(0.5240, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.0658, device='cuda:0'), 'train_loss_ce': tensor(0.4764, device='cuda:0'), 'train_loss_bbox': tensor(0.1381, device='cuda:0'), 'train_loss_giou': tensor(0.4494, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.5311, device='cuda:0'), 'validation_loss_ce': tensor(0.4494, device='cuda:0'), 'validation_loss_bbox': tensor(0.1959, device='cuda:0'), 'validation_loss_giou': tensor(0.5512, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.2448, device='cuda:0'), 'train_loss_ce': tensor(0.4614, device='cuda:0'), 'train_loss_bbox': tensor(0.1400, device='cuda:0'), 'train_loss_giou': tensor(0.5416, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.4153, device='cuda:0'), 'validation_loss_ce': tensor(0.4393, device='cuda:0'), 'validation_loss_bbox': tensor(0.1699, device='cuda:0'), 'validation_loss_giou': tensor(0.5632, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.1852, device='cuda:0'), 'train_loss_ce': tensor(0.3962, device='cuda:0'), 'train_loss_bbox': tensor(0.1427, device='cuda:0'), 'train_loss_giou': tensor(0.5378, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.5502, device='cuda:0'), 'validation_loss_ce': tensor(0.4350, device='cuda:0'), 'validation_loss_bbox': tensor(0.1922, device='cuda:0'), 'validation_loss_giou': tensor(0.5771, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.3992, device='cuda:0'), 'train_loss_ce': tensor(0.4620, device='cuda:0'), 'train_loss_bbox': tensor(0.1689, device='cuda:0'), 'train_loss_giou': tensor(0.5463, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.3235, device='cuda:0'), 'validation_loss_ce': tensor(0.4311, device='cuda:0'), 'validation_loss_bbox': tensor(0.1645, device='cuda:0'), 'validation_loss_giou': tensor(0.5349, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(3.3016, device='cuda:0'), 'train_loss_ce': tensor(0.4607, device='cuda:0'), 'train_loss_bbox': tensor(0.2840, device='cuda:0'), 'train_loss_giou': tensor(0.7105, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(3.1183, device='cuda:0'), 'validation_loss_ce': tensor(0.4855, device='cuda:0'), 'validation_loss_bbox': tensor(0.2575, device='cuda:0'), 'validation_loss_giou': tensor(0.6727, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.2759, device='cuda:0'), 'train_loss_ce': tensor(0.4727, device='cuda:0'), 'train_loss_bbox': tensor(0.1564, device='cuda:0'), 'train_loss_giou': tensor(0.5106, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.4930, device='cuda:0'), 'validation_loss_ce': tensor(0.4559, device='cuda:0'), 'validation_loss_bbox': tensor(0.1806, device='cuda:0'), 'validation_loss_giou': tensor(0.5671, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.1693, device='cuda:0'), 'train_loss_ce': tensor(0.4572, device='cuda:0'), 'train_loss_bbox': tensor(0.1668, device='cuda:0'), 'train_loss_giou': tensor(0.4391, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.4470, device='cuda:0'), 'validation_loss_ce': tensor(0.4276, device='cuda:0'), 'validation_loss_bbox': tensor(0.1828, device='cuda:0'), 'validation_loss_giou': tensor(0.5526, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.1987, device='cuda:0'), 'train_loss_ce': tensor(0.4733, device='cuda:0'), 'train_loss_bbox': tensor(0.1611, device='cuda:0'), 'train_loss_giou': tensor(0.4599, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.3597, device='cuda:0'), 'validation_loss_ce': tensor(0.4294, device='cuda:0'), 'validation_loss_bbox': tensor(0.1693, device='cuda:0'), 'validation_loss_giou': tensor(0.5418, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.5232, device='cuda:0'), 'train_loss_ce': tensor(0.4011, device='cuda:0'), 'train_loss_bbox': tensor(0.1782, device='cuda:0'), 'train_loss_giou': tensor(0.6154, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2632, device='cuda:0'), 'validation_loss_ce': tensor(0.4187, device='cuda:0'), 'validation_loss_bbox': tensor(0.1576, device='cuda:0'), 'validation_loss_giou': tensor(0.5281, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.6633, device='cuda:0'), 'train_loss_ce': tensor(0.4540, device='cuda:0'), 'train_loss_bbox': tensor(0.1967, device='cuda:0'), 'train_loss_giou': tensor(0.6129, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.3457, device='cuda:0'), 'validation_loss_ce': tensor(0.4227, device='cuda:0'), 'validation_loss_bbox': tensor(0.1699, device='cuda:0'), 'validation_loss_giou': tensor(0.5369, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.4428, device='cuda:0'), 'train_loss_ce': tensor(0.4721, device='cuda:0'), 'train_loss_bbox': tensor(0.1833, device='cuda:0'), 'train_loss_giou': tensor(0.5272, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.5712, device='cuda:0'), 'validation_loss_ce': tensor(0.4430, device='cuda:0'), 'validation_loss_bbox': tensor(0.1854, device='cuda:0'), 'validation_loss_giou': tensor(0.6006, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.2497, device='cuda:0'), 'train_loss_ce': tensor(0.4085, device='cuda:0'), 'train_loss_bbox': tensor(0.1480, device='cuda:0'), 'train_loss_giou': tensor(0.5506, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2828, device='cuda:0'), 'validation_loss_ce': tensor(0.4168, device='cuda:0'), 'validation_loss_bbox': tensor(0.1639, device='cuda:0'), 'validation_loss_giou': tensor(0.5232, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.3250, device='cuda:0'), 'train_loss_ce': tensor(0.4841, device='cuda:0'), 'train_loss_bbox': tensor(0.1521, device='cuda:0'), 'train_loss_giou': tensor(0.5402, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2129, device='cuda:0'), 'validation_loss_ce': tensor(0.4072, device='cuda:0'), 'validation_loss_bbox': tensor(0.1600, device='cuda:0'), 'validation_loss_giou': tensor(0.5028, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(2.6468, device='cuda:0'), 'train_loss_ce': tensor(0.4126, device='cuda:0'), 'train_loss_bbox': tensor(0.1863, device='cuda:0'), 'train_loss_giou': tensor(0.6512, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.1853, device='cuda:0'), 'validation_loss_ce': tensor(0.4065, device='cuda:0'), 'validation_loss_bbox': tensor(0.1541, device='cuda:0'), 'validation_loss_giou': tensor(0.5041, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(3.1960, device='cuda:0'), 'train_loss_ce': tensor(0.3919, device='cuda:0'), 'train_loss_bbox': tensor(0.2759, device='cuda:0'), 'train_loss_giou': tensor(0.7123, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(4.5836, device='cuda:0'), 'validation_loss_ce': tensor(0.4463, device='cuda:0'), 'validation_loss_bbox': tensor(0.4188, device='cuda:0'), 'validation_loss_giou': tensor(1.0216, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.6624, device='cuda:0'), 'train_loss_ce': tensor(0.4196, device='cuda:0'), 'train_loss_bbox': tensor(0.1069, device='cuda:0'), 'train_loss_giou': tensor(0.3542, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.3143, device='cuda:0'), 'validation_loss_ce': tensor(0.4098, device='cuda:0'), 'validation_loss_bbox': tensor(0.1679, device='cuda:0'), 'validation_loss_giou': tensor(0.5325, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.6003, device='cuda:0'), 'train_loss_ce': tensor(0.3036, device='cuda:0'), 'train_loss_bbox': tensor(0.1298, device='cuda:0'), 'train_loss_giou': tensor(0.3238, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.1774, device='cuda:0'), 'validation_loss_ce': tensor(0.4031, device='cuda:0'), 'validation_loss_bbox': tensor(0.1508, device='cuda:0'), 'validation_loss_giou': tensor(0.5101, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
{'training_loss': tensor(1.9200, device='cuda:0'), 'train_loss_ce': tensor(0.4339, device='cuda:0'), 'train_loss_bbox': tensor(0.1293, device='cuda:0'), 'train_loss_giou': tensor(0.4198, device='cuda:0'), 'train_cardinality_error': tensor(1., device='cuda:0'), 'validation_loss': tensor(2.2109, device='cuda:0'), 'validation_loss_ce': tensor(0.4018, device='cuda:0'), 'validation_loss_bbox': tensor(0.1551, device='cuda:0'), 'validation_loss_giou': tensor(0.5167, device='cuda:0'), 'validation_cardinality_error': tensor(1., device='cuda:0')}
```
