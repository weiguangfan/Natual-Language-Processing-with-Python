# re.findall() 找出所有（无重叠的）匹配指定正则表达式的；
# 利用正则表达式提取字符块
import re
import nltk
word = 'supercalifragilisticwxpialidocious'
# print(re.findall(r'[aeiou]', word))
# print(len(re.findall(r'[aeiou]', word)))

# wsj = sorted(set(nltk.corpus.treebank.words()))
# print(wsj)

# fd = nltk.FreqDist(vs for word in wsj
#                    for vs in re.findall(r'[aeiou]{2，}',word))
# print(fd.items())

regexp = r'^[AEIOUaeiou]+|[AEIOUaeiou]+$|[^AEIOUaeiou]'


def compress(word):
    """
    使用re.findall()提取使用匹配的词中的字符，
    然后使用''.join()将他们连接在一起
    :param word:
    :return:
    """
    pieces = re.findall(regexp,word)
    # print(pieces)
    return ''.join(pieces)


# english_udhr = nltk.corpus.udhr.words('English-Latin1')
# print(english_udhr)
# # print(compress(english_udhr[0]))
# data = [compress(w) for w in english_udhr[:75]]
# print(data)
# print(nltk.tokenwrap(data))

# 正则表达式与条件频率结合
rotokas_words = nltk.corpus.toolbox.words('rotokas.dic')
print(rotokas_words)
# cvs = [cv for w in rotokas_words for cv in re.findall(r'[ptksvr][aeiou]',w)]
# print(cvs)
# cfd = nltk.ConditionalFreqDist(cvs)
# print(cfd.conditions())
# cfd.tabulate()

cv_word_pairs = [
    (cv,w) for w in rotokas_words
    for cv in re.findall(r'[ptksvr][aeiou]',w)
]
print(cv_word_pairs)
# nltk.Index()转换成有用的索引
# 类似key:[v1,v2,...]
cv_index = nltk.Index(cv_word_pairs)
print(cv_index)
print(cv_index['su'])
print(cv_index['po'])

