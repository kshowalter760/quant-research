import pandas as pd


def run_backtest(prices, weights):
    """
    Run a simple portfolio backtest using daily returns and portfolio weights.

    Parameters
    ----------
    prices : pd.DataFrame
        Price data with dates as index and tickers as columns.
    weights : pd.DataFrame
        Portfolio weights with dates as index and tickers as columns.

    Returns
    -------
    pd.DataFrame
        DataFrame containing:
        - portfolio_return
        - strategy_equity
        - equal_weight_return
        - equal_weight_equity
        - spy_return
        - spy_equity
    """
    if prices.empty:
        raise ValueError("Price data is empty.")

    if weights.empty:
        raise ValueError("Weights data is empty.")

    # Daily asset returns
    asset_returns = prices.pct_change()

    # Shift weights forward by 1 day to avoid look-ahead bias
    shifted_weights = weights.shift(1)

    # Strategy daily returns
    portfolio_returns = (shifted_weights * asset_returns).sum(axis=1)

    # Equal-weight benchmark across all assets
    equal_weight_returns = asset_returns.mean(axis=1)

    # SPY benchmark
    if "SPY" not in prices.columns:
        raise ValueError("SPY must be in price data for benchmark comparison.")

    spy_returns = asset_returns["SPY"]

    # Equity curves
    strategy_equity = (1 + portfolio_returns.fillna(0)).cumprod()
    equal_weight_equity = (1 + equal_weight_returns.fillna(0)).cumprod()
    spy_equity = (1 + spy_returns.fillna(0)).cumprod()

    results = pd.DataFrame({
        "portfolio_return": portfolio_returns,
        "strategy_equity": strategy_equity,
        "equal_weight_return": equal_weight_returns,
        "equal_weight_equity": equal_weight_equity,
        "spy_return": spy_returns,
        "spy_equity": spy_equity
    })

    return results
