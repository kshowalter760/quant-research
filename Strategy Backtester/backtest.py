import pandas as pd


def run_backtest(data: pd.DataFrame) -> pd.DataFrame:
    df = data.copy()

    # Daily market returns
    df["market_return"] = df["Close"].pct_change()

    # Use yesterday's signal for today's position
    df["position"] = df["signal"].shift(1)

    # Strategy returns
    df["strategy_return"] = df["position"] * df["market_return"]

    # Equity curves
    df["buy_and_hold_equity"] = (1 + df["market_return"]).cumprod()
    df["strategy_equity"] = (1 + df["strategy_return"]).cumprod()

    return df