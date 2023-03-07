"""
文体之间的系统性差异
"""
import nltk
from nltk.corpus import brown

news_text = brown.words(categories="news")
print(news_text)
fdist = nltk.FreqDist([w.lower() for w in news_text])
print(fdist.keys())
modals = ["can","could","may","might","must","will"]
for m in modals:
    print(m + ": ", fdist[m])





