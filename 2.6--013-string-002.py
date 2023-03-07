sent = "colorless green ideas sleep furiously"

for char in sent:
    print(char,)

# in 测试一个字符串是否包含一个特定的子字符串
phrase = "And now for something completely different"
if "thing" in phrase:
    print('found "thing"')

# find()找到一个子字符串在字符串内的位置
print(phrase.find("for"))