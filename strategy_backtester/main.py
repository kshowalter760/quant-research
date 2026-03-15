import yfinance as yf
import pandas as pd

from strategy import generate_signals
from backtest import run_backtest
from plots import plot_price_and_emas, plot_equity_curves
from metrics import calculate_metrics


def load_price_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    data = yf.download(ticker, start=start, end=end, auto_adjust=True)

    if data.empty:
        raise ValueError(f"No data returned for ticker {ticker}")

    return data


def main():
    print("Starting backtest...")

    ticker = "SPY"
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    data = load_price_data(ticker, start_date, end_date)
    data = generate_signals(data)
    data = run_backtest(data)

    metrics = calculate_metrics(data)

    print("\nBacktest results:")
    print(data[[
        "Close",
        "EMA_7",
        "EMA_21",
        "signal",
        "position",
        "market_return",
        "strategy_return",
        "strategy_equity"
    ]].tail())

    print("\nPerformance Metrics:")
    for metric_name, metric_value in metrics.items():
        if pd.isna(metric_value):
            print(f"{metric_name}: NaN")
        elif metric_name == "Sharpe Ratio":
            print(f"{metric_name}: {metric_value:.2f}")
        else:
            print(f"{metric_name}: {metric_value:.2%}")

    plot_price_and_emas(data)
    plot_equity_curves(data)


if __name__ == "__main__":
    main()
