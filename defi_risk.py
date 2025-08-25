import matplotlib.pyplot as plt
import requests
import pandas as pd

# Grab data from CoinGecko (top 10 coins)
url = "https://api.coingecko.com/api/v3/coins/markets"
params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10}
data = requests.get(url, params=params).json()

# Pull prices for the chart
prices = [coin["current_price"] for coin in data]

# Plot the chart (replace your old data here)
plt.plot(prices)
plt.title("Top 10 Crypto Prices")
plt.xlabel("Coin Rank")
plt.ylabel("Price (USD)")
plt.savefig("risk_plot.png")  # Saves the new chart
plt.close()
