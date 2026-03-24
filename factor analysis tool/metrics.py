import numpy as np
import pandas as pd


def calculate_total_return(equity_curve):
    """
    Calculate total return from an equity curve.
    """
    if equity_curve.empty:
        raise ValueError("Equity curve is empty.")

    return equity_curve.iloc[-1] / equity_curve.iloc[0] - 1


def calculate_annual_return(return_series, periods_per_year=252):
    """
    Calculate annualized return from a daily return series.
    """
    if return_series.empty:
        raise ValueError("Return series is empty.")

    return_series = return_series.dropna()

    if len(return_series) == 0:
        return np.nan

    compounded_growth = (1 + return_series).prod()
    n_periods = len(return_series)

    return compounded_growth ** (periods_per_year / n_periods) - 1


def calculate_volatility(return_series, periods_per_year=252):
    """
    Calculate annualized volatility from a daily return series.
    """
    if return_series.empty:
        raise ValueError("Return series is empty.")

    return_series = return_series.dropna()

    if len(return_series) == 0:
        return np.nan

    return return_series.std() * np.sqrt(periods_per_year)


def calculate_sharpe_ratio(return_series, risk_free_rate=0.0, periods_per_year=252):
    """
    Calculate annualized Sharpe ratio from a daily return series.
    """
    if return_series.empty:
        raise ValueError("Return series is empty.")

    return_series = return_series.dropna()

    if len(return_series) == 0:
        return np.nan

    annual_return = calculate_annual_return(return_series, periods_per_year)
    annual_volatility = calculate_volatility(return_series, periods_per_year)

    if annual_volatility == 0:
        return np.nan

    return (annual_return - risk_free_rate) / annual_volatility


def calculate_max_drawdown(equity_curve):
    """
    Calculate maximum drawdown from an equity curve.
    """
    if equity_curve.empty:
        raise ValueError("Equity curve is empty.")

    rolling_max = equity_curve.cummax()
    drawdown = equity_curve / rolling_max - 1

    return drawdown.min()


def calculate_performance_metrics(return_series, equity_curve, risk_free_rate=0.0):
    """
    Calculate a set of performance metrics for a strategy.
    """
    metrics = {
        "Total Return": calculate_total_return(equity_curve),
        "Annual Return": calculate_annual_return(return_series),
        "Volatility": calculate_volatility(return_series),
        "Sharpe Ratio": calculate_sharpe_ratio(return_series, risk_free_rate=risk_free_rate),
        "Max Drawdown": calculate_max_drawdown(equity_curve),
    }

    return metrics


def create_metrics_table(results, risk_free_rate=0.0):
    """
    Create a comparison table for strategy and benchmarks.
    """
    strategy_metrics = calculate_performance_metrics(
        results["portfolio_return"],
        results["strategy_equity"],
        risk_free_rate=risk_free_rate
    )

    equal_weight_metrics = calculate_performance_metrics(
        results["equal_weight_return"],
        results["equal_weight_equity"],
        risk_free_rate=risk_free_rate
    )

    spy_metrics = calculate_performance_metrics(
        results["spy_return"],
        results["spy_equity"],
        risk_free_rate=risk_free_rate
    )

    metrics_df = pd.DataFrame({
        "Momentum Strategy": strategy_metrics,
        "Equal Weight": equal_weight_metrics,
        "SPY": spy_metrics
    })

    return metrics_df
