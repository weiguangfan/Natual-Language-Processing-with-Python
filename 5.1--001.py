import nltk
# 将词汇按照他们的词性(part-of-speech)分类以及相应的标注它们的过程被称为词性标注(part-of-speech tagging,POS tagging)或干脆简称标注。
# 词性也称为词类或词汇范畴
# 用于特定任务的标记的集合被称为一个标记集。
# 一个词性标注器(part-of-speech tagger)处理一个词序列，为每个词附加一个词性标记
# text =nltk.word_tokenize("And now for something completely different")
# print(nltk.pos_tag(text))

# CC 并列连词
# RB 副词
# IN 介词
# NN 名词
# JJ 形容词

# print(nltk.help.upenn_tagset('RB'))


# 一个标注器能够正确识别一个句子的上下文中的这些词的标记。
# 一个标注器也可以为我们对未知词的认识过程建模；
# 同形同音异义词
# refuse和permit都以一般现在时动词（VBP）和名词（NN）形式出现；
# text = nltk.word_tokenize("They refuse to permit us to obtain the refuse permit")
# print(nltk.pos_tag(text))

text = nltk.Text(word.lower() for word in nltk.corpus.brown.words())
print(text)
# text.similar()方法为一个词找出所有上下文，
# 然后找出所有出现相同上下文中的词。
print(text.similar('woman'))
print(text.similar('bought'))
print(text.similar('over'))
print(text.similar('the'))




