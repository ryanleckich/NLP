from typing import Text
from pathlib import Path
from numpy import imag
from textblob import Word
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt
from operator import itemgetter
from nyc_trends import nyc_trends
import nltk
import pandas as pd


# 1 Using this information, create a bar chart of the top 10 topics based on their corresponding tweet volume.

trend_list = []
vol_list = []


for tweet in nyc_trends[0]["trends"]:
    if tweet["tweet_volume"]:
        name = tweet["name"]
        volume = tweet["tweet_volume"]
        trend_list.append(name)
        vol_list.append(volume)

print(trend_list[:10])
print(vol_list[:10])

tweets = list(zip(trend_list, vol_list))


sorted_tweets = sorted(tweets, key=itemgetter(1), reverse=True)
popular = sorted_tweets[:10]

df = pd.DataFrame(popular, columns=["Tweets", "Volume"])

df.plot.bar(x="Tweets", y="Volume", legend=False)

plt.gcf().tight_layout()

plt.show()


# 2 Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic) should be based on their tweet volume
