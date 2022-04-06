from typing import Text
from pathlib import Path
from numpy import imag
from pyparsing import col
from textblob import Word
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt
from operator import itemgetter

import wordcloud
from nyc_trends import nyc_trends
import nltk
import pandas as pd


# 1 Using this information, create a bar chart of the top 10 topics based on their corresponding tweet volume.

vol_list = []
trend_list = []


for tweet in nyc_trends[0]["trends"]:
    if tweet["tweet_volume"]:
        name = tweet["name"]
        volume = tweet["tweet_volume"]
        vol_list.append(volume)
        trend_list.append(name)

tweets = list(zip(trend_list, vol_list))


sorted_tweets = sorted(tweets, key=itemgetter(1), reverse=True)
popular = sorted_tweets[:10]

df = pd.DataFrame(popular, columns=["Tweets", "Volume"])

df.plot.bar(x="Tweets", y="Volume", legend=False)

plt.gcf().tight_layout()

plt.show()


# 2 Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic) should be based on their tweet volume


df = pd.DataFrame(sorted_tweets, columns=["Tweet", "Volume"])
x = df["Volume"] >= 20000
df1 = df[x]


words = dict(zip(df1["Tweet"].tolist(), df1["Volume"].tolist()))
cloud = WordCloud(colormap="prism", background_color="white")
cloud = cloud.generate_from_frequencies(words)
cloud = cloud.to_file("tweet_cloud.png")


plt.imshow(cloud)
plt.figure(figsize=(50, 30))
cloud = cloud.to_file("wordcloud.png")
plt.show()
