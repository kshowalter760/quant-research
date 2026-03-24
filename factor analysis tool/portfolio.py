import pandas as pd


def construct_portfolio(ranks, top_n=2, rebalance_frequency="M"):
    """
    Construct an equal-weight portfolio based on top N ranked assets,
    with optional periodic rebalancing.

    Parameters
    ----------
    ranks : pd.DataFrame
        DataFrame of asset ranks (1 = best).
    top_n : int
        Number of top assets to select.
    rebalance_frequency : str
        Rebalancing frequency:
        - "D" for daily
        - "M" for monthly

    Returns
    -------
    pd.DataFrame
        DataFrame of portfolio weights.
    """
    if ranks.empty:
        raise ValueError("Rank data is empty.")

    if top_n <= 0:
        raise ValueError("top_n must be greater than 0.")

    if rebalance_frequency not in ["D", "M"]:
        raise ValueError("rebalance_frequency must be 'D' or 'M'.")

    if rebalance_frequency == "D":
        rebalance_ranks = ranks.copy()
    else:
        # Use the last available trading day of each month
        rebalance_ranks = ranks.resample("ME").last()

    # Select top N assets on rebalance dates
    selected = rebalance_ranks <= top_n

    # Convert True/False to 1/0
    weights = selected.astype(int)

    # Normalize so selected assets sum to 1
    weights = weights.div(weights.sum(axis=1), axis=0)

    if rebalance_frequency == "M":
        # Expand monthly weights back to daily index and carry forward
        weights = weights.reindex(ranks.index).ffill()

    return weights
