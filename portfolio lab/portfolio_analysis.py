import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ------------------------
# DATA FUNCTIONS
# ------------------------

def get_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)["Close"]
    return data


def compute_returns(data):
    return data.pct_change().dropna()


# ------------------------
# PORTFOLIO FUNCTIONS
# ------------------------

def build_portfolio(returns, weights):
    portfolio_returns = returns.dot(weights)
    equity_curve = (1 + portfolio_returns).cumprod()
    return portfolio_returns, equity_curve


def compute_metrics(portfolio_returns, equity_curve):
    total_return = equity_curve.iloc[-1] - 1
    annual_return = portfolio_returns.mean() * 252
    volatility = portfolio_returns.std() * np.sqrt(252)
    sharpe = annual_return / volatility

    drawdown = (equity_curve / equity_curve.cummax()) - 1
    max_drawdown = drawdown.min()

    return {
        "Total Return": total_return,
        "Annual Return": annual_return,
        "Volatility": volatility,
        "Sharpe": sharpe,
        "Max Drawdown": max_drawdown
    }


# ------------------------
# ANALYSIS FUNCTIONS
# ------------------------

def plot_correlation(returns):
    corr = returns.corr()
    plt.figure(figsize=(6, 5))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()


def plot_comparison(returns, equity_curve):
    individual = (1 + returns).cumprod()

    plt.figure(figsize=(10, 5))

    for col in individual.columns:
        plt.plot(individual[col], alpha=0.5, label=col)

    plt.plot(equity_curve, linewidth=2, label="Portfolio")

    plt.legend()
    plt.title("Portfolio vs Individual Assets")
    plt.show()


# ------------------------
# MAIN EXECUTION
# ------------------------

if __name__ == "__main__":

    tickers = ["SPY", "QQQ", "AAPL", "MSFT"]
    start = "2018-01-01"
    end = "2023-01-01"

    weights = np.array([0.25, 0.25, 0.25, 0.25])

    data = get_data(tickers, start, end)
    returns = compute_returns(data)

    portfolio_returns, equity_curve = build_portfolio(returns, weights)

    metrics = compute_metrics(portfolio_returns, equity_curve)

    print("\nPortfolio Metrics:\n")
    for k, v in metrics.items():
        print(f"{k}: {round(v, 4)}")

    plot_correlation(returns)
    plot_comparison(returns, equity_curve)

    plt.figure(figsize=(10, 5))
    plt.plot(equity_curve)
    plt.title("Portfolio Equity Curve")
    plt.show()
