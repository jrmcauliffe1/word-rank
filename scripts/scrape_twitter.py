# scrape_twitter.py
import tweepy
import pandas as pd
import yaml
from datetime import datetime, timedelta

# Load API credentials and settings
with open("../config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

auth = tweepy.OAuthHandler(config["twitter"]["api_key"], config["twitter"]["api_secret_key"])
auth.set_access_token(config["twitter"]["access_token"], config["twitter"]["access_token_secret"])
api = tweepy.API(auth)

def scrape_twitter_trending(hashtags, days_back):
    # Calculate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=days_back)
    tweet_data = []

    for hashtag in hashtags:
        for tweet in tweepy.Cursor(
            api.search_tweets, 
            q=hashtag, 
            lang="en", 
            tweet_mode="extended",
            since=start_date.strftime('%Y-%m-%d'),
            until=end_date.strftime('%Y-%m-%d')
        ).items(100):
            tweet_data.append({'text': tweet.full_text, 'hashtag': hashtag})

    return pd.DataFrame(tweet_data)

if __name__ == "__main__":
    hashtags = config["twitter_settings"]["hashtags"]
    days_back = config["scrape_period_days"]
    df = scrape_twitter_trending(hashtags, days_back)
    df.to_csv("../data/raw_tweets/tweet_data.csv", index=False)
