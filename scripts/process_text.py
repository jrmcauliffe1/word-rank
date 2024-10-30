# process_text.py
import pandas as pd
import re
import spacy
from nltk.corpus import stopwords

nlp = spacy.load("en_core_web_sm")
stop_words = set(stopwords.words("english"))

def clean_text(text):
    # Remove URLs, mentions, hashtags, and punctuation
    text = re.sub(r"http\S+|@\S+|#\S+|\W", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def process_data(df):
    processed_text = []
    for text in df['text']:
        clean = clean_text(text)
        doc = nlp(clean)
        tokens = [token.lemma_ for token in doc if token.text not in stop_words and not token.is_punct]
        processed_text.append(" ".join(tokens))
    
    df['processed_text'] = processed_text
    return df[['processed_text']]

if __name__ == "__main__":
    df = pd.read_csv("../data/raw_news/news_data.csv")
    processed_df = process_data(df)
    processed_df.to_csv("../data/processed/processed_news.csv", index=False)
