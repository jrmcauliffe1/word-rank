# main.py
import pandas as pd
from scripts.scrape_news import scrape_news
from scripts.scrape_twitter import scrape_twitter_trending
from scripts.process_text import process_data
from scripts.analyze_trends import analyze_data
from scripts.visualize_trends import visualize_trends

def main():
    # Step 1: Scrape data
    print("Scraping news articles...")
    news_sources = ["https://www.bbc.com", "https://www.cnn.com"]
    news_df = scrape_news(news_sources)
    news_df.to_csv("data/raw_news/news_data.csv", index=False)

    print("Scraping Twitter data...")
    hashtags = ["#Trending", "#News"]
    tweet_df = scrape_twitter_trending(hashtags)
    tweet_df.to_csv("data/raw_tweets/tweet_data.csv", index=False)

    # Step 2: Process data
    print("Processing data...")
    processed_news = process_data(news_df)
    processed_tweets = process_data(tweet_df)
    
    # Save processed data
    processed_news.to_csv("data/processed/processed_news.csv", index=False)
    processed_tweets.to_csv("data/processed/processed_tweets.csv", index=False)

    # Step 3: Analyze trends
    print("Analyzing trends...")
    trends_summary = analyze_data(processed_news, processed_tweets)
    trends_summary.to_csv("data/summaries/weekly_trends_summary.csv", index=False)

    # Step 4: Visualize trends
    print("Visualizing trends...")
    visualize_trends(trends_summary)
    print("Pipeline completed successfully!")

if __name__ == "__main__":
    main()
