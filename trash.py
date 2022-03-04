import requests
from bs4 import BeautifulSoup as bs


def competition():
    url = 'http://tpego.hyplaygo.com/TPEGo/Home/Index2'
    resp = requests.get(url)
    if resp.status_code != 200:
        print('url發生錯誤')
        return
    soup = bs(resp.text, 'html5lib')
    titles = soup.find_all(class_='col-md-3 portfolio-item')
    names = ['今日比賽資訊!']
    for i in range(len(titles)):
        if '時間' in titles[i].text:
            a += 1
            print(a)
            # for title in titles[i]:
            #     opens = title.h4.a.text
            #     hrefs = title.a['href']
            #     names.append(opens)
            #     names.append(hrefs)
        else:
            fucks = soup.find_all('h4')
            for fuck in fucks:
                t_topics = fuck.a.text
                t_hrefs = fuck.a['href']
                names.append(t_topics)
                names.append(t_hrefs)
                 
            

    return '\n'.join(names)


competition()
