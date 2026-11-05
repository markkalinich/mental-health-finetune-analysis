---
license: mit
---
NOTICE:  
our training and benchmark both implemented on block size 8,  
which is equivalent to num_speculative_tokens=8 of vllm

# 1 Results(accept_length)  
| domain | dataset | qwen3-4b-dspark (ours) | qwen3-4b-dflash2 (ours) | qwen3-4b-dflash2 (reference)  |
|---|---|---:|---:|---:|
| math | gsm8k | 6.00 | 6.14 | 6.09 |
| math | math500 | 5.67 | 5.80 | 5.67 |
| math | aime25 | 5.19 | 5.32 | 5.18 |
| code | mbpp | 5.04 | 5.14 | 5.07 |
| code | human eval | 5.26 | 5.38 | 5.25 |
| code | live code bench（LCB） | 4.66 | 4.79 | 4.58 |
| chat | ceval | 3.58 | 3.59 | 3.57 |
| chat | mt-bench | 4.21 | 4.14 | 4.16 |
| chat | alpaca | 2.61 | 2.50 | 2.53 |
| chat | arena hard | 4.18 | 4.18 | 4.15 |  

ours qwen3-4b-dflash2 according to：https://huggingface.co/AQ-MedAI/Qwen3-4B-DFlash2  
reference qwen3-4b-dflash2 according to：https://huggingface.co/RedHatAI/Qwen3-4B-speculator.dflash2

# 2 Reproduce
## 2-1 train
### 2-1-1 enviornment
according to https://github.com/vllm-project/speculators/commit/7a58fc56217632d8d179b665734fa2269e8d9ffa#diff-c94e7047d3ac690b5a75e602e6ff745ec3156a87df40160f5a5c73001ac0184b 
```bash
git clone https://github.com/vllm-project/speculators.git
cd speculators
git checkout 7a58fc56217632d8d179b665734fa2269e8d9ffa
pip install -e .
```

### 2-1-2 dataset 
according to https://modelscope.cn/datasets/inference-optimization/Qwen3-8B-Regenerated-Collection 
```bash
modelscope download --dataset inference-optimization/Qwen3-8B-Regenerated-Collection --local_dir /path/dataset/Qwen3-8B-Regenerated-Collection
```

