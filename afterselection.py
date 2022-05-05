# 拿到欲查詢之重名者生日後
import requests
from bs4 import BeautifulSoup as bs


def final(name_and_birthday):
    name = name_and_birthday.partition('\n')[0]
    birthday = name_and_birthday.partition('\n')[2]
    # print(type(birthday)
    main_page = 'http://tpego.hyplaygo.com'
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
    # print(qSoup)
    reply_lists = qSoup.find_all(
        "div", class_="col-md-10")[1]
    href = main_page + reply_lists.find('a', string=birthday)['href']
    temp = []
    cutter = []
    transition = []
    temp = href.split('=')
    cutter = temp[1].split('&')
    transition.append(temp[0] + '=' + name + '&' + cutter[1] + '=' + temp[2])
    final_href = transition[0]
    # print(final_href)
    new_url = final_href
    new_session = requests.Session()
    new_resp = new_session.get(new_url)
    if new_resp.status_code != 200:
        print('url發生錯誤')
        return
    new_soup = bs(new_resp.text, 'html.parser')
    game_histories = new_soup.find_all('td', align='center')
    # print(game_histories)
    titles = new_soup.find_all('td', width='50%')
    result = []
    reply = []
    topic = titles[0].text + '\t' + titles[1].text
    reply.append(topic)
    for game_history in game_histories:
        # print(game_history.a)
        if (game_history.a):
            result.append(game_history.a.text)
        else:
            result.append('輪空')
    for i in range(0, len(result), 2):
        if len(result[i]) == 2:
            contents = '   ' + result[i] + '\t\t  ' + result[i+1]
            reply.append(contents)
        elif len(result[i]) == 4:
            contents = result[i] + '      ' + result[i+1]
            reply.append(contents)
        else:
            contents = ' ' + result[i] + '\t\t' + result[i+1]
            reply.append(contents)

    return'\n'.join(reply)


if __name__ == '__main__':
    feedback = '陳品崴\n54勝116敗(出生年月:2004/02)'
    print(final(feedback))
