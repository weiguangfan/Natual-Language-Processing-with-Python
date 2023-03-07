"""
函数nltk.regexp_tokenize()与re.findall()类似，我们一直在使用它进行分词；
nltk.regexp_tokenize()分词效率更高，且不需要特殊处理括号;
nltk.regexp_tokenize()函数有一个可选的gaps参数，设置为True时，正则表达式指定标识符间的距离
"""
import nltk

text = 'That U.S.A poster-print costs $12.40...'
# (?x) 告诉python去掉嵌入的空白字符和注释
pattern = r'''(?x)([A-Z]\.)+|\w+(-\w+)*|\$?\d+(\.\d+)?%?|\.\.\.|[][.,;'"?():-_`]'''
print(nltk.regexp_tokenize(text, pattern))







