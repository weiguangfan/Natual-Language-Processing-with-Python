"""
路透社语料库
"""
from nltk.corpus import reuters

print(reuters.fileids())

print(reuters.categories())

print(reuters.categories("training/9865"))  # 单个field

print(reuters.categories(["training/9865", "training/9880"]))  # fields列表

print(reuters.fileids("barley"))

print(reuters.fileids(["barley", "corn"]))

print(reuters.words("training/9865")[:14])

print(reuters.words(["training/9865", "training/9880"]))

print(reuters.words(categories="barley"))

print(reuters.words(categories=["barley", "corn"]))

