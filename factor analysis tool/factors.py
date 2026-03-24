import pandas as pd


def compute_momentum(data, lookback=63):
    """
    Compute momentum as trailing return over a specified lookback period.

    Parameters
    ----------
    data : pd.DataFrame
        Price DataFrame with dates as index and tickers as columns.
    lookback : int
        Number of trading days to look back.

    Returns
    -------
    pd.DataFrame
        Momentum DataFrame with the same shape as input data.
    """
    if data.empty:
        raise ValueError("Input price data is empty.")

    return data.pct_change(periods=lookback)


def compute_composite_momentum(data, lookbacks=(63, 126, 252)):
    """
    Compute composite momentum by averaging momentum signals
    across multiple lookback periods.

    Parameters
    ----------
    data : pd.DataFrame
        Price DataFrame with dates as index and tickers as columns.
    lookbacks : tuple
        Tuple of lookback periods in trading days.

    Returns
    -------
    pd.DataFrame
        Composite momentum DataFrame.
    """
    if data.empty:
        raise ValueError("Input price data is empty.")

    if len(lookbacks) == 0:
        raise ValueError("At least one lookback period must be provided.")

    momentum_list = [data.pct_change(periods=lb) for lb in lookbacks]
    composite_momentum = sum(momentum_list) / len(momentum_list)

    return composite_momentum
