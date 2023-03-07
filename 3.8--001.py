import pprint

import nltk
# 断句
# 布朗语料库
# print(nltk.corpus.brown)
# 57340个句子
# print(nltk.corpus.brown.sents())
# print(len(nltk.corpus.brown.sents()))
# print(nltk.corpus.brown.words())
# 1161192个单词
# print(len(nltk.corpus.brown.words()))
# 每个句子的平均词数
# 20.250994070456922个词，每个句子中
# print(len(nltk.corpus.brown.words()) / len(nltk.corpus.brown.sents()))

# nltk通过包含Punkt句子分割器，将文本分割成句子
# sent_tokenizer = nltk.data.load("tokenizers/punkt/english.pickle")
# print(sent_tokenizer)

# text = nltk.corpus.gutenberg.raw('chesterton-thursday.txt')
# print(text)

# 断句比较困难
# sents = sent_tokenizer.tokenize(text)
# pprint.pprint(sents[-20:])

# 分词
a = 'doyouseethekitty'
b = 'seethedoggy'
c = 'doyoulikethekitty'
d = 'likethedoggy'
text = a + b + c + d
# print(text)
# 给每个字符标注一个布尔值来指示这个字符后面是否有一个分词标志
# 初始分词
seg1 = '0000000000000001000000000010000000000000000100000000000'
# print(len(seg1))
# 最终分词
seg2 = '0100100100100001001001000010100100010010000100010010000'
seg3 = '0000100100000011001000000110000100010000001100010000001'

def segment(text,segs):
    words = []
    last = 0
    for i in range(len(segs)):
        if segs[i] == '1':
            words.append(text[last:i+1])
            last = i + 1
    words.append(text[last:])
    return words


# print(segment(text, seg1))
# print(segment(text, seg2))
# print(segment(text, seg3))

# 找到将文本字符串正确分割成词汇的字位串，我们假定学习者接收词，将它们存储在一个内部词典中。
# 给定一个合适的词典，是能够由词典中的词的序列来重构源文本的。
# 计算目标函数：给定一个假设的源文本的分词，推导出一个词典和推导表，它能让源文本重构，
# 然后合计每个词项（包括边界标志）与推导表的字符数，作为分词质量的得分；
# 分值越小表明分词越好


def evaluate(text,segs):
    words = segment(text,segs)
    # print(words)
    text_size = len(words)
    # print(text_size)
    # print(list(set(words)))
    lexicon_size = len(' '.join(list(set(words))))
    # print(lexicon_size)
    return text_size + lexicon_size


# print(evaluate(text, seg3))
# print(evaluate(text, seg2))
# print(evaluate(text, seg1))

# 寻找最大化目标函数值的0和1的模式
# 使用模拟退火算法的非确定性搜索：
# 一开始仅搜索短语分词；
# 随机扰动0和1，它们与‘温度’成正比；
# 每次迭代温度都会降低，扰动边界会减少
from random import randint


def flip(segs,pos):
    """更改pos处的值：0或1"""
    return segs[:pos] + str(1 - int(segs[pos])) + segs[pos+1:]


def flip_n(segs,n):
    """一共随机更改len(segs)次"""
    for i in range(n):
        segs = flip(segs,randint(0,len(segs) - 1))
    return segs


def anneal(text,segs,iterations,cooling_rate):
    """

    :param text: 原始文本
    :param segs: 随机扰动后的文本
    :param iterations: 扰动次数
    :param cooling_rate: 下降比值
    :return:
    """
    temperature = float(len(segs))
    print(temperature)
    while temperature > 0.5:
        # text不变；segs一直在变；
        best_segs,best = segs,evaluate(text,segs)
        for i in range(iterations):
            # guess 是一直在变
            guess = flip_n(segs,int(round(temperature)))
            # guess的分值，也是一直在变
            score = evaluate(text,guess)
            # 分值越小越好
            if score < best:
                # 文本和分值，都进行替换
                best,best_segs = score,guess
        # 小循环结束，文本和分值再次进行替换
        score,segs = best,best_segs
        # 温度下降
        temperature = temperature / cooling_rate
        print(temperature)
        # 打印此时的分值和分词
        print(evaluate(text,segs),segment(text,segs))
    # 大循环结束，返回文本
    return segs


print(anneal(text, seg1, 5000, 1.2))

# 有了足够的数据，就可能以一个合理的准确度自动将文本分割成词汇。
# 这种方法可用于为哪些词的边界没有任何视觉表示的书写系统分词


