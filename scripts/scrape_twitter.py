# scrape_twitter.py
import tweepy
import pandas as pd
import yaml

# Load API credentials
with open("../config/config.yaml", "r") as file:
    config = yaml.safe_load(file)

auth = tweepy.OAuthHandler(config["twitter"]["api_key"], config["twitter"]["api_secret_key"])
auth.set_access_token(config["twitter"]["access_token"], config["twitter"]["access_token_secret"])
api = tweepy.API(auth)

def scrape_twitter_trending(hashtags):
    tweet_data = []
    for hashtag in hashtags:
        for tweet in tweepy.Cursor(api.search_tweets, q=hashtag, lang="en", tweet_mode="extended").items(100):
            tweet_data.append({'text': tweet.full_text, 'hashtag': hashtag})
    return pd.DataFrame(tweet_data)

if __name__ == "__main__":
    hashtags = ["#Trending", "#News"]  # Example hashtags
    df = scrape_twitter_trending(hashtags)
    df.to_csv("../data/raw_tweets/tweet_data.csv", index=False)
