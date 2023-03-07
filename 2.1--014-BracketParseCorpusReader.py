"""
本地磁盘存放一些库
"""
from nltk.corpus import BracketParseCorpusReader

corpus_root = r""
file_patterns = r""
ptb = BracketParseCorpusReader(corpus_root,file_patterns)
print(ptb.fileids())
len(ptb.sents())
ptb.sents(fileids="")





