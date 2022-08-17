from typing import Text
from linebot.models import TextSendMessage


def contact_me():
    myself = []
    welcome = TextSendMessage(
        text='哈囉使用者，在使用機器人時遇到什麼問題或者操作上有遇到問題的歡迎聯絡我，請透過以下聯絡方式:\nDiscord: oAzIs#4307\nEmail: oAzIs.aTh@gmail.com')
    myself.append(welcome)

    return myself


if __name__ == '__main__':
    print(contact_me())
