"""
同义词
"""
from nltk.corpus import wordnet as wn

# motorcar只有一个可能的含义，它被定义为car.n.01，car的第一个名词意义；
# car.n.01被称为synset或“同义词集”，意义相同的词（或“词条”）的集合；
print(wn.synsets("motorcar"))  # synset同义词集
print(wn.synset("car.n.01").lemma_names)  # 同义词集的元素
for i in wn.synset("car.n.01").lemma_names():
    print(i)

# 同义词集一般的定义
# 定义帮助人们了解一个同义词集的本意
print(wn.synset("car.n.01").definition())
print(wn.synset("car.n.01").examples())  # 例句

# 同义词集和词的配对叫做词条
# 得到同义词集的所有词条
print(wn.synset("car.n.01").lemmas())


# 查找特定的词条
print(wn.lemma("car.n.01.automobile"))


# 查找一个词条对应的同义词集
print(wn.lemma("car.n.01.automobile").synset())

# 得到一个词条的名字
print(wn.lemma("car.n.01.automobile").name())


# car有五个同义词集
print(wn.synsets("car"))
# 遍历每一个词集的所有词条
for synset in wn.synsets("car"):
    print(synset.lemma_names())
    print(synset.lemmas())

# 查找所有包含词car的词条
print(wn.lemmas("car"))
