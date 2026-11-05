# TinyLlama Model (ONNX-Free)

This model has been completely stripped of ONNX dependencies to work with @xenova/transformers.

## Model ID
`thejefferson29/therapy-ai-tinyllama-onnx-free`

## Changes Made
- Completely removed ONNX dependencies
- Updated all configuration files
- Optimized for @xenova/transformers compatibility
- No ONNX runtime required

## Usage
```javascript
const { pipeline } = require('@xenova/transformers');

const generator = await pipeline(
    'text-generation',
    'thejefferson29/therapy-ai-tinyllama-onnx-free',
    {
        device: 'cpu',
        dtype: 'float32',
        use_onnx: false
    }
);
```

## Files
- `config.json`: Model configuration (ONNX-free)
- `tokenizer_config.json`: Tokenizer configuration (ONNX-free)
- `generation_config.json`: Generation parameters (ONNX-free)
- `special_tokens_map.json`: Special tokens mapping (ONNX-free)
- `model.safetensors`: Model weights
- `tokenizer.json`: Tokenizer vocabulary
- `chat_template.jinja`: Chat template

## Compatibility
- ✅ @xenova/transformers
- ✅ Node.js
- ✅ Render.com
- ❌ ONNX Runtime (not needed)
