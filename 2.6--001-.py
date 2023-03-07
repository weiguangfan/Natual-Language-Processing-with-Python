from urllib.request import urlopen
# help(urllib)
proxies = {"http":"http://103.138.74.167:7890"}
# url = "http://www.gutenberg.org/files/2554/2554.txt"
url = "http://www.baidu.com"
raw = urlopen(url).read()
# raw = urlopen(url,proxies=proxies).read()
print(type(raw))
# print(len(raw))
# print(raw[:75])


