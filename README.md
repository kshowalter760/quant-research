# quant-research

A collection of Python tools for quantitative trading research and strategy development.

This repository explores core concepts in systematic investing, including simulation, backtesting, factor modeling, and risk analysis.

---

## Projects

### Monte Carlo Risk Simulator

Simulates trading strategy outcomes to analyze:

* variance and randomness
* equity curve distributions
* drawdowns and losing streaks
* risk of ruin

Focus: understanding uncertainty and probabilistic outcomes in trading systems.

---

### EMA Strategy Backtester

A modular backtesting engine for evaluating an EMA crossover strategy across multiple assets.

Features:

* signal generation using exponential moving averages
* multi-asset testing
* performance metrics (return, volatility, Sharpe, drawdown)
* parameter sweeps and result comparison

Focus: building and evaluating rule-based trading strategies.

---

### Factor Analysis Tool

A signal-driven portfolio construction framework based on momentum factors.

Features:

* composite momentum (3m / 6m / 12m)
* cross-sectional asset ranking
* top-N portfolio selection
* monthly rebalancing
* full backtesting pipeline
* performance metrics and visualization

Focus: transitioning from static portfolios to **dynamic, signal-based allocation**.

---

## Technologies Used

* Python
* pandas
* numpy
* yfinance
* matplotlib

---

## Key Concepts Covered

* compounding and return modeling
* volatility and risk measurement
* Monte Carlo simulation
* backtesting methodology
* factor investing
* portfolio construction
* performance evaluation

---

## Purpose

This repository is a structured learning and portfolio-building project focused on developing practical skills in:

* quantitative finance
* data-driven strategy design
* Python for financial analysis

Each project is designed to be:

* modular
* easy to extend
* grounded in real-world concepts

---

## Next Steps

Future additions may include:

* multi-factor models
* optimization techniques
* transaction cost modeling
* machine learning applications in finance

---

## Notes

This repository is intended for educational and research purposes only and does not constitute financial advice.

