"""
在正则表达式前加字母'r'，
它告诉python解释器按照字面表示对待字符串，
而不去处理正则表达式中包含的反斜杠字符；
re库内置的缩写'\s',表示匹配所有空白字符。
\S 是 \s的补;
python提供的字符类'\w'匹配词中的字符，相当于[a-zA-Z0-9_];
这个类的补'\W',即所有字母、数字和下划线以外的字符;
'\n'换行符
'\t'制表符
'\b'词边界（零宽度）
'\d' 任一十进制数字（相当于[0-9]）
'\D' 任何非数字字符（等价于[^0-9]）
"""
import re
raw = """
Job stores house the scheduled jobs. The default job store simply keeps the jobs in memory, but others store them in various kinds of databases. A job’s data is serialized when it is saved to a persistent job store, and deserialized when it’s loaded back from it. Job stores (other than the default one) don’t keep the job data in memory, but act as middlemen for saving, loading, updating and searching jobs in the backend. Job stores must never be shared between schedulers.
"""
# raw.split()在空格符处分割原始文本
# 使用正则表达式，匹配字符串中的所有空格是不够的，分词结果包含'\n'换行符
# print(re.split(r' ', raw))

# 我们需要匹配任何数量的空格符、制表符或换行符
# <<[ \t\n]+>>匹配一个或多个空格、制表符(\t)或换行符(\n)
# print(re.split(r'[ \t\n]+', raw))

# re库内置的缩写'\s',表示匹配所有空白字符。
# print(re.split(r'\s+', raw))

# 用'\W'来分割所有单次字符意外的输入
# 在开始和结尾都给了我们一个空字符串
# print(re.split(r'\W+', raw))


# 通过re.findall(r'\w+',raw)使用模式匹配词汇而不是空白符号
# print(re.findall(r'\w+', raw))

# 正则表达式<<\w+|\S\w*>>将首先尝试匹配词中字符的所有序列，
# 如果没有找到匹配的，它会尝试匹配后面跟着词中字符的任何非空白字符（\S 是\s的补）
# 这意味着标点会与跟在后面的字母（如's）在一起，但两个或两个以上的标点字符序列会被分割
# re库内置的缩写'\s',表示匹配所有空白字符。
# \S 是\s的补
# print(re.findall(r'\w+|\S\w*', raw))

# <<\w+([-']\w)*>> 允许连字符和撇号
# <<[-.(]+>> 会使双连字符、省略号、右括号被单独分词
print(re.findall(r"\w+(?:[-']\w+)*|'|[-.(]+|\S\w*", raw))










