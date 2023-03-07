# 表示已标注的标识符
# 按照NLTK的约定，一个已标注的标识符使用一个由标识符和标记组成的元组来表示；
# 函数str2tuple()从表示一个已标注的标识符的标注字符串创建一个这样的特殊元组：
import nltk
# tagged_token = nltk.tag.str2tuple('fly/NN')
# print(tagged_token)
# print(tagged_token[0])
# print(tagged_token[1])

# 我们可以直接从一个字符串构造一个已标注的标识符的链表。
# 第一步是对字符串分词以便能访问单独的词/标记字符串，
# 然后将每一个转换成一个元组
sent = '''
The/AT grand/JJ jury/NN commented/VBD on/IN a/AT number/NN of/IN
other/AP topics/NNS ,/, AMONG/IN them/PPO the/AT Atlanta/NP and/CC
././.
'''
print([nltk.tag.str2tuple(t) for t in sent.split()])









