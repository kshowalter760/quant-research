#read_me

# EMA Strategy Backtester

This project implements a simple Python backtesting engine for evaluating systematic trading strategies using historical market data.

The example strategy uses a **7-day and 21-day exponential moving average (EMA) crossover** to generate trading signals.

When the short-term EMA crosses above the long-term EMA, the strategy takes a long position. When the short-term EMA crosses below the long-term EMA, the strategy exits or reverses the position.

## Features

* Downloads historical market data using Yahoo Finance
* Calculates exponential moving averages
* Generates trading signals
* Simulates strategy returns
* Builds an equity curve
* Computes key performance metrics
* Visualizes strategy performance

## Strategy Logic

```
EMA(7) > EMA(21)  → Long
EMA(7) < EMA(21)  → Short
```

Signals are shifted forward by one period to avoid look-ahead bias when calculating strategy returns.

## Performance Metrics

The backtester calculates several commonly used performance statistics:

* Total return
* Annualized return
* Volatility
* Sharpe ratio
* Maximum drawdown

## Example Output

Running the backtester produces:

* Price chart with EMA indicators
* Strategy equity curve vs buy-and-hold
* Printed performance metrics in the terminal

## How to Run

Install dependencies:

```
pip install yfinance pandas matplotlib
```

Run the backtest:

```
python main.py
```

## Project Structure

```
strategy_backtester/

main.py        # runs the backtest
strategy.py    # signal generation logic
backtest.py    # trade simulation and equity curve
metrics.py     # performance metrics
plots.py       # visualization functions
```

## Purpose

This project demonstrates the basic workflow used in quantitative trading research:

```
Market Data
→ Signal Generation
→ Backtesting
→ Performance Evaluation
```

It is part of a larger repository exploring quantitative finance concepts and trading system analysis.
