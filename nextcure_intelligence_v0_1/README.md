# NextCure Intelligence System

Iteration 0.2 prototype for the Week 1 Market Positioning Layer.

## Scope

- Premium Streamlit shell
- One-button START ANALYSIS workflow
- Mock NXTC vs XBI vs QQQ relative performance view
- Mock six-month stock technical chart with price, EMA20/EMA50, RSI 14, and MACD
- Mock peer momentum table
- CEO-readable executive readout
- Modular architecture prepared for real market-data engines

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
streamlit run app.py
```

## Next iteration

Wire real data sources into `data/market_data.py`, then replace `engines/prototype_runner.py` mock calls with real orchestration. The technical chart contract is already isolated in `ui/charts.py`, so the future real-data swap should not require UI rewrites.
