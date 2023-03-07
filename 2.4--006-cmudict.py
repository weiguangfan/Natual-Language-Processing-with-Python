"""
cmu发音词典，对每一个词，提供语音的代码
"""
import nltk

entries = nltk.corpus.cmudict.entries()
# print(entries)
print(len(entries))

# for entry in entries[39943:39951]:
#     print(entry)

# for word,pron in entries:  # 包含三个因素的词
#     if len(pron) == 3:
#         ph1,ph2,ph3 = pron
#         if ph1 == "P" and ph3 == "T":
#             print(word,ph2)

# syllable = ["N","IH0","K","S"]  # 发音结尾与nicks相似的词汇
# print([word for word, pron in entries if pron[-4:] == syllable])

# 发音和书写不匹配
# print([w for w, pron in entries if pron[-1] == "M" and w[-1] == "n"])

# print(sorted(set(w[:2] for w, pron in entries if pron[0] == "N" and w[0] != "n")))
