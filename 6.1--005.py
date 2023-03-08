# 序列分类
# 为了捕捉相关的分类任务之间的依赖关系，我们可以使用联合分类器模型，
# 收集有关输入，选择适当的标签。
# 在词性标注的例子中，
# 各种不同的序列分类器模型可以被用来为一个给定的句子中的所有的词共同选择词性标签。
# 一种序列分类器策略，
# 称为连续分类或贪婪序列分类，
# 是为第一个输入找到最有可能的类标签，
# 然后使用这个问题的答案帮助找到下一个输入的最佳的标签。
# 这个过程可以不断重复直到所有的输入都被贴上标签。
import nltk
from nltk.corpus import brown
# 首先，我们必须扩展我们的特征提取函数使其具有参数history,
# 它提供一个我们到目前为止已经为句子预测的标记的链表。
# history中的每个标记对应句子中的一个词。
# 但是，请注意，history将只包含我们已经归类的词的标记，
# 也就是目标词左侧的词。
# 因此，虽然是有可能查看目标词右边的词的某些特征，
# 但查看那些词的标记是不可能的（因为我们还未产生它们）。


def pos_features(sentence,i,history):
    """
    获取目标词的词缀、前一个词和词性
    :param sentence:
    :param i:
    :param history:
    :return:
    """
    features = {
        "suffix(1)":sentence[i][-1:],
        "suffix(2)":sentence[i][-2:],
        "suffix(3)":sentence[i][-3:],
    }
    if i == 0:
        features['prev-word'] = "<START>"
        features['prev-tag'] = "START"
    else:
        features['prev-word'] = sentence[i-1]
        features['prev-tag'] = history[i-1]
    return features


# 已经定义了特征提取器，我们可以继续建立我们的序列分类器。
# 在训练中，我们使用已标注的标记为特征提取器提供适当地历史信息，
# 但标注新的句子时，我们基于标注器本身的输出产生历史信息。


class ConsecutivePosTagger(nltk.TaggerI):
    def __init__(self, train_sents):
        train_set = []
        for tagged_sent in train_sents:
            """
            获取每一句
            """
            # 去掉词性标记
            untagged_sent = nltk.tag.untag(tagged_sent)
            # 每个循环会清空
            history = []
            for i,(word,tag) in enumerate(tagged_sent):
                """
                获取每一句的词
                """
                featureset = pos_features(untagged_sent,i,history)
                train_set.append((featureset,tag))
                history.append(tag)
        self.classifier = nltk.NaiveBayesClassifier.train(train_set)

    def tag(self,sentence):
        history = []
        for i,word in enumerate(sentence):
            featureset = pos_features(sentence,i,history)
            tag = self.classifier.classify(featureset)
            history.append(tag)
        return zip(sentence,history)


tagged_sents = brown.tagged_sents(categories='news')
size = int(len(tagged_sents) * 0.1)
train_sents,test_sents = tagged_sents[size:],tagged_sents[:size],
tagger = ConsecutivePosTagger(train_sents)
print(tagger.evaluate(test_sents))
"""
这种方法的一个缺点是我们的决定一旦做出无法更改。
例如：如果我们决定将一个词标注为名词，
但后来发现的证据表明应该是一个动词，
就没有办法回去修复我们的错误。

这个问题的一个解决方案是采取转型策略。
转型联合分类的工作原理是为输入的标签创建一个初始值，
然后反复提炼那个值，尝试修复相关输入之间的不一致。

另一种方案是为词性标记所有可能的序列打分，
选择总得分最高的序列。
隐马尔可夫模型类似于连续分类器，它不光看输入也看已预测标记的历史。
然而，
不是简单的找出一个给定的词的单个最好的标签，
而是为标记产生一个概率分布，
然后将这些概率结合起来计算标记序列的概率得分，
最高概率的标记序列会被选中。

不幸的是，可能的标签序列的数量相当大。
为了避免单独考虑使用这些可能的序列，
隐马尔可夫模型要求特征提取器只看最近的标记
（或最近的n个标记，其中n是相当小的）。
由于这种限制，它可以使用动态规划，有效地找出最有可能的标记序列。
特别是，对每个连续的词索引i,每个可能的当前及以前的标记都被计算得分。
这样同样基础的方法被两个更先进的模型采用，
它们被称为最大熵马尔科夫模型和线性链条件随机场模型。
但为标记序列打分用的是不同的算法。
"""