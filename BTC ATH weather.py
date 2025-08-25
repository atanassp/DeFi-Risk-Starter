import requests
import matplotlib.pyplot as plt
import numpy as np

# BTC ATH data (expanded list)
ath_data = [
    {"date": "2011-06-08", "price": 31.91},
    {"date": "2013-11-30", "price": 1163.00},
    {"date": "2017-12-17", "price": 19783.06},
    {"date": "2020-12-17", "price": 23770.00},
    {"date": "2021-04-14", "price": 64863.10},
    {"date": "2021-11-10", "price": 68789.00},
    {"date": "2022-03-14", "price": 73737.94},
    {"date": "2024-11-22", "price": 99637.00},
    {"date": "2025-07-14", "price": 123150.00},
    {"date": "2025-08-14", "price": 124128.00}
]
dates = [d["date"] for d in ath_data]
prices = [d["price"] for d in ath_data]

# OpenWeatherMap (get YOUR_API_KEY from open-meteo.com)
api_key = "YOUR_API_KEY"
city = "Zurich,CH"
weather_data = []
for date in dates:
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude=47.3667&longitude=8.55&start_date={date}&end_date={date}&hourly=temperature_2m,rain"
    response = requests.get(url).json()
    if "hourly" in response:
        temp = response["hourly"]["temperature_2m"][0]
        rain = response["hourly"]["rain"][0] if "rain" in response["hourly"] else 0
        weather_data.append({"date": date, "temp": temp, "rain": rain})

# Fancy graph
fig, ax1 = plt.subplots(figsize=(14, 8))
ax1.set_facecolor("#1a1a1a")  # Dark background
fig.patch.set_facecolor("#1a1a1a")
ax1.plot(dates, prices, color="#00ffcc", linewidth=3, marker="o", label="BTC ATH Price", markersize=10)
ax1.set_xlabel("Date", color="white")
ax1.set_ylabel("Price (USD)", color="#00ffcc")
ax1.tick_params(axis="y", colors="#00ffcc")
ax1.tick_params(axis="x", colors="white", rotation=45)

ax2 = ax1.twinx()
ax2.bar(dates, [w["rain"] for w in weather_data], color="#ff4d4d", alpha=0.7, label="Rain (mm)", width=0.4)
ax2.plot(dates, [w["temp"] for w in weather_data], color="#ffcc00", linewidth=2, label="Temp (°C)", marker="s", markersize=8)
ax2.set_ylabel("Rain/Temp", color="white")
ax2.tick_params(axis="y", colors="white")

plt.title("BTC ATHs vs. Zurich Weather", color="white", pad=20)
fig.legend(loc="upper left", bbox_to_anchor=(0.1,0.9), facecolor="#1a1a1a", edgecolor="white")
plt.text(0.5, 0.05, "Sometimes you need rain to grow flowers...", transform=fig.transFigure, 
         ha="center", color="#ffcc00", fontsize=12, bbox=dict(facecolor="black", alpha=0.8))
plt.tight_layout()
plt.savefig("btc_ath_weather_fancy.png", dpi=300, facecolor="#1a1a1a")
plt.close()
