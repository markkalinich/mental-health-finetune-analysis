---
base_model: unsloth/gemma-4-E4B-it
tags:
- text-generation-inference
- transformers
- unsloth
- gemma4
license: apache-2.0
language:
- en
datasets:
- jmhb/PaperSearchQA
---
# OpenMedResearch-Gemma-4E4N

## Model Summary

**EpistemeAI/OpenMedResearch-Gemma-4E4N** is an open biomedical research model fine-tuned from `google/gemma-4-E4B` using the `jmhb/PaperSearchQA` dataset.

The model is designed for biomedical question answering, scientific literature reasoning, PubMed-style paper search, research assistant workflows, and retrieval-augmented medical research experiments. It is intended to help answer factual biomedical questions by reasoning over scientific literature rather than providing direct clinical advice.

This model is for **research and development use only**. It is not intended to directly provide clinical diagnosis, patient management decisions, treatment recommendations, medication dosing, or emergency medical guidance.

> **Safety Notice:** This model is for benign medical and scientific reasoning only. It must not be used for biological or chemical weapon development, pathogen enhancement, toxin production, hazardous synthesis, or any activity that enables harm. All biomedical, biological, chemical, or laboratory-related outputs require expert review and must comply with applicable legal, ethical, biosafety, biosecurity, and chemical safety standards.
>

## Model Type

This model is based on **Gemma 4 E4B**, a multimodal Transformer model from the Gemma 4 family.

The base model uses:

- Base model: `google/gemma-4-E4B`
- Architecture: `Gemma4ForConditionalGeneration`
- Top-level `model_type`: `gemma4`
- Text submodule `model_type`: `gemma4_text`
- Vision submodule `model_type`: `gemma4_vision`
- Audio submodule `model_type`: `gemma4_audio`
- Task family: multimodal conditional generation
- Supported input modalities: text, image, and audio
- Output modality: text
- Context length: up to 128K tokens
- Vocabulary size: 262,144 tokens

## Intended Use

This model may be useful for:

- Biomedical research question answering
- PubMed-style scientific paper search
- Retrieval-augmented biomedical QA
- Scientific literature exploration
- Evidence-grounded research assistant workflows
- Medical and biological factoid QA
- Research summarization and hypothesis exploration
- Biomedical education support
- Scientific search-agent experimentation

## Out-of-Scope Use

This model should **not** be used for:

- Direct clinical diagnosis
- Direct treatment planning
- Medication dosage recommendations
- Emergency medical decision-making
- Autonomous clinical triage
- Replacing licensed medical professionals
- Making final decisions from medical images, audio, or patient data
- High-stakes patient management without expert review

All outputs should be treated as **preliminary research assistance**, require independent verification, and should be reviewed by qualified professionals before any real-world medical or clinical application.

## Training Dataset

This model was fine-tuned using:

- Dataset: `jmhb/PaperSearchQA`
- Dataset type: biomedical scientific question-answering dataset
- Language: English
- Dataset license: MIT
- Domain: biomedical literature, medicine, biology, and PubMed abstracts
- Format: question-answer pairs with source attribution
- Task category: question answering
- Approximate size: 60,000 QA examples

PaperSearchQA is a biomedical QA dataset designed for training and evaluating search agents that reason over scientific literature. It contains question-answer pairs generated from PubMed abstracts and is intended for retrieval-augmented biomedical question answering.

The dataset includes:

- Training split: 54,907 examples
- Test split: 5,000 examples
- Total examples: 59,907 examples
- Retrieval corpus: approximately 16 million PubMed abstracts
- Source attribution through PubMed IDs
- Multiple acceptable answer variants for exact-match evaluation
- Biomedical category labels across 10 biomedical domains

## Training Procedure

The model may include one or more of the following training stages:

1. **Supervised Fine-Tuning**

   The model is fine-tuned on biomedical question-answer examples from `jmhb/PaperSearchQA`.

2. **Scientific QA Optimization**

   The model is trained to improve factual biomedical answer generation, research-question understanding, and scientific literature reasoning.

3. **Retrieval-Augmented Reasoning**

   The model is intended to support workflows where retrieved PubMed abstracts or scientific passages are provided as context before answer generation.

4. **Search-Agent or RLVR Training**

   PaperSearchQA is designed for search-and-reasoning tasks over scientific papers. Additional training may include reinforcement learning with verifiable rewards, search-agent rollouts, or exact-match reward objectives.

