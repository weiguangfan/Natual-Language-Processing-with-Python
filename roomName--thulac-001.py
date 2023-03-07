import thulac
data = open("roomName2.txt",encoding="utf8").read()
thu1 = thulac.thulac()
text = thu1.cut(data,text=True)
print(text)








