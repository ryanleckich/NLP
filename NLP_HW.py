from cgitb import text
from pathlib import Path
from numpy import imag
from textblob import Word
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt


# 1 Using this information, create a bar chart of the top 10 topics based on their corresponding tweet volume.

mylist = []

from nyc_trends import nyc_trends


for i in nyc_trends:
    hasattr


from operator import itemgetter

sorted_items = sorted(mylist)
# print(sorted_items[:10])

sorted_items = sorted(mylist, key=itemgetter(1), reverse=True)
print(sorted_items[:10])

top20 = sorted_items[:20]

df = pd.DataFrame(top20, columns=["words", "Count"])

print(df)

import matplotlib.pyplot as plt

df.plot.bar(x="words", y="Count", legend=False)

plt.gcf().tight_layout()

plt.show()


# 2 Create a Word Cloud of all topics with over 20,000 tweet volume. The size of the word (topic) should be based on their tweet volume
