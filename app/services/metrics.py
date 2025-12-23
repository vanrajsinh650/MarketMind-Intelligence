import pandas as pd
import numpy as np

class MetricsCalculator:
    """Calculate stock metrics"""

    def Calculate_basic_metrics(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate required metrics from assigment"""

        # Daily Return = (Close - Open) / open
        df ['daily_return'] = ((df['Close'] - df['Open']) / df['Open']) * 100

        # 7 day moving average
        df['ma_7'] = df['Close'].rolling(window=7).mean()

        # 52-week High/Low (these are calculated over full dataset)
        df['52_week_high'] = df['High'].rolling(window=252, min_periods=1).max()
        df['52_week_low'] = df['Low'].rolling(window=252, min_periods=1).min()
        return df
    
    def add_custom_metric(self, df: pd.DataFrame) -> pd.DataFrame:
        """Add one creative metric - Volatility Score"""

        # Volatility - 30 day standerd devitaion of returns
        df['volatility'] = df['daily_return'].rolling(window=30).std()

        # Fill NaN value for initial rows
        df['ma_7'] = df['ma_7'].fillna(df['Close'])
        df['volatility'] = df['volatility'].fillna(0)

        return df
    
    def process_stock_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Complete processing pipeline"""
        df = self.Calculate_basic_metrics(df)
        df = self.add_custom_metric(df)

        return df
    
# TEST

if __name__ == "__main__":
    from app.services.data_fetcher import StockDataFetcher

    fetcher = StockDataFetcher()
    data = fetcher.Fetch_Stocks("TCS")

    if data is not None:
        calculator = MetricsCalculator()
        processed = calculator.process_stock_data(data)

        print("\n Processed data with metrics")
        print(processed[['Close', 'daily_return', 'ma_7', 'volatility']].tail())        