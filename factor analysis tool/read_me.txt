# Factor Analysis Tool

A Python-based quantitative research tool that constructs and evaluates a momentum-driven portfolio using cross-sectional ranking and monthly rebalancing.

## Overview

This project implements a simple but powerful **factor investing workflow**:

Market Data
→ Factor Calculation (Momentum)
→ Asset Ranking
→ Portfolio Construction
→ Backtesting
→ Performance Evaluation

The strategy dynamically allocates capital to the strongest-performing assets based on momentum signals.

---

## Strategy Logic

### Factor: Momentum

Momentum is defined as the past return over multiple lookback periods:

* 3-month (63 trading days)
* 6-month (126 trading days)
* 12-month (252 trading days)

A **composite momentum score** is computed by averaging these signals.

---

### Ranking

* Assets are ranked cross-sectionally on each date
* Highest momentum = rank 1

---

### Portfolio Construction

* Select top N assets (default: 2)
* Equal-weight allocation among selected assets
* Rebalance monthly (end-of-month)

---

### Backtesting

* Daily returns computed from price data
* Portfolio weights are **shifted forward by one day** to avoid look-ahead bias
* Equity curves are generated via compounding

Benchmarks:

* Equal-weight portfolio (all assets)
* SPY (market benchmark)

---

## Performance Metrics

The following metrics are calculated:

* Total Return
* Annualized Return
* Volatility
* Sharpe Ratio
* Maximum Drawdown

Results are exported to:

```bash
factor_metrics.csv
```

---

## Visualization

* Equity curve comparison:

  * Momentum Strategy
  * Equal Weight
  * SPY

---

## Project Structure

```bash
factor_analysis_tool/
│
├── main.py
├── data_loader.py
├── factors.py
├── ranking.py
├── portfolio.py
├── backtest.py
├── metrics.py
├── plots.py
└── README.md
```

---

## Example Asset Universe

* SPY (S&P 500)
* QQQ (Nasdaq-100)
* EEM (Emerging Markets)
* GLD (Gold)
* TLT (Treasury Bonds)
* VNQ (Real Estate)

---

## Key Concepts Demonstrated

* Factor investing
* Momentum signals
* Cross-sectional ranking
* Dynamic portfolio allocation
* Monthly rebalancing
* Backtesting methodology
* Risk and performance analysis

---

## Future Improvements

* Multiple factor integration (volatility, mean reversion)
* Transaction cost modeling
* Turnover analysis
* Rolling performance metrics
* Parameter sensitivity testing

---

## Purpose

This project is part of a broader quantitative research toolkit designed to explore systematic trading strategies and build practical experience in:

* financial data analysis
* strategy development
* performance evaluation
* Python-based research workflows
