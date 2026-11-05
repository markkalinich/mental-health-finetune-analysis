---
library_name: transformers
tags:
- finance
- sentiment-analysis
- text-classification
- market-impact
- gated-fusion
- multitask-learning
- event-study
datasets:
- NickyNicky/finance-financialmodelingprep-stock-news-sentiments-rss-feed
- siddharthmb/stocks-ohlcv
license: mit
---

# FinImpact Direction1D V4

This repository contains a custom Hugging Face/PyTorch model for financial text impact modeling.
It combines a financial language encoder with market context features through a gated fusion head.
This v4 checkpoint is trained primarily as a 1-day market-impact signal model and adds return-aware auxiliary losses for directional-score alignment and confidence calibration.

## Task

Input:

- Financial news title/body
- Symbol-level market context available before the event date

Outputs:

- `direction_1d`: bearish / neutral / bullish future 1-day abnormal market reaction
- auxiliary diagnostics: `sentiment`, `direction_5d`, and `volatility` heads are still exported, but their default loss weights are zero in this v4 run.

## Architecture

- Encoder: `microsoft/deberta-v3-large`
- Pooling: attention-mask-aware mean pooling over `last_hidden_state`
- Text branch: LayerNorm -> Linear -> GELU -> Dropout
- Numeric branch: LayerNorm -> Linear -> GELU -> Dropout
- Fusion: learned sigmoid gate between text and numeric branches
- Heads: 1D direction classification head plus auxiliary diagnostic heads
- Return-aware training: `P(bullish) - P(bearish)` is softly aligned to realized 1-day abnormal return sign/magnitude

This is intentionally not an embedding-only classifier. The model fine-tunes a contextual encoder and learns a supervised 1-day market-impact boundary.

## Training Data

News source:

- `NickyNicky/finance-financialmodelingprep-stock-news-sentiments-rss-feed`
- Fields used: `symbol`, `publishedDate`, `title`, `text`, `sentiment`, `sentimentScore`

Price source:

- `siddharthmb/stocks-ohlcv`
- Daily close data used to build lagged market features and future-return labels.

Training rows after join: `13930`

Time split:

- train: `10865`
- validation: `1532`
- test: `1533`

Symbols:

`AAPL, ABNB, ADBE, ADI, ADP, AMAT, AMD, AMZN, ARKK, ASML, AVGO, BA, BABA, BAC, BIDU, BMY, CAT, CMCSA, COIN, COST, CRM, CSCO, CVX, DHR, DIS, ELF, GE, GM, GOOGL, HD, IBM, INTC, IOVA, JNJ, JPM, KO, LULU, MA, MCD, MDB, META, MRNA, MSFT, MU, NFLX, NKE, NVDA, ORCL, PEP, PFE, PLTR, PYPL, QCOM, RCL, SHOP, SNOW, SPOT, TGT, TSLA, TSM, TXN, UAL, UBER, UNH, UPS, WMT, XOM, ZM`

## Numeric Features

- `source_sentiment_score`
- `sentiment_abs_score`
- `site_benzinga`
- `site_globenewswire`
- `site_yahoo_finance`
- `site_marketwatch`
- `text_char_len`
- `title_char_len`
- `is_after_close`
- `is_premarket`
- `is_market_hours`
- `published_hour_sin`
- `published_hour_cos`
- `ret_1d_lag`
- `ret_5d_lag`
- `ret_20d_lag`
- `vol_5d`
- `vol_20d`
- `vol_60d`
- `vol_ratio_5_20`
- `drawdown_20d`
- `volume_z_20d`
- `sector_code`
- `market_ret_1d_lag`
- `market_ret_5d_lag`
- `sector_ret_1d_lag`
- `sector_ret_5d_lag`
- `beta_market_60d`
- `beta_sector_60d`

All numeric features are fit/scaled on the training split only.

## Label Construction

- `sentiment` comes from the source dataset label.
- `direction_1d` is generated from future 1-day beta-adjusted abnormal log return after the event anchor date.
- `direction_5d` is generated from future 5-day beta-adjusted abnormal log return.
- A return is neutral when it falls inside a volatility-adjusted threshold.
- `volatility` is based on train-split tertiles of future absolute 5-day return.

Event anchoring shifts after-close UTC news to the next calendar day and uses the next available trading date.
Duplicate same-symbol same-day event titles are removed before training.

## Test Metrics

