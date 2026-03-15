import matplotlib.pyplot as plt


def plot_equity_curves(results):
    for equity in results[:20]:
        plt.plot(equity)

    plt.title("Monte Carlo Equity Paths")
    plt.xlabel("Trades")
    plt.ylabel("Capital")
    plt.show()


def plot_final_capital_distribution(final_capitals):
    plt.hist(final_capitals, bins=50)
    plt.title("Distribution of Final Capital")
    plt.xlabel("Final Capital")
    plt.ylabel("Frequency")
    plt.show()
