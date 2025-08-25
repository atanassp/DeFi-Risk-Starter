import requests
import matplotlib.pyplot as plt
import numpy as np

# BTC ATH data (10 dates)
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

# Open-Meteo API (get YOUR_API_KEY from open-meteo.com)
api_key = "YOUR_API_KEY"  # Replace with your key
city = "Zurich,CH"
weather_data = []
for date in dates:
    url = f"https://archive-api.open-meteo.com/v1/archive?latitude=47.3667&longitude=8.55&start_date={date}&end_date={date}&hourly=temperature_2m"
    response = requests.get(url).json()
    if "hourly" in response:
        temp = response["hourly"]["temperature_2m"][0]
        weather_data.append({"date": date, "temp": temp})

# Fancy graph (temp only)
fig, ax1 = plt.subplots(figsize=(14, 8))
ax1.set_facecolor("#1a1a1a")  # Dark background
fig.patch.set_facecolor("#1a1a1a")
ax1.plot(dates, prices, color="#00ffcc", linewidth=3, marker="o", label="BTC ATH Price", markersize=10)
ax1.set_xlabel("Date", color="white")
ax1.set_ylabel("Price (USD)", color="#00ffcc")
ax1.tick_params(axis="y", colors="#00ffcc")
ax1.tick_params(axis="x", colors="white", rotation=45)

ax2 = ax1.twinx()
ax2.plot(dates, [w["temp"] for w in weather_data], color="#ffcc00", linewidth=2, label="Temp (°C)", marker="s", markersize=8)
ax2.set_ylabel("Temperature (°C)", color="white")
ax2.tick_params(axis="y", colors="white")

plt.title("BTC ATHs vs. Zurich Temperature", color="white", pad=20)
fig.legend(loc="upper left", bbox_to
