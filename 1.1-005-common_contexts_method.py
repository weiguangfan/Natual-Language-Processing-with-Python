"""
显示两个及以上词的共同的上下文
"""

from nltk.book import *

print(text2.common_contexts({"monstrous", "very"}))