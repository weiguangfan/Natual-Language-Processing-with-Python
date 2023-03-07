# 未简化的标记
# 找出名词类型中最频繁的名词
import nltk


# def findtags(tag_prefix,tagged_text):
#     cfd = nltk.ConditionalFreqDist(
#         (tag,word) for (word,tag) in tagged_text
#         if tag.startswith(tag_prefix)
#     )
#     return dict((tag,list(cfd[tag].keys())[:5]) for tag in cfd.conditions())


# print(nltk.corpus.brown.tagged_words(categories='news'))
# tagged_text = nltk.corpus.brown.tagged_words(categories='news')
# print([i[0] for i in tagged_text if i[1].startswith('NN')])
# cfd = nltk.ConditionalFreqDist(
#     (tag,word) for (word,tag) in tagged_text
#     if tag.startswith('NN')
# )
# print(cfd.conditions())
# print(list(cfd["NN"].keys())[:5])



# tagdict = findtags('NN',nltk.corpus.brown.tagged_words(categories='news'))
# print(tagdict.items())
# for tag in sorted(tagdict):
#     print(tag,tagdict[tag])


# 查看跟在often后面的词汇
# brown_learned_text = nltk.corpus.brown.words(categories='learned')
# print(brown_learned_text)
# print(nltk.bigrams(brown_learned_text))
# print([(a, b) for (a, b) in nltk.bigrams(brown_learned_text)])
# print(sorted(set(b for (a, b) in nltk.bigrams(brown_learned_text) if a == 'often')))

# 使用tagged_words()方法查看跟随词的词性标记可能更具有指导性
# brown_lrnd_tagged = nltk.corpus.brown.tagged_words(categories='learned')
# print(brown_lrnd_tagged)
# tags = [b[1] for (a,b) in nltk.bigrams(brown_lrnd_tagged) if a[0] == 'often']
# print(tags)
# fd = nltk.FreqDist(tags)
# fd.tabulate()
# often后面最高频率的词性是动词。名词从来没有在这个位置出现（在这个特别的语料中）

# 看一些较大范围的上下文，找出涉及特定标记和词序列的词
from nltk.corpus import brown

# print(brown.tagged_sents())
# print(list(nltk.trigrams(brown.tagged_sents()[0])))

# def process(sentence):
#     for (w1,t1),(w2,t2),(w3,t3) in nltk.trigrams(sentence):
#         if (t1.startswith('V') and t2 == "TO" and t3.startswith('V')):
#             print(w1,w2,w3)


# for tagged_sent in brown.tagged_sents():
#     process(tagged_sent)

# 看看与它们的标记关系高度模糊不清的词
brown_news_tagged = brown.tagged_words(categories='news')
# print(brown_news_tagged)
data = nltk.ConditionalFreqDist(
    (word.lower(),tag)
    for (word,tag) in brown_news_tagged
)
# print(data.conditions())
# print(data.items())
# print(data['the'])
# print(data['the'].keys())
for word in data.conditions():
    if len(data[word]) > 3:
        tags = data[word].keys()
        print(word,' '.join(tags))
