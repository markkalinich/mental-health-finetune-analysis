---
dataset_info:
  features:
  - name: prompt
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  - name: completion
    list:
    - name: content
      dtype: string
    - name: role
      dtype: string
  splits:
  - name: train
    num_bytes: 16148054
    num_examples: 9572
  download_size: 3120025
  dataset_size: 16148054
configs:
- config_name: default
  data_files:
  - split: train
    path: data/train-*
---

# Art Therapy Dialogue Dataset

## Dataset Summary

A synthetic Spanish-language dataset of post–art-making therapeutic dialogues, designed for supervised fine-tuning of a clinically grounded conversational model (the *Method Actor*). The dataset simulates the structured phase-by-phase interaction that follows the creation of an artwork in an art therapy session.

Real art-therapy dialogue corpora are extremely scarce and, when available, are typically inaccessible due to privacy, confidentiality, and ethical constraints. This dataset was synthetically generated to provide the scale and phase coverage needed for fine-tuning, anchored by a small set of therapist-reviewed seed examples.

---

## Dataset Details

### Languages

Spanish (`es`). All dialogues were generated in Spanish. A curation step was applied to remove instances with English-language intrusions (see [Curation](#curation) below).

### Dataset Size

| Split | Examples | Size |
|-------|----------|------|
| train | 9,572    | ~15.4 MB |

### Phases

Each instance is labelled with one of four therapeutic phases:

| Phase key   | Phase name (ES)                       | Description |
|-------------|---------------------------------------|-------------|
| `phase_1`   | Mirada intencional                    | Pure visual description of the artwork — colours, shapes, textures, spatial relationships. No interpretation yet. |
| `phase_2`   | Diálogo con la obra                   | Dialogic engagement: the client is invited to address the artwork directly, project into its elements, or take on its perspective. |
| `phase_3`   | Reflexión cognitiva y simbólica       | Open reflective conversation about personal meaning — what the work represents or resonates with in the client's life. |
| `phase_4`   | Cierre y resignificación              | Integration and closure: consolidating insights, naming what has shifted, and ending the session with intention. |

---

## Model

Generation was performed using `gpt-5-nano` via the OpenAI API.

---

## Dataset Structure

Every instance follows a **prompt–completion** conversational format compatible with chat-oriented trainers such as TRL's `SFTTrainer`.

### `prompt` field

A list of role–content message dicts:

1. **System message** — the complete clinical specification for the corresponding subphase (therapist role, permitted interventions, tone constraints, phase boundaries).
2. **Historical turns** — 2–5 prior user/assistant turn pairs that provide conversational context.
3. **Current user message** — the client's most recent utterance, to which the therapist must respond.

### `completion` field

A single-element list containing one assistant message: the target therapist response.



### Example

```json
{
  "prompt": [
    {
      "role": "system",
      "content": "Eres una terapeuta de arte … [phase specification] …"
    },
    { "role": "user",      "content": "Creo que lo hice sin pensar mucho, solo fui poniendo colores." },
    { "role": "assistant", "content": "¿Y qué colores fueron apareciendo?" },
    { "role": "user",      "content": "Sobre todo azules y un poco de amarillo en el centro." },
    { "role": "assistant", "content": "Azules que llenan casi todo… y ese amarillo en el centro. Cuéntame más sobre cómo quedó esa zona central." },
    { "role": "user",      "content": "Es pequeño, pero se ve bastante. Como si estuviera ahí aunque no quisiera llamar la atención." }
  ],
  "completion": [
    {
      "role": "assistant",
      "content": "Pequeño pero presente. ¿Qué te parece si te quedas un momento mirando esa parte?"
    }
  ]
}
```

---

## Generation Pipeline

### Seed examples and few-shot anchoring

The pipeline starts from a curated set of phase-labelled input–output pairs reviewed by a licensed art therapist. These serve as ground-truth anchors for clinical tone and structure. For each generation call, **3 seed examples** from the target phase are sampled as few-shot demonstrations, consistent with findings in the synthetic data generation literature showing that small exemplar sets (2–3 instances) provide stronger distributional anchoring than larger contexts.

### Combinatorial generation strategy

Rather than sampling a fixed few-shot set per phase, the pipeline exhaustively enumerates **all $\binom{n}{3}$ combinations** of seed examples for each phase and issues one generation call per combination. This ensures every possible distributional anchor is exploited, maximising stylistic and thematic diversity across the corpus. Each call requests a batch of **10 examples**, so the total yield per phase equals 10 × (number of seed combinations).

### Single-call generation 

Each example is a self-contained conversational fragment comprising four fields: phase label, historical context window (2–5 turn pairs), client input utterance, and therapist response. All components are produced within a **single inference pass** to preserve semantic and pragmatic coherence across the multi-turn fragment. 

---

## Curation

Despite the diversity constraints embedded in the generation prompts, manual inspection of the raw corpus revealed two recurring quality issues that were addressed through a two-stage automated curation pipeline.

### Stage 1 — Intra-instance message repetition

For each instance, all therapist-side messages (historical turns + final output) and all patient-side messages (historical turns + final input) were collected separately. Pairwise textual overlap was measured using **Jaccard similarity over character-level trigrams**, and the maximum pairwise score per role was retained as the role-level repetition indicator. The instance-level score was defined as the maximum of the two role scores, yielding a single value in [0, 1] capturing worst-case internal redundancy.

Character n-grams were chosen over word-level tokens because they are language-agnostic, computationally lightweight, and sensitive to near-duplicate sentences that differ only in minor surface variation.

All instances were ranked in descending order of their repetition score. A human reviewer inspected instances from the top of this ranked list and removed those exhibiting genuine looping behaviour. Because the score decreases monotonically, the review process reaches a natural stopping point beyond which remaining instances are free of meaningful repetition.

### Stage 2 — Language leakage detection

Each instance was tokenised and normalised to lowercase; the resulting tokens were matched against a curated lexicon of common English words unlikely to appear in natural Spanish text. To minimise false positives, **cognates and loanwords orthographically identical in both languages** (e.g. *plan*, *normal*, *similar*, *control*) were explicitly excluded from the lexicon. Flagged instances were isolated for targeted review, and those confirmed to contain genuine language leakage were corrected or removed.

---

## Intended Use

This dataset is intended for **supervised fine-tuning** of a Spanish-language therapeutic dialogue model designed to support art therapists in post–art-making conversations.

### Out-of-scope uses

- Deployment as a standalone therapy tool without human clinical oversight.
- Training models intended to replace licensed therapists.
- Use cases outside Spanish-language art therapy contexts without domain adaptation.

---

## Licensing and Ethics

All content is synthetically generated. No real client data were used. Seed examples were reviewed by a licensed art therapist to ensure clinical appropriateness. Users of this dataset should ensure that any models trained on it are deployed responsibly and with appropriate human oversight in clinical or quasi-clinical contexts.

