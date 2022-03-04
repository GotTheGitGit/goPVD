# 名字好酷喔，只有你耶
import requests
from bs4 import BeautifulSoup as bs


def unique(name):
    url = 'http://tpego.hyplaygo.com/TPEGo/Apply/HisCombatRecordList'
    resp = requests.get(url)
    if resp.status_code != 200:
        print('url發生錯誤')
        return

    soup = bs(resp.text, 'html5lib')
    request_headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                       (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "referer": "http://tpego.hyplaygo.com/TPEGo/Home/Index2",
        "Cookie": request_entry
    }
    request_entry = soup.find_all('form', class_='form-inline')[2].find(
        'input', {"name": "__RequestVerificationToken"})['value']
    formdata = {
        '__RequestVerificationToken': request_entry,
        'AttName': name
    }
    queryUrl = soup.find(class_='form-inline')['action']
    print(queryUrl, url)
    qResp = requests.post(
        url, headers=request_headers, data=formdata)
    qSoup = bs(qResp.text, 'html.parser')
    battle_history = qSoup.find_all('tr', 'table table-bordered table-striped')

    print(qSoup)
    print(battle_history)
    print('\n')
    for bh in battle_history:
        td = bh.find_all('td')
        print('對戰%s: %s' % td[0].a.get_text, td[1].a.get_text)


unique('周昱翔')
