import re


# def stem(word):
#     """
#     查找词干
#     :param word:
#     :return:
#     """
#     for suffix in ["ing","ly","ed","ious","ies","ive","es","s","ment"]:
#         if word.endswith(suffix):
#             return word[:-len(suffix)]
import nltk

# print(re.findall(r'^.*(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))
# print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processing'))
# print(re.findall(r'^(.*)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes'))
# print(re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)$', 'processes'))
# print(re.findall(r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$', 'language'))


def stem(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment)?$'
    print(re.findall(regexp, word)[0])
    stem, suffix = re.findall(regexp,word)[0]
    return stem
raw = """
Job stores house the scheduled jobs. The default job store simply keeps the jobs in memory, but others store them in various kinds of databases. A job’s data is serialized when it is saved to a persistent job store, and deserialized when it’s loaded back from it. Job stores (other than the default one) don’t keep the job data in memory, but act as middlemen for saving, loading, updating and searching jobs in the backend. Job stores must never be shared between schedulers.
"""
tokens = nltk.word_tokenize(raw)
print(tokens)
print([stem(t) for t in tokens])
