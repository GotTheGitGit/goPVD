from typing import Text
from linebot.models import TextSendMessage


def contact():
    myself = []
    welcome = TextSendMessage(
        text='嗨!這個功能可以讓您直接跟開發人員做對於此機器人的建議與回饋，請幫我完成下方的步驟!')
