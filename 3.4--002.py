"""
对python解释器，一个正则表达式与任何其他字符串没有两样；
字符串中包含反斜杠后面跟一些特殊字符，python解释器将会特殊处理他们；
\b 会被解释为一个退格符合
给字符串加一个前缀'r'来表明他是一个原始字符串；会被re库解释为匹配词的边界；

"""
import re
import nltk
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
# [a,b,c, ...]，匹配任一一个字符；方括号内的字符的顺序是没有关系的
# print([w for w in wordlist if re.search('^[ghi][mno][jlk][def]$', w)])

# '+',适用于单个字母或括号内的字母集,前面的项目的一个或多个实例
chat_words = sorted(set(w for w in nltk.corpus.nps_chat.words()))
# print([w for w in chat_words if re.search('^m+i+n+e+$', w)])

# print([w for w in chat_words if re.search('^[ha]+$', w)])

# '*',前面的项目的零个或多个实例
# print([w for w in chat_words if re.search('^m*i*n*e*$', w)])

# '^' 出现在[]内第一个字符位置是有另外的功能
# <<[^aeiouAEIOU]>>匹配除元音字母之外的所有字母
# print([w for w in chat_words if re.search('^[^aeiouAEIOU]+$', w)])

# 寻找匹配特定模式的词汇标识符
# '.' 通配符，匹配使用字符
# '\' 转义字符;表示其后面的字符不再有特殊的含义而是按照字面的表示匹配特定的字符
# '{}' 表示前面的项目重复指定的次数；括号内：单个数字代表个数；多个数字代表两者之间；逗号+数字代表截止到数字；数字+逗号代表大于这个数字；
# '()' 表示一个操作符的范围，可以与'|'一起使用
# '|' 代表或者；表示从左边的内容和右边的内容中选择一个；
wsj = sorted(set(nltk.corpus.treebank.words()))
# print([w for w in wsj if re.search('^[0-9]+\.[0-9]+$', w)])
# print([w for w in wsj if re.search('^[A-Z]+\$$', w)])
# print([w for w in wsj if re.search('^[0-9]{4}$', w)])
# print([w for w in wsj if re.search('^[0-9]+-[a-z]{3,5}$', w)])
# print([w for w in wsj if re.search('^[a-z]{5,}-[a-z]{2,3}-[a-z]{,6}$', w)])
# print([w for w in wsj if re.search('(ed|ing)$', w)])
# print([w for w in wsj if re.search('ed|ing$', w)])
# print([w for w in wsj if re.search('(ion)$', w)])


