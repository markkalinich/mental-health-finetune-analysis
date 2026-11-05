---
base_model:
- Delta-Vector/Rei-V3-KTO-12B
- Retreatcost/Chrysologus-12B
- Vortex5/Harmony-Bird-12B
- Vortex5/Red-Synthesis-12B
- Vortex5/Lunar-Nexus-12B
- Vortex5/Scarlet-Eclipse-12B
library_name: transformers
tags:
- mergekit
- merge
- roleplay
---
<div class="noctyx-stage">
  <section class="model-card">


  <header class="card-header">
      <div class="title-block">
        <div class="title-frame" aria-hidden="true"></div>

  <h1 class="model-title">NoctyxCosma-12B</h1>


  <div class="title-accents" aria-hidden="true">
          <span class="accent-bar"></span>
          <span class="accent-dot"></span>
          <span class="accent-bar"></span>
        </div>
      </div>

  <div class="hero-wrap">
        <div class="hero-frame" aria-hidden="true"></div>
        <img
          src="https://cdn-uploads.huggingface.co/production/uploads/6669a3a617b838fda45637b8/mCzdjBlQiwnTgnpKaaNn8.png"
      </div>
    </header>

  <div class="flow-divider" aria-hidden="true"></div>


  <section class="content-panel">
      <div class="panel-frame" aria-hidden="true"></div>
      <div class="panel-inner">
        <h2 class="panel-heading">Overview</h2>

  <p>
          <strong>NoctyxCosma-12B</strong> was created by merging
          <a href="https://huggingface.co/Vortex5/Harmony-Bird-12B">Harmony-Bird-12B</a>,
          <a href="https://huggingface.co/Retreatcost/Chrysologus-12B">Chrysologus-12B</a>,
          <a href="https://huggingface.co/Delta-Vector/Rei-V3-KTO-12B">Rei-V3-KTO-12B</a>,
          <a href="https://huggingface.co/Vortex5/Scarlet-Eclipse-12B">Scarlet-Eclipse-12B</a>,
          <a href="https://huggingface.co/Vortex5/Lunar-Nexus-12B">Lunar-Nexus-12B</a>,
          and
          <a href="https://huggingface.co/Vortex5/Red-Synthesis-12B">Red-Synthesis-12B</a>
          using a custom merge method.
        </p>

  <details class="yaml-toggle">
          <summary>Show merge configuration</summary>
          <pre>models:
  - model: Vortex5/Harmony-Bird-12B
  - model: Retreatcost/Chrysologus-12B
  - model: Delta-Vector/Rei-V3-KTO-12B
  - model: Vortex5/Scarlet-Eclipse-12B
  - model: Vortex5/Lunar-Nexus-12B
  - model: Vortex5/Red-Synthesis-12B
merge_method: smi_oni
parameters:
  k_core: 2
  strength_core: 1.0
  consensus_core: 0.48
  drop_cos: 0.10
  drop_min: 3
  strength_nov: 0.45
  novelty_budget: 0.22
  consensus_nov: 0.32
  conflict_bonus: 0.18
dtype: bfloat16
tokenizer:
  source: Vortex5/Red-Synthesis-12B
          </pre>
        </details>
      </div>
    </section>

  <div class="flow-divider thin" aria-hidden="true"></div>


  <section class="content-panel">
      <div class="panel-frame" aria-hidden="true"></div>
      <div class="panel-inner">
        <h2 class="panel-heading">Intended Use</h2>

  <div class="use-rect-row">
          <div class="use-rect">Creative Writing</div>
          <div class="use-rect">Storytelling</div>
          <div class="use-rect">Roleplay</div>
        </div>
      </div>
    </section>

  <div class="end-cap" aria-hidden="true"></div>

  </section>
</div>

<style>
@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;600&family=Inter:wght@400;500;600&display=swap');

:root{
  --bg0: #06070a;
  --bg1: #0b0d12;

  --ink: #eef0f6;
  --muted: rgba(238,240,246,0.72);

  --silver1: #e7e9ef;
  --silver2: #b9bfcc;
  --silver3: #7c8392;

  --red:  #b0121d;
  --pink: #e04b7a;

  --line: rgba(231,233,239,0.16);
  --shadow: rgba(0,0,0,0.60);
}


