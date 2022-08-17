# 你的名字有其他人欸 更酷了
import requests
from bs4 import BeautifulSoup as bs


def overlap(name):
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
    result = []
    qResp = session.post(
        url, headers=request_headers, data=formdata)
    qSoup = bs(qResp.text, 'html.parser')
    # print(qSoup)
    reply_lists = qSoup.find_all(
        "div", class_="col-md-10")[1]
    selections = reply_lists.find_all('a')
    for selection in selections:
        if result == []:
            result.append(name + '\n' + selection.text)
        else:
            result.append('\n' + selection.text)

    return result


if __name__ == '__main__':
    print(overlap('王彥翔'))
# overlap('舒敬雯')
