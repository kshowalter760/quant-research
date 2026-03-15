import matplotlib.pyplot as plt
import pandas as pd


def plot_price_and_emas(data: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["Close"], label="Close")
    plt.plot(data.index, data["EMA_7"], label="EMA 7")
    plt.plot(data.index, data["EMA_21"], label="EMA 21")
    plt.title("Price with 7-Day and 21-Day EMAs")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.tight_layout()
    plt.show()


def plot_equity_curves(data: pd.DataFrame) -> None:
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data["strategy_equity"], label="Strategy Equity")
    plt.plot(data.index, data["buy_and_hold_equity"], label="Buy and Hold Equity")
    plt.title("Strategy Equity vs Buy-and-Hold")
    plt.xlabel("Date")
    plt.ylabel("Equity Growth")
    plt.legend()
    plt.tight_layout()
    plt.show()
