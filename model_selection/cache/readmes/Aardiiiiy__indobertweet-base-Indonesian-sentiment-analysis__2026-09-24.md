---
widget:
- text: >-
    Gapapa kalian gak tahu band Indo ini. Tapi jangan becanda. Karena mereka
    berani menyanyikan dengan lantang bagaimana aktivis ditikam, diracun,
    dikursilitrikkan, dan dibunuh di udara. Orang-orang yang berkorban nyawa
    supaya kalian menikmati hari ini sambil ngetwit tanpa khawatir
  example_title: Example 1
  output:
  - label: Negative
    score: 0.2964
  - label: Neutral
    score: 0.067
  - label: Positive
    score: 0.6969
- text: >-
    Selama ada kelompok yg ingin jd mesias, selama itu jg govt punya justifikasi
    but bikin banyak aturan = celah korup/power abuse. Keadilan adalah
    deregulasi.
  example_title: Example 2
  output:
  - label: Negative
    score: 0.971
  - label: Neutral
    score: 0.0165
  - label: Positive
    score: 0.126
- text: >-
    saat pendukungmu oke😹 gas ✌🏽oke😹 gas ✌🏽tapi kamu malah ketawa 🤣 itu ga
    respek 😠banget wok jangan lupa makan siang 😁geratisnya wok😋😹✌🏽
  example_title: Example 3
  output:
  - label: Negative
    score: 0.6457
  - label: Neutral
    score: 0.048
  - label: Positive
    score: 0.3063
- text: >-
    Infoin loker wfh/freelance untuk mahasiswa dong, pengin bangget buat
    tambahan uang jajan di kos
  example_title: Example 4
  output:
  - label: Negative
    score: 0.0544
  - label: Neutral
    score: 0.6973
  - label: Positive
    score: 0.2482
- text: >-
    Cari kerja sekarang tuh susah. Anaknya Presiden aja mesti dicariin kerjaan
    sama bapaknya
  example_title: Example 5
  output:
  - label: Negative
    score: 0.9852
  - label: Neutral
    score: 0.0116
  - label: Positive
    score: 0.0032
- text: >-
    Komisi Penyiaran Indonesia (KPI) meminta agar tayangan televisi menampilkan
    citra positif Polri secara edukatif dan akurat. Hal ini disampaikan ketua
    KPI Pusat Ubaidillah dalam sebuah diskusi panel
  example_title: Example 6 
  output:
  - label: Neutral
    score: 0.9932
  - label: Positive
    score: 0.0063
  - label: Negative
    score: 0.0005
- text: >-
    Jgnkan tweet becandaan.. kadang tweet normal yg gue baca 'oh menarik' trs
    gue like/retweet, trs gue tinggal tidur, BESOKNYA ITU TWEET DIRUJAK. Gue jadi
    mikir, ini emang gue yang merasa semua hal menarik dan semua org bisa aja
    bener.. ATAU.. SEMUA ORANG jadi sensitif
  example_title: Example 7 
  output:
  - label: Negative
    score: 0.5531
  - label: Neutral
    score: 0.4426
  - label: Positive
    score: 0.0043

library_name: transformers
license: mit
language:
- id
---
# Model Card for Model ID

<!-- Provide a quick summary of what the model is/does. -->

## Model Details

