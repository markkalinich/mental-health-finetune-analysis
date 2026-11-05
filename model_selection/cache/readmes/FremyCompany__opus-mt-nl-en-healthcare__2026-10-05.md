---
license: mit
language:
- nl
- en
pipeline_tag: translation
---
# Opus-MT-NL-EN-Healthcare

This model can be used to translate medical text from Dutch to English, as a baseline for Clinical NLP systems in Dutch.

## Model Details

### Model Description

This model based on MarianMT was trained using OpusNLP data as well as specialized medical data (see paper for more details).

- **Developed by:** François Remy
- **Model type:** Translation
- **Languages:** From Dutch to English
- **License:** MIT
- **Finetuned from model:** Helsinki-NLP/opus-mt-nl-en

### Model Sources

- **Repository:** [Snomed Translation Dictionaries](https://github.com/FremyCompany/snomed-translate-dictionaries)
- **Paper:** [Taming large lexicons: translating clinical text using medical ontologies and sentence templates](https://biblio.ugent.be/publication/01GMN7J3X37CKWCKQV6DWGM4ZE/file/01GMN7NT30DKF37RXN31DSJZ2D.pdf)

## Citation

If you use this model as part of your work, please cite the following paper:

**BibTeX:**

```
@inproceedings{remy-et-al-2022-translating,
  author       = {{Remy, François and De Jaeger, P. and Demuynck, Kris}},
  title        = {{Taming large lexicons: translating clinical text using medical ontologies and sentence templates}},
  booktitle    = {{EmP 2022}}
  location     = {{Roeselare, Belgium}},
  year         = {{2022}},
  language     = {{en}},
  pages        = {{5}},
}
```

**APA:**

```
Remy, F., De Jaeger, P., & Demuynck, K. (2022). Taming large lexicons: translating clinical text using medical ontologies and sentence templates. Presented at the EmP 2022, The “Engineers meet Practicians” conference, Roeselare, Belgium.
```

