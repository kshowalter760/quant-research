# Portfolio Analysis Tool

A Python-based portfolio construction and analysis tool for evaluating multi-asset allocations using historical market data.

---

## Overview

This project builds a simple portfolio analysis engine that allows users to:

- construct portfolios using custom asset weights  
- analyze portfolio performance over time  
- compare multiple allocation strategies  
- study diversification and correlation effects  

It extends beyond single-strategy backtesting into **portfolio-level research and risk analysis**.

---

## Features

- historical price data retrieval using `yfinance`  
- daily return calculation for multiple assets  
- portfolio return aggregation using weighted allocations  
- equity curve construction  
- performance metrics:
  - total return  
  - annualized return  
  - volatility  
  - Sharpe ratio  
  - maximum drawdown  
- correlation matrix calculation and heatmap visualization  
- portfolio vs individual asset comparison  
- multi-portfolio comparison framework  
- ranked performance table  
- CSV export of results  

---

## Example Assets

Typical test set:

- SPY  
- QQQ  
- AAPL  
- MSFT  

---

## Example Portfolio Allocations

- Equal Weight  
- SPY Heavy  
- QQQ Heavy  
- Mixed Allocation  

---

## Key Concepts Demonstrated

- portfolio return aggregation  
- compounding and equity curves  
- volatility and risk measurement  
- drawdowns and capital preservation  
- Sharpe ratio (risk-adjusted return)  
- correlation and diversification  
- allocation-driven performance differences  

---

## Workflow

Market Data  
→ Return Calculation  
→ Portfolio Construction  
→ Performance Evaluation  
→ Portfolio Comparison  

---

## Purpose

The goal of this project is to build intuition around:

- how portfolio weights affect performance  
- the tradeoff between risk and return  
- the benefits and limitations of diversification  
- how to evaluate and compare multiple portfolios  

This serves as a foundation for more advanced topics such as portfolio optimization and position sizing.
