import pandas as pd


def rank_assets(factor_data):
    """
    Rank assets cross-sectionally for each date.

    Parameters
    ----------
    factor_data : pd.DataFrame
        DataFrame of factor values (e.g. momentum) with dates as index
        and tickers as columns.

    Returns
    -------
    pd.DataFrame
        DataFrame of ranks where 1 = strongest asset on that date.
    """
    if factor_data.empty:
        raise ValueError("Factor data is empty.")

    ranks = factor_data.rank(axis=1, ascending=False, method="min")

    return ranks
