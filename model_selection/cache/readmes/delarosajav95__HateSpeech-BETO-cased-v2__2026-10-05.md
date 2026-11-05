---
datasets:
- manueltonneau/spanish-hate-speech-superset
- Paul/hatecheck
language:
- es
metrics:
- accuracy
- precision
- recall
- f1
base_model:
- dccuchile/bert-base-spanish-wwm-cased
pipeline_tag: text-classification
library_name: transformers
tags:
- BERT
- text-classification
- sentiment-analysis
- spanish
- fine-tuned
- nlp
- transformers
- content-moderation
- social-media-analysis
- beto
---
# HateSpeech-BETO-cased-v2

## 1. Model Overview:

- **Base Model**: [dccuchile/bert-base-spanish-wwm-cased](https://huggingface.co/dccuchile/bert-base-spanish-wwm-cased)

- **Task**: Hate speech detection in Spanish text.

- **Target**: Racism, homophobia, sexism, transphobia and other forms of discrimination.

## 2. Try it out:

You can interact with the model directly through the [Inference Endpoint](https://huggingface.co/spaces/delarosajav95/HateSpeech-BETO-cased-v2):

[![Open Inference Endpoint](https://img.shields.io/badge/Open_Inference_Endpoint-blue)](https://huggingface.co/spaces/delarosajav95/HateSpeech-BETO-cased-v2)


## 3. Key Enhancements in v2:

- **Previous Version (v1)**: Fine-tuned on the [**Paul/hatecheck-spanish**](https://huggingface.co/datasets/Paul/hatecheck-spanish) dataset, but real-world testing revealed performance issues, limiting its effectiveness.

- **Dataset Update**: To improve performance, this model was fine-tuned with a more extensive and diverse dataset, the [**manueltonneau/spanish-hate-speech-superset**](https://huggingface.co/datasets/manueltonneau/spanish-hate-speech-superset).

  - This larger dataset allowed the model to learn from a broader range of hate speech patterns.

- **Incorporation of Paul Samples**: After evaluating the results, it was clear that including key samples from the [**Paul dataset**](https://huggingface.co/datasets/Paul/hatecheck) would help the model capture additional nuanced forms of hate speech, such as **transphobia** and **multiple types of racism**.
  - A significant amount of effort went into carefully selecting and processing these samples from the Paul dataset and integrating them with the **manueltonneau** dataset. This careful curation created a more comprehensive dataset, **enhancing the model's ability to differentiate between hate and non-hate speech**.

## 4. Preprocessing and Postprocessing:

To prepare the datasets for fine-tuning and ensure optimal model performance, the following steps were undertaken:

**Filtering and Selection:**
  - Relevant samples from the Paul dataset were filtered based on performance goals.
  - Focused on hateful and non-hateful examples related to trans people and Muslims (['target_ident'] field).

**Text Normalization:**
  - All text samples were converted to lowercase.
  - This step enhanced the model's ability to understand semantic relationships by focusing on the underlying meaning of the text rather than superficial stylistic differences caused by capitalization.

**Translation:**
  - Paul dataset samples (in English) were translated into Spanish using the Hugging Face translation pipeline:
```python
pipeline("translation_en_to_es", model="Helsinki-NLP/opus-mt-en-es")
```
  - Total translated samples: **955**.

**Dataset Integration:**
  - Adjusted the Paul dataset format to align with the manueltonneau dataset schema:
    - Reformatted columns: text, labels, source, dataset, nb_annotators, tweet_id, post_author_country_location.
    - Cleaned and reorganized rows to ensure compatibility.
  - Concatenated the reformatted Paul samples with the manueltonneau dataset into a single .csv file.
  - Shuffled the combined dataset using seed=42 to ensure randomness.

**Dataset Splitting:**
  - Combined dataset size: **30,809 samples.**
  - Split into:
    - **Training set:** 18,485 samples (60%).
    - **Development set:** 12,324 samples (40%).
    - Shuffling used seed=123 for consistency.

**Label Mapping:**
  - Converted float labels (from the manueltonneau dataset) to integers for tensor compatibility:
```python
label_mapping = {0.0: 0, 1.0: 1}
```

**Dynamic Padding:**
  - Applied dynamic padding using the Hugging Face DataCollator to handle varying text lengths efficiently.
  - Batch settings: batch_size=8, shuffle=True.

## 5. Performance Improvements:

- **Greater Accuracy**: The inclusion of diverse samples led to a more balanced model that can better handle different forms of discrimination.
- **Precision in Detecting Non-Hate Speech**: The model is now more reliable at detecting non-hateful content, minimizing false positives.
- **Robustness**: The updated model performs better in real-world scenarios, offering stronger results for content moderation tasks.

## 6. Use Case:

- This model is optimized for content moderation on online platforms, where it can detect harmful speech and help foster safer online environments.
- **Classification Task**: The model categorizes text into two labels:

  - **Non-Hateful (LABEL_0)**: Content that does not contain hate speech and is neutral or constructive.
  - **Hateful (LABEL_1)**: Content that promotes hate speech or harmful rhetoric.

## 7. Goal:

The **goal** of the model is to identify content that promotes **harmful rhetoric** or **behavior**, while distinguishing it from **neutral** or **constructive speech**. This makes it highly applicable for **moderating online content**, ensuring that **harmful speech** and **behavior** are flagged while maintaining the integrity of **non-hateful communication**. By accurately identifying and differentiating between **harmful** and **non-harmful** content, this model supports the creation of a **safer** and more **inclusive digital environment**.

## 8. Future Work:

While the model demonstrates significant improvements over the previous version, **content moderation** is an ongoing challenge. Further refinements are always possible to improve its accuracy and effectiveness in diverse contexts and improved versions are expected in the near future.

## 9. Full classification example in Pyhton:

To assess the model’s performance, I selected 23 examples representing various types of hate speech and non-hate speech, covering categories such as homophobia, racism, sexism, and transphobia. These examples were carefully chosen from outside the datasets the model was trained or evaluated on, providing a comprehensive test of the model’s ability to generalize and handle real-world data.

<details>
<summary><strong>Click to expand Python code example</strong></summary>

```python
from transformers import pipeline

pipe = pipeline(model="delarosajav95/HateSpeech-BETO-cased-v2")

inputs = [
  # Homophobia
  "No soporto a los maricones, deberían quedarse en su casa y no andar provocando en público.",
  "No tengo nada contra los gays, pero no deberían adoptar niños, es antinatural.",
  "El camarero a cargo del bar era demasiado afeminado, se notaba que la manera de moverse no era la propia de un hombre.",

  # Pro-LGBTQ+ Rights
  "Cada ser humano, independientemente de su orientación sexual, merece respeto y dignidad.",
  "Admiro a las parejas homosexuales que luchan por sus derechos y forman familias llenas de amor.",

  # Racism
  "Los inmigrantes solo vienen a robar y quitarle el trabajo a los españoles.",
  "Seguro que robó, todos los gitanos son iguales.",

  # Intercultural and Intersectional Dynamics
  "Los inmigrantes enriquecen nuestra cultura con su diversidad y contribuyen al progreso de nuestra sociedad.",
  "La comunidad gitana tiene una gran herencia cultural y tradiciones únicas que debemos respetar y valorar.",

  # Sexism
  "Las mujeres no deberían trabajar, su lugar está en la cocina y cuidando a los hijos.",
  "Seguro consiguió el ascenso porque se acostó con el jefe.",

  # Gender Equality Advocacy
  "Las mujeres tienen el mismo derecho a trabajar y desarrollarse profesionalmente que los hombres.",
  "El ascenso de mi colega fue bien merecido, es una profesional dedicada y capaz.",

  # Transphobia
  "Los transexuales nunca serán hombres o mujeres de verdad, solo están confundidos.",
  "Las personas trans están locas, lo único que quieren es llamar la atención.",

  # Support for Trans Rights
  "Las personas transexuales merecen el mismo respeto y derechos que cualquier otra persona.",
  "Aprender nuevos pronombres es una forma sencilla de respetar la identidad de los demás.",

  # Intersectional hate
  "Las mujeres musulmanas son oprimidas porque todas están obligadas a llevar velo.",
  "Esas drag queens no deberían aparecer en la televisión, los niños pueden confundirse y volverse como ellos.",

   # Intersectional Support
  "Muchas mujeres musulmanas eligen llevar el velo como parte de su identidad y libertad religiosa.",
  "Las drag queens son artistas talentosos que inspiran a muchas personas con su creatividad.",
  
  # Neutral and non-hateful cases
  "La lluvia nos hizo salirnos de la carretera y chocarnos contra el árbol.",
  "Estaba muy cansada para ir andando hasta la feria, así que decidimos quedarnos en casa.",
  ]

result = pipe(inputs, return_all_scores=True)
label_mapping = {
    'LABEL_0': 'Non-Hate Speech',
    'LABEL_1': 'Hate Speech'
}
for i, predictions in enumerate(result):
  print("==================================")
  print(f"Text {i + 1}: {inputs[i]}")
  for pred in predictions:
    label = label_mapping.get(pred['label'], pred['label'])
    score = pred['score']
    print(f"{label}: {score:.2%}") 
```
</details>

**<u>Output</u>:**

<details>
<summary><strong>Click to expand Python code example</strong></summary>

```pyhton
==================================
Text 1: No soporto a los maricones, deberían quedarse en su casa y no andar provocando en público.
Non-Hate Speech: 0.02%
Hate Speech: 99.98%
==================================
Text 2: No tengo nada contra los gays, pero no deberían adoptar niños, es antinatural.
Non-Hate Speech: 0.03%
Hate Speech: 99.97%
==================================
Text 3: El camarero a cargo del bar era demasiado afeminado, se notaba que la manera de moverse no era la propia de un hombre.
Non-Hate Speech: 0.02%
Hate Speech: 99.98%
==================================
Text 4: Cada ser humano, independientemente de su orientación sexual, merece respeto y dignidad.
Non-Hate Speech: 99.99%
Hate Speech: 0.01%
==================================
Text 5: Admiro a las parejas homosexuales que luchan por sus derechos y forman familias llenas de amor.
Non-Hate Speech: 99.99%
Hate Speech: 0.01%
==================================
Text 6: Los inmigrantes solo vienen a robar y quitarle el trabajo a los españoles.
Non-Hate Speech: 0.01%
Hate Speech: 99.99%
==================================
Text 7: Seguro que robó, todos los gitanos son iguales.
Non-Hate Speech: 0.01%
Hate Speech: 99.99%
==================================
Text 8: Los inmigrantes enriquecen nuestra cultura con su diversidad y contribuyen al progreso de nuestra sociedad.
Non-Hate Speech: 99.79%
Hate Speech: 0.21%
==================================
Text 9: La comunidad gitana tiene una gran herencia cultural y tradiciones únicas que debemos respetar y valorar.
Non-Hate Speech: 99.96%
Hate Speech: 0.04%
==================================
Text 10: Las mujeres no deberían trabajar, su lugar está en la cocina y cuidando a los hijos.
Non-Hate Speech: 0.01%
Hate Speech: 99.99%
==================================
Text 11: Seguro consiguió el ascenso porque se acostó con el jefe.
Non-Hate Speech: 0.03%
Hate Speech: 99.97%
==================================
Text 12: Las mujeres tienen el mismo derecho a trabajar y desarrollarse profesionalmente que los hombres.
Non-Hate Speech: 99.95%
Hate Speech: 0.05%
==================================
Text 13: El ascenso de mi colega fue bien merecido, es una profesional dedicada y capaz.
Non-Hate Speech: 99.98%
Hate Speech: 0.02%
==================================
Text 14: Los transexuales nunca serán hombres o mujeres de verdad, solo están confundidos.
Non-Hate Speech: 0.01%
Hate Speech: 99.99%
==================================
Text 15: Las personas trans están locas, lo único que quieren es llamar la atención.
Non-Hate Speech: 0.01%
Hate Speech: 99.99%
==================================
Text 16: Las personas transexuales merecen el mismo respeto y derechos que cualquier otra persona.
Non-Hate Speech: 99.99%
Hate Speech: 0.01%
==================================
Text 17: Aprender nuevos pronombres es una forma sencilla de respetar la identidad de los demás.
Non-Hate Speech: 99.98%
Hate Speech: 0.02%
==================================
Text 18: Las mujeres musulmanas son oprimidas porque todas están obligadas a llevar velo.
Non-Hate Speech: 0.02%
Hate Speech: 99.98%
==================================
Text 19: Esas drag queens no deberían aparecer en la televisión, los niños pueden confundirse y volverse como ellos.
Non-Hate Speech: 0.01%
Hate Speech: 99.99%
==================================
Text 20: Muchas mujeres musulmanas eligen llevar el velo como parte de su identidad y libertad religiosa.
Non-Hate Speech: 99.38%
Hate Speech: 0.62%
==================================
Text 21: Las drag queens son artistas talentosos que inspiran a muchas personas con su creatividad.
Non-Hate Speech: 99.99%
Hate Speech: 0.01%
==================================
Text 22: La lluvia nos hizo salirnos de la carretera y chocarnos contra el árbol
Non-Hate Speech: 99.98%
Hate Speech: 0.02%
==================================
Text 23: Estaba muy cansada para ir andando hasta la feria, así que decidimos quedarnos en casa
Non-Hate Speech: 99.98%
Hate Speech: 0.02%
```
</details>

## 10. Metrics and results:

It achieves the following results on the *evaluation set* (last epoch):
- 'eval_loss': 0.3601696193218231
- 'eval_accuracy': 0.8465595585848751
- 'eval_precision_per_label': [0.8799580272822666, 0.7326413743736578]
- 'eval_recall_per_label': [0.918208693747947, 0.6414916953932936]
- 'eval_f1_per_label': [0.8986765257461287, 0.6840434419381788]
- 'eval_precision_weighted': 0.8418139637126973
- 'eval_recall_weighted': 0.8465595585848751
- 'eval_f1_weighted': 0.8431025099695003
- 'eval_runtime': 50.2267
- 'eval_samples_per_second': 245.367
- 'eval_steps_per_second': 30.681
- 'epoch': 6.0

## 11. Training Details and Procedure:

### Main Hyperparameters:

The following hyperparameters were used during training:
- evaluation_strategy: "epoch"
- learning_rate: 1e-5
- per_device_train_batch_size: 8
- per_device_eval_batch_size: 8
- num_train_epochs: 6
- optimizer: AdamW
- weight_decay: 0.01
- save_strategy: "epoch"
- lr_scheduler_type: "linear"
- warmup_steps: 820
- warmup_ratio: 0.1
- logging_steps: 10
- load_best_model_at_end: True
- metric_for_best_model: "eval_loss"
- greater_is_better: False

## 12. Framework versions:

- Transformers 4.47.1
- PyTorch version 2.5.1+cu121
- Datasets version 3.2.0
- Tokenizers version 0.21.0

## 13. CITATION:

- **manueltonneau/spanish-hate-speech-superset**:

```bibitex
@inproceedings{tonneau-etal-2024-languages,
    title = "From Languages to Geographies: Towards Evaluating Cultural Bias in Hate Speech Datasets",
    author = {Tonneau, Manuel  and
      Liu, Diyi  and
      Fraiberger, Samuel  and
      Schroeder, Ralph  and
      Hale, Scott  and
      R{\"o}ttger, Paul},
    editor = {Chung, Yi-Ling  and
      Talat, Zeerak  and
      Nozza, Debora  and
      Plaza-del-Arco, Flor Miriam  and
      R{\"o}ttger, Paul  and
      Mostafazadeh Davani, Aida  and
      Calabrese, Agostina},
    booktitle = "Proceedings of the 8th Workshop on Online Abuse and Harms (WOAH 2024)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.woah-1.23",
    pages = "283--311",
    abstract = "Perceptions of hate can vary greatly across cultural contexts. Hate speech (HS) datasets, however, have traditionally been developed by language. This hides potential cultural biases, as one language may be spoken in different countries home to different cultures. In this work, we evaluate cultural bias in HS datasets by leveraging two interrelated cultural proxies: language and geography. We conduct a systematic survey of HS datasets in eight languages and confirm past findings on their English-language bias, but also show that this bias has been steadily decreasing in the past few years. For three geographically-widespread languages{---}English, Arabic and Spanish{---}we then leverage geographical metadata from tweets to approximate geo-cultural contexts by pairing language and country information. We find that HS datasets for these languages exhibit a strong geo-cultural bias, largely overrepresenting a handful of countries (e.g., US and UK for English) relative to their prominence in both the broader social media population and the general population speaking these languages. Based on these findings, we formulate recommendations for the creation of future HS datasets.",
}
```
For additional information about the dataset, refer to the original [repository](https://aclanthology.org/2024.woah-1.23/)

- **Pre-trained model:**
**[Spanish Pre-Trained BERT Model and Evaluation Data](https://users.dcc.uchile.cl/~jperez/papers/pml4dc2020.pdf)**

```bibitex
@inproceedings{CaneteCFP2020,
  title={Spanish Pre-Trained BERT Model and Evaluation Data},
  author={Cañete, José and Chaperon, Gabriel and Fuentes, Rodrigo and Ho, Jou-Hui and Kang, Hojin and Pérez, Jorge},
  booktitle={PML4DC at ICLR 2020},
  year={2020}
}
```

- **Citation for this model:**
```bibitex
@misc{delarosa2025hatespeechbeto,
  author = {Javier de la Rosa Sánchez},
  title = {HateSpeech-BETO-cased-v2: A Fine-Tuned Model for Hate Speech Detection in Spanish},
  year = {2025},
  url = {https://huggingface.co/your-model-url},
  note = {Hugging Face Model Repository},
}
```
Please, if you use this model, do not forget to include my citation. Thank you!

## 14. Authorship and Contact Information:

This model was fine-tuned and optimized by **Javier de la Rosa Sánchez**, applying state-of-the-art techniques to enhance its performance for hate speech detection in Spanish. 

For inquiries or collaboration opportunities, please contact:  
- Email: [javier.delarosa95@gmail.com](mailto:javier.delarosa95@gmail.com)  
- LinkedIn: [linkedin.com/in/delarosajav95](https://www.linkedin.com/in/delarosajav95/)