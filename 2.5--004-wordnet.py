"""
语义相似度
如果两个同义词集共用一个非常具体的上位词--在上位词层次结构中处于较低层的上位词--他们一定有密切的联系
"""
from nltk.corpus import wordnet as wn

# 查找同义词集
right = wn.synset("right_whale.n.01")
print(right)
orca = wn.synset("orca.n.01")
print(orca)
minke = wn.synset("minke_whale.n.01")
print(minke)
tortoise = wn.synset("tortoise.n.01")
print(tortoise)
novel = wn.synset("novel.n.01")
print(novel)

# 查找两个同义词集，共用的在上位词层次结构中处于较低层的上位词
print(right.lowest_common_hypernyms(minke))
print(right.lowest_common_hypernyms(orca))
print(right.lowest_common_hypernyms(tortoise))
print(right.lowest_common_hypernyms(novel))

# 实体完全是抽象的一般的
# 查找每个同义词集深度量化这个一般性的概念
print(wn.synset("baleen_whale.n.01").min_depth())
print(wn.synset("whale.n.02").min_depth())
print(wn.synset("vertebrate.n.01").min_depth())
print(wn.synset("entity.n.01").min_depth())


# path_similarityassigns
# 是基于上位词层次结构中相互连接的概念之间的最短路径在0-1范围的打分（两者之间没有路径就返回-1）
# 同义词集与自身比较将返回1
# 数字本身的意义并不大
print(right.path_similarity(minke))
print(right.path_similarity(orca))
print(right.path_similarity(tortoise))
print(right.path_similarity(novel))


