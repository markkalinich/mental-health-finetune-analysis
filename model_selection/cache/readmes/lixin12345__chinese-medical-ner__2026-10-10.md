
### Usage

```python

from transformers import AutoTokenizer, AutoModelForTokenClassification
import torch

class NER:
    """
    实体命名实体识别
    """
    def __init__(self,model_path) -> None:
        """
        Args:
            model_path:模型地址
        """

        self.model_path = model_path
        self.tokenizer = AutoTokenizer.from_pretrained(model_path)
        self.model = AutoModelForTokenClassification.from_pretrained(model_path)

    def ner(self,sentence:str) -> list:
        """
        命名实体识别
        Args:
            sentence:要识别的句子
        Return:
            实体列表:[{'type':'LOC','tokens':[...]},...]
        """
        ans = []
        for i in range(0,len(sentence),500):
            ans = ans + self._ner(sentence[i:i+500])
        return ans
    
    def _ner(self,sentence:str) -> list:
        if len(sentence) == 0: return []
        inputs = self.tokenizer(
            sentence, add_special_tokens=True, return_tensors="pt"
        )
        
        if torch.cuda.is_available():
            self.model = self.model.to(torch.device('cuda:0'))
            for key in inputs:
                inputs[key] = inputs[key].to(torch.device('cuda:0'))
            
        with torch.no_grad():
            logits = self.model(**inputs).logits
        predicted_token_class_ids = logits.argmax(-1)
        predicted_tokens_classes = [self.model.config.id2label[t.item()] for t in predicted_token_class_ids[0]]
        entities = []
        entity = {}
        for idx, token in enumerate(self.tokenizer.tokenize(sentence,add_special_tokens=True)):
            if 'B-' in predicted_tokens_classes[idx] or 'S-' in predicted_tokens_classes[idx]:
                if len(entity) != 0:
                    entities.append(entity)
                entity = {}
                entity['type'] = predicted_tokens_classes[idx].replace('B-','').replace('S-','')
                entity['tokens'] = [token]
            elif 'I-' in predicted_tokens_classes[idx] or 'E-' in predicted_tokens_classes[idx] or 'M-' in predicted_tokens_classes[idx]:
                if len(entity) == 0:
                    entity['type'] = predicted_tokens_classes[idx].replace('I-','').replace('E-','').replace('M-','')
                    entity['tokens'] = []
                entity['tokens'].append(token)
            else:
                if len(entity) != 0:
                    entities.append(entity)
                    entity = {}
        if len(entity) > 0:
            entities.append(entity)
        return entities

ner_model = NER('lixin12345/chinese-medical-ner')
text = """
患者既往慢阻肺多年;冠心病史6年，平素规律服用心可舒、保心丸等控制可;双下肢静脉血栓3年，保守治疗效果可;左侧腹股沟斜疝无张力修补术后2年。否认"高血压、糖尿病"等慢性病病史，否认"肝炎、结核"等传染病病史及其密切接触史，否认其他手术、重大外伤、输血史，否认"食物、药物、其他"等过敏史，预防接种史随社会。
"""
ans = ner_model.ner(text)
# ans

# DiseaseNameOrComprehensiveCertificate
# 慢阻肺

# DiseaseNameOrComprehensiveCertificate
# 冠心病

# Drug
# 心可舒

# Drug
# 保心丸

# DiseaseNameOrComprehensiveCertificate
# 双下肢静脉血栓

# DiseaseNameOrComprehensiveCertificate
# 左侧腹股沟斜疝

# TreatmentOrPreventionProcedures
# 无张力修补术

# DiseaseNameOrComprehensiveCertificate
# 高血压

# DiseaseNameOrComprehensiveCertificate
# 糖尿病

# DiseaseNameOrComprehensiveCertificate
# 肝炎

# DiseaseNameOrComprehensiveCertificate
# 结核
```

### Source

From hit [wi](https://wi.hit.edu.cn/gk.htm) 

---
license: apache-2.0
---
