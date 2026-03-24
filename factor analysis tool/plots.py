import matplotlib.pyplot as plt


def plot_equity_curves(results):
    """
    Plot equity curves for the momentum strategy, equal-weight benchmark,
    and SPY benchmark.

    Parameters
    ----------
    results : pd.DataFrame
        Backtest results DataFrame containing:
        - strategy_equity
        - equal_weight_equity
        - spy_equity
    """
    required_columns = ["strategy_equity", "equal_weight_equity", "spy_equity"]

    for col in required_columns:
        if col not in results.columns:
            raise ValueError(f"Missing required column: {col}")

    plt.figure(figsize=(12, 6))
    plt.plot(results.index, results["strategy_equity"], label="Momentum Strategy")
    plt.plot(results.index, results["equal_weight_equity"], label="Equal Weight")
    plt.plot(results.index, results["spy_equity"], label="SPY")

    plt.title("Equity Curves Comparison")
    plt.xlabel("Date")
    plt.ylabel("Growth of $1")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
