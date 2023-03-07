from nltk.book import *
# from __future__ import division
print(len(text3))
print("$"*50)
print(set(text3))  # 词汇表
print(len(set(text3)))
print("$"*50)
print(sorted(set(text3)))
# print(len(text3) / len(set(text3)))  # 文本词汇丰富度
print("$"*50)
print(text3.count("smote"))  # 一个词在文本中出现的次数
print("$"*50)
print(100 * text4.count("a") / len(text4))  # 一个词在文本中占据的百分比


def lexical_diversity(text):
    return len(text) / len(set(text))


def percentage(count,total):
    return 100 * count / total

print("$"*50)
print(lexical_diversity(text3))
print("$"*50)
print(lexical_diversity(text5))
print("$"*50)
print(percentage(4, 5))
print("$"*50)
print(percentage(text4.count("a"),len(text4)))