*{ box-sizing: border-box; }

.noctyx-stage{
  min-height: 100vh;
  padding: 84px 20px;
  background:
    radial-gradient(1200px 620px at 18% 16%, rgba(224,75,122,0.18), transparent 60%),
    radial-gradient(900px 540px at 84% 18%, rgba(176,18,29,0.18), transparent 62%),
    radial-gradient(1000px 560px at 55% 92%, rgba(231,233,239,0.10), transparent 62%),
    linear-gradient(180deg, var(--bg0), var(--bg1));
  position: relative;
  overflow: hidden;
}

.noctyx-stage::before{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:
    linear-gradient(180deg, rgba(0,0,0,0.00), rgba(0,0,0,0.55)),
    repeating-linear-gradient(
      90deg,
      rgba(231,233,239,0.05) 0px,
      rgba(231,233,239,0.05) 1px,
      transparent 1px,
      transparent 38px
    ),
    repeating-linear-gradient(
      0deg,
      rgba(231,233,239,0.04) 0px,
      rgba(231,233,239,0.04) 1px,
      transparent 1px,
      transparent 38px
    );
  opacity: 0.55;
}

.noctyx-stage::after{
  content:"";
  position:absolute;
  inset:-20%;
  pointer-events:none;
  background:
    radial-gradient(circle at 25% 30%, rgba(224,75,122,0.10), transparent 55%),
    radial-gradient(circle at 70% 35%, rgba(176,18,29,0.10), transparent 58%),
    radial-gradient(circle at 55% 75%, rgba(231,233,239,0.06), transparent 62%);
  filter: blur(10px);
  opacity: 0.9;
}

.model-card{
  max-width: 1120px;
  margin: 0 auto;
  padding: 120px 74px 110px;
  border-radius: 28px;
  position: relative;
  color: var(--ink);
  font-family: "Inter", sans-serif;

  border: 2px solid transparent;
  background:
    radial-gradient(1000px 520px at 20% 10%, rgba(224,75,122,0.10), transparent 55%),
    radial-gradient(900px 520px at 82% 12%, rgba(176,18,29,0.12), transparent 58%),
    linear-gradient(180deg, rgba(16,18,26,0.92), rgba(10,11,16,0.92)) padding-box,
    linear-gradient(145deg, rgba(231,233,239,0.85), rgba(124,131,146,0.85), rgba(231,233,239,0.85)) border-box;

  box-shadow:
    0 46px 120px var(--shadow),
    inset 0 1px 0 rgba(255,255,255,0.10);

  overflow: hidden;
}

.model-card::before{
  content:"";
  position:absolute;
  inset: 12px;
  border-radius: 22px;
  pointer-events:none;
  border: 1px solid rgba(231,233,239,0.20);
  box-shadow:
    inset 0 0 0 1px rgba(0,0,0,0.55),
    inset 0 0 34px rgba(224,75,122,0.08),
    inset 0 0 34px rgba(176,18,29,0.08);
}

.model-card::after{
  content:"";
  position:absolute;
  inset:0;
  pointer-events:none;
  background:
    radial-gradient(circle at 0% 0%, rgba(231,233,239,0.12), transparent 38%),
    radial-gradient(circle at 100% 0%, rgba(231,233,239,0.10), transparent 40%),
    radial-gradient(circle at 0% 100%, rgba(224,75,122,0.12), transparent 44%),
    radial-gradient(circle at 100% 100%, rgba(176,18,29,0.12), transparent 46%),
    repeating-linear-gradient(180deg, rgba(255,255,255,0.03) 0px, rgba(255,255,255,0.03) 1px, transparent 1px, transparent 7px);
  opacity: 0.75;
}

.card-header{
  text-align:center;
  position: relative;
  z-index: 1;
  margin-bottom: 120px;
}

.title-block{
  display:inline-block;
  position: relative;
  padding: 30px 44px 26px;
  border-radius: 14px;
  background: linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
  border: 1px solid rgba(231,233,239,0.18);
  box-shadow: 0 26px 66px rgba(0,0,0,0.55);


  max-width: min(900px, 100%);
}

