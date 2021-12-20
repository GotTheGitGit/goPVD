from linebot.models import TextSendMessage


def user_manual():
    manual = []
    welcome = TextSendMessage(text="歡迎使用圍棋資訊PVD~\n以下為各個功能之使用說明")
    manual.append(welcome)
    competition = TextSendMessage(text="最新比賽資訊：\n\
        隨時隨地掌握第一手比賽資訊，讓你快速瀏覽各個比賽，並附上報名比賽之連結！\
        點選下方圖文選單左上方後系統將會自動帶給你完整的將至比賽資訊！")

    manual.append(competition)
    rank = TextSendMessage(text="勝率前百排行榜:\n\
        點選下方圖文選單中央的「排行榜」後圍棋資訊PVD就會提供最新的勝率排行榜！\
        (勝率排行榜僅包含透過Playgo平台所辦理的比賽成績，更新時間亦以Playgo平台為準)")

    manual.append(rank)
    news_in_time = TextSendMessage(text="每日五則圍棋新聞：\n\
        每天忙於工作的你是否無暇好好的掌握圍棋屆最新資訊？在此圍棋資訊PVD提供隨機五\
        則的圍棋新聞，你可以在任何地點、任何時間開啟圍棋資訊PVD接收第一時間的訊息！\
        點選圖文選單右上方的格子後將會得到每日隨機的五則新聞！")

    manual.append(news_in_time)
    taiwangoorg = TextSendMessage(text="台灣棋院最新資訊：\n\
        身為一位台灣的棋手，時刻掌握台灣棋院的最新資訊是一定要的\
        。透過圍棋資訊PVD最快速地接收台灣圍棋重要資訊！\
        點選圖文選單第一行中央的區域後系統將即速傳達給你台灣棋院最新資訊！")
    manual.append(taiwangoorg)
    return manual
