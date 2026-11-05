---
license: apache-2.0
datasets:
- ai4privacy/pii-masking-openpii-1.5m
language:
- en
- nl
- fr
- de
- es
- it
- da
- sv
- pt
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: token-classification
library_name: transformers
tags:
- pii
- deidentification
---


Finetuning was done using [MedNER](https://github.com/UPOD-datascience/MedNER.nl) with the following script:

We limited the training to the following languages: English, Dutch, French, German, Spanish, Italian, Danish, Swedish and Portuguese, 
which are relatively close, in a linguistic sense, allowing for a languages to benefit from cross-over information.

The model was train in a multiclass-sense, using a cross-entropy loss. We replaced the standard 768-weight linear layer
by 3x768 dense layers with 10\% dropout and ReLu activations.
```bash
#!/usr/bin/env bash
set -euo pipefail

# Ready-to-run training script for:
#   ai4privacy/pii-masking-openpii-1.5m
#
# Usage:
#   bash scripts/run_hf_ai4privacy_training.sh multilabel
#   bash scripts/run_hf_ai4privacy_training.sh multiclass
#
# Optional:
#   export HF_TOKEN=hf_xxx   # only needed for gated/private datasets

MODE="${1:-multiclass}"

COMMON_ARGS=(
  --lang multi
  --hf_dataset ai4privacy/pii-masking-openpii-1.5m
  --text_column source_text
  --tags_column privacy_mask
  --selector_column language
  --selection nl en fr de es it da sv pt
  --parse_annotations
  --train_model
  --force_splitter
  --model FacebookAI/xlm-roberta-base
  --chunk_size=32
  --max_token_length=32
  --batch_size 2
  --accumulation_steps 8
  --learning_rate=2e-5
  --weight_decay=1e-5
  --num_epochs=5
  --num_splits=5
  --use_class_weights
  --classifier_hidden_layers 768 768 768
  --chunk_type paragraph
  --entity_types AGE DATE BUILDINGNUM CITY ZIPCODE STREET GIVENNAME SURNAME SOCIALNUM PASSPORTNUM SEX GENDER TELEPHONENUM IDCARDNUM EMAIL

)

if [ -n "${HF_TOKEN:-}" ]; then
  COMMON_ARGS+=(--hf_token "${HF_TOKEN}")
fi

if [ "${MODE}" = "multiclass" ]; then
  poetry run python -m cardioner.main \
    "${COMMON_ARGS[@]}" \
    --multiclass \
    --output_dir /out/put/location_multilabel
elif [ "${MODE}" = "multilabel" ]; then
  poetry run python -m cardioner.main \
    "${COMMON_ARGS[@]}" \
    --output_dir /out/put/location_multilabel
else
  echo "Unknown mode: ${MODE}. Use 'multilabel' or 'multiclass'." >&2
  exit 1
fi
```


Token classification scores (answering the question: ***given** the span, to which class does it belong?*):

```json
      "eval_AGE": {
        "f1": 0.9672360768551506,
        "number": 32192,
        "precision": 0.9484920871902061,
        "recall": 0.9867358349900597
      },
      "eval_BUILDINGNUM": {
        "f1": 0.9832519792331442,
        "number": 28889,
        "precision": 0.9798886138613861,
        "recall": 0.9866385129287965
      },
      "eval_CITY": {
        "f1": 0.9726022504018575,
        "number": 41669,
        "precision": 0.9651668399659703,
        "recall": 0.9801531114257601
      },
      "eval_DATE": {
        "f1": 0.997746454524687,
        "number": 80940,
        "precision": 0.9972108062744517,
        "recall": 0.9982826785273041
      },
      "eval_EMAIL": {
        "f1": 0.9962614462862082,
        "number": 51445,
        "precision": 0.9953818689847873,
        "recall": 0.9971425794537856
      },
      "eval_GENDER": {
        "f1": 0.974448482073879,
        "number": 17457,
        "precision": 0.973473587925909,
        "recall": 0.9754253308128544
      },
      "eval_GIVENNAME": {
        "f1": 0.9365210222588624,
        "number": 100350,
        "precision": 0.9334706161888168,
        "recall": 0.9395914299950174
      },
      "eval_IDCARDNUM": {
        "f1": 0.9049785748995008,
        "number": 22068,
        "precision": 0.8827889338964061,
        "recall": 0.9283124886713794
      },
      "eval_PASSPORTNUM": {
        "f1": 0.9242263349514563,
        "number": 12959,
        "precision": 0.9087180252069506,
        "recall": 0.9402731692260206
      },
      "eval_SEX": {
        "f1": 0.9694227341286166,
        "number": 14570,
        "precision": 0.9683604985618408,
        "recall": 0.970487302676733
      },
      "eval_SOCIALNUM": {
        "f1": 0.9280586914587484,
        "number": 15327,
        "precision": 0.9004663721158567,
        "recall": 0.9573954459450643
      },
      "eval_STREET": {
        "f1": 0.9810103469263542,
        "number": 32803,
        "precision": 0.9793116019078287,
        "recall": 0.9827149955796726
      },
      "eval_SURNAME": {
        "f1": 0.9306129607436204,
        "number": 85192,
        "precision": 0.926976695433423,
        "recall": 0.9342778664663348
      },
      "eval_TELEPHONENUM": {
        "f1": 0.9940678080618354,
        "number": 36941,
        "precision": 0.9924450920079866,
        "recall": 0.9956958393113343
      },
      "eval_ZIPCODE": {
        "f1": 0.9856799457604832,
        "number": 24346,
        "precision": 0.9860648661980516,
        "recall": 0.9852953257208577
      }
```

End2End scores (answering the question: *given a text, what are the spans **and** to which class do they belong?*): 
```json
{
	"strict": {
		"per_category": {
			"AGE": {
				"Precision": 0.86,
				"Recall": 0.87,
				"F1": 0.87
			},
			"BUILDINGNUM": {
				"Precision": 0.94,
				"Recall": 0.91,
				"F1": 0.93
			},
			"CITY": {
				"Precision": 0.88,
				"Recall": 0.88,
				"F1": 0.88
			},
			"DATE": {
				"Precision": 0.69,
				"Recall": 0.68,
				"F1": 0.68
			},
			"EMAIL": {
				"Precision": 0.12,
				"Recall": 0.1,
				"F1": 0.11
			},
			"GENDER": {
				"Precision": 0.95,
				"Recall": 0.88,
				"F1": 0.91
			},
			"GIVENNAME": {
				"Precision": 0.92,
				"Recall": 0.9,
				"F1": 0.91
			},
			"IDCARDNUM": {
				"Precision": 0.77,
				"Recall": 0.64,
				"F1": 0.7
			},
			"PASSPORTNUM": {
				"Precision": 0.84,
				"Recall": 0.74,
				"F1": 0.79
			},
			"SEX": {
				"Precision": 0.95,
				"Recall": 0.9,
				"F1": 0.92
			},
			"SOCIALNUM": {
				"Precision": 0.71,
				"Recall": 0.82,
				"F1": 0.76
			},
			"STREET": {
				"Precision": 0.86,
				"Recall": 0.87,
				"F1": 0.86
			},
			"SURNAME": {
				"Precision": 0.91,
				"Recall": 0.89,
				"F1": 0.9
			},
			"TELEPHONENUM": {
				"Precision": 0.67,
				"Recall": 0.73,
				"F1": 0.7
			},
			"ZIPCODE": {
				"Precision": 0.91,
				"Recall": 0.89,
				"F1": 0.9
			}
		},
		"micro": {
			"Precision": 0.79,
			"Recall": 0.77,
			"F1": 0.78
		},
		"macro": {
			"Precision": 0.8,
			"Recall": 0.78,
			"F1": 0.79
		}
	},
	"relaxed": {
		"per_category": {
			"AGE": {
				"Precision": 0.9,
				"Recall": 0.9,
				"F1": 0.9
			},
			"BUILDINGNUM": {
				"Precision": 0.96,
				"Recall": 0.92,
				"F1": 0.94
			},
			"CITY": {
				"Precision": 0.94,
				"Recall": 0.95,
				"F1": 0.95
			},
			"DATE": {
				"Precision": 0.97,
				"Recall": 0.96,
				"F1": 0.96
			},
			"EMAIL": {
				"Precision": 0.96,
				"Recall": 0.79,
				"F1": 0.86
			},
			"GENDER": {
				"Precision": 0.97,
				"Recall": 0.9,
				"F1": 0.93
			},
			"GIVENNAME": {
				"Precision": 0.98,
				"Recall": 0.97,
				"F1": 0.97
			},
			"IDCARDNUM": {
				"Precision": 0.9,
				"Recall": 0.74,
				"F1": 0.81
			},
			"PASSPORTNUM": {
				"Precision": 0.92,
				"Recall": 0.8,
				"F1": 0.86
			},
			"SEX": {
				"Precision": 0.95,
				"Recall": 0.91,
				"F1": 0.93
			},
			"SOCIALNUM": {
				"Precision": 0.78,
				"Recall": 0.9,
				"F1": 0.84
			},
			"STREET": {
				"Precision": 0.95,
				"Recall": 0.96,
				"F1": 0.96
			},
			"SURNAME": {
				"Precision": 0.97,
				"Recall": 0.96,
				"F1": 0.97
			},
			"TELEPHONENUM": {
				"Precision": 0.91,
				"Recall": 0.98,
				"F1": 0.94
			},
			"ZIPCODE": {
				"Precision": 0.94,
				"Recall": 0.92,
				"F1": 0.93
			}
		},
		"micro": {
			"Precision": 0.95,
			"Recall": 0.92,
			"F1": 0.93
		},
		"macro": {
			"Precision": 0.93,
			"Recall": 0.9,
			"F1": 0.92
		}
	}
}
```

which we obtained by running:
```bash
MODEL=/path/to/model
ARGS=(
  --inference_only
  --model_path="$MODEL"
  --corpus_inference=ai4privacy/pii-masking-openpii-1.5m
  --text_column=source_text
  --tags_column=privacy_mask
  --lang=multi
  --inference_stride=32
  --selector_column=language
  --selection nl en fr de es it da sv pt
  --inference_pipe=dt4h
  --trust_remote_code
  --output_file_prefix=multiclass_multilang_
  --allow_numeric_tags AGE BUILDINGNUM DATE IDCARDNUM PASSPORTNUM SOCIALNUM TELEPHONENUM ZIPCODE
)

poetry run python -m cardioner.main "${ARGS[@]}"
```