### Model Description
This model is a fine-tuned version of [IndoBertweet-base-uncased](https://huggingface.co/indolem/indobertweet-base-uncased) for Indonesian sentiment analysis. The model is designed to classify sentiment into three categories: negative, positive, and neutral. It was trained on a diverse dataset comprising reactions from Twitter and other social media platforms, covering various topics, including politics, disasters, and education. The model is optimized using Optuna for hyperparameter tuning and evaluated using accuracy, F1-score, precision, and recall metrics.

## Bias and Limitations
Do consider that this model is trained using certain data, which may cause bias in the sentiment classification process. The model may inherit socio-cultural biases from its training data and may be less accurate for the most recent events that are not covered in the data. The limitation of the three categories may also not fully grasp the complexity of emotions, especially in capturing particular contexts. Therefore, it is important to consider and account for such biases when using this model.

## Evaluation Results
The training process uses hyperparameter optimization techniques with Optuna. The model was trained for a maximum of 10 epochs with a batch size of 16, using an optimized learning rate and weight decay. The evaluation strategy is performed every 100 steps, saving the best model based on accuracy. The training also applied early stopping with patience 3 to prevent overfitting.

<table style="text-align: center; width: 100%;">
  <tr>
    <th>Epoch</th>
    <th>Training Loss</th>
    <th>Validation Loss</th>
    <th>Accuracy</th>
    <th>F1</th>
    <th>Precision</th>
    <th>Recall</th>
  </tr>
  <tr>
    <td>100</td>
    <td>1.052800</td>
    <td>0.995017</td>
    <td>0.482368</td>
    <td>0.348356</td>
    <td>0.580544</td>
    <td>0.482368</td>
  </tr>
  <tr>
    <td>200</td>
    <td>0.893700</td>
    <td>0.807756</td>
    <td>0.730479</td>
    <td>0.703134</td>
    <td>0.756189</td>
    <td>0.730479</td>
  </tr>
  <tr>
    <td>300</td>
    <td>0.583400</td>
    <td>0.476157</td>
    <td>0.850126</td>
    <td>0.847161</td>
    <td>0.849467</td>
    <td>0.850126</td>
  </tr>
  <tr>
    <td>400</td>
    <td>0.413600</td>
    <td>0.385942</td>
    <td>0.867758</td>
    <td>0.867614</td>
    <td>0.870417</td>
    <td>0.867758</td>
  </tr>
  <tr>
    <td>500</td>
    <td>0.345700</td>
    <td>0.362191</td>
    <td>0.885390</td>
    <td>0.883918</td>
    <td>0.886880</td>
    <td>0.885390</td>
  </tr>
  <tr>
    <td>600</td>
    <td>0.245400</td>
    <td>0.330090</td>
    <td>0.897985</td>
    <td>0.897466</td>
    <td>0.897541</td>
    <td>0.897985</td>
  </tr>
  <tr>
    <td>700</td>
    <td>0.485000</td>
    <td>0.308807</td>
    <td>0.899244</td>
    <td>0.898736</td>
    <td>0.898761</td>
    <td>0.899244</td>
  </tr>
  <tr>
    <td>800</td>
    <td>0.363700</td>
    <td>0.328786</td>
    <td>0.896725</td>
    <td>0.895167</td>
    <td>0.898695</td>
    <td>0.896725</td>
  </tr>
  <tr>
    <td>900</td>
    <td>0.369800</td>
    <td>0.329429</td>
    <td>0.892947</td>
    <td>0.893138</td>
    <td>0.898281</td>
    <td>0.892947</td>
  </tr>
  <tr>
    <td>1000</td>
    <td>0.273300</td>
    <td>0.305412</td>
    <td>0.910579</td>
    <td>0.910355</td>
    <td>0.910519</td>
    <td>0.910579</td>
  </tr>
  <tr>
    <td>1100</td>
    <td>0.272800</td>
    <td>0.388976</td>
    <td>0.891688</td>
    <td>0.893113</td>
    <td>0.896606</td>
    <td>0.891688</td>
  </tr>
  <tr>
    <td>1200</td>
    <td>0.259900</td>
    <td>0.305771</td>
    <td>0.913098</td>
    <td>0.913123</td>
    <td>0.913669</td>
    <td>0.913098</td>
  </tr>
  <tr>
    <td>1300</td>
    <td>0.293500</td>
    <td>0.317654</td>
    <td>0.908060</td>
    <td>0.908654</td>
    <td>0.909939</td>
    <td>0.908060</td>
  </tr>
  <tr>
    <td>1400</td>
    <td>0.255200</td>
    <td>0.331161</td>
    <td>0.915617</td>
    <td>0.915708</td>
    <td>0.916149</td>
    <td>0.915617</td>
  </tr>
  <tr>
    <td>1500</td>
    <td>0.139800</td>
    <td>0.352545</td>
    <td>0.909320</td>
    <td>0.909768</td>
    <td>0.911014</td>
    <td>0.909320</td>
  </tr>
  <tr>
    <td>1600</td>
    <td>0.194400</td>
    <td>0.372482</td>
    <td>0.904282</td>
    <td>0.904296</td>
    <td>0.906285</td>
    <td>0.904282</td>
  </tr>
  <tr>
    <td>1700</td>
    <td>0.134200</td>
    <td>0.340576</td>
    <td>0.906801</td>
    <td>0.907110</td>
    <td>0.907780</td>
    <td>0.906801</td>
  </tr>
</table>

## Citation 
```
@misc{Ardiyanto_Mikhael_2024,
    author    = {Mikhael Ardiyanto},
    title     = {Aardiiiiy/indobertweet-base-Indonesian-sentiment-analysis},
    year      = {2024},
    URL       = {https://huggingface.co/Aardiiiiy/indobertweet-base-Indonesian-sentiment-analysis},
    publisher = {Hugging Face}
}