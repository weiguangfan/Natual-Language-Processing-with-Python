# 识别文字蕴含
# Recognizing textual entailment(RTE)
# 是判断文本T的一个给定片段是否蕴含着另一个叫做“假设”的文本。
# 应当强调，文字和假设之间的关系并不一定是逻辑蕴含，
# 而是一个人是否会得出结论：文本提供了合理的证据证明假设是真实的。

# 我们可以把RTE当做一个分类任务，
# 尝试为每一对预测真/假标签。
# 虽然这项任务的成功做法似乎看上去涉及语法分析、语义和现实世界的知识的组合，
# RTE的许多早期的尝试使用粗浅的分析基于文字和假设之间的在词级别的相似度取得了相当不错的结果。
# 在理想情况下，我们希望如果有一个蕴含，那么假设所表示的所有信息也应该在文本中表示。
# 相反，如果假设中有的资料文本中没有，那么就没有蕴含。

# 在我们的RTE特征探测器中，
# 我们让词（即词类型）作为信息的代理，
# 我们的特征，
# 计数词重叠的程度和假设中而文本中没有的词的程度（由hyp_extra()方法获取）。
# 不是所有的词都是同样重要的---
# 命名实体，如人、组织和地方的名称，可能会更为重要，
# 这促使我们分别为words和nes（命名实体）提取不同的信息。
# 此外，一些高频虚词作为“停用词”被过滤掉。
import nltk


# RTEFeatureExtractor类建立了一个，
# 除去一些停用词后在文本和假设中都有的词汇包，
# 然后计算重叠和差异。
def rte_features(rtepair):
    """
    '认识文字蕴含'的特征提取器。
    :param rtepair:
    :return:
    """
    extractor = nltk.RTEFeatureExtractor(rtepair)
    features = {}
    features['word_overlap'] = len(extractor.overlap('word'))
    features['word_hyp_extra'] = len(extractor.hyp_extra('word'))
    features['ne_overlap'] = len(extractor.overlap('ne'))
    features['ne_hyp_extra'] = len(extractor.hyp_extra('ne'))
    return features

# 为了说明这些特征的内容，
# 我们检查前面显示的文本/假设对34的一些属性
rtepair = nltk.corpus.rte.pairs(['rte3_dev.xml'])[33]
print(rtepair)
extractor = nltk.RTEFeatureExtractor(rtepair)
print(extractor.text_words)
print(extractor.hyp_words)
print(extractor.overlap('word'))
print(extractor.overlap('ne'))
print(extractor.hyp_extra('word'))
# 这些特征表明假设中所有重要的词都包含在文本中，
# 因此有一些证据支持标记这个为True.

# nltk.classify.rte_classify模块使用这些方法在合并的RTE测试数据上取得准确率。

"""
扩展到大型数据集
python提供了一个良好的环境进行基本的文本处理和特征提取。
然而，它处理机器学习方法需要的密集数值计算不能够如C语言那样的低级语言那么快。
因此，如果你尝试在大型数据集使用纯python的机器学习实现
（如nltk.NavieBayesClassifier），
你可能会发现学习算法会花费大量的时间和内存。

如果你打算用大量训练数据或大量特征来训练分类器，
我们建议你探索NLTK与外部机器学习包的接口。
只有这些软件包已安装，NLTK可以透明地调用它们
（通过系统调用来训练分类模型，明显比纯python的分类实现快）
请看NLTK网站上推荐的NLTK支持的机器学习包列表。


"""