# Quant-Research

A collection of Python tools for quantitative trading research, on-chain analysis, and strategy development. This repository explores core concepts in systematic investing, including portfolio construction, simulation, backtesting, factor-based strategies, and real-time blockchain signal detection.

---

## Projects

### Portfolio Analysis Tool (Portfolio Lab)

A portfolio analysis framework for evaluating multi-asset portfolios using risk and return metrics.

**Features:**

* multi-asset portfolio construction (equal/custom weights)
* return and volatility calculations
* Sharpe ratio and max drawdown
* correlation matrix analysis
* diversification insights

**Focus:** Understanding how asset combinations impact overall portfolio performance and risk.

---

### Monte Carlo Risk Simulator

Simulates trading strategy outcomes to analyze:

* variance and randomness
* equity curve distributions
* drawdowns and losing streaks
* risk of ruin

**Focus:** Understanding uncertainty and probabilistic outcomes in trading systems.

---

### EMA Strategy Backtester

A modular backtesting engine for evaluating an EMA crossover strategy across multiple assets.

**Features:**

* signal generation using exponential moving averages
* multi-asset testing
* parameter sweeps and comparison
* performance metrics (return, volatility, Sharpe, drawdown)

**Focus:** Building and evaluating rule-based trading strategies.

---

### Factor Analysis Tool

A signal-driven portfolio construction system based on momentum factors.

**Features:**

* composite momentum (3m / 6m / 12m)
* cross-sectional asset ranking
* top-N asset selection
* monthly rebalancing
* full backtesting pipeline
* performance metrics and visualization

**Focus:** Transitioning from static portfolios to dynamic, signal-based allocation.

---

### Arkham On-Chain Alert Bot

A real-time signal engine that monitors blockchain activity using the Arkham API and detects meaningful capital flows across centralized exchanges (CEXs) and decentralized protocols (DEXs).

**Features:**

* live on-chain data ingestion via API
* normalization of complex blockchain payloads
* entity classification (CEX, DEX, unlabeled wallets)
* exchange outflow detection (capital leaving exchanges)
* DEX stablecoin flow detection (potential deployment activity)
* repeated flow detection (pattern-based behavior analysis)
* Discord webhook integration for real-time alerts
* multi-layer filtering to isolate high-signal events

**Focus:** Transforming raw blockchain data into actionable signals by detecting behavioral patterns and capital movement in real time.

---

## Technologies Used

* Python
* pandas
* numpy
* yfinance
* matplotlib
* requests (API integration)

---

## Key Concepts Covered

* portfolio construction and diversification
* correlation and risk management
* compounding and return modeling
* Monte Carlo simulation
* backtesting methodology
* factor investing
* dynamic allocation strategies
* on-chain data analysis
* event-driven and pattern-based signal detection

---

## Purpose

This repository is a structured learning and portfolio-building project focused on developing practical skills in:

* quantitative finance
* data-driven strategy design
* Python for financial analysis
* real-time data processing and signal engineering

Each project builds on the previous one, progressing from:

→ portfolio analysis
→ simulation and risk modeling
→ strategy backtesting
→ factor-based allocation
→ real-time on-chain signal detection

---

## Future Improvements

* multi-factor models
* transaction cost modeling
* optimization techniques
* machine learning applications in finance
* real-time streaming (WebSocket-based ingestion)
* cloud deployment (e.g., DigitalOcean)

---

## Notes

This repository is intended for educational and research purposes only and does not constitute financial advice.



