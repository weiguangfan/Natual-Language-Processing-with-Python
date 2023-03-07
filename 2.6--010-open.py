"""
读取本地文件
"""
import nltk
import os
print(os.listdir('.'))  # 检查当前目录
f = open("./test.txt")
print(f)
raw = f.read()
print(raw)

f = open("./test.txt","r")
for line in f:
    print(line.strip())  # strip()删除输入行结尾的换行符


# nltk.download("gutenberg")
# path = nltk.data.find("corpora/gutenberg/melville-moby_dict.txt")
# raw = open(path).read()
# print(raw)

