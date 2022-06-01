from flask import Flask, request, abort

from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from battle_history import individual
from line import handler, reply_message
from message_queue import MessageQueue
import news_in_time
import competitions
import taiwangoorg
import user_manual

# https://go185.herokuapp.com/callback
app = Flask(__name__)


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

    if MessageQueue.handle(event):
        print('handled, quit')
        return

    if "最新比賽資訊!" in event.message.text:
        response = competitions.getcompetition()
    elif "Competition informations" in event.message.text:
        response = competitions.getcompetition()
    elif "個人戰績查詢" in event.message.text or \
            "battle history" in event.message.text:
        individual(event)
        return
    elif "每日五則圍棋新聞!" in event.message.text:
        response = news_in_time.Everyday_news()
    elif "台灣棋院最新資訊!" in event.message.text:
        response = taiwangoorg.Taiwangoorg()
    elif "圍棋資訊PVD使用說明!" in event.message.text:
        response = user_manual.user_manual()
    else:
        response = "無法辨識指令"

    reply_message(event, response)


if __name__ == "__main__":
    app.run()
