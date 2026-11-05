---
license: apache-2.0
language:
- en
pipeline_tag: text-classification
library_name: transformers
tags:
- emotions
- multi-task-learning
- text-classification
- sentiment-analysis
- natural-language-processing
- psychological-modeling
- emotion-recognition
- bert
- deep-learning
- emotion-embeddings
- valence-arousal
- emotion-ontology
---

<style>
/* ==========================================================================
   EmotionVerse-2 • Premium Cosmic Theme (README-safe, JS-free)
   Advanced layering, theming tokens, elevation system, and accessible motion.
   Keep existing class names for drop-in replacement.
   ========================================================================== */

/* ------------------------------------------------
   0) Typeface & base tokens
   ------------------------------------------------ */
@import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300;400;700&family=Space+Grotesk:wght@400;700&display=swap');

:root{
  /* Core palette */
  --bg-1:#0b1320;
  --bg-2:#101d30;
  --bg-3:#0a111b;
  --surface:#162335;       /* primary glass */
  --surface-2:#1b2a41;     /* secondary surface */
  --surface-3:#21334f;     /* deep surface */
  --ink:#a8b6cb;           /* body text */
  --ink-strong:#e7f2ff;    /* strong text */
  --ink-dim:#8ea0ba;

  /* Accents (Aurora) */
  --accent:#7fffd4;        /* aqua */
  --accent-2:#a2f4ff;      /* ice */
  --accent-3:#8ef1d2;      /* mint */
  --hot:#ffb86b;           /* warm highlight */

  /* Lines & glass */
  --line:rgba(150,200,255,.18);
  --line-strong:rgba(160,210,255,.35);
  --soft:rgba(255,255,255,.06);
  --glass:rgba(22, 35, 53, .84);
  --muted:rgba(90,110,140,.35);

  /* Radii & spacing */
  --r-sm:10px; --r-md:14px; --r-lg:18px; --r-xl:28px; --r-xxl:36px;
  --space-1:8px; --space-2:12px; --space-3:16px; --space-4:24px; --space-5:36px; --space-6:56px;

  /* Elevation system (layered shadows) */
  --elev-1:0 6px 14px rgba(0,0,0,.32), inset 0 0 16px rgba(255,255,255,.04);
  --elev-2:0 10px 22px rgba(0,0,0,.42), inset 0 0 16px rgba(160,200,255,.06);
  --elev-3:0 18px 36px rgba(0,0,0,.55), inset 0 0 22px rgba(160,200,255,.09);
  --elev-4:0 26px 58px rgba(0,0,0,.62), inset 0 0 28px rgba(160,200,255,.11);

  /* Gradients */
  --grad-sky:
    radial-gradient(1200px 800px at 10% -10%, rgba(127,255,212,.10), transparent 60%),
    radial-gradient(900px 600px at 90% 0%,  rgba(162,244,255,.08), transparent 60%),
    linear-gradient(180deg, var(--bg-1), var(--bg-2) 52%, var(--bg-3));
  --grad-aurora:
    conic-gradient(from 180deg at 70% 20%, rgba(127,255,212,.18), rgba(162,244,255,.12), rgba(127,255,212,.06), transparent 75%);
  --grad-border:linear-gradient(90deg, rgba(127,255,212,.45), rgba(162,244,255,.35), rgba(127,255,212,.45));
  --grad-chip:linear-gradient(90deg, rgba(127,255,212,.16), rgba(127,255,212,.04));

  /* Accent glow */
  --glow:0 0 0 1px rgba(127,255,212,.22), 0 0 24px rgba(127,255,212,.22);

  /* Typography */
  --font-body:'Roboto Mono', monospace;
  --font-head:'Space Grotesk', sans-serif;

  /* Motion */
  --dur-fast:.18s; --dur:.32s; --dur-slow:.6s;
  --ease:cubic-bezier(.2,.6,.2,1);
}

/* Optional alternate theme (apply on a wrapper: .theme-aurora) */
.theme-aurora{
  --surface:#14273b; --surface-2:#1a2f47; --surface-3:#1f3a59;
  --accent:#90ffe1; --accent-2:#b9f6ff; --line:rgba(170,220,255,.22);
}

