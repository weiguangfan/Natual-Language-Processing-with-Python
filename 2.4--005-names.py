"""
名字语料库
"""
import nltk


names = nltk.corpus.names

print(names.fileids())

female_names = names.words("female.txt")
print(female_names)

male_names = names.words("male.txt")
print(male_names)

print([w for w in male_names if w in female_names])

cfd = nltk.ConditionalFreqDist(
    (fileid, name[-1],)
    for fileid in names.fileids
    for name in names.words(fileid)

)
cfd.plot()
