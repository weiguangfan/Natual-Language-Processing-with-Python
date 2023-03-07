"""
没有在停用词列表的词的比例
"""
import nltk


def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words("english")
    content = [w for w in text if w.lower() not in stopwords]
    return len(content) / len(text)


print(content_fraction(nltk.corpus.reuters.words()))