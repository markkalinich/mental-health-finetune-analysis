---
base_model: unsloth/gemma-3-4b-it-unsloth-bnb-4bit
tags:
- text-generation-inference
- transformers
- unsloth
- gemma3
license: apache-2.0
language:
- en
---

# Uploaded finetuned  model

This repository contains a Gemma 3 4B model fine-tuned to generate radiology reports from ultrasound images. It was trained using the Unsloth library and is provided here in GGUF format for use with `llama.cpp`.

This model card demonstrates a complete, end-to-end example of running inference using `llama.cpp` and the `llama_cpp_dart` package.

- **Base Model:** [unsloth/gemma-3-4b-it-unsloth-bnb-4bit](https://huggingface.co/unsloth/gemma-3-4b-it-unsloth-bnb-4bit)
- **Fine-tuning Data:** [unsloth/Radiology_mini](https://huggingface.co/datasets/unsloth/Radiology_mini)

## Example Usage

This example uses the `llama_cpp_dart` package to run the model on a macOS machine with Metal GPU acceleration.

### 1. Input Image

The following ultrasound image (`radiology.png`) was used as input.

![Ultrasound Image](radiology.png)

### 2. Dart Inference Code

The model was called using the code below. Note the use of `ChatFormat.gemma`, which correctly applies the `<bos><start_of_turn>user...` template required by the model.

```dart
import 'dart:io';
import 'package:llama_cpp_dart/llama_cpp_dart.dart';

Future<void> main() async {
  Llama.libraryPath = "bin/MAC_ARM64/libmtmd.dylib";

  final modelParams = ModelParams()..nGpuLayers = -1;

  final contextParams = ContextParams()
    ..nPredict = 512
    ..nCtx = 8192
    ..nBatch = 8192;

  final samplerParams = SamplerParams()
    ..temp = 0.0
    ..topK = 64
    ..topP = 0.95
    ..penaltyRepeat = 1.1
    ..addStopSequence("<end_of_turn>");

  final llama = Llama(
      "./model-radiology-Q4_K_M.gguf",
      modelParams,
      contextParams,
      samplerParams,
      false,
      "./mmproj-radiology.gguf");

  final image =
      LlamaImage.fromFile(File("./radiology.png"));

  final chat = ChatHistory();
  chat.addMessage(role: Role.user, content: """<image>
      You are an expert radiographer. Describe accurately what you see in this image.""");
  
  // Use the correct chat format that matches the fine-tuning process
  final prompt =
      chat.exportFormat(ChatFormat.gemma, leaveLastAssistantOpen: true);

  print("==== PROMPT SENT TO MODEL ====");
  print(prompt);
  print("==============================");

  final sw = Stopwatch()..start();
  try {
    final stream = llama.generateWithMeda(prompt, inputs: [image]);

    await for (final token in stream) {
      stdout.write(token);
    }
    await stdout.flush();
    stdout.writeln();
  } on LlamaException catch (e) {
    stderr.writeln("An error occurred: $e");
  } finally {
    sw.stop();
    stdout.writeln('⏱️  Inference time: ${sw.elapsed}');
    llama.dispose();
  }
}
```

# Outputs
*   **Image Type:** Transvaginal ultrasound
*   **Date:** 10-05-2012
*   **Measurement:** 40mm
*   **Findings:**
    *   A large, heterogeneous, cystic mass is seen in the right adnexa.
    *   The mass appears to be connected to the ovary.
    *   The mass is 40mm in diameter.
    *   The right ovary is 62.7 mm in diameter.
    *   The left ovary is 125/255 mm in diameter.
    *   The uterus is 3D5-8EK.
    *   The uterine body is 11:36:15.
    *   The uterine tube is 0.2.