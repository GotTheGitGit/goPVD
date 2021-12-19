#提供實時圍棋資訊新聞
import requests
from bs4 import BeautifulSoup as bs
import random

def Everyday_news():
    url = "http://sports.sina.com.cn/chess/weiqi/"
    resp = requests.get(url)
    #print(resp.encoding)
    #print(resp.apparent_encoding)
    resp.encoding = resp.apparent_encoding 
    html = resp.text
    #print(html)

    if resp.status_code != 200:
        return ('url錯誤:' + url)
        
    
    text = bs(html, 'html5lib')
    text.prettify()
    total = text.find("td", class_ = "link03 f14 lh24")
    http = []
    topics = []
    reply_list = ["每日五則圍棋新聞!\n"]
    titles = total.find_all('a')
    for t in titles:
        topics.append(t.text)
        http.append(t['href'])
    
    for i in range(5):
        number = random.randint(0, len(topics))
        news = topics[number] + "\n" + http[number]
        reply_list.append(news)
    reply_list.append("\n查看所有新聞在這裡\n>>" + url)
    return ''.join(reply_list)

#print(Everyday_news())