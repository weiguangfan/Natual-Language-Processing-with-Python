"""
nltk中包括现成的词干提取器：Porter,Lancaster
"""
import re
import nltk
raw = """
DENNIS:Listen,strange women lying in ponds distributing swords ia no basis for a system of government.
Supreme executive power derives from a mandate from the masses, not from some farcical aquatic ceremony.
"""

tokens = nltk.word_tokenize(raw)
print(tokens)

# porter = nltk.PorterStemmer()
# print(porter)
# lancaster = nltk.LancasterStemmer()
# print(lancaster)

# print([porter.stem(t) for t in tokens])
# print([lancaster.stem(t) for t in tokens])


# 使用词干提取器索引文本
class IndexedText(object):
    def __init__(self,stemmer,text):
        self._text = text
        self._stemmer = stemmer
        self._index = nltk.Index((self._stem(word),i)
                                 for (i,word) in enumerate(text))

    def concordance(self,word,width=40):
        key = self._stem(word)
        wc = width/4
        for i in self._index[key]:
            lcontext = ''.join(self._text[i-wc:i])
            rcontext = ''.join(self._text[i:i+wc])
            ldisplay = '%*s' % (width,lcontext[-width:])
            rdisplay = '%-*s' % (width,rcontext[:width],)
            print(ldisplay,rdisplay)

    def _stem(self,word):
        return self._stemmer.stem(word).lower()


# porter = nltk.PorterStemmer()
# print(porter)
# grail = nltk.corpus.webtext.words('grail.txt')
# print(grail)
# text = IndexedText(porter,grail)
# print(text.concordance('lie'))

# wordNet词形归并器删除词缀产生的词，都是在它的字典中的词。
wnl = nltk.WordNetLemmatizer()
print(wnl)
print([wnl.lemmatize(t) for t in tokens])