.title-frame{
  position: absolute;
  inset: -8px -12px;
  border-radius: 14px;
  z-index: -1;

  background: transparent;

  border: 1px solid rgba(231,233,239,0.35);

  box-shadow:
    0 10px 28px rgba(0,0,0,0.45);
}

.model-title{
  margin: 0;
  padding: 6px 0;

  font-family: "Orbitron", sans-serif;
  font-size: clamp(1.65rem, 3.0vw, 2.7rem);
  letter-spacing: 0.095em;
  line-height: 1.25;

  white-space: nowrap;
  overflow: visible;

  color: var(--ink);
  text-shadow:
    0 1px 0 rgba(0,0,0,0.55),
    0 0 16px rgba(224,75,122,0.10),
    0 0 16px rgba(176,18,29,0.10);
}

.model-subtitle{
  margin: 14px 0 0;
  font-size: 1.02rem;
  letter-spacing: 0.06em;
  color: var(--muted);
}

.title-accents{
  margin: 18px auto 0;
  width: min(520px, 80%);
  display:flex;
  align-items:center;
  justify-content:center;
  gap: 14px;
}

.accent-bar{
  height: 4px;
  flex: 1;
  border-radius: 999px;
  background: linear-gradient(90deg, transparent, rgba(231,233,239,0.55), transparent);
}
.accent-dot{
  width: 10px;
  height: 10px;
  border-radius: 999px;
  background: radial-gradient(circle at 30% 30%, var(--pink), var(--red));
  box-shadow: 0 0 18px rgba(224,75,122,0.35);
}

.hero-wrap{
  margin-top: 58px;
  display: inline-block;
  position: relative;
  max-width: 94%;
}

.hero-frame{
  display: none;
}

.hero-wrap img{
  display: block;
  max-width: 100%;

  border-radius: 12px;

  outline: 0.5px solid rgba(231,233,239,0.35);
  outline-offset: 0;

  box-shadow: none;
}

.flow-divider{
  width: 86%;
  height: 8px;
  margin: 120px auto;
  border-radius: 999px;
  position: relative;
  z-index: 1;
  background: linear-gradient(90deg, transparent, rgba(231,233,239,0.34), rgba(224,75,122,0.38), rgba(231,233,239,0.34), transparent);
  box-shadow: 0 0 20px rgba(224,75,122,0.14), 0 0 18px rgba(231,233,239,0.10);
}
.flow-divider.thin{
  width: 70%;
  height: 6px;
}

.content-panel{
  max-width: 980px;
  margin: 120px auto;
  position: relative;
  z-index: 1;

  overflow: visible;
}

.panel-frame{
  position:absolute;
  inset:-14px;
  border-radius: 12px;
  pointer-events:none;
  background: linear-gradient(145deg, rgba(231,233,239,0.40), rgba(124,131,146,0.32), rgba(231,233,239,0.36));
  box-shadow: 0 34px 92px rgba(0,0,0,0.55);
}

.panel-frame::before{
  content:"";
  position:absolute;
  inset: 3px;
  border-radius: 11px;
  background: linear-gradient(180deg, rgba(0,0,0,0.35), rgba(0,0,0,0.15));
  box-shadow: inset 0 0 0 1px rgba(231,233,239,0.14), inset 0 0 26px rgba(224,75,122,0.08);
}

.panel-inner{
  position: relative;
  padding: 86px 76px;
  border-radius: 10px;
  text-align: center;
  background:
    radial-gradient(900px 260px at 50% 0%, rgba(224,75,122,0.12), transparent 60%),
    radial-gradient(900px 260px at 50% 110%, rgba(176,18,29,0.10), transparent 62%),
    linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.02));
  border: 1px solid rgba(231,233,239,0.16);
}

.panel-heading{
  margin: 0 0 42px;
  font-family:"Orbitron",sans-serif;
  font-size: 2.35rem;
  letter-spacing: 0.14em;
  color: var(--ink);
  transition: text-shadow 0.25s ease, transform 0.25s ease;
}

