# TinyLlama Model (ONNX Fixed)

This model has been fixed to work with @xenova/transformers without ONNX dependencies.

## Model ID
`thejefferson29/therapy-ai-tinyllama-fixed`

## Changes Made
- Disabled ONNX dependencies
- Updated configuration files
- Optimized for @xenova/transformers compatibility

## Usage
```javascript
const { pipeline } = require('@xenova/transformers');

const generator = await pipeline(
    'text-generation',
    'thejefferson29/therapy-ai-tinyllama-fixed',
    {
        device: 'cpu',
        dtype: 'float32',
        use_onnx: false
    }
);
```

## Files
- `config.json`: Model configuration (ONNX disabled)
- `tokenizer_config.json`: Tokenizer configuration
- `generation_config.json`: Generation parameters
- `special_tokens_map.json`: Special tokens mapping
- `model.safetensors`: Model weights
- `tokenizer.json`: Tokenizer vocabulary
