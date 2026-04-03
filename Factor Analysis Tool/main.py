from data_loader import load_price_data
from factors import compute_composite_momentum
from ranking import rank_assets
from portfolio import construct_portfolio
from backtest import run_backtest
from metrics import create_metrics_table
from plots import plot_equity_curves


def main():
    tickers = ["SPY", "QQQ", "EEM", "GLD", "TLT", "VNQ"]

    prices = load_price_data(
        tickers=tickers,
        start="2018-01-01",
        end="2025-01-01"
    )

    composite_momentum = compute_composite_momentum(
        prices,
        lookbacks=(63, 126, 252)
    )

    ranks = rank_assets(composite_momentum)

    weights = construct_portfolio(
        ranks,
        top_n=2,
        rebalance_frequency="M"
    )

    results = run_backtest(prices, weights)
    metrics_table = create_metrics_table(results)

    metrics_table.round(4).to_csv("factor_metrics.csv")

    print("\nFinal equity values:")
    print(f"Strategy Equity:      {results['strategy_equity'].iloc[-1]:.4f}")
    print(f"Equal Weight Equity:  {results['equal_weight_equity'].iloc[-1]:.4f}")
    print(f"SPY Equity:           {results['spy_equity'].iloc[-1]:.4f}")

    print("\nPerformance Metrics:")
    print(metrics_table.round(4))

    print("\nMetrics saved to factor_metrics.csv")

    plot_equity_curves(results)


if __name__ == "__main__":
    main()