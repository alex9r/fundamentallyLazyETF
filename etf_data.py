import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

# TTP.TO - TD Canadian Equity Index ETF
TICKER_SYMBOL = "TTP.TO"

end_date = datetime.now()
start_date = end_date - timedelta(days=5*365) # past 5 years of data

print(f"--- Fetching historical data for {TICKER_SYMBOL} ---")

try:
    etf_data = yf.download(
        tickers=TICKER_SYMBOL, 
        start=start_date, 
        end=end_date, 
        interval="1d"  # Daily data
    )

    # head
    print(etf_data.head())

    print("\n--- Summary Statistics ---")
    #  Open, High, Low, Close, Volume throughout period
    print(etf_data.describe().round(2))

    # 4. Extract Key Metrics (e.g., last closing price)
    last_close = etf_data['Close'].iloc[-1].round(2)
    print(f"\nLast Closing Price: CAD ${last_close}")

except Exception as e:
    print(f"An error occurred while fetching data: {e}")