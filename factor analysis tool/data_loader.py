import yfinance as yf
import pandas as pd


def load_price_data(tickers, start="2018-01-01", end="2025-01-01"):
    """
    Download adjusted close price data for a list of tickers.

    Parameters
    ----------
    tickers : list
        List of ticker symbols.
    start : str
        Start date in YYYY-MM-DD format.
    end : str
        End date in YYYY-MM-DD format.

    Returns
    -------
    pd.DataFrame
        DataFrame of adjusted closing prices with dates as index
        and tickers as columns.
    """
    data = yf.download(
        tickers,
        start=start,
        end=end,
        auto_adjust=True,
        progress=False
    )

    if data.empty:
        raise ValueError("No data was downloaded. Check tickers or date range.")

    # If multiple tickers are downloaded, yfinance returns a multi-index column structure.
    # We only want the Close prices.
    if isinstance(data.columns, pd.MultiIndex):
        if "Close" not in data.columns.get_level_values(0):
            raise ValueError("Close prices not found in downloaded data.")
        prices = data["Close"].copy()
    else:
        # Fallback for single ticker case
        prices = data[["Close"]].copy()
        prices.columns = tickers

    # Drop rows where all values are missing
    prices.dropna(how="all", inplace=True)

    # Optional: forward fill small gaps
    prices = prices.ffill()

    if prices.empty:
        raise ValueError("Price DataFrame is empty after cleaning.")

    return prices
