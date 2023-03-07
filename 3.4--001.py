"""
在python中使用正则表达式，需要使用import re导入re函数库
"""
import re
import nltk
wordlist = [w for w in nltk.corpus.words.words('en') if w.islower()]
# print(wordlist)

# 正则表达式<<ed$>>，查找以ed结尾的词汇
# 函数re.search(p,s)检查字符串s中是否有模式p
# print([w for w in wordlist if re.search('ed$', w)])

# 通配符"."匹配任何单个字符。
# 插入符号"^"匹配字符串的开始
# "$"匹配字符串的结尾
# print([w for w in wordlist if re.search('^..j..t..$', w)])

# "?"表示前面的字符是可选的
print(sum(1 for w in wordlist if re.search('^e- mail$', w)))






