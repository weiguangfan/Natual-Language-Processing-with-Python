# -*- coding:unicode_escape -*-
from collections import Counter
import jieba

# jieba.load_userdict('userdict.txt')
# 创建停用词list
def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r').readlines()]
    return stopwords


# 对句子进行分词
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordslist('baidu_stopwords.txt')  # 这里加载停用词的路径
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    print(outstr)
    return outstr


inputs = open('roomName3.txt', 'rb') #加载要处理的文件的路径
outputs = open('output1.txt', 'w') #加载处理后的文件路径
for line in inputs:
    # print(line)
    line_seg = seg_sentence(line)  # 这里的返回值是字符串
    outputs.write(line_seg)
outputs.close()
inputs.close()

# WordCount
with open('output1.txt', 'r') as fr: #读入已经去除停用词的文件
    data = jieba.cut(fr.read())
data = dict(Counter(data))


with open('output2.txt', 'w') as fw: #读入存储wordcount的文件路径
    for k,v in data.items():
        fw.write('%s,%d\n' % (k, v))