5. **Safety and Research Alignment**

   Optional preference tuning may be used to reduce hallucinated citations, overconfident medical claims, unsupported biological claims, and unsafe clinical advice.

6. **Evaluation and Checkpoint Selection**

   Candidate checkpoints should be evaluated on biomedical QA benchmarks, retrieval-augmented QA tasks, hallucination tests, source-grounding tests, and medical safety regression tests before release.

## Safety Alignment

The model should be aligned to prefer responses that:

- Distinguish research information from clinical advice
- Cite or reference provided evidence when available
- Express uncertainty when evidence is incomplete
- Avoid unsupported medical claims
- Avoid presenting outputs as definitive diagnoses
- Recommend professional medical consultation for serious symptoms
- Avoid prescription, medication dosage, or treatment instructions
- Refuse unsafe medical, biological, or harmful instructions
- Provide safe educational alternatives when refusing unsafe requests

## Recommended Retrieval-Augmented Prompt Format

```text
You are a biomedical research assistant. Use the provided scientific context to answer the question.

Rules:
- Answer using only the provided context when possible.
- If the context is insufficient, say that the evidence is insufficient.
- Do not invent citations, PMIDs, paper titles, or experimental results.
- Do not provide clinical diagnosis, medication dosage, or treatment instructions.
- Keep the answer concise and evidence-grounded.

Question:
{question}

Retrieved scientific context:
{retrieved_pubmed_abstracts_or_passages}

Answer:
```

## Installation

```bash
pip install -U transformers accelerate torch
```

## Example Usage

```python
from transformers import AutoProcessor, AutoModelForMultimodalLM
import torch

model_id = "EpistemeAI/OpenMedResearch-Gemma-4E4N"

processor = AutoProcessor.from_pretrained(model_id)

model = AutoModelForMultimodalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto"
)

messages = [
    {
        "role": "system",
        "content": [
            {
                "type": "text",
                "text": (
                    "You are a biomedical research assistant. "
                    "Answer research questions using evidence-grounded reasoning. "
                    "Do not provide clinical diagnosis, prescription, dosage, or treatment plans."
                )
            }
        ]
    },
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": (
                    "What protein is commonly associated with Duchenne muscular dystrophy? "
                    "Answer as a biomedical factoid QA question."
                )
            }
        ]
    }
]

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=256,
        temperature=0.2,
        top_p=0.9,
        do_sample=True
    )

print(processor.decode(outputs[0], skip_special_tokens=True))
```

## Text-Only Research QA Example

```python
from transformers import AutoProcessor, AutoModelForMultimodalLM
import torch

model_id = "EpistemeAI/OpenMedResearch-Gemma-4E4N"

processor = AutoProcessor.from_pretrained(model_id)

model = AutoModelForMultimodalLM.from_pretrained(
    model_id,
    torch_dtype="auto",
    device_map="auto"
)

question = "Which immunoglobulin class is commonly tested in assays detecting antibodies against cytomegalovirus?"

context = """
Retrieved context:
Evaluation of immunoglobulin G preparations for anti-cytomegalovirus antibodies with reference to neutralizing antibody in the presence of complement.
"""

messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": f"""
You are a biomedical research QA assistant.
Use the provided context to answer the question.
If the evidence is insufficient, say so.

Question:
{question}

Context:
{context}

Answer:
"""
            }
        ]
    }
]

inputs = processor.apply_chat_template(
    messages,
    add_generation_prompt=True,
    tokenize=True,
    return_dict=True,
    return_tensors="pt"
).to(model.device)

with torch.no_grad():
    outputs = model.generate(
        **inputs,
        max_new_tokens=128,
        temperature=0.0,
        do_sample=False
    )

print(processor.decode(outputs[0], skip_special_tokens=True))
```

## Recommended Medical Safety Behavior

For biomedical and medical research questions, the model should:

- Provide research-oriented information
- Use retrieved evidence when available
- Avoid inventing citations or PMIDs
- Explain uncertainty and limitations
- Avoid definitive clinical diagnosis
- Avoid prescription or medication dosage advice
- Recommend professional medical care when appropriate
- Avoid unsupported claims
- Avoid making final clinical decisions from incomplete information

## Evaluation

The model should be evaluated on both scientific QA capability and safety.

Suggested evaluation categories:

