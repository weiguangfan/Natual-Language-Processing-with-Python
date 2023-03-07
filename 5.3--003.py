# 复杂的键和值
# 我们可以使用具有复杂的键和值的默认字典
# 研究一个词可能的标记的范围，给定词本身和它前一个词的标记
import nltk
from nltk.corpus import brown
# 使用了一个字典，它的条目的默认值也是一个字典（其默认值是int()，即0）
# pos = nltk.defaultdict(lambda :nltk.defaultdict(int))
# print(pos)
# brown_news_tagged = brown.tagged_words(categories='news')
# print(brown_news_tagged)
# print(list(nltk.bigrams(brown_news_tagged))[:2])
# for ((w1,t1),(w2,t2)) in nltk.bigrams(brown_news_tagged):
    # 每次遍历处理一个词-标记对
    # 每次通过循环时，我们更新字典pos中的条目(t1,w2),一个标记和它后面的词

    # pos[(t1,w2)][t2] += 1
# 当我们在pos再查找一个项目时，我们必须指定一个复合键，然后得到一个字典对象
# print(pos[("DET", 'right')])

# counts = nltk.defaultdict(int)
# for word in nltk.corpus.gutenberg.words('milton-paradise.txt'):
#     counts[word] += 1

# print([key for (key, value) in counts.items() if value == 32])

pos = {"colorless":'ADJ',"ideas":'N','sleep':'V','furiously':'ADV'}
# pos2 = dict((value,key) for (key,value) in pos.items())
# print(pos2['N'])

pos.update({'cats':'N',"scratch":'V','peacefully':'ADV','old':'ADJ'})
print(pos)

pos2 = nltk.defaultdict(list)
for key,value in pos.items():
    # append()积累词和每个词性
    pos2[value].append(key)
print(pos2['ADV'])

# 可以使用nltk中索引支持
pos3 = nltk.Index((value,key) for (key,value) in pos.items())
print(pos3['ADV'])