import requests
from bs4 import BeautifulSoup as bs


def classify(name):
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
    checkers = qSoup.find_all("div", class_="col-md-10")[1].label.text


# classify('黃亭赫')
