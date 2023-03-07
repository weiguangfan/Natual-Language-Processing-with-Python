"""
音素包含数字表示主重音(1)，次重音(2)和无重音(0)
"""
import nltk
entries = nltk.corpus.cmudict.entries()
# print(entries)

# 定义一个函数来提取重音数字
def stress(pron):
    return [char for phone in pron
            for char in phone if char.isdigit()]

# 扫描词典，找到具有特定重音模式的词汇
# print([w for w, pron in entries if stress(pron) == ["0", "1", "0", "2", "0"]])
print([w for w, pron in entries if stress(pron) == ["0", "2", "0", "1", "0"]])

# 找到词汇的最小受限集合
# p3 = [(pron[0] + "-" + pron[2],word)
#       for (word,pron) in entries
#       if pron[0] == "P" and len(pron) == 3
#       ]
# print(p3)
# cfd = nltk.ConditionalFreqDist(p3)
# print(cfd)
# print(cfd.conditions())
# print(cfd["P-P"])
# print(cfd["P-P"].keys())
# for template in cfd.conditions():
#     if len(cfd[template]) > 10:
#         words = cfd[template].keys()
#         wordlist = " ".join(words)
#         print(template,wordlist[:70] + "...")
