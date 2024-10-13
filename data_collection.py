# data_collection.py

import praw
import pandas as pd
from config import CLIENT_ID, CLIENT_SECRET, USER_AGENT, USERNAME, PASSWORD

def scrape_reddit_data(subreddit_name, limit=50):
    reddit = praw.Reddit(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        user_agent=USER_AGENT,
        username=USERNAME,
        password=PASSWORD
    )
    
    subreddit = reddit.subreddit(subreddit_name)
    posts_data = []

    for post in subreddit.top(limit=limit):
        posts_data.append({
            'title': post.title,
            'score': post.score,
            'num_comments': post.num_comments,
            'created_utc': post.created_utc,
            'url': post.url
        })

    df = pd.DataFrame(posts_data)
    df['created_utc'] = pd.to_datetime(df['created_utc'], unit='s')
    
    return df

def clean_data(df):
    # 1. Remove duplicates
    df.drop_duplicates(subset='title', inplace=True)

    # 2. Handle missing values
    df.dropna(subset=['title', 'created_utc'], inplace=True)  # Drop rows where title or timestamp is missing

    # 3. Remove unnecessary columns (optional, depending on what you want to keep)
    # For example, we might only want to keep 'title', 'created_utc', 'sentiment', etc.
    # df.drop(['score', 'num_comments'], axis=1, inplace=True)

    # 4. Text Preprocessing: Clean text in the 'title' column (useful for sentiment analysis)
    df['title_cleaned'] = df['title'].str.replace(r'[^a-zA-Z\s]', '', regex=True)  # Remove special characters
    df['title_cleaned'] = df['title_cleaned'].str.lower()  # Convert to lowercase

    # 5. (Optional) Handle short or irrelevant posts
    df = df[df['title_cleaned'].str.len() > 5]  # Remove posts where the cleaned title is too short

    return df

if __name__ == "__main__":
    # Scrape data
    df = scrape_reddit_data('wallstreetbets')
    print(f"Before cleaning: {df.shape}")

    # Clean the data
    cleaned_df = clean_data(df)
    print(f"After cleaning: {cleaned_df.shape}")

    # Save cleaned data to a new CSV file
    cleaned_df.to_csv('cleaned_reddit_data.csv', index=False)
