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


def run_single_backtest(
    ticker: str,
    start_date: str,
    end_date: str,
    fast_ema: int,
    slow_ema: int,
    show_plots: bool = False
) -> dict:
    print(f"Running backtest for {ticker} | EMA({fast_ema}, {slow_ema})...")

    data = load_price_data(ticker, start_date, end_date)
    data = generate_signals(data, fast_ema=fast_ema, slow_ema=slow_ema)
    data = run_backtest(data)

    metrics = calculate_metrics(data)
    metrics["Ticker"] = ticker
    metrics["Fast EMA"] = fast_ema
    metrics["Slow EMA"] = slow_ema

    if show_plots:
        plot_price_and_emas(data, fast_ema=fast_ema, slow_ema=slow_ema, ticker=ticker)
        plot_equity_curves(data, ticker=ticker, fast_ema=fast_ema, slow_ema=slow_ema)

    return metrics


def format_results_table(results_df: pd.DataFrame) -> pd.DataFrame:
    formatted_df = results_df.copy()

    percent_columns = [
        "Total Return",
        "Annualized Return",
        "Volatility",
        "Max Drawdown",
    ]

    for col in percent_columns:
        formatted_df[col] = formatted_df[col].apply(
            lambda x: f"{x:.2%}" if pd.notna(x) else "NaN"
        )

    formatted_df["Sharpe Ratio"] = formatted_df["Sharpe Ratio"].apply(
        lambda x: f"{x:.2f}" if pd.notna(x) else "NaN"
    )

    return formatted_df


def main():
    print("Starting EMA parameter sweep...")

    tickers = ["SPY", "QQQ", "AAPL", "MSFT"]
    ema_pairs = [(3, 10), (5, 21), (12, 30), (21, 50)]
    start_date = "2020-01-01"
    end_date = "2025-01-01"

    results = []

    for ticker in tickers:
        for fast_ema, slow_ema in ema_pairs:
            try:
                metrics = run_single_backtest(
                    ticker=ticker,
                    start_date=start_date,
                    end_date=end_date,
                    fast_ema=fast_ema,
                    slow_ema=slow_ema,
                    show_plots=False
                )
                results.append(metrics)
            except Exception as e:
                print(f"Error running {ticker} EMA({fast_ema}, {slow_ema}): {e}")

    print(f"Completed runs: {len(results)}")

    if not results:
        print("No backtest results were generated.")
        return

    results_df = pd.DataFrame(results)

    column_order = [
        "Ticker",
        "Fast EMA",
        "Slow EMA",
        "Total Return",
        "Annualized Return",
        "Volatility",
        "Sharpe Ratio",
        "Max Drawdown",
    ]
    results_df = results_df[column_order]

    full_results_df = results_df.sort_values(
        by=["Ticker", "Sharpe Ratio"],
        ascending=[True, False]
    )

    print("\nEMA Parameter Sweep Results:")
    print(format_results_table(full_results_df).to_string(index=False))

    top_results_df = results_df.sort_values(
        by="Sharpe Ratio",
        ascending=False
    ).head(5)

    print("\nTop 5 Results by Sharpe Ratio:")
    print(format_results_table(top_results_df).to_string(index=False))

    formatted_full_results = format_results_table(full_results_df)
    formatted_full_results.to_csv("ema_parameter_sweep_results.csv", index=False)

    print("\nSaved full results to ema_parameter_sweep_results.csv")


if __name__ == "__main__":
    main()