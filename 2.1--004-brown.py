"""
布朗语料库，作为句子链表或词链表来访问；
"""
from nltk.corpus import brown
print(brown.categories())  # 显示类别
print("$"*50)

print(brown.words(categories="news"))  # 显示特定类别
print("$"*50)

print(brown.words(fileids=['cg22']))  # 显示特定文件
print("$"*50)

print(brown.sents(categories=["news", "editorial", "reviews"]))
print("$"*50)

