from simulation import run_simulations, get_final_capitals
from plots import plot_equity_curves, plot_final_capital_distribution

results = run_simulations()
final_capitals = get_final_capitals(results)

plot_equity_curves(results)
plot_final_capital_distribution(final_capitals)
