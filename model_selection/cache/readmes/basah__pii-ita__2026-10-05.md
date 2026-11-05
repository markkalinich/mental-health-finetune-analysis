---
language:
- it
license: apache-2.0
library_name: opf
base_model: openai/privacy-filter
pipeline_tag: token-classification
tags:
- privacy-filter
- pii-detection
- italian
- anonymization
- ner
- opf
---

# pii-ita

Fine-tuning di [openai/privacy-filter](https://huggingface.co/openai/privacy-filter) su documenti italiani sintetici per il riconoscimento di PII (Personally Identifiable Information).

Modello addestrato su dataset sintetico italiano (checkpoint_step1_italian_docs_v2).

## ⚠️ Come caricare il modello

Questo modello usa un'architettura **custom** (`model_type: privacy_filter`) **non** registrata in `transformers`. NON funziona con `AutoModel` / `transformers.pipeline`.

Per usarlo serve la libreria `opf`:

```bash
pip install git+https://github.com/openai/privacy-filter.git
```

```python
import os
os.environ['OPF_MOE_TRITON'] = '0'  # disabilita kernel CUDA-only su MPS/CPU

from opf import OPF
from huggingface_hub import snapshot_download

# Scarica il modello (viene messo in cache locale)
local_path = snapshot_download(repo_id='basah/pii-ita')

model = OPF(
    model=local_path,
    device='cuda',           # oppure 'mps' (Apple Silicon) o 'cpu'
    output_mode='typed',
    decode_mode='viterbi',
)

text = 'Il sottoscritto Mario Rossi, CF RSSMRA80A01H501U, residente in Via Roma 10, Milano.'
result = model.redact(text)

print(result.redacted_text)
# -> Il sottoscritto <PRIVATE_PERSON>, <CODICE_FISCALE>, residente in <PRIVATE_ADDRESS>.

for span in result.detected_spans:
    print(f'{span.label:25s} "{span.text}" [{span.start}:{span.end}]')
```

## 📋 Categorie riconosciute

Il modello riconosce **18** categorie di PII italiane:

| Categoria | Descrizione |
|---|---|
| `private_person` | Nomi di persone fisiche |
| `private_address` | Indirizzi (vie, città, numeri civici) |
| `private_email` | Indirizzi email |
| `private_phone` | Numeri di telefono italiani |
| `private_url` | URL contenenti dati personali |
| `private_date` | Date (nascita, scadenze, eventi) |
| `account_number` | Numeri di conto (generici) |
| `secret` | Credenziali, password, token |
| `codice_fiscale` | Codice Fiscale italiano (16 caratteri) |
| `carta_identita` | Numero Carta d'Identità italiana |
| `patente` | Numero Patente di guida |
| `passaporto` | Numero Passaporto |
| `partita_iva` | Partita IVA italiana (11 cifre) |
| `iban` | IBAN italiano (27 caratteri) |
| `tessera_sanitaria` | Tessera Sanitaria |
| `numero_procedimento` | Numero procedimento legale (RG) |
| `riferimento_catastale` | Riferimento catastale (foglio/mappale) |
| `parte_in_causa` | Parti in procedimento giudiziario |

## 📊 Dettagli training

- **Base model**: `openai/privacy-filter`
- **Dati**: **7500** esempi di training, **1250** di validation, **(held-out, non usato in training)** di test (held-out)
- **Epoche**: 14
- **Batch size**: 1
- **Grad accum steps**: 4
- **Learning rate**: 1e-05
- **Hardware training**: cuda
- **Best epoch**: 14 (validation loss: 0.0000)
- **Param dtype**: bfloat16

## 🎯 Metriche (validation set)

- **Token accuracy** (best): 1.0000
- **Validation loss** (best): 0.0000

## 🎨 Esempi di output

**Input**: `Per bonifici IBAN IT60X0542811101000000123456 intestato a Luigi Bianchi. luigi.bianchi@studio.it`

**Output**: `Per bonifici <IBAN> intestato a <PRIVATE_PERSON>. <PRIVATE_EMAIL>`

## ⚖️ Licenza & limitazioni

- **Licenza**: Apache 2.0 (ereditata dal base model)
- **Limiti**: il dataset è sintetico — il modello potrebbe avere pattern overfitted su formati tipici (es. "CF RSSMRA80A01H501U" preceduto da prefisso). Testa con i tuoi testi prima dell'uso in produzione.
- **Contesto**: addestrato su testo italiano generico (email, CV, news, chat, business). Non ottimizzato per domini specifici (medico, scientifico, etc.).
- **Dati sintetici**: nessun dato reale di terze parti usato nel training. Tutti gli esempi sono generati programmaticamente con formati italiani validi ma valori casuali.

## 📎 Citazione

Se usi questo modello, per favore cita il lavoro originale di OpenAI:

```
@misc{openai-privacy-filter,
  title = {Privacy Filter},
  author = {OpenAI},
  year = {2024},
  url = {https://github.com/openai/privacy-filter}
}
```
