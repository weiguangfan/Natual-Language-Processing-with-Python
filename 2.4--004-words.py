"""
词的谜题
"""
import nltk

puzzle_letters = nltk.FreqDist("egivrvon")
print(puzzle_letters)
obligatory = "r"
wordlist = nltk.corpus.words.words()
print([w for w in wordlist if len(w) >= 6
       and obligatory in w
       and nltk.FreqDist(w) <= puzzle_letters])




