"""
自己收集的文本文件
"""
from nltk.corpus import PlaintextCorpusReader


corpus_root = "F:\Ebooks"
wordlists = PlaintextCorpusReader(corpus_root,".*")
print(wordlists.fileids())

print(wordlists.words(".git/config"))

