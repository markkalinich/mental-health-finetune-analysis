---
license: apache-2.0
datasets:
- ai4privacy/pii-masking-openpii-1.5m
language:
- nl
base_model:
- DTAI-KULeuven/robbert-2023-dutch-large
pipeline_tag: token-classification
library_name: transformers
tags:
- pii
- deidentification
---


Finetuning was done using [MedNER](https://github.com/UPOD-datascience/MedNER.nl).

We limited the training to Dutch.

The model was trained in a multiclass, using a cross-entropy loss, which followed the standard IOB-schema 
(that is **O**utside the span, **B**eginning of the span, **I**nside the span)
We replaced the standard 768-weight linear layer by 3x768 dense layers with 10\% dropout and ReLu activations.

The weights are a result of chained SLERP over five cross-validated folds.

Token classification scores (answering the question: ***given** the span, to which class does it belong?*):

```json
{
  "eval_AGE": {
    "f1": 0.958,
    "precision": 0.957,
    "recall": 0.959
  },
  "eval_BUILDINGNUM": {
    "f1": 0.968,
    "precision": 0.968,
    "recall": 0.969
  },
  "eval_CITY": {
    "f1": 0.974,
    "precision": 0.968,
    "recall": 0.980
  },
  "eval_CREDITCARDNUMBER": {
    "f1": 0.954,
    "precision": 0.951,
    "recall": 0.957
  },
  "eval_DATE": {
    "f1": 0.998,
    "precision": 0.996,
    "recall": 0.999
  },
  "eval_DRIVERLICENSENUM": {
    "f1": 0.961,
    "precision": 0.957,
    "recall": 0.966
  },
  "eval_EMAIL": {
    "f1": 0.970,
    "precision": 0.958,
    "recall": 0.984
  },
  "eval_GENDER": {
    "f1": 0.936,
    "precision": 0.928,
    "recall": 0.945
  },
  "eval_GIVENNAME": {
    "f1": 0.903,
    "precision": 0.898,
    "recall": 0.908
  },
  "eval_IDCARDNUM": {
    "f1": 0.815,
    "precision": 0.792,
    "recall": 0.841
  },
  "eval_PASSPORTNUM": {
    "f1": 0.976,
    "precision": 0.972,
    "recall": 0.981
  },
  "eval_SEX": {
    "f1": 0.950,
    "precision": 0.952,
    "recall": 0.948
  },
  "eval_SOCIALNUM": {
    "f1": 0.640,
    "precision": 0.650,
    "recall": 0.632
  },
  "eval_STREET": {
    "f1": 0.980,
    "precision": 0.979,
    "recall": 0.981
  },
  "eval_SURNAME": {
    "f1": 0.898,
    "precision": 0.894,
    "recall": 0.901
  },
  "eval_TAXNUM": {
    "f1": 0.746,
    "precision": 0.740,
    "recall": 0.751
  },
  "eval_TELEPHONENUM": {
    "f1": 0.984,
    "precision": 0.979,
    "recall": 0.989
  },
  "eval_TITLE": {
    "f1": 0.998,
    "precision": 0.997,
    "recall": 0.999
  },
  "eval_ZIPCODE": {
    "f1": 0.966,
    "precision": 0.968,
    "recall": 0.964
  },
  "eval_overall": {
    "accuracy": 0.985,
    "f1": 0.939,
    "precision": 0.935,
    "recall": 0.943
  }
}
```

End2End scores (answering the question: *given a text, what are the spans **and** to which class do they belong?*): 
```json
{
	"strict": {
		"per_category": {
			"AGE": {
				"Precision": 0.85,
				"Recall": 0.82,
				"F1": 0.83
			},
			"BUILDINGNUM": {
				"Precision": 0.91,
				"Recall": 0.84,
				"F1": 0.88
			},
			"CITY": {
				"Precision": 0.91,
				"Recall": 0.9,
				"F1": 0.9
			},
			"CREDITCARDNUMBER": {
				"Precision": 0.97,
				"Recall": 0.96,
				"F1": 0.96
			},
			"DATE": {
				"Precision": 0.89,
				"Recall": 0.87,
				"F1": 0.88
			},
			"DRIVERLICENSENUM": {
				"Precision": 0.81,
				"Recall": 0.75,
				"F1": 0.78
			},
			"EMAIL": {
				"Precision": 0.8,
				"Recall": 0.8,
				"F1": 0.8
			},
			"GENDER": {
				"Precision": 0.91,
				"Recall": 0.89,
				"F1": 0.9
			},
			"GIVENNAME": {
				"Precision": 0.85,
				"Recall": 0.88,
				"F1": 0.87
			},
			"IDCARDNUM": {
				"Precision": 0.78,
				"Recall": 0.78,
				"F1": 0.78
			},
			"PASSPORTNUM": {
				"Precision": 0.82,
				"Recall": 0.77,
				"F1": 0.8
			},
			"SEX": {
				"Precision": 0.93,
				"Recall": 0.88,
				"F1": 0.9
			},
			"SOCIALNUM": {
				"Precision": 0.65,
				"Recall": 0.7,
				"F1": 0.67
			},
			"STREET": {
				"Precision": 0.95,
				"Recall": 0.94,
				"F1": 0.94
			},
			"SURNAME": {
				"Precision": 0.87,
				"Recall": 0.86,
				"F1": 0.86
			},
			"TAXNUM": {
				"Precision": 0.79,
				"Recall": 0.69,
				"F1": 0.74
			},
			"TELEPHONENUM": {
				"Precision": 0.72,
				"Recall": 0.7,
				"F1": 0.71
			},
			"TITLE": {
				"Precision": 0.99,
				"Recall": 0.99,
				"F1": 0.99
			},
			"ZIPCODE": {
				"Precision": 0.86,
				"Recall": 0.94,
				"F1": 0.89
			}
		},
		"micro": {
			"Precision": 0.86,
			"Recall": 0.85,
			"F1": 0.86
		},
		"macro": {
			"Precision": 0.86,
			"Recall": 0.84,
			"F1": 0.85
		}
	},
	"relaxed": {
		"per_category": {
			"AGE": {
				"Precision": 0.94,
				"Recall": 0.91,
				"F1": 0.92
			},
			"BUILDINGNUM": {
				"Precision": 0.93,
				"Recall": 0.86,
				"F1": 0.89
			},
			"CITY": {
				"Precision": 0.96,
				"Recall": 0.96,
				"F1": 0.96
			},
			"CREDITCARDNUMBER": {
				"Precision": 0.98,
				"Recall": 0.97,
				"F1": 0.98
			},
			"DATE": {
				"Precision": 0.99,
				"Recall": 0.96,
				"F1": 0.98
			},
			"DRIVERLICENSENUM": {
				"Precision": 0.98,
				"Recall": 0.91,
				"F1": 0.94
			},
			"EMAIL": {
				"Precision": 0.99,
				"Recall": 0.99,
				"F1": 0.99
			},
			"GENDER": {
				"Precision": 0.94,
				"Recall": 0.92,
				"F1": 0.93
			},
			"GIVENNAME": {
				"Precision": 0.94,
				"Recall": 0.97,
				"F1": 0.95
			},
			"IDCARDNUM": {
				"Precision": 0.78,
				"Recall": 0.78,
				"F1": 0.78
			},
			"PASSPORTNUM": {
				"Precision": 0.98,
				"Recall": 0.93,
				"F1": 0.95
			},
			"SEX": {
				"Precision": 0.95,
				"Recall": 0.89,
				"F1": 0.92
			},
			"SOCIALNUM": {
				"Precision": 0.65,
				"Recall": 0.7,
				"F1": 0.67
			},
			"STREET": {
				"Precision": 0.98,
				"Recall": 0.96,
				"F1": 0.97
			},
			"SURNAME": {
				"Precision": 0.96,
				"Recall": 0.95,
				"F1": 0.96
			},
			"TAXNUM": {
				"Precision": 0.79,
				"Recall": 0.7,
				"F1": 0.74
			},
			"TELEPHONENUM": {
				"Precision": 0.97,
				"Recall": 0.95,
				"F1": 0.96
			},
			"TITLE": {
				"Precision": 0.99,
				"Recall": 0.99,
				"F1": 0.99
			},
			"ZIPCODE": {
				"Precision": 0.88,
				"Recall": 0.96,
				"F1": 0.92
			}
		},
		"micro": {
			"Precision": 0.95,
			"Recall": 0.93,
			"F1": 0.94
		},
		"macro": {
			"Precision": 0.93,
			"Recall": 0.91,
			"F1": 0.92
		}
	}
}
```

Usage:

```python

> pipe = pipeline("token-classification", model="UMCU/PII_RobBERT", trust_remote_code=True, aggregation_strategy="simple", dtype=torch.float32,)

> pipe("De patient Henk de Vries is geboren op 12-03-1980 en woont in Amsterdam.")

> [{'entity_group': 'GIVENNAME',
  'score': np.float32(0.9999993),
  'word': ' Henk',
  'start': 12,
  'end': 15},
 {'entity_group': 'SURNAME',
  'score': np.float32(0.99999994),
  'word': ' de Vries',
  'start': 17,
  'end': 24},
 {'entity_group': 'DATE',
  'score': np.float32(1.0),
  'word': ' 12 - 03 - 1980',
  'start': 40,
  'end': 49},
 {'entity_group': 'CITY',
  'score': np.float32(0.99999917),
  'word': ' Amsterdam',
  'start': 63,
  'end': 71}]

```
