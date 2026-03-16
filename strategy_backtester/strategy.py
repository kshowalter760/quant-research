import pandas as pd


def generate_signals(
    data: pd.DataFrame,
    fast_ema: int = 7,
    slow_ema: int = 21
) -> pd.DataFrame:
    df = data.copy()

    df[f"ema_{fast_ema}"] = df["Close"].ewm(span=fast_ema, adjust=False).mean()
    df[f"ema_{slow_ema}"] = df["Close"].ewm(span=slow_ema, adjust=False).mean()

    df["signal"] = 0
    df.loc[df[f"ema_{fast_ema}"] > df[f"ema_{slow_ema}"], "signal"] = 1
    df.loc[df[f"ema_{fast_ema}"] < df[f"ema_{slow_ema}"], "signal"] = -1

    return df