.panel-heading:hover{
  transform: translateY(-1px);
  text-shadow: 0 0 18px rgba(224,75,122,0.28), 0 0 24px rgba(231,233,239,0.14);
}

.content-panel p{
  margin: 0;
  font-size: 1.30rem;
  line-height: 1.95;
  color: rgba(238,240,246,0.82);
}

strong{ color: var(--ink); font-weight: 700; }

.model-card a{
  color: rgba(238,240,246,0.86);
  text-decoration: underline;
  text-decoration-thickness: 2px;
  text-underline-offset: 3px;
}
.model-card a:hover{ text-shadow: 0 0 14px rgba(224,75,122,0.22); }

.yaml-toggle summary{
  margin-top: 40px;
  font-size: 1.05rem;
  font-weight: 650;
  letter-spacing: 0.04em;
  cursor:pointer;
  color: rgba(238,240,246,0.74);
}
.yaml-toggle summary:hover{
  color: rgba(238,240,246,0.92);
  text-shadow: 0 0 16px rgba(224,75,122,0.18);
}
.yaml-toggle pre{
  margin-top: 18px;
  padding: 28px;
  text-align:left;
  border-radius: 10px;
  overflow-x:auto;
  background: linear-gradient(180deg, rgba(231,233,239,0.10), rgba(231,233,239,0.05));
  border: 1px solid rgba(231,233,239,0.16);
  border-left: 6px solid rgba(224,75,122,0.65);
  font-size: 1.02rem;
  line-height: 1.65;
  color: rgba(238,240,246,0.86);
}

.yaml-toggle pre{
  max-width: 100%;
  overflow-x: auto;
  box-sizing: border-box;
}

.yaml-toggle pre{
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;

  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;

  transform: none;
  backface-visibility: hidden;
}

.use-rect-row{
  display: flex;
  justify-content: center;
  align-items: stretch;
  gap: 28px;
  margin-top: 42px;

  flex-wrap: nowrap;
  max-width: 100%;
}

.use-rect{
  width: 100%;
  max-width: 100%;

  padding: 22px 16px;

  text-align: center;
  font-size: 1.02rem;
  letter-spacing: 0.03em;
  white-space: nowrap;

  color: rgba(238,240,246,0.96);

  background:
    linear-gradient(
      180deg,
      rgba(255,255,255,0.10),
      rgba(255,255,255,0.02)
    );

  border: 1px solid rgba(231,233,239,0.22);
  border-radius: 5px;

  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.14),
    inset 0 -2px 0 rgba(0,0,0,0.55),
    0 10px 24px rgba(0,0,0,0.55),
    0 2px 0 rgba(0,0,0,0.65);

  position: relative;
}

.use-rect::after{
  content:"";
  position:absolute;
  left: 22%;
  right: 22%;
  bottom: 9px;
  height: 2px;
  border-radius: 999px;
  background: linear-gradient(
    90deg,
    rgba(176,18,29,0.95),
    rgba(224,75,122,0.95)
  );
  box-shadow: 0 0 10px rgba(224,75,122,0.26);
}

.use-rect:hover{
  transform: translateY(-2px);
  box-shadow:
    inset 0 1px 0 rgba(255,255,255,0.16),
    inset 0 -2px 0 rgba(0,0,0,0.65),
    0 18px 36px rgba(0,0,0,0.65),
    0 4px 0 rgba(0,0,0,0.75);
}

@media (max-width: 1100px){
  .use-rect-row{
    flex-wrap: wrap;
  }
  .use-rect{
    flex: 1 1 100%;
    max-width: 100%;
    white-space: normal;
  }
}

.end-cap{
  width: 64%;
  height: 8px;
  margin: 72px auto 0;
  border-radius: 999px;
  background: linear-gradient(90deg, transparent, rgba(231,233,239,0.22), rgba(224,75,122,0.32), rgba(231,233,239,0.22), transparent);
  position: relative;
  z-index: 1;
}

.noctyx-stage::before,
.noctyx-stage::after{
  content: none !important;
  background: none !important;
  filter: none !important;
  opacity: 0 !important;
}

</style>