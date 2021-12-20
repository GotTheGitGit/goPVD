from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
import time
import configparser
import rank
import news_in_time
import competition
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

    if "比賽" in event.message.text:
        sendString = competition.getcompetition()
    elif "Competition informations" in event.message.text:
        sendString = competition.getcompetition()
    elif "勝率" in event.message.text or \
            "winrate" in event.message.text:
        sendString = rank.Rank()
    elif "每日五則圍棋新聞" in event.message.text:
        sendString = news_in_time.Everyday_news()
    elif "台灣棋院最新資訊" in event.message.text:
        sendString = taiwangoorg.Taiwangoorg()
    elif "使用說明" in event.message.text:
        sendString = user_manual.user_manual()
    else:
        sendString = "無法辨識指令"

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=sendString)
    )


if __name__ == "__main__":
    app.run()
