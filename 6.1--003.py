# 文档分类
# 首先，我们构造一个标记了相应类别的文档清单。
# 对于这个例子，我们选择电影评论语料库，将每个评论归类为正面或负面。
import random

import nltk
from nltk.corpus import movie_reviews
# documents = [(list(movie_reviews.words(fileid)),category)
#              for category in movie_reviews.categories()
#              for fileid in movie_reviews.fileids(category)]
# random.shuffle(documents)
# print(documents)


# 接下来，我们为文档定义一个特征提取器，这样分类器就会知道哪些方面的数据应注意。
# 对于文档主题识别，我们可以为每个词定义一个特性表示该文档是否包含这个词。
# 为了限制分类器需要处理的特征的数目，我们一开始构建一个整个语料库中前2000个最频繁词的链表。
# 然后，定义一个特征提取器，简单地检查这些词是否在一个给定的文档中。
# all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
# word_features = list(all_words.keys())[:2000]


# def document_features(document):
#     """
#     一个文档分类的特征提取器，其特征表示每个词是否在一个给定的文档中
#     :param document:
#     :return:
#     """
#     document_words = set(document)
#     features = {}
#     for word in word_features:
#         features['contains(%s)' % word] = (word in document_words)
#     return features


# print(document_features(movie_reviews.words('pos/cv957_8737.txt')))

# 现在，我们已经定义了我们的特征提取器，可以用它来训练一个分类器，为新的电影评论加标签。
# 为了检查产生的分类器可靠性如何，我们在测试集上计算其正确性，
# 再一次的，我们使用show_most_informative_features()来找出哪些特征是分类器发现最有信息量的。
# 训练和测试一个分类器进行文档分类
# featuresets = [(document_features(d),c) for (d,c) in documents]
# train_set,test_set = featuresets[100:],featuresets[:100],
# classifier = nltk.NaiveBayesClassifier.train(train_set)
# print(nltk.classify.accuracy(classifier, test_set))
# print(classifier.show_most_informative_features(5))

# 词性标注
# 训练一个分类器来算出哪个后缀最有信息量。
# 首先，让我们找出最常见的后缀
from nltk.corpus import brown
suffix_fdist = nltk.FreqDist()
for word in brown.words():
    suffix_fdist[word[-1:]] += 1
    suffix_fdist[word[-2:]] += 1
    suffix_fdist[word[-3:]] += 1
common_suffixes = list(suffix_fdist.keys())[:100]
# print(common_suffixes)


# 接下来，我们将定义一个特征提取器函数，检查给定的单词的这些后缀
def pos_features(word):
    features = {}
    for suffix in common_suffixes:
        features['endswith(%s)' % suffix] = word.lower().endswith(suffix)
    return features

# 特征提取函数的行为就像有色眼镜一样，强调我们的数据中的某些属性，
# 并无法看到其他属性。
# 分类器在决定如何标记输入时，将完全依赖它们强调的属性。
# 在这种情况下，分类器将只基于一个给定的词拥有哪个常见后缀的信息来做决定。

# 现在，我们已经定义了我们的特征提取器，可以用它来训练一个新的“决策树”的分类器
tagged_words = brown.tagged_words(categories='news')
featuresets = [(pos_features(n),g) for (n,g) in tagged_words]
size = int(len(featuresets) * 0.1)
train_set,test_set = featuresets[size:],featuresets[:size],
classifier = nltk.DecisionTreeClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))

print(classifier.classify(pos_features('cats')))

# 决策树模型的一个很好的性质是它们往往很容易解释的。
# 实际的分类器包含这里显示的if-then语句下面进一步的嵌套，参数depth=4只显示决策树的顶端部分。

print(classifier.pseudocode(depth=4))



