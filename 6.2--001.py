# 有监督分类的更多例子
# 句子分割
# 句子分割可以看做是一个标点符号的分类任务：
# 每当我们遇到一个可能会结束一个句子的符号，
# 如句号或问号，
# 我们必须决定它是否终止了当前句子。
# 第一步是获得一些已被分割成句子的数据，将它转换成一种适合提取特征的形式。
import nltk
sents = nltk.corpus.treebank_raw.sents()
# print(sents)
tokens = []
boundaries = set()
offset = 0
for sent in nltk.corpus.treebank_raw.sents():
    # 在这里，tokens是单独句子标识符的合并链表；
    # list().extend():在列表末尾追加另一个列表的全部元素
    tokens.extend(sent)
    offset += len(sent)
    # boundaries是一个包含所有句子边界标识符索引的集合
    # set().add():在集合中添加元素，存在则不添加；
    boundaries.add(offset-1)
# print(tokens)


# 下一步，我们需要指定用于决定标点是否表示句子边界的数据特征
def punct_features(tokens,i):
    return {
        # 下一个词的首字符大写
        'next-word-capitalized':tokens[i+1][0].isupper(),
        # 前一个词的首字母小写
        'prevword':tokens[i-1].lower(),
        # 当前词
        'punct':tokens[i],
        # 前一个词的长度是否为1
        "pre-word-is-one-char":len(tokens[i-1]) == 1
    }

# 基于这一特征提取器，
# 我们可以通过选择所有的标点符号创建一个加标签的特征集的链表，
# 然后标注它们是否是边界标识符
featuresets = [
    (punct_features(tokens,i),(i in boundaries))
    for i in range(1,len(tokens)-1)
    if tokens[i] in '.?!'
]

# 使用这些特征集，我们可以训练和评估一个标点符号分类器
size = int(len(featuresets) * 0.1)
train_set,test_set = featuresets[size:],featuresets[:size],
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier,test_set))

# 使用这种分类器进行断句，我们只需检查每个标点符号，
# 看它是否是作为一个边界标识符，在边界标识符处分割词链表。
def segment_sentences(words):
    start = 0
    sents = []
    for i,word in words:
        if word in '.?!' and classifier.classify(words,i) == True:
            sents.append(words[start:i+1])
            start = i + 1
    if start < len(words):
        sents.append(words[start:])
