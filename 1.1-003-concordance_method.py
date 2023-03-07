"""
获取词的每一次出现，连同词的上下文
"""

from nltk.book import *

print(text1.concordance("monstrous"))
print("$"*50)
print(text2.concordance("affection"))
print("$"*50)
print(text3.concordance("lived"))
print("$"*50)
print(text4.concordance("god"))
print("$"*50)
print(text5.concordance("im"))
