---
language: en
license: apache-2.0
datasets:
- google-research-datasets/go_emotions
metrics:
- f1
tags:
- text-classification
- multi-label
- emotion
- distilbert
base_model: distilbert-base-uncased
model-index:
- name: Undertone-GoEmotion
  results:
  - task:
      type: text-classification
      name: Multi-label Text Classification
    dataset:
      name: GoEmotions (simplified)
      type: go_emotions
      split: test
    metrics:
    - type: f1
      value: 0.5836
      name: Micro F1
    - type: f1
      value: 0.5001
      name: Macro F1
---

<div style="background:#0d0c0b;color:#f4ede0;font-family:Georgia,'Times New Roman',serif;margin:-16px -16px 0 -16px;padding:0 0 64px 0;">

<div style="padding:80px 56px 56px 56px;border-bottom:1px solid #2a2622;">
  <div style="font-family:'SF Mono',Menlo,Consolas,monospace;font-size:11px;letter-spacing:0.22em;text-transform:uppercase;color:#b8ada0;display:flex;align-items:center;gap:12px;margin-bottom:36px;">
    <span style="display:inline-block;width:24px;height:1px;background:#e8b23a;"></span>
    QuantaSparkLabs · Multi-label classifier
  </div>
  <h1 style="font-family:Georgia,serif;font-weight:400;font-size:clamp(64px,10vw,128px);line-height:0.92;letter-spacing:-0.03em;margin:0 0 20px 0;color:#f4ede0;">
    Under<em style="font-style:italic;font-weight:400;color:#e8b23a;">tone</em>
  </h1>
  <p style="font-family:Georgia,serif;font-style:italic;font-weight:400;font-size:clamp(18px,2vw,26px);line-height:1.35;color:#b8ada0;max-width:580px;margin:0 0 40px 0;">
    A 28-label emotion tagger. One text, many colors.
  </p>
  <div style="display:flex;flex-wrap:wrap;gap:10px;">
    <span style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.08em;padding:7px 12px;border:1px solid #2a2622;border-radius:999px;color:#b8ada0;"><b style="color:#f4ede0;font-weight:500;">distilbert</b> · base</span>
    <span style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.08em;padding:7px 12px;border:1px solid #2a2622;border-radius:999px;color:#b8ada0;"><b style="color:#f4ede0;font-weight:500;">go_emotions</b> · simplified</span>
    <span style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.08em;padding:7px 12px;border:1px solid #2a2622;border-radius:999px;color:#b8ada0;">28 labels</span>
    <span style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.08em;padding:7px 12px;border:1px solid #2a2622;border-radius:999px;color:#b8ada0;">apache-2.0</span>
    <span style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.08em;padding:7px 12px;border:1px solid #2a2622;border-radius:999px;color:#b8ada0;">fast</span>
  </div>
</div>

<div style="display:flex;height:6px;width:100%;border-bottom:1px solid #2a2622;">
  <div style="flex:1;background:#e8b23a;"></div>
  <div style="flex:1;background:#f4a261;"></div>
  <div style="flex:1;background:#c1272d;"></div>
  <div style="flex:1;background:#d97742;"></div>
  <div style="flex:1;background:#7fa650;"></div>
  <div style="flex:1;background:#e8a3a8;"></div>
  <div style="flex:1;background:#8e7cc3;"></div>
  <div style="flex:1;background:#4a90a4;"></div>
  <div style="flex:1;background:#b03a5b;"></div>
  <div style="flex:1;background:#6b7a8f;"></div>
  <div style="flex:1;background:#8b5a3c;"></div>
  <div style="flex:1;background:#4a6b3d;"></div>
  <div style="flex:1;background:#e8b4b8;"></div>
  <div style="flex:1;background:#f4c430;"></div>
  <div style="flex:1;background:#3d405b;"></div>
  <div style="flex:1;background:#e5a87c;"></div>
  <div style="flex:1;background:#4a5a6b;"></div>
  <div style="flex:1;background:#f9d77e;"></div>
  <div style="flex:1;background:#d9465f;"></div>
  <div style="flex:1;background:#c8a2c8;"></div>
  <div style="flex:1;background:#7fb069;"></div>
  <div style="flex:1;background:#8b4a9c;"></div>
  <div style="flex:1;background:#5b8c8f;"></div>
  <div style="flex:1;background:#a8c5a0;"></div>
  <div style="flex:1;background:#7a6b5d;"></div>
  <div style="flex:1;background:#4a6fa5;"></div>
  <div style="flex:1;background:#e89b5b;"></div>
  <div style="flex:1;background:#9a9a9a;"></div>
