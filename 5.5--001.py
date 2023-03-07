# N-gram标注
# 一元标注（Unigram Tagging）
# 一元标注器基于一个简单的统计算法：
# 对每个标识符分配这个独特的标识符最有可能的标记。
# 一个一元标注器的行为就像一个查找标注器，
# 除了有一个更方便的建立它的技术，称为训练
import nltk
from nltk.corpus import brown
brown_tagged_sents = brown.tagged_sents(categories='news')
brown_sents = brown.sents(categories='news')
# unigram_tagger = nltk.UnigramTagger(brown_tagged_sents)
# print(unigram_tagger.tag(brown_sents[2007]))
# print(unigram_tagger.accuracy(brown_tagged_sents))
# 我们训练一个UnigramTagger,
# 通过在我们初始化标注器时指定已标注的句子数据作为参数。
# 训练过程中涉及检查每个词的标记，将所有词的最可能的标记存储在一个字典里面
# 这个字典存储在标注器内部


# 分离训练和测试数据
# 在一些数据上训练一个标注器，必须小心不要在相同的数据上测试；
# 一个只是记忆它的训练数据，
# 而不是试图建立一个一般的模型的标注器会得到一个完美的得分，但在标注新的文本时将是无用的；
# 分割数据，90% 为测试数据，其余10%为测试数据
size = int(len(brown_tagged_sents) * 0.9)
print(size)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]
# unigram_tagger = nltk.UnigramTagger(train_sents)
# print(unigram_tagger.accuracy(test_sents))
# 虽然得分更糟糕了，但是我们现在对这种标注器是无用的（如：它在前所未见的文本上的性能）有一个刚好的了解。


# 一般的N-gram的标注
# 在基于unigram处理一个语言处理任务时，我们使用上下文中的一个项目。
# 标注的时候，我们只考虑当前的标识符，与更大的上下文隔离；
# 给定一个模型，我们能做的最好的是为每个词标注其先验的最可能的标记；
# 这意味着我们将使用相同的标记标注一个词。
# 一个 n-gram标注器是一个unigram标注器的一般化，
# 它的上下文是当前词和它前面n-1个标识符的词性标记。
# 一个n-gram标注器挑选在给定的上下文中最可能的标记。
# 1-gram标注器是一元标注器（unigram tagger）另一个名称：
# 即用于标注一个标注符的上下文的只是标识符本身。
# 2-gram标注器也称为二元标注器（bigram taggers）
# 3-gram标注器也称为三元标注器（trigram tagger）
# NgramTagger类使用一个已标注的训练语料库来确定对每个上下文那个词性标记最可能。
# bigram标注器
bigram_tagger = nltk.BigramTagger(train_sents)
print(bigram_tagger.tag(brown_sents[2007]))
unseen_sent = brown_sents[4203]
print(bigram_tagger.tag(unseen_sent))
# 请注意，bigram标注器能够标注训练中它看到过的句子中的所有词，但对一个没见过的句子表现很差。
# 只要一到一个新词，就无法给它分配标记。
# 它的整体准确度得分非常低。
print(bigram_tagger.accuracy(test_sents))
# 当n越大，上下文的特异性就会增加，我们要标注的数据中包含训练数据中不存在的上下文的几率也增大。
# 这被称为数据稀疏问题，在NLP中是相当普遍的。
# N-gram标注器不应考虑跨越句子边界的上下文。
# 因此，NLTk的标注器被涉及用于句子链表，一个句子是一个词链表。
# 在一个句子的开始，t_n-1 和前面的标记被设置为None

