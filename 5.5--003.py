# 存储标注器
from pickle import dump
import nltk
from nltk.corpus import brown

brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
print(size)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents,backoff=t0)
t2 = nltk.BigramTagger(train_sents,backoff=t1)

# output = open('t2.pkl','wb')
# dump(t2, output, -1)
# output.close()

from pickle import load
# input = open('t2.pkl','rb')
# tagger = load(input)
# print(tagger)
# input.close()

text = '''
The board's action shows what free enterprise is up against in our complex maze of regulatory laws.

'''

# tokens = text.split()
# print(tagger.tag(tokens))


# 性能限制
# cfd = nltk.ConditionalFreqDist(
#     ((x[1],y[1],z[0]),z[1])
#     for sent in brown_tagged_sents
#     for x,y,z in nltk.trigrams(sent)
# )
# ambiguous_contexts = [c for c in cfd.conditions() if len(cfd[c]) > 1]
# print(sum(cfd[c].N() for c in ambiguous_contexts) / cfd.N())

# 1/20的trigrams是有歧义的。
# 给定当前单词及其前两个标记，根据训练数据，在5%的情况中，
# 有一个以上的标记可能合理地分配给当前词。
# 假设我们总是挑选在这种含糊不清的上下文中最优可能的标记，
# 可以得出trigram标注器性能的一个下界。


# 调查标注器性能的另一种方法是研究它的错误
# 一个方便的方式查看标注错误是混淆矩阵
# test_tags = [tag for sent in brown.sents(categories='news')
#              for (word,tag) in t2.tag(sent)]
#
# gold_tags = [tag for (word,tag) in brown.tagged_words(categories='news')]
#
# print(nltk.ConfusionMatrix(gold_tags, test_tags))

# 跨句子边界标注
print(t2.accuracy(test_sents))

