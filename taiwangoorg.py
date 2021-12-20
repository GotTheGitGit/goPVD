import requests
from bs4 import BeautifulSoup as bs


def Taiwangoorg():
    url = 'https://taiwangorg.blogspot.com'
    resp = requests.get(url)
    if resp.status_code != 200:
        return ('url發生錯誤')

    soup = bs(resp.text, 'html.parser')
    topics = soup.find_all('h3', class_='post-title entry-title')
    titles = []
    hrefs = []
    reply_list = ["台灣棋院最新資訊!"]
    for topic in topics:
        title = topic.a.text
        href = topic.a['href']
        titles.append(title)
        hrefs.append(href)

    for i in range(len(titles)):
        news = titles[i] + '\n' + hrefs[i]
        reply_list.append(news)

    reply_list.append("台灣棋院官方Blog\n>>" + url)
    return '\n'.join(reply_list)

# print(Taiwangoorg())
