"""
unicodedata模块检查Unicode字符的属性
"""
import codecs
import nltk
import unicodedata
# 定位文件
path = nltk.data.find("corpora/unicode_samples/polish-lat2.txt")
# 以latin2为encoding参数，打开波兰语文件
lines = codecs.open(path, encoding='latin2').readlines()
print(lines)

line = lines[2]
print(line)

print(line.encode('unicode_escape'))

# 超出ASCII范围的字符，输出它们的：UTF-8转义值，使用标准Unicode约定的编码点整数，Unicode名称；
# for c in line:
#     if ord(c) > 127:
#         print("%r U+%04x %s",c.encode('utf8'),ord(c),unicodedata.name(c))
        # 格式化字符串时用%s替换%r(产生repr()值)
        # print("%s U+%04x %s",c.encode('utf8'),ord(c),unicodedata.name(c))

print(line.find(u'zosta\u0142y'))
line = line.lower()
print(line)
line = line.encode('unicode_escape')
print(line)


# re 模块接收Unicode字符串
# import re
# m = re.search(u'\u015b',line)
# print(m.group())

# NLTK分词器允许Unicode字符串作为输入，并输出相应的Unicode字符串
# print(nltk.word_tokenize(line))