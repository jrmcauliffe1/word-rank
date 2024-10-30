# analyze_trends.py
import pandas as pd
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

def get_common_phrases(text_list):
    all_words = " ".join(text_list).split()
    return Counter(all_words).most_common(10)

def analyze_data(news_df, tweet_df):
    combined_df = pd.concat([news_df, tweet_df])
    
    # Top phrases
    top_phrases = get_common_phrases(combined_df['processed_text'].tolist())

    # Sentiment analysis
    sentiments = combined_df['processed_text'].apply(lambda x: sia.polarity_scores(x)["compound"])
    combined_df['sentiment'] = sentiments

    # Summary DataFrame
    summary = pd.DataFrame({
        "Top Phrases": [top_phrases],
        "Average Sentiment": [sentiments.mean()]
    })
    
    return summary

if __name__ == "__main__":
    news_df = pd.read_csv("../data/processed/processed_news.csv")
    tweet_df = pd.read_csv("../data/processed/processed_tweets.csv")
    summary = analyze_data(news_df, tweet_df)
    summary.to_csv("../data/summaries/weekly_trends_summary.csv", index=False)
