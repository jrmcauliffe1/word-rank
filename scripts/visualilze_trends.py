# visualize_trends.py
import matplotlib.pyplot as plt
from wordcloud import WordCloud

def visualize_trends(summary_df):
    # Visualize Top Phrases
    top_phrases = dict(summary_df.iloc[0]["Top Phrases"])
    wordcloud = WordCloud(width=800, height=400).generate_from_frequencies(top_phrases)
    
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Top Trending Phrases")
    plt.show()

    # Visualize Sentiment
    avg_sentiment = summary_df.iloc[0]["Average Sentiment"]
    plt.bar(["Average Sentiment"], [avg_sentiment], color="blue" if avg_sentiment > 0 else "red")
    plt.ylim(-1, 1)
    plt.title("Overall Sentiment")
    plt.show()

if __name__ == "__main__":
    summary_df = pd.read_csv("../data/summaries/weekly_trends_summary.csv")
    visualize_trends(summary_df)
