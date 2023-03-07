import jieba
data = open("roomName.txt",encoding="utf8").read()
# seg_list = jieba.cut(data,cut_all=True)
# seg_list = jieba.cut_for_search(data)
# print(seg_list)
# print("Full Mode: " + "/ ".join(seg_list))
# print(", ".join(seg_list))

import jieba.analyse
# for x, w in jieba.analyse.extract_tags(data, withWeight=True):
#     print('%s %s' % (x, w))


