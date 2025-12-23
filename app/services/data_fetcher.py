import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta

class StockDataFetcher:
    """ Featching stock data from Yahoo Finance """

    def __init__(self):
        self.nse_stocks = [
            "RELIANCE", "TCS", "HDFCBANK", "INFY", "ICICIBANK", "HINDUNILVR", "BHARATIARTL", "SBIN", "ITC", "LT"
        ]

    def Fetch_Stocks(self, symbol: str, period: str = "1y"):
        """Fetch single stock data"""
        try:
            ticker = yf.Ticker(f"{symbol}.NS")
            df = ticker.history(period=period)

            if df.empty:
                print(f"No data for {symbol}")
                return None
            
            print(f"Fetched {symbol}: {len(df)} records")
            return df
        except Exception as e:
            print(f"Error fetching {symbol}: {e}")
            return None
        
    def fetch_multiple_stocks(self, symbols: list = None):
        """Fetch multiple stocks"""

        if symbols is None:
            symbols = self.nse_stocks

        results = {}
        for symbol in symbols:
            df = self.Fetch_Stocks(symbol)
            if df is not None:
                results[symbol] = df

        return results
    
# Test function
if __name__ == "__main__":
    fetcher = StockDataFetcher()
    data = fetcher.Fetch_Stocks("RELIANCE")
    
    if data is not None:
        print("\nSample Data:")
        print(data.tail())
        print(f"\nTotal records: {len(data)}")