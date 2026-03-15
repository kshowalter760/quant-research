import numpy as np
import pandas as pd


def calculate_total_return(data: pd.DataFrame) -> float:
    return data["strategy_equity"].iloc[-1] - 1


def calculate_annualized_return(data: pd.DataFrame, trading_days: int = 252) -> float:
    total_periods = len(data)
    ending_value = data["strategy_equity"].iloc[-1]

    if total_periods == 0 or ending_value <= 0:
        return np.nan

    return ending_value ** (trading_days / total_periods) - 1


def calculate_volatility(data: pd.DataFrame, trading_days: int = 252) -> float:
    return data["strategy_return"].std() * np.sqrt(trading_days)


def calculate_sharpe_ratio(data: pd.DataFrame, trading_days: int = 252, risk_free_rate: float = 0.0) -> float:
    annualized_return = calculate_annualized_return(data, trading_days)
    annualized_volatility = calculate_volatility(data, trading_days)

    if annualized_volatility == 0 or np.isnan(annualized_volatility):
        return np.nan

    return (annualized_return - risk_free_rate) / annualized_volatility


def calculate_max_drawdown(data: pd.DataFrame) -> float:
    equity_curve = data["strategy_equity"]
    running_max = equity_curve.cummax()
    drawdown = (equity_curve - running_max) / running_max
    return drawdown.min()


def calculate_metrics(data: pd.DataFrame) -> dict:
    return {
        "Total Return": calculate_total_return(data),
        "Annualized Return": calculate_annualized_return(data),
        "Volatility": calculate_volatility(data),
        "Sharpe Ratio": calculate_sharpe_ratio(data),
        "Max Drawdown": calculate_max_drawdown(data),
    }
