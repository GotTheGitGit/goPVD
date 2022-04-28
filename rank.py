import time
import requests
from bs4 import BeautifulSoup as bs


def Rank():
    nowTime = int(time.time())  # 取得現在時間
    struct_time = time.localtime(nowTime)  # 轉換成時間元組
    timeString = time.strftime("%Y", struct_time)  # 將時間元組轉
    url = 'http://tpego.hyplaygo.com/TPEGo/APPLY/HisWinRateRecord?pmYear=2021'
    resp = requests.get(url)
    if resp.status_code != 200:
        return ('url發生錯誤')

    soup = bs(resp.text, 'html.parser')
    # print(soup.prettify())
    titles = soup.find(
        'table', class_='table table-bordered table-striped').thead.find_all('tr')
    rows = soup.find(
        'table', class_='table table-bordered table-striped').tbody.find_all('tr')
    topic = soup.find('div', class_="col-md-8").h3.text.replace(' ', '')
    ranking = []
    names = []
    total_win = []
    total_loss = []
    winrates = []
    total_games = []
    top_column = []
    for row in rows:
        ranks = row.find_all('td')[0].text
        ranking.append(ranks)
        name = row.find_all('td')[1].text
        names.append(name)
        win = row.find_all('td')[2].text
        total_win.append(win)
        loss = row.find_all('td')[3].text
        total_loss.append(loss)
        winrate = row.find_all('td')[4].text
        winrates.append(winrate)
        game = row.find_all('td')[5].text
        total_games.append(game)

    for title in titles:
        for i in range(6):
            top = title.find_all('td')[i].text
            top_column.append(top)
    reply_list = []
    reply_list.append(topic)
    first_line = "凡" + timeString + \
        "年參與PlayGo所辦理之賽事三場以上之六段以上選手，均列入" + timeString + "年勝率排行榜。"
    reply_list.append(first_line)

    sec_line = top_column[0] + '\t  ' + top_column[1] + '\t'\
                             + top_column[2] + '\t' + top_column[3] + '\t'\
                             + top_column[4] + '\t' + top_column[5] + '\t'
    reply_list.append(sec_line)

    for g in range(99):
        detail = ' ' + ranking[g] + '\t ' + names[g] + '\t\t '\
                 + total_win[g] + '\t\t ' + total_loss[g] + '\t\t'\
                 + winrates[g] + '\t   ' + total_games[g]
        reply_list.append(detail)
    return '\n'.join(reply_list)


print(Rank())
