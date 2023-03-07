from nltk.corpus import swadesh

print(swadesh.fileids())

print(swadesh.words())

print(swadesh.words("en"))

fr2en = swadesh.entries(["fr","en"])  # 同源词
print(fr2en)

translate = dict(fr2en)
print(translate)
print(translate["chien"])
print(translate["jeter"])

de2en = swadesh.entries(["de","en"])
print(de2en)
translate.update(dict(de2en))
print(translate["Hund"])
es2en = swadesh.entries(["es","en"])
print(es2en)
print(dict(es2en))
translate.update(dict(es2en))
print(translate["perro"])

languages = ["en","de","nl","es","fr","pt","la"]
for i in [139,140,141,142]:
    print(swadesh.entries(languages)[i])

