import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ------------------------
# SETTINGS
# ------------------------

tickers = ["SPY", "QQQ", "AAPL", "MSFT"]
start_date = "2018-01-01"
end_date = "2023-01-01"

weights = np.array([0.2, 0.25, 0.4, 0.15])

# ------------------------
# DOWNLOAD DATA
# ------------------------

data = yf.download(
    tickers,
    start=start_date,
    end=end_date,
    auto_adjust=True
)["Close"]

# ------------------------
# CALCULATE RETURNS
# ------------------------

returns = data.pct_change().dropna()

#-------------------------
# CORRELATION MATRIX
#-------------------------
corr_matrix = returns.corr()
print("\nCorrelation Matrix:\n")
print(corr_matrix)

#-------------------------
# IMPORT HEAT MAP
#-------------------------

import seaborn as sns

plt.figure(figsize=(6, 5))
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Asset Correlation Matrix")
plt.show()

# ------------------------
# PORTFOLIO RETURNS
# ------------------------

portfolio_returns = returns.dot(weights)

# ------------------------
# EQUITY CURVE
# ------------------------

equity_curve = (1 + portfolio_returns).cumprod()

#-------------------------
# COMPARE WITH INDIVIDUAL ASSETS
#-------------------------

individual_equity = (1 + returns).cumprod()

plt.figure(figsize=(10, 5))

for col in individual_equity.columns:
    plt.plot(individual_equity[col], alpha=0.5, label=col)

plt.plot(equity_curve, linewidth=2, label="Portfolio", color="black")

plt.legend()
plt.title("Portfolio vs Individual Assets")
plt.show()

# ------------------------
# METRICS
# ------------------------

total_return = equity_curve.iloc[-1] - 1
annual_return = portfolio_returns.mean() * 252
volatility = portfolio_returns.std() * np.sqrt(252)
sharpe = annual_return / volatility

drawdown = (equity_curve / equity_curve.cummax()) - 1
max_drawdown = drawdown.min()

print("Total Return:", round(total_return, 4))
print("Annual Return:", round(annual_return, 4))
print("Volatility:", round(volatility, 4))
print("Sharpe Ratio:", round(sharpe, 4))
print("Max Drawdown:", round(max_drawdown, 4))

# ------------------------
# PLOT
# ------------------------

plt.figure(figsize=(10, 5))
plt.plot(equity_curve)
plt.title("Portfolio Equity Curve")
plt.xlabel("Date")
plt.ylabel("Growth of $1")
plt.show()
