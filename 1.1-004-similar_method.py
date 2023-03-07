"""
显示哪些词具有相似的上下文
"""

from nltk.book import *
print("$"*50)
print(text1.similar("monstrous"))
print("$"*50)
print(text2.similar("monstrous"))