"""
网络文本小集合
"""
from nltk.corpus import webtext

for fileid in webtext.fileids():
    print(fileid,webtext.raw(fileid)[:65])
    print("$"*50)

