# 探索上下文语境
# 通过增加特征提取函数，我们可以修改这个词性标注器来利用各种词内部的其他特征，
# 例如：词长、它所包含的的音节数或者它的前缀。
# 然而，主要特征提取器仅仅看着目标词，我们就没法添加依赖词出现的上下文语境特征。
# 然而上下文语境特征往往提供关于正确标记的强大线索；
# 为了采取基于词的上下文的特征，我们必须修改以前为我们的特征提取器定义的模式。
# 不是只传递已标注的词，我们将传递整个（未标注）句子，以及目标词的索引。
# 一个词性分类器，它的特征检测器检查一个词出现的上下文以便决定应该分配的词性标记。
# 特别的，前面的词被作为一个特征。
from nltk.corpus import brown
import nltk


def pos_features(sentence,i):
    features = {
        "suffix(1)":sentence[i][-1:],
        "suffix(2)":sentence[i][-2:],
        "suffix(3)":sentence[i][-3:]

    }
    if i == 0:
        features['prev-word'] = "<START>"
    else:
        features['prev-word'] = sentence[i-1]
    return features


# print(pos_features(brown.sents()[0], 8))

tagged_sents = brown.tagged_sents(categories='news')
featuresets = []
for tagged_sent in tagged_sents:
    # print(tagged_sent)
    # 去掉标注
    untagged_sent = nltk.tag.untag(tagged_sent)
    # print(untagged_sent)
    for i,(word,tag) in enumerate(tagged_sent):
        # print(i,(word,tag))
        featuresets.append((pos_features(untagged_sent,i),tag))

size = int(len(featuresets) * 0.1)
train_set,test_set = featuresets[size:],featuresets[:size],
classifer = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifer, test_set))
# 很显然，利用上下文特征提高了我们的词性标注器的性能。
# 然而，它无法学到：一个词如果它跟在形容词后面可能是名词，
# 这样更一般的，因为它没有获得前面这个词的词性标记。







