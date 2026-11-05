---
library_name: openmed
license: apache-2.0
pipeline_tag: image-text-to-text
base_model: CohereLabs/North-Micro-Vision-Instruct
language:
- en
- de
- fr
- es
- it
- pt
- hi
- ja
- ko
- zh
- ar
tags:
- mlx
- openmed
- openmedkit
- apple-silicon
- ios
- on-device
- vision
- multimodal
- clinical
- medical
- privacy
- native-resolution
---

# North Micro Vision Instruct — OpenMed MLX family

Native OpenMed and OpenMedKit vision-language inference for Apple Silicon,
including local clinical-document and chart workflows on Mac, iPhone, and iPad.

These repositories contain MLX conversions of
[`CohereLabs/North-Micro-Vision-Instruct`](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct),
a compact 2.4B-parameter Cohere Compass vision-language model released under
Apache 2.0. OpenMed provides the Python and Swift runtime paths described here
and consumes the repositories as data-only model artifacts.

The same byte-identical README is published across all five precision
variants. The repository name, `config.json`, and `openmed-mlx.json` identify
the precision.

## Choose a precision

| Repository | Weight payload | Intended trade-off |
| --- | ---: | --- |
| [`OpenMed/North-Micro-Vision-Instruct-4bit-mlx`](https://huggingface.co/OpenMed/North-Micro-Vision-Instruct-4bit-mlx) | 2.02 GiB | Smallest affine variant; validate quality on your document set |
| [`OpenMed/North-Micro-Vision-Instruct-5bit-mlx`](https://huggingface.co/OpenMed/North-Micro-Vision-Instruct-5bit-mlx) | 2.25 GiB | Compact middle ground |
| [`OpenMed/North-Micro-Vision-Instruct-6bit-mlx`](https://huggingface.co/OpenMed/North-Micro-Vision-Instruct-6bit-mlx) | 2.48 GiB | Recommended first quality/size trial |
| [`OpenMed/North-Micro-Vision-Instruct-8bit-mlx`](https://huggingface.co/OpenMed/North-Micro-Vision-Instruct-8bit-mlx) | 2.93 GiB | Higher-fidelity quantized variant |
| [`OpenMed/North-Micro-Vision-Instruct-bf16-mlx`](https://huggingface.co/OpenMed/North-Micro-Vision-Instruct-bf16-mlx) | 4.63 GiB | Full converted-precision reference |

The 4/5/6/8-bit repositories use 64-element affine weight groups. Their
vision tower remains in source precision; eligible language-model layers are
quantized. This preserves the source visual encoder for OCR and document work
while reducing the decoder footprint.

## Python through OpenMed

Install OpenMed with Apple MLX support:

```bash
uv pip install "openmed[mlx]"
```

Image plus text:

```python
from openmed.mlx import OpenMedMLXVisionLanguageModel

model = OpenMedMLXVisionLanguageModel(
    "OpenMed/North-Micro-Vision-Instruct-6bit-mlx"
)

result = model.generate_with_metadata(
    "Read this synthetic document and list the visible medication and dose.",
    image="synthetic-clinical-note.png",
    max_tokens=128,
)

print(result.text)
print(result.prompt_tokens, result.generation_tokens)
```

Text-only generation uses the same loaded model:

```python
response = model.generate(
    "Explain why local processing can improve clinical-document privacy.",
    max_tokens=96,
)
```

Pass a local artifact directory instead of the Hub repository ID for a fully
offline deployment. OpenMed validates the Compass artifact, loads weights
strictly, applies the bundled chat template, performs native-resolution image
processing, and generates with MLX. It never enables remote model code.

## Swift and iOS through OpenMedKit

OpenMedKit implements Cohere Compass directly in Swift on MLX. Add the tested
OpenMed branch until the implementation is merged and included in a tagged
release:

```swift
dependencies: [
    .package(
        url: "https://github.com/maziyarpanahi/openmed.git",
        branch: "feature/cohere-compass-runtime"
    ),
]
```

Load from Hugging Face and ask a question about a local image:

```swift
import OpenMedKit

let model = try await OpenMedVisionLanguageModel.load(
    modelID: "OpenMed/North-Micro-Vision-Instruct-6bit-mlx"
)

let result = try await model.generate(
    "List the visible medication and dose.",
    imageURL: clinicalDocumentURL,
    maxTokens: 128
)

print(result.text)
```

For a bundled, app-managed, or air-gapped artifact:

```swift
let model = try await OpenMedVisionLanguageModel.load(
    modelDirectory: localModelDirectory
)
```

`OpenMedVisionLanguageGeneration` exposes decoded text, generated token IDs,
prompt/generation token counts, and timing. Overloads support text-only input,
`CIImage`, a local image URL, or multiple `UserInput.Image` values.

The initial Hub download is a network operation. Prompt and image inference is
local after the artifact is cached, with no telemetry and no cloud inference
fallback. For PHI workflows, pre-download or bundle the model before intake,
keep raw documents out of logs and analytics, and apply OpenMedKit privacy
policies before an explicitly authorized export.

Implementation and review status: [OpenMed PR #2885](https://github.com/maziyarpanahi/openmed/pull/2885)

## Why this model fits OpenMedKit

North Micro Vision accepts interleaved text and images, preserves native image
aspect ratios, and was trained for OCR, document understanding, charts,
grounding, captioning, multilingual prompts, and multi-image conversations.
That maps naturally to a privacy-first OpenMedKit pipeline:

1. Capture or import a page locally on iPhone, iPad, or Mac.
2. Run image normalization and VLM inference on the device.
3. Validate names, identifiers, medications, measurements, and other generated
   fields against the source page.
4. Redact or pseudonymize with OpenMedKit policies before any authorized
   disclosure.
5. Preserve provenance and require human review before consequential use.

Local inference reduces a network boundary; it does not make generated content
automatically safe or correct. Never auto-trigger diagnosis, treatment,
disclosure, or another consequential clinical action from model output.

## OpenMed runtime validation

Before the runtime and cards were published, every precision was loaded
independently and run through the same synthetic suite in both native runtimes:

- Python: `OpenMedMLXVisionLanguageModel`, strict safetensors loading;
- Swift: `OpenMedVisionLanguageModel` in an Xcode Metal-backed test bundle;
- coherent deterministic text-only privacy explanation;
- exact `Tuesday` extraction from a short synthetic note;
- correct name, synthetic record ID, medication, dose, frequency, and allergy
  extraction from a generated clinical-document image;
- exact `Screening, 42` extraction from a generated chart image;
- tokenizer/chat-template and prompt-token-count parity;
- native image resize, patch-grid, visual-token, and multimodal decode checks;
- macOS execution for all five payloads and an iOS device-target build gate.

The Python and Swift tests use the same prompts, image fixtures, token counts,
and clinical fact acceptance criteria. Canonical fact and chart answers are
also token-exact. Free-form sentences can choose equivalent near-tied tokens
across MLX language bindings, so those are checked for coherence and required
facts instead of brittle punctuation or wording.

`openmed-runtime-validation.json` records the OpenMed runtime gates for this
variant. `openmed-validation.json` preserves the original conversion and
independent-reference certificate. Those fixtures are synthetic and are not
clinical-quality evidence.

## Artifact contract

Each repository is data-only and includes:

- `model.safetensors` plus its index;
- `config.json` with `model_type: cohere_compass`;
- tokenizer, chat-template, and generation configuration;
- native-resolution image processor configuration;
- `openmed-mlx.json` runtime/precision metadata;
- OpenMed conversion and native-runtime validation reports.

No conversion-time Python package or executable model code is stored in the
repository. Both OpenMed runtimes consume the same artifact payload.

## Scope and limitations

The source model supports visual question answering, grounding, OCR, document
and chart understanding, multilingual prompts, and multiple images. Cohere
reports multimodal training and validation up to 8K tokens; do not silently
claim longer multimodal reliability.

The source model is not a reasoning model, has limited math and code ability,
does not support tool calling, and is intended as a compact foundation for
prototyping and specialization. Native-resolution images can materially
increase memory use, latency, and thermal pressure on mobile devices. Measure
the exact precision, image sizes, and sustained workload on each target device.

This model and OpenMedKit are not medical devices. Outputs can be incomplete,
incorrect, or fabricated. A qualified human must verify consequential use.

## Reproducibility and credits

- Source: [`CohereLabs/North-Micro-Vision-Instruct`](https://huggingface.co/CohereLabs/North-Micro-Vision-Instruct)
- Pinned source revision: `373bda96ac70bf89f99f7048f420cf00dc07c149`
- OpenMed / OpenMedKit: [github.com/maziyarpanahi/openmed](https://github.com/maziyarpanahi/openmed)

Thank you to Cohere for releasing North Micro Vision and to the Apple MLX
contributors who make private on-device inference possible.

The converted weights retain the source model's Apache 2.0 license. OpenMed's
SDK source is separately licensed under Apache 2.0.
