"""
上位词和下位词被称为词汇关系，因为它们是同义词集之间的关系；
从物品到它们的部件（部分）或到它们被包含其中的东西（整体）
"""
import nltk
from nltk.corpus import wordnet as wn
# 查找同义词集
print(wn.synset("tree.n.01"))
# 查找同义词集的上位词
print(wn.synset("tree.n.01").hypernyms())
# 查找同义词集的下位词
print(wn.synset("tree.n.01").hyponyms())
# 从物体到它们的部分
print(wn.synset("tree.n.01").part_meronyms())
# 物体的实质
print(wn.synset("tree.n.01").substance_meronyms())
# 物体的集合
print(wn.synset("tree.n.01").member_holonyms())

# 获取mint的同义词集
print(wn.synsets("mint"))
print(wn.synsets("mint", wn.NOUN))

# 具有几个密切相关意思的词mint
# 获取同义词集的名字和定义
for synset in wn.synsets("mint",wn.NOUN):
    print(synset.name() + ":", synset.definition())


# 从物体到部分
print(wn.synset("mint.n.04").part_holonyms())
# 物体的实质
print(wn.synset("mint.n.04").substance_holonyms())



# 动词之间也有关系
# 走路的动作包括抬脚的动作
print(wn.synset("walk.v.01").entailments())
# 吃的动作包括咀嚼和咽下的动作
print(wn.synset("eat.v.01").entailments())
# 戏弄的动作包括激怒和失望
print(wn.synset("tease.v.03").entailments())


# 词条之间的一些词汇关系：反义词
print(wn.lemma("supply.n.02.supply"))
# supply的反义词demand
print(wn.lemma("supply.n.02.supply").antonyms())
# rush的反义词linger
print(wn.lemma("rush.v.01.rush").antonyms())
# horizontal的反义词vertical
print(wn.lemma("horizontal.a.01.horizontal").antonyms())
# staccato的反义词legato
print(wn.lemma("staccato.r.01.staccato").antonyms())

# dir()查看词汇关系和同义词集上定义的其它方法
print(dir(wn.synset("harmony.n.02")))
