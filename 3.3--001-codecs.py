"""
Unicode支持超过一百万种字符；
每个字符分配一个编号，称为编码点；
在python中，编码点写作\uXXXX的形式，其中XXXX是四位十六进制形式数

当Unicode字符被存储在文件或在终端上显示，必须被编码为字节流；
一些编码（如ASCII和Lation-2）中的每个编码点使用单字节；
其他的编码（如UTF-8）使用多个字节；

文件中的文本都是有特定编码的，需要机制将文本翻译成Unicode---翻译成Unicode叫做解码；
将Unicode写入一个文件或终端，将Unicode转化为合适的编码---这种将Unicode转化为其他编码的过程叫作编码；

从Unicode的角度，字符是可以实现一个或多个字形的抽象的实体；
一个字体是一个字符到字形的映射；
"""
# 定位文件
import nltk
path = nltk.data.find("corpora/unicode_samples/polish-lat2.txt")
# print(path)

# 从文件中提取已编码文本
# python的codecs模块提供了将编码数据读入为Unicode字符串和将Unicode字符串以编码形式写出的函数；
# codecs.open()函数有一个encoding参数来指定被读取或写入的文件的编码；
import codecs
f = codecs.open(path,encoding='latin2')
# print(f)
# print(f.read())

# 在终端上查看文本，需要使用合适的编码对文本对象进行编码；
# python特定的编码unicode_escape是一个虚拟的编码
# 把所有的非ASCII字符转换成\uXXXX形式
# 编码点在ASCII码 127 < x < 256 使用连个日数字的形式\xXX表示
# for line in f:
#     line = line.strip()
#     print(line.encode("unicode_escape"))

# ord()查找一个字符的整数序列
print(ord('a'))
# 在 python中，一个Unicode字符串常量通过在字符串常量前加一个u来指定；
# 任意Unicode字符，通过在Unicode字符串常量内使用\uXXXX转义序列来定义
a = u'\u0061'
print(a)

# print语句假设Unicode字符的默认编码是ASCII码
# ń不在ASCII码范围之内，除非指定编码，否则不被输出
# repr()输出UTF-8转义序列（以\xXX的形式），而不是试图显示字形
nacute = u'\u0144'
print(nacute)

nacute_utf = nacute.encode('utf8')
# print(nacute_utf)
print(repr(nacute_utf))

