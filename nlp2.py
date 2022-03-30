from textblob import TextBlob
import nltk
from pathlib import Path
import pandas as pd
import textblob


nltk.download("stopwords")

from nltk.corpus import stopwords


stops = stopwords.words("english")

# print(stops)

blob = TextBlob("Today is a beautiful day.")

# print(blob.words)

cleanlist = [word for word in blob.words if word not in stops]

# print(cleanlist)

blob = TextBlob(Path("RomeoAndJuliet.txt").read_text())

# print(blob.word_counts["juliet"])

# print(blob.noun_phrases.count("lady capulet"))

more_stops = ["thee", "thy", "thou"]

stops += more_stops

items = blob.word_counts.items()

# print(items)

# use a list comprhension to elimanate any tuples
# containing stop words

items = [i for i in items if i[0] not in stops]

print(items[:10])


from operator import itemgetter

sorted_items = sorted(items)
# print(sorted_items[:10])

sorted_items = sorted(items, key=itemgetter(1), reverse=True)
print(sorted_items[:10])

top20 = sorted_items[:20]

df = pd.DataFrame(top20, columns=["words", "Count"])

print(df)

import matplotlib.pyplot as plt

df.plot.bar(x="words", y="Count", legend=False)

plt.gcf().tight_layout()

plt.show()
