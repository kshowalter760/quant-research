import matplotlib.pyplot as plt

def plot_equity_curves(results):

    for equity in results[:20]:
        plt.plot(equity)

    plt.title("Monte Carlo Equity Paths")
    plt.xlabel("Trades")
    plt.ylabel("Capital")

    plt.show()
