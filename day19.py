import pandas as pd
import matplotlib.pyplot as plt

# Sample stock dataset
data = {
    "Date": pd.date_range(start="2025-01-01", periods=15, freq="D"),
    "Stock_A": [100, 105, 103, 110, 115, 113, 120, 118, 125, 130, 128, 135, 140, 138, 145],
    "Stock_B": [90, 92, 91, 95, 97, 96, 100, 98, 102, 105, 103, 108, 110, 109, 112]
}

df = pd.DataFrame(data)

# Moving Average
df["Stock_A_MA"] = df["Stock_A"].rolling(window=3).mean()
df["Stock_B_MA"] = df["Stock_B"].rolling(window=3).mean()

# Identify peaks and drops
stock_a_peak = df.loc[df["Stock_A"].idxmax()]
stock_a_drop = df.loc[df["Stock_A"].idxmin()]

print("Stock A Highest Price:")
print(stock_a_peak)

print("\nStock A Lowest Price:")
print(stock_a_drop)

# Volatility
df["Stock_A_Change"] = df["Stock_A"].pct_change()
df["Stock_B_Change"] = df["Stock_B"].pct_change()

print("\nStock A Volatility:", df["Stock_A_Change"].std())
print("Stock B Volatility:", df["Stock_B_Change"].std())

# Visualization: Price Trend
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Stock_A"], marker="o", label="Stock A Price")
plt.plot(df["Date"], df["Stock_B"], marker="o", label="Stock B Price")
plt.title("Stock Price Trend")
plt.xlabel("Date")
plt.ylabel("Stock Price")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Visualization: Moving Average
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Stock_A"], marker="o", label="Stock A")
plt.plot(df["Date"], df["Stock_A_MA"], marker="o", label="Stock A Moving Average")

plt.title("Stock A Moving Average Line")
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Compare multiple stocks
plt.figure(figsize=(10, 5))
plt.plot(df["Date"], df["Stock_A_MA"], marker="o", label="Stock A MA")
plt.plot(df["Date"], df["Stock_B_MA"], marker="o", label="Stock B MA")

plt.title("Comparison of Multiple Stocks")
plt.xlabel("Date")
plt.ylabel("Moving Average Price")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()