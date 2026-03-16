# EMA Strategy Backtester

This project implements a simple Python backtesting engine for evaluating systematic trading strategies using historical market data.

The example strategy uses an **exponential moving average (EMA) crossover** to generate trading signals.

The backtester supports **multiple assets and multiple EMA parameter configurations**, allowing basic strategy research and comparison across different settings.

---

# Features

- Downloads historical market data using Yahoo Finance
- Calculates exponential moving averages
- Generates trading signals
- Simulates strategy returns
- Builds an equity curve
- Computes key performance metrics
- Supports **multi-asset backtesting**
- Supports **EMA parameter sweeps**
- Produces a **ranked performance summary table**
- Saves experiment results to CSV
- Visualizes price data and strategy performance

---

# Strategy Logic

The strategy follows a standard EMA crossover rule:

EMA(fast) > EMA(slow)  → Long  
EMA(fast) < EMA(slow)  → Short  

Signals are shifted forward by one period when calculating returns to avoid **look-ahead bias**.

---

# Parameter Sweep

The backtester can evaluate multiple EMA configurations automatically.

Example configurations used in this project:

(3, 10)  
(5, 21)  
(12, 30)  
(21, 50)

These parameter combinations are tested across multiple assets:

SPY  
QQQ  
AAPL  
MSFT

Results are summarized and ranked to identify the strongest configurations.

---

# Performance Metrics

The backtester calculates several commonly used performance statistics:

- Total return
- Annualized return
- Volatility
- Sharpe ratio
- Maximum drawdown

These metrics allow comparison of strategies on both **absolute return** and **risk-adjusted performance**.

---

# Example Output

Running the backtester produces:

- A **summary table comparing all tested strategies**
- A **ranked list of the best configurations by Sharpe ratio**
- Optional visualizations including:
  - price with EMAs
  - strategy equity curve vs buy-and-hold

Results from the parameter sweep are also saved to:

ema_parameter_sweep_results.csv

---

# How to Run

Install dependencies:

pip install yfinance pandas matplotlib

Run the backtest:

python main.py

---

# Project Structure

strategy_backtester/

main.py        # orchestrates experiments and parameter sweeps  
strategy.py    # EMA signal generation  
backtest.py    # strategy return simulation  
metrics.py     # performance calculations  
plots.py       # visualization utilities  
results/       # saved experiment outputs (CSV)

---

# Purpose

This project demonstrates the basic workflow used in quantitative trading research:

Market Data  
→ Signal Generation  
→ Backtesting  
→ Performance Evaluation  
→ Parameter Testing  

It is part of a larger repository exploring **quantitative finance concepts, strategy evaluation, and risk analysis**.

---

# Future Improvements

Future improvements may include:

- portfolio-level backtesting
- position sizing models
- additional technical indicators
- expanded strategy comparison tools
