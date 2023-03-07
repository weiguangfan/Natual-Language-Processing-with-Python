"""
查看词频分布
"""

from nltk.book import *

fdist1 = FreqDist(text1)
# print(fdist1)
# print("$"*50)
# vocabulary1 = fdist1.keys()
# print(vocabulary1)
# print("$"*50)
# print(vocabulary1[:50])
print("$"*50)
print(fdist1["whale"])
# fdist1.plot(50,cumulative=True)  # 高频词的分布
print("$"*50)
print(fdist1.hapaxes()) # 只出现一次的词
