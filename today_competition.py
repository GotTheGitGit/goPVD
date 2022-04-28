import requests
from bs4 import BeautifulSoup as bs


def today():
    url = 'http://tpego.hyplaygo.com/'
    resp = requests.get(url)
    if resp.status_code != 200:
        print('url發生錯誤')
        return
    try:
        result = ['今日比賽資訊!\n']
        soup = bs(resp.text, 'html5lib')
        sources = soup.find(
            'div', class_='panel-body').find_all('div', class_='col-md-3 portfolio-item')
        for t_source in sources:
            result.append(t_source.h4.a.text + '\n' +
                          'LIVE戰績表查詢>> ' + url + t_source.h4.a['href'])

        return '\n'.join(result)
    except:
        return ''


# print(today())


# def competition():
#     url = 'http://tpego.hyplaygo.com/TPEGo/Home/Index2'
#     resp = requests.get(url)
#     if resp.status_code != 200:
#         print('url發生錯誤')
#         return
#     soup = bs(resp.text, 'html5lib')
#     today_yn = soup.find(class_='col-md-3 portfolio-item').text
#     if '日期' in today_yn:
#         titles = soup.find_all(class_='col-md-3 portfolio-item')
#         independent = []
#         for title in titles:
#             name = title.a.text
#             date = title.p.text
#     else:
#         today()

#     for title in titles:
