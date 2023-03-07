import nltk
raw = open("./test.txt").read()
print(type(raw))
tokens = nltk.word_tokenize(raw)
print(type(tokens))
print(tokens)
words = [w.lower() for w in tokens]
print(type(words))
print(words)
print(set(words))
vocab = sorted(set(words))
print(type(vocab))
print(vocab)
vocab.append("blog")
print(vocab)


