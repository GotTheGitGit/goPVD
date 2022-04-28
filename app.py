from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import time
import configparser
import today_competition
import afterselection
import overlap
import news_in_time
import competitions
import taiwangoorg
import user_manual

app = Flask(__name__)

# LINE 聊天機器人的基本資料
config = configparser.ConfigParser()
config.read('config.ini')

line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))


# 接收 LINE 的資訊
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    try:
        print(body, signature)
        handler.handle(body, signature)

    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def Feedback(event):

    if "最新比賽資訊!" in event.message.text:
        sendString = competitions.getcompetition()
    elif "Competition informations" in event.message.text:
        sendString = competitions.getcompetition()
    elif "個人歷史戰績查詢" in event.message.text or \
            "battle history" in event.message.text:
        sendString = '請輸入姓名'
    elif "每日五則圍棋新聞!" in event.message.text:
        sendString = news_in_time.Everyday_news()
    elif "台灣棋院最新資訊!" in event.message.text:
        sendString = taiwangoorg.Taiwangoorg()
    elif "使用說明" in event.message.text:
        sendString = user_manual.user_manual()
    else:
        sendString = "無法辨識指令"

    if type(sendString) == list:
        line_bot_api.reply_message(event.reply_token, sendString)
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=sendString)
        )


if __name__ == "__main__":
    app.run()
