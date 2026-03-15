# Monte Carlo Trading Risk Simulator

This project implements a Monte Carlo simulation framework for analyzing the risk characteristics of trading strategies.

Monte Carlo simulation generates many possible trading paths using probabilistic outcomes. This allows researchers to study how a strategy may behave under different sequences of wins and losses.

The simulator models trade outcomes using configurable parameters such as win rate, payoff ratio, and position sizing.

## Features

* Simulates thousands of independent trading paths
* Models compounding returns over many trades
* Visualizes possible equity curve trajectories
* Analyzes the distribution of final capital outcomes
* Provides insight into variance and strategy risk

## Simulation Logic

Each trade outcome is generated probabilistically based on a specified win rate.

Example parameters:

```text
Win rate: 55%
Reward/Risk: 1:1
Risk per trade: 1% of capital
```

At each step:

```
capital_change = position_size × trade_outcome
```

The simulation repeats this process across many trades and many independent runs.

## Example Output

Running the simulator produces:

* Multiple simulated equity curves
* Distribution of final capital values across simulations

These visualizations help illustrate how randomness affects trading outcomes.

## How to Run

Install dependencies:

```
pip install numpy matplotlib
```

Run the simulation:

```
python main.py
```

## Project Structure

```
monte_carlo_risk/

main.py           # runs the simulation
simulation.py     # Monte Carlo engine
config.py         # strategy parameters
plots.py          # visualization functions
risk_metrics.py   # risk analysis utilities
```

## Purpose

Monte Carlo simulation is commonly used in quantitative finance to evaluate strategy robustness and risk.

This project demonstrates how randomness and variance impact trading performance, even when a strategy has a positive expected value.

The simulator is part of a broader repository exploring quantitative trading research and strategy evaluation.

