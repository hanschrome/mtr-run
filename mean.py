import sys
import os
import pandas as pd
from binance.client import Client
from datetime import datetime, timedelta

public_key = os.getenv("BINANCE_PUBLIC_KEY")
private_key = os.getenv("BINANCE_PRIVATE_KEY")

if not public_key or not private_key:
    print("Please, add to the .env file the variables BINANCE_PUBLIC_KEY y BINANCE_PRIVATE_KEY")
    sys.exit(1)

client = Client(public_key, private_key)
    
def get_market_data(market):
    time_ago = datetime.now() - timedelta(days=180)
    klines = client.get_historical_klines(market, Client.KLINE_INTERVAL_1DAY, time_ago.strftime("%d %b %Y %H:%M:%S"), "now")
    df = pd.DataFrame(klines, columns=["Open time", "Open", "High", "Low", "Close", "Volume", "Close time", "Quote asset volume", "Number of trades", "Taker buy base asset volume", "Taker buy quote asset volume", "Ignore"])
    df["Close"] = df["Close"].astype(float)

    mean = df["Close"].mean()
    top_mean = df[df["Close"] > mean]["Close"].mean()
    bottom_mean = df[df["Close"] < mean]["Close"].mean()

    precision = client.get_symbol_info(market)['baseAssetPrecision']
    mean = round(mean, precision)
    top_mean = round(top_mean, precision)
    bottom_mean = round(bottom_mean, precision)

    return mean, top_mean, bottom_mean

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("python mean.py <market>")
        sys.exit(1)
        
    market = sys.argv[1]

    mean, top_mean, bottom_mean = get_market_data(market)

    print("mean, top_mean, bottom_mean")
    print(f"{mean},{top_mean},{bottom_mean}")
