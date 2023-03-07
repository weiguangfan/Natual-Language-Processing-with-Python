# 组合标注器
# 解决精度和覆盖率之间的权衡的一个办法是尽可能的使用更精确的算法，
# 但却在很多时候落后于具有更广覆盖范围的算法。
import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
size = int(len(brown_tagged_sents) * 0.9)
print(size)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

# 尝试使用bigram标注器标注标识符
# 如果bigram标注器无法找到一个标记，尝试unigram标注器；
# 如果unigram标注器也无法找到一个标记，使用默认标注器；
# 大多数NLTK标注器允许指定一个回退标注器。
# 回退标注器自身可能也有一个回退标注器：
t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents,backoff=t0)
t2 = nltk.BigramTagger(train_sents,backoff=t1)
print(t2.accuracy(test_sents))

t3 = nltk.TrigramTagger(train_sents,backoff=t2)
print(t3.accuracy(test_sents))

# 在标注器初始化时指定回退标注器，从而使训练能利用回退标注器
# 如果在一个上下文中bigram标注器将分配与它的unigram回退标注器一样的标记，
# 那么bigram标注器丢弃训练的实例。
# 这样保持尽可能小的bigram标注器模型。
# 我们可以进一步指定一个标注器需要看到一个上下文的多个实例才能保留它。
# 例如：nltk.BigramTagger(sents,cutoff=2,backoff=t1)将会丢弃那些只看到一次或两次的上下文；

# 标注生词
# 我们标注生词的方法仍然是回退到一个正则表达式标注器或一个默认标注器。
# 这些都无法利用上下文。
# 一个有用的基于上下文标注生词的方法是限制一个标注器的词汇表为最频繁的n个词
# 替代每个其他的词为一个特殊的词UNK。
# 训练时，一个unigram标注器可能会学到UNK通常是一个名词。
# 然而，n-gram标注器会检测它的一些其他标记中的上下文。




