import configparser

from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))

handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


def reply_message(event, message):
    if type(message) == list:
        response = message
    elif type(message) == str:
        response = TextSendMessage(text=message)
    else:
        raise Exception("unknown type message:", message)
    line_bot_api.reply_message(
        event.reply_token, response)
