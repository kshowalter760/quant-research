import pandas as pd


def generate_signals(data: pd.DataFrame) -> pd.DataFrame:

    df = data.copy()

    # Calculate EMAs
    df["EMA_7"] = df["Close"].ewm(span=7, adjust=False).mean()
    df["EMA_21"] = df["Close"].ewm(span=21, adjust=False).mean()

    # Generate signal
    df["signal"] = 0
    df.loc[df["EMA_7"] > df["EMA_21"], "signal"] = 1
    df.loc[df["EMA_7"] < df["EMA_21"], "signal"] = -1

    return df
