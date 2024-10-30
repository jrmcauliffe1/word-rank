# scrape_news.py
import newspaper
import pandas as pd
from newspaper import Article

def scrape_news(sources):
    news_data = []
    for url in sources:
        paper = newspaper.build(url)
        for article in paper.articles[:5]:  # Limit to 5 articles per source for efficiency
            try:
                article.download()
                article.parse()
                news_data.append({'title': article.title, 'text': article.text})
            except Exception as e:
                print(f"Failed to scrape {article.url}: {e}")
    return pd.DataFrame(news_data)

if __name__ == "__main__":
    sources = ["https://www.bbc.com", "https://www.cnn.com"]  # Add more sources as needed
    df = scrape_news(sources)
    df.to_csv("../data/raw_news/news_data.csv", index=False)
