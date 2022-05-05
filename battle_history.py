# 名字好酷喔，只有你耶
from email.message import Message
import requests
from bs4 import BeautifulSoup as bs
from line import reply_message
from message_queue import MessageQueue, ask
from no_such_name_or_overlap import classify
from overlap_name import overlap
from afterselection import final
from unique_name import unique


def individual(event):
    event = ask(event, "請輸入姓名")
    name = event.message.text
    print(name)
    try:
        classify(name)
        unique(name)
    except AttributeError:
        reply_message(event, ''.join('查無此人'))
    except IndexError:
        feedback = overlap(name)
        event = ask(event, ", ".join(feedback))
        print(event.message.text)
        final(feedback)

        #alt_text = '名字有重複囉，請選擇下方Flex Message中自己的生日'
        # line_bot_api.reply_message(
        # event.reply_token,
        # FlexSendMessage(alt_text, overlap(name)))
# class SameName(Exception):
#     def __str__(self) -> str:
#         return super().__str__()
# print(unique('陳昕'))
# unique('周昱翔')
