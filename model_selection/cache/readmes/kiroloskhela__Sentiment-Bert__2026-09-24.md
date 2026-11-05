# Emotion Analysis Model (Arabic)

This repository contains a model for emotion analysis in Arabic text. The model predicts the emotion associated with a given text input. It was developed by Kirolos Amgad Khela and trained on the Emotone dataset and the SetFit/Emotion dataset after transcribing text to Arabic.

## Model Details
- **Model type:** Text classification
- **Language(s):** Arabic
- **Finetuned from model:** MarBert

## Usage
### Direct Use
The model can be directly used for emotion analysis. It takes text inputs in Arabic and predicts the corresponding emotion associated with the text.

## Training Details
### Training Data
The model was trained using the Emotone dataset and the SetFit/Emotion dataset after translate text to Arabic.

### Training Procedure
#### Preprocessing
The training data was preprocessed by cleaning the text from English and removing punctuations.

#### Training Hyperparameters
- **Output Directory:** "train"
- **Logging Directory:** "logs"
- **Evaluation Strategy:** "epoch"
- **Per Device Train Batch Size:** 32
- **Per Device Eval Batch Size:** 32
- **Gradient Accumulation Steps:** 1
- **Number of Train Epochs:** 3
- **Learning Rate:** 3e-5
- **Warmup Ratio:** 0.1
- **Weight Decay:** 0.01
- **Adam Beta1:** 0.9
- **Adam Beta2:** 0.999
- **Adam Epsilon:** 1e-8
- **FP16:** True
- **Save Strategy:** "epoch"
- **Save Total Limit:** 3
- **Load Best Model at End:** True
- **Metric for Best Model:** "macro_f1"
- **Greater is Better:** True

## Dataset
The Emotone dataset and the SetFit/Emotion dataset are available for training. These datasets contain Arabic text annotated with emotion labels.

## Fine-tuning in Colab
To fine-tune the model on a custom dataset, you can use the provided Colab notebook. Follow the steps outlined in the notebook to upload your dataset, configure the training parameters, and start the fine-tuning process.

## Fine-tuned Model and Dataset
The fine-tuned model files and dataset are available in this [Google Drive folder](https://drive.google.com/drive/folders/1UWcBal3Myn4SipHhIX9bNpmbkQsO0Yow?usp=sharing). You can download the necessary files from this folder.

## Accuracy
The model achieved an accuracy of 82% on the evaluation dataset.

## Authors
- Kirolos Amgad Khela

## Contact
For any inquiries about the model, please contact Kirolos Amgad Khela at kirokhela5@gmail.com.
