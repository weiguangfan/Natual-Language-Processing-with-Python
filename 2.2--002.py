from nltk.corpus import udhr
import nltk
languages = ["Chickasaw","English","German_Deutsch","Creenlandic_Inuktikut","Hungarian_Magyar","Ibibio_Efik"]
cfd = nltk.ConditionalFreqDist(
    (lang,len(word),)
    for lang in languages
    for word in udhr.words(lang + "-Latin1")

)
cfd.tabulate(
    conditions = ["English","German_Deutsch"],
    samples=range(10),
    cumulative=True
)







