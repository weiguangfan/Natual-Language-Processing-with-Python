import nltk

# pos = {}
# print(pos)
# pos['colorless'] = 'ADJ'
# print(pos)
# pos['idea'] = 'N'
# pos['sleep'] = 'V'
# pos['furiously'] = 'ADV'
# print(pos)
# print(pos['idea'])
# print(pos['colorless'])
# 要找到键，可以将字典转换成一个链表或在需要使用链表的地方使用字典
# print(list(pos))
# print(sorted(pos))
# print([w for w in pos if w.endswith('s')])

# for循环输出字典的内容
# for word in sorted(pos):
#     print(word + ":",pos[word])

# 字典的方法keys() values() items()允许我们访问作为单独的链表的键、值以及键值对
# print(pos.keys())
# print(pos.values())
# print(pos.items())
# 按它们的第一个元素排序元组（如果第一个元素相同，就使用它们的第二个元素）
# print(sorted(pos.items()))
# for key,val in sorted(pos.items()):
#     print(key + ":",val)

# 我们要确保当我们在字典中查找某词时，一个键只得到一个值
# pos['sleep'] = 'V'
# print(pos['sleep'])

# pos['sleep'] = 'N'
# print(pos['sleep'])

# 有一个方法可以在该项目中存储多个值
# pos['sleep'] = ['N','V']

# 字典的键必须是不可改变的类型，如字符串和元组

# 如果我们试图访问一个不在字典中的键，会得到一个错误；
# 如果一个字典能为这个新键自动创建一个条目并给它一个默认值，如0或者一个空链表，将是有用的；
# python:defaultdict
# nltk:nltk.defaultdict
# 为了使用它，我们必须提供一个参数，用来创建默认值，如：int float str list dict tuple
# frequency = nltk.defaultdict(int)
# frequency['colorless'] = 4
# print(frequency)
# print(frequency['ideas'])
# pos = nltk.defaultdict(list)
# pos['sleep'] = ['N',"V"]
# print(pos)
# print(pos['ideas'])

# 这些默认值实际上是将其他对象转换为指定类型的函数（例如：int("2") list("2")
# 当它们被调用的时候没有参数--也就是说，int() list()分别返回0 和 []

# 也可以指定任何我们喜欢的默认值，只要提供可以无参数的被调用产生所需值的函数的名字。
# 创建一个任一条目的默认值是'N'的字典
# 当我们访问一个不存在的条目时，它会自动添加到字典；
# pos = nltk.defaultdict(lambda :'N')
# pos['colorless'] = 'ADJ'
# print(pos['blog'])
# print(pos.items())

# 这个lambda表达式没有指定参数，所以我们用不带参数的括号调用它。
# 下面的f和g的定义是等价的
# f = lambda :'N'
# print(f())


# def g():
#     return 'N'
#
#
# print(g())


# 许多语言处理任务--包括标注--费了很大力气来正确处理文本中只出现过一次的词。
# 如果有一个固定的词汇和没有新词会出现的保证，它们会有更好的表现。
# 我们可以预处理一个文本，在一个默认字典的帮助下，
# 替换低频词汇为一个特殊的‘超出词汇表’标识符，
# UNK(out of vocabulary)
# 我们需要创建一个默认字典，映射每个词为它们的替换词。
# 最频繁的n个词将被映射到它们自己。其他的被映射到UNK;
alice = nltk.corpus.gutenberg.words('carroll-alice.txt')
# print(alice)
# print(len(alice))
# print(len(set(alice)))
vocab = nltk.FreqDist(alice)
# print(vocab)
v1000 = list(vocab)[:1000]
print(v1000)
mapping = nltk.defaultdict(lambda :'UNK')
# print(mapping)
for v in v1000:
    mapping[v] = v

print(mapping.keys())
alice2 = [mapping[v] for v in alice]
print(alice2[:100])

# print(len(set(alice2)))
