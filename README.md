# quant-research

A collection of Python tools for quantitative trading research and risk analysis. This repository contains small projects exploring concepts used in systematic trading such as simulation, backtesting, and portfolio analysis.

---

## Projects

### Monte Carlo Risk Simulator

Simulates trading outcomes to study:

- variance  
- drawdowns  
- risk of ruin  
- distribution of equity curves  

---

### EMA Strategy Backtester

A modular Python backtesting engine for evaluating an exponential moving average (EMA) crossover strategy using historical market data.

Features include:

- signal generation using EMA crossovers  
- strategy backtesting and equity curve simulation  
- performance metrics (return, volatility, Sharpe ratio, drawdown)  
- multi-asset testing  
- EMA parameter sweeps  
- ranked performance summary tables  

---

### Portfolio Analysis Tool

A portfolio construction and analysis engine for evaluating multi-asset allocations.

Features include:

- historical data retrieval using `yfinance`  
- daily return calculation for multiple assets  
- portfolio return aggregation using custom weights  
- equity curve construction  
- performance metrics:
  - total return  
  - annualized return  
  - volatility  
  - Sharpe ratio  
  - maximum drawdown  
- correlation matrix calculation and heatmap visualization  
- comparison of portfolio vs individual asset performance  
- multi-portfolio comparison framework  
- ranked portfolio performance table  
- CSV export of results  

Example use cases:

- comparing different allocation strategies  
- analyzing diversification effects  
- evaluating risk vs return tradeoffs  
- experimenting with portfolio construction ideas  

---

## Purpose

The goal of this repository is to build practical tools that demonstrate key ideas in quantitative finance such as:

- expected value  
- variance and volatility  
- drawdowns  
- risk analysis  
- strategy evaluation  
- performance analysis utilities  
- strategy comparison frameworks  
- portfolio construction and diversification  