### 2-1-3 script
```shell
#!/bin/bash

set -euo pipefail

REPO_DIR="/speculators"
MODEL="/path/model/Qwen3-4B"

DATA_DIR="/path/dataset/qwen3_8b_regen"
DATASETS=(
    "$DATA_DIR/autoif_train_Qwen3-8B.jsonl"
    "$DATA_DIR/evol_codealpaca_train_Qwen3-8B.jsonl"
    "$DATA_DIR/lmsys_arena_train_Qwen3-8B.jsonl"
    "$DATA_DIR/magpie_output.jsonl"
    "$DATA_DIR/metamathqa_train_Qwen3-8B.jsonl"
    "$DATA_DIR/nemotron_chat_Qwen3-8B.jsonl"
    "$DATA_DIR/nemotron_stem_Qwen3-8B.jsonl"
    "$DATA_DIR/orca_math_train_Qwen3-8B.jsonl"
    "$DATA_DIR/tulu3_Qwen3-8B.jsonl"
    "$DATA_DIR/ultrachat_output.jsonl"
    "$DATA_DIR/ultrafeedback_train_sft_Qwen3-8B.jsonl"
    "$DATA_DIR/ultrainteract_train_Qwen3-8B.jsonl"
)

OUTPUT_DIR="$REPO_DIR/output/dspark_qwen3_4b_8spec"
SAVE_PATH="/path/ckpt/speculators/dspark_qwen3_4b/checkpoints"
HIDDEN_STATES_DIR="/personal/tmp/hidden_states_dspark_qwen3_4b_redhat"   # wiped at startup

VLLM_PORT=8000
MAX_SAMPLES=""           
SEQ_LENGTH=8192
EPOCHS=1
LR=6e-4
NUM_WORKERS=32

SPECULATOR_TYPE="dspark"
BLOCK_SIZE=8             
                         
MAX_ANCHORS=512
NUM_LAYERS=5
TARGET_LAYER_IDS="1 9 17 25 33"   
                                                         
MARKOV_RANK=256
MARKOV_HEAD_TYPE="vanilla"   
CONFIDENCE_HEAD_ALPHA=1.0
LOSS_FN='{"ce": 0.1, "tv": 0.9}'   
                                   
                                   
DFLASH_DECAY_GAMMA=4.0
PER_POSITION_LOSS_WEIGHT="fixed-exp-decay"

OPTIMIZER="adamw"
WEIGHT_DECAY=0.0
SCHEDULER_TYPE="cosine"
SCHEDULER_WARMUP_RATIO=0.04
SEED=42
CHECKPOINT_FREQ=0.1


VLLM_GPUS="0,1,2,3"
VLLM_DP=4
TRAIN_GPUS="4,5,6,7"
NUM_TRAIN_GPUS=4

cd "$REPO_DIR"

fail() { echo "ERROR: $*" >&2; exit 1; }

mkdir -p "$OUTPUT_DIR" "$SAVE_PATH"

MS_ARGS=()
if [ -n "$MAX_SAMPLES" ]; then MS_ARGS=(--max-samples "$MAX_SAMPLES"); fi

# Build --data arguments for prepare_data
DATA_ARGS=()
for f in "${DATASETS[@]}"; do
    DATA_ARGS+=(--data "$f")
done

rm -rf "$HIDDEN_STATES_DIR"
mkdir -p "$HIDDEN_STATES_DIR"


CUDA_VISIBLE_DEVICES="$VLLM_GPUS" python scripts/launch_vllm.py "$MODEL" \
    --target-layer-ids $TARGET_LAYER_IDS \
    --hidden-states-path "$HIDDEN_STATES_DIR" \
    -- --data-parallel-size "$VLLM_DP" --port "$VLLM_PORT" \
    --enforce-eager \
    --no-enable-chunked-prefill \
    2>&1 | tee "$SAVE_PATH/vllm.log" &
VLLM_PID=$!


while ! curl -s "http://localhost:${VLLM_PORT}/health" >/dev/null 2>&1; do
    # 检查进程是否意外崩溃
    if ! kill -0 "$VLLM_PID" 2>/dev/null; then
        echo "ERROR: vLLM failed to start. Check $SAVE_PATH/vllm.log for details."
        exit 1
    fi
    sleep 3
done


python scripts/prepare_data.py \
    --model "$MODEL" \
    "${DATA_ARGS[@]}" \
    --output "$OUTPUT_DIR" \
    --render-endpoint "http://localhost:${VLLM_PORT}" \
    --seq-length "$SEQ_LENGTH" \
    --num-preprocessing-workers "$NUM_WORKERS" \
    ${MS_ARGS[@]+"${MS_ARGS[@]}"} \
    2>&1 | tee "$SAVE_PATH/prepare_data.log"


CUDA_VISIBLE_DEVICES="$TRAIN_GPUS" torchrun \
    --standalone --nproc_per_node "$NUM_TRAIN_GPUS" \
    scripts/train.py \
    --verifier-name-or-path "$MODEL" \
    --speculator-type "$SPECULATOR_TYPE" \
    --data-path "$OUTPUT_DIR" \
    --vllm-endpoint "http://localhost:${VLLM_PORT}/v1" \
    --save-path "$SAVE_PATH" \
    --block-size "$BLOCK_SIZE" \
    --max-anchors "$MAX_ANCHORS" \
    --target-layer-ids $TARGET_LAYER_IDS \
    --num-layers "$NUM_LAYERS" \
    --markov-rank "$MARKOV_RANK" \
    --markov-head-type "$MARKOV_HEAD_TYPE" \
    --enable-confidence-head \
    --confidence-head-with-markov \
    --confidence-head-alpha "$CONFIDENCE_HEAD_ALPHA" \
    --loss-fn "$LOSS_FN" \
    --dflash-decay-gamma "$DFLASH_DECAY_GAMMA" \
    --per-position-loss-weight "$PER_POSITION_LOSS_WEIGHT" \
    --optimizer "$OPTIMIZER" \
    --lr "$LR" \
    --weight-decay "$WEIGHT_DECAY" \
    --scheduler-type "$SCHEDULER_TYPE" \
    --scheduler-warmup-ratio "$SCHEDULER_WARMUP_RATIO" \
    --epochs "$EPOCHS" \
    --total-seq-len "$SEQ_LENGTH" \
    --seed "$SEED" \
    --fsdp-shard \
    --on-missing generate \
    --on-generate delete \
    --hidden-states-path "$HIDDEN_STATES_DIR" \
    --checkpoint-freq "$CHECKPOINT_FREQ" \
    2>&1 | tee "$SAVE_PATH/train.log"
```


## 2-2 benchmark
### 2-2-1 dataset 
- gsm8k：https://modelscope.cn/datasets/modelscope/gsm8k 
- math500：https://modelscope.cn/datasets/AI-ModelScope/MATH-500 
- aime25：https://modelscope.cn/datasets/evalscope/aime25 
- mbpp：https://modelscope.cn/datasets/opencompass/mbpp 
- human eval：https://modelscope.cn/datasets/opencompass/humaneval 
- live code bench：https://modelscope.cn/datasets/Skywork/LiveCodeBench
- ceval：https://modelscope.cn/datasets/evalscope/ceval
- mt bench：https://modelscope.cn/datasets/HuggingFaceH4/mt_bench_prompts
- alpaca：https://modelscope.cn/datasets/AI-ModelScope/alpaca-gpt4-data-zh
- arena hard：https://modelscope.cn/datasets/AI-ModelScope/arena-hard-auto-v0.1

### 2-2-2 server
```bash
vllm serve /path/model/Qwen3-4B \
  --no-enable-flashinfer-autotune \
  --max-num-seqs 128 \
  --data-parallel-size 8 \
  --no-enable-prefix-caching \
  --speculative-config '{"method":"dspark","model":"/path/ckpt/speculators/dspark_qwen3_4b_redhat/checkpoints/0", "num_speculative_tokens": 8}'
```

### 2-2-3 benchmark
```bash
vllm bench serve \
  --base-url http://localhost:8000 \
  --model /path/model/Qwen3-4B \
  --dataset-name custom \
  --dataset-path /path/dataset/human-eval/humaneval-prompt.jsonl \
  --num-prompts 1040 \
  --temperature 0 \
  --custom-output-len 3072 \
  --no-oversample \
  --max-concurrency 32
```