"""
词汇随时间推移的使用情况
"""

from nltk.corpus import inaugural
import nltk

cfd = nltk.ConditionalFreqDist(
    (target,file[:4])
    for file in inaugural.fileids()
    for w in inaugural.words()
    for target in ["america","citizen"]
    if w.lower().startswith(target)
)

cfd.plot()




