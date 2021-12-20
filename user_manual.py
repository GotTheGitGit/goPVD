from linebot.models import TextSendMessage


def user_manual():
    manual = []
    welcome = TextSendMessage(text="歡迎使用圍棋資訊PVD~\n以下為各個功能之使用說明")
    manual.append(welcome)
    competition = TextSendMessage(text="歡迎使用圍棋資訊PVD~\n以下為各個功能之使用說明")
    manual.append(competition)
    rank = TextSendMessage(text="歡迎使用圍棋資訊PVD~\n以下為各個功能之使用說明")
    manual.append(rank)
    news_in_time = TextSendMessage(text="歡迎使用圍棋資訊PVD~\n以下為各個功能之使用說明")
    manual.append(news_in_time)
    taiwangoorg = TextSendMessage(text="歡迎使用圍棋資訊PVD~\n以下為各個功能之使用說明")
    manual.append(taiwangoorg)
    return manual
