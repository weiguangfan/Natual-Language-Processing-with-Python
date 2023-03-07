# <> 用于标记标识符的边界，尖括号之间的所有空白都内忽略；这只对nltk的findall*(方法处理文本有效；
# <.*> 匹配所有单个标识符，将它括在()里,表示只匹配词
import nltk
from nltk.corpus import gutenberg,nps_chat
# moby = nltk.Text(gutenberg.words("melville-moby_dick.txt"))
# print(moby.findall(r'<a>(<.*>)<man>'))

# 找出以词bro结尾的三个词组成的短语；
# chat = nltk.Text(nps_chat.words())
# print(chat.findall(r"<.*><.*><bro>"))

# 找出以字母l开始的三个或更多词组成的序列
# print(chat.findall(r"<l.*>{3,}"))

# nltk.re_show(p,s),它能标注字符串s中所有匹配模式p的地方
# nltk.app.nemo(),它能提供一个探索正则表达式的图形界面

# 搜索x and other ys形式的表达式
# python提供的字符类'\w'匹配词中的字符，相当于[a-zA-Z0-9_]
# 这个类的补'\W'即所有字母、数字和下划线意外的字符
from nltk.corpus import brown
hobbies_learned = nltk.Text(brown.words(categories=['hobbies','learned']))
print(hobbies_learned.findall(r"<\w*><and><other><\w*s>"))