```json
{
  "sentiment": {
    "accuracy": 0.009784735812133072,
    "macro_precision": 0.0032615786040443573,
    "macro_recall": 0.3333333333333333,
    "macro_f1": 0.006459948320413436,
    "confusion_matrix": [
      [
        0,
        110,
        0
      ],
      [
        0,
        15,
        0
      ],
      [
        0,
        1408,
        0
      ]
    ],
    "predicted_class_counts": {
      "bearish": 0,
      "neutral": 1533,
      "bullish": 0
    },
    "true_class_counts": {
      "bearish": 110,
      "neutral": 15,
      "bullish": 1408
    },
    "expected_calibration_error": 0.8247767172447622,
    "brier_score": 1.5716914553389048
  },
  "direction_1d": {
    "accuracy": 0.3333333333333333,
    "macro_precision": 0.2797514006239241,
    "macro_recall": 0.30693224852151285,
    "macro_f1": 0.28541099148120913,
    "confusion_matrix": [
      [
        31,
        217,
        212
      ],
      [
        54,
        138,
        244
      ],
      [
        124,
        171,
        342
      ]
    ],
    "predicted_class_counts": {
      "bearish": 209,
      "neutral": 526,
      "bullish": 798
    },
    "true_class_counts": {
      "bearish": 460,
      "neutral": 436,
      "bullish": 637
    },
    "expected_calibration_error": 0.03496117605077468,
    "brier_score": 0.6723385830557309
  },
  "direction_5d": {
    "accuracy": 0.45857795172863663,
    "macro_precision": 0.28120269843193446,
    "macro_recall": 0.33741824434028733,
    "macro_f1": 0.30491929241175314,
    "confusion_matrix": [
      [
        0,
        123,
        143
      ],
      [
        0,
        553,
        311
      ],
      [
        0,
        253,
        150
      ]
    ],
    "predicted_class_counts": {
      "bearish": 0,
      "neutral": 929,
      "bullish": 604
    },
    "true_class_counts": {
      "bearish": 266,
      "neutral": 864,
      "bullish": 403
    },
    "expected_calibration_error": 0.024249568105288305,
    "brier_score": 0.633983250156182
  },
  "volatility": {
    "accuracy": 0.39921722113502933,
    "macro_precision": 0.13307240704500978,
    "macro_recall": 0.3333333333333333,
    "macro_f1": 0.1902097902097902,
    "confusion_matrix": [
      [
        0,
        534,
        0
      ],
      [
        0,
        612,
        0
      ],
      [
        0,
        387,
        0
      ]
    ],
    "predicted_class_counts": {
      "lower_vol": 0,
      "normal_vol": 1533,
      "higher_vol": 0
    },
    "true_class_counts": {
      "lower_vol": 534,
      "normal_vol": 612,
      "higher_vol": 387
    },
    "expected_calibration_error": 0.1760233100613036,
    "brier_score": 0.712886643106662
  },
  "event_backtest": {
    "split": "test",
    "transaction_cost_bps": 10.0,
    "active_1d_fraction": 0.6568819308545336,
    "hit_ratio_1d_active": 0.5789473684210527,
    "avg_signal_return_1d_all": 0.0023507131510749455,
    "avg_signal_return_1d_all_net": 0.0016938312202204116,
    "avg_signal_return_1d_active": 0.0035785931088360393,
    "avg_signal_return_1d_active_net": 0.002578593108836038,
    "avg_abnormal_signal_return_1d_all": 0.0007162017627715418,
    "avg_abnormal_signal_return_1d_all_net": 5.93198319170076e-05,
    "avg_abnormal_signal_return_1d_active": 0.0010903051661656142,
    "avg_abnormal_signal_return_1d_active_net": 9.030516616561321e-05,
    "soft_signal_backtest_1d": {
      "mean_abs_signal": 0.049029190093278885,
      "active_fraction_abs_score_ge_0.10": 0.11545988258317025,
      "hit_ratio_all_gross": 0.532941943900848,
      "hit_ratio_active_gross": 0.4463276836158192,
      "avg_signal_return_all": -4.1903094825102016e-05,
      "avg_signal_return_all_net": -9.093229164136574e-05,
      "avg_abnormal_signal_return_all": 6.6492548285168596e-06,
      "avg_abnormal_signal_return_all_net": -4.237994289724156e-05
    },
    "active_5d_fraction": 0.39399869536855836,
    "hit_ratio_5d_active": 0.3708609271523179,
    "avg_signal_return_5d_all": -0.004762698527096634,
    "avg_signal_return_5d_active": -0.012088107354369436,
    "confidence_backtests_1d": {
      "top_10pct_directional_confidence": {
        "num_events": 153,
        "mean_confidence": 0.40472039580345154,
        "hit_ratio": 0.48366013071895425,
        "avg_signal_return": -0.0017291086948829782,
        "avg_signal_return_net": -0.002729108694882979,
        "median_signal_return": -0.0011537353275343776,
        "avg_abnormal_signal_return": 0.0023775517351216227,
        "avg_abnormal_signal_return_net": 0.001377551735121622
      },
      "top_20pct_directional_confidence": {
        "num_events": 307,
        "mean_confidence": 0.39327916502952576,
        "hit_ratio": 0.46579804560260585,
        "avg_signal_return": -0.0018346647964980064,
        "avg_signal_return_net": -0.0028346647964980075,
        "median_signal_return": -0.001494303229264915,
        "avg_abnormal_signal_return": 0.00013626769358741198,
        "avg_abnormal_signal_return_net": -0.0008637323064125889
      },
      "top_30pct_directional_confidence": {
        "num_events": 460,
        "mean_confidence": 0.3858344554901123,
        "hit_ratio": 0.5021739130434782,
        "avg_signal_return": 0.000168503345380684,
        "avg_signal_return_net": -0.0008314966546193169,
        "median_signal_return": 0.00047751690726727247,
        "avg_abnormal_signal_return": -0.0006967808645482443,
        "avg_abnormal_signal_return_net": -0.0016967808645482452
      },
      "threshold_0.34": {
        "num_events": 1108,
        "coverage": 0.7227658186562296,
        "hit_ratio": 0.5523465703971119,
        "avg_signal_return": 0.002400788538323842,
        "avg_signal_return_net": 0.001400788538323841,
        "median_signal_return": 0.0029742957558482885,
        "avg_abnormal_signal_return": 0.00043566977963306825,
        "avg_abnormal_signal_return_net": -0.0005643302203669326
      },
      "threshold_0.36": {
        "num_events": 636,
        "coverage": 0.41487279843444225,
        "hit_ratio": 0.5471698113207547,
        "avg_signal_return": 0.001725182487273244,
        "avg_signal_return_net": 0.000725182487273243,
        "median_signal_return": 0.0027859483379870653,
        "avg_abnormal_signal_return": -0.0001395135721791607,
        "avg_abnormal_signal_return_net": -0.0011395135721791617
      },
      "threshold_0.38": {
        "num_events": 247,
        "coverage": 0.16112198303979125,
        "hit_ratio": 0.44129554655870445,
        "avg_signal_return": -0.0028902063559107334,
        "avg_signal_return_net": -0.0038902063559107343,
        "median_signal_return": -0.0022296553943306208,
        "avg_abnormal_signal_return": 0.0008437850360328761,
        "avg_abnormal_signal_return_net": -0.00015621496396712474
      },
      "threshold_0.40": {
        "num_events": 85,
        "coverage": 0.055446836268754074,
        "hit_ratio": 0.43529411764705883,
        "avg_signal_return": -0.0034284473146887168,
        "avg_signal_return_net": -0.004428447314688717,
        "median_signal_return": -0.0031941309571266174,
        "avg_abnormal_signal_return": 0.0008126156158087884,
        "avg_abnormal_signal_return_net": -0.00018738438419121242
      },
      "threshold_0.42": {
        "num_events": 20,
        "coverage": 0.01304631441617743,
        "hit_ratio": 0.25,
        "avg_signal_return": -0.008969856356270612,
        "avg_signal_return_net": -0.009969856356270613,
        "median_signal_return": -0.011959618888795376,
        "avg_abnormal_signal_return": -0.0006033775032847188,
        "avg_abnormal_signal_return_net": -0.0016033775032847197
      },
      "threshold_0.45": {
        "num_events": 2,
        "coverage": 0.001304631441617743,
        "hit_ratio": 0.5,
        "avg_signal_return": 0.0010717622935771942,
        "avg_signal_return_net": 7.176229357719333e-05,
        "median_signal_return": 0.0010717622935771942,
        "avg_abnormal_signal_return": 0.01302456425037235,
        "avg_abnormal_signal_return_net": 0.01202456425037235
      },
      "threshold_0.50": {
        "num_events": 0,
        "coverage": 0.0,
        "hit_ratio": null,
        "avg_signal_return": null,
        "avg_signal_return_net": null,
        "median_signal_return": null,
        "avg_abnormal_signal_return": null,
        "avg_abnormal_signal_return_net": null
      }
    },
    "mean_text_gate_weight": 0.506599485874176,
    "std_text_gate_weight": 0.0016385371563956141
  }
}
```

The `confidence_backtests_1d` section ranks events by directional confidence, where directional confidence is `max(P(bearish), P(bullish))`.
This is the preferred way to inspect whether the model is useful as a signal filter.
V4 also reports cost-adjusted backtest fields using `10.0` bps per active directional event.

## Important Limitations

This is a research model, not trading advice.

Known limitations:

- Public news sentiment labels can be noisy.
- Daily OHLCV alignment is an approximation; intraday timestamp alignment would be better.
- Market-direction labels are derived from future returns and are sensitive to threshold choice.
- Results should be evaluated out-of-sample by date and by ticker before any practical use.

## Files

- `pytorch_model.bin`: custom gated-fusion model weights.
- `training_config.json`: training and dataset configuration.
- `feature_schema.json`: numeric feature scaler and schema.
- `label_mapping.json`: task label names.
- `metrics.json`: train/validation/test metrics.
- `test_predictions.csv`: event-level test predictions and returns.
- `top_10pct_directional_confidence_1d` in `test_predictions.csv`: marks the highest-confidence directional event subset.
- `confusion_matrix_*.csv`: confusion matrices per split/task.
