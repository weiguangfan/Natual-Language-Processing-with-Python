# 学习分类文本
# 模式识别是自然语言处理的一个核心部分
# 可观察到的模式---词的结构和词频---恰好与特定方面的含义关联，
# 如：时态和主题
# 有监督分类
# 分类是为给定的输入选择正确的类标签的任务。
# 在基本的分类任务中，每个输入被认为是与所有其它输入隔离的，并且标签是预先定义的。

# 基本的分类任务有许多有趣的变种。
# 例如：在多类分类中，每个实例可以分配多个标签；
# 在开放性分类中，标签集是事先没有定义的；
# 在序列分类中，一个输入链表作为一个整体分类；

# 如果分类的建立基于包含每个输入的正确标签的训练语料，被称为有监督分类；
# 在训练过程中，特征提取器用来将每一个输入值转换为特征集。
# 这些特征集捕捉每个输入中应被用于对其分类的基本信息；
# 特征集与标签的配对被送入机器学习算法，生成模型；
# 在预测过程中，相同的特征提取器被用来将未见过的输入转换为特征集；
# 之后，这些特征集被送入模型产生预测标签；


# 性别鉴定
# 创建一个分类器的第一步是决定输入的什么样的特征是相关的，
# 以及如何为那些特征编码。

import nltk

# 在这个例子中，我们一开始只是寻找一个给定的名称的最后一个字母；
def gender_features(word):
    """
    特征提取器函数建立一个字典，包含有关给定名称的相关信息；
    :param word:
    :return:
    """
    return {'last_letter':word[-1]}


# print(gender_features('Shrek'))
# 这个函数返回的字典被称为特征集，映射特征名称到它们的值。
# 特征名称是区分大小写的字符串，通常提供一个简短的人可读的特征描述；
# 特征值是简单类型的值，如布尔、数字和字符串

# 大多数分类方法要求特征使用简单的类型进行编码，如布尔类型、数字和字符串。
# 但要注意仅仅因为一个特征是简单类型，并不一定意味着该特征的值易于表达或计算；
# 的确，它可以用非常复杂的和有信息量的值作为特征；

# 现在，我们已经定义了一个特征提取器，
# 我们需要准备一个例子和对应类标签的链表
from nltk.corpus import names
import random
names = ([(name,'male') for name in names.words('male.txt')]
+ [(name,'female') for name in names.words('female.txt')])

# print(names)
random.shuffle(names)

# 接下来，使用特征提取器处理名称数据，
# 并划分特征集的结果链表为一个特征集和一个测试集；
# 训练集用于训练一个新的朴素贝叶斯分类器

featuresets = [(gender_features(n),g) for (n,g) in names]
train_set,test_set = featuresets[500:],featuresets[:500],
classifier = nltk.NaiveBayesClassifier.train(train_set)

# 现在，让我们只是在上面测试一些没有出现在训练数据中的名字
# print(classifier.classify(gender_features('Neo')))
# print(classifier.classify(gender_features('Trinity')))

# 我们可以在大数据量的未见过的数据上系统地评估这个分类器
print(nltk.classify.accuracy(classifier,test_set))

# 最后，我们可以检查分类器，确定哪些特征对于区分名字的性别是最有效的；
# print(classifier.show_most_informative_features(5))
# 显示结果最后一列，这些比率称为似然比，可以用于比较不同特征-结果关系

# 在处理大型语料库时，
# 构建一个包含每一个实例的特征的单独的链表会使用大量的内存。
# 在这些情况下，使用函数nltk.classify.apply_features,
# 返回一个行为像一个链表而不会在内存存储所有特征集的对象
# from nltk.classify import apply_features
# train_set = apply_features(gender_features,names[500:])
# test_set = apply_features(gender_features,names[:500])
# print(train_set)
# print(test_set)
