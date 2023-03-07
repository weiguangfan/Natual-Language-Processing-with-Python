"""
字符串基本操作
"""
# 使用转义字符
monty = 'Monty Python'
print(monty)
circus = "Monty Python's Flying Circus"
print(circus)
circus = 'Monty Python\'s Flying Circus'
print(circus)

# 一个包含两个字符串的序列被链接为一个字符串，需要使用反斜杠或者括号，解释器就会知道第一行的表达式不完整
couplet = "Shall I compare thee to a Summer's day?"\
    "Thou are more lovely and more temperate:"
print(couplet)
couplet = ("Rough winds do shake the darling buds of May,"
           "And Summers's lease hath all roo short a date:"
           )
print(couplet)

# 三重引号，达到换行
couplet = """
Shall I compare thee to a Summer's day?
Thou are more lovely and more temperate:
"""
print(couplet)
couplet = '''
Rough winds do shake the darling buds of May,
And Summer's lease hath all short a date:
'''
print(couplet)