</div>

<div style="padding:80px 56px;border-bottom:1px solid #2a2622;">
  <div style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.22em;text-transform:uppercase;color:#b8ada0;margin-bottom:36px;display:flex;align-items:center;gap:12px;">
    <span style="display:inline-block;width:24px;height:1px;background:#e8b23a;"></span>
    Results · test split · tuned thresholds
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:1px;background:#2a2622;border:1px solid #2a2622;">
    <div style="background:#0d0c0b;padding:36px 28px;">
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:10px;letter-spacing:0.2em;text-transform:uppercase;color:#b8ada0;margin-bottom:16px;">Micro F1</div>
      <div style="font-family:Georgia,serif;font-weight:400;font-size:64px;line-height:1;letter-spacing:-0.03em;color:#e8b23a;">0.584</div>
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:11px;color:#e8b23a;margin-top:12px;letter-spacing:0.05em;">+4.9 pts over 0.5 threshold</div>
    </div>
    <div style="background:#0d0c0b;padding:36px 28px;">
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:10px;letter-spacing:0.2em;text-transform:uppercase;color:#b8ada0;margin-bottom:16px;">Macro F1</div>
      <div style="font-family:Georgia,serif;font-weight:400;font-size:64px;line-height:1;letter-spacing:-0.03em;color:#f4ede0;">0.500</div>
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:11px;color:#e8b23a;margin-top:12px;letter-spacing:0.05em;">+2.5 pts over 0.5 threshold</div>
    </div>
    <div style="background:#0d0c0b;padding:36px 28px;">
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:10px;letter-spacing:0.2em;text-transform:uppercase;color:#b8ada0;margin-bottom:16px;">Val → Test gap</div>
      <div style="font-family:Georgia,serif;font-weight:400;font-size:64px;line-height:1;letter-spacing:-0.03em;color:#f4ede0;">0.006</div>
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:11px;color:#e8b23a;margin-top:12px;letter-spacing:0.05em;">micro · no overfit</div>
    </div>
  </div>
</div>

<div style="padding:80px 56px;border-bottom:1px solid #2a2622;">
  <div style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.22em;text-transform:uppercase;color:#b8ada0;margin-bottom:36px;display:flex;align-items:center;gap:12px;">
    <span style="display:inline-block;width:24px;height:1px;background:#e8b23a;"></span>
    The 28 emotions
  </div>
  <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:1px;background:#2a2622;border:1px solid #2a2622;">
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#e8b23a;flex:0 0 10px;"></span>admiration</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#f4a261;flex:0 0 10px;"></span>amusement</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#c1272d;flex:0 0 10px;"></span>anger</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#d97742;flex:0 0 10px;"></span>annoyance</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#7fa650;flex:0 0 10px;"></span>approval</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#e8a3a8;flex:0 0 10px;"></span>caring</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#8e7cc3;flex:0 0 10px;"></span>confusion</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#4a90a4;flex:0 0 10px;"></span>curiosity</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#b03a5b;flex:0 0 10px;"></span>desire</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#6b7a8f;flex:0 0 10px;"></span>disappointment</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#8b5a3c;flex:0 0 10px;"></span>disapproval</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#4a6b3d;flex:0 0 10px;"></span>disgust</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#e8b4b8;flex:0 0 10px;"></span>embarrassment</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#f4c430;flex:0 0 10px;"></span>excitement</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#3d405b;flex:0 0 10px;"></span>fear</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#e5a87c;flex:0 0 10px;"></span>gratitude</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#4a5a6b;flex:0 0 10px;"></span>grief</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#f9d77e;flex:0 0 10px;"></span>joy</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#d9465f;flex:0 0 10px;"></span>love</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#c8a2c8;flex:0 0 10px;"></span>nervousness</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#7fb069;flex:0 0 10px;"></span>optimism</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#8b4a9c;flex:0 0 10px;"></span>pride</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#5b8c8f;flex:0 0 10px;"></span>realization</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#a8c5a0;flex:0 0 10px;"></span>relief</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#7a6b5d;flex:0 0 10px;"></span>remorse</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#4a6fa5;flex:0 0 10px;"></span>sadness</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#e89b5b;flex:0 0 10px;"></span>surprise</div>
    <div style="background:#0d0c0b;padding:18px 16px;display:flex;align-items:center;gap:12px;font-size:13px;color:#b8ada0;"><span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#9a9a9a;flex:0 0 10px;"></span>neutral</div>
  </div>
