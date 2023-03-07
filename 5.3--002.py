# 递增地更新字典
# 我们可以使用字典计数出现的次数
# 计数词汇的方法
# 按值排序一个字典的习惯用法，按频率递减顺序显示词汇
import nltk
# 初始化一个空的defaultdict
# counts = nltk.defaultdict(int)
# 处理文本中每个词性标记，如果标记以前没有见过，就默认计数为零
# from nltk.corpus import brown
# for (word,tag) in brown.tagged_words(categories='news'):
#     # 每次我们遇到一个标记，就使用+=运算符递增它的计数
#     counts[tag] += 1
# print(counts["NN"])
# print(list(counts))
from operator import itemgetter
# sorted()的第一个参数是要排序的项目，它是由一个pos标记和一个频率组成的元组的链表。
# 第二个参数使用函数itemgetter()指定排序键。
# sorted()的最后一个参数指定项目是否应被按相反的顺序返回，即频率值递减
# itemgetter(n)返回一个函数，这个函数可以在一些其他序列对象上被调用获得这个序列的第n个元素的。

# print(sorted(counts.items(), key=itemgetter(1), reverse=True))

# print([t for t, c in sorted(counts.items(), key=itemgetter(1), reverse=True)])

# pair = ('NP',8336)
# print(pair[1])
#
# print(itemgetter(1)(pair))
# print(itemgetter(0)(pair))


# last_letters = nltk.defaultdict(list)
words = nltk.corpus.words.words('en')
# print(words)
# print(words[:10])
# print(sorted(words[:10]))
# print(''.join(sorted(words[:10])))
# for word in words:
#     key = word[-2:]
#     last_letters[key].append(word)

# print(last_letters['ly'])
# print(last_letters['zy'])

# anagrams = nltk.defaultdict(list)
# for word in words:
#     # 根据ascii码将word的字符重新排序
#     key = "".join(sorted(word))
#     anagrams[key].append(word)
# print(anagrams['aeilnrt'])

# nltk.Index()的形式提供一个创建defaultdict(list)更方便的方式
anagrams = nltk.Index((''.join(sorted(w)),w) for w in words)
print(anagrams['aeilnrt'])

# nltk.Index是一个额外支持初始化的defaultdict(list)。
# 类似的，nltk.FreqDist本质是一个额外支持初始化的defaultdict(int)(附带排序和绘图方法)
