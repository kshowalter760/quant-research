import numpy as np
from config import *

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


def run_simulations():
    results = []

    for _ in range(SIMULATIONS):
        equity = simulate_equity()
        results.append(equity)

    return results


def get_final_capitals(results):
    return [equity[-1] for equity in results]
