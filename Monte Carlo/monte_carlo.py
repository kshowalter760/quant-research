import numpy as np
import matplotlib.pyplot as plt

# Strategy parameters
win_rate = 0.55
reward_risk = 1       # win = 1R
risk_per_trade = 0.01 # 1%

# Simulation parameters
starting_capital = 10000
trades = 500
simulations = 1000

final_capitals = []

for sim in range(simulations):

    capital = starting_capital

    for t in range(trades):

        risk = capital * risk_per_trade

        if np.random.rand() < win_rate:
            capital += risk * reward_risk
        else:
            capital -= risk

        if capital <= 0:
            capital = 0
            break

    final_capitals.append(capital)

print("Average final capital:", np.mean(final_capitals))
print("Median final capital:", np.median(final_capitals))

plt.hist(final_capitals, bins=50)
plt.title("Monte Carlo Final Capital Distribution")
plt.xlabel("Final Capital")
plt.ylabel("Frequency")
plt.show()

def simulate_equity():

    capital = starting_capital
    equity = [capital]

    for t in range(trades):

        risk = capital * risk_per_trade

        if np.random.rand() < win_rate:
            capital += risk * reward_risk
        else:
            capital -= risk

        equity.append(capital)

    return equity

for _ in range(20):

    equity = simulate_equity()
    plt.plot(equity)

plt.title("Monte Carlo Equity Paths")
plt.xlabel("Trades")
plt.ylabel("Capital")
plt.show()

ruin_threshold = starting_capital * 0.25
ruin_count = 0

for sim in range(simulations):

    equity = simulate_equity()

    if min(equity) < ruin_threshold:
        ruin_count += 1

print("Risk of ruin:", ruin_count / simulations)

def max_drawdown(equity):

    peak = equity[0]
    max_dd = 0

    for value in equity:

        if value > peak:
            peak = value

        drawdown = (peak - value) / peak

        if drawdown > max_dd:
            max_dd = drawdown

    return max_dd

dd = max_drawdown(simulate_equity())
print("Max drawdown:", dd)