</div>

<div style="padding:80px 56px;border-bottom:1px solid #2a2622;">
  <div style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.22em;text-transform:uppercase;color:#b8ada0;margin-bottom:36px;display:flex;align-items:center;gap:12px;">
    <span style="display:inline-block;width:24px;height:1px;background:#e8b23a;"></span>
    Usage
  </div>
  <div style="background:#080706;border:1px solid #2a2622;border-radius:4px;padding:24px 28px;font-family:'SF Mono',Menlo,Consolas,monospace;font-size:13px;line-height:1.75;color:#cfc4b3;overflow-x:auto;">
<span style="color:#e8b23a;">from</span> transformers <span style="color:#e8b23a;">import</span> pipeline<br><br>
clf = pipeline(<br>
&nbsp;&nbsp;&nbsp;&nbsp;<span style="color:#a8c5a0;">"text-classification"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;model=<span style="color:#a8c5a0;">"QuantaSparkLabs/Undertone-GoEmotion"</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;top_k=<span style="color:#e8b23a;">None</span>,<br>
&nbsp;&nbsp;&nbsp;&nbsp;function_to_apply=<span style="color:#a8c5a0;">"sigmoid"</span>,<br>
)<br><br>
text = <span style="color:#a8c5a0;">"I can't believe this worked, thank you!"</span><br>
scores = clf(text)[<span style="color:#a8c5a0;">0</span>]<br><br>
<span style="color:#6b6259;font-style:italic;"># Apply per-label thresholds from thresholds.json</span><br>
<span style="color:#6b6259;font-style:italic;"># instead of a blanket 0.5 for calibrated decisions.</span>
  </div>
</div>

<div style="padding:80px 56px;border-bottom:1px solid #2a2622;">
  <div style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.22em;text-transform:uppercase;color:#b8ada0;margin-bottom:36px;display:flex;align-items:center;gap:12px;">
    <span style="display:inline-block;width:24px;height:1px;background:#e8b23a;"></span>
    Specification
  </div>
  <div style="display:grid;grid-template-columns:220px 1fr;gap:0;border:1px solid #2a2622;">
    <div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;background:#0a0908;display:flex;align-items:center;">Base</div><div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-size:14px;line-height:1.6;color:#f4ede0;">distilbert-base-uncased</div>
    <div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;background:#0a0908;display:flex;align-items:center;">Head</div><div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-size:14px;line-height:1.6;color:#f4ede0;">28-output linear, sigmoid, BCEWithLogitsLoss</div>
    <div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;background:#0a0908;display:flex;align-items:center;">Epochs</div><div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-size:14px;line-height:1.6;color:#f4ede0;">3 · lr 3e-5 · warmup 400 steps</div>
    <div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;background:#0a0908;display:flex;align-items:center;">Batch / len</div><div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-size:14px;line-height:1.6;color:#f4ede0;">32 train · 64 eval · max_len 128</div>
    <div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;background:#0a0908;display:flex;align-items:center;">Precision</div><div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-size:14px;line-height:1.6;color:#f4ede0;">fp16 mixed precision</div>
    <div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;background:#0a0908;display:flex;align-items:center;">Seed</div><div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-size:14px;line-height:1.6;color:#f4ede0;">42</div>
    <div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;background:#0a0908;display:flex;align-items:center;">Class weight</div><div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-size:14px;line-height:1.6;color:#f4ede0;">pos_weight, clipped [1, 10]</div>
    <div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;background:#0a0908;display:flex;align-items:center;">Thresholds</div><div style="padding:16px 20px;border-bottom:1px solid #2a2622;font-size:14px;line-height:1.6;color:#f4ede0;">per-label grid over [0.10, 0.70], rounded to 0.02</div>
    <div style="padding:16px 20px;font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;background:#0a0908;display:flex;align-items:center;">Runtime</div><div style="padding:16px 20px;font-size:14px;line-height:1.6;color:#f4ede0;">~5 min on a single consumer GPU</div>
  </div>
