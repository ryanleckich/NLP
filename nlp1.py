from typing import Text
from textblob import TextBlob
import textblob

text = "Today is a beautiful day. Tomorrow looks like bad weather."

blob = TextBlob(text)

# print(blob)

sentences = blob.sentences

# print(sentences)

# print(blob.noun_phrases)

# print(blob.sentiment)

# print(blob.sentiment.polarity)
# print(blob.sentiment.subjectivity)

# for sentence in sentences:
# print(round(sentence.sentiment.polarity), 3)

# from textblob.sentiments import NaiveBayesAnalyzer

# blob = textblob(text, analyzer=NaiveBayesAnalyzer)

# print(blob.sentiment)

# for sentence in sentences:
# print(sentence.setiment, 3)


# ------- notes from class------


# ------ notes from class ---------


from textblob import Word

index = Word("index")
catci = Word("cacti")


print(index.pluralize())

print(catci.singularize())


animals = TextBlob("dog cat fish bird").words
print(animals.pluralize())

# spell check
word = Word("theyr")

print(word.spellcheck())

print(word.correct())  # goes for the highest confidence

from nltk.stem import WordNetLemmatizer


word1 = Word("studies")
word2 = Word("varieties")

print(word1.stem())
print(word2.stem())

# print(word1.lemmatize())
# print(word2.lemmatize())


happy = Word("happy")

print(happy.definitions())
