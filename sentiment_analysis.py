# sentiment_analysis.py

from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

def analyze_sentiment(data_file='cleaned_reddit_data.csv'):
    analyzer = SentimentIntensityAnalyzer()
    df = pd.read_csv(data_file)

    df['sentiment'] = df['title'].apply(lambda title: analyzer.polarity_scores(title)['compound'])

    print(df.head())  # Sample output to check sentiment analysis
    df.to_csv('reddit_data_with_sentiment.csv', index=False)

if __name__ == "__main__":
    analyze_sentiment()
