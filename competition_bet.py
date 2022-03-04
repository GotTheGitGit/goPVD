import requests
from bs4 import BeautifulSoup as bs


def today():
    url = 'http://tpego.hyplaygo.com/TPEGo/Home/Index2'
    resp = requests.get(url)
    if resp.status_code != 200:
        print('url發生錯誤')
        return
    soup = bs(resp.text, 'html5lib')
    # test = soup.find(class_='col-md-3 portfolio-item').text
    # print(test)
    name = soup.find(class_='col-md-3 portfolio-item').h4.a.text
    href = soup.find(class_='col-md-3 portfolio-item').a['href']
    game_today = []
    game_today.append('今日比賽資訊!')
    game_today.append(name)
    game_today.append(url + href)
    return '\n'.join(game_today)


print(today())


def competition():
    url = 'http://tpego.hyplaygo.com/TPEGo/Home/Index2'
    resp = requests.get(url)
    if resp.status_code != 200:
        print('url發生錯誤')
        return
    soup = bs(resp.text, 'html5lib')
    today_yn = soup.find(class_='col-md-3 portfolio-item').text
    if '日期' in today_yn:
        titles = soup.find_all(class_='col-md-3 portfolio-item')
        independent = []
        for title in titles:
            name = title.a.text
            date = title.p.text
    else:
        today()

    for title in titles:
