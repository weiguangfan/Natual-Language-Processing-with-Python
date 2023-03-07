"""
string的一些函数
"""

from nltk.book import *

print(sent7)
print("$"*50)
print([w for w in sent7 if len(w) < 4])
print("$"*50)
print([w for w in sent7 if len(w) <= 4])
print("$"*50)
print([w for w in sent7 if len(w) == 4])
print("$"*50)
print([w for w in sent7 if len(w) != 4])
print("$"*50)
print([w for w in sent7 if len(w) > 4])

print(sorted([w for w in set(text1) if w.endswith("ableness")]))
print(sorted([term for term in set(text4) if "gnt" in term]))
print(sorted([item for item in set(text6) if item.istitle()]))
print(sorted([item for item in set(sent7) if item.isdigit()]))