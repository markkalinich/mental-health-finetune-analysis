---
license: mit
language:
- ko
base_model:
- Jinuuuu/KoELECTRA_fine_tunning_emotion
pipeline_tag: text-classification
---

**<모델 소개>**

한국어 텍스트의 감정을 분류하기 위해 Jinuuuu님의 KoELECTRA 모델을 파인튜닝한 모델입니다.
6개의 감정 레이블(기쁨/행복, 평온/만족, 슬픔/우울, 분노/짜증, 불안/걱정, 지루/권태)을 multi-hot encoding 방식으로 분류합니다.

**<데이터>**

파인튜닝에 사용된 데이터는 AI HUB에 배포된 감성 대화 말뭉치(Single-label, Company : 미디어젠)입니다.
비상업적 목적으로 멀티 레이블 변환(수동 레이블링) 후 사용하였으며, 데이터는 재배포하지 않았습니다.

Test set 중 일부는 한국어 번역된 Reddit 및 기타 사이트의 텍스트가 포함되었습니다(전체의 10%). Test 이외의 목적으로 사용하지 않았습니다.
<table style="margin-bottom: 5px; margin-top: 5px;">
<tr><th>dataset</th><th>Amount</th></tr>
<tr><td>Train Set</td><td>2,087</td>
<tr><td>Test Set</td><td>572</td></tr>
</table>

**<레이블 매핑>**

<p style="font-size : 0.9em;">
0: 기쁨/행복 | 1: 평온/만족 | 2: 슬픔/우울 | 3: 분노/짜증 | 4: 불안/걱정 | 5: 지루/권태
</p>

**<성능>**

- Task: multi-label emotion classification

- Label representation : Multi-hot encoding

- Loss: BCEWithLogitsLoss

- Activation: Sigmoid

1. Epoch
<table style="margin-bottom: 5px; margin-top: 5px;">
<tr><th>Epoch</th><th>Training Loss</th><th>Validation Loss</th><th>F1 Macro</th><th>F1 Micro</th></tr>
<tr><td>1</td><td>0.197600</td><td>0.152192</td><td>0.868398</td><td>0.868145</td></tr>
<tr><td>2</td><td>0.100800</td><td>0.106208</td><td>0.897518</td><td>0.897767</td></tr>
<tr><td>3</td><td>0.048900</td><td>0.101381</td><td>0.898255</td><td>0.898483</td></tr>
</table>

2. Test
<table style="margin-bottom: 5px; margin-top: 5px;">
<tr><th>Metric</th><th>Value</th></tr>
<tr><td>Test Loss</td><td>0.2145</td></tr>
<tr><td>F1 Macro</td><td>0.8002</td></tr>
<tr><td>F1 Micro</td><td>0.7987</td></tr>
</table>

3. Classification Report
<table style="margin-bottom: 5px; margin-top: 5px;">
<tr><th>Class</th><th>Precision</th><th>Recall</th><th>F1-score</th><th>Support</th></tr>
<tr><td>기쁨/행복</td><td>0.79</td><td>0.82</td><td>0.81</td><td>108</td></tr>
<tr><td>평온/만족</td><td>0.79</td><td>0.77</td><td>0.78</td><td>102</td></tr>
<tr><td>슬픔/우울</td><td>0.85</td><td>0.70</td><td>0.77</td><td>114</td></tr>
<tr><td>분노/짜증</td><td>0.84</td><td>0.71</td><td>0.77</td><td>121</td></tr>
<tr><td>불안/걱정</td><td>0.91</td><td>0.76</td><td>0.83</td><td>101</td></tr>
<tr><td>지루/권태</td><td>0.93</td><td>0.77</td><td>0.84</td><td>100</td></tr>
<tr><td>micro avg</td><td>0.85</td><td>0.76</td><td>0.80</td><td>646</td></tr>
<tr><td>macro avg</td><td>0.85</td><td>0.76</td><td>0.80</td><td>646</td></tr>
<tr><td>weighted avg</td><td>0.85</td><td>0.76</td><td>0.80</td><td>646</td></tr>
<tr><td>samples avg</td><td>0.82</td><td>0.79</td><td>0.80</td><td>646</td></tr>
</table>
