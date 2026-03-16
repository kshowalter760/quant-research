import matplotlib.pyplot as plt
import pandas as pd


def plot_price_and_emas(
    data: pd.DataFrame,
    fast_ema: int,
    slow_ema: int,
    ticker: str = ""
) -> None:
    fast_col = f"ema_{fast_ema}"
    slow_col = f"ema_{slow_ema}"

    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"], label="Close")
    plt.plot(data.index, data[fast_col], label=f"EMA {fast_ema}")
    plt.plot(data.index, data[slow_col], label=f"EMA {slow_ema}")

    title = f"Price with EMA({fast_ema}, {slow_ema})"
    if ticker:
        title = f"{ticker} - {title}"

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_equity_curves(
    data: pd.DataFrame,
    ticker: str = "",
    fast_ema: int | None = None,
    slow_ema: int | None = None
) -> None:
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["strategy_equity"], label="Strategy Equity")
    plt.plot(data.index, data["buy_and_hold_equity"], label="Buy and Hold Equity")

    title = "Strategy Equity vs Buy-and-Hold"
    if ticker and fast_ema is not None and slow_ema is not None:
        title = f"{ticker} - EMA({fast_ema}, {slow_ema}) - {title}"
    elif ticker:
        title = f"{ticker} - {title}"

    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Equity Growth")
    plt.legend()
    plt.tight_layout()
    plt.show()
