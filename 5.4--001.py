# 给文本自动添加词性标记
import nltk
from nltk.corpus import brown
# 自动标注
# brown_tagged_sents = brown.tagged_sents(categories='news')
# print(brown_tagged_sents)
# brown_sents = brown.sents(categories='news')
# print(brown_sents)


# 默认标注器
# tags = [tag for (word,tag) in brown.tagged_words(categories='news')]
# print(nltk.FreqDist(tags).max())

# raw = 'I do not like green eggs and ham, I do not like then Sam I an!'
# tokens = nltk.word_tokenize(raw)
# print(tokens)
# 默认的标注器可以帮助我们提高语言处理系统的稳定性
# default_tagger = nltk.DefaultTagger('NN')
# print(default_tagger.tag(tokens))
# print(default_tagger.evaluate(brown_tagged_sents))
# print(default_tagger.accuracy(brown_tagged_sents))


# 正则表达式标注器
# 正则表达式标注器基于匹配模式分配标记给标识符
# patterns = [
#     (r'.*ing$','VBG'),
#     (r'.*ed$',"VBD"),
#     (r'.*es$','VBZ'),
#     (r'.*ould$','MD'),
#     (r'.*\'s$','NN$'),
#     (r'.*s$','NNS'),
#     (r'^-?[0-9]+(.[0-9]+)?$','CD'),
#     (r'.*','NN')
#
# ]

# regexp_tagger = nltk.RegexpTagger(patterns)
# print(regexp_tagger)
# print(brown_sents[3])
# print(regexp_tagger.tag(brown_sents[3]))

# print(regexp_tagger.accuracy(brown_tagged_sents))


# 查询标注器 NLTK UnigramTagger
# 找出100个最频繁的词，存储它们最有可能的标记
# 使用这个信息，作为查找标注器（NLTk UnigramTagger）的模型
from operator import itemgetter
# print(brown.words(categories='news'))
# fd = nltk.FreqDist(brown.words(categories='news'))
# print(fd.keys())
# print([i for i,j in sorted(fd.items(), key=itemgetter(1), reverse=True)][:10])
# print(brown.tagged_words(categories='news'))
# cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
# print(cfd.keys())
# most_freq_words = list(fd.keys())[:100]
# print(most_freq_words)
# likely_tags = dict((word,cfd[word].max()) for word in most_freq_words)
# print(likely_tags.items())
# baseline_tagger = nltk.UnigramTagger(model=likely_tags)
# print(baseline_tagger)
# 现在应该并不奇怪，
# 仅仅知道100个最频繁的词的标记就使我们能正确标注很大一部分标识符（近一半，事实上）
# print(baseline_tagger.accuracy(brown_tagged_sents))

# 看看它在一些未标注的输入文本上做得如何
# sent = brown_sents[3]
# print(sent)
# print(baseline_tagger.tag(sent))
# 许多词都被分配了一个None标签，因它们不在100个最频繁的词之中
# 这些情况下，我们想分配默认标记NN
# 换句话说，我们要先使用查找表，
# 如果它不能指定一个标记就使用默认标注器，这个过程叫做回退；
# 我们可以做到这个，通过指定一个标注器作为另一个标注器的参数
# 现在查找标注器将只存储名词以外的词的词-标记对，
# 只要它不能给一个词分配标记，它将会调用默认标注器
# baseline_tagger = nltk.UnigramTagger(model=likely_tags,
#                                      backoff=nltk.DefaultTagger('NN'))


def performance(cfd,wordlist):
    lt = dict((word,cfd[word].max) for word in wordlist)
    baseline_tagger = nltk.UnigramTagger(model=lt,backoff=nltk.DefaultTagger('NN'))
    return baseline_tagger.accuracy(brown.tagged_sents(categories='news'))


def display():
    import pylab
    word_by_freq = list(nltk.FreqDist(brown.words(categories='news')))
    cfd = nltk.ConditionalFreqDist(brown.tagged_words(categories='news'))
    sizes = 2 ** pylab.arange(15)
    perfs =[performance(cfd,word_by_freq[:size]) for size in sizes]
    pylab.plot(sizes,perfs,'-bo')
    pylab.tile('Lookup Tagger Performance with Varying Model Size')
    pylab.xlabel('Model Size')
    pylab.ylabel('Performance')
    pylab.show()

display()
# 随着模型规模的增长，最初的性能增长迅速，最终达到一个稳定水平，
# 这时模型的规模大量增减性能的提升很小。






