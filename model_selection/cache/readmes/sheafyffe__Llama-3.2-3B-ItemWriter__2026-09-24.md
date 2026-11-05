---
base_model: meta-llama/Llama-3.2-3B-Instruct
library_name: peft
license: mit
language:
- en
pipeline_tag: text-generation
tags:
- personality
- psychology
- assessment
---

# Model Card for Model ID

Model trained, using DPO, to generate personality items in structured JSON format. The base architecture is [`meta-llama/Llama-3.2-3B-Instruct`](https://huggingface.co/meta-llama/Llama-3.2-3B-Instruct).

## How to Get Started with the Model

```py
# Use a pipeline as a high-level helper
from transformers import pipeline

messages = [
    {"role": "user", "content": "Write 10 items that measure conscientiousness at work."},
]
pipe = pipeline("text-generation", model="sheafyffe/Llama-3.2-3B-ItemWriter", trust_remote_code=True)
pipe(messages)
```

```py
# Load model directly
from transformers import AutoModelForCausalLM

model = AutoModelForCausalLM.from_pretrained("sheafyffe/Llama-3.2-3B-ItemWriter", trust_remote_code=True)
```

## Training Details

### Training Data

Item training data was created roughly following the generation schema:

```py
from pydantic import (BaseModel, Field)
from dataclasses import (dataclass, field)
from typing import (Any, List, Optional)
import json

class LikertItem(BaseModel):
    item_text: str = Field(description="A Likert statement representing a personality or psychological characteristic to which a person can agree or disagree")
    item_construct: str = Field(description="The personality trait or psychological characteristic an item measures")
    situational_context: Optional[str] = Field(None, description="The situation or environment the item relates to", examples = ['general', 'work', 'school', 'military'])

class MFCItem(BaseModel):
    item_text: str = Field(description="The text of a multidimensional-forced choice item", default = "Rank the following options from Most Like You (1) to Least Like You (3):")
    option_choices: List[str] = Field(description="Statements of similar social desirability that measure each of the option constructs", min_items=3, max_items=3)
    option_constructs: List[str] = Field(description="The personality trait or psychological characteristic an option choice measures", min_items=3, max_items=3)
    situational_context: Optional[str] = Field(None, description="The situation or environment the item relates to", examples = ['general', 'work', 'school', 'military'])

class SJTItem(BaseModel):
    item_text: str = Field(description="The text of a situational judgement test which includes a situation or context and a question related to that situation")
    option_choices: List[str] = Field(description="Behavioral responses or reactions to the situation described by the item text which vary in terms of degrees of the item construct", min_items=4, max_items=5)
    item_construct: str = Field(description="The personality trait or psychological characteristic an item measures")
    situational_context: Optional[str] = Field(None, description="The situation or environment the item relates to", examples = ['general', 'work', 'school', 'military'])

@dataclass
class AssessmentScale:
    ItemSchema: BaseModel
    kwargs: dict[str, Any] | None = field(default_factory=dict)

    @classmethod
    def asLikert(cls) -> 'AssessmentScale':
        return cls(ItemSchema=LikertItem)

    @classmethod
    def asMFC(cls) -> 'AssessmentScale':
        return cls(ItemSchema=MFCItem)

    @classmethod
    def asSJTScale(cls) -> 'AssessmentScale':
        return cls(ItemSchema=SJTItem)

    @property
    def schema(self) -> BaseModel:
        return self._schema
    
    def __post_init__(self):
        self._schema = create_model(
            "Assessment Scale", 
            ScaleItemList = (List[self.ItemSchema],
                             Field(description='A list or array of scale items',
                                   alias='ScaleItemList', **self.kwargs)
            )
        )
    def __str__(self):
        return json.dumps(self._schema.model_json_schema(), indent=4)
```


### Framework versions

- PEFT 0.14.0


### Model Developer

**Developed by:** Shea Fyffe