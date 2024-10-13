# # report.py

# import pandas as pd

# def generate_report(sentiment_file='reddit_data_with_sentiment.csv', stock_file='TSLA_stock_data.csv'):
#     sentiment_data = pd.read_csv(sentiment_file)
#     stock_data = pd.read_csv(stock_file)

#     sentiment_data['created_utc'] = pd.to_datetime(sentiment_data['created_utc'])
#     stock_data.index = pd.to_datetime(stock_data.index)

#     # Merge data
#     merged_data = pd.merge_asof(sentiment_data, stock_data, left_on='created_utc', right_index=True)

#     # Calculate correlation
#     correlation = merged_data[['sentiment', 'Close']].corr()
    
#     print("Correlation between sentiment and stock price:")
#     print(correlation)
    
#     # Simple insights based on correlation
#     if correlation.loc['sentiment', 'Close'] > 0:
#         print("Positive sentiment seems to correlate with stock price increases.")
#     else:
#         print("Negative sentiment seems to correlate with stock price decreases.")
    
#     # Further insights can be added here...

# if __name__ == "__main__":
#     generate_report()





import pandas as pd
import yfinance as yf

def generate_report():
    # Load sentiment data
    sentiment_data = pd.read_csv('reddit_data_with_sentiment.csv')

    # Ensure the 'created_utc' column in sentiment_data is in datetime format
    sentiment_data['created_utc'] = pd.to_datetime(sentiment_data['created_utc'])

    # Fetch stock data (example: Tesla - TSLA)
    stock_data = yf.download('TSLA', start='2023-01-01', end='2023-12-31')

    # Ensure the stock data index is in datetime format
    stock_data.index = pd.to_datetime(stock_data.index)

    # **Sort both DataFrames by their datetime columns**
    sentiment_data = sentiment_data.sort_values('created_utc')
    stock_data = stock_data.sort_index()

    # Perform the merge_asof operation
    merged_data = pd.merge_asof(sentiment_data, stock_data, left_on='created_utc', right_index=True)

    # Example analysis: Correlation between sentiment and stock price (Close)
    correlation = merged_data[['sentiment', 'Close']].corr()
    print("Correlation between sentiment and stock price (Close):")
    print(correlation)

if __name__ == "__main__":
    generate_report()
