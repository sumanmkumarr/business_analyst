# # visualization.py

# import pandas as pd
# import matplotlib.pyplot as plt

# def visualize_sentiment(data_file='reddit_data_with_sentiment.csv'):
#     df = pd.read_csv(data_file)
#     df['created_utc'] = pd.to_datetime(df['created_utc'])

#     # Plot sentiment distribution
#     df['sentiment'].hist(bins=20)
#     plt.title('Sentiment Distribution of Reddit Posts')
#     plt.xlabel('Sentiment Score')
#     plt.ylabel('Frequency')
#     plt.show()

#     # Plot sentiment over time
#     df.set_index('created_utc', inplace=True)
#     df['sentiment'].plot(title='Sentiment Over Time')
#     plt.ylabel('Sentiment Score')
#     plt.show()

# def visualize_stock_and_sentiment(stock_file='TSLA_stock_data.csv', sentiment_file='reddit_data_with_sentiment.csv'):
#     stock_data = pd.read_csv(stock_file)
#     sentiment_data = pd.read_csv(sentiment_file)
    
#     sentiment_data['created_utc'] = pd.to_datetime(sentiment_data['created_utc'])
#     stock_data.index = pd.to_datetime(stock_data.index)

#     # Merge stock and sentiment data
#     merged_data = pd.merge_asof(sentiment_data, stock_data, left_on='created_utc', right_index=True)

#     # Plot stock price and sentiment
#     fig, ax1 = plt.subplots()

#     ax1.set_xlabel('Date')
#     ax1.set_ylabel('Sentiment', color='tab:blue')
#     ax1.plot(merged_data['created_utc'], merged_data['sentiment'], color='tab:blue')

#     ax2 = ax1.twinx()
#     ax2.set_ylabel('Stock Price', color='tab:red')
#     ax2.plot(merged_data['created_utc'], merged_data['Close'], color='tab:red')

#     plt.title('Sentiment vs Stock Price Over Time')
#     plt.show()

# if __name__ == "__main__":
#     visualize_sentiment()
#     visualize_stock_and_sentiment()






import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt

# Load sentiment data
sentiment_data = pd.read_csv('reddit_data_with_sentiment.csv')

# Ensure the 'created_utc' column in sentiment_data is in datetime format
sentiment_data['created_utc'] = pd.to_datetime(sentiment_data['created_utc'])

# Fetch stock data (example: Tesla - TSLA)
stock_data = yf.download('TSLA', start='2023-01-01', end='2023-12-31')

# Ensure the stock data index is in datetime format
stock_data.index = pd.to_datetime(stock_data.index)

# Sort both dataframes by their datetime columns (necessary for merge_asof)
sentiment_data = sentiment_data.sort_values('created_utc')
stock_data = stock_data.sort_index()

# Perform the merge_asof operation
merged_data = pd.merge_asof(sentiment_data, stock_data, left_on='created_utc', right_index=True)

# Visualize Sentiment vs Stock Price
plt.figure(figsize=(10, 6))
plt.plot(merged_data['created_utc'], merged_data['sentiment'], color='blue', label='Sentiment')
plt.plot(merged_data['created_utc'], merged_data['Close'], color='red', label='Stock Price (Close)')
plt.legend()
plt.title('Sentiment vs Stock Price Over Time')
plt.xlabel('Time')
plt.show()
