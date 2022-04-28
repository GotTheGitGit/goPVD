import urllib.request as req
import bs4


def getcompetition():
    url = "http://tpego.hyplaygo.com"
    # 建立一個request 物件，附加request headers的資訊
    request = req.Request(url, headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    })
    with req.urlopen(request) as response:
        data = response.read().decode("utf-8")
    # 解析資料
    # 尋找想要的資料的特色
    root = bs4.BeautifulSoup(data, 'html.parser')
    # print(root)
    img_respond = root.find_all("div", class_="col-md-3 portfolio-item")
    #img_respond = (img_respond.replace('<br>', '')).replace('<br/>', '')

    result = ["圍棋比賽最新資訊!", '\n']
    for i in range(len(img_respond)):
        if (img_respond[i].h3):
            img_respond[i] = img_respond[i].text.replace(" ", "")
            img_respond[i] = img_respond[i].replace("\r", "")
            img_respond[i] = img_respond[i].replace(":\n", ":")
            img_respond[i] = img_respond[i].replace(":\n", ":")
            img_respond[i] = img_respond[i].replace("\n\n\n\n", "")
            # img_respond[i] = img_respond[i].replace("\", "")
            img_respond[i] = img_respond[i].replace("\n\n", "")
            img_respond[i] = img_respond[i].replace("\t", "")
            print(img_respond)
            link_name = []
            temp = list(img_respond[i])
            for j in range(1, len(temp)):
                if temp[j] != '\n':
                    link_name.append(temp[j])
                elif temp[j] == '\n':
                    break
            link_name = ''.join(link_name)
            link = root.find('a', string=link_name)
            # print(link)
            http = url + link['href']
            result.append(img_respond[i] + '\r報名網頁超連結:\n' + http + '\n')
    return ''.join(result)


getcompetition()
