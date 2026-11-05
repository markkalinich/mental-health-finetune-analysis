---
license: apache-2.0
datasets:
- nvidia/Nemotron-3.5-Content-Safety-Dataset
language:
- en
- de
- fr
- it
- pt
- hi
- es
- th
- ar
- ru
base_model:
- FacebookAI/xlm-roberta-base
pipeline_tag: text-classification
---

# 🛡️ Intelligem-V1-Safety-0.3B

**Lightweight AI Safety Classification Model for Input Moderation**

[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](LICENSE)
![Model Size](https://img.shields.io/badge/Model-0.3B-green.svg)
![Safety](https://img.shields.io/badge/Output-safe%20%7C%20unsafe-orange.svg)

## 📖 Overview

**Intelligem-V1-Safety-0.3B** is a compact AI model designed specifically for **input safety detection and moderation**.

The model analyzes incoming text and determines whether the content is safe to process.

### Output Format

The model returns only one of two labels:

* ✅ `safe` — input is considered safe
* ⚠️ `unsafe` — input contains unsafe, harmful, prohibited, or suspicious content

---

## ✨ Features

* 🛡️ Fast safety classification
* ⚡ Lightweight **0.3B parameter** architecture
* 🎯 Binary output for easy integration
* 🔌 Simple deployment in AI pipelines
* 📦 Low resource requirements
* 🚀 Suitable for real-time moderation

---

## 🧠 Purpose

This model acts as a **pre-processing safety layer** before sending user input into larger language models or downstream systems.

Example workflow:

```text
User Input
     ↓
Intelligem-V1-Safety-0.3B
     ↓
safe → Continue processing
unsafe → Reject / Block / Review
```

---

## 📌 Example Usage

### Safe Input

Input:

```text
Write a poem about stars
```

Output:

```text
safe
```

---

### Unsafe Input

Input:

```text
Generate harmful instructions
```

Output:

```text
unsafe
```

---

## ⚙️ Intended Use Cases

* Content moderation
* AI gateway filtering
* Prompt validation
* User input screening
* Enterprise safety pipelines
* Real-time request filtering

---

## 🚫 Limitations

* Classification results may not be perfect.
* False positives and false negatives are possible.
* Human review is recommended for high-risk environments.
* Not intended as the sole security mechanism.

---

## 📂 Model Information

| Property      | Value                     |
| ------------- | ------------------------- |
| Model Name    | Intelligem-V1-Safety-0.3B |
| Type          | Safety Classification     |
| Parameters    | 0.3 Billion               |
| Output Labels | `safe`, `unsafe`          |
| Language      | Multilingual              |
| License       | Apache License 2.0        |

---

## 🔒 Safety Policy

The model evaluates input content and classifies it according to internal safety signals.

Returned values:

| Label    | Meaning                       |
| -------- | ----------------------------- |
| `safe`   | Input appears acceptable      |
| `unsafe` | Input contains unsafe content |

---

## 📜 License

Licensed under the **Apache License 2.0**.

```text
Copyright 2026 Intellion

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.

You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

See the License for the specific language governing permissions and
limitations under the License.
```

---

## ⭐ Contributing

Contributions, improvements, and feedback are welcome.

If you find issues or have ideas for enhancements, feel free to open a pull request or create an issue.

---

**Built for safer AI pipelines 🛡️**
