"""
带条件的频率分布函数
"""

import nltk
from nltk.corpus import brown
cfd = nltk.ConditionalFreqDist(
    (genre,word)
    for genre in brown.categories()
    for word in brown.words(categories=genre)
)
genre = ["news","religion","hobbies","science_fiction","romance","humor"]
modals = ["can","could","may","might","must","will"]
print(cfd.tabulate(conditions=genre, samples=modals))










