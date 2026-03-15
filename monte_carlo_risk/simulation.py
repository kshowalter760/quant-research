import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Strategy Parameters
# -----------------------------

WIN_RATE = 0.55
REWARD_RISK = 1
RISK_PER_TRADE = 0.01

STARTING_CAPITAL = 10000
TRADES = 500
SIMULATIONS = 1000


# -----------------------------
# Single Equity Simulation
# -----------------------------

def simulate_equity():

    capital = STARTING_CAPITAL
    equity = [capital]

    for _ in range(TRADES):

        risk = capital * RISK_PER_TRADE

        if np.random.rand() < WIN_RATE:
            capital += risk * REWARD_RISK
        else:
            capital -= risk

        equity.append(capital)

    return equity


# -----------------------------
# Run Monte Carlo Simulations
# -----------------------------

def run_simulations():

    results = []

    for _ in range(SIMULATIONS):

        equity = simulate_equity()
        results.append(equity)

    return results


# -----------------------------
# Plot Equity Curves
# -----------------------------

def plot_equity_curves(results):

    for equity in results[:20]:
        plt.plot(equity)

    plt.title("Monte Carlo Equity Paths")
    plt.xlabel("Trades")
    plt.ylabel("Capital")

    plt.show()


# -----------------------------
# Main Execution
# -----------------------------

if __name__ == "__main__":

    results = run_simulations()
    plot_equity_curves(results)
