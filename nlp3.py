from cgitb import text
from pathlib import Path
from numpy import imag
from textblob import Word
from wordcloud import WordCloud
import imageio
import matplotlib.pyplot as plt


text = Path("RomeoAndJuliet.txt").read_text()

mask_image = imageio.imread("mask_heart.png")

wordcloud = WordCloud(colormap="prism", mask=mask_image, background_color="white")

wordcloud = wordcloud.generate(text)

wordcloud = wordcloud.to_file("RomeoJulietheart.png")

plt.imshow(wordcloud)

plt.show()