/* High-contrast preference bump */
@media (prefers-contrast: more){
  :root{ --line:rgba(170,220,255,.3); --ink:#cfe2ff }
}

/* ------------------------------------------------
   1) Base layout & starfield layers
   ------------------------------------------------ */
*{ box-sizing:border-box }

html,body{
  margin:0; padding:0;
  font-family:var(--font-body);
  color:var(--ink);
  background:var(--grad-sky);
  background-attachment:fixed;
  line-height:1.78;
}

/* Subtle starfield & noise without images */
body::before,
body::after{
  content:'';
  position:fixed; inset:0; pointer-events:none;
}
body::before{
  /* twinkle grid */
  background:
    radial-gradient(2px 2px at 20% 30%, rgba(255,255,255,.08) 0, transparent 60%),
    radial-gradient(1.5px 1.5px at 75% 18%, rgba(255,255,255,.06) 0, transparent 60%),
    radial-gradient(1.6px 1.6px at 40% 70%, rgba(255,255,255,.05) 0, transparent 60%),
    radial-gradient(1.3px 1.3px at 85% 65%, rgba(255,255,255,.05) 0, transparent 60%);
  animation:twinkle var(--dur-slow) linear infinite alternate;
  opacity:.7;
}
body::after{
  background:var(--grad-aurora);
  filter:blur(40px) saturate(120%);
  opacity:.35;
}

/* Reduced motion: calm space */
@media (prefers-reduced-motion: reduce){
  body::before{ animation:none }
  .container::before{ animation:none }
}

/* ------------------------------------------------
   2) Container with layered glass & grid glow
   ------------------------------------------------ */
.container{
  max-width:1200px;
  margin:40px auto;
  padding:var(--space-6) clamp(16px,3vw,48px);
  background:var(--glass);
  border:1.5px solid var(--line);
  border-radius:var(--r-xxl);
  box-shadow:var(--elev-4);
  position:relative; overflow:hidden;
  backdrop-filter:saturate(110%) blur(10px);
}
@supports not ((backdrop-filter: blur(10px)) or (-webkit-backdrop-filter: blur(10px))){
  .container{ background:rgba(22,35,53,.92) }
}

/* Aurora wash */
.container::before{
  content:'';
  position:absolute; inset:-60%;
  background:
    radial-gradient(600px 600px at 12% 12%, rgba(127,255,212,.18), transparent 60%),
    radial-gradient(420px 420px at 88% 0%,  rgba(162,244,255,.16), transparent 62%),
    radial-gradient(540px 540px at 70% 85%, rgba(127,255,212,.12), transparent 65%);
  animation:cosmic-pulse 14s linear infinite;
  pointer-events:none; z-index:0;
}

/* Subtle grid overlay */
.container::after{
  content:'';
  position:absolute; inset:0; z-index:0; pointer-events:none;
  background-image:
    linear-gradient(rgba(255,255,255,.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,.04) 1px, transparent 1px);
  background-size:22px 22px, 22px 22px;
  mask:linear-gradient(180deg, transparent, rgba(0,0,0,.5) 20%, rgba(0,0,0,.9) 60%, transparent);
}

/* ------------------------------------------------
   3) Headings & micro-typography
   ------------------------------------------------ */
h1,h2,h3,h4{
  font-family:var(--font-head);
  text-transform:uppercase;
  letter-spacing:1.25px;
  text-shadow:3px 3px 8px rgba(0,0,0,.55);
  margin:0 0 18px 0;
}

h1{
  font-size:clamp(28px,4.4vw,46px);
  text-align:center;
  background:linear-gradient(90deg,#fff,var(--accent),#e0ffff);
  -webkit-background-clip:text; background-clip:text; color:transparent;
  margin-bottom:28px;
  filter:drop-shadow(0 6px 16px rgba(127,255,212,.25));
}
h2{
  color:var(--accent);
  font-size:clamp(20px,2.8vw,28px);
  border-bottom:2px solid rgba(127,255,212,.3);
  padding-bottom:10px; margin-top:28px;
}
h3{ color:#bfe8ff; font-size:clamp(18px,2.2vw,22px) }
h4{ color:#cbeeff; font-size:clamp(16px,2vw,20px) }

.small{ font-size:.94em; opacity:.92 }
.center{ text-align:center }

/* ------------------------------------------------
   4) Sections, cards, and interactive details
   ------------------------------------------------ */
.section{
  margin:36px 0 48px;
  background:linear-gradient(180deg, rgba(30,45,60,.94), rgba(26,43,61,.92));
  border:1px solid var(--muted);
  border-radius:var(--r-lg);
  padding:26px;
  box-shadow:var(--elev-2);
  position:relative; z-index:1;
  transition:transform var(--dur) var(--ease), box-shadow var(--dur) var(--ease), border-color var(--dur) var(--ease);
}
.section::before{
  content:'';
  position:absolute; inset:0; pointer-events:none; border-radius:inherit;
  background:linear-gradient(180deg, rgba(127,255,212,.12), transparent 40%);
  border:1px solid transparent;
  mask:linear-gradient(#000,#000) padding-box, linear-gradient(#000,#000);
}
.section:hover{
  transform:translateY(-4px);
  border-color:var(--line-strong);
  box-shadow:var(--elev-3);
}

/* Collapsibles */
details{
  border:1px solid rgba(160,200,255,.24);
  border-radius:var(--r-md);
  padding:12px 14px;
  background:rgba(30,45,60,.78);
  margin:12px 0; box-shadow:var(--elev-1);
}
details>summary{
  cursor:pointer; font-weight:700; color:#c7ecff; outline:none;
}
details[open]{ border-color:rgba(160,200,255,.36) }

/* ------------------------------------------------
   5) Informational “detail” callouts
   ------------------------------------------------ */
.detail{
  padding:16px 18px; margin:14px 0;
  border-left:4px solid var(--accent);
  border:1px solid rgba(100,130,170,.22);
  border-radius:var(--r-md);
  background:
    linear-gradient(180deg, rgba(40,55,70,.92), rgba(40,55,70,.84)),
    radial-gradient(600px 300px at 0% 0%, rgba(127,255,212,.10), transparent 70%);
  box-shadow:var(--elev-1);
  transition:transform var(--dur-fast) var(--ease), border-color var(--dur-fast) var(--ease), background var(--dur-fast) var(--ease);
}
.detail:hover{
  transform:translateX(4px);
  border-left-color:var(--accent-2);
  background:
    linear-gradient(180deg, rgba(50,65,80,.94), rgba(50,65,80,.86)),
    radial-gradient(600px 300px at 0% 0%, rgba(162,244,255,.12), transparent 70%);
  box-shadow:var(--elev-2);
}
.detail-icon{ font-size:1.25em; margin-right:12px; color:var(--accent) }

/* ------------------------------------------------
   6) Lists, links, chips/badges, kbd
   ------------------------------------------------ */
ul{ list-style:none; padding:0; margin:0 }
ul li{
  margin:12px 0; padding:14px 16px;
  background:rgba(50,60,75,.70);
  border-left:3px solid #b0e0e6;
  border-radius:var(--r-sm);
  box-shadow:inset 0 0 8px rgba(0,0,0,.2);
  transition:transform var(--dur-fast) var(--ease), background var(--dur-fast) var(--ease), border-color var(--dur-fast) var(--ease);
}
ul li:hover{
  transform:translateX(6px);
  background:rgba(60,70,85,.86);
  border-left-color:#e0ffff;
}

a{ color:#add8e6; text-decoration:none; font-weight:700; outline:none }
a:hover{ color:#e0ffff; text-shadow:0 0 8px rgba(173,216,230,.8) }
a:focus-visible{ box-shadow:0 0 0 3px rgba(162,244,255,.35), 0 0 0 6px rgba(127,255,212,.22); border-radius:8px }

.badges{
  display:flex; flex-wrap:wrap; gap:10px; justify-content:center;
  margin:10px 0 24px;
}
.badge{
  padding:8px 12px; border-radius:999px; font-size:.85em; font-weight:700;
  border:1px solid var(--line);
  background:var(--grad-chip);
  box-shadow:inset 0 0 12px rgba(127,255,212,.12), 0 6px 18px rgba(0,0,0,.2);
  backdrop-filter:saturate(120%) blur(3px);
}

/* Keyboard tag */
.kbd{
  padding:2px 6px; border-radius:6px;
  border:1px solid rgba(255,255,255,.15);
  background:rgba(0,0,0,.35);
  color:#e0ffff; font-weight:700
}

/* ------------------------------------------------
   7) Code & pre blocks
   ------------------------------------------------ */
pre,code{ font-family:var(--font-body) }
pre{
  background:rgba(0,0,0,.34);
  border:1px solid rgba(100,130,170,.24);
  padding:16px; border-radius:var(--r-md);
  overflow:auto; box-shadow:var(--elev-1);
}
code{
  background:rgba(0,0,0,.28);
  padding:3px 6px; border-radius:6px; color:var(--accent);
}
pre code{ background:transparent; color:#e0ffff }

/* ------------------------------------------------
   8) Tables & SVG frames
   ------------------------------------------------ */
.ranking-table{
  width:100%; border-collapse:collapse; margin-top:18px; font-size:1.05em;
  background:linear-gradient(180deg, rgba(255,255,255,.02), transparent);
  border-radius:var(--r-md); overflow:hidden;
}
.ranking-table th,.ranking-table td{
  padding:14px 12px; text-align:left;
  border-bottom:1px solid rgba(127,255,212,.12);
}
.ranking-table th{
  background:rgba(127,255,212,.12);
  color:var(--accent); text-transform:uppercase; letter-spacing:.6px;
}
.ranking-table tr:hover{ background:rgba(127,255,212,.06) }
.ranking-table td:first-child{ color:#e0ffff; font-weight:700 }
.ranking-table td:last-child{ color:var(--accent); font-weight:700 }
.highlight-row{
  background:linear-gradient(90deg, rgba(127,255,212,.22), rgba(127,255,212,.08));
  box-shadow:inset 0 0 18px rgba(127,255,212,.12);
}

.svg-frame{
  background:linear-gradient(180deg, rgba(255,255,255,.03), rgba(255,255,255,.01));
  border:1px solid rgba(160,200,255,.24);
  border-radius:var(--r-lg);
  padding:18px; box-shadow:var(--elev-2); margin:14px 0;
}

/* ------------------------------------------------
   9) Decorative lines & utilities
   ------------------------------------------------ */
.hr{
  height:1px; margin:24px 0;
  background:linear-gradient(90deg, transparent, rgba(127,255,212,.35), transparent);
  box-shadow:0 0 12px rgba(127,255,212,.12);
}

/* Elevation utilities */
.elev-1{ box-shadow:var(--elev-1) }
.elev-2{ box-shadow:var(--elev-2) }
.elev-3{ box-shadow:var(--elev-3) }
.elev-4{ box-shadow:var(--elev-4) }

/* ------------------------------------------------
   10) Motion keyframes
   ------------------------------------------------ */
@keyframes cosmic-pulse{
  0%  { transform:scale(.82) rotate(0deg);   opacity:.34 }
  50% { transform:scale(1.08) rotate(180deg); opacity:.54 }
  100%{ transform:scale(.82) rotate(360deg); opacity:.34 }
}
@keyframes twinkle{
  from{ opacity:.55; filter:brightness(100%) }
  to  { opacity:.85; filter:brightness(120%) }
}

/* ------------------------------------------------
   11) Print adjustments
   ------------------------------------------------ */
@media print{
  .container{ box-shadow:none; border-color:#ccc; background:#fff; color:#111; backdrop-filter:none }
  .section{ box-shadow:none; background:#fff; border-color:#ddd }
  a{ color:#004aad; text-shadow:none }
}

/* ------------------------------------------------
   12) Visualization sizing & consistency (no-theme-change)
   Ensures inline SVGs scale responsively, keep strokes readable,
   and text remains legible inside .svg-frame containers.
   ------------------------------------------------ */
.svg-frame{
  /* keep original look, just refine layout */
  --svg-pad: clamp(12px, 2.5vw, 22px);
  padding: var(--svg-pad);
  overflow: hidden;             /* prevent bleed at edges */
  isolation: isolate;           /* layer blending safety */
  container-type: inline-size;  /* enable container queries */
}

.svg-frame svg{
  display: block;               /* remove inline gap */
  inline-size: 100%;            /* responsive width */
  block-size: auto;             /* natural height from viewBox */
  max-inline-size: 100%;
  height: auto;                 /* Safari/Chromium: respect aspect via viewBox */
  shape-rendering: geometricPrecision;
  text-rendering: optimizeLegibility;
}

/* keep strokes readable when scaled */
.svg-frame svg [stroke]{
  vector-effect: non-scaling-stroke;
}

/* crisper grid/axes without aliasing */
.svg-frame svg line, .svg-frame svg path{
  shape-rendering: crispEdges;
}

/* typography inside charts */
.svg-frame svg text{
  font-family: var(--font-body, 'Roboto Mono', monospace);
  font-size: clamp(10px, 1.4vw, 12px);
  line-height: 1;
  letter-spacing: .2px;
  fill: var(--ink, #a8b6cb);
  user-select: none;
  pointer-events: none; /* avoid accidental selections */
}

/* emphasize headline values (e.g., 0.951) without overflow */
.svg-frame svg text[font-weight="700"],
.svg-frame svg text[font-weight="bold"]{
  fill: var(--ink-strong, #e7f2ff);
}

/* tick/axis labels can dim slightly to reduce clutter */
.svg-frame svg .axis, .svg-frame svg .tick, .svg-frame svg .label-muted{
  fill: color-mix(in oklab, var(--ink) 85%, transparent);
}

/* Rounded rectangles render smoother when scaled */
.svg-frame svg rect{
  shape-rendering: geometricPrecision;
}

/* container-aware adjustments for very narrow widths */
@container (max-width: 620px){
  .svg-frame svg text{ font-size: clamp(9px, 1.9vw, 11px) }
}
@container (max-width: 420px){
  .svg-frame{ --svg-pad: 12px }
  .svg-frame svg text{ font-size: 9px }
}

/* print: keep vectors crisp and visible on white */
@media print{
  .svg-frame{ border-color:#ccc; background:#fff }
  .svg-frame svg text{ fill:#111 }
}


/* ------------------------------------------------
   13) Redacted finale header (blur + blackout)
   Targets the final <h1> in the document so you can paste the snippet at
   the end and it will appear blurred/black-barred. Optionally, add
   class="redacted" to any <h1> to force the effect.
   ------------------------------------------------ */
.container h1:last-of-type,
.container h1.redacted{
  position: relative;
  z-index: 0;
  isolation: isolate; /* ensure ::after overlays text correctly */
}

.container h1:last-of-type::after,
.container h1.redacted::after{
  content: "";
  position: absolute; inset: -8px; /* cover glow & extra padding */
  border-radius: 16px;
  background: rgba(0,0,0,.92);      /* blackout */
  backdrop-filter: blur(10px) saturate(0) brightness(0.25); /* blur the text behind */
  -webkit-backdrop-filter: blur(10px) saturate(0) brightness(0.25);
  box-shadow: 0 10px 26px rgba(0,0,0,.6), inset 0 0 18px rgba(0,0,0,.6);
  z-index: 2; /* above text */
  pointer-events: none; /* keep it non-interactive */
}

/* Reduced motion fallback: keep blackout without blur */
@media (prefers-reduced-motion: reduce){
  .container h1:last-of-type::after,
  .container h1.redacted::after{
    backdrop-filter: none; -webkit-backdrop-filter: none;
  }
}

</style>


<div class="container">

 <h2><p class="center small">🌌 EmotionVerse-2: Galactic Emotional Intelligence</p></h2>

<div class="badges">
  <span class="badge">Apache-2.0</span>
  <span class="badge">BERT-base encoder</span>
  <span class="badge">Multi-Task (6 heads)</span>
  <span class="badge">Plutchik + Circumplex</span>
  <span class="badge">F1 Macro: <span class="kbd">0.951</span></span>
  <span class="badge">Coherence Index: <span class="kbd">0.97</span></span>
  <span class="badge">HF Transformers</span>
</div>

<h2><p class="center small">
EmotionVerse-2 unifies psychologically-grounded labeling (Plutchik) with a valence-arousal manifold, neural plasticity, and memory consolidation. It doesn’t just tag text—it resolves <em>why</em> it feels the way it does, across interlocking tasks that share a single encoder for maximal transfer.
</p></h2>

<div class="section">
  <h2>✨ Revolutionary Emotional Paradigm</h2>
  <p>
    A single BERT encoder feeds six specialized heads—Primary, Secondary, Meta, Sentiment, Interaction, and Context—trained end-to-end with dynamic loss weighting. The result is emergent cross-task awareness: subtle shifts, mixed feelings, and psychologically consistent outputs.
  </p>

  <ul>
    <li>
      <div class="detail"><span class="detail-icon">🚀</span>
      <strong>Unified Multi-Task Engine.</strong> One encoder; six heads. Joint optimization learns shared affective features while preserving task-specific finesse.</div>
    </li>
    <li>
      <div class="detail"><span class="detail-icon">🧬</span>
      <strong>Plutchik × Russell Fusion.</strong> Labels live in a combined categorical + circumplex space (valence, arousal, intensity), preserving family hierarchies and psychological distances.</div>
    </li>
    <li>
      <div class="detail"><span class="detail-icon">🔗</span>
      <strong>Adaptive Loss Balancing.</strong> Dynamic task weights + focal components lift rare emotions without destabilizing common ones.</div>
    </li>
    <li>
      <div class="detail"><span class="detail-icon">📊</span>
      <strong>Holistic Metrics.</strong> Per-task precision/recall/F1 plus a cross-task <em>Emotion Coherence Index</em> (valence-arousal similarity across heads).</div>
    </li>
  </ul>

  <details>
    <summary>View architecture diagram (SVG)</summary>
    <div class="svg-frame">
      <svg viewBox="0 0 980 260" width="100%" height="auto" role="img" aria-label="EmotionVerse-2 architecture">
        <defs>
          <linearGradient id="g1" x1="0" x2="1">
            <stop offset="0" stop-color="#7fffd4" stop-opacity=".4"/>
            <stop offset="1" stop-color="#a2f4ff" stop-opacity=".35"/>
          </linearGradient>
        </defs>
        <rect x="30" y="70" width="260" height="120" rx="14" fill="url(#g1)" stroke="#7fffd4" stroke-opacity=".6"/>
        <text x="160" y="105" text-anchor="middle" fill="#e0ffff" font-size="16" font-weight="700">BERT Encoder</text>
        <text x="160" y="128" text-anchor="middle" fill="#b0e0e6" font-size="12">w/ Circumplex Injector</text>
        <text x="160" y="148" text-anchor="middle" fill="#b0e0e6" font-size="12">Neural Plasticity Gate</text>
        <text x="160" y="168" text-anchor="middle" fill="#b0e0e6" font-size="12">GRU Memory Consolidator</text>

  <rect x="360" y="30" width="170" height="70" rx="10" fill="rgba(127,255,212,.15)" stroke="#7fffd4" stroke-opacity=".45"/>
        <text x="445" y="60" text-anchor="middle" fill="#e0ffff" font-size="13" font-weight="700">Primary</text>

  <rect x="560" y="30" width="170" height="70" rx="10" fill="rgba(127,255,212,.15)" stroke="#7fffd4" stroke-opacity=".45"/>
        <text x="645" y="60" text-anchor="middle" fill="#e0ffff" font-size="13" font-weight="700">Secondary</text>

  <rect x="760" y="30" width="170" height="70" rx="10" fill="rgba(127,255,212,.15)" stroke="#7fffd4" stroke-opacity=".45"/>
        <text x="845" y="60" text-anchor="middle" fill="#e0ffff" font-size="13" font-weight="700">Meta</text>

  <rect x="360" y="160" width="170" height="70" rx="10" fill="rgba(127,255,212,.15)" stroke="#7fffd4" stroke-opacity=".45"/>
        <text x="445" y="192" text-anchor="middle" fill="#e0ffff" font-size="13" font-weight="700">Sentiment</text>

  <rect x="560" y="160" width="170" height="70" rx="10" fill="rgba(127,255,212,.15)" stroke="#7fffd4" stroke-opacity=".45"/>
        <text x="645" y="192" text-anchor="middle" fill="#e0ffff" font-size="13" font-weight="700">Interaction</text>

  <rect x="760" y="160" width="170" height="70" rx="10" fill="rgba(127,255,212,.15)" stroke="#7fffd4" stroke-opacity=".45"/>
        <text x="845" y="192" text-anchor="middle" fill="#e0ffff" font-size="13" font-weight="700">Context</text>

  <g stroke="#a2f4ff" stroke-opacity=".7" stroke-width="2">
          <line x1="290" y1="110" x2="360" y2="65"/>
          <line x1="290" y1="110" x2="560" y2="65"/>
          <line x1="290" y1="110" x2="760" y2="65"/>
          <line x1="290" y1="150" x2="360" y2="195"/>
          <line x1="290" y1="150" x2="560" y2="195"/>
          <line x1="290" y1="150" x2="760" y2="195"/>
        </g>
      </svg>
    </div>
  </details>
</div>

<div class="section">
  <h2>🏆 Grand Performance Showcase</h2>
  <p>
    The evaluation deliberately pits generalist GoEmotions models against a specialist trained on Plutchik’s eight core emotions. The “unfairness” is instructive: it exposes the cost of vocabulary mismatch and the power of a psychologically aligned label space.
  </p>

  <h3>🧠 Emotional Lexicons: Why Translation Fails</h3>
  <ul>
    <li><strong>Missing Concepts.</strong> GoEmotions lacks dedicated pathways for Plutchik categories like <em>Trust</em> or <em>Anticipation</em> as defined here.</li>
    <li><strong>Forced Guesses.</strong> Inputs such as “I have complete faith in your plan” map to “Approval/Admiration,” not “Trust.” Close ≠ correct when precision matters.</li>
    <li><strong>Semantic Misalignment.</strong> The learned geometry of the label space differs; a round peg in a square hole.</li>
  </ul>

  <table class="ranking-table">
    <thead><tr><th>Model</th><th>F1 Macro</th></tr></thead>
    <tbody>
      <tr class="highlight-row"><td><strong>EMOTIONVERSE-2</strong></td><td><strong>0.951</strong> 🌟</td></tr>
      <tr><td>GoEmotions-RoBERTa</td><td>0.024 🔻</td></tr>
      <tr><td>GoEmotions-BERT</td><td>0.012 📉</td></tr>
      <tr><td>DistilBERT-Emotion</td><td>0.007 👻</td></tr>
    </tbody>
  </table>

  <div class="svg-frame" aria-label="Bar chart comparing F1 Macro">
    <svg viewBox="0 0 820 240" width="100%" height="auto" role="img">
      <desc>F1 Macro scores: EmotionVerse-2 0.951, GoEmotions-RoBERTa 0.024, GoEmotions-BERT 0.012, DistilBERT-Emotion 0.007</desc>
      <defs>
        <linearGradient id="bar" x1="0" x2="1">
          <stop offset="0" stop-color="#7fffd4"/><stop offset="1" stop-color="#a2f4ff"/>
        </linearGradient>
      </defs>
      <line x1="120" y1="190" x2="780" y2="190" stroke="rgba(255,255,255,.2)"/>
      <line x1="120" y1="30"  x2="120" y2="190" stroke="rgba(255,255,255,.2)"/>
      <g fill="#b0e0e6" font-size="12">
        <text x="115" y="205" text-anchor="end">0.0</text>
        <text x="350" y="205" text-anchor="middle">0.25</text>
        <text x="580" y="205" text-anchor="middle">0.50</text>
        <text x="780" y="205" text-anchor="middle">1.00</text>
      </g>
        <text x="20" y="70" fill="#e0ffff" font-weight="700">EmotionVerse-2</text>
        <rect x="120" y="50" width="627" height="26" rx="8" fill="url(#bar)"/>
        <text x="760" y="68" fill="#e0ffff" font-weight="700">0.951</text>
      </g>
      <g>
        <text x="20" y="110" fill="#b0e0e6">GoEmotions-RoBERTa</text>
        <rect x="120" y="92" width="16" height="20" rx="6" fill="url(#bar)" opacity=".5"/>
        <text x="150" y="108" fill="#b0e0e6">0.024</text>
      </g>
      <g>
        <text x="20" y="150" fill="#b0e0e6">GoEmotions-BERT</text>
        <rect x="120" y="132" width="8" height="20" rx="6" fill="url(#bar)" opacity=".45"/>
        <text x="140" y="148" fill="#b0e0e6">0.012</text>
      </g>
      <g>
        <text x="20" y="190" fill="#b0e0e6">DistilBERT-Emotion</text>
        <rect x="120" y="172" width="5" height="20" rx="6" fill="url(#bar)" opacity=".4"/>
        <text x="138" y="188" fill="#b0e0e6">0.007</text>
      </g>
    </svg>
  </div>

  <h3>💎 Nearly-Perfect Diagonal (Confusion Matrix)</h3>
  <p class="small">Diagonal dominance indicates surgical separation of Plutchik classes; off-diagonals remain low and psychologically adjacent when present.</p>
  <div class="svg-frame">
    <svg viewBox="0 0 560 260" width="100%" height="auto" role="img" aria-label="Confusion matrix heatmap">
      <defs>
        <linearGradient id="hot" x1="0" x2="0" y1="1" y2="0">
          <stop offset="0" stop-color="#203248"/><stop offset="1" stop-color="#7fffd4"/>
        </linearGradient>
      </defs>
      <g font-size="11" fill="#b0e0e6">
        <text x="110" y="18">Predicted →</text>
        <text transform="translate(12,150) rotate(-90)">Actual ↓</text>
      </g>
      <g font-size="11" fill="#e0ffff">
        <text x="110" y="38">Joy</text><text x="170" y="38">Trust</text><text x="230" y="38">Antic.</text><text x="290" y="38">Surpr.</text><text x="350" y="38">Anger</text><text x="410" y="38">Sad.</text><text x="470" y="38">Fear</text><text x="530" y="38">Disg.</text>
        <text x="60" y="66">Joy</text><text x="58" y="96">Trust</text><text x="54" y="126">Antic.</text><text x="54" y="156">Surpr.</text><text x="52" y="186">Anger</text><text x="62" y="216">Sad.</text><text x="62" y="246">Fear</text><text x="50" y="276">Disg.</text>
      </g>

  <g transform="translate(100,50)">
        <g fill="#7fffd4">
          <rect x="0"   y="0"   width="30" height="30" fill="#7fffd4" fill-opacity=".95"/>
          <rect x="30"  y="30"  width="30" height="30" fill="#7fffd4" fill-opacity=".94"/>
          <rect x="60"  y="60"  width="30" height="30" fill="#7fffd4" fill-opacity=".95"/>
          <rect x="90"  y="90"  width="30" height="30" fill="#7fffd4" fill-opacity=".96"/>
          <rect x="120" y="120" width="30" height="30" fill="#7fffd4" fill-opacity=".94"/>
          <rect x="150" y="150" width="30" height="30" fill="#7fffd4" fill-opacity=".95"/>
          <rect x="180" y="180" width="30" height="30" fill="#7fffd4" fill-opacity=".95"/>
          <rect x="210" y="210" width="30" height="30" fill="#7fffd4" fill-opacity=".95"/>
        </g>
        <g fill="#a2f4ff" fill-opacity=".18">
          <rect x="30"  y="0"   width="30" height="30"/>
          <rect x="0"   y="30"  width="30" height="30"/>
          <rect x="60"  y="30"  width="30" height="30"/>
          <rect x="90"  y="60"  width="30" height="30"/>
          <rect x="120" y="90"  width="30" height="30"/>
          <rect x="150" y="120" width="30" height="30"/>
        </g>
        <g stroke="rgba(255,255,255,.12)" stroke-width="1">
          <line x1="0" y1="0" x2="0" y2="240"/><line x1="30" y1="0" x2="30" y2="240"/><line x1="60" y1="0" x2="60" y2="240"/><line x1="90" y1="0" x2="90" y2="240"/>
          <line x1="120" y1="0" x2="120" y2="240"/><line x1="150" y1="0" x2="150" y2="240"/><line x1="180" y1="0" x2="180" y2="240"/><line x1="210" y1="0" x2="210" y2="240"/><line x1="240" y1="0" x2="240" y2="240"/>
          <line x1="0" y1="0" x2="240" y2="0"/><line x1="0" y1="30" x2="240" y2="30"/><line x1="0" y1="60" x2="240" y2="60"/><line x1="0" y1="90" x2="240" y2="90"/>
          <line x1="0" y1="120" x2="240" y2="120"/><line x1="0" y1="150" x2="240" y2="150"/><line x1="0" y1="180" x2="240" y2="180"/><line x1="0" y1="210" x2="240" y2="210"/><line x1="0" y1="240" x2="240" y2="240"/>
        </g>
      </g>
    </svg>
  </div>

  <details>
    <summary>Cross-task capability radar (SVG)</summary>
    <div class="svg-frame">
      <svg viewBox="0 0 360 300" width="100%" height="auto" role="img" aria-label="Capability radar: Precision, Recall, F1, Coherence, Stability">
        <defs>
          <linearGradient id="radar" x1="0" x2="1">
            <stop offset="0" stop-color="#7fffd4" stop-opacity=".4"/>
            <stop offset="1" stop-color="#a2f4ff" stop-opacity=".4"/>
          </linearGradient>
        </defs>
        <g transform="translate(180,150)">
          <!-- axes -->
          <g stroke="rgba(255,255,255,.2)">
            <polygon points="0,-120 114,-37 70,97 -70,97 -114,-37" fill="none"/>
            <polygon points="0,-90 86,-28 52,72 -52,72 -86,-28" fill="none"/>
            <polygon points="0,-60 57,-18 35,48 -35,48 -57,-18" fill="none"/>
            <polygon points="0,-30 29,-9 17,24 -17,24 -29,-9" fill="none"/>
          </g>
          <!-- labels -->
          <g fill="#e0ffff" font-size="12" text-anchor="middle">
            <text x="0" y="-140">Precision</text>
            <text x="134" y="-38">Recall</text>
            <text x="82" y="118">F1</text>
            <text x="-82" y="118">Coherence</text>
            <text x="-134" y="-38">Stability</text>
          </g>
          <!-- polygon values (approx: P=.96, R=.94, F1=.95, C=.97, S=.95) -->
          <polygon points="0,-115 107,-34 67,110 -67,110 -109,-35" fill="url(#radar)" stroke="#a2f4ff" stroke-opacity=".8"/>
        </g>
      </svg>
    </div>
  </details>
</div>

<div class="section">
  <h2>🔬 Architecture & Emotional Data Synthesis</h2>
  <h4>Core Modules</h4>
  <ul>
    <li><strong>Neural Plasticity Gate.</strong> Reweights hidden states conditioned on intensity and local valence/arousal; supports context-sensitive adaptation.</li>
    <li><strong>Amygdala-Inspired Intensifier.</strong> Saturating non-linearity emphasizes high-arousal signals without drowning low-arousal nuance.</li>
    <li><strong>GRU Memory Consolidator.</strong> Injects sequential emotional context to stabilize predictions across turns or sentences.</li>
    <li><strong>Circumplex Injector.</strong> Concatenates/merges valence-arousal (+ intensity) vectors into token-level or pooled embeddings.</li>
  </ul>

  <div class="hr"></div>

  <h4>Training Setup</h4>
  <ul>
    <li><strong>Backbone:</strong> BERT-base uncased.</li>
    <li><strong>Optimization:</strong> AdamW, linear warmup/decay, mixed precision.</li>
    <li><strong>Loss:</strong> Weighted sum across heads with dynamic task weights; focal term for rare labels; label smoothing for stability.</li>
    <li><strong>Regularization:</strong> Dropout, stochastic depth on head adapters (if enabled), gradient clipping.</li>
  </ul>
</div>

<div class="section">
  <h2>🚀 Psychologically-Informed Embeddings</h2>
  <p>Emotion labels are embedded vectors, not IDs. Selected dimensions:</p>
  <ul>
    <li><strong>Valence/Arousal Anchors.</strong> First two dims: positivity/negativity and activation.</li>
    <li><strong>Intensity Signal.</strong> Third dim calibrated from dataset statistics.</li>
    <li><strong>Family Centroids.</strong> Pull toward Plutchik family centers to preserve conceptual proximity.</li>
    <li><strong>Relationship Pull.</strong> Secondary affinities (e.g., Joy↔Anticipation) maintain a smooth manifold.</li>
  </ul>
</div>

<div class="section">
  <h2>📊 Evaluation & Performance Horizons</h2>
  <ul>
    <li><strong>Primary Head:</strong> Accuracy, Top-2 recall.</li>
    <li><strong>Secondary & Meta:</strong> Macro/Weighted F1.</li>
    <li><strong>Interaction & Context:</strong> Precision/Recall for communicative style cues.</li>
    <li><strong>Sentiment:</strong> Mixed-class accuracy with polarity overlap analysis.</li>
    <li><strong>Emotion Coherence Index:</strong> Cross-head valence/arousal agreement.</li>
  </ul>
</div>

<div class="section">
  <h2>🛠️ Usage & Integration</h2>

  <details open>
    <summary>Quickstart (Transformers)</summary>
    <pre><code class="language-python">from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

name = "ayjays132/EmotionVerse-2"
tok  = AutoTokenizer.from_pretrained(name)
mdl  = AutoModelForSequenceClassification.from_pretrained(name)

text = "I’m thrilled yet anxious about tomorrow’s launch."
batch = tok(text, return_tensors="pt", truncation=True, padding=True)
with torch.no_grad():
    out = mdl(**batch)

</code></pre>
  </details>

  <details>
    <summary>Example: Plutchik mapping & softmax</summary>
    <pre><code class="language-python">import torch.nn.functional as F

plutchik_labels = ["joy","trust","anticipation","surprise","anger","sadness","fear","disgust"]
plutchik_logits = out.logits[:, :len(plutchik_labels)]  # slice depends on export
probs = F.softmax(plutchik_logits, dim=-1)[0].tolist()

for lbl, p in sorted(zip(plutchik_labels, probs), key=lambda x: -x[1]):
    print(f"{lbl:12s} {p:.3f}")
</code></pre>
  </details>

  <details>
    <summary>Batch inference with coherence check</summary>
    <pre><code class="language-python">def coherence(valence_arousal_primary, valence_arousal_sentiment):
    # cosine similarity across valence/arousal heads
    a, b = valence_arousal_primary, valence_arousal_sentiment
    return (a @ b) / ((a.norm()+1e-8) * (b.norm()+1e-8))

</code></pre>
  </details>
</div>

<div class="section">
  <h2>📂 EmotionVerse Dataset: Cosmic Fuel</h2>
  <p>
    The <a href="https://huggingface.co/datasets/ayjays132/Emotionverse" target="_blank">EmotionVerse</a> dataset anchors this model with 3K+ entries annotated across six dimensions, including meta-emotional and contextual narratives.
  </p>
</div>

<div class="section">
  <h2>📚 Reproducibility Snippets</h2>
  <details>
    <summary>Minimal training loop sketch</summary>
    <pre><code class="language-python">from torch.optim import AdamW
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()
optim  = AdamW(mdl.parameters(), lr=3e-5, weight_decay=0.01)

for step, batch in enumerate(train_loader):
    with autocast():
        out = mdl(**{k:v.to(mdl.device) for k,v in batch.items()})
        # combine task losses (weights dynamically updated)
        loss = out.loss  # if model returns weighted sum
    scaler.scale(loss).backward()
    scaler.step(optim); scaler.update(); optim.zero_grad()
</code></pre>
  </details>

  <details>
    <summary>Evaluation (macro F1) sketch</summary>
    <pre><code class="language-python">from sklearn.metrics import f1_score

      all_y, all_p = [], []
for batch in val_loader:
    with torch.no_grad():
        out = mdl(**{k:v.to(mdl.device) for k,v in batch.items()})
    logits = out.logits[:, :8]  # primary head slice
    preds  = logits.argmax(-1).cpu().tolist()
    all_p += preds; all_y += batch["labels"].tolist()

print("F1 Macro:", f1_score(all_y, all_p, average="macro"))
</code></pre>
  </details>
</div>

<div class="section">
  <h2>📜 Licensing</h2>
  <p>Released under the <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank">Apache 2.0 License</a>. Use, modify, and ship with confidence.</p>
</div>

<div class="section">
  <h2>🙏 Acknowledgements</h2>
  <p>Thanks to Hugging Face (<code>transformers</code>, <code>datasets</code>) and the research community advancing affective computing, psychological modeling, and trustworthy NLP.</p>
</div>

</div>