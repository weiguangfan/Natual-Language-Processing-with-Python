"""
特定词汇访问
"""
import nltk

prondict = nltk.corpus.cmudict.dict()
# print(prondict)
print(prondict["fire"])
# print(prondict["blog"])

# 过滤某些属性的词
text = ["natural","language","processing"]
print([ph for w in text for ph in prondict[w][0]])
