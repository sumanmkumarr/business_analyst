# stock_data.py

import yfinance as yf

def fetch_stock_data(ticker='TSLA', start_date='2023-01-01', end_date='2023-12-31'):
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data.to_csv(f'{ticker}_stock_data.csv')

    print(stock_data.head())  # Sample output to check stock data fetching
    return stock_data

if __name__ == "__main__":
    fetch_stock_data()
