import requests
from bs4 import BeautifulSoup as bs
from today_competition import today


def getcompetition():
    result = []
    result.append(today())
    result.append('最新比賽資訊!')
    main = 'http://tpego.hyplaygo.com/'
    url = 'http://tpego.hyplaygo.com/TPEGo/Active/SearchResult?ItemType=6&IsHighLight=N'
    resp = requests.get(url)
    if resp.status_code != 200:
        print('url發生錯誤')
        return
    soup = bs(resp.text, 'html5lib')
    sources = soup.find_all('div', class_='col-md-3 portfolio-item')
    type = soup.find_all('span', class_='btn-primary btn-sm')
    i = 0
    # result = ['最新比賽資訊!']
    for source in sources:
        result.append(source.h4.a.text + '\n' + '日期: ' +
                      source.p.span.text + '\n' + '活動型態:' +
                      type[i].text.replace('  ', '').replace('\n', '') + '\n' + '比賽報名連結>> ' +
                      main + source.h4.a['href'])
        i += 1

    return '\n\n'.join(result)


# print(getcompetition())
# getcompetition()
