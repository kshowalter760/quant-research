import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

pd.set_option("display.max_columns", None)
pd.set_option("display.width", 1200)


# ------------------------
# DATA FUNCTIONS
# ------------------------

def get_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end, auto_adjust=True)["Close"]
    return data


def compute_returns(data):
    returns = data.pct_change().dropna()
    return returns


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
    sharpe = annual_return / volatility if volatility != 0 else np.nan

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
# ANALYSIS / PLOTTING FUNCTIONS
# ------------------------

def plot_correlation(returns):
    corr = returns.corr()

    print("\nCorrelation Matrix:\n")
    print(corr.round(4).to_string())

    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Correlation Matrix")
    plt.show()


def plot_comparison(returns, equity_curve):
    individual_equity = (1 + returns).cumprod()

    plt.figure(figsize=(10, 5))

    for col in individual_equity.columns:
        plt.plot(individual_equity[col], alpha=0.5, label=col)

    plt.plot(equity_curve, linewidth=2, label="Portfolio")

    plt.legend()
    plt.title("Portfolio vs Individual Assets")
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.show()


def plot_equity_curve(equity_curve, title="Portfolio Equity Curve"):
    plt.figure(figsize=(10, 5))
    plt.plot(equity_curve)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.show()


def plot_manual_vs_monte_carlo(manual_equity, monte_carlo_equity, manual_name, monte_carlo_name):
    plt.figure(figsize=(10, 5))
    plt.plot(manual_equity, label=manual_name, linewidth=2)
    plt.plot(monte_carlo_equity, label=monte_carlo_name, linewidth=2)

    plt.legend()
    plt.title("Best Manual Portfolio vs Best Monte Carlo Portfolio")
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.show()


def plot_monte_carlo_scatter(mc_results):
    plt.figure(figsize=(10, 6))

    scatter = plt.scatter(
        mc_results["Volatility"],
        mc_results["Annual Return"],
        c=mc_results["Sharpe"]
    )

    best = mc_results.iloc[0]
    plt.scatter(
        best["Volatility"],
        best["Annual Return"],
        marker="*",
        s=300,
        label="Best Sharpe"
    )

    plt.colorbar(scatter, label="Sharpe Ratio")
    plt.legend()
    plt.title("Monte Carlo Portfolio Scatter Plot")
    plt.xlabel("Volatility")
    plt.ylabel("Annual Return")
    plt.show()


# ------------------------
# MONTE CARLO FUNCTION
# ------------------------

def generate_constrained_weights(num_assets, max_weight=0.35):
    while True:
        weights = np.random.random(num_assets)
        weights = weights / weights.sum()

        if weights.max() <= max_weight:
            return weights


def run_monte_carlo_portfolios(returns, num_portfolios, max_weight=0.35):
    results = []
    num_assets = returns.shape[1]

    for _ in range(num_portfolios):
        weights = generate_constrained_weights(num_assets, max_weight=max_weight)

        portfolio_returns, equity_curve = build_portfolio(returns, weights)
        metrics = compute_metrics(portfolio_returns, equity_curve)

        metrics["Weights"] = weights
        results.append(metrics)

    results_df = pd.DataFrame(results)
    return results_df


# ------------------------
# HELPER FUNCTION
# ------------------------

def format_weights(tickers, weights):
    return ", ".join(
        [f"{ticker}: {weight:.1%}" for ticker, weight in zip(tickers, weights)]
    )


# ------------------------
# MAIN EXECUTION
# ------------------------

tickers = ["SPY", "EEM", "TLT", "GLD", "DBC"]
start = "2023-01-01"
end = "2026-03-01"

data = get_data(tickers, start, end)
returns = compute_returns(data)

plot_correlation(returns)


# Order:
# [SPY, EEM, TLT, GLD, DBC]
# [BTC, ETH, SOL, XRP, LINK] DON'T FORGET TO ADJUST TRADING DAYS!

weights_list = [
    np.array([0.50, 0.20, 0.10, 0.10, 0.10]),  # Equity Growth Tilt/BTC Heavy
    np.array([0.20, 0.20, 0.20, 0.20, 0.20]),  # Equal Weight
    np.array([0.30, 0.15, 0.25, 0.20, 0.10]),  # Balanced Diversified
    np.array([0.00, 0.00, 0.00, 1, 0.00])   # Defensive Allocation/Alt Heavy
]

portfolio_names = [
    "Equity Growth Tilt",
    "Equal Weight",
    "Balanced Diversified",
    "Defensive Allocation"
]

results = []

for name, weights in zip(portfolio_names, weights_list):
    portfolio_returns, equity_curve = build_portfolio(returns, weights)
    metrics = compute_metrics(portfolio_returns, equity_curve)

    metrics["Portfolio"] = name
    metrics["Weights"] = weights
    metrics["Readable Weights"] = format_weights(tickers, weights)

    results.append(metrics)

results_df = pd.DataFrame(results)

results_df = results_df[
    ["Portfolio", "Readable Weights", "Total Return", "Annual Return", "Volatility", "Sharpe", "Max Drawdown"]
]

results_df = results_df.sort_values(by="Sharpe", ascending=False)

num_portfolios = 1000
max_weight = 0.99

mc_results = run_monte_carlo_portfolios(returns, num_portfolios, max_weight=max_weight)

mc_results["Readable Weights"] = mc_results["Weights"].apply(lambda w: format_weights(tickers, w))

mc_results = mc_results[
    ["Weights", "Readable Weights", "Total Return", "Annual Return", "Volatility", "Sharpe", "Max Drawdown"]
]

mc_results = mc_results.sort_values(by="Sharpe", ascending=False)

print("\nTop 10 Monte Carlo Portfolios by Sharpe:\n")
print(
    mc_results[["Annual Return", "Volatility", "Sharpe", "Max Drawdown", "Readable Weights"]]
    .head(10)
    .round(4)
    .to_string()
)

print("\nPortfolio Comparison:\n")
print(results_df.round(4).to_string())

best_name = results_df.iloc[0]["Portfolio"]
best_weights = weights_list[portfolio_names.index(best_name)]

best_portfolio_returns, best_equity_curve = build_portfolio(returns, best_weights)

best_mc_weights = mc_results.iloc[0]["Weights"]
best_mc_name = "Best Monte Carlo"

best_mc_returns, best_mc_equity_curve = build_portfolio(returns, best_mc_weights)

plot_comparison(returns, best_equity_curve)
plot_equity_curve(best_equity_curve, title=f"{best_name} Equity Curve")

plot_manual_vs_monte_carlo(
    best_equity_curve,
    best_mc_equity_curve,
    best_name,
    best_mc_name
)

plot_monte_carlo_scatter(mc_results)

results_df.to_csv("portfolio_results.csv", index=False)
mc_results.to_csv("monte_carlo_portfolios.csv", index=False)

print("\nResults exported to portfolio_results.csv")
print("Monte Carlo results exported to monte_carlo_portfolios.csv")
print(f"Monte Carlo max weight constraint used: {max_weight:.0%}")