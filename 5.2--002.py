# 读取已标注的语料库
# nltk中包括的若干语料库已标注了词性。
import nltk
# 只要语料库包含已标注的文本，NLTK的语料库接口都将有一个tagged_words()方法。
# print(nltk.corpus.brown.tagged_words())

# 并非所有的语料库都采用同一组标记；
# 使用一个内置的到一个简化的标记集的映射
# print(nltk.corpus.brown.tagged_words(simplify_tags=True))
# print(nltk.corpus.treebank.tagged_words(simplify_tags=True))

# print(nltk.corpus.nps_chat.tagged_words())

# print(nltk.corpus.conll2000.tagged_words())

# print(nltk.corpus.treebank.tagged_words())

# nltk中还有其他几种语言的已标注语料库，
# 这些通常含有非ASCII文本，
# 当输出较大的结构如列表时，python总是以十六进制显示这些；
# 中文
# print(nltk.corpus.sinica_treebank.tagged_words())
# 印度
# print(nltk.corpus.indian.tagged_words())

# print(nltk.corpus.mac_morpho.tagged_words())

# print(nltk.corpus.conll2002.tagged_words())

# print(nltk.corpus.cess_cat.tagged_words())
# 如果语料库也被分割成句子，
# 将有一个tagged_sents()方法将已标注的词划分成句子，
# 而不是将它们表示成一个大链表

# 简化的词性标记集
# 已标注的语料库使用许多不同的标记集约定来标注词汇
# 查看哪些标记是布朗语料库的新闻类中最常见的
from nltk.corpus import brown
brown_news_tagged = brown.tagged_words(categories='news')
# print(brown_news_tagged)
# tag_fd = nltk.FreqDist(tag for (word,tag) in brown_news_tagged)
# print(tag_fd.keys())

# 使用标记做搜索，
# 结合一个图形化的pos一致性工具nltk.app.concordance(),
# 用它来寻找任一词和pos标记的组合
# print(nltk.app.concordance())

# 名词
# 名词一般指的是人、地点、事情或概念
# 名词可能出现在限定词和形容词之后，可以是动词的主语或宾语
# 检查哪些词类出现在一个名词前，频率最高的在最前面；
# 构建一个双连词链表,它的成员是它们自己的词-标记对
# 构建一个双连词的标记部分的FreqDist
word_tag_pairs = nltk.bigrams(brown_news_tagged)
# print(word_tag_pairs)
# print(list(nltk.FreqDist(a[1] for (a, b) in word_tag_pairs if b[1] == 'N')))

# 动词
# 动词是用来描述事件和行动的词
# 在一个句子中，动词通常表示涉及一个或多个名词短语所指示物的关系
# 新闻文本中最常见的动词是什么？按频率排序所有动词
wsj = nltk.corpus.treebank.tagged_words()
# print(wsj)
# 频率分布中计算的是词-标记对
word_tag_fd = nltk.FreqDist(wsj)
# print(word_tag_fd)
# print([word + "/" + tag for (word, tag) in word_tag_fd if tag.startswith('V')])

# 可以把词作为条件，标记作为事件
# 使用条件-事件对的链表初始化一个条件频率分布
# 看到一个给定的词的标记的频率顺序列表
cfd1 = nltk.ConditionalFreqDist(wsj)
# print(cfd1)
# print(cfd1.conditions())
# print(cfd1['yield'].keys())
# print(cfd1['cut'].keys())


# 颠倒配对的顺序，标记作为条件，词汇作为事件
# cfd2 = nltk.ConditionalFreqDist((tag,word) for (word,tag,) in wsj)
# print(cfd2)
# print(cfd2.conditions())
# print(cfd2['VN'].keys())

# print([w for w in cfd1.conditions() if 'VD' in cfd1[w] and 'Vn' in cfd1[w]])
# 查看周围文字
idx1 = wsj.index(('authorizes', 'VBZ'))
print(idx1)
print(wsj[idx1 - 4:idx1 + 1])

# 形容词修饰名词，可以作为修饰符或谓语
# 英语形容词可以有内部结构
# 副词修饰动词，指定时间、方式、地点或动词描述的事件的方向
# 副词也可以修饰形容词





