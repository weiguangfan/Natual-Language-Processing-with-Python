"""
及时消息聊天会话语料库
"""
from nltk.corpus import nps_chat

chatroom = nps_chat.posts("10-19-20s_706posts.xml")
print(chatroom[123])