</div>

<div style="padding:80px 56px;border-bottom:1px solid #2a2622;">
  <div style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.22em;text-transform:uppercase;color:#b8ada0;margin-bottom:36px;display:flex;align-items:center;gap:12px;">
    <span style="display:inline-block;width:24px;height:1px;background:#e8b23a;"></span>
    Limitations
  </div>
  <div style="display:flex;flex-direction:column;gap:0;max-width:720px;">
    <div style="display:grid;grid-template-columns:32px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid #2a2622;font-size:15px;line-height:1.7;color:#b8ada0;">
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:12px;color:#e8b23a;padding-top:4px;">01</div>
      <div>Trained on <b style="color:#f4ede0;font-weight:500;">Reddit comments</b>. Domain shift on formal text — legal, medical, academic — is expected and measurable.</div>
    </div>
    <div style="display:grid;grid-template-columns:32px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid #2a2622;font-size:15px;line-height:1.7;color:#b8ada0;">
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:12px;color:#e8b23a;padding-top:4px;">02</div>
      <div><b style="color:#f4ede0;font-weight:500;">Truncated at 128 tokens.</b> Long documents are only partially seen; outputs reflect the first chunk.</div>
    </div>
    <div style="display:grid;grid-template-columns:32px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid #2a2622;font-size:15px;line-height:1.7;color:#b8ada0;">
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:12px;color:#e8b23a;padding-top:4px;">03</div>
      <div>Rare labels — <b style="color:#f4ede0;font-weight:500;">grief, pride, relief, remorse</b> — have low test support. Check per-label F1 before depending on them.</div>
    </div>
    <div style="display:grid;grid-template-columns:32px 1fr;gap:20px;padding:18px 0;border-bottom:1px solid #2a2622;font-size:15px;line-height:1.7;color:#b8ada0;">
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:12px;color:#e8b23a;padding-top:4px;">04</div>
      <div>Emotion annotations are <b style="color:#f4ede0;font-weight:500;">subjective and culturally biased</b>. The model inherits both.</div>
    </div>
    <div style="display:grid;grid-template-columns:32px 1fr;gap:20px;padding:18px 0;font-size:15px;line-height:1.7;color:#b8ada0;">
      <div style="font-family:'SF Mono',Menlo,monospace;font-size:12px;color:#e8b23a;padding-top:4px;">05</div>
      <div><b style="color:#f4ede0;font-weight:500;">Not a mental-health or diagnostic tool.</b> Signals, not decisions. Human review required for any consequential use.</div>
    </div>
  </div>
</div>

<div style="padding:56px;display:flex;justify-content:space-between;align-items:baseline;gap:32px;flex-wrap:wrap;">
  <div style="font-family:Georgia,serif;font-style:italic;font-weight:400;font-size:20px;color:#b8ada0;">One text, many colors.</div>
  <div style="font-family:'SF Mono',Menlo,monospace;font-size:11px;letter-spacing:0.14em;text-transform:uppercase;color:#b8ada0;">QuantaSparkLabs · 2026</div>
</div>

</div>