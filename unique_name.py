import requests
from bs4 import BeautifulSoup as bs


class PlayerNotFound(Exception):
    pass


def unique(name):
    url = 'http://tpego.hyplaygo.com/TPEGo/Apply/HisCombatRecordList'
    session = requests.Session()
    resp = session.get(url)
    if resp.status_code != 200:
        print('url發生錯誤')
        return

    soup = bs(resp.text, 'html5lib')
    request_headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
                       (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "referer": "http://tpego.hyplaygo.com/TPEGo/Home/Index2",
    }
    request_entry = soup.find_all('form', class_='form-inline')[2].find(
        'input', {"name": "__RequestVerificationToken"})['value']
    formdata = {
        '__RequestVerificationToken': request_entry,
        'AttName': name
    }
    # queryUrl = soup.find(class_='form-inline')['action']
    #print(queryUrl, url)
    qResp = session.post(
        url, headers=request_headers, data=formdata)
    qSoup = bs(qResp.text, 'html.parser')
    battle_histories = qSoup.find_all('td', align='center')
    # print(battle_histories)
    titles = qSoup.find_all('td', width='50%')
    result = []
    reply_list = []
    # print(qSoup)
    try:
        topic = titles[0].text + '\t' + titles[1].text
    except IndexError:
        raise PlayerNotFound(f'{name} is not found')

    reply_list.append(topic)
    for battle_history in battle_histories:
        if battle_history.a:
            result.append(battle_history.a.text)
        else:
            result.append('輪空')

    for i in range(0, len(result), 2):
        if len(result[i]) == 2:
            contents = '   ' + result[i] + '\t\t  ' + result[i+1]
            reply_list.append(contents)
        elif len(result[i]) == 4:
            contents = result[i] + '      ' + result[i+1]
            reply_list.append(contents)
        else:
            contents = ' ' + result[i] + '\t\t' + result[i+1]
            reply_list.append(contents)

    return '\n'.join(reply_list)
