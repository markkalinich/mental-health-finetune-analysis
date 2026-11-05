---
license: apache-2.0
language: "es"

tags:
- generated_from_trainer
- sentiment
- emotion
- suicide
- depresión
- suicidio
- español
- es
- spanish
- depression
widget:
- text: "La vida no merece la pena"
  example_title: "Ejemplo 1"
- text: "Para vivir así lo mejor es estar muerto"
  example_title: "Ejemplo 2"
- text: "me siento triste por no poder viajar"
  example_title: "Ejemplo 3"
- text: "Quiero terminar con todo"  
  example_title: "Ejemplo 4"
- text: "Disfruto de la vista"
  example_title: "Ejemplo 5"    
  
metrics:
- accuracy
model-index:
- name: electricidad-small-discriminator-finetuned-clasificacion-comentarios-suicidas 
  results: []
---

# electricidad-small-discriminator-finetuned-clasificacion-comentarios-suicidas 

El presente modelo se encentra basado en una versión mejorada de [mrm8488/electricidad-small-discriminator](https://huggingface.co/mrm8488/electricidad-small-discriminator), y con el uso de la base de datos [hackathon-pln-es/comentarios_depresivos](https://huggingface.co/datasets/hackathon-pln-es/comentarios_depresivos).
Siendo de esta manera los resultados obtenidos en la evaluación del modelo:
- Pérdida 0.0458
- Precisión: 0.9916 

## Autores

- Danny Vásquez
- César Salazar
- Alexis Cañar
- Yannela Castro
- Daniel Patiño

## Descripción del Modelo

electricidad-small-discriminator-finetuned-clasificacion-comentarios-suicidas es un modelo Transformers pre-entrenado bajo un largo corpus de comentarios obtenidos de REDDIT traducidos al español, con el fin de poder predecir si un comentario tiene una tendencia suicida en base al contexto. Por ende, recibirá una ENTRADA en la cuál se ingresará el texto a comprobar, para posteriormente obtener como única SALIDA de igual manera dos posibles opciones: “Suicida” o “No Suicida”. 

## Motivación

Siendo la principal inspiración del modelo que sea utilizado para futuros proyectos que busquen detectar los casos de depresión a tiempo mediante el procesamiento del lenguaje natural, para poder prevenir los casos de suicido en niños, jóvenes y adultos.

## ¿Cómo usarlo?

El modelo puede ser utilizado de manera directa mediante la importación de la librería pipeline de transformers:

```python
>>> from transformers import pipeline
>>> model_name= 'hackathon-pln-es/electricidad-small-discriminator-finetuned-clasificacion-comentarios-suicidas'
>>> cls= pipeline("text-classification", model=model_name)
>>> cls(“Estoy feliz”)[0]['label']
[{'resultado': "No Suicida"
}]
>>> cls(“Quiero acabar con todo”)[0]['label']
[{'resultado': " Suicida"
}]
```
## Proceso de entrenamiento

### Datos de entrenamiento
Como se declaró anteriormente, el modelo se pre-entrenó basándose en la base de datos [comentarios_depresivos]( https://huggingface.co/datasets/hackathon-pln-es/comentarios_depresivos), el cuál posee una cantidad de 192 347 filas de datos para el entrenamiento, 33 944 para las pruebas y 22630 para la validación.

### Hiper parámetros de entrenamiento
- learning_rate: 2e-05
- train_batch_size: 32
- eval_batch_size: 32
- lr_scheduler_type: linear
- num_epochs: 15

### Resultados del entrenamiento
| Pérdida_entrenamiento | Epoch | Pérdida_Validación | Presición |
|:-------------:|:-----:|:---------------:|:--------:|
| 0.161100       | 1.0   | 0.133057         | 0.952718 |
| 0.134500        | 2.0   | 0.110966       | 0.960804 |
| 0.108500        | 3.0   | 0.086417      | 0.970835 |
| 0.099400        | 4.0   | 0.073618      | 0.974856 |
| 0.090500       | 5.0   | 0.065231       | 0.979629 |
| 0.080700       | 6.0   | 0.060849    | 0.982324   |
| 0.069200        | 7.0   | 0.054718       | 0.986125 |
| 0.060400        | 8.0   | 0.051153        | 0.985948 |
| 0.048200        | 9.0   | 0.045747       | 0.989748 |
| 0.045500        | 10.0   | 0.049992        | 0.988069 |
| 0.043400        | 11.0   | 0.046325         | 0.990234 |
| 0.034300        | 12.0   | 0.050746         | 0.989792 |
| 0.032900        | 13.0   | 0.043434       | 0.991737 |
| 0.028400        | 14.0   | 0.045003        | 0.991869 |
| 0.022300        | 15.0   | 0.045819        | 0.991648 |

### Versiones del Framework
- Transformers 4.17.0
- Pytorch 1.10.0+cu111
- Datasets 2.0.0
- Tokenizers 0.11.6

## Citación BibTeX

```bibtex
@article{ccs_2022,
  author    = {Danny Vásquez and
               César Salazar and
               Alexis Cañar and
               Yannela Castro and
Daniel Patiño},
  title     = {Modelo Electricidad-small-discriminator-finetuned-clasificacion-comentarios-suicidas},
  journal   = {Huggingface},
  year      = {2022},
}
```

<h3>Visualizar en GRADIO:</h3>
<a href="https://huggingface.co/spaces/hackathon-pln-es/clasificador-comentarios-suicidas">	
<img width="300px" src="https://hf.space/embed/hackathon-pln-es/clasificador-comentarios-suicidas/static/img/logo.svg">
</a>

---

