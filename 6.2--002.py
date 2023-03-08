# 识别对话行为类型
# 处理对话时，将对话看作说话者执行的动作是很有用的。
# 但是问候、问题、回答、断言和说明都可以被认为是基于语言的行动类型。
# 识别对话中言语下的对话行为是理解谈话的重要的第一步。
# NPS聊天语料库，我们可以利用这些数据建立一个分类器，
# 识别新的及时消息帖子的对话类型。
# 第一步是提取基本的消息数据。
# 我们将调用xml_post()来得到一个数据结构，
# 表示每个帖子的xml注释。

import nltk
posts = nltk.corpus.nps_chat.xml_posts()[:10000]
# print(posts)

# 下一步，我们将定义一个简单的特征提取器，检查帖子包含什么词；
def dialogue_act_features(post):
    features = {}
    for word in nltk.word_tokenize(post):
        features['contains(%s) % word.lower()'] = True
    return features

# 最后，我们通过为每个帖子提取特征
# （使用post.get('class'）获得一个帖子的对话行为类型）
# 构建训练和测试数据，
# 并创建一个新的分类器。
featuresets = [
    (dialogue_act_features(post.text),post.get('class'))
    for post in posts
]

size = int(len(featuresets)*0.1)
train_set,test_set = featuresets[size:],featuresets[:size],
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))
