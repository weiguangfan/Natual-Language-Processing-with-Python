# 评估
# 为了决定一个分类模型是否准确地捕捉了模式，
# 我们必须评估该模型。
# 评估的结果对于决定模型是多么值得信赖以及我们如何使用它是非常重要。
# 评估也可以是一个有效的工具，
# 用于指导我们在未来改进模型。

# 测试集
# 大多数评估技术为模型计算一个得分，
# 通过比较它在测试集（或评估集）中为输入生成的标签与那些输入的正确标签。
# 该测试集通常与训练集具有相同的格式。
# 然而，测试集与训练语料不同是非常重要的：
# 如果我们简单地重复使用训练集作为测试集，
# 那么一个只记住了它的输入而没有学会如何推广到新的例子的模型会得到误导人的高分。


# 建立测试集时，往往是一个可用于测试的和可用于训练的数量之间的权衡。
# 对于有少量平衡的标签和一个多样化的测试集的分类任务，
# 只要100个评估实例就可以进行有意义的评估。
# 但是，如果一个分类任务有大量的标签或包括非常罕见的标签，
# 你们选择的测试集的大小就要保证出现次数最少的标签至少出现50次。

# 此外，如果测试集包含许多密切相关的实例---
# 例如：来自一个独立文档中的实例---
# 你们测试集的大小应增加，
# 以确保这种多样性的缺乏不会扭曲评估结果。
# 当有大量已标注数据可用时，只使用整体数据的10%进行评估常常会在安全方面犯错。

# 选择测试集时，另一个需要考虑的是测试集中实例与开发集中的实例的相似程度。
# 这两个数据集越相似，我们对将评估结果推广到其他数据集的信心就越小。
# 例如：考虑词性标注任务。
# 在一种极端情况，
# 我们可以通过从一个反映单一的文体（如新闻）的数据源随机分配句子，
# 创建训练集和测试集
import random

import nltk
from nltk.corpus import brown
# tagged_sents = list(brown.tagged_sents(categories='news'))
# random.shuffle(tagged_sents)
# size = int(len(tagged_sents) * 0.1)
# train_set,test_set = tagged_sents[size:],tagged_sents[:size],
# 这种情况下，我们的测试集和训练集将是非常相似的。
# 训练集和测试集均取自同一文体，
# 所以我们不能相信评估结果可以推广到其他文体。
# 更糟糕的是，因为调用random.shuffle()，
# 测试集中包含来自训练使用过的相同的文档的句子。
# 如果文档中有相容的模式
# （也就是说，如果一个给定的词与特定词性标记一起出现特别频繁），
# 那么这种差异将体现在开发集和测试集。
# 一个稍好的做法是确保训练集和测试集来自不同的文件：
# file_ids = brown.fileids(categories='news')
# size = int(len(file_ids) * 0.1)
# train_set = brown.tagged_sents(file_ids[size:])
# test_set = brown.tagged_sents(file_ids[:size])

# 如果我们要执行更令人信服的评估，
# 可以从与训练集中文档联系更少的文档中获取测试集。
# train_set = brown.tagged_sents(categories='news')
# test_set = brown.tagged_sents(categories='fiction')
# 如果我们在此测试集上建立了一个性能很好的分类器，
# 那么我们完全可以相信它有能力很好的泛化到用于训练它的数据以外的。


# 准确度
# 用于评估一个分类最简单的度量是准确度，
# 测量测试集上分类器正确标注的输入的比例。
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print('Accuracy:%4.2f' % nltk.classify.accuracy(classifier,test_set))

# 解释一个分类器的准确性得分，考虑测试集中单个类标签的频率是很重要的。
# 例如：考虑一个决定词bank每次出现的正确的词意的分类器。

# 精确度和召回率
# 另一个准确度分数可能会产生误导的实例是在“搜索”任务中，
# 如：信息检索，我们试图找出与特定任务有关的文档。
# 由于不相关的文档的数量远远多于相关文档的数量，
# 一个将每一个文档都标记为无关的模型的准确度分数将非常接近100%。
# 因此，对搜索任务使用不同的测量集是很常见的。

# 真阳性是相关项目中我们正确识别为相关的。
# 真阴性是不相关项目中我们正确识别为不相关的。
# 假阳性是不相关项目中我们错误识别为相关的。
# 假阴性是相关项目中我们错误识别为不相关的。

# 精确度（Precision），表示我们发现的项目中有多少是相关的，TP/(TP + FP)
# 召回率（Recall），表示相关的项目中我们发现了多少，TP/(TP + FN)
# F-度量值（F-Measure）（或F-得分），组合精确度和召回率为一个单独的得分，
# 被定义为精确度和召回率的调和平均数(2 * Precision * Recall) / (Precision + Recall)

# 混淆矩阵
# 当处理有3个或更多的标签的分类任务时，
# 基于模型错误类型，细分模型的错误是有信息量的。
# 一个混淆矩阵是一个表，其中每个cells[i,j]表示正确的标签i被预测为标签j的次数。
# 因此，对角线项目（即cells[i,i]）表示正确预测的标签，
# 非对角线项目表示错误。


def tag_list(tagged_sents):
    """
    得到每个句子的每个词的词性
    :param tagged_sents:
    :return:
    """
    return [tag for sent in tagged_sents for (word,tag) in sent]


def apply_tagger(tagger,corpus):
    return [tagger.tag(nltk.tag.untag(sent)) for sent in corpus]

brown_tagged_sents = brown.tagged_sents(categories='editorial')
size = int(len(brown_tagged_sents) * 0.9)
train_sents = brown_tagged_sents[:size]
test_sents = brown_tagged_sents[size:]

t0 = nltk.DefaultTagger('NN')
t1 = nltk.UnigramTagger(train_sents,backoff=t0)
t2 = nltk.BigramTagger(train_sents,backoff=t1)


gold = tag_list(brown.tagged_sents(categories='editorial'))
test = tag_list(apply_tagger(t2,brown.tagged_sents(categories='editorial')))
cm = nltk.ConfusionMatrix(gold,test)
print(cm)

# 交叉验证
# 为了评估我们的模型，我们必须为测试集保留一部分已标注的数据。
# 正如我们提到的，如果测试集太小了，我们的评价可能不准确。
# 然而，测试集设置较大通常意味着训练集设置较小，
# 如果已标注的数据的数量有限，这样设置对性能会产生重大影响。


# 这个问题的解决方案之一是在不同的测试集上执行多个评估，
# 然后组合这些评估的得分，这种技术被称为交叉验证。
# 特别是，我们将原始语料细分为N个子集称为折叠（folds）,
# 对于每一个这些的折叠，我们使用除这个折叠中的数据外其他对于数据训练模型，
# 然后在这个折叠上测试模型。
# 即使个别的折叠可能是太小了，而不能在其上给出准确的评价分数，
# 综合评估得分是基于大量的数据，因此是相当可靠的。

# 第二，同样重要的，采用交叉验证的优势是，
# 它可以让我们研究不同的训练集上性能变化有多大。
# 如果我们从所有N个训练集得到非常相似的分数，
# 然后我们可以相当有信心，得分是准确的。
# 另一方面，如果N个训练集上分数很大不同，
# 那么，我们应该对评估得分的准确性保持怀疑态度。


