"""
就职演说语料库
"""
from nltk.corpus import inaugural

print(inaugural.fileids())

print([field[:4] for field in inaugural.fileids()])





