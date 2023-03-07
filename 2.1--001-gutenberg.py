"""
古腾堡语料库
"""
from nltk.book import *
from nltk.misc import babelize_shell
import nltk
from nltk.corpus import gutenberg
# print(babelize_shell())
# nltk.chat.chatbots()

# print(nltk.corpus.gutenberg.fileids())
#
# emma = nltk.corpus.gutenberg.words("austen-emma.txt")
# print(len(emma))
#
# emma2 = nltk.Text(nltk.corpus.gutenberg.words("austen-emma.txt"))
# print(emma2.concordance("surprize"))

print(gutenberg.fileids())
# emma3 = gutenberg.words("austen-emma.txt")
# for fileid in gutenberg.fileids():
#     num_chars = len(gutenberg.raw(fileid))
#     num_words = len(gutenberg.words(fileid))
#     num_sents = len(gutenberg.sents(fileid))
#     num_vocab = len(set([w.lower() for w in gutenberg.words(fileid)]))
#     print(int(num_chars / num_words),int(num_words / num_sents),int(num_words / num_vocab),fileid)


macbeth_sentences = gutenberg.sents("shakespeare-macbeth.txt")
print(macbeth_sentences)
