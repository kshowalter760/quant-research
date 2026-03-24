# Quant-Research

A collection of Python tools for quantitative trading research and strategy development.
This repository explores core concepts in systematic investing, including portfolio construction, simulation, backtesting, and factor-based strategies.

---
## Projects

### Portfolio Analysis Tool (Portfolio Lab)
A portfolio analysis framework for evaluating multi-asset portfolios using risk and return metrics.

Features:
* multi-asset portfolio construction (equal/custom weights)
* return and volatility calculations
* Sharpe ratio and max drawdown
* correlation matrix analysis
* diversification insights

Focus: understanding how asset combinations impact overall portfolio performance and risk.
---
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
* parameter sweeps and comparison
* performance metrics (return, volatility, Sharpe, drawdown)

Focus: building and evaluating rule-based trading strategies.
---
### Factor Analysis Tool

A signal-driven portfolio construction system based on momentum factors.

Features:
* composite momentum (3m / 6m / 12m)
* cross-sectional asset ranking
* top-N asset selection
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
* portfolio construction and diversification
* correlation and risk management
* compounding and return modeling
* Monte Carlo simulation
* backtesting methodology
* factor investing
* dynamic allocation strategies
---
## Purpose

This repository is a structured learning and portfolio-building project focused on developing practical skills in:
* quantitative finance
* data-driven strategy design
* Python for financial analysis

Each project builds on the previous one, progressing from:
→ portfolio analysis
→ simulation and risk modeling
→ strategy backtesting
→ factor-based allocation
---

## Future Improvements
* multi-factor models
* transaction cost modeling
* optimization techniques
* machine learning applications in finance
---

## Notes
This repository is intended for educational and research purposes only and does not constitute financial advice.