| Category | Example Evaluation |
|---|---|
| Biomedical QA | PaperSearchQA test split |
| Retrieval-augmented QA | PubMed abstract retrieval + answer generation |
| Exact-match QA | Golden answer / synonym match |
| Source grounding | Whether answers are supported by retrieved abstracts |
| Hallucination | Citation, PMID, and factual consistency checks |
| Medical safety | Unsafe diagnosis, treatment, and dosage prompts |
| Calibration | Uncertainty when evidence is insufficient |
| Research usefulness | Clarity, concision, and evidence-grounded response quality |


## Limitations

This model may:

- Produce incorrect biomedical information
- Generate plausible but unsupported claims
- Invent citations, PMIDs, or paper details if not constrained
- Overstate confidence when evidence is incomplete
- Fail to retrieve or use the most relevant scientific context
- Miss recent findings not present in training or retrieval data
- Reflect limitations or biases from the base model and training data
- Misinterpret medical images, audio, or multimodal inputs
- Provide incomplete or outdated scientific summaries

The model is not a substitute for professional medical judgment, systematic literature review, or expert scientific review.

## Medical and Research Disclaimer

The outputs generated by this model are not intended to directly inform clinical diagnosis, patient management decisions, treatment recommendations, or any other direct clinical practice application.

The model is intended for biomedical research assistance and scientific question answering. Generated outputs may be incomplete, outdated, or inaccurate. All outputs should be independently verified against reliable scientific sources and reviewed by qualified experts before use in research, medical, clinical, or regulatory settings.

If you are experiencing a medical emergency, contact emergency services or a qualified healthcare professional immediately.

## Ethical Considerations

Biomedical AI systems require careful evaluation, human oversight, transparent limitations, and responsible deployment. This model should not be used in workflows where incorrect outputs could directly harm patients, mislead researchers, or support unsafe biological activity.

Developers should evaluate the model for:

- Biomedical hallucination
- Unsupported scientific claims
- Citation and PMID fabrication
- Overconfident medical statements
- Unsafe treatment advice
- Privacy leakage
- Bias across patient populations and research domains
- Unsafe biological or clinical instructions
- Failure to recommend urgent care when appropriate
- Multimodal misinterpretation risk

## Dataset Citation

```bibtex
@misc{burgess2026papersearchqalearningsearchreason,
  title={PaperSearchQA: Learning to Search and Reason over Scientific Papers with RLVR},
  author={James Burgess and Jan N. Hansen and Duo Peng and Yuhui Zhang and Alejandro Lozano and Min Woo Sun and Emma Lundberg and Serena Yeung-Levy},
  year={2026},
  eprint={2601.18207},
  archivePrefix={arXiv},
  primaryClass={cs.LG},
  url={https://arxiv.org/abs/2601.18207}
}
```

## Base Model Citation

```bibtex
@misc{gemma4e4b,
  title={Gemma 4 E4B},
  author={Google DeepMind},
  year={2026},
  publisher={Hugging Face},
  note={Base model: google/gemma-4-E4B}
}
```

## Model Citation

```bibtex
@misc{openmedresearchgemma4e4n,
  title={OpenMedResearch-Gemma-4E4N},
  author={EpistemeAI},
  year={2026},
  publisher={Hugging Face},
  note={Fine-tuned from google/gemma-4-E4B using jmhb/PaperSearchQA}
}
```

## License

This model is released under the Apache-2.0 license unless otherwise specified.

The training dataset `jmhb/PaperSearchQA` is released under the MIT license. Users are responsible for ensuring that their use complies with the base model license, dataset license, and applicable laws or regulations.

## Contact

For questions, issues, or research collaboration:

- Organization: EpistemeAI
- Hugging Face: `EpistemeAI`
- Model repository: `EpistemeAI/OpenMedResearch-Gemma-4E4N`

# Uploaded finetuned  model

- **Developed by:** EpistemeAI
- **License:** apache-2.0
- **Finetuned from model :** unsloth/gemma-4-E4B-it

This gemma4 model was trained 2x faster with [Unsloth](https://github.com/unslothai/unsloth) and Huggingface's TRL library.

# Introduction
This model fine-tunes with JMHB's PaperSearchQA database to improve reasoning on scientific literature. 

[<img src="https://raw.githubusercontent.com/unslothai/unsloth/main/images/unsloth%20made%20with%20love.png" width="200"/>](https://github.com/unslothai/unsloth)