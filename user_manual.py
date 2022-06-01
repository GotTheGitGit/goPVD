from linebot.models import TextSendMessage


def user_manual():
    manual = []
    welcome = TextSendMessage(text="歡迎使用圍棋資訊PVD~\n以下為各個功能之使用說明")
    manual.append(welcome)
    competition = TextSendMessage(
        text="最新比賽資訊：\n隨時隨地掌握第一手比賽資訊，讓你快速瀏覽各個比賽，並附上報名比賽之連結！點選下方圖文選單左上方後系統將會自動帶給你完整的將至比賽資訊！")
    manual.append(competition)
    contact = TextSendMessage(
        text="個人戰績查詢:\n想查看自己比賽的輝煌戰果?點選圖文選單左下方圖塊後輸入欲查詢之姓名，若名字有重複請輸入對應的出生年月即可。本功能僅支援使用playgo報名比賽後的戰績紀錄!若有重名情況系統將回傳有重名的各人出生年月\n範例:\n林耕平 2000/10\n1983/2接著打入欲查詢者的出生年月即可!)")
    manual.append(contact)
    news_in_time = TextSendMessage(
        text="每日五則圍棋新聞：\n每天忙於工作的你是否無暇好好的掌握圍棋屆最新資訊？在此圍棋資訊PVD提供隨機五則的圍棋新聞，你可以在任何地點、任何時間開啟圍棋資訊PVD接收第一時間的訊息！點選圖文選單右上方的格子後將會得到每日隨機的五則新聞！")
    manual.append(news_in_time)
    taiwangoorg = TextSendMessage(
        text="台灣棋院最新資訊：\n身為一位台灣棋手，時刻掌握台灣棋院的最新資訊是一定要的。透過圍棋資訊PVD最快速地接收台灣圍棋重要資訊！點選圖文選單第一行中央的區域後系統將即速傳達給你台灣棋院最新資訊！")
    manual.append(taiwangoorg)

    return manual
