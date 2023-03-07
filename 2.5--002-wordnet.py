"""
层次结构
实体、状态、事件，这些被称为独一无二的根同义词集；
wordnet概念：
每个节点对应一个同义词集；
边表示上位词/下位词关系，即上级概念与从属概念的关系；
"""
from nltk.corpus import wordnet as wn

# 查找同义词集
motorcar = wn.synset("car.n.01")
print(motorcar)

# 查找同义词集的下位词
# 下位词，一系列的同义词集
types_of_motorcar = motorcar.hyponyms()
print(types_of_motorcar)
# 索引获取下位词
print(types_of_motorcar[26])
# 获取特定同义词集的下位词的每个同义词集的词条的名字
# print(sorted([lemma.name for synset in types_of_motorcar for lemma in synset.lemmas()]))


# 查找同义词集的一个上位词路径
print(motorcar.hypernyms())
# 查找同义词集的所有上位词路径
paths = motorcar.hypernym_paths()
print(paths)
# 两条路径
print(len(paths))
# 第一条路径
print([synset.name for synset in paths[0]])
# 第二条路径
print([synset.name for synset in paths[1]])

# 得到一个最一般的上位（或根上位）同义词集
print(motorcar.root_hypernyms())
