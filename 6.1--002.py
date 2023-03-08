# 选择正确的特征

# 选择相关的特征，并决定如何为一个学习方法编码它们，
# 这对学习方法提取一个好的模型可以产生巨大的影响；
# 建立一个分类器的很多有趣的工作之一是找出哪些特征可能是相关的，
# 以及我们如何能够表示它们。
# 虽然使用相当简单而明显的特征集往往可以得到像样的性能，
# 但是使用精心构建的基于对当前任务的透彻理解的特征，通常会显著提高收益。

# 典型地，特征提取通过反复实验和错误的过程建立的，由哪些信息是与问题相关的直觉指引的。
# 它通常以“厨房水槽”的方法开始，
# 包括你能想到的所有特征，
# 然后检查哪些特征是实际有用的。
import nltk
# def gender_features(word):
#     """
#     特征提取器函数建立一个字典，包含有关给定名称的相关信息；
#     :param word:
#     :return:
#     """
#     return {'last_letter':word[-1]}


# def gender_features2(name):
#     """
#     一个特征提取器，过拟合性别特征。
#     这个特征提取器返回的特征集包括大量指定的特征，
#     从而导致对于相对较小的名字语料库过拟合。
#     :param name:
#     :return:
#     """
#     features = {}
#     features['firstletter'] = name[0].lower()
#     features['lastletter'] = name[-1].lower()
#     for letter in 'abcdefghijklmnopqrstuvwxyz':
#         features["count(%s)" % letter] = name.lower().count(letter)
#         features["has(%s)" % letter] = (letter in name.lower())
#     return features


# print(gender_features2('John'))


# 然而，你要用于一个给定的学习算法的特征的数目是有限的---
# 如果你提供太多的特征，那么该算法将高度依赖你的训练数据的特性，
# 而一般化到新的例子的效果不会很好。
# 这个问题被称为过拟合。
# 当运作在小训练集上时尤其会有问题。
from nltk.corpus import names
import random
names = ([(name,'male') for name in names.words('male.txt')]
         + [(name,'female') for name in names.words('female.txt')])

# print(names)
random.shuffle(names)

# 造成系统的精度比只考虑每个名字最后一个字母的分类器的精度低约1%
# featuresets = [(gender_features2(n),g) for (n,g) in names]
# train_set,test_set = featuresets[500:],featuresets[:500],
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, test_set))

# 一旦初始特征集被选定，完善特征集的一个非常有成效的方法是错误分析。
# 首先，我们选择一个开发集，包含用于创建模型的语料数据。
# 然后将这种开发集分为训练集和开发测试集。
train_names = names[1500:]
devtest_names = names[500:1500]
test_names = names[:500]

# 训练集用于训练模型，开发测试集用于进行错误分析，测试集用于系统的最终评估。
# train_set = [(gender_features(n),g) for (n,g) in train_names]
# devtest_set = [(gender_features(n),g) for (n,g) in devtest_names]
# print(devtest_set)
# test_set = [(gender_features(n),g) for (n,g) in test_names]
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, devtest_set))

# 语料数据分为两类：开发集和测试集。
# 开发集通常被进一步分为训练集和开发测试集。
# 使用开发测试集，我们可以生成一个分类器预测名字性别时的错误列表。
# errors = []
# for (name,tag) in devtest_names:
#     guess = classifier.classify(gender_features(name))
#     if guess != tag:
#         errors.append((tag,guess,name))
# print(errors)
# 然后，可以检查个别错误案例，
# 在那里该模型预测了错误的标签，
# 尝试确定什么额外信息将使其能够作出正确的决定（或者现有的哪部分信息导致其做出错误的决定）
# 然后可以相应的调整特征集。
# for (tag,guess,name) in sorted(errors):
#     print('correct=%-8s guess=%-8s name=%-30s' % (tag,guess,name))
# 浏览这个错误列表，它明确指出一些多个字母的后缀可以指示名字性别。
# 因此，调整我们的特征提取器包括两个字母的后缀的特征：


def gender_features(word):
    return {'suffix1':word[-1:],'suffix2':word[-2:]}


train_set = [(gender_features(n),g) for (n,g) in train_names]
devtest_set = [(gender_features(n),g) for (n,g) in devtest_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
# 使用新的特征提取器重建分类器，我们看到测试数据集上的性能提高了
print(nltk.classify.accuracy(classifier, devtest_set))

# 这个错误分析过程可以不断重复，检查存在于由新改进的分类器产生的错误中的模式，
# 每一次错误分析过程被重复，我们应该选择一个不同的开发测试/训练分割，以确保该分类器不会开始反映开发测试集的特质。
# 但是，一旦我们已经使用了开发测试集帮助我们开发模型，关于这个模型在新数据会表现多好，
# 我们将不能再相信它会给我们一个正确地结果！
# 因此，保持测试集分离、未使用过，直到我们的模型开发完毕是很重要的。
# 在这一点上，我们可以使用测试集评估模型在新的输入值上执行的有多好。










