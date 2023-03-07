# 选择正确的特征
# 选择相关的特征，并决定如何为一个学习方法编码它们，
# 这对学习方法提取一个好的模型可以产生巨大的影响；
# 建立一个分类器的很多有趣的工作之一是找出哪些特征可能是相关的，
# 以及我们如何能够表示它们。
# 虽然使用相当简单而明显的特征集往往可以得到像样的性能，
# 但是使用精心构建的基于对当前任务的透彻理解的特征，通常会显著提高收益。
# 典型地，特征提取通过反复实验和错误的过程建立的，由哪些信息是与问题相关的直觉指引的。
def gender_features2(name):
    features = {}
    features['firstletter'] = name[0].lower()
    features['lastletter'] = name[-1].lower(0)
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count(%s)" % letter] = name.lower().count(letter)
        features["has(%s)" % letter] = (letter in name.lower())
    return features


gender_features2('John')




















