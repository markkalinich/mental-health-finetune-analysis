---
license: apache-2.0
library_name: transformers
pipeline_tag: token-classification
language:
- es
base_model:
- BSC-LT/MrBERT-es
tags:
- biomedical
- spanish
- dental
- dentistry
- ner
- token-classification
- snomed-ct
- multiclass
- medical-entities
---

# ALIA MrBERT-es Snomed Dental Multiclass NER Model (Context 8192)

This repository contains **ALIA-MrBERT-es-snomed-dental-ner-multiclass-ctx8192**, a Spanish dentistry domain multiclass Named Entity Recognition (NER) model. It is built upon [MrBERT-es](https://huggingface.co/BSC-LT/MrBERT-es), a bilingual (Spanish-English) foundational language model based on the ModernBERT architecture, and fine-tuned on dentistry-specific clinical data.

Unlike binary or single-class entity extraction models, this model is a **direct multiclass token classifier**. It detects dental clinical entities and assigns them directly to their corresponding **SNOMED CT codes** in a single inference step, utilizing a BIO (Beginning, Inside, Outside) tagging schema tailored for each concept.

> [!WARNING]
> **DISCLAIMER:** This model is a domain-specific proof-of-concept designed to demonstrate multiclass entity recognition and direct coding in the Spanish dentistry domain.
> Clinical decisions should always be verified by qualified dental professionals and clinical experts. The model should not be used as a standalone diagnostic tool.

---

## Model Details

### Model Lineage

```
ModernBERT (architecture)
       ↓
  MrBERT-es (BSC-LT)
  Bilingual ES/EN encoder
  150M parameters
       ↓
  ALIA-MrBERT-es-snomed-dental-ner-multiclass-ctx8192 (UJA)
  Dentistry Multiclass Named Entity Recognition fine-tuning
  ~400 SNOMED CT clinical codes (Direct Coding)
```

### Key Features

- 🦷 **Domain**: Spanish dental and dentistry clinical reports.
- 📐 **Architecture**: ModernBERT adapted for Multiclass Token Classification (NER).
- 📏 **Long context**: Up to 8,192 tokens, enabling complete clinical histories or multi-turn dental dialogues to be processed in a single pass.
- 🏷️ **Direct SNOMED CT Coding**: Classifies tokens directly into specific SNOMED CT concepts, bypassing the need for a separate downstream entity linking step.
- ⚙️ **BIO Schema**: Assigns `B-{SNOMED_CODE}` and `I-{SNOMED_CODE}` tags to extract exact entity boundaries and classifications simultaneously.

### Architecture

This model utilizes the ModernBERT architecture, extended with a multiclass token classification head:

|                              |               |
|------------------------------|:--------------|
| **Base Architecture**        | ModernBERT    |
| **Total Parameters**         | ~150M         |
| **Hidden size**              | 768           |
| **Intermediate size**        | 1,152         |
| **Attention heads**          | 12            |
| **Hidden layers**            | 22            |
| **Context length**           | 8,192 tokens  |
| **Vocabulary size**          | 51,200        |
| **Precision**                | bfloat16      |
| **Positional encoding**      | RoPE          |
| **Activation function**      | GeLU          |
| **Attention type**           | Mixed (global every 3 layers + sliding window) |
| **Classification Head**      | Multiclass Token Classification (Linear + Softmax) |
| **Label Space**              | ~815 labels (BIO tags for ~400 concepts + O) |

---

## Training

### Training Script & Strategy

The model was fine-tuned using the training pipeline defined in `train_multiclass.py`. The strategy maps spans in the dental corpus to BIO-formatted labels of the form `B-{SNOMED_CODE}` and `I-{SNOMED_CODE}`, where each code corresponds to one of the dental clinical terms.

- **Loss Function**: Cross-Entropy Loss at the token level (ignoring padding tokens with a label of `-100`).
- **Evaluation Metric**: **Strict Token Micro-F1**, which calculates True Positives, False Positives, and False Negatives globally. If the model predicts an entity with an incorrect SNOMED CT code, it is penalized as both a False Positive for the predicted class and a False Negative for the gold class.

### Training Hyperparameters

The model was trained using the following parameters:

| Hyperparameter | Value | Description |
|----------------|:-----:|:------------|
| **Learning Rate (LR)** | 3×10⁻⁵ | Nominal learning rate for multiclass token classification |
| **Global Batch Size** | 16 | Batch size per training step |
| **Max Epochs** | 50 | Maximum training epochs |
| **Optimizer** | AdamW | Weight decay optimizer |
| **Weight Decay** | 0.01 | L2 regularization coefficient |
| **Precision** | bf16 | Bfloat16 mixed precision for training efficiency |
| **Max Sequence Length** | 8,192 | Maximum sequence length processed |
| **Evaluation Strategy** | epoch | Evaluation performed at the end of each epoch |
| **Early Stopping** | 3 epochs | Patience for early stopping based on validation F1-score |
| **Validation Split** | 0.05 | Test split size for evaluation during training |

---

## Intended Use

### Direct Use

- **End-to-end Dental Entity Extraction and Coding**: Identifying and mapping dental pathologies, anatomy, and procedures directly to SNOMED CT codes in a single step.
- **Clinical Text Structuring**: Structuring unstructured dental patient files into standardized SNOMED CT term representations.

### Out-of-Scope Use

- General clinical Named Entity Recognition outside of dentistry.
- Non-Spanish clinical texts.
- Text-generation tasks (this is an encoder-only model).
- Automated diagnostic or treatment decisions without human expert validation.

---

## How to Use

### With HuggingFace `pipeline`

```python
from transformers import pipeline

# Load the multiclass token classification pipeline
ner_pipeline = pipeline(
    "token-classification",
    model="SINAI/ALIA-MrBERT-es-snomed-dental-ner-multiclass-ctx8192",
    aggregation_strategy="simple"
)

# Clinical text example
clinical_text = "El paciente presenta caries dental en el canino inferior derecho y apiñamiento severo."

# Run inference
entities = ner_pipeline(clinical_text)
for entity in entities:
    print(f"Texto: {entity['word']} | Código SNOMED: {entity['entity_group']} | Confianza: {entity['score']:.4f}")
```

### With `transformers` (Manual Inference)

```python
import torch
from transformers import AutoTokenizer, AutoModelForTokenClassification

model_name = "SINAI/ALIA-MrBERT-es-snomed-dental-ner-multiclass-ctx8192"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

text = "Paciente refiere abrasión dental y requiere un puente de dentina."
inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=8192)

with torch.no_grad():
    outputs = model(**inputs)

predictions = torch.argmax(outputs.logits, dim=-1)
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

for token, pred_id in zip(tokens, predictions[0].tolist()):
    label = model.config.id2label[pred_id]
    if label != "O":
        print(f"Token: {token:15} -> Label: {label}")
```

---

## Evaluation

The model was evaluated using a train/test split containing **80% training** and **20% testing** data, representing a total of **6,022 entities** in the test set.

### Metrics

The token-level multiclass Named Entity Recognition performance on the test set is as follows:

| Metric | Value |
|:---|:---:|
| **Precision** | 96.83% |
| **Recall** | 95.83% |
| **F1-score** | 96.33% |

---

## Supported SNOMED CT Codes

This model is trained to recognize and directly code the following clinical terms from the Spanish dentistry domain:

| Término clínico (Texto) | Código SNOMED CT |
| :--- | :--- |
| abrasión | 47222000 |
| abrasión dental | 47222000 |
| acentuada | 24484000 |
| adelgazamiento | 109706009 |
| agregado óseo | 61838003 |
| aleta de mordida | 241046008 |
| alteración | 18307000 |
| altura del hueso remanente | 710083001 |
| altura del hueso remanente deficiente | 710083001 |
| altura ósea | 769045007 |
| alveolar | 731114003 |
| alvéolo | 1240400004 |
| ameloblastoma unilocular | 278385006 |
| ameloblastoma unilocular infectado | 20462008 |
| amelo-cementaria | 245707008 |
| amplio | 1359828000 |
| anastomosan | 41796003 |
| anatomía patológica | 1255732006 |
| anatomía radicular | 85077000 |
| anquilosis | 36504009 |
| antrolitos | 470756000 |
| apical | 43674008 |
| ápice | 16626007 |
| apiñamiento | 12351004 |
| apolillado | 129736006 |
| artefacto oscuro | 47973001 |
| aspecto granulado | 15933001 |
| aspergilosis | 65553006 |
| ATM | 53620006 |
| atrofia ósea | 53174001 |
| aumento del espacio periodontal | 109630002 |
| basal | 57195005 |
| basilar | 33898000 |
| beam hardening | 47973001 |
| bifurcación | 110586005 |
| bifurcación radicular | 245737004 |
| bilateral | 51440002 |
| lateral | 51440002 |
| biopsia | 86273004 |
| birradicular convergente | 109463000 |
| birradicular divergente | 109462005 |
| borde | 57183005 |
| reborde | 57183005 |
| borde incisal | 245645004 |
| bordes irregulares | 129736006 |
| borrosidad | 111516008 |
| brecha edéntula | 278650002 |
| buco-sinusual | 1156269004 |
| búsqueda de conducto | 234707000 |
| calcificación | 18115005 |
| calculo pulpar | 57602001 |
| cámara | 245740004 |
| cara | 245740004 |
| cámara pulpar | 245740004 |
| cambio degenerativo pulpar | 22361007 |
| canal del nervio dentario inferior | 7854005 |
| canal mandibular | 7854005 |
| canal nasopalatino | 367625000 |
| canales mandibulares | 7854005 |
| canino | 45208001 |
| caninos | 45208001 |
| capuchón pericoronario | 22240003 |
| capuchones foliculares | 110975002 |
| cara vestibular | 245647007 |
| caries | 80967001 |
| caries dental | 80967001 |
| cavidad antral | 110975002 |
| cavidad glenoidea | 46385009 |
| cavidad pulpar | 72236009 |
| cefálico | 66787007 |
| cemento ósea | 6043006 |
| cementoósea | 6043006 |
| cervical | 716360003 |
| cicatriz ósea | 12402003 |
| cierre | 112695004 |
| circular | 354652004 |
| colapso | 271787007 |
| complicación endo periodontal | 2556008 |
| comprometida | 246332000 |
| compromiso de furca | 110585009 |
| compromiso severo de furca | 110585009 |
| concéntrica | 255465008 |
| concomitante | 68405009 |
| concrescencia | 33504000 |
| conducto | 368876003 |
| conducto accesorio | 90956000 |
| conducto DV | 245750003 |
| conducto ML | 245749003 |
| conducto MV | 245748006 |
| conducto vestibular | 245747001 |
| conservado | 11163003 |
| conservada | 11163003 |
| contacto | 11723008 |
| continuas | 255238004 |
| contorno radicular mesial | 245716007 |
| convergente | 263727000 |
| corona | 75628001 |
| coronario | 75628001 |
| corona conservada | 278552004 |
| cortes axiales | 24422004 |
| corticada | 129746008 |
| cortical | 87791003 |
| corticalizadas | 260409000 |
| cráter oseo | 179003002 |
| crestas | 245699009 |
| crestas alveolares | 129143008 |
| Crónica | 90734009 |
| cuadrante mandibular | 245551001 |
| cuerno pulpar | 245742007 |
| cuernos pulpares | 245742007 |
| cuerpo extraño | 19227008 |
| curvatura | 298360005 |
| curvatura | 60301000 |
| defecto óseo | 109706009 |
| degenerativo pulpar | 22361007 |
| dehiscencia | 11108009 |
| densidad osea | 385342005 |
| dentición mixta | 245545006 |
| dentigero | 9245008 |
| dentina de la cámara | 84540008 |
| desajuste marginal | 399898009 |
| desalojo de dispositivo | 128538000 |
| diente cónico | 1162597008 |
| dilaceración | 62568001 |
| disminuido | 1250004 |
| displasia | 25723000 |
| dispositivo hiperdenso | 129744006 |
| dispositivo metálico | 4816004 |
| dispositivo metálico intraconducto | 4816004 |
| distal | 46053002 |
| divergente | 263741009 |
| edéntula | 278650002 |
| edéntulas | 278650002 |
| edéntulo | 278650002 |
| eminencia | 303403006 |
| En formación | 90555008 |
| en formación | 90555008 |
| encapsulado | 59135002 |
| endodóntico | 55670007 |
| endoperiodontal | 55670007 |
| engrosamiento | 263899003 |
| ensanchado | 90522003 |
| ensanchamiento | 90522003 |
| ensanchando | 90522003 |
| entrada de | 263558002 |
| erosión | 82212003 |
| erupción | 397797004 |
| erupcionada | 397797004 |
| erupcionado | 397797004 |
| eruptivo | 397797004 |
| escaso trabeculado | 449781000 |
| espacio cameral | 245740004 |
| espacio del ligamento periodontal | 245775004 |
| espacio folicular | 110975002 |
| espacio medular | 46535001 |
| espacio sinusal | 271745005 |
| espigo | 463864000 |
| espigo metálico | 463864000 |
| espina nasal anterior | 767496007 |
| estadio de maduración | 364673002 |
| estrechos | 134223000 |
| estructura dentaria | 38199008 |
| estudio histopatológico | 252416005 |
| evolución extraósea | 234949000 |
| evolución intraósea | 397797004 |
| fenestra | 257825001 |
| fenestración | 257825001 |
| fibrodontoma ameloblástico | 84983008 |
| fibroma osificante | 25603007 |
| finalidad protésica | 971009 |
| fisiológica | 1360005 |
| fistula | 118622000 |
| fisura | 47393002 |
| foramen | 276742007 |
| forma de cuña | 310423000 |
| formación radicular | 1259298002 |
| fosa nasal | 53912006 |
| fosas nasales | 53912006 |
| fractura | 72704001 |
| fragmento | 29140007 |
| fuerza eruptiva | 110294004 |
| gingival | 372457001 |
| giroversion | 38089000 |
| granulado | 385043007 |
| Granuloma | 45647009 |
| heterogéneo | 1359749008 |
| Hipercementosis | 78537008 |
| hiperdensa | 129744006 |
| hipermovilidad | 263778007 |
| hiperplasia folicular | 43961000 |
| hipodenso | 129746008 |
| homogeneo | 255384007 |
| hueso esponjoso | 20870005 |
| hueso medular | 46535001 |
| idiopática | 54690008 |
| imagen isodensa | 129745007 |
| imagenologico | 363679005 |
| imagenológico de normalidad | 17621005 |
| impactación | 235104008 |
| impacta | 235104008 |
| semi-impactado | 1148577004 |
| semi-incluido | 1148577004 |
| implante | 1303757005 |
| implante dental | 1303757005 |
| implante dental rehabilitado | 1371558003 |
| impresiona pérdida mineral | 128420001 |
| incipiente | 25721003 |
| incisivos | 78509001 |
| inclinado | 278653000 |
| incluida | 235104008 |
| inclusión | 235104008 |
| completo | 255594003 |
| incompleta | 255599008 |
| incompleto | 255599008 |
| infiltración | 47351003 |
| informe de corte | 371525003 |
| infraoclusión | 234973008 |
| injerto óseo | 80983001 |
| inserción | 738993004 |
| integridad | 32082000 |
| intraóseo | 417255000 |
| invertidos | 263787003 |
| irregulares | 49608001 |
| isodensa | 129745007 |
| isodensidad | 129745007 |
| lamina dura | 450722007 |
| lámina dura | 450722007 |
| laxo | 12554006 |
| lesión | 52988006 |
| ligamento periodontal | 245775004 |
| limite amelocementario | 58592000 |
| Línea no radiodensa | 129746008 |
| lingual | 255579002 |
| lobuladas | 62655004 |
| lumen | 113342003 |
| luz poco visible | 415582006 |
| malposición | 81256000 |
| mandibula | 91609006 |
| Mandíbula | 91609006 |
| marcado | 46998006 |
| material desadaptado | 109728009 |
| material hiperdenso | 129744006 |
| material hipodenso | 129746008 |
| maxilar | 70925003 |
| membrana sinusal | 87550002 |
| mesial | 710099007 |
| Mesiodens | 17802000 |
| mesio-distal | 245679003 |
| Mesioinclinada | 699457000 |
| mesiovestibular | 245662009 |
| mesio-vestibular | 245662009 |
| mesolingulo inclinada | 278676002 |
| microdoncia | 32337007 |
| mineral | 87918000 |
| ML | 245749003 |
| molar | 76928009 |
| mucositis | 95361005 |
| Multirradicular | 19231000000000 |
| muñón protésico | 706370006 |
| MV | 245748006 |
| nervio dentario inferior | 49792003 |
| neumatización | 47173002 |
| nivel de tercio medio | 261133007 |
| no radiodensa | 129746008 |
| objeto extraño | 19227008 |
| oblicua | 21114003 |
| obliteración | 15524008 |
| obliterado | 89925002 |
| obturación | 50173008 |
| obturado | 50173008 |
| oclusal | 710098004 |
| oclusales | 710098004 |
| ocupado | 118247008 |
| odontoma complejo | 29020002 |
| orientación cefálica | 1209182005 |
| osteólisis | 203522001 |
| osteolítica | 30425001 |
| osteolítico | 30425001 |
| palatina | 72203008 |
| palatino | 72203008 |
| papila dental | 726069006 |
| parcialmente | 255609007 |
| pared lateral | 277154009 |
| patrón de reabsorción externo | 41918006 |
| patrón imagenológico de normalidad | 168500000 |
| patrón remodelado | 370549005 |
| penetrante | 53568006 |
| perdida de estructura dentaria | 234977009 |
| pérdida de tejido mineralizado | 128420001 |
| pérdida ósea | 312894000 |
| pérdida total del tejido coronal | 234977009 |
| perfil radicular | 245712009 |
| perforación | 36191001 |
| perfora | 36191001 |
| pericoronario ensanchado | 22240003 |
| peri-implantares | 699422003 |
| periodonto | 1230218002 |
| permeabilidad | 82540007 |
| perno | 77444004 |
| pieza dentaria supernumeraria | 367534004 |
| pilar de prótesis fija | 707144009 |
| pin intraradicular | 272346006 |
| piso de fosa nasal | 279549004 |
| plano axial | 399061009 |
| póntico | 260930001 |
| pónticos | 260930001 |
| posición asimétrica | 4128009 |
| posición horizontal | 24020000 |
| posición oblicua | 399366008 |
| post extracción | 128926000 |
| premolar | 76424003 |
| proceso de cicatrización | 48677004 |
| proceso osteolítico perirradicular | 34282009 |
| protuberancia | 49557009 |
| protuberancias | 49557009 |
| proximal | 40415009 |
| puente de dentina | 109601009 |
| quiste | 367643001 |
| radicular | 85084008 |
| radio densa | 129744006 |
| radiodensa | 129744006 |
| radioedensa | 129744006 |
| radiolúcida | 263850002 |
| raices curvas | 110333006 |
| raíces vestibulares | 85077000 |
| Raíz DV | 245734006 |
| Raíz MV | 245733000 |
| raíz única | 245729007 |
| rama ascendente mandibular | 23938008 |
| rasgos imagenológicos | 258106000 |
| rayos X | 363680008 |
| reabsorbidos | 22200009 |
| reabsorción ósea | 70931000 |
| reborde alveolar | 109703001 |
| reborde basilar | 11048003 |
| recidiva | 246455001 |
| reducción de la luz | 415582006 |
| relación de proximidad | 40415009 |
| relleno | 311933008 |
| relleno óseo | 118417008 |
| Remanente radicular | 66569006 |
| remodelado | 370549005 |
| residual | 65320000 |
| respuesta endoperiodontal | 235006007 |
| respuesta ósea | 30397001 |
| respuesta periodontal | 2556008 |
| restauración | 173307000 |
| retención mucosa | 1260280009 |
| retención mucoso | 6078006 |
| retenida | 196419009 |
| retenido | 196419009 |
| retraso eruptivo | 5639000 |
| rizálisis avanzada | 109588005 |
| seno maxilar | 15924003 |
| seudoquiste | 13467000 |
| sin datos a destacar | 281900007 |
| sínfisis | 336205008 |
| sinuoso | 70984001 |
| sinusitis | 36971009 |
| solución de continuidad | 247442005 |
| soporte óseo | 272673000 |
| submucosa | 68439008 |
| sumergido | 234973008 |
| superficies articulares | 70746003 |
| supernumeraria | 367534004 |
| supernumerario | 367534004 |
| tabla ósea | 271003 |
| tallado mecánico coronario | 234740009 |
| tejidos blandos | 95937008 |
| temporario | 21644001 |
| tercio | 272427006 |
| tercio medio | 261133007 |
| tomográfico | 312251004 |
| Torus | 70033004 |
| trabeculas oseas | 20870005 |
| trabéculas | 20870005 |
| transmigración | 50033000 |
| transposición | 405257002 |
| trayecto fistuloso | 1360029003 |
| trifurca | 245738009 |
| tubular | 13336003 |
| tumor queratoquistico odontogenico | 713277006 |
| unilocular | 66715007 |
| unirradicular | 245729007 |
| vértica cuspideo | 28255003 |
| vertical | 33096000 |
| vértice cuspideo | 28255003 |
| vestibular | 302990001 |
| vestíbulo | 109773002 |
| vestíbulo inclinación | 278666000 |
| vitalometría | 12282003 |
| vitalométrica | 12282003 |
| zona apical | 16626007 |
| zona basal | 91609006 |
| zona de furca | 110585009 |
| zonas de densidad | 129744006 |
| zonas de densidad dentaria | 129744006 |
| birradicular | 19221000122103 |
| periradicular | 19221000122103 |
| compromiso zona de furca | 110585009 |
| densidad dental | 385342005 |
| cara proximal | 245651009 |
| enamel | 76993005 |
| tejido coronal | 76993005 |
| perlas de esmalte | 3783004 |

---

## Limitations and Biases

### Known Limitations

- **Large Label Space**: Classifying tokens into ~815 possible classes (BIO tags for ~400 concepts) is a highly complex task. While it allows direct mapping, rare concepts with limited training representation may show lower extraction performance compared to more frequent terms like *caries*.
- **Domain Focus**: Highly specialized for Spanish dental reports and maxillofacial descriptions.
- **Syntactic Context**: Mappings rely on contextual clues. Out-of-context dental lists or non-standard abbreviations may be misclassified.

### Biases

- Training data primarily mirrors institutional writing conventions and regional terminology variations from the clinic source.

---

## Additional Information

### License
[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

### Citation

If you use this model in your research, please cite:

```bibtex
@misc{ALIA-MrBERT-es-snomed-dental-ner-multiclass-ctx8192,
  title        = {ALIA MrBERT-es Snomed Dental Multiclass NER Model},
  author       = {SINAI Research Group, Universidad de Jaén},
  year         = {2026},
  publisher    = {HuggingFace},
  howpublished = {\url{https://huggingface.co/SINAI/ALIA-MrBERT-es-snomed-dental-ner-multiclass-ctx8192}}
}
```

Please also cite the base model:

```bibtex
@misc{tamayo2026mrbertmodernmultilingualencoders,
      title={MrBERT: Modern Multilingual Encoders via Vocabulary, Domain, and Dimensional Adaptation}, 
      author={Daniel Tamayo and Iñaki Lacunza and Paula Rivera-Hidalgo and Severino Da Dalt and Javier Aula-Blasco and Aitor Gonzalez-Agirre and Marta Villegas},
      year={2026},
      eprint={2602.21379},
      archivePrefix={arXiv},
      primaryClass={cs.CL},
      url={https://arxiv.org/abs/2602.21379}, 
}
```

### Funding
This work is funded by the Ministerio para la Transformación Digital y de la Función Pública - Funded by EU – NextGenerationEU within the framework of the project [ALIA](https://alia.gob.es).

### Acknowledgments
This dataset has been generated thanks to [CEATIC](https://www.ujaen.es/centros/ceatic/) (Centro de Estudios Avanzados en Tecnologías de la Información y de la Comunicación) – [UJA](http://www.ujaen.es/) (Universidad de Jaén) which provided the needed computational resources on its clusters.

---

**Contact:** [ALIA Project](https://www.alia.gob.es/) - [SINAI Research Group](https://sinai.ujaen.es) - [Universidad de Jaén](https://www.ujaen.es/)

**More Information:** [SINAI Research Group](https://sinai.ujaen.es) | [ALIA-UJA Project](https://github.com/sinai-uja/ALIA-UJA)
